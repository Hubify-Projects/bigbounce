# P1B auto-2026-06-08_1737pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11221 chars)
**Wall time**: 536.7s

---

# Referee Report — P1B
**Manuscript:** "Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"

---

## Overview

This is a "technical verification companion" to an as-yet-unwritten Paper I(a). The manuscript reports three numerical exercises, each of which is *explicitly disclaimed* in the abstract and body as **not testing the theory it is supposed to verify**:

1. The MCMC is stock CAMB with ΔNeff free — the abstract and §III state this "carries no torsion modifications" and is "not a spin-torsion theory module."
2. The NaMaster run is a bias-injection MC — the abstract states this "is **NOT** the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α" and "the MC recovery is therefore a pipeline-validation figure, not a sky-detection significance claim."
3. The spectator-ALP exercise is disclaimed in both the abstract and §VI as "not a distinctive ECH prediction" because "the same birefringence arises in standard GR with an identical ALP."

After 11 pages, the reader cannot identify any positive scientific claim that the manuscript actually establishes about Einstein–Cartan–Holst spin-torsion cosmology. By the author's own framing, this is a verification paper that verifies nothing about the theory it accompanies. That alone is fatal at PRD, but the manuscript is *also* riddled with arithmetic inconsistencies, internal audit prose, sample-count contradictions, and a companion-paper structure where the primary paper is "in preparation" (i.e., does not exist).

---

## ESSENTIAL findings (paper cannot proceed without these fixes)

### P1B-E1 — Arithmetic error in Table II, footnote b (wpivot derivation), p. 4
The footnote states:
> "σ²_wpivot = σ²_w0 + (1−ap)² σ²_wa = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²"

Recomputing the RHS: (0.0436)² = 0.001901; (0.3320)²(0.1864)² = 0.003830. Sum = 0.005731 → √ = **0.0757**, not 0.0301. The advertised σ_wpivot = 0.0301 is incompatible with the displayed inputs by more than a factor of two. Either the value, the inputs, or the formula (which is also missing the cross-covariance term) is wrong. This invalidates the "−1.1σ from −1" wpivot tension claim, which is the *only* piece of Table II that the body uses to soften the "+4.3σ" w0 departure from ΛCDM.

**Fix:** Recompute Cov(w0, wa) from the chain, present the complete variance formula with cross term, and report the actual numerical answer. If the −1.1σ wpivot claim does not survive, retract it.

### P1B-E2 — Sign error in pivot-decorrelation definition, Table II, footnote b
The footnote defines: "ap = 1 − Cov(w0, wa)/Var(wa)". The standard decorrelation condition Cov(w_pivot, w_a) = 0 with w_pivot = w_0 + (1−a_p) w_a yields **a_p = 1 + Cov(w_0,w_a)/Var(w_a)**. The sign as written is wrong; with the paper's quoted ap = 0.6680 it implies the *opposite* sign of Cov(w_0, w_a) than the data require for the reported σ(w_0+w_a) = 0.1485 to be consistent with σ_w0 and σ_wa. The Table II covariance structure is internally over-determined and the displayed numbers cannot all be simultaneously correct.

**Fix:** Recompute and reconcile {σ_w0, σ_wa, σ(w0+wa), ap, σ_wpivot} from a single covariance matrix and present that matrix.

### P1B-E3 — Bias headline in abstract contradicts body
Abstract states: "injecting the spectator-ALP fiducial value β = 0.27° recovers β̂ = 0.238° (pipeline-recovery bias 0.032°)." Body (§IV, p. 6) states: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°." The abstract's headline bias figure is the *best-case* injection, not the worst case (0.040°). The §VII Conclusions correctly say "worst-case 0.040°"; the abstract does not.

**Fix:** Replace the abstract bias number with the worst-case 0.040°, and remove the explicit retraction prose from §IV.

