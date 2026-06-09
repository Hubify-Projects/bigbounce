# P4 auto-2026-06-08_1737pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 257.1s

---

# Meta-Review of P4 — Galaxy Chirality Catalog Manuscript

**Meta-referee role:** systematic blind-spot audit across all 5 prior reports. Below are findings the prior 5 reviewers did NOT catch (or caught only in passing without developing the implication).

---

## ESSENTIAL findings (new)

### P4-META-E1 — The falsification criterion is logically self-contradictory
**Section:** Abstract, p. 1; §VII(d), p. 8.
**Why missed:** All 5 reviewers attacked the falsification *language* (Shamir comparison, overreach) but none worked out the logic of the criterion itself.
**Quote:** "A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% (the demonstrated empirical 50%-recovery-at-3σ threshold under the adopted per-pixel-shuffle null on the HC pipeline) would falsify the present null."
**Problem:** A null measured with only **50% recovery probability at A = 0.75%** does NOT exclude A = 0.75% signals — it is consistent with them by construction. A future 5σ detection at A = 0.75% would therefore be entirely **consistent** with the present non-detection, not a falsification. To falsify "the present null" coherently the future detection must be at an amplitude the present analysis would have detected with high probability (e.g., A ≳ 1.5–2%, where recovery would be ≫ 50%). As written, the criterion is unfalsifiable in either direction.
**Fix:** Re-derive the falsification threshold as the amplitude at which the present analysis would have detected at ≥ 95% probability, not the 50%-recovery point. State it explicitly: e.g., "future detection at σ > 5 with A ≳ A₉₅ would be in tension with the present non-detection."

### P4-META-E2 — Hidden estimator (+4.31σ) in Appendix E contradicts the headline +0.43σ
**Section:** Appendix E(b), p. 11.
**Why missed:** All 5 reviewers parsed the main-body estimator chain but did not register that Appendix E silently introduces a *different* Catalog-C estimator giving a 10× larger σ.
**Quote:** "the Catalog C-full **+4.31σ monopole-preserving dipole** collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict), consistent with the headline 0.43σ real-space dipole."
**Problem:** A +4.31σ Catalog-C dipole estimator is nowhere in Table I, Section IV C, or the headline results. The text presents it as "consistent with 0.43σ" but +4.31σ vs +0.43σ is a factor-10 discrepancy at the same nominal sample — these are NOT consistent. The "monopole-preserving" qualifier is undefined; either it is a third estimator concealed in the appendix or it is a typo. Either way, the headline null silently sits next to a buried +4.3σ measurement on the same data.
**Fix:** Either (a) add the "monopole-preserving dipole" estimator to Table I with full null definition and explain why it is +4.31σ when the demonopole-subtracted version is +0.43σ, or (b) acknowledge that this is *the same estimator before subtracting the global 0.5294% monopole*, in which case it does not measure a dipole at all but the projection of the monopole onto the dipole basis under the mask — and remove the "consistency with headline" claim.

### P4-META-E3 — The "Declared Analysis Hierarchy" is post-hoc, not pre-registered
**Section:** §III A, p. 3.
**Why missed:** All 5 reviewers accepted the hierarchy as given; none asked when it was declared.
**Problem:** §III A lists primary estimators (real-space +0.43σ, subsample-mask MASTER −0.122σ) and demotes the canonical-mask MASTER (+3.64σ) to "diagnostic." But the manuscript also describes the canonical-mask result as the natural matched-footprint estimator (fsky = 0.49005 = exactly the data footprint); the strict-superset subsample mask (fsky = 0.659) extends beyond where the data actually live — this is a non-standard choice that needs justification. The paper does not document whether this hierarchy was set before computing the three values, or chosen after seeing that one gave null and the other gave +3.64σ. The "strict-superset subsample mask" is operationally a footprint *larger* than the canonical data footprint, which is the unusual choice; a pre-registered analysis would have used the canonical mask.
**Fix:** State the date the hierarchy was declared relative to the data analysis. If it was post-hoc, label it as such. If pre-registered, point to the commit/registration. Justify why a fsky=0.659 mask is preferred over a fsky=0.49005 mask when the data only live on the latter.

---

## MAJOR findings (new)

