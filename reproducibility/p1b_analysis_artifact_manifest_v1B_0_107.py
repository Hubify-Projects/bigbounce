#!/usr/bin/env python3
"""Write the non-circular SHA-256 manifest for Paper 1B v1B.0.107.

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
OUTPUT = ROOT / "reproducibility" / "p1b_analysis_artifact_manifest_v1B.0.107.json"

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
    "reproducibility/p1_namaster_500mc/scripts/test_realization_parallel.py",
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
    "reproducibility/cosmology/reproduce_cosmology.sh",
    "reproducibility/cosmology/cobaya_planck.yaml",
    "reproducibility/cosmology/cobaya_planck_bao.yaml",
    "reproducibility/cosmology/cobaya_planck_bao_sn.yaml",
    "reproducibility/cosmology/cobaya_full_tension.yaml",
    "reproducibility/cosmology/convergence_latest.csv",
    "reproducibility/cosmology/dataset_chain_map.csv",
    "reproducibility/cosmology/frozen/full_tension_20260311_1728/MANIFEST.md",
    "reproducibility/cosmology/frozen/full_tension_20260311_1728/SHA256SUMS.txt",
    "reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/convergence_summary.json",
    "reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/parameter_summary_CORRECTED.json",
    "reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/MANIFEST.md",
    "reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/SHA256SUMS.txt",
    "reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/diagnostics/convergence_report.txt",
    "reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/diagnostics/parameter_summary_CORRECTED.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py",
    "research/branch_R_alp_birefringence/phase2_mcmc/alp_theory.py",
    "research/branch_R_alp_birefringence/phase2_mcmc/birefringence_lk.py",
    "research/branch_R_alp_birefringence/phase2_mcmc/run1_full.yaml",
    "reproducibility/cosmology/alp_prior_predictive.py",
    "reproducibility/cosmology/alp_prior_predictive_result.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/c10a_spectator_slice.py",
    "research/branch_R_alp_birefringence/phase2_mcmc/c10a_spectator_slice.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/c10b_alp_envelope_scan.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/c14_costheta_summary.py",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c14_costheta/c14_summary.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/c5_table_iv_recompute.py",
    "research/branch_R_alp_birefringence/phase2_mcmc/c5_table_iv_recompute.json",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.1.txt",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.2.txt",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.3.txt",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/c5.4.txt",
    "reproducibility/cosmology/chains/w0wa_quintom_desi_dr2/c15_converged/c15_summary.json",
]

FROZEN_CHAIN_DIRECTORIES = [
    "reproducibility/cosmology/frozen/full_tension_20260311_1728/chains",
    "reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/chains",
]

ALP_RESULT_DIRECTORIES = [
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/run1_full",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/run2_extended",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/run3_baseline",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous",
    "research/branch_R_alp_birefringence/phase2_mcmc/chains/c14_costheta",
]
ALP_SCIENTIFIC_SUFFIXES = {".txt", ".yaml", ".json", ".covmat", ".png", ".pdf"}


def manifest_artifacts() -> list[str]:
    """Return a stable, duplicate-free list including every frozen chain file."""
    discovered = list(ARTIFACTS)
    for relative_directory in FROZEN_CHAIN_DIRECTORIES:
        directory = ROOT / relative_directory
        discovered.extend(
            path.relative_to(ROOT).as_posix()
            for path in sorted(directory.rglob("*"))
            if path.is_file()
        )
    # Checkpoint/progress files are transient sampler-resume state. The paper's
    # numerical claims depend on the scientific chains, frozen inputs/updates,
    # covariance matrices, summaries, and plots retained here.
    for relative_directory in ALP_RESULT_DIRECTORIES:
        directory = ROOT / relative_directory
        discovered.extend(
            path.relative_to(ROOT).as_posix()
            for path in sorted(directory.rglob("*"))
            if path.is_file() and path.suffix in ALP_SCIENTIFIC_SUFFIXES
        )
    return list(dict.fromkeys(discovered))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    artifacts = manifest_artifacts()
    missing = [relative for relative in artifacts if not (ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError("missing required artifacts: " + ", ".join(missing))
    base_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    payload = {
        "schema_version": 1,
        "paper_version": "v1B.0.107",
        "status": "pre-release analysis-artifact provenance; not a paper-release commit",
        "base_repository_commit": base_commit,
        "hash_algorithm": "sha256",
        "artifacts": [
            {
                "path": relative,
                "bytes": (ROOT / relative).stat().st_size,
                "sha256": sha256(ROOT / relative),
            }
            for relative in artifacts
        ],
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
