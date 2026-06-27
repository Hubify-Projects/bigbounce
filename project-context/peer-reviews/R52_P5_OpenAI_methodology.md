# P5 R52 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/p5_desi_chirality_v0.1.82-2026-06-18.pdf` md5=401a73f9 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7335 chars)
**Wall time**: 276.2s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T‑Web (Hahn 2007) Tidal‑Tensor Cross‑Check Across the DR1 Matched‑Spiral Sample”

Scope of review
- Journal: Physical Review D (methodology rigor). I audited the entire 32-page manuscript: abstract, figures, tables, equations, numerical claims, and appendices. I recomputed the quoted σ, p-values, binomial errors, and key ratios from the tabulated numbers; checked dimensional consistency (notably the distance–h convention), and inspected the multiplicity controls and null procedures.

Overall assessment
- The central conclusion (no detectable dependence of spiral chirality on environment at current sensitivity) is consistent with the presented calculations. Many internal numbers check out to within rounding. The DESIVAST-based primary contrast and the T-Web secondary analyses are, in general, statistically and methodologically sound.
- However, several ESSENTIAL issues must be addressed before PRD can consider publication: dependency on an unpublished companion (Paper IV) for a load-bearing “classifier-monopole systematic” claim, missing DOI for the frozen analysis repository despite claiming one exists, presence of version-history language in the body, and one explicit formula typo that is incorrect as written.
- Additional MAJOR/MINOR fixes will further tighten the methodology exposition and remove potential ambiguities.

Findings

ESSENTIAL

P5-E1 (Abstract + throughout; pages 1–3, 6, 8–9, 20–21)
Problem: Load-bearing reliance on Paper IV (in preparation) to treat the catalog-wide ¯fCW = 0.4974 (∆f = −0.0026) as a “known classifier‑monopole systematic,” and to anchor σpred used repeatedly. Example abstract text: “... the known Paper IV catalog-wide classifier-monopole systematic of ≈0.26 pp ... is subtracted explicitly ...”; Sec. II: “Paper IV establishes the catalog‑wide CW-fraction monopole as a classifier-residual bias ...”
Required fix: Reframe all uses of the “Paper IV monopole” as an empirical reference that can be (and is) computed on the P5 matched sample (fP5CW = 0.49719 on 812,793 rows; Table XII shows residuals vs fP5CW). Remove any claims that the monopole is “known to be a classifier systematic” unless supported by a peer‑reviewed, citable source (not “in preparation”). If you wish to keep the interpretation, (i) cite a peer‑reviewed analysis establishing it, or (ii) state explicitly that this interpretation is external to P5 and does not enter any hypothesis test; show all key residuals with respect to the internal fP5CW as primary. Adjust abstract language accordingly.

P5-E2 (Appendix C; page 31)
Problem: Data/code archival DOI is promised but not provided: “A DOI-minted archival snapshot of this directory accompanies journal submission.” No DOI is given.
Required fix: Provide a working DOI (or equivalent immutable archival identifier) for the exact tag used (v0.1.82-2026-06-18) and ensure the archive contains all artifacts needed to reproduce every number, table, and figure. Include the DOI in Appendix C and in the data-availability section of the main text.

P5-E3 (Version history language in body; pages 3, 5, 31)
Problem: Version-history/internal-tracking language appears in the scientific narrative: e.g., “Paper IV v1.0.166,” “earlier preprint versions used the ‘V-Web’ label loosely...,” “manuscript tag v0.1.82-2026-06-18.”
Required fix: Remove all version numbers and preprint‑history statements from the body of the paper. These can appear, if necessary, only in a code‑release note in Appendix C (without implying scientific precedence), but PRD prefers stable citations (DOIs, arXiv IDs) over internal version strings in the main text. Replace with neutral wording (“We adopt the T-Web tidal-tensor implementation of Hahn et al. (2007) ...”).

P5-E4 (Clopper–Pearson bound typo; page 17, §VIII A)
Problem: The formula printed for the one-sided 95% upper bound with 0/6 successes reads “1 − 0.051/6 = 39%,” which algebraically is wrong. It should be 1 − 0.05^(1/6) ≈ 0.393.
Required fix: Correct to 1 − α^(1/n) with α = 0.05, n = 6; explicitly typeset the exponent to avoid ambiguity: “1 − 0.05^(1/6) = 0.393.”

