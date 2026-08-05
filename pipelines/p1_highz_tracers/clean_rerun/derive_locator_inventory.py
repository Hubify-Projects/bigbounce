#!/usr/bin/env python3
"""Pod-side derivation of the DESI DR1 iron HEALPix coadd locator inventory.

Reads the already-downloaded, SHA-256-verified `zall-pix-iron.fits` zcatalog
and emits a sorted, deterministic JSON-lines inventory of every unique
`(survey, program, healpix)` group present in the catalog, mapped to its
relative coadd FITS path under the DESI DR1 iron healpix tree:

    healpix/<survey>/<program>/<healpix // 100>/<healpix>/coadd-<survey>-<program>-<healpix>.fits

This mirrors the on-disk/URL layout DESI publishes at
https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/.

Memory bound: TARGETID/SURVEY/PROGRAM/HEALPIX are read in fixed-size row
chunks (`--chunk-rows`, default 500,000) via an astropy `memmap=True` HDU, so
peak resident memory is bounded by one chunk plus the (small — thousands, not
millions) set of unique groups, never by the full ~18-27M-row column length.

Fail-closed: this script refuses to open the zcatalog FITS file for reading
unless its SHA-256 matches the `catalog_sha256` recorded in the supplied
manifest (draft or final), and refuses any manifest whose `catalog_sha256` is
not a lowercase 64-hex digest.

Also finalizes `input_manifest.draft.json` into a runnable
`input_manifest.json` by computing the real SHA-256 of a written inventory
file and injecting it as `locator_inventory_sha256`. This is the ONLY
supported way to populate that field; it must never be typed in by hand, and
`clean_rerun_contract.py` rejects anything that is not a genuine lowercase
64-hex digest anyway.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Iterable


class LocatorDerivationError(RuntimeError):
    """Raised when the zcatalog cannot be trusted or read safely."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise LocatorDerivationError(f"required artifact is absent: {path}") from exc
    except json.JSONDecodeError as exc:
        raise LocatorDerivationError(f"invalid JSON artifact: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise LocatorDerivationError(f"JSON artifact must be an object: {path}")
    return value


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def require_sha(value: Any, label: str) -> None:
    if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise LocatorDerivationError(f"{label} must be a lowercase SHA-256")


def verify_zcatalog_checksum(zcatalog_path: Path, manifest: dict[str, Any]) -> None:
    if not zcatalog_path.is_file():
        raise LocatorDerivationError(f"zcatalog FITS file is absent: {zcatalog_path}")
    expected = manifest.get("catalog_sha256")
    require_sha(expected, "manifest catalog_sha256")
    observed = sha256_file(zcatalog_path)
    if observed != expected:
        raise LocatorDerivationError(
            f"zcatalog SHA-256 mismatch: expected {expected}, got {observed} for {zcatalog_path}"
        )


def coadd_relative_path(survey: str, program: str, healpix: int) -> str:
    group = healpix // 100
    return f"healpix/{survey}/{program}/{group}/{healpix}/coadd-{survey}-{program}-{healpix}.fits"


def decode_fits_str(value: Any) -> str:
    if isinstance(value, (bytes, bytearray)):
        return value.decode("utf-8").strip()
    return str(value).strip()


def find_catalog_hdu(hdul: Any) -> Any:
    required = {"TARGETID", "SURVEY", "PROGRAM", "HEALPIX"}
    for hdu in hdul:
        columns = getattr(hdu, "columns", None)
        if columns is not None and required <= set(columns.names):
            return hdu
    raise LocatorDerivationError(
        "no HDU in the zcatalog exposes TARGETID/SURVEY/PROGRAM/HEALPIX columns"
    )


def scan_zcatalog_groups(zcatalog_path: Path, chunk_rows: int = 500_000) -> dict[tuple[str, str, int], int]:
    """Stream TARGETID/SURVEY/PROGRAM/HEALPIX in bounded row chunks.

    Returns a mapping from unique (survey, program, healpix) to the number
    of TARGETID rows observed for that group (a cheap, bounded-size
    aggregate — never a per-TARGETID list).
    """
    try:
        from astropy.io import fits
    except ImportError as exc:  # pragma: no cover - runtime prerequisite
        raise LocatorDerivationError("astropy is required to read the zcatalog FITS file") from exc

    counts: dict[tuple[str, str, int], int] = {}
    with fits.open(zcatalog_path, memmap=True) as hdul:
        table_hdu = find_catalog_hdu(hdul)
        data = table_hdu.data
        n_rows = len(data)
        for start in range(0, n_rows, chunk_rows):
            stop = min(start + chunk_rows, n_rows)
            # Bounded-size column slices only — never the full column at once.
            survey_chunk = data["SURVEY"][start:stop]
            program_chunk = data["PROGRAM"][start:stop]
            healpix_chunk = data["HEALPIX"][start:stop]
            targetid_chunk = data["TARGETID"][start:stop]
            if not (len(survey_chunk) == len(program_chunk) == len(healpix_chunk) == len(targetid_chunk)):
                raise LocatorDerivationError(f"column-length mismatch in zcatalog chunk [{start}:{stop}]")
            for survey_raw, program_raw, healpix_raw, _targetid in zip(
                survey_chunk, program_chunk, healpix_chunk, targetid_chunk
            ):
                key = (decode_fits_str(survey_raw), decode_fits_str(program_raw), int(healpix_raw))
                counts[key] = counts.get(key, 0) + 1
    return counts


def derive_inventory(zcatalog_path: Path, manifest_path: Path, output_path: Path, chunk_rows: int) -> Path:
    manifest = read_json(manifest_path)
    verify_zcatalog_checksum(zcatalog_path, manifest)
    counts = scan_zcatalog_groups(zcatalog_path, chunk_rows=chunk_rows)
    if not counts:
        raise LocatorDerivationError("zcatalog yielded zero (survey, program, healpix) groups")
    ordered_keys: Iterable[tuple[str, str, int]] = sorted(counts)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        for survey, program, healpix in ordered_keys:
            record = {
                "survey": survey,
                "program": program,
                "healpix": healpix,
                "targetid_count": counts[(survey, program, healpix)],
                "coadd_relative_path": coadd_relative_path(survey, program, healpix),
            }
            handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
            handle.write("\n")
    os.replace(tmp_path, output_path)
    return output_path


def finalize_manifest(draft_path: Path, inventory_path: Path, output_path: Path) -> dict[str, Any]:
    if not inventory_path.is_file():
        raise LocatorDerivationError(f"inventory file is absent: {inventory_path}")
    draft = read_json(draft_path)
    manifest = {key: value for key, value in draft.items() if not key.startswith("_")}
    require_sha(manifest.get("catalog_sha256"), "draft catalog_sha256")
    manifest["locator_inventory_sha256"] = sha256_file(inventory_path)
    write_json_atomic(output_path, manifest)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    derive = subcommands.add_parser(
        "derive-inventory", help="stream the zcatalog and write a sorted JSON-lines inventory"
    )
    derive.add_argument("--zcatalog", type=Path, required=True)
    derive.add_argument(
        "--manifest", type=Path, required=True, help="draft or final manifest carrying catalog_sha256"
    )
    derive.add_argument("--output", type=Path, required=True)
    derive.add_argument("--chunk-rows", type=int, default=500_000)

    finalize = subcommands.add_parser(
        "finalize-manifest", help="inject a real locator_inventory_sha256 into the draft manifest"
    )
    finalize.add_argument("--draft", type=Path, required=True)
    finalize.add_argument("--inventory", type=Path, required=True)
    finalize.add_argument("--output", type=Path, required=True)

    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "derive-inventory":
        path = derive_inventory(args.zcatalog, args.manifest, args.output, args.chunk_rows)
        print(f"wrote inventory: {path} (sha256={sha256_file(path)})")
    elif args.command == "finalize-manifest":
        manifest = finalize_manifest(args.draft, args.inventory, args.output)
        print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
