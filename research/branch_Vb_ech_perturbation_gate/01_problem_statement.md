# 01: Problem Statement — ECH Perturbation Feasibility Gate

**Created:** 2026-03-17
**Status:** COMPLETE

---

## What the novelty audit found

The Branch V dust-contraction → ECH bounce → radiation expansion program, as implemented in Phase 1a, is **too close to prior work**:

1. **Wilson-Ewing (2013)** solves the identical scenario with the identical modified Friedmann equation (from LQC instead of ECH). Same n_s = 1 result.
2. **Cai et al. (2009)** established f_NL = −35/8 for the matter bounce 15 years ago.
3. **Alexander et al. (2014)** computed the scalar spectrum through an actual Einstein-Cartan torsion bounce (Fermi-bounce).
4. Our Phase 1a used the **classical Bardeen equation on the modified Friedmann background** — the same calculation that LQC papers already performed, with a different label.

## Why the classical treatment is not novel

In Phase 1a, we:
- Used the standard Bardeen potential equation: Φ̈ + (4+3c_s²)HΦ̇ + [c_s²k²/a² + 2Ḣ + (3+3c_s²)H²]Φ = 0
- Plugged in H(t), Ḣ(t), a(t) from the ECH-modified Friedmann equation
- Found T(k) = 1 for super-Hubble modes, n_s = 1

This is identical to what you get from LQC effective equations at the classical perturbation level. The only input from ECH is the modified background — the perturbation equation itself is unchanged from GR.

Wilson-Ewing (2013) goes further: he includes LQC "dressed metric" corrections to the Mukhanov-Sasaki equation that modify the effective mass term z''/z. These quantum-geometry corrections suppress r from ~16 to ~10⁻⁴. **Our Phase 1a is strictly less complete than Wilson-Ewing.**

## The remaining ECH-specific novelty question

The only path to genuine ECH novelty is:

> **Does the ECH action (first-order Palatini + Holst term), when perturbed around FRW and with torsion integrated out at the perturbed level, produce correction terms in the scalar perturbation action that differ from both the classical result AND the LQC dressed-metric result?**

If YES → ECH gives genuinely new perturbation physics, and the branch is alive.
If NO → ECH perturbations reduce to the classical form, and ECH-specific perturbation novelty is dead.

## What this gate determines

- Whether Branch V has any ECH-specific perturbation content
- Whether the ALP-curvaton program (Branch W) builds on ECH-specific dynamics or is merely bounce-compatible
- Whether the ECH framework contributes anything to perturbation cosmology beyond the modified Friedmann equation