P5-E5 (Primary estimator declaration; page 8, §V B and Abstract)
Problem: The paper explicitly states that the primary analysis path (DESIVAST-anchored) was designated post hoc. This is acceptable if multiplicity is cleanly handled and the abstract does not oversell pre-registration.
Required fix: In the abstract and conclusions, clearly state that the DESIVAST void-vs-non‑void contrast is the designated primary estimand and that multiplicity for the five DESIVAST estimators is controlled via Bonferroni‑5 at α = 0.05. Remove any phrasing that could be read as pre-registration.

MAJOR

P5-M1 (“h−1 Mpc” vs “Mpc/h” notation and conversion convention; page 5, §IV A step 2; footnote 1; elsewhere)
Problem: The manuscript uses both “h−1 Mpc” and “Mpc/h,” and adopts the multiply‑by‑h convention for numeric values. While this convention is self‑consistent, it is easy to confuse readers, and the community standard often uses “divide-by‑h” language.
Required fix: State once, prominently (e.g., §III B or §IV A), the convention: “We report distances in h−1 Mpc (≡ Mpc/h). Numeric values in h−1 Mpc are obtained from Mpc by multiplying by h.” Ensure notation is uniform throughout (use one of “h−1 Mpc” or “Mpc/h,” not both), and keep the footnote but clarify that both notations denote the same unit.

P5-M2 (Rs = 10 Mpc/h cells below grid scale; Table VII and text; pages 14–15)
Problem: The Rs=10 rows are flagged as “grid-unresolved,” but the symbol † in the table is not defined; readers may miss the caveat despite the text.
Required fix: Add a table footnote explicitly defining † (“Below the 25.9 Mpc/h grid sampling scale; excluded from robustness claims”). Also restate this caveat once in the caption.

P5-M3 (Stand‑alone reader test: dependence on external, non‑peer‑reviewed classifiers; multiple pages)
Problem: Several robustness statements refer to concurrent preprints ([11], [12]) and an in‑prep companion (Paper IV). While acceptable as context, the core inference should be demonstrably independent of non‑peer‑reviewed material.
Required fix: Where a statement depends on an external preprint (e.g., the DR1 T-Web volume-fraction comparison), soften the language to “consistent at the level expected given survey geometry,” and ensure no load‑bearing conclusion depends on those. For Paper IV, rephrase as in P5‑E1.

P5-M4 (Abstract-last drift; page 1 vs body §§VI–VIII)
Problem: The abstract states several look‑elsewhere p-value ranges (e.g., 0.13–0.56), per‑class σ, and phase‑2 residual maxima. These match the body, but the abstract also attributes the filament/cluster negative σ explicitly to the Paper IV catalog‑monopole; in the body you also provide the internal fP5CW residuals (Table XII).
Required fix: Add one sentence in the abstract noting that the same verdict holds when subtracting the matched‑sample monopole fP5CW (all four T-Web classes have |σ| < 1.15 after subtraction; Table XII), i.e., the conclusion does not rely on external Paper IV.

MINOR

P5-n1 (Arithmetic spot checks — all OK but add explicit pointers)
- Table III σfrom half values recompute correctly from counts; good. Consider adding a one‑line note/formula in the caption for reproducibility: “σ = 2(f − 0.5)√n.”
- Table X standard errors z∆ recompute from n and f; values match to rounding; consider adding se = 0.5√(1/n1+1/n2) in the caption.

P5-n2 (Notational clarity on “void-bin smallness”; page 9)
Problem: Two “void volume fractions” are contrasted: T-Web (24.4%) vs DESIVAST-in-hole cells (~0.1%). The explanation is correct but dense.
Required fix: Add a clarifying clause: “The DESIVAST-in-hole fraction refers to grid cells contained in VoidFinder spheres on the 25.9 Mpc/h grid used for the stratification — not the volume of DESIVAST voids in the continuous field.”

P5-n3 (Permutation NMC stated; page 6)
Problem: NMC = 1000 is stated with MC standard errors; good. In a few places you reuse the same RNG seed across scan families; you later note distinct streams confirm stability.
Required fix: Add one sentence consolidating this in §V: “We verified that re‑running with independent RNG streams leaves pLEE within one Monte‑Carlo s.e. across all scans.”