### P1B-E4 — Internal review-log prose embedded in the body
The manuscript contains extensive editorial bookkeeping that does not belong in a published paper. Examples:
- §III, p. 3: "An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w0wa samples at the LCDM point..."
- §III, p. 3: "(note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically)."
- §III, p. 4: "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood..."
- §III, p. 4–5: "MB–H0 joint-posterior offset check. A concern was raised that the joint posterior mean (MB = −19.263, H0 = 67.69) was inconsistent with an active sn.pantheonplus likelihood, claiming a Cobaya YAML alias failure."
- §III, p. 5: "NOT a YAML alias failure; the parameters are correctly aliased per the spin_torsion.input.yaml configuration..."
- §IV, p. 6: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°..."
- §VI, p. 8: "§VI for the explicit numerical derivation correcting the earlier Caγθi product"
- Footnote 1: "references to 'k = 7' elsewhere in this paper refer to..."

This is review-response prose; it must be removed entirely. The paper should read as if these audits never happened.

**Fix:** Strip all review-log, "earlier draft," "earlier count," "addresses concerns," "NOT a YAML alias failure" prose.

### P1B-E5 — Companion paper to a non-existent paper
Paper I(a) [ref 1], Paper II [ref 4], Paper III [ref 5], and Paper IV [ref 6] are all listed as "(in preparation) (2026), HUBIFY-2026-001A," etc. The Introduction states "the 13 logically-independent structural barriers, the perturbation-transparency theorem, the 14-barrier table... are in Paper I(a) [1]." A verification companion cannot be evaluated when the paper being verified is not available. PRD does not accept submissions whose load-bearing references are unpublished and non-public manuscripts by the same author.

**Fix:** Either (a) submit Paper I(a) simultaneously, or (b) recast this manuscript as a stand-alone work that does not rely on Paper I(a)'s structural-closure claims.

### P1B-E6 — Sample-count inconsistencies among Abstract, Table I, Figure 1, Figure 2, and Footnote 1
The full-tension chain has at least four distinct sample-count numbers in this paper:
- Table I: 176,240 raw samples (full-tension column)
- Footnote 1: post-burnin = 123,368 (computed) vs 123,129 ("within ±1%")
- Figure 1 caption: 119,617 post-burnin samples
- Figure 2 caption: 175,545 samples (full-tension legend)

None of {175,545, 176,240, 119,617, 123,129, 123,368} is reconcilable to the others without a separate explanatory paragraph, and one (175,545) is not explained at all. The 309,189 abstract figure assumes 176,240 + 132,949, so the 175,545 in Fig. 2 is internally undocumented.

**Fix:** Choose one accounting convention (raw / post-burnin / effective with weights) and use it consistently across all tables, figures, and the abstract.

### P1B-E7 — ALP-MCMC posterior is outside its own prior envelope, then declared "consistent"
§VI, p. 8 acknowledges: "the data-preferred posterior implies the joint product Caγ (∆ϕ/fa) ≈ 10.3, which at the quoted Caγ = 8 fixed corresponds to ∆ϕ/fa ≈ 1.29, ∼ 17% above the natural envelope upper bound." If the posterior peaks **outside the prior on ∆ϕ/fa = [0.2, 1.1]**, the chain is prior-edge-truncated and the quoted βALP = 0.336° ± 0.107° cannot be interpreted as a Bayesian posterior — it is a prior-railed estimate. Either the prior on (θi, m/H0) must be widened until the posterior is interior, or the result must be reported as a prior-boundary-driven artifact, not as a measurement.

**Fix:** Widen the natural-prior box and rerun, or report the posterior explicitly as boundary-pulled and remove "βALP consistent with βobs" framing.

