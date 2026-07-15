#!/usr/bin/env python3
"""Download and independently verify a RunPod network-volume retention set."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import hashlib
from pathlib import Path

import retain_remote_production as retention
import generate_remote_bootstrap as bootstrap

try:  # Optional for offline tests and zero-spend preflight.
    import boto3  # type: ignore
except ImportError:  # pragma: no cover - exercised only on minimal runtimes
    boto3 = None


# RunPod documents direct S3 access only for these network-volume regions.
RUNPOD_S3_ENDPOINTS = {
    "US-KS-2": "https://s3api-us-ks-2.runpod.io",
    "US-CA-2": "https://s3api-us-ca-2.runpod.io",
    "EU-RO-1": "https://s3api-eu-ro-1.runpod.io",
    "EUR-IS-1": "https://s3api-eur-is-1.runpod.io",
}


def s3_client(datacenter_id: str):
    if datacenter_id not in RUNPOD_S3_ENDPOINTS:
        raise ValueError("network volume datacenter has no supported RunPod S3 endpoint")
    if boto3 is None:
        raise ValueError("boto3 is required for RunPod S3 retention verification")
    # Credentials are intentionally obtained only through boto3's standard
    # environment/provider chain and are never accepted as arguments.
    return boto3.client("s3", endpoint_url=RUNPOD_S3_ENDPOINTS[datacenter_id],
                        region_name=datacenter_id)


def _listed_keys(client, bucket: str, prefix: str) -> set[str]:
    keys: set[str] = set()
    token = None
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix}
        if token:
            kwargs["ContinuationToken"] = token
        response = client.list_objects_v2(**kwargs)
        keys.update(item["Key"] for item in response.get("Contents", []))
        if not response.get("IsTruncated"):
            return keys
        token = response.get("NextContinuationToken")
        if not token:
            raise ValueError("ambiguous truncated S3 listing without continuation token")


def download_and_verify(*, client, network_volume_id: str, datacenter_id: str,
                        prefix: str, staging_root: Path, manifest: dict,
                        receipt_path: Path) -> dict:
    if not network_volume_id:
        raise ValueError("networkVolumeId is required")
    if datacenter_id not in RUNPOD_S3_ENDPOINTS:
        raise ValueError("unsupported RunPod S3 datacenter")
    normalized = prefix.strip("/")
    expected_prefix = f"p1b-retention/{manifest['contract_id']}--{manifest['git_commit']}"
    if normalized != expected_prefix or not re.fullmatch(
            r"p1b-retention/[A-Za-z0-9._-]+--[0-9a-f]{40}", normalized):
        raise ValueError("unsafe or manifest-mismatched S3 retention prefix")
    final_dir = staging_root / normalized
    if final_dir.exists():
        verified = retention.validate_retention(
            final_dir, commit=manifest["git_commit"], contract_id=manifest["contract_id"]
        )
        receipt = _verification_receipt(network_volume_id, datacenter_id, normalized,
                                        manifest, verified)
        retention.atomic_json(receipt_path, receipt)
        return receipt
    marker_key = f"{normalized}/{retention.MARKER}"
    marker_tmp = staging_root / f".{normalized.replace('/', '_')}.marker.tmp"
    marker_tmp.parent.mkdir(parents=True, exist_ok=True)
    client.download_file(network_volume_id, marker_key, str(marker_tmp))
    marker = json.loads(marker_tmp.read_text())
    marker_snapshot = marker_tmp.read_bytes()
    contract_path = "reproducibility/p1_namaster_500mc/runpod_production_contract.json"
    if marker.get("contract_sha256") != (manifest.get("input_sha256") or {}).get(contract_path):
        raise ValueError("S3 retention marker contract hash mismatch")
    bound_hash = hashlib.sha256(bootstrap.canonical_manifest_bytes(manifest)).hexdigest()
    if marker.get("bound_manifest_sha256") != bound_hash:
        raise ValueError("S3 retention marker bound-manifest hash mismatch")
    declared = marker.get("inventory")
    if not isinstance(declared, list) or not declared:
        raise ValueError("S3 retention marker has no declared inventory")
    relative = {item.get("path") for item in declared}
    if None in relative or any(not isinstance(name, str) or name.startswith("/") or ".." in Path(name).parts
                               for name in relative):
        raise ValueError("S3 retention marker contains unsafe inventory paths")
    expected = {marker_key} | {f"{normalized}/{name}" for name in relative}
    actual = _listed_keys(client, network_volume_id, normalized + "/")
    if actual != expected:
        raise ValueError("S3 retention prefix has missing or extra objects")

    partial = staging_root / f".{normalized.replace('/', '_')}.download"
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True)
    try:
        for name in sorted(relative):
            target = partial / name
            target.parent.mkdir(parents=True, exist_ok=True)
            client.download_file(network_volume_id, f"{normalized}/{name}", str(target))
        marker_second = partial / ".marker-second"
        client.download_file(network_volume_id, marker_key, str(marker_second))
        if marker_second.read_bytes() != marker_snapshot:
            raise ValueError("S3 retention marker changed during download")
        marker_second.unlink()
        if _listed_keys(client, network_volume_id, normalized + "/") != actual:
            raise ValueError("S3 retention inventory changed during download")
        shutil.move(str(marker_tmp), partial / retention.MARKER)
        verified = retention.validate_retention(
            partial, commit=manifest["git_commit"], contract_id=manifest["contract_id"]
        )
        # validate_retention recomputes every byte count and SHA-256.
        if final_dir.exists():
            raise ValueError("verified local retention destination already exists")
        final_dir.parent.mkdir(parents=True, exist_ok=True)
        os.replace(partial, final_dir)
        receipt = _verification_receipt(network_volume_id, datacenter_id, normalized,
                                        manifest, verified)
        retention.atomic_json(receipt_path, receipt)
        return receipt
    except Exception:
        # Preserve downloaded evidence for forensic inspection.
        raise


def _verification_receipt(network_volume_id: str, datacenter_id: str, prefix: str,
                          manifest: dict, verified: dict) -> dict:
    return {
        "schema": "p1b-runpod-s3-verification/v1", "state": "verified",
        "network_volume_id": network_volume_id, "datacenter_id": datacenter_id,
        "prefix": prefix, "git_commit": manifest["git_commit"],
        "contract_id": manifest["contract_id"], "inventory": verified["inventory"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--network-volume-id", required=True)
    parser.add_argument("--datacenter-id", choices=sorted(RUNPOD_S3_ENDPOINTS), required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--staging-root", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    download_and_verify(client=s3_client(args.datacenter_id), network_volume_id=args.network_volume_id,
                        datacenter_id=args.datacenter_id, prefix=args.prefix,
                        staging_root=args.staging_root.resolve(), manifest=manifest,
                        receipt_path=args.receipt.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
