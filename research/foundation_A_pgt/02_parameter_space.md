# 02 — PGT Parameter Space and Ghost-Free Conditions

**Date:** 2026-03-13
**Purpose:** Catalog the known ghost-free and tachyon-free conditions on PGT coupling constants from the literature.
**Status:** Literature compilation with analysis

---

## 1. The Parameter Space

From 01_pgt_action_definition.md, the quadratic PGT action has 9 free coupling constants (setting a_0 = 1):

| Parameter | Role | Sector |
|-----------|------|--------|
| t_1 | Tensor torsion kinetic term | ^(1)T |
| t_2 | Vector torsion kinetic term | ^(2)T |
| t_3 | Axial-vector torsion kinetic term | ^(3)T |
| r_1 | Kretschner-like curvature^2 | Curvature |
| r_2 | Ricci-squared | Curvature |
| r_3 | R-squared | Curvature |
| r_4 | Parity-odd curvature^2 | Curvature (P-odd) |
| r_5 | Parity-odd Ricci | Curvature (P-odd) |
| r_6 | Parity-odd scalar | Curvature (P-odd) |

Plus Lambda_0 (bare cosmological constant), which we set to zero for the linearized spectrum analysis.

---

## 2. Spin-Parity Content of the Torsion Sector

Around flat Minkowski spacetime, the torsion perturbation decomposes into irreducible Lorentz representations. The 24-component torsion field contains:

| Mode | Spin-Parity | Components | Source |
|------|-------------|------------|--------|
| Scalar S+ | 0+ | 1 | From ^(2)T (trace) |
| Scalar S- | 0- | 1 | From ^(3)T (axial) |
| Vector V+ | 1+ | 3 | From ^(1)T mixing with ^(2)T |
| Vector V- | 1- | 3 | From ^(1)T mixing with ^(3)T |
| Tensor | 2+ | 5 | From ^(1)T |
| Tensor | 2- | 5 | From ^(1)T |

Plus the massless graviton (2+, 2 components) from the metric sector.

**Note:** Not all of these propagate for generic parameter values. Whether a given mode propagates depends on the signs and values of the coupling constants.

---

## 3. Ghost-Free Conditions: Literature Summary

### 3.1 Sezgin & van Nieuwenhuizen (1980)

The foundational particle-spectrum analysis. They decomposed the PGT action around flat space and identified ghost-free parameter regions.

**Key result:** For a "Yang-Mills-like" PGT action (only curvature-squared terms, specific signs), they found ghost-free spectra with massive spin-2 and spin-0 torsion modes. However, most generic parameter choices produce ghosts.

**Specific ghost-free model (SvN Class I):**
```
r_1 > 0,   r_2 = -4 r_1,   r_3 = r_1
```
with all torsion couplings zero (t_I = 0). This gives a massive spin-2 mode only (no spin-0 or spin-1 torsion).

**Problem:** Spin-2 massive modes in gravity generically suffer from the Boulware-Deser ghost at the nonlinear level (cf. de Rham-Gabadadze-Tolley massive gravity). The linearized analysis may not be sufficient.

### 3.2 Yo & Nester (1999, 2002)

Hamiltonian (3+1) analysis of PGT. More rigorous than the Sezgin-van Nieuwenhuizen particle-spectrum approach because it counts constraints and identifies primary/secondary constraint chains.

**Key results:**
- Confirmed that most of the PGT parameter space has ghost degrees of freedom.
- Identified specific constraint bifurcation surfaces where extra constraints remove ghosts.
- For the torsion-squared sector alone (r_I = 0), viable models exist with:
  - Pure axial-vector torsion: t_3 != 0, t_1 = t_2 = 0
  - Pure vector torsion: t_2 != 0, t_1 = t_3 = 0
  - But mixed models (multiple t_I nonzero) are generically ghostly unless on special surfaces.

### 3.3 Nikiforova, Randjbar-Daemi & Rubakov (2009)

Studied "infrared modified gravity with propagating torsion" — directly relevant to our cosmological question.

**Key results:**
- Focused on the torsion-squared sector with small masses (IR-relevant).
- Found that a massive spin-0+ torsion mode can be ghost-free and tachyon-free.
- **Specific ghost-free model (NRR):**
  ```
  t_2 > 0, t_1 = t_3 = 0, r_I = 0
  ```
  Yields a single massive spin-0+ torsion mode with mass:
  ```
  m_0^2 = 1 / (2 kappa^2 t_2)
  ```
- The spin-0+ mode couples to matter through the torsion trace, which is sourced by the fermion vector current (not the axial current).
- For t_2 ~ O(1) (in Planck units), the mass is m_0 ~ M_Pl. To get m_0 ~ H_0 requires t_2 ~ (M_Pl/H_0)^2 ~ 10^{60} — an enormous dimensionless coupling.

**This is a critical observation.** See Section 5 below.

### 3.4 Karananas (2015)

Systematic unitarity analysis using optical theorem and forward scattering amplitude positivity.

**Key results:**
- Mapped out the full ghost-free and tachyon-free region of the {t_1, t_2, t_3} space at fixed curvature couplings.
- Confirmed that only isolated submanifolds of the parameter space are viable.
- Emphasized that unitarity constraints from tree-level graviton-torsion scattering amplitudes are more restrictive than the naive Hamiltonian no-ghost conditions.

### 3.5 Blagojevic & Cvetkovic (2018)

Most complete Hamiltonian analysis to date.

**Key results for the torsion sector (curvature-squared terms set to zero):**

**Ghost-free models (torsion-squared only):**

