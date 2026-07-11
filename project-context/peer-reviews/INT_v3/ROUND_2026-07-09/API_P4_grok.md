# INT API Review — P4 v1.0.235 — grok (grok-4.3)
paper: P4  version: v1.0.235  model: grok-4.3
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-11T02:31:04.062997Z  |  latency: 50.7s  |  attempt: 1
usage: {"input_tokens": 36037, "input_tokens_details": {"cached_tokens": 896}, "output_tokens": 1080, "output_tokens_details": {"reasoning_tokens": 601}, "total_tokens": 37117, "num_sources_used": 0, "num_server_side_tools_used": 0, "cost_in_usd_ticks": 468054500, "context_details": {"input_tokens": 36037, "output_tokens": 1081}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Sec. IV D and Appendix D: the post-MASTER ℓ=1 residual (+3.64σ canonical) leaves an explicit ~47% unmodeled amplitude (Ap=0.32%) whose physical origin is unresolved; the forward model of imaging+morphology templates accounts for only ~53% and the per-galaxy morphology addition raises it by only +0.7 pp, yet the paper still claims the residual is “below the real-space estimator’s recovery threshold” without a quantitative bound on any cosmological content of the remainder.
[MAJOR] Sec. IV C and VI B: the primary real-space HC dipole (+0.41σ, p=0.31) and injection-recovery floor (A95∈(1.0%,1.5%]) are reported on the peq>0.6 subsample (N=949k), but the block-bootstrap WLS template fit that disfavors Aref=0.017 (z≈−7.6) is performed on the unthresholded full Catalog C (N=3.2M) without propagating the HC selection function into the spatial covariance, rendering the two “primary” estimators statistically incommensurable.
[MINOR] Sec. II B and VI A: the 66.5% CE-ResNet pseudo-label fraction is acknowledged to limit the label-shuffle nulls, yet the model-independent GZ1-human-only test (z=−0.54σ) is performed on a sample 21× smaller than the headline HC set; its A95~4.5–6.8% sensitivity is insufficient to constrain the sub-percent inherited structure that the paper itself identifies as the remaining open systematic.
[MINOR] Sec. V A: the amplitude-level tension with Shamir (1.7–4.0% vs. present 0.455% best-fit) is stated without a matched-footprint Ganalyzer reanalysis, so the claim of “~3.7–8.8× tension” remains an estimator mismatch rather than a statistical exclusion.

(3) The central claim of a null real-space chirality dipole at sub-percent sensitivity on the high-confidence equivariant subsample is supported by the primary estimator and injection-recovery calibration.