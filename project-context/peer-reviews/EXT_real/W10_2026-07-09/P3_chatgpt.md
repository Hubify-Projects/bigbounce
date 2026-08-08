chat: https://chatgpt.com/c/6a4fda11-7f34-83e8-b8fb-9c59d1f9a5e0
reviewer: ChatGPT (GPT-5 Thinking) | paper: P3 v3.1.146 | date: 2026-07-09
VERDICT: Major Revisions (5-6 MAJOR, all presentation/framing + all self-disclosed; NEOWISE-injection is only methodological one). Same as R9 baseline MAJOR — ChatGPT harsh-referee floor.
---RAW---
VERDICT: Major Revisions

CENTRAL CLAIM: The paper’s main claim—that BigAE produces a reproducible multi-survey anomaly-candidate catalog with a validated 268,519-object catalog-grade subset—is partially supported, but the validation standard is uneven across survey components and the headline framing remains too complicated for a strong PRD publication. 

w_P3

ISSUES:

MAJOR — §III/Table I/§VII: The paper reports several competing headline counts: 377,482 inclusive, 268,519 validated, 377,282 point-source, 274,353 pre-dedup, plus excluded eROSITA/Gaia/ACT/LAMOST tiers. This is transparent but still too confusing. Fix by making the validated 268,519 the sole abstract/conclusion headline and moving exploratory/process-volume totals to a secondary table.

MAJOR — §III H/§VI D(ii)/Fig. 10: NEOWISE is included in the validated subset despite passing only a mask-geometry QA gate “by construction,” not a detector-sensitivity test. Either remove NEOWISE from “validated catalog-grade” or run a real signal-injection recovery test.

MAJOR — §III C/Table I: The SDSS 77,905 tier is a fixed-size continuity slice, not a physically or statistically motivated anomaly threshold; the native strict S>5 result is only 12 sources and the top-1% set is 19,253. Fix by defining one primary SDSS threshold before catalog construction and using it consistently.

MAJOR — §III A/Table II: DESI’s full-stream count is dominated by non-primary science targets, with only 2,468 science-class matches. The manuscript discloses this honestly, but the abstract’s large process-volume framing still risks overclaiming. Fix by foregrounding the 2,468 like-for-like DESI science-target result.

MAJOR — §V/§VII: The cosmological applications are not PRD-level results: fNL improvement is consistent with zero, and the NANOGrav Bayes factor applies only against an idealized circular SMBHB reference. The paper discloses this, but these sections should be shortened or moved to an appendix.

MINOR — §II B: Full-sample scaler fitting for eROSITA/NEOWISE is acknowledged and partly bounded, but future-proof validation should use train-only scalers uniformly.

MINOR — §IV B: The spatial χ² test is dominated by footprint geometry and is correctly caveated; it should be removed from the main result list.

MINOR — Figures 3, 8, 10: Several captions contain long caveats and non-catalog score-axis warnings. Simplify figures or split diagnostic plots from catalog-result plots.
