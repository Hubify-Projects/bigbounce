# INT API Review — P3 v3.2.0-r6 — openai (gpt-5.5)
paper: P3  version: v3.2.0-r6  model: gpt-5.5
provenance: commit=c6277107cb8d705d6b2c1b675269f507fa54ab9a  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=a16c217930a31ba799b68a88b2477b020ad5e309ff79626e49b2b69a715fdd5a
packet: key=3ab042051bdcc7ded3cad1a683f6247eec61f0fa845ada819fd871562dffbebf  profile=APJS-CATALOG
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T19:21:25.446825Z  |  latency: 59.7s  |  attempt: 1
usage: {"input_tokens": 18190, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2250, "output_tokens_details": {"reasoning_tokens": 1273}, "total_tokens": 20440}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Title/Abstract/Conclusions — The phrase “Public-ID Recovery” and the headline count of 181 imply recovered object identities, but the manuscript’s own local-shift control shows that the 0.1–1″ tail has no positive positional-association evidence and is explicitly “not secure candidate-level identity.” Either redefine the primary catalog as 170 high-coordinate-consistency recovered IDs plus an explicitly lower-confidence 11-row appendix/auxiliary tier, or consistently call the 181 objects “positional associations” rather than recovered identities.

2. [MAJOR] Sections 3.5, 4.3, and 7 — The chance-association analysis is not adequately integrated into the catalog interpretation. For the strict cohort, the shifted expectation within 1″ is 76.2 compared with 181 observed, implying a non-negligible background for the full 1″ definition even though the sub-0.1″ core is strong. The paper should quantify the expected background/excess by tier in the main text and catalog metadata, and state more explicitly that the 1″ primary catalog is not a purity-controlled sample.

3. [MAJOR] Data Availability / Release Versioning — The release provenance is difficult to audit because the manuscript mixes v3.2.0-r2 catalog, v3.2.0-r6 manuscript, r3 viewer audits, r4 AAS table package, and r5 warning-bearing auxiliary products. For an ApJS catalog paper, the peer-reviewed data product must be unambiguous: provide one definitive frozen bundle or clearly separated primary/auxiliary bundles, each with exact contents, checksums, immutable identifier, and relationship to the submitted machine-readable table.

4. [MAJOR] Sections 2.1 and 5.1 — The historical anomaly scores and upstream BigAE preprocessing are explicitly not reproducible from public spectra. This limitation is honestly stated, but it weakens the scientific meaning of carrying `original_score` as a ranking column. The catalog dictionary and main text should label these scores as legacy metadata in every relevant place and should avoid any language suggesting comparable anomaly significance, model performance, or physical abnormality.

5. [MAJOR] Section 3.1 / Matching Definition — The manuscript should justify the use of DESI `TARGET_RA`, `TARGET_DEC` rather than any observed/fiber/coadd coordinate, and should state whether the historical anomaly coordinates were originally target coordinates, spectral-product coordinates, or cluster means derived from mixed sources. This is important because the entire recovery rests on subarcsecond positional matching.

6. [MINOR] Abstract and Section 4.1 — “Warning-free” should be defined at first use as `ZWARN=0` from the public Redrock/zcatalog row, not as a general statement that the spectra are problem-free. Some readers may otherwise infer stronger data quality than the DESI flag supports.

7. [MINOR] Tables 3 and 4 / Typography — The bit notation in Table 3 appears as “21”, “22”, and “211” in the parsed text and could be misread as decimal integers rather than powers of two. Use unambiguous notation such as \(2^1\), \(2^2\), \(2^{11}\), and check all prime/arcsecond symbols for proper AASTeX rendering.

8. [MINOR] Section 3.3 — The duplicate-handling rule is well described, but since no duplicate removal occurs in the final strict cohort, the manuscript should explicitly distinguish between rules that affected the released table and rules included only for determinism in possible reruns.

9. [MINOR] Section 6.2 — The public-viewer retrieval audit is useful but should be clearly demoted as a convenience check; screenshots and viewer pages are not stable archival data products and should not be presented alongside FITS-row rejoin validation as equivalent evidence.

10. [MINOR] Section 4.2 — The two negative-redshift objects are retained under the declared rule, which is acceptable, but the catalog should include an easy Boolean or recommended filter for users wanting positive-redshift extragalactic subsets.

11. [MINOR] References and acknowledgments — Verify that all DESI DR1 references, data-model URLs, and acknowledgments match the journal-required and DESI-required citation language at final submission, especially because several cited items are versioned or accessed by date.

(3) The central claim is supported for a reproducible DESI DR1 positional rejoin and warning-free primary-row catalog, but not for secure physical anomaly identification or uniformly secure candidate-level identity for all 181 rows.