# Priority Ranking: Top Targets

**Date:** 2026-03-16

---

## Ranking Criteria

1. **Novelty:** Does this produce a result not already in the literature?
2. **Tractability:** Can it be completed analytically or with modest numerics?
3. **Observational payoff:** Does it connect to real data?
4. **Chance of success:** Given what Branches A--O established, how likely
   is a positive outcome?

---

## Rank 1: Torsion Relic Cosmology (Channels 4+5)

**Target:** Calculate the energy density of the propagating torsion mode
after the PGT bounce, track its cosmological evolution, and determine
BBN/CMB constraints on m_T.

### Novelty: HIGH

The "cosmological moduli problem" for PGT torsion has not been worked out
in the literature. The standard treatments of PGT cosmology focus on the
modified Friedmann equation and perturbation spectra, not on the relic
torsion energy density. This would be a genuinely new result.

### Tractability: HIGH

The calculation requires:
1. Torsion field equation on the bounce background (linear ODE)
2. Initial conditions at the bounce (set by the bounce solution)
3. Post-bounce evolution (oscillation + decay in expanding universe)
4. Standard BBN/N_eff constraints applied to torsion energy fraction

This is analytically tractable with standard cosmological tools.
No MCMC needed. No numerical PDE solving needed.

### Observational payoff: MEDIUM-HIGH

BBN constraints (Delta N_eff < 0.2--0.4 at 95% CL from Planck+BBN) and
CMB constraints (N_eff = 2.99 +/- 0.17 from Planck 2018) are precise.
If the torsion energy fraction is significant, these give a sharp
constraint on m_T.

Spectral distortion constraints (FIRAS: mu < 9 x 10^{-5}; PIXIE goal:
mu < 10^{-8}) provide an additional window if torsion decays in the
distortion epoch.

### Chance of success: MEDIUM

Two scenarios:

**(A) Torsion energy fraction ~ O(1) at the bounce:**
The torsion is a massive relic that dominates the energy budget, decays
gravitationally, and is subject to the standard "cosmological moduli problem."
This gives STRONG constraints: m_T must be large enough for the torsion to
decay before BBN (m_T > ~10^9 GeV from the decay rate estimate). This
would be a genuine, publishable constraint.

**(B) Torsion energy fraction ~ (m_T/M_Pl)^2:**
The torsion is a sub-dominant perturbation. Constraints are weak
(Delta N_eff ~ (m_T/M_Pl)^4 or worse). This gives no useful bound.

The outcome hinges on one question: **how much energy does the bounce
deposit in the torsion field?** This is the gating calculation.

### Risk assessment

- If scenario (A): publishable constraint, clear parameter bound
- If scenario (B): null result, another closure
- Either way: the calculation is clean and the answer is definitive

**RANK 1 because the risk/reward ratio is the best available. Even
a null result is informative and publishable.**

---

## Rank 2: Pre-Bounce Model + Scalar Predictions (Channel 3)

**Target:** Pair the PGT bounce with a specific contraction mechanism
(ekpyrotic or matter contraction) and compute the full scalar prediction
(n_s, running, r, f_NL) for comparison with CMB data.

### Novelty: MEDIUM

Ekpyrotic and matter-bounce scalar spectra are well-studied. The PGT
bounce is transparent (T(k) = 1), so the predictions are identical to
those with any other symmetric bounce. The novelty is limited to
stating this explicitly and identifying which contraction models are
compatible.

### Tractability: HIGH

The scalar spectrum calculation is standard. The bounce contributes
nothing (T = 1). This is essentially a literature review + consistency
check.

### Observational payoff: LOW-MEDIUM

The predictions constrain the pre-bounce mechanism, NOT the PGT bounce.
Any result applies equally to LQC, EC, or any other time-symmetric bounce.

### Chance of success: LOW

Because the bounce is transparent, this channel cannot distinguish PGT
from any other bounce model. The "success" would be finding a compatible
contraction model, but this tests the contraction model, not PGT.

**RANK 2 because it is tractable and provides context, but cannot
produce a PGT-specific result.**

---

## Rank 3: Full GW Spectrum + Detector Map (Channel 1, refined)

**Target:** Compute the complete GW energy density spectrum including
all sub-leading effects (anisotropic stress, neutrino free-streaming,
QCD phase transition imprint) and overlay with all detector curves.

### Novelty: LOW

Branch M already established the spectrum shape and the 10^{17} gap.
Adding sub-leading corrections does not change the conclusion.

### Tractability: HIGH

Standard transfer function calculation.

### Observational payoff: ZERO

The signal is 10^{17} below any detector. Sub-leading corrections
of O(10%) do not matter.

### Chance of success: ZERO

The gap is 17 orders of magnitude. No refinement closes it.

**RANK 3 (last) because the answer is already known: undetectable.
Further calculation is academic completeness, not phenomenology.**

---

## Channels NOT Ranked (Already Dead)

| Channel | Why not ranked |
|---------|---------------|
| Torsion oscillation GW (2a) | (m_T/M_Pl)^3 -- worse than vacuum |
| Parametric resonance (2b) | Too brief, too weak |
| Phase transition GW (2c) | Not bounce-specific |
| Graviton N_eff (6a) | (m_T/M_Pl)^2 suppression |
| Modified expansion (8) | Exponentially small at observable epochs |

---

## Blunt Assessment

**There is exactly one genuinely promising target: the torsion relic
cosmology calculation (Rank 1).** It is the only channel that is
simultaneously (a) bounce-specific (the torsion mode IS the PGT ingredient),
(b) potentially constrainable (BBN/CMB), (c) not already computed, and
(d) has a definite gating question that can be answered.

If the torsion energy fraction turns out to be O(1) at the bounce, the
program has a real positive center: PGT bounce phenomenology becomes
"constrained bouncing cosmology with a massive torsion relic." If the
fraction is (m_T/M_Pl)^2, the program is effectively closed -- no
observable channel survives.

**The entire Branch P program reduces to one calculation: the torsion
energy fraction at the PGT bounce.**
