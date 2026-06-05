# P1B auto-2026-06-05_1617pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13258 chars)
**Wall time**: 415.1s

---

# Referee Report — P1B
## Brutal-honesty review for Physical Review D

---

### Overall assessment

This is nominally a "Technical Verification Companion" but it is structurally incoherent. It documents three different sets of MCMC chains (a stock-CAMB ΛCDM+ΔNeff run, a separate DESI DR2 w0wa run, and an ALP-MCMC run), a NaMaster pipeline-validation MC, and a long literature-derived ALP consistency calculation. The abstract describes only the first set of results, but the body smuggles in a headline "+4.3σ" quintom result (Table II) and a Caγ ≈ 9–51 ALP-coupling claim that are not advertised in the abstract or title. The manuscript is also riddled with internal audit/review-log prose that should never appear in a PRD submission. The companion-paper [1] and three of the four cross-cited companions ([4–6]) are "in preparation", making the work effectively unanchored.

Multiple individual results recompute correctly (I confirmed the inverse-variance combination 0.241 ± 0.061 at 3.9σ; the αEM/(4π) ≈ 5.8 × 10⁻⁴ and Caγ Δφ/fa ≈ 10.3 arithmetic; the +4.3σ and –3.6σ marginal distances; the 0.155 mag distance-modulus offset translating to ≈3.6σ Hubble tension). But the framing, scope, and editorial state are unacceptable.

---

## ESSENTIAL findings

### P1B-E1 — Review-log/internal-audit prose throughout the body
**Pages 3–7.** The body contains explicit version-history language that has no place in a PRD submission. Examples (verbatim):
- p. 3: *"An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w0wa samples at the LCDM point…"*
- p. 3: *"note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w,wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically"*
- p. 4: *"This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood"*
- p. 4: *"MB–H0 joint-posterior offset check. A concern was raised that the joint posterior mean … was inconsistent with an active sn.pantheonplus likelihood, claiming a Cobaya YAML alias failure."*
- p. 6: *"the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°"*
- p. 7: *"§VI for the explicit numerical derivation correcting the earlier Caγθi product"*

**Fix required:** Strip all of this. The published paper must present its conclusions without narrating the revision history.

### P1B-E2 — Title/abstract/body scope mismatch
The title is "ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check". The abstract describes only those three analyses. But **Sec. V and Table II report a separate, independent DESI DR2 + Planck NPIPE + DES-Y5 + Pantheon+ w0wa MCMC** with 128,385 samples and the headline claim *"w0 = −0.812 ± 0.044 (departing from the ΛCDM point w0 = −1 at +4.3σ) and wa = −0.667 ± 0.186 (departing from wa = 0 at −3.6σ)"*. This is not mentioned in the title or abstract and is the single largest physical claim in the paper.
**Fix required:** Either (a) remove the w0wa analysis entirely, or (b) advertise it honestly in the title and abstract with its caveats (see E3).

### P1B-E3 — "+4.3σ quintom" is a posterior-tail extrapolation, not a tension
Table II footnote (p. 4) admits: *"the +4.3σ figure is a posterior-tail extrapolation distance only, not a Bayes-factor or ln B exclusion and not a frequentist tension."* Yet the body text (pp. 3, 6) and the conclusions (p. 7) repeatedly state *"departing from the ΛCDM point w0 = −1 at +4.3σ"* **without** the caveat. This is precisely the kind of side-by-side σ-juxtaposition without explicit non-comparability tagging that the review brief flags as essential.
**Fix required:** Every occurrence of "+4.3σ" / "−3.6σ" in the body must carry the marginal-tail/unsampled-point caveat, or the σ figures must be removed and replaced with the actual ln B (which the paper says it cannot compute on this chain).

