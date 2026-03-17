# Branch U: Candidate Two-Field Models

**Date:** 2026-03-17

---

## Model Zoo

### Model U1: Independent Two-ALP (Minimal)

**Fields:** φ_1 (birefringence ALP) + φ_2 (DE ALP), no direct coupling.

**Lagrangian:**
$$\mathcal{L} = -\frac{1}{2}(\partial\phi_1)^2 - V_1(\phi_1) - \frac{g_1}{4}\phi_1 F\tilde{F} - \frac{1}{2}(\partial\phi_2)^2 - V_2(\phi_2)$$

where V_i = m_i² f_{a,i}² [1 - cos(φ_i/f_{a,i})].

**Parameters:** θ_{i,1}, m_1, f_{a,1}, C_1 (birefringence) + θ_{i,2}, m_2, f_{a,2} (DE).

**Fiducial:**
- φ_1: f_{a,1} = M_Pl, m_1 ~ 10^{-31} eV (>> H_0), C_1 = 8, θ_{i,1} ~ 1.3
- φ_2: f_{a,2} = M_Pl, m_2 ~ H_0 ~ 10^{-33} eV, θ_{i,2} ~ O(1)

**Pros:** Clean separation. Each field does one job. φ_1 is identical to the spectator ALP. φ_2 is standard ultralight DE.
**Cons:** φ_2 is just Λ in disguise (m_2 ~ H_0 tuning). No interaction between fields → no new physics. Essentially spectator ALP + quintessence.

**Verdict:** WORKS BUT TRIVIAL. This resolves the tension by construction but adds nothing beyond spectator ALP + separate DE. Not publishable as a new result.

---

### Model U2: Kinetic Mixing

**Fields:** φ_1 + φ_2 with kinetic mixing term ε(∂φ_1)(∂φ_2).

**Lagrangian:**
$$\mathcal{L} = -\frac{1}{2}(\partial\phi_1)^2 - \frac{1}{2}(\partial\phi_2)^2 - \varepsilon(\partial\phi_1 \cdot \partial\phi_2) - V_1 - V_2 - \frac{g_1}{4}\phi_1 F\tilde{F}$$

**Effect:** Mass eigenstates are rotated. The lighter eigenstate (mostly φ_2) inherits a small photon coupling ~ ε × g_1. The heavier eigenstate (mostly φ_1) has coupling ~ g_1.

**For birefringence:** Total β = β_1(φ_1 rolling) + ε × β_2(φ_2 oscillating). Since φ_2 is frozen (m_2 ~ H_0), its contribution to β is ~ ε × θ_{i,2} × (tiny η). The mixing does not help — the frozen field still doesn't contribute birefringence.

**Verdict:** DOES NOT HELP. Kinetic mixing rotates the mass basis but doesn't change the rolling-vs-freezing dynamics. The birefringence still comes from φ_1 alone.

---

### Model U3: Potential Coupling (Aligned Axions)

**Fields:** φ_1 + φ_2 with aligned potentials (Kim-Nilles-Peloso mechanism).

**Potential:**
$$V = \Lambda_1^4\left[1 - \cos\!\left(\frac{\phi_1}{f_1} + \frac{\phi_2}{f_2}\right)\right] + \Lambda_2^4\left[1 - \cos\!\left(\frac{n\phi_1}{f_1} - \frac{\phi_2}{f_2}\right)\right]$$

**Effect:** The effective decay constant for one linear combination is enhanced: f_eff ~ n × f_1 (super-Planckian for n >> 1). This was designed for large-field inflation.

**For birefringence + DE:** One combination rolls (birefringence), orthogonal combination is frozen (DE). The alignment provides a natural hierarchy without tuning individual masses.

**Pros:** Provides a mechanism for m_1 >> m_2 from O(1) parameters. The mass hierarchy comes from the alignment, not from bare tuning.
**Cons:** Still requires Λ_1, Λ_2 tuning. n must be large (n ~ 30-100 for the needed hierarchy). The photon coupling is to one linear combination, not necessarily the rolling one.

**Verdict:** INTERESTING BUT OVERBUILT for one data point. Worth noting as a possibility but not worth a full calculation unless the paper needs to address the mass hierarchy question.

---

### Model U4: Quintessence + Spectator (Standard)

**Fields:** Quintessence field Q (not necessarily ALP) + spectator ALP φ.

This is Model U1 but without requiring φ_2 to be an ALP. Q could be any slow-roll quintessence field. The ALP φ is the spectator that provides birefringence.

**Pros:** Most general. Doesn't force DE to be an ALP.
**Cons:** Nothing new — this IS the spectator ALP model with any DE model underneath.

**Verdict:** THIS IS WHAT WE ALREADY HAVE. Model U4 = spectator ALP (any DE model). Not a new branch.

---

### Model U5: ALP-Assisted Vacuum Decay

**Fields:** Single ALP φ with two-minimum potential. ALP rolls to provide birefringence, then settles into metastable minimum with V_min = Λ_DE.

**Potential:**
$$V(\phi) = \Lambda_{\rm UV}^4\left[1 - \cos\!\left(\frac{\phi}{f_a}\right)\right] + \delta V(\phi)$$

where δV tilts the potential to create a metastable minimum at φ_0 with V(φ_0) = ρ_DE.

**For birefringence:** β = g_{aγ}/2 × (φ_rec - φ_0). The field rolls from θ_i to θ_0 ≈ 0 during/after recombination.
**For DE:** V(φ_0) = ρ_DE requires tuning δV.

**Pros:** Single field does both jobs if the potential shape cooperates.
**Cons:** δV is hand-tuned to give ρ_DE — same CC problem. The tilted potential breaks the shift symmetry that protects the ALP mass. Branch J (Liouville theorem) applies: the bounce cannot select the landing state.

**Verdict:** REDUCES TO CC PROBLEM. No improvement over bare Λ.

---

## Screening Summary

| Model | Resolves tension? | Natural? | New prediction? | Bounce adds? | Verdict |
|-------|------------------|----------|----------------|-------------|---------|
| U1 (independent) | YES (by construction) | NO (m_2 tuning) | NO | NO | TRIVIAL |
| U2 (kinetic mixing) | NO | — | — | — | KILLED |
| U3 (aligned) | YES | PARTIAL (n >> 1) | MAYBE (mass hierarchy) | NO | OVERBUILT |
| U4 (Q + spectator) | YES (= existing model) | — | — | — | REDUNDANT |
| U5 (vacuum decay) | YES | NO (δV tuning) | NO | NO (Branch J) | KILLED |

---

## Key Finding

**No two-field model improves on spectator ALP + Λ in a nontrivial way.**

- Models that resolve the tension do so by putting in two separate scales by hand (equivalent to what spectator ALP + Λ already does)
- Models that try to connect the fields (U2, U3) either don't help or introduce new tuning
- The bounce adds nothing to any of these models (Branch I scale separation applies to all)

The rolling-vs-freezing tension is not a bug of the spectator model — it is a **feature** that correctly identifies birefringence and DE as separate phenomena requiring separate explanations.
