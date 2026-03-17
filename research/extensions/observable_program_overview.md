# Observable Extension Program Overview

**Date:** 2026-03-13
**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology (v1.5.0)
**Purpose:** Strengthen the observable phenomenology beyond the weak/near-zero ΔN_eff result

---

## 1. Why These Tracks Are Relevant

The spin-torsion bounce cosmology framework has three observable sectors:

1. **Cosmological parameters (ΔN_eff, H₀, σ₈)** — Already constrained by MCMC. Result: ΔN_eff consistent with zero. This is the weakest observable channel.

2. **Parity-odd sector (cosmic birefringence, EB/TB correlations)** — The framework's central equation is a parity-odd operator that qualitatively motivates cosmic birefringence. Planck and ACT have measured β ≈ 0.30° at 2.4–2.9σ. This is the strongest observable channel.

3. **Galaxy spin asymmetry** — Contested signal, 9–12 OOM gap between theory and observation. Explicitly excluded from this extension program (separate future paper).

The extension program evaluates three additional tracks to determine whether they can strengthen the current paper.

---

## 2. Track Summary and Honest Assessment

### Track A — Early SMBH Seed Abundance
**Connection to framework:** NONE DIRECT. The bounce occurs at Planck densities (ρ ≈ 0.27 ρ_Pl). SMBH seeds form at astrophysical densities ~83 orders of magnitude below this. The modified Friedmann equation reduces identically to GR at all relevant scales. The only indirect connection is ΔN_eff shifting standard cosmological parameters, but (a) ΔN_eff ≈ 0 from our MCMC, and (b) any model with the same parameter values gives the same prediction.

**Verdict:** FUTURE WORK ONLY. Including this would be padding, not science.

### Track B — PBH-like Relic / Compact Seeds
**Connection to framework:** NONE. The bounce creates baby universes *inside* existing BHs; it does not create PBHs in our universe. PBH formation requires enhanced curvature perturbations during inflation — no such calculation exists in the framework. Existing LQC perturbation calculations generally find power *suppression*, not enhancement.

**Verdict:** FUTURE WORK ONLY. Would require substantial new theoretical work (perturbation spectrum through the bounce) before any phenomenology is meaningful.

### Track C — Parity/CMB Observable Model
**Connection to framework:** DIRECT. The parity-odd operator (α/M)ε^{abcd}K_{ab}R_{cd} is the central equation. The birefringence formula C_ℓ^{EB} = 2β(C_ℓ^{EE} − C_ℓ^{BB}) is exact. Published measurements give β ≈ 0.30° at >2σ from multiple independent experiments. The one gap — the photon-torsion vertex — can be cleanly parameterized as f_photon and constrained.

**Verdict:** READY FOR CONSTRAINT ANALYSIS. This is the legitimate observable extension.

---

## 3. Rankings

| Criterion | Track A (SMBH) | Track B (PBH) | Track C (Parity) |
|-----------|---------------|---------------|-----------------|
| Scientific relevance to equations | 0/5 | 0/5 | 5/5 |
| Tractability | 3/5 | 1/5 | 5/5 |
| Available public data | 2/5 | 4/5 | 5/5 |
| Compute cost | Low | N/A | Negligible |
| Likelihood of publishable constraints | 1/5 | 0/5 | 5/5 |
| **Overall** | **REJECT** | **REJECT** | **PROCEED** |

---

## 4. Recommendation

**Run Track C only.** It is the only track with a direct equation chain, public data, and a defensible parameterization. Tracks A and B should be mentioned as future directions in the paper, not implemented.

Track C deliverables:
1. Consistency window plot: what f_photon is required for α/M ≈ 10^{-21} GeV^{-1} to produce β ≈ 0.30°?
2. Gaussian posterior on g_eff using published β measurements
3. Forward-model EB shape comparison against published bandpowers
4. Summary table of constraints

These can be completed in hours, not days. No MCMC pod needed.

---

## 5. What This Means for the Paper

The ΔN_eff result (consistent with zero) is honest but weak. Track C provides a second, independent observable constraint that:
- Uses the framework's central equation directly
- Has real data at >2σ significance
- Shows that the framework's parity-odd coupling is consistent (not in tension) with observed birefringence
- Identifies the photon-torsion coupling as the specific missing calculation needed for a quantitative prediction
- Provides a clean forward-looking test for LiteBIRD and CMB-S4

This materially strengthens the paper without overclaiming.