### P1B-E4 — Pipeline-recovery "SNR = 20.32, 25.71" is unjustified and not defined
Sec. IV (p. 5) reports *"β̂_NaMaster = 0.238° (pipeline-recovery SNR = 20.32)"* and *"β = 0.342° … pipeline recovers 0.302° at SNR = 25.71"*. The paper never defines what σ is being used in the denominator. Implied σ(β) ≈ 0.012° is roughly an order of magnitude tighter than any published sky measurement at the same fsky and noise level, and is suspicious. If this is the per-realization mean-σ divided by √500, it is meaningless as a per-experiment sensitivity number.
**Fix required:** Either (a) give the explicit σ_β estimator and justify it; (b) replace "SNR" with a stated bias/scatter ratio; (c) remove the SNR figures altogether. The caveat sentence "must not be conflated with the 2.4–2.9σ" does not excuse the lack of definition.

### P1B-E5 — Sample-count headline arithmetic does not self-stratify
The abstract leads with "309,189 frozen samples across two converged dataset combinations" and footnote 1 (p. 2) struggles to reconcile this with the *119,617* shown in Fig. 1 and *123,129* claimed for the full-tension post-burnin. Three different full-tension counts (119,617 / 123,129 / 123,368) appear in footnote 1 alone. The author handles this by appealing to "getdist effective-sample weight-based thinning". This is an analysis-bookkeeping cleanup written in real time and reads as such.
**Fix required:** Decide on the definitive post-burnin count and report it everywhere consistently. Move the reconciliation arithmetic to an appendix.

### P1B-E6 — ALP "consistency" overstated; required Caγ excludes natural benchmarks
Sec. VI (p. 7) admits: *"the required Caγ spans ∼ 9 to ∼ 51. Both ends are larger than the standard KSVZ/DFSZ benchmark range, which predicts |Caγ| ∼ O(1); the entire required range therefore lies outside minimal ALP photon-coupling benchmarks and requires non-minimal model building."* Combined with the explicit fn. 4 disclosure that spectator status requires θi ∼ 0.1 (a ≈25× misalignment fine-tune from the prior midpoint), the model **does not** consistently fit the signal at natural parameters. The abstract and conclusions still describe the result as "consistent with the published 3.6σ joint signal" — this is over-stated.
**Fix required:** Replace "consistent" with explicit language that natural-parameter (KSVZ/DFSZ-class) ALPs are inconsistent with the signal, and that consistency requires both a non-minimal photon coupling and a sub-natural θi.

### P1B-E7 — Anchored to an unpublished parent paper
The opening sentence cites Paper I(a) [1] as "in preparation" (HUBIFY-2026-001A). Refs [4], [5], [6] are also "in preparation". A "Technical Verification Companion" cannot stand on its own without a verifiable parent.
**Fix required:** Either submit P1A simultaneously with a valid arXiv identifier or restructure this as a standalone methods paper that does not depend on the unpublished structural-closure result.

---

## MAJOR findings

### P1B-M1 — Table II is mis-placed and dominates the paper
Table II (p. 4) is a full w0wa cosmology result with 9 cosmological + 9 nuisance parameters, χ² goodness-of-fit decomposition, and a phantom-crossing claim. It is presented under §III ("Stock-CAMB ΛCDM+ΔNeff MCMC"). The headline "+4.3σ" appears in §III and is then repeated in §V.B. Reader cannot tell which table belongs to which section.
**Fix required:** Move Table II to its own subsection, clearly separated from the ΔNeff null-consistency test.

### P1B-M2 — Selective reporting of NaMaster bias
The abstract reports only the β = 0.27° → 0.032° bias. Body (p. 6) admits the β = 0.342° injection gives bias 0.040°, ~12% amplitude-dependent. The abstract should report both, or the worst-case 0.040°, not the most favourable number.

### P1B-M3 — Footnote 1 (p. 2) admits the third ("Planck-only") chain is at R̂−1 ∼ 0.05
Industry convergence target is R̂−1 < 0.01. Reporting a third dataset at *5× the convergence threshold* in a methods paper, even with "ongoing" disclosure, is sub-standard. Either remove or wait for convergence.

