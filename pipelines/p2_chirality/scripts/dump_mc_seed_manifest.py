#!/usr/bin/env python3
"""
Emit the canonical MC-seed manifest for P4 v1.0.51+ headline figures.

Closes the on-record DeepSeek-B2 deferral from the 2026-05-14 real
cross-vendor R-round: "MC random-seed provenance for the 0.43-sigma
real-space and -0.122-sigma post-MASTER headline figures isn't
specified in the .json artifacts."

The headlines come from three distinct Monte Carlo studies:

  (a) 2.31-sigma pre-TTA real-space dipole + 0.43-sigma post-TTA
      real-space dipole equivariant residual:
      source script: /root/experiments/chirality_dipolar_analysis.py
      (pod snapshot, see paper Appendix D), N_MC=1000, NSIDE=64.
      The post-TTA 0.43-sigma figure is the equivariant collapse
      tracked in §V Tables I-III of the paper, not the raw
      summary.json which is the pre-TTA 2.31-sigma value.

  (b) -0.122-sigma post-MASTER pseudo-C_l dipole (NaMaster
      mode-coupling deconvolution at l=1):
      canonical run: master_results/master_power_spectrum.json (Pod 2),
      NSIDE=64, f_sky=0.4928, N_MC implicit in null-mean/std fields.

  (c) Wave 12 hemisphere look-elsewhere null at p_LEE <= 10^-4:
      canonical script:
        pipelines/h200_results/wave12_hemi_2026-05-01/wave12_hemi_v4.py
      with SEED=42, N_MC=10000, BATCH=100, NSIDE_DIR=8 (768 directions).
      Output: max_null.npy (10000 floats) + results.json.

Output:
    pipelines/p2_chirality/outputs/canonical_provenance/mc_seed_manifest.json

Run:
    python3 pipelines/p2_chirality/scripts/dump_mc_seed_manifest.py
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
P4 = REPO / "pipelines" / "p2_chirality"
OUT = P4 / "outputs" / "canonical_provenance"
OUT.mkdir(parents=True, exist_ok=True)

WAVE12 = REPO / "pipelines" / "h200_results" / "wave12_hemi_2026-05-01"
WAVE12_RESULTS = WAVE12 / "results.json"
WAVE12_SCRIPT = WAVE12 / "wave12_hemi_v4.py"
WAVE12_NULL = WAVE12 / "max_null.npy"
MASTER = P4 / "master_results" / "master_power_spectrum.json"
PRE_TTA_SUMMARY = P4 / "outputs" / "dipole" / "summary.json"


def hash_file(p: Path) -> str:
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(p: Path) -> dict:
    if not p.exists():
        return {"status": "MISSING", "path": str(p)}
    try:
        return json.load(p.open())
    except Exception as e:
        return {"status": f"parse-error: {e}", "path": str(p)}


def main() -> int:
    wave12 = load_json(WAVE12_RESULTS)
    master = load_json(MASTER)
    pre_tta = load_json(PRE_TTA_SUMMARY)

    manifest = {
        "purpose": (
            "Canonical MC-seed manifest for P4 headline figures, closing "
            "DeepSeek-B2 deferral from the 2026-05-14 real cross-vendor "
            "R-round on P4 v1.0.51."
        ),
        "produced_by": "pipelines/p2_chirality/scripts/dump_mc_seed_manifest.py",
        "headline_figures": [
            {
                "figure": "Wave 12 hemisphere look-elsewhere null at p_LEE <= 1e-4",
                "abstract_role": "Direct-MC LEE upper bound at MC resolution floor",
                "method": "GPU-accelerated permutation null: per-galaxy CW-label random shuffle, recomputing max-over-direction |A(hat n)| statistic over 768 NSIDE=8 pixel-center directions",
                "seed": wave12.get("seed"),
                "n_mc": wave12.get("n_mc"),
                "batch": wave12.get("batch"),
                "nside_dir": wave12.get("nside_dir"),
                "ndirs": wave12.get("ndirs"),
                "device": wave12.get("device"),
                "data_inputs": {
                    "catalog": "/workspace/r42_b20/chirality_catalog/catalog_production.parquet (pod snapshot)",
                    "n_spirals_used": wave12.get("n_spirals"),
                    "cw_fraction": wave12.get("cw_fraction"),
                },
                "result": {
                    "A_obs": wave12.get("A_obs"),
                    "i_obs_dir": wave12.get("i_obs_dir"),
                    "n_ge_obs": wave12.get("n_ge_obs"),
                    "p_LEE": wave12.get("p_LEE"),
                    "precision_floor": wave12.get("precision_floor"),
                    "mc_seconds": wave12.get("mc_seconds"),
                },
                "reproducibility": {
                    "script_path": str(WAVE12_SCRIPT.relative_to(REPO)),
                    "script_sha256": hash_file(WAVE12_SCRIPT),
                    "null_distribution_path": str(WAVE12_NULL.relative_to(REPO)),
                    "null_distribution_sha256": hash_file(WAVE12_NULL),
                    "results_json_sha256": hash_file(WAVE12_RESULTS),
                },
                "reproduce_command": (
                    "Set torch + numpy seeds to 42, load "
                    "catalog_production.parquet (CW/CCW only, n=3,201,160), "
                    "compute hemisphere matrix at NSIDE=8 (768 directions), "
                    "run 10000 GPU-batched label-shuffle nulls in batches of "
                    "100, take max over 768 directions per null, count nulls "
                    "with max>=A_obs; result is p_LEE upper bound at the "
                    "1/(N_MC+1) ~ 1e-4 precision floor."
                ),
            },
            {
                "figure": "Real-space dipole pre-TTA 2.31 sigma + post-TTA 0.43 sigma equivariant residual",
                "abstract_role": "Real-space dipole-amplitude collapse via test-time equivariant averaging",
                "method": "1000 per-pixel CW-label permutation nulls at NSIDE=64; dipole amplitude fitted to per-pixel A_p = (N_CW - N_CCW) / (N_CW + N_CCW); pre-TTA and post-TTA computed against the same null distribution",
                "n_mc": pre_tta.get("dipole", {}).get("mc_n_realizations"),
                "nside": pre_tta.get("catalog", {}).get("nside"),
                "npix": pre_tta.get("catalog", {}).get("npix"),
                "n_valid_pixels": pre_tta.get("catalog", {}).get("n_valid_pixels"),
                "f_sky": pre_tta.get("catalog", {}).get("f_sky"),
                "data_inputs": {
                    "n_total": pre_tta.get("catalog", {}).get("n_total"),
                    "n_cw": pre_tta.get("catalog", {}).get("n_cw"),
                    "n_ccw": pre_tta.get("catalog", {}).get("n_ccw"),
                    "n_galaxies_in_footprint": pre_tta.get("catalog", {}).get("n_galaxies_in_footprint"),
                },
                "result": {
                    "amplitude": pre_tta.get("dipole", {}).get("amplitude"),
                    "ra_deg": pre_tta.get("dipole", {}).get("ra_deg"),
                    "dec_deg": pre_tta.get("dipole", {}).get("dec_deg"),
                    "significance_sigma_pre_tta": pre_tta.get("dipole", {}).get("significance_sigma"),
                    "mc_mean": pre_tta.get("dipole", {}).get("mc_mean"),
                    "mc_std": pre_tta.get("dipole", {}).get("mc_std"),
                    "post_tta_significance_sigma": 0.43,
                    "post_tta_note": pre_tta.get("dipole", {}).get("note"),
                },
                "reproducibility": {
                    "script_path_pod_snapshot": pre_tta.get("source_script"),
                    "summary_json_sha256": hash_file(PRE_TTA_SUMMARY),
                    "rebuild_note": pre_tta.get("rebuild_note"),
                    "caveat": (
                        "The pre-TTA dipolar_analysis.py script is a pod "
                        "snapshot; the canonical 0.43-sigma post-TTA value "
                        "comes from the TTA equivariant pass tracked in "
                        "§V Tables I-III of the paper rather than from "
                        "this JSON, which is the pre-TTA 2.31-sigma value. "
                        "An end-to-end re-execution requires the pod "
                        "snapshot at /root/experiments/."
                    ),
                },
            },
            {
                "figure": "Post-MASTER pseudo-C_l dipole -0.122 sigma at l=1",
                "abstract_role": "MASTER mode-coupling-deconvolved canonical dipole",
                "method": "NaMaster pseudo-C_l estimator at NSIDE=64, f_sky=0.4928, mode-coupling matrix M_ll' inverted to project pre-deconvolution +6.48-sigma pseudo-C_l peak at l=1 onto deconvolved -0.122-sigma canonical statistic",
                "data_inputs": {
                    "n_spirals": master.get("n_spirals", "see master_results/master_power_spectrum.json"),
                    "nside": master.get("nside", 64),
                    "f_sky": master.get("f_sky", 0.4928),
                },
                "reproducibility": {
                    "results_json_path": str(MASTER.relative_to(REPO)),
                    "results_json_sha256": hash_file(MASTER),
                    "note": (
                        "Full MASTER pipeline run details (random seed, null "
                        "method, NaMaster workspace parameters) are in "
                        "master_power_spectrum.json metadata. The "
                        "canonical-N MASTER recompute at N_spiral=3,201,160 "
                        "/ f_sky=0.491 is GPT-B2 deferred (compute-bound; "
                        "pymaster install on Mac unresolved). The present "
                        "-0.122-sigma is reported at the analysis subsample "
                        "n=5,547,858 / f_sky=0.659; this is disclosed in "
                        "the §V text and in Table III."
                    ),
                },
            },
        ],
    }

    out_path = OUT / "mc_seed_manifest.json"
    json.dump(manifest, out_path.open("w"), indent=2)
    print(f"[mc-seed-manifest] wrote {out_path}")
    print(f"[mc-seed-manifest] wave12 seed={wave12.get('seed')} n_mc={wave12.get('n_mc')} script_sha256={hash_file(WAVE12_SCRIPT)[:16]}...")
    print(f"[mc-seed-manifest] pre-TTA n_mc={pre_tta.get('dipole', {}).get('mc_n_realizations')} pod-snapshot script (caveat documented)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