### P1B-E8 — 3.6σ (H0) and 3.2σ (MB) are conflated as "the same canonical Hubble tension"
§III, p. 5: "This offset is ∼3.2σ relative to the chain's σMB = 0.049 marginal width and corresponds exactly to the canonical 3.6σ Hubble tension manifesting in the MB axis (the same ∼3.6σ that appears in H0 when the tension is expressed in distance-ladder terms)." The two values are not "exactly" the same; they are 3.16σ and 3.59σ, computed from different parametrizations with different propagated uncertainties. The word "exactly" is wrong by ~14%.

**Fix:** Remove "exactly" and "the same"; report the two tensions as numerically distinct manifestations of the same underlying disagreement.

### P1B-E9 — Stated contribution is null; manuscript does not earn the page count
The abstract and Introduction explicitly state all three analyses are non-tests of ECH: stock CAMB ≠ torsion module; MC validation ≠ sky detection; spectator-ALP ≠ distinctive ECH prediction. The "Key finding" in §III is "∆Neff consistent with zero ... The ∆Neff extension alone does not resolve the Hubble tension." The §VII Conclusions reiterate this. **The paper documents three null verification exercises that the author themselves declares insufficient to test the theory.** PRD requires positive scientific content. As written, this manuscript should be ≤4 pages and submitted as a methodology note, not 11 pages of caveats and recomputation.

**Fix:** Either (a) rescope to a methods-note format ≤4 pages, or (b) produce an actual modified-CAMB ECH-torsion module and rerun, so that the paper has a positive content claim.

---

## MAJOR findings

### P1B-M1 — SNR conflation between MC sample-mean precision and per-realization sensitivity
The body repeatedly states "SNR_SE = 25.71" and "SNR = 20.32" (§IV) with footnote 3 disclosing that these are sample-mean precisions, with per-realization SNR ≈ 0.91. The published Planck/ACT sky measurements (~2.4–2.9σ) operate at single-sky precision. Quoting the 20.32–25.71 figures in the body and Fig. 3 without explicit "not comparable to sky-detection sigma" qualification at *every* juxtaposition risks misreading. Footnote 3 is insufficient; the qualification must appear in the body at each instance.

### P1B-M2 — w0wa headline result is reported without ln B but with "+4.3σ" departure from ΛCDM
Table II reports w0 = −0.8122 ± 0.0436 as "+4.3σ" from ΛCDM, while §V explicitly defers ∆AIC, ∆BIC, and ln B "to a follow-up nested-sampling analysis." A +4.3σ frequentist marginal-tail figure without a corresponding model-comparison number is inadmissible at PRD for a parameter ratio that the author admits sits in the unsampled tail of a Metropolis–Hastings chain. The footnote tries to soften this with "posterior-tail extrapolation distance only," but the figure remains in the rightmost column of Table II as the headline.

**Fix:** Either run nested sampling (as the paper promises three times) before submission, or remove the "vs LCDM" column from Table II.

### P1B-M3 — Required Caγ ∈ [9, 51] is dismissed without consequence
§VI states the required photon coupling spans 9–51, well above the standard KSVZ/DFSZ |Caγ| ~ O(1) benchmarks, then concludes "The signal is therefore accommodated across the considered parameter space rather than fine-tuned only at one benchmark." A factor-9 to factor-51 enhancement over the standard ALP benchmarks *is* fine-tuning, particularly when combined with the disclosed θi ~ 0.1 fine-tuning (~25× per fn. 5). The paper acknowledges all of this but then sells the result as "consistent." It is consistent only with substantial UV-completion model-building plus a ~25× misalignment tuning plus a ~10–50× photon-coupling enhancement. This is not "consistent"; this is tightly constrained against.

### P1B-M4 — Appendix A advertises galaxy-chirality pipeline code irrelevant to this paper
Appendix A lists "galaxy_spins/spin_fit_stan.py—hierarchical Bayesian model (CmdStanPy) fitting A(z) to published aggregate CW/CCW galaxy counts" and "data_build/build_galaxy_spin_dataset.py—reproducible pipeline downloading Galaxy Zoo DECaLS." This paper does not discuss galaxy chirality. The Galaxy Zoo content belongs in Paper IV [6] (which is "in preparation"). Including it here is misleading.

