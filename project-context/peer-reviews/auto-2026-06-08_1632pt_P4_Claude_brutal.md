# P4 auto-2026-06-08_1632pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14194 chars)
**Wall time**: 403.4s

---

# Referee Report: P4 — Survey-Scale Galaxy Chirality with Equivariant TTA

**Reviewer:** Brutal-honesty PRD referee
**Manuscript:** Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null...
**Recommendation will appear at end.**

---

## Overall assessment

This paper presents an interesting catalog-construction and bias-hardening exercise on 8.47M DESI Legacy galaxies producing a chirality catalog and a null ℓ=1 dipole result. However, the manuscript suffers from severe structural and presentational defects that prevent acceptance in PRD in its current form: a wildly bloated title that telegraphs reviewer concessions rather than scientific conclusions, an abstract that juxtaposes multiple incommensurable σ values without disciplined separation, a "headline finding" in the Conclusions that contradicts the abstract's "headline scientific result," internal numerical inconsistencies between abstract/table/text, and an extensive systematic analysis (Appendix D) that effectively undermines several of the body claims. The actual scientific content (a null dipole at sub-percent sensitivity on a new large catalog, plus a demonstration of monopole-mask leakage) could be a publishable PRD methods paper at roughly half the present length, but only after major revisions.

---

## ESSENTIAL findings

### P4-E1 — Title is not a scientific title (Page 1)
The title literally encodes σ-values, sample sizes, and reviewer-style hedges:
> "A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)"

This is not a PRD title. It reads as a self-defensive concession list constructed during revision. PRD titles are concise (~10–15 words) and state the physics result, not the σ value of the null. **Required fix:** Replace with a ~12-word title, e.g., "A null ℓ=1 chirality dipole at sub-percent sensitivity from 3.2 million DESI Legacy spirals."

### P4-E2 — Abstract contains a contradiction with the Conclusions about what the "headline" finding is (Pages 1, 6–7)
Abstract states:
> "The headline scientific result is a null ℓ = 1 chirality-dipole observable on the analysis subsample mask…"

Conclusions Section VII states:
> "a. **Headline finding**: a quantifiable monopole-mask leakage channel."

These are two different "headline" claims. The reader cannot tell whether the headline contribution is (a) a null dipole, or (b) the leakage-channel demonstration. **Required fix:** Pick one headline and use that single phrasing consistently in abstract, intro, and conclusions.

### P4-E3 — Incommensurable σ values juxtaposed without disciplined separation (Abstract, Page 1)
The abstract lists, in close succession: −0.122σ (label-shuffle null), +0.43σ (isotropic-null bootstrap), +3.64σ (binomial pp-shuffle), +3.57σ (apodized variant), −2.89σ (cross-spectrum permutation), 3.05σ (hemisphere max-statistic). The single bracketed note "σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators" is insufficient given how the numbers are then thrown around. The compliance burden in the reviewer instructions is "at every juxtaposition" — this is not met. **Required fix:** Either tabulate σ values exclusively in Table I and refer to them by row, or attach a one-clause null-identifier to every single σ in the abstract and body. Strip σ-values out of the title (see P4-E1).

### P4-E4 — Arithmetic inconsistency: Table II "Excess (%)" column does not match σ column or quoted abstract value (Page 4)
Table II Catalog C row: fCW = 0.4974, "Excess −0.26%", "Dev 9.5σ".
- σ₀ for N=3,201,160 at p=0.5: σ = √(0.25/3,201,160) = 2.795×10⁻⁴, matches the quoted 0.000279. ✓
- Deviation: (0.4974 − 0.5)/0.000279 = −9.32. Quoted as 9.5σ — rounding tolerable but should be −9.3σ in magnitude. ✓ approximately
- Excess: 0.4974 − 0.5 = −0.0026 = −0.26%. ✓
But: The abstract says "the equivariant CW fraction is 0.4974 ± 0.000279" — fine. And Sec IV B claims a "9.5σ monopole" but also calls Catalog C "−0.53%" raw-to-equivariant collapse: "raw +2.05% to equivariant −0.53%". Table II shows Catalog A excess = +0.79% (not +2.05%), and Catalog C excess = −0.26% (not −0.53%). **Where does +2.05% / −0.53% come from?** Either Table II is wrong or the IV B narrative is wrong. **Required fix:** Reconcile the asymmetry-suppression-factor figures (3.86×) and reconcile +2.05/−0.53 vs +0.79/−0.26 throughout.

### P4-E5 — The "3.86× suppression factor" is unverifiable from the numbers given (Page 4)
Sec IV B: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates…" But 2.05/0.53 = 3.87 ✓ — *if* those numbers are right. They contradict Table II (+0.79 / −0.26 → ratio 3.04 or 0.79/0.26 = 3.04). Neither match 3.86×. **Required fix:** Identify which set is the equivariant CW fraction definition (CW/(CW+CCW) vs CW/all) and use one consistently in Table II and Sec IV B.

### P4-E6 — Cohen's κ = 0.40 implies the classifier is "fair" agreement, propagation to "subpercent systematic floor" is unjustified (Pages 2–3)
> "The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91% (Cohen's κ = 0.40). We treat 69.91% as the conservative accuracy floor and propagate it to all downstream isotropy bounds via the sub-percent systematic floor in Sec. IV C."

