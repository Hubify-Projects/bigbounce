# INT API Review — P3APJS v3.2.0-r4 — openai (gpt-5.5)
paper: P3APJS  version: v3.2.0-r4  model: gpt-5.5
provenance: commit=5898e0c3  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=a0cfe715667b54122566122e976a3c7fedbc2881a747698cc0d431e5e0f086e8
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T14:31:25.927610Z  |  latency: 41.4s  |  attempt: 1
usage: {"input_tokens": 14742, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 1793, "output_tokens_details": {"reasoning_tokens": 1034}, "total_tokens": 16535}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:  
1. [MINOR] Data Availability / release permanence: the manuscript relies on a Hugging Face commit as the current immutable byte-level reference while stating that the AAS digital-asset DOI is not yet assigned; before publication the full 181-row, 43-column catalog, dictionary, manifest, and executable scripts should be deposited as the journal digital asset or another durable DOI-backed archive, and the text should cite that final archival identifier.  
2. [MINOR] Title/Abstract terminology: “Anomaly-Candidate Catalog” is acceptable only because the text repeatedly disclaims physical validation, but the abstract should state even more explicitly that “anomaly” refers solely to membership in the historical BigAE score-selected input stream and not to independently verified anomalous spectra.  
3. [MINOR] Section 2.1, historical anomaly-cluster substrate: the upstream positional clustering is treated as a frozen input, but the manuscript should give the clustering radius/algorithm or point readers to the exact documentation for that file, since the final catalog depends on cluster centroids rather than solely on original DESI anomaly-member coordinates.  
4. [MINOR] Section 3.2, target-bit definition: provide the exact integer or hexadecimal value of the DESI_TARGET mask used for bits 0, 1, 2, 60, and 61, and preferably a one-line code expression, to remove any possible ambiguity about unsigned 64-bit handling.  
5. [MINOR] Section 3.3, duplicate handling: the manuscript states that no final tie-breaking was needed and that all cohorts already have unique cluster and TARGETID keys; include the actual duplicate counts before and after each deduplication stage in COHORT_COUNTS.json or the text so this important null result is directly auditable.  
6. [MINOR] Section 3.4 / Section 4.3, positional-tail interpretation: the one case with 1.979″ separation from the canonical original DESI member should be highlighted in the released catalog notes and table metadata, because users may otherwise assume that the 1″ criterion applies to both cluster centroid and original anomaly-member position.  
7. [MINOR] Section 4.1, ZWARN rejection: the large reduction from 2448 primaries to 181 warning-free rows is central; add a short statement clarifying whether the rejected 2267 rows are included anywhere as an auxiliary table or are completely omitted, and whether users can reproduce a broader “primary but warned” follow-up list from the supplied checkpoint parts.  
8. [MINOR] Section 4.2, negative redshifts: the retention of two ZWARN=0 negative-redshift rows is methodologically consistent, but the text should note whether these have reliable DESI viewer spectra/coadds and whether they fall in the 20-target public-viewer audit.  
9. [MINOR] Figures 1–2: improve readability for publication by enlarging labels and legends; Figure 2a especially has small overplotted markers and a compressed legend that may be difficult to interpret in ApJS column format.  
10. [MINOR] References and provenance: several cited items are versioned web resources or future/current DESI products; ensure final references include stable URLs, access dates where appropriate, and complete immutable identifiers rather than abbreviated hashes in the bibliography or data-availability section.

(3) The central claim is supported: the manuscript adequately demonstrates a reproducible public-DESI-ID recovery and quality-gated 181-row catalog, provided the final catalog and code artifacts are archived exactly as described.