| Model | Parameters | Propagating modes | Mass |
|-------|-----------|-------------------|------|
| BC-I | t_2 > 0, t_1 = t_3 = 0 | 0+ (scalar) | m^2 = 1/(2 kappa^2 t_2) |
| BC-II | t_3 < 0, t_1 = t_2 = 0 | 0- (pseudoscalar) | m^2 = -1/(2 kappa^2 t_3) |
| BC-III | t_1 < 0, t_2 = t_3 = 0 | 2+ (tensor, massive) | m^2 = -1/(2 kappa^2 t_1) |

**Constraints:**
- Only **single-mode** models are ghost-free in the pure torsion-squared sector.
- Turning on multiple t_I simultaneously introduces ghost degrees of freedom on generic surfaces.
- Models with curvature-squared terms can sometimes cure the ghosts from the torsion sector, but this introduces new higher-derivative pathologies.

### 3.6 Lin, Hobson & Sherrill (2019)

Systematic computational scan of the full 9-parameter space.

**Key results:**
- Confirmed the Blagojevic-Cvetkovic ghost-free models.
- Found additional ghost-free models when both torsion-squared and curvature-squared terms are present, but these typically have masses set by the curvature-squared coupling scale (near M_Pl).
- **No model found with naturally light torsion masses** in the scan.

---

## 4. Summary of Ghost-Free Parameter Regions

From the literature, the cleanest ghost-free models with propagating torsion are:

| Label | Surviving mode | Spin-parity | Ghost-free condition | Mass formula |
|-------|---------------|-------------|---------------------|--------------|
| Model A (scalar) | Torsion trace | 0+ | t_2 > 0, t_1 = t_3 = 0 | m^2 = 1/(2 kappa^2 t_2) |
| Model B (pseudoscalar) | Torsion axial | 0- | t_3 < 0, t_1 = t_2 = 0 | m^2 = -1/(2 kappa^2 t_3) |
| Model C (tensor) | Torsion tensor | 2+ | t_1 < 0, t_2 = t_3 = 0 | m^2 = -1/(2 kappa^2 t_1) |

**Critical pattern:** In every ghost-free case, the mass is set by:
```
m^2 ~ 1 / (kappa^2 |t_I|) = M_Pl^2 / |t_I|
```

For a Planck-mass mode: |t_I| ~ O(1).
For a cosmologically light mode (m ~ H_0): |t_I| ~ (M_Pl/H_0)^2 ~ 10^{60}.

---

## 5. The Mass Hierarchy Problem for Cosmological Torsion

This is the central technical obstacle for Foundation A.

### The problem:
Ghost-free propagating torsion modes have masses given by m^2 = M_Pl^2 / |t_I|. To obtain a cosmologically relevant mass m ~ H_0 ~ 10^{-33} eV, we need:

```
|t_I| ~ (M_Pl / H_0)^2 ~ (2.4 x 10^{18} GeV / 1.5 x 10^{-33} eV)^2 ~ 10^{122}/4 ~ 10^{61}
```

This is an enormous dimensionless coupling constant. It is not forbidden by any symmetry, but it reintroduces a fine-tuning problem comparable to (though distinct from) the cosmological constant problem:

**Instead of asking "why is Lambda ~ 10^{-122} M_Pl^4?", we would ask "why is t_I ~ 10^{61}?"**

### Possible resolutions:

1. **Accept the hierarchy as parametric.** The torsion mass is a free parameter; its smallness is an input, not a prediction. This is no worse than quintessence.

2. **Radiative stability.** If the torsion mass is protected by a symmetry (e.g., a shift symmetry in the pseudoscalar case 0-), quantum corrections may not destabilize it. This is analogous to axion mass protection by a Peccei-Quinn symmetry.

3. **Dynamical relaxation.** A cosmological mechanism (e.g., torsion condensation during inflation) could dynamically select a small effective mass.

4. **Not all masses need to be ~ H_0.** A torsion mode with m ~ meV (the dark energy scale) or m ~ eV (relevant for structure formation) could also have cosmological effects, requiring only |t_I| ~ 10^{40}–10^{50}. Still large, but potentially more natural.

5. **The mass could be generated by a different mechanism.** If the torsion mode gets its mass from a symmetry-breaking potential (as in massive gauge theories), the mass is not simply M_Pl^2/t_I but depends on the VEV and coupling structure. This requires going beyond the quadratic PGT action.

### Assessment:
None of these resolutions is compelling without further work. The mass hierarchy is a real obstacle. It does not automatically close Foundation A — the PGT framework may still provide viable cosmological torsion — but it means that a light torsion mode requires either fine-tuning or a dynamical explanation that has not yet been provided.

---

## 6. Summary Table: Parameter Space Verdict

| Question | Answer | Confidence |
|----------|--------|------------|
| Does a ghost-free PGT parameter region exist? | **Yes** | High (multiple independent analyses) |
| How many ghost-free models are known? | 3 clean single-mode models (0+, 0-, 2+) | High |
| Are the ghost-free regions large or small? | Small (isolated submanifolds of the 9D parameter space) | High |
| Is there a ghost-free model with multiple propagating torsion modes? | Not established; generically no in pure torsion-squared sector | Moderate |
| What sets the torsion mass scale? | m^2 = M_Pl^2 / |t_I| for quadratic PGT | Derived |
| Can the torsion mass be cosmologically small? | Parametrically yes; requires |t_I| >> 1 | Parametric only |
| Is this natural? | No — comparable hierarchy problem to Lambda | Assessment |

---

## Key References

Same as 01_pgt_action_definition.md, plus:

11. Nikiforova, V. et al. (2009). Phys. Rev. D 80, 124050.
12. Chen, P. et al. (2009). "Poincare gauge theory with even and odd parity dynamic connection modes." Phys. Rev. D 80, 024045.
13. Obukhov, Y.N. et al. (2017). "General analysis of Poincare gauge field theory." Phys. Rev. D 96, 104036.
