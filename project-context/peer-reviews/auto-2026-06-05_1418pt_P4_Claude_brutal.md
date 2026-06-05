# P4 auto-2026-06-05_1418pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13573 chars)
**Wall time**: 407.4s

---

# PRD Referee Report — Paper P4

**Manuscript:** "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null..."

I have read the full PDF carefully, recomputed every load-bearing scalar, and audited the figures, tables, and references. The work is largely an honest null result with useful pipeline-level engineering, but the manuscript suffers from substantial internal inconsistencies, post-hoc systematics interpretation, a circular training-label structure, and a presentation that does not meet PRD's clarity and conciseness bar. Detailed findings follow.

---

## ESSENTIAL findings (must fix before any further consideration)

### P4-E1. Internal numerical contradiction: "0.79%" vs "2.05%" for raw Catalog A asymmetry
- Page 6 (Sec. VI): *"a classifier bias of only 0.79%"* and *"The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%"* (Sec. IV B, page 4).
- Table II (page 4) lists Catalog A excess = **+0.79%**, Catalog C excess = **−0.26%**.
- These are mutually inconsistent. The "2.05% → −0.53%" pair in Sec. IV B contradicts the table by a factor of ~2.6× and ~2× respectively. The 3.86× suppression number is computed from numbers that do not exist anywhere else in the paper.
- **Fix:** reconcile the body text with Table II. State explicitly what metric "+2.05%" and "−0.53%" refer to (e.g., CW/CCW ratio − 1?), and recompute the suppression factor self-consistently.

### P4-E2. Table II σ-deviations are arithmetically wrong
Recomputing with the stated σ_binomial = 0.000279 (which itself checks: √(0.25/3,201,160) = 0.000279 ✓):
- Catalog A: (0.5079 − 0.5)/0.000279 = **28.32σ**; paper claims **28.8σ**.
- Catalog B: 0.004/0.000279 = **14.34σ**; paper claims **14.6σ**.
- Catalog C: 0.0026/0.000279 = **9.32σ**; paper claims **9.5σ** (and the "9.5σ" propagates throughout the body as a load-bearing scalar).
All three are systematically ~2% inflated. Either the binomial uncertainty in the table is wrong, or the σ-deviations are. The "9.5σ" appears in Secs. IV B, IV D, VI, App. C as a headline. Fix the arithmetic and propagate.

### P4-E3. Look-elsewhere correction inconsistent with quoted numbers
Sec. VI (page 6): *"the direct-MC p_LEE ≤ 10⁻⁴ rejection is attributed to the same sub-percent ... systematic"* and App. C: *"the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ."*
- A direct-MC p ≤ 10⁻⁴ with ~650 trials gives a Bonferroni-corrected p ≈ 0.065, i.e. ≈1.85σ Gaussian-equivalent — *not* "<1σ." The claim "<1σ" is arithmetically unsupported.
- Additionally, "pLEE ≤ 10⁻⁴" with N=10,000 random shuffles only means "no shuffle exceeded data," which is a 1-sided p-bound at 10⁻⁴, ~3.7σ — not a measured significance.
- **Fix:** state the actual numerical post-LEE significance, or remove the "<1σ" claim.

### P4-E4. Training labels are 67.6% sourced from CE-ResNet predictions
Sec. II B / page 3: *"67.6% of training labels derive from CE-ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth."*
The independent GZ1 cross-match accuracy is 69.91% with **Cohen's κ = 0.40** — i.e. weak-to-moderate agreement at best on real ground truth. This is acknowledged in the paper, but the consequences are not adequately propagated:
- A κ=0.40 binary classifier is barely better than chance on its primary observable.
- All "bias-hardening" tests in Table V (T1=1.000, T2=94.4%, etc.) are computed on a training distribution that is dominated by another CNN's output. They demonstrate consistency with CE-ResNet, not bias absence.
- The "dilution factor g = 2a−1 = 0.398" treatment in Sec. VI A only addresses the magnitude of an injected dipole, not the possibility of a *correlated* mislabeling pattern shared between CE-ResNet and the present ViT.