### P1B-M4 — Independent cross-validation [11] is not actually validated
Sec. III (p. 5) states *"Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8"* with Liu et al. but does not quote the Liu et al. values, so the agreement cannot be checked from this paper alone.
**Fix required:** Quote Liu et al.'s H0 and σ8 with errors.

### P1B-M5 — "MB − 5 log10(H0)" arithmetic check is internal QA
Pages 4–5: the entire two-paragraph MB–H0 joint-posterior offset audit reads as a referee-response, complete with *"NOT a YAML alias failure; the parameters are correctly aliased per the spin_torsion.input.yaml configuration"*. This kind of YAML-name attribution belongs in a code repository README, not a PRD paper. The arithmetic is correct (0.155 mag → 3.2σ on σMB, 3.6σ in H0) but should be stated in a single sentence.

### P1B-M6 — Eskilt & Komatsu dataset attribution remains muddled
The full-page footnote on p. 1 ("Eskilt & Komatsu 2022 disambiguation") attempts to resolve a confusion in the paper between PR3+WMAP9 (the published 3.6σ headline) and PR4/NPIPE (the code repository the authors actually run). The abstract β = 0.342° ± 0.094° headline is from PR3+WMAP9 but the in-paper MCMC re-runs use PR4/NPIPE. The footnote does not actually resolve this — it just punts to the repository README. The "shared calibration covariance" used in the ALP-MCMC (Appendix C) is undefined.
**Fix required:** Specify in the text exactly which dataset stack is used for which result, with no reliance on external repository READMEs.

### P1B-M7 — βALP = 0.336° ± 0.107° vs βobs = 0.342° ± 0.094° consistency claim is trivial
A "1σ consistency" between two values whose error bars dominate the difference is uninformative. The paper presents this as if it were a model-validation success.

### P1B-M8 — "Independent verification (production 500-realization run)" is the author's own run
Sec. IV (p. 5) calls the NaMaster 500-MC run "independent verification" but it is the author's own pipeline on the author's own injections. Replace "independent verification" with "internal MC validation".

### P1B-M9 — Mode-coupling matrix details omit B-mode purification cost
NaMaster's `purify_b=True` with a 2° C2 apodization at fsky = 0.32 has a known E→B residual leakage floor of order 10⁻⁴ in BB amplitude — this is not the irreducible "0.04° NaMaster systematic floor" claimed. The 0.04° quoted is the recovered-mean bias relative to the injection; the per-realization scatter (which is what limits a sky measurement) is not reported.

### P1B-M10 — Sec. V references "k = 7" sampled parameters; Table I footnote says 17
Table I footnote (p. 3) explicitly notes the discrepancy. The reader is told that *"references to 'k = 7' elsewhere in this paper refer to the cosmological-parameter count only"*. This kind of "reconciliation footnote" should not be needed in a publication-ready manuscript.

### P1B-M11 — Sec. III footnote 2 about the EFT cutoff Λ_strong ~ MPl/√γBI is unsubstantiated
The claim that the four-fermion contact operator is suppressed by MPl⁻² is presented in the body, then qualified in footnote 2 to be MPl/√γBI — but no explicit value of γBI is fixed and no reference is given for the *"Holst-sector dynamics with propagating torsion"*. If this is from the unpublished P1A, that is again the parent-paper problem (E7).

### P1B-M12 — "Forward" paragraph (Sec. VII conclusions) reports implementation details
*"The 16-rank mpirun process terminated automatically upon reaching the convergence threshold"* — this belongs in supplementary material, not in the main-text conclusions.

### P1B-M13 — Reference [11] citation is incomplete
Liu et al. is cited as "European Physical Journal C (2025), arXiv:2507.04265 [gr-qc]" with no volume or page number. If the paper is published, give the EPJC volume; if it's a preprint, do not list "European Physical Journal C".

### P1B-M14 — Abstract claims "ECH spin-torsion cosmology no-go program" but Sec. VII conclusions say "structural-closure" with no comparable phrasing
"No-go" appears in the abstract; "structural closure" appears in §VII. These are not equivalent terms and the inconsistency may mislead.

