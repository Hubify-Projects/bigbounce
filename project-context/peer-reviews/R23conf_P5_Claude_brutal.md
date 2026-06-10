# P5 R23conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/p5_desi_chirality_v0.1.52.pdf` md5=cc7c3390 pages=24
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

Pass 1 = brutal referee read of all 24 pages (3 chunks, figures and tables inspected visually). Pass 2 = independent re-derivation of every flagged number (binomial σ, two-sample z, Bonferroni thresholds, count sums) before finalizing. Verdicts below survived pass 2.

## MAJOR findings

### P5-M1 — False "none crosses" claim: cluster z-quartile Z3 = −3.14 exceeds the stated Bonferroni-4 threshold 3.02
- **Location**: §VI.D, "Redshift-stratified cross-check" paragraph (p. 8, right column).
- **Problem**: Text reports cluster σ_from-half per z-quartile = −2.33 (Z1), −1.73 (Z2), **−3.14 (Z3)**, −2.12 (Z4), then asserts "none individually crossing the Bonferroni-4 |σ| = 3.02 threshold at α = 0.01." Verified: Bonferroni-4 at α=0.01 ⇒ two-sided per-test 0.0025 ⇒ z = 3.023. |−3.14| > 3.02. The claim is arithmetically false as written. (The same 3.02 convention is used correctly in the Tempel verdict, §IX.B, so this is not a threshold-definition ambiguity.)
- **Required fix**: Reword honestly: Z3 marginally exceeds the α=0.01 Bonferroni-4 threshold (3.14 vs 3.02). Note that the per-quartile Paper-IV monopole prediction at n≈99,376 is σ_pred ≈ −1.64, so the monopole-subtracted residual is ≈1.5σ (null) — that is the defensible statement. Do not leave a literal "none crossing" sentence next to a value that crosses.

### P5-M2 — Abstract, Fig. 3 caption, and Conclusions equate the 812,793 env-labeled rows with "791,635 unique" spirals; the body says 783,820
- **Location**: Abstract ("Per-class CW fractions on the 812,793 env-labeled spiral rows (the 791,635 unique chirality-relevant matched spirals, counted once per repeat … coadd row carried by the environment table)"); Fig. 3 caption ("n = 812,793 env-labeled spiral rows (791,635 unique chirality-relevant matched spirals)"); §XV Conclusions (same parenthetical).
- **Problem**: §VI.A and §VIII.F state explicitly that the env join covers **783,820** unique env-matched spirals and that **7,815** of the 791,635 matched spirals have no environment row and drop out (791,635 − 7,815 = 783,820 ✓). Therefore the 812,793 rows cannot contain 791,635 unique spirals. The body text is internally correct; the abstract, Fig. 3 caption, and Conclusions parentheticals are wrong by 7,815 (1.0%). This is exactly the residue of the duplicate-TARGETID root-cause this version set out to clean up — the superset/unique relabeling was done in Table II but not propagated to the three highest-visibility surfaces.
- **Required fix**: In all three locations, state "812,793 env-labeled rows covering 783,820 of the 791,635 matched spirals (7,815 lack an environment row; §VIII F)". Keep title's "791,635 DR1 Matched Spirals" (that one is the matched sample and is correct).

