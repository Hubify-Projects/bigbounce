# Branch O: Toy Frameworks

**Date:** 2026-03-16

---

## Reference Scales

```
ECH bounce:
  ρ_crit = 0.21 M_Pl⁴ ≈ 10¹¹⁴ GeV⁴
  R_bounce ≈ 21 M_Pl² ≈ 10³⁷ GeV²
  S_bounce ~ M_Pl³ ~ 10⁵⁵ GeV³ (spin density)
  t_bounce ~ t_Pl ~ 5.4 × 10⁻⁴⁴ s
  H = 0 at the bounce, |Ḣ| ~ M_Pl² ~ 10³⁷ GeV²
  a(t) = a_b(1 + 4α²t²)^{1/4}, α² = (2π/3)ρ_crit G

PGT bounce (propagating torsion):
  ρ_crit = m_T² M_Pl² (depends on torsion mass m_T)
  For m_T = 10⁹ GeV: ρ_crit ~ 10⁵⁴ GeV⁴
  R_bounce ~ m_T² ~ 10¹⁸ GeV²
  t_bounce ~ 1/m_T ~ 10⁻³³ s

Dark energy:
  ρ_DE = (2.3 meV)⁴ ≈ 2.8 × 10⁻¹¹ eV⁴ ≈ 10⁻⁴⁷ GeV⁴
  Λ_DE = (ρ_DE)^{1/4} ≈ 2.3 meV ≈ 2.3 × 10⁻¹² GeV
  H₀ ≈ 2.2 × 10⁻³³ eV ≈ 10⁻⁴² GeV

Hierarchy:
  ρ_crit/ρ_DE ~ 10¹²² (ECH) or 10¹⁰¹ (PGT, m_T = 10⁹ GeV)
  M_Pl/Λ_DE ~ 10³⁰
  t_bounce × Λ_DE ~ 10⁻⁵⁵ (ECH) — the hidden sector is FROZEN
```

---

## Toy O1: First-Order Phase Transition During the Bounce

### Setup

Hidden-sector scalar χ with potential:

```
V(χ, T) = D(T² - T₀²)χ² - ATχ³ + (λ/4)χ⁴
```

Parameters chosen for a first-order transition at T = T_c:
- T₀ = symmetry restoration temperature in flat space
- A = cubic coupling (controls first-order strength)
- λ = quartic coupling

Curvature coupling:
```
ΔV = ξRχ²/2
```

Effective critical temperature with curvature:
```
T_c²(R) = T₀² + ξR/(2D)
```

### Bounce-era effective potential

At the bounce (R = R_b ≈ 21 M_Pl²), the curvature coupling
adds an effective mass²:

```
m²_eff = 2D(T² - T₀²) + ξR_b
```

For ξ > 0: this is a positive mass² contribution of order
ξ × 21 M_Pl² at the bounce. The symmetric phase (χ = 0) is
stabilized for ANY hidden-sector scale T₀ ≪ M_Pl.

For ξ < 0: the mass² contribution is negative. If |ξ|R_b > 2DT²,
the symmetric phase is destabilized even at T > T₀. The
transition is triggered EARLY.

### Before / During / After

**Pre-bounce (contracting phase):**
The hidden sector is in the broken phase (χ = v) if T < T_c.
If the hidden sector is cold (T_h ≪ T_c), it's deep in the
broken phase.

**During the bounce (ξ > 0 case):**
R rises to R_b ~ 21 M_Pl². The curvature contributes
ξR_b ~ 21ξ M_Pl² to the mass². For ξ ~ 1, this is M_Pl-scale.
The barrier between χ = 0 and χ = v becomes:

```
V_barrier(R_b) ≈ V_barrier(0) + ξR_b v²/2
                ~ λv⁴ + M_Pl² v²
                ~ M_Pl² v² (for v ≪ M_Pl)
```

The barrier is RAISED by M_Pl² v². The field is trapped in its
current minimum. No transition.

**During the bounce (ξ < 0 case):**
The curvature REMOVES the barrier. The field can roll from
the broken phase to the symmetric phase.

Time for the field to roll distance v:
```
t_roll ~ v / √(|ξ|R_b) ~ v / (M_Pl √(21|ξ|))
```

For v ~ 10⁶ GeV (EW-ish scale):
```
t_roll ~ 10⁶ / (10¹⁸ × 4.6) ~ 10⁻¹³ GeV⁻¹ ~ 10⁻³⁸ s
```

