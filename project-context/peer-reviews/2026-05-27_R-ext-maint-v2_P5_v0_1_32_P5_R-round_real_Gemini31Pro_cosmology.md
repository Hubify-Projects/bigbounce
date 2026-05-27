# P5 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P5_v0_1_32
**Wall time**: 56.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=30023, completion=5389, reasoning=4416, total=35412

---

## PAPER-GEM-B1: Macroscopic and observer-dependent vectors in fundamental Lagrangian
**Classification:** BLOCKER
**Section:** XI.B (Mapping to a physical operator)
**Issue:** The text defines a Lagrangian operator $\mathcal{L}_{\rm parity}\!\supset\!g_\phi\, (\nabla_i\phi)\,(\nabla^i\rho/\rho_{\rm bg})\,(\hat L\cdot\hat z)$. A fundamental Lagrangian density must be a local Lorentz (or 3-space) scalar built from covariant fields. It is theoretically invalid to include a discrete macroscopic property (galaxy angular momentum $\hat L$) and an observer-dependent line-of-sight vector ($\hat z$) directly in $\mathcal{L}$. 
**Fix:** Define the EFT operator by coupling $\partial_\mu \phi$ to a fundamental covariant matter current (e.g., spin density $J^\mu_{\rm spin}$ or vorticity). Move the projection onto the observable $\hat L \cdot \hat z$ to the cross-section or observational selection function where it belongs.

## PAPER-GEM-M1: Dimensional inconsistency in EFT bound derivation
**Classification:** MAJOR
**Section:** XI.B (Mapping to a physical operator)
**Issue:** The derivation equates the spatial gradient $\nabla \rho / \rho_{\rm bg}$ (which carries dimensions of inverse length) with the dimensionless scalar contrast $\langle|\Delta\rho/\rho_{\rm bg}|\rangle$, completely dropping the characteristic length scale of the gradient (e.g., $1/R_s$). Consequently, the normalization by $H_0$ in the bound $|g_\phi\,(\nabla\phi)/H_0|\!\lesssim\!1\!\times\!10^{-2}/ \langle|\Delta\rho/\rho_{\rm bg}|\rangle$ is dimensionally arbitrary and physically meaningless.
**Fix:** Retain the spatial gradient scale in the derivation (e.g., $\nabla \rho / \rho_{\rm bg} \sim \delta / R_s$) and express the final bound in terms of the proper dimensionless combination $g_\phi |\nabla \phi| / R_s$.

## PAPER-GEM-M2: Non-covariant, gauge-dependent density coupling
**Classification:** MAJOR
**Section:** XI.B (Mapping to a physical operator)
**Issue:** The operator uses a naive spatial gradient of density $\nabla^i \rho$, which is not a gauge-invariant tensor quantity in General Relativity. If this is intended to be a fundamental action, it violates diffeomorphism invariance; if it is an EFT of Large-Scale Structure fluid action, it lacks the proper mapping to gauge-invariant comoving density perturbations or velocity potentials.
**Fix:** Formulate the coupling covariantly using the stress-energy tensor (e.g., $\partial_\mu \phi \, T^{\mu\nu} u_\nu$), or explicitly state this is an EFT of LSS fluid operator and use the gauge-invariant comoving density gradient $\nabla_i \delta_m$.

## PAPER-GEM-min1: Overstated UV-completion independence
**Classification:** minor
**Section:** XI.B (Bounce vs. inflation discrimination)
**Issue:** The claim that this is an "observational upper bound that any future bounce or inflation model proposing an environment-dependent parity signature must satisfy" overstates the scope of the constraint. Models where parity violation is mediated purely by tensor modes (e.g., chiral gravitational waves) rather than scalar-density couplings can produce environment-dependent signatures (via tidal alignments) without generating the specific $\nabla \rho$ signature bounded here.
**Fix:** Restrict the claim to state it bounds any model proposing a *scalar-mediated* or *density-gradient-coupled* environment-dependent parity signature.

## PAPER-GEM-nit1: Conflation of tensor and scalar parity-violation mechanisms
**Classification:** nit
**Section:** XI.B (Mapping to a physical operator)
**Issue:** Lue, Wang, and Kamionkowski 1999 (LWK99) is cited as an example of a "chiral-gravitational-wave coupling" in the same sentence that introduces a scalar density-gradient operator. LWK99 relies on the $\phi R \tilde{R}$ operator which modifies tensor modes (GWs), not scalar density gradients, making it a confusing reference for the specific $\nabla \rho$ operator being constructed.
**Fix:** Move the LWK99 citation to a sentence explicitly discussing tensor-mediated mechanisms, and cite a standard axion-matter fifth-force paper for the scalar density-gradient coupling.
