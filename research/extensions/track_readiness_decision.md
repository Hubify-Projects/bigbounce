# Track Readiness Decision

**Date:** 2026-03-13
**Basis:** Model-to-observable maps + dataset audit

---

## Decision Matrix

| Track | Status | Justification |
|-------|--------|---------------|
| A — SMBH Seeds | **FUTURE WORK ONLY** | No direct framework connection. Torsion effects vanish at astrophysical densities (suppressed by ρ/ρ_Pl ≈ 10^{-83}). Would be standard astrophysics with a spin-torsion label. |
| B — PBH Relics | **FUTURE WORK ONLY** | No production mechanism. Framework creates baby universes inside BHs, not PBHs. Missing calculation: perturbation spectrum through the quantum bounce. LQC literature suggests power suppression, not enhancement. |
| C — Parity/CMB | **READY FOR CONSTRAINT ANALYSIS** | Direct equation chain (α/M → parity-odd operator → birefringence). One clean gap (photon-torsion vertex) that can be parameterized. Published Gaussian constraints from Planck, ACT, SPIDER. Negligible compute cost. |

---

## Track A — Detailed Rejection Rationale

1. The modified Friedmann equation H² = (8πG/3)ρ[1 − ρ/ρ_crit] deviates from GR only when ρ → 0.27 ρ_Pl. SMBH seeds form at ρ ~ 10^{-83} ρ_Pl. The correction term is literally 10^{-83}.
2. The four-fermion contact interaction coupling is suppressed by (M_W/M_Pl)² ~ 10^{-34} relative to weak interactions.
3. ΔN_eff ≈ 0 from MCMC means no significant modification to early-universe expansion.
4. Any "constraint" would be constraining standard cosmological parameters through an unnecessarily indirect route.
5. JWST high-z SMBH data is real and interesting, but tells us nothing about spin-torsion physics.

## Track B — Detailed Rejection Rationale

1. The bounce mechanism creates new universes inside BHs; it does not create PBHs in our universe.
2. PBH production requires enhanced curvature perturbations on specific scales during inflation. The framework does not modify the inflationary perturbation spectrum.
3. No forward model exists: there is no function f(framework parameters) → PBH abundance.
4. PBH constraint datasets (PBHbounds repository) are excellent but uninformative without a production mechanism.
5. Theoretical work needed before any phenomenology is possible: full scalar perturbation evolution through the LQC bounce with spin-torsion effects.

## Track C — Detailed Approval Rationale

1. **Direct equation chain:** α/M → parity-odd operator → qualitative birefringence motivation → β
2. **One clean gap:** The photon-torsion coupling f_photon is unknown, but can be parameterized as g_eff ≡ (α/M) × f_photon. This is honest and transparent.
3. **Public data:** At least 3 independent β measurements with published error bars, directly usable as Gaussian constraints:
   - Eskilt 2022: β = 0.30° ± 0.11° (Planck, superseding Minami & Komatsu 2020)
   - Diego-Palazuelos & Komatsu 2025: β = 0.215° ± 0.074° (ACT DR6)
   - SPIDER 2025: combined total rotation ~7σ (calibration caveats apply)
4. **Negligible compute:** This is Gaussian constraint sampling on a laptop. No pod needed.
5. **Publishable output:** Consistency window plot, posterior on g_eff, forward-model EB shape check.
6. **Honest strength:** Shows that the framework's parity-odd coupling is *consistent with* observed birefringence (O(1) f_photon required), which is a non-trivial positive result.

---

## What Would Change These Decisions?

- **Track A → READY** if: Someone derives a modified primordial perturbation spectrum from the bounce that specifically enhances density fluctuations at SMBH seed scales.
- **Track B → READY** if: A full perturbation calculation through the LQC bounce with spin-torsion effects shows enhanced power on specific scales.
- Neither is likely to happen within the current paper's timeline.
