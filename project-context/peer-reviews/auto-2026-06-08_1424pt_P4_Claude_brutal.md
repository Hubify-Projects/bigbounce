# P4 auto-2026-06-08_1424pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14213 chars)
**Wall time**: 544.3s

---

# Referee Report — P4

**Manuscript:** "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, ..."

---

## Overall Assessment

This is a long, inflated paper around what is fundamentally a null result with a side-finding about monopole-mask leakage in pseudo-Cℓ estimators. The methodology is mostly reasonable, the bias hardening is creditable, and the leakage demonstration is interesting pedagogically. However, the manuscript suffers from (i) internal-version-control leakage into the body text, (ii) a chosen "primary" estimator that conveniently gives the null while a co-equal estimator with larger fsky on the same catalog gives +3.64σ, (iii) recomputation failures on multiple table values, (iv) an excessive title and abstract, (v) orphan/uncited references, and (vi) overuse of σ-units from non-comparable nulls. As a PRD submission, this is not ready.

---

## ESSENTIAL findings

### P4-E1 — Internal-version-control / bookkeeping language in the body (multiple locations)
**Page 4, footnote 1 (Section IV.D):** The footnote explicitly references earlier wording, code-script paths, and pending recalculations:
- *"The previous wording 'Binomial(ntotal, p^global_CW)' was ambiguous..."*
- *"the code in scripts/monopole_null_generative.py uses Nspiral(p)..."*
- *"A parallel rerun on N(p)all-trial draws is in queue for the canonical-mask sensitivity-budget recompute and is expected to shift the per-pixel inflation by ⟨Nall/Nspiral⟩ ≈ 1.49..."*

**Page 4, Sec. IV.D body:** *"...were interpreted in earlier paper versions as mask-geometric leakage..."*

This is review-log / draft-history prose that has no place in a published PRD article. It also reveals (a) that the headline "99.3%" leakage-reproduction figure depends on a choice (Nspiral vs Nall) the authors themselves flag as ambiguous, and (b) that a key validation rerun has not been performed ("in queue"). **The "in queue" sentence alone is grounds for rejection of the current draft** — PRD does not publish analyses with pending computations whose outcomes are merely "expected" to be sub-0.1σ.

**Required fix:** Remove all draft-history language. Complete the deferred rerun and report the actual number, not the "expected" number. Confirm headline figures with the unambiguous trial-count choice.

---

### P4-E2 — Internal inconsistency on raw vs equivariant CW excess (Page 4 vs Table II)
Section IV.B states: *"The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%."*

But **Table II** reports Catalog A (raw) excess = **+0.79%** and Catalog C excess = **−0.26%**. 

