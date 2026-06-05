# P1B R10v3 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K
**Wall time**: 190.5s

---

# Referee Report: P1B (Technical Verification Companion to ECH Spin-Torsion Program)

**Reviewer:** Brutal-honesty PRD referee
**Submission:** Technical verification companion paper, 10 pages
**Recommendation preview:** See end of report

---

## Overall Assessment

This paper is a "companion" technical verification document for a no-go program (Paper I(a)) that itself is "in preparation." The paper is unusually candid about its own limitations — to the point where the abstract and body repeatedly admit that the three reported analyses do not actually test the framework they purport to verify. This is intellectually honest, but it raises a fundamental question: **what is the scientific contribution that justifies publication in PRD?**

Stripped of caveats, the paper contains:
1. A null ΛCDM+ΔN_eff MCMC run (no torsion physics) that reproduces standard Planck values.
2. A NaMaster pipeline self-test that recovers an injected signal (not a sky measurement).
3. An ALP birefringence consistency check that admits it is "not a distinctive ECH prediction" and requires ~25× misalignment fine-tuning.

None of these constitute novel physics results. The MCMC reproduces published cosmology. The NaMaster test is a sanity check on a public library. The ALP check is admitted to be model-independent of the framework being verified. The "companion paper" framing tries to deflect this by pointing to Paper I(a), but **Paper I(a) is not available for review** (cited as "in preparation"), so the only thing on the table is this technical document, which by its own admission tests nothing.

Beyond the framing problem, the paper contains substantial internal inconsistencies, arithmetic problems, mid-paper "addressed reviewer concerns" prose, internal audit fossils ("earlier count erroneously quoted," "prior caveat promised"), and a Table II (DESI w0wa) result that appears nowhere in the abstract but contains the only potentially publishable finding — yet that result is undermined by the authors' own admission that the LCDM point lies outside the chain's sampled region and no robust Bayes factor was computed.

---

## ESSENTIAL Findings

### P1B-E1: Paper depends on an unpublished companion paper
**Section:** Throughout; Refs. [1, 4, 5, 6]
**Problem:** The paper is repeatedly framed as a "companion to Paper I(a)" [1], which is "in preparation" (HUBIFY-2026-001A). The same is true of Papers II, III, IV. The Introduction (p. 2) states "The 13 logically-independent structural barriers, the perturbation-transparency theorem, the 14-barrier table, and the surviving matter-bounce-specific test predictions ... are in Paper I(a)." A companion paper cannot be evaluated when the primary paper is unavailable. The abstract even claims "14 independent structural constraints" exist in Paper I(a), but the reader cannot verify this.
**Required fix:** Either (a) submit Paper I(a) jointly so the companion has a basis for evaluation, or (b) restructure this manuscript to stand alone with a clearly stated independent contribution.

### P1B-E2: Abstract claim of "14 independent structural constraints" is unverifiable here
**Section:** Abstract / Intro p. 2
**Problem:** Abstract refers to "14 independent structural constraints" in Paper I(a); Introduction also refers to "13 logically-independent structural barriers" and a "14-barrier table" (p. 2). The mismatch (13 vs 14) is itself a flag, and neither number is justified in this paper.
**Required fix:** Remove the 14/13 references or justify them in this manuscript.

### P1B-E3: Abstract NaMaster SNR juxtaposed with sky-detection σ without explicit non-comparability warning at every juxtaposition
**Section:** Abstract p. 1; Sec. IV p. 5
**Problem:** The abstract presents the NaMaster pipeline-recovery and the Planck/ACT 2.4–2.9σ sky detection in adjacent sentences. While the paper *does* eventually disclaim non-comparability, the abstract gives the pipeline SNR-recovery figure (β̂ = 0.238°, bias 0.032°) and the sky-detection σ in a way that, despite hedging language, juxtaposes them. Worse, on p. 5 the text introduces "pipeline-recovery SNR = 20.32" alongside the published 2.4–2.9σ — these are dimensionally similar quantities that are not directly comparable, and the per-juxtaposition disclaimer is uneven.
**Required fix:** At every numerical juxtaposition (including Eq. 1 caption and the abstract), explicitly tag "pipeline-recovery only, NOT comparable to sky-detection σ." Better: remove the pipeline SNR figure from the abstract entirely.

