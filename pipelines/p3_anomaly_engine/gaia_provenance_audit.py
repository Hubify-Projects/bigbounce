#!/usr/bin/env python3
"""Gaia DR3 tier — provenance audit (HONEST BOUND).

The exact 20-feature production preprocessing script for the published Gaia 50K
run was never recovered from any pod backup. This audit goes one step further and
inspects what the *committed Gaia output product* actually contains, so the paper
can state precisely what is and is not reproducible.

Finding
-------
The committed Gaia tier `hf_staging/gaia_dr3_anomalies.parquet` is NOT real Gaia
DR3 data. Every `source_id` is exactly `int(5e18 + i)` for sequential i — the
signature of `generate_synthetic_gaia()` in recovered_pod_scripts/gaia_expanded.py
(line 131: `int(5e18 + i)`), which is the synthetic fallback that script uses when
the Gaia TAP query returns insufficient rows. Confirming markers:
  * all source_id residuals (source_id - 5e18) lie in [0, 500000)  (sequential i)
  * duplicate source_ids appear (real catalogs have unique source_id)
  * G magnitudes run far outside the real Gaia range (down to ~2 mag)

Consequence: the committed Gaia anomaly table is a synthetic PLACEHOLDER, not a
detection product. Neither its preprocessing NOR its underlying source list can be
reproduced against real Gaia DR3. This is a stronger, more honest bound than
"preprocessing script lost": the tier is not reproducible because its committed
outputs are synthetic. The Gaia tier must therefore be flagged as a
synthetic-placeholder / non-reproducible tier and excluded from any science count
(it already fails the injection-recovery gate and is exploratory-only; this audit
documents WHY it can never be promoted).

To genuinely recover a real Gaia tier one must re-run gaia_expanded.py against a
live Gaia TAP endpoint (query in that script) — a from-scratch re-derivation, not
a reproduction of the committed artifact.

Output
------
    outputs/gaia_provenance_audit.json

Run
---
    python3 pipelines/p3_anomaly_engine/gaia_provenance_audit.py
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

P3 = Path(__file__).resolve().parent
GAIA = P3 / "hf_staging/gaia_dr3_anomalies.parquet"
OUT = P3 / "outputs/gaia_provenance_audit.json"

SYNTH_BASE = 5 * 10**18   # generate_synthetic_gaia: source_id = int(5e18 + i)
SYNTH_N = 500000          # i in [0, 500000)


def main() -> None:
    df = pd.read_parquet(GAIA)
    sid = df["source_id"].to_numpy()
    resid = sid.astype(object) - SYNTH_BASE
    resid = np.array([int(r) for r in resid], dtype=np.int64)

    all_in_range = bool(((resid >= 0) & (resid < SYNTH_N)).all())
    n_unique = int(df["source_id"].nunique())
    has_dupes = n_unique < len(df)
    g = df["mean_obs_magnitude_g_fov"].to_numpy(np.float64)
    g_out_of_real_range = bool((g.min() < 8.0) or (g.max() > 22.0))

    is_synthetic = all_in_range and has_dupes and g_out_of_real_range

    out = {
        "job": "gaia-provenance-audit",
        "committed_artifact": str(GAIA.relative_to(P3.parents[1])),
        "n_rows": int(len(df)),
        "n_unique_source_id": n_unique,
        "duplicate_source_ids_present": has_dupes,
        "source_id_signature": {
            "all_residuals_in_synthetic_range_[0,500000)": all_in_range,
            "expected_pattern": "int(5e18 + i) from generate_synthetic_gaia()",
            "residual_min": int(resid.min()),
            "residual_max": int(resid.max()),
        },
        "g_magnitude": {
            "min": float(g.min()),
            "median": float(np.median(g)),
            "max": float(g.max()),
            "outside_real_gaia_range_8_to_22": g_out_of_real_range,
        },
        "verdict": ("SYNTHETIC-PLACEHOLDER" if is_synthetic else "APPEARS-REAL"),
        "reproducible": False,
        "honest_bound": (
            "The committed Gaia tier is the synthetic fallback of gaia_expanded.py, "
            "not real Gaia DR3. It cannot be reproduced against real data (neither the "
            "lost 20-feature production script nor a real source list survives), and it "
            "is not a genuine detection product. The Gaia tier is flagged synthetic / "
            "non-reproducible and contributes zero science-count objects; a real Gaia "
            "tier would require a from-scratch re-run of the TAP query in gaia_expanded.py."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1))
    print(f"wrote {OUT}")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