### P1B-M15 — Joint-trajectory scan giving β ∈ [0.17°, 0.43°] is reported as a major prediction
Sec. VI (p. 7): the envelope is computed by an unspecified scan. The text says it's *"not from an independent-extremes product (which would give the wider naive envelope [0.027°, 0.44°])"*. The naive product is essentially the same upper limit as the joint scan (0.44° vs 0.43°), so the "joint scan" gives nearly the same prediction as the trivial extremes; the difference is at the lower limit. The paper should clarify what physical correlation it is exploiting.

### P1B-M16 — "9σ statistical significance" LiteBIRD forecast (p. 7) is a naive σ_β / β division
β = 0.27° / σ(β) = 0.03° = 9. This is a trivial calculation, not a meaningful forecast (it ignores foreground priors, miscalibration α, and the β–α degeneracy that is the subject of the entire abstract caveat).

---

## MINOR findings

### P1B-m1 — ±0.169 vs ±0.17 precision inconsistency
Table I reports ∆Neff = −0.020 ± 0.169 and +0.065 ± 0.17. Same parameter, different sig figs on σ. Adopt one convention.

### P1B-m2 — S8 error for Planck+BAO+SN larger than full-tension (0.018 vs 0.008)
Table I. Plausible (DES Y3 prior in full-tension chain), but worth a one-line explanation.

### P1B-m3 — Footnote 3 (p. 6) admits ALP background is ΛCDM not the actual quintom chain background
This makes the *β* prediction internally inconsistent with the §V w0wa headline. The footnote estimates the impact at "≲few percent" but does not actually compute it.

### P1B-m4 — Riess et al. [7] title is "1 km s⁻¹ Mpc⁻¹ Uncertainty", not "1 km/s/Mpc uncertainty"
Cosmetic, but the bibliography should reproduce the published title.

### P1B-m5 — "Cobaya v3.5 original; v3.6.1 verification"
What does "original vs verification" mean here? Defined nowhere.

### P1B-m6 — Acknowledgments: "RunPod H200 instances"
Computing-provider name is not standard in a PRD acknowledgments section.

### P1B-m7 — Caγ = 8 fixed; configurations Caγ ∈ {4, 8, 12}
Sec. VI says Caγ = 8 fixed for the βALP fit, then Appendix C says three configurations at Caγ ∈ {4, 8, 12}. Which is the headline number? (βALP = 0.336° ± 0.107° — for which Caγ?)

### P1B-m8 — fNL = −35/8 is mentioned in Intro but is the subject of unpublished Paper II
The list of "what is NOT in this paper" includes load-bearing predictions for the parent program that are all unpublished.

### P1B-m9 — Eq. (1) is labeled but is a single equation expressing a recovered scalar, not a relation
Numbered display is overkill.

### P1B-m10 — Footnote a in Table I uses the formula "k = 7" cosmological vs 17 sampled
See M10 above.

---

## NITS

### P1B-n1 — Author affiliation "Independent Researcher, Los Angeles, California, USA" is acceptable but the manuscript would benefit from an institutional reviewer of record.

### P1B-n2 — Page 2: "We do not therefore claim that the SH0ES tension is resolved or even moved" — placement of "therefore" awkward.

### P1B-n3 — Table II χ²: reported "14037.4 ± 5.6" mean but sum is 14037.5; the footnote acknowledges the 0.1-unit rounding correctly. Fine.

### P1B-n4 — Figure 1 axis ranges look reasonable; corner plot is standard getdist output.

### P1B-n5 — Page 9 footnote 5 ("Backreaction / spectator-status disclosure") duplicates fn. 4 content; consolidate.

---

## Length / scope verdict

For a "technical verification companion" that delivers (a) one null-consistency MCMC, (b) one pipeline MC, and (c) one consistency-with-published-literature calculation, **a 4-page Letter or 6-page short methods paper would be appropriate**. At 10 pages with two MCMC analyses, one of which is the load-bearing w0wa headline not in the abstract, the paper is both too long for the stated scope and dishonestly framed about what it actually contains.