**Fix:** the paper must either (a) re-derive the headline σ values using *only* the GZ1-trained subset, or (b) explicitly characterize the covariance of CE-ResNet pseudo-label errors with sky position/depth, or (c) substantially soften the "bias-hardened" framing.

### P4-E5. Title and abstract overload; central claim is a null but is presented as a multi-finding showcase
The title is 48 words long and contains four separate "results," two of which are systematics, plus "ℓ=1" notation in a title. Per PRD norms, the title should communicate the principal physical result. The actual scientific content is one null and one un-explained residual that the authors themselves attribute to systematics. **Fix:** shorten the title to convey the headline null; move systematics language to the abstract.

### P4-E6. The "+3.64σ canonical-mask residual" is interpreted post hoc
The paper reports +3.64σ, then runs a five-anchor "systematic analysis" (App. D) that produces a curated explanation. The discriminators against interpretation (i) (real dipole) are themselves post-hoc:
- App. D(f): "z = −264.5 from the naive WLS posterior" reduced by block-bootstrap to "z ≈ −18.1." Two-orders-of-magnitude shifts in z under a covariance choice are a red flag, not a refutation.
- App. D(c): "summed leg-induced ℓ=1 amplitude is ∼25% of the observed" — i.e. the leg-proxy explains only a quarter of the excess, not the whole.
- App. D(d): density-stratified null gives σ = +3.80 — i.e. *higher* than +3.64, which actually *strengthens* the residual, not weakens it. The paper presents this as supporting the systematic interpretation; it does the opposite.

**Fix:** either properly null the +3.64σ with a forward model that fully reproduces it, or present it as an unresolved anomaly with appropriate caveats and *do not* claim "the most likely explanation is a per-pixel-correlated systematic."

### P4-E7. Single-mode pseudo-Cℓ at ℓ=1 is not a standard estimator and its interpretation is non-trivial
Headline result uses NaMaster with `nlb=1` and reports only ℓ=1. At NSIDE=64, ℓ=1 has 3 independent m-modes and the asymmetry map's ℓ=1 power is a sum of squares of three Gaussian quantities — the null distribution is χ²-like, not Gaussian. The paper reports "−0.122σ" using a 500-MC moment ratio. The procedure conflates a χ² estimator with a Gaussian σ. **Fix:** report the result as a p-value from the empirical MC CDF, and clarify whether the negative sign is meaningful (for a power, it should not be).

---

## MAJOR findings

### P4-M1. Apparent contradiction in significance reporting framework
The abstract states: *"σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators."* The very same abstract then lists three σ values (−0.122, +0.43, +3.64) in adjacent sentences without per-instance restatement of incomparability. Per the review instructions, this requires re-flagging at every juxtaposition; the abstract pairs them three times. Add the qualifier inline.

### P4-M2. References [2], [11], and most of [13]–[28], [30] appear uncited in the body
- [2] L. Shamir, PASJ 74, 1114 (2022) — I cannot find a body citation.
- [11] Land et al. 2008 — same.
- [13] LEE Gross & Vitells — same (despite extensive LEE discussion in App. C).
- [14]–[28], [30] — most appear to be context references with no body citation.
This is a bloated bibliography. **Fix:** either cite each reference where it is used, or remove it. In particular [13] *should* be cited next to the LEE claim.

### P4-M3. Edge-on contamination treated as a footnote despite affecting 65.7% of edge-on objects
App. E states 65.7% of b/a<0.3 systems receive CW/CCW labels rather than NS. The paper claims equivariant averaging "mitigates" this. But for an edge-on disk, the *true* chirality is undetermined from a single image — any nonzero CW or CCW probability is noise. A ~10–15% sample-size dilution claim is offered without a quantitative axis-ratio cross-match. **Fix:** perform the b/a cross-match in this paper, not a future paper.

### P4-M4. ℓ=2 evidence against a dipole is presented as if it were a strong constraint
App. D(b): *"σ_ℓ=1 = +3.63, σ_ℓ=2 = +4.73"* with "ℓ=2 > ℓ=1 broadband structure is incompatible with interpretation (i)." A real cosmological dipole could easily produce ℓ=2 leakage through the same patchy mask. This is not a clean discriminator and should not be presented as one.

### P4-M5. The 99.3% leakage reproduction is overstated
Abstract: *"pre-MASTER raw pseudo-C₁ ... is reproduced at 99.3% of its observed amplitude."*
Table IV: data = 1.696×10⁻², null = (1.685±0.007)×10⁻², z = +1.68. Ratio of means is 1.685/1.696 = 99.35%, so this is a *ratio of means*, not a "reproduction at 99.3% of amplitude." The residual is +1.68σ, which by the paper's own logic could itself be "consistent with leakage" but is also consistent with a small (~0.7%) residual dipole. The "99.3%" framing oversells the leakage interpretation.

### P4-M6. Direct-MC z = (1.696 − 1.685)/0.007 = 1.571, paper says 1.68
Table IV arithmetic: (1.696 − 1.685)/0.007 = 1.571σ, not 1.68. Off by ~7%. Probably comes from more precise underlying numbers, but as displayed the table is inconsistent. **Fix:** display more significant figures or correct the z.

### P4-M7. "1.6× CE-ResNet scale" — true on spirals, misleading on total
CE-ResNet: 1.95M galaxies (which were already spirals). Present work: 8.47M galaxies *but only 3.2M classified as spirals*. So the spiral-scale ratio is 3.2/1.95 = 1.64× ✓; but the abstract phrasing "8.47 million ... 1.6× CE-ResNet's scale" is misleading. Restate as "1.6× spiral coverage."

### P4-M8. "Survey-scale" framing is marketing
Title and Sec. I emphasize "survey-scale," but Galaxy Zoo DESI [9] is already at 8.7M galaxies on the same parent. The novelty here is *chirality classification*, not survey scale. Tone down.

### P4-M9. The cw/ccw=0.998 quote from Jia et al. is presented as a property of the catalog, not the architecture
Sec. I: *"yielding cw/ccw = 0.998 on ∼1.95 million galaxies."* CE-ResNet by construction has exact mirror equivariance; cw/ccw = 0.998 is a measured imbalance on the *output*, reflecting the underlying sky. Comparing to the present work's 0.4974 (CW fraction, not cw/ccw) confuses units. State both as CW fractions, or both as cw/ccw ratios.

### P4-M10. Shamir (2012) sample size citation
Sec. I: *"using ∼1.27 × 10⁵ SDSS galaxies"* for Shamir (2012). Shamir 2012 actually used ~15,000 spirals (or roughly 4 × 10⁴ depending on the version). Please verify the 1.27 × 10⁵ figure against the published paper.

### P4-M11. Apodization notation "C² 2°"
App. A and App. D: *"C² 2° apodization."* This notation is non-standard; NaMaster offers "C1" and "C2" apodization styles with a scale parameter. Spell out the choice.

### P4-M12. Hemisphere LEE result and signal-hunt diagnostics are scattered
Sec. IV E and App. C duplicate content. The "+3.3σ in [0.5, 0.6) bin → −0.03σ at peq>0.6" sample-purity claim is interesting but presented without a table of the full ladder. The diagnostic in App. C(e) shows the same signal is "DECaLS-concentrated, the signature of a footprint-correlated systematic" — but a real cosmological signal could also be footprint-localized due to depth variations. Provide a quantitative coverage map.

### P4-M13. Block-bootstrap covariance inflation factor of 14.7× is enormous
App. D(f): *"Block-bootstrap at NSIDE = 8 ... inflates σ(A_dipole) by 14.7×."* This factor implies the WLS uncertainty was underestimated by ~15×, which means none of the unbooted "z = −264.5" or even "z ≈ −18.1" should be taken at face value. A 14.7× inflation in σ at NSIDE=8 is itself a sign that the spatial covariance is poorly characterized — both the original z and the bootstrapped z are unreliable. Honestly characterize the spatial-covariance uncertainty.

