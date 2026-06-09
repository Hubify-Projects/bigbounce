# P4 auto-2026-06-08_2353pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (15347 chars)
**Wall time**: 668.5s

---

# Referee Report — P4

**Title:** "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null..."
**Format:** PRD methods paper, 13 pp.

This is a paper with a defensible null cosmological result wrapped in a self-undermining title and abstract, multiple internal-consistency failures between figures, tables and body text, and several pieces of clearly visible review-process residue. The science is plausible but the manuscript is not in submittable form.

---

## ESSENTIAL findings

### P4-E1. Figure 2 numbers contradict the body and are mislabeled.
**Section IV A / Fig. 2 caption (page 6):**
Body text (Sec. IV A): "Catalog C (equivariant): CW 1,592,107 (18.78%), CCW 1,609,053 (18.99%), NS/edge-on 5,273,371 (62.23%); spiral total N_spiral = 3,201,160 (37.78%)."
Figure 2 (Catalog class breakdown): "CW 1,687,069 (19.9%), CCW 1,634,726 (19.3%), Not-Spiral 5,152,736 (60.8%)."

These are different numbers. Worse, the sign of the chirality excess in the figure is **reversed**: the body has CCW > CW (consistent with f_CW = 0.4974 deficit), the figure has CW > CCW (1,687,069/3,321,795 = 0.5079, which is the **Catalog A raw** fraction). The caption nevertheless says "Catalog C composition. ...the equivariant TTA classifier (§III C) assigns..."

This is not a rounding issue — the spiral total in the figure is 3,321,795 vs 3,201,160 in the body (120 k galaxy mismatch), and the chirality sign is inverted. Either the figure is showing Catalog A under a Catalog C caption (almost certainly the case), or the body text is wrong. Either way the headline f_CW = 0.4974 and N_spiral = 3,201,160 numbers used throughout the analysis cannot both be correct.

**Required fix:** Regenerate Figure 2 from the Catalog C numbers actually used in the analysis, or correct the caption/body to match.

### P4-E2. Figure 4 caption does not match the figure.
**Section IV D / Fig. 4 caption (page 8):**
Caption states: "Top: ℓ = 1 dipole power. Bottom: ℓ = 2 quadrupole."
The figure is a **single panel** bar chart of C_ℓ vs multipole at ℓ = 1, 2, 3, 4, 5. There is no Top/Bottom split. In addition, the figure carries the inline sigma labels "2.7σ" (at ℓ=1) and "2.5σ" (at ℓ=5) which match **no tabulated value** in the paper — Table III gives ℓ=1 single-mode at −0.122σ (subsample) and +3.64σ (canonical), and the broadband ℓ_eff = 4 value is +6.097σ. The labels 2.7σ / 2.5σ are unsourced.

**Required fix:** Rewrite the caption to describe what is actually plotted, and resolve the provenance of the 2.7σ / 2.5σ annotations against Table III.

### P4-E3. Visible "in queue" / version-history language in the body.
**Page 5, footnote 1:** "A parallel rerun on N(p)all-trial draws is **in queue** for the canonical-mask sensitivity-budget recompute." and "The **previous wording** 'Binomial(n_total, p_CW^global)' was ambiguous between N_spiral(p) and N(p)_all..."

These are review-loop artifacts: (i) "in queue" announces an unfinished computation in a paper being submitted as a final result; (ii) "previous wording" is an internal correction record. PRD does not publish in-queue computations or wording-change retrospectives. Furthermore the footnote concedes that "the size of the resulting shift in the headline 99.3% reproduction figure ... is not predictable analytically", which directly weakens the abstract's "reproduced at 99.3% of its observed amplitude" claim.

**Required fix:** Either run the N_all variant before submission and report a single internally-consistent number, or remove the qualifier and footnote and state plainly that the result is conditional on the N_spiral trial pool.

### P4-E4. The "+3.64σ headline" is contradicted by the empirical rank inside its own definition.
**Abstract; Sec. IV D; Sec. VII a:** "+3.64σ (z = Δ/σ_null moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent ...)"

Quoting a result as "3.64σ" while in the same sentence acknowledging the empirical-rank p-value translates to ≈1.9σ Gaussian-equivalent is precisely the kind of σ-inflation that the brutal-honesty standard rejects. The actual rank-based significance is ~1.9σ; the 3.64σ value is a moment ratio whose tail is not Gaussian. The dominant reported figure throughout the paper, including in the title in spirit ("3.64σ canonical-mask residual"), should be the rank-based number or both, prominently. As written, headline σ values are not earned.

