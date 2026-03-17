# 02: Closest Prior Work Map

**Created:** 2026-03-17

---

## Top 5 Closest Papers to Branch V

---

### #1. Wilson-Ewing (2013) — arXiv: 1211.6269
**"The Matter Bounce Scenario in Loop Quantum Cosmology"**

| Dimension | Wilson-Ewing 2013 | Our Branch V | Match? |
|-----------|------------------|-------------|--------|
| Contraction phase | Dust (w = 0) | Dust (w = 0) | IDENTICAL |
| Bounce realization | LQC holonomy: H² = (8πG/3)ρ(1 − ρ/ρ_c) | ECH torsion: H² = (ρ/3M²)(1 − ρ/ρ_crit) | IDENTICAL background equation |
| Matter content | Single pressureless fluid | Scalar field (effective dust) | Equivalent |
| Scalar spectrum | n_s ≈ 1 (scale-invariant) | n_s = 1 | IDENTICAL |
| Tilt result | Small red tilt from LQC quantum corrections to perturbation eq | No tilt (classical Bardeen eq on modified background) | DIFFERS — LQC perturbs the perturbation equation itself |
| Non-Gaussianity | Not computed | f_NL = 5/12 (now known to be wrong; literature: −35/8) | N/A |
| Torsion/ECH role | No torsion. LQC holonomy corrections. | ECH torsion modifies Friedmann eq | Different UV completion, same IR equation |
| r (tensor-to-scalar) | r ≈ 9 × 10⁻⁴ (from LQC-dressed Mukhanov-Sasaki) | r ~ 10⁻⁵⁵ (from classical Bardeen on modified background) | DRAMATICALLY DIFFERENT |
| What is missing relative to us | Uses LQC, not ECH. Different perturbation corrections. | ECH perturbation corrections unknown — we used classical perturbation eq on modified background | The key difference is the perturbation equation corrections |

**Verdict:** This is the single most dangerous overlap. Same background equation, same scenario, same n_s = 1 result. The only possible difference is whether the ECH perturbation equation gets quantum-geometry-like corrections that differ from LQC. Wilson-Ewing finds r ~ 10⁻⁴ from LQC corrections; we find r ~ 10⁻⁵⁵ without any such corrections. **If our perturbation equation is just the classical Bardeen equation on the modified background (which is what Phase 1a does), then we are strictly less complete than Wilson-Ewing.**

---

### #2. Cai, Xue, Brandenberger & Zhang (2009) — arXiv: 0903.0631
**"Non-Gaussianity in a Matter Bounce"**

| Dimension | Cai et al. 2009 | Our Branch V | Match? |
|-----------|----------------|-------------|--------|
| Contraction phase | Dust (scalar field) | Dust (scalar field) | IDENTICAL |
| Bounce realization | Ghost condensate / Lee-Wick scalar NEC violation | ECH torsion | DIFFERENT mechanism |
| Matter content | Single canonical scalar | Scalar field | IDENTICAL |
| Scalar spectrum | n_s = 1 | n_s = 1 | IDENTICAL |
| Tilt result | n_s = 1 (no tilt from pure dust) | n_s = 1 | IDENTICAL |
| Non-Gaussianity | f_NL^local = −35/8 ≈ −4.375 | We incorrectly claimed 5/12 | THEIR RESULT IS THE STANDARD ONE |
| Torsion/ECH role | None | ECH bounce | Different bounce, but f_NL generated in contraction (before bounce) |
| What is missing | No ECH. Uses ghost condensate bounce. | We should get same f_NL if contraction is the same | The bounce mechanism is different but the pre-bounce physics is identical |

**Verdict:** This paper establishes f_NL = −35/8 for the matter bounce. The non-Gaussianity is generated entirely during dust contraction, independent of the bounce mechanism. **Our Branch V would get the same f_NL (not 5/12).** The only possible ECH-specific modification is through the bounce transfer, which is O((k/k_b)²) ~ 10⁻⁵⁶ for CMB modes.

---

### #3. Quintin et al. (2015) — arXiv: 1508.04141
**"Evolution of cosmological perturbations and the production of non-Gaussianities through a nonsingular bounce: Indications for a no-go theorem"**