### P4-M14. Page count vs content
For a null result with the contribution claimed, 10 pages is excessive. The methods/results could be presented in ≤6 pages, with the canonical-mask systematic discussion as a single appendix. Recommended max length: **6 pages of body + ≤4 of appendices**.

---

## MINOR findings

### P4-m1. Sec. III A "Declared Analysis Hierarchy" reads as a methods-paper internal audit
This section justifies estimator choice in advance, which is good practice, but the prose ("Primary cosmological estimators... Secondary diagnostic estimators...") reads like a reviewer-facing checklist rather than a results section. Restructure as a methods subsection.

### P4-m2. Eq. (1): "256→3 (softmax)" — the parenthetical "softmax" is a layer description but written as an output unit
Clarify whether softmax is applied during training (probably with cross-entropy this is implicit) vs at inference.

### P4-m3. Eq. (B1): variable `S` (permutation matrix) and `p(x)` (probability vector) are not defined as such; reader must infer.

### P4-m4. Table I last row "470,049 HC" — the HC count is 471,049 (Sec. III A and Sec. VI A). Inconsistent. **Recheck.**
Actually: Sec. III A says "471 049 high-confidence per-spiral" and Sec. VI A says "N = 471,049." Table I row (vi) shows "471,049 HC" — checked, consistent. (Apologies, false alarm — actually re-reading Table I: "471,049 HC" ✓.)

### P4-m5. Catalog A 0.5079 + Catalog C 0.4974: equivariant TTA shifts in the *opposite* direction past 0.5
This is a 0.0105 absolute shift, but the equivariant operation should symmetrize about a model-determined fixed point. The fact that it *over-shoots* 0.5 suggests the TTA is not symmetric about the true classifier mean. Comment on this.

### P4-m6. "8,474,531 galaxies (157 of 8,474,688 failed quality checks)" — arithmetic: 8,474,688 − 157 = 8,474,531 ✓.

### P4-m7. Sec. IV C: "We pixelize the sky at HEALPix resolution NSIDE = 64 (49,152 pixels, ∼0.84 deg² per pixel)." 
41,253/49,152 = 0.84 — fine. But the pixel area is 41,253/49,152 ≈ 0.839 deg², not "∼0.84 deg² per pixel" → actually 41252.96 sq.deg / 49152 = 0.8393 ≈ 0.84 ✓ (units of "sky" / pixel). OK.

### P4-m8. Page 7 "Headline 93.7% three-class accuracy ... post-hoc evaluation without augmentation yields 94.9%." 
The post-hoc-without-augmentation number is *higher* than the with-augmentation number, which is unusual and warrants brief explanation.

### P4-m9. Per-imaging-leg signal "BASS+MzLS +0.30σ / DECaLS +4.50σ / DES +2.46σ" 
These do not naturally combine to +3.29σ; either compute the weighted combination explicitly or remove the implied addition.

### P4-m10. Multiple typographic issues
- Sec. IV D: "(15/500 = 0.030)" — empirical p of 0.030 should be 1 − (rank/N), not rank/N, depending on tail convention. State convention.
- Sec. VI: "the direct-MC pLEE ≤ 10⁻⁴" — typeset "p_LEE" consistently.

### P4-m11. "1.95 million" / "1.95×10⁶" inconsistent unit style between sections.

### P4-m12. Appendix A "Monopole subtraction ... increases σ from +1.85 to +3.64" — a procedural choice that *increases* the residual by a factor of ~2 deserves a separate justification, not a one-liner.

### P4-m13. Fig./Table audit
The paper contains no figures and 5 tables (I–V). The tables are dense and largely text-substitutable; a single power-spectrum figure (Cℓ vs ℓ with null bands) would be far more informative than Table III. PRD typically expects at least one diagnostic figure for a methods paper.

---

## NITs

