from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from verify_p4_p5_science_contracts import (  # noqa: E402
    ContractError,
    P4_CATALOG_SHA256,
    P5_PARENT_SHA256,
    verify_p4_harmonics,
    verify_p4_primary,
    verify_p5,
)


def p4_primary() -> dict:
    return {
        "schema": "p4-primary-hc-safe-label-shuffle/v1",
        "catalog": {"sha256": P4_CATALOG_SHA256},
        "selection": "primary_hc == True and raw_flip_qc_unsafe == False",
        "selection_counts": {
            "n_primary_hc_before_qc_exclusion": 949584,
            "n_raw_flip_qc_unsafe_excluded_from_primary_hc": 59515,
            "n_selected_rows": 890069,
            "n_unsafe_rows_selected": 0,
        },
    }


def p4_harmonics() -> dict:
    mask = "a" * 64
    result = {
        "schema": "p4-fsc-exact-support-harmonics/v1",
        "status": "complete",
        "catalog": {"sha256": P4_CATALOG_SHA256},
        "support": {
            "n_pixels": 24087,
            "expected_n_pixels": 24087,
            "definition": "class_eq in {CW,CCW}; N_spiral(pixel) >= 10",
            "mask": {"sha256": mask},
        },
        "common_support_invariants": {
            "all_data_fields_use_mask_sha256": mask,
            "all_null_fields_use_mask_sha256": mask,
        },
    }
    for key in (
        "fixed_occupancy_direct_mc_binary",
        "master_monopole_only_binary_500",
        "apodized_fsc_c2_2deg",
    ):
        result[key] = {"n_draws": 500}
    result["master_monopole_only_binary_10000"] = {"n_draws": 10_000}
    result["multipole_spectrum_binary"] = {
        f"ell_{ell}": {"n_draws": 500} for ell in range(1, 6)
    }
    return result


def inference(represented: int = 3) -> dict:
    return {
        "represented_clusters": represented,
        "inferential_status": "available",
        "normal_p_two_sided": 0.5,
        "se": 0.1,
        "ci95": [-0.2, 0.2],
    }


def suppressed() -> dict:
    return {
        "represented_clusters": 1,
        "inferential_status": "unavailable",
        "normal_p_two_sided": None,
        "se": None,
        "ci95": None,
    }


def p5() -> dict:
    cluster_results = {
        key: {"ci95": [-0.01, 0.01]}
        for key in (
            "healpix_nside2",
            "healpix_nside4",
            "healpix_nside8",
            "voidfinder_nearest_maximal_3d",
        )
    }
    return {
        "schema": "p5.focal-interaction-clustering-robustness/v1",
        "parent_contract": {"n": 145766, "canonical_rows_sha256": P5_PARENT_SHA256},
        "k13_identical_estimand_clustering_robustness": {
            "k": 13,
            "design_rank": 13,
            "results": cluster_results,
        },
        "void_by_program_interaction": {
            "interpretation_guardrail": "sparse-stratum inference is unavailable below two represented clusters",
            "cluster_robust_marginal_results": {
                "angular": {
                    "within_program_marginal_contrasts": {
                        "bright": inference(5),
                        "other": suppressed(),
                    },
                    "log_odds_interaction_coefficients": {
                        "other": {**suppressed(), "represented_clusters": 1},
                    },
                },
            },
            "cluster_robust_difference_in_differences": {
                "angular": {
                    "other_minus_bright": {**suppressed(), "represented_clusters": 1},
                },
            },
        },
    }


class ScienceContractTests(unittest.TestCase):
    def test_valid_fixtures_pass(self):
        verify_p4_primary(p4_primary())
        verify_p4_harmonics(p4_harmonics())
        verify_p5(p5())

    def test_p4_primary_fails_on_unsafe_selection_or_catalog_drift(self):
        for mutation in ("selection", "catalog", "count", "missing_explicit_unsafe_count"):
            with self.subTest(mutation=mutation):
                value = p4_primary()
                if mutation == "selection":
                    value["selection"] = "primary_hc == True"
                elif mutation == "catalog":
                    value["catalog"]["sha256"] = "0" * 64
                elif mutation == "missing_explicit_unsafe_count":
                    del value["selection_counts"]["n_unsafe_rows_selected"]
                else:
                    value["selection_counts"]["n_selected_rows"] += 1
                with self.assertRaises(ContractError):
                    verify_p4_primary(value)

    def test_p4_harmonics_fails_on_missing_leg_or_mask_drift(self):
        missing = p4_harmonics()
        del missing["apodized_fsc_c2_2deg"]
        with self.assertRaisesRegex(ContractError, "leg missing"):
            verify_p4_harmonics(missing)
        drift = p4_harmonics()
        drift["common_support_invariants"]["all_null_fields_use_mask_sha256"] = "b" * 64
        with self.assertRaisesRegex(ContractError, "another mask"):
            verify_p4_harmonics(drift)

    def test_p5_fails_if_any_cluster_interval_excludes_zero(self):
        value = p5()
        value["k13_identical_estimand_clustering_robustness"]["results"]["healpix_nside8"]["ci95"] = [0.1, 0.2]
        with self.assertRaisesRegex(ContractError, "excludes zero"):
            verify_p5(value)

    def test_p5_fails_if_sparse_stratum_publishes_inference(self):
        value = p5()
        sparse = value["void_by_program_interaction"]["cluster_robust_marginal_results"]["angular"][
            "within_program_marginal_contrasts"
        ]["other"]
        sparse.update({"inferential_status": "available", "normal_p_two_sided": 0.01, "se": 0.02, "ci95": [-0.1, 0.1]})
        with self.assertRaisesRegex(ContractError, "published as valid"):
            verify_p5(value)

    def test_p5_fails_without_sparse_guardrail(self):
        value = copy.deepcopy(p5())
        value["void_by_program_interaction"]["interpretation_guardrail"] = "use caution"
        with self.assertRaisesRegex(ContractError, "guardrail"):
            verify_p5(value)


if __name__ == "__main__":
    unittest.main()