### P1B-E4: Internal audit / reviewer-response fossils embedded in the body
**Section:** Sec. III p. 3–4; Sec. IV p. 5
**Problem:** Multiple instances of mid-paper review-response prose that should not appear in a published article:
- p. 3: "An earlier count erroneously quoted '98.6% quintom-B' weight"
- p. 3: "note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically"
- p. 4: "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood"
- p. 5: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°"
- p. 5: "NOT a YAML alias failure" — responding to a reviewer who is not the reader

These are version-history artifacts.
**Required fix:** Remove all reviewer-response language. Present only the final state of each analysis.

### P1B-E5: Abstract claims the "third Planck-only combination ongoing" — incomplete work submitted
**Section:** Abstract p. 1; Sec. III p. 2
**Problem:** Abstract: "plus a third Planck-only combination ongoing." A paper should not be submitted with stated incomplete analyses. The "ongoing" run is at R̂−1 ~ 0.05, which is non-converged.
**Required fix:** Either complete the third run or remove it from the manuscript entirely.

### P1B-E6: Table II (DESI w0wa) is not in the abstract, yet contains the only nontrivially novel result
**Section:** Sec. III/Table II p. 4; Abstract
**Problem:** The abstract focuses entirely on the null ΛCDM+ΔN_eff run, but Table II reports w0 = −0.812 ± 0.044 and wa = −0.667 ± 0.186 — a +4.3σ / −3.6σ departure from ΛCDM. This is by far the most consequential numerical claim in the paper, yet:
(a) it is not mentioned in the abstract;
(b) the authors immediately disclaim that LCDM "is unsampled by this chain" so the σ is "a posterior-tail extrapolation distance only, not a Bayes-factor or ln B exclusion and not a frequentist tension" (Table II footnote a, p. 4);
(c) no Bayes factor is computed (deferred);
(d) the headline +4.3σ is therefore an unsupported tail-extrapolation that the authors themselves explicitly disavow as a tension.
This is the worst kind of double-speak: report a large σ in a table, then footnote that it isn't really a σ.
**Required fix:** Either (a) compute a robust Bayes factor via nested sampling and report it, or (b) remove all σ-style numerical comparisons of (w0, wa) to LCDM. The current framing is misleading.

### P1B-E7: Table II arithmetic inconsistency
**Section:** Table II p. 4
**Problem:** χ²_total = 14037.4 ± 5.6, but the sum of components is 10.6 + 10983.9 + 3043.0 = **14037.5**, not 14037.4. The footnote claims this is "a 0.1-unit arithmetic-rounding artifact." This is implausible: if each component is reported to one decimal place, the rounding error of the sum is at most ±0.15, but the discrepancy is structural — GetDist's weighted-mean over a non-Gaussian posterior generally does not equal the sum-of-means even within rounding. The footnote's claim that the two are "formally identical to within sampling precision" is incorrect; they are formally different objects (E[X+Y+Z] vs E[X]+E[Y]+E[Z] are equal for the mean, so this should match exactly modulo rounding — meaning either the rounding is wrong or one of the components is misreported).
**Required fix:** Recompute and resolve. Either the means are wrong or the explanation is wrong.

### P1B-E8: ALP coupling derivation contains an inconsistency between Eq. (3) and the text
**Section:** Sec. VI p. 7
**Problem:** Equation (3) states β ≈ (α_EM × 8)/(4π) × 1.07 ≈ 0.29° for C_aγ = 8, θ_i = 1, m ≈ 2H_0. But the text says "The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H_0, ∆ϕ/f_a ≈ 1.0." Computing: α_EM × 8/(4π) × 1.0 with α_EM = 1/137 = 7.30×10⁻³, gives in radians 7.30×10⁻³ × 8/(4π) = 4.65×10⁻³ rad = 0.266° — that matches 0.27°. But Eq. (3) uses 1.07 (not 1.00) and gets 0.29°. So either the factor 1.07 is ∆ϕ/f_a (≠ the 0.65 reported in Eq. 2 for θ_i = 1, m = H_0), or the parameters used differ from those stated. The narrative is internally inconsistent.