**Required fix:** Demote 3.64σ from "headline" framing or report it consistently alongside the rank-based 1.9σ at every appearance, including the table.

### P4-E5. A_95 ≈ 1.5–2% is asserted but not demonstrated.
**Abstract; Sec. VII d:** "A_95 ≈ 1.5–2% is the amplitude at which the present injection-recovery analysis would have detected a signal at ≥95% probability."

Sec. VI A only reports injection results at A = 0.5% (P(σ > 3) = 0.15) and A = 0.75% (P(σ > 3) = 0.55). There is no reported point at A ≳ 1.5%. The 95% recovery amplitude is not measured — it is extrapolated from two points, and the manuscript never says so. The entire falsification criterion in the abstract is built on this extrapolated number.

**Required fix:** Either show the injection curve out to ≥95% recovery, or state explicitly that A_95 is an extrapolation and bound the extrapolation uncertainty.

### P4-E6. Hemisphere LEE: direct-MC vs Bonferroni numbers are inconsistent.
**Table I; Appendix C c:** Table I quotes "p_LEE ≤ 10⁻⁴" for the hemisphere maximum-asymmetry max-stat MC. Appendix C then says "the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ."

A direct-MC max-stat test already incorporates the look-elsewhere effect; Bonferroni is normally a *more* conservative (looser) bound on the same quantity, but it cannot legitimately *reverse* the conclusion of a max-stat MC that has already absorbed LEE. The text waves this away by attributing the MC rejection to the global classifier monopole, but the Table I entry still advertises "p_LEE ≤ 10⁻⁴" in a row whose interpretation in the body is "<1σ after correction." This is exactly the kind of σ-inflation a referee must flag.

**Required fix:** Reconcile the two numbers, or report both with explicit explanation of why direct-MC and Bonferroni disagree by >4σ. Do not present "p_LEE ≤ 10⁻⁴" in a summary table when the paper's actual reading of that test is <1σ.

### P4-E7. Two different "headline" findings.
**Abstract:** "The headline scientific result is a null ℓ = 1 chirality-dipole observable on the analysis subsample mask."
**Sec. VII Conclusions item (a):** "Headline finding: a quantifiable monopole-mask leakage channel."

A PRD paper may not have two different headline findings in two different places. Pick one.

**Required fix:** Choose one headline framing and use it consistently in title, abstract, and conclusions.

---

## MAJOR findings

### P4-M1. Title is unreadable and self-defeating.
The title is 60+ words, includes three separate findings, two precise numbers (−0.122σ and 8.47 million), and the parenthetical "(3.2 Million Spirals)". PRD title norm is one declarative line. The current title also publishes a non-detection σ value (−0.122σ) in the title, which is unusual and not standard practice.

### P4-M2. Abstract is over length and runs as a narrative essay.
The abstract is roughly 700 words and contains: a falsification criterion, scope statement, three numbered interpretations, a four-null battery summary, cross-spectrum numbers, and an editorial "we emphasize at the outset" preamble. PRD abstracts are typically ≤ 250 words. As written, the abstract reads like a section, not an abstract.

### P4-M3. ≥15 references appear in the bibliography but are never cited in the body.
References [13]–[30] (with the exception of [29] DESI which is partially used and [12] ViT which is used) are not cited anywhere in the body text I can find — including Gross & Vitells [13], SpArcFiRe [14], Motloch [15], Lue–Wang–Kamionkowski [16], Cabass [17], Philcox [18], Eskilt [19], Cosmoglobe [20], Hou–Slepian–Cahn [21], Cahn–Slepian–Hou [22], Komatsu [23], Hayes [24], Bamford [25], Hart [26], Walmsley DECaLS [27], Yu [28], DESI [29], LSST [30]. The "Software" line at the end cites [31, 34, 35, 36, 37, 38, 39] but **omits citation numbers for NaMaster/pymaster**, whose actual references [32, 33] are uncited there.

**Required fix:** Cite each reference at the point where it supports a claim, or remove it from the bibliography. Fix software-list citations.

