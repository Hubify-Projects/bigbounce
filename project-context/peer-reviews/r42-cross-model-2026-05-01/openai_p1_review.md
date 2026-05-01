---
model: gpt-5
paper: p1 — Spin-Torsion Cosmology — structural closure of ECH dark energy
pdf: /Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/main.pdf
date: 2026-05-01
input_tokens: 47301
output_tokens: 10572
total_tokens: 57873
reviewer: openai (cross-model adversarial)
retry: true (reasoning=medium, max_output=32000)
---
## BLOCKERs
1) Reproducibility contradiction for new CMB and galaxy-spin results
Evidence: §VI “Independent verification (April 2026, production 500-realization run)” and Eq. (18) report a NaMaster E–B pipeline recovery (βˆNaMaster = 0.238°; “rejects the null at high significance”), and §V plus §III.B claim an independent 8.47M-galaxy ViT-Small chirality analysis; but “Data and Code Availability” (p. 28–30) explicitly states “No CMB polarization map analysis code is provided… No CNN galaxy classifier is included.”
Fix: Either (a) remove all new NaMaster and ViT-Small results from the manuscript, or (b) deposit the exact code, masks, beams, noise realizations, seeds, trained weights, data splits, and scripts necessary to reproduce Eq. (18) and the 8.47M classifier numbers, and update the repository links in the paper.

2) Misleading “high-significance” language for a simulation-only pipeline check
Evidence: §VI, after Eq. (18): “This… rejects the null at high significance.” The test is a bias/validation study with injected β on Monte Carlo realizations, not a detection from sky data.
Fix: Delete the “rejects the null” phrasing and replace with: “The pipeline shows negligible bias (<0.04°) for constant-β injections; no independent detection claim is made.”

3) Formal inconsistency in the action and variational setup
Evidence: Eq. (1) includes a TabcTabc term while the text says the action is already “obtained after algebraic elimination of torsion” and “we work entirely in the second-order (metric) formalism,” yet Rabμν is still described as curvature of the torsionful Lorentz connection and the Holst sector is carried along. This mixes first-order and second-order treatments and leaves unclear what is being varied, with what fields remaining.
Fix: Rewrite §II.A.1 to present one consistent formulation. Either: (i) first-order Palatini with torsion as an independent variable and show explicitly how integrating out torsion yields the four-fermion term and makes the Holst piece purely Nieh–Yan/topological on-shell; or (ii) second-order, set Γ=Γ̊ from the start (T=0 for scalar matter), drop TabcTabc from the action, and move all four-fermion terms to an explicit “after elimination” effective Lagrangian. Make the variable set and EOM unequivocal.

4) Dimensionally incorrect estimate used to argue “torsion remains algebraic”
Evidence: §II.A.2 (“Torsion remains algebraic.— … correction O(α/MMPl2) ∼ 10−3”). The factor (α/M) has dimensions of inverse mass; multiplying by MPl2 is not dimensionless and the stated 10−3 is unjustified. The comparison must use a physical momentum/curvature scale.
Fix: Replace with a dimensionless, scale-aware estimate (e.g., compare the induced kinetic term ∼(α/M)k to the EC algebraic term ∼κ∼1/MPl2, giving a ratio ∼(α/M)k MPl2; then evaluate at a stated k such as H, reheating, etc.). If this ratio is not universally ≪1, drop the numeric “10−3” and qualify when the algebraic approximation is valid.

5) Overclaim: “no free parameters” for the post-bounce initial conditions
Evidence: §II.B, bullet list: “The bounce creates a new expanding region with initial conditions completely determined by the parent black hole properties, with no free parameters.” In LQC the matter sector (e.g., φB, V(φ)) specifies post-bounce evolution; black-hole provenance does not eliminate these degrees of freedom.
Fix: Qualify to: “the bounce fixes the maximum density ρcrit; post-bounce evolution still depends on matter initial conditions (e.g., φB and its momentum/potential), even if one hypothesizes BH-origin priors.”

6) Inconsistent availability of derivations cited as central to claims
Evidence: §IV and Ref. [28] (p. 30): “companion technical note… available upon request” contains key negative results (condensate channel, one-loop effective action) used multiple times (e.g., §XVI “First-principles derivation status”). PRD cannot evaluate non-public calculations.
Fix: Move the relevant derivations into an appendix of this manuscript or post the technical note on arXiv and cite its identifier.

## MAJOR
1) Bayes factor and “model preference” are for ΛCDM+ΔNeff, not for the spin–torsion theory, yet presented prominently
Evidence: Table III and §VII.B report ln B=+4.8 (tension dataset) using Savage–Dickey, while §VII caveat admits the model is stock CAMB ΛCDM+ΔNeff and the estimator is biased for correlated posteriors. The abstract and Table I headline this as part of the framework assessment.
Fix: Relegate Bayes-factor discussion to an appendix or 1–2 lines in §VII with an explicit title “ΛCDM+ΔNeff proxy only” and remove any suggestion that it tests ECH. State that robust evidence would require a torsion-modified Boltzmann code and nested sampling.

2) Heuristic “inflationary suppression” formula lacks derivation and clear domain of validity
Evidence: Eq. (14) and §II.C.1 introduce Dinf = e−3Ntot (Treh/MGUT)3/2 and set Ntot≈92 to match ρΛ, but no derivation is shown and the dependence on reheating history is only asserted.
Fix: Provide a short derivation (number density redshifting assumptions, entropy production, which quantity is being diluted) and a sensitivity analysis to Treh and non-instantaneous reheating; otherwise label Eq. (14) explicitly as an ansatz and move the Ntot≈92 “fit” out of Results.

