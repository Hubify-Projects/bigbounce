# What to Deprioritize After Submission

**Created:** 2026-03-19
**Purpose:** Explicit list of directions that should NOT receive further effort, with clear reasoning for each.

---

## 1. ECH Perturbation Loops -- PERMANENTLY CLOSED

Both scalar and tensor gates conclusively shut. The chain of identities: zero spin (scalar field) -> zero torsion (Cartan equation) -> Holst term topological -> no perturbation-level dynamics. This is not an approximation that might be circumvented; it is a mathematical identity. 14+ structural barriers cataloged across `research/ech_bispectrum_gate/` and `research/ech_tensor_gate/`. The ECH bounce resolves the singularity at the background level but is perturbation-transparent for scalar field matter.

**Do not reopen under any circumstances.** Every session spent here is a session wasted.

---

## 2. Gradient Expansion Extensions -- SUPPORTING ONLY

The gradient expansion confirmed four structural features of the matter-bounce bispectrum (negative sign, O(1) magnitude, local shape, parameter-freedom) that were ALL already established by the in-in execution phase. It does NOT resolve the -35/8 vs -35/16 coefficient question -- it reaches the same mathematical bottleneck (growing-mode-squared coupling). Its sole new contribution is formalism-independent confirmation.

**Use in the paper as 3-4 sentences or a 1-page appendix.** Do not extend further. Active extension would provide no computational advantage over the in-in approach and would at best reproduce what SymPy already found.

---

## 3. More MCMC Without New Theory -- POINTLESS

Current chains (236,000+ samples, 64 chains, R-hat - 1 < 0.005) confirm Delta-N_eff ~ 0 with stock CAMB. This is because the bounce contributes nothing to the late-time expansion history that CAMB can model. Without a custom theory hook implementing bounce-specific modifications to the transfer functions or the Friedmann equation, more chains just reconfirm the same null. Every chain run without a theory modification is guaranteed to return the same answer.

**Only rerun if:** A custom CAMB/CLASS modification implementing Wilson-Ewing LQC corrections is built. This would be a non-trivial code development effort, not a configuration change.

---

## 4. Teleparallel / f(T) / f(Q) Bounce Builders -- SPRAWL

These frameworks massively expand the theory space (arbitrary functions of torsion scalars, non-metricity, etc.) without converging on testable discriminators. Each produces a bounce for some parameter choice, but none produces a parameter-free prediction that differs from what the Wilson-Ewing model already gives. The fundamental problem: more general frameworks have more freedom, which means more parameters, which means weaker predictions.

**Avoid.** The Wilson-Ewing model was selected precisely because it is maximally constrained (0 extra fields, 1 parameter, 1 parameter-free prediction). Loosening constraints moves backward.

---

## 5. GFT Condensate Cosmology -- TOO FAR

Conceptually interesting (emergent spacetime from group field theory), but years from observational predictions. The connection between GFT condensate dynamics and perturbation-level observables requires several layers of approximation that are not yet under control. Not the right next step for a program that has a testable prediction on a 2028 timeline.

---

## 6. Hybrid DE Splice -- EXHAUSTIVELY REJECTED

Explored in 7 disguised forms across the repo:
1. Direct bounce -> DE connection
2. ALP-mediated bridge
3. Environmental mass mechanism
4. Disformal coupling
5. Cyclic cosmology link
6. Attractor-sensitivity argument
7. Vacuum selection mechanism

All 7 closed with rigorous structural arguments (Foundations A-G). Adding w0wa to the bounce model gives the same improvement as adding w0wa to plain LCDM -- the bounce contributes nothing to the DE sector. The energy scale separation is 10^60 (Planck vs meV). This is structural, not approximate.

**Do not attempt an 8th form.**

---

## 7. Galaxy Spin Dipole -- EFFECTIVELY FALSIFIED

The coupling gap between the theoretical prediction and the observational null is 9-12 orders of magnitude. No viable bridge mechanism was found. Null reanalyses exist in the literature. The hierarchical Bayesian model in `reproducibility/galaxy_spins/` confirms no signal.

**Dead. Move on.**

---

## 8. CMB Anomaly Programs Without Sharp Predictions -- HAND-WAVING

The low-ell CMB anomalies (power deficit, hemispherical asymmetry, cold spot) are individually 2-3 sigma. Cosmic variance at ell < 30 is large. A posteriori statistics inflate significance. No single LQC model simultaneously explains all anomalies with specific parameter values -- the existing work (Agullo et al. 2021) provides qualitative fits, not quantitative predictions. Without a parameter-free prediction for C_ell at specific multipoles, this is fitting, not predicting.

**Only revisit if:** The LQC formalism audit (Path 2) reveals that dressed-metric vs hybrid give different low-ell predictions with specific numerical values. Otherwise, avoid.

---

## 9. Re-verifying f_NL = -35/8 -- DONE

The Cai action audit (`research/cai_action_audit/`) resolved all 3 implementation mismatches:
- Leading vertex coefficient: epsilon^2 vs (epsilon^2 - epsilon^3/2)
- Mode function phase: e^{-iketa} vs e^{+iketa}
- Chi-sector structure: completely different terms

The shape function reproduces all special cases:
- Squeezed: -35/8
- Equilateral: -255/64
- Folded: -9/4

SymPy verification at `research/fnl_symbolic_cancellation/` independently confirmed T1-T4 = 35/16 to 0.07% accuracy. The gradient expansion at `research/gradient_expansion_fnl_derivation/` confirmed structural features from an independent formalism.

**The verification chain is complete. Do not re-derive.**

---

## 10. Reopening the Factor-of-2 Debate -- RESOLVED

Cai et al.'s f_NL = -35/8 is the correct physical value. Li-Brandenberger's -35/16 was diagnosed as arising from a convention/implementation difference. The Cai action audit traced this to the mode function convention: Cai uses u_k = A*sqrt(3)*zeta_k^* (complex conjugate), which makes the bispectrum superhorizon-dominated. In this regime all cubic action terms contribute, yielding the full -35/8. Even if -35/16 were correct, MegaMapper still detects at 4.4 sigma.

**The audit settled this. Move on.**

---

## Summary Decision Matrix

| Direction | Status | Time Cost if Pursued | Information Gained |
|-----------|--------|---------------------|-------------------|
| ECH perturbation loops | DEAD | 2-4 months | Zero |
| Gradient expansion extension | SUPPORTING | 1-2 weeks | Marginal |
| More MCMC (no theory hook) | DEAD | Weeks of chains | Zero |
| Teleparallel / f(T) / f(Q) | SPRAWL | 6+ months | No prediction |
| GFT condensate | TOO FAR | Multi-year | Qualitative only |
| Hybrid DE splice | DEAD | Any time wasted | Zero (7 forms closed) |
| Galaxy spin dipole | DEAD | Weeks | Zero (9-12 OOM gap) |
| CMB anomalies (no prediction) | DEAD | 2-3 months | Narratives, not numbers |
| f_NL re-verification | DONE | 1-2 sessions | Zero (already verified) |
| Factor-of-2 debate | RESOLVED | Sessions | Zero (convention resolved) |

**Total time saved by not pursuing these: 12-24+ months of research effort redirected to genuinely open paths.**
