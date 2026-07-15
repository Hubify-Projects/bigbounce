from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "morphology_validator", HERE / "validate_p4_morphology_join_v1_0_251.py"
)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


def test_axis_ratio_exact_shape_selection_and_clipping() -> None:
    frame = pd.DataFrame({
        "TYPE": ["DEV", "comp", "SER", "EXP", "REX"],
        "FRACDEV": [0.0, 0.0, 0.0, 0.5, 0.49],
        "SHAPEDEV_E1": [0.0, 0.6, 2.0, 0.3, 0.8],
        "SHAPEDEV_E2": [0.0, 0.8, 0.0, 0.4, 0.0],
        "SHAPEEXP_E1": [0.9, 0.9, 0.9, 0.9, 0.0],
        "SHAPEEXP_E2": [0.0, 0.0, 0.0, 0.0, 0.0],
    })
    observed = validator.derive_axis_ratio(frame)
    chosen_e = np.array([0.0, 0.999, 0.999, 0.5, 0.0])
    np.testing.assert_allclose(observed, (1 - chosen_e) / (1 + chosen_e))


def test_verify_file_rejects_bytes_before_digest(tmp_path: Path, monkeypatch) -> None:
    artifact = tmp_path / "artifact"
    artifact.write_bytes(b"wrong")
    monkeypatch.setattr(validator, "sha256_file", lambda _: pytest.fail("must not hash"))
    with pytest.raises(validator.JoinContractError, match="byte-count mismatch"):
        validator.verify_file(artifact, {"bytes": 6, "sha256": "unused"})


def test_download_missing_uses_immutable_revision(tmp_path: Path, monkeypatch) -> None:
    source = tmp_path / "cache" / "artifact"
    source.parent.mkdir()
    source.write_bytes(b"pinned")
    calls = []

    def fake_download(**kwargs):
        calls.append(kwargs)
        return str(source)

    import sys
    import types
    monkeypatch.setitem(sys.modules, "huggingface_hub", types.SimpleNamespace(hf_hub_download=fake_download))
    target = tmp_path / "local" / "artifact"
    validator.download_missing_file(target, remote_path="remote/path", revision="a" * 40)
    assert target.read_bytes() == b"pinned"
    assert calls == [{
        "repo_id": validator.REPO_ID,
        "filename": "remote/path",
        "repo_type": "dataset",
        "revision": "a" * 40,
    }]


def test_download_missing_never_replaces_existing(tmp_path: Path, monkeypatch) -> None:
    target = tmp_path / "artifact"
    target.write_bytes(b"existing")
    import sys
    import types
    monkeypatch.setitem(
        sys.modules,
        "huggingface_hub",
        types.SimpleNamespace(hf_hub_download=lambda **_: pytest.fail("must not download")),
    )
    validator.download_missing_file(target, remote_path="remote/path", revision="b" * 40)
    assert target.read_bytes() == b"existing"


def test_ensure_inputs_rejects_mutable_or_wrong_manifest_source(tmp_path: Path) -> None:
    manifest = {
        "inputs": {
            "safe_catalog": {
                "bytes": 0,
                "sha256": "0" * 64,
                "huggingface": {
                    "repo_id": validator.REPO_ID,
                    "repo_type": "dataset",
                    "revision": "main",
                    "path": validator.SAFE_REMOTE_PATH,
                },
            },
            "morphology_sidecar": {
                "bytes": 0,
                "sha256": "0" * 64,
                "huggingface": {
                    "repo_id": validator.REPO_ID,
                    "repo_type": "dataset",
                    "revision": validator.MORPHOLOGY_REVISION,
                    "path": validator.MORPHOLOGY_REMOTE_PATH,
                },
            },
        }
    }
    with pytest.raises(validator.JoinContractError, match="immutable Hugging Face"):
        validator.ensure_inputs(
            tmp_path / "safe", tmp_path / "morph", manifest, download_missing=False
        )
