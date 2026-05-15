# P4_v1078_R3 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1645pt
**Wall time**: 23.7s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=64697, completion=2545, reasoning=1655, total=67242

---

**PAPER-GRO-B1: N=500 monopole null reproduction claim**

**Classification:** BLOCKER

**Section:** Abstract (para 1) and §monopole_mask_null (Table IV)

**Issue:** The 99.3% pre-MASTER pseudo-C1 reproduction (observed 1.696e-2 vs null mean 1.685e-2) is reported as explaining prior literature claims, but the smoke-test snapshot used 4.23e-2; the discrepancy is attributed to mask cut / N_spiral recount without explicit quantification of how much of the difference is methodological vs geometric.

**Fix:** Add one sentence: "The current observed pre-MASTER value (1.70e-2) is lower than the v1.0.77 smoke snapshot (4.23e-2) due to the canonical N_spiral=3.2M recount and mask definition; the 99.3% figure applies strictly to the present pipeline and mask."

**PAPER-GRO-B2: Overclaim on resolving Shamir-class controversy**

**Classification:** MAJOR

**Section:** Abstract (final para) and §conclusions (headline finding)

**Issue:** The text repeatedly states the leakage "explains" or "resolves" prior 2–4% claims at the percent level, yet explicitly notes no matched-footprint Ganalyzer reanalysis was performed; this creates a false impression of closure while the formal exclusion caveat is buried.

**Fix:** Replace "resolves at the present sub-percent sensitivity" with "disfavors at the amplitude level under the present ViT-Small + DESI Legacy pipeline; a like-for-like Ganalyzer reanalysis on the same footprint is required for a formal exclusion."

**PAPER-GRO-B3: Sensitivity floor framing**

**Classification:** MAJOR

**Section:** Abstract and §sensitivity (injection sweep)

**Issue:** The abstract and sensitivity section lead with "sub-percent sensitivity" and Fisher ~0.29%, but the load-bearing empirical result is the 50%-recovery threshold at A=0.75% (P(σ>2)=0.18 at 0.5%); the gap is not clearly labeled as the operative detection floor.

**Fix:** Change the abstract sensitivity sentence to: "Systematic-inclusive sensitivity is |A_dipole| ≳ 0.5% (50%-recovery threshold under per-pixel-shuffle nulls); the statistical Fisher floor is ~0.29% full-amplitude."

**PAPER-GRO-B4: Hemisphere max-statistic interpretation**

**Classification:** MAJOR

**Section:** §hemisphere and §monopole_mask_null

**Issue:** The +4.42σ hemisphere max|A| with only 49% monopole-null reproduction is reported as "consistent with null" after LEE, yet the direct MC rejects random-label null at p_LEE ≤ 10^{-4}; the attribution to depth/PSF systematics is asserted without a quantitative cross-power test.

**Fix:** Add: "The residual +4.42σ after monopole projection indicates additional depth/PSF coupling; a per-pixel PSF-ellipticity cross-power with the CW map is required to close this channel."

**PAPER-GRO-B5: D4-TTA holdout statistical power**

**Classification:** minor

**Section:** §tta (D4-TTA paragraph)

**Issue:** The 1,558-galaxy holdout has 1.3% Poisson floor (5× larger than the 0.26% monopole), yet is used to claim "rotation invariance in expectation"; this understates the inability to rule out rotational contribution at the monopole amplitude.

**Fix:** Change to: "The 1,558-galaxy holdout confirms mean p_CW invariance but has insufficient power to exclude a rotational component at the 0.26% monopole level; a full-catalog D4 re-inference is required."

**PAPER-GRO-B6: Headline table internal consistency**

**Classification:** nit

**Section:** Table I (headline_summary)

**Issue:** Row (i) lists N_catalog_spiral but leaves map_weighted as "---"; row (vi) uses HC subsample while others use full 3.2M; the N_MC column is omitted entirely.

**Fix:** Add explicit N_MC column and footnote the HC vs full distinction for row (vi).
