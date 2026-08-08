#!/usr/bin/env python3
"""g1_ce_composition_assembly.py — reproducible driver for the G1 CE-included
data-assembly / composition count (the 826-vs-846 adjudication).

Runs the EXACT wrapper path (train_g1_manifest.build_dataset / make_split /
write_manifest) with the CE-ResNet catalog present, but WITHOUT the GPU training
step (no timm, no build_model). The composition counts it emits are deterministic
under seed=42 + the pinned gz_desi revision + the committed pre_desi.fits, so this
CPU-only run reproduces the identical gz1 / ce_spiral / ce_not_spiral counts that
the pod --full retrain records in g1_training_manifest.json.

Result (2026-07-19/20, gz_desi rev b7583bb2..., seed 42):
  gz1=6637  ce_spiral=17153  ce_not_spiral=819  synthetic=2000  total=26609
  -> reproduces the two large historical components (6637, 17153) EXACTLY;
     26,616 historical = 6637+17153+826+2000, so the historical 826-vs-846 /
     26616-vs-26626 conflict is isolated ENTIRELY to the CE non-spiral crossmatch;
     the regenerable value is 819 (NEITHER 826 nor 846; 7 below 826).

Usage:
  python3 pipelines/p2_chirality/scripts/g1_ce_composition_assembly.py [smoke|full]
Env:
  HF_TOKEN read from <repo-root>/.env.local automatically if not already set.
  G1_OUT   output dir (default pipelines/p2_chirality/outputs/g1_full_composition).
"""
import os
import sys
import json
import time
from collections import Counter

MODE = sys.argv[1] if len(sys.argv) > 1 else "full"
SMOKE = (MODE == "smoke")
HERE = os.path.dirname(os.path.abspath(__file__))
P2 = os.path.dirname(HERE)                                  # pipelines/p2_chirality
REPO = os.path.dirname(os.path.dirname(P2))                 # repo root
CE_FILE = os.path.join(P2, "external_catalogs", "pre_desi.fits")

os.environ.setdefault("G1_OUT", os.path.join(P2, "outputs", "g1_full_composition"))
if "HF_TOKEN" not in os.environ:
    envp = os.path.join(REPO, ".env.local")
    if os.path.exists(envp):
        for _l in open(envp):
            if _l.startswith("HF_TOKEN="):
                os.environ["HF_TOKEN"] = _l.strip().split("=", 1)[1].strip().strip('"').strip("'")
os.environ.setdefault("HUGGING_FACE_HUB_TOKEN", os.environ.get("HF_TOKEN", ""))

sys.path.insert(0, P2)
import train_g1_manifest as W  # noqa: E402
W.CE_FILE = CE_FILE
os.makedirs(W.OUT_DIR, exist_ok=True)


def log(m):
    print("[%s] %s" % (time.strftime("%H:%M:%S"), m), flush=True)


def main():
    if not os.path.exists(CE_FILE):
        sys.exit("FATAL: CE catalog missing at %s (see external_catalogs/PROVENANCE.md)" % CE_FILE)
    W.seed_all()
    t0 = time.time()
    images, labels, sources, ids, prov = W.build_dataset(SMOKE, log)
    n_total = len(images)
    train_idx, val_idx = W.make_split(n_total)
    mpath = os.path.join(W.OUT_DIR, "g1_%s_manifest.json" % ("smoke" if SMOKE else "training"))
    manifest = W.write_manifest(mpath, images, labels, sources, ids, prov,
                                train_idx, val_idx, SMOKE)
    srcc = Counter(sources)
    print("\n===== CE COMPOSITION (wrapper build_dataset, %s) =====" % MODE)
    print("ce_resnet_present:", prov.get("ce_resnet_present"))
    print("ce_resnet_sha256 :", prov.get("ce_resnet_sha256"))
    print("scan_limit       :", prov.get("scan_limit"))
    print("gz_desi_rev      :", prov.get("gz_desi_resolved_rev"))
    print("source counts    :", dict(srcc))
    print("prov counts      :", prov.get("counts"))
    print("class_counts     :", manifest["class_counts"])
    print("n_total/train/val:", n_total, len(train_idx), len(val_idx))
    print("elapsed min      : %.1f" % ((time.time() - t0) / 60))
    json.dump({"mode": MODE, "source_counts": dict(srcc), "prov_counts": prov.get("counts"),
               "class_counts": manifest["class_counts"], "ce_sha256": prov.get("ce_resnet_sha256"),
               "gz_desi_rev": prov.get("gz_desi_resolved_rev")},
              open(os.path.join(W.OUT_DIR, "ce_composition_%s.json" % MODE), "w"), indent=2)


if __name__ == "__main__":
    main()
