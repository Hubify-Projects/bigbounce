"""Execute the batch-4 sealed runs and publish result+receipt pairs to public4/.

Same harness as run_blind3.py (same reference contract construction, same
namaster_proof.receipts.publish_json content binding); it routes variants
through variants4.run_variant so the S7 and S8 arms are available, and it hands
the fixed full operator down through the cache so S7 pays no extra build.
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

import pcl  # noqa: E402
import variants  # noqa: E402
import variants3  # noqa: E402
import variants4  # noqa: E402
from namaster_proof.receipts import publish_json  # noqa: E402

NSIDE, LMAX, REF_SEED = 64, 64, 20260904
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed4"))


def build_reference() -> tuple[dict, np.ndarray, dict]:
    out, trace = variants.run_variant("honest", NSIDE, LMAX, REF_SEED)
    trace["intermediates"]["pseudo_cl"] = variants3.pseudo_spectrum(NSIDE, LMAX, REF_SEED)
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
    public = ROOT / "public4"
    assignment = json.loads((SEALED / "assignment.json").read_text())
    contract, ref_out, ref_trace = build_reference()
    (public / "contract.json").write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n")
    m_ref = pcl.coupling_matrix(pcl.mask_power(pcl.make_mask(NSIDE), LMAX), LMAX)
    cache = {"m": None, "out": ref_out, "trace": ref_trace, "m_full": m_ref}

    for run_id in sorted(assignment):
        spec = assignment[run_id]
        out, trace = variants4.run_variant(spec["variant"], NSIDE, LMAX,
                                           spec["map_seed"], cache=cache)
        if spec["variant"] == "S4_cache_substitute":
            for field in ("coupling_sha256", "coupling_shape", "coupling_support", "n_wigner3j"):
                trace["intermediates"][field] = ref_trace["intermediates"][field]
            trace["wall_s"] = ref_trace["wall_s"]
        if spec["variant"] == "S5_metadata_forgery":
            # Complete forgery, as pre-registered: the forger also fabricates the
            # declared pseudo-spectrum consistently, p := M C (one mat-vec).  This
            # is the informed-forger limitation R7 and R8 both declare up front.
            trace["intermediates"] = dict(ref_trace["intermediates"])
            forged = np.zeros(LMAX + 1)
            forged[2:] = m_ref[2:, 2:] @ np.asarray(out, dtype=float)[2:]
            trace["intermediates"]["pseudo_cl"] = [float(x) for x in forged]
            trace["wall_s"] = ref_trace["wall_s"]
        payload = {"run_id": run_id, "ell": list(range(LMAX + 1)),
                   "bandpowers": [float(x) for x in out]}
        publish_json(public / "runs" / run_id / "bandpowers.json", payload, trace)
        print(f"{run_id}: published ({trace['intermediates'].get('n_wigner3j')} 3j evals)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