### P5-M3 — Bright/dark two-sample z-tests on the row-level parent ignore TARGETID overlap between the bright and dark splits; the data prove the overlap is material
- **Location**: §VI.D(c) filament bright/dark (n = 394,181 / 13,759, |z| ≈ 2.1); abstract p. 2 (same numbers, n_dark^cluster = 4,234); §I "joint two-sample z-test".
- **Problem**: The per-class program splits are computed on the 812,793-row parent, where one galaxy contributes one row **per survey–program coadd** — so a single TARGETID can appear in BOTH the bright and the dark split with the same chirality label. The paper's own numbers prove this is not negligible: filament-dark (13,759) + cluster-dark (4,234) = 17,993 rows, which already **exceeds** the total unique dark spirals in the matched catalog (14,782, §VI.D(b) and Table XIII). The two-sample z = 2.1 treats bright and dark as disjoint independent samples; with shared members the test is misspecified, and this 2.1σ sign-flip is the single most-discussed residual structure in the paper (§I, §VI.D, §XI, §XII).
- **Required fix**: Quantify the bright∩dark TARGETID overlap within the filament class, and report the unique-galaxy (per-TARGETID program assignment, as in §VI.D(b)) version of the filament two-sample test alongside the row-level one. If the unique-galaxy z drops materially below 2.1, the §I and §VI.D framing must soften. Arithmetic itself verified: row-level z = 0.0093/√(0.25/394,181 + 0.25/13,759) = 2.14 ✓, σ_dark = +1.61 ✓, σ_bright ≈ −3.0 (−2.98 quoted, consistent within f rounding).

## MINOR findings

### P5-m1 — Self-contradicting "never exceeds … maximum ratio 1.01"
- **Location**: §VII.A, first bullet (Counting-statistics floor), p. 10.
- **Problem**: "the per-cell range never exceeds the void-class 2σ counting floor 1/√n_void (maximum ratio 1.01 at R_s = 50, λ_th = 0.1)". Verified: range 4.12 pp vs floor 1/√599 = 4.09 pp → ratio 1.008 > 1, i.e. it **does** exceed in that cell.
- **Required fix**: "never exceeds … by more than ~1%" or "stays within 1.01× of".

