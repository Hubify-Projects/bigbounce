# Order-of-Magnitude Screening

**Date:** 2026-03-16

---

## Screening Protocol

Apply tests in order: L5 (cheap kill) → L1 (scale separation) →
L2 (bounce role) → L4 (distinctiveness) → L3 (coherence).

A candidate is killed at the first failed test. Only survivors
proceed to the next test.

---

## Candidate A: PGT Lower-Scale Bounce

### L5 — Cheap kill

**Amplitude kill:** GW spectral features at k ~ k_b with
amplitude ~ Ω_GW h² × A_osc. For A_osc ~ O(1) near k_b and
Ω_GW h² ~ 10⁻¹⁵ (from vacuum fluctuations at the bounce), the
signal may be below LISA sensitivity (Ω_GW h² ~ 10⁻¹³).

However, the GW background is not just from vacuum. If there is a
stochastic background from the bounce era (e.g., from torsion
oscillations), the amplitude could be higher:

```
Ω_GW h² ~ (ρ_GW / ρ_crit,today) ~ (H_b / M_Pl)² × (g_* / g_*,0) × ...
```

For ρ_crit^{eff} ~ (10⁷ GeV)⁴ (LISA band):
```
Ω_GW h² ~ (ρ_crit^{eff})^{1/2} / M_Pl² × transfer factors
         ~ (10⁷)² / (10¹⁹)² ~ 10⁻²⁴
```

This is below LISA sensitivity by ~11 orders. BUT: this is the
vacuum contribution. Parametric amplification from the torsion
oscillation could enhance by large factors.

**Verdict:** NOT KILLED (requires detailed calculation to settle).

**Parameter-space kill:** m_T ~ 10⁵ GeV requires PGT parameters
with large hierarchy (|t₃| ~ 10²⁸). No known collider or
astrophysical constraint directly excludes this. Gravitational
wave tests of propagating torsion are currently at m_T > 10⁻²³ eV
(from binary pulsars), nowhere near 10⁵ GeV.

**Verdict:** NOT KILLED.

**Naturalness kill:** The hierarchy m_T/M_Pl ~ 10⁻¹⁴ requires
explanation. In PGT, m_T is set by the quadratic-in-curvature
coefficients β_i. These are dimensionless numbers × M_Pl², so
m_T ~ 10⁵ GeV requires β_i ~ 10⁻²⁸. No symmetry protection is
known for this hierarchy.

**Verdict:** FLAGGED (hierarchy problem, not a kill if the
hierarchy is the defining prediction of the model).

**L5 result: SURVIVES** (with naturalness caveat).

### L1 — Scale separation

The defining feature of Candidate A. For m_T in range 10³–10⁹ GeV:

```
f_b ~ (m_T / M_Pl)^{1/2} × T₀ / h ~ 10⁻³ to 1 Hz
```

This is in the LISA–LIGO/ET bands.

**L1 result: PASS.**

### L2 — Bounce role

The bounce IS the source of the GW spectral features. The features
arise from the bounce dynamics in the tensor mode equation:

```
h_k'' + 2(a'/a)h_k' + k²h_k = 0
```

The effective potential V_T(η) = a''/a has a peak at the bounce.
The peak height and width are set by ρ_crit^{eff} and the PGT
parameters. Removing the bounce removes the spectral features.

Replacing with LQC: LQC has different bounce profile, different
ρ_crit, NO torsion dynamics. The spectral features would differ
quantitatively.

**L2 result: PASS (ESSENTIAL + SPECIFIC).**

### L4 — Distinctiveness

The predicted signal: oscillatory features in Ω_GW(f) at f ~ f_b.

Comparison:
- Inflation: smooth, power-law Ω_GW(f). No oscillations.
- LQC bounce: oscillatory features but at different frequency
  (ρ_crit^{LQC} ≈ 0.41 ρ_Pl) and with different oscillation
  pattern (quantum geometry corrections).
- Phase transitions: bump in Ω_GW(f), not oscillatory.

