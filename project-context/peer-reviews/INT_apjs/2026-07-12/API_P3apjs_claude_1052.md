# INT Claude-subscription Review (ApJS-framed) — P3APJS v3.1.157-apjs — claude-opus-4-8
paper: P3APJS  version: v3.1.157-apjs  tex: pipelines/p3_anomaly_engine/paper3_apjs.tex
venue-framing: The Astrophysical Journal Supplement Series (ApJS)
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T17:52:48Z

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have enough to render a verdict. Let me confirm the two manifests' file-set divergence is real (LAMOST absent from the JSON manifest).

The RELEASE_MANIFEST.json `files[]` array (25 entries) contains no LAMOST file, while `DATA_RELEASE_MANIFEST.md` lists `lamost_dr10_pathc_native.parquet` and the paper's DAS says LAMOST blocks carry per-object canonical-S scores in the release. That divergence, plus the pinned-hash mismatch, are the crux. Writing the review.

---

**(1) VERDICT: MAJOR REVISIONS**

**(2) ISSUES:**

**[MAJOR] 1 — The immutable pinned pointer is internally inconsistent across the three release artifacts (this is the exact ApJS acceptance hinge).** The paper's Data Availability statement (`paper3_apjs.tex:1694`) pins the reviewed release at HuggingFace commit `34319c75edec1f65c34cfe99bef89f6cd5562ae5`, and `DATA_RELEASE_MANIFEST.md:6` cites the same hash. But the machine-readable, authoritative `RELEASE_MANIFEST.json:12` sets `"pinned_revision": "d5ff9b85318b522f38fe75326c2b72bf6c22e9db"`, and its own `pinned_revision_note` (line 170) asserts that *this* commit "is the immutable citable pointer used in the paper." A reviewer downloading "the pinned revision" therefore gets two different answers, and the manifest's self-description directly contradicts the paper. For a data-release journal whose entire premise is an unambiguous immutable pointer, the pin cannot be ambiguous. Reconcile all three to a single frozen commit.

**[MAJOR] 2 — `RELEASE_MANIFEST.json` does not enumerate "every released catalog file," and disagrees with its companion manifest on the canonical file set.** The DAS (`:1694`) states the manifest lists "every released catalog file" (25 files) and that "DESI, SDSS, **LAMOST**, and NEOWISE blocks carry per-object canonical-$S$ scores." Yet the 25-file `RELEASE_MANIFEST.json` contains **no LAMOST file at all**, while `DATA_RELEASE_MANIFEST.md:22` lists `lamost_dr10_pathc_native.parquet` (113,342). The JSON manifest also omits `pathc_unique_objects_no_act.parquet` — the file `DATA_RELEASE_MANIFEST.md:16` designates the **PRIMARY** canonical catalog (378,280, 7-way, ACT-excluded) — as well as `neowise_pathc_masked_anomalies.parquet` and `cmb_native_anomalies.parquet`. So the two manifests describe divergent file sets and even a different "primary" catalog file (the JSON's headline recompute runs off the 8-way `pathc_unique_objects.parquet`; the MD calls the `_no_act` file primary). A reviewer cannot verify "every released catalog file" against the manifest the paper points them to. Make the machine-readable manifest complete and authoritative, and delete/merge the divergent MD.

**[MINOR] 3 — The abstract still carries prospective release language, the very phrasing this closure was meant to remove.** The abstract's final sentence (`:1029`) reads "The catalog, model weights, and reproducibility scripts **will be publicly released with the arXiv posting**." That is future-tense availability — inconsistent with the DAS's claim that the catalog is *already* public, immutable, and pinned. Update to past/present tense with the pinned pointer.

**[MINOR] 4 — Stale / mismatched checksum provenance in the human-readable manifest.** `DATA_RELEASE_MANIFEST.md:101` states checksums were "computed with `sha256sum` on 2026-06-10 (pre-public staging snapshot)," a month before `RELEASE_MANIFEST.json`'s `manifest_frozen_utc` of 2026-07-12; and the MD lists SHA-256 values (e.g., for the `_no_act` primary and LAMOST) that do not appear in the frozen JSON. Recompute and date-stamp against the frozen revision so the two manifests agree.

*Note on verification scope:* I confirmed `scripts/reproduce_headline_dedup.py` is a genuine, deterministic 4-way 5″ union-find deduplicator that regenerates the 268,519 validated count from the released per-survey tables, and that the DAS-quoted SHA-256 for `pathc_unique_objects.parquet` (`b14deb02…6138c643`) matches the JSON manifest. I could **not** recompute the parquet SHA-256s or the 377,482/268,519 counts locally because the `.parquet` products live only in the HF release, not in the committed tree — which is acceptable for a hosted release but means the pin/manifest consistency above is the only in-repo lever a reviewer has, making issues 1–2 load-bearing.

**(3)** The central claim — a genuinely multi-survey, native-retrained, honestly-tiered anomaly catalog with reproducible headline counts and per-survey validity flags — is well-supported, unusually candid about its process-volume framing and failed tiers, and squarely appropriate for ApJS; **but the immutable-reviewable-release gap is not yet cleanly closed**, because the pinned commit hash is internally contradictory across the paper, the JSON manifest, and the MD manifest, and the machine-readable manifest is incomplete relative to the release it claims to enumerate — mechanical fixes, but they must land before the "immutable, independently runnable reviewable release" claim holds.
