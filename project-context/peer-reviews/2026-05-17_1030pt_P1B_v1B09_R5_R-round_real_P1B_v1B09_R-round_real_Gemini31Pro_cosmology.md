# P1B_v1B09 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_1030pt_P1B_v1B09_R5_R-round_real
**Wall time**: 117.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=13608, completion=15996, reasoning=15360, total=29604

---

## PAPER-GEM-B1: SH0ES Prior Mathematically Missing/Broken in "Full-Tension" Chain
**Classification**: BLOCKER
**Section**: 2 and Table 1
**Concrete Issue**: The claim that Planck's inverse-variance weight "pulls" the Full-tension $H_0$ posterior to $67.68 \pm 1.06$ despite the SH0ES prior ($73.04 \pm 1.04$) is mathematically false for a Bayesian update. In $\Lambda$CDM+$\Delta N_{\rm eff}$, Planck's unconstrained $H_0$ error is $\sim 1.5$; adding a Gaussian prior of $73.04 \pm 1.04$ must shift the mean to $\sim 70$. The fact that $H_0$ actually *decreased* from the Planck+BAO+SN baseline ($67.79 \pm 1.09$) to the Full-tension run ($67.68 \pm 1.06$) proves the SH0ES likelihood is either missing, zero-weighted, or failing to evaluate in the Cobaya YAML.
**Fix**: Fix the Cobaya YAML to properly include the SH0ES likelihood, rerun the Full-tension chain, and update the posteriors; alternatively, remove the SH0ES dataset from the paper entirely.

## PAPER-GEM-M1: NaMaster Validation Bypasses Miscalibration Degeneracy
**Classification**: MAJOR
**Section**: 4 (Data Methods: CMB E-B Analysis)
**Concrete Issue**: The pseudo-$C_\ell$ validation injects rotation into a foreground-cleaned CMB map. This bypasses the primary observational challenge of modern cosmic birefringence measurements: breaking the degeneracy between the cosmic rotation angle $\beta$ and the instrumental miscalibration angle $\alpha$, which strictly requires the presence of unrotated galactic foregrounds.
**Fix**: Add an explicit disclaimer stating that this pipeline validates only the algebraic pseudo-$C_\ell$ $E \to B$ deconvolution, not the physical separation of $\beta$ from instrumental miscalibration systematics.

## PAPER-GEM-M2: Undefined Variable $\beta_{\rm free}$ in MCMC Fit
**Classification**: MAJOR
**Section**: 6 (MCMC parameter estimation)
**Concrete Issue**: The variable $\beta_{\rm free} = 0.344^\circ \pm 0.096^\circ$ is introduced without definition, context, or citation. It is impossible to tell if this is a baseline fit from the author's own 9,720-sample MCMC program or a literature value being referenced.
**Fix**: Define $\beta_{\rm free}$ explicitly (e.g., "our model-independent MCMC fit to the Planck+ACT likelihood") or provide the missing literature citation.

## PAPER-GEM-m1: Holst Four-Fermion Parity-Violation Omission
**Classification**:
