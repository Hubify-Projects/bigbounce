# Foundation A Consistency Check: The Mass-Coupling Lock

**Date:** 2026-03-16

---

## 1. What Foundation A Established

Foundation A (completed 2026-03-13) analyzed PGT propagating torsion
for dark energy applications and found:

### The mass-coupling lock

```
g_eff ~ 1 / (M_Pl √|t₃|)
```

where g_eff is the effective torsion-fermion coupling in the
low-energy theory and |t₃| is the PGT parameter controlling the
torsion mass.

Since m_T = M_Pl / (2√|t₃|), we can rewrite:

```
g_eff ~ m_T / M_Pl² × 2 = 2m_T / M_Pl²
```

**The coupling is proportional to the mass.** Making torsion lighter
simultaneously makes it more weakly coupled. This is the "lock":
mass and coupling are not independent.

### Radiative instability

Foundation A found:
- Graviton loops: δm_T² ~ M_Pl² / (16π²)
- No shift symmetry protection in PGT
- 't Hooft naturalness: FAILS (m_T → 0 does not enhance symmetry
  in the GEOMETRIC sense, because torsion is a connection component)
- Fine-tuning: 1 in 10⁵⁷ for m_T ~ meV

### Foundation A verdict

STRUCTURALLY_VIABLE_BUT_PHENOMENOLOGICALLY_EMPTY for dark energy.
The same |t₃| that makes m_T light kills all distinctive signatures.

---

## 2. Does the Lock Kill the Lower-Scale Bounce?

### Critical distinction: bounce existence vs signal amplitude

The mass-coupling lock has TWO separate effects:

**Effect 1: Bounce critical density.**
ρ_crit ~ m_T² M_Pl² is set by the torsion mass parameter in the
PGT Lagrangian. This is a KINEMATIC property of the background
solution — it depends on m_T², not on g_eff.

The lock does NOT affect ρ_crit. A light torsion (m_T ≪ M_Pl)
still gives a low-scale bounce regardless of coupling.

**Effect 2: Signal amplitude.**
The GW spectral features from the bounce depend on how strongly
the torsion mode couples to tensor perturbations. The coupling
enters the tensor mode equation as a correction:

```
h_k'' + 2(a'/a)h_k' + [k² + δV_torsion(η)]h_k = 0
```

where δV_torsion is the torsion contribution to the effective
potential. The amplitude of δV_torsion is proportional to g_eff².

With the lock: g_eff ~ m_T / M_Pl². The torsion correction to
the tensor potential:

```
δV_torsion / V_GR ~ g_eff² × τ_bounce² ~ (m_T/M_Pl²)² × (n₅/m_T²)²
                   ~ n₅² / (m_T² M_Pl⁴)
```

At the bounce, the fermion number density n₅ ~ ρ_crit^{3/4}
~ (m_T M_Pl)^{3/2}:

```
δV_torsion / V_GR ~ (m_T M_Pl)³ / (m_T² M_Pl⁴) = m_T / M_Pl
```

**The torsion correction to the tensor potential scales as m_T/M_Pl.**

For m_T = 10⁻⁵ GeV (LISA band):
```
δV_torsion / V_GR ~ 10⁻⁵ / 10¹⁹ = 10⁻²⁴
```

**This is catastrophically small.**

---

## 3. Detailed Signal Amplitude Estimate

### Oscillation amplitude in GW spectrum

The bounce produces oscillatory features in the GW spectrum with
amplitude A_osc relative to the smooth background:

```
A_osc ~ δV_torsion / V_GR ~ m_T / M_Pl
```

The GW energy density spectrum:

```
Ω_GW(f) = Ω_GW,smooth(f) × [1 + A_osc × F(f/f_b)]
```

where F is an oscillatory function of order unity near f ~ f_b.

The SMOOTH background Ω_GW from the PGT bounce (vacuum fluctuations
amplified by the bounce):

```
Ω_GW,smooth ~ (ρ_crit^{eff} / M_Pl⁴) × (transfer factors)
             ~ (m_T / M_Pl)² × O(1)
```

### Signal vs sensitivity

**For LISA (m_T ~ 10⁻⁷ GeV, f_b ~ 5 × 10⁻³ Hz):**

```
Ω_GW,smooth ~ (10⁻⁷/10¹⁹)² ~ 10⁻⁵²
A_osc ~ 10⁻⁷/10¹⁹ ~ 10⁻²⁶
Ω_GW,feature ~ 10⁻⁵² × 10⁻²⁶ ~ 10⁻⁷⁸
LISA sensitivity: Ω_GW ~ 10⁻¹³
Gap: 10⁶⁵
```