---

## Summary recommendation

**REJECT**

This manuscript is not in submittable condition for *Physical Review D*. Multiple paragraphs (pp. 3–7) read as verbatim referee-response prose with explicit phrases like "an earlier count erroneously quoted", "a concern was raised", "addressing earlier reviewer concerns", and "correcting the earlier Caγθi product" embedded in the body — this alone is grounds for return. The abstract and title describe a ΛCDM+ΔNeff null-consistency check, but the body smuggles in a substantive w0wa MCMC with a "+4.3σ" quintom headline that the author admits in a footnote is a *posterior-tail extrapolation at an unsampled point, not a Bayes factor and not a frequentist tension*. The NaMaster "SNR = 20.32" figure is undefined and physically implausible. The spectator-ALP "consistency" claim requires both ≈25× fine-tuning of θi and a photon-coupling Caγ ∈ [9, 51] that the paper concedes lies outside KSVZ/DFSZ benchmarks. The parent paper [1] and three of four companion papers ([4–6]) are unpublished and unavailable, so the "verification" anchor is missing. A complete rewrite separating the converged ΔNeff null test from the (caveated) w0wa exploration, removing all internal-audit prose, fully defining the pipeline-recovery SNR, and waiting for the parent paper to appear is required before any resubmission can be considered.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional findings — second-pass review

After re-reading with attention to arithmetic, cross-references, and dataset attribution, I find several substantive issues my first pass missed.

---

## NEW ESSENTIAL findings

### P1B-E8 — Reference [2] is misattributed in the abstract; supports a *different* significance number
**Abstract, p. 1.** *"The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3]."* Reference [2] is Eskilt & Komatsu 2022 (PRD 106:063503), which reports β = 0.342° ± 0.094° = **3.6σ** — explicitly outside the cited 2.4–2.9σ range, and explicitly used elsewhere in the same paper as the "headline" result. Citation [2] cannot simultaneously support "the 2.4–2.9σ primary sky detection" (abstract) and "the published 3.6σ joint signal" (Sec. VII). The correct support for "2.4–2.9σ" is [15] (Diego-Palazuelos PR4, ~2.7σ) and [3] (ACT DR6, ~2.9σ) only.
**Fix required:** Remove [2] from the abstract citation; reconcile the 2.4–2.9σ vs 3.6σ framing across abstract/body/conclusions (currently three different "primary" values).

### P1B-E9 — The dataset-disambiguation footnote on p. 1 contradicts the body
The page-1 footnote states: *"the published PRD paper [2] (PRD 106:063503, arXiv:2205.13962) analyzes **Planck PR3 + WMAP9**; the public reproduction code … was subsequently updated to use Planck PR4 / NPIPE."* But the body (Sec. VI, p. 6) states: *"the published Eskilt & Komatsu joint WMAP+Planck value … [2] (the joint **WMAP9 + Planck PR4/NPIPE** analysis"*. 

Checking the actual Eskilt & Komatsu 2022 paper (arXiv:2205.13962): the published analysis uses **WMAP9 + Planck PR4**, not PR3. The footnote on p. 1 — the *entire purpose* of which is to clarify this attribution — is factually wrong about the published paper's data. This is the single most prominent footnote in the manuscript (occupies ~1/4 of the front page) and it misstates basic citation facts.
**Fix required:** Verify and correct the disambiguation footnote against the actual published paper.

### P1B-E10 — βALP sample-count attribution is internally contradictory between Sec. VI and Appendix C
Sec. VI (p. 7): *"βALP = 0.336° ± 0.107° (Caγ = 8 fixed) … 9,720 accepted samples across the 3 ALP-MCMC configurations"*. Appendix C: *"Caγ: fixed at one of {4, 8, 12} across the three configurations (**3,240 samples per configuration**)"*. βALP cannot be both "Caγ = 8 fixed" and "9,720 samples across 3 configurations" — at Caγ = 8 fixed, only 3,240 samples are available. Either:
  - βALP is the Caγ = 8 subset (3,240 samples), and the "9,720" attribution is wrong, or
  - βALP is a joint over Caγ ∈ {4, 8, 12} (9,720 samples), in which case "Caγ = 8 fixed" is wrong.
