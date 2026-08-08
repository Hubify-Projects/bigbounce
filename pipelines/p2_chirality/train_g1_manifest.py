#!/usr/bin/env python3
"""
train_g1_manifest.py — G1 regenerable ViT-Small chirality retrain WITH a fully
retained object/split/seed manifest.

This is the P4 open-compute Gate G1 deliverable (COMPUTE_CAMPAIGN_2026-07-17.md).
It reproduces the exact data-assembly path of train_chirality_v2.py (GZ1 S3 CW/CCW
labels + mwalmsley/gz_desi streaming crossmatch for images+coords + optional
CE-ResNet not-spiral/spiral labels + synthetic not-spiral) but, BEFORE training,
writes g1_training_manifest.json capturing:
  - every object's identity per split (train_idx / val_idx), with the gz_desi row
    id fields (dr8_id / iauname / ra / dec) for real matches and a synthetic tag
    for generated not-spiral examples;
  - all random seeds (python / numpy / torch) and the split rule;
  - data-revision provenance (gz_desi resolved commit sha, GZ1 file sha256,
    CE-ResNet file sha256 if present, Smith42 parent rev as cited);
  - package versions + git SHA + host GPU.

The manifest makes the realization REGENERABLE (supersedes the unrecoverable
historical 26,616-vs-26,626 record; it does not reproduce it — honestly disclosed).

Modes:
  --smoke   assemble a small batch (~SMOKE_TARGET matched imgs), write the smoke
            manifest, run ONE forward+backward pass on ViT-Small, write
            g1_smoke_result.json. ~15-20 min. Verifies the path end-to-end.
  (default) full manifest + full retrain, checkpoint every epoch.

Usage:
  python3 train_g1_manifest.py --smoke
  python3 train_g1_manifest.py --full --epochs 80
"""
import argparse
import hashlib
import io
import json
import os
import platform
import subprocess
import sys
import time
import urllib.request

import numpy as np

# ------------------------------------------------------------------ config
GZ1_URL = "https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.gz"
GZ_DESI_DATASET = "mwalmsley/gz_desi"
SMITH42_PARENT_REV = "bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2"  # cited parent (tex L788)
CE_FILE = "/workspace/external_catalogs/pre_desi.fits"
OUT_DIR = os.environ.get("G1_OUT", "/workspace/g1/out")
SEED = 42
MATCH_TOL = 2 * np.sin(3.0 / 206265.0 / 2)  # 3 arcsec great-circle chord
# gz_desi row identity fields to retain (whatever exists on the row)
ID_FIELDS = ["dr8_id", "iauname", "id_str", "brickid", "objid", "ra", "dec"]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return os.environ.get("G1_GIT_SHA", "unknown")


def resolve_dataset_rev(repo_id):
    try:
        from huggingface_hub import HfApi
        info = HfApi().dataset_info(repo_id)
        return info.sha
    except Exception as e:
        return f"unresolved:{e.__class__.__name__}"


def pkg_versions():
    import torch
    v = {"python": sys.version.split()[0], "numpy": np.__version__,
         "torch": torch.__version__}
    for m in ("timm", "datasets", "astropy", "scipy", "pandas",
              "huggingface_hub", "PIL"):
        try:
            mod = __import__("PIL" if m == "PIL" else m)
            v[m] = getattr(mod, "__version__", "?")
        except Exception:
            v[m] = "absent"
    return v


