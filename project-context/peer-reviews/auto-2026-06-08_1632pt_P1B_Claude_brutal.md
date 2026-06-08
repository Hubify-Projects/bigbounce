# P1B auto-2026-06-08_1632pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11202 chars)
**Wall time**: 416.9s

---

# Referee Report — P1B
**Manuscript:** Technical Verification Companion to the ECH Spin-Torsion Program
**Journal:** Physical Review D
**Recommendation:** REJECT (see Summary at end)

---

## Overall assessment

This manuscript is described by its own authors as a "technical verification companion" in which (i) the MCMC carries *no* torsion modifications, (ii) the NaMaster analysis is *not* a sky detection, and (iii) the ALP birefringence is *not* a distinctive prediction of the underlying theory. The paper therefore concedes, in its own abstract, that none of its three analyses test the theoretical framework it claims to support. What remains is a re-running of stock CAMB+Cobaya on standard likelihoods, a pipeline self-test, and a fine-tuned ALP toy. None of these rises to a PRD-grade contribution. Compounding this, the paper is a companion to a manuscript ([1], "Paper I(a)") that is listed as "(in preparation)" — PRD does not accept companion papers whose primary partner is unpublished. The body further contains explicit reviewer-response prose, "earlier draft" corrections, conflicting sample counts, internal audit language, and an abstract that omits the single most consequential numerical result (the w₀wₐ chain in Table II). I recommend rejection.

---

## ESSENTIAL findings

**P1B-E1 — Companion to an unpublished paper.** (p. 9, Ref. [1])
Reference [1] H. Golden, *Structural Closure of...*, "(in preparation) (2026)". The entire premise of this paper is that it verifies results in [1]. PRD does not accept companion-of-companion submissions to unpublished works. Refs. [4], [5], [6] are also "(in preparation)".
**Fix:** Either submit [1] simultaneously with explicit cross-reference and editor-shared review, or recast this paper as fully self-contained (in which case essentially nothing of substance remains, since the paper admits none of its analyses test the theory).

**P1B-E2 — The paper admits it tests nothing theory-specific.**
- Abstract: "this run uses stock CAMB with ∆N_eff as a free parameter and carries *no torsion modifications to the Boltzmann equations*"
- p. 2 / Sec. III: "It does *not* verify the spin-torsion theory module itself"
- p. 5 / Sec. IV: NaMaster figure is "*Not a competitive sky detection*"
- p. 6 / Sec. VI: "*Not a distinctive ECH prediction*"
- p. 8: "The same result arises in standard GR"

After these disclaimers there is no theory-specific deliverable left. A PRD methods paper must produce a result that materially advances the field; this paper's own scope statements explicitly disavow that.
**Fix:** State what novel, falsifiable, theory-specific output the paper provides. If none, withdraw.

**P1B-E3 — Reviewer-response and version-history prose in the manuscript body.** Numerous instances of internal audit / review-log language appear in the published-facing body:
- p. 3: "An earlier count erroneously quoted '98.6% quintom-B' weight"
- p. 4: "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent..."
- p. 4: "A concern was raised that the joint posterior mean (M_B = …) was inconsistent with an active sn.pantheonplus likelihood, claiming a Cobaya YAML alias failure."
- p. 6: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°"
- p. 7: "§VI for the explicit numerical derivation correcting the earlier C_aγθ_i product"
- p. 3 (caveat): "prior caveat promised a Savage-Dickey ratio on the converged 2D (w, w_a) marginal, but with zero free-w₀wₐ samples at the LCDM point the KDE estimator fails catastrophically"

This is referee-correspondence prose, not a manuscript. Each instance must be removed.

