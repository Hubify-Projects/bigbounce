# Order-of-Magnitude Screening

**Date:** 2026-03-16

---

## The Three Scales

```
Bounce scale:    M_bounce ~ M_Pl ~ 10¹⁸ GeV
                 R_bounce ~ 21 M_Pl²
                 t_bounce ~ 1/M_Pl ~ 10⁻⁴³ s
                 ρ_bounce ~ 0.21 M_Pl⁴

Dark energy scale: m_DE ~ H₀ ~ 10⁻³³ eV ~ 10⁻⁶¹ M_Pl
                   V_DE ~ Λ⁴ ~ 10⁻¹²² M_Pl⁴
                   f_DE ~ M_Pl (for pNGB)

Coupling scale:    ξ ~ O(1) (non-minimal, natural)
                   or ξ ~ 10⁻⁶² (tuned to DE scale)
```

The hierarchy: M_bounce/m_DE ~ 10⁶¹. This is 61 orders of
magnitude in mass, 122 in energy density, 244 in V⁴ terms.

---

## Kill Test 1: Can the bounce set a misalignment angle?

**Required:** θ_post determined (or narrowed) by the bounce.
**Available:** Curvature kick rotates (θ, θ̇) by O(1).

The kick rotates the state but doesn't contract the allowed
range. From Toy 1:

```
θ_post = a(ξ) × θ_pre + b(ξ) × θ̇_pre
```

with |a|² + |b|² M_Pl² ~ 1 (unitary-ish).

**For narrowing:** Need many initial conditions → few outcomes.
This requires dissipation (absent at H ≈ 0) or many oscillation
cycles (need ξ ≫ 1, generating huge radiative corrections).

**Kill verdict: KILLED.** Liouville + naturalness prevents
predictive misalignment setting.

---

## Kill Test 2: Can the bounce select a discrete vacuum branch?

**Required:** The bounce reliably drives the field to one specific
vacuum out of N options, for generic pre-bounce states.

**Available:** The bounce drives the field toward φ = 0 (for
ξ > 0). After the bounce, the field falls into the vacuum
nearest φ = 0.

**The "nearest to φ = 0" vacuum is determined by V(φ), not
by the bounce.** Different V(φ) → different selected vacuum.
The bounce provides no information beyond "reset to symmetric
point."

**Comparison test:** Would INFLATION do the same thing?

During inflation with H_inf ~ 10¹⁴ GeV: any DE field with
m ≪ H_inf is frozen. Its value is set by pre-inflationary
conditions, randomized by quantum fluctuations (δφ ~ H_inf/2π
per e-fold), and ends up at a random value in the potential
after reheating.

The bounce does LESS than inflation: it shifts the field by
O(1) toward φ = 0, whereas inflation randomizes the field
across the entire potential over 60 e-folds.

**Kill verdict: KILLED.** Bounce provides less state selection
than standard inflation. No unique content.

---

## Kill Test 3: Can the bounce trap a metastable state?

**Required:** Bounce makes a metastable state MORE stable or
traps the field in a specific local minimum.

**Result from Toy 3:**
- ξ > 0: transient stabilization, no permanent effect
- ξ < 0: DESTROYS metastable state (anti-trapping)

**Kill verdict: KILLED.** The bounce destabilizes rather than
traps (for ξ < 0) and has no lasting effect (for ξ > 0).

**Mildly interesting negative result:** Metastable vacuum DE
with |ξ| > 0.05 may be INCOMPATIBLE with bouncing cosmologies.
But this is a generic curvature coupling result, valid for any
epoch with R > m²/ξ, not specific to the spin-torsion bounce.

---

## Kill Test 4: Can nonadiabatic particle production set the DE state?

**Required:** Particle production creates a condensate with
ρ ~ 10⁻¹²² M_Pl⁴ and w ≈ -1.

**Available (from Candidate E calculation):**

Condensate energy today:
```
ρ_χ ~ m² χ₀² ~ H₀² × (M_Pl × a_b/a_0)²
     ~ H₀² × (10⁻³² M_Pl)²
     ~ 10⁻¹²⁸ M_Pl⁴
```

This is 10⁶ BELOW ρ_DE. And the estimate is optimistic (assumes
maximum displacement χ₀ ~ M_Pl at the bounce).

**Equation of state:** For m > H₀, the field oscillates with
w ≈ 0 (matter, not DE). For m < H₀, the field hasn't started
oscillating and acts as a CC — but its energy density is even
smaller (ρ ~ m² M_Pl² × (a_b/a_0)² ~ m²/H₀² × 10⁻¹²⁸ M_Pl⁴).

**Even the most optimistic scenario is 10⁶ below ρ_DE.** And the
amplitude depends on the initial displacement (arbitrary IC).

**Kill verdict: KILLED.** Wrong amplitude, wrong equation of
state, and dependent on initial conditions.

---

## Kill Test 5: Can the spin-torsion coupling (J⁵)² do anything unique?

**Required:** The four-fermion interaction specific to EC gravity
provides a unique state-selection channel not available in GR.

**The spin-torsion coupling:**
```
L_eff ⊃ -3πG/2 × (J⁵)²
```

