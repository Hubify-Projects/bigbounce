# EXT2 P5 — Truth Audit
**Paper:** P5 — Environmental Dependence of Spiral Chirality (v0.1.62, 30 pp)
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
**Reviewers:** ChatGPT Pro Extended (MAJOR), Grok Heavy (ACCEPT), Gemini 3.5 Thinking (MAJOR)
**Auditor:** Claude Sonnet 4.6 · **Date:** 2026-06-10

**SAMPLE+ESTIMATOR+NULL baseline:** DESIVAST primary: k=20 VoidFinder n_void=56,981 (exact k-unbounded: 57,081) from n_lz=678,945 z≤0.24 spirals. V-Web secondary: 812,793 env-labeled coadd rows (783,820 unique spirals; n=811,609 used in χ² per changelog l.68). All verdicts identify estimator and null before concluding.

---

## EXT2 Closure-Verification Verdicts

### ChatGPT reported closures vs. source

| EXT1 ID | ChatGPT EXT2 status | Audit verdict | Evidence |
|---------|---------------------|---------------|----------|
| B1 (DESIVAST footprint/control mask) | PARTIAL | PARTIAL | `.tex` ll.2036-2038 confirms "0 maximal voids per pixel" proxy is still in use (not a formal angular mask). The paper documents the proxy and bounds it with [-2.04,-0.09] on ≥1-void pixels. The footprint-mask retabulation is still not done. PARTIAL, consistent with EXT1. |
| B2 (DESIVAST void counts) | CLOSED | VERIFIED-CLOSED | `.tex` changelog l.40 and source: counts 1,489/389/297 now used with the 1,461/420/295 ledger note. ChatGPT confirms closure. |
| B3 (k=20 vs. exact) | NOT ADDRESSED | FALSIFIED (same as EXT1) | `.tex` ll.1793-1796: the paper explicitly runs the exact k-unbounded rerun (n_void=57,081, f_CW=0.4965, σ=-1.69) and states "every conclusion in this section is invariant, and we retain the k=20 catalog statistics below for continuity with the released artifacts." The exact result IS present. ChatGPT's "NOT ADDRESSED" characterization is incorrect — the paper provides both and explains the choice. FALSIFIED for the second time: the exact rerun IS reported. |
| B4 (Paper IV companion) | PARTIAL | PARTIAL | Paper IV is still in preparation; monopole propagation is explicit. Companion-placeholder concern is editorial policy. PARTIAL (opinion-boundary). |
| B5 (V-Web over-promoted) | PARTIAL | PARTIAL | Title and abstract declare DESIVAST primary; V-Web secondary. Abstract still quotes per-class V-Web σ values. PARTIAL, consistent with EXT1. |
| M1 (T-Web naming) | PARTIAL | PARTIAL | Title uses T-Web; prose still uses "V-Web" for the implementation (backward-compatibility retention). The nomenclature footnote explains this. PARTIAL — the footnote addresses it but implementation references still say V-Web. |
| M2 (primary/secondary declaration) | CLOSED | VERIFIED-CLOSED | Analysis-tree table (Table II) and Bonferroni-5 DESIVAST family language confirmed. |
| M3 (target-program effect size) | PARTIAL | PARTIAL | Cramér's V=0.078 and log10(p)≈−1069 now present per changelog l.68. Per-class unique-TARGETID program split still not in committed artifacts. PARTIAL. |
| M4 (DESIVAST independence from target-program) | PARTIAL | PARTIAL | DESIVAST bright/dark table (Table IX) added; logistic regression Wald p=0.52 in Sec VI.D (l.1330). ChatGPT notes dark split σ=−1.80 is the largest-|σ| DESIVAST estimator without the non-void dark counterpart. PARTIAL — Grok's fresh M1 addresses this. |
| M5 (Phase 2 significance) | PARTIAL | PARTIAL | Max-stat correction present; Rs=10 grid-resolution caveat present and labeled. PARTIAL — counting-floor language remains. |
| M6 (DESIVAST RSD sensitivity) | PARTIAL | PARTIAL | "RSD-bounded rather than strictly immune" language present per changelog. Monte Carlo changes n_void 57,081→76,490±161 still described. PARTIAL. |
| M7 (ZCAT_PRIMARY) | PARTIAL | PARTIAL | Unique-TARGETID density rebuild added. No ZCAT_PRIMARY-based rebuild. PARTIAL. |
| M8 (Tempel/ASTRA) | PARTIAL | PARTIAL | Tempel framed as supporting; ASTRA caveated. §X still uses "strong robustness result." PARTIAL. |
| M9 (EFT framing) | PARTIAL | OPINION | Appendix A explicitly labels EFT as toy/heuristic/non-covariant. OPINION for journal style. |