### P4-M4. Novelty claim "advancing beyond CE-ResNet" is undermined by training-label provenance.
Sec. II B: "67.6% of training labels derive from CE-ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth." This is acknowledged, but the same paragraph elsewhere argues the new classifier "advances beyond CE-ResNet" in three respects. Distilling CE-ResNet labels into a ViT and scaling to a larger sample is engineering, not classifier-level scientific advance. The independent-ground-truth GZ1 cross-match yields only 69.9% / κ = 0.40 ("fair" agreement). The bibliography call to "advancing beyond" CE-ResNet should be tempered.

### P4-M5. σ values from different nulls juxtaposed without per-instance non-comparability flags.
Per the review standard. The abstract carries one global non-comparability note, but the same juxtaposition recurs in Table I, Conclusions ("the full-catalog real-space dipole at +0.43σ and the subsample-mask MASTER at −0.122σ"), and Sec. IV C–IV D, each time without the reader being re-warned that these are not Gaussian-equivalent. In a table that mixes label-shuffle, bootstrap, max-stat MC, and monopole-only nulls in adjacent rows (Table I) this is dangerous.

**Required fix:** Add an in-table footnote to Table I stating each σ is conditional on its own null and cannot be combined. Re-state the caveat at the conclusions juxtaposition.

### P4-M6. Reference numbering is non-monotonic, with citation-order inverted relative to appearance.
The introduction (page 2) cites "Shamir (2012) [4]", "Shamir (2020) [1]", "Shamir (2022) [3]" in that order. PRD convention is numerical-by-order-of-appearance. This appears either an artifact of a switched citation style or a leftover from a prior version.

### P4-M7. The "monopole-only null reproduces 99.3% of pre-MASTER pseudo-C₁ power" claim is conditional on a trial-pool choice the paper itself admits is ambiguous.
See P4-E3. Restated as a science claim: the 99.3% figure is the headline of Sec. IV D and Sec. VII (a). The footnote concedes that the alternative trial-pool choice would shift this number by an unknown but non-negligible amount. The paper cannot claim "99.3%" as a tight diagnostic while simultaneously saying the value is "not predictable analytically" and an alternative computation is pending.

### P4-M8. The "9.5σ monopole" framing.
Sec. IV B: the global f_CW = 0.4974 deviation is reported as "9.5σ from 0.5000," where σ is the binomial standard error on a sample of 3.2 M. Calling a known classifier artifact "9.5σ" is technically correct but rhetorically misleading: the paper then uses this 9.5σ language to motivate the leakage analysis as if a real physical anomaly required explanation. The classifier-monopole interpretation is correct; the σ framing inflates the apparent problem. Recommend reporting f_CW − 0.5 = −0.0026 ± 0.0003 (5σ deficit on classifier-bias scale) and dropping the "9.5σ monopole" phrasing.

### P4-M9. Cross-spectrum r_{ℓ=2} = −0.65 (σ = −2.89).
A −2.89σ value from a permutation null is moderate at best. The abstract and Sec. IV E describe this as a definitive third independent line of evidence against interpretation (i) — but −2.89σ is roughly 1-in-200 against a null that itself is not look-elsewhere-corrected (one chooses ℓ = 2 having seen the auto-spectrum quadrupole excess). At face value this is consistent with a depth-correlated systematic but not strong evidence; the rhetoric in the abstract overstates.

### P4-M10. "Strict-superset subsample mask" terminology is confusing.
Sec. IV C and Appendix A: the "subsample" mask has *higher* f_sky (0.659) than the canonical mask (0.49005), so it is in fact a *superset* of the canonical mask. Calling it "subsample" inverts the natural reading. The masking-construction logic (relaxed per-pixel threshold) should be described mechanically — "less restrictive per-pixel cut" — rather than with a name that points the wrong way.

### P4-M11. Edge-on contamination at 65.7% is large and the "mitigation" is informal.
Sec. VI A and Appendix E a: 65.7 % of b/a < 0.3 (edge-on) objects receive CW or CCW labels rather than NS. The mitigation argument is that flip-equivariance enforces symmetric CW/CCW assignments on flip-symmetric inputs. That is true on average but does not mitigate per-pixel scatter — an edge-on galaxy can still be flipped to a definite CW or CCW label depending on which side wins the noisy probability split. The 10–15 % effective-N reduction estimate is asserted without derivation.