If κ=0.40 (moderate, by Landis-Koch), then per-galaxy label noise is large, and the dilution factor g = 2a−1 = 0.398 (correctly quoted later) means a true-underlying dipole of A would appear as 0.4A. The "true-underlying threshold ~1.88%" calculation (Sec VI A) is consistent. But the abstract's claim "0.75% (the demonstrated empirical 50%-recovery-at-3σ threshold)" appears in the title and abstract without the dilution caveat — the *true cosmological dipole* the survey can rule out is **1.88%**, not 0.75%. This is a major framing problem. **Required fix:** State the dilution-corrected detection threshold (≈1.88%) in the abstract and recompute the "factor of ~6–12 below Shamir's 3%" claim accordingly: 3%/1.88% ≈ 1.6×, not 6–12×.

### P4-E7 — The "factor of ~6–12" Shamir-amplitude comparison is wrong (Pages 2, 6, 7)
Abstract: "inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼6–12 under the present pipeline."
Sec VI B: "the Shamir ∼3% amplitude class by a factor of ∼6–12."
Sec VII: "disfavors at the amplitude level any model predicting…dipole ≥0.75%…the Shamir ∼3% amplitude class by a factor of ∼6–12."

If the empirical threshold is A=0.75% at 3σ, then 3%/0.75% = 4. If the lower-end empirical sensitivity is A=0.5% (15% recovery), then 3%/0.5% = 6. To get 12, you need 3%/0.25%. None of these are derived in the paper. Where does 12 come from? **Required fix:** Derive the upper bound of the range explicitly or remove "~6–12" and state a single defensible ratio.

### P4-E8 — Apparent contradiction: "+3.64σ canonical-mask residual is consistent with monopole-mask leakage" vs. residual after monopole subtraction (Page 1, Sec IV D, Appendix A)
Abstract: "A canonical-mask diagnostic of the leakage mechanism shows that pre-MASTER raw pseudo-C1 in the un-monopole-subtracted CW-fraction map (…) is reproduced at 99.3% of its observed amplitude by a controlled monopole-only generative null… The post-MASTER canonical-mask direct-MC residual is +3.64σ (…) under proper galaxy-weighted monopole subtraction."

Then: "The +3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry."

But if monopole has been subtracted, how is the residual "monopole leakage"? Appendix A says monopole subtraction reduces decoupled C₁ at ℓ=1 from 2.30×10⁻⁵ to 1.51×10⁻⁵, **and increases σ from +1.85 to +3.64**. So subtracting the monopole makes the significance worse. This is then re-attributed to a "depth/morphology-correlated systematic" in Appendix D, not "monopole leakage." The abstract's phrasing is internally inconsistent. **Required fix:** Either call the +3.64σ a "depth-correlated systematic residual" everywhere (matching Appendix D's verdict) or explain precisely how monopole subtraction can *increase* the σ if the residual is still "monopole leakage."

### P4-E9 — empirical rank p_MC = 0.030 corresponds to ≈1.88σ Gaussian, not 3.64σ (Page 1)
Abstract: "+3.64σ (z = ∆/σnull moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent…"

Reporting +3.64σ as the headline number while simultaneously admitting the empirical rank null gives 1.9σ is misleading. The honest number is 1.9σ; the 3.64σ is a moment-ratio that assumes Gaussian null tails that the empirical null disproves. **Required fix:** Throughout the paper, when the empirical p_MC differs from the moment-ratio z, lead with the empirical p_MC value (1.9σ) and explain the discrepancy as evidence of non-Gaussian null tails. The phrase "+3.64σ" in tables and abstract is reviewer bait.

### P4-E10 — Footnote 1 (page 4) admits a queued recomputation that may change the headline "99.3% reproduction" figure
> "A parallel rerun on N(p)all-trial draws is in queue for the canonical-mask sensitivity-budget recompute… the size of the resulting shift in the headline 99.3% reproduction figure … is not predictable analytically … and will be reported empirically when the N(p)all rerun completes."

A paper submitted to PRD cannot have a "queued" computation that may move its headline number. **Required fix:** Either complete the rerun before submission or remove the 99.3% figure from the abstract and present only the qualitative claim.

### P4-E11 — pMC ≤ 10⁻⁴ from "N = 10,000 random-label shuffles" is the floor, not a measurement (Page 8, Appendix C)
> "The direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives pLEE ≤10⁻⁴"

With 10,000 shuffles the minimum measurable p is 1/10,000 = 10⁻⁴ (or "0 of 10,000"). Quoting "pLEE ≤ 10⁻⁴ (rejection of the random-label null)" without quoting how many of 10,000 actually exceeded the observed value is uninformative. **Required fix:** Report the actual count (e.g., "0 of 10,000 random-label realizations exceeded the observed asymmetry") and revise the LEE correction discussion accordingly.

### P4-E12 — Table I "Mask" column shows em-dash for Nmap_weighted on canonical rows but the canonical mask should also have a weighted count (Page 4)
Row (iii) and (v) show "—" for Nmap_weighted; only (ii) shows 5,547,858. This is inconsistent — every NaMaster execution has a weighted-mask sum. **Required fix:** Fill in Nmap_weighted for every row or explicitly state which rows do not use weighted masks.

### P4-E13 — Falsification criterion in abstract is internally inconsistent (Page 1)
> "A future survey detecting a chirality dipole at σ >5 with full amplitude ≳ 0.75% (the demonstrated empirical 50%-recovery-at-3σ threshold under the adopted per-pixel-shuffle null on the HC pipeline) would falsify the present null."

The current null is at sub-percent (0.75% threshold). A future survey detecting ≥0.75% at 5σ would not "falsify the present null" — it would be entirely consistent with the present non-detection at this sensitivity, since 0.75% is the *threshold*, not an exclusion. **Required fix:** State the actual exclusion upper limit (e.g., 95% C.L. upper limit on A) and base the falsification criterion on that.

