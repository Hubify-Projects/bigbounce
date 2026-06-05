# P4 auto-2026-06-05_1617pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (17237 chars)
**Wall time**: 448.3s

---

# Referee Report — P4

**Manuscript:** Survey-Scale Galaxy Chirality with Equivariant TTA …
**Pages:** 10
**Target journal:** Physical Review D

I have read the full PDF, audited every load-bearing number in the abstract, recomputed table arithmetic, and checked the cited literature against quoted statistics. My honest assessment follows.

---

## ESSENTIAL FINDINGS (paper cannot be accepted without these)

### P4-E1. Title contains a numerical result ("−0.122σ")
**Front matter, page 1.** The title literally encodes the headline σ value and the leakage-amplitude qualifier. PRD titles do not embed transient pipeline-specific significance figures. Quoting "−0.122σ" in the title implies (a) the value is robust across reasonable pipeline choices (the body shows it is one of several mutually inconsistent σ values from different nulls), and (b) the precision is meaningful at three significant figures (it is not — 500 MC realizations give a finite-sample σ-of-σ comparable to the digit).
**Fix:** Rewrite to a conventional descriptive title, e.g. "An equivariance-corrected null dipole search for galaxy chirality on the DESI Legacy footprint." Remove all σ values and the multi-clause subtitle.

### P4-E2. Table II arithmetic does not reproduce
Catalog A: 0.5079 vs 0.5000 with σ=0.000279 →
 |0.0079|/0.000279 = **28.32σ**, paper reports **28.8σ**.
Catalog B: 0.504 → 0.004/0.000279 = **14.34σ**, paper reports **14.6σ**.
Catalog C: 0.4974 → 0.0026/0.000279 = **9.32σ**, paper reports **9.5σ** (this value is reused in the abstract, §IV B, §IV D, §VI, §VII, and the Data Availability statement).
All three column-3 deviations are inflated by ~2–3% relative to the displayed σ in column 2. The 9.5σ monopole anchor is load-bearing for the entire interpretation of the +3.64σ canonical-mask residual.
**Fix:** Recompute, correct every downstream sentence, and state which uncertainty (binomial-only, or binomial + classifier covariance) is used.

### P4-E3. "Five-anchor" analysis lists six anchors
§IV E and §VII reference a "five-anchor systematic analysis" but the parenthesized list in §IV D reads "(cross-spectrum, leg-proxy, density-stratified, boundary-distance, full-catalog injection, block-bootstrap WLS fit)" — six items. Appendix D documents six items (a)–(g) (apodized, multipole, leg-proxy, density-stratified, boundary-distance, joint WLS). The count is internally inconsistent and the "full-catalog injection" anchor named in the body is not actually documented as a numbered sub-section of Appendix D.
**Fix:** Reconcile the count or list each anchor explicitly. Add the missing "full-catalog injection" subsection to Appendix D or remove it from the body.

### P4-E4. Catalog has no independent ground truth at the precision claimed
Two facts must be juxtaposed:
- "67.6% of training labels derive from CE-ResNet predictions" (page 3).
- "The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91% (Cohen's κ = 0.40)" (page 3).
A 69.91% binary-chirality agreement on the only independent label set is poor (κ = 0.40 is "fair-to-moderate," not "high-confidence"). The catalog is then used to claim a sub-percent sensitivity floor and to falsify Shamir's 2–4σ class. The dilution-factor argument (g = 2a−1 ≈ 0.40) is mentioned only in §VI A, where the authors quietly admit the true-underlying sensitivity is ~1.88%, not 0.75%. The abstract and §VII claim a "factor of ~6–12" exclusion of Shamir's 3% class — using the dilution-corrected floor that factor collapses to roughly 1.5–2 and is consistent with no exclusion at all.
**Fix:** Either (a) revise the abstract and conclusions to quote the dilution-corrected sensitivity floor, or (b) demonstrate (with a held-out, non-CE-ResNet, non-GZ1 label set) that the catalog actually meets the precision needed to discriminate the Shamir signal at the amplitude claimed.

### P4-E5. T1 "Flip-swap r = 1.000" is tautological under TTA
Table V reports T1 (flip-swap consistency) = 1.000 against threshold 0.80. Catalog C is constructed by averaging the original prediction with the flip prediction (Eq. 2). By construction, the flip-swap correlation of the *equivariant* probabilities is identically 1. Reporting this as a passed bias test is circular. The reader has no way to distinguish "test passes because equivariance was enforced" from "underlying classifier was equivariant."
**Fix:** Quote T1 on the *pre-TTA* classifier (Catalog A) so the test is non-trivial; or remove the T1 row from Table V.

