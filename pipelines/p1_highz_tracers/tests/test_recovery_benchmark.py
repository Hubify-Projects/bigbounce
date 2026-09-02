"""Offline unit tests for `benchmark_known_object_recovery.py`
(NEXT_SCIENCE_LEDGER.md item #8 -- anomaly catalogue known-object recovery
benchmark).

No network access; no VizieR/astroquery calls; no live reference catalogues.
Covers only the pure, locally-computable pieces: positional cross-match,
HEALPix footprint restriction, Wilson-score CI arithmetic, and the
enrichment/closed-loop-candidate computation, all against small synthetic
fixtures with hand-verifiable expected results.
"""

from __future__ import annotations

import importlib.util
import math
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

MODULE_PATH = Path(__file__).resolve().parents[1] / "clean_rerun" / "benchmark_known_object_recovery.py"
SPEC = importlib.util.spec_from_file_location("benchmark_known_object_recovery", MODULE_PATH)
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)  # type: ignore[union-attr]


def make_catalog_spec(**overrides) -> "mod.CatalogSpec":
    defaults = dict(
        name="test_catalog",
        path="unused.parquet",
        id_col="targetid",
        ra_col="ra",
        dec_col="dec",
        score_col="score",
        z_col="z",
        threshold=5.0,
        parent_total=1_000_000,
        catalog_total_at_threshold=1_000,
        catalog_total_note="synthetic test fixture",
    )
    defaults.update(overrides)
    return mod.CatalogSpec(**defaults)


class TestWilsonScoreInterval(unittest.TestCase):
    def test_zero_denominator_is_nan(self):
        lo, hi = mod.wilson_score_interval(0, 0)
        self.assertTrue(math.isnan(lo))
        self.assertTrue(math.isnan(hi))

    def test_known_case_matches_hand_computation(self):
        # k=8, n=10 -> p_hat=0.8; closed-form Wilson 95% CI, verified against
        # the standard formula (z=1.959963984540054) by direct computation.
        lo, hi = mod.wilson_score_interval(8, 10)
        self.assertAlmostEqual(lo, 0.4901624715366418, places=9)
        self.assertAlmostEqual(hi, 0.9433178485456247, places=9)

    def test_perfect_recovery_lower_bound_is_positive_upper_bound_capped(self):
        # k=n=5 -- algebraically the Wilson upper bound for p_hat=1 is EXACTLY 1
        # (center+half_width both reduce to (1+z^2/n)/(1+z^2/n)), never < 1; the
        # lower bound must still be a strictly positive, non-trivial value.
        lo, hi = mod.wilson_score_interval(5, 5)
        self.assertGreater(lo, 0.0)
        self.assertLess(lo, 1.0)
        self.assertEqual(hi, 1.0)

    def test_partial_recovery_bounds_strictly_inside_unit_interval(self):
        lo, hi = mod.wilson_score_interval(8, 10)
        self.assertGreater(lo, 0.0)
        self.assertLess(hi, 1.0)

    def test_ci_widens_as_n_shrinks(self):
        lo_small, hi_small = mod.wilson_score_interval(1, 2)
        lo_large, hi_large = mod.wilson_score_interval(50, 100)
        self.assertGreater(hi_small - lo_small, hi_large - lo_large)


class TestPositionalCrossmatch(unittest.TestCase):
    def test_exact_coincidence_matches_within_radius(self):
        ref_ra = np.array([10.0, 20.0, 30.0])
        ref_dec = np.array([0.0, 0.0, 0.0])
        cat_ra = np.array([10.0001, 20.5, 30.0001])  # ~0.36 arcsec, ~far, ~0.36 arcsec
        cat_dec = np.array([0.0, 0.0, 0.0])
        matched, sep, idx = mod.crossmatch_positional(ref_ra, ref_dec, cat_ra, cat_dec, radius_arcsec=1.5)
        self.assertTrue(matched[0])
        self.assertFalse(matched[1])
        self.assertTrue(matched[2])
        np.testing.assert_array_equal(idx, [0, 1, 2])

    def test_empty_catalog_matches_nothing(self):
        ref_ra = np.array([10.0, 20.0])
        ref_dec = np.array([0.0, 0.0])
        matched, sep, idx = mod.crossmatch_positional(ref_ra, ref_dec, np.array([]), np.array([]), radius_arcsec=1.5)
        self.assertFalse(matched.any())
        self.assertTrue(np.all(idx == -1))

    def test_empty_reference_returns_empty(self):
        matched, sep, idx = mod.crossmatch_positional(
            np.array([]), np.array([]), np.array([10.0]), np.array([0.0]), radius_arcsec=1.5
        )
        self.assertEqual(len(matched), 0)

    def test_radius_boundary_is_respected(self):
        # separation exactly ~2.0 arcsec; a 1.5" radius must reject, a 3.0" radius must accept
        ref_ra = np.array([10.0])
        ref_dec = np.array([0.0])
        cat_ra = np.array([10.0 + 2.0 / 3600.0])
        cat_dec = np.array([0.0])
        matched_tight, _, _ = mod.crossmatch_positional(ref_ra, ref_dec, cat_ra, cat_dec, radius_arcsec=1.5)
        matched_loose, _, _ = mod.crossmatch_positional(ref_ra, ref_dec, cat_ra, cat_dec, radius_arcsec=3.0)
        self.assertFalse(matched_tight[0])
        self.assertTrue(matched_loose[0])


