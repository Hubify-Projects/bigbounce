#!/usr/bin/env python3
"""Serial/parallel equivalence regression for the canonical NaMaster leg."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().with_name("namaster_500mc.py")


def run(output: Path, workers: int) -> dict:
    env = {
        **os.environ,
        "NAMASTER_SMOKE": "1",
        "NAMASTER_NREAL": "2",
        "NAMASTER_REALIZATION_WORKERS": str(workers),
        "NAMASTER_OUTPUT_DIR": str(output),
        "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "VECLIB_MAXIMUM_THREADS": "1",
    }
    subprocess.run([sys.executable, str(SCRIPT)], check=True, env=env)
    payload = json.loads((output / "summary.json").read_text())
    payload.pop("runtime_seconds")
    payload.pop("execution")
    return payload


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="p1b_canonical_parallel_") as tmp:
        root = Path(tmp)
        serial = run(root / "serial", 1)
        parallel = run(root / "parallel", 2)
        if serial != parallel:
            raise AssertionError("canonical serial and parallel scientific JSON differ")
        print("canonical serial-vs-parallel scientific JSON: IDENTICAL")


if __name__ == "__main__":
    main()
