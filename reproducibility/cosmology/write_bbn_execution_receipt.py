#!/usr/bin/env python3
"""Execute and retain the exact CAMB 1.6.5 BBN provenance contract for P1B."""

from __future__ import annotations

import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import camb
import camb.bbn
import numpy
import scipy
import yaml

import test_bbn_provenance


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "frozen" / "bbn_execution_receipt.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    test_bbn_provenance.main()
    table_name = test_bbn_provenance.TABLE
    table_path = Path(camb.__file__).resolve().parent / table_name
    configs: list[dict[str, str]] = []
    for name in test_bbn_provenance.YAMLS:
        path = ROOT / name
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        configured = payload["theory"]["camb"]["extra_args"]["bbn_predictor"]
        if configured != table_name:
            raise ValueError(f"{name} does not configure {table_name}")
        configs.append(
            {
                "path": path.relative_to(ROOT.parents[1]).as_posix(),
                "sha256": sha256(path),
                "bbn_predictor": configured,
            }
        )

    receipt = {
        "schema": "bigbounce.p1b-bbn-execution-receipt/v1",
        "status": "PASS",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "camb_version": camb.__version__,
        "numpy_version": numpy.__version__,
        "scipy_version": scipy.__version__,
        "predictor_class": type(camb.bbn.get_predictor()).__name__,
        "executed_table": table_name,
        "executed_table_sha256": sha256(table_path),
        "public_yaml_setting": table_name,
        "validated_configs": configs,
        "validation_script": {
            "path": "reproducibility/cosmology/test_bbn_provenance.py",
            "sha256": sha256(ROOT / "test_bbn_provenance.py"),
        },
        "command": (
            "python reproducibility/cosmology/write_bbn_execution_receipt.py"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS wrote {OUTPUT.relative_to(ROOT.parents[1])}")


if __name__ == "__main__":
    main()
