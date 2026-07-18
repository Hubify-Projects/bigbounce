# INT API Review — P2 v1.7.125 — gemini (gemini-3.1-pro-preview)
paper: P2  version: v1.7.125  model: gemini-3.1-pro-preview
provenance: commit=a4c5dbaff377996308a79619c1bbeb815a5b89f4  pdf=research/focused_paper_source_integration/02_full_draft.pdf  sha256=45846f4ac780ac4663ef24a6e5d48c4924e4691b057a0cf7683399f48d534490
packet: key=e5a90ea35763836944ddc30fc9490abd78166d106b9923158c1a1b2337a32025  profile=PRD-RESEARCH
modality: native-PDF (inline_data base64)
UTC: 2026-07-18T08:34:58.878625Z  |  latency: 18.1s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 18.1, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "szpbaoSgNtWGz7IP_5zzyAc", "usage": {"candidatesTokenCount": 362, "promptTokenCount": 5822, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 5720}, {"modality": "TEXT", "tokenCount": 102}], "serviceTier": "standard", "thoughtsTokenCount": 1160, "totalTokenCount": 7344}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MINOR] Section IV and Table III: The "channel-native surrogate covariance" is introduced with very little mathematical description of its construction (e.g., how the multi-tracer noise, redshift binning, and overlapping populations are approximated relative to the Heinrich et al. baseline). Even though it is heavily caveated as an illustrative diagnostic, a brief mathematical definition of the surrogate Fisher matrix elements should be provided in the text or an appendix so the reader can understand the origin of the $3.5\sigma$ to $0.4\sigma$ range without having to parse the raw source code.
2. [MINOR] Throughout the text (e.g., Sec II.C, Sec II.D, Appendix B), raw repository filenames (e.g., `research/cubic_bounce_transmission/g1_dressedmetric_ic_close.py`, `scripts/p2_vertex_check.py`) are embedded directly within the narrative prose. This disrupts the reading flow of a standard journal article; these explicit file references should be moved to footnotes or consolidated in the Data and Code Availability section.
3. [MINOR] Section II.C: The order-of-magnitude estimate for the torsion-sourced correction in Eq. (5) relies on a spin-coherent proxy $\langle J_5^2 \rangle \lesssim n_\psi^2$. It would be helpful to briefly comment on the physical circumstances under which this maximal alignment is achieved or broken in the pre-bounce epoch to fully contextualize the bound.

The central claim resolving the historical factor-of-two discrepancy in the exact matter-bounce $f_{\rm NL}$ amplitude is thoroughly derived and algebraically supported.