**P1B-E4 — Abstract omits the single most quantitatively striking result.** The abstract describes only the ΛCDM+∆N_eff proxy ("two converged dataset combinations… plus a third Planck-only combination ongoing"). However, Table II (p. 4) reports a separate DESI DR2 w₀wₐ chain with N = 128 385 samples and w₀ = −0.812 ± 0.044, wₐ = −0.667 ± 0.186, with a "phantom-crossing required" quintom-B result described in the body as "the canonical quintom signature". This is a fourth dataset combination not mentioned in the abstract at all, yet it carries the largest claimed departure from ΛCDM in the entire paper. Either the abstract is misleading by omission or Table II is out of scope.
**Fix:** Either remove Table II from this paper (it has nothing to do with the three advertised analyses) or rewrite the abstract to disclose it. The current configuration is inadmissible.

**P1B-E5 — Sample-count inconsistencies across abstract, body, footnote, and Fig. 1.** The full-tension chain alone is variously reported as:
- 176 240 raw samples (Table I, footnote 1)
- 119 617 post-burn-in samples (Fig. 1 caption)
- 123 368 = 176 240 × 0.7 (footnote 1 arithmetic)
- 123 129 (footnote 1 reported value)
- 216 432 (claimed both-chain post-burn-in total in footnote 1 — but this is the sum of *both* full-tension and Planck+BAO+SN, not one chain)

Footnote 1 acknowledges these are inconsistent and tries to reconcile them with hand-waving about "additional getdist effective-sample weight-based thinning of this subset only". This is unacceptable bookkeeping in a quantitative methods paper.
**Fix:** Report one sample count per chain, defined operationally, with the same number used in Fig. 1, Table I, and the body.

**P1B-E6 — "Spectator-ALP" check actually samples the dark-energy-ALP regime.** The abstract caveat states that spectator status requires θ_i ≪ 1, but Appendix C states the MCMC prior is θ_i ∈ [0.5, 2]. Footnote 5 explicitly admits: "Posterior samples at θ_i ≳ 0.5 correspond to the dark-energy-ALP regime (excluded from the spectator-consistency claim of this companion paper)". The MCMC therefore *does not sample the parameter region the paper claims to validate*. The advertised "consistency" is for a model the chain has not explored.
**Fix:** Re-run the ALP MCMC with priors restricted to the spectator-consistent sub-regime, or relabel the result as a DE-ALP fit and remove all "spectator-ALP consistency" language. As written, the headline of Sec. VI is false to its own posterior.

**P1B-E7 — Required C_aγ lies outside KSVZ/DFSZ benchmarks across the entire allowed range; this is not "comfortably bracketing" the data.** Sec. VI states C_aγ ∆ϕ/fₐ ≈ 10.3 and ∆ϕ/fₐ ∈ [0.2, 1.1], implying C_aγ ∈ [9, 51]. The paper itself writes "the entire required range therefore lies outside minimal ALP photon-coupling benchmarks". Yet the same section claims the model "comfortably brackets the observed value" and the abstract claims the field is "consistent" with the data. These two statements cannot both stand.
**Fix:** Either retract the "consistency"/"comfortably brackets" framing, or quantify the prior penalty of requiring C_aγ ≳ 10 in a UV-complete model. The current text is overclaim.

**P1B-E8 — Pipeline-recovery SNR juxtaposed with sky-detection σ without "not directly comparable" disambiguation at every juxtaposition.** Abstract: "pipeline-recovery SNR figures refer to recovery of injected MC signals and are *not* competitive sky measurements" — but later, in Sec. IV and Sec. VII, the figures "20.32" and "25.71" reappear without the same disclaimer in immediate proximity, and "2.4–2.9σ" is also juxtaposed. Per the review instructions, this requires explicit annotation at every co-location.
**Fix:** Place the "not directly comparable" qualifier inline at every occurrence of the pipeline-recovery SNR.

**P1B-E9 — "Planck/ACT DR6 2.4–2.9σ" cannot be reconstructed from cited references.**
- Planck NPIPE [15]: β = 0.30 ± 0.11 → 2.73σ
- ACT DR6 [3]: β = 0.215 ± 0.074 → 2.91σ

Neither reference yields 2.4σ. Where does 2.4σ come from?
**Fix:** Cite the source of the 2.4σ value or correct the range to 2.7–2.9σ.

