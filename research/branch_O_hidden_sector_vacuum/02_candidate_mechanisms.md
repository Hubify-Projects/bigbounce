# Branch O: Candidate Mechanisms

**Date:** 2026-03-16

---

## Candidate A: Hidden-Sector First-Order Phase Transition Triggered by Bounce Curvature

### Basic Structure

Hidden scalar χ with temperature- and curvature-dependent effective potential:

```
V_eff(χ, T, R) = D(T² - T_c²)χ² - ETχ³ + λχ⁴/4 + ξRχ²/2
```

where D, E, λ are hidden-sector couplings and T_c is the critical
temperature in flat space.

### Bounce Coupling

The curvature coupling ξRχ²/2 shifts the effective critical temperature:

```
T_c²(R) = T_c² - ξR/(2D)
```

At the bounce (R ~ 21 M_Pl² for ECH, R ~ m_T² for PGT):

- ξ > 0: T_c is LOWERED. Symmetry breaking is delayed/prevented.
  After the bounce, T_c returns to its flat-space value and the
  transition occurs normally (or is supercooled).

- ξ < 0: T_c is RAISED. Symmetry breaking is triggered at higher
  temperature. The transition is ACCELERATED during the bounce.

### Irreversible Ingredient

First-order phase transitions are irreversible:
- Bubble nucleation is stochastic (entropy production)
- Latent heat release is thermodynamically irreversible
- Domain wall dynamics and bubble collisions produce entropy
- The transition completion is a one-way process

### Biggest Theoretical Risk

**Bounce specificity.** First-order transitions happen at a critical
temperature regardless of whether there was a bounce. The bounce
modifies T_c by O(ξM_Pl²/D), but the transition still occurs when
T drops to T_c during normal cooling. The bounce might shift the
transition temperature but doesn't qualitatively change whether
the transition happens.

**Unless** the bounce causes the transition to happen DURING the
bounce epoch itself (when R is large), trapping the system in a
specific vacuum that it would not reach during normal cooling.
This requires the hidden sector to be near-critical at bounce
curvature scales.

### Late-Time Quantity Determined

The vacuum energy difference between the pre-transition and
post-transition phases: ΔV = V(χ=0) - V(χ=v). This is the
hidden-sector contribution to the CC.

**Critical problem:** ΔV is set by the hidden-sector potential
parameters (D, E, λ, T_c), NOT by the bounce. The bounce
determines WHETHER the transition occurs, not WHAT the resulting
vacuum energy is.

---

## Candidate B: Metastable Vacuum Trapping via Bounce-Induced Mass Deformation

### Basic Structure

Hidden scalar with multiple local minima:

```
V(χ) = Σ_n V_n(χ - χ_n)    (landscape with N local minima)
```

Each minimum n has vacuum energy V_n. The field starts in some
minimum and can tunnel between them.

Curvature coupling: ξRχ²/2 deforms the landscape during the bounce.

### Bounce Coupling

During the bounce:
```
V_eff(χ) = V(χ) + ξR_b χ²/2
```

For ξ > 0: minima near χ = 0 are deepened/stabilized; minima far
from χ = 0 are raised/destabilized. The bounce funnels the field
toward χ ≈ 0.

For ξ < 0: opposite — minima near χ = 0 are destabilized.

### Irreversible Ingredient

- Tunneling between minima (quantum, irreversible)
- Thermal transitions over barriers (if hidden sector is hot)
- Classical rolling after barrier removal (if ξR_b removes barrier)

The field can be trapped in a minimum that it cannot subsequently
escape (if the barrier is restored after the bounce and the
remaining tunneling rate is negligibly slow).

### Biggest Theoretical Risk

**This is Branch J Toy 3 with a hidden sector instead of DE.**
Branch J showed that ξ > 0 gives only transient stabilization
(no permanent change) and ξ < 0 gives destabilization (destroys
metastable vacua). The same analysis applies here.

The only escape: if the hidden sector has MANY minima and the
bounce reshuffles which one the field occupies. But which minimum
the field ends up in depends on the pre-bounce state (Liouville
again, unless there is genuine thermalization).

### Late-Time Quantity Determined

The vacuum label n (which minimum) and correspondingly V_n.
But V_n is set by the landscape parameters, not the bounce.