P5-n4 (Table VII and Fig. 7 phrasing)
Problem: “range dominated by void-bin counting noise” is narrative; could be quantified more mechanically.
Required fix: Add a parenthetical quantifier in the caption: “In each cell, |σvoid| ≤ 1.35; the cross‑class range ≤ 1.01× the void-bin 2σ counting floor.”

P5-n5 (Typo/grammar)
- Page 2: “surveyor-shell” -> “survey-shell” (check across the text).
- Page 7: “Bonferroni-9 secondary family ... threshold |σ| = 2.77 (two-sided)” — correct; consider adding “computed from Eq. (2)”.
- Page 17: “per-galaxy DESIVAST void/non-void classification is a single point-in-sphere (or watershed-cell) test” — fine; consider hyphenation consistency “point‑in‑sphere.”

P5-n6 (Units)
- Ensure consistent use of “Mpc/h” vs “h−1 Mpc” (see P5-M1); I noticed both in caption/footnotes. Pick one.

P5-n7 (Figure labelling)
- Ensure every figure panel has axis labels where relevant (Fig. 6, 8 colorbars do; OK). For Fig. 7, add explicit labels on axes: “Rs [Mpc/h]” and “λth”.

NIT

P5-z1 (Length)
The paper is long (32 pages) for a negative result. Consider condensing descriptive robustness (e.g., some repetition around the Phase‑2 sweep and the multiple sky‑position scans) to target ~24–26 pages without loss of substance.

P5-z2 (Cross-referencing artifacts)
You include many internal file paths (pipelines/...). Keep these in Appendix C and footnotes rather than the main narrative to improve readability.

P5-z3 (Small rounding consistency)
A few places round differently between text and tables (e.g., σ −2.60 vs −2.61). This is acceptable; consider standardizing to 2 d.p. throughout.

Quantitative audit summary (selected checks)

- Table III: σfrom half recomputes: void: 2(0.4836−0.5)√428 = −0.68; wall: +0.56; filament: −2.60; cluster: −4.66 — consistent to rounding.
- χ2 homogeneity (Table XVI): totals 812,793; foverall = 404,111/812,793 = 0.49719; given the small per‑row deviations, χ2 = 3.55 with 3 d.o.f., p = 0.31 is plausible. (Counts match table.)
- Phase‑2 sweep (Table VII): max |σobs−σpred| ≤ 1.64 in resolved cells; pLEE across cells 0.13–0.48; the 10 Mpc/h cells noted as unresolved; OK.
- DESIVAST primary contrast (Table X): VoidFinder ∆ = +0.0007, SE 0.00219, z = 0.31 (p = 0.76) — recomputed; V2‑REVOLVER and V2‑VIDE rows recompute.
- Footprint-restricted non‑void (Table VIII): n = 253,276; f = 0.4983; σ = −1.73; and ∆f = +0.0018 (SE 0.0023, z = 0.78, p = 0.43) — consistent.
- Target‑program split (Table XV): bright f = 0.4970 (n = 775,760), dark f = 0.5051 (n = 14,782) → z ≈ 1.95 (unique-galaxy) — recomputed.

Effect sizes and multiple testing
- Class × program χ2 is supplemented with Cramér’s V = 0.078 (effect size); good.
- Multi-cell LEE handled via both Bonferroni and empirical max‑stat; NMC = 1000 with seMC quoted; good.
- Across the five DESIVAST estimators, Bonferroni‑5 gate |z| ≈ 2.58 is stated; all contrasts below; good.

Dimensional/algorithmic checks
- T-Web construction steps (δ, smoothing, Poisson solve, Hessian, eigenvalue thresholding) are correct; sign conventions clarified. The Gaussian smoothing scale choices and mask dilation are discussed; grid‑resolution convergence run (128^3, 256^3, 384^3) supports stability at Rs = 25 Mpc/h; good.
- The “multiply-by‑h” convention for h−1 Mpc is clearly stated (though unusual); ensure consistency (P5‑M1).
- RSD treatment: you correctly state that the P5 headline is a redshift‑space statement; the fixed‑geometry Monte‑Carlo at σ = 5 Mpc/h supports robustness of ∆fCW under boundary jitter; good. Keep the caveat that a full real‑space reconstruction is future work.

