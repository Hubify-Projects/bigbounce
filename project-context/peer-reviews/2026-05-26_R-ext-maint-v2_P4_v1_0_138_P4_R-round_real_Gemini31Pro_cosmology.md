# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint-v2_P4_v1_0_138
**Wall time**: 60.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=106918, completion=5936, reasoning=5033, total=112854

---

I have reviewed the manuscript with a focus on theoretical physics, EFT counting, GR projection effects, and model-class scope boundaries. I found no blocker-grade flaws that invalidate the core observational null result, but there are several major theoretical errors in the interpretation and future-projection sections that must be corrected.

## PAPER-GEM-M1
**Severity:** MAJOR
**Location:** Section VI.H, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Issue:** The text attributes the parity-odd 4PCF to "dimension-7 operators in the EFT of Inflation, parameterized by $g_*$". This is a factual error in EFT counting. Cabass, Ivanov, & Philcox (2022) explicitly define $g_*$ as the coefficient of the leading parity-odd operator in the EFT of Inflation, which is dimension-8 (specifically, it requires three spatial derivatives and one time derivative of the Goldstone boson to contract with the Levi-Civita tensor).
**Fix:** Change "dimension-7 operators" to "dimension-8 operators".

## PAPER-GEM-M2
**Severity:** MAJOR
**Location:** Section VI.H, paragraph "Symmetry classification of the chirality dipole"
**Issue:** The text claims an axial-vector dipole "would require a background vector or tensor source rather than a scalar EFT operator." This is theoretically false. A background pseudoscalar field with a superhorizon spatial gradient (an isocurvature fluctuation) or a domain wall naturally breaks isotropy, provides a preferred spatial direction ($\nabla \phi$), and sources an axial dipole via standard scalar EFT operators like $\phi F \tilde{F}$.
**Fix:** Soften to "would require a background vector, tensor source, or a scalar field with a superhorizon spatial gradient, rather than a strictly homogeneous scalar EFT operator."

## PAPER-GEM-M3
**Severity:** MAJOR
**Location:** Section VI.I (Future Directions), LSST projection paragraph
**Issue:** The paper projects an LSST statistical sensitivity floor of $|A_{\rm dipole}| \sim 0.08\%$. This falls below the Solar System's kinematic dipole ($v/c \approx 0.12\%$). Doppler aberration and magnification bias will differentially modulate CW/CCW observed number counts if the classifier has any asymmetric sensitivity to surface brightness or apparent size, creating a hard GR/kinematic systematic floor at $\mathcal{O}(10^{-3})$ that will mimic a chirality dipole.
**Fix:** Add a sentence acknowledging that at the $0.08\%$ LSST sensitivity level, the kinematic dipole ($v/c \approx 0.12\%$) and associated Doppler aberration/magnification bias effects become a hard theoretical systematic floor that requires explicit modeling.

## PAPER-GEM-m4
**Severity:** minor
**Location:** Section IV.E, paragraph "The $w_{CW}(\theta)$ result is a fourth complementary diagnostic..."
**Issue:** The text frames the parity-even $w_{CW}(\theta)$ null as a "$\Lambda$CDM-tidal-torque-theory consistency test". At the largest scales ($\theta \sim 8^\circ$), GR projection effects (e.g., lensing, volume distortions) contribute to the observed angular correlation of shapes/spins. TTT is a purely Newtonian framework and is insufficient to define a strict consistency relation at cosmological scales without GR corrections.
**Fix:** Clarify that this is a "Newtonian $\Lambda$CDM-tidal-torque-theory consistency test" and note that strict cosmological-scale consistency relations require GR projection corrections.

## PAPER-GEM-N5
**Severity:** nit
**Location:** Section VI.H, "Symmetry classification of the chirality dipole"
**Issue:** The text correctly derives that the dipole is parity-even and tests isotropy, stating "a nonzero dipole would indicate a preferred axis in the cosmological-principle sense, and the present null sets an upper bound on any such axis". It fails to explicitly state the inverse corollary: a pure parity-violating but isotropic background (like a homogeneous $\dot{\phi} F \tilde{F}$) yields exactly zero dipole.
**Fix:** Add a half-sentence: "...upper bound on any such axis, meaning the dipole observable does not constrain isotropic parity-violating backgrounds."