### P4-E6. No figures in a 10-page paper analyzing sky maps and angular power spectra
The paper claims "spatial uniformity (all 7 equatorial coordinate slabs within 0.5% of 50/50; available in the companion data repository)" (page 4) but no sky map is shown. There is no figure of the asymmetry map, no plot of pseudo-Cℓ vs ℓ, no injection-recovery curve, no figure of the canonical mask, and no figure illustrating the leg-stratified ℓ=1 partial closure. For a PRD methods paper whose central claim is a leakage channel revealed by survey geometry, this is unacceptable. The figures cannot be off-loaded to a HuggingFace repository.
**Fix:** Add at minimum (i) the canonical mask + asymmetry map, (ii) MASTER-deconvolved Cℓ vs ℓ with null band, (iii) the injection-recovery curve underlying the A ≈ 0.75% claim, and (iv) the monopole-only null distribution overlaid on the data.

### P4-E7. PACS codes are deprecated; PRD has not accepted PACS since 2015
The front matter lists "PACS numbers: 98.80.-k, 98.62.Ai, 95.75.Mn." PRD uses PhySH terms now.
**Fix:** Replace with PhySH descriptors or remove.

---

## MAJOR FINDINGS

### P4-M1. The interpretive load on the +3.64σ canonical-mask residual is excessive
The paper enumerates three interpretations (clean dipole at 1.7%, depth/morphology systematic, NaMaster deconvolution artifact). Interpretation (ii) is selected. But:
- The generative monopole-only null (§IV D) reproduces 99.3% of the *pre*-MASTER power. The body silently transitions to claiming this also explains the *post*-MASTER +3.64σ ("non-headline, systematics-attributed value consistent with residual mode-coupling"). These are not the same statement. A monopole-only null that reproduces pre-MASTER leakage does not, by itself, explain a post-MASTER residual that has, by construction, had the dominant monopole-coupling channel removed.
- The WLS posterior z = −264.5 in Appendix D for the dipole interpretation is reported with a straight face, then deflated to z ≈ −18.1 after block bootstrap. The 14.7× bootstrap inflation is itself a sign that the WLS covariance is wildly under-estimating spatial correlations — the result should not be quoted at three-digit precision in either form.
- The cross-spectrum r(Ap × ntotal) = −0.65 at ℓ=2 is offered as the smoking gun, but ℓ=2 ≠ ℓ=1 and the paper does not show a directly analogous ℓ=1 cross-spectrum.
**Fix:** Either present a fully quantitative model of the depth/morphology systematic that *predicts* the +3.64σ residual amplitude (not merely "is consistent with" it), or label this residual as unexplained.

### P4-M2. Sensitivity floor derived on HC subsample, applied to full sample
§VI A: "The empirical injection-recovery sweep on the HC-spiral subsample (N = 471,049, …) gives P(σ>3) = 0.55 at A=0.75%." The threshold is then quoted throughout the paper, including the falsification criterion in the abstract, as if it applied to the full 3.2M catalog. The HC subsample has different purity, different noise covariance, and a different per-pixel count distribution.
**Fix:** Repeat the injection-recovery on the full Catalog C and report that floor. If the HC sweep was used because the full-sample sweep is intractable, justify this explicitly.

### P4-M3. Comparison with Shamir is rhetorically asymmetric
The abstract and §VII claim Shamir's signal is disfavored "by a factor of ~6–12 under the present pipeline." §V A then explicitly states "We do not claim a frequentist exclusion of Shamir's Ganalyzer estimator: a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis." These two statements cannot both stand. The abstract should match the §V A caveat. As written, the abstract substantially overclaims.
**Fix:** Soften abstract to "amplitude-level inconsistency under the present pipeline; a Ganalyzer matched-footprint reanalysis is required for a likelihood-level exclusion." Remove "factor of 6–12" or qualify it.