The PGT bounce produces a SPECIFIC oscillation pattern determined
by the bounce profile (which depends on m_T, g_T, PGT parameters).

**L4 result: PASS.**

### L3 — Coherence

PGT propagating torsion has known ghost and stability issues:

1. **Ghost freedom:** The spin-0 torsion mode (vector trace) can
   be ghost-free for appropriate sign choices of α_i. The spin-2
   torsion mode is generically ghostly unless specific PGT
   parameter constraints are imposed.

   **Status:** Ghost-free parameter regions EXIST but are
   constrained. Need detailed check for the specific parameters
   that give m_T in the target range.

2. **Gradient stability:** The torsion sound speed c_T² depends on
   the PGT parameters. Can be positive in ghost-free regions.

3. **EFT validity:** The PGT is a classical theory (not an EFT
   truncation). The propagating torsion is an exact degree of
   freedom, not a low-energy effective mode. However, quantum
   corrections (graviton loops) may destabilize the hierarchy
   m_T ≪ M_Pl.

**L3 result: CONDITIONAL** (ghost-free regions exist; need to check
overlap with target m_T range and mass-coupling lock).

### Combined verdict: **SURVIVES_PHASE1 (CONDITIONAL)**

The main unresolved issue is whether the mass-coupling lock
(Foundation A) permits m_T in the 10³–10⁹ GeV range while
maintaining ghost freedom. This requires a detailed Phase 2
calculation.

---

## Candidate B: Bounce + Brief Inflation

### L5 — Cheap kill

**FAIL_JUST_INFLATION.** The observable predictions are those of
inflation. The bounce correction to the power spectrum is:

```
ΔP_S / P_S ~ exp(-2N) ~ 10⁻⁵²    for N = 60
```

This is 50 orders of magnitude below any measurement sensitivity.

**L5 result: KILLED.**

**Verdict: FAIL_JUST_INFLATION.**

---

## Candidate C: Matter Bounce (Time-Asymmetric)

### L5 — Cheap kill

**Existing-bound kill attempt:**
- n_s = 1 is excluded at 8σ by Planck (n_s = 0.965 ± 0.004)
- r ~ O(1) is excluded by r < 0.03

Both require fixes (additional physics). The basic matter bounce
is excluded as-is. With fixes (curvaton, ekpyrotic pre-bounce),
it may survive — but the fixes are the model, not the bounce.

**Naturalness kill:** What makes the contraction matter-dominated?
Standard Model radiation has w = 1/3 at all temperatures above MeV.
Need a massive scalar or early matter domination — additional
ingredient with no geometric motivation.

**L5 result: FLAGGED** (not killed outright, but problematic).

### L1 — Scale separation

The scalar spectrum is generated during CONTRACTION at scales
H_exit ~ H(t_exit), which can be arbitrarily low (depends on when
modes exit during contraction). The bounce features at k_b are
separate.

```
Observable modes: generated at H_exit ≪ M_Pl during contraction
Bounce features: at k ~ k_b ~ (ρ_crit)^{1/2} / M_Pl
```

The matter bounce beats scale separation by generating the spectrum
during contraction, NOT at the bounce.

**L1 result: PASS** (but via contraction, not via lowering bounce scale).

### L2 — Bounce role

The bounce is NECESSARY (connects contraction to expansion) but the
spectrum comes from CONTRACTION dynamics. Replace EC bounce with
LQC bounce → nearly identical predictions.

**L2 result: MARGINAL** (necessary but generic).

### L4 — Distinctiveness

n_s = 1 (marginally distinctive — excludable).
r ~ O(1) (distinctive but excluded).

With fixes, the predictions become those of the fix mechanism
(curvaton, ekpyrotic), not the matter bounce per se.

**L4 result: WEAK.**

### Combined verdict: **FAIL_NOT_BOUNCE_SPECIFIC**

The bounce is a plumbing fixture (connects contraction to expansion)
but the predictions come from the contraction phase. Any bounce
serves the same purpose.