Also: Eq. (2) gives ∆ϕ/f_a ≈ 0.65 for m = H_0, θ_i = 1, but the text on p. 7 says "midpoint m ≈ 1.8 H_0, ∆ϕ/f_a ≈ 1.0" — but Eq. (2) does not give the m = 1.8H_0 case anywhere. The reader cannot reconstruct where the 1.07 in Eq. (3) comes from.

**Required fix:** Make the ALP-EOM computation reproducible. State exactly which (m/H_0, θ_i) gives each ∆ϕ/f_a value used.

### P1B-E9: ALP MCMC "model-independent fit" disclosure is buried in an unparseable paragraph
**Section:** Sec. VI p. 7
**Problem:** The text says β_free = 0.344° ± 0.096° is from "our internal model-independent MCMC fit to the Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter, 9,720 accepted samples across the 3 ALP-MCMC configurations described in Sec. VI (configurations C_aγ = 4, 8, 12 on Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter; full priors and dataset details in Appendix C); β_free denotes the unconstrained-amplitude fit distinct from β_ALP which has C_aγ = 8 fixed) and the observed β_obs = 0.342° ± 0.094°."

But Appendix C says β_free is a SEPARATE fit with β ∈ [−2°, 2°] uniform prior and no ALP structure, while the ALP fit fixes C_aγ. The parenthetical above conflates the two. The result β_free = 0.344° ± 0.096° being suspiciously close to the published Eskilt+Komatsu 0.342° ± 0.094° (and to β_ALP = 0.336°± 0.107°) makes the result internally circular: the authors fit a published likelihood and recover the published value. This is not independent verification.
**Required fix:** Clarify that β_free is a re-derivation of the published value using the same likelihood code, and disclose that this is by construction the published value within sampling error.

### P1B-E10: Abstract caveat about "spectator status" is severe and undercuts the framing
**Section:** Abstract p. 1
**Problem:** The abstract explicitly states: "the spectator label is only consistent under the explicit restriction θ_i ≪ 1 (which constitutes fine-tuning of the misalignment initial condition); at θ_i ∼ 1 the ALP must instead be treated as the dark-energy field itself, which is outside the scope of this companion-paper consistency check." This is a fatal disclaimer — the natural-parameter range used in the consistency check is itself outside the model's validity. The ~25× tuning is then admitted in Sec. VI fn. 4, but the abstract's "fa ∼ M_Pl, m ∼ H_0 is consistent with the published joint WMAP+Planck value" is then misleading because the consistency only holds in a fine-tuned corner.
**Required fix:** The abstract must state the ~25× fine-tuning explicitly in the same sentence as the consistency claim.

### P1B-E11: Footnote on dataset attribution (Eskilt+Komatsu PR3 vs PR4) is dataset confusion
**Section:** Abstract footnote `a` p. 1
**Problem:** Footnote `a` admits that the headline 3.6σ result is from Planck PR3 + WMAP9 (PRD 106:063503), but the ALP-MCMC re-runs in this paper use PR4/NPIPE (from the repository code). The headline σ and the re-derivation are therefore NOT on the same data. This is fundamental: the central comparison ("our βfree = 0.344°± 0.096° matches β_obs = 0.342°± 0.094°") is comparing posteriors on different datasets while claiming agreement. The agreement may be partly coincidental and partly because the underlying β value is similar across datasets — but quoting them as agreeing within "1σ" is misleading.
**Required fix:** State explicitly that β_obs (published, PR3+WMAP9) and β_free (re-derived, PR4/NPIPE) are on different data, and quote the appropriate published PR4 value for direct comparison.