### P4-M4. Land et al. (2008) [11] not discussed despite direct relevance
Reference [11] is the GZ1 spin-statistics paper that established the existence of a human-handedness bias in CW/CCW vote counts. The present catalog inherits its training labels from GZ1 → CE-ResNet → this paper. The 0.26% residual CW excess (9.3σ, not 9.5σ — see P4-E2) is plausibly the propagated GZ1 visual-handedness systematic. The paper cites Hayes, Davis & Silva 2017 [24] ("On the nature and correction of the spurious winding bias in Galaxy Zoo 1") but does not discuss it. This is the literature anchor for the entire monopole offset and it is silently bypassed.
**Fix:** Add a paragraph in §IV B or §VI relating the 0.26% monopole to refs [11] and [24] and explaining why a correction at the level of those works was or was not applied.

### P4-M5. The 99.3% reproduction claim is overstated as a "headline finding"
§VII a calls the leakage channel the "headline finding." But (a) mask-coupled monopole leakage at low ℓ is a textbook CMB analysis result, (b) the abstract simultaneously declares the −0.122σ null to be the "primary scientific result," and (c) the abstract subtitle calls the leakage channel "quantifiable" — a non-claim. Pick one headline and defend it; the paper currently asserts two.

### P4-M6. ℓ=1 single-mode estimator vs bandpower description
Table III row 1 reports the ℓ=1 single-mode value at fsky = 0.659 (subsample). Rows 2–5 are ℓ=4, 9, 14, … bandpowers at fsky = 0.491 (canonical). Mixing two masks in one table makes the column comparisons meaningless. The χ²/dof = 161.2/38 = 4.24 is presumably computed across rows of *one* mask, but the table mixes both.
**Fix:** Separate into two tables, or label each row with its mask and footnote that rows are not jointly fit.

### P4-M7. Bias-hardening test thresholds are arbitrary and weakly motivated
Appendix B states acceptance thresholds (r>0.80, >80% agreement, etc.) are "generous relative to the 0.75% empirical sensitivity floor" but does not derive that statement. T1=1.000 (tautological — see P4-E5), T6 "<10%" with actual <0.4% — these tests are designed to pass.
**Fix:** Either derive each threshold from a precision-target argument, or label the suite "necessary but loose sanity checks" and de-emphasize.

### P4-M8. Bibliography ordering / numbering pathology
Reference [4] is Shamir 2012; ref [1] is Shamir 2020; ref [3] is Shamir 2022 (MNRAS); ref [2] is Shamir 2022 (PASJ). Citations in text appear in order [4], [1], [3], [5], [6], [7] — non-monotonic. PRD permits citation-order-of-appearance numbering; if alphabetical-by-author is intended, the numbering is inconsistent.
**Fix:** Reorder references to citation order of appearance or fix the in-text citation labels.

---

## MINOR FINDINGS

### P4-N1. "p_LEE ≤ 10⁻⁴" is uninformative
Table I row (iv) lists "p_LEE ≤ 10⁻⁴" with NMC = 10,000 (page 8). With 10,000 trials a non-occurrence gives p ≤ 1/10001, which to one sig fig is ≤10⁻⁴. This is a Wilson-rule-of-three statement, not a measurement. Quote the actual outcome (zero occurrences in 10,000) or expand the MC.

### P4-N2. "monopole-mask" hyphenation is inconsistent
Throughout: "monopole-mask," "monopole+mask," "monopole-only," "monopole-leakage." Pick one.

### P4-N3. "post-MASTER ℓ=1" vs "MASTER-deconvolved single-mode pseudo-C1" — the paper uses ≥4 names for the same estimator across §III A, §IV C, Appendix A.

### P4-N4. The abstract is 530 words. PRD prefers ≤250.

### P4-N5. Equation (1) is not really an equation
The classification head is written as a one-line "Eq. (1)" combining a layer description with a softmax label. It is a textual diagram, not an equation. Either typeset as a code/architecture box or remove the equation number.

### P4-N6. "1.6× CE-ResNet's scale"
3,201,160 / 1,950,000 = 1.642. OK, but earlier abstract phrases (3.2 M spirals vs 1.95 M) should be made consistent in both abstract and §I.

### P4-N7. "1.27 × 10⁵ SDSS galaxies" for Shamir 2012
The cited Shamir 2012 used ~126,501 galaxies, so 1.27×10⁵ is fine. OK.

### P4-N8. "DECaLS +4.50σ" for the [0.5, 0.6) confidence bin (Appendix C)
This 4.5σ cell-level result deserves a paragraph in the main body, not a buried sentence in Appendix C, especially because the family-corrected p (0.0086, ≈2.4σ) is still nontrivial.

