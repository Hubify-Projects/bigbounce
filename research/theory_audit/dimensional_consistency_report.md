# Dimensional Consistency Audit

**Date:** 2026-03-12
**Convention:** Natural units (c = ℏ = 1) unless stated. [X] = mass dimension of X.

---

## Dimension Reference

| Quantity | Mass dimension | SI equivalent |
|----------|---------------|---------------|
| Length | -1 | m |
| Time | -1 | s |
| Energy/Mass | +1 | GeV |
| Action | 0 | dimensionless |
| Lagrangian density | +4 | GeV⁴ |
| G_N | -2 | GeV⁻² |
| M_Pl = 1/√G | +1 | GeV |
| Curvature R_{μν} | +2 | m⁻² |
| Torsion T^{abc} | +1 | m⁻¹ |
| Tetrad e^a_μ | 0 | dimensionless |
| d⁴x | -4 | m⁴ |
| √(-g) | 0 | dimensionless |

---

## Equation-by-Equation Audit

### 1. Einstein-Cartan-Holst Action (Eq. 1, main.tex:157)

```
S_ECH = (1/16πG) ∫ d⁴x e [e^μ_a e^ν_b R^{ab}_{μν} + (1/γ) ε^{abcd} e_a^μ e_b^ν R_{cdμν}]
```

| Factor | Dimension |
|--------|-----------|
| 1/(16πG) | +2 (since [G] = -2) |
| d⁴x | -4 |
| e (tetrad det) | 0 |
| e^μ_a e^ν_b R^{ab}_{μν} | 0 + 0 + 2 = +2 |
| 1/γ | 0 |

**Action dimension:** [1/G] × [d⁴x] × [eR] = (+2) + (-4) + (+2) = **0** ✓

**Status: OK** — Action is dimensionless.

---

### 2. Torsion from spin density (Eq. 3, main.tex:181)

```
T^{abc} = 8πG · S^{abc}
```

| Factor | Dimension |
|--------|-----------|
| T^{abc} (torsion) | +1 |
| G | -2 |
| S^{abc} = ψ̄ γ^[a γ^{bc}] ψ | +3 (each ψ has dim 3/2) |

**Check:** [G] × [S] = (-2) + (+3) = **+1** = [T] ✓

**Status: OK**

---

### 3. Four-fermion interaction (Eq. 4, main.tex:187)

```
L_int = -(3πG_N/2) × [γ²/(γ²+1)] × J_{(A)μ} J^μ_{(A)}
```

| Factor | Dimension |
|--------|-----------|
| G_N | -2 |
| γ²/(γ²+1) | 0 |
| J_{(A)μ} = ψ̄ γ^μ γ^5 ψ | +3 |
| J² | +6 |

**Lagrangian density:** [G] × [J²] = (-2) + (+6) = **+4** ✓

**Status: OK** — Correct dimension for a Lagrangian density.

---

### 4. Holst term in first-order form (Eq. 5, main.tex:193)

```
S_Holst = (M_Pl²/γ) ∫ e_I ∧ e_J ∧ R^{IJ}(ω)
```

| Factor | Dimension |
|--------|-----------|
| M_Pl² | +2 |
| 1/γ | 0 |
| e_I ∧ e_J (two 1-forms) | -2 (each 1-form has dim -1 in form language) |
| R^{IJ} (curvature 2-form) | 0 (2-form with dim +2 components and dim -2 from dx∧dx) |

**Note on forms:** In differential form language, a p-form carries an implicit factor of (dx)^p with dimension -p. The curvature 2-form R^{IJ} = R^{IJ}_{μν} dx^μ ∧ dx^ν has components [R^{IJ}_{μν}] = +2 and the 2-form basis has dim -2, so [R^{IJ}] = 0 as a form. Similarly [e_I] = [e^a_μ dx^μ] = 0 + (-1) = -1.

**Action:** (+2) + (0) + (-1) + (-1) + (0) = **0** ✓

**Status: OK**

---

### 5. Parity-odd effective action (Eq. 7, main.tex:201)

```
S_eff = ∫ d⁴x √(-g) (α/M) ε^{μνρσ} e^I_μ e^J_ν F_{IJρσ}
```

| Factor | Dimension |
|--------|-----------|
| d⁴x √(-g) | -4 |
| α/M | -1 (since M ~ M_Pl, α dimensionless) |
| ε^{μνρσ} | 0 (Levi-Civita symbol) |
| e^I_μ e^J_ν | 0 |
| F_{IJρσ} (contorsion-curvature) | +2 (contains ∂K ~ M² and K∧K ~ M²) |

**Integrand (Lagrangian density):** (-1) + (0) + (0) + (+2) = **+1**

**Problem identified in paper:** This gives mass dimension +1, which is 3 short of the required +4 for a Lagrangian density.

**Paper's resolution (main.tex:204):** "The missing three powers of mass arise through *on-shell evaluation* at Planck-scale densities, where K ~ M_Pl and R ~ M_Pl²."

On-shell: F_{IJρσ} evaluates to K·R ~ M_Pl × M_Pl² = M_Pl³, giving:
[α/M] × [M_Pl³] = (-1) + (+3) = +2

Then with ε e e giving dimension 0, and the full d⁴x √(-g) integral:
S = ∫ d⁴x × (dim +2 density) × M_Pl² = action dim 0 ← only works if we treat it as ρ_Λ = Ξ × M_Pl⁴

**The paper correctly identifies this as a "scaling ansatz" (main.tex:204), not a rigorous EFT derivation.**

