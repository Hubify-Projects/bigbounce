# Phase 2A — Strong-Coupling Scale Analysis

**Date:** 2026-03-13
**Status:** Original analysis

---

## 1. Question

At what energy scale does the perturbative expansion of Model B break
down? Does this scale fall below cosmologically relevant energies at
large |t_3|?

---

## 2. Identifying the Strong-Coupling Scale

For a theory with a massive vector field A_mu coupled to matter with
strength g_eff and self-interacting through gravity, the strong-coupling
scale Lambda_sc is determined by the lowest scale at which loop
corrections become O(1).

### 2a. Matter-sector loops

The 1-loop correction to the A_mu propagator from fermion loops scales as:

```
Pi(k^2) ~ g_eff^2 k^2 / (16 pi^2) ~ k^2 / (16 pi^2 M_Pl^2 |t_3|)
```

This becomes O(1) at:

```
Lambda_sc^(matter) ~ 4 pi M_Pl sqrt(|t_3|)
```

This RISES with |t_3|. At |t_3| = 10^58, Lambda_sc^(matter) ~ 10^30 M_Pl.

### 2b. Gravitational loops

The graviton loop correction to the A_mu propagator scales as:

```
Pi^(grav)(k^2) ~ kappa^2 k^4 / (16 pi^2) ~ k^4 / (16 pi^2 M_Pl^2)
```

This becomes O(1) at:

```
Lambda_sc^(grav) ~ sqrt(4 pi) M_Pl ~ M_Pl
```

This is independent of |t_3|. The gravitational strong-coupling scale is
always M_Pl, as expected — this is just the statement that quantum gravity
becomes strongly coupled at the Planck scale regardless of the torsion
sector.

### 2c. Torsion self-interaction loops

The A_mu self-interaction through the torsion-squared term generates loop
corrections. The relevant vertex comes from expanding the torsion-squared
term beyond quadratic order (which requires going beyond the linearized
theory). The cubic and quartic vertices in the canonical normalization are:

```
g_3 ~ kappa / sqrt(|t_3|) ~ 1 / (M_Pl sqrt(|t_3|))
g_4 ~ kappa^2 / |t_3| ~ 1 / (M_Pl^2 |t_3|)
```

Both are suppressed at large |t_3|. The self-interaction strong-coupling
scale is:

```
Lambda_sc^(self) ~ (16 pi^2 / g_3^2)^{1/2} ~ 4 pi M_Pl |t_3|^{1/4}
```

This also rises with |t_3|.

---

## 3. The Hierarchy of Scales

Collecting all scales at generic |t_3|:

```
m_B << M_Pl < Lambda_sc^(grav) ~ M_Pl < Lambda_sc^(self) < Lambda_sc^(matter)
```

The controlling scale is always M_Pl (from gravitational loops). This
is not specific to Model B — it is the universal statement that any
EFT containing gravity has a cutoff at M_Pl.

At |t_3| = 10^58 (DE-scale mass):

| Scale | Value | Ratio to m_B |
|-------|-------|-------------|
| m_B | ~7 meV | 1 |
| M_Pl | ~1.2e28 eV | ~10^30 |
| Lambda_sc^(self) | ~10^7 M_Pl | ~10^37 |
| Lambda_sc^(matter) | ~10^30 M_Pl | ~10^60 |

**No strong-coupling scale falls below M_Pl.** The theory is weakly
coupled throughout the entire sub-Planckian regime.

---

## 4. Comparison with Problematic Theories

To appreciate why Model B at large |t_3| is NOT in trouble, compare with
theories that DO have a strong-coupling problem:

### Massive gravity (dRGT)

In massive gravity with mass m_g:

```
Lambda_sc = (m_g^2 M_Pl)^{1/3} ~ (H_0^2 M_Pl)^{1/3} ~ 10^{-13} eV
```

This is absurdly low — solar system tests already probe above this scale.
The Vainshtein mechanism is required to save the theory. This is a genuine
strong-coupling problem.

### Massive spin-2 in PGT (Model C)

The Boulware-Deser ghost potentially appears at the nonlinear level. Even
if tuned away, the strong-coupling scale for massive spin-2 is parametrically:

```
Lambda_sc^(BD) = (m_C^4 M_Pl)^{1/5}
```

which at m_C ~ meV gives Lambda_sc ~ 10^{-8} eV. This IS a problem.

### Model B (0- pseudoscalar)

```
Lambda_sc = M_Pl (independent of |t_3|, or rising)
```

No problem. The spin-0 nature of the pseudoscalar mode eliminates the
Boulware-Deser obstruction and the Vainshtein issue. There is no scale
at which perturbation theory fails below M_Pl.

---

## 5. Does Large |t_3| Affect Gravitational Dynamics?

One might worry that the large torsion-squared coupling backreacts on
the gravitational sector at some finite energy below M_Pl. This does not
happen because:

1. **The torsion mode is decoupled.** Its energy-momentum tensor
   contributes to gravity, but its stress-energy is suppressed by g_eff^2
   relative to minimally-coupled matter. At large |t_3|, the torsion
   contribution to the gravitational field equations is negligible unless
   the field has a large classical expectation value (initial conditions).

2. **The graviton propagator is not modified.** At the linearized level,
   the graviton propagator receives corrections from torsion loops that
   scale as:

   ```
   delta D_graviton ~ kappa^2 m_B^2 / (16 pi^2) ~ 1 / (16 pi^2 |t_3|)
   ```

   These corrections VANISH at large |t_3|. The gravitational sector
   becomes MORE standard (more GR-like) as |t_3| increases.

3. **No new light states appear.** The only propagating torsion mode is
   the single 0- pseudoscalar. There are no additional light states that
   emerge at large |t_3| to modify the gravitational dynamics.

---

## 6. The EFT Validity Assessment

| EFT criterion | Status at large |t_3| |
|---------------|---------------------|
| Perturbative unitarity | SATISFIED — s_unit >> M_Pl^2 |
| Loop expansion parameter | SMALL — g_eff^2/(16 pi^2) << 1 |
| Strong-coupling scale | ABOVE M_Pl for all torsion interactions |
| Graviton modifications | SUPPRESSED by 1/|t_3| |
| New states below cutoff | NONE |
| Cutoff stability | CONTROLLED — cutoff is M_Pl, universal |

**The EFT is under complete perturbative control at all sub-Planckian
energies for any value of |t_3|.**

---

## 7. Summary

**Large |t_3| does not produce a strong-coupling problem.** The strong-
coupling scale rises (or stays at M_Pl) as |t_3| increases. The theory
becomes more weakly coupled, more perturbative, and more GR-like.

This is good for consistency but devastating for phenomenology. A theory
that becomes arbitrarily weakly coupled at the parameter values needed
for cosmological relevance is a theory that predicts nothing cosmologically
distinctive.

The strong-coupling analysis reinforces the finding of Document 02:
**large |t_3| is a decoupling limit.** The theory is healthy but empty.