---

## Candidate C: Symmetry Restoration at the Bounce + Biased Re-Breaking

### Basic Structure

Hidden sector with spontaneously broken discrete symmetry (Z_N):

```
V(χ) = λ(χ^N - v^N)² + higher-order
```

with N degenerate vacua (for Z_N), some of which have different
vacuum energies when a small explicit breaking ε is added.

### Bounce Coupling

ξRχ²/2 restores the symmetry at the bounce (as in Branch J Toy 4).
The field is driven to χ = 0. After the bounce, the symmetry
re-breaks.

### Irreversible Ingredient

**This is the critical question.** Two scenarios:

1. **Deterministic re-breaking:** The field rolls from χ = 0 to
   the nearest minimum, determined by residual velocity from the
   pre-bounce state. This is HAMILTONIAN — Liouville applies.
   Branch J Toy 4 showed this is ξ-sensitive and unpredictive.
   **No genuine irreversibility. FAILS.**

2. **Thermalized re-breaking:** The bounce thermalizes the hidden
   sector. The field at χ = 0 is in a thermal bath at temperature
   T_bounce. It undergoes a thermal phase transition as T drops.
   The selected vacuum depends on the nucleation rates in each
   Z_N sector.

   The nucleation rates can be BIASED if:
   - There is explicit Z_N breaking (ε ≠ 0)
   - The bounce curvature couples differently to different sectors
   - Torsion-induced fermion bilinears break Z_N

   Biased nucleation is genuinely irreversible and stochastic.

### Biggest Theoretical Risk

**Bounce specificity.** Thermal symmetry restoration + re-breaking
occurs in ANY hot cosmology (e.g., after inflation + reheating).
The bounce provides the heat, but so does reheating. Unless the
bounce provides a UNIQUE bias (via torsion, spin density, or
curvature profile) that reheating does not, this is generic.

The (J⁵)² interaction is parity-EVEN, so it doesn't provide a
parity-odd bias. Curvature coupling is also available after
inflation. The spin density S ~ M_Pl³ at the bounce is unique,
but it couples to the hidden sector only gravitationally
(suppressed by G or G²).

### Late-Time Quantity Determined

The Z_N vacuum label, and correspondingly the vacuum energy
contributed by the hidden sector. But the vacuum energy is still
set by ε and the potential parameters.

---

## Candidate D: Tunneling Enhancement/Suppression via Bounce Potential Distortion

### Basic Structure

Hidden sector stuck in a false vacuum. Tunneling to the true
vacuum proceeds via Coleman-De Luccia (CdL) bubble nucleation:

```
Γ ~ A exp(-S_E)
```

where S_E is the Euclidean bounce action.

### Bounce Coupling

During the cosmological bounce, the curvature R modifies the
effective potential and the CdL action:

```
S_E[R] = S_E[0] + δS_E(R)
```

If δS_E < 0 (curvature lowers barrier), the tunneling rate is
EXPONENTIALLY enhanced.
If δS_E > 0 (curvature raises barrier), the tunneling rate is
EXPONENTIALLY suppressed.

The sensitivity is exponential: a modest change in S_E (say
δS_E ~ 10) changes Γ by a factor of e^10 ~ 10⁴.

### Irreversible Ingredient

Quantum tunneling is genuinely irreversible (the bubble expands
and converts the false vacuum to true vacuum). The nucleation
event is stochastic and entropy-producing.

### Biggest Theoretical Risk

**Timing.** The bounce lasts ~ t_Pl (ECH) or ~ 1/m_T (PGT).
The tunneling must complete DURING this window. The nucleation
rate must satisfy:

```
Γ × t_bounce × V_horizon > 1
```

At the bounce, H = 0 so the causal volume is formally infinite.
But the relevant volume is the one that thermalizes post-bounce.
Using V ~ t_Pl³ (ECH):

```
Γ × t_Pl⁴ > 1  →  Γ > M_Pl⁴
```

This means the tunneling rate must be Planck-scale. The Euclidean
action must be S_E < O(1). This is only possible if the barrier
is completely obliterated during the bounce (not suppressed, but
removed). At that point, it's a classical roll, not tunneling.

