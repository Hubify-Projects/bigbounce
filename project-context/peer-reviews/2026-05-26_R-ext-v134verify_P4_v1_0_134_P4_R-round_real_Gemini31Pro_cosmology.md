# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v134verify_P4_v1_0_134
**Wall time**: 73.9s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=102675, completion=7416, reasoning=6613, total=110091

---

## PAPER-GEM-M1: Incorrect EFT of Inflation Operator Dimension (MAJOR)
**Section:** VIII.H.1, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Issue:** The text claims Cabass et al. (2023) parameterize "dimension-7 operators in the EFT of Inflation". This is theoretically incorrect; Liu et al. (2019) proved, and Cabass et al. explicitly state, that the leading parity-odd interaction for a single-clock Goldstone boson $\pi$ in the EFT of Inflation appears at dimension 8 (e.g., $\epsilon^{\mu\nu\rho\sigma} \partial_\mu \dot{\pi} \partial_\nu \partial^2 \pi \partial_\rho \partial^3 \pi \partial_\sigma \partial^4 \pi$). 
**Fix:** Change "dimension-7 operators" to "dimension-8 operators".

## PAPER-GEM-M2: Missing Kinematic Dipole (Ellis-Baldwin) Bound (MAJOR)
**Section:** IV.C (Dipole Analysis) / VIII.H
**Issue:** The paper ignores the guaranteed kinematic dipole from the observer's velocity with respect to the CMB ($\beta \sim 1.2 \times 10^{-3}$). Because the classifier exhibits morphology/size-dependent biases (demonstrated in Fig 11), Doppler magnification and aberration will modulate the observed CW fraction across the sky, inducing a kinematic chirality dipole via GR projection effects. 
**Fix:** Add a sentence explicitly bounding the kinematic chirality dipole ($\beta \times \text{classifier bias} \sim 10^{-5}$), demonstrating it falls safely below the $0.2\%$ statistical floor.

## PAPER-GEM-M3: Contradiction on Parity-Odd Observables (MAJOR)
**Section:** Abstract / I. Introduction vs. VIII.H.1
**Issue:** The Abstract and Introduction claim "the parity-odd analog requires 3D spin-vector... observables", but Section VIII.H.1 correctly states "The signed parity-odd diagnostics in our data are the monopole". The 2D projected monopole is a parity-odd pseudoscalar observable; 3D vectors are not strictly required to test parity violation, only to form parity-odd *anisotropies*.
**Fix:** Revise the Abstract/Intro to clarify that it is the parity-odd *anisotropy* (or vector analog) that requires 3D spin-vectors, acknowledging the 2D monopole is already a parity-odd test.

## PAPER-GEM-m4: Missing Foundational TTT Citations (minor)
**Section:** VIII.H.1, paragraph "(i) Chiral gravitational-wave power asymmetry"
**Issue:** The text references "Tidal-torque theory (Doroshkevich 1970; White 1984)" inline, but neither Doroshkevich (1970) nor White (1984) are actually included in the bibliography.
**Fix:** Add the formal citations for Doroshkevich (1970) and White (1984) to the bibliography.

## PAPER-GEM-m5: Ambiguous EFT Source Phrasing (minor)
**Section:** VIII.H.1, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Issue:** The claim that an $\ell=1$ dipole "would require a background vector or tensor source rather than a scalar EFT operator" conflates background isotropy breaking with operator spin. A scalar EFT operator evaluated on an anisotropic background can perfectly well source a dipole.
**Fix:** Change "rather than a scalar EFT operator" to "rather than an isotropic scalar EFT operator background".
