# Referee report — A3M v3M.0.9 (R4, Claude Fable 5.1 INT leg)

- **PDF:** `site/public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` (12 pages, all read incl. Appendix A)
- **sha256:** `6c543e5e9885c6db58e07576482ed6f283b0307ad1499c6309a4651d3c26fb1a`
- **Date:** 2026-09-04
- **Venue:** Physical Review D (regular article)
- **Reviewer stance:** independent, skeptical; no prior boards/dispositions/SSOT read. External spot-checks: arXiv abstracts of refs [1],[4],[8],[9],[15],[18] (title/author/venue/abstract only).

## Summary

The paper (i) re-derives the matter-bounce squeezed amplitude f_NL = −35/16 vertex-by-vertex in the in-in formalism, localizes the Cai et al. factor of two, and reconciles the separate-universe values via a linear identity δN_c = (1−ε/3)ζ plus an L/K/X/S shift decomposition; (ii) bounds linear transmission through the bounce (T < 1/2, scheme S1) and adds the bounce's own cubic term, giving f_NL^after ∈ [−0.65,−0.50]; (iii) tests the value against NANOGrav (slope only), PBH abundance (ratio-level, then a null on the lab's own spectrum), and LSS (DESI DR1 + forecasts). The arithmetic I could check (Table I sums, angular averages, Eqs. 5, 7, 10, A3, Tables II–IV z-scores and σ-ratios, Appendix A identities) is internally consistent. The headline transmitted range, however, is not consistent with the transfer interval quoted beside it; the γ=3 justification in §IV relies on a low-k spectrum P_R ∝ k that contradicts the near-scale-invariant spectrum used in §V C and the cited source's own abstract; the transfer formula Eq. (6) is not derivable from the text and its definition (bispectrum vs f_NL transfer) is ambiguous; and one key reference is mis-titled. The scope and limitation statements are otherwise unusually candid.

## Verdict: **major-revisions**

## MAJOR findings

1. **Headline transmitted range excludes part of the transfer interval it is quoted with (abstract; §III p.4; §III A table p.4; §VI B; §VII).** The abstract and §III state T_fNL ranges over 0.165–0.409 (the 0.409 value is the LQC effective-fluid convention, explicitly listed on p.4). With Eq. (7), f^after = −(85/48)T − 5/24 exactly (I verified the three tabulated rows −0.501/−0.651/−0.555 to 3 decimals). At T = 0.409 this gives f^after = −0.93 (and −1.83 at −35/8), outside the quoted [−0.65,−0.50] ([−1.20,−0.86]). The §III A table and every downstream number (Table IV, §VI B Δf = 0.35–0.55, Discussion) silently use only the geometric-convention rows (T ≤ 0.25). Either the effective-fluid convention is excluded by the S1 scheme — in which case say so explicitly and stop quoting 0.409 next to the range — or the range must be widened to [−0.93,−0.50] with corresponding changes to Table IV (SPHEREx bare significance would reach 1.3σ at −35/16) and the discrimination discussion. Resolves: state the convention that defines the range, recompute all downstream numbers under it.

2. **§IV D γ=3 justification is inconsistent with the paper's own spectrum and with the cited source (p.6, left column; §V C p.8).** The paper attributes Ω_GW ∝ f² to "Ω_GW ∝ P_R² … combined with the source spectrum's near-linear low-k growth P_R ∝ k (Eq. (8) there)". But §V C takes the model's spectrum at all scales to be a near-scale-invariant power law with n_s = 0.9649 (extrapolated 10–15 decades to PBH scales), which through the standard radiation-era induced-GW kernel gives Ω_GW ∝ f^0 (log-corrected), i.e. γ ≈ 5, not 3. Papanikolaou's abstract (arXiv:2504.11641) describes a nearly scale-invariant P_R for k < 10⁴ Mpc⁻¹ with enhancement on very small scales; the f² infrared scaling there is a property of that enhanced-peak spectrum's IR tail, not of a flat spectrum. The paper cannot simultaneously (a) claim γ=3 follows from the matter bounce's broad source spectrum and (b) use a flat n_s = 0.965 spectrum to declare the PBH channel a null. Resolves: derive (or cite with equation) the actual post-bounce P_R(k) the model predicts over nHz-to-PBH scales; either the §IV slope argument or the §V C null must change, or the paper must state explicitly that the two channels assume different spectra and why.

3. **Eq. (6) transfer is not derivable from the text and its definition is ambiguous (§III p.4).** T_fNL = [1 + r(1−ρ)]/(1+2r) is asserted with r = −9iA²I_∞/k³ and "|r| ≫ 1 numerically", then T = (1−ρ)/2. Three problems: (a) if the linear mode-mixing matrix carries the decaying mode with weight r and |r| ≫ 1, the post-bounce ζ is dominated by the pre-bounce decaying/constant mode, whose matter-contraction spectrum is not scale-invariant — this affects the power spectrum, not only the bispectrum, and the paper does not say whether T_fNL is the bispectrum transfer, the f_NL = B/P² transfer, or something else (a pure linear rescaling ζ→Tζ would give f_NL → f_NL/T, an enhancement); (b) A, I_∞, and the origin of the "1+2r" denominator are undefined in the paper; (c) the conclusion "linear transfer can only suppress, never invert or amplify" rests entirely on this formula. Resolves: give the linear mixing matrix, define T_fNL in terms of bispectrum and power-spectrum transfers, show the |r|≫1 limit, and state the post-bounce power spectrum implied.