**For LIGO/ET (m_T ~ 10⁻³ GeV, f_b ~ 0.5 Hz):**

```
Ω_GW,smooth ~ (10⁻³/10¹⁹)² ~ 10⁻⁴⁴
A_osc ~ 10⁻³/10¹⁹ ~ 10⁻²²
Ω_GW,feature ~ 10⁻⁴⁴ × 10⁻²² ~ 10⁻⁶⁶
ET sensitivity: Ω_GW ~ 10⁻¹³
Gap: 10⁵³
```

### The verdict on signal amplitude

> **The mass-coupling lock suppresses the GW signal by 50–65
> orders of magnitude below detector sensitivity.**

The bounce EXISTS at the right frequency, but the SIGNAL is
undetectable. The lock converts the scale-separation problem
into an amplitude-suppression problem.

---

## 4. Can the Lock Be Evaded?

### Attempt 1: Non-minimal torsion-tensor coupling

If the torsion couples to tensor perturbations through a
dimension-4 operator (not via g_eff):

```
L ~ τ² R_{μνρσ} R^{μνρσ} / Λ²
```

For Λ ~ m_T: the coupling ~ τ²/m_T² × R². At the bounce:
```
R ~ ρ_crit / M_Pl² ~ m_T²
```

So:
```
δV ~ τ²/m_T² × m_T⁴ = τ² m_T²
```

With τ ~ n₅/m_T² ~ (m_T M_Pl)^{3/2}/m_T²:
```
δV ~ (m_T M_Pl)³/(m_T⁴) × m_T² = M_Pl³/m_T
```

And V_GR ~ m_T² (at the PGT bounce), so:
```
δV/V_GR ~ M_Pl³/(m_T³) ≫ 1
```

This is TOO LARGE — the perturbation theory breaks down. The
dimension-4 operator overcorrects in the opposite direction.

**Result:** Non-minimal couplings either undercouple (via the lock)
or overcouple (perturbation theory breaks down). No Goldilocks
intermediate.

### Attempt 2: Resonant amplification

If the torsion oscillates coherently during the bounce, the small
per-oscillation coupling can be resonantly amplified:

```
Enhancement ~ exp(μ × N_osc)
```

where μ is the Floquet exponent and N_osc is the number of torsion
oscillations during the bounce.

Number of torsion oscillations: N_osc ~ m_T × t_bounce ~ m_T/m_T = 1.

**Only ~1 oscillation.** No resonant amplification possible. The
bounce duration is set by 1/m_T, and the torsion oscillation period
is also ~1/m_T. There is no parametric separation to exploit.

### Attempt 3: Different PGT sector

In Sector I (spin-0⁺), the coupling structure is different. But
the mass-coupling lock is a GENERAL feature of PGT: the coupling
to matter always goes through the inverse of the same parameter
that sets the mass. This is because the torsion-matter coupling
comes from the minimal coupling prescription (covariant derivative),
and the kinetic normalization of the torsion field involves the
same PGT parameters.

**The lock is sector-independent.**

### Attempt 4: Torsion self-interaction

If the torsion has strong self-interactions (from higher powers
of T² in the PGT action), the torsion amplitude at the bounce
could be enhanced beyond the linear estimate.

However, the PGT action is quadratic in torsion (by construction
of the quadratic PGT). Higher-order terms would require extending
beyond quadratic PGT — a further theory extension on top of
already going from EC to PGT.

**Not available within quadratic PGT.**

---

## 5. Comparison with Foundation A

### Foundation A context (dark energy)

- Target: m_T ~ 10⁻³³ eV (cosmological constant scale)
- Required: |t₃| ~ 10¹⁰⁴
- g_eff ~ 10⁻³³ eV / M_Pl² ~ 10⁻⁶¹ GeV⁻¹
- Signal: completely negligible (10²⁹× weaker than gravity)
- Verdict: PHENOMENOLOGICALLY_EMPTY

### Branch L context (GW bounce features)

- Target: m_T ~ 10⁻⁵ GeV (LISA band)
- Required: |t₃| ~ 10⁴⁸
- g_eff ~ 10⁻⁵ / 10³⁸ ~ 10⁻⁴³ GeV⁻¹
- Signal: 10⁵³–10⁶⁵ below sensitivity
- Verdict: **SAME PROBLEM, DIFFERENT NUMBERS**

