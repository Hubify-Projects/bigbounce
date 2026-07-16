#!/usr/bin/env python3
"""Build P4 v1.0.259's strict-primary public release-contract overlay."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from reproduce_p4_primary_null_v1_0_259 import reproduce

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEFAULT_OUT = HERE / "apjs_release_v1.0.259_strict"
BASE_CATALOG = HERE / "apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
STRICT_NULL = (
    HERE / "outputs/canonical_provenance/"
    "p4_primary_hc_safe_label_shuffle_10k_v1_0_257.npy"
)
REPRODUCER = HERE / "reproduce_p4_primary_null_v1_0_259.py"
BASE = {
    "repo_id": "bamfai/galaxy-chirality-catalog",
    "revision": "db11023306ab4eed1d7727670bd78e127b7af17a",
    "path": "apjs-release/v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet",
    "bytes": 386_712_994,
    "sha256": "139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def record(path: Path) -> dict:
    return {
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def build(output: Path) -> dict:
    if output.exists():
        raise RuntimeError(f"refusing to overwrite existing release: {output}")
    if BASE_CATALOG.stat().st_size != BASE["bytes"] or sha256_file(BASE_CATALOG) != BASE["sha256"]:
        raise RuntimeError("base immutable catalog identity mismatch")
    output.mkdir(parents=True)
    null_target = output / "primary_strict_fixed_occupancy_amps_10000.npy"
    repro_target = output / REPRODUCER.name
    shutil.copy2(STRICT_NULL, null_target)
    shutil.copy2(REPRODUCER, repro_target)
    reproduction = reproduce(BASE_CATALOG, null_target)
    (output / "PRIMARY_REPRODUCTION.json").write_text(
        json.dumps(reproduction, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    schema = {
        "schema": "p4-apjs-strict-primary-release/v1",
        "paper": "P4",
        "paper_version": "v1.0.259",
        "primary_selection": "primary_hc == true and raw_flip_qc_unsafe == false",
        "base_catalog": BASE,
        "strict_primary": {
            "n_selected": 890_069,
            "n_support": 887_472,
            "n_pixels": 23_633,
            "null_type": "fixed-occupancy multivariate-hypergeometric galaxy-label randomization",
            "n_draws": 10_000,
            "seed": 20_260_715,
            "z_moment": 0.6346508534484177,
            "rank_p_one_sided_upper_tail": 0.23767623237676233,
        },
        "supersedes_primary_contract": {
            "release": "apjs-release/v1.0.244",
            "reason": (
                "The catalog bytes remain authoritative, but the prior release's "
                "named primary filter and retained null included quarantined rows."
            ),
        },
        "release_gates": {
            "immutable_provider_revision": "OPEN until provider receipt is published",
            "doi_archive": "OPEN",
            "human_apjs_review": "OPEN",
        },
    }
    (output / "SCHEMA.json").write_text(
        json.dumps(schema, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    readme = """# P4 strict-primary release overlay — v1.0.259

This overlay changes the **primary analysis contract**, not the 8,474,531-row
catalog bytes. It consumes the immutable catalog identified in `SCHEMA.json`
and requires:

```text
primary_hc == true and raw_flip_qc_unsafe == false
```

The retained 10,000-draw array uses fixed-occupancy galaxy-label randomization
on that exact strict selection. The result is `z_moment=+0.6346508534` and
one-sided add-one rank `p=0.2376762324`.

The unsafe predicate was finalized during post-review corrective work after the
earlier result had been inspected. This is not represented as preregistered or
blinded. The result is an observed-label descriptive isotropy null, not a
physical or primordial amplitude bound.
"""
    (output / "README.md").write_text(readme, encoding="utf-8")
    products = {
        path.stem.lower(): record(path)
        for path in (
            null_target,
            repro_target,
            output / "PRIMARY_REPRODUCTION.json",
            output / "SCHEMA.json",
            output / "README.md",
        )
    }
    manifest = {
        "schema": "p4-apjs-strict-primary-manifest/v1",
        "paper": "P4",
        "paper_version": "v1.0.259",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "release_gate": "LOCAL_RELEASE_CANDIDATE_ONLY; provider revision and DOI open",
        "base_catalog": BASE,
        "products": products,
        "primary_reproduction": reproduction,
    }
    (output / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    checksums = [
        f"{sha256_file(path)}  {path.name}"
        for path in sorted(output.iterdir())
        if path.name != "SHA256SUMS"
    ]
    (output / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    try:
        result = build(args.output)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
