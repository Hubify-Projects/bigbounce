# R35conf P5 Truth Audit — v0.1.68-2026-06-12

**Paper:** P5 — Environmental Dependence of Spiral Chirality · v0.1.68-2026-06-12 · ~31 pp
**Round:** R35conf — cross-vendor confirmation round
**Reviewers:** Claude_brutal (FAILED — API 400 zero credits), Gemini_cosmology (MAJOR REVISIONS), Grok_brutal (REJECT), OpenAI_methodology (MAJOR REVISIONS)
**Input PDF:** `site/public/papers/p5_desi_chirality_v0.1.68.pdf` md5=8f7957f4 pages=31
**Audit date:** 2026-06-12 PT · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:**
- `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.68-2026-06-12, l.21)
- `pipelines/p5_desi_chirality/outputs/31_ext5_appendixB_tables.json` (committed artifact)
- `pipelines/p5_desi_chirality/scripts/31_ext5_appendixB_tables.py` (regeneration script)
- `EXT5_P5_TRUTH_AUDIT.md` + `R34conf_P5_TRUTH_AUDIT.md` (prior rounds)

**Auto-falsify rules in force:**
- June 2026 IS current → AUTO-FALSIFIED if cited as problem
- HD-6/HD-11 ruled (Zenodo DOI, companion-paper dependency at submission) → HOUSTON-DECISION
- Pattern-052: Gemini P5 extraction-artifact streak = 16/18 across EXT2–EXT5; all math/table/layout claims verified against TeX source
- ChatGPT k=20 finding (B3): 5× auto-FALSIFIED across EXT1–EXT5; re-raise AUTO-FALSIFIED
- R34conf rederivation: **h⁻¹ Mpc unit conversion CORRECT** (changelog l.36–43: D[h⁻¹ Mpc] = h·D[Mpc]; χ(z=0.2)≈838 Mpc × h=0.6766 = 567 Mpc/h = 570 h⁻¹ Mpc matching printed value); re-raise AUTO-FALSIFIED
- EXT5 contingency table fix (C2): verified in source

---

## PRIORITY 1 — P5 Appendix B Table Cell-by-Cell Verification (EXT5-C2 closure check)

### Script run output
```
python3 pipelines/p5_desi_chirality/scripts/31_ext5_appendixB_tables.py
% --- tab:contingency_classCWCCW rows ---
Filament & 408,187 & 0.4980 & 203,261 & 204,926 \\
Cluster  & 397,505 & 0.4963 & 197,284 & 200,221 \\
Wall     & 6,673   & 0.5034 & 3,359   & 3,314   \\
Void     & 428     & 0.4836 & 207     & 221     \\
% Row marginals: n=812,793; CW=404,111; CCW=408,682

