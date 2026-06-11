# P5 R29 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7 (in-session)`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.61.pdf` md5=5eb81cd5 pages=30
**Input format**: NATIVE PDF (in-session render of pages 8, 9, 17, 18) + .tex full-read + JSON-artifact cross-check
**Wall time**: in-session (API leg failed on credits; in-session replacement per Houston directive)

---

## Scope of this referee leg

In-session brutal-honesty PRD referee against `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.61-2026-06-10, post-EXT1-closure-wave) and the compiled `site/public/papers/p5_desi_chirality_v0.1.61.pdf`. Read full .tex, rendered PDF pages 8–9 (Analysis-tree Table II) and 17–18 (DESIVAST-program-split Table IX + Three-algorithm Table X) to verify the two NEW tables, and cross-checked every number in the new tables against `pipelines/p5_desi_chirality/outputs/27_ext1_logistic_program_control.json` and `outputs/28_ext1_desivast_program_split.json`.

Upgraded sweeps (15)–(19) per Houston EXT1-closure directive applied below.

---

## Provenance + new-artifact verification (sweep 16)

**JSON files exist and match the paper EXACTLY**:

`outputs/27_ext1_logistic_program_control.json`:
- `M0.joint_env_wald_chi2 = 2.7533`, `p = 0.4312` → paper §VI.A.d (line 1311): `χ² = 2.75 (p = 0.43)` ✓
- `M1.joint_env_wald_chi2 = 2.2508`, `p = 0.5220` → paper: `χ² = 2.25 (p = 0.52)` ✓
- `M1.is_bright.z = -1.971`, `p = 0.0487` → paper: `z = −1.97, p = 0.049` ✓
- `sample.n_bright_dark = 782,710` → paper line 1306: `n = 782,710` ✓
- Verdict statement in JSON ("env coefficients shift ≤0.01 SE") → paper claims "shift by ≤ 0.01 on their standard errors" ✓ (manual recompute from JSON: void coef shifts (-0.00460 → -0.00397) / SE 0.0985 = 0.0064; wall (0.0228 → 0.0203) / 0.0248 = 0.10; cluster (-0.00588 → -0.00537) / 0.00454 = 0.11 — see MINOR-2 below).

`outputs/28_ext1_desivast_program_split.json`:
- Void bright n=56477, n_cw=28053, f_cw=0.4967, σ=−1.56 → paper Table IX ✓
- Void dark n=469, n_cw=215, f_cw=0.4584, σ=−1.80 → ✓
- Non-void bright n=615078, σ=−4.72 → ✓
- Non-void dark n=5845, f_cw=0.5056, σ=+0.85 → ✓

PROVENANCE VERDICT: clean. Both JSONs exist; every quoted number reproduces from the artifact.

---

## DESIVAST count update sweep (sweep 16b)

Grep for `1,489|1,461|420|389|297|295`:
- Line 1637–1640 (§sec:desivast_primary opening): `1,489 interior voids with VoidFinder, 389 with V2-REVOLVER, and 297 with V2-VIDE (final published counts from ApJ 982, 38, Table 1; an earlier preprint version cited 1,461/420/295, which were preliminary values)`. ✓
- Line 56–57 (preamble changelog): ledger note documents the 1,461/420/295 → 1,489/389/297 transition. ✓
- Line 1870–1873: `389 (V2-REVOLVER) and 297 (V2-VIDE) interior void counts` — consistent with updated values. ✓
- Lines 1985, 2381: `297` appears in unrelated contexts (HEALPix occupied pixels; cluster-class density quartile) — false positives, not the DESIVAST count.

VERDICT: All four occurrences updated. No stale `1,461/420/295` remains in body text (only in the explicit "earlier preprint version cited" pedagogy line and the preamble ledger). Pass.

---

## ESSENTIAL findings

### P5-E29-1 — Six-object n=6 binomial-bound presentation buries the qualifier the EXT1 protocol mandated (sweep 15)

**Refs**: line 251–255 (abstract); line 1722–1745 (§sec:desivast_xmatch).

**Quote (abstract, line 251)**: "supplemented by an n=6 per-galaxy classifier-disagreement check --- in this six-object illustrative check, 0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes at z ≤ 0.24; the n=6 sample is too small for a formal purity constraint, but it illustrates the survey-shell systematic driving the V-Web void class at low z".

**Quote (§sec:desivast_xmatch, line 1736)**: "With 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.05^(1/6) = 39%, so this purity statement is indicative rather than statistically established".

**Issue**: F17 closure ADDED the "in this six-object illustrative check" qualifier, but the body text in §sec:desivast_xmatch immediately follows with the rule-of-three-equivalent calculation that yields an upper bound of **39%** — i.e. the data do not exclude a true V-Web-void-purity-vs-DESIVAST fraction as high as ~40%. This is presented in a way that an attentive reader will register, but a casual reader of the abstract sees "0/6 V-Web 'void' spirals" + "survey-shell systematic" and walks away with the impression of a quantitative purity bound that the n=6 sample CANNOT deliver. The "indicative rather than statistically established" hedge is correct; the abstract's framing does not echo this hedge strongly enough.

**Fix**: In the abstract, change "in this six-object illustrative check, 0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes" to "in this six-object illustrative check, 0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes (1-sided 95% UL on true in-hole fraction: 39%, consistent with the V-Web-void survey-shell systematic but too few objects to formally constrain it)". Keeps the result in the abstract but does not let n=6 read as a tight purity bound. **Effort: 1 sentence, 1 commit. P5-E29-1.**

### P5-E29-2 — "catalog-wide monopole offset" terminology consistency claim NOT FULLY HONORED (sweep + closure verification)

**Refs**: line 267, 277, 1077, 1133, 2035–2036, 2087.

**EXT1 closure ledger** (lines 65–66) claims: `C1/F19/F21: "catalog-level -5sigma headline" -> "catalog-wide monopole offset" at all 2 problematic instances (§VI.A.d and §VIII.maximal HEALPix)`.

**Issue**: Five remaining `catalog-level` uses survive in the body text that DO read as headline-equivalent residuals:
- Line 267 (abstract): "the −5σ catalog-level signal concentrated entirely in the '0 maximal voids per pixel' bin" — still reads "the −5σ catalog-level signal" as a headline result.
- Line 1077 (§sec:results_within_class_density): "The catalog-level cluster-class deviation of −4.7σ at n_cluster = 397,505 (Section VI A) is the strongest single-class signal in the headline table." — language `catalog-level` + `strongest single-class signal in the headline table` is exactly the dual-use the closure was supposed to eliminate.
- Line 1133: "The catalog-level".
- Line 2035–2036 (§VIII maximal HEALPix): "showing that the catalog-wide −5σ monopole offset" — this one IS fixed, the closure went here.
- Line 2087: "the ∼9.5σ catalog-level monopole reported in Paper IV" — this is a Paper-IV monopole, terminologically OK.

Of the 5 hits, the fix only landed at 1 (line 2035–2036). The abstract (line 267) and §sec:results_within_class_density (line 1077) still call this "the catalog-level signal" / "the catalog-level cluster-class deviation" without the explicit "monopole offset" qualifier. This is a half-closure of C1/F19/F21.

**Fix**: Replace the abstract `the −5σ catalog-level signal concentrated entirely` with `the −5σ catalog-wide monopole offset concentrated entirely`. Replace line 1077 `The catalog-level cluster-class deviation of −4.7σ` with `The catalog-wide-monopole-projected cluster-class deviation of −4.7σ` (or equivalent). Then re-run the grep — should leave only Paper-IV-monopole references in `catalog-level` form. **P5-E29-2.**

### P5-E29-3 — Abstract over-states "robustness" by listing the BGS-bright-only "control" as a clean separation, when the paper itself flags it as confounded

**Refs**: abstract line 273–292; body §VI.A.d line 1280–1302.

**Quote (abstract, line 273–280)**: "The signal tracks survey-mask geometry, not environment density, consistent with the BGS-selection-function-conditioned imaging-leg systematics tracked in Paper IV; this is confirmed by a tracer-program decomposition showing the catalog-level −5σ is entirely driven by the BGS-bright sample, with the LRG/ELG/QSO-dark sample returning σ = +1.25 (filament class, on the declared env-labeled parent: bright n=394,181 at σ=−2.98 vs dark n=13,759 at σ=+1.61, opposite sign)."

**Quote (body, line 1280–1290)**: "We therefore cannot assert V-Web class orthogonality to the target-program split, and the |z| ≈ 2.1σ bright-vs-dark sign-flip in the filament class is best read as a residual structure that the current data do not allow us to cleanly partition between (a) a BGS-selection-function-only origin propagated through a V-Web-class-correlated target-program distribution, and (b) a residual class-and-target-program-conditioned astrophysical signal at the ∼2σ level on n_dark^filament = 13,759."

**Issue**: The abstract presents the tracer-program decomposition as a CONFIRMATION ("this is confirmed by a tracer-program decomposition") that the −5σ is selection-function. The body explicitly says the data CANNOT partition the two interpretations (BGS-selection-only vs residual astrophysical signal). The abstract should not call this a "confirmation"; it is a CONSISTENCY check with an unresolved ~2σ residual. This is exactly the kind of abstract-vs-body drift the EXT1 sweep was meant to surface — the abstract gained the Cramér's V + log₁₀p text (good) but did not soften the "is confirmed by" verb (bad).

**Fix**: Change abstract `this is confirmed by a tracer-program decomposition showing the catalog-level −5σ is entirely driven by the BGS-bright sample` to `this is CONSISTENT with a tracer-program decomposition in which the catalog-wide monopole offset is dominated by the BGS-bright sample (the bright vs dark sign-flip at |z|≈2.1σ in the filament class remains a residual structure the current data cannot cleanly partition into selection-only vs residual astrophysical components; §VI.A.d)`. **P5-E29-3.**

---

## MAJOR findings

### P5-M29-1 — Effect-size honesty: Cramér's V=0.078 IS explicitly labelled "small" in §VI.A.d (line 1274–1275) but the abstract presents the same number naked next to χ²=4932, log₁₀p≈−1069 (sweep 19)

**Refs**: abstract line 295–298 vs body line 1272–1279.

**Quote (abstract, line 295)**: "A contingency test (§VI.A) finds V-Web class and target program are not independent (χ² = 4932, 3 d.o.f., log₁₀p ≈ −1069, Cramér's V = 0.078, max class-to-overall bright-fraction deviation 1.5 pp)".

**Quote (body, line 1274–1275)**: "Cramér's V = √(χ²/n) = 0.078 (small effect despite the enormous sample)".

**Issue**: Body has the correct effect-size interpretation in parentheses ("small effect despite the enormous sample"). Abstract drops the qualifier and lets V=0.078 sit next to a log₁₀p=−1069 number that any reader will round to "infinitely significant". Sweep 19 directive is specifically: does the paper now honestly characterize this as small-effect-size? The body does; the abstract does not. The reader-level outcome is determined by the abstract.

**Fix**: Append "(Cramér's V=0.078 is conventionally a small effect; the chi-squared statistic is driven by sample size n=811,609 rather than effect magnitude)" to the abstract sentence at line 297. Three additional words; no compute. **P5-M29-1.**

### P5-M29-2 — DESIVAST −5σ catalog-wide monopole offset itself is now "small effect" by the same Cramér's-V logic the paper just adopted, but the paper never says so

**Refs**: §sec:desivast_anchored_void Table VIII (line 1783–1796); abstract line 256–259.

**Quote (body, Table VIII)**: void f_CW = 0.4964 (σ=−1.71, n=56,981) vs non-void f_CW = 0.4971 (σ=−4.59, n=621,964), Δf_CW = 0.0007.

**Issue**: The paper's main DESIVAST primary-path result (a void/non-void f_CW difference of 0.07 pp on n_void = 56,981 + n_non-void = 621,964) has its own Cramér's V equivalent. Computing crudely from the 2×2 table: φ = √(χ²/n_tot) where χ² ≈ (2σ)² of the difference. The observed two-sample z is about (0.0007 / √(0.5×0.5×(1/56981+1/621964))) ≈ 0.32 (effectively null) — so φ ≈ 0.0004 — a TRULY tiny effect. This is consistent with the paper's "statistically indistinguishable" framing of the void/non-void comparison and is FINE. But the SAME Cramér's-V reasoning, applied to the −5σ "catalog-wide monopole offset" itself, gives V ≈ √(25/812793) ≈ 0.0055 — vanishingly small. The paper just adopted Cramér's V as the honest effect-size language for the bright/dark contingency; it should adopt the same language consistently for the −5σ monopole offset, which is a SAMPLE-SIZE driven significance, not a large effect.

**Fix**: In §VI.A (around line 902 in the headline result language) and/or in the abstract description of the −5σ monopole, add a single parenthetical: "the catalog-wide monopole offset is highly statistically significant by σ-from-half (n ≈ 8×10⁵) but corresponds to a fractional offset of |Δf_CW| ≈ 0.0026 — a small effect by the same Cramér's-V scaling used above for the V-Web×program contingency". Brings the effect-size honesty to the headline statistic, not just the residual structure. **P5-M29-2.**

### P5-M29-3 — Logistic-regression "≤0.01 SE" claim is approximately correct but the JSON shows the wall and cluster shifts are 0.10–0.11 SE, not 0.01 SE

**Refs**: §VI.A.d line 1314–1318; JSON `outputs/27_ext1_logistic_program_control.json`.

**Quote (paper, line 1314–1316)**: "Crucially, the three V-Web environment coefficients (void, wall, cluster vs filament) shift by ≤ 0.01 on their standard errors after program adjustment in M1 relative to M0".

**JSON-derived recompute** (M0 → M1 shift in units of M0 SE):
- void: (−0.00461 → −0.00398) / 0.09847 = **0.0064 SE** ✓
- wall: (0.02278 → 0.02028) / 0.02483 = **0.101 SE** ✗ (10× the claim)
- cluster: (−0.00588 → −0.00537) / 0.00454 = **0.112 SE** ✗ (11× the claim)

The "≤ 0.01 on their standard errors" wording is FALSE for the wall and cluster coefficients. The shifts are ~0.1 SE for those two — still small enough to support the "not confounded" verdict (the joint Wald p shifts 0.43 → 0.52, also small motion), but the claim "≤ 0.01 SE" is QUANTITATIVELY WRONG.

This is exactly the kind of finding that R-rounds catch and that propagates to F25 follow-ups if not fixed cleanly NOW.

**Fix**: Change line 1314 from "shift by ≤ 0.01 on their standard errors" to "shift by ≤ 0.12 on their standard errors (void 0.006σ, wall 0.10σ, cluster 0.11σ — all small relative to the |z|>1.96 significance threshold)". Numbers from JSON. One sentence. **P5-M29-3.**

### P5-M29-4 — DESIVAST count update propagated to body but not to derived assertions about Tempel / DR1-BGS density consistency

**Refs**: line 1637–1640 vs §sec:tempel (line 2411+).

**Issue**: The DESIVAST counts updated 1,461/420/295 → 1,489/389/297 (+1.9%/-7.4%/+0.7%). The V2-REVOLVER count dropped 7.4% (420 → 389). This is a non-trivial change in the V2-REVOLVER interior void count that anchors the three-algorithm robustness statement. The body text at line 1870–1873 acknowledges these are the new numbers, and Table X (page 18 of the PDF) reports n_void = 102,911 for V2-REVOLVER on the matched-spiral subsample (a per-galaxy count, not the interior-void count, so the −7.4% in the catalog count does not necessarily propagate to a −7.4% in n_void on the matched subsample — KDTree query against published effective-radius spheres includes ALL effective voids, not just interior ones).

This is potentially OK if the Table X point-in-sphere test was rerun against the **updated** V2-REVOLVER void catalog. But the paper does not state explicitly that the Table X numbers come from the final-ApJ V2-REVOLVER catalog rather than the preliminary preprint catalog. Given that V2-REVOLVER count moved −7.4%, this is a non-zero check.

**Fix**: Add one sentence at §sec:desivast_three_algo (around line 1867) clarifying: "The point-in-sphere queries in Table X use the final ApJ 982,38 DESIVAST catalogs (n_eff_void = 1,992 V2-REVOLVER, 1,478 V2-VIDE); the upstream interior-void count revision (420 → 389 for V2-REVOLVER interior) does not change the effective-void total used for the membership test". OR if Table X numbers were computed against the preliminary preprint catalog, RE-RUN the point-in-sphere queries against the final catalog and update Table X. Default disposition per Houston standing directive `feedback_take_critiques_seriously.md`: re-run. **P5-M29-4.**

---

## MINOR findings

### P5-m29-1 — Table II (analysis_tree) primary-family declaration mixes two non-orthogonal estimator pairs (sweep 17)

**Refs**: Table II rendered on PDF page 8; .tex line 805–809.

**Issue**: Bonferroni-5 primary family includes:
- DESIVAST VoidFinder point-in-sphere
- DESIVAST V2-REVOLVER point-in-sphere
- DESIVAST V2-VIDE point-in-sphere
- V2-REVOLVER catalog-native GALZONE
- V2-VIDE catalog-native GALZONE

Estimators 2+4 (V2-REVOLVER point-in-sphere AND V2-REVOLVER GALZONE) and 3+5 (V2-VIDE point-in-sphere AND V2-VIDE GALZONE) are NOT independent — they both partition the same matched-spiral subsample under correlated definitions of "V2-REVOLVER void" (sphere-approximation vs catalog-native). Treating the 5 as a Bonferroni-5 family OVER-corrects (the 5 effective tests are closer to ~3.5 independent tests). The paper's own Table X+ catalog-native discussion explicitly says "the catalog-native void definition is the cleaner statistic" (line 1937–1938) — i.e. it is THE result, not an additional independent test.

This DOES NOT change the verdict (every estimator is null), but the Bonferroni-5 framing reads as harder than necessary. A reader who flags this will conclude the multiplicity correction is mis-applied.

**Fix**: Add a footnote to Table II: "The five primary estimators are not strictly mutually independent: V2-REVOLVER point-in-sphere and V2-REVOLVER GALZONE share the V2-REVOLVER catalog parent (similarly V2-VIDE), so the effective number of independent primary tests is between 3 and 5; Bonferroni-5 is therefore a conservative upper bound on the per-test multiplicity threshold". One sentence. No re-compute. **P5-m29-1.**

### P5-m29-2 — RSD-scoping sentence is correctly softened but reads as a paragraph-length detour from the primary-result statement (sweep — RSD scoping verification)

**Refs**: §sec:desivast_primary line 1645–1702 ("RSD treatment for DESIVAST" subsection).

**Quote (line 1646–1649)**: "The DESIVAST primary path is RSD-bounded (rather than strictly immune) at the level relevant to this work --- individual in/out membership flips for spirals near hole boundaries are not excluded, but the displacement scale argument below bounds their rate".

**Issue**: F11 closure (per preamble, line 76–78) downgraded the RSD claim from "inherit no anisotropic RSD systematic" to "RSD-bounded at the level of this fixed-void-geometry membership sensitivity test; full immunity would require void-catalog reconstruction". This is honest and correct. But the resulting 60-line subsection (lines 1645–1702) is dense and DOES read as the paper protesting too much. A skeptical reader will pattern-match to "this is doing a lot of work to explain why we can't actually do the RSD test properly".

**Fix**: Move the FoG Monte-Carlo bound (line 1672–1687) into an appendix; keep only the scaling argument + the conclusion ("RSD-bounded; FoG MC gives |Δf_CW| within ±0.4 pp; bound below at present precision") in the body. **P5-m29-2.**

### P5-m29-3 — Rs=10 grid-unresolved labelling in Table VI is good but the abstract still leaves the reader to derive the resolved-cell bound

**Refs**: abstract line 213–216; Table VI ("Resolved cells" / "Grid-unresolved" split) on PDF.

**Quote (abstract, line 214–216)**: "the headline sign-pattern ... is invariant under the smoothing scale and threshold choices (the R_s = 10 Mpc/h cells sit below the 25.9 Mpc/h grid resolution and are retained only as a degenerate near-unsmoothed limit, §VI.B)".

**Issue**: The abstract does the work for the reader on Rs=10 — good. But it does NOT state the resolved-6-cell maximum residual bound (1.64σ from line 1414), only the 9-cell bound (1.87σ from line 1413). The body-level robustness CLAIM is on the resolved 6 cells (per preamble line 71–72: "max(resolved 6)=1.64σ now explicitly the primary robustness bound"). The abstract should reflect this.

**Fix**: In the abstract paragraph after the Phase-2-cell description (line 207–216), add: "Restricting to the six grid-resolved cells (R_s ∈ {25, 50} Mpc/h), the max monopole-subtracted residual is 1.64σ; the Rs=10 cells (sub-grid-scale) are retained for completeness only". One sentence. **P5-m29-3.**

### P5-m29-4 — DESIVAST void volume fraction sentence reads correctly (sweep verification)

**Refs**: line 925–928 (§sec:results_density).

**Quote**: "the small void volume fraction of ≈0.1% of in-footprint cells".

VERDICT: F16 closure fix is present. Pass. No action.

### P5-m29-5 — Standalone-reader: P4 companion placeholder language is internally consistent (sweep 18 verification)

The paper cites Paper IV as "companion work, not yet peer-reviewed" (abstract line 135). The "v1.0.166" specific version reference at lines 39 (preamble) and 2308 in the body is OK as a forward-pinned anchor. Multiple places of Paper-IV-anchored quantitative claims (Δf_CW = −0.0026, 0.4974 reference monopole) are stated with the relevant Paper IV citation; the reader can in principle reach the quoted numbers via the P4 PDF in the same arxiv submission. Pass. No action.

### P5-m29-6 — Logistic regression sample size n=782,710 ≠ n=783,820 unique env-matched spirals — explain the difference

**Refs**: line 1306 vs line 167–168 abstract.

**Issue**: Logistic regression model uses n = 782,710 (line 1306, "bright+dark env-matched spirals"). The headline parent is n_unique = 783,820. The difference (1,110 spirals) is the "neither bright nor dark" subset (BACKUP + OTHER programs). The paper does not say this explicitly. A reader chasing reproducibility will hit this gap.

**Fix**: One half-sentence at line 1307: "(the 1,110-spiral BACKUP+OTHER subset is excluded)". **P5-m29-6.**

---

## NIT findings

### P5-n29-1 — Table IX caption could state the artifact path

Table IX (rendered, page 17) caption ends without the artifact path. The same paragraph cites `outputs/28_ext1_desivast_program_split.json` in text. Move/duplicate the artifact path to the table caption to make the table self-contained.

### P5-n29-2 — Table II caption could explicitly cite the artifact path

Table II (analysis_tree) caption (line 795–798) does not cite the artifact / source data. Add `\artifact{...}` reference to the underlying tabulation source for review reproducibility, OR explicitly say "tabulation in body sections referenced; no separate artifact".

### P5-n29-3 — Abstract drift: bracket the new abstract additions in parentheses

The abstract additions (Cramér's V text, six-object qualifier) are integrated mid-sentence rather than in a structured Robustness / Caveats trailer. The abstract is now ~180 lines of LaTeX (the whole `\begin{abstract} ... \end{abstract}`) — long but acceptable for a PRD null-result paper. Optionally split into 3 paragraphs: Methods (lines 134–166), Headline (167–232), Robustness (233–308). Not load-bearing. **NIT only.**

### P5-n29-4 — Preamble changelog is again drifting toward 50+ lines

Preamble changelog at lines 53–84 + 86–122 is now ~70 lines for v0.1.61. The GRO-n1 closure (v0.1.44) explicitly stripped 380 lines of preamble changelog to `CHANGELOG_pre-v0.1.44.txt`. The same pattern is recurring. Roll v0.1.44–v0.1.60 changelog (lines 86–122) into the external file; keep only v0.1.61 in-preamble.

---

## Cross-checks against EXT1 closure ledger (preamble lines 53–84)

| EXT1 ID | Claim in closure ledger | This-review verdict |
|---|---|---|
| F2 | DESIVAST 1,489/389/297 updated | ✓ Pass (sweep 16b above). |
| F8 | Cramér's V=0.078 + log10(p)≈−1069 in abstract + §VI.A.d | ✓ Pass — but see P5-M29-1 (abstract drops "small effect" qualifier). |
| F9+F20 | Table tab:desivast_program_split + JSON 28 | ✓ Pass (Table IX renders cleanly page 17; numbers match JSON exactly). |
| F16 | "small void volume fraction (~0.1%)" replaces typo | ✓ Pass (m29-4 above). |
| C1/F19/F21 | "catalog-level −5σ headline" → "catalog-wide monopole offset" | ✗ HALF-CLOSURE — see P5-E29-2. Only line 2035–2036 fixed; abstract line 267 + §VI.D.b line 1077 + line 1133 + others still use `catalog-level` in headline-equivalent way. |
| F7/F22 | analysis-tree table tab:analysis_tree in §V.B | ✓ Pass (Table II renders cleanly page 8); see P5-m29-1 for over-correction note. |
| F10/C2 | Rs=10 rows separated + labelled grid-unresolved | ✓ Pass; but abstract should state resolved-6 max (P5-m29-3). |
| F25 | Logistic regression M0/M1 + JSON 27 | ✓ Pass on JSON sync; ✗ MAJOR-3 above (paper claim "≤0.01 SE" is quantitatively wrong; should be "≤0.12 SE"). |
| F11 | RSD language softened to "RSD-bounded" | ✓ Pass; P5-m29-2 minor cleanup only. |
| F17 | n=6 qualifier "in this six-object illustrative check" | ✓ Pass at both occurrences; P5-E29-1 asks for one extra word in the abstract. |
| F1 | Footprint-mask proxy primary-null clarification | ✓ Pass (verified in body §VIII.E and primary DESIVAST result is preserved). |

---

## Summary recommendation

**Counts**: ESSENTIAL 3 / MAJOR 4 / MINOR 6 / NIT 4 / total 17.

**Recommendation**: **Minor revisions, one major.** The EXT1 closure wave landed cleanly on the most expensive items (F25 logistic regression with new JSON, F9/F20 program-split table). Two unforced errors REMAIN: (a) the "≤0.01 SE" claim in §VI.A.d is QUANTITATIVELY WRONG by ~10× for wall + cluster coefficients (P5-M29-3 — must fix; one-sentence numerical correction with no re-run), and (b) the C1/F19/F21 "catalog-wide monopole offset" terminology sweep is only HALF-DONE, leaving the abstract and §VI.D.b dual-use that the closure was supposed to eliminate (P5-E29-2 — must fix; ~5 lines of text replacement, no re-run). One re-compute item exists (P5-M29-4: confirm Table X point-in-sphere queries used the FINAL ApJ V2-REVOLVER catalog, not the preliminary preprint), which can be settled in one paragraph if the queries already used the final catalog.

**Justification**: The paper is honest about its null result, anchors on the cleanest DESIVAST primary path with proper multiplicity declaration (Table II), and supports it with three-algorithm + GALZONE-native + HEALPix cross-checks. The two essential issues identified are both LANGUAGE issues (terminology consistency, abstract-vs-body drift on "confirmed" vs "consistent with"), not result-level issues. The one quantitative error (P5-M29-3) is a transcription-level mistake in the "≤0.01 SE" assertion, not a methodological flaw — the underlying logistic regression result (joint env Wald p shifts 0.43 → 0.52, env-independence holds under program control) is correct and the JSON artifact reproduces. Effect-size honesty (sweep 19) is half-present: the body labels V=0.078 "small effect"; the abstract does not (P5-M29-1). The provenance + DESIVAST-count-update sweeps both pass cleanly. Net: 1–2 commits of text edits + 1 confirmation paragraph close every finding above except the optional structural NITs.

**Confidence in this leg**: Medium-high — this is an in-session referee leg (API credit out), not a clean native-PDF dispatch. The PDF was rendered + read at the two critical new-table pages (8, 17–18); the JSONs were cross-checked numerically; full .tex was traversed. Repeat with a real native-PDF Anthropic vendor dispatch after credit refresh to capture any figure-level findings this leg may have missed.


