# Branch O: Order-of-Magnitude Screening

**Date:** 2026-03-16

---

## The Central Question

For every candidate:

> HOW does a Planck-scale (or m_T-scale) event at t ~ 10⁻⁴³ s
> determine a vacuum energy at 10⁻¹²² M_Pl⁴ without fine tuning?

This is the question that must be answered quantitatively.
No hand-waving.

---

## Kill Test O-K1: Does the Irreversibility Actually Come from the Bounce?

### Candidate A (First-order PT triggered by curvature)

The transition can be triggered during the bounce (ξ < 0 removes
the barrier). But the resulting vacuum energy ΔV is set by the
potential parameters, not R_b. The curvature determines WHETHER
the transition happens, not WHAT results.

Does the same transition happen without the bounce? YES — it
happens when T drops below T_c during normal cooling. The bounce
at most shifts the timing.

**Exception:** If the barrier is ONLY removed by Planck-scale
curvature (the barrier height V_barrier > m_T² v² but < M_Pl² v²),
then the ECH bounce triggers the transition but the PGT bounce
and inflation do not. This is bounce-specific for ECH only.

But the vacuum energy is STILL set by potential parameters.

**Verdict: MARGINAL.** Bounce can trigger, but ρ_DE is not
determined by the bounce.

### Candidate B (Metastable trapping)

Branch J Toy 3 recycled with minor modifications. The ξ > 0
case gives transient stabilization. The ξ < 0 case gives
barrier removal (same as Candidate A).

**Verdict: DEAD (Branch J recycled).**

### Candidate C (Symmetry restoration + re-breaking)

The thermal re-breaking after the bounce is identical to
thermal re-breaking after inflationary reheating. The bounce
heats the hidden sector to T_h; so does reheating.

The only bounce-specific feature would be a coupling to the
spin density S or (J⁵)². But (J⁵)² is parity-even — it cannot
bias Z_N breaking. And S couples gravitationally (suppressed by
G ~ M_Pl⁻²).

**Verdict: DEAD (not bounce-specific).**

### Candidate D (Tunneling enhancement)

The exponential sensitivity of tunneling to barrier parameters
makes this the most promising candidate on paper. During the
bounce, δS_E can change by O(1) or more.

But the tunneling must complete during the bounce (t ~ t_Pl).
This requires:

```
Γ × t_Pl⁴ > 1  →  Γ > M_Pl⁴  →  S_E < O(1)
```

For S_E < O(1), this is NOT tunneling; it's classical barrier
crossing. The exponential sensitivity that makes tunneling
interesting is irrelevant when the barrier is obliterated.

For S_E ≫ 1 in flat space with modest reduction during the bounce
(δS_E ~ -10), the rate during the bounce is:

```
Γ_bounce ~ M_Pl⁴ × exp(-(S_E - 10)) ≪ M_Pl⁴ if S_E ≫ 10
```

The transition does NOT complete during the bounce.

**The dilemma:** either the barrier is obliterated (S_E → 0,
classical roll, no tunneling advantage) or it's reduced but
still large (S_E ≫ 1, transition too slow for t_Pl).

For PGT with longer bounce duration t_b ~ 1/m_T:
```
Γ × t_b⁴ > 1  →  S_E < 4 ln(m_T/m_h)
```

For m_T = 10⁹ GeV, m_h = 1 GeV: S_E < 4 × 20 = 80.
This allows moderate-barrier tunneling. But S_E ~ 80 is a
specific requirement on the hidden-sector potential — a tuning.

**Verdict: DEAD for ECH (timing), MARGINAL for PGT (requires
specific barrier height).**

### Candidate E (Nonadiabatic production)

Gravitational particle production creates particles at k ~ M_Pl.
These are UV modes that don't affect the vacuum-selecting zero
mode. The zero mode is adiabatic (ω = m_χ ≪ Ḣ/H is not
meaningful since H = 0 at the bounce; the proper adiabaticity
parameter is ω̇/ω² ~ Ṙ/(m_χ R) ~ M_Pl/m_χ which is ≫ 1 and
would suggest nonadiabatic evolution — but the COUPLING to the
zero mode is gravitational and Planck-suppressed).

Actually, wait. The adiabaticity parameter for a mode with
effective mass m_eff² = m² + ξR(t) is:

```
η = |ṁ_eff|/m_eff² = |ξṘ|/(2m_eff³)
```

At the bounce: Ṙ ~ M_Pl³, m_eff ~ √(|ξ|R_b) ~ M_Pl.
So η ~ M_Pl³/(2M_Pl³) ~ 1. The evolution IS nonadiabatic for
the effective mass during the bounce.

