#!/usr/bin/env python3
"""Validate and atomically merge the exact-window N=500 production shards."""

from __future__ import annotations

from pathlib import Path

from checkpoint_io import publish_json, validate_json_receipt


RESULTS = Path(__file__).resolve().parent.parent / "results" / "exact_window_500mc"
SHARDS = RESULTS / "shards"
N_REAL = 500
SEED_START = 42
SEED_END = 541
OPERATOR = "NmtWorkspace.get_bandpower_windows exact tensor contraction"

C10_CONFIGS = [
    "canonical_refit",
    "lensing_bb_camb",
    "apod_fwhm_0p5",
    "apod_fwhm_3p0",
    "mask_b30",
    "purify_b",
]
DECLARED_CONFIGS = ["fsky_0p85", "fsky_0p65", "negative_beta_fsky_0p32"]


def load_suite(suite: str, prefix: str, names: list[str]):
    payloads = []
    receipts = []
    for name in names:
        path = SHARDS / f"{prefix}_{name}.json"
        payload, receipt = validate_json_receipt(
            path,
            expected_suite=suite,
            expected_configs=[name],
            expected_n_real=N_REAL,
            expected_seed_start=SEED_START,
            expected_seed_end=SEED_END,
        )
        if receipt.get("theory_operator") != OPERATOR:
            raise ValueError(f"mixed theory operator in {path}")
        if float(receipt.get("window_equivalence_max_abs", 1.0)) > 1e-10:
            raise ValueError(f"failed window-equivalence tolerance in {path}")
        payloads.append(payload)
        receipts.append(receipt)
    return payloads, receipts


def merge_c10() -> dict:
    payloads, receipts = load_suite("c10", "c10", C10_CONFIGS)
    software = receipts[0]["software"]
    if any(receipt.get("software") != software for receipt in receipts[1:]):
        raise ValueError("c10 shards used mixed software versions")
    configs = [item for payload in payloads for item in payload["configs"]]
    names = [item["name"] for item in configs]
    if names != C10_CONFIGS:
        raise ValueError(f"incomplete, duplicate, or reordered c10 shards: {names}")
    if any(item["n_real"] != N_REAL for item in configs):
        raise ValueError("c10 shard changed the declared N=500 ensemble")
    canonical = configs[0]
    payload = {
        "experiment": "c10 NaMaster robustness battery (R23conf META-M1/M2/M3/M5/M6)",
        "beta_injected_deg": 0.27,
        "n_real": N_REAL,
        "seed_base": SEED_START,
        "theory_operator": OPERATOR,
        "software": software,
        "canonical_exact_window_result": {
            "recovered_beta_deg": canonical["recovered_beta_deg"],
            "bias_deg": canonical["bias_deg"],
        },
        "superseded_effective_ell_anchor": payloads[0]["superseded_effective_ell_anchor"],
        "execution": "independently checkpointed production shards; exact canonical bandpowers reused without resimulation",
        "configs": configs,
        "total_runtime_s_sum_of_shards": sum(payload["total_runtime_s"] for payload in payloads),
        "child_shards": [
            {
                "path": f"shards/c10_{name}.json",
                "bytes": receipt["result_bytes"],
                "sha256": receipt["result_sha256"],
            }
            for name, receipt in zip(C10_CONFIGS, receipts, strict=True)
        ],
    }
    publish_json(
        RESULTS / "c10_robustness_battery.json",
        payload,
        {
            "suite": "c10_merged",
            "config_names": C10_CONFIGS,
            "n_real": N_REAL,
            "seed_start": SEED_START,
            "seed_end": SEED_END,
            "theory_operator": OPERATOR,
            "child_sha256": [item["result_sha256"] for item in receipts],
        },
    )
    return payload


def merge_declared() -> dict:
    payloads, receipts = load_suite(
        "declared_fsky_sign", "declared", DECLARED_CONFIGS
    )
    configs = [item for payload in payloads for item in payload["results"]]
    names = [item["name"] for item in configs]
    if names != DECLARED_CONFIGS:
        raise ValueError(f"incomplete, duplicate, or reordered declared shards: {names}")
    if any(item["n_real"] != N_REAL for item in configs):
        raise ValueError("declared shard changed the N=500 ensemble")
    software = payloads[0]["software"]
    if any(payload["software"] != software for payload in payloads[1:]):
        raise ValueError("declared shards used mixed software versions")
    payload = {
        "experiment": "declared NaMaster f_sky and sign checks with exact bandpower windows",
        "status_of_historical_outputs": "superseded effective-ell-template evidence preserved at top-level results",
        "n_real": N_REAL,
        "seed_base": SEED_START,
        "theory_operator": OPERATOR,
        "software": software,
        "results": configs,
        "total_runtime_s_sum_of_shards": sum(payload["total_runtime_s"] for payload in payloads),
        "child_shards": [
            {
                "path": f"shards/declared_{name}.json",
                "bytes": receipt["result_bytes"],
                "sha256": receipt["result_sha256"],
            }
            for name, receipt in zip(DECLARED_CONFIGS, receipts, strict=True)
        ],
    }
    publish_json(
        RESULTS / "declared_fsky_sign_battery.json",
        payload,
        {
            "suite": "declared_fsky_sign_merged",
            "config_names": DECLARED_CONFIGS,
            "n_real": N_REAL,
            "seed_start": SEED_START,
            "seed_end": SEED_END,
            "theory_operator": OPERATOR,
            "child_sha256": [item["result_sha256"] for item in receipts],
        },
    )
    return payload


def main() -> None:
    c10 = merge_c10()
    declared = merge_declared()
    print(
        f"validated and merged {len(c10['configs'])} c10 + "
        f"{len(declared['results'])} declared N=500 shards"
    )


if __name__ == "__main__":
    main()
