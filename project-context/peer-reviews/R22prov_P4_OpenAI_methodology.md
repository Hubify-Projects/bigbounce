# P4 R22prov — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4366 chars)
**Wall time**: 159.8s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (15 pp)

I have read the manuscript line-by-line, recomputed the quoted statistics and traced every scalar that enters the abstract and conclusions.  The work is interesting and the authors have clearly invested enormous effort, but in its present form the submission does not yet meet the methodological and presentation standards of Physical Review D.  My detailed findings follow.

--------------------------------------------------------------------
FINDINGS
--------------------------------------------------------------------

ESSENTIAL (must be fixed for any further consideration)

P4-E1  Abstract & throughout (pp. 1, 6, 10)  
The text contains version-history and retraction bookkeeping that belongs in a “Note added” on arXiv, not in the body of a peer-review paper:
• “Withdrawal note: versions ≤1.0.165 …”  
• “A June 2026 provenance audit found … the result is therefore withdrawn.”  
• Dozens of “Artifact:” and internal path strings.  
Required fix: Remove all version-tracking prose, internal file-path comments, and audit log references from the published text.  Summarise any necessary provenance in a single concise sentence in App. A or the Data-availability section.

P4-E2  Fig. 2 caption vs. Table II (p. 5)  
Caption states a CW-fraction shift of “+2.05 % (A) to −0.53 % (C)”.  
Table II gives +0.79 % (A) and −0.26 % (C) when the same definition
cw/(cw+ccw) is used.  The two numbers cannot both be correct.  
Required fix: Recompute and reconcile the percentages; state explicitly which denominator (all galaxies vs. spirals only) is being used in each place.

P4-E3  Real-space dipole (pp. 6 & 10)  
Only the significance “+0.43 σ (p = 0.30)” is quoted.  The best-fit amplitude |A|, its 1 σ uncertainty, and the dipole direction (in Galactic or Equatorial coordinates) are not given, preventing reproduction.  
Required fix: Provide the three Cartesian components or (A, l, b) with uncertainties and the exact estimator definition.

P4-E4  Template-fit exclusion (Table I row (ii) & App. D, p. 13)  
The manuscript quotes “z ≈ −18” for ruling out a 1.7 % dipole but does not give (i) the fitted amplitude with its bootstrap error, (ii) the χ² or likelihood ratio, or (iii) the number of free nuisance parameters.  
Required fix: Tabulate Abest, σboot, χ²/d.o.f. and make the exclusion criterion quantitative (e.g. p-value or Δχ²).

P4-E5  MASTER ℓ = 1 diagnostic significance (pp. 6–7)  
The +7.28 σ value is obtained from only NMC = 500 label-shuffle realisations.  With 500 draws the sampling uncertainty of the standard deviation itself is ≈6 %.  A >7 σ claim is therefore unsupported.  
Required fix: Either raise the MC count to ≥10 000 or quote the significance as a rank p-value (≤1/500 = 0.002, i.e. <3 σ) rather than a Gaussian σ.  Clarify that the result is entirely diagnostic and not used for cosmology.

P4-E6  Mixed units for amplitudes (many places, e.g. p. 6 & App. D)  
The manuscript alternates between “in fCW units”, “full-amplitude”, and “% asymmetry” without definition.  
Required fix: Adopt one symbol (e.g. A≡(NCW−NCCW)/(NCW+NCCW)) throughout, state unambiguously whether a quoted percentage is 100 × A or 100 × A/2, and amend every occurrence.

P4-E7  Internal consistency of σ mapping (Table I & body)  
Table I distinguishes seven null procedures, but the main text occasionally places σ from two different nulls in the same sentence without the mandatory caveat (e.g. p. 7 bottom, p. 9 top).  
Required fix: At every juxtaposition of σ from different nulls, add the explicit clause “σ values are relative to their own null distributions and are not directly comparable”.

MAJOR (significant revision required)

P4-M1  Method description of the isotropic bootstrap (p. 6)  
The text does not state how the 10 000 “isotropic” realisations are generated: random sky rotations, latitude scrambles, or label permutations?  The dipole variance depends on the choice.  
Fix: Describe the bootstrap algorithm in a numbered list and justify that it is unbiased.

P4-M2  WLS block bootstrap (App. D, p. 13)  
Only NSIDE = 8 blocks and Nboot = 1000 are mentioned.  No convergence check or block-size dependence study is shown.  
Fix: Provide a plot or table demonstrating that σ(Adipole) is stable against doubling the block size and/or the number of bootstrap draws.

P4-M3  Page length (15 pp)  
For what is essentially a dipole null result, 15 typeset pages plus very long appendix-style footnotes is excessive.  
Fix: Reduce to ≤10 journal pages by moving code-path discussion and catalogue minutiae to an external “extended data” document.

P4-M4  Residual systematics attribution chain (Sec. IV D & App. D)  
The dismissal of interpretation (i) relies on three qualitative diagnostics.  No quantitative goodness-of-fit to a “dipole-only” model is given.  
Fix: Add a formal likelihood ratio or Δχ² test comparing the dipole-only model with the 9-template systematic model over the canonical mask.

MINOR

