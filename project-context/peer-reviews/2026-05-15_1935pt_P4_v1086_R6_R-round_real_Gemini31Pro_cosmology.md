# P4_v1086_R6 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1935pt
**Wall time**: 132.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=77155, completion=15996, reasoning=15357, total=93151

---

This adversarial review evaluates the theoretical framing, statistical methodology, and cosmological interpretation of the manuscript. The review identifies one critical theoretical blocker regarding the symmetry classification of the observable, alongside major and minor findings related to EFT operator mapping, leakage attribution, and statistical phrasing.

## PAPER-GEM-B1: Fundamental symmetry misclassification of the dipole observable (BLOCKER)
**Location:** Title, Abstract, Section I, Section VIII.H
**Issue:** The paper (following the Shamir literature it critiques) fundamentally conflates a chirality dipole with parity violation. The observable is the CW fraction asymmetry $A(\hat{n}) \propto \vec{L} \cdot \hat{n}$. Under a global parity transformation $\vec{x} \to -\vec{x}$, the line of sight $\hat{n} \to -\hat{n}$ and the axial spin vector $\vec{L} \to \vec{L}$, so the asymmetry field transforms as $A^P(\hat{n}) = -A(-\hat{n})$. Expanding in spherical harmonics, the coefficients transform as $a_{\ell m}^P = (-1)^{\ell+1} a_{\ell m}$. Therefore, the monopole ($\ell=0$) and quadrupole ($\ell=2$) are parity-odd. However, the dipole ($\ell=1$) transforms as $a_{1m}^P = +a_{1m}$. A chirality dipole is a parity-even polar vector; it indicates a breaking of *isotropy* (e.g., a bulk flow or local anisotropic structure), but *not* parity violation. 
**Fix:** Explicitly state the $a_{\ell m}^P = (-1)^{\ell+1} a_{\ell m}$ derivation to correct the literature's misconception. Reframe the paper as testing *isotropy* via the dipole, while noting that the (systematic-dominated) monopole is the actual parity-odd observable.

## PAPER-GEM-M1: Category error in EFT operator mapping (MAJOR)
**Location:** Section VIII.H, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Issue:** The text claims that morphological chirality and the parity-odd 4PCF "can couple to the same dim-7 EFT amplitude $g_*$" (Cabass et al. 2023). This is a category error. The 4PCF is an isotropic parity-odd scalar correlator sourced by a scalar EFT operator. A global chirality dipole ($\langle \text{spin} \cdot \hat{n} \rangle \neq 0$) breaks spatial isotropy (selecting a preferred axis). An isotropic scalar EFT operator like $g_*$ cannot source an isotropy-breaking dipole without a background vector/tensor field. 
**Fix:** Remove the claim that the dipole couples to the $g_*$ scalar EFT operator. Clarify that the dipole tests isotropy-breaking chiral vectors/tensors, whereas the 4PCF tests isotropic parity-violating scalars.

## PAPER-GEM-M2: Residual attribution error in MASTER leakage collapse (MAJOR
