#!/usr/bin/env python3
from __future__ import annotations

import unittest
from unittest import mock

import c10_source_correction as correction


EXPECTED_DIFF = """
+from multipole_contract import field_harmonic_kwargs
-        lmax=LMAX
+        **field_harmonic_kwargs(lmax=LMAX, purify_b=purify)
+        lmax_mask=LMAX if purify else None
+        purify_b=state["purify"]
"""


class C10SourceCorrectionTests(unittest.TestCase):
    def test_expected_purification_only_diff_passes(self):
        correction.verify_narrow_equivalence(EXPECTED_DIFF)

    def test_scientific_contract_change_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "non-purification"):
            correction.verify_narrow_equivalence(EXPECTED_DIFF + "\n+N_REAL = 100\n")

    def test_missing_completed_shards_fail_closed(self):
        with mock.patch.object(correction, "SHARDS", correction.ROOT / "absent"):
            with self.assertRaises(FileNotFoundError):
                correction.shard_records()


if __name__ == "__main__":
    unittest.main()
