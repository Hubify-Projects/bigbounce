# P4 R25conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/chirality_catalog_paper_v169.pdf` md5=ad396d7d6cb05fe58969b73130bd4ddf pages=20
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique

---

## Calibration set respected
Per Houston: June 2026 date, retraction/correction notes (incl. 0.43→0.41σ regen note and generator-defect disclosure), unthresholded 4.2σ + confidence-cut profile (+4.27/+4.11/+4.02 → +0.41/+1.14/+0.51), Table I per-row heterogeneous "Reported statistic" tags, HC selection (winning-class conf>0.6, N=949,584, f_sky=0.4801 with derivation footnote), A_dip<6.8×10⁻³ 95% UL — all deliberate and NOT flagged.

---

## Findings

### P4-E1 (Editorial) — Bandpower-bin language vs ℓ=1 "single-multipole bin"
In Appendix A.c (tex L506; PDF p.14) the bin spec is "single-multipole linear bin (nmt.NmtBin.from_lmax_linear(lmax=191, nlb=1))" and Appendix A.b explicitly labels the headline as "the *single-multipole bin* from ℓ=1 to ℓ=1 …, ℓ=1 row of the bandpower matrix, NOT a bandpower over a range." The header sentence Appendix A.b is precise; recommend a single explicit cross-reference from the Table III caption ("Band 1 is the single mode ℓ=1 decoupled within the full 39-band coupling matrix") to Appendix A.b so a reader scanning Table III immediately sees that "Band 1" ≠ a ≥1-multipole bandpower. Mechanical (1 sentence). No physics impact.

### P4-E2 (Editorial) — "axis-averaged" vs "θ-uniform" — clarify which polar convention is the falsification grid
The injection axis-protocol sentence (§VI.A, tex L443; PDF p.11/Table V caption) does state "polar angle θ ~ U(0,π) … uniform in polar angle, which mildly over-weights near-polar axes relative to an area-uniform draw" and reports a fixed-axis spot check (0.54 vs 0.55 area- vs θ-uniform). That is the cleanest version yet and satisfies the R24conf "injection-scorer convention sentence" ask. One minor improvement: in §VII.e ("Sensitivity convention and falsification criterion"), the operational statement "A_50 and A_95 are floors of the *real-space dipole estimator* under its per-pixel-shuffle null" should add the parenthetical "(θ-uniform axis-averaging; cf. §VI.A spot check)" so the §VII boundary inherits the convention spelled out in §VI.A without backreference. Pure mechanical clarification.

### P4-m1 (minor) — Catalog A row in Table I has em-dashes in the N_map weighted column but row (iv) has 8,474,531; readers may briefly read row (i) as f_sky-only
Row (i) "real-space dipole (HC)" prints `N_catalog spiral = 949,584` and `N_map weighted = ---`, then `f_sky = 0.4801` with the long footnote-a. This is correct (the real-space HC dipole does not pass through a NaMaster mask-weighted construction; only the apod. MASTER row does), but it leans on the reader to notice that rows (i)/(v)/(vi)/(vii) reuse the canonical mask construction while row (iv) is the only mask-weighted row. Recommend a half-sentence in the Table I header note: "`—` in `N_map weighted` indicates rows where the NaMaster weight construction is not invoked." Improves table-as-island readability.

### P4-m2 (minor) — `A_dip = 6.8×10⁻³` UL phrasing in PDF p.7 vs §VII.e
PDF p.7 sentence: "max(A_obs, A_95^UL) coincides with it since A_obs < A_95^UL, gives A_95^UL = 6.8×10⁻³ in A_p units (null {50,68,90,95,99}% quantiles = {3.5,4.4,6.0,6.8,8.4}×10⁻³)". This is the *rank* (estimator-level) UL on the pixel-permutation null amplitude — a different object from the injection-recovery A_95 ∈ (1.0%,1.5%] of Table V. The paper already labels each correctly in context ("an estimator-level rank construction, not a signal-injected limit"). One minor improvement: in the abstract, the phrase "injection–recovery brackets A_95 between 1.0% and 1.5% (A_50 ≈ 0.75%)" could append "(injection-based; the estimator-level rank UL on the observed null, A_95^UL = 6.8×10⁻³ in A_p, is reported in §IV.C and is a distinct object)" — purely to forestall the predictable reviewer conflation. Optional.

### P4-m3 (minor) — Equal-area slab claim cross-reference
§IV.B (tex L297; PDF p.6) reports "An equal-*area* partition (8 declination bands of equal in-mask pixel count on the canonical mask) gives the same verdict: per-band f_CW deviations from 0.5 reach at most 0.49% on the full spiral sample (max |z|=2.9 vs. the global rate) and 0.56% on the HC subsample (max |z|=1.4), comparable to the equal-count maximum of 0.46% (artifact c12_r24conf_local_batch.json)." This closes the R24conf "equal-area slab" ask cleanly and is consistent with the global f_CW-deviation magnitude. No issue. Suggest adding `\label{eq:equal_area_check}` for cross-link discipline but no scientific concern.