**Fix:** Remove galaxy-spin code references from this manuscript's reproducibility appendix.

### P1B-M5 — Liu et al. [11] "independent cross-validation" is not a cross-validation
§III, p. 5: "Liu et al. [11] constrained an EC torsion model... Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8." Liu et al. used a torsion-modified Boltzmann code; this paper used stock CAMB without torsion. Agreement at 0.5σ between stock-ΛCDM+∆Neff and a torsion model says only that present data lack the precision to distinguish them — it does not "cross-validate" anything about ECH.

**Fix:** Either remove this paragraph or rewrite it honestly as "current data lack the sensitivity to distinguish these models."

### P1B-M6 — Section VI delivers no ECH-specific content
The section heading is "Cosmic Birefringence: Spectator ALP Consistency Check," but the section itself admits "The model class was previously studied by Fujita et al. [21]," "The same prediction β ≈ 0.27° arises in standard GR with an identical ALP Lagrangian," and "The ECH framework provides heuristic motivation ... but no derived photon-torsion coupling connects the Holst action to a specific ALP potential." The section therefore does not test, support, or constrain ECH. It should be removed or reduced to a single paragraph in the Introduction noting that any ALP-based birefringence interpretation is model-independent.

### P1B-M7 — Excessive caveat-to-content ratio
Almost every numerical claim in this paper is followed by a 2–4 sentence disclaimer, often with nested footnote disclaimers (footnote 1's reconciliation, footnote 3's SNR disambiguation, footnote 5's spectator-status caveat, footnote 6's backreaction disclosure). The disclaimer text exceeds the result text. A PRD paper should establish a result; this paper hedges three non-results.

---

## MINOR findings

### P1B-Mi1 — Date "2026-06-08 PDT" and "April 2026" / "early 2030s" forward references
The cover date is 2026-06-08 PDT and the body says "Independent verification (production 500-realization run, April 2026)." This is unusual but not invalid; please confirm date consistency upon resubmission.

### P1B-Mi2 — Footnote 'a' on the title page is a multi-paragraph disambiguation
The PR3/PR4 disambiguation in footnote 'a' is necessary content but should be promoted to a section or methods note, not buried in a title-page footnote.

### P1B-Mi3 — Figure 1 corner plot lacks axis units on some panels (e.g., ΔNeff is dimensionless but H0 axis units not displayed in subscripts)
Standard PRD plotting hygiene; please add explicit units to every axis.

### P1B-Mi4 — Table III "Status" column includes "Defn." entries for scope statements
"Stock CAMB proxy ≠ ECH theory module — Scope — Defn." A scope statement is not a verified claim; it is a definition. Either drop these rows or reformat the table to separate definitions from claims.

### P1B-Mi5 — Table I worst-row R̂−1 footnote refers to "k = 7" but the chain has 17 parameters
Footnote a in Table I notes "references to 'k = 7' elsewhere in this paper refer to the cosmological-parameter count only" — this is an editorial-bookkeeping disclosure that should be removed; the table itself should simply state the relevant parameter count.

### P1B-Mi6 — Eq. (3) prefactor αEM × 8 / (4π) is missing parentheses
"β ≈ αEM × 8 / 4π × 1.07" should be β ≈ (αEM × Caγ)/(4π) × (Δφ/fa). The way it is written is ambiguous about operator precedence.

### P1B-Mi7 — χ²_total stated as 14037.4 ± 5.6, but explained as a "0.1-unit arithmetic-rounding artifact"
The footnote attempts to reconcile 14037.4 vs 10.6 + 10983.9 + 3043.0 = 14037.5. This 0.1-unit discrepancy is harmless but the explanation should be one sentence, not three.