class TestRedshiftAgreement(unittest.TestCase):
    def test_agreement_and_disagreement_and_not_applicable(self):
        ref_z = np.array([1.0, 1.0, 1.0, np.nan])
        cat_z = np.array([1.001, 2.0, 1.0])
        cat_idx = np.array([0, 1, 2, 0])
        matched = np.array([True, True, True, False])
        flags = mod.redshift_agreement(ref_z, cat_z, cat_idx, matched, z_tol=0.05)
        self.assertTrue(flags[0])   # close enough
        self.assertFalse(flags[1])  # far off
        self.assertTrue(flags[2])   # exact
        self.assertIsNone(flags[3])  # unmatched -> N/A


class TestFootprintRestriction(unittest.TestCase):
    def setUp(self):
        # Build a tiny synthetic locator inventory with two healpix pixels present.
        import healpy as hp

        self.nside = 64
        # Pick two real pixel centers so we can construct ra/dec that land inside them.
        self.pixel_a = 1000
        self.pixel_b = 2000
        theta_a, phi_a = hp.pix2ang(self.nside, self.pixel_a, nest=True)
        theta_b, phi_b = hp.pix2ang(self.nside, self.pixel_b, nest=True)
        self.ra_a, self.dec_a = math.degrees(phi_a), 90.0 - math.degrees(theta_a)
        self.ra_b, self.dec_b = math.degrees(phi_b), 90.0 - math.degrees(theta_b)
        # Far outside pixel, a point definitely not in {pixel_a, pixel_b}
        self.ra_out, self.dec_out = 0.0, -89.0

    def test_membership_matches_expected_pixels(self):
        footprint = {self.pixel_a, self.pixel_b}
        ra = np.array([self.ra_a, self.ra_b, self.ra_out])
        dec = np.array([self.dec_a, self.dec_b, self.dec_out])
        mask = mod.restrict_to_footprint(ra, dec, footprint, nside=self.nside, nest=True)
        self.assertTrue(mask[0])
        self.assertTrue(mask[1])
        # the "out" point is not guaranteed to miss both real pixels by construction,
        # so instead assert it disagrees whenever it truly falls outside the 2-pixel set
        import healpy as hp

        out_pix = hp.ang2pix(self.nside, math.radians(90.0 - self.dec_out), math.radians(self.ra_out), nest=True)
        self.assertEqual(mask[2], out_pix in footprint)

    def test_load_footprint_pixel_set_reads_jsonl(self, tmp_path=None):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "locator_inventory.jsonl"
            path.write_text(
                '{"healpix": 111, "survey": "main", "program": "dark"}\n'
                '{"healpix": 222, "survey": "main", "program": "bright"}\n'
                '{"healpix": 111, "survey": "sv1", "program": "dark"}\n',
                encoding="utf-8",
            )
            pixels = mod.load_footprint_pixel_set(path)
            self.assertEqual(pixels, {111, 222})

    def test_load_footprint_pixel_set_fails_closed_on_missing_file(self):
        with self.assertRaises(mod.BenchmarkError):
            mod.load_footprint_pixel_set(Path("/nonexistent/locator_inventory.jsonl"))


