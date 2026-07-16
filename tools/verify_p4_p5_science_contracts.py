#!/usr/bin/env python3
"""Fail-closed validation of the current P4/P5 closure receipts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "bigbounce.p4-p5-science-contracts/v1"
P4_PRIMARY_SCHEMA = "p4-primary-hc-safe-label-shuffle/v1"
P4_HARMONIC_SCHEMA = "p4-fsc-exact-support-harmonics/v1"
P5_SCHEMA = "p5.focal-interaction-clustering-robustness/v1"
P4_CATALOG_SHA256 = "139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
P5_PARENT_SHA256 = "3ff5afbb34eb7a1675b16e1ed895316de495d8b941c773ce750dd39d7f6e4ecb"
P4_HARMONIC_LEGS = (
    "fixed_occupancy_direct_mc_binary",
    "master_monopole_only_binary_500",
    "master_monopole_only_binary_10000",
    "apodized_fsc_c2_2deg",
    "multipole_spectrum_binary",
)
P5_CLUSTER_KEYS = (
    "healpix_nside2",
    "healpix_nside4",
    "healpix_nside8",
    "voidfinder_nearest_maximal_3d",
)
P4_TEX = Path("pipelines/p2_chirality/chirality_catalog_paper.tex")
P5_TEX = Path("pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex")


class ContractError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot load required science receipt {path}: {exc}") from exc
    _require(isinstance(value, dict), f"science receipt must be an object: {path}")
    return value


def _record(path: Path, root: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {
        "path": path.relative_to(root).as_posix(),
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def verify_p4_primary(payload: dict[str, Any]) -> None:
    _require(payload.get("schema") == P4_PRIMARY_SCHEMA, "P4 primary schema mismatch")
    _require(payload.get("catalog", {}).get("sha256") == P4_CATALOG_SHA256, "P4 catalog SHA mismatch")
    counts = payload.get("selection_counts", {})
    _require(counts.get("n_selected_rows") == 890_069, "P4 selected-row count must be 890069")
    _require(
        counts.get("n_raw_flip_qc_unsafe_excluded_from_primary_hc") == 59_515,
        "P4 unsafe exclusion count must be 59515",
    )
    _require(
        counts.get("n_primary_hc_before_qc_exclusion") == 949_584,
        "P4 pre-exclusion HC count must be 949584",
    )
    _require(949_584 - 59_515 == counts.get("n_selected_rows"), "P4 exclusion arithmetic mismatch")
    selection = payload.get("selection", "").replace(" ", "").lower()
    _require("raw_flip_qc_unsafe==false" in selection, "P4 selection does not exclude unsafe rows")
    _require("primary_hc==true" in selection, "P4 selection does not require primary_hc")
    _require(
        counts.get("n_unsafe_rows_selected") == 0,
        "P4 primary must explicitly report zero selected unsafe rows",
    )


def verify_p4_harmonics(payload: dict[str, Any]) -> None:
    _require(payload.get("schema") == P4_HARMONIC_SCHEMA, "P4 harmonic schema mismatch")
    _require(payload.get("status") == "complete", "P4 harmonic receipt is incomplete")
    _require(payload.get("catalog", {}).get("sha256") == P4_CATALOG_SHA256, "P4 harmonic catalog SHA mismatch")
    support = payload.get("support", {})
    _require(support.get("n_pixels") == 24_087, "P4 FSC must contain 24087 pixels")
    _require(support.get("expected_n_pixels") == 24_087, "P4 expected FSC count must be 24087")
    definition = str(support.get("definition", "")).replace(" ", "").lower()
    _require("n_spiral(pixel)>=10" in definition, "P4 FSC definition must require N_spiral >= 10")
    mask_sha = support.get("mask", {}).get("sha256")
    _require(isinstance(mask_sha, str) and len(mask_sha) == 64, "P4 FSC mask SHA is missing")
    invariants = payload.get("common_support_invariants", {})
    _require(invariants.get("all_data_fields_use_mask_sha256") == mask_sha, "P4 data fields use another mask")
    _require(invariants.get("all_null_fields_use_mask_sha256") == mask_sha, "P4 null fields use another mask")
    for leg in P4_HARMONIC_LEGS:
        _require(isinstance(payload.get(leg), dict), f"P4 harmonic leg missing: {leg}")
    _require(
        payload["fixed_occupancy_direct_mc_binary"].get("n_draws") == 500,
        "P4 fixed-occupancy binary leg must retain 500 draws",
    )
    _require(
        payload["apodized_fsc_c2_2deg"].get("n_draws") == 500,
        "P4 apodized leg must retain 500 draws",
    )
    _require(
        payload["master_monopole_only_binary_500"].get("n_draws") == 500,
        "P4 monopole calibration leg must retain 500 draws",
    )
    _require(
        payload["master_monopole_only_binary_10000"].get("n_draws") == 10_000,
        "P4 monopole calibration leg must retain 10000 draws",
    )
    multipoles = payload["multipole_spectrum_binary"]
    _require(
        set(multipoles) == {f"ell_{ell}" for ell in range(1, 6)},
        "P4 multipole leg must contain exactly ell=1..5",
    )
    _require(
        all(item.get("n_draws") == 500 for item in multipoles.values()),
        "P4 multipole legs must retain 500 draws",
    )


def _assert_zero_interval(item: Any, label: str) -> None:
    _require(isinstance(item, dict), f"P5 cluster result missing: {label}")
    interval = item.get("ci95")
    _require(
        isinstance(interval, list)
        and len(interval) == 2
        and isinstance(interval[0], (int, float))
        and isinstance(interval[1], (int, float))
        and interval[0] <= 0 <= interval[1],
        f"P5 cluster interval excludes zero: {label}",
    )


def _assert_suppressed(item: Any, label: str) -> None:
    _require(isinstance(item, dict), f"P5 sparse inference entry missing: {label}")
    _require(item.get("inferential_status") == "unavailable", f"P5 sparse inference published as valid: {label}")
    for field in ("normal_p_two_sided", "se", "ci95"):
        _require(item.get(field) is None, f"P5 sparse inference retains {field}: {label}")


def verify_p5(payload: dict[str, Any]) -> None:
    _require(payload.get("schema") == P5_SCHEMA, "P5 robustness schema mismatch")
    parent = payload.get("parent_contract", {})
    _require(parent.get("n") == 145_766, "P5 parent count must be 145766")
    _require(parent.get("canonical_rows_sha256") == P5_PARENT_SHA256, "P5 parent hash mismatch")
    k13 = payload.get("k13_identical_estimand_clustering_robustness", {})
    _require(k13.get("k") == 13 and k13.get("design_rank") == 13, "P5 K13 rank contract failed")
    results = k13.get("results", {})
    _require(set(results) == set(P5_CLUSTER_KEYS), "P5 must contain exactly four clustering results")
    for key in P5_CLUSTER_KEYS:
        _assert_zero_interval(results.get(key), key)

    interaction = payload.get("void_by_program_interaction", {})
    guardrail = str(interaction.get("interpretation_guardrail", "")).lower()
    _require("sparse-stratum" in guardrail, "P5 interaction sparse-stratum guardrail is absent")
    marginal = interaction.get("cluster_robust_marginal_results", {})
    did = interaction.get("cluster_robust_difference_in_differences", {})
    for cluster, cluster_result in marginal.items():
        by_program = cluster_result.get("within_program_marginal_contrasts", {})
        for program, item in by_program.items():
            represented = item.get("represented_clusters")
            _require(isinstance(represented, int), f"P5 represented_clusters missing: {cluster}/{program}")
            if represented < 2:
                _assert_suppressed(item, f"{cluster}/{program}")
                if program != "bright":
                    _assert_suppressed(
                        did.get(cluster, {}).get(f"{program}_minus_bright"),
                        f"{cluster}/{program}_minus_bright",
                    )
                    _assert_suppressed(
                        cluster_result.get("log_odds_interaction_coefficients", {}).get(program),
                        f"{cluster}/log_odds/{program}",
                    )


def verify_manuscript_contracts(p4_text: str, p5_text: str) -> None:
    """Prevent reviewed artifact/manuscript synchronization defects recurring."""
    p4_compact = " ".join(p4_text.split())
    p5_compact = " ".join(p5_text.split())
    for required in (
        "3a03ca4b008844fd...e32ce7d",
        "$890{,}069$ / $887{,}472$",
        "$(0.60414{\\pm}0.91749){\\times}10^{-6}$",
        "$(0.57796{\\pm}0.89263){\\times}10^{-6}$",
        "same exact 24,087-pixel \\FSC{} base mask",
        "not preregistered or fixed before unblinding",
        # 2026-07-16: the strict-primary overlay is PUBLISHED and byte-verified;
        # the manuscript must cite the immutable provider revision.
        "911316f31c21f2c4b933a2f3a761274cfe85c6d6",
        "apjs-release/v1.0.259-strict-primary",
    ):
        _require(required in p4_compact, f"P4 manuscript science contract missing: {required}")
    for forbidden in (
        "f6360f4bec226690...152c0",
        "$949{,}584$ / $947{,}326$",
        "$(5.2420{\\pm}0.9257){\\times}10^{-6}$",
        "$(5.1242{\\pm}0.2618){\\times}10^{-6}$",
        # Stale pre-publication disclosures (false after the 2026-07-16
        # overlay publication at revision 911316f3...):
        "still documents the earlier unsafe-inclusive",
        "does not claim that publication has occurred",
    ):
        _require(forbidden not in p4_compact, f"P4 superseded manuscript value recurred: {forbidden}")

    for required in (
        "corrected filament and cluster residuals are",
        "approximately $+1.40$ and $-1.56$",
        "applying the separate $z\\leq0.24$ cut leaves six",
        "A43--A44 interaction calculation finds no robust",
        "substantial program-by-environment interaction effects",
        "unstable sort changes 22 parent rows",
        "$3.09\\times10^{-5}$",
    ):
        _require(required in p5_compact, f"P5 manuscript science contract missing: {required}")
    _require(
        "no existing calculation bounds the program-by-environment interaction" not in p5_compact,
        "P5 stale no-interaction-calculation statement recurred",
    )


def verify(root: Path, paths: dict[str, str]) -> dict[str, Any]:
    root = root.resolve(strict=True)
    required = ("p4_primary", "p4_harmonics", "p4_strict_release", "p5_robustness")
    _require(set(paths) == set(required), "science-contract paths must name exactly p4_primary, p4_harmonics, p5_robustness")
    resolved: dict[str, Path] = {}
    for key in required:
        rel = Path(paths[key])
        _require(not rel.is_absolute() and ".." not in rel.parts, f"unsafe science-contract path: {paths[key]}")
        candidate = (root / rel).resolve()
        _require(candidate.is_relative_to(root) and candidate.is_file(), f"required science-contract receipt missing: {paths[key]}")
        resolved[key] = candidate
    p4_primary = _load(resolved["p4_primary"])
    p4_harmonics = _load(resolved["p4_harmonics"])
    p4_release = _load(resolved["p4_strict_release"])
    p5 = _load(resolved["p5_robustness"])
    verify_p4_primary(p4_primary)
    verify_p4_harmonics(p4_harmonics)
    verify_p5(p5)
    _require(
        p4_release.get("schema") == "p4-apjs-strict-primary-manifest/v1",
        "P4 strict release manifest schema mismatch",
    )
    _require(p4_release.get("paper_version") == "v1.0.259", "P4 strict release version mismatch")
    _require(
        p4_release.get("base_catalog", {}).get("sha256") == P4_CATALOG_SHA256,
        "P4 strict release base catalog mismatch",
    )
    reproduction = p4_release.get("primary_reproduction", {})
    _require(reproduction.get("status") == "PASS", "P4 strict release reproduction failed")
    _require(
        all(reproduction.get("hard_gates", {}).values()),
        "P4 strict release reproduction gates failed",
    )
    _require(reproduction.get("n_selected") == 890_069, "P4 strict release selected count mismatch")
    _require(reproduction.get("n_support") == 887_472, "P4 strict release support count mismatch")
    p4_tex = root / P4_TEX
    p5_tex = root / P5_TEX
    _require(p4_tex.is_file() and p5_tex.is_file(), "P4/P5 manuscript source is missing")
    verify_manuscript_contracts(
        p4_tex.read_text(encoding="utf-8"),
        p5_tex.read_text(encoding="utf-8"),
    )
    return {
        "schema": SCHEMA,
        "verdict": "PASS",
        "receipts": {key: _record(path, root) for key, path in resolved.items()},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--p4-primary", required=True)
    parser.add_argument("--p4-harmonics", required=True)
    parser.add_argument("--p4-strict-release", required=True)
    parser.add_argument("--p5-robustness", required=True)
    args = parser.parse_args()
    try:
        result = verify(args.project_root, {
            "p4_primary": args.p4_primary,
            "p4_harmonics": args.p4_harmonics,
            "p4_strict_release": args.p4_strict_release,
            "p5_robustness": args.p5_robustness,
        })
    except ContractError as exc:
        print(f"FAIL: {exc}")
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