4. **Ref. [9] is mis-cited (p.12).** Title given is "Gravitational Waves Induced by non-Gaussian Scalar Perturbations" but arXiv:1909.13728 / PRD 102, 083528 (2020) is Cai, Pi & Sasaki, "Universal infrared scaling of gravitational wave background spectra" (verified). The mis-titled paper is PRL 122, 201101 (2019), arXiv:1810.11000. The f³ causal-floor claim in §IV D and §VII B needs the correct title; check the .bib entry was not merged from two records.

5. **Abstract over-states the δN reconciliation (abstract; §II D; App. A.2).** The abstract says the gap "is explained at the equation level: the linear-order relation is a derived identity … the second-order piece is a recorded identity whose mechanism is not derived". "Explained" and "recorded, mechanism not derived" are not the same claim; the second-order coefficient 5ε(9−ε)/18 is a fit of numbers (5/4 + 15/8 = 25/8), not a derivation. The abstract should say the gap is *accounted for* at linear order and *tabulated* at second order. Also, Eq. (A3) and f^ρ = 5(ε−7)/8 give f_NL = −5 and −35/8 at ε→0, not the de Sitter/Maldacena values; the paper must state that these general-ε formulae hold only on the non-attractor growing branch ζ' = −3ζ/η and give their domain of validity in ε.

## Minor findings

1. p.2, after Eq. (4): "a monopole −15/8 and a quadrupole 15/16" — 15/16 is the μ² coefficient; the ℓ=2 Legendre coefficient is (2/3)(15/16) = 5/8. Say "μ² coefficient".
2. p.8 §V C: "T_B ≳ 10⁸–10¹⁰ GeV – seven decades above the BBN scale used to bound the mass range elsewhere in this section" — 10⁸ GeV is ~11 decades above 1 MeV, and BBN is not used elsewhere in §V. Fix or delete.
3. p.8: "a shortfall of 7.0 orders of magnitude" — the ranges 0.006–0.019 vs 5×10⁻¹⁰–1.3×10⁻⁹ span 6.7–7.6 decades; quote a range, not one decimal.
4. Abstract quotes A-ratio "≈1.7–1.9" (lab-shape threshold scan) while Table III's 27-point lognormal grid gives 1.732 [1.610, 1.809]; the abstract should quote both or the primary tabulated one.
5. §IV: the refit γ = 2.567 ± 0.382 is only 1.5σ from the generic causal floor γ = 2; Table II should include a γ = 2 row (official: 3.3σ; refit: 1.5σ) since §IV D and §VII B make the γ=2 vs 3 distinction a central point.
6. Table II caption: "differences from a self-reproduction run … ≤ 3×10⁻¹⁵" is not a validation; drop or move to the reproducibility statement.
7. §V B: f_PBH "moves by more than 100 decades" across the grid — this is a statement about exp(−δ_c²/2σ²) at fixed A; say so, otherwise it reads as a numerical pathology.
8. Footnote 1 (p.8): the paper knowingly propagates Ω_DM = 0.674 (actually h) "as printed"; since Eq. (12) is displayed, print the correct value and note the source typo instead of reproducing it.
9. §VI A: fine as stated; but the DESI z-scores use the asymmetric error on the side of the prediction only — say which side.
10. Reproducibility statement: internal repo paths (`research/track_a3_multichannel/…`, `outputs/*.json`) are quoted as if archival; PRD requires a persistent identifier — the text acknowledges no DOI is minted. Mint before submission.
11. Reference list: [8] Papanikolaou arXiv:2504.11641 and [15] Choudhury et al. EPJC 85, 472 (2025) verified correct; [18] DESI DR1 numbers (samples, redshifts, both f_NL values) verified; [4] Li et al. verified.

## Questions to authors

1. Under scheme S1 with |r| ≫ 1, what is the post-bounce *power spectrum* tilt? If the constant mode dominates, how is n_s = 0.9649 recovered in §V C?
2. Is the LQC effective-fluid convention (T = 0.409) part of scheme S1 or not? Table on p.4 omits it without comment.
3. Does Eq. (A3) reduce to Maldacena's (5/12)(1−n_s) in any limit, or is it valid only on the non-attractor branch? State the domain.
4. What is the model's P_R(k) between the LSS pivot and the nHz band — the one required to convert Channel I to an amplitude prediction (§IV D last sentence)?
5. For the FIRAS μ = 1.65×10⁻⁸: computed with which k_D(z) window and which spectrum (flat n_s = 0.9649 or the lab's extrapolated one)?

## Integrity note

No fabricated numbers detected; every value I recomputed (Table I sum, angular average, Eq. 7 rows, Eq. 10 ceilings, Table II z-scores, Table IV σ-ratios, App. A identities) matches. Unsupported as printed: the [−0.65,−0.50] range (excludes T = 0.409 listed beside it) and the P_R ∝ k attribution in §IV D (contradicted by §V C and by the cited abstract).
