# INT API Review — P4 v1.0.241 — grok (grok-4.3)
paper: P4  version: v1.0.241  model: grok-4.3
provenance: commit=4420453d2ae3614bc08bd22eec9454df3b3546b5  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=d6eded1df29da5d2ccf6acb1e04277876289ae1547a1b8a3d2fda819ae7097f2
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-14T10:20:40.137223Z  |  latency: 60.4s  |  attempt: 1
usage: {"input_tokens": 36409, "input_tokens_details": {"cached_tokens": 192}, "output_tokens": 1022, "output_tokens_details": {"reasoning_tokens": 735}, "total_tokens": 37431, "num_sources_used": 0, "num_server_side_tools_used": 0, "cost_in_usd_ticks": 478646500, "context_details": {"input_tokens": 36409, "output_tokens": 1023}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MINOR] Sec. II B and VI A: The 66.5% CE-ResNet pseudo-label fraction and resulting shuffle-null limitation are acknowledged, but the model-independent GZ1-human-only null (z = −0.54σ at N = 4.60 × 10^4) should be elevated to the abstract and introduction as the decisive independence statement.
[MINOR] Sec. IV D and Appendix D: Multiple internal “artifact pipelines/...” paths and git-commit references render the text non-self-contained; these must be replaced by public data-release DOIs or removed.
[MINOR] Sec. IV C: The pre-registration claim for the p_eq > 0.6 cut is documented only via an internal commit hash; a frozen public tag or supplementary note is required for reproducibility.
[MINOR] Table I and Sec. III B: The estimator hierarchy table is internally consistent but the distinction between “primary” real-space results and “diagnostic” harmonic residuals must be restated verbatim in the abstract to prevent misinterpretation of the +3.64σ/+7.28σ values.

(3) The central claim of a statistically null real-space chirality dipole is supported by the pre-specified HC estimator, block-bootstrap template fit, and fully model-independent GZ1 cross-check.