3) Constant-β combination inflates significance and is inconsistently presented
Evidence: §VI “Consolidated birefringence summary”—the paper adopts an inverse-variance combined β = 0.241° ± 0.061° (3.9σ) as “headline,” despite acknowledging shared calibration between Planck and ACT and citing the published joint analysis β = 0.342° ± 0.094° (3.6σ). Elsewhere (§III.A) the “actual statistical detection significance” is 2.4–2.9σ.
Fix: Choose a single, publication-grade number. Prefer the published single-pipeline results (Planck 2.4–2.7σ; ACT 2.9σ) or the published joint analysis (3.6σ) and remove the ad hoc 3.9σ IVW unless you provide a proper treatment of inter-experiment correlations.

4) NaMaster pipeline description is insufficient for validation
Evidence: §VI gives Nside, ℓmax, fsky and some mask variants, but omits key details (beam/window, E/B leakage treatment, mode-coupling matrix details, noise and foreground model used, calibration marginalization).
Fix: Add a concise methods paragraph: masking scheme, apodization, purification settings, beam and transfer functions, how β is estimated (quadratic estimator or template fit), and what is injected (uniform β vs. anisotropic), with equations.

5) “Torsion remains algebraic” claim requires scale choice; otherwise may fail in high-curvature regimes
Evidence: §II.A.2 asserts smallness generically; but the correction depends on background scales (K, R). Later you invoke Planck-scale evaluation for vacuum energy (Appendix B), where the same suppression would be weakest.
Fix: Bound the correction in the regimes actually used (bounce epoch, inflation, late universe) with explicit k/H or R/M2 scales, and state if/where the algebraic approximation could break down.

6) Forecast claims for SPHEREx fNL lack sufficient specification
Evidence: §IX and Table V quote “3–5σ realistic (5–5.5σ optimistic)” with some degradation factors in footnote 5, but no explicit priors, redshift binning, shot noise, and survey systematics model are given.
Fix: Provide the minimal forecast inputs: survey volume, number density vs. z, bias model, bφ prior, photo-z model, GR-projection templates, and clarify whether the result is from Heinrich et al. [14] adopted directly or recomputed here.

7) “Vacuum energy from condensates too large by 1044” and related one-loop statements rely on unavailable calculations
Evidence: §IV and §XVI (“First-principles derivation status”) repeatedly cite results relegated to the non-public [28].
Fix: Either include the key steps (channel decomposition, sign of the coupling at γ=0.274, criticality estimate) in an appendix or remove the quantitative claims and keep only the qualitative statement “not viable at one loop in the minimal model.”

8) Inconsistent use of “production 500-MC run” vs. “no CMB code provided”
Evidence: §VI claims a “production 500-realization run… canonical source: …/summary.json” while “Data and Code Availability” says no CMB code is provided.
Fix: Align the paper: either provide the code and data products or drop the result entirely.

9) Barrier 4 “Planck suppression” uses k2/MPl2 ≈ 10−122 without justifying the chosen k
Evidence: Eq. (24) assumes k ≈ H0. For CMB/galaxy perturbations or recombination-era physics, the relevant k differ by many orders. The same section elsewhere uses Planck-scale on-shell evaluations.
Fix: State clearly the scale at which the ratio is evaluated and apply it consistently. If using late-time cosmology, justify H0; if using bounce-era estimates elsewhere, avoid mixing regimes.

10) Wilson–Ewing citation missing
Evidence: Fig. 1 caption contains “Wilson-Ewing [?]” as a placeholder.
Fix: Add full reference or remove the placeholder.

## MINOR
- Multiple inconsistent spellings of “Poplawski” (“Pop lawski”) and minor grammatical issues (e.g., §III.B “consis­tent with null all-sky dipole (0.43σ; the 2.0σ monopole offset…)”).
Evidence: §I.A, §III.B, references [11–13].
Fix: Standardize spelling; copyedit for clarity.

- Clarify mapping between Λ and ρΛ in text
Evidence: Eq. (12) uses Λeff = Ξ MPl2 while elsewhere you use ρΛ = Ξ MPl4 (Appendix B).
Fix: Add one sentence after Eq. (12): “With the Einstein–Hilbert convention S ⊃ (MPl2/2)∫√−g (R−2Λ), Λ=ρΛ/MPl2.”

- Chain count bookkeeping language is hard to follow
Evidence: Footnote 4 in §III.D describes raw, weighted, post-burn-in, and getdist-thinned counts with four numbers.
Fix: Present a small table listing raw, post-burn-in, and effective sample size per dataset to eliminate ambiguity.

- Replace informal “Scope note.—” lead-ins with standard subsection headings suitable for PRD style.
Evidence: p. 4 (Table I context) and §III.D “Scope statement.—”.
Fix: Convert to formal subsections.

## Strengths
- The “perturbation-transparency” theorem is stated clearly and correctly for canonical scalar matter, with a compact, checkable argument (§XII). This is a useful reminder that the Holst sector decouples in scalar perturbations.
- The paper is unusually candid about limitations and negative results (e.g., ΔNeff consistent with zero; galaxy spin channel null; ALP birefringence as a spectator rather than an ECH prediction), which improves credibility.
- The systematic “barrier catalog” is a valuable organizing device. Even where some “barriers” rest on standard EFT lore, collecting them against ECH helps narrow which observables are worth pursuing.
- The cosmology MCMC is transparently documented (likelihoods, priors, R̂ values; Table II) and lands on sensible parameters consistent with Planck ΛCDM.
