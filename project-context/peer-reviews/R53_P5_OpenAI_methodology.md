# P5 R53 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R53_P5/p5_desi_chirality.pdf` md5=e294df9b pages=33
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5753 chars)
**Wall time**: 438.1s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample”

Scope of review
- Role: methodology/statistics rigor. I checked arithmetic, sigma/p-values, dimensional consistency, estimator definitions, error propagation, and internal consistency of tables/figures. I audited the abstract and conclusions line-by-line against the body.

Overall assessment
- The analysis is extensive and many internal cross-checks are thoughtfully designed. Most headline scalars in the abstract trace back and recompute.
- However, there are several methodology and presentation issues that must be addressed for PRD. Chief among them: (i) the “primary” analysis choice is explicitly post hoc (Section V.B), which requires either family-wise error control across the explored options or rephrasing as exploratory; (ii) the work relies on an unpublished companion “Paper IV” for load-bearing inputs and interpretations, while mixing two different monopole references (Paper IV and “P5”) across tests; (iii) the data/code reproducibility statement promises a DOI but does not supply it; (iv) the manuscript is significantly longer than needed for the core contribution and includes repository-internal bookkeeping that belongs in a Supplement.

Findings

ESSENTIAL

P5-E1 — Section V.B, p.7: Post hoc declaration of the primary estimator
- Text: “This is an inherently multi-classifier, multi-stratification analysis and a single a priori preregistered analysis plan was not filed; the choice of which classifier to report as ‘primary’ is therefore made post hoc… We designate the DESIVAST-anchored void cross-check … as the primary…”
- Problem: The primary analysis path is chosen after exploration. This inflates the nominal Type-I error unless multiplicity is controlled over the explored choices (classifiers, stratifications, metric choices). While you apply Bonferroni within some families, there is no correction for the post-hoc selection of the primary path itself.
- Required fix: Either (a) treat all classifier paths as co-primary and apply a family-wise error control across them (e.g., Bonferroni/Holm across T-Web canonical, T-Web sensitivity grid, DESIVAST sphere-PIS, DESIVAST GALZONE, Tempel, ASTRA overlap); or (b) explicitly downgrade all conclusions from inferential to exploratory for any post hoc selection and remove “primary/secondary” language, or (c) provide a pre-specified, data-independent criterion (documented prior to running) that justifies selecting DESIVAST as primary and apply a holdout or simulation to show selection does not bias the stated error rates. Revise the abstract and conclusions accordingly.

P5-E2 — Abstract p.1; Section II p.3; Sections V–VI multiple: Mixed external (“Paper IV”) and internal (“P5”) monopole references in test statistics
- Text: You repeatedly predict σpred using ∆fCW = −0.0026 from Paper IV while also reporting an internally measured matched-sample monopole fP5CW = 0.49719 (∆f ≈ −0.00281, −5.07σ). Table XII then subtracts fP5CW, whereas Eq.(1) uses the Paper IV ∆f.
- Problem: This mixes two different references in different parts of the inferential pipeline, risking double counting or underestimating uncertainty, and it is not fully self-contained if Paper IV is unavailable. Some readers will not accept using an unpublished external number inside your null model when you can use the internal value consistently.
- Required fix: Use a single, internal monopole reference consistently throughout the inferential comparisons (both σpred and σvs-monopole) based solely on the matched sample used in this paper, and propagate its uncertainty. If you keep the Paper IV value, treat it strictly as a cross-check and move all Paper IV–anchored σpred displays to Supplement. State explicitly, near Eq.(1), which reference is used in every place and why. Update the abstract to reflect the reference used.

P5-E3 — Appendix C/D and in-text artifacts, p.31–32 and passim: Reproducibility DOI missing; repository-specific plumbing in the main text
- Text: “A DOI-minted archival snapshot of this directory accompanies journal submission.” Numerous [A#] GitHub paths are embedded in the body.
- Problem: No DOI is provided. PRD requires a stable, citable archive. The body of the paper contains implementation paths that are brittle at publication time.
- Required fix: Provide the exact DOI (e.g., Zenodo) for an immutable snapshot matching the final accepted version, and move the long list of repository-internal file paths [A2]–[A30] out of the main text to a Data Availability/Supplementary Materials section. Keep one compact paragraph in the main text with the DOI and top-level instructions.

P5-E4 — Abstract p.1 and Section titles/footnotes: Broken footnote insertion (“a on”)
- Text: “... Cautun et al. 2014 [7]) a on the full 14,622,283-galaxy DESI DR1...” and again at the footnote marker in §II (“a We use ...”).
- Problem: The footnote marker disrupts the sentence (typesetting/LaTeX issue) and reads as “a on …”.
- Required fix: Fix footnote placement and remove the stray “a” in the running text.

