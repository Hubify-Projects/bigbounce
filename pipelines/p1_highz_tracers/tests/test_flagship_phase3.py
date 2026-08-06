"""Offline unit tests for the AUG-011 anomaly-flagship phase-3 tooling.

No network access; no full-scale DESI download; no coadd files. Covers only
the pure, locally-computable pieces of `pipelines/p1_highz_tracers/clean_rerun/`
`build_flagship_sample.py`, `crossmatch_flagship.py`, and
`taxonomy_flagship.py`:

  - `build_flagship_sample.py`'s describe-mode score distribution (quantiles
    + candidate-threshold counts) against a hand-verifiable synthetic
    shard/receipt/summary fixture built through the REAL
    `clean_rerun_contract.py` (`build_contract`, `record_receipt`,
    `summarize_after_dedup` are invoked exactly as production would);
  - selection-mode manifest completeness and exact threshold/filter
    application;
  - fail-closed behavior when `summary.json`'s `contract_sha256` does not
    match the contract, and when a shard is tampered after its receipt was
    recorded (`verify-receipts` must catch it);
  - `crossmatch_flagship.py`'s zcatalog coordinate-join logic against a
    synthetic zcatalog-like FITS table, and its own SHA-256 fail-closed
    checks;
  - `taxonomy_flagship.py`'s pure labeling/merge logic (score-tier cutpoints,
    descriptor-identity family merge) and its fail-closed SHA-256 check.
    Clustering itself (`cluster_features`, which needs `umap-learn`) is not
    exercised here — it is guarded by an explicit ImportError with an
    install hint, consistent with this repo's other optional-dependency
    guards (torch/astropy/pyarrow).
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
CLEAN_RERUN_DIR = ROOT / "pipelines/p1_highz_tracers/clean_rerun"
sys.path.insert(0, str(CLEAN_RERUN_DIR))

CONTRACT_MODULE_PATH = ROOT / "pipelines/p1_highz_tracers/clean_rerun_contract.py"
MODEL_PATH = ROOT / "best_model_47k.pt"
INFERENCE_CODE_PATH = ROOT / "pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py"


def _load_contract_module():
    spec = importlib.util.spec_from_file_location("clean_rerun_contract_under_test", CONTRACT_MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require_pyarrow_astropy_torch(test_case: unittest.TestCase):
    try:
        import pyarrow  # noqa: F401
        import pyarrow.parquet  # noqa: F401
    except ImportError as exc:  # pragma: no cover - environment prerequisite
        test_case.skipTest(f"pyarrow unavailable: {exc}")
    try:
        import torch  # noqa: F401
    except ImportError as exc:  # pragma: no cover - environment prerequisite
        test_case.skipTest(f"torch unavailable: {exc}")
    if not MODEL_PATH.is_file():
        test_case.skipTest(f"archived model checkpoint absent: {MODEL_PATH}")


def _build_fixture(work: Path):
    """Build a real contract + two scored shards + a real summarize-after-dedup
    summary, exactly the way the pod pipeline would, so the phase-3 tools are
    tested against genuine `clean_rerun_contract.py` provenance artifacts.
    """
    import pyarrow as pa
    import pyarrow.parquet as pq

    contract_tool = _load_contract_module()

    digest = "a" * 64
    input_manifest = {
        "manifest_version": "desi-dr1-clean-rerun-input/v1",
        "source_revision": "iron",
        "catalog_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits",
        "catalog_checksum_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum",
        "catalog_sha256": digest,
        "targetid_column": "TARGETID",
        "spectrum_locator": {"type": "desi_dr1_iron_healpix", "base_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/"},
        "locator_inventory_sha256": "b" * 64,
    }
    calibration = {
        "artifact_version": "desi-bigae-calibration/v1",
        "status": "sealed",
        "score_definition": "mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins",
        "fit_scope": "held_out_training_validation_split",
        "mse_mean": 0.1,
        "mse_std": 0.02,
        "selection_threshold": 5.0,
        "training_manifest_sha256": "c" * 64,
        "validation_manifest_sha256": "d" * 64,
        "fit_code_sha256": "e" * 64,
    }
    input_path, calibration_path = work / "input.json", work / "calibration.json"
    input_path.write_text(json.dumps(input_manifest))
    calibration_path.write_text(json.dumps(calibration))

    contract = contract_tool.build_contract(MODEL_PATH, INFERENCE_CODE_PATH, input_path, calibration_path)
    contract_path = work / "contract.json"
    contract_tool.write_json_atomic(contract_path, contract)

    shard_dir, receipt_dir = work / "shards", work / "receipts"
    shard_dir.mkdir()
    checkpoint = work / "checkpoint.json"

    # part-000: targetid 1,2,3 ; part-001: targetid 3 (overwrites),4,5
    # Deterministic lexical shard-then-row dedup winner set:
    #   1 -> 2.0, 2 -> 6.0, 3 -> 11.0 (part-001 wins), 4 -> 3.5, 5 -> 7.0
    pq.write_table(
        pa.table(
            {
                "targetid": pa.array([1, 2, 3], type=pa.int64()),
                "anomaly_score": pa.array([2.0, 6.0, 9.0], type=pa.float64()),
                "mean_mse": pa.array([0.1, 0.2, 0.3], type=pa.float64()),
                "survey": pa.array(["main", "main", "sv3"], type=pa.string()),
                "program": pa.array(["dark", "dark", "bright"], type=pa.string()),
                "healpix": pa.array([10, 10, 20], type=pa.int64()),
            }
        ),
        shard_dir / "part-000.parquet",
    )
    pq.write_table(
        pa.table(
            {
                "targetid": pa.array([3, 4, 5], type=pa.int64()),
                "anomaly_score": pa.array([11.0, 3.5, 7.0], type=pa.float64()),
                "mean_mse": pa.array([0.4, 0.5, 0.6], type=pa.float64()),
                "survey": pa.array(["sv3", "main", "main"], type=pa.string()),
                "program": pa.array(["bright", "dark", "dark"], type=pa.string()),
                "healpix": pa.array([20, 30, 30], type=pa.int64()),
            }
        ),
        shard_dir / "part-001.parquet",
    )
    for shard in sorted(shard_dir.glob("*.parquet")):
        contract_tool.record_receipt(contract_path, shard, receipt_dir, checkpoint)

    summary_path = work / "summary.json"
    contract_tool.summarize_after_dedup(contract_path, shard_dir, receipt_dir, work / "dedup.sqlite", summary_path)

    return contract_tool, contract_path, shard_dir, receipt_dir, summary_path


class BuildFlagshipSampleTest(unittest.TestCase):
    def setUp(self) -> None:
        _require_pyarrow_astropy_torch(self)
        import build_flagship_sample  # noqa: F401

        self.mod = sys.modules["build_flagship_sample"]

    def test_describe_mode_quantiles_and_threshold_counts_correct(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            contract_tool, contract_path, shard_dir, receipt_dir, summary_path = _build_fixture(work)

            report = self.mod.describe_distribution(contract_tool, contract_path, shard_dir, receipt_dir, summary_path)

            expected_scores = np.array([2.0, 6.0, 11.0, 3.5, 7.0])  # post-dedup winners
            self.assertEqual(report["raw_rows"], 6)
            self.assertEqual(report["unique_targetids"], 5)
            self.assertAlmostEqual(report["quantiles"]["q50"], float(np.quantile(expected_scores, 0.50)))
            self.assertAlmostEqual(report["quantiles"]["q00"], float(expected_scores.min()))
            self.assertAlmostEqual(report["quantiles"]["q100"], float(expected_scores.max()))
            for threshold in (3.0, 4.0, 5.0, 6.0, 8.0, 10.0):
                expected_count = int((expected_scores >= threshold).sum())
                key = f"sigma_{threshold:g}"
                self.assertEqual(report["counts_above_threshold"][key]["count"], expected_count)
                self.assertAlmostEqual(
                    report["counts_above_threshold"][key]["fraction_of_unique"], expected_count / 5
                )

    def test_selection_manifest_complete_and_threshold_applied_exactly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            contract_tool, contract_path, shard_dir, receipt_dir, summary_path = _build_fixture(work)

            output_sample = work / "flagship_sample.parquet"
            output_manifest = work / "flagship_sample_manifest.json"
            manifest = self.mod.build_sample(
                contract_tool, contract_path, shard_dir, receipt_dir, summary_path,
                score_threshold=5.0, output_sample=output_sample, output_manifest=output_manifest,
            )

            # Post-dedup: {1:2.0, 2:6.0, 3:11.0, 4:3.5, 5:7.0}; score>=5.0 -> {2,3,5}
            self.assertEqual(manifest["row_count"], 3)
            self.assertEqual(manifest["rule"]["score_threshold"], 5.0)
            self.assertEqual(manifest["rule"]["operator"], ">=")
            self.assertIn("parent", manifest)
            self.assertEqual(manifest["parent"]["contract_sha256"], contract_tool.payload_sha256(contract_tool.read_json(contract_path)))
            self.assertIn("shard_receipt_binding", manifest)
            self.assertEqual(manifest["shard_receipt_binding"]["shard_count"], 2)
            self.assertEqual(manifest["output"]["sha256"], self.mod.sha256_file(output_sample))

            import pyarrow.parquet as pq

            table = pq.read_table(output_sample).to_pydict()
            self.assertEqual(sorted(table["targetid"]), [2, 3, 5])

    def test_selection_exclude_survey_filter_applied(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            contract_tool, contract_path, shard_dir, receipt_dir, summary_path = _build_fixture(work)

            output_sample = work / "flagship_sample.parquet"
            output_manifest = work / "flagship_sample_manifest.json"
            manifest = self.mod.build_sample(
                contract_tool, contract_path, shard_dir, receipt_dir, summary_path,
                score_threshold=5.0, output_sample=output_sample, output_manifest=output_manifest,
                exclude_survey=["sv3"],
            )
            # {2:6.0 (main), 3:11.0 (sv3, excluded), 5:7.0 (main)} -> {2,5}
            self.assertEqual(manifest["row_count"], 2)
            import pyarrow.parquet as pq

            table = pq.read_table(output_sample).to_pydict()
            self.assertEqual(sorted(table["targetid"]), [2, 5])

    def test_summary_contract_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            contract_tool, contract_path, shard_dir, receipt_dir, summary_path = _build_fixture(work)

            tampered_summary = json.loads(summary_path.read_text())
            tampered_summary["contract_sha256"] = "0" * 64
            tampered_path = work / "tampered_summary.json"
            tampered_path.write_text(json.dumps(tampered_summary))

            with self.assertRaises(self.mod.SampleError):
                self.mod.describe_distribution(contract_tool, contract_path, shard_dir, receipt_dir, tampered_path)

    def test_tampered_shard_fails_closed_via_verify_receipts(self) -> None:
        import pyarrow as pa
        import pyarrow.parquet as pq

        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            contract_tool, contract_path, shard_dir, receipt_dir, summary_path = _build_fixture(work)

            # Rewrite the shard with different (but still schema-valid)
            # scores AFTER its receipt was recorded: this must be caught by
            # verify-receipts' SHA-256 re-hash, not a Parquet parse error.
            shard = shard_dir / "part-000.parquet"
            pq.write_table(
                pa.table(
                    {
                        "targetid": pa.array([1, 2, 3], type=pa.int64()),
                        "anomaly_score": pa.array([99.0, 99.0, 99.0], type=pa.float64()),
                        "mean_mse": pa.array([0.1, 0.2, 0.3], type=pa.float64()),
                        "survey": pa.array(["main", "main", "sv3"], type=pa.string()),
                        "program": pa.array(["dark", "dark", "bright"], type=pa.string()),
                        "healpix": pa.array([10, 10, 20], type=pa.int64()),
                    }
                ),
                shard,
            )

            with self.assertRaises(contract_tool.ContractError):
                self.mod.describe_distribution(contract_tool, contract_path, shard_dir, receipt_dir, summary_path)


class CrossmatchFlagshipTest(unittest.TestCase):
    def setUp(self) -> None:
        try:
            from astropy.io import fits  # noqa: F401
        except ImportError as exc:  # pragma: no cover - environment prerequisite
            self.skipTest(f"astropy unavailable: {exc}")
        import crossmatch_flagship  # noqa: F401

        self.mod = sys.modules["crossmatch_flagship"]

    def _write_synthetic_zcatalog(self, path: Path) -> None:
        from astropy.io import fits

        targetid = np.array([1, 2, 3, 4, 5], dtype=np.int64)
        ra = np.array([10.0, 20.0, 30.0, 40.0, 50.0], dtype=np.float64)
        dec = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
        columns = [
            fits.Column(name="TARGETID", format="K", array=targetid),
            fits.Column(name="TARGET_RA", format="D", array=ra),
            fits.Column(name="TARGET_DEC", format="D", array=dec),
        ]
        hdu = fits.BinTableHDU.from_columns(columns)
        fits.HDUList([fits.PrimaryHDU(), hdu]).writeto(path, overwrite=True)

    def test_coordinate_join_memory_bounded_chunked_streaming(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            zcatalog_path = work / "zall-pix-iron-synthetic.fits"
            self._write_synthetic_zcatalog(zcatalog_path)

            # chunk_rows smaller than the table forces multi-chunk streaming.
            coordinates = self.mod.read_coordinates_for_targetids(zcatalog_path, {1, 3, 5}, chunk_rows=2)

            self.assertEqual(set(coordinates.keys()), {1, 3, 5})
            self.assertEqual(coordinates[1], (10.0, 1.0))
            self.assertEqual(coordinates[3], (30.0, 3.0))
            self.assertEqual(coordinates[5], (50.0, 5.0))
            # Targetids not requested must never appear, even though present.
            self.assertNotIn(2, coordinates)
            self.assertNotIn(4, coordinates)

    def test_join_sample_with_coordinates_success_and_fail_closed(self) -> None:
        sample_rows = [
            {"targetid": 1, "anomaly_score": 5.0, "survey": "main", "program": "dark", "healpix": 10},
            {"targetid": 3, "anomaly_score": 9.0, "survey": "sv3", "program": "bright", "healpix": 20},
        ]
        coordinates = {1: (10.0, 1.0), 3: (30.0, 3.0)}
        joined = self.mod.join_sample_with_coordinates(sample_rows, coordinates)
        self.assertEqual(joined[0]["ra"], 10.0)
        self.assertEqual(joined[1]["dec"], 3.0)

        missing_coordinates = {1: (10.0, 1.0)}  # targetid 3 unresolved
        with self.assertRaises(self.mod.CrossmatchError):
            self.mod.join_sample_with_coordinates(sample_rows, missing_coordinates)

    def test_verify_zcatalog_and_sample_sha_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            zcatalog_path = work / "zall-pix-iron-synthetic.fits"
            self._write_synthetic_zcatalog(zcatalog_path)

            real_sha = self.mod.sha256_file(zcatalog_path)
            manifest_ok = {"parent": {"catalog_sha256": real_sha}}
            self.mod.verify_zcatalog_for_sample(zcatalog_path, manifest_ok)  # must not raise

            manifest_bad = {"parent": {"catalog_sha256": "0" * 64}}
            with self.assertRaises(self.mod.CrossmatchError):
                self.mod.verify_zcatalog_for_sample(zcatalog_path, manifest_bad)

            sample_path = work / "sample.parquet"
            sample_path.write_bytes(b"not a real parquet file, just needs a stable sha")
            real_sample_sha = self.mod.sha256_file(sample_path)
            self.mod.verify_input_sample(sample_path, {"output": {"sha256": real_sample_sha}})  # must not raise
            with self.assertRaises(self.mod.CrossmatchError):
                self.mod.verify_input_sample(sample_path, {"output": {"sha256": "1" * 64}})


class TaxonomyFlagshipTest(unittest.TestCase):
    def setUp(self) -> None:
        import taxonomy_flagship  # noqa: F401

        self.mod = sys.modules["taxonomy_flagship"]

    def test_score_tier_label_boundaries(self) -> None:
        cutpoints = [3.0, 6.0, 9.0]
        labels = ("low", "elevated", "high", "extreme")
        self.assertEqual(self.mod.score_tier_label(2.0, cutpoints, labels), "low")
        self.assertEqual(self.mod.score_tier_label(3.5, cutpoints, labels), "elevated")
        self.assertEqual(self.mod.score_tier_label(6.5, cutpoints, labels), "high")
        self.assertEqual(self.mod.score_tier_label(9.0, cutpoints, labels), "extreme")
        self.assertEqual(self.mod.score_tier_label(100.0, cutpoints, labels), "extreme")

    def test_characterize_and_merge_families_identical_descriptors_merge(self) -> None:
        targetids = [1, 2, 3, 4, 5, 6]
        labels = np.array([0, 0, 1, 1, 2, 2])
        is_core = np.array([True, True, True, False, True, True])
        metadata = {
            "anomaly_score": [2.0, 2.0, 9.0, 9.0, 2.0, 2.0],
            "survey": ["main", "main", "sv3", "sv3", "main", "main"],
            "program": ["dark", "dark", "bright", "bright", "dark", "dark"],
            "ra": [10.0, 10.1, 50.0, 50.1, 11.0, 11.1],
            "dec": [1.0, 1.1, 5.0, 5.1, 1.2, 1.3],
        }
        clusters = self.mod.characterize_and_label(
            targetids, labels, is_core, metadata,
            score_tier_quantiles=(0.50, 0.80, 0.95),
            score_tier_labels=("low", "elevated", "high", "extreme"),
        )
        self.assertEqual(set(clusters.keys()), {0, 1, 2})
        # Clusters 0 and 2 are identical in every labeling-relevant respect
        # (same score, same survey, same program) so must produce the SAME
        # descriptor even though they came from different HDBSCAN labels.
        self.assertEqual(clusters[0]["family_descriptor"], clusters[2]["family_descriptor"])
        self.assertNotEqual(clusters[0]["family_descriptor"], clusters[1]["family_descriptor"])

        family_info, cluster_to_family = self.mod.merge_families(clusters)
        self.assertEqual(len(family_info), 2)
        self.assertEqual(cluster_to_family[0], cluster_to_family[2])
        self.assertNotEqual(cluster_to_family[0], cluster_to_family[1])
        sizes = sorted(info["n_objects"] for info in family_info.values())
        self.assertEqual(sizes, [2, 4])

    def test_build_taxonomy_fails_closed_on_unmatched_sha_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            unmatched_path = work / "unmatched.parquet"
            unmatched_path.write_bytes(b"not a real parquet file, just needs a stable sha")

            crossmatch_manifest_path = work / "crossmatch_manifest.json"
            crossmatch_manifest_path.write_text(json.dumps({"unmatched_output": {"sha256": "0" * 64}}))

            with self.assertRaises(self.mod.TaxonomyError):
                self.mod.build_taxonomy(
                    unmatched_path, crossmatch_manifest_path,
                    work / "results.json", work / "manifest.json",
                )


if __name__ == "__main__":
    unittest.main()
