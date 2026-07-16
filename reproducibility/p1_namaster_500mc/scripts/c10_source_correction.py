#!/usr/bin/env python3
"""Write or verify the narrow source-provenance correction for in-flight C10 shards."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "reproducibility/p1_namaster_500mc/results/physical_spectrum_v2"
SHARDS = RESULTS / "shards"
OUTPUT = RESULTS / "c10_inflight_source_correction.json"
START_COMMIT = "201f8ef69d2487ab5b109ec486d10f1b97319ad8"
PATCH_COMMIT = "f2564cf4716e906f7b1b0521b0d79b0880aa576d"
STARTED_LOCAL = "2026-07-16T04:22:28-07:00"
CONFIGS = ("apod_fwhm_0p5", "apod_fwhm_3p0", "mask_b30")
SCRIPT = "reproducibility/p1_namaster_500mc/scripts/c10_robustness_battery.py"
MULTIPOLE = "reproducibility/p1_namaster_500mc/scripts/multipole_contract.py"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_commit(commit: str) -> None:
    subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def source_diff() -> str:
    return subprocess.check_output(
        ["git", "diff", "--no-ext-diff", START_COMMIT, PATCH_COMMIT, "--", SCRIPT, MULTIPOLE],
        cwd=ROOT,
        text=True,
    )


def verify_narrow_equivalence(diff: str) -> None:
    required = (
        "field_harmonic_kwargs",
        "lmax_mask",
        "if purify",
        "purify_b=state[\"purify\"]",
    )
    if any(token not in diff for token in required):
        raise ValueError("source diff is not the expected purification-only change")
    forbidden = (
        "SEED_BASE =",
        "N_REAL =",
        "NOISE_LEVEL_UKARMIN =",
        "recover_beta_deg(",
        "load_camb_lensed_spectra(",
    )
    if any(token in diff for token in forbidden):
        raise ValueError("source diff changed a non-purification scientific contract")


def shard_records() -> list[dict[str, Any]]:
    records = []
    for name in CONFIGS:
        result = SHARDS / f"c10_{name}.json"
        receipt = result.with_name(result.name + ".receipt.json")
        if not result.is_file() or not receipt.is_file():
            raise FileNotFoundError(f"missing completed shard pair: {result}")
        receipt_payload = json.loads(receipt.read_text(encoding="utf-8"))
        if receipt_payload.get("config_names") != [name]:
            raise ValueError(f"unexpected config receipt: {receipt}")
        if receipt_payload.get("result_sha256") != sha256(result):
            raise ValueError(f"result hash mismatch: {result}")
        records.append(
            {
                "config_name": name,
                "result_path": result.relative_to(ROOT).as_posix(),
                "result_sha256": sha256(result),
                "original_receipt_path": receipt.relative_to(ROOT).as_posix(),
                "original_receipt_sha256": sha256(receipt),
                "original_recorded_code_sha256": receipt_payload.get("code_sha256"),
            }
        )
    return records


def build_payload() -> dict[str, Any]:
    require_commit(START_COMMIT)
    require_commit(PATCH_COMMIT)
    diff = source_diff()
    verify_narrow_equivalence(diff)
    return {
        "schema": "bigbounce.p1b-c10-source-correction/v1",
        "status": "CORRECTIVE_PROVENANCE_NOT_RESULT_REWRITE",
        "process_started_local": STARTED_LOCAL,
        "process_start_commit": START_COMMIT,
        "later_purification_fix_commit": PATCH_COMMIT,
        "affected_configs": list(CONFIGS),
        "scope": (
            "non-purification runs only; field_harmonic_kwargs returns the same "
            "lmax argument for purify_b=False"
        ),
        "invalid_evidence": "the failed pre-fix purify_b attempt is excluded",
        "source_diff_sha256": hashlib.sha256(diff.encode("utf-8")).hexdigest(),
        "source_diff_paths": [SCRIPT, MULTIPOLE],
        "original_receipts_preserved": True,
        "shards": shard_records(),
    }


def verify_payload(payload: dict[str, Any]) -> None:
    expected = build_payload()
    if payload != expected:
        raise ValueError("source-correction receipt is stale or does not match current shards")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.verify:
        payload = json.loads(args.output.read_text(encoding="utf-8"))
        verify_payload(payload)
        print(f"PASS: {args.output.relative_to(ROOT)}")
        return
    payload = build_payload()
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