class TestComputeClassRecovery(unittest.TestCase):
    def test_recovery_and_enrichment_hand_computed(self):
        # 10 reference objects, all in footprint (no footprint restriction passed),
        # 5 of them coincide exactly with catalog rows -> recovery = 0.5
        ref_ra = np.array([float(i) for i in range(10)])
        ref_dec = np.zeros(10)
        ref_z = None

        cat_ra = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 100.0])  # 5 of these hit ref[0..4]
        cat_dec = np.zeros(6)
        catalog_df = pd.DataFrame({"targetid": range(6), "ra": cat_ra, "dec": cat_dec, "z": [np.nan] * 6})

        spec = make_catalog_spec(parent_total=1_000_000, catalog_total_at_threshold=1_000)
        # base_rate = 1000/1e6 = 0.001; recovery = 0.5 -> enrichment = 500

        result = mod.compute_class_recovery(
            class_id="synthetic",
            class_name="Synthetic test class",
            citation="test fixture",
            ref_ra=ref_ra,
            ref_dec=ref_dec,
            ref_z=ref_z,
            catalog_df=catalog_df,
            spec=spec,
            footprint_pixels=None,
            radius_arcsec=1.0,
            z_tol=0.05,
        )
        self.assertEqual(result.n_reference_in_footprint, 10)
        self.assertEqual(result.n_matched, 5)
        self.assertAlmostEqual(result.recovery, 0.5)
        self.assertAlmostEqual(result.base_rate, 0.001)
        self.assertAlmostEqual(result.enrichment, 500.0)
        self.assertTrue(result.is_closed_loop_candidate)  # 500x > 10x and 5 matches >= min 5

    def test_closed_loop_candidate_requires_min_matches(self):
        # enrichment is huge but only 2 matches -- must NOT be flagged (min 5 matches)
        ref_ra = np.array([0.0, 1.0, 100.0, 101.0, 102.0])
        ref_dec = np.zeros(5)
        cat_ra = np.array([0.0, 1.0])
        cat_dec = np.zeros(2)
        catalog_df = pd.DataFrame({"targetid": range(2), "ra": cat_ra, "dec": cat_dec, "z": [np.nan, np.nan]})
        spec = make_catalog_spec(parent_total=1_000_000, catalog_total_at_threshold=1_000)

        result = mod.compute_class_recovery(
            class_id="synthetic2",
            class_name="Synthetic test class 2",
            citation="test fixture",
            ref_ra=ref_ra,
            ref_dec=ref_dec,
            ref_z=None,
            catalog_df=catalog_df,
            spec=spec,
            footprint_pixels=None,
            radius_arcsec=1.0,
            z_tol=0.05,
        )
        self.assertEqual(result.n_matched, 2)
        self.assertGreater(result.enrichment, mod.CLOSED_LOOP_ENRICHMENT_MIN)
        self.assertFalse(result.is_closed_loop_candidate)

    def test_zero_matches_gives_zero_recovery_not_nan(self):
        ref_ra = np.array([500.0, 501.0])
        ref_dec = np.zeros(2)
        cat_ra = np.array([0.0])
        cat_dec = np.zeros(1)
        catalog_df = pd.DataFrame({"targetid": [0], "ra": cat_ra, "dec": cat_dec, "z": [np.nan]})
        spec = make_catalog_spec()
        result = mod.compute_class_recovery(
            class_id="synthetic3",
            class_name="Synthetic test class 3",
            citation="test fixture",
            ref_ra=ref_ra,
            ref_dec=ref_dec,
            ref_z=None,
            catalog_df=catalog_df,
            spec=spec,
            footprint_pixels=None,
            radius_arcsec=1.0,
            z_tol=0.05,
        )
        self.assertEqual(result.n_matched, 0)
        self.assertEqual(result.recovery, 0.0)
        self.assertEqual(result.enrichment, 0.0)
        self.assertFalse(result.is_closed_loop_candidate)

    def test_footprint_restriction_reduces_denominator(self):
        import healpy as hp

        nside = 64
        pixel_in = 5000
        theta, phi = hp.pix2ang(nside, pixel_in, nest=True)
        ra_in, dec_in = math.degrees(phi), 90.0 - math.degrees(theta)

        ref_ra = np.array([ra_in, ra_in, 0.0])  # first two inside footprint, third far outside (likely not)
        ref_dec = np.array([dec_in, dec_in, -89.9])
        cat_ra = np.array([ra_in])
        cat_dec = np.array([dec_in])
        catalog_df = pd.DataFrame({"targetid": [0], "ra": cat_ra, "dec": cat_dec, "z": [np.nan]})
        spec = make_catalog_spec()

        footprint = {pixel_in}
        result = mod.compute_class_recovery(
            class_id="synthetic4",
            class_name="Synthetic test class 4",
            citation="test fixture",
            ref_ra=ref_ra,
            ref_dec=ref_dec,
            ref_z=None,
            catalog_df=catalog_df,
            spec=spec,
            footprint_pixels=footprint,
            radius_arcsec=1.0,
            z_tol=0.05,
            nside=nside,
            nest=True,
        )
        # only the two ra_in/dec_in points should survive footprint restriction
        # (third point may or may not also land in pixel_in by coincidence but is
        # extremely unlikely to at this separation)
        self.assertLessEqual(result.n_reference_in_footprint, 3)
        self.assertGreaterEqual(result.n_reference_in_footprint, 2)
        self.assertEqual(result.n_matched, result.n_reference_in_footprint)  # both match the single cat row exactly
        self.assertEqual(result.recovery, 1.0)