P5-E5 — Standalone-reader test, multiple places: Reliance on “Paper IV (in preparation)” for load-bearing claims
- Text: Multiple passages appeal to Paper IV for the global monopole significance, dipole null, and systematics (“BGS-selection-function-conditioned imaging-leg systematics tracked in Paper IV”). The catalog provenance is only briefly sketched here.
- Problem: The present paper should be fully interpretable and reproducible without the companion. Using “tracked in Paper IV” as an explanatory crutch for residuals is not acceptable unless you demonstrate the same within this manuscript.
- Required fix: Remove explanatory appeals to Paper IV’s systematics, or reproduce within this paper the minimum diagnostics needed to substantiate the claims you rely on (e.g., per-leg monopoles and their contribution to the matched-sample monopole; a brief summary table with leg/program residuals). Keep the dipole mention as context but not as support for any inference here.

MAJOR

P5-M1 — Section IV.A p.5; §IX.A p.23–24: Canonical T-Web classifier uses a global mean density in redshift space; selection-corrected variant is later
- Problem: The canonical T-Web run is selection-contaminated by construction (you acknowledge this). While you later provide a selection-corrected shell-mean and a randoms-weighted stress test (good), the manuscript still frames the canonical T-Web table (Table III) as “headline” and uses it prominently in the abstract.
- Required fix: Reframe the T-Web results so the selection-corrected version is the displayed baseline and the uncorrected version is explicitly labeled as a check susceptible to selection leakage. Alternatively, keep the present structure but add a sentence in the abstract clarifying that the cosmic-web T-Web cross-check is performed in redshift space with a global-mean overdensity and that a shell-corrected rebuild confirms the null (χ2 = 0.11, p = 0.99).

P5-M2 — Abstract p.1; §VIII.B–E p.18–20: Void re-projection ∆fCW quoted with 3 decimals (“+0.0007”) but without a simultaneous effect-size floor statement in the abstract
- Problem: The abstract states the difference precisely but leaves the sampling floor implicit until later.
- Required fix: Add “SE = 0.0022 (two-sample), z = 0.31, p = 0.76” (as in Table VIII) directly in the abstract sentence reporting ∆fCW to convey practical insignificance.

P5-M3 — Section V p.6 and throughout: Multiple σ-like statistics juxtaposed
- Problem: The paper uses at least four distinct scalar summaries: σfrom half (binomial z), σvs-monopole (residual z), MC pLEE, and χ2. You often note non-comparability across bins, but in a few places the language could still confuse (e.g., Section VII heat-map discussion combines σfrom half maxima with σobs−σpred maxima and pLEE).
- Required fix: Add an explicit one-sentence reminder at the beginning of Sections VI and VII that σfrom half and σvs-monopole are different and not comparable to permutation p-values; label axes or table columns with “one-sample binomial z” vs “monopole-subtracted residual z” to prevent misinterpretation. Add a parenthetical in the abstract that the quoted σ are one-sample binomial z-scores.

P5-M4 — Section VI.D p.10–12: Row-level bright/dark split uses overlapping samples; significance quoted
- Problem: You do flag the overlap caveat, but you still quote |z| ≈ 2.1 at face value.
- Required fix: Move the row-level |z| calculation to Supplement and replace the quoted |z| in the main text with the unique-galaxy value (|z| = 1.95) and/or an overlap-robust test (e.g., paired analysis on the intersection where the same TARGETID is in both programs, or restrict to non-overlapping subsets), or label the row-level |z| as non-inferential and exploratory.

