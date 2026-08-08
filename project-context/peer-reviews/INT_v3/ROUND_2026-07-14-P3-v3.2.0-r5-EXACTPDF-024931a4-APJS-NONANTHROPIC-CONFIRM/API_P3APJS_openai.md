# INT API Review — P3APJS v3.2.0-r5 — openai (gpt-5.5)
paper: P3APJS  version: v3.2.0-r5  model: gpt-5.5
provenance: commit=7cf60218b521a8154f9ad6ed3b58c0bbc420ab59  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=024931a40e88124f75f2f6872549936e909db0a3b504dbd2e4e68e91878a39dc
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T17:45:46.835342Z  |  latency: 72.7s  |  attempt: 1
usage: {"input_tokens": 15702, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 3677, "output_tokens_details": {"reasoning_tokens": 2588}, "total_tokens": 19379}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Sections 3.1, 3.4, 4.3, and title/abstract — The manuscript’s central phrase “public-ID recovery” requires a quantitative false-association analysis. The all-neighbor and cluster-separation checks show internal uniqueness, but they do not estimate the probability that an unrelated DESI science target falls within 1″ of one of 190,015 historical cluster positions. A random-shift/local-surface-density test is needed, especially for the 11 objects in the 0.1–1″ tail and for P3-DESI-000030, whose recovered public target is 1.979″ from the canonical original DESI anomaly member.

2. [MAJOR] Sections 2.1, 5.1, and 7 — The anomaly-selection provenance is not sufficiently reproducible to support the word “anomaly” without stronger qualification. The manuscript states that the production normalization, resampling, object-to-spectrum mapping, and sensitivity function are unavailable, so the score cannot be regenerated from public spectra. This is acceptable for a recovery catalog only if the title, abstract, and catalog metadata make unmistakably clear that these are “historical anomaly-list positional recoveries,” not independently reproducible anomaly detections.

3. [MAJOR] Data Availability and Section 6.4 — The data-release/version story is too complicated for an archival ApJS catalog paper. The manuscript mixes v3.2.0-r2, r3 audits, r4 AAS submission assets, and r5 closure/auxiliary products, while the journal digital asset DOI is explicitly not yet assigned. Before acceptance, the authoritative primary table, auxiliary warned table if cited, scripts, manifests, and dictionaries must be deposited in a durable, immutable location with final checksums, and the manuscript must clearly state which exact artifact is the citable catalog.

4. [MAJOR] Sections 3.3 and 4.1 — The ZWARN=0 cut removes 2,267 of 2,448 global-primary matches, i.e. 92.6%, but the manuscript gives only limited characterization of the rejected population. Since this cut dominates the catalog definition and is likely correlated with unusual spectral morphology, the paper should include a more complete comparison of accepted versus rejected-primary rows in redshift, SPECTYPE, target bits, score, separation, and DELTACHI2, even if no correction is attempted.

5. [MAJOR] Sections 3.3 and Appendix A — The selection rule uses target-to-cluster separation, not target-to-original-DESI-member separation, yet the scientific interpretation depends on associating a historical DESI anomaly member with a public DESI TARGETID. The manuscript should justify this choice more explicitly, provide a per-row flag for original-member separation tier, and state whether any candidate would be dropped under a 1″ target-to-original-member rule.

6. [MINOR] Section 2.2 and Data Availability — The DESI input file is validated by checksum, byte ranges, and live endpoint metadata, but the manuscript also mentions a stale May 2026 provenance sidecar with a different SHA-256. This is potentially confusing; move the stale-value discussion to an audit appendix or state more plainly that it is not part of the reproducible input definition.

7. [MINOR] Table 3 — The “Binary components” column should be typeset unambiguously as powers of two, e.g. \(2^1\), \(2^2\), \(2^{11}\), not in a way that can be read as 21, 22, or 211 in extracted text.

8. [MINOR] Table 5 and Section 4.2 — Displaying the two negative-redshift objects as \(z=-0.000\) is confusing. Give enough significant figures in the table, or mark them explicitly as small negative Redrock redshifts retained by the declared selection.

9. [MINOR] Sections 3.2 and Table 1 — Clarify that bits 60 and 61 are DESI_TARGET bits corresponding to BGS_ANY and MWS_ANY, distinct from the separate BGS_TARGET and MWS_TARGET columns that are carried as metadata but not used in the Boolean selection.

10. [MINOR] Figures 1–2 — The figures are useful, but the separation-tail panel would be clearer if it directly annotated the counts above 0.1″, 0.5″, 0.75″, and 1″, since those numbers are important to the positional-association argument.

11. [MINOR] References and acknowledgments — Several software/data-model references are web pages or versioned documentation without persistent identifiers. Where possible, add DOIs or archived access information, and ensure the DESI acknowledgment text matches the current DESI DR1 required wording.

(3) The central claim that 181 warning-free global-primary DESI DR1 rows can be exactly rejoined under the declared cuts is substantially supported, but the stronger interpretation that all 181 are secure recovered anomaly-source counterparts requires the positional false-match, versioning, and upstream-provenance issues above to be resolved.