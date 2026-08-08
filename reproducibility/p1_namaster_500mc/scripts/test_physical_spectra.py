#!/usr/bin/env python3
"""Bounded regression tests for the raw CAMB spectrum contract."""

from __future__ import annotations

import unittest

import numpy as np

from physical_spectra import load_camb_lensed_spectra, validate_raw_lensed_spectra


class PhysicalSpectraTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ee, cls.bb, cls.metadata = load_camb_lensed_spectra(
            256, require_pinned_version=False
        )

    def test_raw_camb_spectra_pass_contract(self):
        validation = validate_raw_lensed_spectra(self.ee, self.bb)
        self.assertEqual(validation["status"], "pass")
        self.assertTrue(self.metadata["contract"]["raw_cl"])
        self.assertEqual(self.metadata["contract"]["camb_unit"], "muK")
        self.assertEqual(len(self.metadata["sha256"]["cl_ee_raw_uK2"]), 64)
        self.assertEqual(len(self.metadata["sha256"]["cl_bb_raw_uK2"]), 64)

    def test_d_ell_as_c_ell_scale_is_rejected(self):
        ell = np.arange(len(self.ee), dtype=float)
        fake_d_as_c = self.ee * ell * (ell + 1) / (2 * np.pi)
        fake_d_as_c[:2] = 0.0
        with self.assertRaisesRegex(ValueError, "D_ell-as-C_ell"):
            validate_raw_lensed_spectra(fake_d_as_c, self.bb)

    def test_historical_gaussian_template_is_rejected(self):
        ell = np.arange(len(self.ee), dtype=float)
        historical = np.zeros_like(ell)
        for amplitude, centre, width in [
            (15.0, 5.0, 3.0),
            (40.0, 140.0, 40.0),
            (20.0, 400.0, 60.0),
            (8.0, 700.0, 80.0),
        ]:
            historical += amplitude * np.exp(-0.5 * ((ell - centre) / width) ** 2)
        historical[:2] = 0.0
        with self.assertRaisesRegex(ValueError, "raw-C_ell scale"):
            validate_raw_lensed_spectra(historical, 0.05 * historical)

    def test_fixed_fraction_bb_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "physical-shape"):
            validate_raw_lensed_spectra(self.ee, 0.05 * self.ee)

    def test_hashes_are_deterministic_within_runtime(self):
        _, _, again = load_camb_lensed_spectra(256, require_pinned_version=False)
        self.assertEqual(self.metadata["sha256"], again["sha256"])


if __name__ == "__main__":
    unittest.main()
