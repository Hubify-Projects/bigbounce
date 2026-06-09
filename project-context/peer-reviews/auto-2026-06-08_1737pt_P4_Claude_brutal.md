# P4 auto-2026-06-08_1737pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13540 chars)
**Wall time**: 499.3s

---

# Referee Report — Manuscript P4

**Title:** "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, …"

**Recommendation up front:** REJECT in present form; the paper carries a non-trivial body of work but multiple internal inconsistencies, a figure/caption mismatch involving the central catalog numbers, headline σ inflation, and overlong/over-promised framing all need to be corrected before this can be reconsidered.

---

## ESSENTIAL findings

### P4-E1 — Figure 2 pie chart contradicts its own caption (and the body)
**Page 6, Fig. 2.** The pie chart displays:
- CW 1,687,069 (19.9 %)
- CCW 1,634,726 (19.3 %)
- Not-Spiral 5,152,736 (60.8 %)

The caption claims these are Catalog C (equivariant) and quotes
"N_CW = 1,592,107, N_CCW = 1,609,053, N_NS = 5,273,371".

These two number sets are **not equal**. The displayed pie has CW > CCW (CW fraction 1,687,069/(1,687,069+1,634,726) = 0.5078), which is the **raw Catalog A** signature (Table II: 0.5079), not Catalog C (0.4974, CW < CCW). The figure that the body uses to advertise "Catalog C composition" is therefore showing the wrong tier — the very tier whose bias the paper claims to have removed.

**Fix:** Either regenerate the pie from Catalog C numbers (1,592,107 / 1,609,053 / 5,273,371) or relabel the figure as Catalog A and add a Catalog C panel. Until corrected, the central catalog-composition figure contradicts the headline.

### P4-E2 — Figure 4 internally inconsistent (σ labels, MC count, mask)
**Page 8, Fig. 4.** The figure shows annotations "2.7σ" at ℓ=1 and "2.5σ" at ℓ=5, with a legend "Null expectation (1000 shuffles)". The body and Table IV explicitly state:
- ℓ=1 canonical-mask post-MASTER = **+3.64σ** (not 2.7σ);
- the canonical-mask null uses **N = 500** realizations (not 1000).

The caption further says this is "ℓ=1 dipole power. Bottom: ℓ=2 quadrupole" — but the figure plotted goes from ℓ=1 to ℓ=5 in a single panel. Caption and panel do not correspond.

**Fix:** Reconcile figure, caption, and body. State which mask, which null, which MC count, and which σ convention is shown.

### P4-E3 — Headline +3.64σ is *not* the empirical significance
**Abstract & Sec. IV / Appendix D.** The abstract reports the canonical-mask residual as "+3.64σ (z = Δ/σ_null moment-ratio … empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent)". A 3.64σ Gaussian tail corresponds to p ≈ 1.4 × 10⁻⁴; the actual empirical rank-based p is **0.030** (15/500), i.e. **1.9σ**. Reporting 3.64σ in the headline, the abstract, the section titles, Table III, Fig. 4, and Sec. VII is misleading: it pretends Gaussianity that the empirical null distribution does not support. The honest headline number is the rank-based ≈1.9σ.

**Fix:** Demote moment-ratio z to a footnote diagnostic; report rank-based p / equivalent σ as the headline canonical-mask residual everywhere it appears.

### P4-E4 — σ values from incomparable null procedures still juxtaposed in title and headline sentences
The title bundles "−0.122σ subsample-mask ℓ=1 null" with "+3.64σ" and "depth/morphology-correlated canonical-mask residual" without the comparability caveat. The abstract has a one-line disclaimer ("σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators"), but the *title itself* compares a label-shuffle null σ to a binomial per-pixel-shuffle null σ, and Sec. VII repeats the juxtaposition. Per the review instructions this is flagged ESSENTIAL.

**Fix:** Either drop the σ numerics from the title, or rewrite so that each headline σ in the abstract, in section headings, and in conclusions is followed by the null procedure each time (not just once at the top).

