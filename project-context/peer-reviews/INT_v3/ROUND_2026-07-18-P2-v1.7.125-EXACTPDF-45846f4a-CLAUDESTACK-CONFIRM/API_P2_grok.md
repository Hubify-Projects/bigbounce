# INT API Review — P2 v1.7.125 — grok (grok-4.3)
paper: P2  version: v1.7.125  model: grok-4.3
provenance: commit=a4c5dbaff377996308a79619c1bbeb815a5b89f4  pdf=research/focused_paper_source_integration/02_full_draft.pdf  sha256=45846f4ac780ac4663ef24a6e5d48c4924e4691b057a0cf7683399f48d534490
packet: key=af1095edad0450381cc4957030e57d6b7d3e9fd6964d6e5528e7137467ad91d2  profile=PRD-RESEARCH
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-18T08:34:58.882828Z  |  latency: 20.4s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 20.4, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "9559558a-4882-9a95-9d1b-a7f68487d575", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "9559558a-4882-9a95-9d1b-a7f68487d575", "usage": {"context_details": {"input_tokens": 21673, "output_tokens": 1113}, "cost_in_usd_ticks": 296696500, "input_tokens": 21673, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1112, "output_tokens_details": {"reasoning_tokens": 719}, "total_tokens": 22785}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Sec. II.A and Appendix B: The claimed exact four-vertex sum yielding coefficients (3,1,−9,5,−33,9) and f_NL=−35/16 is presented as a definitive correction to Cai et al., but the manuscript provides only internal script references and order-grouped intermediates rather than a fully self-contained, referee-reproducible symbolic expansion of all four Maldacena vertices at ϵ=3/2; the discrepancy with the printed polynomial is asserted but not derived term-by-term from the source expressions in a form that can be independently verified without external artifacts.
[MAJOR] Sec. IV and VII: The SPHEREx “illustrative” mappings (2.63σ, 3.5σ–0.4σ ladder) are presented with explicit numerical values derived from an in-house surrogate covariance, yet the text repeatedly states that these are conditional on unverified cubic transmission, a missing external per-triangle covariance, and free nuisance parameters; this violates PRD standards for separating theory results from forecast-style claims and risks reader misinterpretation.
[MINOR] Sec. I and II.C: Multiple assumptions (d)–(f) are listed as load-bearing yet the linear transmission calculation is scheme-specific (dressed-metric only) and the torsion bound is parametric; these should be elevated to a dedicated subsection with explicit caveats on model dependence.
[MINOR] Throughout: References to private GitHub paths, internal .py/.json files, and “research/” directories are inappropriate for a journal submission; all numerical claims must be reproducible from the published text and supplementary material alone.

(3) The central algebraic claim of an exact −35/16 amplitude from the four-vertex sum is supported by the internal consistency checks shown, while the conditional observational mapping is not.