### The structural parallel

| Aspect | Foundation A (DE) | Branch L (GW bounce) |
|--------|------------------|---------------------|
| Target mass | 10⁻³³ eV | 10⁻⁵ GeV |
| |t₃| | 10¹⁰⁴ | 10⁴⁸ |
| g_eff suppression | 10⁻⁶¹ GeV⁻¹ | 10⁻⁴³ GeV⁻¹ |
| Signal gap | Enormous | 10⁵³–10⁶⁵ |
| Root cause | Mass-coupling lock | Mass-coupling lock |
| Verdict | EMPTY | **EMPTY** |

**Foundation A's mass-coupling lock is FATAL for the lower-scale
bounce signal, just as it was fatal for dark energy.**

---

## 6. Radiative Stability Revisited

### Foundation A finding: δm² ~ M_Pl²/(16π²)

Graviton loops generate a quadratically divergent correction to the
torsion mass. This is the standard gravitational hierarchy problem.

### Reassessment for Branch L

For the bounce application, the target mass range is
m_T ~ 10⁻⁵ to 10⁷ GeV. The hierarchy:

```
m_T / M_Pl ~ 10⁻¹² to 10⁻²⁴
```

The graviton-loop fine-tuning:

```
δm² / m_T² ~ M_Pl² / (16π² m_T²) ~ 10²⁴ to 10⁴⁸
```

This is severe but comparable to the Standard Model hierarchy
problem (δm_H² / m_H² ~ 10³⁴).

### Technical naturalness argument

In File 02, I argued that m_T → 0 enhances symmetry (massless
limit). Foundation A disputed this for geometric reasons (torsion
is a connection, not a scalar; constant shift broken).

**Resolution:** The disagreement is about which level of description
applies:

- **Geometric level (Foundation A):** The torsion is a connection
  component. Its mass comes from the PGT action structure. A shift
  τ → τ + c changes the connection and is NOT a symmetry of the
  geometric action.

- **Effective field theory level:** After integrating out all
  Planck-mass modes, the low-energy theory is GR + massive
  pseudoscalar τ. In this effective theory, the shift τ → τ + c
  IS a symmetry of the kinetic term (broken only by the mass).
  Standard 't Hooft naturalness applies: radiative corrections to
  m_T² are proportional to m_T² × log(Λ/m_T), not to Λ².

**Which is correct?** Foundation A is correct at the UV (PGT) level.
The EFT argument is correct at the IR level. The graviton loop
δm² ~ M_Pl²/(16π²) is a UV contribution from the PGT level, not
captured by the IR EFT. The hierarchy IS unprotected at the full
PGT level.

**Verdict: Foundation A's radiative instability finding STANDS.**
The mass hierarchy is not protected. This is the same hierarchy
problem as the Higgs, applied to PGT torsion.

---

## 7. Summary: The Lock Reappears

| Question | Answer |
|----------|--------|
| Does the bounce exist at lower scale? | YES (ρ_crit ~ m_T² M_Pl²) |
| Is it ghost-free? | YES (Sector II) |
| Does the lock affect ρ_crit? | NO (kinematic, not coupling-dependent) |
| Does the lock affect signal amplitude? | **YES — FATALLY** |
| Signal suppression | m_T/M_Pl ~ 10⁻¹² to 10⁻²⁶ |
| Gap to detector sensitivity | 10⁵³ to 10⁶⁵ |
| Can the lock be evaded? | NO (4 attempts, all fail) |
| Is the mass hierarchy protected? | NO (graviton loops, same as Foundation A) |
| Is the problem specific to Branch L? | NO (same lock as Foundation A, different scale) |

> **The Foundation A mass-coupling lock reappears in Branch L and
> is FATAL to the signal amplitude. The PGT bounce occurs at the
> right frequency but is undetectable because the torsion-tensor
> coupling is suppressed by the same parameter that lowers the mass.**

### The structural lesson (refined)

> **Lesson 10 (refined): The mass-coupling lock is universal in
> quadratic PGT.** Any attempt to use PGT torsion at a scale
> m_T ≪ M_Pl encounters the same decoupling: g_eff ~ m_T/M_Pl²,
> suppressing all distinctive torsion signatures regardless of
> the application (dark energy, GW bounce features, or anything
> else). This is not a tuning problem but a STRUCTURAL feature of
> the PGT Lagrangian.
