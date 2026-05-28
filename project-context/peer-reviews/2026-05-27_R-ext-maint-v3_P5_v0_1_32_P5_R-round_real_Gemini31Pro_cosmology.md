# P5 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P5_v0_1_32
**Wall time**: 41.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=29988, completion=4353, reasoning=3610, total=34341

---

## BLOCKER

### PAPER-GEM-B1
**Section:** Conclusions (Section XI.B)
**Issue:** The proposed fundamental EFT operator $\mathcal{L}_{\rm parity} \supset g_\phi (\nabla_i \phi) (\nabla^i \rho / \rho_{\rm bg}) (\hat{L} \cdot \hat{z})$ explicitly contains the observer's line-of-sight vector $\hat{z}$. A local UV Lagrangian cannot depend on the Earth's position; this violates local Lorentz and rotational invariance.
**Fix:** Formulate the interaction covariantly (e.g., coupling the pseudoscalar to a fluid kinematic quantity like vorticity $\omega^\mu$), and derive the $\hat{z}$ dependence strictly as an observational projection effect of the 3D angular momentum onto the sky plane.

## MAJOR

### PAPER-GEM-M1
**Section:** Conclusions (Section XI.B)
**Issue:** The text cites Alexander & Yunes (Chern-Simons gravity, $\phi R \tilde{R}$) and Lue-Wang-Kamionkowski (chiral tensor modes) as justifications for the $\nabla \phi \cdot \nabla \rho$ operator. Both of these foundational papers describe couplings to tensor modes (gravitational waves), which do not generate tree-level scalar density-gradient couplings to galaxy angular momentum.
**Fix:** Remove the claim that this specific scalar-density operator is "Chern-Simons-style" or in the "LWK sense", or replace the citations with literature that actually derives parity-violating couplings to LSS scalar/vector modes.

### PAPER-GEM-M2
**Section:** Conclusions (Section XI.B)
**Issue:** The operator uses $\nabla^i \rho / \rho_{\rm bg}$ in the Lagrangian. In general relativity, matter density $\rho$ is a frame-dependent component of the stress-energy tensor $T_{\mu\nu}$, not a fundamental scalar field, making the operator non-covariant.
**Fix:** Replace the density gradient with a well-defined covariant fluid scalar gradient (e.g., $\nabla^\mu n / n$ where $n$ is fluid number density) or a curvature invariant.

## minor

### PAPER-GEM-min1
**Section:** Conclusions (Section XI.B)
**Issue:** The EFT coupling $g_\phi$ in the dimension-5 (or higher, depending on the $\hat{L}$ formulation) operator is written with mass dimension 1, but the bound is expressed as a dimensionless ratio $|g_\phi \nabla \phi / H_0| \lesssim 10^{-2}$, which obscures the EFT power counting and the mass scale of the new physics.
**Fix:** Parameterize the operator with an explicit UV cutoff scale $\Lambda$ (e.g., $\mathcal{L} \supset \frac{1}{\Lambda} \partial_\mu \phi \dots$) so the bound directly constrains the physical scale $\Lambda$.

### PAPER-GEM-min2
**Section:** Conclusions (Section XI.B)
**Issue:** The theoretical bound directly equates the real-space EFT density gradient $\nabla \rho$ to the observed V-Web class density contrast without accounting for the redshift-space distortion (RSD) Jacobian, which anisotropically deforms apparent density gradients.
**Fix:** Add a sentence explicitly stating that the bound assumes the real-to-redshift space gradient mapping is order-unity, deferring the exact RSD transfer-function calculation to future work.