### P4-M12. Sensitivity-floor argument leaks the classifier-noise dilution factor.
Sec. VI A: "GZ1-dilution factor g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼1.88%." If the dilution-corrected threshold is 1.88 %, then the constraint on a physical dipole is 1.88 % (50%-recovery) and ≳ 4 % at 95 % recovery — not 0.75 % / 1.5–2 %. The abstract's headline "sub-percent" sensitivity language is the **classifier-projected** sensitivity. A reader could easily conclude the constraint on the underlying physical signal is sub-percent; it is not. The paper should clearly distinguish "classifier-channel A_50 = 0.75 %" from "underlying-isotropy A_50 = 1.88 %".

### P4-M13. T7 "calibration: qualitative PASS" in Table V is not a passing criterion.
A "qualitative" pass with the column "Threshold" reading "qualitative" is not a test. Either define a quantitative pass/fail or remove from the table.

---

## MINOR findings

### P4-mi1. Table III ℓ_eff = 4 significance not internally consistent at the displayed precision.
Row ℓ_eff = 4 has C_ℓ = 3.210 × 10⁻⁶, σ_null = 0.804 × 10⁻⁶, significance +6.097. Naively 3.210/0.804 = 3.99, so the null mean must be ≈ −1.69 × 10⁻⁶ for the moment ratio to give 6.097. The null mean is not displayed in the table and should be, otherwise the σ column is not auditable.

### P4-mi2. Table IV z arithmetic.
Pre-MASTER row: (1.696 − 1.685) × 10⁻² / 0.007 × 10⁻² = 1.57, table reports +1.68. Likely a rounding issue (uncertainties displayed to two sig figs), but the reader cannot reproduce the number from the displayed inputs.

### P4-mi3. Hemisphere row of Table IV: z = (3.48 − 1.69)/0.41 = 4.37, table reports +4.42. Same rounding ambiguity.

### P4-mi4. Section IV.B states P(σ > 3) = 0.55 at A = 0.75% but the abstract calls this the "50%-recovery" threshold.
55 % ≠ 50 %. Either re-quote A_50 by interpolation between 0.5 % (15 %) and 0.75 % (55 %), or call it "≈55%-recovery". Cosmetic but it propagates everywhere.

### P4-mi5. Abstract: "isotropic-null bootstrap, N_MC = 10,000" appears twice for the same number with slightly different framings.

### P4-mi6. "MASTER" is used both for the algorithm (Hivon et al.) and informally as a verb ("MASTER decoupling removes...", "MASTER deconvolves..."). At least once at first use, write "mode-coupling (MASTER) deconvolution."

### P4-mi7. Section IV.D footnote crosses pages — long single footnote runs more than half a page, which is poor typography.

### P4-mi8. Sec. VI B parity-violating-sectors paragraph is hand-wavy.
"A mapping onto primordial parity-violating tensor amplitudes requires a transfer function ... that transfer function is not derived in this paper and is left to follow-up theory work." The paragraph then immediately claims the present null "disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥ 0.75 %". This is a circular statement — without the transfer function, "morphology-channel dipole" is not a primordial-sector observable. Either delete the paragraph or state that it is an empirical, not theoretical, constraint.

### P4-mi9. Footnotes-in-abstract style: the abstract's "Note:" qualifier is non-standard for PRD.

### P4-mi10. Sec. III B: equation (1) "softmax" should be in roman type. Eq. (B1) likewise: "L_CE" vs "L".

### P4-mi11. Cohen's κ = 0.40 reported as "we treat 69.91% as the conservative accuracy floor" — but Cohen's κ already accounts for chance agreement, so it is the more defensible quantity. The text picks the larger number for headline framing.

### P4-mi12. "Catalog tags A/B/C" terminology overlaps with "Catalog C dipole at +0.43σ" — adopt a non-letter tag to avoid clash with bandpower / catalog cross-mentions.

### P4-mi13. The "AI tool usage" paragraph (page 12) is appropriate but could be moved to acknowledgments.

### P4-mi14. Some paragraphs repeat the same content verbatim (e.g., the +0.43σ / −0.122σ pairing appears at least 6 times — Abstract, §III A, §IV C, §VI, §VII, conclusions). Tighten.

---

## NIT

