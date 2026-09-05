"""Execute the batch-3 sealed runs and publish result+receipt pairs to public3/.

Identical harness to run_blind2.py (same reference contract construction, same
namaster_proof.receipts.publish_json content binding); it reads the sealed
assignment from $NP_SEALED_DIR and routes variants through variants3.run_variant
so the new S4b and S6 arms are available.
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
import variants2  # noqa: E402
import variants3  # noqa: E402
from namaster_proof.receipts import publish_json  # noqa: E402

NSIDE, LMAX, REF_SEED = 64, 64, 20260904
SEALED = Path(os.environ.get("NP_SEALED_DIR", ROOT / "sealed3"))


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
    public = ROOT / "public3"
    assignment = json.loads((SEALED / "assignment.json").read_text())
    contract, ref_out, ref_trace = build_reference()
    (public / "contract.json").write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n")
    cache = {"m": None, "out": ref_out, "trace": ref_trace}
    m_ref = pcl.coupling_matrix(pcl.mask_power(pcl.make_mask(NSIDE), LMAX), LMAX)

    sources = {}
    for run_id in sorted(assignment):
        spec = assignment[run_id]
        if spec["variant"] == "S4b_cache_crossrun":
            # substitute an EARLIER run of this batch (R6 cross-run disjunct);
            # if this arm lands in run_000 there is none, so fall back to the
            # reference and record which source was actually used.
            sources[run_id] = cache.get("prior_id") or "reference"
            cache["prior_out"] = cache.get("prior_out_run", ref_out)
        out, trace = variants3.run_variant(spec["variant"], NSIDE, LMAX,
                                           spec["map_seed"], cache=cache)
        if spec["variant"] == "S4_cache_substitute":
            for field in ("coupling_sha256", "coupling_shape", "coupling_support", "n_wigner3j"):
                trace["intermediates"][field] = ref_trace["intermediates"][field]
            trace["wall_s"] = ref_trace["wall_s"]
        if spec["variant"] == "S5_metadata_forgery":
            # Complete forgery, as pre-registered: the forger also fabricates the
            # declared pseudo-spectrum consistently, p := M C (one mat-vec).  This
            # is exactly the informed-forger limitation R7 declares up front.
            trace["intermediates"] = dict(ref_trace["intermediates"])
            forged = np.zeros(LMAX + 1)
            forged[2:] = m_ref[2:, 2:] @ np.asarray(out, dtype=float)[2:]
            trace["intermediates"]["pseudo_cl"] = [float(x) for x in forged]
            trace["wall_s"] = ref_trace["wall_s"]
        payload = {"run_id": run_id, "ell": list(range(LMAX + 1)),
                   "bandpowers": [float(x) for x in out]}
        publish_json(public / "runs" / run_id / "bandpowers.json", payload, trace)
        cache["prior_id"], cache["prior_out_run"] = run_id, np.asarray(out, dtype=float)
        print(f"{run_id}: published ({trace['intermediates']['n_wigner3j']} 3j evals)")
    (SEALED / "crossrun_sources.json").write_text(
        json.dumps(sources, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
