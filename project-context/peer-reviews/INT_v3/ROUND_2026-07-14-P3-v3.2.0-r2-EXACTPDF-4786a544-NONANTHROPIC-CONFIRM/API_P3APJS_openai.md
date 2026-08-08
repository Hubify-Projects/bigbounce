# INT API Review — P3APJS v3.2.0-r2 — openai (gpt-5.5)
paper: P3APJS  version: v3.2.0-r2  model: gpt-5.5
provenance: commit=245e24a0  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=4786a544b7d0dbb47dd00690d795c671f06cfc04df62c863b0e639b1a0292e1b
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T12:52:31.610201Z  |  latency: 46.4s  |  attempt: 1
usage: {"input_tokens": 11900, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2358, "output_tokens_details": {"reasoning_tokens": 1552}, "total_tokens": 14258}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Abstract/Sections 1 and 5 — The claim that the “selection function is reconstructable” is overstated. The DESI rejoin, primary-row, and ZWARN selection are well specified, but the upstream historical anomaly stream is not scientifically reconstructable from the manuscript: the anomaly model, preprocessing, score definition, thresholding, and original inclusion rules are not described sufficiently. Either document that upstream selection in enough detail to reproduce it, or narrow the claim/title to a recovered public-ID catalog from a pre-existing historical anomaly list.

2. [MAJOR] Sections 3.3 and Appendix A — The ordering of duplicate handling versus the ZCAT_PRIMARY and ZWARN gates is ambiguous and potentially non-commutative. Appendix A appears to deduplicate before applying the primary/warning cuts, whereas the waterfall reads as if primary and ZWARN cuts are applied directly to the 2468 matches. The paper must give an exact executable logical order, with intermediate counts, and demonstrate that no warning-free primary candidate is lost because a nearer non-primary or warning-bearing row was retained first.

3. [MAJOR] Sections 2.1, 3.4, and 4.3 — The positional identity recovery needs stronger validation. The adopted match is target-to-cluster, not target-to-original-DESI-member, and one released object is 1.98″ from the canonical original member. Since public identity is the central product, the manuscript should provide the full distribution of target-to-original-member separations, the number of competing eligible DESI rows within 1″ and perhaps 2″ of each cluster/original member, and a clear confidence flag or exclusion rationale for ambiguous cases.

4. [MAJOR] Data Availability — For an ApJS catalog paper, the released catalog and code should be placed in a durable, citable archival repository with a DOI, or otherwise meet journal standards for long-term preservation. A Hugging Face tag/commit plus checksums is useful for reproducibility but is not obviously sufficient as the authoritative archival location for a published catalog.

5. [MINOR] Abstract/Title/Sections 4 and 8 — The phrase “warning-free primary spectra” should be used carefully, since the object of selection is a zcatalog row/coadd primary redshift entry rather than necessarily an individual exposure-level spectrum. Consider using “primary redshift rows” consistently.

6. [MINOR] Section 4.2 — The retention of two negative-redshift objects with ZWARN=0 is logically consistent with the stated cuts, but the manuscript should identify their SPECTYPEs and clarify whether these are stellar/low-redshift template artifacts or simply Redrock metadata retained by policy.

7. [MINOR] Section 4.4/Table 3 — The example table contains only the highest-score objects and all are classified as GALAXY. For a catalog paper, it would be more informative to include at least one QSO, the STAR, and one high-separation-tail object, or state explicitly that Table 3 is not intended to illustrate the diversity of the release.

8. [MINOR] Sections 3.1 and 6 — The validation discussion is strong, but the manuscript should state whether the released build scripts were run from a clean environment using only the public inputs named in Data Availability, rather than relying on any pre-existing local checkpoint artifacts.

9. [MINOR] References — Verify all bibliographic metadata and formatting against journal style, especially the future/in-press DESI DR1 and Nicolaou et al. entries, and include DOIs where available.

(3) The central claim is substantially supported for the DESI DR1 public-ID recovery and warning-free 181-row release, but not yet for a fully reconstructable anomaly-candidate selection function including the upstream historical anomaly generation.