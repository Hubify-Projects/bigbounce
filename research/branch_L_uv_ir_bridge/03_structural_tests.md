# Structural Test Framework for UV→IR Bridge Extensions

**Date:** 2026-03-16

---

## Test L1 — Scale-Separation Test

### Question
Does the extension move bounce-specific features to scales accessible
by current or planned experiments?

### Procedure

1. Identify the characteristic scale of the extension's observable
   signal (k_signal or f_signal).

2. Compare with experimental reach:
   - CMB: k ~ 10⁻⁴ to 0.3 Mpc⁻¹ (f ~ 10⁻¹⁸ Hz)
   - LSS: k ~ 0.01 to 10 Mpc⁻¹
   - PTA: f ~ 10⁻⁹ to 10⁻⁷ Hz
   - LISA: f ~ 10⁻⁴ to 10⁻¹ Hz
   - LIGO/ET: f ~ 1 to 10⁴ Hz
   - CMB distortions: k ~ 1 to 10⁴ Mpc⁻¹
   - BBN: indirect, T ~ MeV

3. Compute the residual suppression factor:
   ```
   S = (signal amplitude at detector) / (detector sensitivity)
   ```
   If S < 1, the signal is undetectable regardless of other merits.

### Pass criterion
S ≥ 1 for at least one planned experiment, with parameters in
a technically natural range.

### Fail label: FAIL_SCALE_SEPARATION

The extension does not actually beat the UV→IR gap. Observable
effects remain at k ~ k_b or are suppressed by (a_b/a_0)^n with
no amelioration.

---

## Test L2 — Essential-Bounce-Role Test

### Question
Is the spin-torsion bounce ESSENTIAL to the mechanism, or merely
decorative backstory?

### Procedure

1. Construct the mechanism's prediction WITH the bounce.
2. Replace the bounce with:
   (a) A generic initial singularity (standard Big Bang)
   (b) A different bounce (LQC, ekpyrotic)
   (c) No bouncing phase at all (pure inflation)
3. Compare predictions.

### Pass criterion
The prediction changes QUALITATIVELY (not just quantitatively)
when the bounce is removed or replaced. Specifically:

- **ESSENTIAL:** Removing the bounce destroys the mechanism entirely.
  The bounce IS the source of the signal.
- **SPECIFIC:** Replacing EC bounce with LQC bounce gives different
  predictions (different ρ_crit, different bounce profile, different
  torsion dynamics).
- **NECESSARY but GENERIC:** Any bounce would serve the same purpose.
  The spin-torsion bounce is one implementation among many.
- **DECORATIVE:** The bounce can be removed entirely with no change
  to predictions.

### Pass levels
- ESSENTIAL + SPECIFIC: full pass
- ESSENTIAL but not SPECIFIC: partial pass (still promising)
- NECESSARY but GENERIC: marginal (publishable but weak)
- DECORATIVE: fail

### Fail label: FAIL_NOT_BOUNCE_SPECIFIC

The mechanism works without the bounce or works identically with
any bounce. The spin-torsion bounce plays no essential role.

---

## Test L3 — Theoretical-Coherence Test

### Question
Is the extension ghost-free, stable, and within the domain of
validity of its effective field theory?

### Procedure

For each extension, check:

1. **Ghost freedom:** The kinetic matrix has positive eigenvalues
   for all propagating degrees of freedom. Specifically:
   - Scalar sector: Q_S > 0
   - Tensor sector: Q_T > 0
   - Torsion sector (if propagating): Q_torsion > 0

2. **Gradient stability:** Sound speeds are real and subluminal:
   - c_S² > 0 (no gradient instability)
   - c_S² ≤ 1 (no superluminal propagation, or at least
     c_S² ≤ c_front² for causal consistency)

3. **EFT validity:** The energy scale of the mechanism is below the
   EFT cutoff:
   - For PGT: E_signal < Λ_PGT (cutoff of the PGT EFT)
   - For spectator fields: m_σ < H_exit (light during mode exit)

4. **Unitarity:** No tree-level unitarity violation at the scales
   where the mechanism operates.

5. **Absence of strong coupling:** The perturbative expansion is
   valid (coupling constants < 1 at relevant scales).

### Pass criterion
All five checks satisfied for at least one viable parameter point.

### Fail label: FAIL_PATHOLOGY

