# INT API Review — P4 v1.0.245 — grok (grok-4.3)
paper: P4  version: v1.0.245  model: grok-4.3
provenance: commit=54aeaae34614e24ee9d106416b46b7bbb5718128  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=e37d0af72c9d132af6324ddfa80c71d7d78bc14a2f153a7ca7b9a156cc4a2dca
packet: key=d56532979f4521342ee3b040b10a221f3391e59d54061360899a18aeb0ab8a8c  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-15T10:13:21.244025Z  |  latency: 39.5s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 39.5, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "868c2ef9-3248-9dff-8b31-d396476467c3", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "868c2ef9-3248-9dff-8b31-d396476467c3", "usage": {"context_details": {"input_tokens": 35761, "output_tokens": 987}, "cost_in_usd_ticks": 469646500, "input_tokens": 35761, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 986, "output_tokens_details": {"reasoning_tokens": 597}, "total_tokens": 36747}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT: MINOR REVISIONS**

**ISSUES:**
1. [MINOR] Sec. I & Abstract: The opening claim that the result is a “standalone observational result” whose “null dipole ... does not depend on any unpublished companion work” is undercut by the explicit statement (Sec. II B, VI A) that 67.5 % of the training pool is CE-ResNet pseudo-labels; the independence caveat must be moved into the abstract and first paragraph.
2. [MINOR] Sec. III B & Table I: The estimator hierarchy is declared internally but the text repeatedly notes the absence of preregistration, blinding, or external timestamp; the sentence “we therefore do not claim formal preregistration” should be repeated verbatim in the abstract and Sec. IV C so readers cannot mis-read the hierarchy as a registered analysis.
3. [MINOR] Sec. IV C & VI B: The finite-injection “score-crossing counts” (1/20 … 20/20) and the 100-injection fractions are presented without any statement that they are uncalibrated; a one-sentence disclaimer that “these fractions are not a calibrated recovery curve or physical upper bound” must appear in both the abstract and the caption of Table IX.
4. [MINOR] Appendix B & Data Availability: The released Parquet schema omits the raw and flip-pass probability columns (replaced by a Boolean flag); the exact SQL/Parquet filter that reproduces the quarantined 249 066 rows and the HC sample must be supplied as executable code in the Data Availability section.

**One sentence:** The central claim—that the primary HC real-space observed-label dipole (N = 949 584) is statistically consistent with the fixed-occupancy label-randomization null—is directly supported by the reported moment-z = +0.71 and rank p = 0.225.