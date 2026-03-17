# Paper Integration Decision

**Date:** 2026-03-13
**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology (v1.5.0)

---

## Decision Summary

| Track | Decision | Rationale |
|-------|----------|-----------|
| A — SMBH Seeds | **SAVE FOR SEPARATE PAPER** | No framework connection. Would be padding. |
| B — PBH Relics | **SAVE FOR SEPARATE PAPER** | No production mechanism. Requires substantial theoretical work first. |
| C — Parity/CMB | **INCLUDE IN CURRENT PAPER** | Direct equation chain, legitimate data, materially strengthens the paper. |

---

## Track C Integration Plan

### What to include:

1. **Consistency window result** — The spin-torsion parity-odd coupling α/M ≈ 10^{-21} GeV^{-1} is naturally consistent with observed cosmic birefringence β ≈ 0.24° (combined Planck + ACT DR6). The required photon-torsion coupling f_photon ≈ 1.7 is O(1), meaning no additional fine-tuning is needed beyond the existing framework parameters.

2. **Combined birefringence constraint** — Inverse-variance weighted combination of Eskilt 2022 (Planck) and Diego-Palazuelos & Komatsu 2025 (ACT DR6): β = 0.242° ± 0.061° (3.9σ). This strengthens the significance beyond any single measurement.

3. **EB spectrum shape consistency** — The predicted C_ℓ^{EB} = 2β(C_ℓ^{EE} − C_ℓ^{BB}) shape is consistent with uniform birefringence (the framework's isotropic prediction), as opposed to scale-dependent alternatives.

### Where in the paper:

- **Discussion section** (after the existing birefringence paragraph): Add ~2-3 paragraphs on the consistency window analysis
- **New figure**: `consistency_window.pdf` showing f_photon vs β with observational bands
- **Possibly**: `beta_posterior.pdf` showing the combined Planck + ACT constraint
- **Discussion text**: "The framework's parity-odd coupling scale [(α/M)·M_Pl ≈ 10^{-2}] requires a photon-torsion vertex factor f_photon ≈ 1.7 to match the combined birefringence measurement β = 0.242° ± 0.061°. This O(1) value is consistent with a generic one-loop photon-torsion vertex, though the explicit calculation remains an open problem."

### Language constraints:

- **DO say:** "The framework's parity-odd coupling is naturally consistent with observed cosmic birefringence."
- **DO say:** "The required photon-torsion coupling is O(1), meaning no additional fine-tuning is needed."
- **DO say:** "This is a consistency check, not a prediction — the photon-torsion coupling has not been derived."
- **DO NOT say:** "The framework predicts the observed birefringence angle."
- **DO NOT say:** "The consistency confirms the model."

### What this adds to the paper:

1. **A second independent observable** beyond ΔN_eff — while ΔN_eff ≈ 0 is honest but weak, the birefringence consistency is a positive result (O(1) coupling, no fine-tuning).
2. **Quantitative content** for the birefringence discussion, which currently says only "qualitatively consistent."
3. **A specific testable prediction** — once the photon-torsion coupling is calculated, f_photon ≈ 1.7 ± 0.4 becomes a concrete target.
4. **Combined significance** — 3.9σ for cosmic birefringence from two independent experiments.

### Honesty requirements:

The consistency window analysis must be clearly labeled as:
- Consistency check, not prediction
- Conditional on the unknown C_0 geometric factor
- Subject to the calibration caveats (instrumental polarization angle degeneracy)
- Explicitly noting that SPIDER's ~7σ is excluded from the primary fit due to calibration degeneracy

---

## Tracks A and B — Future Work Mentions

### Track A in the paper:
Mention in the Future Directions section: "High-redshift SMBH seed formation provides a potential observational window, but the framework's torsion effects are negligible at astrophysical densities; establishing a connection requires deriving a modified primordial perturbation spectrum from the quantum bounce."

### Track B in the paper:
Mention in the Future Directions section: "Primordial black hole production from enhanced curvature perturbations during or immediately after the bounce transition remains unexplored; a full perturbation calculation through the LQC bounce with spin-torsion effects would determine whether PBH-like compact seeds are produced at observationally interesting abundances."

---

## Integration Timeline

Track C integration should happen:
1. **After** planck_only freezes and its results are integrated (~March 19-20)
2. **Before** the final referee-style review (~March 21)
3. **In the same version bump** as the planck_only integration (v1.6.0 or v1.7.0)

This ensures a clean, single update pass rather than multiple small edits.