P5-M5 — Appendix B p.31: Max class-to-overall bright-fraction deviation quoted as 1.5 pp
- Data: overall bright fraction 0.978; wall fbright = 0.9622 → deviation 1.58 pp; cluster 0.9893 → 1.13 pp; filament 0.9663 → 1.17 pp; void 0.9813 → 0.33 pp.
- Problem: The text claims 1.5 pp; the exact maximum is 1.58 pp.
- Required fix: Update the text to “1.6 pp” (or “1.58 pp”), or round consistently (“≈1.6 pp”).

P5-M6 — Length and organization
- Problem: The main text runs 33 pages and includes lengthy implementation details, repository paths, and many second-order diagnostics that could move to Supplement, obscuring the core message.
- Required fix: Condense the main text to ≤ 22–25 pages by (i) moving the Phase-2 nine-cell grid, grid-convergence, and much of §IX and §X details to Supplement, (ii) consolidating repository path lists into a compact Data Availability section with DOI, and (iii) trimming repetition of the same null across multiple decompositions.

P5-M7 — Abstract-last drift sweep: ordering and emphasis
- Problem: The abstract leads with a T-Web four-class summary and p-values despite later elevating DESIVAST as the “primary” path. This can mislead a reader about what is load-bearing.
- Required fix: Reorder the abstract so the DESIVAST primary result (n = 56,981 void spirals; ∆fCW = +0.0007 ± 0.0022) is presented first as the headline, followed by the T-Web cross-check summary.

MINOR

P5-m1 — Section IV.A footnote 1 p.5: h-convention
- Comment: The multiply-by-h convention is correct but unusual; the note is clear.
- Fix: None required; consider adding one sentence that numerical distances printed in h−1 Mpc use this convention throughout for avoidance of doubt.

P5-m2 — Table VII p.15: “Grid-unresolved” label
- Fix: Add a sentence in the caption explicitly stating “The Rs = 10 Mpc/h rows are below the 25.9 Mpc/h grid sampling scale and are excluded from robustness claims,” matching the text.

P5-m3 — Section VIII.A p.17: Clopper–Pearson bound reference
- Fix: Cite a standard reference or append the formula used for the 0-success case.

P5-m4 — Section VI.B p.9–10: Regression covariates
- Fix: Define “confidence” explicitly on first use (classifier maximum softmax probability of the equivariant CW/CCW label) for standalone clarity.

P5-m5 — Figures 6 and 8 captions p.14 and p.22: Axes units/thresholds
- Fix: Note explicitly that σ per pixel is a one-sample binomial z normalized by the pixel’s own counting error; readers may otherwise conflate with standardized residuals from other nulls.

P5-m6 — Bibliography formatting
- Fix: Ensure the two 2026 arXiv references [11], [12] have consistent author diacritics and journal submission status noted (e.g., “submitted to MNRAS”) per PRD style; confirm arXiv IDs and years.

P5-m7 — Typographic/grammar nits
- Multiple minor hyphenation and readability issues (e.g., “per-galaxy classifier-disagreement check — in this six-object illustrative check, 0/6 T-Web ‘void’ spirals …”). Consider tightening.

NITS

P5-n1 — Page 3: “the present manuscript treats its catalog and quoted monopole offset as inputs whose uncertainty is propagated explicitly below” could be tightened to avoid passive voice.

P5-n2 — Page 11 Figure 5(b): The dotted Bonferroni lines are described as α = 0.01 per family; consider adding the numeric |σ| ≈ 3.09 on the plot for quick reading.

P5-n3 — In several places you write “supporting rather than load-bearing”; consider replacing with journal-neutral phrasing (“supporting consistency check”).

Arithmetic and internal-consistency audit (selected)
- Table III σ recomputations: void (n=428, f=0.4836) → σ = −0.68; wall (6673, 0.5034) → +0.56; filament (408,187, 203,261 CW) → −2.60; cluster (397,505, 197,284 CW) → −4.64. Matches reported within rounding.
- Range across classes: 0.5034 − 0.4836 = 0.0198 = 1.98 pp (matches).
- χ2 homogeneity (4×2): not recomputed exactly here but counts in Appendix B permit it; the reported χ2 = 3.55 (p = 0.31) is plausible given tiny deviations and large N.
- Density quintiles (Table IV): σpred = 2×0.0026×√158,327 ≈ 2.07; residuals match table values.
- DESIVAST void vs non-void: ∆f = 0.0007; SE ≈ 0.5·√(1/56,981+1/621,964) ≈ 0.00219; z = 0.31; p ≈ 0.76 (matches).
- Cramér’s V: √(4933/811,609) ≈ 0.07798 (matches 0.078).
- Bonferroni thresholds: K=5, α=0.01 → |σ| ≈ 3.09; K=9, α=0.05 → |σ| ≈ 2.77; K=1054, α=0.05 → |σ| ≈ 4.0–4.05. Values as quoted.