### P1B-Mi8 — fn. 4 conflates ΛCDM background with quintom-bounce dynamics
"The ΛCDM-background choice is conservative for the ALP-MCMC" — a conservative choice for ALP forecasting in a quintom cosmology is not obviously the ΛCDM background; this should be quantified rather than asserted.

---

## NITS

### P1B-N1 — "spectator-status caveat" phrase repeated in abstract and §VI and fn. 5 and fn. 6
Same caveat appears at least four times. Pick one location.

### P1B-N2 — "matter-bounce-class" hyphenation inconsistent
"matter-bounce" vs "matter-bounce-class" vs "minimal-ECH" — choose one and apply consistently.

### P1B-N3 — Repeated "spin-torsion" capitalization inconsistency
"Einstein-Cartan-Holst" vs "Einstein–Cartan–Holst" (en-dash vs hyphen). Use en-dashes throughout per PRD style.

### P1B-N4 — "(in preparation)" five times in references
Refs [1], [3], [4], [5], [6] are all "(in preparation)" or arXiv preprints with no journal. PRD generally requires either published or simultaneously submitted companion papers.

### P1B-N5 — Reference [10] formatting
"Y.-F. Cai, W. Xue, R. Brandenberger, and X. Zhang, Non-gaussianity in a matter bounce, JCAP 0905, 011, arXiv:0903.0631." — JCAP volume/issue/article-id formatting is non-standard; should be JCAP 05 (2009) 011.

---

## Summary recommendation

# REJECT

This is not a publishable PRD manuscript in its current form. The author has produced three numerical exercises, **each of which the abstract and body explicitly state does not test the theory the paper claims to verify**: the MCMC is stock CAMB with no torsion modifications; the NaMaster MC is a pipeline-recovery validation explicitly disclaimed as not a sky measurement; and the spectator-ALP exercise is explicitly disclaimed as not a distinctive ECH prediction because the same physics arises in standard GR. After 11 pages, the manuscript reaches the conclusion that "current data neither require nor exclude" the theory and defers the actual statistical tests (∆AIC, ∆BIC, ln B, modified Boltzmann code) to follow-up work. Layered on top of this null-content structure are a hard arithmetic error in the wpivot derivation in Table II (factor-2.5 inconsistency in the variance formula), a sign error in the same footnote's pivot definition, an abstract bias figure that contradicts the body, at least four mutually inconsistent sample counts for the full-tension chain (175,545 / 176,240 / 123,368 / 119,617), an ALP MCMC whose posterior peaks *outside* its own stated prior envelope and is nevertheless declared "consistent," extensive embedded review-log prose ("an earlier count erroneously quoted," "a concern was raised that," "NOT a YAML alias failure"), and a citation structure in which the four primary companion papers it depends on are all "in preparation." The author should either (i) write Paper I(a), produce a torsion-modified CAMB, and submit a real verification paper; or (ii) rescope this material as a ≤4-page methods note that honestly states it is a null exercise with the wpivot and bias-headline arithmetic corrected and all review-log prose removed.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings on Re-Examination

Several substantive issues escaped my initial pass. The most consequential are a mathematically impossible covariance structure in Table II, a misclassification of the NaMaster bias as additive when it is in fact multiplicative, and a stale-σ floor in the abstract that does not appear anywhere in the body.

---

## ESSENTIAL (new)

### P1B-E10 — Table II covariance structure is mathematically impossible (|ρ| > 1)
This is independent of the sign error in P1B-E2. Take the Table II displayed numbers at face value:
- σ_w0 = 0.0436, σ_wa = 0.1864, ap = 0.6680, σ_wpivot = 0.0301.

The pivot-decorrelation condition Cov(w_pivot, w_a) = 0 forces (1−a_p) = −Cov(w_0,w_a)/Var(w_a), so
Cov(w_0, w_a) = −(1 − a_p) Var(w_a) = −0.3320 × 0.0347 = **−0.01153**.

