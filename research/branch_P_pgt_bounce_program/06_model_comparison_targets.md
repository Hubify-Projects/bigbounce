# Model Comparison Targets

**Date:** 2026-03-16

---

## 1. What PGT Bounce Must Be Compared Against

The PGT bounce is one of many alternatives to inflation for the
very early universe. To assess its phenomenological viability and
distinctiveness, it must be compared against:

1. Inflationary models (the dominant paradigm)
2. Other bouncing cosmologies (the direct competitors)

---

## 2. Inflation

### 2a. Slow-roll inflation (generic)

| Observable | Inflation | PGT bounce |
|-----------|----------|-----------|
| n_s | 0.96 -- 0.97 (predicted) | Set by pre-bounce (not predicted) |
| r | 10^{-3} -- 0.06 (model-dep.) | ~10^{-55} (undetectable) |
| f_NL | O(0.01) (slow-roll) | 0 at observable scales |
| GW background | Omega ~ 10^{-15} r (detectable for large r) | 10^{-30} at best (undetectable) |
| Running | dn_s/dlnk ~ -10^{-3} | Set by pre-bounce |
| Reheating | T_reh from inflaton decay | T_bounce from bounce scale |

**Key difference:** Inflation PREDICTS n_s and r. The PGT bounce does
not -- scalar observables are set by the pre-bounce mechanism. This is
a significant disadvantage: the bounce is not falsifiable by n_s or r
measurements because it makes no prediction for them.

### 2b. Starobinsky (R^2) inflation

| Observable | Starobinsky | PGT bounce |
|-----------|------------|-----------|
| n_s | 1 - 2/N ~ 0.965 | Not predicted |
| r | 12/N^2 ~ 0.003 | ~10^{-55} |
| Running | -(n_s-1)^2 ~ -10^{-3} | Not predicted |

Starobinsky is the current best-fit single-field model. It makes
sharp predictions testable by CMB-S4 and LiteBIRD.

**The PGT bounce cannot compete with Starobinsky on predictive
power for CMB observables.** The bounce is transparent (T = 1),
so it predicts nothing.

### What would make PGT competitive

The PGT bounce could compete only if:
1. It predicts something inflation cannot (a unique signature)
2. Or inflation is ruled out (e.g., r < 10^{-4} with specific n_s)

For (1): the only potentially unique PGT prediction is the torsion
relic constraint (if f_T ~ O(1)). This constrains m_T but does not
compete with CMB observables.

For (2): even if inflation is disfavored, the PGT bounce would still
need a pre-bounce mechanism to generate the observed spectrum, making
it a composite model (pre-bounce + bounce) rather than a standalone
alternative.

---

## 3. Loop Quantum Cosmology (LQC)

LQC is the closest competitor to the PGT bounce.

| Property | PGT bounce | LQC bounce |
|----------|-----------|-----------|
| Bounce mechanism | Spin-torsion (contorsion^2) | Holonomy correction |
| rho_crit | m_T^2 M_Pl^2 (tunable) | 0.41 rho_Pl (fixed) |
| Propagating torsion? | YES (mass m_T) | NO |
| Scalar transfer | T(k) = 1 for k << k_b | T(k) ~ 1 for k << k_b |
| GW spectrum | Omega ~ (m_T/M_Pl)^2 | Omega ~ 10^{-6} |
| GW frequency | f_b ~ 10^10 (m_T/M_Pl)^{1/2} | f_b ~ 10^{10} Hz |
| Tensor chirality | Delta chi = 0 | Delta chi = 0 (in simplest models) |
| Pre-bounce needed? | YES (for n_s) | YES (typically) |
| Torsion relic? | YES (if m_T << M_Pl) | NO |

**Key difference:** LQC has a FIXED bounce scale (rho_crit ~ rho_Pl),
while PGT has a TUNABLE one. This gives PGT more parameter space but
also less predictive power.

**Potentially distinctive:** The torsion relic. LQC has no propagating
torsion mode, so the "cosmological moduli problem" from torsion decay
is PGT-specific. If this gives a constraint, it distinguishes PGT from LQC.