### P4-META-M1 — Two primary estimators measuring the same physics give opposite signs; no consistency check performed
**Section:** §III A, §IV C; Table I.
**Why missed:** Reviewers tested each estimator individually but did not test whether the two "primary" estimators agree.
**Problem:** Real-space dipole = **+0.43σ** (positive). MASTER ℓ=1 = **−0.122σ** (negative). Both estimators are computed on the *same* Catalog C, on substantially overlapping masks, measuring the same ℓ=1 multipole. They should agree to within their joint noise. The paper presents both as "null" and moves on, but the sign disagreement is non-trivial: a real-space dipole vector pointing one direction and a harmonic ℓ=1 mode of opposite sign indicates that either (a) the two estimators are measuring different projections of the same field that happen to cancel, or (b) the noise dominates both at the level where signs are uninformative. Case (b) means the estimators carry less information than reported.
**Fix:** Compute the formal correlation between the two estimators under the null. Report the joint test statistic. If the two are noise-dominated (likely), the manuscript should weaken language about "two complementary reductions" producing "null."

### P4-META-M2 — Z2 vs D4 TTA shifts mean ⟨p_CW⟩ by 0.0016, which is the same order as the claimed sensitivity floor
**Section:** §III C, p. 3; Appendix B(c), p. 9.
**Why missed:** Reviewers focused on the D4 vs Z2 mismatch between figure caption and body, but not on the *magnitude* of the validation discrepancy.
**Quote:** "mean per-galaxy PCW stable under Z2 and D4 to within |Δ⟨pCW⟩| < 0.0016."
**Problem:** 0.0016 = 0.16% systematic shift between Z2 and D4 TTA on the SAME 2000-galaxy hold-out. The headline empirical sensitivity floor is 0.75% (factor 4.7 above this) and the Fisher floor is 0.29% (factor 1.8 above this). A 0.16% methodological-choice systematic between two equally-defensible TTA groups consumes ~25% of the empirical sensitivity floor and 55% of the Fisher floor. The 0.16% shift is described as "stable", but it is in fact comparable to the precision the paper claims to defend, and the production choice (Z2) was selected without quantitative justification that it is the optimal/unbiased one.
**Fix:** Either (a) include the |Δ⟨pCW⟩| < 0.0016 shift as a TTA-protocol systematic added in quadrature to the noise budget, or (b) demonstrate that Z2 is the unique unbiased choice via a theoretical argument (currently asserted but not proven). The "rotation-TTA probes classifier non-equivariance rather than chirality assignment" argument is verbal, not quantitative.

### P4-META-M3 — Effective independent sample size after classification noise dilution
**Section:** §VI A, p. 7.
**Why missed:** Reviewers pushed on the κ = 0.40 propagation logic but didn't compute its consequence for the full-catalog sensitivity.
**Problem:** With GZ1-anchored accuracy a = 0.6991, the signal dilution is g = 2a−1 = 0.398, so effective independent N for a *binary* chirality observable is N_eff ≈ N × g² ≈ 0.158 × N. On the full catalog this gives N_eff ≈ 0.158 × 3,201,160 ≈ **506k effective spirals**, essentially identical to the HC subsample of 471k. This means the full-catalog primary estimators carry *no more statistical information* than the HC subsample on which the sensitivity floor was derived. The paper presents full-catalog −0.122σ and HC injection-recovery 0.75% as separate stages, but they are statistically equivalent. This also implies the Fisher floor calculation (0.29% from raw counts) is an overstatement by factor ≈ 2.5 — the true Fisher floor under classification noise is ≈ 0.73%, essentially identical to the empirical 0.75%.
**Fix:** Re-derive the Fisher floor with the dilution factor included: σ(A_eff) = σ_binomial / g. Reconcile with the empirical injection-recovery threshold. State explicitly that the full-catalog estimators do not improve on the HC subsample in effective N.

### P4-META-M4 — Possible duplicate sources from DECaLS/DES/BASS overlap regions never deduplicated; Iye et al. explicitly cited this as a problem in Shamir
**Section:** §II A, p. 2.
**Why missed:** No reviewer cross-checked whether the cited methodological critique of Iye et al. was applied to the present pipeline.
**Quote (Sec. I):** "Iye et al. (2021) [5] re-examined Shamir's SDSS spiral catalog ... and found no significant dipole **after correcting for reading-direction bias and photometric-object duplication** in earlier Shamir catalogs."
**Problem:** Iye et al.'s critique flagged photometric-object duplication as a primary systematic. DR8 explicitly has overlap regions (DECaLS+DES overlap; BASS+MzLS+DECaLS boundary at δ=+32°). The paper acknowledges these legs (§II A) but does not state whether duplicate sources have been removed at the dr8_id level. With 8.47M objects and degree-scale overlap, duplicates could be 10⁵-scale and spatially structured along the leg boundaries — exactly the place where the per-imaging-leg signal (DECaLS-concentrated +4.50σ) shows up.
**Fix:** Report the deduplication procedure on dr8_id. Quantify the duplicate fraction. Test whether removing duplicates changes the per-leg signal. The paper's central methodological corroboration of Iye et al. is undermined if the same fix is not applied.