### P4-N1. "Catalog A (raw, single-pass softmax); Catalog B (Platt-calibrated, +0.4% excess); Catalog C (equivariant production, 2-fold flip TTA)" — listing the Platt-calibrated "+0.4% excess" as a defining feature is odd. The excess is a *measurement*, not a definition.

### P4-N2. Pun-adjacent phrasing in Sec. VI: *"the characteristic signature of a footprint-correlated systematic rather than a primordial isotropy-breaking signal"* — appears nearly verbatim multiple times. Trim.

### P4-N3. Title uses "−0.122σ" with a minus sign in a title; this is unconventional. Use absolute magnitude or rewrite.

### P4-N4. Citation style varies: some entries have arXiv IDs, some have DOIs, some both. Standardize per PRD style.

### P4-N5. "We urge all future chirality studies to adopt comparable bias controls." (Sec. VII) — exhortation language; trim.

### P4-N6. Author affiliation "Independent Researcher, Los Angeles, California, USA" + Hubify-Projects GitHub + bamfai HuggingFace handle — no conflict per se, but please disclose any commercial affiliation explicitly.

---

## Summary recommendation
**MAJOR REVISIONS**

The headline scientific claim — a null chirality dipole at ≈0.75% sensitivity floor on 3.2M spirals — is plausible and the equivariant TTA + MASTER pipeline is reasonable engineering. However: (i) the +3.64σ canonical-mask residual is explained post hoc with discriminators that are not internally consistent (App. D(d) actually *strengthens* the residual); (ii) 67.6% of training labels are CE-ResNet pseudo-labels and the independent GZ1 κ=0.40 floor is treated cursorily; (iii) at least one quantitative inconsistency between the body ("+2.05% → −0.53%, 3.86× suppression") and Table II ("+0.79% → −0.26%") affects a load-bearing claim; (iv) Table II σ-deviations and Table IV z value are arithmetically wrong by ~2–7%; (v) the LEE arithmetic for the hemisphere result contradicts the "<1σ" claim by ~1σ; (vi) the bibliography contains many uncited entries; (vii) the title and length are disproportionate to the actual contribution, which is a null with a quantified mask-leakage diagnostic. None of these are individually fatal, but together they require a serious rewrite before PRD can consider this manuscript. With the issues addressed and the paper compressed to ≤6 pages of main text, this could become a respectable methods note.

---

## PASS 2 — self-critique findings (what initial review missed)

# PRD Referee Report — Paper P4 (Second Pass)

