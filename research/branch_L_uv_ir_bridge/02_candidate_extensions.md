# Candidate UV→IR Bridge Extensions

**Date:** 2026-03-16

---

## Candidate A: Lower-Scale Bounce in Poincaré Gauge Theory (PGT)

### Mechanism

In standard Einstein-Cartan, torsion is non-propagating and
ρ_crit ~ M_Pl⁴ is fixed by the gravitational coupling. In
Poincaré gauge theory (PGT), torsion propagates with its own
mass m_T and coupling constants. The bounce critical density
becomes a function of the PGT parameters:

```
ρ_crit ~ m_T² M_Pl²
```

(parametric estimate; exact form depends on the specific PGT
Lagrangian). For m_T ≪ M_Pl, this gives ρ_crit ≪ M_Pl⁴.

### How it beats scale separation

The bounce feature frequency scales as ρ_crit^{1/4}:

```
f_b ∝ ρ_crit^{1/4} = (m_T M_Pl)^{1/2}
```

| m_T | ρ_crit^{1/4} | f_b today | Band |
|-----|-------------|-----------|------|
| M_Pl | M_Pl | 40 GHz | None |
| 10⁹ GeV | 10¹⁴ GeV | ~1 Hz | LIGO/ET |
| 10⁵ GeV | 10¹² GeV | ~0.01 Hz | LISA |
| 10 GeV | 10¹⁰ GeV | ~10⁻⁴ Hz | LISA |
| 10⁻¹ GeV | 10⁹ GeV | ~10⁻⁵ Hz | Sub-LISA |

For m_T in the range 10⁵–10⁹ GeV, bounce features fall in the
LISA or LIGO/ET bands.

### Observable channel

**Gravitational waves.** The tensor spectrum through the PGT
bounce would have features (oscillations in P_T(k)) at the
bounce scale k_b. If k_b is in the GW detector bands, these
features are potentially detectable as a modulation of the
stochastic gravitational wave background.

### Biggest theoretical risk

**Foundation A mass-coupling lock.** Foundation A showed that
propagating torsion in PGT has a constraint g_eff ~ 1/(M_Pl √|t₃|)
relating the effective coupling to the PGT parameters. The lock
constrains the viable (m_T, g_T) parameter space. The question
is whether the lock PERMITS ρ_crit in the observable range.

Additionally: lower ρ_crit means a later bounce. The universe
must reach ρ_crit during contraction without other pathologies
(e.g., the universe must not form black holes or undergo other
phase transitions before reaching the bounce).

### Bounce role: ESSENTIAL

The bounce IS the source of the signal. The features in the
GW spectrum are directly tied to the bounce dynamics. No other
mechanism produces the same spectral shape.

---

## Candidate B: Prolonged Near-Bounce Phase (Bounce + Brief Inflation)

### Mechanism

Add a scalar field φ with a flat potential near φ = φ_b. As
the universe bounces, φ is displaced from its minimum by the
curvature coupling (ξRφ²). After the bounce, φ slow-rolls for
N e-folds before decaying, producing a brief inflationary phase.

```
H² = (8πG/3)[V(φ) + ρ_rad(1 - ρ_rad/ρ_crit)]
```

The inflationary phase stretches the bounce-scale modes to
observable scales. N ~ 60 e-folds would be needed for CMB
observability.

### How it beats scale separation

During the inflationary phase, modes exit the Hubble horizon at
k ~ aH_inf (not k ~ k_b). The observable spectrum is generated
by inflation, with the bounce providing initial conditions.

### Observable channel

**CMB scalar spectrum + tensor spectrum.** Standard inflationary
observables (n_s, r, f_NL), potentially modified by the bounce
initial conditions.

### Biggest theoretical risk

**FAIL_JUST_INFLATION.** The predictions are those of inflation.
The bounce provides initial conditions for the inflaton, but the
observables (n_s, r) are determined by the inflationary potential
V(φ). The bounce modifies the pre-inflationary state, which
affects the trans-Planckian initial conditions for inflation —
but this is a well-known subtlety of ALL inflationary models
(not bounce-specific).

### Bounce role: SECONDARY

The bounce sets initial conditions for inflation. The observable
predictions come from inflation. Removing the bounce and
replacing it with a generic initial state (e.g., Bunch-Davies
vacuum) gives nearly identical predictions (the bounce
corrections are suppressed by e^{-2N} for N e-folds).

---

## Candidate C: Time-Asymmetric Bounce (Matter Contraction → Radiation Expansion)

### Mechanism

The contracting phase has a different equation of state than the
expanding phase. Specifically: the contraction is
matter-dominated (w = 0) and the expansion is radiation-dominated
(w = 1/3). The bounce connects the two phases.

