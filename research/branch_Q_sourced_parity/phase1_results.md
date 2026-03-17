# Branch Q Phase 1 Results: Sourced Parity Violation

**Date:** 2026-03-16
**Branch:** Q (minimal parity-violating extension of ECH)

---

## Verdict: BRANCH_Q_WEAK

---

## Executive Summary

Seven candidate parity-violating extensions of the ECH framework were
assessed. Five were killed at the OOM screening level. Two survive:

1. **Candidate C (dynamical Barbero-Immirzi field):** Geometrically
   motivated, coupling strong enough for birefringence, not excluded.
   Predicts beta ~ 0.1 deg for O(1) misalignment with f_phi ~ M_Pl.
   BUT: phenomenologically identical to a standard ALP after torsion
   elimination. The induced phi F F-tilde coupling is the standard
   ABJ anomaly coefficient, not ECH-specific.

2. **Candidate A (gravitational Chern-Simons):** Produces chiral GWs
   but requires r > 10^{-3} and is standard dCS gravity, not ECH-specific.

**No candidate produces an observable that is both accessible to current
data AND distinctively ECH.**

---

## Strongest Candidate

**Candidate C: Dynamical Barbero-Immirzi field (torsion-axion mixing)**

### What it does right
- One new field (promoted Immirzi parameter), geometrically natural
- One free parameter (f_phi), bounded to Planck scale by geometric origin
- Coupling alpha * N_eff / (4 pi f_phi) ~ 5 * 10^{-21} GeV^{-1} strong enough
- Predicts beta ~ 0.13 degrees, compatible with observed 0.35 +/- 0.09 deg
- Not excluded by any current data

### What it does wrong
- After torsion elimination, identical to any ALP with f_a ~ M_Pl
- The ABJ anomaly coefficient is universal (Adler-Bardeen theorem)
- No new operator beyond standard ALP terms
- Mass m_phi must be added by hand (no natural potential from ECH)
- The Nieh-Yan vertex contributes nothing (38 orders below Route 1)

---

## Observable Produced

**Cosmic birefringence** (isotropic, frequency-independent)

```
beta = [alpha * N_eff / (8 pi)] * (Delta phi / f_phi)
     ~ 0.13 degrees for Delta phi / f_phi ~ 1
```

This is within the observed range but is not an ECH prediction. It is the
standard ALP birefringence prediction with f_a ~ 4 pi f_phi / (alpha N_eff).

---

## Is It Distinctively ECH?

**NO, at the level of observable predictions.** The birefringence prediction
is identical to any ALP with the appropriate decay constant.

**WEAKLY YES, at the level of theoretical priors:**
- f_phi ~ M_Pl is predicted by the Immirzi field identification (not free)
- Direct phi F F-tilde is forbidden (coupling must go through ABJ triangle)
- These are THEORETICAL RESTRICTIONS on the ALP parameter space, not
  new observables

**The honest summary:** The dynamical Immirzi field provides a geometric
motivation for the existence of an ultralight pseudoscalar. It does not
provide any observable that distinguishes it from a generic ALP.

---

## Why WEAK (Not PROMISING, Not CLOSED)

### Why not PROMISING
- No ECH-specific observable signature
- No new operator in the effective theory
- The Nieh-Yan vertex is irrelevant (38 orders below standard ABJ)
- The identification f_phi ~ M_Pl is a prior, not a prediction

### Why not CLOSED
- The birefringence prediction IS consistent with data
- The model IS geometrically well-motivated
- The MCMC fit has not been performed (data could favor or disfavor f_phi ~ M_Pl)
- Calculation 1 (exact torsion elimination) has not been done (small chance
  of new operators at higher order in phi/f_phi)

---

## Does It Open a Real Channel?

**Technically yes: the dynamical Immirzi field produces birefringence.**
The channel is real and matches data.

**Practically no: the channel is not ECH-specific.** Any ALP with
f_a ~ M_Pl produces the same birefringence. The ECH framework does not
provide a distinctive prediction that can be confirmed or refuted
independently of generic ALP constraints.

---

## Recommended Next Step

**Calculation 1: Exact torsion elimination with dynamical gamma**

Solve the torsion equation of motion with gamma(x) = gamma_0 + phi(x)/f_phi
to all orders. Determine whether any new operators appear beyond the
standard ALP terms.

- If new operators found: upgrade to BRANCH_Q_PROMISING
- If no new operators: downgrade to BRANCH_Q_CLOSED (phenomenologically generic)

**Time estimate:** 2-4 hours

**Quick kill:** This calculation is the decisive test. If the answer is
"no new operators," the parity program is over and the project should
either (a) publish a generic ALP constraints paper using existing MCMC
infrastructure, or (b) add the dynamical Immirzi result to the Paper 1.2
closure document as the final negative result.

---

## The Broader Lesson

The ECH framework's parity structure is insufficient to produce distinctive
parity-odd observables. The mechanism is always the same:

1. ECH has parity-odd structure (Holst term, gamma, torsion decomposition)
2. After torsion elimination, all parity-odd structure is absorbed into the
   (J^5)^2 coupling coefficient, which is parity-EVEN
3. The only way to restore parity-odd observables is to add a new pseudoscalar
   field (dynamical gamma, standard ALP, etc.)
4. Any such field produces observables through the STANDARD ABJ anomaly,
   not through ECH-specific operators
5. The ECH origin is invisible in the low-energy effective theory

This is a STRUCTURAL result, not a failure of ingenuity. It follows from
three mathematical facts:
- (J^5)^2 is parity-even (algebraic identity)
- The ABJ anomaly is universal (Adler-Bardeen theorem)
- The Nieh-Yan vertex is Planck-suppressed after torsion elimination

No amount of clever model-building within the ECH framework can overcome
these three facts.

---

## Barrier Count Update

This analysis confirms and sharpens Barrier 8 (parity-even effective
interaction) and Barrier 9 (anomaly universality + Planck suppression)
from previous branches. No new barrier is established, but the two
existing barriers are shown to be robust against the most natural
parity-violating extension (dynamical Immirzi field).

---

## Summary Table

| Item | Result |
|------|--------|
| Candidates screened | 7 (A through G) |
| Candidates surviving OOM | 2 (A, C) |
| Best candidate | C (dynamical Barbero-Immirzi field) |
| Observable | Cosmic birefringence (beta ~ 0.13 deg) |
| ECH-specific? | Theoretical priors only, no distinctive observable |
| Coupling mechanism | Standard ABJ anomaly (not ECH-specific) |
| Nieh-Yan contribution | 38 orders below standard route |
| f_phi prediction | ~ M_Pl (from Immirzi identification) |
| Consistent with data? | YES |
| New operators? | Not yet checked (Calculation 1 needed) |
| Verdict | **BRANCH_Q_WEAK** |
| Next step | Exact torsion elimination with dynamical gamma |