where J⁵ is the STANDARD MODEL axial current.

**For this to affect a dark scalar φ:**
Need φ to couple to J⁵. Options:

1. φ J⁵_μ J^{5μ} / f² — dimension-8 operator, suppressed by f⁴.
   At the bounce: (J⁵)² ~ ρ_crit² ~ 10⁻² M_Pl⁸ (Planck density
   fermion condensate). Force on φ:
   F ~ ρ_crit² / f² ~ 10⁻² M_Pl⁸ / M_Pl² ~ 10⁻² M_Pl⁶.
   Wait, this needs dimensional analysis work. In any case,
   (J⁵)² is parity-EVEN (Branch H result), so there's no
   qualitative advantage over curvature coupling.

2. Introduce a DARK FERMION ψ_dark that couples to φ via
   Yukawa: yφψ̄ψ. Then the torsion generates:
   L ⊃ -3πG/2 × (J⁵_dark)².
   At the bounce: if dark fermions are thermalized, (J⁵_dark)²
   ~ T⁴ ~ M_Pl⁴. This contributes to the dark scalar's
   effective potential: δV ~ G M_Pl⁴ ~ M_Pl².
   Same Planck-scale kick as curvature coupling.

**The spin-torsion coupling provides no qualitative advantage
over ξRφ².** It's another Planck-scale contribution to the
effective potential during the bounce, with no special structure
that would enable state selection.

**Kill verdict: KILLED.** No unique spin-torsion state-selection
channel.

---

## The Ninth Barrier: Liouville Phase-Space Conservation

The screening reveals a new structural barrier underlying all
five candidate failures:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  BARRIER 9: Hamiltonian phase-space conservation        │
│                                                         │
│  The bounce is a Hamiltonian scattering event.          │
│  Liouville's theorem preserves phase-space volume.      │
│  The bounce ROTATES dark-sector initial conditions       │
│  but cannot CONTRACT them to a predictive outcome.      │
│  Dissipation (needed for contraction) requires H ≠ 0    │
│  or irreversible processes, both absent/negligible       │
│  at the bounce instant.                                 │
│                                                         │
│  Combined with the naturalness dilemma (ξ ~ O(1)       │
│  breaks mass protection), this prevents ANY curvature-  │
│  coupled state selection from being both strong enough  │
│  to act AND natural enough to preserve the DE sector.   │
│                                                         │
│  This is the state-selection analog of the scale-       │
│  separation barrier (Barrier 5).                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Surviving Candidates After Screening

**None.**

All five candidates are killed by the combination of:
1. Liouville's theorem (no phase-space contraction)
2. Naturalness dilemma (ξ ~ O(1) vs. mass protection)
3. Scale separation (M_Pl vs. meV)

The bounce is a HAMILTONIAN SCATTERING EVENT at Planck energy.
It rotates dark-sector states but cannot select them. The
post-bounce state is a deterministic (and reversible) function
of the pre-bounce state, with no narrowing or selection.

---

## Could Anything Survive Further Analysis?

### The one remaining loophole: parametric amplification

If the bounce time profile R(t) has a RESONANCE with a
dark-sector frequency, parametric amplification could create
an exponentially large response for specific parameter values.

The resonance condition: ω_dark ≈ ω_bounce/2, where
ω_bounce ~ M_Pl (the characteristic frequency of R(t)).

For ω_dark ~ M_Pl: the dark sector is Planck-scale, not DE.
For ω_dark ~ m_DE ~ H₀: the mismatch is 10⁶¹, no resonance.

**No parametric resonance between DE and the bounce.**

### The second loophole: quantum effects

Quantum decoherence during the bounce could provide the
irreversibility needed for phase-space contraction. But:

1. Decoherence requires an ENVIRONMENT (many degrees of freedom
   to trace over). At the bounce, the environment is the SM
   radiation bath. The dark scalar's decoherence rate:
   γ_dec ~ g² T ~ g² M_Pl (at bounce temperature).
   Decoherence in time t_Pl: γ t_Pl ~ g².
   For g ~ 10⁻⁶⁰ (natural coupling): γ t_Pl ~ 10⁻¹²⁰.
   No decoherence.

2. Even if decoherence occurred, it would RANDOMIZE the state
   (thermal equilibrium), not SELECT a specific state. This
   gives θ uniformly distributed — worse than the pre-bounce
   state.

**Quantum effects don't help.**

---

## Final Screening Result

| Candidate | Kill test | Status |
|-----------|----------|--------|
| A: pNGB misalignment | Liouville + naturalness | **DEAD** |
| B: Multi-vacuum | Potential-determined, not bounce | **DEAD** |
| C: Symmetry re-breaking | ξ-sensitive or random | **DEAD** |
| D: Metastable trapping | Transient or anti-trapping | **DEAD** |
| E: Nonadiabatic | Wrong amplitude + w ≈ 0 | **DEAD** |
| Spin-torsion specific | No advantage over ξR | **DEAD** |
| Parametric resonance | Frequency mismatch 10⁶¹ | **DEAD** |
| Quantum decoherence | Too slow + randomizes | **DEAD** |

**Zero candidates survive the cheap-kill screening.**
