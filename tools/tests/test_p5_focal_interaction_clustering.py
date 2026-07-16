import importlib.util
import json
import math
import subprocess
import sys
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
SCRIPT = (
    REPO / "pipelines/p5_desi_chirality/scripts/"
    "39_focal_interaction_clustering_robustness.py"
)
OUTPUT = (
    REPO / "pipelines/p5_desi_chirality/outputs/"
    "39_focal_interaction_clustering_robustness.json"
)


@unittest.skipUnless(OUTPUT.exists(), "generated P5 closure artifact not present")
class P5FocalInteractionClusteringTest(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads(OUTPUT.read_text(encoding="utf-8"))

    def test_exact_parent_and_program_counts(self):
        parent = self.payload["parent_contract"]
        self.assertEqual(parent["n"], 145_766)
        self.assertEqual(
            parent["program_by_void_counts"],
            {
                "bright": {"nonvoid": 113_573, "void": 31_868},
                "dark": {"nonvoid": 187, "void": 50},
                "other": {"nonvoid": 69, "void": 19},
            },
        )

    def test_identical_k13_estimand_and_requested_clusters(self):
        result = self.payload["k13_identical_estimand_clustering_robustness"]
        self.assertEqual(result["k"], 13)
        self.assertEqual(result["design_rank"], 13)
        expected = {
            "healpix_nside2": 25,
            "healpix_nside4": 50,
            "healpix_nside8": 128,
            "voidfinder_nearest_maximal_3d": 3750,
        }
        estimates = []
        for key, clusters in expected.items():
            item = result["results"][key]
            self.assertEqual(item["clusters"], clusters)
            self.assertLess(item["ci95"][0], 0.0)
            self.assertGreater(item["ci95"][1], 0.0)
            estimates.append(item["delta_nonvoid_minus_void"])
        self.assertLess(max(estimates) - min(estimates), 1e-14)

    def test_interaction_is_explicit_and_sparse_strata_are_not_overclaimed(self):
        result = self.payload["void_by_program_interaction"]
        self.assertIn("void * C(program", result["formula"])
        self.assertIn("sparse-stratum", result["interpretation_guardrail"])
        for cluster in ("healpix_nside4", "voidfinder_nearest_maximal_3d"):
            by_program = result["cluster_robust_marginal_results"][cluster][
                "within_program_marginal_contrasts"
            ]
            self.assertEqual(set(by_program), {"bright", "dark", "other"})
            self.assertEqual(by_program["dark"]["n"], 237)
            self.assertEqual(by_program["other"]["n"], 88)
            self.assertEqual(
                set(result["cluster_robust_difference_in_differences"][cluster]),
                {"dark_minus_bright", "other_minus_bright"},
            )
            self.assertEqual(
                set(result["cluster_robust_marginal_results"][cluster][
                    "log_odds_interaction_coefficients"
                ]),
                {"dark", "other"},
            )
        angular = result["cluster_robust_marginal_results"]["healpix_nside4"]
        self.assertEqual(
            angular["within_program_marginal_contrasts"]["other"]["inferential_status"],
            "unavailable",
        )
        self.assertIsNone(
            angular["within_program_marginal_contrasts"]["other"]["normal_p_two_sided"]
        )
        self.assertEqual(
            result["cluster_robust_difference_in_differences"]["healpix_nside4"][
                "other_minus_bright"
            ]["inferential_status"],
            "unavailable",
        )

    def test_counterfactual_toggles_void_interaction_columns(self):
        spec = importlib.util.spec_from_file_location("p5_39", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Intercept, void, dark, void×dark.  Both observed rows are DARK;
        # their observed void state differs, but both counterfactual pairs
        # must use interaction=0 at void=0 and interaction=1 at void=1.
        x = __import__("numpy").array([
            [1.0, 0.0, 1.0, 0.0],
            [1.0, 1.0, 1.0, 1.0],
        ])
        beta = __import__("numpy").array([0.1, 0.2, -0.3, 0.8])
        estimate, _ = module.marginal_delta_gradient(
            x, beta, 1, [3], __import__("numpy").array([True, True]),
        )
        expit = lambda value: 1.0 / (1.0 + math.exp(-value))
        expected = expit(0.1 - 0.3) - expit(0.1 + 0.2 - 0.3 + 0.8)
        self.assertAlmostEqual(estimate, expected, places=14)

    def test_artifact_is_deterministic(self):
        before = OUTPUT.read_bytes()
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=REPO,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            check=False,
            # A standalone run is normally about one minute on this host, but
            # concurrent six-paper closure jobs can saturate BLAS and pushed a
            # verified deterministic rerun just beyond five minutes.
            timeout=900,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr.decode())
        self.assertEqual(OUTPUT.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
