# 05: Best First Calculation Target

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Assessment after dynamical screening

All four candidate models have been screened. The results are sobering:

- **Models A & B** (ALP curvaton): Work as generic curvatons, but the ECH connection is killed by the 75-order-of-magnitude mass incompatibility between the birefringence ALP and the curvaton mass needed for tilt.
- **Model C** (two-field conversion): Already in the literature (Cai & Brandenberger 2011). Not ECH-specific.
- **Model D** (isocurvature transfer): Non-viable (double suppression).

**There is no ECH-motivated curvaton model that simultaneously:**
1. Generates n_s ≈ 0.965
2. Is connected to the birefringence ALP
3. Is distinct from existing literature

---

## If forced to pick the best target

The least-bad option is **Model A: generic quadratic curvaton** in a matter bounce, ignoring the ECH connection entirely.

### What the calculation would look like

1. Specify a spectator scalar σ with mass m_σ ≈ 0.2 H_k
2. Compute δσ spectrum during dust contraction (analytic, using massive Hankel functions)
3. Track δσ through the bounce (trivially: super-Hubble, frozen)
4. Compute curvaton dynamics after bounce: oscillation, decay, conversion to ζ
5. Extract n_s, A_s, f_NL from the curvaton parameters
6. Map the (m_σ, σ_*, Γ_decay) parameter space

### What result would kill it quickly

If the curvaton produces:
- |f_NL| > 10 for the parameter range that gives n_s ≈ 0.965 → killed
- Running α_s in wrong direction or too large → killed
- Requires σ_* > M_Pl (super-Planckian initial displacement) → theoretically suspect

### Why this is not worth doing

**This is exactly the Cai & Brandenberger (2011) calculation** — "The Matter Bounce Curvaton Scenario," arXiv: 1101.0822. They already did it. Our version would differ only in:
1. Using the ECH bounce instead of a generic bounce → but the bounce is transparent to super-Hubble modes, so the curvaton dynamics are identical
2. Possibly using a different curvaton potential → but the quadratic case is already done

**There is no calculation target that is both worth doing and distinct from prior work.**

---

## The honest recommendation

**Do not proceed to a detailed calculation.** The ALP curvaton tilt program does not have enough novelty or ECH connection to justify the investment.

If the goal is to fix the n_s = 1 problem, the cleanest option is the simplest: **acknowledge that the pure matter bounce gives n_s = 1 and that a tilt mechanism (curvaton, w ≠ 0, etc.) is needed, cite the existing literature, and note that the ECH framework does not provide a natural tilt mechanism.**

This is an honest negative result that should be documented, not hidden behind a calculation that reproduces existing work.