- **N1.** "anchored on" used repeatedly (≥ 6 times). Use "based on" or "rests on" for variety.
- **N2.** "subsample-mask" / "canonical-mask" hyphenation is inconsistent in places.
- **N3.** Eq. (1) — the architecture description in a numbered equation is non-standard; usually presented as text or a table.
- **N4.** Bibliography entry [35]: missing title.
- **N5.** Tables I and IV use different decimal precisions for σ (two vs three significant figures).
- **N6.** "headline" used 9+ times — at this density the word is meaningless.
- **N7.** "DOI:" prefix inconsistent across references.

---

## Recommended page count
For the genuinely new content — a 3.2 M-spiral catalog, a TTA-equivariant chirality classifier, and a null dipole measurement — a tight 7–9 page submission would be appropriate. The current 13 pages are inflated by the extensive defense of a residual that the paper itself disowns as a systematic.

---

## Summary recommendation

**REJECT** (resubmittable after major revision).

The science is plausibly correct and the null result is plausibly publishable, but the manuscript as submitted fails PRD's basic standards on multiple independent axes: Figure 2 directly contradicts the body's Catalog C numbers and the chirality sign; Figure 4's caption does not describe the figure; the abstract and conclusions disagree on what the "headline finding" is; visible "in queue" and "previous wording" language reveals an unfinished computation; the falsification amplitude A_95 is asserted but not measured; the "+3.64σ" headline is internally acknowledged to be ≈1.9σ on its own rank statistic; the LEE row of Table I disagrees with its own discussion by >4σ; ≥15 references are uncited; the title and abstract are oversized; the novelty framing is undermined by training-label provenance from CE-ResNet itself; and the distinction between classifier-channel sensitivity (~0.75%) and underlying-physical-isotropy sensitivity (~1.88%) is not communicated to the reader. Each of these is fixable, but the cumulative count is not consistent with a publishable PRD submission at first pass.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P4 (Second Pass)

After re-examining the manuscript with the checklist criteria, I found multiple additional issues, including several arithmetic/internal-consistency failures and one major figure/abstract inversion I hinted at but didn't pursue fully in the first pass.

---

## ADDITIONAL ESSENTIAL findings

### P4-E8. Section IV B "+2.05% to −0.53%" and "3.86× suppression factor" contradict Table II.
**Sec. IV B (page 4):** "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates the dominance of the equivariant TTA processing."

Table II gives:
- Catalog A (raw): f_CW = 0.5079 → excess (f − 0.5) = +0.79%, or asymmetry 2(f − 0.5) = +1.58%.
- Catalog C (eq): f_CW = 0.4974 → excess −0.26%, asymmetry −0.52%.

Under either convention:
- The "−0.53%" matches the asymmetric convention for Catalog C (≈ −0.52%). ✓
- The "+2.05%" matches **neither** convention for Catalog A (0.79% nor 1.58%). ✗
- The "3.86×" factor (= 2.05/0.53) is therefore wrong. The correct factor under either convention is 1.58/0.52 = 3.04× or 0.79/0.26 = 3.04×.

This is not a rounding issue — 2.05% vs 0.79% is a >2× discrepancy. **This is a stale number from an earlier version of the analysis.** It propagates the "dominance of equivariant TTA" claim with an inflated effect size.

**Required fix:** Replace "+2.05%", "−0.53%", "3.86×" with values consistent with Table II.

### P4-E9. The headline +3.64σ is an artifact of monopole-subtraction convention.
**Appendix A (page 9):** "Monopole subtraction reduces decoupled C₁ at ℓ = 1 from 2.30 × 10⁻⁵ to 1.51 × 10⁻⁵ (∼ 34%) **and increases σ from +1.85 to +3.64** (the canonical-mask number)."

Without artificial monopole subtraction, the canonical-mask post-MASTER significance is **+1.85σ**, not +3.64σ. The body text and abstract present +3.64σ as **the** canonical-mask residual without disclosing that the unsubtracted value is roughly half. The abstract characterizes this as occurring "under **proper** galaxy-weighted monopole subtraction" — the word "proper" is editorial. On a partial sky, subtracting a mask-mean rather than a true ℓ=0 mode does not orthogonally remove monopole power; it can inject power into ℓ ≥ 1. That this subtraction nearly doubles the apparent ℓ=1 significance suggests precisely such injection.

The conservative number to headline is +1.85σ (unsubtracted), not +3.64σ (subtracted), and certainly not +3.64σ without disclosing that the unsubtracted value exists and is much smaller. Combined with the already-acknowledged empirical-rank 1.9σ (P4-E4), the actual "anomaly" the paper expends Appendix D defending is in the 1.8–1.9σ range.

