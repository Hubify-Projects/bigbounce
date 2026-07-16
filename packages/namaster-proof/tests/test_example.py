from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


def test_synthetic_example_is_independent_and_reproducible(tmp_path: Path) -> None:
    example = Path(__file__).resolve().parents[1] / "examples/synthetic_window.py"
    spec = importlib.util.spec_from_file_location("synthetic_window", example)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = tmp_path / "result.json"
    result = module.run(output, 0.25)
    assert result["recovered_beta_deg"] == pytest.approx(0.25)
    assert result["equivalence_error"] < 1e-14
    assert output.is_file()
    assert output.with_name(output.name + ".receipt.json").is_file()