Dimensional/algorithm checks
- T-Web sign conventions and units are explicitly stated and consistent.
- h-convention footnote is correct (multiplying by h to report in h−1 Mpc).
- CIC not deconvolved: clearly disclosed.

Abstract–body traceability (pattern-045)
- All headline numbers in the abstract (class counts, fractions, range 1.98 pp, χ2 = 3.55, p-values, DESIVAST ∆fCW ≈ +0.0007, Phase-2 ranges, HEALPix p-values, redshift/density nulls) are present in tables/sections and consistent. However, the ordering (T-Web before DESIVAST) and lack of SE with the +0.0007 are flagged above (P5-M2, P5-M7).

Provenance surfaces (patterns 046/047)
- A DOI is promised but not included (P5-E3). The heavy use of GitHub-internal paths in the body should be moved to Supplement.

Uncomputed quantitative claims (pattern-048)
- Most “robust to” statements are quantified with numbers or artifact pointers. Keep this standard; where “consistent with” is used (e.g., ASTRA overlap), you provide per-class ranges; acceptable.

Effect sizes (requirement)
- You provide Cramér’s V for the large χ2 contingency (good). In other places, adding SE alongside ∆f, as in P5-M2, will help.

Recommended maximum page count
- Recommend ≤ 22–25 pages main text. Move Phase 2 sweep table/heat-map, grid convergence, much of §IX and §X, and the artifact path table to Supplement.

## Summary recommendation
MAJOR REVISIONS

The core quantitative result appears sound: within DESI DR1, spiral chirality does not vary with environment at the quoted sensitivity, and the DESIVAST-anchored void/non-void contrast is null with adequate power. However, PRD requires that the primary analysis not be chosen post hoc without multiplicity control; that the paper be fully self-contained without relying on an unpublished companion; and that a permanent DOI for all code/data be provided. Addressing these essential points, clarifying the mixed use of monopole references, tightening the presentation, and trimming the main text will bring the manuscript up to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

New issues only. I do not repeat items already raised in my first report.

ESSENTIAL

P5-E6 — Stale/inconsistent headline numbers carried in different sections
- Issue: The paper quotes two different values for the Paper IV dipole and for the matched-sample monopole z:
  • Dipole: +0.41σ (p = 0.31) in the Introduction vs +0.43σ (p = 0.30) in Section II.
  • Matched-sample monopole: −5.07σ (near Eq. 1/Section V) vs −5.00σ in §VIII F.
- Why it matters: These are load-bearing contextual anchors used repeatedly (including σpred narrative). Mixed values are a red flag for stale edits and make it harder to trace exact references.
- Required fix: Use one consistent set across the paper (and abstract). If numbers changed during revisions, update all mentions and note the parent sample each refers to (row-level vs unique-galaxy).

P5-E7 — Mis-typed Clopper–Pearson expression for 0 successes
- Location: §VIII A, paragraph computing the 95% one-sided upper bound after 0/6.
- Text: “1 − 0.051/6 = 39% (the standard one-sided Clopper–Pearson bound 1 − α1/n).”
- Problem: As printed, “0.051/6” reads as a division; the correct formula is 1 − α1/n = 1 − 0.05^(1/6) ≈ 0.393. The numeric result (≈39%) is right, but the rendered expression is wrong and will confuse readers.
- Required fix: Correct the typesetting to 1 − 0.05^(1/6) and add a citation for the bound.

MAJOR

