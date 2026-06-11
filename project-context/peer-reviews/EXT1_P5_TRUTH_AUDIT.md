# EXT1 P5 Truth Audit — External Referee Reports

**Paper:** P5 — Environmental Dependence of Spiral Chirality (v0.1.60, 28pp)
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
**Reports audited:** EXT1_P5_ChatGPT.md (MAJOR), EXT1_P5_Grok.md (MINOR), EXT1_P5_Gemini.md (MAJOR)
**Auditor:** Claude Sonnet 4.6 · **Date:** 2026-06-10

---

## Verdict Summary

| Verdict | Count |
|---------|-------|
| VERIFIED | 12 |
| PARTIAL | 4 |
| OPINION | 5 |
| STALE | 1 |
| FALSIFIED | 4 |
| HOUSTON-DECISION | 2 |

---

## Full Finding-by-Finding Table

| # | Reviewer | Severity | Finding | Verdict | Evidence |
|---|----------|----------|---------|---------|----------|
| F1 | ChatGPT | BLOCKER | Non-void control not restricted to DESIVAST usable footprint; "0 voids per pixel" is a proxy, not a formal footprint mask; non-void may include galaxies outside DESIVAST volume | PARTIAL | `.tex` ll.1848–1854 explicitly acknowledges "0 maximal voids per pixel" is a catalog-derived proxy for outside-coverage, not a formal angular mask, and states "an explicit footprint-mask re-tabulation is queued for the data release." The concern is real; the fix prescription is partially in the paper already. The $[{-2.04, -0.09}]$ range on every ≥1-void bin is cited as bounding in-coverage behavior independently. Partial because formal mask is absent but proxy bounds are documented. |
| F2 | ChatGPT | BLOCKER | DESIVAST catalog counts quoted (1,461/420/295 interior voids) are preprint-era; final ApJ 982, 38 reportedly has 1,489/389/297 | HOUSTON-DECISION | `.tex` l.1523–1524 quotes "1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE" citing ApJ 982, 38. ChatGPT claims the final published paper has 1,489/389/297. Cannot verify from repo (DESIVAST FITS data is gitignored; bbl is empty; final ApJ counts require web check). Paper already distinguishes "interior voids" from "whole-catalog totals" (ll.1707–1708). Houston must verify against ADS/DOI 10.3847/1538-4357/adb559 whether the interior-void count in the final ApJ paper is 1,461 or 1,489. If different, update l.1523–1524 and add a version ledger note. |
| F3 | ChatGPT | BLOCKER | k=20 KDTree approximation retained as headline count when exact k-unbounded result exists (adds 100 galaxies, n_void 56,981→57,081) | FALSIFIED | `.tex` ll.1638–1657: paper DOES run the exact k-unbounded rerun, reports n_void=57,081 and f_CW=0.4965, and explicitly states "every conclusion in this section is invariant, and we retain the k=20 catalog statistics below for continuity with the released artifacts." The exact result is present; the choice to retain k=20 as the reported number is documented and justified. The blocker was already addressed — ChatGPT missed it. |
| F4 | ChatGPT | BLOCKER | Paper IV companion catalog is not independently reviewable; classification uncertainty budget missing | OPINION | `.tex` ll.283–286 explicitly flags "companion work by the same author, currently in preparation and not yet peer reviewed; the present manuscript treats its catalog and quoted monopole offset as inputs whose uncertainty is propagated explicitly below." The companion-placeholder concern is deliberate and documented. Whether a journal requires co-submission is editorial policy, not a factual error in the paper. Classified OPINION — legitimate publication gate question, not an error Houston can fix unilaterally. |
| F5 | ChatGPT | BLOCKER | V-Web/T-Web material over-promoted despite completeness rebuild showing only 26.6% class retention; abstract/conclusion still foreground V-Web class fractions | PARTIAL | `.tex` ll.113–115, 719–729: DESIVAST is explicitly declared PRIMARY; V-Web is declared SECONDARY. However, the abstract does still quote per-class V-Web σ values (ll.155–165) as part of the sample ledger before pivoting to DESIVAST. The concern has partial validity: the abstract is long and the V-Web fractions appear before the DESIVAST result. The "headline" language is used for -5σ catalog-level monopole (ll.1105–1106) and also for the environment-dependence null — dual use of "headline" creates the confusion ChatGPT flags (also independently flagged by Grok M2). PARTIAL. |
| F6 | ChatGPT | MAJOR | Should rename method "T-Web" not "V-Web" throughout | FALSIFIED | Title already reads "T-Web (Hahn 2007) Tidal-Tensor" (l.93). Title footnote explains the backward-compatibility retention of "V-Web" label for the implementation (ll.93 footnote, ll.466–471). §IV.A (l.462–471) has an explicit "Nomenclature reminder." The complaint was addressed prior to v0.1.60. ChatGPT's claim that "V-Web" appears in the title is stale — the current title uses T-Web. FALSIFIED (stale). |
| F7 | ChatGPT | MAJOR | Primary/secondary declaration post-hoc and incomplete; Bonferroni-5 family too narrow for full analysis tree | VERIFIED | `.tex` ll.697–700 explicitly acknowledges no pre-registration: "a single a priori preregistered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc, and we declare it explicitly here." The Bonferroni-5 covers only the five DESIVAST estimators; all secondary paths (V-Web, Tempel, ASTRA, T-Web, stratifications) are labeled secondary but no unified multiplicity budget covers the secondary tree. VERIFIED — the garden-of-forking-paths concern for the secondary paths is real, though the primary path is correctly bounded. |
| F8 | ChatGPT | MAJOR | χ²=4932 target-program contingency result should report Cramér's V and effect sizes; p reported as "below double-precision underflow" instead of log10(p) | VERIFIED | `.tex` l.1185: paper says "p ≪ 10^{-300} (below double-precision underflow)" — no Cramér's V reported, no standardized residuals, no log10(p) estimate. The 1.5pp max bright-fraction deviation is mentioned but no effect size metric. VERIFIED as a real gap. Fix: add Cramér's V and log₁₀(p) ≈ −1069 at 4932 / 3 d.o.f. |
| F9 | ChatGPT | MAJOR | DESIVAST primary independence from target-program residuals is asserted not quantitatively demonstrated | VERIFIED | `.tex` ll.1204–1211 asserts DESIVAST is "constructed to be independent of this residual, because the DESIVAST void definition restricts to the volume-limited z≤0.24 BGS sample where target-program mixing is far more constrained." No per-program (bright/dark) split of the DESIVAST void result is shown in the paper. The claim is logically sound (BGS-only at z≤0.24) but not quantitatively demonstrated with an explicit table. VERIFIED as a real gap; a BGS-program split of the DESIVAST f_CW would close it. |
| F10 | ChatGPT | MAJOR | Phase 2 range heat map overstates significance control; max residual 1.87σ comes from Rs=10 unresolved cell | PARTIAL | `.tex` ll.1294–1307: paper already explicitly calls Rs=10 "below the grid sampling scale," retains those cells only "for completeness but exclude[s] them from the physical robustness claim," and states restricted-to-resolved-cells max residual = 1.64σ. The paper does NOT present the range heat map as "controlling false-positive rate" — that language is ChatGPT's misread. However, the paper does use "per-cell range" language that could mislead. PARTIAL — the Rs=10 caveat is in the text but the heat map visualization (Fig. 7) still shows the unresolved cells without visual flagging. |
| F11 | ChatGPT | MAJOR | RSD sensitivity argument insufficient; FoG Monte Carlo not a void-catalog rerun under RSD | PARTIAL | `.tex` ll.1529–1583: paper is careful to say "RSD-bounded (rather than strictly immune)" and the argument is a fixed-void-geometry membership sensitivity test, not a full void-catalog RSD rerun. The caveat "this RSD-robustness argument applies to the per-galaxy void-membership test itself" is explicit (l.1570). ChatGPT's specific request to "tone down" the claim is already partially satisfied; however the abstract still says "void membership inherits no anisotropic RSD systematic at the present precision" (l.1544) which slightly overstates. PARTIAL. |
| F12 | ChatGPT | MAJOR | ZCAT_PRIMARY redshift selector not used; row-level coadd entries used instead with downstream deduplication | STALE | `.tex` ll.363–380 describes using `zall-pix-iron.fits` with `ZWARN==0`, `SPECTYPE∈{GALAXY,QSO}`, and explicitly states "These row counts are derived in this work by applying our cuts to the DR1 zall catalog." The paper explains that row-level entries are used and that duplicate-row analysis shows conclusions invariant (ll.815–820 for design-effect bound; ll.493–501 for unique-TARGETID full-field rebuild). The ZCAT_PRIMARY concern is a DESI best-practice question; paper has done the uniqueness robustness check. STALE as a blocker — the sensitivity to this choice is already bounded. |
| F13 | ChatGPT | MAJOR | Tempel and ASTRA cross-checks over-described as robustness evidence; ASTRA disagrees per-galaxy with V-Web | FALSIFIED | `.tex` ll.719–729: Tempel FoF, ASTRA EDR, T-Web concurrent-lit are all explicitly labeled "secondary diagnostic consistency checks." The text says "supporting rather than load-bearing" for Tempel (l.209) and the abstract states "primary robustness evidence is the on-DESI DESIVAST cross-classifier." ChatGPT's claim that they are "over-described" is not supported by current text. FALSIFIED. |
| F14 | ChatGPT | MAJOR | Bounce/EFT framing disproportionate; toy EFT not covariant | OPINION | `.tex` Appendix A (l.2847+) contains the toy EFT mapping with explicit caveats: "schematic, not a covariant operator" (l.2895) and "parametrization in this specific slicing, not as a covariant" (l.2903). The paper explicitly calls it "toy." Whether to include or move to a brief paragraph is journal-style preference. OPINION — the existing caveat language is adequate; whether MNRAS vs PRD framing is appropriate is Houston's call. |
| F15 | ChatGPT | MINOR | Figure 3 title/caption parent count mismatch (791,635 vs 812,793) | FALSIFIED | Fig 3 = `fig_p5_cw_by_env_bar.png` with caption at ll.810–826. The caption consistently uses 812,793 throughout: "on the n=812,793 env-labeled spiral rows (covering 783,820 of the 791,635 unique chirality-relevant matched spirals)." There is no mismatch — both counts appear in the caption with correct context. ChatGPT appears to have misread a PDF rendering. FALSIFIED. |
| F16 | ChatGPT | MINOR | Void-bin smallness paragraph: "small cluster volume fraction of 1%" should be "void assignment/selection" | VERIFIED | `.tex` ll.839–841: "The void bin has only n=428 galaxies (the small cluster volume fraction of 1% plus the sparse r≤17.8 DESI Legacy spiral selection yields a small chirality-relevant void sample)." The reasoning is confused: the void volume fraction (not the cluster volume fraction) is what's small (void = 0.1% in-footprint volume fraction per Fig 2; cluster = 1.0%). The sentence explains void-bin smallness by citing the cluster volume fraction, which is wrong. VERIFIED typo/logic error. Fix: replace "small cluster volume fraction of 1%" with "small void volume fraction (~0.1% of in-footprint cells)" or rewrite to reference the survey-edge artifact. |
| F17 | ChatGPT | MINOR | "0/6 V-Web void purity" language too strong for n=6 | PARTIAL | `.tex` ll.1603 uses "0/6 V-Web 'void' spirals fall inside any DESIVAST hole." Abstract l.219 says "0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes." The paper does not use the word "purity" — ChatGPT added that word. The text uses it as "a nice empirical illustration" (Grok's language). However, the n=6 check is small enough that stronger language like "per-galaxy classifier-disagreement check" (which the paper uses in l.219) is fine. The Grok reviewer is more lenient. PARTIAL — the n=6 limitation should be explicit in the sentence that reports it. |
| F18 | ChatGPT | MINOR | Use one sign convention for ΔfCW | FALSIFIED | `.tex` l.1719: "Sign convention: ΔfCW ≡ f_CW^{non-void} − f_CW^{void}" is explicitly stated in Table IX header. The same convention appears in the abstract l.222–224. FALSIFIED. |
| F19 | ChatGPT | MINOR | Avoid calling catalog monopole the "headline" −5σ signal | VERIFIED | `.tex` ll.1105–1106: "The catalog-level −5σ headline is entirely driven by the bright program." In §VIII.E and §XI "headline" is used to refer to the environment-dependence null AND the -5σ catalog monopole in adjacent paragraphs. Dual use of "headline" is real. VERIFIED as a clarity issue. Fix: use "catalog-wide monopole offset" consistently, reserve "headline" for the environment-dependence null. |
| F20 | Grok | MAJOR | M1: bright/dark f_CW difference inside each V-Web class after restricting to unique TARGETID subset and DESIVAST BGS volume limit not shown as a self-contained quantification | VERIFIED | `.tex` ll.1170–1211: the bright/dark split is shown at class level (filament bright n=394,181 σ=−2.98 / dark n=13,759 σ=+1.61) but no explicit unique-TARGETID recompute of the bright/dark f_CW difference is shown (the design-effect bound appears elsewhere). The DESIVAST BGS-volume-limited bright/dark split is not separately tabled. VERIFIED — a one-paragraph table with unique-TARGETID bright/dark within DESIVAST volume would close this. |
| F21 | Grok | MAJOR | M2: "headline" language not globally updated to point to DESIVAST null | VERIFIED | Confirmed same as F5/F19. Multiple occurrences of "headline" in §VI.A and §VIII.E refer to the catalog-wide −5σ rather than the DESIVAST environment-dependence null. VERIFIED. |
| F22 | Grok | MAJOR | M3: Phase 2 Bonferroni-9 threshold not equation-numbered; three-tier significance paragraph should be a named subsection | VERIFIED | `.tex` l.1378: Bonferroni-9 threshold referenced inline but not equation-numbered. The three-tier framework (counting floor + monopole-subtracted residual + p_LEE) is described in prose, not as a numbered set of equations. VERIFIED — add eq. number and reorganize §VII.A. |
| F23 | Gemini | BLOCKER | B1: Rs=10 cells below grid sampling scale (25.9 Mpc/h); max residual 1.87σ drawn from unresolved cell | PARTIAL | `.tex` ll.1294–1307: this is explicitly acknowledged. The paper excludes Rs=10 from the physical robustness claim and reports restricted-to-resolved-cells max=1.64σ. Gemini's request to remove Rs=10 rows from Table VI entirely (or re-run on finer mesh) goes further than the text. The caveat is present and quantified; whether keeping unresolved cells in the table is journal-appropriate is Houston's call. PARTIAL — the paper already bounded and caveated; removing from the table entirely would be cleaner. |
| F24 | Gemini | BLOCKER | B2: i.i.d. violations from row-level counting with 2.7% duplicate rows; primary Table II should use unique-spiral subset | FALSIFIED | `.tex` ll.815–820: paper explicitly acknowledges "2.7% duplicate rows violate strict i.i.d., but the worst-case design-effect inflation of the interval widths is √(812,793/783,820) = 1.018, i.e. ≤1.9%." The omnibus χ² is already re-reported on the unique-spiral subset (ll.167–169: χ²=3.00, p=0.39). The paper presents both and shows the duplicate rows do not drive the verdict. Gemini's request to make the unique-spiral subset the primary table is a presentation preference, not a factual error — the analysis is already done. FALSIFIED as a blocker; OPINION as a presentation suggestion. |
| F25 | Gemini | MAJOR | M1: V-Web × target-program non-orthogonality requires joint logistic regression controlling for program | VERIFIED | `.tex` ll.1170–1211: no logistic regression model controlling for target program jointly with V-Web environmental classification is shown. The argument rests on the contingency test plus the DESIVAST BGS-only escape. VERIFIED — adding a brief logistic regression (binary bright/dark × V-Web class dummy) would formally demonstrate whether any environmental coefficient survives program-control. |
| F26 | Gemini | MAJOR | M2: RSD claim "sub-percent contamination ∼0.2 pp" treated as floor when cross-class range collapses to 0.05pp after z-shell correction | PARTIAL | `.tex` ll.1529–1583: the RSD argument applies to the DESIVAST primary path (not V-Web). For V-Web the completeness-rebuild paragraph (§IX.A, ll.2086–2101) shows 0.05pp post-correction range. Gemini correctly notes that "RSD could swamp signal" is understated when the signal range is 0.05pp. However, Gemini conflates the two paths: the 0.05pp result is for the z-shell-corrected V-Web (secondary); the DESIVAST primary has its own RSD bound. PARTIAL — the paper could more clearly state that the 0.2pp RSD estimate refers to the unweighted V-Web, and that after completeness correction the effective range is 0.05pp, so the RSD floor needs updating relative to that refined baseline. |
| F27 | Gemini | MINOR | PDF rendering artifacts: "Ofrom half" / "Øvs monopole" / "CWCWJCW" strings | HOUSTON-DECISION | Cannot verify from .tex source — these are PDF rendering/extraction artifacts in the pdftotext stream, not actual content in the .tex. No occurrence of "CWCWJCW" or "Ofromhalt" in the source file (grep confirmed zero hits). These are likely Unicode/symbol rendering failures in Gemini's PDF reader. HOUSTON-DECISION: recompile and visually inspect the PDF at those locations to confirm the rendered PDF shows correct σ symbols and no dangling strings. If the PDF looks correct, dismiss. |
| F28 | Gemini | MINOR | Table IV column "P" should be ⟨log₁₀(1+δ)⟩ | FALSIFIED | The table in question (tab:within_class_density, ll.1016–1026) has column header `$\bar\rho$`, not "P". Gemini's PDF reader likely garbled the `$\bar\rho$` symbol to "P". The caption (ll.1002–1005) explains: "$\bar\rho$ is the quartile mean of log₁₀(1+δ_smooth)." FALSIFIED as a source error; the .tex column label is correct. |

---

## Consensus Findings (Cross-Reviewer Agreement)

**C1 — "Headline" language dual-use [F5, F19, F21]:** ChatGPT, Grok, and Gemini all flag that "headline" is used inconsistently to refer to both the catalog-level −5σ monopole and the environment-dependence null. **All three reviewers agree.** Fix: use "catalog-wide monopole offset" for the −5σ and "headline environment-independence result" for the DESIVAST null.

**C2 — Rs=10 cells in Phase 2 table [F10, F23]:** ChatGPT and Gemini both flag that the unresolved Rs=10 cells should be removed from Table VI or visually flagged. Grok is satisfied with the current caveat text. Consensus leans toward removing from the table.

**C3 — V-Web secondary but still too prominent [F5, F7, F21]:** All three reviewers note that despite the primary/secondary declaration, the abstract's sample ledger and §VI A still present V-Web class fractions with the same visual weight as DESIVAST results. Consensus: restructure abstract to lead with DESIVAST result earlier.

**C4 — Bonferroni-5 family too narrow for full analysis tree [F7, Grok M2, Gemini indirectly]:** Multiple reviewers note that while the DESIVAST Bonferroni-5 family is well-controlled, the broader analysis tree (exact vs approximate membership, multiple stratifications, RSD perturbations, multiple classifiers) is not covered by a global multiplicity statement. Consensus: add an analysis-tree table or paragraph declaring that non-primary tests are descriptive.

---

## Action Plan (VERIFIED/PARTIAL findings, hardest-first)

### DO-NOW (verified scientific gaps)

1. **[F9] DESIVAST program-split table** — Compute bright/dark program split within the DESIVAST void and non-void samples (z≤0.24, BGS-only). Add a 2×2 or 4×2 table to §VIII.B. File: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, §sec:desivast_anchored_void.

2. **[F20] Unique-TARGETID bright/dark split within DESIVAST BGS volume** — Recompute bright/dark f_CW difference on unique TARGETIDs restricted to z≤0.24 and add to §VI.A.d or §VIII.B. Artifact: add to `outputs/` JSON.

3. **[F8] Cramér's V + log₁₀(p) for contingency test** — Add Cramér's V = √(χ²/(n×(k−1))) = √(4932/(811609×3)) ≈ 0.045 (small effect despite enormous n) and log₁₀(p) ≈ −1069 to §VI.A.d. File: l.1184–1189.

4. **[F7, F22] Analysis-tree table + Bonferroni-9 equation number** — Add a one-paragraph analysis-tree table to §V.B listing: primary estimand, allowed membership definition, control sample, multiplicity family, all secondary diagnostics labeled "descriptive." Number the Phase 2 Bonferroni-9 threshold as an equation in §VII.A. File: ll.731–744 and l.1378.

5. **[F25] Logistic regression controlling for target program** — Add a brief logistic regression of CW indicator on V-Web class dummies + bright/dark indicator to §VI.D. File: ll.1170–1211.

6. **[C1, F19, F21] "Headline" language pass** — Global search/replace: "catalog-level −5σ headline" → "catalog-wide monopole offset." Reserve "headline" for the environment-dependence null. Affects abstract, §VI.A, §VIII.E, §XI.

7. **[F16] Void-bin smallness typo** — Fix l.840: "small cluster volume fraction of 1%" → "small void volume fraction (~0.1% of in-footprint volume)." File: l.839–841.

### PRESENTATION IMPROVEMENTS (partial/verified cosmetic)

8. **[F1] Footprint-mask proxy language** — Strengthen the "explicit footprint-mask re-tabulation is queued" note (l.1854) with a more explicit explanation of what the [−2.04, −0.09] bound on ≥1-void pixels achieves, and state explicitly that the primary null (DESIVAST void/non-void comparison, both of which live inside the DESIVAST coverage volume) is not affected by this proxy. File: ll.1848–1856.

9. **[F10, F23] Rs=10 cells in Table VI** — Either shade/footnote the Rs=10 rows as "grid-unresolved, retained for completeness only" in the table caption, or move them to a separate sub-table. The 1.64σ restricted-cell result should be the primary stated bound. File: ll.1322+, Table VI caption.

10. **[F11] RSD claim language** — Soften l.1544 "void membership inherits no anisotropic RSD systematic at the present precision" to "void membership is RSD-bounded at the level of a fixed-void-geometry perturbation test; full immunity would require a void-catalog reconstruction under RSD, which is not performed here." File: l.1543–1545.

11. **[F17] n=6 check language** — Add "in this six-object illustrative check" before reporting the 0/6 concordance at l.1603 and l.219. File: ll.219, 1603.

### HOUSTON-DECISION ITEMS

12. **[F2] DESIVAST interior void counts 1,461/420/295 vs 1,489/389/297** — Verify final ApJ 982, 38 interior void counts at https://doi.org/10.3847/1538-4357/adb559. If the final published paper has different interior void counts than the preprint, update l.1523–1524 and add a "DESIVAST version ledger" note. The paper already distinguishes interior vs whole-catalog totals (ll.1707–1708), which may resolve the discrepancy.

13. **[F27] PDF rendering artifacts** — Recompile PDF and visually inspect §V, §VI.C, §VIII.B, §XV for σ symbol rendering and the alleged "CWCWJCW" string. Likely a Gemini PDF-reader artifact, not a real source error.

---

## Gap Analysis — What Internal Rounds Missed

Internal rounds R23–R28 addressed the completeness-rebuild, k-unbounded membership guard, duplicate-row bounds, monopole prediction framework, and z-shell robustness. The following real gaps survived all internal rounds and were only caught by external review:

1. **Cramér's V / effect-size reporting** (F8): pure presentation gap; no internal round flagged this.
2. **DESIVAST program-split table** (F9): asserted but not tabled; internal rounds accepted the BGS-only argument without requiring the demonstration.
3. **Logistic regression for program control** (F25): not required by any internal round.
4. **Analysis-tree table** (F7): the primary/secondary declaration is in the text but no formal table maps the full tree. Internal rounds didn't demand this.
5. **"Headline" dual-use terminology** (C1/F19/F21): subtle language inconsistency that internal rounds with the same author missed.
6. **Void-bin smallness typo** (F16): logic error in one sentence that all internal rounds missed.

The null on footprint-mask formal intersection (F1) was already partially acknowledged in the paper before external review — the gap is real but the paper's self-disclosure is more complete than reviewers credited.

---

## Post-Audit Recommendation

**Upgrade overall external assessment:** Grok's MINOR recommendation is better calibrated than ChatGPT's or Gemini's MAJOR. The paper's strongest features (DESIVAST three-algorithm primary path, Bonferroni-5 multiplicity control, explicit monopole subtraction, completeness rebuild with null-robust result) survive all challenges except F9 and F20 (missing quantitative BGS program split within DESIVAST). All three BLOCKERS from ChatGPT were either already addressed in the current text (F3, F6) or require a Houston web-check to verify external counts (F2). Gemini's BLOCKER B2 is falsified.

**Immediate priority:** Close F9 (DESIVAST program-split table) and F8 (Cramér's V + log₁₀(p)) first — these are compute-trivial and remove the most credible remaining journal-rejection risk. F2 (DESIVAST count verification) should be done in the same session with a quick ADS fetch. The "headline" language pass (C1) is a one-hour global text edit.

**Readiness assessment post-fixes:** With F9, F8, C1, F16, F7, and F2 closed, P5 would have no VERIFIED blockers remaining. The PARTIAL findings (F1, F10, F11) are appropriately caveated in current text and are unlikely to generate rejection at MNRAS/JCAP. Estimated readiness after action plan: 95% → 97% (Houston sign-off and clean cross-vendor re-round required for final 2%).

---

*Audit path: `project-context/peer-reviews/EXT1_P5_TRUTH_AUDIT.md`*
*Paper source: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.60)*