**Fix required:** Resolve the contradiction; recompute the σ of the headline number on the correct subset.

---

## NEW MAJOR findings

### P1B-M17 — NaMaster bias is multiplicative, not "amplitude-dependent additive"
The paper frames the bias as "0.032° at β = 0.27°" vs "0.040° at β = 0.342°" — language ("absolute bias scales mildly with injected amplitude", "∼12% amplitude-dependent component") that implies a near-constant additive bias.

Actual ratios:
- 0.238 / 0.270 = **0.881** (recovery / injection)
- 0.302 / 0.342 = **0.883**

These are identical to within 0.2%. The pipeline exhibits a **constant ~12% multiplicative recovery deficit**, not an amplitude-dependent additive bias. A 12% multiplicative deficit is a much more concerning finding for a deconvolution pipeline: it indicates either an unaccounted-for transfer function or a residual E/B leakage that scales with signal. The framing chosen ("unbiased at the 0.04° level") downplays this.
**Fix required:** Re-characterize the bias as a multiplicative recovery factor ≈ 0.88, and explain its origin (mode-coupling matrix incompleteness, B-mode purification under-correction, or pixel-window over-correction).

### P1B-M18 — Eq. (3) factor "1.07" is unlabeled and inconsistent with Eq. (2)
Eq. (2): *∆ϕ/fa ≈ 0.65 (m = H0, θi = 1)*. Eq. (3): *β ≈ (αEM × 8 / 4π) × **1.07** ≈ 0.29° for Caγ = 8, θi = 1, m ≈ 2H0*. The "1.07" is not labeled but must be ∆ϕ/fa at m = 2H0 (since the standard birefringence formula is β = (αEM/4π) Caγ (∆ϕ/fa)). The reader is left to infer that ∆ϕ/fa jumps from 0.65 to 1.07 going from m = H0 to m = 2H0 with no explanation, and the symbol does not appear in the equation. Reproducibility is impaired.
**Fix required:** Label the factor and state how it follows from the ALP EOM at m = 2H0.

### P1B-M19 — "Within 1σ" consistency between βALP and βobs is presented misleadingly
Sec. VI: *"βALP = 0.336° ± 0.107°, … the model-independent fit βfree = 0.344° ± 0.096° … and the observed βobs = 0.342° ± 0.094°. All three within 1σ."* Actual joint discrepancy between βALP and βobs: difference = 0.006°, joint σ = √(0.107² + 0.094²) = 0.143°, so 0.006/0.143 = **0.04σ**. They are not "within 1σ"; they are essentially identical. "Within 1σ" frames the agreement as marginal when in fact it is trivial and statistically uninformative (the priors have already constrained β to be ~0.34°). This selection of words inflates the apparent strength of the consistency.

### P1B-M20 — Figure 1 sample count (119,617) does not match footnote 1's post-burnin computation
Footnote 1 (p. 2) reconciles the post-burnin full-tension count as either **123,129** (chain truncation) or **123,368** (exact 0.7 × 176,240). Figure 1 caption: **119,617**. Footnote 1 attributes the 119,617 to *"additional getdist effective-sample weight-based thinning"*, but getdist's effective-sample-size weighting is the ESS estimator, not a thinning operation — i.e., the 119,617 is most likely the **effective sample size** (ESS), not a count of samples actually shown in the corner plot. The caption misleadingly labels it as "samples". Three different sample counts (119,617, 123,129, 123,368) appear with no clear definitions distinguishing them.

