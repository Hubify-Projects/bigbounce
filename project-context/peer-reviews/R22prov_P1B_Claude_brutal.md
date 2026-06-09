# P1B R22prov — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11896 chars)
**Wall time**: 454.5s

---

# Referee Report — P1B "Technical Verification Companion to the ECH Spin-Torsion Program"

## Overall assessment

The paper packages three loosely-related analyses, each of which is *explicitly disclaimed by the authors themselves* as not testing the theoretical framework the paper is allegedly verifying:

1. The MCMC is "Not a spin-torsion theory module" (their own words, §III header).
2. The NaMaster pipeline does "NOT [test] the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α" (abstract).
3. The ALP birefringence is "Not a distinctive ECH prediction" (§I.3).

The paper is therefore a 12-page document in which the authors carefully explain that they have not actually verified the theory they are companion-papering. PRD does not publish methodological null-results companion papers to unpublished theoretical papers. Compounding the problem: the body is heavily contaminated with review-response prose, internal version-control language, redundant disclaimers, and at least one numerical inconsistency presented as agreement. I recommend rejection.

---

## ESSENTIAL findings

**P1B-E1 [Companion to unpublished papers] — pp. 1–2, 11**
Paper I(a), Paper II, Paper III, and Paper IV are all cited as "in preparation" (refs. [1], [4], [5], [6]). The entire premise of this "Technical Verification Companion" is that it supports Paper I(a). PRD cannot accept a companion paper to a paper that does not exist in any reviewable form. Either bundle all the content into a single submission, or wait until Paper I(a) is at minimum on arXiv with a stable version.

**P1B-E2 [Contribution does not clear the PRD bar] — entire paper**
The author's own scope statements (§I, p. 2) establish that:
- The MCMC tests stock ΛCDM+∆Neff with no torsion modifications, and the data are consistent with ∆Neff = 0.
- The NaMaster run is a *pipeline calibration check*, not a sky measurement.
- The ALP β prediction is identical in standard GR.

What new physics result does this paper establish? None is identifiable. Recompute the actual deliverables: a re-derivation of the well-known canonical Hubble-tension persistence under ∆Neff in stock CAMB, a pipeline self-consistency check that recovers an injected signal at the level of the apodization-induced bias, and a numerical evaluation of an ALP β formula whose required Cₐγ ∈ [9, 51] sits "outside minimal ALP photon-coupling benchmarks." There is no PRD-novel result.

**P1B-E3 [Review-response and version-control language inside the body] — multiple pages**
The body contains extensive prose that belongs only in a response-to-referees document:
- §III, p. 3: "An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w0wa samples at the LCDM point…"
- §III, p. 5: "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood…"
- §III, p. 5: "A concern was raised that the joint posterior mean (MB = −19.263, H0 = 67.69) was inconsistent with an active sn.pantheonplus likelihood, claiming a Cobaya YAML alias failure."
- §III, p. 5: "NOT a YAML alias failure; the parameters are correctly aliased per the spin_torsion.input.yaml configuration"
- §IV, p. 6: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°…"
- §VI, p. 8: "Because the EOM-required coupling range [∼9, ∼51] exceeds the Cₐγ ∈ [1, 30] prior of the original extended configuration (which truncated ∼28% of the posterior mass above Cₐγ = 30), we reran the Cₐγ-free fit…"
- §VII, p. 9: "the 16-rank mpirun process terminated automatically upon reaching the convergence threshold"
- §V.A, p. 7: "Cobaya [20] (v3.5 original; v3.6.1 verification)"

Strip all of this and rewrite the body as a self-contained scientific document. The reader does not need to know what earlier drafts said.

**P1B-E4 [Self-contradiction: "3.6σ exactly" vs. computed 3.2σ] — §III, p. 5**
The "Mᵦ–H0 joint-posterior offset check" reports the MB-axis offset as "∼ 3.2σ relative to the chain's σ(MB) = 0.049 marginal width" but then claims this "corresponds *exactly* to the canonical 3.6σ Hubble tension." Recomputed: 0.155/0.049 = 3.16σ, not 3.6σ. These are different numbers; calling them "exactly" the same is wrong. Either explain quantitatively how the H0-axis 3.6σ maps to a 3.2σ MB-axis offset (degeneracy projection) or remove the "exactly" claim.