### P1B-E12: Sec. VI claim that "the model accommodates the observed signal" is undermined by C_aγ ∈ [9, 51] requirement
**Section:** Sec. VI p. 7
**Problem:** The paper admits C_aγ in the range [9, 51] is required, while standard KSVZ/DFSZ benchmarks give |C_aγ| ~ O(1). The text frames this as "accommodated across the considered parameter space rather than fine-tuned only at one benchmark, but the upper-coupling end is not generic." This is a euphemism for "the entire required range is outside standard ALP benchmarks." Combined with the ~25× misalignment tuning, the model has two independent tunings — coupling enhancement of ~10–50× and θ_i suppression of ~25× — neither admitted in the abstract.
**Required fix:** Acknowledge both tunings honestly in the abstract and conclusions.

---

## MAJOR Findings

### P1B-M1: Sample-count footnote is opaque and internally noisy
**Section:** Sec. III footnote 1 p. 2–3
**Problem:** Footnote 1 explains how 309,189 raw samples become 216,432 post-burnin and 119,617 in Fig. 1, with subsequent "additional getdist effective-sample weight-based thinning of this subset only" and an admitted ±1% offset (123,129 vs 123,368). This is unreviewable bookkeeping. The fact that this footnote exists at all suggests poor data hygiene.
**Required fix:** Report one consistent sample-count number throughout. Eliminate the bookkeeping footnote.

### P1B-M2: Figure 1 caption refers to footnote 1 inside the figure caption
**Section:** Fig. 1 p. 5
**Problem:** Fig. 1 caption: "119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1." Captions referencing footnotes for basic sample-counting is bad style and suggests the numbers do not agree without explanation.
**Required fix:** State the relevant sample count in the caption directly, without footnote.

### P1B-M3: Figure 1 is a generic corner plot adding no new information
**Section:** Fig. 1 p. 5
**Problem:** Fig. 1 is a standard ΛCDM+ΔN_eff corner plot showing that ΔN_eff is consistent with zero. This is well-known and not a contribution. The figure is purely confirmatory and could be moved to an appendix.
**Required fix:** Either provide novel diagnostic information (e.g., shift relative to a published reference) or move to an appendix.

### P1B-M4: Table I "Worst R̂ − 1" footnote conflates parameter-counting conventions
**Section:** Table I footnote `a` p. 3
**Problem:** The footnote states "all 17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: A_planck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, M_b for the SNIa absolute magnitude)" — this is 10 listed nuisance parameters, but the list contains 9 Planck items + 1 M_b = 10. That checks out, but "k = 7 elsewhere" vs "17 here" is reader-hostile. Also: M_b is grouped with Planck likelihood nuisance, which it is not (it belongs to the SH0ES + Pantheon+ likelihoods).
**Required fix:** Use one consistent parameter accounting throughout, and correctly attribute M_b to SN likelihoods, not Planck.

### P1B-M5: Sec. III text contradicts itself on dataset combination naming
**Section:** Sec. III p. 2; Sec. V p. 6
**Problem:** Sec. III refers to "two converged dataset combinations" and "full-tension" + "Planck+BAO+SN," but Sec. V A enumerates "four dataset combinations." Are there 2, 3, or 4? The reader is left counting.
**Required fix:** State one consistent count of dataset combinations.

### P1B-M6: Caveats paragraph in Sec. III contains a duplicate/redundant phrasing on Bayes factors
**Section:** Sec. III p. 3
**Problem:** "The robust Bayesian evidence / Bayes factor ln B against LCDM is NOT reported here; standard posterior MCMC samples do not give a robust ln B" — this is the same point made twice in adjacent sentences. The paragraph then repeats the Savage-Dickey impossibility argument three times in slightly different phrasings within ten lines, and references back to itself parenthetically ("note: prior caveat promised...").
**Required fix:** Compress into a single 2-sentence caveat.