**P1B-E10 — Eskilt+Komatsu dataset labeling acknowledged unreliable in the paper itself.** Abstract footnote a admits that "the labels 'PR4/NPIPE' attached to the Eskilt+Komatsu likelihoods" refer to a *code-repository* dataset different from the published PRD paper, and that "the repository README is the authoritative source for the dataset attribution in the executed pipeline." A PRD submission cannot defer dataset provenance to a third-party GitHub README. The authors must verify and state which dataset the executed pipeline used.
**Fix:** State unambiguously which dataset (PR3+WMAP9 vs PR4+NPIPE) was used in the ALP-MCMC reported in Sec. VI; do not delegate to an external README.

**P1B-E11 — Cobaya version ambiguity.** Sec. V A: "Cobaya [20] (v3.5 original; v3.6.1 verification)". What was run on v3.5? What was re-run on v3.6.1? Were both included in the 309 189 sample headline? CAMB versions also need to be pinned. Reproducibility is impossible as stated.
**Fix:** Single version specification per chain; provide hash-pinned environment lock files.

---

## MAJOR findings

**P1B-M1 — Acknowledged catastrophic failure of the promised Bayes-factor / Savage-Dickey computation.** Sec. III caveat and Sec. V B both admit that the headline w₀wₐ quintom claim cannot be supported by Bayesian evidence: "the LCDM point (w, wₐ) = (−1, 0) lies at > 4σ in the joint marginal tails (Table II...) and is therefore unsampled". The departure quoted as "+4.3σ" is then explicitly downgraded in Table II footnote a to "a posterior-tail extrapolation distance only, not a Bayes-factor or ln B exclusion and not a frequentist tension". This is fatal to the headline phrasing of Sec. III (Physics interpretation): "disfavors… the LCDM point at the joint level".
**Fix:** Replace "+4.3σ" / "−3.6σ" in body and Table II with "marginal-tail posterior-extrapolation distance" everywhere — *including the Sec. III narrative sentences*, which currently read as σ-tension claims.

**P1B-M2 — w₀+wₐ joint significance is undefined as written.** "w₀+wₐ = −1.4788 ± 0.1485" is reported as if it were an independent statement, but it is a linear combination whose σ depends on Cov(w₀, wₐ), which is not given. The reader cannot judge whether the joint distance is what σ_{w₀+wₐ} suggests.
**Fix:** Report the full 2×2 covariance.

**P1B-M3 — Pivot redshift calculation reproduces ±0.0301 from a different ap than 0.668.** Footnote b: "σ²_{w_pivot} = σ²_{w₀} + (1−aₚ)² σ²_{wₐ} = (0.0436)² + (0.3320)² (0.1864)² = (0.0301)²". But this is *not* the standard decorrelated pivot variance; the cross term is missing because at the decorrelated point Cov(w₀, wₐ) is forced to vanish. Recomputing: 0.0436² + (1−0.668)² × 0.1864² = 0.00190 + 0.110² × 0.1864²? No — (0.332)² × (0.1864)² = 0.1102 × 0.0347 = 0.00383, then sqrt(0.00190+0.00383) = 0.0757, not 0.0301. The footnote's parenthetical "(0.3320)²(0.1864)²" appears to multiply σ_{wₐ}² by (1−aₚ)² but then doubles the squaring. The arithmetic is wrong as printed.
**Fix:** Recompute and verify σ_{w_pivot}; the displayed equation does not give the displayed answer.

**P1B-M4 — "Worst Rˆ−1" footnote contradicts table.** Table I caption claims "all 17 sampled parameters… satisfy Rˆ−1 < 3 × 10⁻³" but the table row "Worst Rˆ−1" shows 0.003 only for Planck+BAO+SN. The text in Sec. III also says "Worst Rˆ−1" = 0.001 for full-tension. Which is the actual worst, and across which parameters?
**Fix:** Single, consistent convergence number per chain with named parameter.