**For genuine tunneling (S_E ≫ 1 in flat space), the bounce can
at best reduce S_E by δS_E ~ ξR_b/(barrier height). If the barrier
height is ≪ M_Pl⁴, then δS_E can be large. But the barrier must
also be large enough that the field doesn't tunnel in flat space.**

### Late-Time Quantity Determined

Whether the field is in the true or false vacuum. The vacuum energy
of each is set by the potential, not the bounce.

---

## Candidate E: pNGB Hidden Sector with Nonadiabatic Branch Occupation

### Basic Structure

Hidden-sector pseudo-Nambu-Goldstone boson (pNGB) χ with
approximate continuous symmetry broken to Z_N at scale Λ_h:

```
V(χ) = Λ_h⁴ [1 - cos(Nχ/f_h)]
```

The bounce creates particles/excitations nonadiabatically.
The occupation numbers of the N branches after the bounce
determine the late-time vacuum.

### Bounce Coupling

Gravitational particle production: the time-varying metric
during the bounce creates χ particles via the Bogoliubov
mechanism. The number density:

```
n_χ ~ |β_k|² k³/(2π²)
```

where β_k is the Bogoliubov coefficient for mode k.

For a minimally coupled scalar during the spin-torsion bounce,
the dominant production is at k ~ M_Pl (ECH) or k ~ m_T (PGT).
The low-energy modes (k ~ meV) are in the adiabatic regime
and are NOT produced.

### Irreversible Ingredient

