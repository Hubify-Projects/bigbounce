#!/usr/bin/env python3
"""
STAGE A — full-catalog mirror-pair sweep through the ACTUAL ViT classifier.

OPEN-COMPUTE directive-L, P4 #1 recurring MAJOR closure at FULL SCALE.

This is the scaled-up, RunPod, shard-checkpointed version of the local pilot
`e2e_mirror_flip_transfer_function.py`. It reuses:
  * the EXACT model/preprocessing from run_v2_inference.py / run_eq_dataloader.py
    (ViT-Small/16 + 3-class head, Resize(224,224)->ToTensor->Normalize(ImageNet))
  * the PROVEN DataLoader + per-shard pattern from run_eq_dataloader.py that hit
    1000+ gal/s on a datacenter GPU (Smith42/galaxies, 192 shards, mirror in
    __getitem__)
  * the EXACT transfer-function statistics (RAW T, EQ T_eq + antisymmetry check,
    confidence strata, g_img = 2*a_img - 1) from the pilot.

Per-galaxy record written per shard (resumable): dr8_id, p_raw[CW,CCW,NS],
p_raw_mirror[CW,CCW,NS], p_eq[CW,CCW,NS], class_raw, class_raw_mirror, class_eq,
flip_detected, conf_raw. Coordinates (ra/dec) merged from the production coords
catalog if present for per-sky-region strata; otherwise strata are
confidence/leg/depth only (labels permitting).

Checkpointing: one parquet per shard in $OUT/e2e_shards/, plus a running
summary JSON rebuilt from ALL done shards every shard. rsync back to local is
driven by the launcher, not this script (this script only writes to disk).

Model: bamfai/galaxy-chirality-v2 (val_acc 0.937).  NEVER FABRICATE — whatever
the numbers are, they are written verbatim.
"""
from __future__ import annotations
import os, sys, time, json, gc, shutil, argparse
import numpy as np

os.environ.setdefault('HF_HOME', '/workspace/hf_e2e_cache')

import torch
import torch.nn as nn
import timm
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from huggingface_hub import hf_hub_download
import pandas as pd
from PIL import Image
import io

CLASS_NAMES = ['CW', 'CCW', 'NS']
REPO = "Smith42/galaxies"
N_SHARDS = 192

CONF_BINS = [(0.0, 0.7), (0.7, 0.9), (0.9, 0.99), (0.99, 1.0001)]


def build_model(work, device):
    class Head(nn.Module):
        def __init__(self):
            super().__init__()
            self.h = nn.Sequential(
                nn.LayerNorm(384), nn.Linear(384, 512), nn.GELU(), nn.Dropout(0.3),
                nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3))

        def forward(self, x):
            return self.h(x)

    # weights: prefer local pod copy; else pull from HF
    local_ckpt = os.path.join(work, "chirality_model_v2_best.pt")
    if os.path.exists(local_ckpt):
        ckpt_path = local_ckpt
    else:
        ckpt_path = hf_hub_download(
            "bamfai/galaxy-chirality-v2", "chirality_model_v2_best.pt",
            repo_type="model", token=os.environ.get('HF_TOKEN'))
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=True)
    encoder = timm.create_model('vit_small_patch16_224', pretrained=False, num_classes=0)
    head = Head()
    encoder.load_state_dict(ckpt['enc'])
    head.load_state_dict(ckpt['head'])

    class M(nn.Module):
        def __init__(self, e, h):
            super().__init__()
            self.e = e
            self.h = h

        def forward(self, x):
            return self.h(self.e(x))

    model = M(encoder, head).to(device).eval()
    torch.set_float32_matmul_precision('high')
    return model, float(ckpt.get('val_acc', float('nan'))), ckpt_path


TFM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])


