# 05: Compute Decision

**Created:** 2026-03-17

---

## Should we run the full Branch V Phase 1a calculation now?

$$
\boxed{\textbf{NO — not as currently designed}}
$$

---

## Why not

Phase 1a as designed (classical Bardeen equation on modified Friedmann background) produces:
- n_s = 1 — known since 2002
- f_NL = −35/8 — known since 2009 (our earlier estimate of 5/12 was wrong)
- r ~ 10⁻⁵⁵ — the "no quantum corrections" limit, which is less physical than Wilson-Ewing's LQC result (r ~ 10⁻⁴)
- Transfer function T = 1 for super-Hubble modes — known generically for any transparent bounce

Every one of these results is already in the literature. The only difference is the label "ECH" instead of "LQC" or "generic bounce."

**Spending compute time to reproduce 20-year-old results under a new label is not justified.**

---

## What would justify the compute

### Option A: Derive ECH perturbation corrections first, THEN compute
If we derive the perturbation equations from the ECH action and find corrections that differ from LQC, the numerical computation becomes genuinely new. The workflow would be:
1. Derive ECH perturbation equation (analytic, no compute needed)
2. Identify the ECH-specific correction terms
3. If corrections exist and differ from LQC → run the full numerical evolution with the corrected equation
4. Compare ECH vs LQC vs classical predictions for (n_s, r, f_NL)

This is the path to novelty.

### Option B: Frame as closure/verification
If the goal is not a flagship paper but a quick verification that "ECH gives the same matter-bounce results as expected," then a minimal computation (already partially done in Phase 1a) suffices. But this should be treated as a 1-page appendix item, not a branch-level investment.

### Option C: Pivot to Phase 1b (tilt mechanism)
The n_s = 1 problem is the showstopper. Rather than re-deriving known results, we could investigate whether the ECH framework provides a natural tilt mechanism. The ALP curvaton idea (already present in the ECH framework for birefringence) is the most promising direction. But this should be checked for novelty too — Alexander et al. (2014) already proposed a fermion curvaton in the Fermi-bounce context.

---

## Summary

| Option | Justified? | Novelty | Time investment |
|--------|-----------|---------|----------------|
| Phase 1a as designed | NO | Zero — reproduces known results | Wasted |
| ECH action perturbation derivation → then compute | YES (if corrections found) | Potentially strong | High (theoretical derivation) |
| Quick closure verification | Marginally | None (but tidies up) | Low |
| Pivot to tilt mechanism (ALP curvaton) | Maybe | Needs its own novelty audit | Medium |