The Cauchy–Schwarz bound is |Cov| ≤ σ_w0 σ_wa = 0.0436 × 0.1864 = 0.008128.

The implied |Cov| = 0.01153 **exceeds the maximum allowed by the marginal sigmas by 42%**, corresponding to a correlation |ρ| ≈ 1.42 — impossible for a valid posterior. Independently, the displayed σ(w_0+w_a) = 0.1485 implies Cov(w_0, w_a) ≈ −0.0073 (giving ρ = −0.90, a_p ≈ 0.79); this is mutually inconsistent with both the displayed a_p = 0.6680 and the displayed σ_wpivot = 0.0301. The Table II covariance structure is therefore over-determined and **no single posterior covariance matrix can reproduce all five displayed numbers simultaneously**. Either at least two of {σ_w0, σ_wa, σ(w_0+w_a), σ_wpivot, a_p} are wrong, or the underlying chain is not converged and its sample covariance matrix is not positive-semidefinite. Either way, the headline +4.3σ and −1.1σ tension figures are unreliable.

**Fix:** Print the full chain covariance matrix C(w_0, w_a) and recompute every dependent quantity from it. Do not present derived 1-d quantities (σ_wpivot, a_p, σ(w_0+w_a)) until they all reconcile to a single C.

### P1B-E11 — NaMaster bias is multiplicative (~12% gain error), not "additive systematic floor 0.04°"
Recovered/injected ratios:
- 0.238° / 0.27° = **0.881** (−11.9%)
- 0.302° / 0.342° = **0.883** (−11.7%)

These two ratios agree to 0.2%. The bias is therefore an extremely clean **multiplicative gain error of ~11.8%**, not the additive offset of 0.032–0.040° that the body and §VII Conclusions describe. The "amplitude-dependent component ∼12%" phrasing in §IV mis-characterizes a fundamentally multiplicative calibration as a small additive perturbation. The consequence is large: if applied to a sky measurement that recovers β_observed = 0.30°, the inferred true β would be 0.30/0.88 ≈ 0.34°, shifting Planck NPIPE's value by 0.04° — comparable to its 1σ uncertainty of 0.11°. The framing "NaMaster systematic floor 0.04°" understates this calibration error by failing to identify its multiplicative character.

**Fix:** Re-report the result as a multiplicative gain g = 0.882 ± δg with explicit per-injection scatter, and propagate this calibration into any pipeline product. Remove the "additive floor 0.04°" language.

### P1B-E12 — Per-realization NaMaster σ_β̂ ≈ 0.26°, more than 2× worse than Planck's actual 0.11°
From SNR_SE = β̂√N/σ_β̂ with N=500 and SNR_SE = 25.71 at β̂ = 0.302°:
σ_β̂ = 0.302 × √500 / 25.71 = **0.263°**.

Planck NPIPE reports σ_β = 0.11° on the sky. The MC's per-realization sensitivity is therefore ~2.4× worse than the actual data being "validated." A pipeline-recovery exercise at noise level that cannot reach the published sensitivity is not a meaningful validation of the published result. The "conservative worst-case bias check" framing acknowledges this but does not address the consequence: the MC noise model does not exercise the pipeline at Planck-relevant precision, and the bias under the actual Planck noise covariance is left untested.

**Fix:** Rerun the MC at the Planck NPIPE noise level (ΔP ≈ 35 µK·arcmin for 143 GHz polarization in the relevant ℓ range), and report the bias at the sensitivity that corresponds to the published measurement.

---

## MAJOR (new)

### P1B-M8 — Abstract's "2.4–2.9σ" sky-detection range has no derivation for the 2.4σ floor
The abstract and §VII state "the published Planck/ACT DR6 2.4–2.9σ [2,3]." The body cites:
- Planck NPIPE [15]: β = 0.30° ± 0.11° → 2.73σ
- ACT DR6 [3]: β = 0.215° ± 0.074° → 2.91σ
- Eskilt+Komatsu joint [2]: β = 0.342° ± 0.094° → 3.64σ

