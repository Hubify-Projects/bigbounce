#!/usr/bin/env python3
"""Generate a version-matched, Git-bound P1B analysis-artifact manifest."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "arxiv" / "paper1b_mcmc_companion.tex"
LEGACY_GENERATOR = ROOT / "reproducibility" / "p1b_analysis_artifact_manifest_v1B_0_108.py"

CURRENT_FIXED_ARTIFACTS = [
    "reproducibility/generate_p1b_analysis_manifest.py",
    "reproducibility/cosmology/write_bbn_execution_receipt.py",
    "reproducibility/cosmology/frozen/bbn_execution_receipt.json",
    "reproducibility/cosmology/c13_s8_desy3_overlay_postburn.json",
    "reproducibility/cosmology/c13_s8_desy3_overlay_postburn.json.receipt.json",
    "reproducibility/cosmology/c13_s8_desy3_overlay_postburn.png",
    "reproducibility/p1_namaster_500mc/scripts/checkpoint_io.py",
    "reproducibility/p1_namaster_500mc/scripts/multipole_contract.py",
    "reproducibility/p1_namaster_500mc/scripts/physical_spectra.py",
    "reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py",
    "reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py",
    "reproducibility/p1_namaster_500mc/scripts/c10_robustness_battery.py",
    "reproducibility/p1_namaster_500mc/scripts/declared_fsky_sign_battery.py",
    "reproducibility/p1_namaster_500mc/scripts/merge_c10_partials.py",
    "reproducibility/p1_namaster_500mc/scripts/test_c10_checkpoint_resume.py",
    "reproducibility/p1_namaster_500mc/scripts/test_canonical_parallel.py",
    "reproducibility/p1_namaster_500mc/scripts/test_multipole_contract.py",
    "reproducibility/p1_namaster_500mc/scripts/test_physical_spectra.py",
    "reproducibility/p1_namaster_500mc/scripts/test_realization_parallel.py",
    "reproducibility/p1_namaster_500mc/scripts/test_windowed_rotation.py",
]
CURRENT_RESULT_DIRECTORY = (
    ROOT / "reproducibility" / "p1_namaster_500mc" / "results" / "physical_spectrum_v2"
)


def load_legacy_generator():
    spec = importlib.util.spec_from_file_location("p1b_manifest_legacy", LEGACY_GENERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load legacy manifest generator: {LEGACY_GENERATOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def manuscript_version(path: Path = MANUSCRIPT) -> str:
    match = re.search(
        r"\\newcommand\{\\paperVersion\}\{([^}]+)\}",
        path.read_text(encoding="utf-8"),
    )
    if match is None:
        raise ValueError(f"paperVersion macro absent: {path}")
    return match.group(1)


def current_result_artifacts() -> list[str]:
    if not CURRENT_RESULT_DIRECTORY.is_dir():
        raise FileNotFoundError(
            f"current P1B production result directory is missing: {CURRENT_RESULT_DIRECTORY}"
        )
    artifacts = []
    for path in sorted(CURRENT_RESULT_DIRECTORY.rglob("*")):
        if not path.is_file():
            continue
        if any(part.startswith(".") for part in path.relative_to(CURRENT_RESULT_DIRECTORY).parts):
            continue
        artifacts.append(path.relative_to(ROOT).as_posix())
    return artifacts


def require_head_bound(paths: list[str], commit: str) -> None:
    missing = [path for path in paths if not (ROOT / path).is_file()]
    if missing:
        raise FileNotFoundError("missing required artifacts: " + ", ".join(missing))
    status = subprocess.check_output(
        ["git", "status", "--porcelain", "--", *paths],
        cwd=ROOT,
        text=True,
    ).strip()
    if status:
        raise ValueError("manifest artifacts are not clean at HEAD:\n" + status)
    tracked = set(
        subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", commit],
            cwd=ROOT,
            text=True,
        ).splitlines()
    )
    absent = [path for path in paths if path not in tracked]
    if absent:
        raise ValueError("manifest artifacts are absent from base commit: " + ", ".join(absent))


def artifact_record_at_commit(relative: str, commit: str) -> dict[str, Any]:
    data = subprocess.check_output(
        ["git", "show", f"{commit}:{relative}"],
        cwd=ROOT,
    )
    blob_sha256 = hashlib.sha256(data).hexdigest()
    record: dict[str, Any] = {
        "path": relative,
        "local_git_blob_bytes": len(data),
        "local_git_blob_sha256": blob_sha256,
    }
    pointer = re.fullmatch(
        rb"version https://git-lfs.github.com/spec/v1\n"
        rb"oid sha256:([0-9a-f]{64})\n"
        rb"size ([1-9][0-9]*)\n?",
        data,
    )
    if pointer:
        record.update(
            {
                "storage": "git-lfs-pointer",
                "lfs_oid_sha256": pointer.group(1).decode("ascii"),
                "lfs_declared_bytes": int(pointer.group(2)),
                "scientific_payload_mirror": (
                    "https://huggingface.co/datasets/bamfai/p1b-mcmc-diagnostics"
                ),
            }
        )
    else:
        record.update(
            {
                "storage": "git-blob",
                "scientific_payload_sha256": blob_sha256,
                "scientific_payload_bytes": len(data),
            }
        )
    return record


def build_payload(*, paper_version: str, base_commit: str) -> dict[str, Any]:
    legacy = load_legacy_generator()
    artifacts = list(
        dict.fromkeys(
            legacy.manifest_artifacts()
            + CURRENT_FIXED_ARTIFACTS
            + current_result_artifacts()
        )
    )
    require_head_bound(artifacts, base_commit)
    payload = {
        "schema_version": 3,
        "paper_version": paper_version,
        "status": "immutable analysis-artifact provenance bound to a committed repository state",
        "base_repository_commit": base_commit,
        "hash_algorithm": "sha256",
        "storage_semantics": {
            "git-blob": "local blob is the scientific payload",
            "git-lfs-pointer": (
                "local blob hash authenticates only the pointer; "
                "lfs_oid_sha256 and lfs_declared_bytes identify the scientific payload"
            ),
        },
        "scientific_payload_mirrors": {
            "frozen_cosmology_chains": "https://huggingface.co/datasets/bamfai/p1b-mcmc-diagnostics",
            "namaster_artifacts": "https://huggingface.co/datasets/bamfai/p1b-namaster-artifacts",
            "alp_chains": "https://huggingface.co/datasets/bamfai/p1b-alp-chains",
        },
        "authoritative_ess": {
            "estimator": "integrated autocorrelation time in frozen diagnostics",
            "full_tension": {
                "artifact": "reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/freeze_diagnostics_CORRECTED.json",
                "limiting_parameter": "delta_neff",
                "minimum_ess": 4761.371228048536,
            },
            "planck_bao_sn": {
                "artifact": "reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/diagnostics/convergence_report.txt",
                "limiting_parameter": "sigma8",
                "minimum_ess": 4692,
            },
        },
        "artifacts": [
            artifact_record_at_commit(path, base_commit) for path in artifacts
        ],
    }
    if not any(item["storage"] == "git-lfs-pointer" for item in payload["artifacts"]):
        raise RuntimeError("expected frozen-chain Git LFS pointers, found none")
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-version")
    parser.add_argument("--base-commit")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    version = args.paper_version or manuscript_version()
    base_commit = args.base_commit or subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    output = args.output or (
        ROOT / "reproducibility" / f"p1b_analysis_artifact_manifest_{version}.json"
    )
    payload = build_payload(paper_version=version, base_commit=base_commit)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": output.relative_to(ROOT).as_posix(),
                "paper_version": version,
                "base_repository_commit": base_commit,
                "artifact_count": len(payload["artifacts"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
