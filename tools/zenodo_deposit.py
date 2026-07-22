#!/usr/bin/env python3
"""Create/verify/publish a Zenodo deposit from a prepared staging directory.

Fail-closed companion to ``prepare_paper_deposit.py``. Reads ``.zenodo.json``
plus the staged files from ``--staging-dir``, creates a *draft* deposition,
uploads every staged file, verifies every remote MD5 against the local file,
and writes a machine-readable receipt. Publication is irreversible on Zenodo,
so it only happens with ``--publish --confirm PUBLISH`` and a metadata license
present.

The token is read from ``$ZENODO_TOKEN`` or the repo ``.env.local`` and is
never printed. Draft depositions are private and deletable; nothing in the
default mode is irreversible.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_DEFAULT = "https://zenodo.org/api"
REQUIRED_METADATA = ("title", "creators", "description", "upload_type", "access_right")


class DepositError(RuntimeError):
    pass


def load_token(repo: Path) -> str:
    import os

    tok = os.environ.get("ZENODO_TOKEN", "").strip()
    if not tok:
        env = repo / ".env.local"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("ZENODO_TOKEN="):
                    tok = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not tok:
        raise DepositError("ZENODO_TOKEN not found in environment or .env.local")
    return tok


def _request(method: str, url: str, token: str, payload=None, data: bytes | None = None,
             content_type: str | None = None, retries: int = 3):
    headers = {"Authorization": f"Bearer {token}"}
    body = data
    if payload is not None:
        body = json.dumps(payload).encode()
        headers["Content-Type"] = "application/json"
    elif content_type:
        headers["Content-Type"] = content_type
    last = None
    for attempt in range(retries):
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode(errors="replace")[:1000]
            last = DepositError(f"{method} {url} -> HTTP {exc.code}: {detail}")
            if exc.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise last
        except urllib.error.URLError as exc:
            last = DepositError(f"{method} {url} -> {exc}")
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise last
    raise last  # pragma: no cover


def md5_of(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--staging-dir", required=True, help="directory with .zenodo.json + files")
    ap.add_argument("--paper", required=True, help="label for the receipt (e.g. P1A, namaster-proof)")
    ap.add_argument("--receipt-out", required=True, help="path to write the JSON receipt")
    ap.add_argument("--deposition-id", type=int, help="resume an existing draft instead of creating one")
    ap.add_argument("--api", default=API_DEFAULT)
    ap.add_argument("--publish", action="store_true", help="publish after verification (IRREVERSIBLE)")
    ap.add_argument("--confirm", default="", help="must be the literal string PUBLISH to publish")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[1]))
    args = ap.parse_args()

    repo = Path(args.repo)
    staging = Path(args.staging_dir)
    meta_path = staging / ".zenodo.json"
    if not meta_path.exists():
        raise DepositError(f"missing {meta_path}")
    metadata = json.loads(meta_path.read_text())
    for key in REQUIRED_METADATA:
        if not metadata.get(key):
            raise DepositError(f"metadata intentionally incomplete: missing '{key}'")
    if args.publish:
        if args.confirm != "PUBLISH":
            raise DepositError("refusing to publish: pass --confirm PUBLISH (publication is irreversible)")
        if not metadata.get("license"):
            raise DepositError("refusing to publish: metadata has no license (D2 unresolved)")

    files = sorted(p for p in staging.iterdir() if p.is_file() and not p.name.startswith("."))
    if not files:
        raise DepositError(f"no files to upload in {staging}")

    token = load_token(repo)

    if args.deposition_id:
        dep = _request("GET", f"{args.api}/deposit/depositions/{args.deposition_id}", token)
    else:
        dep = _request("POST", f"{args.api}/deposit/depositions", token, payload={})
    dep_id = dep["id"]
    print(f"deposition id: {dep_id} (state={dep.get('state')})")

    dep = _request("PUT", f"{args.api}/deposit/depositions/{dep_id}", token,
                   payload={"metadata": metadata})
    bucket = dep["links"]["bucket"]

    existing = {f["filename"]: f for f in
                _request("GET", f"{args.api}/deposit/depositions/{dep_id}/files", token)}
    uploaded = []
    for path in files:
        local_md5 = md5_of(path)
        prior = existing.get(path.name)
        if prior and prior.get("checksum", "").replace("md5:", "") == local_md5:
            print(f"  skip (already uploaded, md5 match): {path.name}")
        else:
            print(f"  upload: {path.name} ({path.stat().st_size} bytes)")
            _request("PUT", f"{bucket}/{urllib.parse.quote(path.name)}", token,
                     data=path.read_bytes(), content_type="application/octet-stream")
        uploaded.append({"filename": path.name, "size_bytes": path.stat().st_size,
                         "local_staged_md5": local_md5})

    remote = {f["filename"]: f.get("checksum", "").replace("md5:", "") for f in
              _request("GET", f"{args.api}/deposit/depositions/{dep_id}/files", token)}
    all_match = True
    for entry in uploaded:
        entry["zenodo_md5"] = remote.get(entry["filename"], "MISSING")
        entry["md5_match"] = entry["zenodo_md5"] == entry["local_staged_md5"]
        all_match &= entry["md5_match"]
    if not all_match:
        raise DepositError("remote MD5 mismatch after upload — deposit NOT publishable: "
                           + json.dumps([e for e in uploaded if not e["md5_match"]]))
    print(f"all {len(uploaded)} remote MD5s verified against local staging")

    receipt = {
        "paper": args.paper,
        "deposition_id": dep_id,
        "state": "draft",
        "submitted": False,
        "draft_url": dep["links"].get("latest_draft_html") or dep["links"].get("html"),
        "prereserved_doi": (dep.get("metadata", {}).get("prereserve_doi") or {}).get("doi"),
        "metadata": metadata,
        "files": uploaded,
        "receipt_written_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(),
    }

    if args.publish:
        pub = _request("POST", f"{args.api}/deposit/depositions/{dep_id}/actions/publish", token)
        doi = pub["doi"]
        receipt.update({
            "state": pub.get("state"),
            "submitted": pub.get("submitted"),
            "doi": doi,
            "concept_doi": pub.get("conceptdoi"),
            "record_id": pub.get("record_id") or dep_id,
            "record_url": pub["links"].get("record_html") or pub["links"].get("html"),
            "doi_url": f"https://doi.org/{doi}",
            "published_at": pub.get("created"),
            "modified": pub.get("modified"),
        })
        req = urllib.request.Request(f"https://doi.org/{doi}", method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                receipt["doi_head_resolves"] = f"{resp.status} -> {resp.url} (verified)"
        except Exception as exc:  # DataCite propagation can lag minutes
            receipt["doi_head_resolves"] = f"not yet ({exc}); DataCite propagation can lag"
        print(f"PUBLISHED: {doi}")

    out = Path(args.receipt_out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=1) + "\n")
    print(f"receipt: {out}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except DepositError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
