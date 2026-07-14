#!/usr/bin/env python3
"""Regression for deterministic serial/parallel c10 realization execution."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().with_name("c10_robustness_battery.py")


def scientific_bytes(path: Path) -> bytes:
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload.pop("total_runtime_s")
    for config in payload["configs"]:
        config.pop("runtime_s")
        config.pop("execution")
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def compare(serial: Path, parallel: Path) -> None:
    serial_bytes = scientific_bytes(serial)
    parallel_bytes = scientific_bytes(parallel)
    serial_sha = hashlib.sha256(serial_bytes).hexdigest()
    parallel_sha = hashlib.sha256(parallel_bytes).hexdigest()
    if serial_bytes != parallel_bytes:
        raise AssertionError(
            f"scientific JSON differs: serial={serial_sha}, parallel={parallel_sha}"
        )
    print(f"serial scientific SHA-256:   {serial_sha}")
    print(f"parallel scientific SHA-256: {parallel_sha}")
    print("serial-vs-parallel scientific JSON: BITWISE IDENTICAL")


def run(output: Path, workers: int) -> None:
    env = {
        **os.environ,
        "C10_NREAL": "2",
        "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "MKL_NUM_THREADS": "1",
        "VECLIB_MAXIMUM_THREADS": "1",
    }
    subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--only-config",
            "apod_fwhm_0p5",
            "--output",
            str(output),
            "--force",
            "--realization-workers",
            str(workers),
        ],
        check=True,
        env=env,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--serial-json", type=Path)
    parser.add_argument("--parallel-json", type=Path)
    args = parser.parse_args()
    if (args.serial_json is None) != (args.parallel_json is None):
        parser.error("--serial-json and --parallel-json must be supplied together")
    if args.serial_json is not None:
        compare(args.serial_json, args.parallel_json)
        return
    with tempfile.TemporaryDirectory(prefix="p1b_parallel_regression_") as tmp:
        directory = Path(tmp)
        serial = directory / "serial.json"
        parallel = directory / "parallel.json"
        run(serial, 1)
        run(parallel, 2)
        compare(serial, parallel)


if __name__ == "__main__":
    main()