---

## MAJOR findings

### P4-M1 — Length vs. content mismatch (entire paper)
The paper has 11 pages of body + 4 pages of appendices. Substantial portions (Sec IV D + V A + VI + VII + Appendix D) are devoted to repeated discussion of why the +3.64σ canonical residual is not a detection. The core scientific contribution — a null dipole at A < ~1.9% (dilution-corrected) on a 3.2M-spiral catalog — could be presented in ~6 pages plus 2 appendices. **Recommended:** Compress to ~7 pages total. Move Appendix D to supplementary material.

### P4-M2 — 67.6% of training labels are from CE-ResNet predictions (Page 3)
The paper acknowledges: "67.6% of training labels derive from CE-ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth."

This is a circularity issue serious enough to compromise the claim that this is an "independent" check. The κ=0.40 against disjoint GZ1 is the only genuinely independent number, and κ=0.40 is moderate. **Required fix:** Move this disclosure to the abstract and explicitly state the implications for "independence" claims relative to Jia et al. (2023).

### P4-M3 — "Survey-scale" and "1.6× CE-ResNet" framing is barely substantive (Pages 1, 2)
CE-ResNet: 1.95M classifications. This work: 3.20M spirals. Ratio = 1.64. The "1.6× CE-ResNet's scale" is a 60% expansion, not an order-of-magnitude advance. Calling this "survey-scale" while CE-ResNet was already 1.95M is questionable. **Required fix:** Tone down "survey-scale" framing or drop it.

### P4-M4 — The independent CE-ResNet result of cw/ccw = 0.998 is not actually compared apples-to-apples (Pages 2, 6)
Jia et al. report cw/ccw = 0.998 → CW fraction = 0.998/(1+0.998) = 0.4995, i.e. deviation 0.05% from 0.5. The current work reports 0.4974 ± 0.000279, deviation 0.26% (9.3σ). The current pipeline is *less* equivariant than CE-ResNet by ~5×. This is not adequately acknowledged when comparing the two pipelines as "complementary" (Sec V B). **Required fix:** State explicitly: our equivariance residual is ~5× worse than the architectural-equivariance benchmark of Jia et al.

### P4-M5 — Claim that the residual +3.64σ is "consistent with monopole leakage through survey geometry" contradicts Appendix D's verdict (Pages 1, 9)
Appendix D states the residual is *not* monopole leakage but a "depth/PSF/morphology" systematic on the canonical footprint, with a quantitative leg-stratified contribution of ~25%. The abstract should not attribute the residual to monopole-mask leakage if the body's verdict is depth/PSF/morphology. **Required fix:** Use the precise Appendix D attribution in the abstract.

### P4-M6 — "1.7% interpretation (i) at z = −264.5" is preposterous and useless (Page 9, Appendix D)
The WLS posterior z-statistic of −264.5 for the 1.7% dipole interpretation, with block-bootstrap inflation to z ≈ −18.1, is extreme and clearly indicates either over-fitting or a degenerate template basis. Quoting z ~ −250 numbers in a physics paper without diagnostic plots is unjustifiable. **Required fix:** Provide the design-matrix condition number, the bootstrap distribution figure, and either remove the naive z = −264.5 (it is non-informative once you cite the bootstrap z = −18) or justify why it appears.

### P4-M7 — Hemisphere 3.05σ "local maximum" with claim that post-LEE σ < 1 contradicts the direct-MC p_LEE ≤ 10⁻⁴ (Pages 3, 8)
Body says hemisphere max-asymmetry 3.05σ has empirical direct-MC p_LEE ≤ 10⁻⁴ (Bonferroni post-LEE drops below 1σ). But if the direct-MC LEE-corrected null gives p ≤ 10⁻⁴, that *is* the LEE-corrected significance, not 1σ. Bonferroni is more conservative than the direct-MC max-statistic null only if you're penalizing in addition to the MC. The paper's treatment is contradictory: direct-MC LEE ≤ 10⁻⁴ should be the result; Bonferroni-on-top double-counts. **Required fix:** Pick the direct-MC LEE-corrected significance as the answer and explain (or drop) the Bonferroni step.

### P4-M8 — The "p = 0.30" in abstract for the real-space dipole at +0.43σ doesn't match a one-sided test (Page 1)
For a 0.43σ deviation, the two-sided p ≈ 0.67; the one-sided p ≈ 0.33. p=0.30 is roughly one-sided but not quite. **Required fix:** State the tailedness of the bootstrap p-value and recompute.

### P4-M9 — Figure inventory: I cannot find a single figure in the manuscript
The submitted paper contains only tables (Tables I–V). No figures. A paper presenting a 3.2M-galaxy catalog, dipole fits, MASTER bandpower spectra, hemisphere LEE distributions, and a generative null *with no figures whatsoever* is below PRD presentation standards. **Required fix:** Add at minimum: (a) sky map of the chirality-asymmetry field with mask overlay; (b) bandpower plot of pre/post-MASTER Cℓ with null bands; (c) generative-null Cℓ histogram with observed value indicated; (d) injection-recovery curve showing the 0.75% threshold.

### P4-M10 — The dilution factor g = 2a − 1 derivation is missing (Page 6)
Sec VI A asserts: "GZ1-dilution factor g = 2a−1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ~1.88%." Where does g = 2a − 1 come from? This is a binary-classification-error formula that assumes symmetric label flipping with rate (1 − a). It needs derivation or citation. **Required fix:** Derive g = 2a − 1 (or cite) and state the symmetry assumption.