The extension introduces ghosts, gradient instabilities, strong
coupling, or operates outside EFT validity. Not curable by
parameter tuning.

---

## Test L4 — Distinctiveness Test

### Question
Does the predicted signal differ from generic inflationary or
standard-cosmology predictions?

### Procedure

1. Identify the predicted observable(s) (spectrum shape, amplitude,
   frequency, polarization, non-Gaussianity, etc.).

2. Compare with:
   (a) Generic slow-roll inflation predictions
   (b) Standard ΛCDM predictions
   (c) Other bounce model predictions (LQC, ekpyrotic, matter bounce)

3. Ask: Is there a measurement that could distinguish the extension's
   prediction from ALL of (a), (b), (c)?

### Pass criterion
There exists at least one observable O such that:
- O(this extension) ≠ O(inflation) at detectable significance
- O(this extension) ≠ O(ΛCDM) at detectable significance
- Ideally: O(this extension) ≠ O(other bounces)

### Fail labels

- **FAIL_JUST_INFLATION:** The mechanism reduces to "inflation
  happens after the bounce" with the bounce providing only initial
  conditions suppressed by e^{-2N}.

- **FAIL_TOO_TUNED:** The mechanism requires couplings or initial
  conditions tuned to the DE or CMB scale without symmetry protection.
  A mechanism requiring ξ ~ 10⁻¹²² is dead.

---

## Test L5 — Cheap-Kill Test

### Question
Can the candidate be eliminated by a single order-of-magnitude
estimate without detailed calculation?

### Procedure

For each candidate, attempt the following quick kills:

1. **Amplitude kill:** Estimate the signal amplitude. If it is
   more than 10 orders of magnitude below sensitivity, kill.

2. **Parameter-space kill:** Check if the required parameters
   violate known constraints (collider, astrophysical, gravitational).
   A single violated bound kills the candidate.

3. **Counting kill:** Count free parameters. If the extension
   requires ≥ 5 free parameters to produce an observable signal,
   flag as over-engineered (not an automatic kill, but a demerit).

4. **Existing-bound kill:** Check if the predicted signal in ANY
   channel is already excluded by existing data (e.g., BBN, CMB,
   pulsar timing).

5. **Naturalness kill:** Check if the required parameter values
   are technically natural. If a coupling must be tuned to better
   than 1 part in 10⁶ without symmetry protection, kill.

### Pass criterion
Survives all five quick kills.

### Fail label: FAIL_SCALE_SEPARATION (if amplitude kill)
or appropriate specific label.

---

## Combined Scorecard

| Candidate | L1 Scale | L2 Bounce role | L3 Coherence | L4 Distinct | L5 Kill | Verdict |
|-----------|:--------:|:--------------:|:------------:|:-----------:|:-------:|:-------:|
| A: PGT lower scale | | | | | | |
| B: Bounce + inflation | | | | | | |
| C: Matter bounce | | | | | | |
| D: Generic curvaton | | | | | | |
| E: Torsion-curvaton | | | | | | |
| F: Relic production | | | | | | |
| G: Cyclic | | | | | | |

### Verdict labels

- **SURVIVES_PHASE1:** Passes L1–L5. Recommended for Phase 2
  (detailed calculation).
- **CONDITIONAL:** Passes most tests but has one unresolved issue
  that requires calculation to settle.
- **FAIL_SCALE_SEPARATION:** Does not beat UV→IR gap.
- **FAIL_NOT_BOUNCE_SPECIFIC:** Bounce is decorative.
- **FAIL_PATHOLOGY:** Theoretical inconsistency.
- **FAIL_TOO_TUNED:** Unnatural parameter requirements.
- **FAIL_JUST_INFLATION:** Reduces to inflation + decorative bounce.

---

## Application Order

Tests should be applied in order L5 → L1 → L2 → L4 → L3:

1. **L5 first** (cheap kill): Eliminate candidates quickly before
   investing effort.
2. **L1 second** (scale separation): The whole point of Branch L.
   If this fails, nothing else matters.
3. **L2 third** (bounce role): A candidate that beats scale
   separation but doesn't need the bounce is not useful for the
   spin-torsion program.
4. **L4 fourth** (distinctiveness): Ensures the signal is not
   degenerate with inflation or ΛCDM.
5. **L3 last** (coherence): Only invest in detailed stability
   analysis for candidates that pass L1–L2–L4.