### P1B-M7: Eq. (4) auxiliary inverse-variance combination σ-computation
**Section:** Sec. VI p. 7
**Problem:** Combining β_NPIPE = 0.30° ± 0.11° and β_ACT = 0.215° ± 0.074° via inverse-variance:
- weights: w_1 = 1/0.11² = 82.6, w_2 = 1/0.074² = 182.6
- combined mean: (82.6 × 0.30 + 182.6 × 0.215)/(82.6 + 182.6) = (24.78 + 39.26)/265.2 = 64.04/265.2 = 0.2414°  ✓ matches 0.241°
- combined σ: 1/√265.2 = 0.0614°  ✓ matches 0.061°
- σ from zero: 0.241/0.061 = 3.95σ ✓ matches "3.9σ"
Arithmetic checks out. But the text correctly notes this neglects shared calibration systematics; the paper then proceeds to use this auxiliary number rhetorically as 3.9σ even while disclaiming it. This is honest but the rhetorical pattern (compute → disclaim → still quote) is repeated.
**Required fix:** Either remove Eq. (4) or use it consistently as auxiliary only.

### P1B-M8: Backreaction fine-tuning argument has a numerical hand-wave
**Section:** Sec. VI fn. 4 p. 7
**Problem:** Footnote 4: "at θ_i = 0.1 vs the scan-midpoint θ_i = 0.5 the backreaction is Ω_a(0.1)/Ω_a(0.5) ~ 1/25." This is correct (0.1/0.5)² = 1/25, but the text frames this as a "~25× fine-tuning of the misalignment initial condition." A factor 5 in θ_i is fine-tuning of about a factor 5, not 25 — the 25 is in Ω_a, the consequence, not in the parameter itself. The "25× tuning" language repeated in abstract, Sec. III, Sec. VI, and conclusions conflates the parameter tuning with the energy-density consequence.
**Required fix:** Clarify whether the tuning is "5× in θ_i" or "25× in Ω_a"; do not interchange these throughout the paper.

### P1B-M9: The MB–H0 "joint posterior offset check" calculation contains a numerical error
**Section:** Sec. III p. 4
**Problem:** Text claims: "This offset is ~3.2σ relative to the chain's σ_MB = 0.049 marginal width and corresponds exactly to the canonical 3.6σ Hubble tension." Computing 0.155 mag / 0.049 mag = 3.16σ ≈ 3.2σ. But how does this "correspond exactly to the canonical 3.6σ"? 3.2 ≠ 3.6. The text gives no explanation of how 3.2σ "corresponds exactly" to 3.6σ — these are different numbers.
**Required fix:** Either compute the correct conversion or stop claiming "exact correspondence" to a different σ value.

### P1B-M10: SH0ES likelihood + MB nuisance attribution
**Section:** Sec. III p. 4
**Problem:** Text reports M_B = −19.263 ± 0.049, agreeing with Riess M_B = −19.253 ± 0.027 at "0.2σ." Computing: (−19.263 − (−19.253))/√(0.049² + 0.027²) = −0.010 / 0.0559 = 0.18σ ≈ 0.2σ. Arithmetic checks, but the text then says "MB is correctly pulled toward the Riess value." If the posterior MB is at 0.2σ from the prior, it has been almost entirely fixed by the prior — meaning the SH0ES likelihood is dominating MB, which is the prior-data agreement, not a "pull."
**Required fix:** Frame correctly: MB is determined by the prior, not pulled.

### P1B-M11: Conclusions repeat the body verbatim
**Section:** Sec. VII p. 7–8
**Problem:** Conclusions section largely re-states bulletpoints already given in Introduction (Scope of this paper, p. 2). No new synthesis.
**Required fix:** Either remove the Conclusions or provide actual synthesis (e.g., comparative discussion of what these three checks collectively establish for the program).