### P4-M11 — "spirals total Nspiral = 3,201,160 (37.78%)" arithmetic check (Page 3)
CW 1,592,107 + CCW 1,609,053 = 3,201,160. ✓. NS 5,273,371. Total = 8,474,531. Spiral fraction = 3,201,160/8,474,531 = 37.77%. ✓ (rounding fine). However, abstract says "471 049 high-confidence per-spiral after peq_CW > 0.9". This 471,049 number is repeated in Table I row (vi), Sec VI A. The Sec VI A injection sweep uses N=471,049 with peq > 0.9. But Appendix E uses "HC-broad-0.6 (peq > 0.6, N = 949,584) and HC-strict (peq > 0.8, N = 624,660)" — none of which is the 471,049 (peq>0.9). The cuts are inconsistent across sections. **Required fix:** Define a single HC convention or table all HC tiers and reference by tier name.

### P4-M12 — Sec IV C reports Catalog A "+6.48σ pre-MASTER pseudo-Cℓ" but Sec IV D reports +1.68σ residual against the monopole-only null (Pages 4, 5)
The monopole-only null reproduces 99.3% of the pre-MASTER pseudo-C₁ power, leaving +1.68σ residual. But Sec IV C describes Catalog A as having "+6.48σ pre-MASTER pseudo-Cℓ" against (presumably) a different null. Reader cannot tell whether the 6.48σ null is the pp-shuffle (Table I), the binomial monopole null (Table IV), or something else. **Required fix:** Annotate each σ with its null specification, including the +6.48σ Catalog A pre-MASTER number.

### P4-M13 — Section V B "complementary" framing whitewashes a real discrepancy (Page 6)
"The two pipelines are complementary." CE-ResNet has 0.05% equivariance residual; this work has 0.26% residual (5× worse). The paper buries this and frames the comparison as if both pipelines are equally rigorous. **Required fix:** State the relative equivariance performance honestly.

### P4-M14 — The 8-test "bias hardening suite" (Table V) is a self-pass test (Page 8)
All 8 tests pass at thresholds set by the authors. The authors then acknowledge "acceptance thresholds are generous relative to the 0.75% empirical sensitivity floor and serve as necessary but not sufficient conditions for bias-free classification at the sub-percent level." If the thresholds are generous, the test is largely cosmetic. **Required fix:** Either tighten the thresholds (e.g., T6 hemispheric null < 0.5% to match the sub-percent sensitivity floor) or drop Table V as non-load-bearing.

### P4-M15 — Footnote 1 on page 4 is too long and contains version-bookkeeping prose
The footnote begins as a legitimate definitional clarification but devolves into a queued-recomputation status update ("a parallel rerun on N(p)all-trial draws is in queue") that reads like an internal revision note. PRD does not publish status updates. **Required fix:** Strip the footnote to its definitional content and remove the queue notice.

---

## MINOR findings

### P4-Mi1 — Reference [2] vs [3] are both Shamir DESI 2022 papers but the abstract cites Shamir (2022) singular (Page 10)
References list two Shamir 2022 papers ([2] PASJ 74, 1114 and [3] MNRAS 516, 2281). The text cites them separately but the abstract reference list does not differentiate. Verify which 2022 paper(s) are intended at each citation.

### P4-Mi2 — Reference [9] "Galaxy Zoo DESI: detailed morphology measurements for 8.7M galaxies" (Page 10)
The paper uses cross-matching with Galaxy Zoo DESI predictions. Walmsley et al. 2023 covers ~8.7M, matching the parent sample. Citation correct. ✓

### P4-Mi3 — "Adipole" symbol vs. "|Adipole|" usage (Pages 2, 6, 7)
Inconsistent: sometimes "|Adipole| ≥ 0.75%", sometimes "A = 0.75%". Pick one convention.

### P4-Mi4 — The "DES overlap region" is mentioned in Data but never used as a stratification axis (Page 2)
Yet Appendix C reports a 3-way leg breakdown (BASS+MzLS / DECaLS / DES). Section II should at least note the per-leg footprint fractions.

### P4-Mi5 — "0.262″/pixel" claim for DR8 (Page 2)
Standard DECaLS pixel scale is 0.262 arcsec/pixel, but BASS pixel scale is ~0.454″/pixel and MzLS is ~0.260″/pixel. The 0.262″ claim is leg-specific. Fix or qualify.

### P4-Mi6 — "Cohen's κ = 0.40" without sample sizes for the 4-cell confusion matrix (Page 3)
For an audit, provide the actual confusion matrix (CW-CW, CW-CCW, CCW-CW, CCW-CCW).

### P4-Mi7 — Eq. (1) is given as a "layer block" but is not a proper equation (Page 3)
Render the head architecture as either prose or a labeled table; Eq. (1) is not a mathematical equation.

### P4-Mi8 — Eq. (2) "Peq_NS = ½(Porig_NS + Pflip_NS)" — but the constraint Σ Peq = 1 is not verified (Page 3)
Since Porig sums to 1 and Pflip sums to 1, the equivariant probabilities sum to 1 only because the CW/CCW swap is symmetric. State this.

### P4-Mi9 — Section IV B says "all 7 equatorial coordinate slabs" (Page 4)
Why 7? Define the slab geometry (∆RA = 360°/7? declination bands?). This appears again in Appendix E.

### P4-Mi10 — "Cohen's kappa = 0.40" repeated in Data Availability section (Page 9)
Information already given on page 3.

### P4-Mi11 — Table III last row: "Joint χ²/dof (38 bandpowers) — 161.2/38 = 4.24" (Page 5)
χ²/dof = 4.24 is a serious badness-of-fit. The note "Dominated by mask-coupled monopole" is hand-waving. Provide actual residual breakdown.

