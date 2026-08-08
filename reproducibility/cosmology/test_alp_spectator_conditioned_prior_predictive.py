import importlib.util
import stat
import tempfile
import unittest
from pathlib import Path

import numpy as np


SCRIPT = Path(__file__).with_name("alp_spectator_conditioned_prior_predictive.py")
SPEC = importlib.util.spec_from_file_location("spectator_pp", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class SpectatorConditionedPriorPredictiveTests(unittest.TestCase):
    def test_draws_are_deterministic_and_ordered(self):
        first = MODULE.generate_draws(32, 1234)
        second = MODULE.generate_draws(32, 1234)
        for left, right in zip(first, second):
            self.assertTrue(np.array_equal(left, right))
        self.assertFalse(np.array_equal(first[0], first[1]))

    def test_atomic_json_is_portably_readable(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "artifact.json"
            MODULE.atomic_json(path, {"ok": True})
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o644)

    def test_summary_separates_unrestricted_joint_and_conditioned(self):
        beta = np.array([0.342, 0.342, 0.0, 0.0])
        omega = np.array([0.001, 0.1, 0.001, 0.1])
        summary = MODULE.summarize(beta, omega)
        self.assertEqual(summary["n_within_1sigma_unrestricted"], 2)
        self.assertEqual(summary["n_spectator_omega_a_lt_0p01"], 2)
        self.assertEqual(summary["n_joint_within_1sigma_and_spectator"], 1)
        self.assertEqual(summary["fraction_within_1sigma_unrestricted"], 0.5)
        self.assertEqual(summary["fraction_joint_within_1sigma_and_spectator"], 0.25)
        self.assertEqual(summary["fraction_within_1sigma_given_spectator"], 0.5)

    def test_zero_conditioned_count_retains_a_finite_upper_limit(self):
        summary = MODULE.summarize(
            np.array([0.0, 0.0, 0.0]),
            np.array([0.001, 0.002, 0.1]),
        )
        self.assertEqual(summary["n_joint_within_1sigma_and_spectator"], 0)
        self.assertEqual(summary["fraction_within_1sigma_given_spectator"], 0.0)
        self.assertEqual(summary["wilson95_conditioned"][0], 0.0)
        self.assertGreater(summary["wilson95_conditioned"][1], 0.0)

    def test_fast_integrator_matches_committed_reference(self):
        validation = MODULE.validate_fast_against_reference(n_validate=4, seed=17)
        self.assertLess(validation["max_abs_beta_deg"], 1e-6)
        self.assertLess(validation["max_abs_omega_a"], 1e-4)
        self.assertEqual(validation["spectator_classification_mismatches"], 0)


if __name__ == "__main__":
    unittest.main()