Bibliography
- Citations appear correct and traceable (years and arXiv IDs verified for [5]–[8], [10]–[13]). Preprints [11],[12] are cited appropriately as contemporaneous work; do not make them load‑bearing.

## Summary recommendation
MAJOR REVISIONS

Justification
The central analyses and most numerical claims check out, and the DESIVAST‑anchored primary contrast is statistically robust. However, publication in PRD requires (i) removing dependence on an unpublished companion (Paper IV) for a key “classifier‑monopole systematic” claim, or reframing strictly in terms of the internal matched‑sample monopole; (ii) providing the promised archival DOI for the full reproducibility bundle; (iii) eliminating version‑history language from the scientific narrative; and (iv) correcting the explicit formula typo for the 0/6 Clopper–Pearson bound. Addressing these ESSENTIAL items, along with the listed MAJOR/MINOR fixes, will bring the paper to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-audit pass)

ESSENTIAL

P5-E6 (Density-metric definition mismatch; pages 10–11, Table V; §IV A step 12)
Problem: Table V states “ρ̄ is the quartile mean of log10(1+δsmooth),” but the reported values (e.g., cluster Q1/Q4 ρ̄ = 1.55/2.21; filament quartiles 0.90–1.86) are inconsistent with a log10 scale at Rs = 25 Mpc/h and are numerically consistent with linear 1+δ (or δ+1), not log10(1+δ). The text immediately below Table V uses these ρ̄ to argue class-boundary overlap (cluster Q1 less dense than filament Q4), which only makes sense if ρ̄ is linear 1+δ.
Required fix: Correct Table V’s caption and all related text to state explicitly whether ρ̄ is the mean of the linear (1+δsmooth) or log10(1+δsmooth). If linear is intended (as the numbers imply), change the definition and units accordingly and ensure §IV A step 12 (“we store log10(1+δsmooth) and use it for stratification”) is reconciled with what is actually reported (either note that stratification is done on log10 but the displayed means are on linear 1+δ, or compute and display log-means that match the stated definition).

MAJOR

P5-M5 (ASTRA-overlap “n ≥ 100” filter vs printed counts; page 28, Table XIV)
Problem: The table header says the range and max-|σ| are “filtered to classes with n ≥ 100,” but the printed per-class n for “T-Web on same overlap” include 1 and 2 objects in void/wall, and four-class n are listed for all classifiers. It is unclear whether the range/max-|σ| were computed after excluding those tiny classes or not.
Required fix: Make the filtering consistent and explicit. Either (i) remove the <100-n classes from the printed “per-class n” and compute range/max-|σ| only over n ≥ 100, or (ii) keep all counts but state clearly that range/max-|σ| exclude classes with n < 100 and list the effective classes used in each row.

P5-M6 (Non-void count switches between “k=20” and “exact” without a clear table-level cue; page 18, Table VIII; §VIII B–E)
Problem: The table mixes “k = 20 KDTree” membership (non-void = 621,964) with the “exact k-unbounded” rerun (non-void = 621,864) in the footprint-restricted control, but only a parenthetical in the text clarifies the count basis. Readers can miss why 621,964 ≠ 621,864.
Required fix: Add an explicit column note or footnote per row in Table VIII labeling the membership basis (“k = 20” vs “exact k-unbounded”). In the footprint-restricted control row, explicitly state that the exact-membership counts are used and reconcile the non-void total with the earlier k = 20 figure.

P5-M7 (Unjustified “worst-case design-effect inflation” for Jeffreys CIs on duplicated rows; page 9, Fig. 3 caption and §VI A)
Problem: Error bars (Jeffreys CIs) are drawn on the 812,793-row parent that includes 3.56% duplicate coadd rows. The caption claims a “worst-case design-effect inflation” of sqrt(812,793/783,820) = 1.018 without justification (design effect depends on intra-cluster correlation, not merely Nratio). This could understate interval inflation if duplicates are not i.i.d.
Required fix: Either (i) plot Jeffreys CIs computed on the 783,820 unique-TARGETID parent and state that as the default; or (ii) justify the design-effect approximation (e.g., show that duplicate rows have negligible intra-cluster correlation in CW labels conditional on class), or provide robust/clustered-binomial intervals as a sensitivity check.