### P1B-M12: Eq. (3) numerical prefactor (α_EM × 8)/(4π)
**Section:** Sec. VI p. 7
**Problem:** The standard ALP-photon birefringence is β = (C_aγ α_EM / 4π) × (∆ϕ/f_a). For C_aγ = 8, α_EM ≈ 1/137:
- α_EM × 8/(4π) = (7.30×10⁻³ × 8)/(4π) = 0.0584/12.566 = 4.65×10⁻³ rad = 0.266°
- multiplying by 1.07: 0.285° ≈ 0.29°. ✓ checks for the displayed equation.
But: the text says this corresponds to "C_aγ = 8, θ_i = 1, m ≈ 2H_0." Yet Eq. (2) gives ∆ϕ/f_a ≈ 0.65 for (m = H_0, θ_i = 1), NOT 1.07. The 1.07 in Eq. (3) is not derived anywhere in the paper.
**Required fix:** Show the calculation that gives ∆ϕ/f_a = 1.07 for the stated (m, θ_i).

### P1B-M13: Independent cross-validation paragraph is single-sentence over-claim
**Section:** Sec. III p. 5
**Problem:** "Our MCMC agrees at 0.5σ in H_0 and 0.4σ in σ_8" with Liu et al. (arXiv:2507.04265). The Liu et al. paper uses different methodology (EC torsion model, not stock CAMB), so "agreement" at 0.5σ in H_0 between a stock-CAMB null and a torsion-modified analysis is not a cross-validation of anything — both are consistent with Planck ΛCDM because both effectively reduce to it.
**Required fix:** Either remove this paragraph or honestly explain what is being cross-validated.

### P1B-M14: ALP MCMC sample count: 9,720 across 3 configurations = 3,240 per config
**Section:** Sec. VI and Appendix C
**Problem:** "3,240 samples per configuration" for an MCMC posterior on (m/H_0, θ_i) with a stated convergence R̂ − 1 < 0.01 is implausibly small for Metropolis-Hastings. Typical Cobaya runs need 10⁴–10⁵ samples per chain for that convergence. No information about number of chains per config or effective sample size is given.
**Required fix:** Report N_chains, ESS, and burn-in fraction per ALP-MCMC configuration. 3,240 samples total for a meaningful posterior is suspicious.

### P1B-M15: Appendix B / Table III claim "MCMC Verified" for posterior values
**Section:** Table III p. 10
**Problem:** "Verified" implies independent confirmation. These are simply the outputs of the authors' own MCMC. The label "Verified" is overclaim — these are "reported" or "computed."
**Required fix:** Replace "Verified" with "Reported" or "Computed."

### P1B-M16: Two appendices contradict each other on the spectator-status caveat
**Section:** Sec. VI fn. 4 vs Appendix C fn. 5
**Problem:** Both footnotes repeat the spectator-status / θ_i ≪ 1 disclaimer; Appendix C fn. 5 explicitly references fn. 4 in Sec. VI. The paper repeats the same caveat four times (abstract, Sec. VI body, fn. 4, fn. 5, conclusions). This is "burying by repetition" — each instance softens slightly differently.
**Required fix:** State once, prominently, in the abstract. Remove the redundant repetitions.

---

## MINOR Findings

### P1B-Mn1: Date stamp "2026-06-03 PDT" alongside refs to "April 2026" and other future-dated work
**Section:** Header p. 1; Sec. IV p. 5
**Problem:** Header says 2026-06-03; Sec. IV says "April 2026" for production run. Reference [3] is dated 2025 (Diego-Palazuelos & Komatsu ACT DR6, arXiv:2509.13654). Reference [12] is dated 2025. These are forward-dated submissions, which suggests this is an in-progress preprint, not a polished PRD submission.
**Required fix:** Verify all dates and clarify submission status.

### P1B-Mn2: Inconsistent significant figures on ΔN_eff
**Section:** Abstract p. 1; Table I p. 3
**Problem:** Abstract gives ΔN_eff = −0.020 ± 0.169 (3 sig figs on σ) and +0.065 ± 0.17 (2 sig figs). Table I uses ±0.169 and ±0.17. The two are inconsistent.
**Required fix:** Use consistent significant figures.

### P1B-Mn3: "(0.32)" mask fsky notation
**Section:** Abstract; Sec. IV
**Problem:** Both spell out "fsky = 0.32" — fine, but Sec. IV does not state the mask source (Planck polarization mask? Custom?). Reproducibility is harmed.
**Required fix:** Identify the mask source explicitly.

