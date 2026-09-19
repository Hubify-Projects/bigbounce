#!/usr/bin/env python3
"""R10 (A3M v3M.0.26): recompute Table V's f_PBH columns AT THE LABELED grid points.

Why this exists
---------------
The R10 confirmation board (Claude Fable 5.1 INT leg) found that three of Table V's
five rows carried f_PBH values that were not evaluated at the (Delta, r_p k_p, C_th)
the row is labeled with:

  * rows 4 and 5 are labeled C_th = 0.6 and 0.4, but their printed values are the
    `gamma_cr_sensitivity` entries of outputs/pbh_compaction_fnl.json, which
    pbh_compaction_fnl.py computes at C_TH_BASE = 0.5 for every (Delta, r_p k_p);
  * row 1 is labeled (0.35, 0.75, 0.5) but its printed pair
    (5.8e-21, 4.5e-7) is `calibrated_amplitude_comparison["C_th=0.4"]`, i.e. the
    (Delta, r_p k_p, C_th) = (0.5, 1.0, 0.4) baseline.

This script evaluates every row at its own labeled point, with the per-row Gaussian
calibration the caption describes ("evaluated at the Gaussian-calibrated amplitude
A_* with no upper cutoff"), using the committed functions of
research/track_a3_multichannel/pbh_compaction_fnl.py unchanged.

Nothing here changes the ratio column (Eq. 13), which is a required-amplitude ratio
and was independently confirmed correct in all five rows.
"""
import importlib.util, json, pathlib, sys, time

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "pbh_compaction_fnl.py"
spec = importlib.util.spec_from_file_location("pbh_compaction_fnl", SRC)
m = importlib.util.module_from_spec(spec)
sys.modules["pbh_compaction_fnl"] = m
spec.loader.exec_module(m)           # safe: the module guards main() with __name__

FNL = {"gaussian_0": 0.0, "li_-35/16": -35.0 / 16.0, "cai_-35/8": -35.0 / 8.0}

# (Delta, r_p k_p, C_th) exactly as Table V labels them
ROWS = [(0.35, 0.75, 0.5), (0.35, 1.5, 0.5), (0.50, 1.0, 0.5),
        (0.80, 0.75, 0.6), (0.80, 1.5, 0.4)]

out = {"task": "A3M R10: Table V f_PBH columns at the labeled grid points",
       "source_module": str(SRC.relative_to(HERE.parents[2])),
       "criterion": "per-row Gaussian calibration A_* s.t. f_PBH(f_NL=0, A_*)=1, "
                    "no upper cutoff (as Table V's caption states)",
       "rows": []}
t0 = time.time()
for dl, rpk, cth in ROWS:
    m.DL = dl                                    # lognormal width is a module global
    A_star = m.A_for_fpbh(1.0, 0.0, cth, rpk, 1e-4, 20.0)
    _, _, _, gamma_cr = m.covariances(A_star, rpk, 1.0)
    vals = {k: m.f_pbh(v, A_star, cth, rpk) for k, v in FNL.items()}
    out["rows"].append({"Delta": dl, "rp_kp": rpk, "C_th": cth,
                        "gamma_cr": gamma_cr, "A_star": A_star,
                        "f_PBH": vals})
    print(f"Delta={dl} rp_kp={rpk} C_th={cth}: gamma_cr={gamma_cr:.4f} A*={A_star:.4f} "
          f"G={vals['gaussian_0']:.3e} -35/16={vals['li_-35/16']:.3e} "
          f"-35/8={vals['cai_-35/8']:.3e}", flush=True)
out["wall_seconds"] = round(time.time() - t0, 2)
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
print(f"\nwrote {HERE/'results.json'} ({out['wall_seconds']} s)")
