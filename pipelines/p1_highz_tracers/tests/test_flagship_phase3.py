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
  - `enrich_flagship_sample.py` (phase-3b): a synthetic coadd FITS is scored
    through the REAL archived `process_healpix()` (imported unmodified, run
    against the real archived `best_model_47k.pt` on CPU — no synthetic
    model) to build both the "ground truth" sample `mean_mse` values and
    the enriched output, with only `download_file` monkeypatched (on the
    freshly-loaded, otherwise-untouched archived module instance) to copy a
    local fixture file instead of hitting the network. Covers: the enriched
    output keeps ONLY the selected sample's targetids even when the coadd
    has more spectra than the sample; `latent_000..latent_127` are present
    and `lat_000` is not; the MSE cross-check gate passes on genuine
    recomputed values and fails closed (raising, with every offender listed
    in the audit log) when a sample `mean_mse` is tampered; and checkpoint
    resume skips an already-completed group's coadd re-download while a
    still-failing group keeps the run in `status: incomplete` with no final
    output written, until a later incarnation with the missing source
    available completes it.
  - `wise_join_flagship.py` (phase-3c): pure nearest-match selection over
    synthetic multi-candidate AllWISE cone-search results; unmatched
    handling (no candidate within radius, or a candidate missing one band);
    an end-to-end run with the network-calling `query_wise_cone` replaced by
    a canned stub (never real astroquery/network); manifest completeness
    (service/catalog/query-param/SHA/count fields all present and correct);
    checkpoint resume across two incarnations; and the input-SHA256
    fail-closed check.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

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