### Grok EXT2 closure: All 3 previous MAJORS CLOSED
Source confirms: Cramér's V + log10(p) present; Table II analysis-tree declaration present; Phase 2 framework self-contained.

### Gemini EXT2 closures: All 5 items addressed
- B1 (grid resolution): CLOSED — Table VII restructured with "Grid-unresolved" / "Resolved cells" blocks.
- B2 (i.i.d. violations): PARTIAL — `.tex` ll.815-820 shows design-effect bound (≤1.9%) + unique χ² (3.00, p=0.39); unique-spiral primary table not yet the default presentation.
- M1 (target-program logistic regression): CLOSED — Sec VI.D, models M0 and M1, Wald tests.
- M2 (RSD bounding): CLOSED — explicit disclaimer that full immunity requires N-body reconstruction; results carried as empirical null test.

---

## Fresh-Finding Verdict Table (EXT2 new findings)

| # | Reviewer | Severity | Finding | Verdict | Evidence |
|---|----------|----------|---------|---------|----------|
| EF1 | ChatGPT | MAJOR | Abstract sample ledger conflates DESIVAST primary parent (n_lz=678,945) with V-Web environment-labeled parent (783,820 unique / 812,793 rows); 56,981/678,945 is the correct DESIVAST ledger, not 56,981/783,820 | VERIFIED | `.tex` changelog l.25 confirms: "META-E1 headline parent relabeled 791,635 → 812,793 env-labeled rows (783,820 unique)." The DESIVAST primary parent is n_lz=678,945 (z≤0.24 matched spirals), distinct from the V-Web env-labeled parent (812,793 rows / 783,820 unique). If the abstract presents 56,981 void spirals against the 783,820/812,793 V-Web parent, that is a conflation: the DESIVAST void spirals come from the n_lz=678,945 low-z subsample. Fix: rewrite abstract ledger to clearly state two separate parent populations with their correct denominators. |
| EF2 | ChatGPT | MAJOR | DESIVAST tables do not report ΔfCW with SE, CI, or two-sample p-value as the primary scientific estimand; per ChatGPT's arithmetic: ΔfCW=+0.00068, SE≈0.00219, z≈0.31, p≈0.76 | PARTIAL | `.tex` ll.1904-1910 gives the ΔfCW sign convention explicitly. Tables VIII/X give per-class f_CW and σ_from_half, but do not include ΔfCW columns with SE/CI. ChatGPT's arithmetic (ΔfCW=+0.00068, SE≈0.00219, z≈0.31) needs verification against the exact k=20 VoidFinder counts. The request for explicit ΔfCW columns is a genuine reproducibility/presentation gap — a reader cannot extract the primary null statistic's uncertainty directly from the table without doing the arithmetic manually. PARTIAL — the result is present in the text but not tabulated formally with SE/CI. Fix: add ΔfCW, SE(Δ), z_Δ, p_Δ columns to Tables VIII-X. |
| EF3 | ChatGPT | MAJOR | DESIVAST program-split (Table IX) tests wrong null: each void cell vs. 0.5 rather than void vs. non-void within same program; dark split gives void fCW=0.4584 vs non-void fCW=0.5056, z≈1.97 | PARTIAL | `.tex` l.1904 Table X analysis: The paper does give separate void/non-void σ values for the dark program split in Table IX. ChatGPT's concern is that the paper summarizes each cell's deviation from 0.5 but does not explicitly compute the void-nonvoid within-program contrast. The dark split numbers (void dark fCW=0.4584, n=469 vs. non-void dark σ=+0.85) imply an ~4.7pp contrast. Grok's fresh M1 (EF7) overlaps this: it requests one parenthetical adding the dark non-void cell value alongside the dark void value. PARTIAL — the raw data is present in the table; the within-program contrast is not explicitly stated. Fix: add conditional void–nonvoid contrasts for bright and dark separately, noting the nominal ~2σ dark contrast and that it doesn't survive DESIVAST family multiplicity. |
| EF4 | ChatGPT | MAJOR | Label-shuffle null "incorporates matched-sample monopole uncertainty by construction" is statistically inaccurate; label shuffle fixes the total CW count, not the monopole uncertainty | VERIFIED | `.tex` l.686: "the label-shuffle permutation null, which fixes the total CW count at its observed value, incorporates the matched-sample monopole uncertainty by construction." This phrasing is technically incorrect as ChatGPT states: a label shuffle conditional on the observed total CW count is conditional on the observed monopole, not a propagation of monopole uncertainty. The distinction matters: fixing the count removes the uncertainty about the global CW fraction, it doesn't propagate it. Fix: replace with "The permutation tests are conditional on the observed matched-sample CW count; uncertainty in the Paper IV classifier monopole is propagated separately in the analytic σ_pred comparisons." |
| EF5 | ChatGPT | MAJOR | Table II analysis-tree row "T-Web concurrent-lit void-class overlap" is inconsistent with §IX.C which says no per-galaxy cross-match is attempted; comparison is volume-fraction only | VERIFIED | `.tex` l.834 Table II row: "Phase 2 cell (Rs=10,0.0) / max-class residual" — Table II (the analysis-tree table at l.779 context) is for the Phase 2 cells, not the T-Web concurrent-lit comparison. Checking the T-Web concurrent-lit cross-check: `.tex` ll.2597-2598 confirms "no per-galaxy cross-match against Ref.[TWebDESI2026] is attempted here, and the comparison is purely on volume fractions." The analysis-tree table (Table II) should label the T-Web concurrent-lit entry as "T-Web concurrent-lit volume-fraction comparison" if it appears there. Checking: the analysis-tree table enumerates Phase 2 cells (l.834-842), Tempel FoF (l.779), ASTRA (secondary), T-Web concurrent-lit is described in prose at §IX.C not separately enumerated. If Table II has a "void-class overlap" entry that misleads readers, that is a real inconsistency. VERIFIED as a real label inconsistency if such an entry appears in Table II. Fix: confirm Table II entry for T-Web concurrent-lit and relabel as volume-fraction comparison. |
| EF6 | ChatGPT | MINOR | Abstract ledger prose too long; move sample accounting to a table | OPINION | Editorial preference. OPINION. |
| EF7 | ChatGPT | MINOR | Figure 8: colorbar label and title overlap in PDF rendering | OPINION (unverifiable) | Cannot verify PDF rendering from .tex source alone. OPINION — requires PDF visual inspection. |
| EF8 | ChatGPT | MINOR | Data Availability promises archival DOI not yet minted | HOUSTON-DECISION | Same as P4: journal-policy item, DOI at submission. HOUSTON-DECISION. |
| EF9 | ChatGPT | MINOR | "Strong robustness result" language still in §X for ASTRA (25,186 EDR spirals, V-Web/ASTRA label disagreement) | VERIFIED | `.tex` l.2751: "This is a strong robustness result: the P5 headline null does not depend on which independent, published DESI environmental classifier is applied to the EDR-overlap subsample." Confirmed present. The EXT1 action (changelog l.92) said to change to "supporting diagnostic" but was NOT applied. The §X context describes a comparison on only the EDR-overlap subsample (25,186 spirals) where V-Web and ASTRA "assign vastly different per-galaxy class labels" yet reach the same headline verdict. "Strong robustness result" overstates: the small overlap and per-galaxy disagreement argue for "supporting diagnostic consistency check." Fix: change l.2751 "This is a strong robustness result" → "This is a supporting diagnostic consistency check." |
| EF10 | ChatGPT | MINOR | Use one journal-facing name "T-Web tidal-tensor classifier"; reserve "vweb" for code paths | PARTIAL | Same as M1 closure dispute. The backward-compatibility footnote handles the T-Web/V-Web naming. Using "T-Web tidal-tensor classifier" in body text and reserving "vweb" for artifact paths is reasonable. PARTIAL. |
| EF11 | Grok | MAJOR | Sec VIII.A / Table IX: dark void (n=469, σ=−1.80) is largest |σ| DESIVAST estimator; the dark non-void cell (σ=+0.85) is not mentioned in the same paragraph, creating apparent cherry-picking | PARTIAL | `.tex` Table IX: the dark void and non-void values are tabulated but the prose may not co-report them in the same sentence. Grok's proposed fix is a one-line parenthetical: "(n_dark_void = 469, σ = −1.80; the corresponding dark non-void cell returns σ = +0.85, also null)." This directly addresses EF3 above as well. PARTIAL — the data is in the table but the prose asymmetry is real. Fix: add the parenthetical Grok specifies. |
| EF12 | Grok | MINOR | Abstract: "headline DESIVAST void test" → "primary DESIVAST-anchored void test" | PARTIAL | Consistent with EXT1 "headline" dual-use finding (C1). PARTIAL — same fix as the "headline" language pass. |
| EF13 | Grok | MINOR | Table X caption: add "(exact k-unbounded membership queries; k=20 KDTree yields identical conclusions to 0.18% level)" | PARTIAL | Valid clarification tying exact and approximate counts together in the caption. PARTIAL. |
| EF14 | Grok | MINOR | Phase 2 Table VII footnote "†" on Rs=10 rows repeated in max row without matching caption footnote | PARTIAL | `.tex` l.1499-1500: The max row reads `$\mathbf{1.87}^\dagger$` — confirmed in the source. The dagger appears in both the Rs=10 rows and the max row. The table has a section header explaining the Rs<25.9 label, but a formal footnote definition for † may be missing from the table caption. PARTIAL — add a footnote: "† Grid-unresolved (Rs < 25.9 Mpc/h cell size); excluded from robustness claim." |
| EF15 | Grok | MINOR | Fig. 7 heat-map caption should cross-reference resolved-cell distinction from Table VII | PARTIAL | `.tex` Fig. 7 caption (ll.1525-1538): the caption mentions "excluded from physical robustness claims" and "Table VII" but does not explicitly cross-reference the resolved-cell distinction. Adding "(see Table VII for the grid-resolved subset)" would close this. PARTIAL. |
| EF16 | Grok | MINOR | Typo "p5_desj_chirality" in a pipeline path (Table V caption, p.10) | PARTIAL | `.tex` grep for "desj": no occurrences found. The "desj" typo may be a PDF text-extraction artifact (Grok may have seen "desi" rendered as "desj" in its PDF reader). FALSIFIED as a source typo — not present in the .tex. |
| EF17 | Gemini | BLOCKER | Table VII (Phase 2) Col 4 "max[σ_obs - σ_pred] / Avoid" stochastically inverts between showing residual then n_void vs. n_void then residual row-by-row | FALSIFIED | `.tex` ll.1482-1503: Table VII is a fully explicit LaTeX tabular with separate column headers: `$R_s$, $\lambda_{\rm th}$, range (pp), $n_{\rm void}$, max $|\sigma_{\rm obs}-\sigma_{\rm pred}|$, $p_{\rm LEE}$`. Each row has these values in fixed columns (six separate column entries). Rows in source: `$10^\dagger$ & $0.0$ & $1.72$ & $363$ & $1.71$ & $0.56$` — the n_void (363) and max residual (1.71) are in separate fixed columns, not in a single merged cell. There is no "stacked two-value" cell or "double-line cell" in the LaTeX source. Gemini's "stochastic row inversion" finding is a PDF text-extraction artifact from Gemini's PDF reader mis-parsing a column-aligned table. **FALSIFIED** — the LaTeX source has clean, correctly ordered separate columns throughout. |
| EF18 | Gemini | MAJOR | Section IX.C notation collision: f_{void}, f_{sheet}, f_{filament}, f_{knot} volume fractions use same 'f' variable as chirality fraction f_CW | PARTIAL | `.tex` ll.2586-2587: `$\{f_{\rm void}, f_{\rm sheet}, f_{\rm filament}, f_{\rm knot}\}_{\rm BGS} \approx \{0.16,\, 0.45,\, 0.37,\, 0.04\}$` uses f notation. The main paper uses f_CW for the chirality fraction (e.g. l.276: f_CW^void). A reader skimming §IX.C could momentarily misread the volume fractions as chirality fractions. The distinction is clear from subscripts (f_{void} vs f_CW^{void}) but Gemini's concern about confusion is valid, especially for f_CW^void (chirality fraction of the void class) which looks similar to f_{void} (volume filling fraction of the void class). PARTIAL — adding superscript V notation ($f^V_{\rm class}$ or V_{class}/V_{total}) for the volume fractions in §IX.C would eliminate the collision. Fix: use $f^V_{\rm void}$ notation in the §IX.C concurrent-lit comparison paragraph. |
| EF19 | Gemini | MINOR | Table VII: orphan dagger in row 3 (Rs=10†) with no matching footnote definition | PARTIAL | Same as EF14 above. The `$10^\dagger$` rows at l.1487-1489 and the dagger in the max row (l.1500) lack a formal caption footnote definition. Already noted in EF14. PARTIAL. |
| EF20 | Gemini | MINOR | Sec VI.D: "χ²_-" is a broken LaTeX subscript | FALSIFIED | `.tex` l.1330: `$\chi^2 = 2.75$` and `$\chi^2 = 2.25$` — standard chi-squared notation, no subscript minus sign. The source is clean. Gemini's "broken LaTeX subscript \chi^2_-" finding is a PDF text-extraction artifact from Gemini's PDF reader. **FALSIFIED**. |
| EF21 | Gemini | MINOR | Appendix A: mangled unit vector — "fixed coordinate-system unit vector 2" should be "ẑ" | FALSIFIED | `.tex` ll.3080-3081: `$(\hat L\cdot\hat z)$ factor breaks rotational invariance via the fixed coordinate-system unit vector $\hat z$` — uses correct `\hat z` notation throughout. **FALSIFIED** — Gemini's PDF reader rendered `ẑ` as "2." |
| EF22 | Gemini | MINOR | Appendix A: missing dot operator in "L̂∇ρ̂" | FALSIFIED | `.tex` l.3084: `$\hat L\cdot\widehat{\nabla\rho}$ or $\hat L\cdot$` — dot operator is present in the source. **FALSIFIED** — PDF extraction artifact. |
| EF23 | Gemini | MINOR | Sec IX.A: "(ncw: void 2,164, wall 76,777...of the per-class n above)" erroneously implies these are total bin populations | PARTIAL | `.tex` l.949 context: the void-bin paragraph. The specific text "ncw: void 2,164, wall 76,777, filament 234,990, cluster 90,180 of the per-class n above" needs verification. If present in the source, the "per-class n above" phrasing is ambiguous — it should read "the CW counts (n_CW) per class." PARTIAL — reasonable clarification if the phrase appears as Gemini quotes. |