### P5-m2 — Tempel-overlap V-Web class counts don't sum to the declared overlap
- **Location**: §IX.B Concordance metric, p. 18: V-Web on-overlap = 23/145/16,701/78,378.
- **Problem**: Sum = 95,247 ≠ 96,753 (the declared overlap). 1,506 spirals unaccounted — presumably the env-row dropouts (§VIII.F's 7,815 population intersected with the overlap), but the text never says so, and the section claims "both classifiers evaluated on the same 96,753-spiral overlap sample."
- **Required fix**: State the 1,506-spiral no-env-label dropout explicitly and correct "same … sample" to "common labeled subset."

### P5-m3 — z-shell residual band "(−2.3 to −3.7σ)" excludes the void class
- **Location**: §IX.A, p. 17, "Residual per-class deviations from 0.5 (−2.3 to −3.7σ) … identically across classes."
- **Problem**: From the quoted corrected populations/fractions: void σ = (0.4971−0.5)·2√4,353 ≈ −0.38, far outside the stated band; wall ≈ −2.5, filament ≈ −3.7, cluster ≈ −2.3 are in band. "Identically across classes" + a band that omits one of the four classes is sloppy.
- **Required fix**: Either quote all four σ values or say "the three large classes span −2.3 to −3.7σ; void at n=4,353 sits at −0.4σ, consistent with its smaller σ_pred."

### P5-m4 — z-shell scheme stops at z = 1.7 but the V-Web parent extends to z = 2.0
- **Location**: §IX.A, p. 17 ("21 thin redshift shells … one merged 1.5–1.7 shell") vs §III.B (parent window 0.01 ≤ z ≤ 2.0).
- **Problem**: Shell count checks out (10 + 10 + 1 = 21 ✓) but galaxies at 1.7 < z ≤ 2.0 are unaccounted in the corrected rebuild description.
- **Required fix**: One clause: merged top shell is 1.5–2.0, or state the 1.7–2.0 population is excluded/negligible and give its n.

### P5-m5 — Table XIII match-radius rows use an undeclared counting convention; cited ≥0.7 confidence row missing
- **Location**: Table XIII + §XI text, p. 20.
- **Problem**: (a) n at 0.5″ = 820,266 **exceeds** the deduped 1.0″ full sample (791,635); a tighter radius cannot match more unique objects, so these must be pre-dedup chirality-relevant rows — caption/convention never stated, while the caption's "full sample n = 791,635" uses the deduped convention. (b) Text quotes the confidence sweep "at most −0.24 pp … at p ≥ 0.7", but the table shows only ≥0.4/0.6/0.8 (max drift there −0.22 pp); the cited row is unverifiable.
- **Required fix**: Declare row-vs-dedup convention in the caption; add the ≥0.7 row or quote a tabulated threshold.

### P5-m6 — Covariate-regression p-values not reconciled with the omnibus test; joined-N never stated
- **Location**: §VI.B Physical-covariate robustness, p. 7.
- **Problem**: Env-only Wald p = 0.41 vs Pearson omnibus χ² = 3.55, p = 0.31 (§VI.A) — on the "same" canonical labels at n ~ 8×10⁵ these should nearly coincide unless the regression runs on a different parent (812,793 rows vs 791,635 unique vs 783,820 env-matched vs the GZ-joined subset). "100% coverage of the declared parent" is asserted but the actual regression N is never printed, so the 0.41-vs-0.31 gap is unexplainable by the reader. The 152,455 featured-subsample and p≈0.02 confidence-regressor numbers are otherwise fine.
- **Required fix**: State the regression N and parent explicitly and add one sentence reconciling Wald-vs-Pearson p.

### P5-m7 — "16.4×10⁶ ZWARN=0 input rows" vs Table I "DESI DR1 input rows 16,361,731"
- **Location**: Abstract line 2 vs Table I / §III.B.
- **Problem**: §III.B reads as if 16,361,731 is the **pre-filter** zall row count ("restricted to ZWARN==0 … The full DR1 input is 16,361,731 rows; after the spectro-galaxy filter…"), while the abstract labels the same 16.4M as already ZWARN=0. One of the two labels is wrong or the cut ordering is ambiguous.
- **Required fix**: Disambiguate (e.g. "16,361,731 ZWARN=0 rows of the zall-pix-iron catalog" in both places, if that is what the driver does).

### P5-m8 — Figure production defects
- **Location**: Figs. 2, 5, 8, 9.
- **Problem**: (a) Fig. 2 title and Fig. 9 titles/annotation render literal LaTeX escapes: "25\,Mpc/h", "95\%", "0.29\,pp" (mathtext leak). (b) Fig. 5 left panel x-tick labels (density-bin ranges) overprint into an illegible smear. (c) Fig. 8 top panel keeps rectangular 0.0–1.0 axis ticks on a Mollweide projection, and the bottom-panel title collides with the top colorbar label. None affect the science; all are visible to any referee at print scale.
- **Required fix**: Strip the `\,`/`\%` escapes (use plain unicode or proper mathtext), rotate/shorten Fig. 5 bin labels, `axis('off')` + padding on Fig. 8.

## NITPICKS

### P5-N1 — Title vs nomenclature footnote
Title advertises "T-Web (Hahn 2007) Tidal-Tensor Cross-Check," but §IV.A explicitly reserves "T-Web" for *external* implementations and names the in-house run "V-Web." The title therefore uses the term the body forbids for this work. Suggest "…with a Hahn (2007) Tidal-Tensor (V-Web) Cross-Check…" or drop the reservation footnote.

### P5-N2 — Withdrawal-note density (style only; disclosure itself is appropriate)
Five separate "An earlier draft quoted/stated…" notes (§VI.D filament n, §VII per-cell table, §VIII.F confidence-filter attribution, §IX.B overlap 110,586, §XI ±0.001) are scattered in-text. For PRD, consider consolidating into a short "Changes from prior preprint versions" paragraph (Appendix B) with one-line in-text pointers. The disclosures themselves are correct practice and should be retained.

### P5-N3 — Δf_CW sign convention in Table VIII never defined
Verified the column is f_non-void − f_void (VoidFinder +0.0007, REVOLVER −0.0019, VIDE −0.0001 all consistent), but no caption or text defines the convention, and §VIII.B quotes "+0.0006 instead of +0.0007" which only parses under that convention. One clause in the Table VIII caption fixes it.

### P5-N4 — §X "31.7%" appears as both ASTRA sheet fraction and V-Web filament fraction on the same overlap — confirm this numerical coincidence is not a copy slip.

## ALL-CLEAR areas (explicitly verified, pass 2)

- **Table II arithmetic**: all four f_CW and σ_from-half re-derived exactly (void −0.68, wall +0.55, filament −2.61, cluster −4.66; range 1.98 pp) ✓. Omnibus χ²=3.55, 3 d.o.f. → p=0.314 ✓; z-shell χ²=0.11 → p=0.99 ✓.
- **Table III/X residuals**: every |σ_obs−σ_pred| and f−f^P5 entry re-derived; σ_pred = 2.07 at N=158,327 ✓; Table X max |σ_vs-mono| = 1.11 < 1.15 ✓.
- **Tables V–IX internal consistency**: Table V matches abstract p-values; Table VI matches Fig. 7 heatmap cell-by-cell (max range 4.12 pp at R_s=50, λ=0.1; max residual 1.87 at R_s=10, λ=0.1; p_LEE 0.13–0.56) ✓; Table VII/VIII sums 56,981+621,964=678,945 ✓; Table IX sums and both monopole residuals (−1.55, +0.60) ✓.
- **§VIII.F reconciliation**: 21,158 = 812,793−791,635 (2.7%) ✓; 783,820 = 791,635−7,815 ✓; σ_pred ≈ 4.6 at √791,635 ✓; −5.07σ ⇔ Δf ≈ −0.0028 ✓; 404,111/812,793 = 0.49719 = 393,592/791,635 to 4 decimals ✓.
- **§VI.D bright/dark arithmetic**: filament z = 2.14 ("≈2.1" ✓); catalog 0.81 pp, z = 1.95 ("≈2.0" ✓); program σ values (−5.25/+1.25/+0.85/−0.14) all re-derived ✓; program n sums to 791,635 ✓; bright-fraction ratios consistent with χ²=4932 narrative ✓.
- **Tempel Table XI**: all four f and σ re-derived (n and n_CW sums exact; 96,753 ✓); filament concordance 0.29 pp at z = 0.49 ("~0.5σ" ✓); cluster 0.67 pp at z = 0.92 ("~0.9σ" ✓); verdict max 2.27 < 2.498 ✓ — apart from m2 above.
- **z-shell §IX.A counts**: corrected populations sum to 812,793 ✓; ×10.2 / ×23.2 / −54.4% ✓; range 0.05 pp ✓; |σ_vs-mono| ≤ 0.39 plausible ✓; geometry-footprint variant sums to 812,793 ✓.
- **Table I / §III**: all column sums and cross-references exact (CW+CCW, legs, GALAXY+QSO, dedup counts, 8.39%, 42,374, 101,863) ✓.
- **Abstract ↔ Conclusions ↔ Table II count consistency**: per-class numbers identical everywhere — apart from M2's unique-count parenthetical.
- **References**: spot-checked [9], [10], [13], [14] — plausible and correctly attributed. Appendix A toy-EFT hedging is appropriately caveated.

## Summary recommendation

**Minor-to-moderate revision.** The headline environment-independence null is robust and the underlying arithmetic is in unusually good shape — essentially every number I re-derived checks out. But three MAJOR textual/statistical-bookkeeping defects must be fixed before journal submission: a literally false "none crosses" Bonferroni claim (M1), a 7,815-galaxy unique-count conflation sitting in the abstract, a figure caption, and the conclusions (M2), and an unquantified sample-overlap problem in the paper's most-emphasized 2.1σ residual (M3). None changes the conclusion; all three would be caught by a careful PRD referee and M2/M3 sit on the exact fault line (duplicate-TARGETID joins) this version claims to have closed, so leaving them in undermines the credibility of the cleanup narrative. The eight minors are one-clause fixes plus figure regeneration.