**P1B-E5 [Pipeline-validation SNR juxtaposed with sky-detection SNR without per-instance disclaimer] — §IV, pp. 2, 5, 6**
The abstract qualifier is acceptable, but in §IV (p. 6) and Footnote 3 the values 20.32 and 25.71 are repeatedly juxtaposed against the per-map 2.4–2.9σ literature numbers. The required PRD standard is an explicit "not directly comparable" qualifier at every juxtaposition, including in figure captions. Fig. 3 caption shows "Lead result" annotation against a 0.27° line without indicating that the y-axis represents pipeline recovery, not sky-detection significance.

**P1B-E6 [Internal bookkeeping table (Table III) does not belong in a PRD paper]**
Appendix B "Claims classification" with columns "Status: Verified / Omitted / Cited" reads as an internal QA worksheet. PRD readers do not need a verification matrix; they need a methods section. Either delete Table III or fold its information into the methods narrative.

**P1B-E7 [DESI w₀wₐ posterior reported with no model comparison — the only potentially significant result is methodologically incomplete] — Table II, §V.B, pp. 4, 7**
Table II reports w₀ = −0.812 ± 0.044 (+4.3σ from −1) and wₐ = −0.667 ± 0.186 (−3.6σ from 0). These are the most observationally consequential numbers in the paper, yet §V.B explicitly defers all model comparison ("χ²_eff, AIC, BIC, or ln B Bayes-factor model-comparison numbers" are not reported) and admits the Savage–Dickey readout fails because (w, wₐ) = (−1, 0) is unsampled. The author cannot have it both ways: either report a quintom detection with proper Bayesian evidence, or remove the "canonical quintom signature" language. The current presentation is a marginal-tail extrapolation, the σ values are not joint significances, and the table's own note "marg.-tail" admits this. Either run the deferred nested-sampling analysis before resubmission, or remove Table II from this paper.

**P1B-E8 [Spectator-ALP "natural-parameter" claim contradicts the disclosed 25× fine-tuning] — §VI, abstract, §VII**
The paper's own footnote 5 and §VI body establish that the spectator regime (Ωₐ ≪ 1) requires θᵢ ∼ 0.1, while the natural-prior scan adopts θᵢ ∈ [0.5, 2]. The ∼25× misalignment fine-tuning is acknowledged. Despite this, the abstract still says "a field with fₐ ∼ M_Pl, m ∼ H0 is consistent with the published joint WMAP+Planck value" with only a parenthetical caveat. Either the abstract calls out the 25× tuning at the same prominence as the consistency claim, or the consistency claim should be downgraded.

Additionally: the headline ALP-MCMC "β_ALP = 0.336° ± 0.107° at Cₐγ = 8 fixed" requires Cₐγ ⋅ Δφ/fₐ ≈ 10.3. With Cₐγ = 8, this demands Δφ/fₐ ≈ 1.29, which the paper admits is "∼17% above the natural envelope upper bound." So the central reported value is itself outside the natural envelope. This should be stated in the abstract.

---

## MAJOR findings

**P1B-M1 [Eskilt–Komatsu dataset attribution is admitted-ambiguous in the abstract footnote]**
Abstract footnote 'a' acknowledges that the "PR4/NPIPE" labels refer to the *repository* code dataset, while the headline 0.342° ± 0.094° is from the *published* PR3+WMAP9 analysis. Having a dataset-attribution disambiguation footnote in the abstract is a red flag indicating the dataset provenance has not been cleanly handled in the body. Rewrite so that throughout the paper, every quoted β value names exactly one dataset and the reader does not need to re-read a footnote.

**P1B-M2 [Reference [3] arXiv:2509.13654 unverifiable]**
Diego-Palazuelos & Komatsu "Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654" — please verify this arXiv ID is correct and that the cited β = 0.215° ± 0.074° (3σ?) is the value the paper actually quotes. The ACT DR6 birefringence literature should be cited to a stable, verifiable reference. Same for reference [11] arXiv:2507.04265 (Liu et al.).

