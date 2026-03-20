# Claim Discipline Cross-Paper Check

**Created:** 2026-03-20
**Purpose:** Verify that every major claim across all three papers is correctly classified, consistently stated, and appropriately hedged. Identify claims that need softening, strengthening, or relocation.

---

## Claims That Are SAFE Across All Papers

These claims can appear in any paper without risk:

| # | Claim | Classification | Evidence |
|---|-------|---------------|----------|
| 1 | "ECH produces a nonsingular bounce at rho_crit ~ 0.27 rho_Pl" | DERIVED | Standard result in LQC effective dynamics. Well-established. |
| 2 | "The (J^5)^2 four-fermion interaction is unique" | DERIVED | Follows from algebraic torsion in EC theory. Textbook result (Hehl et al. 1976). |
| 3 | "f_NL = -35/8 is a parameter-free matter-bounce prediction" | DERIVED | Cai et al. (2009), verified by 3 independent methods in this project. |
| 4 | "SPHEREx can test f_NL at 4-6 sigma after GR marginalization" | DERIVED | Heinrich et al. (2023) sensitivity + our GR marginalization framework with 800,000 MC samples. |
| 5 | "Delta-N_eff is consistent with zero in all MCMC datasets" | FIT | 236,622 samples, 4 datasets, R-hat - 1 < 0.005. |
| 6 | "Standard single-field inflation gives f_NL ~ 0.015 (Maldacena)" | DERIVED | Maldacena consistency relation. Theorem-level. |
| 7 | "Standard curvaton cannot reach f_NL = -4.375" | DERIVED | Minimum f_NL ~ -1.25 for quadratic curvaton. |
| 8 | "800,000 Monte Carlo realizations support BF > 300 vs SSFSR" | DERIVED | Explicit computation, documented. |
| 9 | "The Holst term is topological when torsion vanishes" | DERIVED | Mathematical identity. The Holst term reduces to the Pontryagin density for T = 0. |
| 10 | "Torsion vanishes for canonical scalar field matter in EC" | DERIVED | Algebraic EC field equation: torsion proportional to spin density; scalar fields have zero spin. |
| 11 | "LiteBIRD can test the birefringence prediction at 9 sigma" | DERIVED | LiteBIRD sensitivity forecast (published). |
| 12 | "The bounce transfer function T(k) = 1 for k << k_bounce" | DERIVED | Time-reversal symmetry + 60-order scale hierarchy. |

---

## Claims That NEED_SOFTENING

| # | Claim | Paper(s) | Current Wording | Problem | Corrected Wording |
|---|-------|----------|----------------|---------|-------------------|
| 1 | ECH predicts f_NL = -35/8 | Dossier, some markdown | "ECH bounce predicts f_NL" | ECH provides the bounce mechanism, not the bispectrum. f_NL comes from matter contraction. | "Matter-dominated contraction produces f_NL = -35/8; ECH/LQC provides the nonsingular transition" |
| 2 | Bounce explains [anything] | Should not appear in papers | "the bounce explains..." | No observation REQUIRES a bounce. We have predictions, not explanations. | "the bounce model PREDICTS [X], which is testable by [Y]" |
| 3 | Tension reduction holdovers | Paper 1 (already retracted in current version) | Check for any remaining positive tension claims | Earlier versions claimed H_0 = 69.2 and tension reduction. Must be fully retracted. | VERIFY: ensure no positive tension-reduction language survives. The retraction should be clear. |
| 4 | "Detection would prove bounce" | Focused paper draft claim #16 | "Detection would prove bounce" | Exotic inflation CAN produce negative f_NL with tuning. Detection favors, not proves. | "Detection would provide strong evidence favoring bounce over single-field inflation" (already in claims table as replacement) |
| 5 | "Rules out inflation" | Focused paper draft claim #17 | "Rules out inflation" | Only rules out standard single-field. Multifield survives with tuning. | "Strongly disfavors standard single-field inflation; multifield requires 2+ tuned parameters" |
| 6 | "We independently derived f_NL" | Focused paper draft claim #18 | "We independently derived" | Cai et al. derived it. We verified. | "We independently verified the Cai et al. prediction using three methods" |
| 7 | "Definitive test" | Focused paper draft claim #19 | "Definitive test" | SPHEREx provides a strong test, not a definitive one. Systematics remain. | "Meaningful/strong test" |
| 8 | Birefringence is bounce-dependent | Should not appear anywhere | Any implication that beta depends on the bounce | The ALP birefringence prediction is entirely bounce-independent. | Must state "bounce-independent" whenever birefringence is mentioned in the context of the bounce program |
| 9 | "Cleanest explanation" | Focused paper draft claim #10 | "Bounce provides cleanest explanation" | "Cleanest" is a subjective comparative without rigorous definition | "Provides the simplest zero-parameter explanation; inflation requires 2+ tuned parameters" |

---

## Claims That NEED_STRENGTHENING