Compare to t_bounce ~ 10⁻⁴³ s (ECH). The roll time is 10⁵
LONGER than the bounce. The field DOESN'T REACH χ = 0 during
the bounce.

For v ~ Λ_DE ~ 10⁻¹² GeV:
```
t_roll ~ 10⁻¹² / (10¹⁸ × 4.6) ~ 10⁻³¹ GeV⁻¹ ~ 10⁻⁵⁶ s
```

This is 10¹³ SHORTER than t_bounce. The field DOES reach χ = 0.

**CRITICAL RESULT:** The field can roll to the symmetric phase
during the bounce ONLY if v ≲ M_Pl × (M_Pl t_bounce) ~ M_Pl.
For ECH: v ≲ M_Pl. For any sub-Planckian v: the field rolls
to χ = 0 during the bounce (for |ξ| ~ 1).

Wait — let me redo this carefully.

The force at the bounce: F = |ξ|R_b χ ~ |ξ| × 21 M_Pl² × v.
Acceleration: χ̈ ~ |ξ| × 21 M_Pl² × v (since mass is negligible
compared to the curvature term).
Displacement in time t_b: Δχ ~ ½ × |ξ| × 21 M_Pl² × v × t_Pl²
= ½ × 21|ξ| × v × (M_Pl t_Pl)² = ½ × 21|ξ| × v.

So Δχ ~ 10|ξ| × v. For |ξ| ~ 1: Δχ ~ 10v. The field overshoots
χ = 0 and oscillates around it.

**After the bounce:**
R drops back to zero. The broken-phase potential reforms.
The field oscillates around χ = 0 (symmetric phase) with
amplitude ~ v. It eventually rolls to one of the broken-phase
minima (±v).

Which minimum? Depends on the phase of oscillation when R drops
below the critical value. This is the SAME ξ-sensitivity as
Branch J Toy 2 and Toy 4. Deterministic but parameter-sensitive.

### The irreversible step?

If the oscillations around χ = 0 produce particles (parametric
resonance into hidden-sector radiation), the oscillation energy
is DISSIPATED. The field then slowly rolls to the nearest minimum
after the energy is lost.

Particle production rate during oscillation:
```
Γ_production ~ g²_h χ̇²/(8π m_h) (for decay into hidden fermions)
```

where g_h is a hidden-sector Yukawa coupling.

The oscillation frequency is ω ~ √(|ξ|R_b) ~ M_Pl during the
bounce, dropping as R decreases. Particle production is efficient
if g_h is O(1) and the hidden-sector DOF are lighter than ω.

**If dissipation is efficient:** The field loses energy and
settles into χ = 0 (symmetric phase). After R → 0, it's at the
hilltop of the Mexican hat. Thermal fluctuations then determine
which minimum it falls into: RANDOM selection (50/50 for Z₂).

**If dissipation is inefficient:** The field retains its
oscillation energy and the minimum selection is deterministic
but ξ-sensitive. No predictivity.

### Resulting late-time state

Both outcomes are bad:
- Dissipative: 50/50 random vacuum selection (FAIL_ARBITRARY_BRANCH)
- Non-dissipative: ξ-sensitive deterministic (FAIL_NO_NARROWING)

### Biggest ambiguity

Whether dissipation is efficient. If it is, we get randomness.
If it isn't, we get Branch J recycled.

### ρ_DE from this mechanism?

Even if a vacuum is selected, ρ_DE = |V(v) - V(0)| = λv⁴/4.
This depends on λ and v, which are hidden-sector parameters.
NO CONNECTION to the bounce.

For ρ_DE ~ (2.3 meV)⁴: need λv⁴ ~ 10⁻⁴⁷ GeV⁴. For v ~ meV:
λ ~ 1. For v ~ GeV: λ ~ 10⁻⁸³. The latter is a fine-tuning.
The former requires v ~ meV with no explanation for why v is
at the DE scale.

### Preliminary verdict: FAIL (multiple tests)

- O1: MARGINAL (dissipation possible but symmetric → random)
- O2: MARGINAL (ξ < 0 transition is bounce-era, but field dynamics
  are not qualitatively different from any curvature-dominated epoch)
- O3: FAIL (50/50 for Z₂ if dissipative; ξ-sensitive if not)
- O4: FAIL (ρ_DE = λv⁴ requires tuning v or λ)
- O5: FAIL (no relation between bounce parameters and ρ_DE)
- O6: PASS (true vacuum is a CC, trivially viable)

---

## Toy O2: Metastable Vacuum Trapping by Bounce-Triggered Tunneling

### Setup

