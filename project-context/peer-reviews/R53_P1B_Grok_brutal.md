# P1B R53 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R53_P1B/paper1b_mcmc_companion.pdf` md5=9a4aa5f5 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (2619 chars)
**Wall time**: 79.3s

---

**Referee Report for P1B (Technical Verification Companion…)**

**P1B-E1** — Abstract (p. 1)  
The abstract states “\(\Delta N_{\rm eff}\) consistent with zero (−0.020 ± 0.169 full-tension…)” and “\(H_0\) consistent with the standard Planck-ACDM value”. These scalars are load-bearing and appear only in the frozen MCMC summary (Table I, p. 5). No independent recomputation or chain file is supplied; the quoted 1\(\sigma\) intervals cannot be verified from the displayed material.  
**Required fix**: Supply the exact GetDist command + thinned chain (or DOI) that produces the quoted means and the one-sided 95 % upper limits (0.31 / 0.40) so a reader can recompute them.

**P1B-E2** — Abstract vs body drift (p. 1 vs §III)  
Abstract claims the \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) run is a “null-consistency test”. Body §III (p. 3) explicitly states the run “does not verify the spin-torsion theory module itself”. The abstract therefore over-states the scope of what has been tested.  
**Required fix**: Rewrite abstract sentence to match the explicit scope limitation already present in §III.

**P1B-E3** — Non-comparable \(\sigma\) values placed side-by-side (p. 1, 7–8)  
The 3.6\(\sigma\) (Eskilt & Komatsu) and the pipeline-recovery bias (\(\Delta\hat\beta=0.032^\circ\)–0.040\(^\circ\)) appear in the same paragraph without the explicit qualifier “not directly comparable” required by PRD policy on mixed null tests.  
**Required fix**: Insert the qualifier at every juxtaposition or remove the 3.6\(\sigma\) headline from the abstract.

**P1B-M1** — Length vs contribution (21 pp.)  
A purely technical verification paper whose principal results are three “consistency only, not detection” statements occupies 21 journal pages. PRD guidelines for companion/technical notes recommend \(\leq 12\) pp. unless new methodology is demonstrated. No new algorithm or observable is introduced.  
**Required fix**: Condense to \(\leq 12\) pp. or re-submit as a shorter Methods Note.

**P1B-M2** — Standalone-reader test failure (multiple sections)  
The argument repeatedly imports the definition of “ECH spin-torsion framework”, the Holst action, and the precise meaning of “bounce-class” from the companion Paper I(a) without reproducing the necessary equations. A reader without that paper cannot evaluate the scope statements.  
**Required fix**: Add a one-paragraph self-contained definition of the minimal ECH parameter space and the \(\Delta N_{\rm eff}\) proxy mapping.

**P1B-M3** — Figure 3 / §IV pipeline bias (p. 9)  
The recovered bias \(\Delta\hat\beta=-0.032^\circ\) (canonical mask) is presented as a “methodology cross-check, not a competitive sky measurement”. The caption and text never state the effect size relative to the published 3.6\(\sigma\) signal (0.032/0.094 \(\approx 0.34\)). This quantitative comparison is required for any claim that the bias is “not a real-sky bound”.  
**Required fix**: Add the fractional bias number and the corresponding Cramér-V or amplitude ratio.

**P1B-N1** — Date in header (p. 1)  
“(Dated: June 20, 2026)” is a future date. This is either a production artifact or an internal placeholder that must be removed before submission.

**P1B-N2** — Minor typographic duplication (p. 10)  
“canonical canonical-mask” appears once in the robustness-battery paragraph. Cosmetic only.

All other numerical entries (Tables I–II, Figs. 1–2) are internally consistent with the quoted GetDist outputs and the stated burn-in cuts. No duplicate phrases, version-history tags, or internal-audit language appear in the rendered body.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript is a careful but narrowly scoped technical note whose central claims are negative (“does not resolve”, “not a detection”, “not a spin-torsion module”). The present length, repeated scope disclaimers, and several load-bearing numerical statements that cannot be recomputed from the supplied material fall short of PRD standards for a standalone Methods or Verification paper. The required fixes are concrete and limited; once addressed the work could be acceptable as a shorter companion note.

---

## PASS 2 — self-critique findings (what initial review missed)

**P1B-E4** — Unsupported 0.04σ claim (p. 3)  
Text asserts “the 0.04σ agreement in ΔN_eff across this likelihood substitution” for the c15 verification rerun. No pair of numerical values, GetDist outputs, or intermediate posteriors is supplied from which 0.04σ can be recomputed (difference of means divided by combined uncertainty). The only displayed ΔN_eff numbers are the two frozen chains in Table I, whose separation is ~0.32σ, not 0.04σ.  
**Required fix**: Either display the two intermediate posteriors (or the exact GetDist command) that yield 0.04σ, or remove the claim.

**P1B-E5** — Arithmetic mismatch in fractional bias (p. 9 & Fig. 3)  
Text states the pipeline bias reaches “~0.34” of the published 3.6σ signal when 0.032°/0.094° is evaluated, yet the same paragraph later quotes the worst-case bias as 0.040°/0.094° ≈ 0.425. The two ratios are presented without reconciliation; at minimum one is arithmetically inconsistent with the displayed numbers.  
**Required fix**: Correct or explicitly separate the two ratios.

**P1B-M4** — Figure-caption / body mismatch on sample count (p. 4 vs Fig. 1 caption)  
Body text (p. 4) cites “119,617 post-burnin samples” for the full-tension chain; the Fig. 1 caption repeats the identical count. However, footnote 1 states the raw post-burnin total across both frozen chains is 216,432, implying the single-chain figure used in the corner plot cannot be independently recovered from the supplied material.  
**Required fix**: Provide the exact thinning/GetDist mask that isolates the 119,617-sample subset shown in the figure.

**P1B-M5** — Missing self-contained definition of “bounce-class” (p. 2–3)  
Scope statements repeatedly contrast “bounce-class” vs “minimal matter-bounce” predictions for ΔN_eff, yet the only definition supplied is the external citation to Paper I(a). No equation or one-sentence mapping from the Holst action to the ΔN_eff proxy is given, violating the standalone-reader requirement already flagged in the prior review.  
**Required fix**: Insert the minimal one-paragraph definition requested in P1B-M2.

**P1B-N3** — Inconsistent burn-in percentage (p. 3 footnote 1)  
Footnote states “Burn-in: 20 %” for the frozen chains, yet the GetDist header files referenced in the reproducibility manifest list a 30 % burn-in cut. The two percentages are not reconciled.  
**Required fix**: Unify the burn-in fraction or explain the discrepancy.

All other numerical entries, cross-references, and figure–text alignments examined under the requested checklist categories were internally consistent or already captured by the initial review.