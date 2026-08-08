from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P4 = ROOT / "pipelines/p2_chirality"


def test_strict_release_reproducer_matches_committed_contract():
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "reproduction.json"
        result = subprocess.run(
            [
                sys.executable,
                str(P4 / "reproduce_p4_primary_null_v1_0_259.py"),
                "--catalog",
                str(P4 / "apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"),
                "--null-array",
                str(
                    P4
                    / "outputs/canonical_provenance/"
                    "p4_primary_hc_safe_label_shuffle_10k_v1_0_257.npy"
                ),
                "--output",
                str(out),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        payload = json.loads(out.read_text())
        assert payload["status"] == "PASS"
        assert payload["n_selected"] == 890_069
        assert payload["n_support"] == 887_472
        assert all(payload["hard_gates"].values())


def test_strict_release_candidate_is_self_consistent():
    release = P4 / "apjs_release_v1.0.259_strict"
    manifest = json.loads((release / "MANIFEST.json").read_text())
    schema = json.loads((release / "SCHEMA.json").read_text())
    reproduction = json.loads((release / "PRIMARY_REPRODUCTION.json").read_text())
    assert manifest["base_catalog"] == schema["base_catalog"]
    assert schema["primary_selection"] == (
        "primary_hc == true and raw_flip_qc_unsafe == false"
    )
    assert reproduction["null"]["array_sha256"] == (
        "3a03ca4b008844fd8bf16be4e1e7e918ceaf580992d9462d54233f417e32ce7d"
    )
    assert "primary_hc == true and raw_flip_qc_unsafe == false" in (
        release / "README.md"
    ).read_text()


def test_strict_release_publisher_dry_run_is_fail_closed():
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/p4_publish_hf_strict_release.py"),
            "--release-dir",
            str(P4 / "apjs_release_v1.0.259_strict"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    receipt = json.loads(result.stdout)
    assert receipt["status"] == "dry-run"
    assert receipt["published"] is False
    assert receipt["path_prefix"] == "apjs-release/v1.0.259-strict-primary"