But the ZERO MODE starts at k = 0, and its energy is:
```
E_0 ~ m_eff(t) ~ M_Pl (during bounce) → m_χ (after bounce)
```

The zero mode DOES undergo nonadiabatic evolution. But the
Bogoliubov coefficient for the zero mode:

```
|β_0|² ~ exp(-π m_χ² / |ξṘ|) ≈ exp(-π m_χ² / (|ξ| M_Pl³))
```

For m_χ ≪ M_Pl: |β_0|² ≈ 1. Maximum production.

The produced zero-mode excitation has amplitude:
```
χ_0 ~ 1/√(2m_χ V)  (quantum fluctuation amplitude)
```

In a volume V ~ t_Pl³: χ_0 ~ M_Pl^{3/2}/√(m_χ).

But this is a QUANTUM FLUCTUATION, not a classical displacement.
It affects the expectation value of χ² but not ⟨χ⟩. It doesn't
select a vacuum branch.

For vacuum BRANCH selection, we need a classical displacement
of the field. Quantum particle production gives |⟨χ⟩| = 0
(zero-point fluctuation is symmetric).

**Verdict: DEAD.** Particle production doesn't select vacuum
branches (symmetric fluctuation).

### Candidate F (Dissipative reheating)

Gravitational particle production + thermalization. Generic to
any cosmology. Not bounce-specific.

The hidden-sector reheat temperature from the bounce:
```
T_h ~ (m_h² M_Pl² / g_*)^{1/4}
```

This depends on m_h (hidden-sector mass), not bounce parameters.
Different hidden sectors with different m_h get different T_h.

Compare to inflationary reheating:
T_reheat can be adjusted via the inflaton coupling. For
T_reheat ~ T_h: same outcome.

**Verdict: DEAD (not bounce-specific).**

### Candidate G (Domain wall percolation)

Domain walls form during the hidden-sector phase transition.
The bounce doesn't bias percolation because:
- The curvature bias ξR ~ M_Pl² is universal (same for all vacua
  at the same χ²)
- The spin density (J⁵)² is parity-even
- The bias vanishes after the bounce (R → 0)
- Domain wall dynamics are set by the phase transition temperature,
  not the bounce

**Verdict: DEAD (no bounce-specific bias).**

---

## Kill Test O-K2: Can Any Candidate Bridge the 10¹²² Hierarchy?

This is the most brutal test. For each surviving candidate:

### Candidate A (marginal after K1)

ρ_DE = V_false - V_true = ΔV.

ΔV is set by hidden-sector parameters. For ΔV ~ (2.3 meV)⁴:
need potential differences at the meV⁴ scale. The bounce provides
M_Pl² curvature. Where does meV⁴ come from?

**Option 1: Direct potential tuning.** ΔV ~ λv⁴ with λv⁴ tuned
to (meV)⁴. For v ~ TeV: λ ~ 10⁻⁶⁰. This is the CC problem
relocated. FAILS.

**Option 2: Dimensional transmutation.** ΔV ~ Λ_h⁴ where Λ_h is
a dynamically generated scale. Λ_h ~ meV requires α_h(M_Pl) ~
0.009/b. This works but is independent of the bounce (Toy O4).

**Option 3: Near-degenerate vacua.** Two vacua with V₁ - V₂ ~
(meV)⁴ ≪ V₁. This requires tuning the degeneracy to 10⁻¹²²
relative precision. FAILS (tuning moved to degeneracy).

**Option 4: Seesaw.** ΔV ~ v⁴/M² where M is a large scale.
For ΔV ~ (meV)⁴: v⁴/M² = 10⁻⁴⁷ GeV⁴.
For M = M_Pl: v⁴ = 10⁻⁴⁷ × 10³⁶ = 10⁻¹¹ GeV⁴ → v ~ 0.03 GeV.
For M = m_T ~ 10⁹ GeV: v⁴ = 10⁻⁴⁷ × 10¹⁸ = 10⁻²⁹ GeV⁴ →
v ~ 3 × 10⁻⁸ GeV ~ 30 eV.

A seesaw with v ~ 30 meV and M ~ M_Pl gives ΔV ~ (meV)⁴.
But v ~ 30 meV must be explained. Where does this scale come
from? If v is a hidden-sector VEV, it needs its own mass
hierarchy. We've moved the problem.

**No option bridges the hierarchy without introducing a new
unexplained small scale.**

### Candidate D (marginal for PGT after K1)

Same problem. The tunneling outcome (which vacuum) is determined
by the potential. The vacuum energy of the selected vacuum is
ΔV set by hidden-sector parameters.

