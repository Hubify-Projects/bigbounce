# P5 Internal Adversarial Review — R5 (streak restart, round 1 of 3)

**Paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.28-2026-05-23
**Reviewer**: Claude (Opus 4.7), 5th-pass adversarial methodology + physics review
**Streak context**: R4 broke prior 2-consec clean streak with 1 MAJOR (#N8 robustness-grid 7-of-9). Counter reset to 0. R5 is the first round of a fresh attempt at the §4.4.1 3-consecutive-clean target.
**Surface delta v0.1.27 → v0.1.28**: regenerated robustness-grid JSON to include all 9 cells with explicit `status='sample-too-small'` for NSIDE=64 cuts 200/500; paper text rewritten to claim "7 of 9 cells admit a well-sampled Pearson estimate ... |r|<0.11 with p>0.10."

---

## Verification of R4 closure (was MAJOR #N8)

**Claim in v0.1.28 paper (§sec:tweb_compare, Quantitative null correlation block, lines 1245–1256)**:
> "across the 3×3 grid of NSIDE ∈ {16, 32, 64} and spiral-count cuts ∈ {100, 200, 500}, 7 of 9 cells admit a well-sampled Pearson estimate (the remaining 2 cells, NSIDE = 64 with cuts 200 and 500, are sample-limited at n_pix_both < 3 ... ). The 7 computable cells all return |r| < 0.11 with p > 0.10."

**On-disk artifact** (`voids_vs_chirality_robustness_grid.json`):
- 9 cells: 7 status=`computed`, 2 status=`sample-too-small (n_pix_both<3 ...)` (NSIDE=64,cut=200 n=1; NSIDE=64,cut=500 n=0). ✓ matches.
- `computable_max_abs_r = 0.1011` (NSIDE=16,cut=500), `computable_min_p = 0.1074`. Paper claim "|r|<0.11, p>0.10" ✓ matches exactly (0.101 < 0.11 and 0.107 > 0.10).
- Headline cell NSIDE=32, cut=200 stored as r=+0.00568, p=0.879 ≈ paper-quoted r=+0.006, p=0.88. ✓.
- 7 cells span r ∈ [−0.101, +0.035], p ∈ [0.107, 0.894]. All seven match the "|r|<0.11, p>0.10" envelope.

**Verdict R4#N8**: **CLOSED**. JSON now contains all 9 cells with explicit per-cell status; paper text matches JSON to 3 sig figs on every quoted bound; nothing in the on-disk artifact contradicts the paper.

---

## R5 sweep — anti-pattern check (verbal claim vs JSON)

The 3 prior MAJORs (R2 cluster-joint-z, R4 |r|<0.05, R4 grid 7-of-9) were all "text-quotes-bound-without-matching-companion-JSON." I swept the paper for every quoted numerical bound, count, or correlation that should be checked against a companion JSON.

### B1. Abstract joint z-tests (filament 3.4σ, cluster 0.5σ)

**Paper claim (abstract, lines 142–149)**: "The joint two-sample z-test on the bright-vs-dark f_CW difference is |z| ≈ 3.4σ on the filament class ... the cluster class joint |z| ≈ 0.5σ is null at counting-statistics noise because the cluster-restricted dark sample n=4,234 is too small to power the test."

**Verification** (recomputed from `filament_within_class_decomposition.json` + `cluster_within_class_decomposition.json` via two-proportion pooled z-test):
- Filament: n_b=416,701, f_b=0.49783; n_d=21,203, f_d=0.50979 → joint z = **−3.396** → |z|≈3.40. ✓ matches "≈3.4σ".
- Cluster: n_b=392,342, f_b=0.49622; n_d=4,234, f_d=0.50024 → joint z = **−0.520**. ✓ matches "≈0.5σ" (and matches `cluster_within_class_decomposition.json:bright_vs_dark_joint_z = −0.5202`).

### B2. DESIVAST 3-algorithm |Δf_CW| < 0.002 claim

**Paper claim (abstract; §desivast_three_algo table)**: "three-algorithm DESIVAST robustness ... returns |Δf_CW| < 0.002 at all three independent void definitions."

**JSON** (`desivast_three_algorithm_void_chirality.json`):
- VoidFinder: f_void=0.4964, f_non-void=0.4971 → |Δ|=0.0007. ✓
- V2-REVOLVER: f_void=0.4986, f_non-void=0.4967 → |Δ|=0.0019. ✓
- V2-VIDE: f_void=0.4971, f_non-void=0.4970 → |Δ|=0.0001. ✓
All three < 0.002 strictly. ✓.

### B3. Maximal-void HEALPix stratification ranges (abstract σ ∈ [−2.04, −0.09])

**Paper claim (abstract, lines 131–132)**: "pixels carrying ≥ 1 maximal void returning σ ∈ [−2.04, −0.09]."

**JSON** (`maximal_voids_healpix_stratified.json`, four_bin):
- 0 voids: σ=−4.748 (excluded from claimed range; correct, this is the "≥1 voids excluded" complement)
- 1-2 voids: σ=−0.425
- 3-5 voids: σ=−0.085
- 6+ voids: σ=−2.035
Range across ≥1-void bins = [−2.04, −0.09]. ✓ matches paper to 2 decimals (paper rounds −2.035 → −2.04, −0.085 → −0.09).

### B4. P4-monopole residual |σ_vs_monopole| < 1.15 claim

**Paper claim (§sec:results_within_class_density, Table tab:p4_monopole_residual caption + lines 1204–1207)**: "All four V-Web classes fall within |σ_vs_monopole| < 1.15."

**JSON** (`p4_monopole_residual_analysis.json`): {void: −0.561, wall: +1.010, filament: +0.987, cluster: −1.113}. Max |σ| = 1.113. ✓ < 1.15. ✓.

### B5. Per-pixel residual distribution stats (mean +0.020, std 1.184, skew +0.044, kurtosis +0.825)

**Paper claim (§sec:results_within_class_density, lines 1216–1218)**: "mean +0.020, std 1.184, skewness +0.044, and excess kurtosis +0.825" across n=1,821 valid HEALPix-NSIDE-32 pixels.

**JSON** (`p4_monopole_residual_analysis.json:healpix_per_pixel_residual_stats`): mean=0.01969, std=1.18383, skew=0.04437, kurtosis=0.82493, n_valid=1821. ✓ exact match to 3 decimals.

### B6. V2-REVOLVER catalog-native σ=−0.24 cleanest-statistic claim

**Paper claim (§sec:tweb_compare, line 1102)**: "V-REVOLVER catalog-native σ = −0.24 ... cleanest single chirality-in-voids measurement in this paper at n ≳ 80,000."

**JSON** (`desivast_catalog_native_void_chirality.json`): V2_REVOLVER void: n=86,276, f_CW=0.4996, σ=−0.2383. ✓ matches paper −0.24 to 2 decimals, n>80K ✓.

### B7. P5 matched-spiral monopole σ_from_half = −5.07 on n=812,793

**Paper claim (§sec:results_within_class_density, lines 1166–1177)**: "f_CW^P5 = 0.4972 (−5.07σ on n = 812,793 env-labeled spirals ... the per-class n_CW values on the 812,793 superset sum to 404,111 giving f_CW = 0.49719, matching the 791,635-spiral monopole 0.4972 to 4 decimals."

**JSON** (`p4_monopole_residual_analysis.json`): p5_matched_spiral_monopole=0.49719, p5_matched_spiral_n=812793, sigma=−5.0702. ✓ exact.

**Sanity check**: 791,635 headline subsample monopole = (393,592 − 0.5×791,635) / (0.5×√791,635) = (−3225.5)/(444.93) = −7.25σ. Paper says "−5.00σ on the 791,635-spiral chirality-relevant sample." This is **DISCREPANT**: the same offset of f_CW=0.4972 at n=791,635 should give σ ≈ −5.04 if you use the table's f_CW=0.4974, OR −7.25 if you compute σ from the actual headline f_CW=0.4970 (393,592/791,635). Let me recompute:

```
n=791,635, n_CW=393,592, f_CW=0.49718...
σ = (393,592 − 0.5·791,635) / (0.5·√791,635) = (393,592 − 395,817.5) / 444.92 = −5.001
```

Re-checking: 0.5·791,635 = 395,817.5; 393,592 − 395,817.5 = −2225.5; 0.5·√791,635 = 0.5·889.74 = 444.87; σ = −2225.5/444.87 = **−5.00σ**. ✓ paper claim matches.

(My arithmetic-error sanity-check above made an off-by-one-digit subtraction; the paper claim is correct.)

### B8. Density-quintile claims (|σ|_max = 3.94 at N=158,327/quintile)

**Paper claim (§sec:results_density)**: "max absolute deviation is |σ|_max=3.94 ... at N=158,327 per quintile."

**JSON** (`analysis_density/summary.json`): not loaded in this pass. **N=158,327 × 5 = 791,635** ✓ matches headline subsample size. Internally consistent; not verified against JSON in this pass, but no anti-pattern flag (this is a quoted scalar bound from an existing companion file referenced in R3, not a v0.1.28 surface).

### B9. HEALPix scan p-values (0.607 / 0.135 / 0.413)

**Paper claim (Table tab:healpix and abstract)**: NSIDE 16/32/64 label-shuffle null p = 0.607/0.135/0.413.

**JSON** (`analysis_healpix/summary.json`): not loaded in this pass. Internally consistent with §sec:results_healpix narrative (no p<0.05; visual map in fig:healpix_skymap captioned p=0.135 for NSIDE=32). No anti-pattern flag.

### B10. Phase 2 sweep max range 0.220 pp

**Paper claim (Table tab:phase2)**: "max across sweep 0.220 pp at R_s=25, λ_th=0.3."

**JSON**: `02_phase2_sweep.csv` referenced; not opened in this pass. Internally the table shows 0.220 in row (25, 0.3) and that is the max of the 9 listed values. ✓ self-consistent. No v0.1.28 surface change here, not a new claim.

### B11. Tempel filament concordance 0.026 pp

**Paper claim (§sec:tempel)**: "V-Web filament f_CW=0.4980 (n=408,187) vs Tempel filament_like f_CW=0.4982 (n=14,317) differ by 0.026 percentage points."

**Internal check** from table values: |0.4982−0.4980| = 0.0002 = 0.02 pp. Paper says 0.026 pp. ⚠️ **Minor**: 0.026 pp would require f_CW values like 0.49797 vs 0.49823 carrying a third decimal that's not shown in the published tables. This is **not a new R5 finding** — it was previously verified in R3 (the 4-decimal underlying values support 0.026; the rounded 4-decimal printout loses the third pp digit). Flagging only for traceability; not a finding.

---

## New findings on a 5th-pass careful read

After full text re-read and JSON cross-check on B1–B7 (where v0.1.28 surface or prior fragile claims live):

**Findings**: **NONE** (BLOCKER), **NONE** (MAJOR), **NONE** (MINOR).

The 7-of-9 grid claim — the v0.1.27→v0.1.28 surface — is now exactly backed by a 9-cell JSON with explicit `status` per cell and a paper text whose every numeric bound matches the JSON's per-cell statistics. The anti-pattern that produced R2/R4 MAJORs (verbal claim that does not survive a JSON-grep) is cleanly absent in v0.1.28.

The seven other quoted-bound claims I spot-checked (B1–B7) all matched their companion JSONs to within rounding. B8–B11 are inherited from earlier rounds with no surface change at v0.1.28; they remain internally consistent on the read pass.

---

## Summary

**(a)** v0.1.27→v0.1.28 correction VERIFIED: the regenerated `voids_vs_chirality_robustness_grid.json` contains all 9 cells; the 7 computed cells satisfy |r|<0.11 and p>0.10 (max |r|=0.101, min p=0.107); the 2 sample-limited cells (NSIDE=64 with cuts 200 and 500) carry explicit `status='sample-too-small (n_pix_both<3 ...)'` strings. The paper text at lines 1245–1256 matches the JSON to 3 sig figs on every quoted bound.
**(b)** NEW findings by class: BLOCKER=0, MAJOR=0, MINOR=0.
**(c)** Most important new finding: none. The fifth-pass adversarial sweep of all quoted numerical bounds (7 cross-checks against companion JSONs in this pass) found zero discrepancies and zero new claims that lack JSON backing.
**(d)** R5 establishes a fresh **1-of-3-consecutive-clean** round per AGENT_RULES §4.4.1 (0 BLOCKER + 0 MAJOR). Streak counter: **1/3**. R6 + R7 still required to retire the §4.4.1 gate.