### P4-N1 (Nice-to-have) — Table III empirical-rank computation
Table III caption (p.10) states `p = (k+1)/(N+1)` with `k=5 of N=10⁴` giving 6/10001 = 6.0×10⁻⁴, and `minimum reportable p is 1/(N+1) ≈ 1.0×10⁻⁴`. Verified arithmetic. The heavy-tailed disclaimer at low ℓ ("permutation null is heavy-tailed relative to Gaussian at low ℓ") is correctly attached. No action.

### P4-N2 (Nice-to-have) — Appendix B "low-ℓ real-Y_ℓm regression" supplement
Appendix B.d (tex L544; PDF p.15) "a low-ℓ real-Y_ℓm regression (ℓ≤3, 16 coefficients) of the headline HC A_p map against a 2000-permutation pixel null finds all three ℓ=1 coefficients consistent with zero (|z|≤1.25); the only outlying coefficient is at (ℓ,m)=(3,−1) (z=−4.4)." Coefficient count check: (ℓ=0:1) + (ℓ=1:3) + (ℓ=2:5) + (ℓ=3:7) = 16 ✓. The (3,-1) outlier being attributed to coherent low-ℓ systematic structure (Appendix D) is the correct cross-reference. Clean.

### P4-N3 (Nice-to-have) — Coupling-matrix conditioning disclosure (Appendix A.c)
"the full 192×192 spin-0 matrix has condition number 3.17 at the 2° apodization used here (3.11/3.25 at 1°/3°), the leading ℓ≤5 block has condition number 2.49, and the ℓ=1 row is diagonally dominant (M_11 / Σ_{ℓ'≠1} |M_{1ℓ'}| = 1.29)". This satisfies the R24conf coupling-conditioning request. Strong.

---

## Explicit all-clears (with arithmetic)

- **Catalog totals**: 1,592,107 + 1,609,053 + 5,273,371 = **8,474,531** ✓; CW+CCW = **3,201,160** ✓; NS frac = 62.226% (paper 62.23%) ✓.
- **Catalog C f_CW = 1,592,107 / 3,201,160 = 0.4973531** → 0.4974 (paper 0.4974, 0.497353) ✓; per-pixel binomial σ = √(f(1-f)/N) = 2.79×10⁻⁴ → table row "0.497353(279)" ✓; dev z = -9.47 ✓ (matches "−9.47" / "9.5σ").
- **Asymmetry A = 2(f_CW − 0.5)**: Catalog A 0.507879 → A = +1.5758% → matches "raw +1.576%" ✓; Catalog C 0.497353 → A = −0.5294% → matches "equivariant −0.529%" ✓; suppression factor 1.576/0.529 = 2.98× ✓.
- **f_sky HC footnote-a**: 23,600 / 49,152 = 0.4801432 → 0.4801 ✓.
- **Table III ℓ=1 (apod)**: z = (24.74−1.93)×10⁻⁶ / 3.12×10⁻⁶ = 7.311 → +7.31 ✓; rank p = 6.0×10⁻⁴ from k=5, N=10⁴ → (5+1)/(10⁴+1) = 5.9994×10⁻⁴ ✓.
- **Table IV monopole-only reproduction**: data 1.6961×10⁻² ; null mean 1.6846×10⁻² → ratio 0.99322 → "99.32%" ✓; residual z = (1.6961−1.6846)/0.0068 = +1.69 ✓.
- **N_map weighted / N_spiral = 8,474,531 / 3,201,160 = 2.6473** → ~62% NS-overcount ratio ✓; consistent with the Sec. IV C text "exceeds N_catalog,spiral because each W_p includes non-spiral objects (∼62% of the catalog)".
- **Gaussian-equivalent σ ≈ 1.9 for canonical MASTER ℓ=1**: paper notes p_MC = 15/500 = 0.030 → two-sided ~1.88σ → matches abstract "≈1.9σ Gaussian-equivalent" ✓.
- **Catalog A header → Cat A row σ in Table II**: f_CW = 0.507879, N = 3,321,795 → σ_dev = (0.507879-0.5)/√(0.507879·0.492121/3321795) = 28.72σ → matches +28.72 ✓.
- **Suppression ratio 0.79% raw → 2.31σ vs 6.48σ**: text "classifier CW excess of only 0.79%, combined with non-uniform sky coverage, produces highly significant but entirely spurious dipole signals" is internally consistent (0.788% f_CW-deviation = 1.576% A units; 2.98× collapse to 0.265%/−0.529%) ✓.
- **Abstract ↔ body ↔ Table I consistency** for the headline +0.41σ / p=0.31 / 10⁴ realizations / N≈9.5×10⁵ at conf>0.6: matches §IV.C and Table I row (i) exactly ✓.
- **Abstract A_dip < 6.8×10⁻³ 95% UL** is from the c12 artifact and is the estimator-level rank UL — labeled clearly in §IV.C ✓ (calibration set respected).
- **Confidence-cut sweep** 0/0.4/0.5 → +4.3/+4.1/+4.0 collapsing at ≥0.6 → +0.41/+1.14/+0.51: matches Table-1-style narrative and is consistent with PDF p.8 / the "calibration set" deliberate disclosure ✓.
- **Falsification criterion ≥5σ at A ≳ A_95 at ≥10⁷ galaxies** is internally consistent across abstract / §VI.A / §VII.e ✓.
- **Withdrawal of subsample-mask null (Appendix A.d)** — provenance audit trail (n=5,547,858; f_sky=0.659; synthetic catalog) clearly disclosed, and the headline real-space null is shown to predate the audit (v1.0.76) so the primacy is preserved. Calibration set respected ✓.