### P4-Mi12 — Table IV "Hemisphere max|A| (NSIDEdir = 8)" gives z = +4.42 (Page 5)
A 4.4σ residual in the hemisphere-statistic monopole null deserves discussion. The paper claims monopole-only null explains 99.3% of pseudo-C₁ power, but the hemisphere statistic shows +4.42σ residual — these are inconsistent statements about how well the monopole-only null explains the data.

### P4-Mi13 — "We treat 69.91% as the conservative accuracy floor" (Page 3) — 69.91% is the *measured* accuracy, not a conservative floor.

### P4-Mi14 — Acknowledgments "AI tool usage" statement (Page 10)
This is appropriate disclosure, but the phrasing should be tightened to follow the APS author-disclosure guideline format if there is one.

### P4-Mi15 — "Cosmoglobe" reference [20] is a Planck/WMAP CMB birefringence paper, not directly relevant to galaxy chirality
Reference list is wide-ranging but several references (e.g., [19], [20], [23]) are CMB-birefringence papers cited under "Relation to Parity-Violating Sectors." The intermediate transfer-function discussion is one sentence: "that transfer function is not derived in this paper." Either derive or drop the speculative parity-violation context, since cited refs do nothing for the cosmological interpretation.

### P4-Mi16 — Reference [33] Hivon et al. MASTER paper journal info (Page 11)
"Astrophys. J. 567, 2 (2002)" — actually the MASTER paper is Hivon et al. 2002 ApJ 567, 2. The page number "2" should be checked; the actual paper appears to begin on page 2 of vol 567. Verify.

### P4-Mi17 — Reference [5] Iye 2021 finding "no significant dipole after correcting" (Page 2) — partially mischaracterized
Iye et al. 2021 used 3D random-walk simulations and re-examined Shamir's catalog. They did not categorically find "no significant dipole" — their conclusion was more nuanced. Tighten the description.

---

## NITs

### P4-N1 — "Bias hardening" is hyphenated inconsistently ("bias-hardening" vs "bias hardening").

### P4-N2 — Pages 5, 7: "−0.122σ" sometimes appears with the unicode minus, sometimes with hyphen-minus.

### P4-N3 — Sec II A: "Cohen's κ" introduced before Sec III's "kappa = 0.40" notation.

### P4-N4 — "spherical-harmonic" hyphenated; "shape r eff" should be "shape_r_eff" or "r_eff".

### P4-N5 — "Smith42/galaxies" dataset name is informal; provide a formal citation if available.

### P4-N6 — Appendix A: "decoupled C₁ at ℓ = 1 from 2.30 × 10⁻⁵ to 1.51 × 10⁻⁵ (∼ 34%)" — ratio is (2.30−1.51)/2.30 = 34.3%. ✓

### P4-N7 — Page 4 contains "Catalog A 2.31σ" but Page 6 "2.31σ → 0.43σ" implicitly claims a quantitative collapse without showing the intermediate Catalog B value (Catalog B real-space σ is not quoted).

### P4-N8 — Eq. (B1): the consistency loss as written treats the original and flipped predictions as if they are perfectly aligned channel-by-channel; the L2 metric should clarify whether it is per-class or summed.

### P4-N9 — Page 8: "Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict)" — what is the +4.31σ "monopole-preserving dipole" — this number is not in Table I or any other table.

### P4-N10 — "AI tool usage" disclosure: harmless but should specify which LLM models were used per APS guidance (if applicable).

---

## Specific numerical recomputations performed

1. **Catalog C binomial σ:** √(0.5·0.5/3,201,160) = 2.795 × 10⁻⁴. ✓ Matches 0.000279.
2. **Catalog C deviation:** (0.4974 − 0.5)/2.795×10⁻⁴ = −9.30σ. Paper says 9.5σ. Discrepancy 0.2σ from rounding the CW fraction; tolerable but report to one more decimal place (0.49740 vs 0.4974 changes σ).
3. **Catalog A CW count:** Sec IV B says +0.79%. Catalog A row of Table II reads 0.5079. ✓
4. **Catalog A deviation:** (0.5079 − 0.5)/2.795×10⁻⁴ = +28.27σ. Paper says 28.8σ. Off by ~2%, likely from rounding 0.50795 to 0.5079.
5. **3.86× suppression factor:** Cannot be reconciled with Table II numbers (0.79/0.26 = 3.04). Section IV B quotes +2.05/−0.53 which gives 3.87. **Inconsistency.**
6. **CW/CCW ratio for CE-ResNet:** 0.998 → CW fraction 0.4995, deviation 0.05% from 0.5; current pipeline 0.26% from 0.5; therefore the current pipeline is ~5× *less* equivariant than CE-ResNet. Not honestly stated in Sec V B.
7. **Excess vs deviation arithmetic:** (0.4974-0.5)/0.5 = -0.0052 = -0.52%, but the "Excess (%)" column reports -0.26%. The column is (fCW - 0.5) in percentage points (i.e., 0.4974 - 0.5 = -0.0026 = -0.26 pp), not "excess." Mislabeled.
8. **Shamir comparison factor:** 3% / 0.75% = 4. The paper's claim of "6–12" is unsupported.
9. **Total catalog rows:** 1,592,107 + 1,609,053 + 5,273,371 = 8,474,531 ✓
10. **Generative null Z:** Pre-MASTER pseudo-C₁ data 1.696×10⁻² vs null 1.685±0.007×10⁻²: Z = (1.696 − 1.685)/0.007 = 1.57, not +1.68. Discrepancy from rounding the null std. **Recompute.**
11. **Hemisphere Z (Table IV):** (3.48 − 1.69) × 10⁻³ / 0.41 × 10⁻³ = 4.37, not +4.42. Rounding tolerable but report to consistent precision.
12. **Apodization Z:** "+3.57σ on C² 2° apodization, essentially unchanged from binary" (vs. +3.64σ). Difference is 0.07σ. ✓ qualitatively but unimportant.