### P1B-Mn4: PACS numbers are obsolete
**Section:** Header p. 1
**Problem:** PRD discontinued PACS as of 2017; current journals use other classification (or none).
**Required fix:** Remove PACS or replace with appropriate classification.

### P1B-Mn5: "≈" and "∼" used interchangeably
**Section:** Sec. VI throughout
**Problem:** β ≈ 0.27° and β ∼ 0.27° appear in different places for the same number.
**Required fix:** Use consistent notation.

### P1B-Mn6: Footnote 3 has dangling "few"
**Section:** Sec. VI fn. 3 p. 6
**Problem:** "shifts H(z) at z ≲ 1 by ∼few percent" — "few" is colloquial.
**Required fix:** Replace with a specific number or "a few."

### P1B-Mn7: "Mb" vs "M_B" inconsistency
**Section:** Sec. III p. 4 and elsewhere
**Problem:** Sometimes M_b (subscript b), sometimes M_B (subscript B). The standard SH0ES notation is M_B.
**Required fix:** Use M_B throughout.

### P1B-Mn8: SH0ES citation uses "H0.riess2020Mb" — but Riess et al. 2022 is cited as [7]
**Section:** Sec. III p. 4
**Problem:** The Cobaya likelihood is named "H0.riess2020Mb" but the reference [7] is Riess+ 2022. Standard versioning, but worth noting.
**Required fix:** Clarify the likelihood version.

### P1B-Mn9: Repeated word: "fn. 4" cross-referenced as both "fn. 4" and "footnote 4"
**Section:** Sec. VI p. 7; Sec. VII p. 8
**Problem:** Inconsistent reference style.
**Required fix:** Unify cross-reference style.

### P1B-Mn10: "n_s in the full-tension combination at R̂ − 1 = 9.74 × 10⁻⁴" but table says 0.001
**Section:** Table I p. 3
**Problem:** Footnote a says 9.74×10⁻⁴, table body says 0.001. Both are consistent to one sig fig but differ — not a problem, but a stylistic inconsistency.
**Required fix:** Be consistent.

### P1B-Mn11: Reference [3] cited as "arXiv preprint" but appears to be a 2025 paper
**Section:** Refs p. 9–10
**Problem:** Reference [3] is labeled "arXiv preprint (2025)" but Diego-Palazuelos & Komatsu (ACT DR6) cosmic birefringence is by now likely published. Check publication status.
**Required fix:** Update to journal reference if available.

### P1B-Mn12: Acknowledgments mentions "Claude (Anthropic) as AI research assistant"
**Section:** Acknowledgments p. 8
**Problem:** Use of AI assistant should be disclosed per journal policy; the statement is appropriate but should also be in the author statement / methods section for PRD.
**Required fix:** Confirm compliance with PRD AI-use policy.

### P1B-Mn13: "RunPod H200 instances" in acknowledgments
**Section:** Acknowledgments p. 8
**Problem:** Hardware vendor name is fine but unusual to specify; the "H200" of "RunPod H200" reflects the GPU model. No issue unless GPU is irrelevant (the analyses are CPU-bound MCMC).
**Required fix:** Optional: state CPU-hours used.

### P1B-Mn14: "Hubify-Projects" repository URL
**Section:** Sec. V; Sec. VII; Appendix A
**Problem:** The repository name "Hubify-Projects/bigbounce" should be verified as a stable, archived location (Zenodo DOI?) per PRD reproducibility standards.
**Required fix:** Provide a Zenodo DOI for the snapshot used.

### P1B-Mn15: Figure 1 axis labels are not described in caption
**Section:** Fig. 1 p. 5
**Problem:** Caption does not specify what parameters are plotted (Ω_m, σ_8, S_8, n_s, τ, ΔN_eff, H_0). A reader needs to inspect the figure.
**Required fix:** Add the parameter list to the caption.

---

## NITs

### P1B-N1: Title is overly long
**Section:** Title p. 1
**Problem:** "Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model" — 32 words.
**Required fix:** Shorten.

