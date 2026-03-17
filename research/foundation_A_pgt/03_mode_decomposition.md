# 03 — Torsion Mode Decomposition

**Date:** 2026-03-13
**Purpose:** Derive the spin-parity decomposition of torsion perturbations around flat spacetime and identify which modes propagate in each ghost-free PGT model.
**Status:** Derivation document

---

## 1. Setup: Linearization Around Minkowski

We expand around flat spacetime:
```
e^I_mu = delta^I_mu + epsilon h^I_mu
omega^{IJ}_mu = 0 + epsilon omega^{IJ}_mu
```
where epsilon is a formal expansion parameter. At zeroth order the torsion and curvature vanish.

At linear order:
```
T^I_{mu nu} = partial_mu h^I_nu - partial_nu h^I_mu + omega^I_{J mu} delta^J_nu - omega^I_{J nu} delta^J_mu
            = partial_mu h^I_nu - partial_nu h^I_mu + omega^I_{nu mu} - omega^I_{mu nu}
```

```
R^{IJ}_{mu nu} = partial_mu omega^{IJ}_nu - partial_nu omega^{IJ}_mu
```

We can trade the connection perturbation for the contorsion:
```
K^I_{mu nu} = omega^I_{mu nu} - stackrel{o}{omega}^I_{mu nu}(h)
```
where stackrel{o}{omega} is the Levi-Civita connection of the perturbed metric. Then:
```
T^I_{mu nu} = K^I_{nu mu} - K^I_{mu nu}
```

For the linearized analysis, we work directly with the torsion components.

---

## 2. Irreducible Decomposition in Momentum Space

In momentum space (k_mu), the torsion field T_{lambda mu nu} decomposes into Lorentz-irreducible representations. Using the standard Wigner classification for massive particles:

### Spin-0 sector (2 modes):

**0+ (scalar, from vector torsion trace):**
```
phi(k) = k^mu V_mu(k) / |k|
```
where V_mu = T^nu_{mu nu} is the torsion trace. This is a Lorentz scalar under the little group.

Couples to the trace of the energy-momentum tensor.

**0- (pseudoscalar, from axial torsion):**
```
chi(k) = k^mu A_mu(k) / |k|
```
where A_mu = (1/6) epsilon_{mu nu rho sigma} T^{nu rho sigma} is the torsion axial vector. This is a Lorentz pseudoscalar.

Couples to the axial current J^mu_5 = psi-bar gamma^mu gamma^5 psi.

### Spin-1 sector (2 modes):

**1+ (vector, from transverse V_mu):**
The transverse part of the torsion trace: V^T_mu with k^mu V^T_mu = 0. Three polarizations.

**1- (axial vector, from transverse A_mu):**
The transverse part of the torsion axial vector: A^T_mu with k^mu A^T_mu = 0. Three polarizations.

### Spin-2 sector (2 modes from tensor torsion):

**2+ (symmetric traceless tensor):**
From the tensor torsion ^(1)T, projected onto spin-2.

**2- (antisymmetric, parity-odd tensor):**
From the parity-odd component of ^(1)T.

### Component counting:
| Mode | Spin-parity | Polarizations | Source |
|------|-------------|---------------|--------|
| phi | 0+ | 1 | V_mu longitudinal |
| chi | 0- | 1 | A_mu longitudinal |
| V^T | 1+ | 3 | V_mu transverse |
| A^T | 1- | 3 | A_mu transverse |
| h^TT_{2+} | 2+ | 5 | ^(1)T symmetric traceless |
| h^TT_{2-} | 2- | 5 | ^(1)T antisymmetric |

Total: 1 + 1 + 3 + 3 + 5 + 5 = 18 torsion polarizations.

**Note:** The remaining 6 of the original 24 torsion components are pure gauge or constrained by the linearized equations.

Additionally, the metric perturbation h_mu nu contributes the massless graviton (2+, 2 polarizations) plus gauge/constraint modes.

---

## 3. Mode Propagation in Ghost-Free Models

### Model A: t_2 > 0, t_1 = t_3 = 0

**Propagating mode:** 0+ (scalar phi from torsion trace)

The linearized equation of motion for V_mu reduces to:
```
(Box - m_A^2) V_mu = kappa^2 J_mu^{(source)}
```
where m_A^2 = 1/(2 kappa^2 t_2).

Only the longitudinal mode (0+) propagates as a massive scalar. The transverse modes (1+) are constrained (non-dynamical) due to the structure of the t_2 coupling.

**Kinetic term sign:** Positive for t_2 > 0 (no ghost).

**Mass-squared sign:** Positive for t_2 > 0 (no tachyon).

**Matter coupling:** V_mu couples to the fermion vector current delta L / delta V_mu ~ psi-bar gamma_mu psi. This means the 0+ torsion mode has spin-independent interactions — it couples to baryon/lepton number, not to spin. This is cosmologically relevant: the 0+ mode acts like a massive vector boson with universal coupling.

