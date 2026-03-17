# Toy State-Selection Frameworks

**Date:** 2026-03-16

---

## Toy 1: pNGB Misalignment Kicked by Bounce Curvature

### Setup

Axion-like DE field:

```
V(θ) = Λ⁴(1 - cos θ),    θ = φ/f
```

with f ~ M_Pl, m² = Λ⁴/f² ~ H₀².

Non-minimal curvature coupling:

```
L ⊃ ξR f² θ²/2
```

### Effective potential during bounce

At the bounce (R = R_b ≈ 21 M_Pl²):

```
V_eff(θ) = Λ⁴(1 - cos θ) + ξR_b f² θ²/2
```

Ratio of curvature to axion potential at θ ~ 1:

```
ξR_b f² / Λ⁴ = ξ × 21 M_Pl² × M_Pl² / (H₀² M_Pl²)
              = 21ξ M_Pl² / H₀²
              ~ 21ξ × 10¹²²
```

The curvature coupling is 10¹²² times stronger than the axion
potential. During the bounce, the field moves in a pure
parabola V_eff ≈ ξR_b f² θ²/2.

### Evolution through the bounce

The equation of motion (in cosmic time):

```
f θ̈ + 3Hf θ̇ + (Λ⁴/f) sin θ + ξRfθ = 0
```

Dividing by f:

```
θ̈ + 3Hθ̇ + m² sin θ + ξRθ = 0
```

At H ≈ 0, dropping m² ≪ ξR:

```
θ̈ + ξR(t) θ = 0
```

where R(t) = 12α²/(1 + 4α²t²)² + ... ≈ 12α²/(1 + 4α²t²)².

This is a PARAMETRIC OSCILLATOR with time-dependent frequency.

### Solution structure

For R(t) = R_b/(1 + 4α²t²)²:

The equation is:

```
θ̈ + ξR_b/(1 + 4α²t²)² θ = 0
```

Substituting u = 2αt:

```
d²θ/du² + (ξR_b/4α²)/(1 + u²)² θ = 0
```

The parameter: ξR_b/(4α²) = ξ × 21 M_Pl² / (4 × 1.76 M_Pl²)
= 21ξ/7.04 ≈ 3ξ.

For ξ = 1: the equation is d²θ/du² + 3/(1+u²)² θ = 0.

This is a SCATTERING problem (same mathematical structure as
the tensor mode equation from Branch H!). The field enters from
u → -∞ with some amplitude and phase, scatters off the potential
bump, and exits to u → +∞.

### The scattering map

For u → ±∞: θ(u) → A₊ + B₊ u (free motion, linear in u).

The map (A₋, B₋) → (A₊, B₊) is a 2×2 matrix that preserves
phase-space area (Liouville). In terms of (θ, θ̇):

```
[θ_post]     [a  b] [θ_pre ]
[θ̇_post]  =  [c  d] [θ̇_pre]
```

with ad - bc = 1 (area-preserving).

For the potential V_eff ∝ 1/(1+u²)²:

The matrix elements depend on ξ. For ξ = 1:

Numerical estimate (by analogy with the tensor Bogoliubov
calculation): |a| ~ |d| ~ O(1), |b| ~ O(1/M_Pl),
|c| ~ O(M_Pl). The field position changes by O(1) and
the velocity changes by O(M_Pl).

### Post-bounce state

```
θ_post = a × θ_pre + b × θ̇_pre/M_Pl
θ̇_post = c × M_Pl × θ_pre + d × θ̇_pre
```

For a frozen DE field (θ̇_pre ~ H₀ M_Pl ≪ M_Pl²):

```
θ_post ≈ a × θ_pre    (the b term is negligible)
θ̇_post ≈ c × M_Pl × θ_pre
```

The post-bounce misalignment is PROPORTIONAL to the pre-bounce
misalignment, with a coefficient |a| ~ O(1).

**The bounce ROTATES the state in phase space but does not
CONTRACT it.** θ_post is a function of θ_pre with no narrowing.

### Late-time dark energy

```
ρ_DE = Λ⁴(1 - cos θ_post) ≈ Λ⁴ a² θ_pre² / 2
```

The energy depends on θ_pre (the pre-bounce misalignment).
The bounce modifies it by the factor a² ~ O(1). No prediction.

### The velocity problem

The bounce also gives a VELOCITY: θ̇_post ~ c M_Pl θ_pre.
This corresponds to kinetic energy:

```
KE = f² θ̇²/2 ~ M_Pl² × c² M_Pl² × θ_pre² / 2
   ~ c² M_Pl⁴ θ_pre²
```

For θ_pre ~ 1: KE ~ M_Pl⁴. This is PLANCK-SCALE kinetic energy!

After the bounce, this kinetic energy redshifts as a⁻⁶ (stiff
matter for a free scalar) until the field slows down and
V(θ) becomes relevant. The kinetic energy today:

```
KE_today ~ M_Pl⁴ × (a_b/a_0)⁶ ~ M_Pl⁴ × 10⁻¹⁹⁵ ~ 10⁻¹⁹⁵ M_Pl⁴
```

This is negligible (10⁻⁷³ below ρ_DE). The Planck-scale kinetic
energy is completely diluted away. The field effectively
re-freezes shortly after the bounce.

**After re-freezing, the field is at θ ≈ θ_post ≈ a × θ_pre.**
The bounce has modified the misalignment by a factor |a| ~ O(1).

### Biggest ambiguity

θ_pre is unknown. The bounce maps it to θ_post = a × θ_pre
but doesn't determine θ_pre.

### Verdict: FAIL_ARBITRARY_INITIAL_CONDITIONS

---

## Toy 2: Double-Well Branch Selection at the Bounce

### Setup

```
V(φ) = λ(φ² - v²)² + εφ    (tilted double-well)
```

with v ~ M_Pl (or v ~ meV for DE-scale), λ chosen so
V_barrier ~ Λ⁴ ~ 10⁻¹²² M_Pl⁴.

Curvature coupling: ξRφ²/2.

### Effective potential during bounce

```
V_eff = λ(φ² - v²)² + εφ + ξR_b φ²/2
```

For ξR_b ≫ λv²: the double-well structure is obliterated.
V_eff ≈ ξR_b φ²/2 (pure parabola). Single minimum at φ = 0.

### Evolution through the bounce

**Before bounce:** Field in one minimum (say φ = +v).
**During bounce:** Curvature coupling dominates. Field is
pulled toward φ = 0 by force F = -ξR_b φ.
**After bounce:** Curvature drops. Double-well re-forms.
Field near φ = 0 (hilltop). Rolls to nearest minimum.

### Which minimum?

The field retains a residual displacement and velocity from
the pre-bounce state. For the pre-bounce field at φ = +v:

The bounce pulls it toward 0 but doesn't reach 0 exactly
(bounce is too brief for complete relaxation). The residual
displacement δφ > 0 means the field rolls back to φ = +v.

**The bounce does NOT change the vacuum branch.** The field
returns to its original minimum after the transient kick.

For the field to change branches: the kick must push the field
PAST φ = 0 to φ < 0. This requires:

```
Δφ > v    (displacement exceeds the well separation)
```

The displacement: Δφ ~ v × (1 - cos(ω_b t_b)) where
ω_b = √(ξR_b) ~ M_Pl and t_b ~ 1/M_Pl. So:

```
Δφ ~ v × (1 - cos(√(21ξ)))
```

For ξ = 1: Δφ ~ v × (1 - cos(4.58)) ~ v × 1.10 > v. **CROSSES!**
For ξ = 0.1: Δφ ~ v × (1 - cos(1.45)) ~ v × 0.87 < v. **DOESN'T CROSS.**

So for ξ ≳ 1, the field CAN cross to the other well. But
whether it does depends on the EXACT value of √(21ξ) modulo 2π.

For specific ξ values:
- ξ = 1: cos(4.58) ≈ -0.10 → Δφ ≈ 1.10v (crosses)
- ξ = 2: cos(6.48) ≈ 0.97 → Δφ ≈ 0.03v (doesn't cross)
- ξ = 3: cos(7.94) ≈ -0.17 → Δφ ≈ 1.17v (crosses)

The outcome is a SENSITIVE function of ξ — the branch selection
oscillates as ξ varies. This is NOT predictive; it depends on
the exact value of a coupling constant.

### Biggest ambiguity

The branch depends sensitively on ξ (a free parameter).
No prediction without knowing ξ to high precision.

### Verdict: FAIL_NO_NARROWING (sensitive to coupling, not bounce)

---

## Toy 3: Metastable Vacuum Trapping via Bounce Mass Deformation

### Setup

```
V(φ) = V_0 + m²φ²/2 - gφ³/3 + λφ⁴/4
```

This has a local minimum near φ = 0 and a global minimum at
φ = φ_true > 0. The metastable vacuum at φ ≈ 0 has vacuum
energy V_0, and the true vacuum has energy V_0 - ΔV.

Curvature coupling: ξRφ²/2.

### Effective potential during bounce

```
V_eff = V_0 + (m² + ξR_b)φ²/2 - gφ³/3 + λφ⁴/4
```

For ξ > 0 and ξR_b ≫ m²: the mass squared becomes large and
positive. The barrier between metastable and true vacuum is
RAISED (the metastable minimum is stabilized).

For ξ < 0 and |ξ|R_b > m²: the mass squared becomes negative.
The metastable minimum DISAPPEARS. The field rolls toward the
true vacuum.

### Case ξ > 0 (stabilization)

The bounce STABILIZES the metastable vacuum. After the bounce,
the mass returns to m² and the metastable vacuum returns to its
pre-bounce form. No permanent change.

The stabilization is TRANSIENT. The field's tunneling rate
returns to its pre-bounce value after the bounce.

Verdict: No lasting effect.

### Case ξ < 0 (destabilization)

The bounce temporarily REMOVES the metastable minimum. The field
rolls toward the true vacuum during the bounce.

After the bounce: the metastable minimum re-forms. If the field
has rolled past the barrier during the bounce, it continues to
the true vacuum. If not, it returns to the metastable minimum.

The transition occurs if the field rolls distance Δφ ~ φ_barrier
in time t_b ~ 1/M_Pl:

```
Δφ ~ |F| t_b² ~ |ξ|R_b φ / M_Pl² ~ |ξ| × 21 × φ
```

For |ξ| ≳ 1/21 ≈ 0.05: the field moves by O(φ) or more.
The barrier is crossed.

BUT: this means the bounce DESTROYS the metastable vacuum
for ANY |ξ| > 0.05. The metastable state is not viable in a
bouncing cosmology with even moderate curvature coupling.

This is an ANTI-TRAPPING result: the bounce PREVENTS metastable
vacuum DE, it doesn't select it.

### Biggest ambiguity

The sign of ξ determines whether trapping or release occurs.
For ξ < 0 (the more dangerous sign): metastable DE is destroyed.
For ξ > 0: transient stabilization, no permanent effect.

### Verdict: FAIL_ARBITRARY_INITIAL_CONDITIONS (trapping is
transient; release depends on ξ sign)