### P4-META-M5 — The 99.3% monopole-only reproduction is a single-mode statistic and is not generalized to the other "monopole-leakage-attributed" bandpowers
**Section:** §IV D, Fig. 4, Table III.
**Why missed:** Reviewers questioned the seed/uncertainty of the 99.3% number itself but did not notice that Table III attributes σ = +6.097 at ℓ_eff=4 and σ = +2.2–2.6 at higher bandpowers to "mask-coupled monopole leakage" — the same mechanism — without ever showing the monopole-only null reproduces those bandpowers too.
**Problem:** If the leakage hypothesis is real, the monopole-only generative null should reproduce the **entire low-ℓ excess**, not just ℓ=1. Showing 99.3% at ℓ=1 while leaving ℓ_eff=4 at +6σ with the "mask coupling" label is a single-mode test extrapolated to a multi-bandpower hypothesis. The χ²/dof = 161.2/38 = 4.24 quoted at the bottom of Table III is large — if the monopole-only null reproduces this, that needs demonstration.
**Fix:** Add a figure showing the monopole-only generative null's predicted Cℓ across all 38 bandpowers vs the data. The reader needs to see the leakage hypothesis tested at ℓ > 1.

### P4-META-M6 — Single-mode ℓ=1 estimator has very few effective degrees of freedom; the −0.122σ is fundamentally limited
**Section:** Appendix A; §IV C.
**Why missed:** Reviewers treated the −0.122σ as a sharp estimator without working out the underlying mode count.
**Problem:** A single-mode ℓ=1 NaMaster estimator at fsky = 0.659 has (2ℓ+1) × fsky ≈ 2 effective independent modes. The pseudo-Cℓ estimator at this mode count is highly non-Gaussian and has fractional std ≈ √(2/N_modes) ≈ √1 = 100% — i.e., σ_null × 1.0 represents the natural Cramér-Rao scale. With N_MC = 500 the *estimator of* σ_null also has fractional uncertainty √(1/998) ≈ 3.2%. Reporting the result as "−0.122σ" with three significant figures vastly overstates the precision the estimator can deliver. The honest statement is roughly "consistent with null at the few-tenths-σ level, but the test has limited resolving power."
**Fix:** Quote −0.12 ± 0.03 σ (or just −0.1σ to one significant figure). Add a note about the effective mode count at ℓ=1 single-mode under the given mask.

### P4-META-M7 — Per-imaging-leg σ inconsistency: 4.50σ vs 4.72σ in adjacent sentences
**Section:** Appendix C(e), p. 10.
**Why missed:** Reviewers caught arithmetic errors elsewhere but not this proximate pair.
**Quote:** "BASS+MzLS +0.30σ / DECaLS **+4.50σ** / DES +2.46σ: the signal is DECaLS-concentrated... Under the 15-cell joint label-shuffle max-statistic null (N_MC = 5,000), the family-corrected p-value is 0.0086 (≈ 2.4σ family-wise), appropriately downgraded from the cell-level **+4.72σ**."
**Problem:** The "cell-level" value is quoted twice in the same paragraph as +4.50σ and +4.72σ. Either there are two different cells being conflated, or one of the numbers is wrong.
**Fix:** Reconcile the two numbers; if they refer to different cells, label them.

### P4-META-M8 — Galactic foreground / E(B-V) stratification mentioned but never tested
**Section:** §IV E, p. 6.
**Why missed:** Reviewers noted that "galactic-foreground axes" appears in the conclusion sentence but didn't check whether any test was actually run.
**Quote:** "the canonical-mask residual is structured along classifier-systematic, footprint-systematic, **and galactic-foreground axes**, not along a primordial-dipole-aligned axis."
**Problem:** No section of the paper presents a test of the chirality field against E(B−V) extinction, galactic latitude binning, or dust-template cross-correlation. The phrase "galactic-foreground axes" is asserted in §IV E and Appendix C(b) (SGP gives +2.02σ "consistent with the dust-correlated foreground zone") but no quantitative dust regression is performed. The DECaLS-concentrated +4.5σ signal sits in low galactic latitude regions where extinction is high; a direct E(B−V) regression is the obvious test.
**Fix:** Either run the E(B−V) regression (5 minutes of work with the publicly available SFD/Planck dust maps) or remove the "galactic-foreground axes" claim.

---

## MINOR findings (new)

### P4-META-m1 — Hemisphere 50%-recovery vs Bonferroni arithmetic
**Section:** §VI, p. 7; Appendix C(c).
**Why missed:** Reviewers noted the hemisphere σ inconsistencies but did not check the Bonferroni arithmetic.
**Problem:** Bonferroni × 650 of p ≤ 10⁻⁴ gives p ≤ 0.065 ≈ 1.85σ, not "<1σ" as claimed. Either the correction factor is much larger than 650 or the post-LEE significance is mis-reported.

