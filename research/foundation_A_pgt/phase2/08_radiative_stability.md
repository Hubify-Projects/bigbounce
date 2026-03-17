# Phase 2B — Radiative Stability of the 0- Torsion Mass

**Date:** 2026-03-13
**Status:** Original analysis (expanding on Section 8 of Document 07)

---

## 1. The Question

If we set m_B^2 = M_Pl^2 / (16 pi |t_3|) at tree level with |t_3| >> 1,
does this mass survive quantum corrections? Or do loops generate
delta m_B^2 ~ M_Pl^2 / (16 pi^2), destroying the hierarchy?

---

## 2. Power Counting

Model B in the canonical normalization has the structure:

```
L = -(1/4) F^2 - (1/2) m_B^2 A^2 + g_eff A_mu J_5^mu
    + (kappa/2) h_{mu nu} T^{mu nu} + ...
```

where:
- g_eff ~ 1/(M_Pl sqrt(|t_3|)) is the matter coupling
- kappa = 1/M_Pl is the gravitational coupling
- h_{mu nu} is the graviton perturbation
- T^{mu nu} is the stress-energy tensor

The mass receives corrections from three sources:

---

## 3. Source 1: Graviton Loops (DOMINANT)

The 1-loop graviton contribution to the A_mu self-energy:

```
[diagram: A_mu -- graviton loop -- A_mu]
```

By dimensional analysis, with the graviton coupling kappa:

```
delta m_B^2 |_{grav} ~ kappa^2 Lambda_UV^4 / (16 pi^2)
                      ~ Lambda_UV^4 / (16 pi^2 M_Pl^2)
```

With the natural cutoff Lambda_UV = M_Pl:

```
delta m_B^2 |_{grav} ~ M_Pl^2 / (16 pi^2) ~ (7.7 x 10^{17} GeV)^2
```

This is **independent of |t_3|.** It is the universal gravitational
contribution to any field mass. It destroys any hierarchy m_B << M_Pl
unless a symmetry cancels it.

### Comparison with tree-level mass

```
delta m_B^2 / m_B^2 ~ |t_3| / (16 pi^2)
```

At |t_3| = 10^58: the correction is 10^57 times larger than the
tree-level mass squared. This is a fine-tuning of 1 part in 10^57.

---

## 4. Source 2: Fermion Loops (SUBDOMINANT)

The 1-loop fermion contribution:

```
[diagram: A_mu -- fermion loop -- A_mu]
```

```
delta m_B^2 |_{ferm} ~ g_eff^2 Lambda_UV^2 / (16 pi^2)
                      ~ Lambda_UV^2 / (16 pi^2 M_Pl^2 |t_3|)
```

With Lambda_UV = M_Pl:

```
delta m_B^2 |_{ferm} ~ M_Pl^2 / (16 pi^2 |t_3|) ~ m_B^2 / (16 pi^2)
```

This correction is **proportional to m_B^2** — it is a small
multiplicative renormalization, not a destabilizing additive correction.

**The fermion loop respects the mass hierarchy.** This is because the
fermion coupling is suppressed by the same 1/sqrt(|t_3|) that suppresses
the mass. This is a consequence of the decoupling structure:
```
m_B^2 ~ M_Pl^2 / |t_3|
g_eff^2 ~ 1 / (M_Pl^2 |t_3|)
=> g_eff^2 M_Pl^2 ~ 1/|t_3| ~ m_B^2/M_Pl^2
```

If ONLY fermion loops existed, the mass would be technically natural.
But graviton loops dominate and destroy this.

---

## 5. Source 3: Torsion Self-Interaction Loops

The torsion self-coupling (from expanding the PGT action beyond
quadratic order) contributes:

```
delta m_B^2 |_{self} ~ g_3^2 Lambda_UV^2 / (16 pi^2)
```

where g_3 ~ 1/(M_Pl sqrt(|t_3|)) is the cubic self-coupling. This gives:

```
delta m_B^2 |_{self} ~ M_Pl^2 / (16 pi^2 |t_3|) ~ m_B^2 / (16 pi^2)
```

Again proportional to m_B^2 — the self-interaction loop also respects
the hierarchy. Only the graviton loop breaks it.

---

## 6. The 't Hooft Naturalness Test

