# INT API Review — P4 v1.0.243 — grok (grok-4.3)
paper: P4  version: v1.0.243  model: grok-4.3
provenance: commit=36badcbdf498123413031aa0a9504127d48f2054  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=9e73fd888699058d421043b0dd2de5d37d2aeb36fe37e8dd1c0bf5409e947d19
packet: key=6d2c08bf438c01b7b50b3d5eb9ffbbc82cae8d0257d89a3f578b696b0dcaa60b  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-14T19:08:17.893762Z  |  latency: 39.2s  |  attempt: 1
usage: {"input_tokens": 35422, "input_tokens_details": {"cached_tokens": 192}, "output_tokens": 1166, "output_tokens_details": {"reasoning_tokens": 740}, "total_tokens": 36588, "num_sources_used": 0, "num_server_side_tools_used": 0, "cost_in_usd_ticks": 469909000, "context_details": {"input_tokens": 35422, "output_tokens": 1168}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Sec. I (Introduction) and III.B (Declared Analysis Hierarchy): Explicitly states no formal preregistration, frozen pre-unblinding tag, or independent blinding record exists, with multiple DP4 gates (15,16,17,21) remaining open; this undermines claimed sub-percent sensitivity for a null result in a catalog/methods paper.
[MAJOR] Sec. II.B (Training Labels): 66.5% of source labels derive from CE-ResNet pseudo-labels, so the catalog and primary HC sample are not independent of prior work; shuffle-nulls and model-permutation tests cannot fully address inherited survey-correlated structure (explicitly acknowledged but not resolved).
[MAJOR] Sec. VI.B (Statistical Scale and Finite Injection Scores) and Table IX: Stage-B deterministic-axis pilot and 100-injection fractions are reported as “descriptive tested-grid evidence” only, with no calibrated recovery curve, coverage, or physical upper bound; this directly affects interpretation of the claimed sensitivity floor.
[MINOR] Sec. IV.A (Catalog Statistics) and Appendix B.e (Bias hardening suite): Catalog-wide max-class probabilities are strongly overconfident (mean 0.951 vs. external GZ1 accuracy 58.7–69.91%); the flip-identity QC flags 2.9% of HC rows and the T7 proxy is a sanity check rather than a full ECE calibration, requiring explicit user guidance in the released catalog metadata.
[MINOR] Sec. VII (Conclusions) and Table X: Harmonic-channel injection scores and MASTER diagnostics are presented as “systematics-attributed” only, yet the abstract and title emphasize an 8.5-million-galaxy catalog whose primary cosmological claim rests on a single estimator; clearer separation of catalog release from the null-result interpretation is needed.

(3) The central claim (HC real-space observed-label dipole null at +0.55σ) is supported by the declared primary estimator and its isotropic pixel-permutation test.