class EnrichFlagshipSampleTest(unittest.TestCase):
    """Phase-3b: per-band SNR + latent enrichment of the SELECTED sample only,
    with the recomputed-vs-shard MSE cross-check gate. Uses the real archived
    `process_healpix()`/`BigAE`/`best_model_47k.pt` throughout; the only
    stand-in is a monkeypatched `download_file` (copies a local synthetic
    coadd FITS instead of hitting the network) on a freshly-loaded module
    instance — the archived FILE itself is never copied or modified.
    """

    # Real DESI per-arm downsample-bin counts (172+145+179 = 496), so the
    # synthetic coadd's downsampled width matches BigAE(n_in=496) exactly,
    # exercising the SAME downsample()/normalization path as production.
    N_B, N_R, N_Z = 172, 145, 179
    DOWNSAMPLE_FACTOR = 16

    def setUp(self) -> None:
        _require_pyarrow_astropy_torch(self)
        import enrich_flagship_sample  # noqa: F401

        self.mod = sys.modules["enrich_flagship_sample"]

    def _write_synthetic_coadd(self, path: Path, targetids: list[int], seed: int) -> None:
        from astropy.io import fits

        rng = np.random.default_rng(seed)
        n_obj = len(targetids)
        b_flux = rng.normal(loc=5.0, scale=2.0, size=(n_obj, self.N_B * self.DOWNSAMPLE_FACTOR)).astype(np.float32)
        r_flux = rng.normal(loc=5.0, scale=2.0, size=(n_obj, self.N_R * self.DOWNSAMPLE_FACTOR)).astype(np.float32)
        z_flux = rng.normal(loc=5.0, scale=2.0, size=(n_obj, self.N_Z * self.DOWNSAMPLE_FACTOR)).astype(np.float32)

        # COADD_NUMEXP must be present: the archived (contract-frozen, never
        # modified) `process_healpix` does `int(coadd_numexp_f[j])`
        # unconditionally, which raises on the NaN default `safe_col_array`
        # returns for an absent column — a real DESI coadd always has it.
        fibermap = fits.BinTableHDU.from_columns(
            [
                fits.Column(name="TARGETID", format="K", array=np.array(targetids, dtype=np.int64)),
                fits.Column(name="COADD_NUMEXP", format="J", array=np.ones(n_obj, dtype=np.int32)),
            ],
            name="FIBERMAP",
        )
        hdul = fits.HDUList(
            [
                fits.PrimaryHDU(),
                fits.ImageHDU(data=b_flux, name="B_FLUX"),
                fits.ImageHDU(data=r_flux, name="R_FLUX"),
                fits.ImageHDU(data=z_flux, name="Z_FLUX"),
                fibermap,
            ]
        )
        hdul.writeto(path, overwrite=True)

    def _install_fake_download(self, inference_module, coadd_sources: dict[str, Path]) -> None:
        import shutil

        def _fake_download_file(url, dest, retries=3, timeout=60):
            source = coadd_sources.get(Path(url).name)
            if source is None or not Path(source).is_file():
                return False
            shutil.copy(source, dest)
            return True

        inference_module.download_file = _fake_download_file

    def _score_ground_truth(self, inference_module, model, device, coadd_path: Path) -> dict[int, float]:
        _n_obj, rows = inference_module.process_healpix(str(coadd_path), None, model, device)
        return {int(r["targetid"]): float(r["anomaly_score"]) for r in rows}

    def _build_fixture(self, work: Path):
        """Real contract (real model/inference-code SHA bindings) + a real
        selected-sample Parquet/manifest whose `mean_mse` values are the
        actual archived `process_healpix()` output for two synthetic coadd
        groups, exactly the way `run_scan.py` + `build_flagship_sample.py`
        would have produced them."""
        import torch
        import pyarrow as pa
        import pyarrow.parquet as pq

        contract_tool = _load_contract_module()

        zcatalog_path = work / "zcatalog.fits"
        zcatalog_path.write_bytes(b"synthetic zcatalog bytes; only its sha256 is ever checked")
        catalog_sha256 = self.mod.sha256_file(zcatalog_path)

        input_manifest = {
            "manifest_version": "desi-dr1-clean-rerun-input/v1",
            "source_revision": "iron",
            "catalog_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits",
            "catalog_checksum_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum",
            "catalog_sha256": catalog_sha256,
            "targetid_column": "TARGETID",
            "spectrum_locator": {
                "type": "desi_dr1_iron_healpix",
                "base_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/",
            },
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
        contract_sha256 = contract_tool.payload_sha256(contract)

        # Real archived module + real archived model, CPU, eval mode — the
        # SAME path run_enrichment will use, so "ground truth" scores here
        # are bit-identical to what enrichment recomputes.
        inference_module = self.mod.load_archived_inference_module()
        device = torch.device("cpu")
        model = self.mod.load_model(inference_module, MODEL_PATH, device)

        group_a = ("main", "dark", 100)
        group_a_targetids = [11, 12, 13, 14]
        group_b = ("sv3", "bright", 55)
        group_b_targetids = [21, 22]

        coadd_dir = work / "coadd_sources"
        coadd_dir.mkdir()
        coadd_paths = {}
        for group, targetids, seed in ((group_a, group_a_targetids, 101), (group_b, group_b_targetids, 202)):
            survey, program, healpix = group
            relative = self.mod.coadd_relative_path(survey, program, healpix)
            fname = Path(relative).name
            coadd_path = coadd_dir / fname
            self._write_synthetic_coadd(coadd_path, targetids, seed=seed)
            coadd_paths[fname] = coadd_path

        ground_truth = {}
        for fname, coadd_path in coadd_paths.items():
            ground_truth.update(self._score_ground_truth(inference_module, model, device, coadd_path))

        # SELECT only a subset of each coadd's targetids into the sample —
        # exercises "keeps ONLY the sample's targetids" against real coadd
        # surplus (12, 14, 22 exist in the coadds but never in the sample).
        selected = {
            11: group_a,
            13: group_a,
            21: group_b,
        }
        sample_rows = []
        for targetid, (survey, program, healpix) in selected.items():
            sample_rows.append(
                {
                    "targetid": targetid,
                    "anomaly_score": 6.5 + targetid * 0.01,  # sealed z-score stand-in; never touched by enrichment
                    "mean_mse": ground_truth[targetid],
                    "survey": survey,
                    "program": program,
                    "healpix": healpix,
                }
            )

        sample_path = work / "flagship_sample.parquet"
        table = pa.table(
            {
                "targetid": pa.array([r["targetid"] for r in sample_rows], type=pa.int64()),
                "anomaly_score": pa.array([r["anomaly_score"] for r in sample_rows], type=pa.float64()),
                "mean_mse": pa.array([r["mean_mse"] for r in sample_rows], type=pa.float64()),
                "survey": pa.array([r["survey"] for r in sample_rows], type=pa.string()),
                "program": pa.array([r["program"] for r in sample_rows], type=pa.string()),
                "healpix": pa.array([r["healpix"] for r in sample_rows], type=pa.int64()),
            }
        )
        pq.write_table(table, sample_path, compression="zstd")

        sample_manifest = {
            "manifest_version": "flagship-sample/v1",
            "row_count": len(sample_rows),
            "parent": {"contract_sha256": contract_sha256, "catalog_sha256": catalog_sha256},
            "output": {"file_name": sample_path.name, "sha256": self.mod.sha256_file(sample_path)},
        }
        sample_manifest_path = work / "flagship_sample_manifest.json"
        sample_manifest_path.write_text(json.dumps(sample_manifest))

        return {
            "contract_path": contract_path,
            "sample_path": sample_path,
            "sample_manifest_path": sample_manifest_path,
            "zcatalog_path": zcatalog_path,
            "inference_module": inference_module,
            "coadd_paths": coadd_paths,
            "selected": selected,
            "ground_truth": ground_truth,
        }

    def _run_paths(self, work: Path):
        return dict(
            coadd_cache_dir=work / "coadd_cache",
            shard_dir=work / "shards",
            checkpoint_path=work / "checkpoint.json",
            audit_log_path=work / "audit.jsonl",
            output_path=work / "enriched.parquet",
            manifest_output_path=work / "enriched_manifest.json",
        )

    def test_enrichment_keeps_only_sample_ids_and_mse_cross_check_passes(self) -> None:
        import pyarrow.parquet as pq

        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            fixture = self._build_fixture(work)
            paths = self._run_paths(work)
            self._install_fake_download(fixture["inference_module"], fixture["coadd_paths"])

            manifest = self.mod.run_enrichment(
                fixture["sample_path"],
                fixture["sample_manifest_path"],
                fixture["contract_path"],
                MODEL_PATH,
                fixture["zcatalog_path"],
                paths["coadd_cache_dir"],
                paths["shard_dir"],
                paths["checkpoint_path"],
                paths["audit_log_path"],
                paths["output_path"],
                paths["manifest_output_path"],
                inference_module=fixture["inference_module"],
            )

            self.assertEqual(manifest["mse_cross_check"]["offenders"], 0)
            self.assertTrue(manifest["mse_cross_check"]["passed"])
            self.assertEqual(manifest["row_counts"]["input_sample_rows"], 3)
            self.assertEqual(manifest["row_counts"]["output_rows"], 3)
            self.assertEqual(manifest["groups"]["skipped"], 0)
            self.assertTrue(paths["output_path"].is_file())
            self.assertEqual(manifest["output"]["sha256"], self.mod.sha256_file(paths["output_path"]))

            table = pq.read_table(paths["output_path"]).to_pydict()
            self.assertEqual(sorted(table["targetid"]), [11, 13, 21])
            # Coadd surplus never in the sample must never leak into output.
            self.assertNotIn(12, table["targetid"])
            self.assertNotIn(14, table["targetid"])
            self.assertNotIn(22, table["targetid"])

            columns = set(table.keys())
            self.assertIn("latent_000", columns)
            self.assertIn("latent_127", columns)
            self.assertNotIn("lat_000", columns)
            self.assertIn("rB", columns)
            self.assertIn("rR", columns)
            self.assertIn("rZ", columns)
            self.assertIn("worst_band", columns)
            self.assertIn("peak_residual_wavelength", columns)
            self.assertIn("residual_kurtosis", columns)
            self.assertIn("median_coadd_snr_b", columns)
            self.assertIn("median_coadd_snr_r", columns)
            self.assertIn("median_coadd_snr_z", columns)
            self.assertIn("spectype", columns)
            self.assertIn("z", columns)
            # Sample's own columns survive untouched, including the SEALED
            # anomaly_score (never overwritten by the raw recomputed MSE).
            self.assertIn("mean_mse", columns)
            self.assertIn("anomaly_score", columns)
            for i, targetid in enumerate(table["targetid"]):
                self.assertAlmostEqual(
                    table["anomaly_score"][i], 6.5 + targetid * 0.01, places=9
                )
            self.assertNotIn("_mse_relative_error", columns)
            self.assertNotIn("_recomputed_mean_mse", columns)

    def test_mismatched_sample_mean_mse_fails_closed(self) -> None:
        import pyarrow as pa
        import pyarrow.parquet as pq

        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            fixture = self._build_fixture(work)
            paths = self._run_paths(work)
            self._install_fake_download(fixture["inference_module"], fixture["coadd_paths"])

            # Tamper ONE row's mean_mse after the fixture computed it
            # honestly, then re-seal the sample manifest's own sha256 (as a
            # legitimate producer would) so the ONLY thing under test is the
            # enrichment cross-check catching a silently wrong mean_mse.
            table = pq.read_table(fixture["sample_path"]).to_pydict()
            tampered_index = table["targetid"].index(13)
            table["mean_mse"][tampered_index] += 5.0
            tampered = pa.table(
                {
                    "targetid": pa.array(table["targetid"], type=pa.int64()),
                    "anomaly_score": pa.array(table["anomaly_score"], type=pa.float64()),
                    "mean_mse": pa.array(table["mean_mse"], type=pa.float64()),
                    "survey": pa.array(table["survey"], type=pa.string()),
                    "program": pa.array(table["program"], type=pa.string()),
                    "healpix": pa.array(table["healpix"], type=pa.int64()),
                }
            )
            pq.write_table(tampered, fixture["sample_path"], compression="zstd")
            sample_manifest = json.loads(fixture["sample_manifest_path"].read_text())
            sample_manifest["output"]["sha256"] = self.mod.sha256_file(fixture["sample_path"])
            fixture["sample_manifest_path"].write_text(json.dumps(sample_manifest))

            with self.assertRaises(self.mod.EnrichmentError) as ctx:
                self.mod.run_enrichment(
                    fixture["sample_path"],
                    fixture["sample_manifest_path"],
                    fixture["contract_path"],
                    MODEL_PATH,
                    fixture["zcatalog_path"],
                    paths["coadd_cache_dir"],
                    paths["shard_dir"],
                    paths["checkpoint_path"],
                    paths["audit_log_path"],
                    paths["output_path"],
                    paths["manifest_output_path"],
                    inference_module=fixture["inference_module"],
                )
            self.assertIn("MSE cross-check gate failed", str(ctx.exception))
            self.assertFalse(paths["output_path"].exists())

            audit_lines = [json.loads(line) for line in paths["audit_log_path"].read_text().splitlines()]
            gate_failures = [line for line in audit_lines if line.get("mse_cross_check_gate") == "FAILED"]
            self.assertEqual(len(gate_failures), 1)
            offender_targetids = {o["targetid"] for o in gate_failures[0]["offenders"]}
            self.assertEqual(offender_targetids, {13})

    def test_checkpoint_resume_skips_completed_group_and_retries_failed_one(self) -> None:
        import pyarrow.parquet as pq

        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            fixture = self._build_fixture(work)
            paths = self._run_paths(work)

            group_a_key = ("main", "dark", 100)
            group_b_key = ("sv3", "bright", 55)
            group_a_fname = Path(self.mod.coadd_relative_path(*group_a_key)).name
            group_b_fname = Path(self.mod.coadd_relative_path(*group_b_key)).name

            # First incarnation: only group A's coadd source is reachable —
            # group B must be skipped (download returns False), the run
            # must report status "incomplete", and NO final output/manifest
            # may be written for an incomplete enrichment.
            only_a_sources = {group_a_fname: fixture["coadd_paths"][group_a_fname]}
            self._install_fake_download(fixture["inference_module"], only_a_sources)

            result = self.mod.run_enrichment(
                fixture["sample_path"],
                fixture["sample_manifest_path"],
                fixture["contract_path"],
                MODEL_PATH,
                fixture["zcatalog_path"],
                paths["coadd_cache_dir"],
                paths["shard_dir"],
                paths["checkpoint_path"],
                paths["audit_log_path"],
                paths["output_path"],
                paths["manifest_output_path"],
                inference_module=fixture["inference_module"],
            )
            self.assertEqual(result["status"], "incomplete")
            self.assertEqual(result["skipped_groups"], 1)
            self.assertFalse(paths["output_path"].exists())
            self.assertFalse(paths["manifest_output_path"].exists())

            checkpoint = json.loads(paths["checkpoint_path"].read_text())
            completed_group_keys = {tuple(entry["group"]) for entry in checkpoint["completed_groups"]}
            self.assertEqual(completed_group_keys, {group_a_key})

            # Second incarnation: group A's source is deliberately REMOVED
            # (proves resume never re-downloads a checkpointed group — if it
            # tried, the group-A shard would be missing from the final
            # output because the "download" would fail with no source);
            # group B's source is now available and gets retried.
            only_b_sources = {group_b_fname: fixture["coadd_paths"][group_b_fname]}
            self._install_fake_download(fixture["inference_module"], only_b_sources)

            manifest = self.mod.run_enrichment(
                fixture["sample_path"],
                fixture["sample_manifest_path"],
                fixture["contract_path"],
                MODEL_PATH,
                fixture["zcatalog_path"],
                paths["coadd_cache_dir"],
                paths["shard_dir"],
                paths["checkpoint_path"],
                paths["audit_log_path"],
                paths["output_path"],
                paths["manifest_output_path"],
                inference_module=fixture["inference_module"],
            )
            self.assertEqual(manifest["groups"]["skipped"], 0)
            self.assertEqual(manifest["row_counts"]["output_rows"], 3)
            self.assertTrue(paths["output_path"].is_file())

            table = pq.read_table(paths["output_path"]).to_pydict()
            self.assertEqual(sorted(table["targetid"]), [11, 13, 21])


class WiseJoinFlagshipTest(unittest.TestCase):
    """Phase-3c: AllWISE (`II/328/allwise`) W1/W2 cross-match join over
    `enrich_flagship_sample.py`'s output (which carries `target_ra`/
    `target_dec` straight through from the archived FIBERMAP columns — see
    that module's docstring). The real network-calling `query_wise_cone` is
    never exercised here; every test replaces it with a canned stub, per
    `crossmatch_flagship.py`'s SIMBAD/NED testing precedent.
    """

    def setUp(self) -> None:
        try:
            import pyarrow  # noqa: F401
            import pyarrow.parquet  # noqa: F401
        except ImportError as exc:  # pragma: no cover - environment prerequisite
            self.skipTest(f"pyarrow unavailable: {exc}")
        import wise_join_flagship  # noqa: F401

        self.mod = sys.modules["wise_join_flagship"]

    # ---- pure nearest-match selection (no network, no mocks needed) ----

    def test_select_nearest_match_picks_closest_of_several_candidates(self) -> None:
        ra, dec = 150.0, 10.0
        candidates = [
            {"ra": 150.01, "dec": 10.01, "w1": 15.0, "w2": 14.0, "allwise_id": "far"},
            {"ra": 150.0003, "dec": 10.0002, "w1": 16.5, "w2": 15.2, "allwise_id": "near"},
            {"ra": 149.99, "dec": 9.99, "w1": 14.0, "w2": 13.0, "allwise_id": "farther"},
        ]
        nearest = self.mod.select_nearest_match(candidates, ra, dec)
        self.assertEqual(nearest["allwise_id"], "near")
        self.assertIn("separation_arcsec", nearest)
        self.assertLess(nearest["separation_arcsec"], 3.0)

    def test_select_nearest_match_empty_candidates_returns_none(self) -> None:
        self.assertIsNone(self.mod.select_nearest_match([], 10.0, 20.0))

    # ---- pure result-row construction ----

    def test_build_result_row_matched_computes_color(self) -> None:
        row = self.mod.build_result_row(42, {"found": True, "w1": 15.2, "w2": 14.1, "separation_arcsec": 1.23})
        self.assertEqual(row["targetid"], 42)
        self.assertAlmostEqual(row["w1"], 15.2)
        self.assertAlmostEqual(row["w2"], 14.1)
        self.assertAlmostEqual(row["w1_w2"], 1.1, places=6)
        self.assertAlmostEqual(row["match_separation_arcsec"], 1.23)
        self.assertTrue(row["match_flag"])

    def test_build_result_row_unmatched_is_all_null(self) -> None:
        row = self.mod.build_result_row(7, {"found": False})
        self.assertEqual(row["targetid"], 7)
        self.assertIsNone(row["w1"])
        self.assertIsNone(row["w2"])
        self.assertIsNone(row["w1_w2"])
        self.assertIsNone(row["match_separation_arcsec"])
        self.assertFalse(row["match_flag"])

    def test_build_result_row_partial_band_yields_null_color(self) -> None:
        # AllWISE can carry a null magnitude for one band even on a match.
        row = self.mod.build_result_row(9, {"found": True, "w1": 15.0, "w2": None, "separation_arcsec": 0.5})
        self.assertAlmostEqual(row["w1"], 15.0)
        self.assertIsNone(row["w2"])
        self.assertIsNone(row["w1_w2"])
        self.assertTrue(row["match_flag"])

    # ---- end-to-end with a mocked network-calling function ----

    def _write_enriched_fixture(self, work: Path, rows: list[dict[str, Any]]):
        import pyarrow as pa
        import pyarrow.parquet as pq

        enriched_path = work / "flagship_sample_enriched.parquet"
        table = pa.table(
            {
                "targetid": pa.array([r["targetid"] for r in rows], type=pa.int64()),
                "target_ra": pa.array([r["target_ra"] for r in rows], type=pa.float64()),
                "target_dec": pa.array([r["target_dec"] for r in rows], type=pa.float64()),
                "anomaly_score": pa.array([6.0 + i for i in range(len(rows))], type=pa.float64()),
            }
        )
        pq.write_table(table, enriched_path, compression="zstd")

        manifest_path = work / "flagship_sample_enriched_manifest.json"
        manifest_path.write_text(
            json.dumps(
                {
                    "manifest_version": "flagship-enrichment/v1",
                    "output": {"file_name": enriched_path.name, "sha256": self.mod.sha256_file(enriched_path)},
                }
            )
        )
        return enriched_path, manifest_path

    def test_run_wise_join_end_to_end_matched_multi_candidate_and_unmatched(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            rows = [
                {"targetid": 101, "target_ra": 150.0, "target_dec": 10.0},   # multi-candidate match
                {"targetid": 102, "target_ra": 200.0, "target_dec": -5.0},   # single-candidate match
                {"targetid": 103, "target_ra": 30.0, "target_dec": 60.0},    # no candidate -> unmatched
            ]
            enriched_path, manifest_path = self._write_enriched_fixture(work, rows)

            canned = {
                (150.0, 10.0): [
                    {"ra": 150.01, "dec": 10.01, "w1": 15.0, "w2": 14.0, "allwise_id": "far"},
                    {"ra": 150.0003, "dec": 10.0002, "w1": 16.5, "w2": 15.2, "allwise_id": "near"},
                ],
                (200.0, -5.0): [
                    {"ra": 200.0001, "dec": -4.9999, "w1": 13.4, "w2": 13.0, "allwise_id": "only"},
                ],
                (30.0, 60.0): [],
            }

            def fake_query_fn(ra, dec, radius_arcsec, timeout):
                candidates = canned[(ra, dec)]
                nearest = self.mod.select_nearest_match(candidates, ra, dec)
                if nearest is None:
                    return {"found": False}
                return {"found": True, **nearest}

            output_path = work / "wise_join.parquet"
            manifest_output_path = work / "wise_join_manifest.json"
            manifest = self.mod.run_wise_join(
                enriched_path, manifest_path, work / "checkpoint.json",
                output_path, manifest_output_path,
                rate_limit_sleep=0.0, query_fn=fake_query_fn,
            )

            self.assertEqual(manifest["n_input"], 3)
            self.assertEqual(manifest["n_matched"], 2)
            self.assertEqual(manifest["n_unmatched"], 1)

            import pyarrow.parquet as pq

            table = pq.read_table(output_path).to_pydict()
            by_tid = {tid: i for i, tid in enumerate(table["targetid"])}

            i101 = by_tid[101]
            self.assertTrue(table["match_flag"][i101])
            self.assertAlmostEqual(table["w1"][i101], 16.5)
            self.assertAlmostEqual(table["w2"][i101], 15.2)
            self.assertAlmostEqual(table["w1_w2"][i101], 1.3, places=6)

            i102 = by_tid[102]
            self.assertTrue(table["match_flag"][i102])
            self.assertAlmostEqual(table["w1"][i102], 13.4)

            i103 = by_tid[103]
            self.assertFalse(table["match_flag"][i103])
            self.assertIsNone(table["w1"][i103])
            self.assertIsNone(table["w2"][i103])
            self.assertIsNone(table["w1_w2"][i103])
            self.assertIsNone(table["match_separation_arcsec"][i103])

    def test_manifest_completeness(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            rows = [{"targetid": 1, "target_ra": 10.0, "target_dec": 1.0}]
            enriched_path, manifest_path = self._write_enriched_fixture(work, rows)

            def fake_query_fn(ra, dec, radius_arcsec, timeout):
                return {"found": True, "ra": ra, "dec": dec, "w1": 15.0, "w2": 14.5, "separation_arcsec": 0.2, "allwise_id": "x"}

            output_path = work / "wise_join.parquet"
            manifest_output_path = work / "wise_join_manifest.json"
            manifest = self.mod.run_wise_join(
                enriched_path, manifest_path, work / "checkpoint.json",
                output_path, manifest_output_path,
                radius_arcsec=3.0, timeout=30.0, rate_limit_sleep=0.0,
                checkpoint_every=50, query_fn=fake_query_fn,
            )

            for key in (
                "manifest_version", "started_utc", "finished_utc", "service", "query_params",
                "input_enriched_sha256", "input_enriched_manifest", "n_input", "n_matched",
                "n_unmatched", "output",
            ):
                self.assertIn(key, manifest)

            self.assertEqual(manifest["manifest_version"], "flagship-wise-join/v1")
            self.assertEqual(manifest["service"]["catalog"], "II/328/allwise")
            self.assertEqual(manifest["service"]["client"], "astroquery.vizier.Vizier")
            self.assertEqual(manifest["query_params"]["radius_arcsec"], 3.0)
            self.assertEqual(manifest["query_params"]["timeout_seconds"], 30.0)
            self.assertEqual(manifest["n_input"], 1)
            self.assertEqual(manifest["n_matched"], 1)
            self.assertEqual(manifest["n_unmatched"], 0)
            self.assertEqual(manifest["input_enriched_sha256"], self.mod.sha256_file(enriched_path))
            self.assertEqual(manifest["output"]["sha256"], self.mod.sha256_file(output_path))
            self.assertEqual(manifest["output"]["file_name"], output_path.name)

    def test_checkpoint_resume_across_two_incarnations(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            rows = [
                {"targetid": 1, "target_ra": 10.0, "target_dec": 1.0},
                {"targetid": 2, "target_ra": 20.0, "target_dec": 2.0},
            ]
            enriched_path, manifest_path = self._write_enriched_fixture(work, rows)
            checkpoint_path = work / "checkpoint.json"

            calls: list[int] = []

            def fake_query_fn(ra, dec, radius_arcsec, timeout):
                calls.append(1)
                if ra == 10.0:
                    return {"found": True, "ra": ra, "dec": dec, "w1": 15.0, "w2": 14.0, "separation_arcsec": 0.1, "allwise_id": "a"}
                raise RuntimeError("simulated transient service outage")

            # First incarnation: targetid 1 resolves; targetid 2's query
            # raises. run_wise_join itself does not catch query_fn
            # exceptions (that fault barrier lives inside query_wise_cone,
            # per the SIMBAD/NED precedent) so this incarnation propagates —
            # but targetid 1's result must already be checkpointed.
            with self.assertRaises(RuntimeError):
                self.mod.run_wise_join(
                    enriched_path, manifest_path, checkpoint_path,
                    work / "wise_join.parquet", work / "wise_join_manifest.json",
                    rate_limit_sleep=0.0, checkpoint_every=1, query_fn=fake_query_fn,
                )
            self.assertEqual(len(calls), 2)
            checkpoint = json.loads(checkpoint_path.read_text())
            self.assertIn("1", checkpoint)
            self.assertNotIn("2", checkpoint)

            # Second incarnation: targetid 2 now resolves; targetid 1 must
            # NOT be re-queried (resume skips it via the checkpoint).
            def fake_query_fn_round_two(ra, dec, radius_arcsec, timeout):
                calls.append(1)
                self.assertEqual(ra, 20.0)  # targetid 1 (ra=10.0) never re-queried
                return {"found": True, "ra": ra, "dec": dec, "w1": 13.0, "w2": 12.5, "separation_arcsec": 0.3, "allwise_id": "b"}

            output_path = work / "wise_join.parquet"
            manifest_output_path = work / "wise_join_manifest.json"
            manifest = self.mod.run_wise_join(
                enriched_path, manifest_path, checkpoint_path,
                output_path, manifest_output_path,
                rate_limit_sleep=0.0, query_fn=fake_query_fn_round_two,
            )
            self.assertEqual(manifest["n_matched"], 2)
            self.assertEqual(manifest["n_unmatched"], 0)

            import pyarrow.parquet as pq

            table = pq.read_table(output_path).to_pydict()
            by_tid = dict(zip(table["targetid"], range(len(table["targetid"]))))
            self.assertAlmostEqual(table["w1"][by_tid[1]], 15.0)
            self.assertAlmostEqual(table["w1"][by_tid[2]], 13.0)

    def test_input_sha256_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            rows = [{"targetid": 1, "target_ra": 10.0, "target_dec": 1.0}]
            enriched_path, manifest_path = self._write_enriched_fixture(work, rows)

            tampered_manifest = json.loads(manifest_path.read_text())
            tampered_manifest["output"]["sha256"] = "0" * 64
            tampered_path = work / "tampered_manifest.json"
            tampered_path.write_text(json.dumps(tampered_manifest))

            with self.assertRaises(self.mod.WiseJoinError):
                self.mod.run_wise_join(
                    enriched_path, tampered_path, work / "checkpoint.json",
                    work / "wise_join.parquet", work / "wise_join_manifest.json",
                    rate_limit_sleep=0.0, query_fn=lambda *a, **k: {"found": False},
                )


if __name__ == "__main__":
    unittest.main()