**Required fix:** Either headline +1.85σ (unsubtracted) or report both prominently and justify the subtraction choice on the partial sky. Drop the editorial "proper".

### P4-E10. Abstract attributes +3.64σ to monopole-mask leakage; Appendix D attributes it to depth/PSF/morphology systematics.
**Abstract:** "The +3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry (Sec. IV D) and is not interpreted as a cosmological signal."

**Appendix D (g):** "The most likely explanation is a per-pixel-correlated systematic at low ℓ on the canonical footprint (**depth/PSF/morphology**), supported by: (a) ℓ = 2 cross-spectrum quadrupole anti-alignment at r_ℓ=2 = −0.65 ... (b) 25% leg-stratified ℓ = 1 contribution; (c) density-stratified-null residual +3.80σ..."

These are different physical channels. The monopole-mask leakage channel is what produces the **pre-MASTER** +6.48σ → reproduced at 99.3% by the monopole-only null. The **post-MASTER** +3.64σ is what survives that channel and is attributed in Appendix D to **independent** depth/PSF/morphology systematics. The abstract collapses these into the wrong attribution.

**Required fix:** Distinguish pre-MASTER (monopole-mask leakage) from post-MASTER (depth/PSF/morphology) attributions in the abstract, conclusions, and Sec. IV D.

### P4-E11. Sec. VI B's null-disfavoring statement uses A_50, not A_95.
**Sec. VI B:** "The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole **≥ 0.75%** on the DESI Legacy footprint, including the Shamir ∼3% amplitude class by a factor of ∼6–12."

A = 0.75% is the **50%-recovery threshold**. A null at this amplitude is consistent with 50% of true signals being missed. By the paper's own falsification framing (Sec. VII d), the disfavoring threshold is A_95 ≈ 1.5–2%, not A_50. Using A_50 here is the same σ-inflation the paper criticizes elsewhere.

**Required fix:** Change ≥ 0.75% to ≥ A_95 ≈ 1.5–2%, and update the "factor of 6–12" accordingly (with the underlying-physical-isotropy dilution factor applied — see also P4-M12 from the first pass).

---

## ADDITIONAL MAJOR findings

### P4-M14. Training-set composition arithmetic fails.
**Sec. II B:** "(1) Galaxy Zoo 1: 6,637 galaxies; (2) CE-ResNet: 17,153 galaxies; (3) Synthetic hard negatives: 2,000 ... The combined training set contains **26,636 images**."

6,637 + 17,153 + 2,000 = **25,790**, not 26,636. There are 846 unaccounted images.

The paper also states "**67.6%** of training labels derive from CE-ResNet predictions". The computed fractions are:
- 17,153 / 25,790 = 66.5% (using the component sum)
- 17,153 / 26,636 = 64.4% (using the stated total)

Neither gives 67.6%. The 67.6% figure is unsupported by the numbers as printed. This matters because the paragraph builds the conservative-accuracy-floor argument around the CE-ResNet contamination fraction.

**Required fix:** Reconcile the component counts with the total and report a single internally-consistent CE-ResNet fraction.

### P4-M15. 21 references (not "≥15") are uncited in the body, and three of them are foundational.
A precise recount of citations in body text vs. bibliography reveals 21 uncited refs: [2], [11], [13]–[30], [33].

Of these, three are foundational and their non-citation is a real problem (not bib bloat):
- **[33] Hivon et al. (2002) — the original MASTER paper.** "MASTER" appears 30+ times in the paper as the central methodology; the foundational reference is uncited.
- **[24] Hayes, Davis, Silva (2017) — "On the nature and correction of the spurious winding bias in Galaxy Zoo 1".** The paper explicitly attributes the classifier monopole to "GZ1 human-handedness training bias propagating through CE-ResNet pseudo-labels" (Data Availability). Hayes et al. is the canonical reference for this exact effect and is not cited at the attribution.
- **[29] DESI Aghamousa et al. (2016) — the DESI experiment paper.** Despite DESI being central to the data, the experiment paper is uncited; only the Legacy Imaging paper [8] is cited.

**Required fix:** Cite [33] at every "MASTER" mention or first-use; cite [24] at the GZ1-bias attribution; cite [29] where DESI is introduced. Remove genuinely unused refs.