---

## Summary recommendation

**REJECT** (with strong encouragement to resubmit after the major rewrite outlined below).

The paper has a real scientific kernel — a null dipole on a 3.2M-spiral catalog with a useful demonstration of monopole-mask leakage in pseudo-Cℓ pipelines — but in its current form it is unpublishable in PRD. The title is not a scientific title; the abstract throws six incommensurable σ values at the reader; the "headline" finding contradicts itself between abstract and conclusions; the +3.64σ residual is presented as both "consistent with monopole leakage" and "depth/morphology systematic" depending on which section you read; the dilution-corrected sensitivity threshold (~1.9%, not 0.75%) is buried and the "factor of 6–12" Shamir comparison is not derivable from the stated numbers; the paper has no figures; arithmetic between Table II and Sec IV B does not close (3.86× vs 3.04×); a footnote on page 4 admits a queued recomputation that could move the headline 99.3% number; and the "1.6× CE-ResNet" framing inflates a 60% expansion into a "survey-scale" advance while burying the fact that the new pipeline's equivariance residual is ~5× worse than CE-ResNet's. Recommended maximum length for the resubmission: **7 body pages + 2 appendix pages**, with Appendix D moved to supplementary material, all σ values traceable to a single null table, the dilution-corrected sensitivity stated prominently, and at least four figures added.

---

## PASS 2 — self-critique findings (what initial review missed)

# Second-Pass Referee Report: P4 (Fresh Eyes)

Below are additional findings missed in the first pass.

---

## ESSENTIAL findings (additional)

### P4-E14 — Sensitivity argument is circular: 0.75% empirical floor is precisely Fisher + dilution, not "above" Fisher (Page 6, Sec VI A)
The paper writes:
> "The headline empirical 50%-recovery-3σ threshold is therefore A ≈ 0.75%, **above the Fisher floor** due to classification noise (GZ1-dilution factor g = 2a−1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼1.88%)."

Recompute: dilution-corrected Fisher floor = 0.29% / 0.398 = **0.73%**. The observed empirical floor is 0.75%. These are statistically identical. The empirical floor is **not** "above" Fisher due to additional classification noise — it is precisely what classification dilution alone predicts. The framing implies a separate "classification noise" effect exists beyond the κ=0.40 label-flip dilution; the numbers show no such effect. **Required fix:** State that "empirical floor matches Fisher × dilution⁻¹ to within 3%, confirming classifier noise is dominated by label-flip dilution alone."

### P4-E15 — Abstract sample-size "n = 5,547,858" mislabels a mask-weight sum as a galaxy count (Pages 1, 3, 4)
Abstract:
> "the strict-superset subsample mask (n = 5,547,858, fsky = 0.659)"

Sec III A repeats:
> "MASTER-deconvolved Cℓ at ℓ = 1 on the analysis subsample mask (n = 5,547,858, fsky = 0.659)"

But Table I caption clarifies: "Nmap_weighted = Σ Wp where Wp = N_all^(p) is the total classified-galaxy count in pixel p (CW+CCW+NS), used as a survey-depth weight." The figure 5,547,858 is **not a galaxy count and not a subsample size** — it is a sum of per-pixel mask weights that double-counts in the sense that pixels with many galaxies contribute more. The actual spiral count in this mask is **not stated**; it is some subset of the 3,201,160 catalog spirals selected by the per-pixel threshold ≥10 spirals plus the mask. Using "n=" for a mask weight in the abstract is a serious presentation error: every reader assumes "n" = sample size. **Required fix:** In the abstract, intro, Sec III A: replace "n = 5,547,858" with "mask weight Σ Wp = 5.55M" and quote the actual spiral count on the analysis-subsample mask.

### P4-E16 — Injection-recovery sensitivity tests are run on the WRONG (smaller) sample than the headline measurement (Pages 6, App E)
The headline −0.122σ MASTER null uses the analysis subsample mask with mask-weight 5,547,858 (~Σ Wp covering 3M+ spirals). The injection-recovery sweep that defines the 0.75% sensitivity floor is run on the **HC-spiral subsample N = 471,049** (peq > 0.9), which is ~15% of the headline sample. Statistical sensitivity scales as 1/√N, so injecting into the 471k HC sample inflates the reported threshold by √(N_full/N_HC) ≈ √(3.2M/0.471M) ≈ 2.6× relative to what the headline pipeline can detect.

The "headline empirical 50%-recovery-3σ threshold at A = 0.75%" is therefore **NOT the sensitivity of the headline ℓ=1 estimator**. The actual headline-pipeline sensitivity could be as small as A ≈ 0.75%/2.6 ≈ 0.29%, identical to the Fisher floor. **Required fix:** Re-run injection-recovery on the analysis subsample (the same mask weighting used for the headline) and quote that as the falsification threshold. The current 0.75% is a conservative estimate from a non-matching pipeline and should not be the headline sensitivity number.

### P4-E17 — App E reveals a +4.31σ Catalog C "monopole-preserving dipole" that is never mentioned in the body (Page 9)
Appendix E states:
> "the Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict), consistent with the headline 0.43σ real-space dipole on the full equivariant catalog."

