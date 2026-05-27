# P5 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P5_v0_1_32
**Wall time**: 51.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=30034, completion=4633, reasoning=3833, total=34667

---

## PAPER-GEM-B1: BLOCKER
**Section:** XIII (Conclusions), "Mapping to a physical operator"
**Issue:** The proposed EFT operator $\mathcal{L}_{\rm parity} \supset g_\phi (\nabla_i \phi) (\nabla^i \rho / \rho_{\rm bg}) (\hat{L} \cdot \hat{z})$ is theoretically nonsensical. A fundamental Lagrangian cannot be constructed from macroscopic fluid variables ($\rho$), emergent astrophysical vectors (galaxy angular momentum $\hat{L}$), or observer-dependent fixed frames (line-of-sight $\hat{z}$), as this violates basic Lorentz/rotational invariance and EFT counting rules.
**Fix:** Remove the equation and the claim of "Mapping to a physical operator." If a parameterization is needed, formulate it strictly as a phenomenological macroscopic bias expansion, not a fundamental Lagrangian term.

## PAPER-GEM-M1: MAJOR
**Section:** IV.A, Steps 8-11
**Issue:** There is a sign error in the text's definition of the tidal tensor. Defining $\Phi(k) = -\delta_k / k^2$ and $T_{ij}(k) = k_i k_j \Phi(k)$ yields a trace of $-\delta_k$. This means overdense regions ($\delta > 0$) have negative eigenvalues, which would cause Step 11 to classify clusters (0 eigenvalues $>0$) as voids.
**Fix:** Correct the text to $T_{ij}(k) = \frac{k_i k_j}{k^2} \delta_k$ (or define the scaled potential as $\Phi(k) = +\delta_k / k^2$) to match the standard Hahn et al. 2007 convention used in the actual code.

## PAPER-GEM-M2: MAJOR
**Section:** IV.A and VII (Phase 2 sensitivity sweep)
**Issue:** The pipeline applies the Newtonian Poisson equation to the observed redshift-space galaxy overdensity to compute the tidal tensor. At the largest smoothing scales probed ($R_s = 50$ Mpc/$h$), gauge-dependent relativistic projection effects (e.g., Doppler magnification, Sachs-Wolfe) alter the observed $\delta$, breaking the Newtonian Poisson assumption and deforming the tidal tensor independently of standard RSD.
**Fix:** Add a caveat in Section XII (Limitations) explicitly stating that the $R_s = 50$ Mpc/$h$ sweep cell is subject to uncorrected GR projection effects that alter the effective density field.

## PAPER-GEM-min1: minor
**Section:** XIII (Conclusions)
**Issue:** Citing Alexander & Yunes (2009) and Lue et al. (1999) to justify the macroscopic $\mathcal{L}_{\rm parity}$ operator is a category error. Those papers describe fundamental field couplings (e.g., to the metric or gauge fields), not phenomenological couplings to fluid density gradients or galaxy angular momentum.
**Fix:** Remove the citations from the EFT operator sentence, or explicitly clarify that they only inspire the macroscopic toy model by analogy.

## PAPER-GEM-min2: minor
**Section:** XI.B (Bounce vs. inflation discrimination)
**Issue:** The paper frames the null as an "observational upper bound" for future models, but provides no theoretical mechanism by which primordial parity violation survives non-linear Tidal Torque Theory (TTT) to produce a specifically *environment-dependent* (void vs cluster) chirality signal at $z \sim 0$. 
**Fix:** Explicitly state that primordial parity violation signatures are expected to be highly suppressed by non-linear TTT, making the environment-dependent bound strictly phenomenological rather than a direct constraint on early-universe action parameters.