class ShardDataset(Dataset):
    def __init__(self, df):
        self.df = df

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        did = str(row.get('dr8_id', row.get('id_str', '')))
        img_data = row['image']
        try:
            if isinstance(img_data, dict) and 'bytes' in img_data:
                img = Image.open(io.BytesIO(img_data['bytes']))
            elif isinstance(img_data, bytes):
                img = Image.open(io.BytesIO(img_data))
            else:
                return '', torch.zeros(3, 224, 224), torch.zeros(3, 224, 224)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            orig = TFM(img)
            flip = TFM(img.transpose(Image.FLIP_LEFT_RIGHT))
            return did, orig, flip
        except Exception:
            return '', torch.zeros(3, 224, 224), torch.zeros(3, 224, 224)


def collate_fn(batch):
    ids, origs, flips = zip(*batch)
    valid = [i for i, d in enumerate(ids) if d != '']
    if not valid:
        return [], torch.zeros(0, 3, 224, 224), torch.zeros(0, 3, 224, 224)
    return ([ids[i] for i in valid],
            torch.stack([origs[i] for i in valid]),
            torch.stack([flips[i] for i in valid]))


def conf_bin_idx(c):
    for j, (lo, hi) in enumerate(CONF_BINS):
        if lo <= c < hi:
            return j
    return len(CONF_BINS) - 1