A mass m is technically natural if setting m = 0 increases the symmetry
of the theory ('t Hooft 1979).

**Test for Model B:** Set m_B = 0 (equivalently, |t_3| -> infinity).

- The matter coupling g_eff -> 0: the torsion decouples from fermions.
- The torsion self-coupling g_3 -> 0: the torsion self-interaction
  vanishes.
- The torsion kinetic term survives with infinite normalization.
- The graviton coupling kappa is UNCHANGED.

Does m_B = 0 enhance a symmetry?

- A massless vector with vanishing coupling to matter and to itself is
  a free field. But a free massive vector has 3 DOF while a free
  massless vector (without gauge invariance) also has 3 DOF in PGT.
  Setting m_B = 0 does NOT restore gauge invariance (there is no U(1)
  gauge symmetry in PGT to restore).

- Without a gauge symmetry restoration at m_B = 0, the mass is NOT
  technically natural in the 't Hooft sense.

**The mass is not technically natural.** Graviton loops will regenerate
it at O(M_Pl / (4 pi)) regardless of the tree-level value.

---

## 7. Could the Graviton Loop Be Avoided?

Three scenarios where the graviton loop might not destabilize the mass:

### 7a. If the UV cutoff is much below M_Pl

If new physics enters at Lambda_UV << M_Pl, the graviton loop gives:

```
delta m_B^2 ~ Lambda_UV^4 / (16 pi^2 M_Pl^2)
```

For delta m_B^2 < m_B^2 (i.e., no fine-tuning), we need:

```
Lambda_UV < (m_B M_Pl)^{1/2} (4 pi)^{1/2}
```

At m_B = meV: Lambda_UV < ~10^7 GeV (~ 10 PeV).

This is a very specific intermediate scale. There is no known physics
at this scale in PGT.

### 7b. If SUSY cancels the graviton loop

In supergravity, the gravitino loop cancels the graviton loop (up to
SUSY-breaking effects). The residual is:

```
delta m_B^2 ~ m_{3/2}^2 / (16 pi^2)
```

where m_{3/2} is the gravitino mass. For this to not destabilize m_B:

```
m_{3/2} < m_B (4 pi) ~ meV * 4 pi ~ 10 meV
```

A gravitino mass at the meV scale would require SUSY breaking at
F ~ (meV * M_Pl)^{1/2} ~ 10^7 GeV — again the same intermediate scale.
This is extremely low-scale SUSY breaking, in strong tension with
collider bounds (which require sfermion masses > TeV, giving
m_{3/2} > TeV in standard mediation).

### 7c. If the cosmological constant cancels the graviton loop

This would require the CC fine-tuning to also solve the torsion mass
hierarchy — converting two problems into one. There is no known
mechanism for this.

**All three scenarios are speculative.** None is available within
standard PGT.

---

## 8. Comparison with Other Mass Hierarchies

| Field | Mass | Hierarchy | Protection mechanism |
|-------|------|-----------|---------------------|
| Higgs boson | 125 GeV | m_H/M_Pl ~ 10^{-17} | SUSY? Compositeness? (unsolved) |
| Axion (QCD) | ~10^{-5} eV | m_a/f_a ~ 10^{-17} | Shift symmetry (demonstrated) |
| Neutrinos | ~0.05 eV | m_nu/v ~ 10^{-13} | Seesaw mechanism (demonstrated) |
| Photon | < 10^{-18} eV | exact | U(1) gauge symmetry (demonstrated) |
| Graviton | 0 | exact | Diffeomorphism invariance (demonstrated) |
| **Model B** | **~meV** | **m_B/M_Pl ~ 10^{-31}** | **None demonstrated** |

The Model B hierarchy is among the worst in physics — 10^{-31} with
no known protection mechanism.

---

## 9. Summary

| Loop source | delta m_B^2 | Relative to m_B^2 | Respects hierarchy? |
|-------------|-----------|-------------------|-------------------|
| Graviton | M_Pl^2/(16 pi^2) | ~10^57 at meV | **NO** |
| Fermion | m_B^2/(16 pi^2) | ~0.006 | YES |
| Self-interaction | m_B^2/(16 pi^2) | ~0.006 | YES |

**The graviton loop dominates and destroys the mass hierarchy.**

The fermion and self-interaction loops are harmlessly small — they
respect the decoupling structure. But the graviton loop is universal
and independent of |t_3|. It regenerates a Planck-scale mass for A_mu
at 1-loop, requiring fine-tuning of 1 part in 10^57 to maintain
m_B ~ meV.

**The 0- torsion mass is not radiatively stable.** This is the same
hierarchy problem that afflicts every light field coupled to gravity,
with no torsion-specific resolution.
