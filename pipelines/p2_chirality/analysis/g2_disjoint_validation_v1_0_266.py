#!/usr/bin/env python3
"""
g2_disjoint_validation_v1_0_266.py — Gate G2: training-DISJOINT held-out GZ1
validation of the G1 manifest-retained ViT-Small checkpoint.

Answers reviewer gate M3 ("GZ1 validation overlap-contaminated; no independent
held-out set"). Evaluates the G1 checkpoint (best_val_acc 0.9931, revision
g1-retrain-2026-07-17) on GZ1 confident spirals that are provably DISJOINT from
the G1 training pool along BOTH axes:

  (1) gz_desi ROW disjointness — eval galaxies are drawn only from gz_desi rows
      that were NEVER scanned during G1 training. G1 training scanned rows
      [0, TRAIN_SCAN_LIMIT); this eval streams rows [TRAIN_SCAN_LIMIT, ...).
      Every gz_desi row is a distinct physical galaxy, so a distinct id_str.

  (2) GZ1 OBJECT disjointness (belt-and-suspenders) — any eval candidate whose
      matched GZ1 sky position falls within the crossmatch tolerance of ANY
      training object (from g1_training_manifest.json's retained ra/dec) is
      dropped, so the same physical GZ1 object cannot leak in via a duplicate.

HONESTY: the G1 checkpoint under test is the GZ1-core + synthetic realization
(`ce_resnet_present = false` in its manifest — the Jia 2023 CE-ResNet catalog
still needs external re-provisioning). This G2 evaluation therefore measures the
checkpoint's CW/CCW discrimination on training-disjoint GZ1 spirals only; it does
NOT exercise the CE non-spiral component. Metrics are reported verbatim.

Labels: GZ1 confident CW (P_CW>0.7) -> 0, GZ1 confident ACW (P_ACW>0.7) -> 1.
Model is 3-class (0=CW, 1=CCW/ACW, 2=NOT_SPIRAL); NS predictions on a true
spiral are counted as errors and their rate is reported explicitly.

Run (pod, GPU):
  G2_CKPT=/workspace/g1/out/g1_ckpt_best.pt \
  G2_MANIFEST=/workspace/g1/out/g1_training_manifest.json \
  G2_OUT=/workspace/g1/out/g2_disjoint_validation_v1_0_266.json \
  python3 g2_disjoint_validation_v1_0_266.py
"""
import hashlib
import json
import os
import sys
import time

import numpy as np

GZ1_URL = "https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.gz"
GZ_DESI_DATASET = "mwalmsley/gz_desi"
SEED = 42
MATCH_TOL = 2 * np.sin(3.0 / 206265.0 / 2)      # 3 arcsec great-circle chord
TRAIN_SCAN_LIMIT = 150_000                        # G1 training scan window end
EVAL_SCAN_WINDOW = int(os.environ.get("G2_SCAN_WINDOW", 200_000))  # rows past the limit
EVAL_TARGET = int(os.environ.get("G2_TARGET", 3000))               # cap eval objects
GZ1_P_THRESHOLD = 0.7
CKPT = os.environ.get("G2_CKPT", "/workspace/g1/out/g1_ckpt_best.pt")
MANIFEST = os.environ.get("G2_MANIFEST", "/workspace/g1/out/g1_training_manifest.json")
OUT = os.environ.get("G2_OUT", "/workspace/g1/out/g2_disjoint_validation_v1_0_266.json")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log(m):
    print("[%s] %s" % (time.strftime("%H:%M:%S"), m), flush=True)


def radec_to_xyz(ra_deg, dec_deg):
    ra = np.radians(np.asarray(ra_deg, dtype=np.float64))
    dec = np.radians(np.asarray(dec_deg, dtype=np.float64))
    return np.column_stack([np.cos(dec) * np.cos(ra),
                            np.cos(dec) * np.sin(ra),
                            np.sin(dec)])


def build_model():
    import torch.nn as nn
    import timm
    enc = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)

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


def cohen_kappa(true, pred, labels):
    """Cohen's kappa over an explicit label set (numpy-only)."""
    true = np.asarray(true); pred = np.asarray(pred)
    idx = {l: k for k, l in enumerate(labels)}
    n = len(labels)
    cm = np.zeros((n, n), dtype=np.float64)
    for t, p in zip(true, pred):
        cm[idx[t], idx[p]] += 1
    tot = cm.sum()
    if tot == 0:
        return float("nan"), cm.astype(int).tolist()
    po = np.trace(cm) / tot
    row = cm.sum(axis=1) / tot
    col = cm.sum(axis=0) / tot
    pe = float(np.sum(row * col))
    kappa = (po - pe) / (1 - pe) if (1 - pe) != 0 else float("nan")
    return float(kappa), cm.astype(int).tolist()