The exponential sensitivity of tunneling gives:
```
Γ ~ exp(-S_E) with S_E = f(potential parameters, R_b)
```

Even if R_b selects which vacuum the field tunnels TO, the
vacuum energy of that vacuum is set by the potential.

**DEAD on naturalness.** Same hierarchy problem.

---

## Kill Test O-K3: Is There Any Unique Spin-Torsion Contribution?

The (J⁵)² interaction at the bounce:
```
L_eff ⊃ -(3πG/2) (ψ̄γ⁵γ^μψ)²
```

This is:
- Parity-EVEN (pseudovector squared = scalar)
- Planck-suppressed (factor G ~ M_Pl⁻²)
- Universal (couples to ALL fermions equally)
- Contact interaction (zero-range)

For hidden-sector effects:
- Need hidden fermions charged under torsion (automatic for
  any fermion in EC gravity)
- The spin-spin interaction at the bounce: ΔV ~ G n_f² ~
  G × (M_Pl³)² ~ M_Pl⁴. Same scale as curvature coupling.
  No additional information.

**The (J⁵)² interaction provides no unique vacuum-selection
channel.** It's another Planck-scale contribution to the
effective potential, with the same scale as ξR and no special
structure.

**Verdict: No unique spin-torsion effect for vacuum selection.**

---

## Kill Test O-K4: PGT Lower-Scale Bounce

For PGT with m_T ~ 10⁹ GeV:
- ρ_crit ~ 10⁵⁴ GeV⁴
- R ~ 10¹⁸ GeV²
- t_bounce ~ 10⁻³³ s (10¹⁰ longer than ECH)
- ρ_crit/ρ_DE ~ 10¹⁰¹ (still enormous but less extreme)

Does the lower scale help?

The hierarchy is reduced from 10¹²² to 10¹⁰¹ in density ratio
(or 10⁵⁰ in mass ratio M_Pl → 10⁻¹² → m_T → 10⁻²¹ → Λ_DE).

For tunneling (Candidate D in PGT): the longer bounce duration
helps. Need S_E < 4 ln(m_T/m_h) ~ 80. This is achievable for
moderate barriers. But the vacuum energy is still set by
hidden-sector parameters.

For first-order PT (Candidate A in PGT): R ~ m_T² can trigger
transitions at the m_T scale. A hidden sector with transition
temperature T_c ~ m_T could have its transition triggered by
bounce curvature rather than thermal effects. This is more
bounce-specific (R ~ m_T² is unique to the PGT bounce, not
reached during inflation if H_inf < m_T).

But ρ_DE from the transition is still ΔV ~ hidden-sector
potential parameters.

**The PGT bounce is more favorable for timing/triggering but
equally hopeless for naturalness.**

The seesaw attempt in PGT:
ΔV ~ v⁴/(m_T² M_Pl²) with v⁴ = ρ_DE × m_T² M_Pl² = 10⁻⁴⁷ ×
10¹⁸ × 10³⁶ = 10⁷ GeV⁴ → v ~ 50 GeV (EW scale!).

**Interesting numerology:** ρ_DE ~ v_EW⁴ / (m_T² M_Pl²). For
m_T ~ 10⁹ GeV: ρ_DE ~ (200 GeV)⁴ / (10⁹)² × 10³⁶) ~
1.6 × 10⁹ / (10⁵⁴) = 10⁻⁴⁵ GeV⁴. This is 10² above ρ_DE.

Close but wrong by two orders of magnitude, and this is a
coincidence, not a mechanism. Why would ΔV ~ v_EW⁴/(m_T² M_Pl²)?
There's no dynamics that produces this formula.

**Verdict: PGT doesn't help. Hierarchy is structural, not
parametric.**

---

## Summary: Which Candidates Die, Which Survive?

| Candidate | K1 (bounce-specific?) | K2 (hierarchy?) | K3 (torsion?) | K4 (PGT?) | STATUS |
|-----------|:---:|:---:|:---:|:---:|--------|
| A: First-order PT | MARGINAL | DEAD | N/A | No help | **DEAD** |
| B: Metastable trapping | DEAD | — | — | — | **DEAD** |
| C: Biased re-breaking | DEAD | — | — | — | **DEAD** |
| D: Tunneling enhancement | MARGINAL (PGT) | DEAD | N/A | Timing OK | **DEAD** |
| E: Nonadiabatic | DEAD | — | — | — | **DEAD** |
| F: Dissipative reheating | DEAD | — | — | — | **DEAD** |
| G: Domain percolation | DEAD | — | — | — | **DEAD** |

**Zero candidates survive the OOM screening.**