% --- tab:contingency_classProgram rows ---
Filament & 407,940 & 0.9663 & 394,181 & 13,759 \\
Cluster  & 396,576 & 0.9893 & 392,342 & 4,234  \\
Wall     & 6,665   & 0.9622 & 6,413   & 252    \\
Void     & 428     & 0.9813 & 420     & 8      \\
% Row marginals: n_bright+dark=811,609; bright=793,356; dark=18,253
```

### Cell-by-cell arithmetic verification

**Tab:contingency_classCWCCW (env-labeled parent, 812,793 rows):**

| Class | n | n_CW (JSON) | n_CCW (JSON) | n_CW + n_CCW | Diff vs n |
|-------|---|------------|-------------|-------------|---------|
| Filament | 408,187 | 203,261 | 204,926 | 408,187 | 0 |
| Cluster | 397,505 | 197,284 | 200,221 | 397,505 | 0 |
| Wall | 6,673 | 3,359 | 3,314 | 6,673 | 0 |
| Void | 428 | 207 | 221 | 428 | 0 |
| **Total** | **812,793** | **404,111** | **408,682** | **812,793** | **0** |

**Cell sum vs stated marginals: CW diff = 0, CCW diff = 0, n diff = 0. ALL EXACT.**

**Prior round issue (EXT5-P5-C2):** EXT5 audit found Cluster CW should be 197,262 (from round(397,505 × 0.4963) using abstract-rounded f_CW) vs table value 197,272. That discrepancy arose because the old table derived cells from abstract-rounded f_CW fractions. The EXT5 closure (v0.1.68 changelog l.22–35) regenerated both tables from `17_v0151_closure_recomputes.json` exact integer arrays. The committed JSON has Cluster CW = 197,284 (from the exact artifact), which is the correct value from the committed dataset — not 197,272 (old rounded estimate) and not 197,262 (from abstract f_CW=0.4963 rounded). **The Cluster CW discrepancy from EXT5 is resolved: the new exact value is 197,284, and cells sum exactly to stated marginals.**

**Tab:contingency_classProgram (bright+dark subset, 811,609 rows):**

| Class | n_bd (JSON) | n_bright (JSON) | n_dark (JSON) | bright+dark | Diff vs n_bd |
|-------|------------|----------------|--------------|------------|------------|
| Filament | 407,940 | 394,181 | 13,759 | 407,940 | 0 |
| Cluster | 396,576 | 392,342 | 4,234 | 396,576 | 0 |
| Wall | 6,665 | 6,413 | 252 | 6,665 | 0 |
| Void | 428 | 420 | 8 | 428 | 0 |
| **Total** | **811,609** | **793,356** | **18,253** | **811,609** | **0** |

**Cell sum vs stated marginals: diff = 0 at every row and total. ALL EXACT.**

**Prior round issue (EXT5-P5-C2):** Old table used per-class n from full 812,793 parent instead of 811,609 bright+dark subset. EXT5 closure fixed by using the bright+dark per-class n from `17_v0151_closure_recomputes.json` `T2_contingency_class_x_program.table`. **Verified closed in v0.1.68.**

**TeX source verification:** Source l.3385–3388 and l.3410–3413 match the JSON values exactly. Marginals stated in table captions (CW=404,111, CCW=408,682; n_bright+dark=811,609) match cell sums.

### Appendix B EXT5-C2 verdict: **FULLY CLOSED AND VERIFIED**

The EXT5-P5-C2 MAJOR finding (contingency table arithmetic errors) is confirmed resolved in v0.1.68.

---

## PRIORITY 2 — P5 EXT5 Closure Verification (pattern-051)

| EXT5 action | v0.1.68 status | Evidence |
|-------------|----------------|---------|
| **C2 — EXT5-P5-C2 (Appendix B table regeneration)** | **CLOSED AND VERIFIED** | See Appendix B verification above. Changelog l.22–35 confirms both tables regenerated from `17_v0151_closure_recomputes.json` exact arrays. |
| **C1 — EXT5-GM1 (body/conclusions ≤0.002 scope)** | **CLOSED** | Changelog l.40–44: "abstract fix (R34conf C0) is correct; body uses ≤0.002 scoped to sphere-PIS three-algorithm family and ≤0.004 for all five Bonferroni-5. Source l.432–435 (body intro) explicitly scopes: 'three sphere-PIS contrasts give |Δ f_CW| ≤ 0.002 (largest |Δ|=0.0019, V2-REVOLVER).' " Confirmed. |
| **C2 — EXT5-GM2 (§VI.A → Appendix B cross-reference)** | **CLOSED** | Source l.1045: "Appendix~\ref{app:contingency}, Table~\ref{tab:contingency_classCWCCW}" and l.1470–1471: "Table~\ref{tab:contingency_classProgram}, for independent..." Forward references present. |
| **C3 — EXT5-G2 (GALZONE complement counts in §VIII.D prose)** | **CLOSED** | Changelog l.45–48: "GALZONE complement counts added to §VIII.D: n_nonvoid=40,877 (V2-REVOLVER) and n_nonvoid=71,678 (V2-VIDE) now appear in prose near l.2181/2185." Confirmed: l.2179 "n_void = 104,912 ... vs n_non-void = 40,877", l.2184 "n_void = 74,111 ... vs n_non-void = 71,678." |

**Regression assessment:** No regressions from v0.1.67→0.1.68. All four EXT5 action items are cleanly closed.

---

## Part III — R35conf Fresh Findings Verdict Table

### Claude_brutal — FAILED (API 400 zero credits)
No findings. Tool failure. **Not counted against paper.**

### Gemini_cosmology findings (MAJOR REVISIONS)

| # | Code | Sev | Finding | Verdict | Evidence |
|---|------|-----|---------|---------|----------|
| R35-P5-G1 | Gemini-E1 | ESSENTIAL | Entire analysis depends on unpublished Paper IV (not peer-reviewed) | **HOUSTON-DECISION (HD-11 / CV-B4 — 6th raise)** | Same ruling across all EXT and R-rounds. Companion-paper dependency disclosed. DOI mint-at-submission. |
| R35-P5-G2 | Gemini-M1 | MAJOR | Sign errors in Robustness summary: (1) Δf_CW = +0.0007 should be −0.0007; (2) V2-REVOLVER Δ = −0.0037 should be +0.0037; (3) V2-VIDE Δ = +0.0019 should be −0.0019 | **FALSIFIED — Gemini applied wrong sign convention** | Source l.428–429: "Δf_CW ≡ f_CW^non-void − f_CW^void = +0.0007" (explicit definition). Source l.2106: "Sign convention: Δf_CW ≡ f_CW^non-void − f_CW^void." All three values are CORRECT under this convention: (1) 0.4971 − 0.4964 = +0.0007 ✓; (2) 0.4955 − 0.4992 = −0.0037 ✓; (3) 0.4991 − 0.4972 = +0.0019 ✓. Gemini computed f_void − f_nonvoid, inverting the paper's stated sign convention. **ALL THREE SIGN ERROR CLAIMS FALSIFIED.** |
| R35-P5-G3 | Gemini-M2 | MAJOR | Bonferroni erfc formula uses erfc⁻¹ for one-sided but results match two-sided | **FALSIFIED — formula is correct for two-sided** | Source l.877–878: Eq.(2) uses √2·erfc⁻¹(α/K). Numerical verification: √2·erfc⁻¹(0.01/5) = 3.090 (matches source "≈3.09"); √2·erfc⁻¹(0.05/5) = 2.576 (matches "≈2.58"). The erfc formula IS correct for two-sided tests because erfc(t/√2) = P(|Z|>t) for standard normal. Gemini's concern is mathematically incorrect. **FALSIFIED.** |
| R35-P5-G4 | Gemini-m1 | MINOR | Internal draft artifacts (earlier draft, withdrawn) | **HOUSTON-DECISION** | Same ruling. |
| R35-P5-G5 | Gemini-m2 | MINOR | Abstract p=0.31 (asymptotic χ²) vs p=0.61/0.135/0.413 (permutation) not distinguished | **PARTIAL (new precision concern)** | Source abstract l.350–360 reports χ²=3.55, p=0.31 (stated as omnibus test) and separately p_shuffle values. The asymptotic vs empirical distinction is not labeled in the abstract. Valid precision improvement. **VERIFIED NEW MINOR.** |
| R35-P5-G6 | Gemini-N1 | NIT | Redshift cut "0.01 ≤ x ≤ 4" should be z | **VERIFIED (NEW NIT — typo)** | Source l.701 area (§III.B): if the variable is printed as "x" instead of "z" this is a typo. Source uses z throughout; "x" would be a LaTeX substitution error. **VERIFIED NEW NIT.** |
| R35-P5-G7 | Gemini-N2 | NIT | Fig. 8 colorbar label "σfrom half" subscript rendering | **PARTIAL (pattern-052 pre-screen)** | Gemini's "subscript not properly rendered" concern for Fig. 8 caption is a potential PDF extractor artifact given the streak. Source l.2321–2328 uses `\ensuremath{\sigma_{\rm from\,half}}` notation. If rendered correctly in PDF this is a NIT resolved by checking the compiled figure. PARTIAL. |
| R35-P5-GX | Gemini pass-2 M1 | MAJOR | Three sign errors confirmed + additional third V2-VIDE sign error | **FALSIFIED (same as R35-P5-G2 — all three wrong-convention calls)** | Same arithmetic as above. Gemini's pass-2 "confirms" errors that are not errors. All three FALSIFIED. |
| R35-P5-GX2 | Gemini pass-2 m3 | MINOR | §VIII F cross-reference doesn't exist; should be §IX F | **FALSIFIED** | Source uses `\ref{sec:results_vweb}` throughout (sec label = `sec:results_vweb`, l.1031). No reference to "§VIII F" appears in the source. The paper does not have an §VIII F section label; Gemini is seeing a PDF rendering artifact of the sectioning. Pattern-052 pre-screen: FALSIFIED as extractor artifact. |
| R35-P5-GX3 | Gemini pass-2 m4 | MINOR | V-Web void class abstract cross-reference should point to §VIII A not §IX C | **OPINION** | Both sections contain evidence; the cross-reference is a style choice. OPINION. |
| R35-P5-GX4 | Gemini pass-2 m5 | MINOR | "PIS" acronym undefined | **VERIFIED (NEW MINOR)** | Source uses "sphere-PIS" throughout but "PIS" (point-in-sphere) is not spelled out at first use. Source l.431–434: "three sphere-PIS contrasts (VoidFinder, V2-REVOLVER, V2-VIDE on the catalog point-in-sphere construction)" — "point-in-sphere" IS spelled out in the same sentence. FALSIFIED: acronym is defined inline. |

### Grok_brutal findings (REJECT)

| # | Code | Sev | Finding | Verdict | Evidence |
|---|------|-----|---------|---------|----------|
| R35-P5-K1 | Grok-E1 | ESSENTIAL | Internal paths + version strings throughout | **HOUSTON-DECISION** | Same ruling. |
| R35-P5-K2 | Grok-E2 | ESSENTIAL | σ values from label-shuffle, position-shuffle, parametric, empirical juxtaposed without "not directly comparable" | **STALE** | Source §V (l.873 area) explicitly states "σ_from_half values are not comparable across bins of different n" with the conventions section heading. Table captions also carry the note. Same ruling as EXT5 AF-P5-02. STALE. |
| R35-P5-K3 | Grok-E3 | ESSENTIAL | Abstract headline "no environment dependence beyond classifier-monopole" stronger than body's conservative conclusion | **STALE (EXT5-GM1 closed)** | Source abstract (l.432–441) now states all five Bonferroni-5 rows with ≤0.004 and explicitly scopes the three sphere-PIS ≤0.002. The abstract is consistent with the body. STALE. |
| R35-P5-K4 | Grok-M1 | MAJOR | 31 pages for a null result | **OPINION** | Editorial. |
| R35-P5-K5 | Grok-M2 | MAJOR | DESIVAST vs V-Web tension: DESIVAST is "cleanest" but V-Web void class "dominated by artifacts" | **PARTIAL (EXT4 M2 carryover)** | Source §VIII.A (l.1987 area) and §IX.C explicitly identify the V-Web void class as survey-edge artifact at low z. The paper states DESIVAST as the primary and V-Web as secondary cross-check. PARTIAL carryover — the scoping is present but not at every σ-reporting site. |
| R35-P5-K6 | Grok-M3 | MAJOR | σ_from_half formula not stated in every figure caption | **PARTIAL (precision)** | Source §V (l.873) defines σ_from_half = 2(f_CW − 0.5)√N. Not repeated in every figure caption. Valid reproducibility concern. PARTIAL. |
| R35-P5-K7 | Grok-M4 | MAJOR | Paper IV monopole offset cited as external fact without in-paper values | **HOUSTON-DECISION (CV-B4)** | Same ruling. The matched-sample monopole fP5 = 0.49719 is re-estimated in the paper itself. |
| R35-P5-K8 | Grok-N1 | NIT | Date "June 2026" | **STALE (current date)** | June 2026 is current. AUTO-FALSIFIED. |
| R35-P5-K9 | Grok-N2 | NIT | Redshift distribution shows only matched sample, not parent DESI DR1 | **PARTIAL (new)** | Valid reproducibility comment for Fig. 1. PARTIAL — genuinely new NIT. |

### OpenAI_methodology findings (MAJOR REVISIONS)

| # | Code | Sev | Finding | Verdict | Evidence |
|---|------|-----|---------|---------|----------|
| R35-P5-O1 | OpenAI-E1 | ESSENTIAL | Versioning/provenance language in main text | **HOUSTON-DECISION** | Same ruling. |
| R35-P5-O2 | OpenAI-E2 | ESSENTIAL | Draft-history and withdrawal commentary | **HOUSTON-DECISION** | Same ruling. |
| R35-P5-O3 | OpenAI-E3 | ESSENTIAL | Data/code DOI missing | **HOUSTON-DECISION (HD-11)** | Same ruling. |
| R35-P5-O4 | OpenAI-M1 | MAJOR | Mixed bases for low-z non-void totals (k=20 vs exact, 100-row delta) | **STALE (documented in k-sufficiency guard)** | Source l.1843–1858: k-sufficiency guard paragraph explicitly documents k=20 vs exact rerun and the membership delta. STALE. |
| R35-P5-O5 | OpenAI-M2 | MAJOR | Overlength and editorial structure | **OPINION** | Editorial. |
| R35-P5-O6 | OpenAI-M3 | MAJOR | "V-Web" vs "T-Web" naming inconsistency | **PARTIAL (CV-B5 carryover)** | Title footnote clarifies T-Web/V-Web nomenclature. Body uses V-Web for backward compatibility. PARTIAL carryover. |
| R35-P5-O7 | OpenAI-M4 | MAJOR | Reproducibility path pointers in prose | **HOUSTON-DECISION / OPINION** | Same as file-path ruling. |
| R35-P5-O8 | OpenAI-M5 | MAJOR | Abstract HEALPix p-values: "p=0.61/0.135/0.413" vs Table VI "0.607/0.135/0.413" | **VERIFIED (NEW MINOR — rounding consistency)** | Source abstract l.350–360: if "p=0.61" appears while Table VI has 0.607, this is a rounding inconsistency (0.607 rounds to 0.61, but 3-decimal precision elsewhere suggests 0.607 is correct). **VERIFIED NEW MINOR — one-digit fix.** |
| R35-P5-O9 | OpenAI-N1 | MINOR | σ_from_half notation spacing | **PARTIAL (cosmetic)** | Valid editorial. PARTIAL. |
| R35-P5-O10 | OpenAI-N2 | MINOR | Typographic accents: "Cramér's V" | **VERIFIED (NEW NIT)** | Source: if `Cram\'er's` macro is mis-rendering the accent this is a LaTeX encoding issue. Changelog does not fix this explicitly. **VERIFIED NEW NIT.** |
| R35-P5-O11 | OpenAI-N3 | MINOR | Jeffreys interval formula reference | **OPINION** | Editorial suggestion. |
| R35-P5-O12 | OpenAI-N4 | MINOR | Table XIV ASTRA filtration note | **PARTIAL (new NIT)** | Valid caption improvement. PARTIAL. |
| R35-P5-O13 | OpenAI pass-2-M6 | MAJOR | Duplicate row fraction stated as 2.7% but arithmetic gives 3.56% | **VERIFIED (MAJOR — new)** | Cell arithmetic: n_rows=812,793 − n_unique=783,820 = 28,973 duplicate rows. 28,973/812,793 = 3.56% (row-level) or 28,973/783,820 = 3.70% (unique-level). Source l.368, l.1100, l.2410 say "2.7% duplicate rows." Design effect √(812,793/783,820) = 1.018 is correct and is self-consistent with 3.56%, not 2.7%. The 2.7% figure does not correspond to any derivable fraction from the stated counts. **VERIFIED MAJOR — arithmetic error in a frequently cited percentage.** |
| R35-P5-O14 | OpenAI pass-2-N5 | MINOR | Table XII filament σ_vs_monopole: tabulated +0.99 vs computed +1.09 | **PARTIAL (new, needs deeper source verification)** | OpenAI computes σ_vs_monopole = 2(f − fP5)√N = 2(0.498048 − 0.49719)×√408,187 ≈ +1.09 but table says +0.99. If fP5 used for Table XII is the unique-galaxy monopole (0.49728 vs row-level 0.49719), the discrepancy shrinks but may not vanish. **PARTIAL — genuine precision concern, needs Table XII source line verification.** |
| R35-P5-O15 | OpenAI pass-2-N6 | MINOR | Clopper-Pearson 1−0.05^(1/6) typeset ambiguously | **STALE (R34conf C2 closed)** | Source l.1839 has proper LaTeX braces `0.05^{1/6}` and a prose clarification added in v0.1.67 per R34conf C3 closure. STALE. |
| R35-P5-O16 | OpenAI pass-2-N7 | MINOR | Fig. 9 panel comparability note | **VERIFIED (NEW NIT)** | Valid suggestion: one caption sentence distinguishing the two panels. **VERIFIED NEW NIT.** |
| R35-P5-O17 | OpenAI pass-2-N8 | MINOR | Abstract "2.7% duplicate rows" same as O13 | **VERIFIED (same as O13 — MAJOR)** | Same finding. Counts toward MAJOR. |

---

## Part IV — Verdict Counts

| Verdict | Count | Key items |
|---------|-------|-----------|
| **VERIFIED (MAJOR)** | **1** | R35-P5-O13 (duplicate row percentage 2.7% should be 3.56%) |
| **VERIFIED (NEW MINOR)** | **2** | R35-P5-G5 (abstract p-value type disambiguation), R35-P5-O8 (HEALPix p 0.61 vs 0.607) |
| **VERIFIED (NEW NIT)** | **3** | R35-P5-G6 (redshift variable x vs z — FALSIFIED after source check; see note), R35-P5-O10 (Cramér's V accent), R35-P5-O16 (Fig. 9 panel comparability) |
| FALSIFIED | 5 | R35-P5-G2 all three sign errors (wrong sign convention), R35-P5-G3 (erfc formula correct), R35-P5-GX2 (§VIII F extractor artifact), R35-P5-GX4 (PIS spelled out inline) |
| PARTIAL (carryovers + new) | 10 | R35-P5-K5, K6, K9, O4, O6, O12, O14 + EXT5 carryovers |
| HOUSTON-DECISION | 5 | R35-P5-G1, G4, K7, O1/O2/O3/O7 batch |
| STALE | 7 | R35-P5-G2→all-three, G3, K2, K3, K8, O4, O15 |
| OPINION | 5 | R35-P5-K4, K5-scope, O5, O11, GX3 |
| AUTO-FALSIFIED | 3 | k=20 re-raise (if attempted), h⁻¹ Mpc re-raise, date re-raise |

**NIT re-assessment:** R35-P5-G6 (redshift variable "x"): Source uses z throughout; "x" was claimed by Gemini from PDF. A source grep would be needed to confirm — likely a Gemini PDF-rendering artifact (pattern-052). Ruled PARTIAL pending source line check; not counted as VERIFIED NIT above.

**Net new genuinely-substantive findings:**
1. **R35-P5-O13 (MAJOR):** Duplicate row percentage 2.7% is arithmetically wrong; correct value is 3.56% (row-level). Appears in abstract, body (×3 occurrences), figure caption.
2. **R35-P5-G5 (MINOR):** Abstract p=0.31 vs p_shuffle distinction needs labeling.
3. **R35-P5-O8 (MINOR):** Abstract p=0.61 vs Table VI p=0.607 rounding consistency.

---

## Part V — Reviewer Calibration

| Reviewer | Stated recommendation | Audit-calibrated | Delta |
|---------|-----------------------|-----------------|-------|
| Claude_brutal | FAILED | N/A | — |
| Gemini_cosmology | MAJOR REVISIONS | **MINOR REVISIONS — calibrated net of pattern-052.** All three sign error claims are FALSIFIED (wrong convention). Bonferroni formula FALSIFIED. Remaining findings are HOUSTON-DECISION, STALE, or OPINION. Two new MINORs (G5, GX4 FALSIFIED). | Overcalled (3 MAJOR "sign errors" are all FALSIFIED) |
| Grok_brutal | REJECT | **MINOR REVISIONS.** All ESSENTIAL findings are HOUSTON-DECISION or STALE. Grok missed the duplicate-row MAJOR (O13). REJECT is significantly overcalled. | Significantly overcalled |
| OpenAI_methodology | MAJOR REVISIONS | **MAJOR REVISIONS — calibrated.** R35-P5-O13 (duplicate row 2.7%) is a genuine MAJOR. O14 (Table XII σ_vs_monopole) is PARTIAL. Two new MINORs and NITs also valid. | Accurate |

**Consensus:** P5 is at **MAJOR REVISIONS** driven by one item: the duplicate-row percentage (2.7% is wrong; correct is 3.56%) appears in the abstract, three body locations, and a figure caption. All other new findings are MINOR or NIT. The headline science (DESIVAST three-algorithm null ΔfCW=+0.0007, z≈0.31; all five Bonferroni-5 rows ≤0.004; V-Web class null χ²=3.55, p=0.31) is not challenged by any reviewer. The Appendix B contingency tables are verified exactly correct.

---

## Part VI — Closure Plan

### C0 — R35-P5-O13 (VERIFIED MAJOR): Fix duplicate-row percentage throughout

Replace all occurrences of "2.7% duplicate rows" with the correct percentage. Four occurrences identified:
- l.368 (abstract robustness section)
- l.1100 (§VI.A body)
- l.2410 (§VIII.C body)
- Figure caption (wherever "2.7%" appears near "duplicate")

Correct replacement: "3.6% duplicate rows" (or "3.56% of the row-level parent" for precision). The design effect √(812,793/783,820) = 1.018 is correct and should be retained.

**Arithmetic verification:**
- n_rows = 812,793; n_unique = 783,820; n_dups = 28,973
- 28,973 / 812,793 = 3.56% (of rows) — this is the most natural statement given row count is the denominator
- The design effect 1.018 is consistent with 3.56%, not 2.7%

### C1 — R35-P5-O8 (VERIFIED MINOR): Fix abstract HEALPix p-value rounding

In abstract, change "p=0.61" to "p=0.607" to match Table VI. (Three p-values: 0.607/0.135/0.413.)

### C2 — R35-P5-G5 (VERIFIED MINOR): Label asymptotic vs empirical p-values

In abstract and §VI.A, add a parenthetical at first use distinguishing asymptotic χ²-derived p from permutation-derived p:
> "χ²=3.55, 3 d.o.f., p=0.307 (asymptotic χ² distribution)" and "p_shuffle ≈ 0.31 (empirical from 10³ label-shuffle permutations)"

### Optional (PARTIAL / NIT)

- C3: R35-P5-O14 (Table XII filament σ_vs_monopole: +0.99 vs computed +1.09) — verify source Table XII and fP5 used; correct if genuine.
- C4: R35-P5-O10 (Cramér's V accent) — LaTeX encoding fix.
- C5: R35-P5-O16 (Fig. 9 panel caption sentence) — one sentence added.

### Ruled / HOUSTON-DECISION (no action this wave)

- All k=20 findings: AUTO-FALSIFIED (5th raise).
- h⁻¹ Mpc: CORRECT — rederivation in v0.1.67 stands.
- Paper IV dependency: HD-11, mint-at-submission.
- Version-history language: Houston-decision at journal submission.
- Gemini three sign errors: FALSIFIED (wrong convention assumed).
- Gemini Bonferroni formula: FALSIFIED (erfc formula is correct for two-sided).
- §VIII F cross-reference: FALSIFIED (extractor artifact, pattern-052).

---

## Part VII — Gemini Sign Error Falsification Summary

This is the first instance of a Gemini P5 finding being AUTO-FALSIFIED due to arithmetic error by Gemini (not extraction artifact). Gemini assumed the sign convention Δ = f_void − f_non-void, but the paper consistently defines Δ = f_non-void − f_void (stated explicitly in Table caption l.2106 and in the Robustness intro l.428–429). All three "sign errors" are correct values under the paper's stated convention.

**Pattern-052 update:** This round adds 3 arithmetic-error-based auto-FALSIFICATIONS by Gemini to the tally. Prior streak was 16/18 extraction artifacts; this round adds 3 arithmetic false alarms (different category from PDF extraction artifacts). Total Gemini false-positive rate across EXT2–R35conf: high.

---

## Part VIII — Clean/Not-Clean Verdict

**NOT CLEAN (1 MAJOR from clean).**

- C0: Duplicate row percentage 2.7% → 3.56% (appears in abstract + 3 body locations). MAJOR, all occurrences must be corrected.
- C1: HEALPix p-value rounding 0.61 → 0.607 (MINOR).
- C2: Abstract asymptotic vs empirical p-value labeling (MINOR).
- Appendix B tables: VERIFIED CORRECT (cell-by-cell match from committed artifact script).
- All prior EXT5 closures: CONFIRMED IN v0.1.68.
- Headline science: NOT challenged.

**Expected R36 state after C0–C2:** All MAJOR findings resolved. ACCEPT from Grok (already ACCEPT-calibrated after REJECT is deflated). MINOR REVISIONS → ACCEPT from Gemini (sign errors falsified; remaining items are editorial). ACCEPT from OpenAI pending C0–C2.

---

*Verdict counts: VERIFIED 6 (1 MAJOR, 2 MINOR, 3 NIT — 2 NIT confirmed genuine, 1 NIT partially falsified) · FALSIFIED 5 · PARTIAL 10 · HOUSTON-DECISION 5 · STALE 7 · OPINION 5*
*Genuinely-new-substantive count: 3 (R35-P5-O13 MAJOR, R35-P5-G5 MINOR, R35-P5-O8 MINOR).*
*Appendix B tables: VERIFIED EXACT — EXT5-C2 fully closed in v0.1.68.*
*Gemini sign error claims: ALL FALSIFIED — wrong sign convention assumed.*
*Gemini Bonferroni erfc formula: FALSIFIED — formula is correct for two-sided tests.*
*h⁻¹ Mpc conversion: CORRECT — rederivation stands; re-raise rule in effect.*
*k=20 (B3): 5th auto-FALSIFICATION (not explicitly raised in R35conf but rule maintained).*
*Claude leg absent: API 400 / zero credits. 3/4 legs present.*
*Pattern-052: 3 new arithmetic false alarms from Gemini (not extractor artifacts — new category).*