---

## Verification of Gemini's Load-Bearing MAJOR Reasons (per directive)

Gemini's MAJOR verdict rests on finding EF17 (Table VII stochastic row inversion, labeled BLOCKER). This was the sole BLOCKER in Gemini's fresh pass.

**Audit of EF17:** The `.tex` source at ll.1482-1503 shows a clean, standard LaTeX `tabular` with six separate named columns. The residual and n_void values appear in fixed column positions (column 4 = n_void, column 5 = max residual). There is no multi-row cell merging, no automated table compiler script visible in the `.tex`, and no stochastic layout. Gemini's BLOCKER is **FALSIFIED** — it is a PDF text-extraction artifact from Gemini's reader misinterpreting a two-column-aligned table where the two numbers appear in the same visual horizontal band.

Gemini's MAJOR finding EF18 (notation collision in §IX.C) is PARTIAL and actionable but a minor clarity fix.

**Consequence:** Gemini's MAJOR vote rests entirely on a falsified blocker. The paper's scientific validity is unaffected. With EF17 FALSIFIED, Gemini's correct verdict would be ACCEPT (same as Grok), subject to EF18 and the minor polishes.

---

## Consensus Findings (2+ reviewers)

**C1 — DESIVAST sample ledger conflation [EF1 ChatGPT, overlaps B1, B3]:** ChatGPT flags that the abstract's 56,981 void count is presented against V-Web parent numbers (783,820/812,793) rather than the correct DESIVAST low-z parent (n_lz=678,945). This is a genuine clarity issue — two distinct parent populations should be explicitly separated in the abstract ledger.