P4-m1  Equation (2) (p. 3): missing “=0.5” prefactor formatting; typeset with clearer parentheses.  
P4-m2  Table I caption: “its two σ values are against the global per-galaxy label-shuffle and depth-stratified nulls respectively” → please repeat that explanation in the table body.  
P4-m3  Footnote 1 (p. 6) contains a 16-line digression better placed in App. A.  
P4-m4  Duplicate phrasing: “canonical canonical-mask” (p. 7 line 3).  
P4-m5  Several references lack journal page numbers (e.g. Ref. [6]).  

NIT (cosmetic)

P4-n1  PACS numbers obsolete; use “Physics Subject Headings” or omit.  
P4-n2  “flip-swap correlation = 1.000” – give the number of decimal places justified by the sample size.  
P4-n3  Avoid first-person plural “We urge all future studies” in a PRD methods paper.

--------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The core idea—using flip-equivariant averaging to harden spiral-handedness measurements—is sound and potentially useful, but the manuscript needs substantial clean-up.  Essential corrections include removal of version-history text, reconciliation of inconsistent numbers, full disclosure of the dipole amplitude/direction, and a statistically robust treatment of the Monte-Carlo significances.  Addressing the major methodological points listed above and tightening the presentation to a focused 8–10-page article would bring the work up to Physical Review D standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS  
(only issues that were NOT identified in the first report are listed; numbering continues the original scheme)

--------------------------------------------------------------------
ESSENTIAL
--------------------------------------------------------------------

P4-E8  Inconsistent quoted significance for the same “ℓ = 1” quantity  
• Table III (p. 7) gives “+7.28 σ” (apodised footprint, Wp = Nall).  
• Appendix D (p. 12) states “σℓ=1 = +3.63”.  
Both passages call the value “the ℓ = 1 excess on the canonical mask”, yet differ by a factor ≈2. The manuscript never labels them as separate estimators (apodised vs. binary, weighted vs. un-weighted) and the reader cannot tell which number underpins later arguments.  
Required fix: Use unique names for the two estimators, place them in one comparison table, and explain explicitly why their σ’s differ.

P4-E9  Unit/normalisation mismatch between Tables III and IV  
Table III quotes Cℓ in “×10⁻⁶ sr”, e.g. C₁ = 23.48 × 10⁻⁶.  
Table IV lists a “Pre-MASTER pseudo-C(ℓ=1)ℓ” of 1.696 × 10⁻² with no units — 3 orders of magnitude larger than Table III despite purporting to be the same raw (pre-MASTER) spectrum. One table is clearly using an un-announced multiplicative factor.  
Required fix: State units in Table IV, reconcile the scaling, and ensure both tables use the same convention.

P4-E10  Sensitivity-floor calculation uses an undefined fsky  
Section VI A cites “fsky = 0.46” when computing the Fisher floor, yet everywhere else the analysis footprint is 0.490–0.494. No mask at fsky = 0.46 is described.  
Required fix: Specify which mask has fsky = 0.46 or correct the calculation; recompute the 0.29 % floor if the true fsky differs.

--------------------------------------------------------------------
MAJOR
--------------------------------------------------------------------

P4-M5  Drifting mask definitions (0.49005 / 0.491 / 0.494)  
The same footprint is variously quoted as fsky = 0.49005 (Table IV), 0.491 (Table III caption), and 0.494 (Table I row (iv) and many places in the text). It is impossible to know which area each statistic uses.  
Fix: Freeze one binary mask, quote its exact fsky once in §II, and propagate that single value everywhere; list any alternative masks in a separate table.

P4-M6  Discrepant σ in Table II  
Using Table II numbers, (0.5079 – 0.5)/0.000279 = 28.3 σ for Catalog A, yet the table lists 28.8 σ. Either Nspiral differs from 3 201 160 or a rounding/typing error occurred. Similar 2–3 % discrepancies appear in the other rows.  
Fix: Recompute Dev.(σ) from the listed counts, update the table, and certify that all σ values are internally consistent.

--------------------------------------------------------------------
MINOR
--------------------------------------------------------------------

P4-m6  Table I row (iv) labels fsky = 0.494 but, per Appendix A, the effective sky fraction after depth-weighting is 0.452. Stating the binary-mask area in a weighted-spectrum row is misleading. Quote both the geometric and the effective fsky or adopt one consistently.

P4-m7  Appendix D gives “σℓ=2 = +4.73”, whereas Table III shows +6.10 σ for the same (ℓ = 2) band-power. Clarify whether one value is canonical and the other apodised.

P4-m8  Figure 8 caption says the orange band is “500-MC monopole-only null”, but the legend in the panel labels it “Null expectation (1000 shuffles)”. The draw count must be stated consistently.

--------------------------------------------------------------------
NIT
--------------------------------------------------------------------

P4-n4  Table V lists r = 1.000 to three decimal places. Given 8.47 M samples, quote either 1.0000 ± 0.0002 or round to 1.00; three decimals look artificially precise.

P4-n5  In Sect. III C: “Z2 and D4 to within |∆⟨pCW⟩|<0.0016” — the inequality sign is flipped in the next sentence (“argmax-CW-fraction shift (−1.35 %)”); restate both numbers with the same precision and inequality orientation.

--------------------------------------------------------------------
## Brief rationale
The additional inconsistencies above were uncovered by re-computing quoted values and by cross-checking the tables against one another. Resolving them is necessary to make the statistical arguments reproducible and to avoid confusion over which estimator each σ refers to.