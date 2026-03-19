# Single Best Remaining Open Path: PBH + Induced GW Second Observable Channel

**Created:** 2026-03-19
**Status:** SELECTED FOR IMMEDIATE EXECUTION

---

## The Answer

**PBH + Induced GW Second Observable Channel.**

This is the consensus answer from BOTH the post-submission roadmap (`post_submission_roadmap/04_single_best_next_program.md`) AND the LQC-specific openings audit (`lqc_specific_openings_audit/03_second_observable_channel_audit.md`). Two independent audits, conducted at different times with different scopes, converged on the same path.

---

## Why It Dominates

### 1. Breaks the single-point-of-failure

The entire focused paper rests on f_NL = -35/8 being detectable by SPHEREx/MegaMapper. This is a strong prediction -- parameter-free, mechanism-independent, verified from three methods -- but it is ONE prediction tested by ONE class of experiments. A second observable family at completely different scales and experiments would transform the architecture from "one number, one chance" to "two independent tests, either of which would be compelling."

### 2. Genuinely independent

| Property | f_NL channel | PBH + GW channel |
|----------|-------------|------------------|
| k-range | 0.002 - 0.2 Mpc^{-1} | 10^5 - 10^15 Mpc^{-1} |
| Observable | Bispectrum amplitude | DM fraction + GW spectrum |
| Experiments | SPHEREx, MegaMapper | PTA, LISA, Einstein Telescope |
| Generation mechanism | Pre-bounce contraction dynamics | Bounce transition dynamics |
| LQC dependence | Weak (contraction is classical) | Strong (bounce sharpness is LQC-specific) |
| Timeline | 2028-2035 | 2030s (LISA), 2035+ (ET) |

### 3. Not touched by ANY previous work in the repo

No calculation in this repository has computed:
- The Wilson-Ewing bounce transfer function T(k) at k ~ k_bounce
- The Bogoliubov coefficient for perturbation enhancement through the LQC bounce
- The PBH mass function from a Wilson-Ewing bounce
- The induced GW spectrum from a Wilson-Ewing bounce

This is genuinely new territory, not a re-verification of known results.

### 4. Clean kill criterion

If the Wilson-Ewing LQC bounce is too smooth at observable scales (T(k) ~ 1 for all k below Planck frequency), the channel is dead. This is determined by a single OOM calculation: characterize the bounce transition and map the enhancement scale to today's frequency/mass. One session.

### 5. Could produce a second paper

If viable: "Primordial Black Holes from the LQC Matter Bounce: Predictions for LISA and Einstein Telescope." Combined with the f_NL paper, this would give the bounce cosmology program two independent, parameter-free predictions -- the most complete observational package from any bouncing cosmology model.

---

## Why Other Paths Are Lower Priority

### LQC formalism sensitivity (#2)
- Most likely null (~85% probability both formalisms agree for superhorizon modes)
- Does not produce a new observable
- Strengthens existing prediction rather than opening a new one
- Worth doing, but after PBH assessment

### Paper 1 framework paper (#3)
- Compilation exercise, not new science
- 75% ready, can be finished anytime
- Does not change the program's observational architecture

### Companion theory paper (#4)
- Same as #3: compilation, not science
- Lower urgency

### Scale-dependent f_NL (#5)
- Permanently below detection threshold (0.14 sigma at MegaMapper)
- Not worth a session

---

## Critical Warning: Frequency-Gate Risk

The chiral GW program (`project_chiral_bounce_GW/phase0_results.md`) established a fundamental structural result:

> A Planck-scale bounce produces Planck-scale signals. The entire observable universe today is the expanded version of a Planck-sized patch. Bounce-scale physics is irretrievably diluted by this expansion.

The characteristic frequency from the bounce is:
```
f_bounce ~ M_Pl * (a_bounce / a_0) ~ 10^{43} Hz * 10^{-30} ~ 10^{13} Hz
```

This is 10 orders of magnitude above LIGO, 16 above LISA, 22 above PTA.

The PBH+GW channel relies on perturbation enhancement at k ~ k_bounce. If the enhanced modes correspond to frequencies ~ 10^{13} Hz, the SAME frequency-gate problem that killed chiral GWs kills PBH+GWs. The key question is whether there is an enhancement mechanism that operates at scales MUCH lower than k_bounce (i.e., for modes that are deeply superhorizon during the bounce).

This is exactly what File 05 must assess.

---

## Expected Outcome

**Probability distribution:**

| Outcome | Probability | Implication |
|---------|------------|-------------|
| Enhancement only at k ~ k_bounce (Planck frequency) | 50-60% | DEAD. Same frequency gate as chiral GW. Modes enhanced at 10^{13} Hz are permanently inaccessible. |
| Enhancement extends to lower k via resonance/parametric amplification | 15-25% | POSSIBLY VIABLE. Need to check if the enhancement reaches asteroid-mass PBH scales (k ~ 10^{12} Mpc^{-1}). |
| Smooth bounce, T(k) ~ 1 everywhere | 20-30% | DEAD. No enhancement at any scale. |

The most probable outcome is that the PBH+GW channel is dead for the Wilson-Ewing LQC bounce, killed by the same frequency-gate physics that killed the chiral GW program. But this must be checked explicitly rather than assumed.

---

## Execution

See File 05 (`05_first_step_execution.md`) for the actual calculation.
