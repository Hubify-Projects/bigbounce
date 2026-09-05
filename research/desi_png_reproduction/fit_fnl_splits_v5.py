#!/usr/bin/env python3
"""Ledger row 4 v5: fit f_NL (p=1.6, b1 free, n_shot=0 fixed) for
WEIGHT_SYS on/off and Galactic-latitude high/low, against the OFFICIAL
window + OFFICIAL EZmock covariance -- reusing fit_fnl_splits.py's
fit_split() unchanged (it is already generic in `prop`/`half`) so these
two re-tested systematics land on the EXACT SAME convention as v4's
EBV/STARDENS/GALDEPTH_Z splits. Also re-emits the full 5-row table in one
file/one convention.
"""
import json
import numpy as np
from fit_fnl_splits import fit_split
from fit_fnl_v2 import get_cosmo_funcs

OUT = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction/outputs"

if __name__ == "__main__":
    alpha_fn, plin_fn, f_zeff, d_zeff = get_cosmo_funcs("camb")

    # load v4's 3 already-fit props to fold into one final table
    with open(f"{OUT}/imaging_splits_fnl_v4.json") as f:
        v4 = json.load(f)

    results = {k: v4[k] for k in ("EBV", "STARDENS", "GALDEPTH_Z")}

    for prop in ["WEIGHTSYS", "GALLAT"]:
        results[prop] = {}
        for half in ("high", "low"):
            r = fit_split(prop, half, alpha_fn, plin_fn, f_zeff)
            results[prop][half] = r
            print(prop, half, r)
        dh, dl = results[prop]["high"]["f_nl"], results[prop]["low"]["f_nl"]
        sh, sl = results[prop]["high"]["sigma_fnl"], results[prop]["low"]["sigma_fnl"]
        delta = dh - dl
        sigma_delta = float(np.sqrt(sh ** 2 + sl ** 2))
        results[prop]["delta_fnl"] = delta
        results[prop]["sigma_delta"] = sigma_delta
        results[prop]["delta_over_sigma"] = delta / sigma_delta if sigma_delta > 0 else None

    with open(f"{OUT}/systematics_table_v5.json", "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