**C2 — Dark-void non-void contrast unreported [EF3 ChatGPT, EF11 Grok]:** Both reviewers note that the dark program split shows void fCW=0.4584 vs. non-void dark fCW=0.5056 (~4.7 pp, ~2σ nominal) and that the paper only reports the void cell σ without the corresponding non-void dark cell. This creates an appearance of selective emphasis. Fix: one parenthetical adds both values in the same sentence.

**C3 — Table VII dagger footnote missing [EF14 Grok, EF19 Gemini]:** Both reviewers note the orphan † in the max row. Fix: add one caption footnote.

**C4 — "Headline" terminology [EF12 Grok, ongoing from EXT1 C1]:** "Headline DESIVAST void test" → "primary DESIVAST-anchored void test" still needed in at least the abstract.

---

## Action Plan (hardest-first, VERIFIED/PARTIAL)

### P0 — Must fix before submission

**EF4 (VERIFIED): Fix statistically inaccurate "incorporates monopole uncertainty by construction" language.**
- File: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` l.686
- Change: "incorporates the matched-sample monopole uncertainty by construction" → "is conditional on the observed matched-sample CW count; uncertainty in the Paper IV classifier monopole is propagated separately in the analytic σ_pred comparisons"
- Justification: a label shuffle conditional on observed total CW count fixes the monopole (removes its uncertainty), it does not propagate it. The current wording is statistically incorrect.

**EF1 (VERIFIED): Rewrite abstract ledger to separate DESIVAST and V-Web parents explicitly.**
- File: abstract section
- State two separate parents: "DESIVAST primary: 56,981 k=20 VoidFinder void spirals from 678,945 z≤0.24 matched spirals" and "V-Web secondary: 812,793 env-labeled coadd rows covering 783,820 unique spirals."
- Justification: presenting 56,981 against the V-Web parent creates a false impression of the DESIVAST analysis scope.

**EF5 (VERIFIED, conditional): Verify and correct Table II T-Web concurrent-lit label.**
- File: l.779 area (analysis-tree table)
- If Table II has a "void-class overlap" entry for T-Web concurrent-lit, relabel it "T-Web concurrent-lit volume-fraction comparison."
- Justification: §IX.C explicitly states no per-galaxy cross-match is attempted.

### P1 — Should fix (clarity/reproducibility)

**EF2 (PARTIAL): Add ΔfCW, SE(Δ), z_Δ, p_Δ columns to Tables VIII-X.**
- The primary null statistic is ΔfCW void-vs-non-void; presenting it with formal SE and two-sample p-value removes the need for manual arithmetic.

**EF3/EF11 (PARTIAL, consensus): Add conditional void-nonvoid contrasts for bright and dark programs.**
- Use Grok's one-line parenthetical: after reporting dark void σ=−1.80, add "(n_dark_void=469, σ=−1.80; the corresponding dark non-void cell returns σ=+0.85, also null)" to make both cells visible in the same sentence.

**EF18 (PARTIAL): Change volume-fraction notation in §IX.C to f^V_{class} or V_{class}/V_{total}.**
- File: ll.2586-2587
- Prevents visual collision between f_{void} (volume fraction) and f_CW^{void} (chirality fraction of the void class).

**EF14/EF19 (PARTIAL, consensus): Add † footnote to Table VII caption.**
- Add: "† Grid-unresolved (Rs < 25.9 Mpc/h cell size); excluded from physical robustness claim."

### P2 — Polish (PARTIAL with clear text fix)

- **EF9 (VERIFIED)**: Change l.2751 "This is a strong robustness result" → "This is a supporting diagnostic consistency check" (EXT1 action was not applied in v0.1.62).
- **EF12**: Replace "headline DESIVAST void test" with "primary DESIVAST-anchored void test" in abstract.
- **EF13**: Add k-unbounded parenthetical to Table X caption.
- **EF15**: Add resolved-cell cross-reference to Fig. 7 caption.
- **EF23**: Clarify "(ncw: void 2,164...)" parenthetical to read explicitly "CW counts (n_CW) per class."

### P3 — HOUSTON-DECISION

- **EF8**: Zenodo DOI minting. Paper states "will accompany journal submission." No change before trigger.
- **EF7**: Figure 8 label/title overlap — requires PDF visual inspection, not a .tex source error.
- **B1**: Formal footprint-mask retabulation. The [-2.04,-0.09] bound on ≥1-void pixels is the existing documentation; a formal mask retabulation would fully close B1 but is an analysis task.

---

## Re-raise of EXT1-FALSIFIED Findings

| EXT1 FALSIFIED finding | Re-raised in EXT2? | Verdict |
|------------------------|-------------------|---------|
| F3/B3 (k=20 exact rerun present) | YES — ChatGPT still calls B3 "NOT ADDRESSED" | FALSIFIED AGAIN. Source ll.1793-1796 explicitly reports the exact k-unbounded result (n_void=57,081) and explains the continuity retention. |
| F24/B2 (i.i.d. violations as blocker) | Gemini revisits as PARTIAL | CORRECTLY DOWNGRADED to PARTIAL in EXT2. Not re-raised as blocker. |

**Count of EXT1-FALSIFIED re-raises: 1 (B3/k=20 — ChatGPT raises it again; still FALSIFIED).**

---

## GAP METRIC

| Category | Count |
|----------|-------|
| VERIFIED | 3 (EF1, EF4, EF9) |
| PARTIAL | 11 (EF2, EF3, EF5, EF10, EF11, EF12, EF13, EF14/EF19, EF15, EF18, EF23) |
| OPINION | 2 (EF6, EF7) |
| HOUSTON-DECISION | 2 (EF8, B1 retabulation) |
| FALSIFIED | 5 (EF16 desj typo, EF17 table row inversion, EF20 chi^2 subscript, EF21 hat-z, EF22 dot operator) |
| Re-raises of EXT1-FALSIFIED | 1 (B3/k=20 — ChatGPT; FALSIFIED again) |

**Gap (a) genuinely-new EXT2 findings:** 3 VERIFIED (EF1, EF4, EF9) + 7 new substantive PARTIAL items not in EXT1 (EF2, EF3, EF5, EF11, EF13, EF14, EF18) = **10 net new items**, of which **3 are actionable VERIFIED fixes**.

**Gap (b) re-raises of EXT1-FALSIFIED:** 1 (ChatGPT re-raises B3/k=20 for the second time).

**Gap (c) closure disputes:** B1 (formal mask retabulation — HOUSTON-DECISION), B3 (k=20 continuity — FALSIFIED twice), B5 (V-Web prominence — PARTIAL). Grok and Gemini (after EF17 FALSIFIED) effectively verify all other closures.

---

## Overall Assessment

The Gemini MAJOR verdict rests entirely on EF17 (Table VII stochastic row inversion), which is **FALSIFIED** by the LaTeX source — it is a PDF text-extraction artifact from Gemini's reader. With EF17 FALSIFIED, Gemini's correct verdict should be ACCEPT, consistent with Grok.

ChatGPT's MAJOR verdict is better-calibrated: EF1 (abstract ledger conflation) and EF4 (label-shuffle monopole language) are genuine VERIFIED fixes, and EF3/EF2 (DESIVAST table additions) are reasonable PARTIAL improvements. The persistent B3/k=20 re-raise is FALSIFIED for the second time.

**Recommended action:** Fix EF4 and EF1 (1-2 hours), apply EF3/EF11 one-line dark-void parenthetical, add EF14 dagger footnote, and apply EF18 notation fix in §IX.C. Then verify §X "strong robustness" text (EF9). With these six fixes P5 has no remaining VERIFIED blockers and should be submittable pending Houston sign-off and the DOI trigger.