**P1B-M3 [Cₐγ continuous-prior MCMC: "69% of posterior mass in [9, 51]" is essentially tautological]**
§VI, p. 8: The reported posterior median Cₐγ = 20.7 with [7.3, 45.6] 68% interval, fit against a single summary statistic β = 0.342° ± 0.094°, is a fit of a one-dimensional constraint Cₐγ Δφ/fₐ ≈ 10.3 against three sampled parameters. The marginal Cₐγ posterior is therefore dominated by the prior on (Δφ/fₐ), itself determined by the priors on (θᵢ, m/H₀). Stating that 69% of the posterior mass falls in the EOM-required band [9, 51] is a circular statement: the EOM-required band *is the prior weight* under the implicit Δφ/fₐ distribution induced by the prior box. Either marginalize against an explicit prior choice and report the prior-dependence, or remove the 69% claim.

**P1B-M4 [Figure 4 caption claims consistency at "within 1σ" but the marginal numbers are not statistically independent]**
Fig. 4 caption: "The rotation marginal, β = 0.324° ± 0.099°, is consistent within 1σ with the fixed-Cₐγ = 8 result β_ALP = 0.336° ± 0.107° and the observed β_obs = 0.342° ± 0.094°." All three are fits to the *same* β_obs. The "consistency" is enforced by the likelihood, not measured. This is a misleading characterization.

**P1B-M5 [fsky sweep: per-realization σ_β scaling is implausible without further explanation] — §IV, p. 6**
The canonical fsky = 0.32 run has σ_per_realization = β̂/SNR_real = 0.238/0.91 ≈ 0.262° (from footnote 3). The fsky = 0.85 sweep reports σ_β = 0.029°, a factor of ∼9 reduction. Naive sky-fraction scaling gives √(0.85/0.32) ≈ 1.6 or 0.85/0.32 ≈ 2.7. A factor of 9 needs explanation. Either I am missing the noise/ℓ-range configuration difference, or the numbers are inconsistent with each other.

