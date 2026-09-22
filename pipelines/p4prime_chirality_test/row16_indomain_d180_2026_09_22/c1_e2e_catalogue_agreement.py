#!/usr/bin/env python3
"""Control C1 (PREREGISTRATION_2026-09-22.md sec.5) — catalogue-scale in-domain
agreement, from artifacts already committed in this repo. No download, no GPU.

The 2026-07-11 full-catalogue e2e re-run
(../../p2_chirality/outputs/canonical_provenance/e2e_fullrun/) pushed all 192
Smith42/galaxies train shards through the SAME checkpoint with the SAME released
preprocessing on an A100 and stored the production equivariant triple per
galaxy. Comparing its argmax class against the released catalogue's `class_eq`
therefore measures, at catalogue scale, what the row-13/16 viewer-cutout control
P2c measured at 43.9%: does the released checkpoint reproduce the released
catalogue on the images the catalogue was actually built from?

`NS` (e2e naming) and `NOT_SPIRAL` (release naming) are the same class; the
comparison is on the class index, not the string.

Output: c1_e2e_catalogue_agreement.json
"""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
SHARDS = HERE.parents[1] / "p2_chirality" / "outputs" / "canonical_provenance" / "e2e_fullrun" / "e2e_shards"
CATALOG = HERE.parents[1] / "p2_chirality" / "apjs_release_v1.0.244" / "p4_catalog_primary_safe_v1.0.244.parquet"
OUT = HERE / "c1_e2e_catalogue_agreement.json"
CLS = ["CW", "CCW", "NS"]


def main():
    t0 = time.time()
    rel = pq.read_table(CATALOG, columns=["object_id", "class_eq", "score_cw_eq",
                                          "score_ccw_eq", "score_ns_eq", "primary_hc",
                                          "raw_flip_qc_unsafe"]).to_pandas()
    rel_cls = np.argmax(rel[["score_cw_eq", "score_ccw_eq", "score_ns_eq"]].values, 1)
    assert (np.array(["CW", "CCW", "NOT_SPIRAL"])[rel_cls] == rel["class_eq"].values).all(), \
        "released class_eq is not the argmax of its own released scores"
    rel = rel.assign(cls=rel_cls).set_index("object_id")
    print(f"[{time.time()-t0:.0f}s] released catalogue {len(rel):,} rows", flush=True)

    files = sorted(SHARDS.glob("e2e_*.parquet"))
    n_tot = n_agree = n_unmatched = 0
    n_hc = n_hc_agree = 0
    n_sp = n_sp_agree = 0
    dmax = 0.0
    dsum = 0.0
    per_shard = {}
    for f in files:
        e = pd.read_parquet(f, columns=["dr8_id", "p_cw_eq", "p_ccw_eq", "p_ns_eq"])
        ec = np.argmax(e[["p_cw_eq", "p_ccw_eq", "p_ns_eq"]].values, 1)
        r = rel.reindex(e["dr8_id"].values)
        ok = r["cls"].notna().values
        n_unmatched += int((~ok).sum())
        agree = (ec[ok] == r["cls"].values[ok].astype(int))
        n_tot += int(ok.sum())
        n_agree += int(agree.sum())
        hc = r["primary_hc"].values[ok].astype(bool)
        n_hc += int(hc.sum()); n_hc_agree += int(agree[hc].sum())
        sp = r["cls"].values[ok].astype(int) != 2
        n_sp += int(sp.sum()); n_sp_agree += int(agree[sp].sum())
        d = np.abs(e["p_cw_eq"].values[ok] - r["score_cw_eq"].values[ok])
        dmax = max(dmax, float(d.max())); dsum += float(d.sum())
        per_shard[f.stem] = {"n": int(ok.sum()), "agreement": float(agree.mean())}
        if len(per_shard) % 32 == 0:
            print(f"[{time.time()-t0:.0f}s] {len(per_shard)}/192 shards, "
                  f"running agreement {n_agree/n_tot:.6f}", flush=True)

    res = {
        "control": "C1 (PREREGISTRATION_2026-09-22.md sec.5) - catalogue-scale in-domain agreement",
        "source_of_labels_under_test": str(SHARDS.relative_to(HERE.parents[2])),
        "source_of_reference_labels": str(CATALOG.relative_to(HERE.parents[2])),
        "images": "Smith42/galaxies v1.0 train shards (the catalogue's own imaging source)",
        "model": "bamfai/galaxy-chirality-v2 @237d021c, preprocessing Resize((224,224))->ToTensor->Normalize",
        "n_shards": len(files),
        "n_compared": n_tot,
        "n_unmatched_dr8_id": n_unmatched,
        "class_agreement_all": n_agree / n_tot,
        "class_agreement_catalogue_spirals": n_sp_agree / n_sp,
        "class_agreement_primary_hc": n_hc_agree / n_hc,
        "n_catalogue_spirals": n_sp,
        "n_primary_hc": n_hc,
        "max_abs_eq_cw_difference": dmax,
        "mean_abs_eq_cw_difference": dsum / n_tot,
        "comparison_out_of_domain_viewer_cutouts": 0.439,
        "out_of_domain_reference": "../row16_tta_2026_09_21/p_d180_catalogue_wide.json positive_controls",
        "per_shard_agreement": per_shard,
        "wall_clock_s": time.time() - t0,
    }
    OUT.write_text(json.dumps(res, indent=2))
    for k, v in res.items():
        if k != "per_shard_agreement":
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