| # | Claim | Paper(s) | Current Wording | Problem | Strengthened Wording |
|---|-------|----------|----------------|---------|---------------------|
| 1 | 14-barrier closure is systematic | Paper 1 | "14 structural barriers close all routes" | This undersells the result. "A list of barriers" sounds less impressive than "a systematic CLASS-LEVEL closure." | "We demonstrate closure at the mechanism-class level: 14 named structural barriers close ALL standard routes from the bounce to dark energy, organized by mechanism type (propagating modes, geometric coupling, global integrals, initial conditions, state selection, perturbation channels). This is the first complete mechanism-class enumeration for spin-torsion dark energy." |
| 2 | Perturbation-transparency theorem | Paper 1 | Described but not given a formal name or boxed statement | A theorem-level result deserves theorem-level presentation. | Give it a formal name (e.g., "ECH Perturbation-Transparency Theorem") and present it in a boxed theorem environment: "Theorem: Minimal Einstein-Cartan-Holst gravity with canonical scalar field matter produces zero perturbation-level corrections at all orders in both scalar and tensor sectors. The Barbero-Immirzi parameter is completely invisible in perturbation observables." |
| 3 | Integrated closure + surviving-signal framework | All papers, especially Paper 1 intro | Implicit in the structure but not called out | This is the most original structural contribution and is currently invisible as a named concept. | Call it out explicitly: "The ECH program provides a complete worked example of systematic model testing: framework specification, mechanism-class enumeration, perturbation-level gate analysis, viability filtering, and forecast packaging. This architecture -- not any single result -- is the program's primary methodological contribution." |
| 4 | Wilson-Ewing as unique survivor | Paper 3 | Mentioned but not emphasized | The viability filtering (pass 2) that selected Wilson-Ewing from all candidate models is a substantive analytical contribution. | Add a sentence: "The Wilson-Ewing LCDM quasi-dust bounce emerges as the unique minimal survivor of our viability screen (0 extra fields, 1 fitted parameter, 1 parameter-free prediction)." |
| 5 | Bayesian anti-mimicry | Paper 3 | Present in analysis but could be more prominent | The BF > 300 result with prior robustness is one of Paper 3's strongest contributions. | Move the Bayesian comparison higher in the paper structure. Consider making it the second main result (after the forecast), not a subsection of the inflation comparison. |

---

## Claims That SHOULD_BE_MOVED Between Papers

| # | Claim/Content | Currently In | Should Be In | Reason |
|---|---------------|-------------|-------------|--------|
| 1 | Detailed barrier derivations (14 barriers) | Paper 1 | Paper 1 ONLY | Paper 3 should reference Paper 1 for the closure argument, not reproduce it. If Paper 3 mentions barriers, it should be a single sentence: "As shown in [Paper 1], all ECH-specific perturbation corrections vanish..." |
| 2 | ALP birefringence details | Paper 1 (consistency section) | Paper 2 PRIMARY, Paper 1 BRIEF | Paper 1 should contain at most a paragraph on birefringence consistency as a bridge to Paper 2. The full treatment belongs in Paper 2. |
| 3 | MCMC methodology details | Paper 1 | Paper 1 ONLY (unless Paper 2 MCMC is independent) | Paper 2 has its own MCMC (9,720 samples). Its methodology section should be self-contained. Paper 3 has no MCMC -- it uses Fisher + MC. |
| 4 | Galaxy spin phenomenology | Paper 1 | Consider cutting entirely or moving to supplementary | 9-12 OOM coupling gap means this is a dead end. Including it in Paper 1 adds length without science. |
| 5 | f_NL = -35/8 derivation details | Should NOT appear in Paper 3 | Paper 3 should cite Cai et al. + verification appendix | Paper 3 is a FORECAST paper, not a derivation paper. The verification (Cai audit, SymPy, gradient expansion) can be a short appendix or a reference to a companion note. |

---

## Cross-Paper Consistency Requirements

These terms must be IDENTICAL across all three papers:

| Term | Agreed Wording | DO NOT USE |
|------|---------------|------------|
| The f_NL prediction | "parameter-free prediction of matter-dominated contraction (Cai et al. 2009)" | "ECH prediction"; "our prediction"; "we derived" |
| ECH's perturbation role | "perturbation-transparent; provides nonsingular transition only" | "ECH contributes to the bispectrum"; "ECH predicts f_NL" |
| The barrier count | "14 structural barriers" | "13 barriers" |
| The birefringence result | "bounce-independent; motivated by Planck-scale ALP physics" | "bounce predicts birefringence"; "ECH-specific birefringence" |
| SPHEREx significance | "4-6 sigma via galaxy bispectrum" | "6 sigma" without caveat |
| MegaMapper significance | "3-7 sigma; 8.75 sigma under ideal conditions" | "8.75 sigma" without "under ideal conditions" |
| Bayes factor vs inflation | "BF > 300 vs standard single-field (robust to GR treatment)" | "rules out inflation" |
| Bayes factor vs multifield | "BF = 7-57 depending on prior" | "decisively excludes multifield" |

---

## Final Claim Discipline Summary

| Category | Count |
|----------|-------|
| SAFE (use freely) | 12 |
| NEED_SOFTENING | 9 |
| NEED_STRENGTHENING | 5 |
| SHOULD_BE_MOVED | 5 |

The project's claim discipline has improved dramatically from the original Paper 1 (which overclaimed tension reduction). The current calibration is generally good. The remaining issues are: (a) ECH-specific language for generic results, (b) a few "proves"/"definitive"/"rules out" holdovers in draft claims tables, and (c) underselling of the structural contributions (barrier map, perturbation-transparency theorem, integrated framework).