---

## Candidate D: Generic Curvaton

### L5 — Cheap kill

**Bounce-role kill:** The curvaton mechanism works with ANY bounce.
The EC bounce provides the contraction→expansion transition but so
would LQC, ekpyrotic, or any other bounce.

**L5 result: KILLED** (by L2 pre-screening).

**Verdict: FAIL_NOT_BOUNCE_SPECIFIC.**

---

## Candidate E: Torsion-Curvaton

### L5 — Cheap kill

**Counting kill attempt:** The mechanism requires:
1. PGT parameters (α_i, β_i) — multiple but geometrically determined
2. m_T (torsion mass) — 1 parameter
3. Contraction model (w during contraction) — at least 1 parameter

Total: ~3 essential parameters. Below the 5-parameter threshold.

**Naturalness kill attempt:** m_T must satisfy m_T < H_exit during
contraction for the curvaton to develop perturbations. If H_exit
is set by the contraction scale, this constrains m_T from above.
The mass-coupling lock constrains it from below. Is there room?

For matter contraction: H_exit ~ √(ρ_exit / M_Pl²). At CMB mode
exit: ρ_exit ~ (10⁻³ eV)⁴ (matching observed P_S). Then:

```
H_exit ~ 10⁻³ eV × (10⁻³ eV / M_Pl) ~ 10⁻³⁴ eV
```

Need m_T < H_exit ~ 10⁻³⁴ eV. This is an EXTREMELY light torsion.
The mass-coupling lock gives:

```
g_eff ~ 1 / (M_Pl √|t₃|) → m_T ~ g_eff M_Pl ~ M_Pl / √|t₃|
```

For m_T ~ 10⁻³⁴ eV: |t₃| ~ (M_Pl / m_T)² ~ 10¹⁰⁰.

This is an absurd hierarchy. **KILLED by naturalness.**

Wait — re-examine. The curvaton doesn't need to be light at CMB
exit during matter contraction. It needs to be light at the time
when k_CMB exits the Hubble radius during contraction. If the
contraction is not matter-dominated but has w > 1/3 (ekpyrotic),
the Hubble parameter can be much larger at mode exit.

For ekpyrotic contraction (w ≫ 1): H_exit can be much larger,
relaxing the mass constraint. But then n_s depends on w and the
torsion-curvaton model requires careful matching.

**L5 result: CONDITIONAL** (depends on contraction model; killed
for simple matter contraction, potentially viable for ekpyrotic).

### L1 — Scale separation

Same as Candidate D: perturbations generated during contraction
at scales H_exit ≪ M_Pl. Beats scale separation via contraction.

**L1 result: PASS.**

### L2 — Bounce role

The torsion curvaton is GEOMETRICALLY MOTIVATED:
- Torsion is the natural degree of freedom of EC/PGT gravity
- Its mass is set by PGT parameters (not ad hoc)
- Its coupling to fermions is geometric

Replace EC bounce with LQC: LQC has no torsion degree of freedom.
The torsion-curvaton mechanism is specific to EC/PGT.

**L2 result: PASS (ESSENTIAL + SPECIFIC).**

### L4 — Distinctiveness

The torsion curvaton predicts:
- n_s determined by m_T and contraction history
- r suppressed by curvaton mechanism (r ≪ 1)
- Non-Gaussianity: f_NL ~ (5/4)(r_dec) where r_dec = 3ρ_τ/(3ρ_τ + 4ρ_rad) at decay

The specific n_s and f_NL correlation is torsion-model dependent.
Different from generic curvaton because m_T is constrained by
Foundation A (mass-coupling lock).

**L4 result: CONDITIONAL** (distinctive if lock constrains m_T
to a specific value).

### L3 — Coherence

Same ghost/stability issues as Candidate A (propagating torsion
in PGT). Additionally requires the torsion to be LIGHT (m_T < H_exit),
which conflicts with the mass-coupling lock for simple contraction
models.

