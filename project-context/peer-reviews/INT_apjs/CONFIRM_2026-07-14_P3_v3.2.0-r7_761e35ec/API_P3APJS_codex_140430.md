# INT Codex-subscription Review (ApJS-framed) — P3APJS v3.2.0-r7 — gpt-5.6-sol (high)
paper: P3APJS  version: v3.2.0-r7  tex: pipelines/p3_anomaly_engine/paper3_apjs.tex
venue-framing: The Astrophysical Journal Supplement Series (ApJS)
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
provenance: commit=ba2f5b93a30de41122dc2ed31b543ac0da9a37c8  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=761e35ec840e93599163d68c6b4db9b8d75293545e49c45c978dc0be0f38cb2b
source: pipelines/p3_anomaly_engine/paper3_apjs.tex  sha256=01cb68b1d52d411c1f4b181d6504f2f1344bc45d1f0ad3793d74b58a5d7e75d8
UTC: 2026-07-14T21:04:33Z

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

Review basis: At commit `ba2f5b93a30de41122dc2ed31b543ac0da9a37c8`, I verified PDF SHA-256 `761e35ec840e93599163d68c6b4db9b8d75293545e49c45c978dc0be0f38cb2b` and 16 pages; visually inspected PNG pages 01–16 individually using `view_image`; read the complete 1,076-line source; and reviewed the full 11 MB local bundle, manifests, validators, results, and small Parquet/TSV/JSON/CSV products without accessing FITS files or the network. All pages are legible and free of overlaps or clipping; pages 13–15 have excessive whitespace, and page 5 has awkward float placement.

(2) ISSUES:

1. [MAJOR] Section 6.4 and Data Availability—The claimed “definitive checksum-bound” committed bundle is incomplete at the specified commit. `BUNDLE_MANIFEST.json` requires 41 files, but the Git tree contains only 38 files totaling 438,318 bytes. Three manifest-listed, `.gitignore`-excluded payloads are absent: the 10,514,503-byte historical anomaly Parquet, the 58,038-byte primary 181-row Parquet, and the 352,155-byte warned-auxiliary Parquet. Consequently, a fresh checkout cannot pass the advertised validator, and the cited GitHub warned-auxiliary path does not contain its table. Commit/LFS-store these payloads or deposit the complete package in a durable immutable archive, then validate from a clean clone and correct the availability claims.

2. [MINOR] Section 3.4 and the title—the manuscript establishes that the original \(1''\) radius was predeclared but does not state whether the central \(0.1''\) boundary defining the 170-row core was chosen before or after examining the separation distribution and shift controls. State the provenance of this threshold explicitly and characterize it as post hoc if applicable; the supplied full radius curve appropriately supports sensitivity assessment.

3. [MINOR] Section 5.2—“Testing alternative anomaly models” on this candidate-only list overstates its evaluative use. Without a representative control sample or inclusion probabilities, models can be cross-scored or used for follow-up prioritization but cannot be tested for discrimination, calibration, completeness, or false-positive rate; revise this recommended use consistently with Section 5.3.

4. [MINOR] Sections 2.1, 5, and 7—the manuscript correctly discloses that production normalization, resampling, and object-to-spectrum mapping are unavailable. Ensure the abstract, metadata, and eventual archive description consistently label the product as public-ID recovery from a frozen historical candidate list, not as a reproducible anomaly detector or physically validated anomaly catalog.

5. [MINOR] Presentation—Pages 13–15 are substantially underfilled, and Table 2 produces awkward column flow on page 5. These do not obscure content but should be improved for journal presentation.

(3) The released focused DESI catalog contract is numerically supported as 170 high-coordinate-consistency rows plus 11 explicitly lower-confidence positional associations and is potentially appropriate for ApJS, but only after the missing committed data products are archived reproducibly and without implying astrophysical identity, purity, or classification.