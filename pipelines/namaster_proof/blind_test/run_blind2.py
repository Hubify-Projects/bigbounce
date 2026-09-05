"""Execute the batch-2 sealed runs and publish result+receipt pairs to public2/.

Identical harness to run_blind.py (same reference contract construction, same
namaster_proof.receipts.publish_json content binding); it reads the sealed
assignment from $NP_SEALED_DIR and routes variants through variants2.run_variant
so the new S6 arm is available.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parents[2] / "packages" / "namaster-proof" / "src"))

import variants  # noqa: E402
import variants2  # noqa: E402
from namaster_proof.receipts import publish_json  # noqa: E402

NSIDE, LMAX, REF_SEED = 64, 64, 20260904
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed2"))


def build_reference() -> tuple[dict, np.ndarray, dict]:
    out, trace = variants.run_variant("honest", NSIDE, LMAX, REF_SEED)
    contract = {
        "nside": NSIDE, "lmax": LMAX,
        "code_sha256": trace["code"]["sha256"],
        "mask_sha256": trace["inputs"]["mask_sha256"],
        "ell_grid": trace["intermediates"]["ell_grid"],
        "coupling_shape": trace["intermediates"]["coupling_shape"],
        "coupling_support": trace["intermediates"]["coupling_support"],
        "n_wigner3j": trace["intermediates"]["n_wigner3j"],
        "reference_wall_s": trace["wall_s"],
        "wall_floor_s": round(0.25 * trace["wall_s"], 4),
        "env": trace["env"],
        "reference_bandpowers_sha256": variants.h_array(np.asarray(out)),
    }
    return contract, out, trace


def main() -> int:
    public = ROOT / "public2"
    assignment = json.loads((SEALED / "assignment.json").read_text())
    contract, ref_out, ref_trace = build_reference()
    (public / "contract.json").write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n")
    cache = {"m": None, "out": ref_out, "trace": ref_trace}

    for run_id in sorted(assignment):
        spec = assignment[run_id]
        out, trace = variants2.run_variant(spec["variant"], NSIDE, LMAX,
                                           spec["map_seed"], cache=cache)
        if spec["variant"] == "S4_cache_substitute":
            for field in ("coupling_sha256", "coupling_shape", "coupling_support", "n_wigner3j"):
                trace["intermediates"][field] = ref_trace["intermediates"][field]
            trace["wall_s"] = ref_trace["wall_s"]
        if spec["variant"] == "S5_metadata_forgery":
            trace["intermediates"] = dict(ref_trace["intermediates"])
            trace["wall_s"] = ref_trace["wall_s"]
        payload = {"run_id": run_id, "ell": list(range(LMAX + 1)),
                   "bandpowers": [float(x) for x in out]}
        publish_json(public / "runs" / run_id / "bandpowers.json", payload, trace)
        print(f"{run_id}: published ({trace['intermediates']['n_wigner3j']} 3j evals)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