```
Contracting phase: a ∝ (-η)²    (matter, w = 0)
Bounce: spin-torsion bounce at ρ = ρ_crit
Expanding phase: a ∝ η          (radiation, w = 1/3)
```

The matter contraction generates a SCALE-INVARIANT scalar
spectrum (P_S ∝ k⁰), solving the horizon problem without
inflation.

### How it beats scale separation

The perturbation spectrum is generated during the CONTRACTION
phase (not at the bounce). The bounce simply transmits the
spectrum from the contracting to the expanding phase. The scale
of the perturbations is set by the contraction dynamics (H during
contraction when modes exit), NOT by ρ_crit.

The time asymmetry (w changes across the bounce) breaks the
T(k) = 1 transfer function. The growing mode of the matter
contraction maps to a MIXTURE of constant and decaying modes
in the radiation expansion, modifying the spectrum.

### Observable channel

**CMB scalar spectrum.** The matter bounce predicts n_s = 1
(exactly scale-invariant) which is marginally disfavored by
Planck (n_s = 0.965 ± 0.004 at 8σ from n_s = 1). However,
corrections from the bounce profile or from the matter-radiation
transition could give n_s < 1.

### Biggest theoretical risk

1. **n_s = 1 vs observed n_s = 0.965:** The basic matter
   bounce gives n_s = 1. Getting n_s < 1 requires additional
   physics (running spectral index, curvature of potential, etc.).

2. **Tensor-to-scalar ratio r ~ O(1):** The matter bounce
   generically predicts r ~ O(1) (too large). Planck requires
   r < 0.03. Suppressing r requires specific model-building
   (e.g., curvaton mechanism within the matter bounce).

3. **What makes the contraction matter-dominated?** Standard
   Model radiation gives w = 1/3 at ALL temperatures above
   the MeV scale. Getting w = 0 during contraction requires
   adding massive matter (a new scalar, dark matter domination,
   etc.) — outside the minimal model.

4. **Anisotropy growth:** In a matter-dominated contraction,
   anisotropic stress grows as 1/a⁶, faster than the matter
   density (1/a³). This is the BKL instability: anisotropy
   dominates before the bounce unless the contraction starts
   from extremely isotropic initial conditions.

### Bounce role: ESSENTIAL (as the contraction→expansion bridge)

The bounce is necessary to connect the contracting and expanding
phases. But the SPECTRUM is generated during contraction, not
at the bounce. The bounce's main role is to transmit the spectrum.

---

## Candidate D: Spectator/Curvaton Field with Bounce-Era Conversion

### Mechanism

A light scalar field σ (spectator) is present alongside the
radiation during contraction. The spectator develops
perturbations during contraction (when modes exit the Hubble
radius). After the bounce, the spectator decays to radiation,
converting its perturbations to curvature perturbations
(curvaton mechanism).

```
L = (∂σ)²/2 + m²σ²/2 + interaction(σ, radiation)
```

The spectator mass m is chosen so that m < H during the
contraction era when CMB modes exit the Hubble radius.

### How it beats scale separation

The spectator perturbations are generated during CONTRACTION,
at energy scales H_exit ≪ M_Pl. The bounce transmits them
unchanged (T = 1). After the bounce, the curvaton conversion
imprints them on the curvature perturbation.

The key scale is NOT k_b but rather k ~ a_exit H_exit (when
modes exit during contraction). By choosing the contraction
history appropriately, observable modes can be addressed.

### Observable channel

**CMB scalar spectrum.** The curvaton mechanism produces a
specific spectral shape determined by m and the contraction
history. Can produce n_s ≈ 0.965 with appropriate parameters.

### Biggest theoretical risk

**FAIL_NOT_BOUNCE_SPECIFIC.** The curvaton mechanism works in
ANY bouncing cosmology. The spin-torsion bounce merely provides
the contraction→expansion transition. Replace it with ANY other
bounce (LQC, ekpyrotic, etc.) and the predictions are nearly
identical.

The only bounce-specific effect: ρ_crit sets the maximum
temperature, which constrains the curvaton parameters
(m < H_max ~ √(ρ_crit/M_Pl²)).

### Bounce role: NECESSARY but NOT SPECIFIC

The bounce is necessary (no contraction→expansion without it),
but any bounce would serve the same purpose.

---

## Candidate E: Torsion-Curvaton (PGT Torsion as Spectator)

### Mechanism

In PGT with propagating torsion, the torsion field itself acts
as a curvaton during contraction. The torsion develops
perturbations during the contraction phase. At or after the
bounce, the massive torsion decays to radiation, converting
torsion perturbations to curvature perturbations.

```
L = L_GR + (kinetic torsion) + m_T² T² + (torsion-matter coupling)
```

The torsion mass m_T and its perturbation spectrum are determined
by the PGT Lagrangian — NOT freely chosen parameters.