P5-M8 — Unit-notation inconsistency (Mpc/h vs h−1 Mpc) within the same sections
- Location: Throughout (e.g., §IV A steps 2–4, smoothing and box size).
- Problem: The manuscript alternates between “Mpc/h” and “h−1 Mpc.” While dimensionally equivalent, inconsistent notation makes it harder to verify unit consistency and reproduce configs.
- Required fix: Standardize on one convention (ideally h−1 Mpc in text; use Mpc h−1 only if the code/configs print it that way and say so explicitly once). State at first mention that all lengths are reported in h−1 Mpc and keep it uniform.

P5-M9 — Over-strong inference about per-pixel σ variance > 1 being due to duplicates
- Location: §VIII F (per-pixel σvs-monopole distribution, “heterogeneous pixel populations alone would not inflate the variance — the mild excess over unity … instead traces the 3.56% duplicate rows …”).
- Problem: The claim that heterogeneity “alone would not inflate” Var(Z) above 1 is not established. With spatial correlation, selection gradients, or pixel-to-pixel variation in true rates, overdispersion of the Z-statistic is expected even without duplicates. The unique-TARGETID recompute (std = 1.015) still shows >1 dispersion.
- Required fix: Soften the causal attribution and/or support it with a simulation or a block-bootstrap showing the effect of duplicates vs spatial correlation. As written, the statement is too categorical.

MINOR

P5-m8 — 256^3 typesetting inconsistency
- Location: Multiple places show “2563” inline (e.g., “2563 comoving grid”) while others render 256^3.
- Fix: Use 256^3 consistently.

P5-m9 — Ambiguous p-value reference (class-level vs pixel-level)
- Location: §VI A: “The label-shuffle look-elsewhere p on the max-class |σfrom half| statistic is likewise null … (p = 0.12 free vs 0.12 stratified).”
- Problem: It is not immediately clear this p refers to the four T-Web classes (not the HEALPix maps). Readers may confuse it with the NSIDE results in Table VI.
- Fix: Clarify “class-level permutation (K = 4 classes), pLEE = 0.12 (free) vs 0.12 (stratified), NMC = 1000.”

P5-m10 — Minor wording/clarity in abstract
- Location: Abstract (T-Web void bin sentence).
- Problem: “1.64 pp offset is well inside the 1σ floor (−0.68σfrom half, from half)” — the phrase reads awkwardly, with a duplicated “from half.”
- Fix: Rephrase, e.g., “the observed 1.64 pp offset lies well within the void bin’s 1σ counting floor (|σ| = 0.68).”

P5-m11 — Small rounding mismatch called out explicitly
- Location: §V (denominator adjustment note).
- Problem: You state 4 p0 (1 − p0) = 0.99998 at p0 = 0.4972; the exact value is ≈ 0.99997. Trivial, but since this sentence argues the adjustment is negligible, use 0.99997 or “≈1.00” to avoid nitpicks.

P5-m12 — Figure/body sample-size coherence cues
- Location: Fig. 8 vs body text (§VIII F).
- Comment: The figure caption states 1,496 valid pixels (z ≤ 0.24 subset), while §VIII F discusses 1,791 valid pixels (full redshift parent) and then r on 727 pixels (both voids and ≥ 200 spirals). All are internally consistent but easy to misread.
- Fix: Add a parenthetical in §VIII F reminding that the 1,496-pixel figure panel is for the z ≤ 0.24 subset; the 1,791- and 727-pixel counts refer to the full-range and intersection filters.

P5-m13 — Abstract phrasing about row-level counting
- Location: Abstract (“counted once per repeat DR1 survey–program coadd row carried by the environment table”).
- Problem: This is hard to parse.
- Fix: Clarify: “the 812,793 environment-labeled rows include 3.56% program-coadd duplicates; all statistics are also recomputed on the 783,820 unique TARGETIDs.”

NO OTHER DISCREPANCIES FOUND
- I rechecked the arithmetic in Tables III–V, VII–XI, XIII–XV and the values quoted in the captions; all recompute from the displayed inputs within rounding. The Bonferroni thresholds, σpred calculations, Cramér’s V, and two-sample SE/z for the DESIVAST contrasts match. Figures and captions agree with the claims in the corresponding sections.

Rationale for new items: The fresh pass focused on stale-number drift, typesetting/mathematical clarity, and places where inference could be over-stated. The core quantitative results still appear internally consistent; the added items above aim to remove avoidable ambiguities and ensure numerical and notational consistency.