def per_class_metrics(true, pred, cls):
    true = np.asarray(true); pred = np.asarray(pred)
    tp = int(np.sum((pred == cls) & (true == cls)))
    fp = int(np.sum((pred == cls) & (true != cls)))
    fn = int(np.sum((pred != cls) & (true == cls)))
    support = int(np.sum(true == cls))
    prec = tp / (tp + fp) if (tp + fp) else float("nan")
    rec = tp / (tp + fn) if (tp + fn) else float("nan")
    f1 = (2 * prec * rec / (prec + rec)) if (prec and rec and not np.isnan(prec)
                                             and not np.isnan(rec) and (prec + rec)) else float("nan")
    return {"support": support, "precision": prec, "recall": rec, "f1": f1,
            "tp": tp, "fp": fp, "fn": fn}


def main():
    import pandas as pd
    import urllib.request
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    from scipy.spatial import cKDTree
    from datasets import load_dataset
    import torch
    from torchvision import transforms

    t_start = time.time()
    prov = {"gate": "G2", "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "checkpoint_under_test": CKPT, "manifest": MANIFEST,
            "gz1_url": GZ1_URL, "gz_desi_dataset": GZ_DESI_DATASET,
            "match_tol_chord": float(MATCH_TOL), "gz1_p_threshold": GZ1_P_THRESHOLD,
            "train_scan_limit": TRAIN_SCAN_LIMIT, "eval_scan_window": EVAL_SCAN_WINDOW,
            "eval_target": EVAL_TARGET, "seed": SEED}

    # --- checkpoint + manifest provenance ---
    prov["checkpoint_sha256"] = sha256_file(CKPT)
    prov["manifest_sha256"] = sha256_file(MANIFEST)
    man = json.load(open(MANIFEST))
    prov["manifest_ce_resnet_present"] = man["provenance"].get("ce_resnet_present")
    prov["manifest_git_sha"] = man.get("git_sha")
    prov["manifest_gz_desi_rev"] = man["provenance"].get("gz_desi_resolved_rev")
    prov["manifest_gz1_sha256"] = man["provenance"].get("gz1_sha256")

    # training objects: id_strs + ra/dec of the gz1-source rows retained in the manifest
    train_objs = [o for o in man["objects"] if o.get("source") == "gz1"]
    train_ids = set(o.get("id_str") for o in train_objs if o.get("id_str") is not None)
    train_ra = np.array([o["ra"] for o in train_objs if o.get("ra") is not None], dtype=np.float64)
    train_dec = np.array([o["dec"] for o in train_objs if o.get("dec") is not None], dtype=np.float64)
    prov["n_train_gz1_objects"] = len(train_objs)
    prov["n_train_id_strs"] = len(train_ids)
    prov["train_id_strs_sha256"] = hashlib.sha256(
        "\n".join(sorted(train_ids)).encode()).hexdigest()
    train_tree = cKDTree(radec_to_xyz(train_ra, train_dec)) if len(train_ra) else None
    log("manifest: %d gz1 training objects | ce_resnet_present=%s | ckpt sha %s"
        % (len(train_objs), prov["manifest_ce_resnet_present"],
           prov["checkpoint_sha256"][:12]))

    # --- GZ1 confident catalog (FULL, both classes; label by threshold) ---
    log("GZ1 S3 fetch + confident catalog...")
    gz1_file = os.path.join(os.path.dirname(OUT), "gz1_table2.csv.gz")
    if not os.path.exists(gz1_file):
        req = urllib.request.Request(GZ1_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=180) as resp:
            open(gz1_file, "wb").write(resp.read())
    prov["gz1_sha256"] = sha256_file(gz1_file)
    gz1 = pd.read_csv(gz1_file, compression="gzip")
    cw = gz1[gz1["P_CW"] > GZ1_P_THRESHOLD]
    acw = gz1[gz1["P_ACW"] > GZ1_P_THRESHOLD]
    conf = pd.concat([cw[["RA", "DEC"]].assign(label=0),
                      acw[["RA", "DEC"]].assign(label=1)], ignore_index=True)
    coords = SkyCoord(ra=conf["RA"].values, dec=conf["DEC"].values,
                      unit=(u.hourangle, u.deg))
    conf_ra = coords.ra.deg.astype(np.float64)
    conf_dec = coords.dec.deg.astype(np.float64)
    conf_labels = conf["label"].values.astype(np.int64)
    conf_tree = cKDTree(radec_to_xyz(conf_ra, conf_dec))
    prov["gz1_confident_cw"] = int(len(cw))
    prov["gz1_confident_acw"] = int(len(acw))
    log("GZ1 confident: CW=%d ACW=%d (label universe %d)" % (len(cw), len(acw), len(conf)))

    # --- stream gz_desi rows PAST the training window; collect disjoint eval set ---
    log("streaming gz_desi rows [%d, %d) for DISJOINT eval matches..."
        % (TRAIN_SCAN_LIMIT, TRAIN_SCAN_LIMIT + EVAL_SCAN_WINDOW))
    from huggingface_hub import HfApi
    try:
        prov["gz_desi_resolved_rev"] = HfApi().dataset_info(GZ_DESI_DATASET).sha
    except Exception as e:
        prov["gz_desi_resolved_rev"] = "unresolved:%s" % e.__class__.__name__

    ds = load_dataset(GZ_DESI_DATASET, split="train", streaming=True)
    ds = ds.skip(TRAIN_SCAN_LIMIT)

    tfm = transforms.Compose([
        transforms.Resize((224, 224)), transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    images, labels, eval_ids = [], [], []
    n_scanned = n_match = n_excl_idstr = n_excl_obj = 0
    t0 = time.time()
    for row in ds:
        n_scanned += 1
        if n_scanned > EVAL_SCAN_WINDOW or len(images) >= EVAL_TARGET:
            break
        ra, dec, img = row.get("ra"), row.get("dec"), row.get("image")
        if ra is None or dec is None or img is None:
            continue
        try:
            ra_f, dec_f = float(ra), float(dec)
        except (TypeError, ValueError):
            continue
        xyz = radec_to_xyz([ra_f], [dec_f])[0]
        d, i = conf_tree.query(xyz, k=1)
        if d >= MATCH_TOL:
            continue
        # disjointness axis 1: id_str must not be a training id_str
        idstr = row.get("id_str")
        if idstr is not None and idstr in train_ids:
            n_excl_idstr += 1
            continue
        # disjointness axis 2: matched sky position must not coincide with any training obj
        if train_tree is not None:
            dt, _ = train_tree.query(xyz, k=1)
            if dt < MATCH_TOL:
                n_excl_obj += 1
                continue
        images.append(img.copy()); labels.append(int(conf_labels[i]))
        eval_ids.append({"id_str": idstr, "ra": ra_f, "dec": dec_f,
                         "gz1_label": int(conf_labels[i])})
        n_match += 1
        if n_scanned % 25000 == 0:
            log("  %d scanned | eval=%d excl(idstr=%d,obj=%d) | %.0f/s"
                % (n_scanned, len(images), n_excl_idstr, n_excl_obj,
                   n_scanned / (time.time() - t0)))
    prov["n_scanned"] = n_scanned
    prov["n_excluded_idstr_overlap"] = n_excl_idstr
    prov["n_excluded_object_overlap"] = n_excl_obj
    log("eval set assembled: n=%d (scanned %d; excluded idstr=%d obj=%d) in %.1f min"
        % (len(images), n_scanned, n_excl_idstr, n_excl_obj, (time.time() - t0) / 60))

    if len(images) < 100:
        json.dump({"g2_pass": False, "reason": "insufficient disjoint eval objects",
                   "n_eval": len(images), "provenance": prov}, open(OUT, "w"), indent=2)
        log("FATAL: only %d disjoint eval objects" % len(images))
        sys.exit(2)

    labels = np.array(labels, dtype=np.int64)

    # --- load checkpoint + evaluate ---
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    model = build_model().to(dev)
    state = torch.load(CKPT, map_location=dev)
    sd = state["model"] if "model" in state else state
    missing, unexpected = model.load_state_dict(sd, strict=False)
    prov["ckpt_epoch"] = state.get("epoch")
    prov["ckpt_val_acc"] = state.get("val_acc")
    prov["load_missing_keys"] = len(missing)
    prov["load_unexpected_keys"] = len(unexpected)
    if len(missing) > 5 or len(unexpected) > 5:
        log("WARNING: state_dict load missing=%d unexpected=%d" % (len(missing), len(unexpected)))
    model.eval()
    log("checkpoint loaded (epoch=%s val_acc=%s); running inference on %d objects..."
        % (prov["ckpt_epoch"], prov["ckpt_val_acc"], len(images)))

    preds = np.zeros(len(images), dtype=np.int64)
    probs_ns = np.zeros(len(images), dtype=np.float64)
    bs = 64
    with torch.no_grad():
        for s in range(0, len(images), bs):
            batch = images[s:s + bs]
            x = torch.stack([tfm(im.convert("RGB")) for im in batch]).to(dev)
            out = model(x)
            p = torch.softmax(out, dim=1)
            preds[s:s + bs] = out.argmax(1).cpu().numpy()
            probs_ns[s:s + bs] = p[:, 2].cpu().numpy()

    # --- metrics (verbatim) ---
    n = len(labels)
    n_ns_pred = int(np.sum(preds == 2))
    # binary CW/CCW accuracy on spiral truth (pred==2 counts as error)
    correct_binary = int(np.sum((preds == labels) & (labels != 2)))
    acc_all = float(np.mean(preds == labels))          # NS pred always wrong (no true NS)
    # spiral-only subset where model predicted a spiral class
    spiral_mask = preds != 2
    acc_spiralpred = (float(np.mean(preds[spiral_mask] == labels[spiral_mask]))
                      if spiral_mask.any() else float("nan"))
    labels_present = sorted(set(labels.tolist()) | set(preds.tolist()))
    kappa_full, cm_full = cohen_kappa(labels, preds, labels_present)
    # binary kappa on the subset where a spiral class was predicted
    if spiral_mask.any():
        kappa_bin, cm_bin = cohen_kappa(labels[spiral_mask], preds[spiral_mask], [0, 1])
    else:
        kappa_bin, cm_bin = float("nan"), [[0, 0], [0, 0]]

    metrics = {
        "n_eval": n,
        "class_support": {"CW(0)": int(np.sum(labels == 0)),
                          "CCW(1)": int(np.sum(labels == 1))},
        "accuracy_all_3class": acc_all,
        "accuracy_binary_on_spiral_predictions": acc_spiralpred,
        "n_not_spiral_predictions": n_ns_pred,
        "not_spiral_prediction_rate": n_ns_pred / n,
        "mean_ns_softmax_prob": float(np.mean(probs_ns)),
        "correct_binary_count": correct_binary,
        "per_class": {"CW(0)": per_class_metrics(labels, preds, 0),
                      "CCW(1)": per_class_metrics(labels, preds, 1),
                      "NOT_SPIRAL(2)": per_class_metrics(labels, preds, 2)},
        "cohen_kappa_3category": kappa_full,
        "cohen_kappa_labels": labels_present,
        "confusion_matrix_3category": cm_full,
        "confusion_matrix_labels_rows_true_cols_pred": labels_present,
        "cohen_kappa_binary_spiralpred_subset": kappa_bin,
        "confusion_matrix_binary_spiralpred_subset": cm_bin,
    }

    import platform
    prov["packages"] = {
        "python": sys.version.split()[0], "numpy": np.__version__,
        "torch": torch.__version__, "device": dev,
        "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
    }
    for m in ("timm", "datasets", "astropy", "scipy", "pandas", "huggingface_hub"):
        try:
            prov["packages"][m] = __import__(m).__version__
        except Exception:
            prov["packages"][m] = "absent"

    result = {
        "gate": "G2",
        "title": "Training-disjoint held-out GZ1 validation of the G1 "
                 "manifest-retained ViT-Small checkpoint",
        "honesty_note": "The checkpoint under test is the GZ1-core + synthetic "
                        "realization (ce_resnet_present=false). This G2 measures "
                        "CW/CCW discrimination on training-disjoint GZ1 spirals "
                        "only; it does not exercise the CE non-spiral component. "
                        "Metrics reported verbatim.",
        "disjointness": {
            "axis1_gz_desi_row": "eval galaxies drawn only from gz_desi rows "
                                 "[%d, %d) — never scanned in G1 training [0, %d)"
                                 % (TRAIN_SCAN_LIMIT, TRAIN_SCAN_LIMIT + n_scanned,
                                    TRAIN_SCAN_LIMIT),
            "axis2_gz1_object": "any candidate within %.2e chord (3 arcsec) of a "
                                "training manifest object dropped" % MATCH_TOL,
            "n_excluded_idstr_overlap": n_excl_idstr,
            "n_excluded_object_overlap": n_excl_obj,
        },
        "metrics": metrics,
        "provenance": prov,
        "eval_objects_sample": eval_ids[:50],
        "n_eval_objects_logged": len(eval_ids),
        "runtime_sec": round(time.time() - t_start, 1),
    }
    # attach a hash of the full eval id list for reproducibility
    result["eval_ids_sha256"] = hashlib.sha256(
        json.dumps(eval_ids, sort_keys=True).encode()).hexdigest()
    json.dump(result, open(OUT, "w"), indent=2)
    log("G2 DONE n_eval=%d acc_all=%.4f acc_binary(spiralpred)=%.4f kappa3=%.4f "
        "kappaBin=%.4f NSpred=%d(%.2f%%) -> %s"
        % (n, acc_all, acc_spiralpred, kappa_full, kappa_bin, n_ns_pred,
           100 * n_ns_pred / n, OUT))


if __name__ == "__main__":
    main()