| Dimension | Quintin et al. 2015 | Our Branch V | Match? |
|-----------|---------------------|-------------|--------|
| Contraction phase | Dust | Dust | IDENTICAL |
| Bounce realization | Generic single scalar field | ECH torsion | Different mechanism |
| Matter content | Single scalar | Scalar field | IDENTICAL |
| Scalar spectrum | n_s = 1 | n_s = 1 | IDENTICAL |
| Non-Gaussianity | f_NL enhanced during bounce if r suppressed | Not computed through bounce | CRITICAL — no-go may apply |
| Key result | No-go: can't have small r AND small f_NL in single-field matter bounce | ECH gives r ~ 10⁻⁵⁵ classically — does the no-go apply? | UNKNOWN |
| What is missing | No ECH/torsion-specific analysis | ECH may evade the no-go if torsion modifies the perturbation dynamics | The no-go explicitly assumes Einstein gravity for the bounce |

**Verdict:** This is the most important paper for Branch V's viability. The no-go says: in single-field Einstein gravity, you can't get small r and small f_NL simultaneously in a matter bounce. ECH modifies gravity at the bounce — does it evade the no-go? This is potentially the strongest novelty claim: **testing whether the ECH bounce evades the Quintin et al. no-go theorem.**

---

### #4. Alexander, Bambi, Marcianò, Modesto (2014) — arXiv: 1402.5880
**"Fermi-bounce Cosmology and Scale-Invariant Power Spectrum"**

| Dimension | Alexander et al. 2014 | Our Branch V | Match? |
|-----------|----------------------|-------------|--------|
| Contraction phase | Fermion-dominated (effective dust) | Scalar field dust | Similar but different matter content |
| Bounce realization | EC torsion four-fermion interaction | ECH torsion (spin-fluid) | Both are Einstein-Cartan torsion bounces |
| Matter content | Dirac fermions | Scalar field | DIFFERENT |
| Scalar spectrum | Scale-invariant | n_s = 1 | SAME |
| Tilt result | None (pure scale-invariance) | None | SAME |
| Non-Gaussianity | Not computed | Not correctly computed | BOTH MISSING |
| Torsion role in perturbations | Background only — torsion integrated out | Background only — torsion enters through modified Friedmann | SAME limitation |
| r | Not computed | r ~ 10⁻⁵⁵ (classical) | Not comparable |
| What is missing | No f_NL, no r, no detailed transfer function | Same gaps, different matter content | Very similar level of incompleteness |

**Verdict:** This is the closest torsion-bounce paper. They use actual EC torsion (not LQC), but with fermions instead of scalars, and they don't compute f_NL or r. Our Branch V would essentially be "the scalar-field version of Alexander et al. 2014 with the ECH-specific Friedmann equation." The novelty over this paper is modest — mainly the specific ECH form (Barbero-Immirzi parameter) rather than generic EC.

---

### #5. Cai & Wilson-Ewing (2014) — arXiv: 1412.2914
**"A ΛCDM Bounce Scenario"**

| Dimension | Cai & Wilson-Ewing 2014 | Our Branch V | Match? |
|-----------|------------------------|-------------|--------|
| Contraction phase | CDM + radiation + Λ | Pure dust | MORE REALISTIC than ours |
| Bounce realization | LQC | ECH | Same background equation |
| Scalar spectrum | Nearly scale-invariant with red tilt from Λ | n_s = 1 | THEY GET A TILT (from Λ, not from bounce) |
| Non-Gaussianity | Not primary focus | Incorrectly estimated | N/A |
| Distinguishing prediction | Positive running of n_s | None | They have a better prediction |
| What is missing | No ECH-specific analysis | We have less realistic matter content | They are ahead of us |

**Verdict:** This paper is more complete than our Branch V in every dimension except the specific use of ECH vs LQC. They even get a red tilt (from Λ), which we don't. Our Branch V with pure dust is strictly less developed.

---

## Overall Assessment

The overlap with prior work is **severe**:

1. **n_s = 1** — established by Finelli & Brandenberger (2002), confirmed by everyone since
2. **f_NL** — our estimate of 5/12 was wrong; the correct value is −35/8 (Cai et al. 2009)
3. **Background dynamics** — identical to LQC (Wilson-Ewing 2013)
4. **Torsion bounce spectrum** — done for fermions (Alexander et al. 2014)
5. **No-go theorem** — single-field matter bounce can't have small r + small f_NL (Quintin et al. 2015)

The only clear gap is: **nobody has tested whether the ECH bounce specifically evades the Quintin et al. no-go theorem.**