Hidden sector with two minima:

```
V(χ) = -μ²χ²/2 + λχ⁴/4 + V_0
```

True vacuum at χ_t = μ/√λ with V = V_0 - μ⁴/(4λ).
Add a barrier by including a χ⁶ term or a more general potential:

```
V(χ) = V_0 + (m²/2)χ² - (g/3)χ³ + (λ/4)χ⁴
```

False vacuum at χ = 0, V = V_0.
True vacuum at χ_t > 0, V = V_0 - ΔV.

### Tunneling rate in flat space

Coleman bounce action:
```
S_E ≈ (8π²/3) × m⁸ / (g⁴ ΔV)    [thin-wall approximation]
```

For S_E ≫ 1: tunneling is slow (Γ ~ exp(-S_E) ≪ 1).
The false vacuum is metastable.

### Bounce coupling and tunneling modification

During the bounce, the curvature modifies the potential:

```
V_eff(χ) = V(χ) + ξR_b χ²/2
```

For ξ > 0: false vacuum deepened, barrier raised, S_E INCREASED.
Tunneling is SUPPRESSED during the bounce. No transition.

For ξ < 0: false vacuum destabilized, barrier lowered.
New bounce action:

```
S_E(R_b) ≈ S_E(0) × [1 + |ξ|R_b/m²]^{-p}
```

where p > 0 depends on the potential shape. For |ξ|R_b ≫ m²:

```
S_E(R_b) ~ S_E(0) × (m²/(|ξ|R_b))^p → 0 as R_b → ∞
```

**For Planck-scale curvature with |ξ| ~ 1: the barrier is
completely eliminated (S_E → 0).** This is classical rolling,
not tunneling. The field simply rolls to the true vacuum when
the barrier disappears.

### Before / During / After

**Pre-bounce:** Field in false vacuum χ = 0.

**During the bounce (ξ < 0):**
Barrier removed. Field rolls toward true vacuum.
Roll time: t_roll ~ 1/√(|ξ|R_b) ~ 1/M_Pl ~ t_Pl.
In time t_Pl, the field rolls by:
Δχ ~ √(|ξ|R_b) × t_Pl² × χ ~ χ (same calculation as Toy O1).

If the field reaches the true vacuum during the bounce: TRANSITION
COMPLETE. Irreversible (the true vacuum is the global minimum;
the field stays there even after R → 0).

**After the bounce:**
R drops to zero. The original potential re-forms. But the field
is now in the true vacuum. It stays there.

### The irreversible step

The classical roll from false to true vacuum IS irreversible if:
1. The field reaches the true vacuum during the bounce (timing OK
   for m ≲ M_Pl, which is always true for sub-Planckian hidden sectors)
2. After R → 0, the field is past the barrier in the true vacuum
   basin (yes, if the roll distance exceeds the barrier width)
3. The kinetic energy gained during the roll is dissipated
   (otherwise the field oscillates and might return)

**Point 3 is critical.** The field gains KE ~ |ξ|R_b × Δχ²/2 ~
M_Pl² × χ_t² during the roll. This is Planck-scale kinetic energy.
The field oscillates wildly between the two basins unless damped.

Damping requires: 3Hφ̇ friction (but H ≈ 0 at bounce) or
particle production (needs hidden-sector interactions).

If particle production is efficient: energy is transferred to
hidden-sector radiation. The field settles in the true vacuum.
The transition is truly irreversible.

If particle production is inefficient: the field oscillates
forever (conserving energy in the Hamiltonian limit). Eventually,
expansion provides friction (H > 0 after bounce), but the field
must oscillate for time ~ M_Pl/H before H-friction matters.
During this time the field explores both basins repeatedly.
The final minimum depends on the phase of oscillation when
friction becomes effective — SENSITIVE to parameters.

### Resulting late-time state

Best case (efficient dissipation): field in true vacuum, with
vacuum energy V_true = V_0 - ΔV.

For ρ_DE ~ (2.3 meV)⁴: need V_true ~ (2.3 meV)⁴. This requires:
- V_0 and ΔV both tuned such that V_0 - ΔV ~ 10⁻⁴⁷ GeV⁴
- OR V_0 = 0 (protected by some symmetry) and ΔV ~ -10⁻⁴⁷ GeV⁴
  (still requires ΔV at the DE scale)

There is NO mechanism to generate ΔV ~ (2.3 meV)⁴ from bounce
parameters. ΔV is set by m, g, λ of the hidden sector.

### Biggest ambiguity