### P4-E5 — Independent-validation accuracy (κ = 0.40) is mediocre and propagated unphysically
The only truly independent label benchmark is GZ1: **69.91 %, Cohen's κ = 0.40** on 234,282 disjoint matches. This is barely above coin-flip after accounting for class prior and is not the performance of a sub-percent precision classifier. The paper then re-uses GZ1 *as ground truth* to derive a "dilution factor g = 2a − 1 = 0.398" and to convert the empirical 0.75 % floor into a "true-underlying threshold ∼1.88 %". This conversion is logically inconsistent because GZ1 itself has the documented winding-bias problem (Hayes, Davis & Silva 2017 [24], cited but not used here in the propagation). The "1.88 %" threshold cannot be defended as a sensitivity floor given GZ1's own systematics.

**Fix:** Either drop the GZ1-anchored dilution conversion or include the Hayes et al. correction explicitly and re-derive the sensitivity floor.

### P4-E6 — Catalog C is *less* monopole-symmetric than CE-ResNet, contradicting the "advancement" claim
The paper repeatedly compares to CE-ResNet (Jia et al. 2023) which reports cw/ccw = 0.998 — i.e. |CW − 0.5|/(CW+CCW) ≈ 5 × 10⁻⁴. Catalog C has |0.4974 − 0.5| = 2.6 × 10⁻³, **five times larger** than CE-ResNet's residual. The text frames Catalog C as "complementary" but never confronts that the headline monopole asymmetry of this work is worse than the prior work it claims to advance.

**Fix:** Acknowledge that Catalog C does *not* improve on CE-ResNet's monopole symmetry. Restrict the "advancement" claim to coverage, the not_spiral class, and TTA equivariance.

---

## MAJOR findings