**P1B-M6 [§III's footnote 2 invokes a strong-coupling scale "M_Pl/√γ_BI" without derivation]**
Footnote 2 cites this scale to ref. [9] (Mercuri 2006). Mercuri's paper does not, to my recollection, identify a strong-coupling cutoff at this scale. Please provide an explicit citation point (equation number or section) inside [9] where this scale is derived, or justify the cutoff independently.

**P1B-M7 [Footnote 1 sample-count reconciliation is impossibly convoluted]**
The reconciliation between 309,189 raw, 216,432 post-burnin, 123,368 expected full-tension subset, 123,129 actual, and 119,617 in Fig. 1 requires four levels of explanation. The reader should not need a four-way reconciliation footnote. Either report a single consistent post-burnin count throughout, or remove the inconsistent secondary numbers.

**P1B-M8 [Liu et al. "0.5σ in H₀ and 0.4σ in σ₈" cross-check unverifiable] — §III, p. 5**
What are the Liu et al. values of H₀ and σ₈ that produce these σ-offsets? Not given. The reader cannot reproduce the claim.

**P1B-M9 [Page count too long for actual content]**
Twelve PRD pages for: two ΛCDM+∆Neff posteriors (Table I), one pipeline validation figure (Fig. 3), and one ALP consistency table. The actual scientific deliverables would fit in 4–5 PRD pages. Recommended maximum: 5 pages plus references.

**P1B-M10 [Heuristic-only ALP-ECH connection]**
§VI, p. 7 and §VII, p. 9: "The ECH framework provides heuristic motivation (fₐ ∼ M_Pl from the Holst sector pseudoscalar structure) but no derived photon-torsion coupling connects the Holst action to a specific ALP potential." Then the paper should not present this as an ECH consistency check at all. Either remove §VI from this companion paper or derive the photon-ALP coupling from the Holst action.

**P1B-M11 [DES-Y5 SN count] — Ref. [14]**
Ref. [14] cites "∼1500 new high-redshift type Ia supernovae". DES-Y5 has ∼1635 photometrically classified SNe; please verify the count or use the cited value.

---

## MINOR findings

**P1B-m1** Abstract footnote 'a' is unusually long and breaks abstract flow. Move dataset-disambiguation into §IV.

**P1B-m2** §III, p. 3, footnote 1: "(convergence_summary.json)" is a build-artifact reference; cite the artifact properly through the data-release URL.

**P1B-m3** §V.B, p. 7: "the load-bearing numbers used elsewhere in the paper" — informal phrasing.

**P1B-m4** §VII, p. 9: "settled this at ∼9σ in the early 2030s" — write "decisive measurement (σ(β) ≈ 0.03°)" without a future-σ claim that depends on an assumed underlying β.

**P1B-m5** §III, p. 3, Table I footnote a: 17-parameter / 16-parameter sampled list is correct content but reads as a private QA note. Move to appendix.

**P1B-m6** §VI, p. 8: "Eq. (1)-adjacent disclaimer" — there is no Eq. (1) in §VI; this appears to refer to the abstract. Be explicit.

**P1B-m7** Acknowledgments: "The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation." PRD allows this, but the placement immediately preceding "No external funding was received" is awkward.

**P1B-m8** §VII, p. 9: "An additional 114,992-sample Planck-only run is still accumulating" — papers should not report ongoing computations; either include or omit.

**P1B-m9** §V.A, p. 7: "v3.5 original; v3.6.1 verification" — internal version tracking that does not belong in a methods section.

**P1B-m10** Figure 1 caption "(119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1)" — captions should be self-contained; do not require the reader to consult a four-layer reconciliation footnote.

**P1B-m11** §V.B, p. 7: "The headline result is w₀ = …" — this is *not* the headline result of this paper; it is a side analysis. Reword.

**P1B-m12** Reference [1] tag "HUBIFY-2026-001A" is an internal preprint identifier. Use a public arXiv ID or remove.

**P1B-m13** §III, p. 3: "(per the explicit parameter-scope clarification in Sec. V A; the (ω/H)₀ parameter is discussed in Paper I(a) as a phenomenological bounce-class indicator but is not separately sampled here)" — this parenthetical appears verbatim twice in §II and §V.A. Deduplicate.

**P1B-m14** §VI, p. 7: "(taken at scan-prior midpoint values; the ∼25× misalignment tuning required to reconcile the headline result with the spectator-consistent corner is disclosed in Sec. VI and fn. 5)" — circular self-reference; this very sentence *is* in Sec. VI.

---

## NITS

**P1B-N1** "the 0.155 mag offset from the Riess anchor" — give units (mag) the first time the offset is introduced.

**P1B-N2** Footnote 6 in Appendix C duplicates footnote 5 of §VI almost verbatim. Cross-reference, do not repeat.

**P1B-N3** "RunPod H200 instances" — fine, but trim.

**P1B-N4** Spelling consistency: "Pantheon+" vs "Pantheon+" (with non-breaking spaces) inconsistent.

**P1B-N5** Eq. (4) "βcombined = 0.241° ± 0.061° (3.9σ)" — the σ is *not* the significance of detection of a non-zero β under the standard CMB-rotation null; specify what null this is computed against.

---

## Summary recommendation

**REJECT**

The paper's three analyses are each explicitly disclaimed by the author as not testing the framework they are companion-papering: the MCMC is "not a spin-torsion theory module," the NaMaster run is "not a competitive sky detection," and the ALP birefringence "is not a distinctive ECH prediction." What remains is a stock ΛCDM+∆Neff posterior consistent with zero, a pipeline self-recovery test consistent with apodization-induced bias, and a numerical evaluation of a generic ALP β formula that requires either non-minimal photon couplings or ∼25× misalignment fine-tuning. None of this clears the PRD novelty bar. Compounding the substantive problem, the body is contaminated with review-response prose, internal version-control notes, a dataset-disambiguation footnote in the abstract, an internal "Claims Classification" worksheet (Table III), at least one numerical self-contradiction (3.2σ presented as "exactly" 3.6σ), and dependence on four "in preparation" companion papers. If the author wishes to publish in PRD, the recommended path is to merge the load-bearing content with Paper I(a), strip all review-response and version-control language, complete the deferred nested-sampling Bayesian evidence calculation before reporting any quintom-vs-ΛCDM comparison, and resubmit as a single self-contained paper of at most 5–6 PRD pages.

---

## PASS 2 — self-critique findings (what initial review missed)

# Second-Pass Review — Fresh-Eyes Findings

After the arithmetic / cross-reference / null-procedure sweep, several substantive issues escaped the first pass. New findings only:

---

## ESSENTIAL — new

**P1B-E9 [Table II footnote b: stated w_pivot variance formula does not arithmetically reproduce the quoted value]**

Footnote b claims:
> σ²_wpivot = σ²_w0 + (1 − ap)² σ²_wa = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²

Direct computation:
- (0.0436)² = 0.001901
- (0.3320 × 0.1864)² = (0.0619)² = 0.003830
- Sum = 0.005731 → √ = **0.0757**

The claimed RHS (0.0301)² = 0.000906 is off by **a factor of ∼6** from the LHS. Worse, the sign convention is also wrong on physical grounds: at the decorrelation pivot a_p chosen so that Cov(w_pivot, w_a) = 0, the correct identity is

σ²_wp = σ²_w0 − (1 − a_p)² σ²_wa

(because Cov(w_0, w_a) = −(1 − a_p) Var(w_a) at the pivot). With the plus sign in the paper, σ_wp can only ever exceed σ_w0, contradicting the very purpose of the pivot redshift. With the correct minus sign, the RHS = 0.001901 − 0.003830 = −0.001929, **negative** — which means the quoted (a_p = 0.6680, σ_w0 = 0.0436, σ_wa = 0.1864) triple is mutually inconsistent. The implied posterior correlation ρ(w_0, w_a) needed to produce σ_wp = 0.0301 at a_p = 0.6680 violates |ρ| ≤ 1.

This is a load-bearing entry in Table II (it determines the "−1.1σ from −1" quoted as the pivot-w consistency claim) and must be fully reworked.

---

## MAJOR — new

**P1B-M12 [f_sky sweep numbers do not scale with sky area]**

§IV reports per-realization σ_β values:
- Canonical f_sky = 0.32: σ_β,real ≈ 0.262° (back-computed from SNR_SE = 20.32 and √500)
- f_sky = 0.85: σ_β,real = 0.029°
- f_sky = 0.65: σ_β,real = 0.033°

Under the stated "same apodization recipe, noise level, and N = 500 MC realizations" the per-realization σ_β should scale as roughly 1/√f_sky × (mode-count factors), i.e. the 0.85-sweep σ should land near 0.262 × √(0.32/0.85) ≈ 0.16°, not 0.029°. Observed reduction is a factor of ∼**9** versus a predicted factor of ∼1.6. Either:
(i) the noise level is actually different across sweeps (contradicting body text), or
(ii) ℓ-range or binning differs, or
(iii) one of the σ values is mislabeled (e.g., SE of the mean reported as per-realization, or vice versa).

If (iii) and the 0.029° is actually the SE of the mean, then σ_per_real = 0.029 × √500 ≈ 0.65° — *higher* than canonical, which is also unphysical for f_sky = 0.85 > 0.32. The sweep numbers as printed cannot be reconciled with each other. Until reconciled, the conclusion "statistically indistinguishable from the canonical-mask bias" cannot stand.

**P1B-M13 ["Natural" prior on θᵢ is precisely the regime the paper excludes from the spectator claim]**

This is a quiet but serious logical issue. §VI and Appendix C define the "natural-misalignment range" as θᵢ ∈ [0.5, 2]. Footnote 5 (and footnote 6 of Appendix C) admit that the spectator condition Ω_a ≪ 1 requires θᵢ ∼ 0.1, *a factor of ∼5 below the lower edge of the "natural" prior*. So the ALP-MCMC's "natural prior" actually samples the **dark-energy-ALP regime**, which the paper explicitly excludes from the spectator-consistency claim. The fixed-C_aγ MCMC posterior reported as "β_ALP = 0.336° ± 0.107°" is therefore obtained over a parameter range where the ALP is *not* a spectator. The abstract claim "a field with f_a ∼ M_Pl, m ∼ H₀ is consistent with the published joint WMAP+Planck value β = 0.342°" is supported only in this DE-ALP regime, not in the spectator regime, and the abstract does not make this clear.

**P1B-M14 [β_free posterior σ exceeds the input-likelihood σ, suggesting the "model-independent" MCMC has a non-trivial systematic floor]**

The model-independent fit is described as "β as a free parameter, to a Gaussian summary likelihood on the published joint Planck PR4 + ACT DR6 birefringence measurement β_obs = 0.342° ± 0.094°" with flat prior on β ∈ [−2°, 2°]. Under those conditions the posterior should be *exactly* 0.342° ± 0.094° to MCMC-sampling precision. The quoted β_free = 0.344° ± 0.096° has both a 0.002° mean shift and a 0.002° σ inflation (∼2%). For a flat-prior + Gaussian-likelihood fit with 9,720 samples the SE on the mean should be ∼0.094/√9720 ≈ 0.001°, so a 0.002° shift is marginally significant. The σ inflation in particular is unexplained — a flat prior cannot widen the posterior beyond the likelihood. Either (a) the prior is actually informative (contradicting the description), (b) there is an undisclosed additional likelihood term (e.g., the NaMaster systematic floor 0.04° added in quadrature, but 0.094 ⊕ 0.04 = 0.102, larger than 0.096), or (c) the chain has not converged in σ. None of these is acknowledged.

**P1B-M15 [Fig. 4 caption vs body: 0.324° vs 0.326°]**

Body, §VI p. 8: "The recovered β = 0.326° ± 0.099° posterior matches the observed 0.342° ± 0.094°."
Fig. 4 caption: "The rotation marginal, β = 0.324° ± 0.099°, is consistent within 1σ…"

Same continuous-prior run, two different mean values (0.326° vs 0.324°). Pick one and update both locations.

**P1B-M16 [Fig. 2 sample counts differ from Table I by 695 with no explanation]**

Fig. 2 caption: "Full tension (175,545 samples), Planck+BAO+SN (132,949 samples)".
Table I: full-tension raw samples = 176,240; Planck+BAO+SN = 132,949.

The Planck+BAO+SN count matches exactly. The full-tension count is 695 lower in Fig. 2. Footnote 1 explains 176,240 → 123,368 → 123,129 → 119,617 reductions but does not produce 175,545 at any step. This is a fourth distinct full-tension sample count in the paper, joining the already-incompatible set {176,240; 175,545; 123,368; 123,129; 119,617}. Pick one accounting and apply it uniformly.

**P1B-M17 [Eq. (4): "the naive 3.9σ figure is an upper bound on the true significance, not a lower bound" — direction of the inequality is asserted without quantitative correlation estimate]**

The claim is that ignoring positive correlation between the Planck-NPIPE and ACT-DR6 measurements *underestimates* σ_combined and therefore *overestimates* the significance. This is correct in sign — but the body cites the published joint 3.6σ result, implying ρ_eff ≈ 0.45 from inverting the inverse-variance arithmetic. That correlation should be quoted, and the user should be told that "3.9σ → 3.6σ" requires a calibration covariance with a specific ρ; without that the "auxiliary cross-check" cannot be evaluated by the reader.

**P1B-M18 [Bias sign-convention inconsistency between canonical run and f_sky sweep]**

Canonical: "recovers β̂ = 0.238° (pipeline-recovery bias 0.032°)" — positive magnitude, no sign.
f_sky sweep: "recovery bias of −0.033° to −0.034°" — explicit negative sign.

Both are the same kind of bias: β̂ − β_inj = 0.238 − 0.27 = −0.032°. The canonical value should also be reported as **−0.032°** (negative, i.e., under-recovery). The dropped sign matters because the body explicitly characterizes the bias as apodization-induced power suppression — a directional effect that should be reported with sign throughout.

---

## minor — new

**P1B-m15** Abstract reports "∆Neff … −0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN". Inconsistent precision: 0.169 (3 sig figs) vs 0.17 (2 sig figs). Same parameter, same sampler — unify.

**P1B-m16** §VI body claims the continuous-prior posterior has "22% below" [9, 51] band. Median Cₐγ = 20.7 with 16–84% interval [7.3, 45.6] means the 16th percentile sits at 7.3, so by construction *at most* 16% of the posterior is below 9. The "22%" claim is incompatible with the quoted 16th percentile unless the posterior is multimodal with secondary peak below the 16% line — which is not asserted. Either the 22% or the [7.3, 45.6] interval is wrong.

**P1B-m17** Footnote b of Table II: "Cov(w0, wa)/Var(wa)" appears in the definition of a_p, but the sign convention is inconsistent with the formula directly above (a_p = 1 − Cov/Var) and with Linder's standard convention (a_p = 1 + Cov/Var, depending on which sign convention is used for w_a × (1−a)). State the convention explicitly.

**P1B-m18** §VI quotes "Cₐγ × ∆ϕ/fa ≈ 10.3" and derives Cₐγ ∈ [9, 51] from ∆ϕ/fa ∈ [0.2, 1.1]. Lower bound: 10.3/1.1 = 9.36; upper bound: 10.3/0.2 = 51.5. So the range is [9.4, 51.5], not [9, 51]. The lower bound's truncation to 9 is harmless; the upper bound truncation is fine. But then "(22% below, consistent with the low-∆ϕ/fa tail)" should read "*above*" (since low Δφ/fa means high Cₐγ, i.e. *above* 51, not below 9). Sign of the tail-direction claim is inverted.

**P1B-m19** Reference [3] gives the ACT DR6 birefringence as 0.215° ± 0.074°. Quoted significance from this alone is 0.215/0.074 = 2.91σ. The abstract says "Planck/ACT DR6 2.4–2.9σ". The "2.4" lower edge presumably refers to Planck NPIPE 0.30°/0.11° = 2.73σ — not 2.4σ. Where does 2.4σ come from? Either an earlier Planck PR3 value or a typo; please specify.

**P1B-m20** Acknowledgments list "Computational resources were self-funded (RunPod H200 instances)" — H200 GPU instances are not used for CPU-bound Cobaya MCMC; this likely refers to a different workload (e.g., Stan sampling for the spin-fit pipeline of a different paper). Either remove or clarify which analysis used GPU resources.

**P1B-m21** Table II χ²_BAO = 10.6 ± 1.8 for DESI DR2. DESI DR2 BAO contributes ∼14 data points (multiple tracers × BAO observables). χ² ∼ 10 against ν ∼ 13 is a *too-good* fit (χ²/ν ∼ 0.77); this is worth noting or referencing to the DESI χ²-decomposition convention. As stated it could be read as a tension-relieving rather than tension-driving channel.

---

## nits — new

**P1B-N6** "fA ∼ MPl" appears throughout but the precise value (M_Pl = 2.4 × 10^18 GeV reduced, or 1.2 × 10^19 GeV unreduced?) is never specified. For a ∼25× tuning argument the factor of √(8π) matters.

**P1B-N7** §VI: "the spectator-consistent corner of this envelope (θᵢ ∼ 0.1, per fn. 5)" — "corner" implies a 2D edge but the spectator condition is on the single parameter θᵢ. Use "sub-range" or "sliver" (matching the language in fn. 5).

**P1B-N8** Eq. (3) prefactor "1.07" is described as ∆ϕ/fₐ for the midpoint configuration, but Eq. (2) gives ∆ϕ/fₐ ≈ 0.65 for (m = H₀, θᵢ = 1). The midpoint m = 1.8 H₀, ∆ϕ/fₐ = 1.0 yields β ≈ 0.27° — close to but distinct from the 0.29° in Eq. (3). The 1.07 vs 1.0 vs 0.65 numbers float without a clear table mapping (m/H₀, θᵢ) → ∆ϕ/fₐ.

**P1B-N9** Table I caption: "All values are posterior means ± 1σ". Table II is then introduced without restating the convention but reports "Mean ± σ" — make the convention explicit in both.

**P1B-N10** "Stock CAMB" is repeated ∼15 times in the body to emphasize no theory modifications. State once in §III and once in the disclaimer; further repetition is editorial.

---

## Why the first pass missed these

The first pass focused on framing (scope, novelty, fitness-for-PRD) and on the obvious review-response contamination, which dominated the surface of the manuscript. The arithmetic-level errors (E9, M12, M14, M16, M18) and the cross-reference errors (M15, m16, m18) required actually back-computing the σ values and matching numbers across body / table / figure / footnote — a slower pass that the first iteration did not perform systematically. The logical contradiction in M13 (the "natural" prior being the excluded DE regime) was hiding behind the footnote-5 disclosure language and only emerged from the abstract-faithfulness check. The wpivot footnote in particular (E9) is a load-bearing arithmetic error that should have been caught on the first pass given that footnote explicitly displays its arithmetic.

Recommendation unchanged: **reject**, with the additional note that even if the framing concerns of the first review were resolved, the arithmetic and internal-consistency errors documented here would independently require a full rewrite of Table II and §IV/VI before any resubmission.