Whether the field actually settles in the true vacuum (requires
efficient dissipation) vs oscillating indefinitely.

### Preliminary verdict: FAIL (naturalness)

- O1: PASS (classical roll + dissipation is genuinely irreversible)
- O2: MARGINAL (the barrier removal requires R ~ M_Pl², which IS
  bounce-specific for ECH; but for PGT the scale is m_T² which
  could be reached during inflation too)
- O3: PASS (true vacuum is unique — no arbitrary branch)
- O4: FAIL (V_true = V_0 - ΔV must be tuned to DE scale)
- O5: FAIL (no relation between bounce and V_true)
- O6: PASS (true vacuum is stable CC, trivially viable)

---

## Toy O3: Symmetry Restoration + Dissipative Re-Breaking

### Setup

Hidden sector with spontaneously broken Z_N symmetry:

```
V(χ) = λ(χ^N - v^N)² + ε × f(χ)
```

N degenerate vacua for ε = 0. Small explicit breaking ε lifts
the degeneracy, giving vacuum energies V_1, V_2, ..., V_N with
splittings ΔV ~ ε.

Curvature coupling: ξRχ²/2. For ξ > 0 and R = R_b: symmetry
restored (all vacua merge to χ = 0).

### The thermal re-breaking scenario

**During the bounce:** Symmetry restored. The field is driven
to χ = 0. The hidden sector is heated by the bounce to temperature
T_h.

**After the bounce:** R drops. Symmetry re-breaks. The hidden
sector undergoes a phase transition at T_c (the critical
temperature for Z_N breaking).

If the transition is FIRST-ORDER:
- Bubble nucleation occurs
- The nucleation rate for vacuum i is Γ_i ~ exp(-S_E^i)
- The explicit breaking ε biases the rates: Γ_lower > Γ_higher
  (the lower-energy vacuum nucleates faster)
- The vacuum with the LOWEST energy wins the percolation race

This is genuinely irreversible (nucleation + percolation).

### Does the bounce matter?

The bounce provides T_h (the hidden-sector reheat temperature).
The phase transition occurs at T_c, determined by the hidden-
sector potential. The nucleation rates depend on T/T_c.

**Key question:** Does T_h from the bounce differ from T_h from
standard reheating after inflation?

Gravitational particle production during the bounce:
```
ρ_h ~ C × m_h² M_Pl²    (for m_h ≪ M_Pl, minimal coupling)
```

For m_h ~ 10⁶ GeV: ρ_h ~ 10¹² × 10³⁶ = 10⁴⁸ GeV⁴.
T_h ~ (ρ_h/g_*)^{1/4} ~ (10⁴⁸/100)^{1/4} ~ 10¹¹ GeV.

Compare to reheating after inflation:
T_reheat can range from 10⁴ to 10¹⁵ GeV depending on the model.

**T_h from the bounce is NOT unique.** Inflationary reheating can
produce any comparable T_h.

The ONLY unique feature of the bounce is the spin density
S ~ M_Pl³ and the (J⁵)² interaction. But (J⁵)² is parity-even,
so it doesn't bias Z_N selection. And S couples to the hidden
sector only gravitationally.

### Resulting late-time state

The vacuum with the lowest energy wins (for first-order transition
with explicit Z_N breaking). The vacuum energy is:

```
V_selected ≈ V_min = min(V_1, ..., V_N)
```

This is determined ENTIRELY by the hidden-sector potential,
not the bounce. The bounce provides the heat; the potential
determines the outcome.

### Biggest ambiguity

Whether the hidden-sector phase transition is first-order
(required for biased selection) or second-order (gives random
domain distribution).

### Preliminary verdict: FAIL (not bounce-specific)

- O1: PASS (nucleation is irreversible)
- O2: FAIL (any hot cosmology does the same)
- O3: PASS (lowest-energy vacuum wins, if first-order)
- O4: FAIL (V_min must be at DE scale — hidden-sector tuning)
- O5: FAIL (no bounce-parameter dependence)
- O6: PASS (CC from selected vacuum)

---

## Toy O4: Dissipative Hidden-Sector Reheating with Exponential Hierarchy

### Setup

This toy model attempts to address the naturalness problem
directly. The hidden sector has a potential with an exponentially
small vacuum energy generated by dimensional transmutation.

Hidden-sector gauge group G_h with coupling g_h that runs:

```
α_h(μ) = α_h(M) / (1 + b α_h(M) ln(μ/M) / (2π))
```

Confinement scale:
```
Λ_h = M × exp(-2π/(b α_h(M)))
```