def build_dataset(smoke, log):
    """Reproduce train_chirality_v2 assembly; return images, labels, sources, ids."""
    import pandas as pd
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    from scipy.spatial import cKDTree
    from datasets import load_dataset
    from PIL import Image

    prov = {"gz1_url": GZ1_URL, "gz_desi_dataset": GZ_DESI_DATASET,
            "smith42_parent_rev_cited": SMITH42_PARENT_REV}

    # --- 1a: GZ1 CW/CCW labels (S3) ---
    log("1a: GZ1 CW/CCW labels (S3 fetch)...")
    gz1_file = os.path.join(OUT_DIR, "gz1_table2.csv.gz")
    if not os.path.exists(gz1_file):
        req = urllib.request.Request(GZ1_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=180) as resp:
            open(gz1_file, "wb").write(resp.read())
    prov["gz1_sha256"] = sha256_file(gz1_file)
    gz1 = pd.read_csv(gz1_file, compression="gzip")
    cw_gal = gz1[gz1["P_CW"] > 0.7]
    acw_gal = gz1[gz1["P_ACW"] > 0.7]
    n_per = min(len(cw_gal), len(acw_gal))
    log(f"    GZ1 confident CW={len(cw_gal)} ACW={len(acw_gal)} balanced={n_per}")
    cw_s = cw_gal.sample(n=n_per, random_state=SEED)
    acw_s = acw_gal.sample(n=n_per, random_state=SEED)
    gz1_labeled = pd.concat([
        cw_s[["RA", "DEC", "P_CW", "P_ACW"]].assign(label=0),
        acw_s[["RA", "DEC", "P_CW", "P_ACW"]].assign(label=1)], ignore_index=True)
    coords = SkyCoord(ra=gz1_labeled["RA"].values, dec=gz1_labeled["DEC"].values,
                      unit=(u.hourangle, u.deg))
    gz1_ra = coords.ra.deg.astype(np.float64)
    gz1_dec = coords.dec.deg.astype(np.float64)
    gz1_labels = gz1_labeled["label"].values.astype(np.int64)
    gz1_xyz = np.column_stack([
        np.cos(np.radians(gz1_dec)) * np.cos(np.radians(gz1_ra)),
        np.cos(np.radians(gz1_dec)) * np.sin(np.radians(gz1_ra)),
        np.sin(np.radians(gz1_dec))])
    tree_gz1 = cKDTree(gz1_xyz)

    # --- 1b: CE-ResNet (optional; pod copy is ephemeral) ---
    HAS_CE = os.path.exists(CE_FILE)
    prov["ce_resnet_present"] = HAS_CE
    tree_ns = tree_ce = None
    ce_conf_labels = ns_ra_sample = None
    if HAS_CE:
        from astropy.io import fits
        log("1b: CE-ResNet catalog...")
        prov["ce_resnet_sha256"] = sha256_file(CE_FILE)
        ce = fits.open(CE_FILE)[1].data
        ce_pcw, ce_pacw = ce["P_CW"], ce["P_ACW"]
        ns_mask = (ce_pcw + ce_pacw) < 0.02
        ns_ra = ce["RA"][ns_mask].astype(np.float64)
        ns_dec = ce["DEC"][ns_mask].astype(np.float64)
        ns_xyz = np.column_stack([
            np.cos(np.radians(ns_dec)) * np.cos(np.radians(ns_ra)),
            np.cos(np.radians(ns_dec)) * np.sin(np.radians(ns_ra)),
            np.sin(np.radians(ns_dec))])
        ns_idx = np.random.choice(len(ns_xyz), min(50000, len(ns_xyz)), replace=False)
        tree_ns = cKDTree(ns_xyz[ns_idx])
        conf = (ce_pcw > 0.4) | (ce_pacw > 0.4)
        cra, cdec = ce["RA"][conf].astype(np.float64), ce["DEC"][conf].astype(np.float64)
        ce_conf_labels = (ce_pacw[conf] > ce_pcw[conf]).astype(np.int64)
        ce_xyz = np.column_stack([
            np.cos(np.radians(cdec)) * np.cos(np.radians(cra)),
            np.cos(np.radians(cdec)) * np.sin(np.radians(cra)),
            np.sin(np.radians(cdec))])
        tree_ce = cKDTree(ce_xyz)
    else:
        log("1b: CE-ResNet catalog ABSENT (pod ephemeral) — GZ1-core + synthetic only")

    # --- 2: stream gz_desi, crossmatch ---
    log(f"2: streaming {GZ_DESI_DATASET}, crossmatching...")
    prov["gz_desi_resolved_rev"] = resolve_dataset_rev(GZ_DESI_DATASET)
    ds = load_dataset(GZ_DESI_DATASET, split="train", streaming=True)
    scan_limit = 8000 if smoke else 150_000
    target = 500 if smoke else None
    prov["scan_limit"] = scan_limit
    prov["match_tol_chord"] = float(MATCH_TOL)
    prov["gz1_p_threshold"] = 0.7

    images, labels, sources, ids = [], [], [], []
    n_scanned = n_gz1 = n_ce = n_ns = 0
    t0 = time.time()
    for row in ds:
        n_scanned += 1
        if n_scanned > scan_limit:
            break
        if target and len(images) >= target:
            break
        ra, dec, img = row.get("ra"), row.get("dec"), row.get("image")
        if ra is None or dec is None or img is None:
            continue
        try:
            ra_f, dec_f = float(ra), float(dec)
        except (TypeError, ValueError):
            continue
        rr, dr = np.radians(ra_f), np.radians(dec_f)
        xyz = np.array([np.cos(dr) * np.cos(rr), np.cos(dr) * np.sin(rr), np.sin(dr)])
        rid = {k: (float(row[k]) if k in ("ra", "dec") and row.get(k) is not None
                   else row.get(k)) for k in ID_FIELDS if k in row}
        matched = False
        d, i = tree_gz1.query(xyz, k=1)
        if d < MATCH_TOL:
            images.append(img.copy()); labels.append(int(gz1_labels[i]))
            sources.append("gz1"); ids.append({"source": "gz1", **rid})
            n_gz1 += 1; matched = True
        if not matched and HAS_CE and n_ce < (200 if smoke else 20000):
            d, i = tree_ce.query(xyz, k=1)
            if d < MATCH_TOL:
                images.append(img.copy()); labels.append(int(ce_conf_labels[i]))
                sources.append("ce_spiral"); ids.append({"source": "ce_spiral", **rid})
                n_ce += 1; matched = True
        if not matched and HAS_CE and n_ns < (100 if smoke else 10000):
            d, i = tree_ns.query(xyz, k=1)
            if d < MATCH_TOL:
                images.append(img.copy()); labels.append(2)
                sources.append("ce_not_spiral"); ids.append({"source": "ce_not_spiral", **rid})
                n_ns += 1; matched = True
        if n_scanned % 50000 == 0:
            log(f"    {n_scanned:,} scanned | gz1={n_gz1} ce={n_ce} ns={n_ns} "
                f"| {n_scanned/(time.time()-t0):.0f}/s")
    log(f"  scan done {(time.time()-t0)/60:.1f}min: gz1={n_gz1} ce={n_ce} ns={n_ns}")

    # --- synthetic not-spiral (deterministic under global seed) ---
    n_synth = 60 if smoke else 2000
    log(f"  adding {n_synth} synthetic not-spiral...")
    for i in range(n_synth):
        if i < n_synth * 0.25:
            arr = np.random.randint(0, 30, (424, 424, 3), dtype=np.uint8)
        elif i < n_synth * 0.5:
            c = np.random.randint(20, 80, 3, dtype=np.uint8)
            arr = np.full((424, 424, 3), c, dtype=np.uint8)
        elif i < n_synth * 0.75:
            arr = np.clip(np.random.normal(40, 20, (424, 424, 3)), 0, 255).astype(np.uint8)
        else:
            arr = np.zeros((424, 424, 3), dtype=np.uint8)
            for c in range(3):
                arr[:, :, c] = np.linspace(np.random.randint(0, 50),
                    np.random.randint(50, 100), 424).reshape(1, -1).repeat(424, 0).astype(np.uint8)
        images.append(Image.fromarray(arr)); labels.append(2)
        sources.append("synthetic"); ids.append({"source": "synthetic", "synth_idx": i})
    prov["counts"] = {"gz1": n_gz1, "ce_spiral": n_ce, "ce_not_spiral": n_ns,
                      "synthetic": n_synth, "total": len(images)}
    return images, labels, sources, ids, prov