### P4-M16. Sec. V A "30× extension" arithmetic.
**Sec. V A:** "These conclusions corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2 × 10⁶ spirals (**30× extension**)."

Iye et al. analyzed Shamir's SDSS spiral catalog of "1.27 × 10⁵ SDSS galaxies" per the same paper's intro. 3.2 × 10⁶ / 1.27 × 10⁵ = **25.2×**, not 30×. A modest overstatement of the catalog-size factor.

**Required fix:** Replace "30×" with "25×".

### P4-M17. The "factor of 6–12 below Shamir" compares two different observables.
**Abstract; Sec. V A:** Shamir's reported amplitude is **a dipole** of 2–4%; the present paper's "0.32% maximum regional asymmetry" (Sec. V A, undefined precisely) is **a per-region maximum**. The ratio 2–4% / 0.32% ≈ 6–12 is computed across these different quantities.

The valid like-for-like comparison is either:
- Shamir's dipole 2–4% vs the present dipole upper limit (real-space 0.43σ → A_50 = 0.75% empirical, so ~2.7–5×), or
- Shamir's per-region asymmetry (not the 2–4% figure) vs our 0.32%.

The 6–12× factor is sloppy.

**Required fix:** Compare on the same observable; recompute the factor.

### P4-M18. Sec. VI A Fisher floor uses f_sky = 0.46, undocumented.
**Sec. VI A:** "The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at N_spiral = 3,201,160, **f_sky = 0.46**)."

The canonical mask f_sky is **0.49005** (Sec. IV D); the subsample mask is 0.659. There is no f_sky = 0.46 defined anywhere else in the paper. This is either a stale number or an undefined effective f_sky. The Fisher floor scales as 1/√f_sky, so the choice matters.

**Required fix:** Either rederive using the documented f_sky, or define what the 0.46 refers to (e.g., apodized effective f_sky).

### P4-M19. The 0.32% "maximum regional asymmetry" is undefined.
**Sec. V A:** "Under the present ViT/TTA pipeline, our maximum regional asymmetry is 0.32%..."

This is the load-bearing number in the Shamir comparison (P4-M16). Yet the paper never defines what region, what statistic, or what mask gave 0.32%. Is it max|A_p| over HEALPix pixels at NSIDE=64? Hemisphere maximum? A fitted-dipole amplitude on a subdomain? The reader cannot tell.

**Required fix:** Define the quantity and the procedure, or remove the number.

### P4-M20. Asymmetric treatment of ℓ=1 vs ℓ=2 parity content.
The paper's parity framing is technically correct: for the pseudoscalar chirality field A, even-ℓ multipoles (including ℓ=2) are the parity-odd modes, while odd-ℓ multipoles (including ℓ=1) are parity-even. The abstract emphasizes prominently that ℓ=1 is parity-even and "NOT a direct parity-violation test."

But Table III's ℓ_eff=4 (ℓ ∈ [2,6]) result is +6.097σ — and this **is** in the parity-odd channel. The paper dismisses this as "Mask-coupled monopole leakage" (table) and depth-correlated systematic (Appendix D). The dismissal is plausible, but the asymmetric framing — emphasizing parity content of ℓ=1 in the abstract while quietly attributing the parity-relevant ℓ=2 to systematics — is not transparent. A paper that opens its abstract by warning readers about prior literature conflating parity-even and parity-odd channels should be explicit that its largest excess (+6.097σ broadband ℓ_eff=4) sits in the parity-violating channel of the chirality field, even if attributed to systematics.

**Required fix:** Add explicit discussion in Sec. VI B that the ℓ=2 broadband excess sits in the parity-odd channel and explain why the systematic attribution there is robust enough that it does not constitute a parity-violation detection.

---

## ADDITIONAL MINOR findings

### P4-m14. Table II "Dev." column slightly inflated under stated precision.
With σ = 0.000279 displayed:
- Cat A: 0.0079/0.000279 = **28.32**, table reports 28.8.
- Cat B: 0.004/0.000279 = **14.34**, table reports 14.6.
- Cat C: 0.0026/0.000279 = **9.32**, table reports 9.5.

All three are systematically rounded up. Within rounding tolerance of the inputs, but the consistent direction suggests a slightly smaller σ was used internally than displayed. Either display σ to more precision or report Dev. to match.