### P4-M1 — Monopole-subtraction increases the residual signal, unexplained
Appendix A states that monopole subtraction of ⟨A⟩_mask,gw = −0.005294 **increases** the canonical-mask post-MASTER significance from +1.85σ to +3.64σ. The body never explains why an honest mean removal would inflate, not deflate, residual ℓ=1 power. If the underlying field truly has a coherent ℓ=1 component partially aliased into ℓ=0, removing the alias should *expose* it (which is what's happening), but the paper instead labels the result a "systematic" without justification.

**Fix:** Either (a) demonstrate quantitatively (via simulation) that the +1.85 → +3.64 step is itself a mask-coupling artifact, or (b) honestly reframe: monopole removal exposes a residual that is not killed by MASTER deconvolution and that the auxiliary discriminators (broadband ℓ=2, leg cross-spectrum) still don't fully cover.

### P4-M2 — Pre-MASTER "+6.48σ" appears in body but not in any table
Page 4 (Sec. IV C): "Catalog A (raw) shows a 2.31σ real-space dipole and a +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower". This +6.48σ is load-bearing in the narrative (it motivates the entire MASTER step), yet it appears in no table, no figure, and has no quoted null procedure. The companion +2.31σ also lacks an explicit Catalog-A entry in Table I.

**Fix:** Add Catalog A rows to Table I with the null procedure, σ_null, and Cℓ_meas.

### P4-M3 — Table III bandpowers have negative Cℓ but positive σ — null mean not shown
For ℓ_eff = 9, 14, 19, 24 the measured Cℓ values are negative (−0.248, −0.387, −0.576, −0.648 × 10⁻⁶ sr) yet σ = +2.232 to +2.626. This requires the null *mean* to be more negative than the data. The table column for the null mean is missing. A pseudo-Cℓ MASTER null mean that is *more negative* than the observed across four consecutive bandpowers is at minimum a red flag and at worst evidence that the per-pixel-shuffle null does not properly represent the noise floor.

**Fix:** Add a column for ⟨C_null⟩ in Table III. Justify negative null means or replace with a generative null that does not produce them.

### P4-M4 — Internal contradiction between "monopole-mask leakage" and "depth/morphology systematic"
Abstract: "+3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry". Appendix D conclusion: "The most likely explanation is a per-pixel-correlated systematic at low ℓ on the canonical footprint (depth/PSF/morphology)". These are *different* mechanisms. The monopole-only generative null in Sec. IV D already leaves a +1.68σ residual on the pre-MASTER pseudo-Cℓ (not 3.64σ), so the appendix conclusion is the operative one. The abstract should not invoke "monopole leakage" as the explanation for the +3.64σ.

**Fix:** Rewrite the abstract so it cleanly distinguishes the two mechanisms: (i) monopole-mask leakage explains pre-MASTER raw power; (ii) a separate depth/morphology systematic explains the post-MASTER +3.64σ canonical-mask residual.

### P4-M5 — Shamir exclusion claim is not actually demonstrated
Multiple places (abstract, Sec. V A, Sec. VII): "the present null disfavors the Shamir ∼2–4 % detection class at the amplitude level under our pipeline … by a factor of ∼6–12". Then immediately: "a matched-footprint Ganalyzer reanalysis is required for a formal σ-level exclusion." A pipeline-dependent comparison without re-running the Shamir estimator on a matched footprint cannot disfavor anything at the likelihood level. The hedge cancels the claim.

**Fix:** Either remove the "disfavors by factor 6–12" language or commit to running a matched-footprint Ganalyzer in a revision. As written this is an overclaim.

### P4-M6 — Training-set circularity not bounded
67.6 % of training labels come from CE-ResNet pseudo-labels. The validation accuracy of 93.7 % three-class therefore measures concordance with CE-ResNet on >2/3 of the data and not independent ground truth. The only truly independent test (GZ1, κ=0.40) gives ~70 %. The headline 93.7 % should be qualified to the joint train/validation split definition; otherwise it is misleading.

**Fix:** State the train/validation accuracies separately as (a) on the CE-ResNet-pseudo-labeled fraction and (b) on the GZ1 disjoint sample. Use the latter as the headline.

### P4-M7 — Hemisphere LEE: p_LEE ≤ 10⁻⁴ is then dismissed as a "systematic-floor artifact"
Sec. VI / Appendix C: the direct-MC look-elsewhere p value is ≤ 10⁻⁴, and the Bonferroni correction across ~650 directions cannot reduce <10⁻⁴ × 650 below 1σ; the paper then attributes the rejection to "the same sub-percent GZ1-training-label / depth-coupled systematic that sources the global 9.5σ CW-fraction monopole". This reasoning is asserted, not demonstrated. A monopole alone, isotropic by construction, cannot generate a hemisphere-localized asymmetry at >3σ. Some coupling argument is needed.

**Fix:** Provide a quantitative demonstration that the depth/training-bias systematic produces the observed 3.48 × 10⁻³ hemisphere |A| and not just the global monopole.

### P4-M8 — Footnote 1 (page 4) admits an unresolved data-vector ambiguity at the headline level
The footnote concedes that the previous wording "Binomial(n_total, p_CW^global)" was ambiguous between N_spiral(p) and N_all(p), that the headline 99.3 % figure depends on the spiral-trial draw, and that "a parallel rerun on N_all(p)-trial draws is in queue". A paper that is asking PRD readers to believe a headline 99.3 % reproduction figure should not be in the position of saying the N_all rerun is "in queue".

**Fix:** Run the N_all variant before submission and report both. Remove "in queue" language from a publication-stage manuscript.

### P4-M9 — Page-length vs. content
This is a null result with one new catalog. Twelve pages with five appendices is generous. The phenomenology — equivariant TTA, MASTER deconvolution, monopole-only generative null — could comfortably fit in 7–8 pages.

**Fix:** Compress. Recommended target ≤ 8 pages in PRD format. Move the eight-test bias-hardening table, the D4-TTA hold-out details, and the high-confidence subsample robustness paragraph to a supplement.

### P4-M10 — Abstract sentence "We emphasize at the outset … parity-EVEN" is correct but in the wrong place
This pedagogical paragraph properly belongs in the introduction. Putting it in the abstract suggests the prior literature mis-classification is part of this paper's contribution, which it is not.

---

## MINOR findings

### P4-N1
Title contains a specific σ value ("−0.122σ"). PRD style discourages this; titles should describe content, not advertise individual numbers.

### P4-N2
"3,201,160 DESI Legacy spiral galaxies (8.47 M sources, 471 049 high-confidence …)" — the abstract foregrounds three different N values; the body never explains why 471 049 is the relevant denominator for sensitivity and not 3,201,160. Clarify.

### P4-N3
Catalog A deviation recomputation: (0.5079 − 0.5)/0.000279 = 28.3σ; paper says 28.8σ. Catalog B: 14.3σ vs. quoted 14.6σ. These small discrepancies suggest different N denominators per row of Table II; state explicitly.

### P4-N4
Table IV pre-MASTER residual: z = (1.696 − 1.685)/0.007 = 1.57, paper quotes +1.68. Likely rounding of the displayed null mean; cite to one more sig fig.

### P4-N5
Hemisphere null entry in Table IV: (3.48 − 1.69)/0.41 = 4.37, paper quotes +4.42. Same rounding issue.

### P4-N6
Inconsistent C_ℓ notation: "pre-MASTER pseudo-Cℓ" (Sec. IV C), "pre-MASTER pseudo-C_ℓ^(ℓ=1)" (Sec. IV D), "C_1" (Appendix A). Pick one.

### P4-N7
Reference [3] and reference [2] both cite Shamir 2022; clarify they are different papers (PASJ vs MNRAS). Currently easy to misread as duplicate.

### P4-N8
"3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%": 2.05/0.53 = 3.87, OK. But "+2.05%" is not the Catalog A excess of 0.79 % reported in Table II; the body should reconcile these two definitions of "excess".

### P4-N9
"companion data repository" referenced multiple times in Sec. IV B, IV E, Appendix C — for a standalone PRD submission, all primary numbers should be in the manuscript or its supplement, not a companion repository.

### P4-N10
"AI tool usage" disclosure (Acknowledgments) is appropriate but the sentence "all scientific results are derived from the authors' own analysis" should explicitly name which sections, if any, used AI for analytic decisions (vs. code/edit support).

### P4-N11
Reference [11] (Land et al. 2008, arXiv:0803.3247) is cited in the bibliography but not in the body text.

### P4-N12
Footnote 1 sprawls across half a column; restructure as a methods paragraph or move to Appendix A.

---

## Specific arithmetic re-check (kept here for the authors)

- Catalog C spiral total: 1,592,107 + 1,609,053 = 3,201,160 ✓
- Catalog C CW fraction of spirals: 1,592,107 / 3,201,160 = 0.49735 ≈ 0.4974 ✓
- Catalog C σ_binom: √(0.25 / 3,201,160) = 2.79 × 10⁻⁴ ✓
- Catalog C dev: (0.4974 − 0.5)/2.79 × 10⁻⁴ = −9.32 (paper: 9.5; small rounding)
- Table IV pre-MASTER ratio: 1.685 / 1.696 = 0.9935 ≈ 99.3 % ✓
- Φ⁻¹(1 − 0.030) = 1.88 ≈ 1.9σ Gaussian equivalent ✓
- Fig. 2 pie spiral fraction: 3,321,795 / 8,474,531 = 39.2 % (does **not** match the 37.78 % spiral fraction in Sec. IV A); pie fraction CW/(CW+CCW) = 0.5079 — matches Catalog A, not Catalog C.

The Fig. 2 arithmetic confirms the figure shows raw Catalog A, contradicting both its caption and the body claim.

---

## Summary recommendation

**REJECT** (re-submit only after substantial revision; equivalently, MAJOR REVISIONS at the editor's discretion).

The paper does real and useful work — assembling 3.2 M spiral classifications with explicit equivariant TTA, presenting an honest MASTER-deconvolved null, and documenting a monopole-mask leakage channel that arguably reframes prior detection claims. But the current manuscript is not at PRD acceptance standard: the central composition figure shows the wrong catalog tier, the angular-power figure shows σ labels and an MC count that disagree with the body, the +3.64σ headline is a moment-ratio z whose empirical rank value is half that, the GZ1 dilution chain rests on labels with κ=0.40 used as ground truth, and the abstract conflates "monopole-mask leakage" with the appendix's "depth/morphology systematic" mechanism for the same residual. The Shamir-exclusion language exceeds what the paper actually establishes. After the figure-tier mismatch, the headline-σ honesty fix, the negative-null-mean explanation for Table III, the N_all generative-null rerun, and a tightening to ≤ 8 pages, the manuscript could become acceptable.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Manuscript P4 (Second Pass, Fresh Eyes)

A focused re-read against the ten failure modes turned up several new issues, including one figure/body contradiction that is at least as severe as the Fig. 2 pie-chart problem I flagged in the first pass, and a self-contradiction inside Appendix A on the very definition of the asymmetry field.

---

## ESSENTIAL findings (new)

### P4-E7 — Fig. 1 caption claims D4 averaging; body explicitly says 2-fold TTA only
**Page 5, Fig. 1 caption:** "For each input image x, the classifier is evaluated on the **eight D4 transforms (four rotations × two reflections)**. … yielding a strictly flip-equivariant CW/CCW classifier with flip-swap correlation = 1.000 by construction."

**Sec. III C, page 3:** "We restrict to **2-fold TTA (original + horizontal flip)** rather than the full D4 group because mirrors flip chirality by definition, whereas in-plane rotations do not change chirality; rotation-TTA probes classifier non-equivariance rather than the chirality assignment itself."

**Eq. (2) on page 3** likewise shows averaging over only the original and horizontal-flip predictions — D2 averaging, not D4.

The figure title literally reads "Test-time **D4** equivariant averaging (TTA)." The body argues at length that D4-TTA is the wrong thing to use. Either the figure is mis-labeled or the production pipeline is not what the methods section claims. This is the second central figure (after Fig. 2) where the caption disagrees with the body.

**Fix:** Either (a) the caption is wrong and the figure shows 2-fold (Z₂) averaging consistent with Eq. (2) — relabel — or (b) the production catalog was actually generated with D4-TTA, in which case Sec. III C and Eq. (2) are wrong. Resolve.

### P4-E8 — Fig. 3 caption says "log₁₀ N per HEALPix pixel"; the actual figure is the chirality asymmetry
**Page 7, Fig. 3 caption:** "Sky distribution of the 8.47 M-galaxy chirality catalog (Mollweide projection, **log₁₀ N per HEALPix NSIDE=64 pixel**)."

**The figure colorbar:** the displayed quantity is "(N_CW − N_CCW)/(N_CW + N_CCW)" with range [−0.08, +0.08] — the chirality asymmetry A_p, not log₁₀ N.

The caption describes a number-density map; the panel shows the asymmetry map. These are completely different scientific quantities. Together with P4-E1 and P4-E7 this is now the third central figure with a caption-body mismatch.

**Fix:** Correct the caption to describe the displayed quantity (chirality asymmetry A_p on the canonical mask).

### P4-E9 — Appendix A contains two contradictory definitions of the asymmetry field
**Page 9, Appendix A, paragraph (a):** "The asymmetry field is A_p = (N_CW^(p) − N_CCW^(p))/(N_CW^(p) + N_CCW^(p)) **(spirals only)**."

**Page 9, Appendix A, paragraph (c), four lines later:** "Field: scalar (spin-0) asymmetry map A_p = (N_CW^(p) − N_CCW^(p))/**N_total^(p)**, with galaxy-weighted mask-mean subtraction ⟨A⟩_mask,gw = −0.005294."

These two denominators differ by a factor ⟨N_total/N_spiral⟩ ≈ 1.49 (the ratio explicitly invoked in footnote 1, page 4). A factor-1.49 difference in the field definition propagates as a factor-2.2 difference in C_ℓ, and ⟨A⟩_mask,gw = −0.005294 ≈ p_CW − 0.5 = −0.0026 × (≈2) is only sensible under one of the two definitions.

Body Eq. (3) on page 4 uses the spiral-only denominator. The NaMaster field weight Wp = N_total^(p) (Table I, page 4), but the *data field* should be A_p^(spiral). The appendix conflates the two.

**Fix:** State a single definition for A_p, with explicit consistency with Eq. (3). If the canonical-mask MASTER actually used (N_CW − N_CCW)/N_total, that is a different estimator from what the body claims and the +3.64σ headline number needs to be re-derived.

---

## MAJOR findings (new)

### P4-M11 — Bias-hardening test T8 "passes" while being 9.5σ inconsistent with the claimed sub-percent sensitivity
**Appendix B, Table V:** "T8: CW/CCW balance — Threshold 50 ± 10% — Result 49.7%."

But Table II (page 4) gives Catalog C CW fraction 0.4974 ± 0.000279 = a **9.5σ** deviation from 0.5000. The bias-hardening suite is the body's main classifier-side validation, yet the T8 acceptance threshold (±10%) is two orders of magnitude looser than the sensitivity threshold the paper claims to defend (0.75% empirical floor, 0.29% Fisher floor). A test that passes "PASS" at 9.5σ deviation cannot be the operational bias control for a sub-percent isotropy bound.

The same critique applies to T6 (hemispheric null "<10% difference") and T1 (flip-swap r > 0.80, when the equivariant TTA enforces r = 1.000 by construction). These tests are necessary-not-sufficient — but the manuscript twice claims (page 9, page 10) that "all 8 tests pass at the required thresholds" provides the bias mitigation, which is misleading.

**Fix:** Tighten the T6, T8 thresholds to the actual sensitivity floor (sub-percent) or remove the suite from the chain of evidence for the headline null.

### P4-M12 — Sec. VI A Fisher floor uses f_sky = 0.46, inconsistent with the rest of the paper
**Sec. VI A, page 7:** "The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at N_spiral = 3,201,160, **f_sky = 0.46**)."

But the canonical mask is f_sky = 0.49005 (Sec. IV D) and the subsample mask is f_sky = 0.659 (Sec. IV C). The value 0.46 does not appear anywhere else in the paper. This is either a stale number from an earlier mask choice or a typo. It directly enters the sensitivity-floor calculation that anchors the falsification criterion in the abstract.

A second arithmetic check: σ(A/2) ≈ 0.048% at N=3.2 × 10⁶ corresponds to σ(A) ≈ 0.096%. Pure binomial σ = √(0.25/N) gives 0.028% — about 3.4× smaller. With f_sky = 0.46, the 1/√f_sky correction is only 1.47×. Where does the remaining ~2.3× inflation come from? It is not derived in the paper.

**Fix:** Either correct f_sky to 0.49005 (canonical) or 0.659 (subsample) and re-derive 0.29%, or show explicitly the geometric/binomial calculation that produces σ(A/2) = 0.048%.

### P4-M13 — Hemisphere significance reported as four different values without an explicit hierarchy
The hemisphere observable appears as:
- **3.05σ** "local maximum" (Sec. III A, Appendix C);
- **+3.48** (data |A| in units of null std, Table IV);
- **+4.42σ** (z = Δ/σ_null on hemisphere max|A| at NSIDE_dir = 8, Table IV);
- **p_LEE ≤ 10⁻⁴** (Sec. VI; corresponds to Gaussian ~3.7σ);
- **< 1σ post-Bonferroni/BH across ~650 directions** (Sec. VI).

Four numbers (3.05, 3.48, 3.7, 4.42) plus a "post-correction < 1σ" — all describing the same hemisphere observable on different statistic/null choices. The paper never tabulates these against each other or explains the chain that takes 4.42σ → < 1σ via "Bonferroni/BH across ~650 directions" (Bonferroni × 650 of p=10⁻⁴ gives p~0.065, which is ~1.8σ, not < 1σ).

**Fix:** Provide a single table of (statistic, null, σ_meas, σ_post-LEE) entries for the hemisphere observable. Show the Bonferroni arithmetic that yields the "<1σ" post-correction value, or correct it.

### P4-M14 — ~20 bibliography entries never cited in the body
Bibliography entries [11] (Land et al.), [13] (Gross & Vitells), [14] (Davis & Hayes SpArcFiRe), [15] (Motloch et al.), [16] (Lue, Wang, Kamionkowski), [17] (Cabass, Ivanov, Philcox), [18] (Philcox BOSS), [19] (Eskilt-Komatsu birefringence), [20] (Cosmoglobe), [21] (Hou-Slepian-Cahn), [22] (Cahn-Slepian-Hou), [23] (Komatsu Nature Reviews), [25] (Bamford et al.), [26] (Hart et al.), [27] (Walmsley DECaLS), [28] (Yu et al. primordial chirality), [29] (DESI Part I), [30] (LSST), and [33] (Hivon MASTER) do not appear to be cited in the body text. In particular:

- [13] Gross & Vitells is the canonical LEE-trial-factor reference and Sec. VI explicitly invokes LEE corrections without citing it.
- [33] Hivon et al. is the **original MASTER paper** — Sec. IV C cites only [32] (Alonso et al. NaMaster implementation) for "MASTER mode-coupling deconvolution".
- The entire parity-violation literature ([16]–[23]) is uncited despite Sec. VI B discussing parity-violating sectors.

**Fix:** Either cite every bibliography entry in the body or prune the bibliography. PRD will not let this past production.

### P4-M15 — Internal contradiction in the canonical-mask C_ℓ value between Appendix A and Table III
**Appendix A, page 9:** "Monopole subtraction reduces decoupled C_1 at ℓ = 1 from **2.30 × 10⁻⁵** to **1.51 × 10⁻⁵** (∼ 34%) and increases σ from +1.85 to +3.64 (the canonical-mask number)."

**Table III, page 6, row 1:** "ℓ = 1 (single mode), C_ℓ × 10⁶ (sr) = **1.494**, σ_null × 10⁶ (sr) = 0.429, Significance −0.122σ."

So Appendix A says canonical-mask C_1 = 1.51 × 10⁻⁵ sr; Table III says subsample-mask C_1 = 1.494 × 10⁻⁶ sr. A factor-10 difference is plausible from the mask change, but neither the body nor the captions tabulate the canonical-mask C_1, σ_null, or null mean. Given the central role of "+3.64σ" in the multi-mechanism interpretation, this number should be in the main table, not a sentence in Appendix A.

**Fix:** Add a row to Table III for the canonical-mask C_1 with the same null-mean and σ_null columns. Also add the units-mismatch check; if the appendix has units (decoupled vs. sr-scaled C_ℓ) different from Table III, label them.

---

## MINOR findings (new)

### P4-N13
Catalog A pre-MASTER pseudo-C_ℓ at "+6.48σ" (Sec. IV C, page 4) and Catalog A real-space dipole at "+2.31σ" appear without any table entry. Both are load-bearing in Sec. VI's discussion of bias suppression. Add Catalog-A rows to Table I.

### P4-N14
**Appendix D part (c):** "summed leg-induced ℓ = 1 amplitude is ∼ 25% of the observed canonical-mask ℓ = 1 amplitude." How are r_{ℓ=1}(BASS+MzLS × A_p) = +0.65 and r_{ℓ=1}(DES × A_p) = −0.73 combined into a 25% summed contribution? Provide the formula.

### P4-N15
**Sec. VI A** quotes P(σ > 3) = 0.55 at A = 0.75% and P(σ > 3) = 0.15 at A = 0.5%. Linear interpolation places 50%-recovery at A ≈ 0.72%, not 0.75%. Either re-interpolate or quote 0.72% as the threshold.

### P4-N16
**Fig. 2 spiral total:** 1,687,069 + 1,634,726 = 3,321,795 ≠ 3,201,160 (the Catalog C spiral total in body text and Table I). The pie chart total spiral count is **3.77% larger** than the body's spiral total, in addition to the tier-mismatch flagged in P4-E1. Confirms the pie is a stale Catalog A artifact, not a re-labeled Catalog C breakdown.

### P4-N17
**Sec. IV C:** "MASTER mode-coupling deconvolution using NaMaster [32]" — reference [32] is Alonso, Sanchez, Slosar 2019 (the NaMaster implementation paper). The original MASTER paper is Hivon et al. 2002, in the bibliography as [33] but not cited here. Add [33] when first introducing the MASTER algorithm.

### P4-N18
**Sec. VI A, page 7:** "Edge-on galaxy contamination (65.7% of b/a<0.3 objects receive CW/CCW labels rather than not_spiral) reduces effective sample size by ∼ 10–15%, corresponding to a ∼ 5–8% sensitivity penalty." The 65.7% contamination rate is documented but never propagated into the headline N_spiral = 3,201,160 — should the "effective N" for sensitivity calculations be N_spiral × (1 − 0.15) = 2.72M? If so, the Fisher floor of 0.29% becomes 0.32%, and the empirical 0.75% threshold gets a 5–8% upward correction. State explicitly whether the propagation has been done or not.

### P4-N19
**Table V (Appendix B):** "T8: CW/CCW balance — Result 49.7%." Table II gives Catalog C as 0.4974 = 49.74%. Trivially round 49.74 to 49.7, but consider stating to one more digit so the 9.5σ discrepancy with 50.00% is visible.

### P4-N20
**Sec. V A:** "Under the present ViT/TTA pipeline, our maximum regional asymmetry is 0.32%." This 0.32% is not anchored in any table. Sec. IV B says "all 7 equatorial coordinate slabs within 0.5% of 50/50" — consistent envelope but not the same number. Provide the per-slab table either in the body or in Appendix C.

### P4-N21
**Catalog A C_1 leakage cross-check:** the body argues qualitatively that a 0.79% Catalog-A monopole drives the +6.48σ pre-MASTER pseudo-C_ℓ. By the same mechanism, the Catalog C monopole of 0.26% (= 0.79% × 0.33×) should drive a residual ~0.33² ≈ 11% as large in pseudo-C_ℓ power, or √11% ≈ 33% in σ-units: i.e. (6.48σ) × 0.33 ≈ 2.1σ. The observed canonical-mask post-MASTER residual is +3.64σ (or empirical-rank 1.9σ per P4-E3). The order-of-magnitude consistency of these two numbers should be stated as a quantitative anchor for the "depth/morphology systematic" interpretation, since it places the Catalog C monopole-leakage prediction right at the observed residual.

---

## Summary of new findings

Three new ESSENTIAL issues (Fig. 1 D4-vs-2fold mismatch, Fig. 3 caption-quantity mismatch, Appendix A self-contradictory field definition), five new MAJOR issues (T8 acceptance threshold incompatible with sensitivity claim; f_sky = 0.46 inconsistency in Fisher floor; hemisphere-significance fragmentation; ~20 orphan references including the original MASTER paper; canonical-mask C_1 reported only in Appendix A prose, not in Table III), and nine new MINOR issues.

Combined with the first-pass report, the recommendation **REJECT (resubmit only after substantial revision)** stands and strengthens. The new findings show that the figure-body mismatches I flagged in pass one (Fig. 2 pie chart) are not isolated: all three figures with non-trivial content (Figs. 1, 2, 3) have caption errors, and the appendix on the central NaMaster configuration self-contradicts on the field definition. Production review at PRD will reject on figure/appendix consistency alone.