**Note:** The anti-trapping result (ξ < 0 destroys metastable
vacua) is mildly interesting as a NEGATIVE constraint: bouncing
cosmologies may be incompatible with metastable vacuum DE for
|ξ| > 0.05. But this is a GENERIC curvature-coupling result,
not specific to the spin-torsion bounce.

---

## Toy 4: Symmetry Restoration and Re-Breaking

### Setup

Dark-sector Mexican hat:

```
V(φ) = -μ²φ²/2 + λφ⁴/4 + ξRφ²/2
```

Symmetry-breaking scale: v² = μ²/λ (at R = 0).
At R ≠ 0: v_eff² = (μ² - ξR)/λ.

### Symmetry restoration condition

The symmetry is restored when v_eff² < 0:

```
ξR > μ²  →  ξ × 21 M_Pl² > μ²
```

For μ ~ meV ~ 10⁻³¹ M_Pl:

```
ξ > μ²/(21 M_Pl²) ~ 10⁻⁶²/21 ~ 10⁻⁶³
```

**Any ξ > 10⁻⁶³ restores the symmetry at the bounce.** For
ξ ~ O(1): the symmetry is MASSIVELY restored (the effective
mass at the bounce is m_eff ~ √(ξ × 21) M_Pl ~ M_Pl, far
above the symmetry-breaking scale).

### Evolution

**Pre-bounce:** Field at φ = v (one minimum).
**Bounce:** Symmetry restored, field driven to φ = 0.
**Post-bounce:** Symmetry re-breaks, field at φ ≈ 0 (hilltop).

### Which minimum after re-breaking?

The field at the hilltop has residual velocity from the
pre-bounce kick. The direction of this velocity determines
which minimum the field falls into.

For a field that was at φ = +v before the bounce: the
residual velocity after the curvature-induced oscillation
is v_post ∝ v × sin(√(21ξ) × effective_time).

This is the SAME sensitive ξ-dependence as Toy 2. The branch
selection oscillates with ξ.

### The thermal noise alternative

If the bounce thermalizes the dark sector (T_bounce ~ M_Pl),
the field at the hilltop experiences random thermal kicks.
The probability of falling into either minimum is 50/50
(for exact Z₂ symmetry).

This is RANDOM selection, not DETERMINISTIC selection by the
bounce. It provides no predictive content.

### Biggest ambiguity

Branch selection depends sensitively on ξ (deterministic case)
or is 50/50 random (thermal case). Neither is predictive.

### Verdict: FAIL_NO_NARROWING

---

## Summary of Toy Frameworks

| Toy | Mechanism | Outcome | Fatal flaw |
|-----|-----------|---------|-----------|
| 1: pNGB kick | Phase-space rotation | θ_post = a × θ_pre | Liouville (no contraction) |
| 2: Branch selection | ξ-sensitive oscillation | Depends on exact ξ | Sensitive to coupling |
| 3: Metastable trapping | Transient (ξ>0) or release (ξ<0) | No permanent change | Anti-trapping for ξ<0 |
| 4: Symmetry re-breaking | ξ-sensitive or random | Not predictive | Same as Toy 2 |

**Common fatal flaw: Liouville's theorem prevents the bounce
from contracting phase space. The bounce is a Hamiltonian
scattering event that ROTATES initial conditions, not a
dissipative process that FORGETS them.**

The Liouville obstacle is STRUCTURAL. It applies to ANY
Hamiltonian coupling between the bounce and the dark sector.
Breaking it requires IRREVERSIBILITY (particle production,
decoherence, thermalization) — but these processes destroy the
specific dark-sector state rather than selecting it.