### P4-m15. Table III ℓ_eff = 4 row implies a negative null mean of −1.69 × 10⁻⁶ that is not displayed.
For C_ℓ = 3.210 × 10⁻⁶, σ_null = 0.804 × 10⁻⁶, and significance = +6.097σ:
μ_null = 3.210 − 6.097 × 0.804 = **−1.69 × 10⁻⁶**.

A negative MASTER-deconvolved C_ℓ null mean is not unphysical, but is striking enough to deserve display. As printed, the reader cannot reproduce the +6.097σ figure from the table.

**Required fix:** Add a "null mean" column to Table III.

### P4-m16. 8,474,531 vs 8,474,688: 157-galaxy QC failure not documented.
**Sec. IV A:** "157 of 8,474,688 failed quality checks". The QC procedure that culls 157 galaxies is not described anywhere in the main text. Trivial in fraction, but unaudited.

### P4-m17. Sec. V A "factor of ∼ 6–12" appears in abstract too.
The same comparison (P4-M16) is repeated in the abstract without the qualifier that it compares different observables: "inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼6–12 under the present pipeline". Same issue, more prominent location.

### P4-m18. Sec. IV C says "real-space dipole significance 0.43σ (p=0.30...)", but a Gaussian 0.43σ gives one-sided p=0.334 and two-sided p=0.668. p=0.30 is the empirical bootstrap p-value, which is fine, but the reader is not told whether it is one- or two-sided.

### P4-m19. Sec. III C: D₄-TTA validation reports "sign-flip of the argmax-CW-fraction shift (−1.35% at N = 1,558 vs +2.11% at N = 1,988)" as confirmation of sample noise. This is at the catalog tail and N ~ 2000 is small relative to the 471k HC subsample used elsewhere — the relevance to production-scale stability is asserted rather than demonstrated.

### P4-m20. Sec. VII a: "MASTER decoupling removes the leakage." But +3.64σ remains. The framing reads as if leakage were eliminated; the body says it is reduced (and a different systematic survives). Soften.

### P4-m21. Sec. III B: training-loss equation B1 uses L_CE (calligraphic) but the text intro uses "class-weighted cross-entropy" without defining the weights.

### P4-m22. Sec. IV D / Table IV: "Hemisphere max|A| (NSIDEdir=8)" with data 3.48×10⁻³ vs null (1.69±0.41)×10⁻³ gives z = (3.48−1.69)/0.41 = **4.37**, table reports +4.42. Within rounding (P4-mi3 from first pass), but for a number quoted to three significant figures the recompute should match.

---

## NITS

- **N8.** Abstract "Note:" sentence break is non-PRD typography.
- **N9.** "MASTER" capitalization is inconsistent in body — sometimes the algorithm acronym, sometimes used as a verb.
- **N10.** Sec. II B "67.6%" is stated to one decimal place precision; if recomputed correctly to either 64.4% or 66.5%, the misalignment is at the 1.1–3.2 pp level — visible to a careful reader.
- **N11.** Sec. V A: "Shamir's claimed ∼3% signal" — Shamir's papers report a range of 2–4%; representing it as "∼3%" mid-point is fine but could be sourced explicitly.

---

## Summary of second-pass impact on recommendation

The first-pass recommendation of **REJECT (resubmittable after major revision)** stands and is strengthened, not weakened. The second pass added:

1. A clear arithmetic stale-number trail in Sec. IV B (P4-E8) that propagates a 25% overstated TTA-suppression factor.
2. Demonstration via Appendix A that the headline "+3.64σ canonical residual" is **doubled** by a debatable monopole-subtraction convention (P4-E9), bringing the headline σ for the canonical-mask anomaly closer to the empirical-rank ~1.9σ already conceded.
3. A misalignment between the abstract's monopole-leakage attribution and Appendix D's depth/morphology attribution for the same +3.64σ value (P4-E10).
4. A null-disfavoring statement (Sec. VI B) that uses A_50 instead of A_95, contradicting the paper's own falsification framing (P4-E11).
5. Failed training-set arithmetic (P4-M14) — a simple component-sum discrepancy that should not survive co-author review.
6. The unfilled "MASTER" foundational reference (P4-M15) — a citation gap that is genuinely embarrassing for a paper whose entire methodology rests on the technique.

The cumulative count of independently-flagged numeric or attribution inconsistencies is now in the 25+ range across two passes. The science is recoverable, but the manuscript is not ready for PRD submission in its current state.