The body presents only the monopole-**subtracted** real-space dipole of +0.43σ. A +4.31σ monopole-preserving dipole on the Catalog C full sample is hiding in App E. This is critical context: the real-space dipole has an ℓ=1 amplitude of +4.31σ if you don't subtract the global CW excess. The fact that subtracting the monopole removes 90% of this and the HC cuts reduce it to <1σ is part of the bias-hardening story and belongs in the body, not in App E. **Required fix:** State the +4.31σ monopole-preserving real-space dipole alongside +0.43σ monopole-subtracted in Sec IV C and explain the relationship.

---

## MAJOR findings (additional)

### P4-M16 — Mean confidence 0.951 vs median 0.9997 implies extremely bimodal distribution; p_CW > 0.9 cuts 85% of spirals (Pages 3, 6)
Sec IV A: "Mean classification confidence is 0.951, median 0.9997."

Median ≫ mean indicates strongly bimodal classification: most galaxies are essentially certain (median ≈ 1) but a substantial low-confidence tail drags the mean to 0.95. The p_CW > 0.9 HC cut retains 471,049/3,201,160 = 14.7% of spirals. So **85% of spirals have peq_CW < 0.9**. Either (a) borderline objects (P_CW ≈ P_CCW) dominate, contradicting the very-high median, or (b) the median is measured on all 8.47M galaxies (where NS class soaks up confident "not spiral" votes), and the spiral subset is genuinely difficult. The latter would mean classification of CW vs CCW is fundamentally uncertain for the bulk of spirals, contradicting the "median 0.9997" framing. **Required fix:** Quote separately the confidence distribution for (i) all 8.47M galaxies, (ii) the 3.2M spirals, (iii) the CW vs CCW binary subset. The current single mean/median is misleading.

### P4-M17 — Excess +2.05% raw vs +0.79% (Table II): a factor of ~2 inconsistency, NOT a Catalog A vs A definition difference (Sec IV B vs Table II)
First-pass finding P4-E5 identified this but I should refine. Testing whether "asymmetry" notation explains the gap:

If A = 2(fCW − 0.5):
- Catalog A: A = 2 × 0.0079 = **+1.58%** (not +2.05%)
- Catalog C: A = 2 × (−0.0026) = **−0.53%** ✓ matches

So the **+2.05%** for Catalog A doesn't match Table II under any standard convention. It would require fCW_A = 0.5103, not 0.5079. Either:
- Table II is for a different sample than the IV B text, or
- The +2.05% is from a pre-Catalog-A "raw, single-pass, no-postprocessing" tier not documented elsewhere, or
- Stale number from earlier version.

The "3.86× suppression factor" requires 2.05/0.53. If you use the Table II numbers correctly (1.58/0.52), the suppression factor is 3.04×, not 3.86×. **Required fix:** Reconcile and recompute the suppression factor consistently.

### P4-M18 — Z2-vs-D4 TTA argmax flip rate "21.4% on borderline" is uninformative without borderline fraction (Page 3, Sec III C; App B)
The paper reports "per-galaxy argmax labels flip in 21.4% of cases between Z2 and D4 on borderline galaxies with PCW ≈ PCCW ≈ 0.4." The catalog-wide flip rate is 21.4% × (borderline fraction). The borderline fraction is never stated. Without it, this number is not a sensitivity diagnostic. **Required fix:** Report the catalog-fraction-weighted argmax flip rate between Z2 and D4 TTA.

### P4-M19 — Bibliography contains ~17 uncited references (Sec V B, VI B, refs [11, 13-30] partially)
References [11] (Land et al. SDSS spin), [13] (Gross & Vitells LEE), [14] (SpArcFiRe), [15] (Motloch correlated spins), [16] (Lue-Wang-Kamionkowski parity), [17] (Cabass parity), [18] (Philcox BOSS parity), [19] (Eskilt birefringence), [20] (Cosmoglobe), [21] (Hou BOSS parity), [22] (Cahn 3D parity), [23] (Komatsu parity), [24] (Hayes GZ1 winding bias), [25] (Bamford GZ env), [26] (Hart GZ redshift bias), [27] (Walmsley GZ DECaLS), [28] (Yu primordial chirality), [29] (DESI design), [30] (LSST) — I cannot find inline citations for most of these in the manuscript body.

Particularly conspicuous: the entire "Relation to Parity-Violating Sectors" subsection (VI B) discusses parity-odd vs parity-even channels, primordial chiral-tensor transfer functions, etc., **without citing any of refs [16, 17, 18, 19, 20, 21, 22, 23]** that are literally on this topic and listed in the bibliography. This suggests either (a) the bibliography was assembled separately from inline citations, or (b) the parity-physics section is summarizing literature without attribution. **Required fix:** Add inline citations in Sec VI B to the parity-violation literature in refs [16]–[23], and prune any truly uncited refs.

### P4-M20 — Table III bandpower σ values are unverifiable from displayed numbers (Page 5)
Table III bandpowers:
- ℓeff=4: Cℓ = 3.210, σnull = 0.804, "Significance" = +6.097
- ℓeff=9: Cℓ = −0.248, σnull = 0.574, Sig = +2.232
- ℓeff=14: Cℓ = −0.387, σnull = 0.446, Sig = +2.626

Recompute assuming Sig = Cℓ/σnull:
- ℓeff=4: 3.210/0.804 = +3.99 (not +6.10)
- ℓeff=9: |−0.248|/0.574 = 0.43 (not +2.23)
- ℓeff=14: |−0.387|/0.446 = 0.87 (not +2.63)