After a careful re-read with the directed checklist, I find a substantial number of additional issues, including one that I consider essential (the "+3.64σ" canonical-mask number is overstated by a factor of ~2 relative to the paper's own rank-based significance), and one stale `fsky` value that does not match any other footprint quoted in the paper.

---

## ESSENTIAL findings (additional)

### P4-E8. The headline canonical-mask "+3.64σ" is overstated by a factor of ~2 relative to the paper's own rank-based significance — and this is buried in a parenthetical
The abstract states the canonical-mask residual as
> *"+3.64σ (z = ∆/σ_null moment-ratio; empirical rank p_MC = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC binomial per-pixel-shuffle null)"*

These two characterizations of the **same** measurement disagree by nearly 2×. A moment-ratio "σ" of +3.64 with an empirical rank p of 0.030 (1-sided ≈ 1.88σ Gaussian-equivalent) is a direct, unambiguous indicator that the null distribution has heavy non-Gaussian tails — and therefore that **the +3.64 number is not a meaningful significance**. The honest characterization is ~1.9σ; the paper nonetheless promotes "+3.64σ" through the title (implicitly), abstract (3 occurrences), Sec. IV D, Sec. VII, Table III footnote, and App. D. This is qualitatively misleading.

App. D(d) confirms this independently: *"null mean C₁ = 3.44×10⁻⁶, std 3.07×10⁻⁶, giving σ = +3.80"* — i.e. σ_null ≈ mean_null, which is mathematically incompatible with a Gaussian and confirms the null is dominated by heavy tails for which the "σ" notation is inappropriate.

**Fix:** the headline canonical-mask number must be the rank-based ~1.9σ. The moment-ratio "+3.64" should be retired, or at minimum clearly labeled as a non-Gaussian-null moment ratio that systematically inflates apparent significance.

### P4-E9. "f_sky = 0.46" in Sec. VI A is inconsistent with every other quoted footprint in the paper
Sec. VI A:
> *"The Fisher Poisson floor at 3σ is ∼0.29% full-amplitude (from σ(A/2)≈0.048% at N_spiral = 3,201,160, f_sky = 0.46)."*

The paper otherwise reports only **three** footprints: 0.49005 (canonical), 0.659 (subsample), 0.482 (apodized canonical). The Fisher-floor calculation is a load-bearing number underpinning the entire "0.29% statistical-only floor" and "0.75% empirical threshold" — and the sensitivity argument feeds the falsification criterion in the abstract. A `fsky = 0.46` that matches no documented mask suggests stale arithmetic from an earlier paper version. **Fix:** recompute with the actual mask, or state which mask is meant.

### P4-E10. App. E(b) introduces an undefined "+4.31σ monopole-preserving dipole"
App. E(b):
> *"the Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict)"*

The number "+4.31σ" appears nowhere else in the paper, the estimator "monopole-preserving dipole" is never defined (the headline Catalog C real-space dipole is +0.43σ — *one order of magnitude smaller*), and it is used as the load-bearing pre-cut baseline for the claim that HC subsamples confirm the null. A +4.31σ baseline implies there is a fitting procedure on Catalog C that produces a 4σ "signal" prior to monopole subtraction; this would dramatically change the framing of the headline null. **Fix:** define the estimator, derive +4.31σ from first principles, and reconcile with the +0.43σ real-space dipole headline.

---

## MAJOR findings (additional)

### P4-M15. Table IV hemisphere z = 4.42 is arithmetically wrong
Table IV: data = 3.48×10⁻³, null = (1.69±0.41)×10⁻³.
Computed: (3.48 − 1.69) / 0.41 = **4.37**, not 4.42. Off by ~1%. Together with the Table IV pseudo-C z miscalculation already flagged (1.57 vs stated 1.68), both displayed z values in this load-bearing table are wrong as displayed.

### P4-M16. The headline −0.122σ uses C² 2° apodization, never mentioned in the main text
App. A: *"Apodization: none on the canonical mask; C² 2° apodization on the subsample mask."*

The **headline** −0.122σ is on the subsample mask. So the headline number depends on an apodization choice that is invisible to a reader who does not consult Appendix A. Apodization affects mode-coupling deconvolution and the resulting σ; this must be stated where the headline number is first introduced (abstract and Sec. IV C).

### P4-M17. The "+2.05% → −0.53%, 3.86×" suppression number cannot be reproduced from any tabulated quantity
The −0.53% can be derived from Catalog C counts: A = (1,592,107 − 1,609,053)/3,201,160 = −0.529% ✓. But +2.05% has no derivation from Table II's f_CW = 0.5079: the implied asymmetry is A = 2×(0.5079 − 0.5) = **1.58%**, not 2.05%. The 3.86× number (2.05/0.53) is therefore not the actual suppression factor either; the correct suppression is 1.58/0.53 = 2.98×. **Fix:** recompute and update all downstream prose. (This compounds P4-E1.)

### P4-M18. App. D(d) "density-stratified-null residual +3.80σ" is *higher* than the data residual +3.64σ — paper interprets this backwards
The paper presents *"σ_data vs density-stratified = +3.80"* and concludes *"Density-stratification alone is insufficient to explain the canonical-mask excess"*. But the σ went **up** under stratification, not down. The honest reading is that conditioning on density does not absorb any of the residual — i.e. it tells us nothing about systematic vs cosmological origin. The paper's framing ("supported by ... density-stratified-null residual +3.80σ") inverts the evidence direction.

### P4-M19. Sec. VII conclusion (c) mislabels which mask the −0.122σ lives on
> *"MASTER mode-coupling deconvolution independently collapses the pseudo-Cℓ to the canonical −0.122σ null."*

The −0.122σ is on the **subsample** mask (fsky = 0.659), not the canonical mask (fsky = 0.49005). On the canonical mask, MASTER does **not** collapse to null — it gives the +3.64σ residual that the paper spends two appendices justifying as systematic. The conclusion-section sentence elides this distinction, exactly the conflation the abstract warned against.

### P4-M20. Falsification criterion is logically confused
Abstract: *"A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% ... would falsify the present null."*

The 0.75% is defined as the **50%-recovery-at-3σ** point of the *current* pipeline. A future survey with different systematics, different classifiers, and different footprints would not inherit this sensitivity floor, so a "σ > 5 at A ≳ 0.75%" detection elsewhere is not directly comparable to the present null. The falsification criterion as stated is ill-defined; it should be stated in terms of an amplitude on a comparable footprint at comparable statistical resources.

### P4-M21. SGP +2.02σ attributed to dust without quantitative test
App. C(b): *"SGP (b<0) gives +2.02 (consistent with the dust-correlated foreground zone)."* No correlation with E(B−V), no template projection, no test against dust-free SGP subregions. A 2σ asymmetry in one hemisphere is asserted-explained, not tested-explained.

### P4-M22. Two-point correlation uses 50,000-galaxy subsample of HC=471,049 without justification
App. C(d): the chirality two-point correlation is computed on a *random 50,000-galaxy* subsample. The HC catalog has 471,049 galaxies; using only 50,000 inflates the per-bin uncertainty by √(471/50) ≈ 3.1×. The maximum 2.41σ at θ ≈ 0.5° "attributable to DESI Legacy brick-boundary classifier artifacts" is in fact a measurement at degraded sensitivity, and the brick-interior subsample claim ("vanishing to −0.03σ") is asserted without a count. No computational reason is given for the subsampling.

### P4-M23. Table III mixes two distinct masks in one table without flagging
The ℓ = 1 single-mode row (subsample mask, fsky = 0.659) and ℓ_eff = 4, 9, 14, 19, 24 rows (canonical-N MASTER, fsky = 0.491) are typeset identically in the same table. The footnote tries to disambiguate, but a reader using Table III as a power-spectrum diagnostic would mistakenly compare bandpowers across masks.

### P4-M24. "p_MC = 15/500 = 0.030" — convention (one-sided vs two-sided) never declared
The conversion to "≈1.9σ" implies one-sided, but for a dipole-power test which can in principle go either direction relative to the null mean, two-sided is more natural and would give ~2.17σ. This is not specified anywhere.

---

## MINOR findings (additional)

### P4-m14. The abstract simultaneously offers three incompatible characterizations of one number
"+3.64σ"; "p_MC = 0.030"; "≈1.9σ Gaussian-equivalent" — three numbers, one quantity. The reader is left to infer that the first is a moment ratio under a heavy-tailed null and the second/third are the honest rank significance. Spell this out, and lead with the rank value.

### P4-m15. Sec. III B augmentation actively *hurts* validation accuracy
Aug-on: 93.7%. Aug-off: 94.9%. Sec. III B reports both without comment. Standard practice retains augmentation only if it improves the held-out metric or generalization to OOD. A 1.2pp validation drop suggests the augmentation distribution is mismatched. Justify the choice or remove augmentation.

### P4-m16. "7 equatorial coordinate slabs"
Sec. IV B and App. E(c) report uniformity across 7 slabs. Seven is an unusual choice (not 6, not 8); pick a binning that maps onto e.g. RA hours or declination bands and justify.

### P4-m17. "Cell-level +4.72σ" appears in App. C(e) without prior introduction
The DECaLS [0.5, 0.6) cell is +4.50σ; the max across 15 cells is then +4.72σ. The reader is expected to infer this. Define explicitly.

### P4-m18. Sec. App. A "Monopole subtraction ... increases σ from +1.85 to +3.64" — also relevant to E8
Going from +1.85σ (without monopole subtraction at the data-vector step) to +3.64σ (with subtraction) under the *same* canonical mask is a factor-of-2 change driven by a single preprocessing choice. Combined with the rank-equivalence of 1.9σ, this suggests the +3.64 is fundamentally driven by a single decision rather than a robust statistical excess.

### P4-m19. App. C(b) Galactic-pole NGP/SGP convention is unstated
"b > 0" usually means Galactic north, but in some surveys "b" is also used for axis ratio (cf. App. E "b/a < 0.3"). Disambiguate.

### P4-m20. Table I uses "—" for both Nmap weighted and fsky on multiple rows
Specifically rows (i), (iv), (v), (vi). For estimators using sky maps (esp. (iv) hemisphere), an fsky is well-defined and should be given.

### P4-m21. Sec. IV C: "Catalog A (raw) shows a 2.31σ real-space dipole and a +6.48σ pre-MASTER pseudo-Cℓ"
The +6.48σ pre-MASTER value never reappears in any table. Add to Table III for cross-reference.

### P4-m22. App. A: monopole subtraction is referred to as "galaxy-weighted mask-mean ⟨A⟩_{mask,gw} = −0.005294"
This is the asymmetry A, not the fraction f_CW. f_CW = 0.4974 → A = −0.0053 ✓. But the relation between ⟨A⟩_{mask,gw} and the global Catalog C asymmetry is not stated. They appear identical to 4 decimal places — coincidence or by construction?

---

## NITs (additional)

### P4-N7. App. D(c): "r_ℓ=1(BASS+MzLS×A_p) = +0.65, r_ℓ=1(DES×A_p) = −0.73"
Two large-magnitude opposite-sign correlations are then "summed" to "∼25% of the observed ℓ=1 amplitude." A scalar sum of two cross-correlation amplitudes from different sky regions is not a well-defined operation. Either give the partial coefficients in a regression, or remove the "25% closure" claim.

### P4-N8. Abstract footnote "(z = ∆/σ_null moment-ratio; empirical rank p_MC = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC binomial per-pixel-shuffle null)"
A single parenthetical containing four distinct statistical characterizations of the same number is opaque; restructure as a sentence.

### P4-N9. "Hubify-Projects" GitHub organization name appearing alongside the lead author's "hubify.com" email is a potential commercial-disclosure issue per PRD policy. State explicitly whether Hubify is a company or a personal repository umbrella.

### P4-N10. Reference [29] (DESI Experiment Part I) is not cited anywhere in the main text.

### P4-N11. App. D introduces "interpretation (i)/(ii)/(iii)" labels matching the abstract, but the abstract labels and App. D labels are paired in narrative order, not cross-referenced explicitly. Add explicit "(see Appendix D, interp. (i))" tags.

---

## Updated overall recommendation
**MAJOR REVISIONS (strengthened from first pass).** 

The "+3.64σ" canonical-mask number — which is the only nominally significant result in the paper, drives Sec. IV D, two full appendices, and three abstract sentences — is overstated by ~2× relative to the paper's own rank-based characterization (P4-E8). Combined with the stale `fsky = 0.46` in the sensitivity-floor calculation (P4-E9) and the unsourced "+4.31σ" estimator in App. E(b) (P4-E10), the paper has serious numerical-consistency issues beyond what the first pass uncovered. App. D(d) presents a result (density-stratified null σ = +3.80) that mathematically contradicts the conclusion drawn from it (P4-M18), and the conclusion section misattributes the −0.122σ null to the wrong mask (P4-M19). The honest scientific content — a null real-space dipole at the sub-percent level on a 3.2M-spiral catalog — can be saved, but the current presentation requires substantial restructuring around the rank-based statistical framework rather than the moment-ratio framework, and the canonical-mask discussion needs to be either deprecated to a brief footnote or rebuilt around the actual ~1.9σ excess.