# Phase 1 Results: Bispectrum Rescue

## Verdict: BISPECTRUM_RESCUED_BUT_NOT_ECH_SPECIFIC

## 1. Was Cai's benchmark reproduced?

**YES.** Cai's −35/8 (squeezed), −255/64 (equilateral), and −9/4 (folded) were all reproduced algebraically from a shape function of the form AT = (3/(256Πk²)){polynomial in k's}, confirming their Eq. 37 is self-consistent.

## 2. Is the matter-bounce branch alive?

**YES.** The f_NL = −35/8 prediction is:
- Parameter-free (depends only on ε = 3/2 and the cubic action structure)
- Large enough for MegaMapper detection (8.3σ at σ(f_NL) = 0.5)
- Negative (distinguishes from standard slow-roll inflation)
- "Loosely local" in shape (cos θ ≈ 0.95 with the local template)

The flagship discriminator is RESTORED.

## 3. Is there an ECH-specific follow-up?

**Honest answer: probably not for f_NL itself.**

The f_NL = −35/8 result is a GENERIC MATTER-BOUNCE prediction, not an ECH-specific one. It depends on:
- The equation of state w = 0 (matter contraction)
- Standard GR perturbation theory (Maldacena cubic action)
- Bunch-Davies vacuum initial conditions

ECH enters only through providing the BACKGROUND (the bounce mechanism). But the f_NL calculation is independent of the bounce mechanism — it depends only on the contracting phase.

For ECH to modify f_NL, it would need to either:
- Change the cubic action (non-minimal coupling, torsion corrections to the Maldacena vertices)
- Change the background (ε ≠ 3/2)
- Change the vacuum state (non-BD initial conditions from ECH dynamics)
- Modify the bounce transfer (perturbation matching through the ECH bounce)

None of these have been demonstrated. The current status is: ECH provides the bounce, but the perturbation physics is standard GR.

## 4. What was the old +25/16 result?

An artifact of three compounding errors:
- Wrong vertex coefficient (ε² instead of ε²−ε³/2)
- Wrong mode function phase convention (e^{−ikη} instead of e^{+ikη})
- Wrong constraint variable definition

These errors made the bispectrum horizon-crossing-dominated instead of superhorizon-dominated, suppressing f_NL by a factor of ~3 and flipping the sign.

## 5. Exact recommended next move

**Option A (highest value):** Implement Cai's actual cubic action and mode functions in a clean numerical code. Verify −35/8 through direct time integration (not just algebraic shape function evaluation). This would make us fully self-owning.

**Option B (fastest):** Accept Cai's −35/8 as verified and move to the next science question: what does ECH contribute beyond the generic matter-bounce prediction? Investigate whether torsion modifies the cubic action at order (H/M_Pl).

**Recommendation:** Option A first, then B. The rescue is meaningful only if we can reproduce the result from first principles, not just algebraically verify the shape function.