### P4-N9. "30× extension" of Iye et al. (2021)
Iye et al. analyzed ~10⁶ galaxies; 3.2×10⁶ / 10⁶ ≈ 3×, not 30×. Recheck.

### P4-N10. Acknowledgments declare LLM-assisted manuscript editing
Acceptable under PRD policy but should also include a statement of human verification of all numerical results.

### P4-N11. "Galaxy Zoo DESI predictions catalog [9]" cross-match
The cross-match procedure (§II A) is not documented in detail. What matching radius? What handling of duplicates?

### P4-N12. Catalog A → C transition reported only as bulk fractions
The flow of probabilities from A to B (Platt) to C (TTA) is described in §III D in 3 sentences. For reproducibility, this needs a small table per-tier (or appendix).

### P4-N13. The two equivariant probability formulas (Eq. 2) sum to 1 only if the unflipped P_NS equals the flipped P_NS in expectation. State this assumption.

### P4-N14. "Bonferroni/BH across ~650 directions" — the ~650 number is not derived.
The hemisphere grid is described as "10° increments" — at full sphere coverage this is 10⁴ patches, not 650. State the actual grid (HEALPix NSIDE_dir = 8 → 768 pixels; antipodally identified → 384). Get the number right.

### P4-N15. Appendix D "Block-bootstrap at NSIDE = 8 (N_boot = 1000) inflates σ(A_dipole) by 14.7×, reducing z to ≈ −18.1"
14.7× inflation of σ is a huge effect that says the WLS error bars are radically wrong. The reader needs to know which result to trust. Quote only the block-bootstrap result; relegate the naive WLS to a footnote.

### P4-N16. "GZ1 dilution factor g = 2a − 1 ≈ 0.398 for a = 0.6991"
2(0.6991) − 1 = 0.3982. OK.

### P4-N17. The catalog release "Release tag: v2026.04" implies pre-publication versioning to come.
State the version under review explicitly.

---

## OTHER STRUCTURAL OBSERVATIONS

- **Length vs content:** This is a null result whose main scientific novelty is methodological (TTA-corrected catalog + a worked example of mask-coupled monopole leakage). 10 pages is at the upper end of what is justified. With the figures requested in P4-E6, it will grow to 12–13 pages. Recommend trimming Appendices C and D by ~30% (much of the prose is restated body-text material).
- **σ-comparability disclaimer:** The paper includes the disclaimer "σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators" once in the abstract and once in §IV. Good. However, the abstract then juxtaposes −0.122σ, +0.43σ, +3.64σ, and "factor of 6–12" exclusion within four sentences without re-iterating the disclaimer. A reader scanning the abstract will compare them. Move the disclaimer to immediately precede the σ enumeration.

---

## Summary recommendation

**REJECT** (resubmit allowed after major rework).

The paper contains real intellectual content — a carefully constructed TTA-corrected chirality catalog, an honest null at sub-percent sensitivity, and a useful pedagogical demonstration that monopole×mask coupling can mimic a low-ℓ dipole in chirality catalogs — and that material is publishable. But in its current form the manuscript fails PRD's "earned-by-the-evidence" bar: the title contains a transient pipeline-specific σ value, Table II arithmetic is wrong and the corrupted 9.5σ propagates throughout the interpretation, the paper has no figures despite analyzing sky maps and angular power spectra, the bias-hardening suite contains a tautological test, the "5-anchor" claim is six anchors, the catalog rests on training labels that are 67.6% CE-ResNet pseudo-labels with only κ = 0.40 agreement against the only independent set, and the abstract overclaims the Shamir exclusion that §V A explicitly disclaims. The interpretive load placed on the +3.64σ canonical-mask residual is also disproportionate to the systematics-modeling evidence. After (i) correcting the arithmetic, (ii) adding figures, (iii) running the injection-recovery on the full sample, (iv) softening the Shamir-exclusion language to match §V A, and (v) addressing the relationship to refs [11] and [24] on GZ1 handedness bias, the paper could plausibly meet PRD's bar at major-revision review.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P4 (Second Pass)

Below are findings from a closer audit focused on arithmetic, internal consistency, and σ-comparability. These are NEW findings not in the initial report.

---

## ESSENTIAL FINDINGS (additional)