### P4-META-m2 — DR8 footprint specification (δ > +32° vs <+32°) does not partition the sky
**Section:** §II A, p. 2.
**Problem:** "BASS+MzLS (δ > +32°), DECaLS (δ < +32°), and a DES overlap region" — δ=+32° boundary is sharp but real footprints have ~1° transition zones with dual coverage; the DES region overlaps DECaLS extensively. The descriptions imply mutually exclusive partitions which is not how DR8 is organized.
**Fix:** Cite Dey et al. 2019 [8] Table 1 properly.

### P4-META-m3 — Catalog C "+0.4% excess" for Catalog B contradicts Table II
**Section:** §III D, p. 3.
**Quote:** "Catalog B (Platt-calibrated, +0.4% excess)"
**Problem:** Table II reports Catalog B at fCW = 0.504, i.e. +0.4%. But Catalog A is reported as +0.79% in Table II and Catalog C as −0.26%. The §III D parenthetical fact that B is +0.4% excess is correct but the framing as if calibration produces an excess is misleading — calibration moved A's +0.79% down to B's +0.4%, then equivariance moved B's +0.4% to C's −0.26%. The narrative of monotonic improvement is broken by the sign flip at the C step (caught indirectly by R1 but not in this framing).

### P4-META-m4 — "(b/a < 0.3)" edge-on identification: source unspecified
**Section:** Appendix E(a), p. 11.
**Problem:** "65.7% of visually identified edge-on systems (b/a < 0.3) receive CW or CCW classifications." Where does b/a come from? Galaxy Zoo DESI? DR8 sweep? The number of "visually identified" edge-on systems is not given.

### P4-META-m5 — Spiral fraction 37.78% vs 39.2% (Fig. 2 pie sum / total)
**Section:** §IV A vs Fig. 2.
**Problem:** This is implied by R1's Fig. 2 arithmetic check but not stated as a separate finding: the pie chart implies spiral fraction 3.32M/8.47M = 39.2%, while §IV A reports 37.78%. The difference (~120k galaxies) is much larger than the rounding scale and likely reflects Fig. 2 showing a different tier.

---

## NIT findings (new)

### P4-META-N1 — "Cohen's κ = 0.40" without specifying which Cohen's κ
**Section:** §II B, p. 3.
**Problem:** Cohen's κ for binary classification with class prior far from 50/50 has substantially different interpretation than balanced κ. The catalog has CW ≈ CCW so this is probably fine, but the κ formula (with vs without prevalence/bias correction) should be specified.

### P4-META-N2 — "P(σ > 3)" is loose language
**Section:** §VI A, p. 7.
**Problem:** "P(σ > 3) = 0.55 at A = 0.75%" should be P(|σ| > 3) or P(σ_measured > 3 | A_true = 0.75%); the conditional and the sign convention are ambiguous.

---

## Meta-review recommendation

**REJECT** (or REJECT-AND-RESUBMIT-AS-NEW with extensive overhaul).

Given the union of all 6 reviews, the **blocker count is approximately 35–40 distinct ESSENTIAL/MAJOR findings**, with at least 10 ESSENTIAL items: (i) Fig. 1 D4-vs-Z2 mismatch, (ii) Fig. 2 wrong catalog tier, (iii) Fig. 3 wrong colorbar in caption, (iv) Fig. 4 caption-figure mismatch, (v) Appendix A two contradictory field definitions, (vi) +3.64σ vs p=0.030 conversion inconsistency, (vii) Table II Dev(σ) signs/arithmetic, (viii) Table III arithmetic and unit problems, (ix) version-history language and "June 2026" date in the body, (x) falsification criterion logically self-contradictory (this meta-review), plus catalog/dataset URLs that do not resolve, the hidden +4.31σ Appendix-E estimator, post-hoc analysis-hierarchy declaration, sign disagreement between primary estimators, single-mode estimator precision overstated, no deduplication audit, no dust/extinction test, and a Z2-vs-D4 methodological systematic at the order of the headline sensitivity. My confidence that the paper as currently written would survive non-bigbounce external peer review at PRD is **<5%**; the underlying analysis may well be scientifically defensible after correction, but the manuscript-level density of arithmetic errors, caption-body mismatches, hidden estimators, and self-contradictory logic chains is too high for the journal's standards. A fully revised, pre-registered, ≤8-page manuscript with corrected figures, a single declared field definition, completed (not "in queue") generative-null runs, an honest precision statement for the −0.122σ result, and a coherent falsification criterion could plausibly clear the bar — but that is effectively a new paper, not a revision.