**P1B-M5 — 9 720 accepted samples / 3 configurations = 3 240 per chain.** Sec. VI uses these to claim posterior recovery of three different ALP parameters. With ~3 240 samples per chain and "Rˆ−1 < 0.01 for all runs", convergence diagnostics across MPI ranks should be provided (number of chains, ESS by parameter). At this sample count the βₐLP = 0.336 ± 0.107° claim is not robust.
**Fix:** Provide N_chains, ESS_min per parameter, R-hat by parameter.

**P1B-M6 — The "Liu et al. cross-validation at 0.5σ in H₀" is not a valid cross-check.** Sec. III: "Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈" with Ref. [11]. But the datasets differ (Liu et al. use DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018; this paper's headline ∆N_eff result uses different combinations). Agreement of central values across different stacks is expected and is not a model-comparison cross-check.
**Fix:** Either re-run on the matched stack or remove the claim.

**P1B-M7 — Bias-injection results misframed as systematic floor.** "We carry forward as the NaMaster systematic floor" — a 0.04° MC-injection-recovery bias is a property of the deconvolution algorithm on the simulated covariance, not a sky systematic. It does not bound the foreground+miscalibration systematic budget at all.
**Fix:** Remove "systematic floor" language; the figure is an algorithmic recovery bias only.

**P1B-M8 — Footnote 4 cross-reference is broken.** Footnote 4: "the abstract spectator-status restriction θ_i ≪ 1 (Eq. (1)-adjacent disclaimer)". Eq. (1) in the body is β̂_NaMaster = 0.238°, not anything about Ω_a or θ_i. Wrong cross-reference.
**Fix:** Correct or delete the cross-reference.

**P1B-M9 — Internal pipeline paths in the body.** p. 5: "pipelines/h200_results/pod1_namaster_umap_2026-04-29/". Internal compute-cluster paths and dated artifact directories should not appear in a PRD-facing manuscript.
**Fix:** Replace with the repository-relative reproducibility URL only.

**P1B-M10 — "spin_torsion.input.yaml" mentioned but only generic YAML names appear in the repository description.** Sec. III: "the parameters are correctly aliased per the spin_torsion.input.yaml configuration". Appendix A lists four YAMLs of different names (cobaya_planck.yaml, …, cobaya_full_tension.yaml) — no spin_torsion.input.yaml. Either rename the file or correct the body.

**P1B-M11 — Reporting an "ongoing" Planck-only chain at Rˆ−1 ~ 0.05.** Abstract and Sec. III mention a third dataset combination "currently at sub-convergence sample count" — this should not appear in a published paper at all. Report only what has converged.

**P1B-M12 — Companion-paper claims that are nowhere in this paper.** Sec. I lists "13 logically-independent structural barriers, the perturbation-transparency theorem, the 14-barrier table" — claimed in [1] but not derivable from anything here. References from this paper's body to these results (e.g., "Paper I(a)'s § Structural Tension as a constraint") cannot be reviewed.
**Fix:** Either submit [1] alongside or remove all such cross-references and stand on the present manuscript's own merits (in which case very little remains).

**P1B-M13 — Quintom interpretation overclaimed.** "w₀+wₐ = −1.48 ± 0.15 requiring phantom crossing" — this is the central claim of Sec. III's "Physics interpretation". But w_pivot = −1.034 ± 0.030 (consistent with −1 at 1.1σ). Sentences such as "the chain is centered well into quintom-B territory at w₀+wₐ ≈ −1.48" require disclosure that w_pivot is consistent with −1; the framing is misleading without it.

---

## MINOR findings

**P1B-m1 — Title.** "Technical Verification Companion" is unusual for PRD. Use a descriptive title.

**P1B-m2 — Reference [15]** contains the comment "the value used at L256/L416 of P1B" — an internal cross-paper line-number tag in the bibliography. Remove.

**P1B-m3 — Reference [22]** also contains internal-use notes: "Used in P1A Sec. VI to point readers to the bounce-class alternative…". Bibliography is not for internal annotation.

**P1B-m4 — Long, nested abstract footnote.** Footnote a in the abstract spans ~12 lines explaining a dataset disambiguation. This belongs in the body, not the abstract footnote.

**P1B-m5 — Eq. (1) numbering.** β̂_NaMaster = 0.238° is "Eq. (1)" but is not algebraically an equation — it is a measurement summary.

**P1B-m6 — Headline arithmetic minor inconsistencies.** β_combined = 0.241°/0.061° = 3.95σ; paper quotes 3.9σ — fine.
M_B − 5log₁₀(73.04) gives 0.155 mag offset, divided by σ=0.049 gives 3.16σ; paper rounds to 3.2σ — fine.
But "this is the same ∼3.6σ" is wrong: 3.16σ in M_B-axis ≠ 3.6σ in H₀-axis without the actual joint Fisher computation.

**P1B-m7 — Acronym/notation drift.** "Caγ" appears in mixed forms (C_{aγ}, Caγ).

**P1B-m8 — Figure 1 corner plot.** Caption matches the body, but no readable parameter labels are visible at the rendered resolution in the corner plot; the marginal posteriors are illegible. Either enlarge or split.

**P1B-m9 — "(taken at scan-prior midpoint values; the ∼ 25× misalignment tuning required to reconcile the headline result with the spectator-consistent corner is disclosed in Sec. VI and fn. 4)"** — this hedge appears verbatim in the abstract scope summary, Sec. I scope summary, *and* Sec. VI note. Excessive repetition.

**P1B-m10 — Acknowledgments AI disclosure.** "Use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation" is fine, but should additionally specify which sections/figures were AI-assisted (PRD now expects this).

---

## NITs

**P1B-N1 — Date format inconsistency.** "Dated: 2026-06-08 PDT" — PDT is not standard for a publication date.

**P1B-N2 — Equation/parenthesis nesting in footnote 1.** "176 240 × 0.7 + 132 949 × 0.7 ≈ 216 432" is just (176 240 + 132 949) × 0.7 = 216 432.3. Could be one line.

**P1B-N3 — Self-citing inconsistencies.** Footnotes use mixture of "fn. 4" and "footnote 4".

**P1B-N4 — Length.** At 11 pages for what is by the authors' own admission a null-result verification companion of an unpublished paper, the manuscript is too long for its content. Recommended maximum: 6 pages if any version survives revision.

---

## Summary recommendation

**REJECT**

The paper concedes, in its own abstract and Sec. I, that none of its three analyses is a test of the underlying theory it claims to support; it is a companion to a paper [1] listed as "in preparation" that PRD cannot evaluate; the body contains explicit reviewer-response and "earlier draft" prose, conflicting sample counts for the same chain, an admitted catastrophic failure of the promised Bayes-factor computation, and a "spectator-ALP consistency check" whose MCMC explicitly samples the *non*-spectator regime (per the authors' own footnote 5). Table II reports a w₀wₐ quintom-B chain that is the largest numerical departure from ΛCDM in the paper but is not mentioned in the abstract, while the headline "+4.3σ" is downgraded in the table footnote to a marginal-tail extrapolation distance "not a Bayes-factor or ln B exclusion and not a frequentist tension". These are not revisable defects within a single round; the manuscript requires consolidation with Paper I(a), removal of all internal-audit prose, re-running of the ALP MCMC on a physically consistent prior, and an honest reframing of what was actually proved. I recommend rejection without prejudice to a re-submission of a substantially restructured manuscript bundled with [1].

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings (Second-Pass Review)

After re-examining the paper with fresh attention to arithmetic, cross-references, and internal consistency, I have identified the following additional issues. **The most serious are P1B-E12 and P1B-E13: the Table II pivot-variance arithmetic implies an impossible (>1) correlation coefficient.**

---

## ESSENTIAL findings (additional)

**P1B-E12 — Table II w₀wₐ posterior is internally inconsistent: implied correlation coefficient exceeds 1.**

Cross-checking the three quoted numbers — σ_{w₀} = 0.0436, σ_{wₐ} = 0.1864, σ_{w₀+wₐ} = 0.1485 — against the quoted decorrelation point aₚ = 0.668:

- From σ²_{w₀+wₐ} = σ²_{w₀} + σ²_{wₐ} + 2 Cov(w₀, wₐ):
  0.1485² = 0.0436² + 0.1864² + 2 Cov  ⟹  Cov(w₀, wₐ) = −0.00728,
  implying correlation ρ = −0.00728 / (0.0436 × 0.1864) = **−0.895** (physical).

- From the pivot relation aₚ = 1 − Cov(w₀, wₐ)/σ²_{wₐ} (the paper's stated convention in footnote b):
  Cov = (1 − 0.668) × 0.1864² = +0.01153,
  implying |ρ| = 0.01153 / (0.0436 × 0.1864) = **1.42** > 1. **Impossible.**

These two values of Cov(w₀, wₐ) are not only different in sign and magnitude; one of them implies a correlation > 1 and is therefore inconsistent with *any* multivariate Gaussian posterior. At least one of {σ_{w₀}, σ_{wₐ}, σ_{w₀+wₐ}, aₚ} in Table II is incorrect as printed. Because aₚ and σ_{w_pivot} are both downstream of the covariance, this propagates into the entire "wₚᵢᵥₒₜ = −1.034 ± 0.030, consistent with −1 at −1.1σ" sentence — which is currently a load-bearing caveat against the quintom interpretation.

**Fix:** Recompute the posterior covariance from the actual chain, publish it explicitly, and reconcile all four numbers (σ_{w₀}, σ_{wₐ}, σ_{w₀+wₐ}, aₚ) or correct whichever is wrong.

**P1B-E13 — Footnote b arithmetic does not derive σ_{w_pivot} = 0.0301 from the formula it states.**

Footnote b writes:
> σ²_{w_pivot} = σ²_{w₀} + (1−aₚ)² σ²_{wₐ} = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²

Computing the middle expression directly:
0.0436² + (0.332 × 0.1864)² = 0.00190 + 0.003828 = 0.005728,
√0.005728 = **0.0757**, not 0.0301.

The displayed formula simply omits the cross-correlation term 2(1−aₚ) Cov(w₀, wₐ), which is the *only* term that distinguishes σ²_{w_pivot} from the un-pivoted variance and which is non-zero by construction. The correct standard formula is σ²_{w_pivot} = σ²_{w₀} − Cov(w₀,wₐ)²/σ²_{wₐ}. If one back-solves for the missing term assuming the answer 0.0301² is the intended value, one finds the cross term should contribute approximately −0.00483, implying Cov ≈ −0.00728 — which is consistent with the σ_{w₀+wₐ} derivation but *not* with the quoted aₚ = 0.668 (see P1B-E12). The footnote thus simultaneously (i) writes an incomplete formula, (ii) presents an arithmetic chain that does not yield the final value claimed, and (iii) hides the internal posterior inconsistency.

**Fix:** Rewrite footnote b with the correct decorrelated-pivot formula and a consistent covariance.

**P1B-E14 — Internal contradiction on which Planck dataset Eskilt & Komatsu [2] used.**

- Abstract footnote a: "the published PRD paper [2] (PRD 106:063503, arXiv:2205.13962) analyzes **Planck PR3 + WMAP9**".
- Sec. VI body (p. 6): "the published Eskilt & Komatsu joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ) [2] (the joint **WMAP9 + Planck PR4/NPIPE** analysis…)".

These cannot both be true. The paper later goes on to attach "PR4/NPIPE" labels to the likelihoods actually used in the ALP-MCMC. This contradiction matters because the 3.6σ headline value the paper cites is its anchor observational constraint, and the reader cannot determine which Planck data product underwrites it.

**Fix:** Resolve the contradiction by direct inspection of arXiv:2205.13962 §II and state the correct dataset once, consistently.

---

## MAJOR findings (additional)

**P1B-M14 — Eq. (3) and the abstract use different fiducial Δϕ/fₐ values for "the" β prediction.**

- Eq. (3): β ≈ (α_EM × 8)/(4π) × **1.07** ≈ 0.29° (stated for m ≈ 2H₀).
- Body following Eq. (3): "The fiducial value β ≈ **0.27°** corresponds to the midpoint m ≈ **1.8 H₀**, Δϕ/fₐ ≈ **1.0**".
- Abstract: "the spectator-ALP fiducial value **β = 0.27°**".

So the explicitly displayed equation gives 0.29° with Δϕ/fₐ = 1.07, but the "fiducial" value carried throughout the rest of the paper (0.27°) requires Δϕ/fₐ = 1.0 and m/H₀ = 1.8 — the latter being inside, but not at the midpoint of, the natural prior m/H₀ ∈ [1, 3] (whose actual midpoint is 2.0, not 1.8). The "fiducial" parameter choice is therefore tuned to recover a specific β, not the natural-prior-midpoint prediction the text claims it to be.

**Fix:** State a single fiducial point with consistent (m/H₀, Δϕ/fₐ, β); identify whether "1.8 H₀" was chosen to match the data rather than the prior midpoint.

**P1B-M15 — Table II w₀wₐ chain reports no minimum ESS.**

Table II claims 128,385 accepted samples across 16 chains with R̂−1 = 0.00820 — but no ESS_min is quoted (compare Table I, which reports Min ESS = 4,744 and 4,692). With R̂−1 at borderline 0.008 across 16 chains, ESS by parameter is essential for assessing whether the quoted tail probabilities (especially the "+4.3σ" extrapolation) are reliable. 128,385 / 16 ≈ 8,000 raw per chain; the autocorrelation length on w₀wₐ runs is typically ~50–200, putting ESS per parameter potentially in the low hundreds per chain.

**Fix:** Report Min ESS and per-parameter R̂ for Table II.

**P1B-M16 — Inconsistent post-burn-in count for the full-tension chain appears in three places with three different values.**

- Fig. 1 caption: "119,617 post-burn-in samples".
- Footnote 1 narrative text: "the post-burn-in count of the full-tension subset alone is 123,129".
- Footnote 1 arithmetic: "176,240 × 0.7 ≈ 123,368".

This compounds P1B-E5 with a third value (123,129) which the footnote handwaves as "within ±1% of the 123,368 exact computation". A two-percent disagreement among "samples used in the figure", "samples after burn-in", and "70% of raw" should not exist in a methods paper; one of these is the operational answer and the others are wrong.

**Fix:** Single defined post-burn-in count; reconcile with Fig. 1.

**P1B-M17 — "m ≈ 1.8 H₀" as the "midpoint" of m/H₀ ∈ [1, 3] is not the midpoint.**

p. 7: "The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H₀". The midpoint of [1, 3] is 2, not 1.8. This is either a transcription error or evidence that "midpoint" is being used loosely to mean "the value at which the prediction matches the observation". The latter usage undermines the natural-prior narrative.

**Fix:** Either use the true midpoint m/H₀ = 2 (which gives β ≈ 0.29° per Eq. (3) — and is therefore *inconsistent* with the 0.27° abstract fiducial) or replace "midpoint" with "the data-preferred point in the natural-prior range".

---

## MINOR findings (additional)

**P1B-m11 — Transcription drift between Table I and body text.**
- Table I: H₀ = 67.68 ± 1.06 (full-tension); Sec. III narrative (p. 4): "H₀ = 67.69 ± 1.06"; abstract: 67.68. A 0.01 disagreement.
- Table I: ΔN_eff = −0.020 ± 0.169 (full-tension); Sec. III narrative: "−0.02 ± 0.17". Inconsistent significant figures throughout.

**P1B-m12 — Eq. (1) versus abstract β̂ value consistency.** Eq. (1) gives β̂_NaMaster = 0.238° at SNR = 20.32. Abstract says "recovers β̂ = 0.238° (pipeline-recovery bias 0.032°)". Consistent ✓ — but Eq. (1) is mis-labelled as an "equation" when it is a measurement value, and the SNR is in parentheses without uncertainty quoted on β̂. Provide σ(β̂) per realization or per Monte Carlo ensemble.

**P1B-m13 — Sec. VI bias-scaling claim is based on N = 2 injections.** The "amplitude-dependent ∼12%" relative bias is derived from comparing two injection points (0.27° → 0.032° bias; 0.342° → 0.040° bias). With only two points, "amplitude scaling" cannot be characterized; a third injection or an analytic mask-bias derivation is required to claim this is amplitude-dependent.

**P1B-m14 — Abstract reports "ongoing" Planck-only run.** The abstract states "plus a third Planck-only combination ongoing"; an in-progress chain at R̂−1 ∼ 0.05 should not appear in an abstract at all.

**P1B-m15 — Eq. (3) prefactor "1.07" not derived.** The reader is given β ≈ (α_EM C_aγ)/(4π) × Δϕ/fₐ, then told Eq. (3) uses Δϕ/fₐ = 1.07 (m ≈ 2H₀), without showing where 1.07 comes from. Eq. (2) gives 0.65 at m = H₀, θᵢ = 1; the 1.07 value must come from a separate ODE point. Cite or display.

**P1B-m16 — Footnote 4 "1/25" claim.** The footnote writes "Ωₐ(0.1)/Ωₐ(0.5) ~ 1/25". (0.1/0.5)² = 1/25 ✓ arithmetic. But this presents the spectator vs scan-midpoint ratio as if it were a "fine-tuning of the misalignment initial condition"; it is in fact a *posteriori* relabeling of a scan-prior choice as fine-tuning. The "25× fine-tuning" language is a rhetorical artifact of the prior choice θᵢ ∈ [0.5, 2] and would disappear with θᵢ ∈ [0.05, 0.5].

**P1B-m17 — "3.16σ" rounded to "∼3.2σ" then equated to "the canonical 3.6σ".** p. 4 contains the exact sentence "∼ 3.2σ relative to the chain's σ_{M_B} = 0.049 marginal width and corresponds exactly to the canonical 3.6σ Hubble tension". 3.16σ and 3.60σ are not the same number; they cannot "correspond exactly" because they are 1.7 raw σ apart. The juxtaposition of two different significance values as "the same" is a category-E (null-procedure-comparability) issue not flagged in the original review beyond P1B-m6.

---

## NIT findings (additional)

**P1B-N5 — Eq. (1) numbered as an equation.** Already flagged in P1B-m5 as notation drift; reiterating that "β̂_NaMaster = 0.238° (pipeline-recovery SNR = 20.32)" is a result statement, not an equation, and should be presented as such (in-line or in a small results table).

**P1B-N6 — Inconsistent decimal precision on σ values.** Throughout the paper: 0.169 vs 0.17, 0.107 vs 0.11, 0.094 vs 0.09. The same uncertainty is reported to different precisions in different sentences. Pick a precision convention.

**P1B-N7 — "C₂ apodization at 2° scale" / shape parameter ambiguity.** The standard NaMaster C2 apodization is parametrized by a scale length; the body should specify whether 2° is the apodization aperture or the smoothing FWHM-equivalent.

**P1B-N8 — Abstract length and density of footnoting.** Abstract footnote a spans ~150 words. Footnote material should generally not be in abstracts at all.

---

## Summary of second-pass impact

The two findings that materially change my recommendation strength are **P1B-E12** (Table II posterior parameters imply correlation coefficient > 1, which is mathematically impossible) and **P1B-E13** (footnote b arithmetic does not derive the stated answer). Together with the original P1B-E4 (abstract omits Table II entirely) and the original M1 (the +4.3σ extrapolation is itself walked back in the very same table footnote), the entire dark-energy / w₀wₐ component of the paper is now internally inconsistent at the arithmetic level, not merely under-supported. My original recommendation of **REJECT** is reinforced; if anything, the second pass makes it clearer that a major revision is not viable without re-running and re-reporting the underlying chain.