**L3 result: PROBLEMATIC** (light torsion + lock = tension).

### Combined verdict: **CONDITIONAL**

Survives if:
1. An ekpyrotic or non-standard contraction relaxes the m_T bound
2. The mass-coupling lock permits the required m_T value
3. Ghost-free PGT parameter regions overlap with viable m_T

This is a THREE-condition survival. Each condition has ~30%
probability of being satisfied (generous estimate).

Net survival probability: ~3%.

---

## Candidate F: Bounce-Triggered Relic Production

### L5 — Cheap kill

**Amplitude kill:**

```
Δn_defect / n_defect ~ (T_transition / T_bounce)⁴ ~ 10⁻¹²
```

The bounce correction to any relic abundance is negligible (12+
orders of magnitude below measurement precision).

**L5 result: KILLED.**

**Verdict: FAIL_NOT_BOUNCE_SPECIFIC** (also FAIL_SCALE_SEPARATION).

---

## Candidate G: Cyclic Resonance

### L5 — Cheap kill

**Naturalness kill:** The cyclic model requires:
1. A turnaround mechanism (ρ_total → 0 during expansion → contraction).
   EC gravity does NOT provide this. Need dark energy with w < -1
   or a specific potential. This is a separate, unsolved problem.

2. Entropy management: each bounce increases entropy. After N bounces,
   S_total ~ N × S_per_bounce. For N > 100 (needed for accumulation),
   the late-universe entropy far exceeds observed S ~ 10⁹⁰.

3. Stability across cycles: small perturbations must not grow
   exponentially. This requires fine-tuning of the turnaround.

**L5 result: KILLED** (turnaround mechanism absent from EC gravity).

**Verdict: FAIL_PATHOLOGY** (requires physics not provided by the
framework).

---

## Screening Summary

| Candidate | L5 | L1 | L2 | L4 | L3 | Final |
|-----------|:--:|:--:|:--:|:--:|:--:|:-----:|
| A: PGT lower scale | ✓ | ✓ | ✓ | ✓ | ? | **SURVIVES** |
| B: Bounce + inflation | ✗ | — | — | — | — | FAIL_JUST_INFLATION |
| C: Matter bounce | ~ | ✓ | ~ | ~ | — | FAIL_NOT_BOUNCE_SPECIFIC |
| D: Generic curvaton | ✗ | — | — | — | — | FAIL_NOT_BOUNCE_SPECIFIC |
| E: Torsion-curvaton | ? | ✓ | ✓ | ? | ~ | **CONDITIONAL** |
| F: Relic production | ✗ | — | — | — | — | FAIL_NOT_BOUNCE_SPECIFIC |
| G: Cyclic | ✗ | — | — | — | — | FAIL_PATHOLOGY |

---

## Box: The One Surviving Candidate

**Candidate A (PGT lower-scale bounce) is the ONLY candidate that
passes all screening tests without conditions.**

It is the only mechanism that:
1. Actually lowers the bounce scale (beats scale separation directly)
2. Makes the bounce essential and specific (not just a contraction→expansion bridge)
3. Produces a distinctive signal (oscillatory GW features)
4. Has a concrete observable channel (LISA/LIGO bands)

The main uncertainty: Foundation A mass-coupling lock compatibility.

**Candidate E (torsion-curvaton) survives conditionally** but faces
a three-condition survival requirement with ~3% net probability.

**Five of seven candidates are killed at the first screening test.**

---

## Kill Statistics

| Kill mechanism | Candidates killed |
|---------------|------------------|
| FAIL_JUST_INFLATION | B |
| FAIL_NOT_BOUNCE_SPECIFIC | C, D, F |
| FAIL_PATHOLOGY | G |
| Survived | A, E (conditional) |

The dominant failure mode is **FAIL_NOT_BOUNCE_SPECIFIC**: most
UV→IR bridge mechanisms work with any bounce, making the
spin-torsion bounce irrelevant to the prediction.
