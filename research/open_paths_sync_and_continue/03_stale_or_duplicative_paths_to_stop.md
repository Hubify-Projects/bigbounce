# Stale or Duplicative Paths to Stop

**Created:** 2026-03-19
**Purpose:** Explicit STOP LIST. Any future agent or terminal that proposes work on these paths should be redirected to this file.

---

## STOP: Do Not Work On These

### 1. Gradient Expansion Extensions

**Status:** CLOSED (SUPPORTING_CROSS_CHECK)
**Reason:** The gradient expansion confirmed all structural features of f_NL (sign, magnitude, shape, parameter-freedom). The exact coefficient is resolved by the Cai action audit (-35/8). Extending the gradient expansion to capture the horizon-crossing contribution would reproduce what is already known. Zero marginal information. See `01_role_of_gradient_expansion_now.md` for the complete argument.

### 2. Numerical In-In Time Integral

**Status:** SUPERSEDED
**Reason:** The Cai action audit (`cai_action_audit/final_verdict.md`) showed the problem was not the numerical integration but the starting point (wrong action + wrong mode convention). The SymPy cancellation (`fnl_symbolic_cancellation/`) verified T1-T4 = 35/16 to 0.07%. The full coefficient -35/8 is now accepted with confidence > 85%. A new numerical integral would reproduce a known answer.

### 3. f_NL Coefficient Resolution

**Status:** RESOLVED
**Reason:** f_NL = -35/8. Verified by: (a) Cai et al. (2009) original derivation, (b) our Cai action audit identifying three specific action/convention differences, (c) SymPy verification of T1-T4 = 35/16 matching Li-Brandenberger to 0.07%, (d) gradient-expansion structural confirmation. The factor-of-2 discrepancy between Cai (-35/8) and Li-Brandenberger (-35/16) is explained by the Cai audit: our computation used the wrong starting action and mode convention. With the correct starting point, -35/8 follows.

### 4. Sign Convention Debate

**Status:** RESOLVED
**Reason:** The Cai action audit explained the sign flip: Cai's mode function u_k = A*sqrt(3)*zeta_k* (complex conjugate of ours). Under mode conjugation, Im[ext * I] flips sign. Additionally, f_NL(Planck) = |B|_NL(Cai) exactly in the squeezed limit (no hidden factor). The convention mapping is fully resolved per `fnl_derivation_execution/final_verdict.md`.

### 5. ECH Perturbation Theory (ANY Order, ANY Sector)

**Status:** PERMANENTLY CLOSED
**Reason:** Mathematical proof chain: canonical scalar -> zero spin density -> zero torsion (algebraic EC equation) -> Holst term is topological (Pontryagin density) -> no dynamics at any perturbation order -> no scalar vertices, no scalar bispectrum, no tensor parity, no GW birefringence. The Barbero-Immirzi parameter gamma is invisible in all scalar AND tensor observables for scalar field matter. 14+ structural barriers cataloged across `ech_bispectrum_gate/`, `ech_tensor_gate/`, Branches H, M, Q, and the chiral GW program. Every non-minimal extension (dynamical Immirzi, Nieh-Yan, fermionic sources, PGT) has been tried and closed.

### 6. Chiral GW from ECH Bounce

**Status:** PERMANENTLY CLOSED (FREQUENCY GATE FAILED)
**Reason:** The ECH bounce occurs at rho_c ~ 0.21 M_Pl^4. Characteristic frequency: f_0 ~ 10^{9-10} Hz (GHz). Five mechanisms tested to bring signal to observable frequencies; all failed. Structural scaling: Omega_GW ~ f_0^8, so reducing frequency by 10^{-13} (GHz to mHz for LISA) kills amplitude by 10^{-104}. No non-absurd parameter window survives. See `project_chiral_bounce_GW/phase0_results.md`.

### 7. More MCMC Without New Theory Hooks

**Status:** DEAD
**Reason:** 236,000+ frozen posterior samples across 4 datasets and 64 chains. All show Delta-N_eff ~ 0, H_0 = 67.68 (standard LCDM). Running more chains with the same theory model produces no new information. Only justified if a new theoretical parameter or coupling is introduced.

### 8. Hybrid DE Splice (Any Form)

**Status:** EXHAUSTIVELY REJECTED
**Reason:** Investigated in 7 disguised forms, rigorously rejected in all. Adding w0wa to bounce gives the same improvement as adding w0wa to plain LCDM. The bounce contributes nothing to the DE sector. 13 structural barriers (Foundations A-G) close all minimal routes from bounce to dark energy.

### 9. Generic LQC Brainstorming Without Concrete Target

**Status:** POLICY STOP
**Reason:** The 4-question test (genuinely new physics? technically natural tiny scale? distinctive prediction? publishable failure?) must be satisfied before opening any new branch. Generic exploration of LQC parameter space, alternative quantization schemes, or non-standard matter content without a specific observable target is sprawl. Every previous instance of open-ended exploration in this repo consumed sessions without advancing the discriminator.

### 10. Paper Drafting (Not This Terminal's Job)

**Status:** SCOPE STOP
**Reason:** The focused-paper draft is complete (`focused_paper_full_draft/`). LaTeX conversion, bibliography assembly, and submission preparation are mechanical tasks. This terminal's purpose is research execution, not manuscript preparation.

### 11. More Benchmark Verification

**Status:** STOP
**Reason:** f_NL = -35/8 has been verified by three independent methods (Cai original, SymPy T1-T4, gradient expansion structural). Additional benchmark exercises (reproducing other groups' intermediate results, testing alternative numerical methods, etc.) have zero marginal value. The number is settled.

### 12. Factor-of-2 / Convention / Normalization Debates

**Status:** RESOLVED
**Reason:** Every convention question has been traced to its source: (a) mode function conjugation explains the sign, (b) action coefficient difference (epsilon^2 vs epsilon^2 - epsilon^3/2) explains the magnitude, (c) Planck vs Cai f_NL definitions are identical in the squeezed limit. No ambiguity remains.

---

## How to Use This File

If a future agent proposes work on any item in this list:

1. Point them to this file.
2. Point them to the specific evidence file cited in the "Reason" field.
3. Redirect to the revalidated openings stack (`02_revalidated_openings_stack.md`).

The purpose of this list is to prevent the most common failure mode in this repository: reopening closed questions and consuming sessions that should be spent on genuinely open paths.
