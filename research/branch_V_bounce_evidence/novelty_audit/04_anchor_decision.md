# 04: Anchor Decision

**Created:** 2026-03-17

---

## Decision

$$
\boxed{\textbf{TOO\_CLOSE\_TO\_PRIOR\_WORK}}
$$

as currently conceived (Phase 1a: classical perturbation equation on modified Friedmann background).

With an important caveat — see "Upgrade Path" below.

---

## Reasoning

### Why Branch V is NOT strong enough as flagship

1. **The background calculation is identical to LQC.** The modified Friedmann equation H² = (ρ/3M²)(1 − ρ/ρ_c) is the same. Wilson-Ewing (2013) already solved perturbations through this bounce for dust contraction. Relabeling "LQC" as "ECH" is not a contribution.

2. **n_s = 1 is a 20-year-old result.** Finelli & Brandenberger (2002) established this. Every subsequent paper confirms it. We add nothing.

3. **f_NL = 5/12 was wrong.** The actual matter bounce value is f_NL = −35/8 (Cai et al. 2009). This is a 15-year-old result. Even if we corrected our estimate, it would not be new.

4. **The Phase 1a perturbation calculation (classical Bardeen on modified background) is less complete than Wilson-Ewing (2013).** Wilson-Ewing includes LQC quantum corrections to the perturbation equation, which suppress r to 10⁻⁴. We used the uncorrected classical equation, which gives r ~ 10⁻⁵⁵ — a less physical result.

5. **No ECH-specific perturbation physics was computed.** We did not derive perturbation equations from the ECH action. We did not identify any ECH-specific correction to the Mukhanov-Sasaki equation. We did not show that ECH differs from LQC at the perturbation level.

### Why it might still be worth doing as a consistency test

The only honest framing is: "We verify that the ECH bounce, treated classically at the perturbation level, reproduces the standard matter bounce results." This is a sanity check, not a flagship calculation.

---

## Upgrade Path: What Would Make Branch V Novel

There is exactly one upgrade that would create genuine novelty:

**Derive the ECH perturbation equations from the first-order action (Holst + torsion + matter) perturbed to second order.**

This would:
- Show whether torsion contributes to the perturbation dynamics (not just the background)
- Determine whether ECH gives different corrections than LQC (dressed metric vs ECH torsion perturbation)
- Potentially modify r, f_NL, or even n_s at the quantum-gravity scale
- Test whether the Quintin et al. (2015) no-go theorem is evaded by the modified gravity at the bounce

**If ECH perturbation corrections differ from LQC**, this becomes a genuinely new and publishable result. If they're the same, the negative result ("ECH and LQC perturbation spectra agree") is still worth documenting but is a minor contribution.

This is a harder calculation. It requires:
- Perturbing the first-order (Palatini / Holst) action around FRW
- Identifying the torsion perturbation degrees of freedom
- Integrating out torsion at the perturbed level to get an effective Mukhanov-Sasaki-type equation
- Comparing the effective mass term with the LQC dressed-metric result

This is the calculation that nobody has done. Everything else is in the literature.

---

## Summary

| Question | Answer |
|----------|--------|
| Is Branch V novel as flagship? | **NO** — Phase 1a reproduces known results |
| Is Branch V worth doing as consistency test? | Marginally — confirms ECH reproduces standard matter bounce |
| Is there a path to novelty? | YES — derive ECH perturbation equations from the action |
| Is that path feasible? | Unclear — requires a first-principles perturbation theory calculation in EC gravity |
