# INT API Review — P3APJS v3.1.161-apjs — grok (grok-4.3)
paper: P3APJS  version: v3.1.161-apjs  model: grok-4.3
provenance: commit=913f5033  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=ef7065b05badbdfe8bbeaf44f04895bccbc06354044a63c1651a4a8e5d5b56d1
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-14T09:24:52.100687Z  |  latency: 27.7s  |  attempt: 1
usage: {"input_tokens": 34173, "input_tokens_details": {"cached_tokens": 192}, "output_tokens": 1039, "output_tokens_details": {"reasoning_tokens": 622}, "total_tokens": 35212, "num_sources_used": 0, "num_server_side_tools_used": 0, "cost_in_usd_ticks": 451121500, "context_details": {"input_tokens": 34173, "output_tokens": 1039}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Abstract & §1 (title claim of “268,319 validated point sources”): the headline figure is explicitly a “process-volume” count dominated by non-science-target/sky-fiber spectra (§3.1, Table 3), not a uniform set of confirmed detections; the like-for-like science-target yield is only 2,468 clusters, undermining the title framing.
[MAJOR] §3.4 & §3.5 (LAMOST & eROSITA): LAMOST is a documented 98% training-bias failure with injection-recovery FAIL (5.8%) and no per-object table released; eROSITA is excised for irreproducible score axis yet still contributes to continuity counts—both directly contradict “validated” status.
[MAJOR] §3.6 & §3.7 (Planck & Gaia): native Planck top-200 table and checkpoint are unavailable (lost on exited node); Gaia tier is synthetic/quarantined—yet both are retained in headline continuity counts and the frozen release, violating data-product completeness.
[MAJOR] §2.4 & §5.4 (validation protocol): DESI robustness rests on one production-ensemble gate plus two correlated short-proxy fold checks (val loss >0.30, not independent); NEOWISE gate is masking geometry QA only (passes by construction, not sensitivity)—the mixed, survey-specific “validation” is not equivalent across the catalog.
[MINOR] §2.2 & Table 1 (preprocessing & scan volume): full-sample scaler fits (not train-split only) introduce documented tail-churn risk; “37.3 million” headline rounds up excised tiers without explicit reconciliation in the abstract.

(3) The central claim of a uniformly validated, reproducible multi-survey anomaly catalog is not supported for ApJS because the released product is heterogeneous, contains multiple failing/excised/quarantined tiers, and lacks key per-object tables and native checkpoints.