---

## The Structural Reason for Total Failure

The failure is not accidental. There is a structural reason why
NO irreversible mechanism can connect the bounce to ρ_DE:

### The Decoupling Theorem for Bounce → Vacuum Energy

The bounce operates at scale M (= M_Pl or m_T). The late-time
vacuum energy is at scale Λ_DE ~ meV. For a mechanism that
connects them:

```
ρ_DE = f(M, g_i)
```

where g_i are couplings. For ρ_DE ~ Λ_DE⁴ ≪ M⁴:

```
f(M, g_i) ~ g_eff^p × M⁴ with g_eff^p ~ 10⁻¹²²
```

This requires either:
1. g_eff ~ 10⁻¹²²/p (fine-tuned coupling)
2. g_eff ~ exp(-c/α) (dimensional transmutation) — but then
   α is the fundamental parameter, not set by the bounce
3. g_eff ~ (m_low/M)^q (mass ratio) — requires m_low ~ Λ_DE,
   which must be explained

**In every case, the small number (10⁻¹²²) must come from
somewhere outside the bounce dynamics.** The bounce provides M⁴
but not the suppression factor. Adding irreversibility doesn't
help because irreversibility determines WHETHER a transition
occurs, not the ENERGY SCALE of the resulting vacuum.

This is a more general version of the scale-separation barrier
(Barrier 5). It applies to ALL bounce → vacuum energy mechanisms,
irreversible or not:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  BARRIER 13 (tentative): Decoupling of bounce scale         │
│  from vacuum energy                                         │
│                                                             │
│  The bounce operates at M ≫ Λ_DE. Any formula               │
│  ρ_DE = f(M, g_i) requires f to contain a suppression       │
│  factor ~ (Λ_DE/M)^p. This factor cannot be generated       │
│  by bounce dynamics; it must be input as a parameter         │
│  (coupling, mass ratio, or dimensional transmutation         │
│  scale). Adding irreversibility determines WHETHER the       │
│  transition occurs but not the vacuum energy scale.          │
│  The bounce and the late-time vacuum energy are decoupled.   │
│                                                             │
│  This barrier generalizes Barrier 5 (scale separation)       │
│  to cover ALL indirect mechanisms including irreversible     │
│  hidden-sector transitions.                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If confirmed, this would be Barrier 13: the decoupling of the
bounce energy scale from the late-time vacuum energy, applicable
to all direct AND indirect mechanisms.

---

## Could Anything Survive Further Analysis?

### Loophole 1: Landscape + Anthropic + Bounce Trigger

A string landscape with 10^{500} vacua, each with different ρ_DE.
The bounce triggers transitions between landscape vacua. Anthropic
selection picks the one with ρ_DE ~ (meV)⁴.

This works but has nothing specific to the spin-torsion bounce.
Any cosmology with enough energy to trigger landscape transitions
achieves the same. The bounce is decorative.

### Loophole 2: ρ_DE = 0 + small corrections

If there is a mechanism that sets ρ_DE = 0 exactly (supersymmetry
in the vacuum, sequestering, ...), and the bounce provides a
SMALL perturbation:

```
ρ_DE = δρ(bounce) ~ G² × (something)⁴ ~ M_Pl⁻⁴ × Λ⁴ ~ Λ⁴/M_Pl⁴
```

For ρ_DE ~ (meV)⁴: need Λ ~ (meV × M_Pl)^{1/2} ~ 10⁴ GeV (TeV!).

This is the "vacuum energy seesaw": ρ_DE ~ Λ⁴_EW/M_Pl⁴ × M_Pl⁴
= Λ⁴_EW. But Λ⁴_EW ~ (200 GeV)⁴ ~ 10⁹ GeV⁴ ≫ ρ_DE ~ 10⁻⁴⁷ GeV⁴.

Off by 10⁵⁶. Doesn't work.

What about G² instead of G?
```
ρ_DE ~ G² Λ⁸ = Λ⁸/M_Pl⁴
```

For ρ_DE = (meV)⁴: Λ⁸ = (meV)⁴ M_Pl⁴ → Λ = (meV × M_Pl)^{1/2}
~ 10⁴ GeV. Same problem.

### Loophole 3: Exponential of exponential

```
ρ_DE ~ M_Pl⁴ exp(-exp(c/α))
```

For α ~ 0.1 and c ~ 1: exp(-exp(10)) ~ exp(-22026) ~ 0.
Way too small. Need fine-tuning of c/α to get 10⁻¹²².

This is the usual problem with double exponentials: they're
either way too big or way too small, with a razor-thin window
in parameter space.

### None of these loopholes work.