def make_split(n_total):
    idx = np.arange(n_total)
    rng = np.random.RandomState(SEED)
    rng.shuffle(idx)
    n_val = max(n_total // 5, 500 if n_total >= 500 else n_total // 5)
    n_val = min(n_val, n_total // 5) if n_total >= 2500 else max(1, n_total // 5)
    return idx[n_val:].tolist(), idx[:n_val].tolist()  # train_idx, val_idx


def write_manifest(path, images, labels, sources, ids, prov, train_idx, val_idx, smoke):
    import torch
    manifest = {
        "gate": "G1",
        "purpose": "regenerable ViT-Small chirality realization with retained "
                   "object/split/seed manifest (supersedes unrecoverable historical "
                   "26,616-vs-26,626 record; does not reproduce it)",
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "mode": "smoke" if smoke else "full",
        "seeds": {"global": SEED, "python_random": SEED, "numpy": SEED, "torch": SEED,
                  "gz1_sample_random_state": SEED, "split_RandomState": SEED},
        "split_rule": "RandomState(42).shuffle(arange(n)); val=first max(n//5,500)",
        "n_total": len(images),
        "n_train": len(train_idx), "n_val": len(val_idx),
        "class_counts": {str(c): int(np.sum(np.array(labels) == c)) for c in (0, 1, 2)},
        "provenance": prov,
        "package_versions": pkg_versions(),
        "git_sha": git_sha(),
        "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
        "train_idx": train_idx,
        "val_idx": val_idx,
        "objects": [{"i": k, "label": int(labels[k]), "source": sources[k],
                     **ids[k]} for k in range(len(images))],
    }
    with open(path, "w") as f:
        json.dump(manifest, f)
    return manifest


# ------------------------------------------------------------------ model
def build_model():
    import torch.nn as nn
    import timm
    enc = timm.create_model("vit_small_patch16_224", pretrained=True, num_classes=0)
    for p in enc.parameters():
        p.requires_grad = False
    for blk in enc.blocks[-6:]:
        for p in blk.parameters():
            p.requires_grad = True
    for p in enc.norm.parameters():
        p.requires_grad = True

    class Head(nn.Module):
        def __init__(self, d):
            super().__init__()
            self.head = nn.Sequential(
                nn.LayerNorm(d), nn.Linear(d, 512), nn.GELU(), nn.Dropout(0.3),
                nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3))

        def forward(self, x):
            return self.head(x)

    class Model(nn.Module):
        def __init__(self, e, h):
            super().__init__()
            self.enc, self.head = e, h

        def forward(self, x):
            return self.head(self.enc(x))

    return Model(enc, Head(384))


def make_ds_class():
    import torch
    from torch.utils.data import Dataset
    from torchvision import transforms
    from PIL import Image, ImageEnhance, ImageFilter

    class ChiralityDatasetV2(Dataset):
        def __init__(self, images, labels, is_train=True):
            self.images, self.labels, self.is_train = images, labels, is_train
            self.t = transforms.Compose([
                transforms.Resize((224, 224)), transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

        def __len__(self):
            return len(self.images)

        def __getitem__(self, i):
            img, label = self.images[i], self.labels[i]
            if self.is_train:
                img = img.rotate(np.random.uniform(0, 360), resample=Image.BILINEAR)
                if np.random.random() > 0.5:
                    img = img.transpose(Image.FLIP_LEFT_RIGHT)
                    if label == 0:
                        label = 1
                    elif label == 1:
                        label = 0
                if np.random.random() > 0.5:
                    img = ImageEnhance.Brightness(img).enhance(np.random.uniform(0.6, 1.4))
                if np.random.random() > 0.5:
                    img = ImageEnhance.Contrast(img).enhance(np.random.uniform(0.7, 1.3))
                if np.random.random() > 0.7:
                    img = img.filter(ImageFilter.GaussianBlur(np.random.uniform(0.5, 2.0)))
            return self.t(img), label
    return ChiralityDatasetV2


def seed_all():
    import random
    import torch
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    torch.cuda.manual_seed_all(SEED)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--epochs", type=int, default=80)
    args = ap.parse_args()
    smoke = args.smoke or not args.full
    os.makedirs(OUT_DIR, exist_ok=True)
    logf = open(os.path.join(OUT_DIR, "g1_%s.log" % ("smoke" if smoke else "full")), "a")

    def log(m):
        line = "[%s] %s" % (time.strftime("%H:%M:%S"), m)
        print(line, flush=True); logf.write(line + "\n"); logf.flush()

    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader
    seed_all()
    log("=== G1 %s run ===" % ("SMOKE" if smoke else "FULL"))
    log("device=%s gpu=%s" % (
        "cuda" if torch.cuda.is_available() else "cpu",
        torch.cuda.get_device_name(0) if torch.cuda.is_available() else "-"))

    images, labels, sources, ids, prov = build_dataset(smoke, log)
    n_total = len(images)
    if n_total < 50:
        log("FATAL: assembled only %d examples — data path FAILED" % n_total)
        json.dump({"smoke_pass": False, "reason": "insufficient data", "n_total": n_total,
                   "provenance": prov}, open(os.path.join(OUT_DIR, "g1_smoke_result.json"), "w"))
        sys.exit(2)
    train_idx, val_idx = make_split(n_total)
    mpath = os.path.join(OUT_DIR, "g1_%s_manifest.json" % ("smoke" if smoke else "training"))
    manifest = write_manifest(mpath, images, labels, sources, ids, prov,
                              train_idx, val_idx, smoke)
    log("MANIFEST WRITTEN %s | n_total=%d train=%d val=%d classes=%s"
        % (mpath, n_total, len(train_idx), len(val_idx), manifest["class_counts"]))
    log("gz_desi_rev=%s gz1_sha=%s ce_present=%s"
        % (prov.get("gz_desi_resolved_rev"), prov.get("gz1_sha256", "")[:12],
           prov.get("ce_resnet_present")))

    DSClass = make_ds_class()
    model = build_model().to("cuda" if torch.cuda.is_available() else "cpu")
    dev = next(model.parameters()).device
    ntr = sum(p.numel() for p in model.parameters() if p.requires_grad)
    log("model built: %s trainable params, ViT-Small" % f"{ntr:,}")

    if smoke:
        # ONE forward+backward pass on a small batch — verify the full path.
        log("SMOKE: one forward+backward pass...")
        tr_imgs = [images[i] for i in train_idx]
        tr_lbls = [labels[i] for i in train_idx]
        ds = DSClass(tr_imgs, tr_lbls, is_train=True)
        loader = DataLoader(ds, batch_size=min(32, len(ds)), shuffle=True, num_workers=2)
        crit = nn.CrossEntropyLoss()
        opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=3e-4)
        model.train()
        bi, bl = next(iter(loader))
        bi, bl = bi.to(dev), bl.to(dev)
        t0 = time.time()
        out = model(bi)
        loss = crit(out, bl)
        loss.backward()
        opt.step()
        dt = time.time() - t0
        mem = (torch.cuda.max_memory_allocated() / 1e9) if torch.cuda.is_available() else 0
        res = {"smoke_pass": True, "n_total": n_total, "n_train": len(train_idx),
               "n_val": len(val_idx), "batch": int(bi.shape[0]),
               "logits_shape": list(out.shape), "loss": float(loss.item()),
               "fwd_bwd_sec": round(dt, 2), "peak_gpu_gb": round(mem, 2),
               "class_counts": manifest["class_counts"],
               "gz_desi_rev": prov.get("gz_desi_resolved_rev"),
               "gz1_sha256": prov.get("gz1_sha256"),
               "ce_resnet_present": prov.get("ce_resnet_present"),
               "manifest_path": mpath,
               "manifest_objects_logged": len(manifest["objects"])}
        json.dump(res, open(os.path.join(OUT_DIR, "g1_smoke_result.json"), "w"), indent=2)
        log("SMOKE PASS: loss=%.4f logits=%s fwd_bwd=%.2fs peak_gpu=%.2fGB"
            % (loss.item(), out.shape, dt, mem))
        log("smoke result -> %s" % os.path.join(OUT_DIR, "g1_smoke_result.json"))
        return

    # ---- FULL retrain ----
    tr_imgs = [images[i] for i in train_idx]; tr_lbls = [labels[i] for i in train_idx]
    va_imgs = [images[i] for i in val_idx]; va_lbls = [labels[i] for i in val_idx]
    counts = np.bincount(tr_lbls, minlength=3)
    w = 1.0 / (counts + 1); w = w / w.sum() * 3
    sw = torch.FloatTensor([w[l] for l in tr_lbls])
    sampler = torch.utils.data.WeightedRandomSampler(sw, len(tr_lbls))
    train_loader = DataLoader(DSClass(tr_imgs, tr_lbls, True), batch_size=64,
                              sampler=sampler, num_workers=4, pin_memory=True)
    val_loader = DataLoader(DSClass(va_imgs, va_lbls, False), batch_size=64,
                            shuffle=False, num_workers=4, pin_memory=True)
    crit = nn.CrossEntropyLoss(weight=torch.FloatTensor(w).to(dev))
    flip_perm = torch.tensor([1, 0, 2])
    FLW = 0.5
    opt = torch.optim.AdamW([
        {"params": model.head.parameters(), "lr": 3e-4},
        {"params": [p for p in model.enc.parameters() if p.requires_grad], "lr": 2e-5}],
        weight_decay=0.02)
    sched = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(opt, T_0=10, T_mult=2)
    best_acc, best_ep, patience = 0.0, 0, 0
    hist = []
    for ep in range(args.epochs):
        model.train(); tl = tc = tt = 0
        for bi, bl in train_loader:
            bi, bl = bi.to(dev), bl.to(dev)
            opt.zero_grad()
            out = model(bi)
            closs = crit(out, bl)
            bf = torch.flip(bi, dims=[3])
            of = model(bf)
            floss = nn.functional.kl_div(
                nn.functional.log_softmax(of, 1),
                nn.functional.softmax(out[:, flip_perm], 1), reduction="batchmean")
            loss = closs + FLW * floss
            loss.backward(); opt.step()
            tl += loss.item(); tc += (out.argmax(1) == bl).sum().item(); tt += bl.size(0)
        sched.step()
        model.eval(); vc = vt = 0
        with torch.no_grad():
            for bi, bl in val_loader:
                bi, bl = bi.to(dev), bl.to(dev)
                vc += (model(bi).argmax(1) == bl).sum().item(); vt += bl.size(0)
        va = vc / max(vt, 1); ta = tc / max(tt, 1)
        hist.append({"epoch": ep, "train_acc": ta, "val_acc": va, "loss": tl / max(len(train_loader), 1)})
        log("epoch %d/%d train_acc=%.4f val_acc=%.4f loss=%.4f"
            % (ep, args.epochs, ta, va, tl / max(len(train_loader), 1)))
        # checkpoint every epoch
        torch.save({"epoch": ep, "model": model.state_dict(), "val_acc": va,
                    "manifest_path": mpath},
                   os.path.join(OUT_DIR, "g1_ckpt_epoch%03d.pt" % ep))
        torch.save({"epoch": ep, "model": model.state_dict(), "val_acc": va},
                   os.path.join(OUT_DIR, "g1_ckpt_last.pt"))
        if va > best_acc:
            best_acc, best_ep, patience = va, ep, 0
            torch.save({"epoch": ep, "model": model.state_dict(), "val_acc": va,
                        "manifest_path": mpath}, os.path.join(OUT_DIR, "g1_ckpt_best.pt"))
        else:
            patience += 1
            if patience >= 15:
                log("early stop at epoch %d (best %d, val_acc=%.4f)" % (ep, best_ep, best_acc))
                break
        json.dump({"history": hist, "best_val_acc": best_acc, "best_epoch": best_ep,
                   "manifest_path": mpath, "n_total": n_total},
                  open(os.path.join(OUT_DIR, "g1_training_result.json"), "w"), indent=2)
    log("FULL DONE best_val_acc=%.4f @epoch %d" % (best_acc, best_ep))


if __name__ == "__main__":
    main()