### P4-E8. The "+3.64σ" canonical-mask residual is a moment-ratio, not a Gaussian-equivalent σ — actual significance is ≈1.9σ
The abstract states: "+3.64σ (z = Δ/σ_null moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent)". The Gaussian-equivalent of pMC = 15/500 = 0.030 is Φ⁻¹(0.970) = 1.88σ. The "3.64" is the ratio Δ/σ_null when σ_null is the second central moment of a non-Gaussian null with a heavy upper tail.

Yet *every* downstream use in the paper — the title clause, the abstract, §IV D, §IV E, Table I row (iii), Appendix A, Appendix D, §VII a, §VII b — quotes "+3.64σ" without the Gaussian-equivalent qualifier. The systematic is being reported with an inflation factor of ≈1.9× relative to its actual rejection power. The "five-anchor systematic battery" is then deployed to "explain" a 1.9σ effect (empirical, properly rank-based), which is barely a 2σ fluctuation under the very null the paper constructed.

This propagates into the abstract's structural framing: a "diagnostic evidence for a … residual" is much weaker if the residual is 1.9σ rather than 3.64σ. The entire interpretive infrastructure of Appendix D is built around explaining a 3.64σ excess that, on the paper's own null, is only ~2σ.
**Fix:** Replace "+3.64σ" with "pMC = 0.030 (1.9σ Gaussian-equivalent)" or analogous text everywhere it appears. Re-frame Appendix D and §IV D accordingly. Reconsider whether a 5-or-6-anchor systematic battery is warranted to "explain" a 2σ fluctuation.

### P4-E9. Training-set arithmetic does not close
§II B itemizes:
- GZ1: 6,637 galaxies
- CE-ResNet: 17,153 galaxies  
- Synthetic hard negatives: 2,000 images
- **Sum: 25,790**
- **Stated total: 26,636**
- **Discrepancy: 846 unaccounted images.**

Then "67.6% of training labels derive from CE-ResNet predictions":
- 17,153 / 25,790 = 66.5%
- 17,153 / 26,636 = 64.4%
- 17,153 / 24,636 (excluding synthetic) = 69.6%
- *None* equals 67.6%.

The 67.6% figure is then invoked to motivate the GZ1 cross-match "conservative accuracy floor" (Sec. II B → Sec. IV C) which sets the entire isotropy-bound chain. Stale or wrong.
**Fix:** Reconcile the component counts with the total, and recompute the CE-ResNet-derived label fraction.

### P4-E10. "+2.05% → −0.53%" raw-to-equivariant suppression in §IV B is inconsistent with Table II
§IV B says: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%."
Table II reports: Catalog A excess +0.79%, Catalog C excess −0.26%.
- 2.05/0.53 = 3.87 ✓ (consistent within itself)
- 0.79/0.26 = 3.04 (from Table II)
- The text's 2.05% and 0.53% numbers do not appear anywhere else in the paper and do not match Table II under any obvious definition (CW/CCW, 2(f−0.5), (CW−CCW)/CCW, etc.).

Either §IV B uses stale numbers from an earlier pipeline version, or a different definition of "asymmetry" that is not stated. The "3.86× suppression" claim is one of the paper's three demonstrations that equivariant TTA works; it cannot rest on un-derivable numbers.
**Fix:** State the definition of asymmetry used, recompute from current Catalog A/C, and reconcile with Table II.

### P4-E11. Major orphan-citation problem in the bibliography
The references list contains 39 entries. A scan of the body text shows that the following references are NEVER cited in the main text or appendices:
- [11] Land et al. (GZ1 spin statistics) — directly relevant background, not cited
- [13] Gross & Vitells (LEE) — LEE used in §IV E without this cite
- [14] SpArcFiRe (Davis & Hayes)
- [15] Motloch et al.
- [16] Lue, Wang & Kamionkowski (parity-violating interactions)
- [17] Cabass, Ivanov & Philcox
- [18] Philcox BOSS
- [19] Eskilt & Komatsu
- [20] Eskilt Cosmoglobe
- [21] Hou et al.
- [22] Cahn, Slepian & Hou
- [23] Komatsu
- [24] Hayes, Davis & Silva (GZ1 winding bias) — directly relevant, not cited
- [25] Bamford et al.
- [26] Hart et al.
- [27] Walmsley DECaLS
- [28] Yu et al.
- [29] DESI Collaboration design paper
- [30] LSST Ivezić et al.

That is **19 of 39 references** with no in-text citation. PRD requires all bibliography entries to be cited; orphan citations will be flagged at copy-editing. Many of these (e.g., [11], [13], [24]) *should* be cited and their absence is substantive (the LEE-without-Gross&Vitells case in particular).
**Fix:** Either cite each bibliography entry in text or remove from the list. Especially: cite [11], [13], [24] where they are scientifically required.

