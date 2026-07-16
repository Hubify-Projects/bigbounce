#!/usr/bin/env python3
"""Regression tests for consistent NaMaster field/bin multipole limits."""

from __future__ import annotations

import unittest

from multipole_contract import bandpower_edges


class MultipoleContractTest(unittest.TestCase):
    def test_last_bin_includes_exact_lmax(self):
        edges = bandpower_edges(nside=512, lmax=1024, n_bins=20)
        self.assertEqual(edges[0], 30)
        self.assertEqual(edges[-1], 1025)
        self.assertTrue(all(right > left for left, right in zip(edges, edges[1:])))

    def test_smoke_contract_uses_same_limit(self):
        edges = bandpower_edges(nside=128, lmax=256, n_bins=6)
        self.assertEqual(edges[-1] - 1, 256)

    def test_rejects_harmonics_outside_healpix_support(self):
        with self.assertRaisesRegex(ValueError, "HEALPix"):
            bandpower_edges(nside=128, lmax=384, n_bins=6)


if __name__ == "__main__":
    unittest.main()
