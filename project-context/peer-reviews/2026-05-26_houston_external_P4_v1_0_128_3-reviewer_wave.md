# Houston-dispatched external referee wave — P4 v1.0.128 — 2026-05-26

**Source:** Houston ran 3 external referees (Gemini + Grok + ChatGPT) on P4 v1.0.128 PDF
via direct chatbot interfaces (not OpenRouter API). Verdicts:
- **Gemini-MNRAS** referee: MAJOR REVISIONS — 3 BLOCKERs + 2 MAJORs + 2 MINORs
- **Grok-MNRAS/PRD/JCAP** referee: MAJOR REVISIONS — 2 BLOCKERs + 2 MAJORs + 3 MINORs
- **ChatGPT-MNRAS/PRD/JCAP** referee: REJECT in present form — 9 BLOCKERs + 10 MAJORs + 12 MINORs

This is materially harder than the OpenRouter API wave (which had P4 at all-5/5-clean R-ext fire #87).
Houston's manual external is more demanding than the API-vendor headless review.

## Shared cross-reviewer findings (universally agreed)

### S1 — AI-audit / version-history prose contamination (ALL THREE)
- Gemini-BL3, Grok-BL2, ChatGPT-B9 + ChatGPT-m5/m11
- Must purge from manuscript body: version tags (v1.0.107, v1.0.117, etc.),
  reviewer references (Grok-B1, Gemini-B2, OpenAI external review, Perplexity R22, etc.),
  cron-fire/pod-cycle/queued-for-next-revision operational language.

### S2 — "Three-interpretation closure" overclaim (ALL THREE)
- Gemini-BL1, Grok-BL1 (MASTER-monopole-promotion), ChatGPT-B2/B3
- The +3.64σ canonical-mask residual is NOT closed. Three discriminators (ℓ=2 dominance,
  no p_eq quartile scaling, density-proxy cross-spectrum) are diagnostic, not formal closure.
- Required: rename "closure" → "diagnostic evidence for systematic" OR perform a real
  joint nuisance-marginalized model fit (primordial dipole + depth/PSF/morphology templates).

### S3 — Stale release tags
- Grok-BL2, ChatGPT-B8: v1.0.122 vs v1.0.128 mismatch in abstract footer, footnotes,
  Data Availability section.

### S4 — Hard-label argmax 21% flip rate propagation
- Gemini-BL2, ChatGPT-B6: continuous soft probabilities used for primary load-bearing
  MASTER calc, but hard labels used for confidence strata (Table VII), strict HC injection-
  recovery (Table XIII), face-on robustness (Table XIV). The 21.4% rotational flip rate
  must either propagate into empirical variance bounds OR diagnostics must use soft
  probabilities.

### S5 — MASTER-decoupled monopole-only null promotion
- Grok-BL1: the post-MASTER monopole-only result (data C1=6.55e-6 vs null mean 8.0e-7,
  12% of residual explained by monopole leakage alone, leaving ~88% to other systematics)
  is buried in Table I footnote b. Must promote to a body-text sentence in §IV.D.

## Reviewer-specific BLOCKERs

### ChatGPT-only
- B1: "Pre-registered analysis hierarchy" claim not substantiated. Required: replace
  "pre-registered" with "declared" unless time-stamped preregistration supplied.
- B4: Null models (per-pixel, global random-label, binomial monopole-only, bootstrap,
  direct max-stat MC, analytic Bonferroni/BH, MASTER null) mixed without unified inference
  target. Required: define ONE primary cosmological null + ONE systematics-preserving null;
  treat others as labelled diagnostics.
- B5: Full-catalog injection-recovery sweep deferred; HC-only sensitivity quoted as full-catalog.
- B7: Shamir comparison body text contains [2] vs [3] citation errors and ∼200,000 vs
  ∼1.3M sample-count claim issues.

### Gemini-only
- BL1 (extra detail): Required joint model fit with primordial dipole + depth/PSF/morphology
  systematics + nuisance-marginalized covariance — this is the canonical resolution that
  the paper "defers to future work".
- BL2 (extra detail): Either regenerate hard-binned diagnostics using continuous soft-
  probability weights, OR fold the 21.4% per-galaxy rotational uncertainty into the
  empirical variance bounds of injection-recovery simulations.

### Grok-only
- Stylistic: Family-level max-stat null ordering (raw |σ|=4.724 leading the family-
  corrected p=0.0086 ~2.4σ).

## MAJORs (cross-reviewer)
- ChatGPT-M1: Add systematics-preserving canonical-mask null (preserves density/depth/
  PSF/extinction/imaging-leg/morphology structure).
- ChatGPT-M2: Full systematics template regression (depth, PSF FWHM, PSF ellipticity,
  extinction, imaging leg, b/a, fracdev, size, surface brightness, type, brick-edge).
- ChatGPT-M3: MC size ≥ 10^4 for headline p-values (currently 15/500 and 2/500).
- ChatGPT-M4: Expose null means + covariance + correlation matrix for all bandpowers.
- ChatGPT-M5: Single "data vector definitions" table.
- ChatGPT-M6: Full-catalog D4-TTA closure (currently only ∼2k holdouts).
- ChatGPT-M7: Morphology systematics evidence stronger than prose admits (deep-MLP
  AUC=0.5656); must be treated as primary nuisance source.
- ChatGPT-M8: Hemisphere analysis: pick ONE primary hemisphere null.
- ChatGPT-M9: Limit Shamir-inconsistency claim to "under present ViT/TTA pipeline".
- ChatGPT-M10: Paper too long, split main + supplement.
- Gemini-Major1: Quantify localized fractional asymmetry variance vs pixel distance
  from canonical footprint boundary (prove superset mask doesn't dilute localized
  anomaly).
- Gemini-Major2: Explicit mathematical M_{ll'} mode-coupling matrix expression showing
  how monopole subtraction inflates ℓ=1 significance.

## MINORs (selected, cross-reviewer)
- Hyperlink corruption (Gemini-Minor2): §VIGOa, §VID0c, etc.
- Capitalization (ChatGPT-m1).
- Fused text in Table V caption (ChatGPT-m2).
- "Canonical canonical-mask" duplication (ChatGPT-m3).
- Mask label/fsky standardization (ChatGPT-m7).
- "Directly confirmed" → "suggested" for cross-spectrum (ChatGPT-m8).

## Strengths (cross-reviewer)
- Massive catalog scale (8.47M sources, 3.2M spirals) = substantial leap.
- NaMaster pseudo-Cℓ + mode-coupling deconvolution methodology rigor (CMB-grade).
- Honest D4-TTA retraction + parity-EVEN disclaimer = "exemplary".
- Pre-MASTER monopole-mask leakage demonstration alone is publishable science.

## Bottom line
- Gemini: MAJOR REVISIONS, fixable with the proposed fixes
- Grok: MAJOR REVISIONS, only blocked because v1.0.128 didn't address prior round
- ChatGPT: REJECT in present form, recommends rebuild as "DESI Legacy projected-galaxy-
  chirality catalogue and a null test of large-scale chirality anisotropy" (rename/rescope)

## Closure plan — v1.0.129+

**Phase 1 (immediate, this fire — eat-the-frog universal-agreement items)**:
- S1 — Purge AI-audit/version-history prose from manuscript body
- S2 — Reframe "closure" → "diagnostic evidence for systematic" in title + abstract + §IV.D
- S3 — Scrub v1.0.122 → v1.0.128 stale tags
- S5 — Promote MASTER-decoupled monopole-only null from footnote to body sentence
- Minor: §VIGOa hyperlink corruption fix

**Phase 2 (next fires)**:
- S4 — Hard-label 21% flip propagation OR soft-probability stratum redo
- B1 — "pre-registered" → "declared"
- B7 — Shamir body rewrite
- ChatGPT-M3 — MC size ≥10^4 for headlines
- ChatGPT-M5 — data vector definitions table
- ChatGPT-M9 — Shamir-inconsistency scope narrowing

**Phase 3 (compute-bound, may require pod)**:
- Gemini-BL1 — joint nuisance-marginalized model fit (the real "closure")
- ChatGPT-M1 — systematics-preserving canonical-mask null
- ChatGPT-M2 — full systematics template regression
- B5 — full-catalog injection-recovery sweep
- ChatGPT-M6 — full-catalog D4-TTA
- Gemini-Major1 — boundary-distance variance quantification