The value 2.4σ does not arise from any quantity quoted in the body. The lower bound of the abstract's range is therefore unsourced (possibly a stale reference to Minami+Komatsu 2020 PR4 = 2.5σ, but that is not the [15] cited here).

**Fix:** Replace "2.4–2.9σ" with the actual interval [2.7σ, 2.9σ] derivable from refs [15] and [3], or cite the source for 2.4σ explicitly.

### P1B-M9 — Figure 3 caption's "Eq. 1–3" cross-reference is wrong
Caption: "Bias β̂ − β_inj is below 0.04° across the natural resolution range; this is the NaMaster systematic floor adopted in Eq. 1–3."

Eq. (1) is β_NaMaster = 0.238° (the bias result itself). Eq. (2) is Δφ/fa ≈ 0.65 (ALP-field evolution). Eq. (3) is β ≈ 0.29° (ALP birefringence prediction). The "systematic floor" is not "adopted in" Eqs. (2) or (3); those are physics derivations, not pipeline validation. The cross-reference is a self-citation error.

**Fix:** Reference only Eq. (1) (or, more honestly, do not claim the floor is "adopted" anywhere — it is reported, not adopted).

### P1B-M10 — Caγ(Δφ/fa) ≈ 10.3 is derived from β_obs = 0.342°, not from β_ALP = 0.336° (the chain output)
§VI: "the data-preferred posterior implies the joint product Caγ (Δφ/fa) ≈ 10.3." But the chain output is β_ALP = 0.336° (not 0.342°). Using β_ALP = 0.336°:
0.336° × π/180 = 5.864×10⁻³ rad; divided by α_EM/(4π) = 5.81×10⁻⁴ gives Caγ(Δφ/fa) = **10.09**, not 10.3, and at Caγ = 8 fixed gives Δφ/fa = 1.26 (14% above the natural upper bound, not 17%).

The paper conflates "data-preferred posterior" (β_ALP) with "headline observational value" (β_obs) when deriving the joint product. These are not the same number.

**Fix:** Derive Caγ(Δφ/fa) consistently from one chosen β and label it clearly.

### P1B-M11 — Fig. 2 BBN/ACT reference lines (0.41, 0.40) do not correspond to published values
Figure 2 (a) overlays vertical reference lines at "BBN 2σ upper (0.41)" and "ACT DR6 central (0.40)" on the ΔN_eff axis. Standard BBN (D/H + Y_p) gives ΔN_eff ≲ 0.3–0.4 at 2σ depending on D/H choice — 0.41 is plausible but should be sourced. ACT DR6 + Planck gives N_eff = 2.86 ± 0.13 (Madhavacheril+2024), i.e. ΔN_eff = −0.05, not "central = 0.40." The 0.40 reference is either misattributed or stale from a different combination (perhaps ACT DR4 + WMAP).

**Fix:** Cite the precise source for each reference line, or remove the lines.

### P1B-M12 — Multiplicative bias propagation to the ALP-consistency claim is not done
If the NaMaster pipeline systematically recovers β̂ = 0.88 × β_true, then any inverse-application to a sky measurement requires the inverse correction. The §VI ALP-consistency claim that the ALP MCMC posterior β_ALP = 0.336° is "consistent with" β_obs = 0.342° does not propagate this gain calibration. If the published β_obs were re-calibrated by /0.88, the inferred true β would be ≈ 0.39°, increasing the required Caγ(Δφ/fa) product to ~11.7 and the upper-end fine-tuning correspondingly.

**Fix:** Either propagate the gain calibration through the ALP comparison, or state explicitly that the gain calibration is not applied to published Planck/ACT numbers and explain why not.

### P1B-M13 — "Midpoint m ≈ 1.8 H0" does not equal the prior midpoint m = 2 H0
§VI: "The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H0, Δφ/fa ≈ 1.0."