Particle production is irreversible: |β|² > 0 corresponds to
entropy creation. The created particles subsequently thermalize
(if they interact) or free-stream (if they don't).

### Biggest Theoretical Risk

**Scale mismatch.** Particles are produced at k ~ M_Pl. These
are UV modes, not the zero mode that determines the vacuum
branch. The zero-mode (k = 0) evolution is adiabatic (ω = m_χ
changes slowly compared to ω itself for m_χ ≪ M_Pl). So the
bounce produces HIGH-ENERGY hidden-sector particles but does
NOT excite the vacuum-selecting zero mode.

The UV particles subsequently redshift and (if they interact)
thermalize at T < Λ_h. When T drops below the phase transition
temperature, the field selects a vacuum branch thermally — but
this is the same as Candidate C (thermal selection, not bounce-
specific).

### Late-Time Quantity Determined

The occupation of the N branches after the thermal phase transition.
Set by thermal dynamics, not directly by the bounce.

---

## Candidate F: Dissipative Hidden-Sector Reheating / Thermal Branch Selection

### Basic Structure

The bounce transfers energy to a hidden sector via gravitational
particle production. The hidden sector thermalizes at some
temperature T_h. If the hidden sector undergoes a phase transition
at T_c < T_h, the transition dynamics (and hence the vacuum
branch) are determined by T_h and the hidden-sector microphysics.

### Bounce Coupling

Gravitational production during the bounce:

```
ρ_h(t_bounce) ~ C × M_Pl⁴ × (m_h/M_Pl)^p
```

where C is an O(1) coefficient, m_h is the hidden-sector mass
scale, and p depends on spin and coupling (p = 0 for conformally
coupled scalars in 4D is actually zero production; p ≥ 2 for
massive particles).

For MINIMAL gravitational coupling (no ξRχ²):
```
ρ_h ~ m_h² M_Pl² (for m_h ≪ M_Pl)
```

Hidden-sector temperature after thermalization:
```
T_h ~ (ρ_h/g_*)^{1/4} ~ (m_h² M_Pl² / g_*)^{1/4}
```

### Irreversible Ingredient

Thermalization is irreversible (entropy production). The subsequent
phase transition (if first-order) is also irreversible.

The dissipation comes from hidden-sector self-interactions that
convert coherent field energy into thermal radiation.

### Biggest Theoretical Risk

**Not bounce-specific.** Gravitational particle production occurs
in ANY time-varying background — inflation, preheating, and the
bounce all produce particles. The bounce produces particles at
the bounce scale (M_Pl or m_T), but so does inflation at H_inf.

Unless the spin-torsion bounce produces a QUALITATIVELY DIFFERENT
particle spectrum (e.g., preferentially producing specific species
due to the (J⁵)² interaction), the reheating is generic.

The (J⁵)² interaction IS specific to the EC bounce. It produces
fermion pairs. But:
- It's parity-even (no chirality bias)
- It's Planck-suppressed (G ~ 1/M_Pl²)
- Any fermion with m ≪ M_Pl is produced similarly

**Second risk:** T_h depends on hidden-sector parameters (m_h, g_*),
not primarily on bounce parameters. The bounce provides the energy;
the hidden sector determines how it's used.

### Late-Time Quantity Determined

T_h (hidden-sector reheat temperature) and consequently the
phase-transition dynamics. But ρ_DE is set by the hidden-sector
potential, not T_h.

---

## Candidate G: Domain-Wall / Multi-Vacuum with Bounce-Imposed Branch Asymmetry

### Basic Structure

Hidden sector with N degenerate (or near-degenerate) vacua.
Domain walls form during the phase transition. The final vacuum
is determined by which domain wins the percolation competition.

### Bounce Coupling

The bounce could bias the percolation competition if:

1. The curvature at the bounce lifts the degeneracy (ξRχ² gives
   different contributions to different vacua if they have
   different 〈χ²〉)

2. The spin density at the bounce couples to the domain wall
   network (torsion can source a pseudoscalar bias, but (J⁵)²
   is parity-even)

3. The bounce creates an asymmetric initial particle distribution
   (one vacuum has more particles than another)

### Irreversible Ingredient

Domain wall percolation is irreversible: when one domain wins,
the others shrink and annihilate. This is an entropy-increasing
process.

### Biggest Theoretical Risk

**Same as C:** The domain wall dynamics depend on the phase
transition temperature and the hidden-sector potential, not
on the bounce. Any hot cosmology produces domain walls. The
bounce doesn't bias which domain wins unless there is a
UNIQUE bounce-era coupling to the hidden-sector vacuum
structure.

The curvature bias ξR ~ ξM_Pl² at the bounce is universal
(every vacuum feels it). Different vacua have different 〈χ²〉
so they get different ξR〈χ²〉 contributions, but this is a
splitting ΔV ~ ξM_Pl² × Δ〈χ²〉 at the bounce. After the bounce,
this splitting vanishes (R → 0). The domain walls don't remember
the bounce-era splitting unless the transition COMPLETES during
the bounce (requiring Γ > M_Pl⁴; see Candidate D timing problem).

### Late-Time Quantity Determined

The dominant vacuum label. But the vacuum energy is set by the
potential parameters.

---

## Cross-Cutting Assessment

### Which candidates have genuine irreversibility?

| Candidate | Irreversible step | From the bounce specifically? |
|-----------|------------------|------------------------------|
| A: First-order PT | Bubble nucleation | Maybe (if transition during bounce) |
| B: Metastable trapping | Tunneling/thermal hop | Weak (Branch J Toy 3 recycled) |
| C: Biased re-breaking | Thermal nucleation | Weak (any hot cosmology) |
| D: Tunneling enhancement | Quantum tunneling | Maybe (exponential sensitivity) |
| E: Nonadiabatic production | Particle creation | Weak (UV modes only, not vacuum) |
| F: Dissipative reheating | Thermalization | Weak (generic gravitational production) |
| G: Domain percolation | Percolation dynamics | Weak (post-bounce, not during) |

### The honest assessment

Most candidates have genuine irreversibility but it is NOT
bounce-specific. The irreversible processes (phase transitions,
thermalization, percolation) occur in ANY hot cosmology. The
bounce provides the energy/heat, but so does inflation+reheating.

The only candidates with potential bounce specificity are:
- **A** (if the transition occurs DURING the bounce when R is large)
- **D** (exponential sensitivity of tunneling to curvature)

Even these face the fundamental problem: the late-time vacuum
energy is set by the hidden-sector potential, not by the bounce.
The bounce determines WHETHER/WHEN the transition occurs, not
WHAT vacuum energy results.

**This means Branch O can at best select a vacuum BRANCH, not
determine ρ_DE within that branch.** For ρ_DE to be predicted,
the selected branch must have a vacuum energy that is somehow
natural at (2.3 meV)⁴. This requires either:
- A landscape with an exponential number of vacua (anthropic)
- A symmetry that protects the vacuum energy (sequestering)
- A dynamical relaxation mechanism (not the bounce)

None of these are bounce-specific.
