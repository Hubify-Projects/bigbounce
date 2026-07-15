#!/usr/bin/env python3

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().with_name("verify_runpod_s3_retention.py")
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("verify_runpod_s3_retention", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class FakeS3:
    def __init__(self, objects):
        self.objects = objects
        self.downloads = []

    def list_objects_v2(self, **kwargs):
        keys = sorted(key for key in self.objects if key.startswith(kwargs["Prefix"]))
        return {"Contents": [{"Key": key} for key in keys], "IsTruncated": False}

    def download_file(self, bucket, key, filename):
        self.downloads.append((bucket, key))
        if key not in self.objects:
            raise ValueError("missing object")
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        Path(filename).write_bytes(self.objects[key])


class S3RetentionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.manifest = {"git_commit": "1" * 40, "contract_id": "contract-v1"}
        self.prefix = "p1b-retention/contract-v1--" + "1" * 40
        data = b"scientific evidence\n"
        item = {"path": "state/evidence.json", "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest()}
        marker = {"schema": "p1b-runpod-retention/v1", "state": "complete",
                  "git_commit": self.manifest["git_commit"],
                  "contract_id": self.manifest["contract_id"], "inventory": [item]}
        self.objects = {
            f"{self.prefix}/RETENTION_COMPLETE.json": (json.dumps(marker) + "\n").encode(),
            f"{self.prefix}/state/evidence.json": data,
        }

    def tearDown(self): self.temp.cleanup()

    def verify(self, objects=None):
        client = FakeS3(self.objects if objects is None else objects)
        receipt = self.root / "receipt.json"
        result = MODULE.download_and_verify(
            client=client, network_volume_id="vol-1", datacenter_id="US-KS-2",
            prefix=self.prefix, staging_root=self.root / "stage", manifest=self.manifest,
            receipt_path=receipt,
        )
        return client, receipt, result

    def test_downloads_every_declared_object_and_writes_atomic_receipt(self):
        client, receipt, result = self.verify()
        self.assertEqual(result["state"], "verified")
        self.assertEqual({key for _, key in client.downloads}, set(self.objects))
        self.assertEqual(json.loads(receipt.read_text())["state"], "verified")

    def test_extra_object_is_rejected(self):
        objects = dict(self.objects)
        objects[f"{self.prefix}/unexpected"] = b"x"
        with self.assertRaisesRegex(ValueError, "missing or extra"):
            self.verify(objects)

    def test_missing_or_corrupt_object_never_writes_success(self):
        missing = dict(self.objects)
        missing.pop(f"{self.prefix}/state/evidence.json")
        with self.assertRaisesRegex(ValueError, "missing or extra"):
            self.verify(missing)
        corrupt = dict(self.objects)
        corrupt[f"{self.prefix}/state/evidence.json"] = b"corrupt"
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            self.verify(corrupt)

    def test_unsupported_endpoint_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "unsupported"):
            MODULE.download_and_verify(
                client=FakeS3(self.objects), network_volume_id="vol-1", datacenter_id="UNKNOWN",
                prefix=self.prefix, staging_root=self.root / "stage", manifest=self.manifest,
                receipt_path=self.root / "receipt.json",
            )


if __name__ == "__main__":
    unittest.main()