**Status: NOTED** — Dimensionally consistent only as a scaling ansatz with on-shell Planck-scale evaluation. The paper is transparent about this.

---

### 6. Effective cosmological constant (Eq. 8, main.tex:270)

```
Λ_eff = Ξ · M_Pl² + c_ω ω²
```

| Factor | Dimension |
|--------|-----------|
| Λ_eff | +2 (cosmological constant has dim of inverse length squared) |
| Ξ | 0 (dimensionless) |
| M_Pl² | +2 |
| c_ω | 0 |
| ω² | +2 (vorticity has dim of H, i.e., inverse time = +1) |

**Check:** [Ξ · M_Pl²] = 0 + 2 = **+2** ✓
**Check:** [c_ω ω²] = 0 + 2 = **+2** ✓

**Status: OK**

---

### 7. Vacuum energy density (Eq. 9, main.tex:280)

```
ρ_Λ = [(α/M) · M_Pl] × D_inf × M_Pl⁴
```

| Factor | Dimension |
|--------|-----------|
| ρ_Λ | +4 (energy density) |
| (α/M) · M_Pl | (-1)(+1) = 0 (dimensionless) |
| D_inf | 0 (dimensionless) |
| M_Pl⁴ | +4 |

**Check:** 0 + 0 + 4 = **+4** ✓

**Status: OK** — Energy density is dimensionally correct.

---

### 8. Inflationary dilution factor (Eq. 11, main.tex:291)

```
D_inf = exp(-3 N_tot) × (T_reh / M_GUT)^{3/2}
```

| Factor | Dimension |
|--------|-----------|
| exp(-3 N_tot) | 0 (dimensionless; N_tot is dimensionless) |
| T_reh / M_GUT | 0 (ratio of two energies) |
| (T_reh/M_GUT)^{3/2} | 0 |

**Check:** D_inf is **dimensionless** ✓

**Status: OK**

---

### 9. One-loop coefficient (Eq. 10, main.tex:213)

```
α/M ~ (g²/32π²) × (γ/M) × ln(Λ_UV²/μ²) + δ_NY
```

| Factor | Dimension |
|--------|-----------|
| α/M | -1 |
| g² | 0 |
| 1/(32π²) | 0 |
| γ | 0 |
| 1/M | -1 |
| ln(Λ_UV²/μ²) | 0 |
| δ_NY | -1 (must match α/M) |

**Check:** (0)(0)(0)(-1)(0) = **-1** ✓

**Status: OK**

---

### 10. Modified Friedmann equation (Eq. 12, main.tex:233)

```
H² = (8πG/3) ρ [1 - ρ/ρ_crit]
```

| Factor | Dimension |
|--------|-----------|
| H² | +2 |
| G | -2 |
| ρ | +4 |
| ρ/ρ_crit | 0 |

**Check:** [G × ρ] = (-2) + (+4) = **+2** ✓

**Status: OK**

---

### 11. Critical bounce density (Eq. 13, main.tex:237)

```
ρ_crit = (√3 / 32π²γ³) ρ_Pl
```

| Factor | Dimension |
|--------|-----------|
| ρ_crit | +4 |
| Numerical (√3/32π²γ³) | 0 |
| ρ_Pl | +4 |

**Check:** 0 + 4 = **+4** ✓

**Status: OK**

---

### 12. Galaxy spin asymmetry amplitude (main.tex:326)

```
A₀ ∝ (α/M) × ⟨δ_rms⟩ × f(z_form)
```

| Factor | Dimension |
|--------|-----------|
| A₀ | 0 (dimensionless) |
| α/M | -1 |
| ⟨δ_rms⟩ | 0 (density contrast is dimensionless) |
| f(z_form) | 0 |

**Problem:** [α/M × δ_rms × f] = -1, but A₀ must be dimensionless.

**Resolution:** The proportionality suppresses an energy scale E_eff that makes the product dimensionless: A₀ ~ (α/M) × E_eff × δ_rms × f, where [E_eff] = +1. This is noted in the paper (main.tex:333) as requiring E_eff to close the dimensional gap, and the paper acknowledges a 9–12 order-of-magnitude gap between naive estimates and observation.

**Status: NOTED** — Dimensionally incomplete as written (proportionality hides E_eff). Paper is transparent about this gap.

---

## Summary

| Equation | Expected dim | Actual dim | Status |
|----------|-------------|------------|--------|
| Eq. 1 (ECH action) | 0 | 0 | **OK** |
| Eq. 3 (Torsion = G·S) | +1 | +1 | **OK** |
| Eq. 4 (Four-fermion L) | +4 | +4 | **OK** |
| Eq. 5 (Holst 4-form) | 0 | 0 | **OK** |
| Eq. 7 (S_eff component) | +4 (L density) | +1 | **NOTED** — scaling ansatz |
| Eq. 8 (Λ_eff) | +2 | +2 | **OK** |
| Eq. 9 (ρ_Λ) | +4 | +4 | **OK** |
| Eq. 10 (α/M one-loop) | -1 | -1 | **OK** |
| Eq. 11 (D_inf) | 0 | 0 | **OK** |
| Eq. 12 (Mod. Friedmann) | +2 | +2 | **OK** |
| Eq. 13 (ρ_crit) | +4 | +4 | **OK** |
| Eq. A₀ (spin amplitude) | 0 | -1 | **NOTED** — proportionality hides E_eff |

**10/12 fully consistent. 2/12 have noted dimensional gaps that the paper explicitly acknowledges as scaling ansätze or incomplete derivations.**
