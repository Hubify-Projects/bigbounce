#!/usr/bin/env python3
"""Fetch the retained AUG-011 scored shards and receipts from Backblaze B2.

This utility is intentionally limited to the Phase-3 inputs needed by
``build_flagship_sample.py``.  It never starts compute, changes a B2 object,
or prints credentials, bucket names, or object paths.  Downloads resume by
validated byte size and are written atomically.

Required environment variables (never echoed):
  B2_APPLICATION_KEY_ID (or B2_KEY_ID), B2_APPLICATION_KEY, B2_BUCKET_ID

Example:
  python3 fetch_phase3_inputs.py --destination /work/aug011
  python3 fetch_phase3_inputs.py --destination /work/aug011 --dry-run
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.parse import quote
from urllib.request import Request, urlopen


ARCHIVE_PREFIX = "aug-011-clean-rerun/"
INPUT_KINDS = ("shards", "receipts")
USER_AGENT = "bigbounce-phase3-input-fetch/1.0"


class FetchError(RuntimeError):
    """Raised for a fail-closed input-retrieval error."""


def json_request(url: str, headers: dict[str, str], body: dict[str, Any] | None = None) -> dict[str, Any]:
    encoded = json.dumps(body).encode("utf-8") if body is not None else None
    request = Request(url, headers=headers, data=encoded)
    with urlopen(request, timeout=60) as response:
        payload = json.load(response)
    if not isinstance(payload, dict):
        raise FetchError("provider returned an unexpected response shape")
    return payload


def credentials() -> tuple[str, str, str]:
    key_id = os.environ.get("B2_APPLICATION_KEY_ID") or os.environ.get("B2_KEY_ID")
    key = os.environ.get("B2_APPLICATION_KEY")
    bucket_id = os.environ.get("B2_BUCKET_ID")
    if not all((key_id, key, bucket_id)):
        raise FetchError("B2 credentials or bucket id are unavailable in the environment")
    return key_id, key, bucket_id


def authorize() -> tuple[dict[str, Any], str]:
    key_id, key, _ = credentials()
    basic = base64.b64encode(f"{key_id}:{key}".encode("utf-8")).decode("ascii")
    payload = json_request(
        "https://api.backblazeb2.com/b2api/v2/b2_authorize_account",
        {"Authorization": f"Basic {basic}", "User-Agent": USER_AGENT},
    )
    required = ("apiUrl", "authorizationToken", "downloadUrl", "accountId")
    if any(not payload.get(field) for field in required):
        raise FetchError("B2 authorization response is incomplete")
    return payload, os.environ["B2_BUCKET_ID"]


def bucket_name(auth: dict[str, Any], bucket_id: str) -> str:
    payload = json_request(
        f"{auth['apiUrl']}/b2api/v2/b2_list_buckets",
        {"Authorization": auth["authorizationToken"], "Content-Type": "application/json", "User-Agent": USER_AGENT},
        {"accountId": auth["accountId"], "bucketId": bucket_id},
    )
    buckets = payload.get("buckets")
    if not isinstance(buckets, list) or len(buckets) != 1 or not buckets[0].get("bucketName"):
        raise FetchError("configured B2 bucket could not be resolved")
    return str(buckets[0]["bucketName"])


def list_prefix(auth: dict[str, Any], bucket_id: str, prefix: str) -> list[dict[str, Any]]:
    endpoint = f"{auth['apiUrl']}/b2api/v2/b2_list_file_names"
    headers = {"Authorization": auth["authorizationToken"], "Content-Type": "application/json", "User-Agent": USER_AGENT}
    objects: list[dict[str, Any]] = []
    next_name: str | None = None
    while True:
        body: dict[str, Any] = {"bucketId": bucket_id, "maxFileCount": 1000, "prefix": prefix}
        if next_name:
            body["startFileName"] = next_name
        page = json_request(endpoint, headers, body)
        entries = page.get("files")
        if not isinstance(entries, list):
            raise FetchError("B2 listing response omitted files")
        for entry in entries:
            name, size = entry.get("fileName"), entry.get("contentLength")
            if not isinstance(name, str) or not name.startswith(prefix) or not isinstance(size, int) or size < 0:
                raise FetchError("B2 listing contained an invalid archive object")
            objects.append(entry)
        next_name = page.get("nextFileName")
        if next_name is None:
            break
        if not isinstance(next_name, str):
            raise FetchError("B2 listing continuation is invalid")
    return objects


def target_path(destination: Path, entry: dict[str, Any]) -> Path:
    name = str(entry["fileName"])
    relative = name.removeprefix(ARCHIVE_PREFIX)
    candidate = (destination / relative).resolve()
    root = destination.resolve()
    if not relative or root not in candidate.parents:
        raise FetchError("archive object failed destination safety check")
    return candidate


def fetch_one(download_base: str, token: str, destination: Path, entry: dict[str, Any]) -> str:
    target = target_path(destination, entry)
    expected_size = int(entry["contentLength"])
    if target.is_file() and target.stat().st_size == expected_size:
        return "skipped"
    target.parent.mkdir(parents=True, exist_ok=True)
    url = f"{download_base}{quote(str(entry['fileName']), safe='/')}"
    request = Request(url, headers={"Authorization": token, "User-Agent": USER_AGENT})
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=target.parent, prefix=f".{target.name}.", suffix=".part", delete=False) as handle:
            temporary = Path(handle.name)
            with urlopen(request, timeout=120) as response:
                while block := response.read(8 * 1024 * 1024):
                    handle.write(block)
        if temporary.stat().st_size != expected_size:
            raise FetchError("downloaded object failed byte-size validation")
        os.replace(temporary, target)
        return "downloaded"
    except Exception:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", required=True, type=Path, help="empty or resumable local directory for shards/ and receipts/")
    parser.add_argument("--workers", type=int, default=16, help="parallel B2 downloads (1-64, default: 16)")
    parser.add_argument("--dry-run", action="store_true", help="authenticate and list aggregate archive totals without writing files")
    args = parser.parse_args()
    if not 1 <= args.workers <= 64:
        parser.error("--workers must be between 1 and 64")
    return args


def main() -> int:
    args = parse_args()
    try:
        auth, bucket_id = authorize()
        name = bucket_name(auth, bucket_id)
        entries = [entry for kind in INPUT_KINDS for entry in list_prefix(auth, bucket_id, f"{ARCHIVE_PREFIX}{kind}/")]
        totals = {kind: sum(1 for entry in entries if str(entry["fileName"]).startswith(f"{ARCHIVE_PREFIX}{kind}/")) for kind in INPUT_KINDS}
        byte_total = sum(int(entry["contentLength"]) for entry in entries)
        if totals != {"shards": 36_634, "receipts": 36_634}:
            raise FetchError(f"archive cardinality mismatch: expected 36,634 each, got shards={totals['shards']}, receipts={totals['receipts']}")
        if args.dry_run:
            print(json.dumps({"ok": True, "mode": "dry-run", "objects": len(entries), "shards": totals["shards"], "receipts": totals["receipts"], "bytes": byte_total}, sort_keys=True))
            return 0
        args.destination.mkdir(parents=True, exist_ok=True)
        download_base = f"{auth['downloadUrl']}/file/{quote(name, safe='')}/"
        counts = {"downloaded": 0, "skipped": 0}
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = [executor.submit(fetch_one, download_base, auth["authorizationToken"], args.destination, entry) for entry in entries]
            for index, future in enumerate(as_completed(futures), 1):
                counts[future.result()] += 1
                if index % 5000 == 0:
                    print(json.dumps({"progress": index, "total": len(entries), **counts}, sort_keys=True), flush=True)
        print(json.dumps({"ok": True, "mode": "download", "objects": len(entries), "shards": totals["shards"], "receipts": totals["receipts"], "bytes": byte_total, **counts}, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