### Model B: t_3 < 0, t_1 = t_2 = 0

**Propagating mode:** 0- (pseudoscalar chi from torsion axial part)

The linearized equation of motion for A_mu reduces to:
```
(Box - m_B^2) A_mu = kappa^2 J_mu^{5,(source)}
```
where m_B^2 = -1/(2 kappa^2 t_3) = 1/(2 kappa^2 |t_3|).

Only the longitudinal mode (0-) propagates. The transverse modes (1-) are constrained.

**Kinetic term sign:** Positive for t_3 < 0 (no ghost — the sign flip comes from the totally antisymmetric torsion squared being negative-definite: ^(3)T . ^(3)T = -6 A_mu A^mu).

**Mass-squared sign:** Positive for t_3 < 0 (no tachyon).

**Matter coupling:** A_mu couples to the fermion axial current J^mu_5 = psi-bar gamma^mu gamma^5 psi. This is the same current that appears in the minimal ECH four-fermion interaction. The 0- mode is parity-odd — it is a geometric pseudoscalar.

**This is particularly interesting for our program** because:
1. It couples to the same axial current as the ECH Holst term
2. It is parity-odd (consistent with the birefringence/parity-violation theme)
3. As a pseudoscalar, its mass could potentially be protected by a shift symmetry

### Model C: t_1 < 0, t_2 = t_3 = 0

**Propagating mode:** 2+ (massive tensor from tensor torsion)

The tensor torsion ^(1)T propagates as a massive spin-2 field.

**Ghost-free at linearized level:** Yes, for t_1 < 0.

**Major concern:** Massive spin-2 fields generically develop the Boulware-Deser ghost at the nonlinear level. The only known exception is de Rham-Gabadadze-Tolley (dRGT) massive gravity, which requires a very specific potential structure. It is not clear whether the PGT tensor torsion mode satisfies dRGT conditions.

**Assessment:** Model C is theoretically fragile. The linearized ghost-freedom may not survive at the nonlinear level. We flag this but do not close it without explicit computation.

---

## 4. Mixed Models

When multiple t_I are nonzero, the torsion modes mix. The resulting kinetic matrix must be checked for positive-definiteness.

**General result (Blagojevic-Cvetkovic 2018):**
The kinetic matrix for the (0+, 0-) sector is:
```
K = diag(t_2, -t_3)   [up to conventional signs]
```

For ghost freedom: need t_2 > 0 AND t_3 < 0 simultaneously. This is Model A + Model B combined, and the two modes decouple at the linearized level.

The (1+, 1-) sector kinetic matrix involves both t_1 and a specific combination of t_2, t_3. Ghost freedom requires additional conditions beyond just sign constraints on individual t_I.

**Practical implication:** The cleanest ghost-free theories have a single propagating torsion mode (Models A, B, or C individually). Two-mode models (A+B combined) may be viable but need explicit checking.

---

## 5. Summary: Mode Content of Ghost-Free PGT

| Model | Propagating mode | Spin-parity | Mass | Couples to | Parity-odd? | Shift-symmetry candidate? |
|-------|-----------------|-------------|------|-----------|-------------|--------------------------|
| A | Torsion trace scalar | 0+ | M_Pl/sqrt(t_2) | Vector current | No | No |
| B | Torsion axial pseudoscalar | 0- | M_Pl/sqrt(|t_3|) | Axial current | **Yes** | **Potentially** |
| C | Torsion tensor | 2+ | M_Pl/sqrt(|t_1|) | Stress-energy | No | No (Boulware-Deser risk) |
| A+B | Both 0+ and 0- | 0+, 0- | Two masses | Both currents | Partial | Partial |

**Foundation A assessment so far:**
- Ghost-free propagating torsion modes definitely exist (Question 1: YES).
- The mass spectrum is fully determined by M_Pl^2/|t_I| (Question 2: answered in next document).
- Whether any mode is cosmologically light depends on the magnitude of t_I (Question 3: next two documents).

---

## Key Derivation Notes

The decompositions above follow the standard Bargmann-Wigner analysis for massive higher-spin fields in flat spacetime. The identification of ghost-free conditions follows from requiring:

1. **Correct-sign kinetic energy:** The Hamiltonian density for each mode must be bounded from below. For the torsion modes, this translates to sign conditions on the t_I parameters (accounting for the conventions in the torsion-squared Lagrangian).

2. **Correct-sign mass term:** m^2 > 0 ensures no tachyonic instability. For each mode, this is automatically satisfied when the ghost-free condition holds in the models above.

3. **No higher-derivative pathologies:** The equation of motion for each torsion mode must be second-order (not fourth-order or higher). In the pure torsion-squared sector (r_I = 0), this is automatic because the Lagrangian is at most quadratic in first derivatives of the torsion. When curvature-squared terms are included (r_I != 0), higher derivatives can appear and require additional analysis.