---

## Pass-2 self-critique

- I considered flagging the "axis-averaged" vs "fixed-axis" distinction in §VI.A and Table V caption, but the text already carries an explicit area-uniform vs θ-uniform spot check and a verbal disclaimer; the only remaining gap is a §VII.e back-reference (P4-E2), which I kept as Editorial, not Minor.
- I considered whether the abstract's "robust under a per-galaxy label-shuffle null, z=0.70" needs to mention the independent-implementation provenance (since the text has two label-shuffle z values: 0.58 and 0.70). It does not: 0.70 is the independent re-implementation and is the more conservative robustness anchor — choosing it for the abstract is defensible.
- I considered whether the +0.41σ headline + +7.28σ apod-MASTER reading can be misread as inconsistent. The §IV.C "not on the same statistical footing … harmonic-completeness check projects a Shamir-class real-space dipole through MASTER at z≈68–218 vs. observed +7.28σ" sentence is the right defense. Confirmed no finding needed.
- I considered whether the §V.A Shamir comparison ("our maximum regional asymmetry is 0.32%") is a precise statement. It is (matches the slab and quadrant ranges) and is appropriately qualified ("not a frequentist exclusion … requires a matched-footprint Ganalyzer reanalysis").
- I considered whether the "withdrawn subsample-mask null" treatment is sufficient. The audit log + the threshold-sweep that no real-catalog predicate reproduces f_sky=0.659 + the explicit cataloging in repository README + the v1.0.76 primacy date is a strong provenance package. No finding.
- I considered the abstract's "≈ 1.9σ Gaussian-equivalent" canonical MASTER claim. p_MC = 15/500 = 0.030 → two-sided Gaussian z = 1.88; abstract rounds to 1.9. OK.
- I considered the 6.8×10⁻³ UL appearing in both the §IV.C estimator-level rank construction AND the abstract: the abstract phrasing is "A_dip ≲ 6.8×10⁻³ 95% UL from the c12 artifact" per the calibration set — deliberate. Not flagged. (P4-m2 is an optional preemptive disambiguation, kept as minor.)
- I considered whether Table V's `A=0.75%, P(σ>3)=0.55` ↔ `A_50 ≈ 0.75%` ↔ §VII.e is consistent. It is: 0.55 ≈ 50%-recovery; A_50 is operationally defined at this 0.55 point. Clean.

---

## Summary recommendation

**Verdict: Accept (clean-round 2-of-2)** — *minor mechanical edits only; no scientific or methodological revision required.*

This is the cleanest revision of P4 I have seen across the R-round arc. The R24conf-edited regions (§V.B robustness checks, §VI axis-protocol + θ-uniform vs area-uniform spot check, Table I per-row heterogeneous tags + footnotes, equal-area slab partition cross-check, Y_ℓm low-ℓ regression supplement in Appendix B.d, Appendix A.c coupling-matrix conditioning numbers) all close cleanly. Abstract ↔ body ↔ Table I ↔ Table II ↔ Table III ↔ Table IV consistency holds at every recomputable number I checked. The deliberate disclosures (0.43→0.41σ regen, generator-defect, unthresholded 4.2σ + conf-cut profile, withdrawn subsample-mask null) are all clearly framed as systematics-attribution / provenance items, not retractions of headline science. Remaining items are 2 Editorial cross-reference suggestions and 3 Minor table/abstract polish notes; none touch a scientific claim.

**Counts**: E=2 / M=0 / m=3 / N=3 / BLOCKER=0.

Path: clean-round 2-of-2 → proceed to Houston sign-off / arXiv.
