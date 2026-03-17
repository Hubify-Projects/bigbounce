# Final Verdict: Branch V Novelty Audit

**Created:** 2026-03-17

---

## 1. What is the closest prior literature?

**Wilson-Ewing (2013), arXiv: 1211.6269** — "The Matter Bounce Scenario in Loop Quantum Cosmology"

This paper solves the exact same scenario (dust contraction → bounce → expansion) with the exact same modified Friedmann equation (H² = (8πG/3)ρ(1 − ρ/ρ_c)). It computes scalar and tensor perturbation spectra through the bounce, including LQC quantum-geometry corrections that suppress r to ~10⁻⁴. It gets n_s ≈ 1.

Also critically close:
- Cai et al. (2009): f_NL = −35/8 for matter bounce (the standard non-Gaussianity result)
- Alexander et al. (2014): scalar spectrum through an Einstein-Cartan torsion bounce (Fermi-bounce)
- Quintin et al. (2015): no-go theorem for single-field matter bounce (r vs f_NL tension)

---

## 2. Is f_NL = 5/12 itself novel?

**NO. And it is WRONG.**

- f_NL = 5/12 is the Maldacena (2003) coefficient for single-field slow-roll inflation. It has nothing to do with the matter bounce.
- The correct matter bounce result is **f_NL^local = −35/8 ≈ −4.375** (Cai et al. 2009).
- This value is generated during dust contraction, independent of the bounce mechanism.
- It has been known for 15+ years. It is not novel in any context.
- Our Phase 1a file `06_fNL_estimate.md` contains an incorrect derivation and must be corrected or discarded.

---

## 3. What is the strongest honest novelty claim for Branch V?

**"Determine whether the ECH perturbation equation differs from the LQC dressed-metric equation, and if so, whether this changes the matter-bounce predictions for r and f_NL."**

This requires deriving the perturbation equation from the Einstein-Cartan-Holst action (first-order formalism with torsion) perturbed to second order around FRW. This has NOT been done in the literature.

If the ECH corrections differ from LQC:
- New predictions for r (different from Wilson-Ewing's 10⁻⁴)
- Potentially different f_NL behavior through the bounce
- Test of the Quintin et al. no-go theorem in modified gravity

If the ECH corrections are the same as LQC:
- Negative result, still publishable as a comparison
- Confirms universality of the effective LQC equation

**Everything below this level of analysis (classical Bardeen on modified background) is already done.**

---

## 4. Should we proceed to the full scalar-spectrum calculation?

**NO — not with the Phase 1a design (classical perturbation equation on modified background).**

That calculation reproduces Wilson-Ewing (2013) with a different label. It is not worth the time.

**YES — if we first derive the ECH perturbation equation from the action and find it differs from the classical equation or from LQC.**

---

## 5. What is the exact next move?

### Recommended: Assess feasibility of ECH perturbation derivation

Before committing to any more computation, answer one question:

> **Can we derive the Mukhanov-Sasaki-type equation from the ECH action (first-order Palatini + Holst term + spinor matter) perturbed around FRW, and does torsion contribute correction terms at the perturbation level?**

This is a theoretical (pen-and-paper / analytic) question, not a computational one. Steps:

1. Write the ECH action (Holst + Dirac or scalar matter)
2. Perturb e^a_μ (vierbein) and ω^{ab}_μ (spin connection) around FRW
3. Identify torsion perturbation degrees of freedom
4. Integrate out torsion at the perturbed level
5. Extract the effective Mukhanov-Sasaki equation
6. Compare effective mass term with: (a) classical z''/z, (b) LQC dressed-metric correction

If step 5 gives the classical equation → Branch V is dead (no novelty beyond LQC).
If step 5 gives an ECH-specific correction → Branch V is alive with genuine novelty.

### Alternative: Pivot away from Branch V

If the ECH perturbation derivation is too difficult or produces the classical equation, Branch V should be closed. The remaining ECH predictions (cosmic birefringence from ALP, bounce itself) stand independently and don't need the matter-bounce power spectrum calculation.

---

## Bottom Line

> Branch V as Phase 1a (classical perturbation on modified background) is **a reproduction of Wilson-Ewing (2013)**. The f_NL = 5/12 claim was wrong. The real matter-bounce f_NL is −35/8, known since 2009. The n_s = 1 result is from 2002. There is no novel prediction.
>
> The only path to genuine novelty is deriving whether ECH gives different perturbation-level corrections than LQC. This is an analytic theory question that should be answered before any further computation.
