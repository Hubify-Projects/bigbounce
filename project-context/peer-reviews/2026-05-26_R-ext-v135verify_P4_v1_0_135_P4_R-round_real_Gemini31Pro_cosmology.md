# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v135verify_P4_v1_0_135
**Wall time**: 34.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=103483, completion=3591, reasoning=2970, total=107074

---

## BLOCKER: Incorrect EFT Sourcing Claim
**ID:** PAPER-GEM-B1
**Section:** VI.H, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Concrete Issue:** The text claims a chirality dipole "would require a background vector or tensor source rather than a scalar EFT operator." This is theoretically false. Parity-odd scalar EFT operators (e.g., pseudoscalar inflaton couplings like $\phi R \tilde{R}$ or $\phi W \tilde{W}$) are the standard mechanism for sourcing the chiral tensor perturbations that would drive this observable.
**Fix:** Remove the claim that scalar EFT operators cannot source this effect; explicitly acknowledge that pseudoscalar inflaton couplings routinely source chiral tensors.

## MAJOR: Missing Kinematic Dipole Floor
**ID:** PAPER-GEM-M1
**Section:** VI.F (Sensitivity Floor and Minimum Detectable Signal)
**Concrete Issue:** The paper projects a Fisher sensitivity floor of $\sim 0.29\%$ and an empirical floor of $0.75\%$, but completely ignores the kinematic dipole induced by the observer's peculiar velocity ($v/c \sim 1.2 \times 10^{-3}$). Aberration and Doppler modulation will induce an apparent $\mathcal{O}(10^{-3})$ chirality dipole that acts as a fundamental physical floor for any $\ell=1$ LSS observable.
**Fix:** Explicitly define the kinematic dipole ($\sim 0.12\%$) as a fundamental physical contaminant that must be subtracted or modeled for any sub-percent dipole search.

## MAJOR: Omission of GR Projection Effects in Transfer Function
**ID:** PAPER-GEM-M2
**Section:** VI.H, paragraph "Late-universe to primordial: the link, and its caveats"
**Concrete Issue:** The transfer function discussion lists linear TTT and survey depth, but omits GR projection effects (weak lensing magnification, redshift-space distortions) and non-linear Intrinsic Alignments (IA). These effects are critical because they mix parity-even and parity-odd modes under 2D projection, altering the $\ell=1$ signature.
**Fix:** Add GR projection effects (lensing, RSDs) and non-linear IA mode-mixing to the explicit list of required transfer-function components.

## minor: Overstated UV-Independence of CMB Birefringence
**ID:** PAPER-GEM-m1
**Section:** VI.H, paragraph "(i) Chiral gravitational-wave power asymmetry"
**Concrete Issue:** The text claims CMB birefringence (axion-photon) and morphology (gravitational) are "not directly numerically comparable in any common parameter." This overstates UV-completion independence; in many string-theoretic UV completions, anomaly cancellation strictly links the gauge and gravitational Chern-Simons couplings.
**Fix:** Soften the claim to state that while they constrain different low-energy EFT operators, specific UV completions tightly link their coefficients.