- 0.79/0.26 = 3.04× (not 3.86×)
- 2.05/0.53 = 3.87× ✓ (so the text uses different numbers from the table)
- The Catalog C asymmetry A_eq = (CW−CCW)/(CW+CCW) = 2×(fCW−0.5) = −0.53% is internally consistent (with Table II's −0.26% excess being half of that), but this convention difference is never stated. Catalog A asymmetry A = 2×0.79 = 1.58%, **not 2.05%**.

These numbers cannot be reconciled with a single convention. Either Table II is wrong, the text is wrong, or there is an undisclosed pre-Platt raw asymmetry being quoted in the text. The reader cannot tell.

**Required fix:** Pick one convention, recompute, and reconcile Table II and Sec. IV.B.

---

### P4-E3 — The "+3.64σ" canonical-mask quantity is reported as σ but the empirical rank gives p = 0.030 (≈1.9σ Gaussian-equivalent). Authors acknowledge this but then propagate the 3.64 figure everywhere.
Abstract: *"+3.64σ (z=Δ/σnull moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent ..."*

A 2× discrepancy between a moment-ratio z and the empirical-rank p indicates the null distribution is **strongly non-Gaussian** — yet the manuscript continues to advertise "+3.64σ" in the title, abstract, multiple section headers, Table I, Table III, Sec. IV.D, Sec. VII.a, Appendix D, etc. This is misleading. The honest summary is "p_MC ≈ 0.03, i.e. ~2σ".

**Required fix:** Either drop the σ language in favor of pMC throughout, or restate every "+3.64σ" with the parenthetical "(empirical p = 0.03, ≈1.9σ Gaussian-equivalent)" attached at every occurrence — not just the abstract.

---

### P4-E4 — Recompute of Table II "Dev. (σ)" column disagrees with the displayed values
Using σ = 0.000279 (paper's stated 1σ binomial):
- Catalog A: (0.5079 − 0.5)/0.000279 = **28.32** (paper: 28.8) — off by 1.7%
- Catalog B: (0.504 − 0.5)/0.000279 = **14.34** (paper: 14.6) — off by 1.8%
- Catalog C: (0.4974 − 0.5)/0.000279 = **−9.32** (paper: 9.5) — off by 1.9%

A systematic ~2% offset suggests the σ used in computing the displayed Dev. column is not 0.000279. Either σ is wrong, or Dev. is wrong. Either way the table is internally inconsistent at the level the paper itself relies on (the "9.5σ" monopole is invoked repeatedly in Discussion and Conclusions).

**Required fix:** Recompute and reconcile, or state explicitly which σ was used (e.g., perhaps a different N).

---

### P4-E5 — Table IV row arithmetic fails recomputation
Pre-MASTER pseudo-C(ℓ=1): Data 1.696×10⁻², Null (1.685±0.007)×10⁻². 
Recompute z: (1.696 − 1.685)/0.007 = **1.57**, paper says **+1.68**.

Hemisphere max|A|: (3.48 − 1.69)/0.41 = **4.37**, paper says **+4.42**.

These are small discrepancies but the paper bases narrative on these exact figures. Either provide more decimal places or fix.

**Required fix:** Show enough precision that z-recomputes match, or fix the z column.

---

### P4-E6 — Orphan reference / uncited references
Reference [2] (Shamir 2022 PASJ 74, 1114) is not cited in the body. The Shamir citations in Sec. V.A are *"[1, 3, 4]"*.

Spot-check shows additional likely orphans: [11] Land et al. (2008), [14] SpArcFiRe, [15] Motloch et al., [16] Lue/Wang/Kamionkowski, [17] Cabass/Ivanov/Philcox, [18] Philcox, [19], [20], [21] Hou/Slepian/Cahn, [22], [23] Komatsu, [24] Hayes/Davis/Silva, [25] Bamford, [26] Hart, [27] Walmsley DECaLS, [28] Yu/Motloch, [29] DESI, [30] LSST, [33] Hivon (MASTER). Many of these appear to be reference padding to make the bibliography look complete.

**Required fix:** Either cite each reference at the relevant point in the body or remove it. PRD does not accept padded bibliographies.

---

## MAJOR findings

### P4-M1 — Title is excessively long and editorialized
The title runs ~70 words ("...A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)"). PRD titles are concise. Recommend cutting to something like *"Equivariant Test-Time-Augmented Chirality Analysis of 8.47M DESI Legacy Galaxies: A Null Dipole and a Monopole-Mask Leakage Diagnostic."*

### P4-M2 — Abstract is ~600 words and contains methodology, falsification criteria, and project repository announcement
PRD abstracts are typically ≤250 words. The current abstract reads as an executive summary of the paper plus a press release. Cut by at least half.

### P4-M3 — PACS codes are deprecated
"PACS numbers: 98.80.-k, 98.62.Ai, 95.75.Mn" — APS discontinued PACS in 2010 and replaced it with PhySH. Use PhySH descriptors.

### P4-M4 — Independence of the chirality null is compromised by training-label provenance
Section II.B: *"67.6% of training labels derive from CE-ResNet predictions"*. The paper acknowledges this but then proceeds to advertise the null as 1.6× CE-ResNet's coverage. In practice the classifier is partly a knowledge-distillation of CE-ResNet, which itself was trained on Galaxy Zoo. The "independent GZ1 cross-match accuracy of 69.91%" with Cohen's κ = 0.40 is **mediocre at best** — κ = 0.40 is "fair" agreement, not "substantial". The claim that the analysis is independent of CE-ResNet should be removed or substantially softened.

### P4-M5 — Choice of "primary" estimator is not principled
The headline "−0.122σ null" comes from the **subsample mask (fsky = 0.659)**, while a co-equal MASTER computation on the **canonical mask (fsky = 0.49005)** of the same catalog gives **+3.64σ**. The hierarchy declared in Sec. III.A elevates one to "primary" and the other to "secondary diagnostic". This is post-hoc — the difference between the two is a single mask choice, both are physically sensible, and the larger fsky is not in itself a sufficient reason to call one "primary" if the underlying physics question is identical. The decision should be justified pre-registration-style, not retrofit.

### P4-M6 — "Falsification criterion" wording overpromises
Abstract: *"A future survey detecting a chirality dipole at σ>5 with full amplitude ≳0.75% ... would falsify the present null."*

This is not a meaningful falsification criterion: it states only that a future detection would contradict a null. That is true by tautology. A genuine falsification criterion would specify a footprint, redshift range, and a quantitative discrepancy from a model prediction. Reword or remove.

### P4-M7 — Section IV.B reports the spatial uniformity of the monopole "across 7 equatorial coordinate slabs" but does not show this; it is delegated to "the companion data repository"
Either show this in a table/figure or do not make the claim load-bearing for the conclusion that "this monopole does not produce a dipole".

### P4-M8 — Repeated juxtaposition of σ values from non-comparable nulls
The opening disclaimer in the abstract ("σ values throughout ... are not directly comparable across estimators") is well intended, but Sec. IV.D and Sec. VII.b put −0.122σ (label-shuffle MASTER null on subsample mask) and +3.64σ (per-pixel-shuffle MASTER null on canonical mask) side by side without restating the disclaimer locally. The 30× discrepancy across estimators on the same physical catalog is the most important quantitative tension in the paper and should be set out in a dedicated, plain-language table.

### P4-M9 — Table III interpretation column is conceptually muddled
Bandpowers at ℓeff=4..24 are post-MASTER, but the "Interpretation" column attributes them to "Mask-coupled monopole leakage" and "Residual mask coupling". Post-MASTER residuals should have the mode coupling deconvolved by construction. If MASTER has demonstrably failed to deconvolve at these scales, that is itself a significant methodological problem with the analysis pipeline, not just an "interpretation".

### P4-M10 — Bias-hardening thresholds are designed to pass, not to challenge
Table V's acceptance thresholds (e.g., T2 ">80%" passed at 94.4%, T6 "<10%" passed at <0.4%) are loose by ~10× relative to the sub-percent science target. The paper acknowledges this ("acceptance thresholds are generous relative to the 0.75% empirical sensitivity floor") but then claims these tests as evidence of bias-freeness. A test that cannot fail at the science level is not a test.

### P4-M11 — Appendix C: "The +3.3σ signal in the 1.87M-galaxy [0.5, 0.6) confidence bin does not survive the sample-purity ladder" — this is a hand-wave
The fact that a quality-cut removes the signal is consistent with a real signal that happens to concentrate in lower-quality data **as well as** with a systematic. The paper assumes the latter without justifying the assumption.

### P4-M12 — The +4.50σ DECaLS-concentrated signal in the [0.5,0.6) bin (Appendix C.e) is family-corrected to 0.0086 (~2.4σ); the cell-level 4.5σ is alarming
The fact that one imaging leg shows a 4.5σ excess at one confidence bin should drive an investigation of whether DECaLS data themselves have a real or systematic chirality effect — not a Bonferroni waving-away. The paper offers no physical model for why DECaLS would be specifically affected.

---

## MINOR findings

### P4-N1 — Encoding artifacts in author names
"G´orski" should render "Górski"; "Iveˇzi´c" should render "Ivezić"; "G´eron" should render "Géron". Suggests LaTeX accent commands rendered to PDF incorrectly.

### P4-N2 — Project name "bigbounce" in GitHub URL (Data Availability)
The repository is `Hubify-Projects/bigbounce`. Unusual project naming for a chirality catalog and inappropriate for what is a null-result paper. Will read as unserious to PRD readers.

### P4-N3 — "Independent Researcher" affiliation
This is acceptable; flagging only because the analysis depends on commercial cloud GPUs and an external dataset host (HuggingFace). Long-term reproducibility of the catalog tie should be guaranteed via a DOI-pinned mirror (Zenodo or similar), not just HuggingFace.

### P4-N4 — Section III.D: "+0.4% excess" for Catalog B vs Table II "+0.4" — consistent but the text doesn't make clear this is the calibrated tier, not pre-calibration. Minor.

### P4-N5 — Equation (B1): the operator "S p(x̃ᵢ)" treats p as a vector and S as a permutation matrix but the body never defines S explicitly until the line below. Inline-define S or use indices.

### P4-N6 — Spelling/typography in Table footnote of Table I: "n_catalog spiral", "N_map weighted" use inconsistent subscript style (with and without underscore).

### P4-N7 — Some references give DOI, others only arXiv, others both, inconsistently formatted.

### P4-N8 — Sec. IV.C.a: p = 0.30 from "isotropic-null bootstrap (NMC = 10,000)" but a 0.43σ Gaussian gives p ≈ 0.67 two-sided / 0.33 one-sided. The convention is not stated. Minor but should be specified.

### P4-N9 — Recommended maximum page count for the actual contribution: ~6 pages. The current 11 pages of text + references is at least 50% bloat.

---

## Page-count assessment
The scientific content — a null measurement, a leakage demonstration, and a battery of diagnostic checks — would fit comfortably in a **6-page Letter** or a short **8-page Article**. The current 11 pages contain substantial narrative redundancy (the leakage story is told ~5 times across abstract, intro, Sec. IV.D, Sec. VI, Sec. VII; the falsification criterion appears 3 times; the "0.75%" threshold appears 4 times) and review-log prose. Recommend cutting to 6–8 pages.

---

## Summary recommendation
**REJECT**

The paper has interesting components (the equivariant TTA bias mitigation, the leakage demonstration) but in its current form it cannot be accepted by PRD. The headline conclusion rests on a choice of mask whose alternative gives a +3.64σ residual on the same data, the headline "+3.64σ" is itself inflated relative to its actual empirical rank p = 0.03, multiple table values fail recomputation at the 2–7% level, the bibliography contains an orphan and likely padding, internal version-control prose ("in queue", "earlier paper versions", "previous wording") has leaked into the body, the title and abstract are grossly inflated, and at least one footnote concedes a pending recalculation that has not been performed. Resubmit after substantial rewriting, with the deferred recalculation completed, the canonical-vs-subsample-mask tension addressed head-on (not adjudicated by post-hoc primary/secondary labeling), and the paper cut to roughly half its length.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P4 (Second Pass, Fresh-Eyes Re-Examination)

The following are NEW findings not in the initial review. Several are quantitative arithmetic failures missed on first pass; others are abstract/body fidelity issues.

---

## ESSENTIAL (new)

### P4-E7 — Training-set count fails recomputation; 67.6% CE-ResNet share cannot be reconstructed
**Page 2, Sec. II.B:** "(1) Galaxy Zoo 1: 6,637; (2) CE-ResNet: 17,153; (3) Synthetic: 2,000. The combined training set contains **26,636 images**."

Recompute: 6,637 + 17,153 + 2,000 = **25,790**. Off by **846 images** (3.3%). There is no fourth source disclosed.

Page 3 then claims "67.6% of training labels derive from CE-ResNet predictions":
- 17,153 / 25,790 = **66.51%**
- 17,153 / 26,636 = **64.40%**
- For 67.6% to hold, CE-ResNet would need ≈18,005 labels — not 17,153.

**None of the three possible interpretations match the stated 67.6%.** This is load-bearing because the 67.6% number is the basis for the disclaimer that validation accuracy partially reflects agreement with CE-ResNet rather than ground truth. The number that downstream readers (and future meta-analyses) will quote is therefore unverifiable. **Required fix:** disclose the missing 846 labels, recompute the share, and reconcile the disclaimer.

### P4-E8 — Abstract claim "MASTER deconvolution removes the leakage" is directly contradicted by the same paragraph
**Abstract:** *"a small uniform CW-vs-CCW classifier monopole couples through patchy survey-mask geometry to inflate the raw pseudo-Cℓ at ℓ=1, and **MASTER mode-coupling deconvolution removes the leakage**."*

But two sentences later the abstract concedes: *"The post-MASTER canonical-mask direct-MC residual is +3.64σ ... under proper galaxy-weighted monopole subtraction."*

On the **same canonical mask**, the pre-MASTER pseudo-C₁ is consistent with monopole-only at p = 0.07 (+1.68σ residual, Table IV), and the **post-MASTER** result is +3.64σ. By any honest reading, MASTER **reduces but does not remove** the leakage on the canonical mask. The "removes" claim is true only for the subsample mask, where MASTER gives −0.122σ; on the canonical mask MASTER fails to fully invert the mode coupling, which the paper later admits ("residual mode-coupling that MASTER does not fully invert on the patchy canonical footprint", Sec. IV.D).

The abstract should read "MASTER reduces the leakage on the subsample mask to null but leaves a +3.64σ residual on the canonical mask," not "removes." This is the single most important methodological claim in the paper.

### P4-E9 — Abstract "n = 5,547,858" misrepresents the analysis sample size
**Abstract:** *"the MASTER-deconvolved single-mode pseudo-C1 on the strict-superset subsample mask (**n = 5,547,858**, fsky = 0.659)"*

The natural reading is that 5,547,858 is a galaxy or spiral count. **It is not.** Table I caption explicitly defines this as *Nmap weighted = Σ Wp* where *Wp* = total classified-galaxy count per pixel (CW+CCW+NS), used as a survey-depth weight. The underlying Catalog C spiral count is **3,201,160** — the same as for every other estimator in Table I. The abstract presents the pixel-weight sum as if it were sample size, inflating the apparent statistical power of the headline null by ~1.7×.

**Required fix:** state in the abstract that the headline analysis uses the 3,201,160 Catalog C spirals on a mask of fsky = 0.659; quote pixel-weight totals only where they are operationally meaningful.

---

## MAJOR (new)

### P4-M13 — Section IV.B's "3.86× asymmetry-suppression factor" uses numbers absent from Table II
Already touched on in P4-E2, but specifically: the "raw +2.05% → equivariant −0.53%" pair gives 3.86×, while Table II's "raw +0.79% → equivariant −0.26%" gives 3.04×. The two numbers are not just inconsistent; one (3.86×) is a key narrative claim about how much the bias mitigation accomplished, and the other (3.04×) is what a reader would compute from the only data table. There is no statement reconciling them (e.g., "+2.05% refers to the chirality asymmetry A = 2(fCW−0.5); +0.79% refers to fCW excess from 0.5"). Even if the units are different, the suppression factor should be the same — and it isn't.

### P4-M14 — Galaxy Zoo 1 winding bias literature relevant to the training labels is uncited in the body
Ref [24] (Hayes, Davis & Silva 2017, "On the nature and correction of the spurious winding bias in Galaxy Zoo 1") is in the bibliography but never cited in the text. This paper is **directly relevant** to the present analysis: GZ1 labels constitute 25.7% of the training set (6,637 / 25,790) and CE-ResNet, which provides the other 67.6%, was itself trained on GZ1-derived labels. Hayes et al. (2017) document a measurable handedness bias in raw GZ1 votes traceable to human handedness. The present paper's 9.5σ CW-fraction monopole and its 0.26% "spatially-uniform CW-bias residual" (Data Availability) are quantitatively in the regime Hayes et al. characterize. **The connection should be discussed explicitly** in Sec. II.B or Sec. IV.B, not buried as a silent bibliography entry.

### P4-M15 — Table III bandpower significances cannot be recomputed from displayed (Cℓ, σnull) alone
Reconstructing the implicit null-mean μnull for each row of Table III rows 2–6:
| Row | data Cℓ | σnull | reported σ | implied μnull |
|-----|---------|-------|-----------|---------------|
| ℓeff=4 | 3.210 | 0.804 | +6.097 | **−1.69** |
| ℓeff=9 | −0.248 | 0.574 | +2.232 | **−1.53** |
| ℓeff=14 | −0.387 | 0.446 | +2.626 | **−1.56** |
| ℓeff=19 | −0.576 | 0.420 | +2.229 | **−1.51** |
| ℓeff=24 | −0.648 | 0.366 | +2.470 | **−1.55** |

A consistent μnull ≈ −1.5×10⁻⁶ across bandpowers is required to reproduce the displayed σ values. **The null mean is never displayed.** This makes the table opaque — readers cannot verify the significances without inferring an unstated quantity. The consistent ~−1.5 across bandpowers is suspicious (why would the null have a structured negative bias?) and warrants explanation; a per-pixel-shuffle null with a non-zero global monopole would naturally produce μnull ≠ 0, but the sign and uniformity should be derived, not left implicit.

### P4-M16 — Appendix A reveals different apodization treatments between primary and diagnostic masks, never motivated in the body
**Appendix A:** "*Apodization: none on the canonical mask; C² 2° apodization on the subsample mask.*"

So the headline null (subsample mask, −0.122σ) uses **apodized** mask, while the diagnostic (canonical, +3.64σ) uses **binary**. The Appendix D.a apodized test (+3.57σ at fsky = 0.482) is then a *third* configuration (apodized canonical). These are three different mask treatments, and the choice of apodization-vs-binary correlates with the choice of mask-vs-mask. The paper presents this as a controlled comparison but it is not — two variables (mask geometry and apodization) change simultaneously between the headline and diagnostic estimators. **The motivation for apodizing one but not the other must be stated**, and ideally both should be done both ways to disentangle.

### P4-M17 — Sec. V.A "factor ∼6–12" discrepancy with Shamir's signal is not derived
**Abstract and Sec. V.A:** *"inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼6–12 under the present pipeline."*

3% / 0.75% (50%-recovery threshold) = 4×; 3% / 0.5% (non-detection point) = 6×; 3% / 0.29% (Fisher floor) = 10×. None of these intervals naturally gives "6–12". The range "6–12" appears to be picked without explicit definition. **State the divisor explicitly** (e.g., "compared to our 3σ Fisher floor / 50%-recovery threshold / 95% CL upper limit").

### P4-M18 — "+4.31σ monopole-preserving dipole" appears only in Appendix E, not the body
Appendix E.b: *"the Catalog C-full **+4.31σ monopole-preserving dipole** collapses to +0.62σ (HC-broad-0.6)"*. This is a substantially significant number — 10× the headline +0.43σ — and represents the dipole significance if the global monopole is not subtracted before the fit. The main text never acknowledges that the monopole subtraction shifts the dipole significance from 4.31σ to 0.43σ; it presents only the post-subtraction number. This is a **major analysis-choice dependency** that should be in Sec. IV.C, not buried in an appendix discussing edge-on contamination.

### P4-M19 — Field/weight mismatch: chirality field uses spirals only but mask weights count all galaxies
Eq. (3) defines Ap on spirals only. Footnote 1 (Sec. IV.D) clarifies the NaMaster weight Wp = N_all(p) = NCW + NCCW + NNS. **The weighting field includes non-spirals (~62% of the catalog) that do not contribute to the field's signal but do correlate with large-scale structure** (ellipticals cluster, edge-on disks follow disk LSS). This introduces a coupling between the dipole estimator and the cluster-density field that is never analyzed. A standard treatment would use Wp = Nspiral(p), so that the weighting matches the field. **The choice should be justified or the analysis redone with Wp = Nspiral**, particularly since the Sec. IV.D leakage null *does* use Nspiral(p) for the binomial draw, creating an inconsistency between the data-side weighting and the null-side weighting.

### P4-M20 — Footnote 1 factor "⟨Nall/Nspiral⟩ ≈ 1.49" does not match the catalog-wide ratio
The catalog has Nall = 8,474,531 and Nspiral = 3,201,160, giving Nall/Nspiral = **2.65**, not 1.49. If the 1.49 is meant to be a within-mask weighted average, this should be stated, and the reader should be able to derive it from displayed Nmap weighted = 5,547,858 (subsample mask) or similar quantities. As written, 1.49 is an undocumented number that the abstract's headline "99.3% reproduction" implicitly depends on (via the pending recompute).

---

## MINOR (new)

### P4-N10 — Appendix A reports "decoupled C₁ at ℓ=1 from 2.30×10⁻⁵ to 1.51×10⁻⁵" but Table III row 1 (subsample) gives **1.494×10⁻⁶** — a factor-of-10 difference
Both should be the post-MASTER ℓ=1. The Appendix A number is for the canonical mask, the Table III number for the subsample mask. The two are never displayed together and the order-of-magnitude difference between masks is not commented on. For readers comparing the two anchors, the lack of side-by-side display is a transparency failure.

### P4-N11 — "per-spiral" in the abstract
*"471 049 high-confidence **per-spiral** after p_eq_CW > 0.9"* — grammatically odd. Probably meant "high-confidence spirals".

### P4-N12 — Sec. IV.B claim of "spatial uniformity across 7 equatorial coordinate slabs" is delegated to a data repository
The 7-slab uniformity check is load-bearing for the argument that the 9.5σ monopole "does not produce a dipole pattern". This argument should be supported by a table in the paper (7 rows, 1 column), not pushed to an external repository. The table would take ~5 lines.

### P4-N13 — Sec. III.D claim Catalog B is "Platt-calibrated" but Platt calibration is for probability calibration, not chirality-fraction adjustment
The +0.4% excess on Catalog B vs +0.79% on Catalog A and −0.26% on Catalog C describes the chirality fraction, not the calibration quality. Mechanism not stated; Catalog B never appears in the headline analysis. If B is not used downstream, consider removing it entirely.

### P4-N14 — Table IV null reproduces the data only at the +1.68σ level (residual 1.68σ), but abstract claims "99.3% reproduction"
99.3% reproduction of amplitude leaves 0.7% unreproduced; in z-units that residual is +1.68σ. The two ways of phrasing this — "explains 99.3%" vs "residual +1.68σ" — give quite different reader impressions of how complete the monopole-only model is. The abstract chooses the more favorable phrasing without disclosing the residual significance in the same sentence.

### P4-N15 — Sec. III.C: "21.4% of cases ... on borderline galaxies with PCW ≈ PCCW ≈ 0.4" — what fraction of the catalog is "borderline"?
The argmax-flip rate of 21.4% is qualified by "on borderline galaxies", but the fraction of the catalog that is borderline is never quoted. If 5% are borderline, then ~1% of Catalog C labels flip between Z₂ and D₄; if 30% are borderline, ~6% flip. The cosmological impact differs by 6×. Quantify.

### P4-N16 — Abstract: significance disclaimer "σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators"
This is an excellent disclaimer but is then violated in the same abstract by quoting −0.122σ and +3.64σ and +0.43σ in immediate succession **with the implicit invitation to compare them**. The disclaimer should either be load-bearing (e.g., separate the σ values into clearly delineated boxes) or omitted as performative. Currently it functions as a CYA against a critique the paper invites.

---

## Summary of fresh-eyes pass
The first-pass review captured the high-level problems (orphan refs, abstract/title inflation, recompute failures, version-control prose leakage, mask-choice partisanship). The second pass uncovered:

1. **The training-set arithmetic does not close** (P4-E7), and the 67.6% derived figure is unverifiable.
2. **The abstract's central methodological claim ("MASTER removes the leakage") is contradicted by the abstract itself** (P4-E8).
3. **The abstract presents a pixel-weight sum as if it were a sample size** (P4-E9).
4. **Critical numbers (+4.31σ monopole-preserving, μnull ≈ −1.5×10⁻⁶) are hidden in appendices or implicit** (P4-M15, P4-M18).
5. **The relevant GZ1 winding-bias literature is in the bibliography but never engaged with in the body** (P4-M14), despite GZ1 labels (directly and via CE-ResNet) being the dominant training signal and the paper reporting a 9.5σ residual chirality monopole.
6. **The field/weight construction has a documented inconsistency** between the data side (mask-weighted by N_all) and the null side (binomial-drawn from N_spiral), which is not discussed (P4-M19).

These reinforce the original REJECT recommendation. The paper's underlying observation — a careful null result with a useful pedagogical leakage demonstration — could be a clean Letter, but the manuscript as submitted cannot pass peer review without substantial reanalysis and rewriting.