The displayed σ values require a null with a non-zero mean (subtraction) that is NOT shown. For ℓeff=4: if σ = (3.210 − μ)/0.804 = 6.097, then μ = −1.70. For ℓeff=9: μ = −1.53. For ℓeff=14: μ = −1.56. The null means are different per bandpower but never tabulated. **Required fix:** Add a "⟨Cℓ^null⟩" column to Table III; without it the σ values cannot be reproduced by a reader.

### P4-M21 — Table II Catalog C deviation arithmetic actually checks out — corrects first-pass P4-E4 (Page 4)
**Self-correction of earlier finding.** Using exact CW count 1,592,107 / 3,201,160 = 0.497353…, then (0.497353 − 0.5)/0.000279 = −9.50. So the "9.5σ" in Table II is correct. My first-pass finding P4-E4 incorrectly used 0.4974 instead of 0.497353. **However**, the +2.05%/−0.53% vs +0.79%/−0.26% discrepancy of P4-E5/P4-M17 remains valid. P4-E4 should be retracted; the Catalog A and Catalog B Dev numbers should still be checked independently.

### P4-M22 — App A "Monopole subtraction increases σ from +1.85 to +3.64" is the *opposite* of what monopole subtraction should do under the abstract's interpretation (Page 7)
Appendix A states monopole subtraction **reduces** C₁ from 2.30×10⁻⁵ to 1.51×10⁻⁵ but **increases** significance from +1.85σ to +3.64σ. This means the subtracted-monopole null is much narrower than the un-subtracted null. The mathematical consequence: the +3.64σ is **not** an artifact of monopole-mask leakage as the abstract claims. Monopole leakage would inflate the un-subtracted significance; subtracting the monopole should reduce both the value and the significance if leakage was the cause. The fact that subtraction *increases* significance means the residual signal is NOT monopole-correlated — it's something else (depth/morphology systematic per App D, but NOT leakage). **Required fix:** Remove the abstract's phrase "+3.64σ canonical-mask residual is consistent with monopole leakage" — Appendix A's numbers contradict this.

### P4-M23 — Catalog A "+6.48σ pre-MASTER pseudo-Cℓ" and "Catalog A 2.31σ real-space dipole" — neither null is specified (Page 4, Sec IV C)
Sec IV C states:
> "Catalog A (raw) shows a 2.31σ real-space dipole and a +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower"

Neither significance has its null procedure stated. The +6.48σ is presumably against an isotropic Monte Carlo or label-shuffle null; the 2.31σ is presumably the isotropic-null bootstrap. But these σ values are juxtaposed with the +0.43σ Catalog C value as if directly comparable — **the very issue the abstract flagged as a known reporting hazard**. **Required fix:** Annotate every Catalog A and B σ with the null and N_MC used.

---

## MINOR / NITPICK findings (additional)

### P4-N1 — Appendix A "C² 2°" apodization notation undefined (Page 7)
"C² 2° apodization" appears repeatedly without a definition or NaMaster citation. C2 apodization in NaMaster has a specific functional form; quote it or cite. Same for App D.

### P4-N2 — "the production model's best checkpoint was at epoch 79" but early stopping patience=15 and total budget=80 (Page 7, App B)
Best at epoch 79 of 80 with patience 15 means the model was still improving at the very end of training. Typically one extends training when this occurs. Either the training budget was undersized or the patience criterion was not actually applied. Worth a brief comment.

### P4-N3 — Acknowledgments AI-tool disclosure is too brief for PRD requirements (Page 10)
> "Large-language-model tools were used for code review and manuscript editing"

PRD's AI-tool policy requires specific disclosure of which tools and which sections. "Code review and manuscript editing" is too vague. **Required fix:** Name the specific LLM(s) (e.g., GPT-4, Claude) and the specific manuscript portions edited.

### P4-N4 — Reference [2] (PASJ 74, 1114, 2022) has no arXiv ID provided, only DOI (Page 10)
Inconsistent with the rest of the bibliography style where arXiv IDs are uniformly provided. Add arXiv ID or note "no preprint."

### P4-N5 — Section title "VI. DISCUSSION" / "A. Sensitivity Floor and Minimum Detectable Signal" mixes scope: sensitivity is methodology, not discussion (Page 6)
Move Sec VI A to a Methods or Results subsection; Discussion should contextualize, not present new numerical thresholds.

### P4-N6 — Title acronyms: "TTA" undefined in title (Page 1)
"Test-Time Augmentation" (TTA) is jargon; spell out in the title or remove. PRD titles should be accessible.

### P4-N7 — "8.47 Million" in title but full paper uses "8.47 M" or "8,474,531" inconsistently
Casing/format conventions. Pick one ("M" with non-breaking space) and apply uniformly.

---

## Summary of new vs. initial findings

The initial review identified 13 essential, 15 major, 1 minor findings (29 total).
This pass adds **4 essential, 8 major, 7 minor** (19 additional findings).
Notable: P4-M21 is a self-correction of P4-E4 — the Table II Catalog C arithmetic actually checks out when one uses 0.497353 instead of the displayed 0.4974. The +2.05%/−0.53% inconsistency (P4-M17) is the substantive Table II vs IV B problem and stands.

Most important new findings: **P4-E14** (sensitivity argument is circular), **P4-E15** (mask-weight mislabeled as sample size in abstract), **P4-E16** (injection-recovery on wrong sample), **P4-M19** (~17 uncited references in bibliography), **P4-M22** (Appendix A numbers directly contradict abstract's "monopole leakage" interpretation of the +3.64σ residual).