### How it beats scale separation

Same as Candidate D: perturbations generated during contraction
at scales H_exit ≪ M_Pl. The conversion happens after the bounce.

The torsion spectrum during contraction:

```
P_T^{torsion}(k) ~ (H_exit/m_T)² × H_exit² / M_Pl²
```

For m_T < H_exit: torsion is effectively massless and develops
a scale-invariant spectrum. For m_T > H_exit: torsion is heavy
and perturbations are suppressed.

### Observable channel

**CMB scalar spectrum** (if torsion perturbations convert to
curvature) or **GW spectrum** (if torsion decays leave a
gravitational wave signature).

### Biggest theoretical risk

**Foundation A mass-coupling lock** constrains the viable
PGT parameter space. The torsion-curvaton requires m_T in a
specific range (light enough to develop perturbations during
contraction, heavy enough to decay after the bounce). The lock
may not permit this range.

### Bounce role: ESSENTIAL and SPECIFIC

The torsion IS the geometric degree of freedom of EC/PGT gravity.
It is naturally present, geometrically motivated, and its dynamics
are set by the same theory that provides the bounce. Other bounce
models (LQC) do NOT have a natural torsion curvaton.

**This is the most torsion-specific candidate.**

---

## Candidate F: Bounce-Triggered Relic Production

### Mechanism

As the universe cools from T ~ T_bounce after the bounce, it
passes through standard particle physics phase transitions
(GUT, EW, QCD). The bounce provides specific initial conditions
for these transitions that could differ from standard hot
Big Bang initial conditions.

Potential relics: topological defects (strings, monopoles),
dark matter production, baryogenesis.

### How it beats scale separation

It doesn't. The phase transitions happen at T ≪ T_bounce
(standard cosmology). The bounce's only effect is on the
INITIAL STATE for these transitions, which is a tiny correction
(suppressed by T_transition/T_bounce).

### Observable channel

Dark matter abundance, baryon asymmetry, gravitational wave
background from phase transitions.

### Biggest theoretical risk

**FAIL_NOT_BOUNCE_SPECIFIC.** The phase transitions and their
relics are standard cosmology. The bounce corrections to the
initial state are negligible (T_EW/T_bounce ~ 10⁻¹⁷).

The one exception: the bounce provides GLOBAL causal connection
(H = 0 → infinite Hubble radius). This could suppress monopole
production (fewer causally disconnected domains). But this is a
NEGATIVE prediction (fewer relics, not distinctive relics).

### Bounce role: MARGINAL

---

## Candidate G: Cyclic Resonance Across Multiple Bounces

### Mechanism

In a cyclic cosmology with repeated bounces, small effects
accumulate over many cycles. A signal of amplitude ε per bounce
grows to N × ε after N bounces (linear accumulation) or
exp(Nε) (resonant accumulation).

### How it beats scale separation

Accumulation over many cycles can amplify tiny per-bounce effects
to observable levels. The TOTAL effect is not limited by a single
bounce.

### Observable channel

Depends on what accumulates: perturbation amplitude, entropy,
curvature, isocurvature, etc.

### Biggest theoretical risk

1. **Entropy growth:** Each bounce increases entropy (second law).
   After N bounces, the entropy is ≫ today's value unless N is
   small or entropy is somehow reset.

2. **What causes re-contraction?** Need a turnaround mechanism
   (dark energy → contraction). This is the most difficult part
   of cyclic models and is NOT provided by EC gravity.

3. **Predictions from contraction, not bounce:** In cyclic
   models (Steinhardt-Turok), the perturbation spectrum comes
   from the ekpyrotic contraction phase, not the bounce.

### Bounce role: NECESSARY but predictions from contraction

---

## Candidate Summary and Ranking

| Candidate | Beats scale sep? | Bounce-specific? | Natural? | Viable? |
|-----------|:---------------:|:----------------:|:--------:|:-------:|
| A: PGT lower scale | **YES** | **YES** | MAYBE | **BEST** |
| B: Bounce + inflation | YES (via inflation) | NO | YES | WEAK |
| C: Matter bounce | YES (via contraction) | Partially | NO (BKL, r) | MODERATE |
| D: Generic curvaton | YES (via contraction) | NO | YES | MODERATE |
| E: Torsion-curvaton | YES (via contraction) | **YES** | MAYBE | **SECOND** |
| F: Relic production | NO | NO | YES | DEAD |
| G: Cyclic | YES (via accumulation) | Partially | NO (entropy) | WEAK |

**Top 2 candidates:**
1. **A: PGT lower-scale bounce** — most bounce-specific, moves
   features to GW detector bands, constrained by Foundation A
2. **E: Torsion-curvaton** — geometrically motivated, torsion-specific,
   but requires PGT extension and is partially constrained by Foundation A