---

## MAJOR FINDINGS (additional)

### P4-M9. Table III ℓ_eff = 4 row shows MASTER is NOT removing the canonical-mask leakage
Table III gives a canonical-mask, post-MASTER bandpower at ℓ_eff = 4 (ℓ ∈ [2,6]) of **+6.097σ**, larger than the ℓ = 1 single-mode value of +3.64σ. The label column says "Mask-coupled monopole leakage." But the entire abstract and §IV D narrative is that **MASTER deconvolution removes this leakage**:
- Abstract: "MASTER mode-coupling deconvolution removes the leakage."
- §IV D: "MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage."

These statements are true only of the subsample mask, not the canonical mask. On the canonical mask Table III shows that the leakage *survives* MASTER deconvolution at substantial significance (+6.1σ at ℓ_eff = 4, +2.2 to +2.6σ at ℓ_eff = 9, 14, 19, 24). The natural reading of the abstract — that MASTER removes the leakage in general — is contradicted by the paper's own table.

This is methodologically important: a 5-row stretch of low-ℓ MASTER bandpowers all showing |σ| > 2 on a mask the authors call "patchy" indicates MASTER is not adequately conditioned for this footprint geometry. The headline "MASTER removes the leakage" should be replaced with "MASTER removes the leakage on the apodizable subsample mask but does NOT remove it on the canonical mask."
**Fix:** Add this caveat to the abstract and §IV D. Discuss whether the residual broadband structure indicates the canonical mask is unsuitable for MASTER at low ℓ at all.

### P4-M10. Table IV z-value arithmetic does not match displayed precision
Row 1 (pre-MASTER pseudo-Cℓ): data 1.696×10⁻², null (1.685±0.007)×10⁻²:
(1.696 − 1.685)/0.007 = 0.011/0.007 = **1.571**, but table reports **+1.68**.
(For the table value to be correct, σ_null would have to be ≈0.00655, not 0.007.)

Row 2 (hemisphere max|A|): data 3.48×10⁻³, null (1.69±0.41)×10⁻³:
(3.48 − 1.69)/0.41 = 1.79/0.41 = **4.366**, but table reports **+4.42**.

Both z values are inflated by ~5–7%. With only one displayed digit of σ_null, the z-column carries spurious precision. Either (i) round z to one significant figure (~1.6 and ~4.4) or (ii) display σ_null with another digit so the arithmetic closes.

### P4-M11. "Strict-superset subsample mask" terminology inverts the conventional reading
The abstract introduces "the strict-superset subsample mask (n = 5,547,858, fsky = 0.659)." Conventionally "subsample" means a subset; here the "subsample mask" (fsky = 0.659) is a strict **superset** of the "canonical mask" (fsky = 0.49005). The "strict-superset" qualifier flags this in passing but is buried; a reader will not understand what the relationship between the two masks is.

In addition, the "n = 5,547,858" reported in the abstract is N_map_weighted (the depth-weight sum from Table I caption), NOT a spiral count. A reader is likely to interpret n = 5,547,858 as the analysis spiral count, which would conflict with the Catalog C spiral total of 3,201,160 quoted in the same abstract. This is genuinely confusing.
**Fix:** Rename to "broad mask" and "fiducial mask" or similar. State "n_galaxies = 5,547,858 (all classified objects in mask), n_spiral = 3,201,160" so the reader does not conflate them.

### P4-M12. The "factor of ~6–12" Shamir-exclusion claim is internally inconsistent
The abstract says: "inconsistent in amplitude with Shamir's claimed ~3% signal by a factor of ~6–12 under the present pipeline." Three threshold candidates appear in the paper:
- Empirical 50%-recovery-at-3σ: 0.75% → factor 3%/0.75% = **4×**
- Fisher Poisson floor at 3σ: 0.29% → factor 3%/0.29% = **10.3×**
- Dilution-corrected (§VI A): 1.88% → factor 3%/1.88% = **1.6×** (effectively no exclusion)