MINOR

P5-n8 (Figure/table p-value ranges drift; pages 1, 15, Table VII)
Problem: The abstract gives Phase-2 pLEE = 0.13–0.56 (including unresolved Rs=10 rows); the Table VII caption mentions stratified/free-shuffle ranges of 0.14–0.54 and 0.16–0.55; §VII body text cites 0.13–0.56 and, for resolved cells, 0.13–0.48. These describe slightly different runs/filters but are easy to read as inconsistencies.
Required fix: Consolidate pLEE ranges in one place with explicit qualifiers (“all nine cells including Rs=10: 0.13–0.56; resolved Rs ∈ {25,50}: 0.13–0.48; stratified re-draws: 0.14–0.54”), and use the same ranges consistently across abstract, text, and caption.

P5-n9 (“Per-cap” wording and cap-join clarity; page 19, §VIII D)
Problem: The phrase “per-cap join values” is nonstandard and can be misread; “cap” refers to NGC/SGC concatenation with local index offsets.
Required fix: Replace “per-cap” with “per-cap (NGC/SGC) concatenation” and briefly restate that zone indices are offset to maintain GALZONE-to-VOID0 mapping under cap concatenation.

P5-n10 (Explicit link between Table XI bins and coverage proxy; page 20, Table XI; §VIII E)
Problem: The text correctly explains that “0 maximal voids per pixel” is a proxy for outside-DESIVAST coverage, but Table XI does not explicitly remind readers that this is a proxy, not a mask intersection.
Required fix: Add a table footnote: “0 maximal voids per pixel is a proxy for outside-DESIVAST coverage at NSIDE=16; a small fraction of in-footprint pixels can stochastically have zero maximal voids.”

P5-n11 (Null-comparability qualifier missing in one place; page 20, Table XI discussion)
Problem: The text compares σ across the four “maximal voids per pixel” bins with very different N without reiterating the “σ scales as √n” caveat present elsewhere.
Required fix: Add a brief qualifier here that raw |σ| across these bins are not directly comparable due to differing N; the subsequent P4-monopole residual comparison is the inferential basis.

P5-n12 (Minor typographic items)
- “per-galaxy DESIVAST void/non-void classification is a single point-in-sphere” → standardize hyphenation “point‑in‑sphere” (page 17).
- Ensure all instances of “survey-shell” are spelled consistently (a stray “surveyor-shell” appeared earlier drafts).

NO OTHER DISCREPANCIES DETECTED IN CLASSES A–J
- Arithmetic (A): Spot-checks on counts, σ, χ2, ranges, and propagated Δf/SE/z across Tables III, VII, VIII–XII, XV–XVII match to rounding. Abstract numbers (n, σ, p-ranges, ranges in pp) reconcile with the corresponding body tables/figures.
- Figure-caption vs body (B): Axes/units/numbers in Figs. 1, 2, 3, 5–8 align with the described statistics; previously noted axis-label suggestion for Fig. 7 remains (already in initial review).
- Equation dimensional consistency (C): Eq. (1), Poisson/Hessian steps (Φ, Tij) are dimensionless in the adopted normalization; k-units and conventions stated; no new unit inconsistencies found.
- Internal cross-refs (D): Section, table, and appendix references resolve correctly for claims checked (e.g., χ2 tables in App. B, Phase-2 sweep refs, selection-corrected rebuild §IX A).
- Null-procedure comparability (E): The paper generally avoids juxtaposing incomparable σ; when it does (e.g., Table III), it flags non-comparability. One added qualifier noted above (P5-n11).
- Abstract faithfulness (F): Each abstract claim is traceable to a body table/section; the earlier-requested caveat about using fP5CW residuals should still be added (P5-M4 in prior review).
- Unsupported novelty (G): “largest matched-sample… to our knowledge” remains a soft claim; acceptable with present phrasing.
- Unquantified hedges (H): Where “consistent with” is used, numbers and uncertainties are given nearby.
- Appendix vs main-text (I): Aside from the new DOI request from prior review, configs and drivers referenced in Appendix C map to described runs.

End of addendum.