The prior on m/H0 is [1, 3], with arithmetic midpoint 2. The "1.8 H0" value is off by 10% from the prior midpoint and is not explained.

**Fix:** Either use the actual midpoint m = 2 H0 with the corresponding Δφ/fa, or label "1.8 H0" as the value at which β = 0.27° is achieved (and explain the calculation).

---

## MINOR (new)

### P1B-Mi9 — H0 reported as 67.68 in Table I/Abstract/§VII but 67.69 in §III caveat text
The §III caveat paragraph reads "the full-tension chain returns H_0 = 67.69 ± 1.06" while Table I, the abstract, and §VII all give 67.68. Likely a rounding drift, but inconsistent at the quoted precision.

### P1B-Mi10 — ΔN_eff reported as "−0.020 ± 0.169" vs "−0.02 ± 0.17" inconsistently
Abstract, Table I, and Fig. 2 caption use 3-digit precision; §III caveat text and §V summary use 2-digit. Round consistently.

### P1B-Mi11 — Equation (3) silently mixes radians and degrees
β ≈ (α_EM × 8 / 4π) × 1.07 ≈ 0.29°: the LHS is in degrees, the RHS expression evaluates to radians, and the conversion factor 180/π is implicit. Display the conversion explicitly.

### P1B-Mi12 — χ²_total σ = 5.6 does not equal sqrt-sum 5.82 of channel uncertainties
With σ_BAO = 1.8, σ_CMB = 5.3, σ_SN = 1.6: √(1.8² + 5.3² + 1.6²) = 5.82. Table II reports 5.6. The 4% discrepancy could be from anticorrelations across channels but is not explained.

### P1B-Mi13 — "iter2 chain" notation in Table II footnote b is unexplained
Implies a prior chain was run and abandoned; document or remove.

### P1B-Mi14 — Figure 2 legend says "Full tension (175,545 samples)" but no other location uses this number
Adds a fifth sample count to the already-confused stratification stack (cf. P1B-E6). The Planck+BAO+SN legend correctly matches Table I (132,949), so the discrepancy is full-tension-specific.

---

## NIT (new)

### P1B-N6 — "∼17% above the natural envelope" is computed from a stale β
17% comes from (1.29 − 1.1)/1.1 = 17.3% with Δφ/fa = 1.29 derived from β_obs = 0.342°. From β_ALP = 0.336° the figure is 14%.

### P1B-N7 — "early 2030s" LiteBIRD forecast in §VII
LiteBIRD is currently scheduled for late-2032 launch with first results ~2034. "Early 2030s" is at the optimistic edge; "mid-2030s" is more standard.

### P1B-N8 — "RunPod H200" in Acknowledgments
Naming a commercial cloud GPU vendor in the acknowledgments is unusual for PRD; either cite as a computational facility or remove.

---

## Summary of new findings vs. initial review

The initial review caught the macro-level scope and arithmetic problems (wpivot σ formula, sign error, bias-headline mismatch, sample-count chaos, ALP prior-edge truncation). It missed three quantitatively serious issues:

1. **The Table II covariance is not just sign-wrong, it is internally infeasible** — no posterior covariance matrix exists that reproduces all the displayed numbers.
2. **The NaMaster bias is multiplicative at 11.8% gain**, not additive at 0.04°. This is the largest substantive misinterpretation in the paper and changes the methodological story entirely.
3. **The MC noise level is 2.4× worse than the actual Planck data**, so the "validation" never exercises the pipeline at the relevant sensitivity.

These reinforce the initial **REJECT** recommendation. The Table II covariance infeasibility (P1B-E10) alone — independent of all the scope issues — invalidates the headline w_0wa result the paper relies on; the multiplicative bias re-interpretation (P1B-E11) invalidates the headline pipeline-validation claim. These are not editable issues; they require reruns and reanalysis before resubmission.