### P1B-N2: Abstract is 600+ words, well above PRD norms
**Section:** Abstract p. 1
**Problem:** PRD abstracts are typically 150–250 words. This abstract is so long it contains its own footnote.
**Required fix:** Cut to ≤250 words.

### P1B-N3: Footnote `a` is in the abstract
**Section:** Abstract p. 1
**Problem:** Footnotes in abstracts are highly unusual in PRD.
**Required fix:** Move to main text.

### P1B-N4: Repeated phrase "stock CAMB" appears 15+ times
**Section:** Throughout
**Problem:** The defensive repetition of "stock CAMB, no torsion modifications" suggests over-anticipation of reviewer pushback.
**Required fix:** State once in the methods, then refer back.

### P1B-N5: "Brutal honesty" embedded throughout body in parenthetical asides
**Section:** Throughout
**Problem:** The paper has an unusual self-flagellating tone (e.g., "we do not therefore claim that the SH0ES tension is resolved or even moved"). While honest, this style is unusual in PRD and verges on apologetic.
**Required fix:** Tone down where appropriate; the paper should describe its results, not apologize for them.

### P1B-N6: Reference [11] (Liu et al.) is cited as "European Physical Journal C (2025), arXiv:2507.04265" but no journal volume/pages
**Section:** Refs p. 10
**Problem:** Incomplete reference.
**Required fix:** Complete the reference.

### P1B-N7: "Eskilt+Komatsu" repeated as "Eskilt & Komatsu" and "Eskilt et al."
**Section:** Various
**Problem:** Inconsistent citation style.
**Required fix:** Unify.

### P1B-N8: Reference [22] description is mid-citation editorial commentary
**Section:** Refs p. 10
**Problem:** Reference [22] description includes "Used in P1A Sec. VI to point readers to..." — this is internal cross-paper bookkeeping that does not belong in a published reference.
**Required fix:** Strip editorial commentary from references.

### P1B-N9: Equation (1) labeling
**Section:** Sec. IV p. 5
**Problem:** Equation (1) is a single scalar value with one number — equations should be reserved for actual algebraic content.
**Required fix:** State inline.

### P1B-N10: Page count vs content
**Section:** Overall
**Problem:** Given that the paper's three analyses are (a) a null cosmology run reproducing ΛCDM, (b) a pipeline self-test, and (c) an admitted non-distinctive ALP check, the paper does not justify 10 pages.
**Required fix:** Compress to ≤6 pages.

---

## Page-count recommendation

Given the actual scientific content (which the paper itself acknowledges is null, methods-validation, and not a distinctive prediction), this manuscript should be **≤6 pages** if it must exist standalone, or it should be merged into Paper I(a) as an appendix/companion. A 10-page paper documenting that one ran stock CAMB and got the standard Planck answer is not a PRD article.

---

## Summary recommendation

**REJECT**

This paper, by its own repeated admission, does not test the framework it purports to verify. Analysis (1) is a stock-CAMB null reproducing standard ΛCDM. Analysis (2) is a pipeline self-test that recovers an injected signal. Analysis (3) is admitted to be non-distinctive of the parent theory and requires a ~25× misalignment fine-tuning plus a 10–50× photon-coupling enhancement to even claim consistency with the observed birefringence. The most interesting numerical result (Table II's w0wa departure) is in a table never mentioned in the abstract, and its σ-values are explicitly disavowed by the authors as posterior-tail extrapolations rather than tensions. The manuscript is riddled with reviewer-response fossils ("addresses earlier reviewer concerns," "earlier count erroneously quoted," "prior caveat promised"), version-history bookkeeping (309,189 / 216,432 / 119,617 / 123,368 / 123,129 sample counts in one footnote), arithmetic that does not fully audit (Table II χ² sum), and a primary companion paper [1] that is unavailable for review. The paper should be either (a) merged into Paper I(a) and resubmitted as a single coherent manuscript, or (b) compressed to a short technical note specifically on the NaMaster pipeline-bias characterization, which is the one genuinely useful (if narrow) contribution.