The "6–12×" range matches none of the three cleanly; it appears to be a blend of "Fisher floor at 3σ" → "Fisher floor at 5σ" (3%/(0.29% × 1.67) ≈ 6×). The choice to quote "6–12×" rather than 4× (the empirical, properly-quoted, headline floor) preferentially uses the Fisher floor that the paper itself acknowledges is unrealistic given GZ1-dilution.
**Fix:** Quote a single defensible exclusion factor consistent with the empirical 0.75% threshold (= 4×), or, if the dilution-corrected 1.88% is the right denominator, quote that instead (no exclusion). The current "6–12×" range is the most generous reading and is the wrong reading.

### P4-M13. Pre-MASTER vs post-MASTER, with and without monopole-subtraction, conflated across §IV D and Appendix A
Appendix A states monopole subtraction *increases* the canonical-mask z from +1.85 to +3.64. So the "+3.64σ" residual is sensitive to whether monopole subtraction is performed at the data-vector construction step. Yet:
- Table IV reports the *pre-MASTER* canonical-mask pseudo-Cℓ at +1.68σ (against the monopole-only null).
- Sec. IV D reports the *post-MASTER* canonical-mask residual at +3.64σ (presumably with monopole subtraction).
- The "99.3% reproduction" claim references the pre-MASTER, pre-subtraction value.

The reader cannot tell which of these is "the" canonical-mask number until reading Appendix A. The same numerical quantity (3.64σ) means different things in different sections, depending on whether monopole subtraction has been applied. This is the central technical point of the paper and deserves a clean step-by-step processing-flow paragraph.

### P4-M14. The Joint χ²/dof = 161.2/38 = 4.24 is reported without a p-value
Bottom row of Table III. χ² = 161.2 with 38 dof has p < 10⁻¹⁵ (massive non-null). This is the strongest single rejection of "no canonical-mask signal" in the paper. Yet it is presented as "4.24" with the prose interpretation "Dominated by mask-coupled monopole" and not discussed in §IV C, §IV D, §IV E, or the conclusions. Either this is a >10σ effect requiring explanation, or the χ² test is inapplicable (e.g., the bandpowers are correlated), in which case the value should not be in the table at all.

Also: the table shows 5 numbered rows but the χ² uses "38 bandpowers." Where are the other 33 rows? Add them or footnote the joint test.

### P4-M15. Apodized-mask fsky = 0.482 vs binary fsky = 0.49005
Appendix D: "C² 2° apodization gives +3.57σ at fsky = 0.482, essentially unchanged from the binary-mask +3.64σ." Apodization should reduce effective sky area, so fsky < 0.49005 is expected. But the paper does not state whether the 3.57σ z-score is computed against the same null distribution as the 3.64σ (it should be a re-MC at the new mask), or against a re-scaled binary-mask null. If the null was not re-run for the apodized mask, the comparison is not meaningful.

---

## MINOR / NUMERICAL FINDINGS (additional)

### P4-N18. "factor of ~6–12" repeated in §VI B "by a factor of ∼6–12" — same overstatement as P4-M12.

### P4-N19. Acknowledgements omit funding statement
Standard PRD requirement. The author appears to be independent (Los Angeles), but a statement to that effect ("This work received no external funding") should be added.

### P4-N20. NSIDE_dir = 8 → 768 directions, antipodal-identified → 384; paper says "~650 directions"
Appendix C says "Bonferroni/BH penalty across ∼650 tested directions." With NSIDE_dir = 8 (Table IV row 2) the antipodal-identified pixel count is 384, not 650. The "~650" matches no obvious HEALPix NSIDE. State the actual NSIDE_dir and pixel count.

### P4-N21. "2-fold flip TTA … flip-swap correlation = 1.000"
The flip-swap correlation of 1.000 is reported with three-decimal precision but it is mathematically exact for the equivariant probabilities (P4-E5). State this is enforced, not measured.

### P4-N22. "The 3.05σ hemisphere signal (Appendix C)" 
Quoted in §VI body text. Appendix C reports "maximum asymmetry 3.05σ" and that pLEE ≤ 10⁻⁴. But Table I row (iv) reports "hemisphere LEE (MC)" σ as "pLEE ≤ 10⁻⁴", not a σ. The 3.05σ figure is the local-max value pre-LEE, which is uninformative without a comparison to the random-direction null distribution. Quote both numbers in Table I row (iv), not just pLEE.

### P4-N23. §IV D "(N = 500, binomial realizations at p_global_CW = 0.4974 on the canonical mask)"
The monopole-only null uses p = 0.4974, the Catalog C global CW fraction. This is the global average. But the leakage channel depends on whether p is uniform across pixels. If the per-pixel p has spatial structure (e.g., depth-correlated, as the paper argues for the residual), then the monopole-only null is *too restrictive* and the 99.3% reproduction is an upper limit on the leakage explanation. State this.