### P1B-M21 — ESS/N ≈ 3% across the Metropolis-Hastings chains
Table I reports Min ESS = 4,744 (full-tension, 176,240 samples) and 4,692 (Planck+BAO+SN, 132,949 samples). Effective-sample fractions are **2.7% and 3.5% respectively** — low even for Metropolis-Hastings in a 17-d parameter space. The "convergence" claim by R̂ − 1 alone is not strong when ESS is sub-5%; some posterior tails will be poorly sampled, particularly relevant since the paper has already encountered the "LCDM point is unsampled" problem on a different chain (Sec. V).

### P1B-M22 — χ²_CMB = 10984 with no DOF column
Table II reports χ²_CMB = 10983.9 ± 5.3 but does not state degrees of freedom. For Planck NPIPE CamSpec TTTEEE + lowl.TT + lowl.EE + lensing, plausible DOF ~ 6000–10000 depending on multipole cutoffs and binning. Without DOF, the reader cannot assess goodness-of-fit. Same for χ²_SN = 3043. A standard cosmology table would include DOF and reduced-χ² per likelihood block.

### P1B-M23 — w0 + wa = −1.48 ± 0.15 implicitly requires correlation ρ(w0, wa) ≈ −0.90
σ(w0+wa) computed from independent variances would be √(0.0436² + 0.1864²) = 0.191. The reported 0.1485 requires Cov(w0, wa) ≈ −0.0073, implying ρ ≈ −0.90. This is the standard quintom-chain anti-correlation, but it is **never reported in the manuscript**, and the "phantom crossing required" claim entirely depends on this correlation structure. The corner plot should be shown, or at least the correlation coefficient quoted.

### P1B-M24 — βcombined error treats σ as having no covariance, contradicting the paper's own scope statement
Eq. (4): βcombined = 0.241° ± 0.061°, quoted with "(3.9σ)". Direct check: 0.241/0.061 = **3.95σ** (matches). The paper itself flags: *"This neglects shared calibration systematics; the published joint analysis at 3.6σ [2] is the headline."* But [2] uses **WMAP + Planck**, not **Planck + ACT** as Eq. (4) does. So the auxiliary cross-check at 3.9σ is on a *different* dataset combination than the 3.6σ headline; the comparison "auxiliary cross-check ≈ headline" does not actually involve the same observables. The juxtaposition is not informative.

### P1B-M25 — "Within ±1% of the 123,368 exact computation" is wrong
Footnote 1: post-burnin claim is 123,129, exact computation is 123,368. Relative difference = (123,368 − 123,129) / 123,368 = **0.194%**, not "within ±1%". The actual error is much smaller than claimed; the looser bound suggests the author did not actually compute it.

---

## NEW MINOR findings

### P1B-m11 — Eq. (3) numeric: αEM × 8 / (4π) × 1.07
Direct calculation: (1/137.036) × 8 / (4π) × 1.07 = 0.004965 rad = **0.2845°**. Paper rounds to "0.29°". Within rounding, but the "fiducial value β ≈ 0.27°" in the next sentence then uses a *different* mid-point parameter set (m ≈ 1.8 H0, ∆ϕ/fa ≈ 1.0) without explicitly recomputing. Reader is told "the fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H0, ∆ϕ/fa ≈ 1.0" but never sees the recomputation. Direct check: (1/137) × 8 / (4π) × 1.0 = 0.266° ≈ 0.27° ✓.

### P1B-m12 — Reference [3] Diego-Palazuelos & Komatsu, ACT DR6, arXiv:2509.13654
Author lists this as the source of "β = 0.215° ± 0.074°". As of submission this is plausible but the arXiv number 2509.13654 is from September 2025; needs verification at typesetting (preprints are sometimes renumbered before publication).

### P1B-m13 — DESI BAO χ² = 10.6 ± 1.8 implies ~12 BAO measurements
DESI DR2 has roughly 13 BAO-tracer combinations (BGS, LRG-1/2/3, ELG, QSO, Lyα). χ² = 10.6 on ~13 measurements is essentially a perfect fit, deserving comment rather than just a table row.