If M = M_Pl and α_h(M_Pl) chosen so that Λ_h ~ meV:
```
ln(M_Pl/Λ_h) ~ 70  →  2π/(b α_h) ~ 70  →  α_h ~ 0.09/b
```

For b ~ 10 (many hidden colors): α_h ~ 0.009. This is a
reasonable coupling (no extreme tuning needed).

The vacuum energy from confinement:
```
ρ_vac ~ Λ_h⁴ ~ (meV)⁴ ~ ρ_DE
```

### The bounce's role

The bounce heats the hidden sector. If T_h > Λ_h, the hidden
sector is in the deconfined phase. When T drops below Λ_h, it
confines and generates the vacuum energy.

**Does the bounce determine whether confinement occurs?**

No. Confinement occurs whenever T < Λ_h, regardless of how the
hidden sector was heated. The bounce provides heat; confinement
is an intrinsic property of the gauge theory.

**Does the bounce determine Λ_h?**

Only if the bounce sets the INITIAL CONDITIONS for the hidden-
sector coupling α_h. But α_h is a fundamental parameter of the
theory, not set by dynamics.

**Could the bounce set α_h dynamically?**

If α_h depends on a modulus field φ (as in string compactifications):
α_h = f(φ). The bounce could set φ via state selection. But this
is Branch J recycled — the bounce cannot select φ (Liouville).

### The critical failure

The dimensional transmutation mechanism generates Λ_h ~ meV
naturally (exponentially small from O(1) coupling). This is
a genuine solution to the hierarchy problem for the hidden
sector. But it has NOTHING TO DO WITH THE BOUNCE.

The bounce is decorative. The vacuum energy is set by α_h(M_Pl)
and the hidden-sector gauge group, both fundamental parameters.

### Resulting late-time state

ρ_DE ~ Λ_h⁴. This IS at the right scale if α_h is chosen
appropriately. But the choice of α_h is a parameter selection,
not a bounce prediction.

### Biggest ambiguity

Why α_h has the value it has. The bounce doesn't help with this.

### Preliminary verdict: FAIL (not bounce-specific, bounce is decorative)

- O1: PASS (confinement is irreversible)
- O2: FAIL (confinement happens in any cosmology)
- O3: PASS (unique confined vacuum)
- O4: PASS (Λ_h exponentially small from O(1) coupling)
- O5: FAIL (no bounce parameter in ρ_DE = Λ_h⁴)
- O6: PASS (confined vacuum acts as CC)

**Note:** This model has good naturalness (O4 PASS) precisely
because it has nothing to do with the bounce. The naturalness
comes from dimensional transmutation, a well-known mechanism.
The bounce adds nothing.

---

## Summary of Toy Frameworks

| Toy | Model | Irreversible? | Bounce-specific? | Natural ρ_DE? | Predictive? |
|-----|-------|:---:|:---:|:---:|:---:|
| O1: First-order PT | ξRχ² transition | MARGINAL | MARGINAL | NO | NO |
| O2: Metastable trapping | ξ<0 barrier removal | YES | MARGINAL | NO | NO |
| O3: Z_N re-breaking | Thermal nucleation | YES | NO | NO | NO |
| O4: Dim. transmutation | Hidden gauge confinement | YES | NO | YES | NO |

### The fundamental pattern

Every toy framework separates into two independent pieces:

1. **The bounce provides energy/heat** — this is generic
   (any cosmology does it)

2. **The hidden-sector potential determines the vacuum** — this
   is independent of the bounce

No toy framework connects the two. The bounce energy/scale
never appears in the formula for ρ_DE.

The one toy with natural ρ_DE (Toy O4) achieves it through
dimensional transmutation, which has nothing to do with the
bounce. This is the anti-correlation: mechanisms that solve
naturalness don't need the bounce; mechanisms that use the
bounce can't solve naturalness.

### Why no toy framework can connect bounce to ρ_DE

The fundamental reason: the bounce scale is M_Pl (or m_T) and
the DE scale is meV. Any formula ρ_DE = f(M_Pl, couplings)
that gives (meV)⁴ requires the couplings to bridge the 10¹²²
hierarchy. The bounce provides the M_Pl scale but not the small
couplings. The small couplings must come from somewhere else
(dimensional transmutation, symmetry, landscape, anthropics).

The bounce cannot set the small couplings because:
- Liouville prevents coupling selection (Branch J, Barrier 9)
- The bounce is too brief for equilibration at DE scales
- The bounce couples universally to all sectors (no selectivity)