### P4-N24. Appendix B "best checkpoint was at epoch 79" with early-stopping patience 15 and max 80 epochs
Epoch 79 (of 80, with patience 15) means training stopped at the very last epoch without triggering early stopping. Validation loss was still improving. The model was not converged. State whether epoch 79 was selected by validation-best or by max-epoch.

### P4-N25. Mass usage of "≈" vs strict equality
Throughout: "~3%", "~6–12", "~25%", "~10–15%", "≈1.9σ" — paper has heavy reliance on hedged tilde-numbers without confidence intervals. For PRD, each such hedge should either be quantified or labeled "rough."

### P4-N26. Footnote of Table I: "Nmap_weighted exceeds Ncatalog_spiral because Wp includes non-spiral galaxies (~62% of the catalog); each galaxy is counted once."
3,201,160 (spiral) / 8,474,531 (total) = 37.78% spiral; 1 − 0.3778 = 62.22% non-spiral ✓. OK.

### P4-N27. Reference [11] "Land, Slosar, Lintott et al. (2008)" is the *exact* paper that establishes the GZ1 large-scale spin statistics null — the most directly analogous prior result. Not cited in text. (Reiterates P4-M4 + P4-E11.)

### P4-N28. Reference [2] "Shamir (2022) PASJ" is in the bibliography but Shamir's citations in text are "[1, 3, 4]" — meaning [2] is uncited in text. (Same orphan-citation issue as P4-E11.)

### P4-N29. "Mean classification confidence is 0.951, median 0.9997"
Mean substantially below median with high median = strong left tail. This means a non-trivial fraction of objects has confidence < 0.5. State the fraction below 0.5 and 0.9.

### P4-N30. The peq > 0.9 HC subsample of 471,049 is referenced in the abstract
But §IV A and Table II report the unstratified Catalog C of 3,201,160 spirals. The relationship between the 471,049 HC subsample and the 3,201,160 spiral count needs to be stated explicitly (471,049 / 3,201,160 = 14.7%).

### P4-N31. "Iye et al. (2021) [5] re-examined Shamir's SDSS spiral catalog" — paper says "30× extension."
Shamir SDSS catalog ~1.27 × 10⁵; 3.2 × 10⁶ / 1.27 × 10⁵ = **25.2×**, not 30×. (My earlier P4-N9 stated this as "3×" which was wrong; the actual ratio is 25×, still less than 30 but close.) Replace 30× with 25× or "an order of magnitude."

### P4-N32. The paper does not state which version of NaMaster was used for the production analysis ... Wait, Appendix A says "pymaster 2.6." OK, that is stated. Good.

### P4-N33. Appendix B equation (B1) defines a loss with parameter λ = 0.5, but does not state whether the loss is summed or averaged across the dataset, nor whether x̃ᵢ is included once or twice per epoch.

---

## SUMMARY ASSESSMENT (unchanged)

The second-pass findings substantially **strengthen the case for REJECT with major revisions allowed**. In particular:

- **P4-E8** (the +3.64σ is actually ~1.9σ Gaussian-equivalent) is potentially the most consequential issue not raised in my initial review. It re-frames the entire "depth/morphology-correlated canonical-mask residual" central claim: a 1.9σ excess does not need a five-anchor systematic battery and does not warrant the level of attention given to it.
- **P4-M9** (Table III ℓ_eff=4 = +6.097σ contradicts the "MASTER removes leakage" headline) directly undercuts the abstract's headline interpretive claim about MASTER on the canonical mask.
- **P4-E11** (19 of 39 references uncited in text) is an editorial-level deal-breaker for PRD copy-editing, and includes substantively important orphans ([11], [13], [24]) whose absence biases the methodological context the paper presents.
- **P4-E9** and **P4-E10** (training-set arithmetic does not close; raw-to-equivariant ratio uses untraceable numbers) compound P4-E2 to show that the paper's bookkeeping is unreliable at multiple independent points.
- **P4-M12** and **P4-N18** sharpen the abstract overclaim issue (P4-M3) into a specific arithmetic discrepancy that the authors should be able to resolve mechanically.

After full revision addressing both review passes, a publishable null result remains in this material — but the present manuscript is not the publishable version.