def summarize(shard_dir, val_acc, ckpt_path, device_str, coords_path):
    """Rebuild the full transfer-function summary from ALL done shard parquets."""
    files = sorted(f for f in os.listdir(shard_dir)
                   if f.startswith('e2e_') and f.endswith('.parquet'))
    if not files:
        return None
    dfs = [pd.read_parquet(os.path.join(shard_dir, f)) for f in files]
    df = pd.concat(dfs, ignore_index=True)
    n_total = len(df)

    # RAW spiral pool (orig argmax CW/CCW)
    sp = df[df['class_raw'].isin(['CW', 'CCW'])]
    n_pairs = len(sp)
    flip = ((sp['class_raw'] == 'CW') & (sp['class_raw_mirror'] == 'CCW')) | \
           ((sp['class_raw'] == 'CCW') & (sp['class_raw_mirror'] == 'CW'))
    n_flip = int(flip.sum())
    T = n_flip / n_pairs if n_pairs else float('nan')
    se_T = float(np.sqrt(T * (1 - T) / n_pairs)) if n_pairs else float('nan')

    # confusion orig->mirror (spiral pool rows) for a_img / g_img
    ss = sp[sp['class_raw_mirror'].isin(['CW', 'CCW'])]
    spiral_spiral = len(ss)
    correct_flip_ss = int((((ss['class_raw'] == 'CW') & (ss['class_raw_mirror'] == 'CCW')) |
                           ((ss['class_raw'] == 'CCW') & (ss['class_raw_mirror'] == 'CW'))).sum())
    a_img = correct_flip_ss / spiral_spiral if spiral_spiral else float('nan')
    g_img = 2 * a_img - 1 if spiral_spiral else float('nan')

    # confidence strata on raw orig confidence
    strata = []
    for j, (lo, hi) in enumerate(CONF_BINS):
        sub = sp[(sp['conf_raw'] >= lo) & (sp['conf_raw'] < hi)]
        nb = len(sub)
        fb = int((((sub['class_raw'] == 'CW') & (sub['class_raw_mirror'] == 'CCW')) |
                  ((sub['class_raw'] == 'CCW') & (sub['class_raw_mirror'] == 'CW'))).sum())
        tb = fb / nb if nb else float('nan')
        seb = float(np.sqrt(tb * (1 - tb) / nb)) if nb else float('nan')
        strata.append({'orig_conf_range': [lo, min(hi, 1.0)], 'n': nb,
                       'n_flip_recovered': fb, 'T': tb, 'T_stderr': seb})

    # EQ mode: argmax of p_eq, flip detection + antisymmetry
    eq_sp = df[df['class_eq'].isin(['CW', 'CCW'])]
    n_eq = len(eq_sp)
    eq_flip = int((((eq_sp['class_eq'] == 'CW') & (eq_sp['class_eq_mirror'] == 'CCW')) |
                   ((eq_sp['class_eq'] == 'CCW') & (eq_sp['class_eq_mirror'] == 'CW'))).sum())
    T_eq = eq_flip / n_eq if n_eq else None
    antisym_maxdev = float(df['eq_antisym_dev'].max()) if 'eq_antisym_dev' in df else None

    # sky-region strata (if ra/dec present via coords merge) — hemisphere split
    sky = None
    if coords_path and os.path.exists(coords_path):
        try:
            coords = pd.read_parquet(coords_path, columns=['dr8_id', 'ra', 'dec'])
            m = sp.merge(coords, on='dr8_id', how='left')
            have = m[m['dec'].notna()]
            if len(have):
                sky = {}
                for name, mask in [('north_dec_ge_0', have['dec'] >= 0),
                                   ('south_dec_lt_0', have['dec'] < 0)]:
                    s = have[mask]
                    nb = len(s)
                    fb = int((((s['class_raw'] == 'CW') & (s['class_raw_mirror'] == 'CCW')) |
                              ((s['class_raw'] == 'CCW') & (s['class_raw_mirror'] == 'CW'))).sum())
                    sky[name] = {'n': nb, 'n_flip': fb,
                                 'T': (fb / nb) if nb else None}
        except Exception as e:
            sky = {'error': str(e)}

    files_done = len(files)
    return {
        'purpose': 'FULL-SCALE end-to-end image-level chirality transfer function via mirror-flip through the ACTUAL ViT classifier',
        'stage': 'A',
        'shards_done': files_done,
        'shards_total': N_SHARDS,
        'status': 'final' if files_done >= N_SHARDS else 'in-progress-checkpoint',
        'model': 'bamfai/galaxy-chirality-v2 (ViT-Small/16 + 3-class head)',
        'model_ckpt': str(ckpt_path),
        'model_val_acc': val_acc,
        'image_source': 'Smith42/galaxies (192 shards) — same production source as run_eq_dataloader.py',
        'preprocessing': 'Resize(224,224)->ToTensor->Normalize(ImageNet) [matches run_v2_inference.py]',
        'device': device_str,
        'n_total_galaxies': n_total,
        'n_pairs_cw_ccw_original_raw': n_pairs,
        'n_flip_recovered_CWtoCCW_or_CCWtoCW_raw': n_flip,
        'transfer_function_T_raw': T,
        'transfer_function_T_raw_stderr': se_T,
        'transfer_function_T_raw_by_orig_conf_bin': strata,
        'image_level_a_img_spiral_spiral_pool': a_img,
        'image_level_g_img_2a_img_minus_1': g_img,
        'spiral_spiral_pool_n': spiral_spiral,
        'eq_mode_production_z2_tta': {
            'n_pairs_eq_cw_ccw_original': n_eq,
            'n_eq_flip_recovered': eq_flip,
            'T_eq': T_eq,
            'antisymmetry_max_abs_deviation': antisym_maxdev,
            'note': ('Production catalog uses Z2 mirror-equivariant TTA (class_eq/p_eq). '
                     'T_eq=1 up to argmax ties BY CONSTRUCTION — verified numerically. '
                     'RAW g_img is the informative image-level parity-odd measure; '
                     'GZ1-derived g=0.398 is the ground-truth accuracy calibration.'),
        },
        'sky_region_strata_raw': sky,
        'paper_assumed_hard_label_g': 0.398,
        'paper_assumed_a': 0.6991,
        'timestamp_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--work', default='/workspace/e2e')
    ap.add_argument('--bs', type=int, default=512)
    ap.add_argument('--workers', type=int, default=16)
    ap.add_argument('--max-shards', type=int, default=N_SHARDS)
    ap.add_argument('--shards-per-proc', type=int, default=10,
                    help='exit cleanly after this many shards (fresh heap; a '
                         'supervisor loop restarts the resumable process). '
                         'Guards the 125GB container cgroup limit against '
                         'DataLoader fork-CoW heap growth (cgroup OOM-killed '
                         'the parent at shard 14 on 2026-07-12).')
    ap.add_argument('--summary-every', type=int, default=10,
                    help='rebuild the all-shard summary JSON every N shards '
                         '(the rebuild reads every done shard parquet; per-shard '
                         'rebuilds amplified memory late in the run)')
    ap.add_argument('--prefetch', type=int, default=2,
                    help='DataLoader prefetch_factor (4 kept ~19GB of decoded '
                         'pinned tensors in flight with 16 workers x bs 512)')
    ap.add_argument('--abort-below-gps', type=float, default=300.0,
                    help='abort if measured gal/s below this after shard 0')
    args = ap.parse_args()

    work = args.work
    os.makedirs(work, exist_ok=True)
    shard_dir = os.path.join(work, 'e2e_shards')
    os.makedirs(shard_dir, exist_ok=True)
    summary_path = os.path.join(work, 'e2e_transfer_function_full.json')
    coords_path = os.path.join(work, 'catalog_a_with_coords.parquet')

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    t0 = time.time()
    model, val_acc, ckpt_path = build_model(work, device)
    dev_name = torch.cuda.get_device_name(0) if device.type == 'cuda' else str(device)
    print(f"[{time.time()-t0:.0f}s] model loaded val_acc={val_acc:.4f} device={dev_name}", flush=True)

    done = set()
    for f in os.listdir(shard_dir):
        if f.startswith('e2e_') and f.endswith('.parquet'):
            try:
                done.add(int(f.split('_')[1].split('.')[0]))
            except Exception:
                pass
    print(f"[{time.time()-t0:.0f}s] resuming: {len(done)}/{N_SHARDS} shards already done", flush=True)

    t_global = time.time()
    total_gal = 0
    shards_this_proc = 0
    for shard_idx in range(min(args.max_shards, N_SHARDS)):
        if shard_idx in done:
            continue
        if shards_this_proc >= args.shards_per_proc:
            print(f"PROC_RECYCLE: {shards_this_proc} shards this process, "
                  f"{len(done)}/{N_SHARDS} total — exiting for fresh heap "
                  f"(supervisor restarts)", flush=True)
            sys.exit(0)
        t_shard = time.time()
        shard_file = f"data/train-{shard_idx:05d}-of-{N_SHARDS:05d}.parquet"
        try:
            path = hf_hub_download(repo_id=REPO, filename=shard_file, repo_type='dataset',
                                   token=os.environ.get('HF_TOKEN', ''),
                                   cache_dir=os.path.join(work, 'hf_cache'))
        except Exception as e:
            print(f"  S{shard_idx}: download error {e}", flush=True)
            time.sleep(5)
            continue
        df = pd.read_parquet(path)
        ds = ShardDataset(df)
        loader = DataLoader(ds, batch_size=args.bs, num_workers=args.workers,
                            collate_fn=collate_fn, pin_memory=True,
                            prefetch_factor=args.prefetch, persistent_workers=False)
        rows = []
        for ids, origs, flips in loader:
            if len(ids) == 0:
                continue
            origs = origs.to(device, non_blocking=True)
            flips = flips.to(device, non_blocking=True)
            with torch.no_grad():
                po = torch.softmax(model(origs), dim=1).cpu().numpy()
                pm = torch.softmax(model(flips), dim=1).cpu().numpy()
            for did, o, m in zip(ids, po, pm):
                # EQ (production Z2 TTA): p_eq(orig)=[o + swap(m)]/2 ; p_eq(mirror)=[m + swap(o)]/2
                swap_m = m[[1, 0, 2]]
                swap_o = o[[1, 0, 2]]
                pe_o = (o + swap_m) / 2.0
                pe_m = (m + swap_o) / 2.0
                dev = float(np.max(np.abs(pe_m - pe_o[[1, 0, 2]])))
                oc = int(o.argmax())
                mc = int(m.argmax())
                eoc = int(pe_o.argmax())
                emc = int(pe_m.argmax())
                rows.append({
                    'dr8_id': did,
                    'p_cw_raw': float(o[0]), 'p_ccw_raw': float(o[1]), 'p_ns_raw': float(o[2]),
                    'p_cw_raw_mirror': float(m[0]), 'p_ccw_raw_mirror': float(m[1]), 'p_ns_raw_mirror': float(m[2]),
                    'p_cw_eq': float(pe_o[0]), 'p_ccw_eq': float(pe_o[1]), 'p_ns_eq': float(pe_o[2]),
                    'class_raw': CLASS_NAMES[oc], 'class_raw_mirror': CLASS_NAMES[mc],
                    'class_eq': CLASS_NAMES[eoc], 'class_eq_mirror': CLASS_NAMES[emc],
                    'conf_raw': float(o.max()),
                    'eq_antisym_dev': dev,
                })
        shard_df = pd.DataFrame(rows)
        # atomic write: tmp then rename
        tmp = os.path.join(shard_dir, f"e2e_{shard_idx:04d}.parquet.tmp")
        shard_df.to_parquet(tmp)
        os.replace(tmp, os.path.join(shard_dir, f"e2e_{shard_idx:04d}.parquet"))
        done.add(shard_idx)
        shards_this_proc += 1
        total_gal += len(rows)
        elapsed = time.time() - t_shard
        gps = len(rows) / max(elapsed, 1e-6)
        remaining = N_SHARDS - len(done)
        eta_h = remaining * elapsed / 3600
        # running RAW T for the log line
        sp = shard_df[shard_df['class_raw'].isin(['CW', 'CCW'])]
        fl = int((((sp['class_raw'] == 'CW') & (sp['class_raw_mirror'] == 'CCW')) |
                  ((sp['class_raw'] == 'CCW') & (sp['class_raw_mirror'] == 'CW'))).sum())
        tsh = fl / len(sp) if len(sp) else float('nan')
        print(f"  S{shard_idx:>3d}: {len(rows):,} in {elapsed:.0f}s ({gps:.0f} gal/s) "
              f"T_raw(shard)={tsh:.3f} | {len(done)}/{N_SHARDS} ETA={eta_h:.1f}h", flush=True)

        # rebuild + write running summary from ALL shards (every N shards —
        # the rebuild reads every done parquet, so per-shard was too heavy)
        if len(done) % args.summary_every == 0 or len(done) >= N_SHARDS:
            summ = summarize(shard_dir, val_acc, ckpt_path, dev_name, coords_path)
            if summ:
                tmpj = summary_path + '.tmp'
                with open(tmpj, 'w') as fh:
                    json.dump(summ, fh, indent=2)
                os.replace(tmpj, summary_path)
                del summ
                gc.collect()

        del df, ds, loader, rows, shard_df
        gc.collect()
        if device.type == 'cuda':
            torch.cuda.empty_cache()
        if shard_idx % 10 == 9:
            shutil.rmtree(os.path.join(work, 'hf_cache'), ignore_errors=True)

        # throughput flag (launcher monitors + decides on abort criteria)
        if gps < args.abort_below_gps:
            print(f"  [WARN] throughput {gps:.0f} gal/s < abort floor {args.abort_below_gps} gal/s", flush=True)

    print(f"\n[{time.time()-t_global:.0f}s] DONE {len(done)}/{N_SHARDS} shards, {total_gal:,} new galaxies", flush=True)
    if len(done) < N_SHARDS:
        # partial pass (max-shards limit) — do NOT print FINAL SUMMARY, the
        # completion watcher keys on that exact string
        print(f"PARTIAL_EXIT: {len(done)}/{N_SHARDS} shards done", flush=True)
        return
    summ = summarize(shard_dir, val_acc, ckpt_path, dev_name, coords_path)
    if summ:
        with open(summary_path, 'w') as fh:
            json.dump(summ, fh, indent=2)
        print("FINAL SUMMARY:", flush=True)
        print(f"  n_total={summ['n_total_galaxies']:,} n_pairs_raw={summ['n_pairs_cw_ccw_original_raw']:,}", flush=True)
        print(f"  T_raw={summ['transfer_function_T_raw']:.4f} +/- {summ['transfer_function_T_raw_stderr']:.4f}", flush=True)
        print(f"  g_img={summ['image_level_g_img_2a_img_minus_1']:.4f} (paper 0.398)", flush=True)
        eq = summ['eq_mode_production_z2_tta']
        print(f"  T_eq={eq['T_eq']} antisym_maxdev={eq['antisymmetry_max_abs_deviation']}", flush=True)


if __name__ == '__main__':
    main()