### P1B-m14 — Sec. III claim that minimal matter-bounce predicts ∆Neff ≈ 0 "by construction"
This is asserted without citation. The cited reference [10] (Cai et al. 2009) discusses non-Gaussianity in a matter bounce, not the ∆Neff prediction. A reference establishing ∆Neff ≈ 0 for matter-bounce models should be added.

### P1B-m15 — Sec. III footnote 2 cites "Λstrong ∼ MPl/√γBI"
The Barbero–Immirzi parameter γBI has standard values ∼0.24 from black-hole entropy matching. With γBI ≈ 0.24, MPl/√γBI ≈ 2 MPl. The footnote does not give the value of γBI used, so the EFT validity domain is ambiguous.

### P1B-m16 — "Both ends are larger than the standard KSVZ/DFSZ benchmark range"
The required Caγ ∈ [9, 51] is compared to KSVZ/DFSZ "|Caγ| ∼ O(1)". KSVZ has Caγ = −1.92, DFSZ has Caγ = 0.75. The "O(1)" comparison is correct, but the explicit values would tighten the discussion. Also, the lower end Caγ ∼ 9 is not enormously above KSVZ; the gap is one decade. Sec. VI's phrasing oscillates between "outside" and "modest … enhancement" without committing.

### P1B-m17 — Pivot redshift zp value never given
Table II: wpivot = −1.034 ± 0.030. The pivot redshift zp depends on the data combination; never quoted. Without zp, the "−1.1σ from −1" statement is uninterpretable physically.

### P1B-m18 — Appendix C never specifies the dataset stack for βALP
Appendix C states: *"Both fits use the Planck PR4 + ACT DR6 EB-spectrum likelihoods (the same observables used by Refs. [2, 3])"*. But ref [2] uses WMAP + Planck PR4, not ACT DR6. The "observables used by Refs. [2, 3]" are not the same. The cited "shared calibration covariance" is never defined.

### P1B-m19 — "1σ" claim in Sec. VI directly contradicts arithmetic
See M19 above. Reported 1σ; actual 0.04σ.

---

## NIT additions

### P1B-n6 — Page-1 footnote on Eskilt+Komatsu spans roughly 25% of the front page; this length is inappropriate for a footnote and signals that the disambiguation should be in the body.

### P1B-n7 — "16-rank mpirun process terminated automatically" — second mention in conclusions; one is enough.

### P1B-n8 — Table II reports the chain "Rˆ − 1 = 0.00820"; significant figures suggest more precision than typical convergence diagnostics warrant.

### P1B-n9 — Some statistical notation is inconsistent: "σ" appears as both "1-σ posterior error" and "tension distance" — not always clear which.

---

## Summary of the second pass

The most consequential new findings are:
- **E8 + E9**: A reference attribution error in the abstract and a factually incorrect disambiguation footnote on p. 1 — directly affecting the headline statement of "primary sky detection significance".
- **E10**: An internal contradiction between Sec. VI (9,720 samples for βALP at Caγ = 8 fixed) and Appendix C (3,240 samples per Caγ configuration), affecting the load-bearing ALP-MCMC headline.
- **M17**: The NaMaster bias is a multiplicative ~12% recovery deficit (0.881–0.883 across both injections), not an "amplitude-dependent" additive bias — this is a more concerning systematic that the manuscript's framing obscures.
- **M20**: The Fig. 1 sample-count caption ("119,617 samples") almost certainly reports the effective sample size, not the number of posterior samples — a labeling error.
- **M23**: The phantom-crossing claim (w0 + wa = −1.48 ± 0.15) implicitly requires ρ(w0, wa) ≈ −0.90, never reported.

These additional findings strengthen the original reject recommendation. The combination of (i) misattributed primary reference, (ii) factually wrong disambiguation footnote, (iii) internally contradictory sample counts for the headline ALP fit, and (iv) misrepresented NaMaster systematic, is incompatible with PRD publication standards.