class TestCatalogSpecAndLoading(unittest.TestCase):
    def test_from_json_requires_keys(self):
        with self.assertRaises(mod.BenchmarkError):
            mod.CatalogSpec.from_json({"name": "x"})

    def test_from_json_round_trip(self):
        payload = {
            "name": "s8_preview",
            "path": "/tmp/x.parquet",
            "id_col": "targetid",
            "ra_col": "target_ra",
            "dec_col": "target_dec",
            "score_col": "anomaly_score",
            "z_col": "z",
            "threshold": 8.0,
            "parent_total": 27547223,
            "catalog_total_at_threshold": 3810,
            "catalog_total_note": "documented in SESSION_HANDOFF",
        }
        spec = mod.CatalogSpec.from_json(payload)
        self.assertEqual(spec.name, "s8_preview")
        self.assertEqual(spec.threshold, 8.0)
        self.assertFalse(spec.is_partial_preview)

    def test_load_catalog_missing_file_fails_closed(self):
        spec = make_catalog_spec(path="/nonexistent/nope.parquet")
        with self.assertRaises(mod.BenchmarkError):
            mod.load_catalog(spec)

    def test_load_catalog_missing_column_fails_closed(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cat.parquet"
            pd.DataFrame({"targetid": [1, 2], "ra": [1.0, 2.0]}).to_parquet(path)
            spec = make_catalog_spec(path=str(path))
            with self.assertRaises(mod.BenchmarkError):
                mod.load_catalog(spec)

    def test_load_catalog_normalizes_columns(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cat.parquet"
            pd.DataFrame(
                {
                    "targetid": [1, 2],
                    "target_ra": [10.0, 20.0],
                    "target_dec": [1.0, 2.0],
                    "anomaly_score": [6.0, 9.0],
                }
            ).to_parquet(path)
            spec = make_catalog_spec(
                path=str(path), id_col="targetid", ra_col="target_ra", dec_col="target_dec", score_col="anomaly_score", z_col=None
            )
            df = mod.load_catalog(spec)
            self.assertListEqual(list(df.columns), ["targetid", "ra", "dec", "score", "z"])
            self.assertTrue(df["z"].isna().all())


class TestReferenceClassRegistry(unittest.TestCase):
    def test_every_class_has_required_fields(self):
        for ref in mod.REFERENCE_CLASSES:
            self.assertTrue(ref.class_id)
            self.assertTrue(ref.name)
            self.assertTrue(ref.citation)
            # vizier_id may be None (little_red_dots), otherwise must be a non-empty string
            if ref.vizier_id is not None:
                self.assertIsInstance(ref.vizier_id, str)
                self.assertTrue(len(ref.vizier_id) > 0)

    def test_class_ids_are_unique(self):
        ids = [r.class_id for r in mod.REFERENCE_CLASSES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_little_red_dots_has_no_catalog_id(self):
        lrd = next(r for r in mod.REFERENCE_CLASSES if r.class_id == "little_red_dots")
        self.assertIsNone(lrd.vizier_id)


class TestFetchReferenceClassNoNetwork(unittest.TestCase):
    def test_no_catalog_id_known_class_short_circuits(self):
        import tempfile

        lrd = next(r for r in mod.REFERENCE_CLASSES if r.class_id == "little_red_dots")
        with tempfile.TemporaryDirectory() as tmp:
            result = mod.fetch_reference_class(lrd, Path(tmp), row_limit=10, timeout_sec=1.0)
        self.assertEqual(result.status, "no_catalog_id_known")
        self.assertEqual(result.n_rows, 0)
        self.assertIsNotNone(result.error)


if __name__ == "__main__":
    unittest.main()
