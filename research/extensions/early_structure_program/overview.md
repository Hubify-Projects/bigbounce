# Early Structure Program Overview

**Date:** 2026-03-13
**Program:** Test whether the spin-torsion bounce framework can produce testable early-structure signatures
**Status:** Roadmap phase — no production compute launched

---

## 1. Why Early SMBH / PBH-Seed Phenomenology Is Relevant

The spin-torsion bounce cosmology replaces the Big Bang singularity with a quantum bounce at ρ_crit ≈ 0.27 ρ_Pl. The bounce-to-inflation transition sets the initial conditions for inflation. If these initial conditions differ from the standard Bunch-Davies vacuum, they can imprint features on the primordial scalar power spectrum P(k).

This is the **only physically legitimate pathway** from bounce physics to early-structure observables. Direct torsion effects vanish at astrophysical densities (suppressed by ρ/ρ_Pl ≈ 10^{-83}). The connection is indirect: bounce → modified P(k) → modified structure formation → observable consequences.

The paper explicitly identifies this as an open problem (Sec. XIV): "Numerical simulation of the transition from torsion-dominated bounce through reheating to standard slow-roll" and "Determination of N_tot as a function of parent black hole mass and spin."

### Why now?

1. **JWST is discovering SMBHs at z > 10** that challenge standard seed formation models (UHZ-1 at z = 10.1, GN-z11 AGN at z = 10.6). These observations create demand for non-standard seed channels.
2. **PBH constraints are maturing** — the PBHbounds repository provides comprehensive, machine-readable constraint curves across 30+ orders of magnitude in mass.
3. **The perturbation spectrum through LQC bounces is actively studied** (Agullo, Ashtekar, Wilson-Ewing, Zhu et al.) — though NOT yet for our specific spin-torsion variant.

---

## 2. What Is Plausibly Connected to Our Theory

### Directly connected (pending calculation):
- **Primordial perturbation spectrum through the bounce.** The modified Friedmann equation H² = (8πG/3)ρ[1 − ρ/ρ_crit] changes perturbation evolution at near-Planck densities. LQC calculations show this can produce oscillatory features, suppression at large scales, or (in some models) enhancement at specific small scales.
- **Parity-odd tensor perturbation asymmetry.** The parity-odd operator (α/M)ε^{abcd}K_{ab}R_{cd} explicitly breaks the left-right symmetry of tensor perturbations during inflation (already noted in the paper's Sec. XIV on "Parity-Odd Primordial Gravitational Waves"). At second order, chiral tensor modes can source scalar perturbations.

### Indirectly connected (phenomenological parameter shifts):
- ΔN_eff ≈ 0 (from MCMC), H₀ = 69.2 ± 0.8, σ₈ = 0.785 ± 0.016. These modify early structure formation timing by ~10%, but this effect is generic to any ΛCDM+ΔN_eff model and not framework-specific.

### Not connected:
- Direct torsion effects at astrophysical densities (suppressed by ≥10^{-83})
- Four-fermion interaction at sub-Planck densities (suppressed by ~10^{-34} relative to weak force)
- Cosmic rotation effects on halo formation (suppressed by (ω/H)² < 10^{-21})

---

## 3. What Is Currently Speculative

| Item | Status |
|------|--------|
| Bounce modifies P(k) in ways favorable to early structure | **Speculative.** LQC calculations exist but not for spin-torsion variant. Results are model-dependent. |
| Bounce produces small-scale P(k) enhancement → PBH formation | **Speculative and unlikely.** Existing LQC calculations generally find suppression, not enhancement. |
| Parity-odd tensor asymmetry → scalar perturbation sourcing at 2nd order | **Highly speculative.** No calculation exists. Would require: chiral GW background → scalar induced at 2nd order → modified P(k). Three levels of speculation. |
| P(k) feature at specific scale → heavy SMBH seeds | **Standard astrophysics.** Well-studied in PBH/enhanced-P(k) literature. Not specific to our framework. |

---

## 4. Strongest Observable Hooks

Ranked by defensibility:

1. **JWST high-z SMBH mass/number-density constraints** — Real data, growing rapidly. The question "what seed properties are needed?" is well-posed even without our framework.

2. **PBH constraint bands** — Comprehensive, public, machine-readable (PBHbounds). Directly constrain P(k) enhancement amplitude.

3. **Combined P(k) bump parameter space** — A single parameterized P(k) feature simultaneously predicts SMBH seed abundance AND PBH constraints. The "allowed window" where seeds are heavy enough but PBH constraints are satisfied is a publishable result.

4. **Minimum growth time consistency** — Given z_obs of a quasar and its estimated M_BH, compute the minimum seed mass M_seed needed for Eddington-limited growth. This is model-independent.

---

## 5. Classification

| Option | Assessment |
|--------|-----------|
| Current-paper extension | **NO.** The perturbation spectrum through the bounce has not been calculated. Without it, any P(k) feature is a free parameter unconnected to our equations. Including this in the current paper would be overclaiming. |
| Follow-up paper | **POSSIBLY.** A Paper 2 focused on: (a) parameterized P(k) features from bounce cosmologies, (b) SMBH seed + PBH constraint analysis, (c) identifying the P(k) feature the bounce would need to produce. This is a legitimate ~15-page paper. |
| Long-term research program | **YES.** The actual perturbation calculation through the spin-torsion bounce is a 1-2 year project requiring numerical LQC expertise. This program lays the groundwork and identifies the observational targets. |

**Recommendation:** Build the phenomenological forward models now (Tracks A and B). These are useful regardless of the bounce framework — they answer "what P(k) features are needed for early SMBHs?" in a model-independent way. The framework connection is motivational, not calculational, and must be stated as such.

---

## 6. Key Distinction from Previous Assessment

The previous extension assessment (2026-03-12) correctly noted that direct torsion effects vanish at astrophysical densities and classified both tracks as FUTURE WORK ONLY. That assessment was correct for the DIRECT connection.

This program takes a different, more serious approach: the connection is through the **primordial perturbation spectrum**, which is set during the bounce-to-inflation transition at Planck densities where the modified Friedmann equation IS active. This is the legitimate theoretical pathway, and it is explicitly flagged as an open problem in our paper.

The difference is:
- Previous: "Does torsion affect SMBH formation?" → No (suppressed by 10^{-83})
- This program: "Does the bounce modify P(k), and if so, does the modified P(k) affect early structure?" → Unknown (calculation not done), but the question is well-posed and the phenomenological consequences can be explored now.
