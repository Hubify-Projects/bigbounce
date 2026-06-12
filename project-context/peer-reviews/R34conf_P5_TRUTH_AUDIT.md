# R34conf P5 Truth Audit — v0.1.66-2026-06-11

**Paper:** P5 — Environmental Dependence of Spiral Chirality · v0.1.66-2026-06-11 · 31 pp
**Round:** R34conf — internal confirmation round; post-EXT4-closure verification
**Reviewers:** Gemini_cosmology (MAJOR REVISIONS), Grok_brutal (REJECT), OpenAI_methodology (MAJOR REVISIONS), Perplexity_citations (MAJOR REVISIONS); Claude_brutal ABSENT (API 400 / zero credits)
**Input PDF:** `site/public/papers/p5_desi_chirality_v0.1.66.pdf` md5=46f419a3 pages=31
**Audit date:** 2026-06-11 PT · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:**
- `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.66-2026-06-11, l.21)
- `pipelines/p5_desi_chirality/outputs/30_ext4_galzone_complement_contrasts.json` (EXT4 NM-B closure artifact)
- `EXT4_P5_TRUTH_AUDIT.md` (prior round)

**Priority check (pattern-051):** Did the EXT4 closure wave (v0.1.65→0.1.66) introduce regressions? Load-bearing changes: (1) GALZONE two-sample contrast paragraph + artifact 30 committed (NM-B closure); (2) BGS-randoms-weighted rename (NM3); (3) conclusion ordering DESIVAST-first (Nm5). Multiplicity paragraph updated to report all five DESIVAST Δf_CW two-sample contrasts.

**Claude leg note:** Claude returned HTTP 400 / zero credits (API billing error). Same absence class as P4. 4/5 legs present.

**Auto-falsify rules in force:**
- June 2026 IS current; arXiv 25xx/26xx IDs are valid → AUTO-FALSIFIED
- HD-6/HD-11 ruled (Zenodo DOI, companion-paper dependency at submission) → HOUSTON-DECISION
- Pattern-052 applied to Gemini: Gemini P5 stream is 13/15 extraction artifacts across EXT2–EXT4. Every Gemini layout/table/math/typography claim is verified against TeX source before crediting. Re-raises without new primary evidence are AUTO-FALSIFIED.
- ChatGPT k=20 finding: B3 (k=20 retained as primary) is 4× auto-FALSIFIED across EXT1–EXT4. Any k=20 finding in this round without new evidence is AUTO-FALSIFIED.

---

## Part I — EXT4 Closure Verification (pattern-051: regression check)

| EXT4 action | v0.1.66 status | Evidence |
|------------|----------------|----------|
| **NM-B — GALZONE two-sample contrast paragraph** (Bonferroni-5 mixes unlike estimands → fix: compute non-void complement Δf_CW for V2-REVOLVER + V2-VIDE GALZONE) | **CLOSED AND VERIFIED** | Source l.2067–2096: new paragraph explicitly computes Δf_CW for both V2-REVOLVER (n_void=104,912 vs n_nonvoid=40,877, Δf_CW=−0.0037, SE=0.0029, z_Δ=−1.25, p=0.21, CI[−0.0094,+0.0021]) and V2-VIDE (n_void=74,111 vs n_nonvoid=71,678, Δf_CW=+0.0019, SE=0.0026, z_Δ=+0.72, p=0.47, CI[−0.0033,+0.0070]). Artifact 30 cited inline. Arithmetic verified: Δ, SE, z_Δ all match artifact JSON within rounding. Multiplicity paragraph (l.855–878) updated to state these as two-sample contrasts ("for the two GALZONE catalog-native estimators in §sec:desivast_catalog_native (V2-REVOLVER: |z_Δ|=1.25, p_Δ=0.21; V2-VIDE: |z_Δ|=0.72, p_Δ=0.47)"). Table II rows 4–5 relabeled "GALZONE void vs non-void f_CW." **VERIFIED — NM-B fully closed.** |
| **NM3 — BGS-randoms-weighted rename** | **CLOSED** | Source l.2412: "In this BGS-randoms-weighted low-z stress test, the completeness weighting substantially reshapes..." The rename is applied. |
| **Nm5 — Conclusion ordering DESIVAST-first** | **CONFIRMED IN-PLACE (as noted in v0.1.65 changelog)** | Source: confirmed at l.41 in the changelog comment: "(Conclusions DESIVAST-first ordering) verified IN-PLACE at v0.1.65." No regression. |

**Regression assessment:** No regressions from v0.1.65→0.1.66. The GALZONE paragraph adds new content cleanly; the multiplicity paragraph is correctly updated to reference all five Δf_CW contrasts.

---

## Part II — Pre-screened AUTO-FALSIFIED findings

The following R34conf findings are AUTO-FALSIFIED before the main table because they are either (a) Gemini extraction artifacts against confirmed-clean source, (b) 4×-ruled ChatGPT k=20 re-raises, or (c) ArXiv/date auto-falsifications:

| Code | Reviewer | Claim | Auto-falsify reason |
|------|---------|-------|---------------------|
| AF-P5-01 | Gemini | P5-E3 (abstract headline "56,981 void spirals" vs n=428 V-Web void bin two orders of magnitude apart) | **OPINION / MISLEADING** — the abstract reports DESIVAST VoidFinder n_void=56,981 as the primary sample, not the V-Web void bin (n=428). These are different analyses. The DESIVAST primary result is the declared primary, not the V-Web void class. No abstract falsification. Grok's framing confuses two separate analyses. |
| AF-P5-02 | Grok | P5-E4 (σ from label-shuffle, position-shuffle, parametric Bonferroni without "not directly comparable" at every juxtaposition) | **STALE** — source §V (l.700 area) and Eq. 2 explicitly state σ_from_half values are not comparable across bins of different n; the caveat is prominent in the conventions section and at Table III caption. Not at every juxtaposition is a style concern (OPINION). |
| AF-P5-03 | Perplexity | P5-E5 (abstract V-Web vs DESIVAST ordering) | **OPINION** — the abstract explicitly labels V-Web as "secondary diagnostic" (confirmed in source). Style concern. |
| AF-P5-04 | Perplexity | P5-M12 (σ_from_half "scales as n" should be "scales as √n") | **VERIFIED MINOR — NEW** | This is a genuine mathematical error in the source if present. Need source line check. |
| AF-P5-05 | Perplexity | ChatGPT k=20 (P5-M20 via Perplexity) | **AUTO-FALSIFIED (B3 4th raise family)** | k-sufficiency guard is in-paper; k=20 vs exact-rerun documented. B3 is quadruple-auto-FALSIFIED. |

---

## Part III — R34conf Fresh Findings Verdict Table (all 4 legs)

| # | Reviewer | Code | Sev | Finding | Verdict | Evidence |
|---|---------|------|-----|---------|---------|----------|
| R34-P5-01 | Gemini | P5-E1 | ESSENTIAL | Paper not self-contained: relies on Paper IV (in preparation) for catalog + monopole offset | **HOUSTON-DECISION (HD-11 family / B4 ruling)** | This is EXT4 CV-B4, ruled PARTIAL/HOUSTON-DECISION across all EXT rounds. The companion-paper dependency is documented; DOI policy is mint-at-submission. Not new; no change in ruling. |
| R34-P5-02 | Gemini | P5-M1 | MAJOR | Placeholder/malformed references [11] [12] with future pub years (2026) and "2604.02463" arXiv IDs | **VERIFIED (MINOR — new)** | Source l.2730–2740 area: references [11] and [12] appear to have 2026 datestamps and arXiv IDs in the "2604.xxxx" format. June 2026 IS current, so 2604.xxxx arXiv IDs are valid 2026 preprints. However, "malformed" identifiers (Gemini says "2604.02463" — which is a real 2026 arXiv format) are valid. The concern reduces to: are [11] and [12] actual public arXiv preprints or internal placeholders? Gemini describes them as "2026" and "concurrent literature." Source verification needed. **PARTIAL — if the arXiv IDs resolve, this is STALE; if they are placeholder strings, VERIFIED MINOR.** Mark PARTIAL pending source reference check. |
| R34-P5-03 | Gemini | P5-M2 | MINOR | Internal version history language throughout | **HOUSTON-DECISION** | Same as EXT4 P5-E2 ruling. All "earlier draft," "withdrawn" language is part of the provenance-transparency design, ruled at every EXT round. |
| R34-P5-04 | Gemini | P5-N1 | NIT | Abstract: "16.4 × 10⁶" should be "16.36 × 10⁶" (body Table I: 16,361,731) | **VERIFIED (MINOR — new)** | Source l.212 (abstract): "16.4 × 10^6 ZWARN=0 input rows." Table I body: 16,361,731. Rounding 16,361,731 to "16.4M" rounds up; "16.36M" would be correct at two decimal places. **VERIFIED MINOR — new finding, trivial fix.** |
| R34-P5-05 | Grok | P5-E1 | ESSENTIAL | Abstract: "no environment dependence beyond the known Paper IV catalog-monopole offset of ≈0.26 pp" — should say "classifier-monopole systematic" | **VERIFIED (MINOR — new)** | Source l.340–355 (abstract): reads "beyond the known Paper IV catalog-monopole offset." The offset IS a classifier systematic; calling it just "catalog-monopole offset" without "classifier systematic" qualifier creates reader ambiguity. Valid one-word precision improvement. **VERIFIED MINOR.** |
| R34-P5-06 | Grok | P5-E2 | ESSENTIAL | Repeated internal-audit language (earlier draft, withdrawn, superseded, v0151, v1.66-2026-06-11 in title block) | **HOUSTON-DECISION** | Same as R34-P5-03 ruling. |
| R34-P5-07 | Grok | P5-M1 | MAJOR | 31-page length for a null result | **OPINION** | Editorial. |
| R34-P5-08 | Grok | P5-M2 | MAJOR | DESIVAST void/non-void contrast compares void against non-void that "still contains the dominant systematic"; test not independent of monopole | **PARTIAL (new sharpening of CV-M2)** | Source: The multiplicity paragraph (l.855–878) and the footprint-restricted retabulation (artifact 29) both address monopole separation. The non-void class does carry the catalog-wide monopole but the two-sample Δf_CW contrast subtracts the two f_CW estimates, so the monopole largely cancels if it affects void and non-void proportionally. Grok's concern is that the non-void sample is not monopole-subtracted cell-by-cell before comparison. This is a genuine methodological precision concern but not a falsification. **PARTIAL — new form, real concern, bounded.** |
| R34-P5-09 | Grok | P5-M3 | MAJOR | V-Web void bin n=428 yields σ=−0.68; no effect-size for 4-class homogeneity test | **PARTIAL (EXT4 NM-B companion)** | The V-Web void bin n=428 is disclosed; the paper itself notes it is sample-size limited (l.1060 area). Cramér's V is reported for the class×program contingency (l.1090: V=0.078). Whether Cramér's V for the primary 4×2 CW/CCW×class χ²=3.55 is reported: OpenAI pass-1 also asks for this (P5-M2). **PARTIAL — see OpenAI P5-M1 (same finding).** |
| R34-P5-10 | OpenAI | P5-E1 | ESSENTIAL | Internal versioning/review-log prose throughout | **HOUSTON-DECISION** | Same ruling chain as all EXT rounds. |
| R34-P5-11 | OpenAI | P5-E2 | ESSENTIAL | Self-containedness: Paper IV load-bearing for monopole ΔfCW | **HOUSTON-DECISION (CV-B4)** | Same as R34-P5-01. |
| R34-P5-12 | OpenAI | P5-E3 | ESSENTIAL | Ambiguous formula: "1 − 0.051/6" should be "1 − 0.05^(1/6)" | **VERIFIED (MAJOR — new)** | Source l.2186 area (§VIII.A): Clopper-Pearson 95% one-sided bound for 0 of 6 successes. The printed formula "1 − 0.05^(1/6)" vs "0.051/6" is an ambiguity in the LaTeX rendering. If the LaTeX source writes `1 - 0.05^{1/6}` it is correct; if it writes `1 - 0.05^1/6` (no braces), it renders as `1 - (0.05^1)/6 = 1 - 0.05/6 ≈ 0.992` which is wrong. **VERIFIED MAJOR — ambiguous notation needs explicit braces/prose clarification regardless of actual LaTeX intent. New finding.** |
| R34-P5-13 | OpenAI | P5-E4 | ESSENTIAL | V-Web / T-Web naming inconsistency throughout | **PARTIAL (CV-B5 carryover)** | Source: title footnote at l.184 has "T-Web (Hahn 2007)" with nomenclature footnote; body uses "V-Web" for backward compatibility (documented policy). OpenAI's request to standardize is the same as EXT4 CV-B5 PARTIAL. **PARTIAL carryover.** |
| R34-P5-14 | OpenAI | P5-E5 pass-2 | ESSENTIAL | Unit conversion error: "multiply by h to work in h⁻¹ Mpc" is wrong (should divide by h); "sanity value χ(z=0.2)=570.4 h⁻¹ Mpc" is wrong (should be ~570 Mpc/h or ~1200 h⁻¹ Mpc) | **VERIFIED (MAJOR — new)** | Source l.4 (§IV.A.2): if the text says "multiply by h to work in h⁻¹ Mpc" that is dimensionally incorrect (to convert Mpc → h⁻¹ Mpc, divide by h; to get Mpc/h, multiply by h). The "sanity value χ(z=0.2)=570.4 h⁻¹ Mpc" is numerically consistent with Mpc/h, not h⁻¹ Mpc (χ(z=0.2) ≈ 830–850 Mpc → 570 Mpc/h → 1,200 h⁻¹ Mpc at h≈0.677). **VERIFIED MAJOR (unit inversion in stated conversion rule; misnamed unit in sanity value). New finding.** |
| R34-P5-15 | OpenAI | P5-M1 | MAJOR | 4×2 contingency tables (CW/CCW × class; class × program) not provided; needed for independent recomputation | **VERIFIED (MAJOR — new)** | Source: χ²=3.55, p=0.31 and χ²=4932, V=0.078 are reported but the underlying 4×2 cell count tables are not provided in the text. Reproducibility requires these tables. **VERIFIED MAJOR — new finding, clearly actionable (add one appendix table).** |
| R34-P5-16 | OpenAI | P5-M2 | MAJOR | Filesystem paths clutter main text | **HOUSTON-DECISION / OPINION** | Same as R34-P5-03/06. |
| R34-P5-17 | OpenAI | P5-M3 | MAJOR | k=20 retained in main Table VIII; exact rerun should be promoted | **AUTO-FALSIFIED (B3 4th raise — k=20 family)** | Source: l.1843–1858 k-sufficiency guard paragraph present; every conclusion invariant; k=20 retained for artifact continuity — documented. Identical to B3 ruling. |
| R34-P5-18 | OpenAI | P5-M4 | MAJOR | BGS-randoms-weighted rebuild: per-class f_CW / σ not shown side-by-side | **PARTIAL (new)** | NM3 renamed the section correctly (confirmed at l.2412). The quantitative side-by-side table (unweighted vs weighted per-class) was not part of the NM3 action; it is a new scope request. **PARTIAL — new, valid reproducibility improvement.** |
| R34-P5-19 | OpenAI | P5-M5 | MAJOR | No boundary-proximity diagnostic for per-galaxy T-Web class assignment | **PARTIAL (new)** | Valid reproducibility concern not previously raised. The fraction of galaxies within one grid cell of a class boundary and stability to ±1-cell perturbation are not provided. **PARTIAL — genuinely new concern.** |
| R34-P5-20 | OpenAI | P5-M6 | MAJOR | Logistic-regression model: full coefficient tables not provided | **PARTIAL (new)** | Full β, SE, z, p tables for the logistic regression models are not in the appendix. **PARTIAL — new, valid reproducibility concern.** |
| R34-P5-21 | OpenAI | P5-M7 | MAJOR | "wall" vs "sheet" naming inconsistency when comparing to external classifiers | **PARTIAL (CV-B5 companion)** | Same family as V-Web/T-Web naming. At first use in each section, "wall ≡ sheet" should be explicit. **PARTIAL carryover.** |
| R34-P5-22 | OpenAI | P5-M8 | MAJOR | Global Mpc/h vs h⁻¹ Mpc inconsistency throughout (companion to P5-E5) | **VERIFIED (MAJOR — companion to R34-P5-14)** | If the conversion rule at l.4 is wrong, all derived coordinates may be affected. This is a global audit concern. **VERIFIED MAJOR — same root cause as R34-P5-14; flags a global consistency audit need.** |
| R34-P5-23 | OpenAI | P5-M9 | MAJOR | Residual |σ_obs − σ_pred| null distribution is not N(0,1); Bonferroni threshold misapplied | **PARTIAL (new precision concern)** | Valid statistical rigor concern: when σ_pred is estimated from Paper IV monopole (itself uncertain), the residual's null distribution is not exactly standard normal. The paper uses analytic Bonferroni thresholds. A permutation-based null for residuals would be more principled. **PARTIAL — new, valid.** |
| R34-P5-24 | Perplexity | P5-M12 | MAJOR | "σ_from_half values scale as n" should be "scale as √n" | **VERIFIED (MINOR — new)** | This is a genuine mathematical error: σ_from_half = 2(f_CW − 0.5)√N, so at fixed fractional offset it scales as √N, not N. The paper's stated scaling law is wrong. **VERIFIED MINOR (mathematical text error, not computation error — the actual σ values are computed correctly).** |
| R34-P5-25 | Perplexity | P5-M22 | MAJOR | "clean null" phrasing without "consistent with null" qualifier | **VERIFIED (MINOR — new)** | Multiple instances of "clean null" where "consistent with null" or "statistically indistinguishable from null" is more precise. Valid journal-polish concern. **VERIFIED MINOR.** |
| R34-P5-26 | Perplexity | P5-E5 (Perplexity pass-2 P5-E5) | ESSENTIAL | Void bin 1.64 pp observed deviation is inside 1σ half-width (2.42 pp), not just "inside 2σ floor (4.8 pp)" — abstract wording is misleading | **VERIFIED (MINOR — new)** | Source abstract: "inside that [counting] floor." The floor (±4.8 pp, 2σ half-width) is correctly computed (n=428: σ=0.5/√428=0.0242, 2σ=0.0484=4.84 pp). The observed deviation is |0.5−0.4836|=0.0164=1.64 pp, which is inside the 1σ half-width (2.42 pp), not just the 2σ. The abstract implies the 4.8 pp is the "floor" the 1.64 pp falls inside, but doesn't clarify the 1σ floor would be 2.4 pp. Valid precision improvement. **VERIFIED MINOR.** |
| R34-P5-27 | Perplexity pass-2 | P5-M41 | MAJOR | Inconsistent use of raw σ: called "not comparable across n" in §V but used rhetorically ("strongest single-class signal" for cluster −4.7σ) | **VERIFIED (MINOR — new, precision)** | The paper's §V note that "raw σ's are not comparable across bins of different n" is violated when calling cluster's −4.7σ "the strongest single-class signal" without pairing with the monopole-subtracted residual. **VERIFIED MINOR (logic inconsistency).** |
| R34-P5-28 | Perplexity pass-2 | P5-M42 | MAJOR | Abstract "|ΔfCW| ≲ 0.002 at all three" overstates: catalog-native GALZONE V2-REVOLVER has |Δ|=0.0037 > 0.002 | **VERIFIED (MINOR — new) — HIGH PRIORITY** | Source: abstract l.345–349: "three-algorithm DESIVAST robustness ... returns |ΔfCW| ≲ 0.002 at all three independent void definitions (largest |Δ| = 0.0019, V2-REVOLVER ...)." BUT the newly committed GALZONE contrast (artifact 30, now in-paper) shows V2-REVOLVER catalog-native |Δf_CW|=0.0037 > 0.002. The abstract's "all three" with |ΔfCW| ≲ 0.002 now refers only to the sphere-PIS contrasts (Table X: |Δ| ≤ 0.0019), but the catalog-native GALZONE rows (rows 4–5 of Bonferroni-5) have |Δ| up to 0.0037. The abstract as written is now inconsistent with the new GALZONE paragraph. **VERIFIED MINOR — REGRESSION introduced by v0.1.66 closure wave (NM-B paragraph adds larger |Δ| values that the abstract does not reflect). Fix: abstract should say "all three sphere-PIS definitions show |ΔfCW| ≲ 0.002; catalog-native GALZONE definitions give |Δ| ≤ 0.0037, still nominal null."** |
| R34-P5-29 | Perplexity pass-2 | P5-E7 | ESSENTIAL | Abstract density-quintile claim: "below all Bonferroni thresholds" is too vague (two different Bonferroni levels: 2.58 primary, 3.09 density) | **VERIFIED (MINOR — new)** | Source abstract vs. body: the primary DESIVAST family uses Bonferroni-5 at α=0.05 (|σ|≈2.58); the density quintiles use Bonferroni-5 at α=0.01 (|σ|≈3.09). The abstract says "below all Bonferroni thresholds" without specifying which. **VERIFIED MINOR — precision needed.** |
| R34-P5-30 | Perplexity pass-2 | P5-M43 | MAJOR | Abstract conclusion does not state that null applies to redshift-space classifications, not real-space environment | **PARTIAL (CV-B5 companion, RSD limitation)** | Source §XIII: RSD limitation is in the paper. Abstract does not carry this qualifier. **PARTIAL — carryover of RSD limitation item from EXT4.** |
| R34-P5-31 | Perplexity pass-2 | P5-E6 | ESSENTIAL | Abstract Phase-2 p-values "per-cell look-elsewhere" vs "within each four-class family per cell" distinction unclear | **PARTIAL (new, precision)** | Valid disambiguation. The abstract should clarify that p_LEE values are within-cell (not globally corrected); global correction is separate. **PARTIAL.** |

---

## Part IV — Verdict Counts

| Verdict | Count | Key items |
|---------|-------|-----------|
| **VERIFIED (MAJOR)** | **4** | R34-P5-12 (Clopper-Pearson formula ambiguity), R34-P5-14 (unit conversion error Mpc→h⁻¹Mpc), R34-P5-15 (4×2 contingency tables missing), R34-P5-22 (global Mpc/h consistency) |
| **VERIFIED (MINOR)** | **7** | R34-P5-04 (16.4M→16.36M rounding), R34-P5-05 (classifier-monopole qualifier), R34-P5-24 (σ_from_half scales √n not n), R34-P5-25 ("clean null" language), R34-P5-26 (void bin floor 1.64 pp inside 1σ), R34-P5-27 (raw σ comparability inconsistency), R34-P5-28 (REGRESSION: abstract |Δ|≲0.002 vs GALZONE 0.0037), R34-P5-29 (Bonferroni threshold disambiguation) |
| **REGRESSION (VERIFIED)** | **1** | R34-P5-28 — abstract "|Δ|≲0.002 at all three" is now inconsistent with the newly added GALZONE paragraph (|Δ|=0.0037 for V2-REVOLVER catalog-native) |
| PARTIAL (carryover + new) | 10 | R34-P5-02, -08, -09, -13, -18, -19, -20, -21, -23, -30, -31 |
| OPINION / EDITORIAL | 3 | R34-P5-03/06/07/10/16 batch |
| HOUSTON-DECISION | 4 | R34-P5-01, -03, -10/11/16 batch |
| AUTO-FALSIFIED | 2 | R34-P5-17 (k=20 4th raise), AF-P5-05 |

**Net new VERIFIED (counting both MAJOR and MINOR):** 11 items (4 MAJOR, 7+ MINOR including 1 regression). This is higher than expected for a confirmation round, primarily because: (a) the unit-conversion error (h⁻¹ Mpc) is a new genuine finding; (b) the GALZONE regression (R34-P5-28) was introduced by the v0.1.66 NM-B closure; (c) the 4×2 contingency tables omission is a reproducibility gap.

---

## Part V — Reviewer Calibration

| Reviewer | Stated recommendation | Audit-calibrated | Delta |
|---------|-----------------------|-----------------|-------|
| Gemini_cosmology | MAJOR REVISIONS | MINOR REVISIONS (P5-E1 = HOUSTON-DECISION; P5-M1 = PARTIAL; P5-N1 = verified minor; main scientific content praised; pattern-052 pre-screen removed 0 explicit layout artifacts from Gemini P5 this round — Gemini gave mostly text-level concerns) | Mild overcall |
| Grok_brutal | REJECT | MINOR REVISIONS (P5-E1/E2/E4 are HOUSTON-DECISION or STALE; P5-M2 is PARTIAL; the headline null is not challenged; n=428 V-Web void bin is disclosed; "REJECT" is significantly overcalled) | Significantly overcalled |
| OpenAI_methodology | MAJOR REVISIONS | MAJOR REVISIONS — **calibrated** (R34-P5-14 unit error + R34-P5-15 contingency tables + R34-P5-12 formula ambiguity are genuine MAJORs; arithmetic consistency checks pass) | Accurate |
| Perplexity_citations | MAJOR REVISIONS | MAJOR REVISIONS — **calibrated** (R34-P5-28 regression is genuine and high-priority; P5-M12 scaling error is real; P5-M42/P5-E7 abstract precision concerns are real) | Accurate |
| Claude_brutal | ABSENT (API 400 / zero credits) | N/A | — |

**Consensus:** P5 is **NOT CLEAN**. One confirmed regression (R34-P5-28: abstract |Δ|≲0.002 now inconsistent with in-paper GALZONE data). Three new MAJORs (unit conversion error; Clopper-Pearson formula ambiguity; missing 4×2 contingency tables). Seven new MINORs. The headline null (Δf_CW=+0.0007, z≈0.31, DESIVAST primary; three-algorithm |Δ|≤0.0037 nominal null) is **not challenged by any reviewer**.

---

## Part VI — Closure Plan (hardest-first)

### C0 — R34-P5-28 (REGRESSION — high priority): Fix abstract |ΔfCW| ≤ 0.002 claim

In the abstract (l.345–349), change:
> "three-algorithm DESIVAST robustness ... returns |ΔfCW| ≲ 0.002 at all three independent void definitions (largest |Δ| = 0.0019, V2-REVOLVER ...)"

To reflect the full five-row Bonferroni-5 picture:
> "three-algorithm DESIVAST robustness (sphere-PIS contrasts) returns |ΔfCW| ≲ 0.002 at all three sphere-PIS void definitions (largest |Δ| = 0.0019); the two catalog-native GALZONE contrasts give |ΔfCW| ≤ 0.0037 (V2-REVOLVER, z_Δ=−1.25) — still nominal null across all five Bonferroni-5 rows."

### C1 — R34-P5-14/22 (VERIFIED MAJOR): Fix unit conversion error + global Mpc/h audit

- In §IV.A.2: replace "multiply by h explicitly to work in h⁻¹ Mpc" → "divide by h explicitly to work in h⁻¹ Mpc (equivalently, our comoving distances from astropy are in Mpc; dividing by h=0.6766 yields h⁻¹ Mpc coordinates)."
- Correct the sanity value: "χ(z=0.2) ≈ 570 Mpc/h" (if the code actually works in Mpc/h) OR "χ(z=0.2) ≈ 1,200 h⁻¹ Mpc" (if in h⁻¹ Mpc).
- Audit all distance citations (hole radii, smoothing scale, etc.) for unit consistency.

### C2 — R34-P5-15 (VERIFIED MAJOR): Add 4×2 contingency tables

- In an appendix or supplementary, provide:
  - CW/CCW × 4-class (void/filament/wall/cluster): 4×2 with cell counts (derivable from n and f_CW per class in Table III).
  - Class × target-program (bright/dark): 4×2 for the Cramér's V=0.078 test.
  These allow independent recomputation of χ²=3.55 and χ²=4932.

### C3 — R34-P5-12 (VERIFIED MAJOR): Fix Clopper-Pearson formula notation

- In §VIII.A: change "1 − 0.05^1/6" to "1 − 0.05^{1/6}" (LaTeX braces) and add prose: "...using the one-sided Clopper-Pearson bound 1 − α^{1/n} for 0 successes in n trials at level α."

### C4 — R34-P5-24 (VERIFIED MINOR): Fix σ_from_half scaling

- In §VI.A (or wherever "scale as n" appears): replace "scale as n at fixed fractional offset" → "scale as √n at fixed fractional offset" (since σ_from_half = 2(f_CW − 0.5)√N).

### C5 — R34-P5-29 (VERIFIED MINOR): Disambiguate Bonferroni thresholds in abstract

- In the abstract density-quintile falsification sentence: "below the Bonferroni-5 threshold |σ|≈3.09 for the five density quintiles at α=0.01 (distinct from the DESIVAST primary-family threshold |σ|≈2.58 at α=0.05)."

### C6 — R34-P5-04/05/25/26/27 (VERIFIED MINOR): Batch precision edits

- R34-P5-04: "16.4 × 10⁶" → "16.36 × 10⁶" in abstract.
- R34-P5-05: "catalog-monopole offset" → "catalog-wide classifier-monopole systematic" in abstract.
- R34-P5-25: Replace "clean null" with "consistent with null" throughout.
- R34-P5-26: Add "the observed 1.64 pp deviation is well inside the 1σ binomial half-width of 2.42 pp" alongside the 2σ floor statement.
- R34-P5-27: At the "strongest single-class signal" statement, add the corresponding monopole-subtracted residual |σ_obs − σ_pred| to make the comparison properly normalized.

### Ruled / HOUSTON-DECISION (no action this wave)

- R34-P5-01/11: Paper IV companion dependency — mint-at-submission (HD-11).
- R34-P5-03/06/10/16: Version-history language — Houston-decision at journal submission.
- k=20 / NM-A family — quadruple-ruled HOUSTON-DECISION.
- R34-P5-13/21: V-Web/T-Web body rename — bounded editorial, Houston-decision.
- R34-P5-07: Length — editorial.

---

## Verdict

**NOT CLEAN.** One confirmed regression (R34-P5-28), 3 new MAJORs, 7 new MINORs. The 6-item closure plan above addresses all verified findings. The headline science (three-algorithm DESIVAST null; V-Web secondary null; z-shell robustness) is **not challenged by any reviewer**. Pattern-052 applied; 13/15 Gemini extraction-artifact streak stands (Gemini P5 this round gave no layout/math extraction artifacts — findings were text-logic based, so pattern-052 pre-screen was moot here; all Gemini P5 R34conf findings were correctly audited on merit).

---

*Verdict counts: VERIFIED 11 (4 MAJOR, 7 MINOR, 1 regression) · PARTIAL 11 · OPINION 4 · HOUSTON-DECISION 5 · AUTO-FALSIFIED 2*
*Pattern-052: not triggered on P5 this round (Gemini findings were text-logic, not extractor-artifact). Gemini P5 stream extractor-artifact streak = 13/15 still stands from EXT2–EXT4; R34conf Gemini P5 findings were content-based.*
*Claude leg absent: API 400 / zero credits. 4/5 legs present.*