---

## 4. Generic Radiation Bounce

A model-independent radiation bounce with:

```
H^2 = (8piG/3) rho (1 - rho/rho_c)
```

for arbitrary rho_c.

| Property | PGT | Generic bounce |
|----------|-----|---------------|
| rho_c | m_T^2 M_Pl^2 | Free parameter |
| a(t) | a_b(1+4alpha^2 t^2)^{1/4} | Same (radiation) |
| GW spectrum | Same shape, amplitude ~ (rho_c/M_Pl^4) | Same |
| Scalar T(k) | = 1 | = 1 |
| Torsion relic? | YES | Model-dependent |

**The PGT bounce IS a specific realization of the generic radiation
bounce.** The only PGT-specific feature is the propagating torsion mode
and its consequences (relic cosmology, mass-coupling lock).

**Without the torsion relic, PGT is observationally indistinguishable
from a generic radiation bounce.** This reinforces the importance of the
torsion relic calculation.

---

## 5. Ekpyrotic / Matter Bounce

| Property | Ekpyrotic | Matter bounce | PGT bounce |
|----------|----------|--------------|-----------|
| Pre-bounce EOS | w >> 1 | w = 0 | w = 1/3 (radiation) |
| n_s | 1 - 2/(epsilon-1) | ~1 (scale-invariant) | Not predicted |
| r | exponentially small | O(1) (problem!) | ~10^{-55} |
| f_NL | O(1) to O(10) | O(1) | 0 at obs. scales |
| Growing mode | Suppressed by w >> 1 | PROBLEM (amplified) | Resolved by symmetry |

**Key comparison:** Ekpyrotic models CAN predict n_s and have distinctive
f_NL signatures. PGT bounce cannot compete on this front.

The matter bounce has a growing mode problem that PGT (and other
time-symmetric bounces) avoid. This is a structural advantage but
not an observable one.

---

## 6. What Would Count as Distinctive

For the PGT bounce to be considered distinctive (not just "another bounce"):

### Minimum bar:

1. **At least one prediction that differs from generic radiation bounce**
   - Candidate: torsion relic constraint on m_T
   - Status: depends on torsion energy fraction calculation

2. **At least one prediction that differs from LQC bounce**
   - Candidate: torsion relic (LQC has no propagating torsion)
   - Status: depends on torsion energy fraction calculation

3. **At least one observable that is not already better predicted by inflation**
   - This is extremely difficult. Inflation predicts n_s, r, f_NL, running.
   - The PGT bounce predicts none of these.
   - The only candidate is the torsion relic constraint, which inflation
     does not address (inflation has its own reheating constraints).

### What would make it competitive:

A concrete BBN/CMB constraint of the form "PGT bounce with m_T in range
[X, Y] GeV is excluded / requires specific parameter values" would be:

- Distinctive (no other bounce model has propagating torsion)
- Data-facing (BBN and CMB data are precise)
- Publishable (constraining a specific gravity theory with cosmological data)

This is a modest bar -- it would not make PGT bounce a competitor to
inflation, but it would make it a well-characterized, observationally
constrained alternative with a unique prediction.

---

## 7. Honest Assessment

### What PGT bounce does well:
- Clean, ghost-free bounce mechanism
- Time-reversal symmetry resolves growing mode
- One-parameter family (m_T) is theoretically elegant
- Concrete UV completion (PGT is a well-defined gauge theory of gravity)

### What PGT bounce does poorly:
- Predicts nothing for CMB observables (n_s, r, f_NL)
- GW background undetectable by 10^{17}
- Scalar sector transparent
- Baryogenesis generic
- Tensor chirality zero

### What remains to be determined:
- Torsion relic cosmology: the ONLY potentially distinctive observable
- If this works: PGT bounce becomes "constrained bouncing cosmology"
- If this fails: PGT bounce is observationally indistinguishable from
  any other radiation bounce

**The model comparison exercise confirms: the torsion relic calculation
is the make-or-break step for PGT bounce phenomenology.**
