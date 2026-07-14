#!/usr/bin/env python3
"""Write the non-circular SHA-256 manifest for Paper 1B v1B.0.106.

The paper source and this generated manifest are deliberately excluded from
the hash set, avoiding a self-reference cycle.  The manifest identifies the
analysis inputs, generators, and result artifacts; a release commit/tag can be
added later without pretending the current uncommitted paper is frozen there.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reproducibility" / "p1b_analysis_artifact_manifest_v1B.0.106.json"

ARTIFACTS = [
    "reproducibility/p1_namaster_500mc/CHECKPOINT_RESUME_DESIGN.md",
    "reproducibility/p1_namaster_500mc/README.md",
    "reproducibility/p1_namaster_500mc/requirements.txt",
    "reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py",
    "reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py",
    "reproducibility/p1_namaster_500mc/scripts/c10_robustness_battery.py",
    "reproducibility/p1_namaster_500mc/scripts/declared_fsky_sign_battery.py",
    "reproducibility/p1_namaster_500mc/scripts/checkpoint_io.py",
    "reproducibility/p1_namaster_500mc/scripts/merge_c10_partials.py",
    "reproducibility/p1_namaster_500mc/scripts/test_windowed_rotation.py",
    "reproducibility/p1_namaster_500mc/scripts/plot_exact_window_results.py",
    "arxiv/figures/fig_namaster_recovery.png",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/summary.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/RUN_NOTES.md",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/bandpowers.npz",
    "reproducibility/p1_namaster_500mc/results/SUPERSEDED.md",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_canonical_refit.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_canonical_refit.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_lensing_bb_camb.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_lensing_bb_camb.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_apod_fwhm_0p5.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_apod_fwhm_0p5.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_apod_fwhm_3p0.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_apod_fwhm_3p0.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_mask_b30.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_mask_b30.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_purify_b.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/c10_purify_b.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/declared_fsky_0p85.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/declared_fsky_0p85.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/declared_fsky_0p65.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/declared_fsky_0p65.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/declared_negative_beta_fsky_0p32.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/shards/declared_negative_beta_fsky_0p32.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/c10_robustness_battery.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/c10_robustness_battery.json.receipt.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/declared_fsky_sign_battery.json",
    "reproducibility/p1_namaster_500mc/results/exact_window_500mc/declared_fsky_sign_battery.json.receipt.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/c5_table_iv_recompute.py",
    "research/branch_R_alp_birefringence/phase2_mcmc/c5_table_iv_recompute.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.1.txt",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.2.txt",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.3.txt",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.4.txt",
    "reproducibility/cosmology/chains/w0wa_quintom_desi_dr2/c15_converged/c15_summary.json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    missing = [relative for relative in ARTIFACTS if not (ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError("missing required artifacts: " + ", ".join(missing))
    base_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    payload = {
        "schema_version": 1,
        "paper_version": "v1B.0.106",
        "status": "pre-release analysis-artifact provenance; not a paper-release commit",
        "base_repository_commit": base_commit,
        "hash_algorithm": "sha256",
        "artifacts": [
            {
                "path": relative,
                "bytes": (ROOT / relative).stat().st_size,
                "sha256": sha256(ROOT / relative),
            }
            for relative in ARTIFACTS
        ],
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
