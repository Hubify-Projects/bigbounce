# Parity-Violating Tensor Signatures: Problem Statement

**Date:** 2026-03-15

---

## Why the Tensor Amplitude Route Failed

The tensor spectrum computation (Branch H, Priority 1) found:
- n_T ≈ 0 (flat, scale-invariant)
- Amplitude P_T ~ 10⁻⁶⁴ (suppressed by (a_b/a_0)² ~ 10⁻⁶⁵)
- Result is GENERIC to radiation bounces, not spin-torsion specific
- Unobservable by > 10⁴ at every detector band

The failure is structural: the bounce is a brief (~t_Pl), Planck-scale
event whose perturbation output is diluted by 10⁶⁵ orders of expansion.

---

## Why Parity/Chirality Is Logically Different

The tensor amplitude computation treated left-handed (L) and
right-handed (R) tensor polarizations identically:

```
v_{k,L}'' + (k² - a''/a) v_{k,L} = 0
v_{k,R}'' + (k² - a''/a) v_{k,R} = 0
```

Same equation → same spectrum → no chirality information.

Parity-violating effects could break this symmetry:

```
v_{k,L}'' + (k² - a''/a + Δ(η)) v_{k,L} = 0
v_{k,R}'' + (k² - a''/a - Δ(η)) v_{k,R} = 0
```

where Δ(η) is a parity-odd term from the torsion/spin structure.

If Δ ≠ 0:
1. Left and right modes are amplified differently by the bounce
2. The chirality asymmetry Δχ = (P_L - P_R)/(P_L + P_R) could
   be a RATIO that avoids the absolute amplitude suppression
3. The effect would be DIRECTLY tied to the spin-torsion structure
   (not generic to radiation bounces)

---

## Why This Might Evade the Dilution Argument

The absolute amplitude P_T ~ 10⁻⁶⁴ is tiny because of dilution.
But a RATIO like Δχ = (P_L - P_R)/(P_L + P_R) is dimensionless
and scale-independent — both numerator and denominator suffer the
same dilution, which cancels.

If the bounce produces Δχ ~ O(1) at the bounce scale, this ratio
would survive to today unchanged (assuming parity-preserving
propagation post-bounce).

The observable would be the HANDEDNESS of the gravitational wave
background, not its absolute amplitude.

---

## What Would Count as Success

### Strong success (PARITY_SIGNATURE_PROMISING)
1. A parity-odd term Δ(η) appears naturally in the tensor equation
   from the spin-torsion structure
2. Δχ is O(1) and frequency-dependent
3. The effect is SPECIFIC to spin-torsion (not generic)
4. An observable (TB/EB correlation, chiral GW background) exists
   that could test the prediction

### Moderate success (PARITY_SIGNATURE_WEAK_BUT_DISTINCTIVE)
1. A parity-odd term exists but is small or parametrically
   suppressed
2. Δχ is nonzero but tiny
3. The effect is theoretically distinctive even if currently
   unobservable

### Failure (PARITY_SIGNATURE_CLOSED)
1. No parity-odd term exists in the minimal model
2. FRW symmetry kills any potential parity violation
3. Parity-odd effects require ADDITIONAL physics beyond EC gravity

---

## The Test

### Question 1: Does the minimal EC theory contain a parity-odd
tensor source?

Check: the four-fermion interaction (J^5)², the Holst/Nieh-Yan
term, torsion background expectation values.

### Question 2: Does FRW symmetry permit a parity-odd tensor
background?

Check: whether homogeneity + isotropy forces all parity-odd
quantities to vanish.

### Question 3: Even if a parity-odd background exists, does it
couple to tensor modes?

Check: whether δJ^{5,0} from tensor perturbations is nonzero.

### Question 4: Is the effect spin-torsion-specific?

Check: whether the same effect appears in any generic bouncing
cosmology.

---

## What Must Be Distinguished

| Concept | Parity property | Relevant? |
|---------|----------------|-----------|
| Torsion T^λ_μν | Mixed (depends on components) | Must check |
| Axial current J^5_μ | Pseudovector | Parity-odd |
| (J^5)² = J^5_μ J^{5μ} | SCALAR (parity-even!) | Does NOT help |
| Nieh-Yan N₄ | Pseudoscalar density | Topological on EC |
| Holst term | Parity-odd in action | Check effect on EOM |
| Chern-Simons R̃R | Parity-odd | NOT in minimal EC |
| Bounce itself | Breaks T, not P | Does NOT break parity |

**The critical distinction:** having parity-odd FIELDS in the
theory (like J^5_μ) does NOT guarantee parity-odd OBSERVABLES.
The fields must produce a nonzero parity-odd BACKGROUND or
SOURCE TERM in the tensor equation.
