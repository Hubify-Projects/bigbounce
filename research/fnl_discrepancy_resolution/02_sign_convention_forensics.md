# 02: Sign Convention Forensics

## The Sign Chain

Our computation gives f_NL > 0 (positive). Cai gets f_NL < 0 (negative). Tracing the sign:

### Step 1: Action sign
S₃ = M²_Pl ∫ (9/4) a² ζ ζ'² dη d³x
**Coefficient is POSITIVE** in the Lagrangian.

### Step 2: Interaction Hamiltonian
H_int = -L₃ = -(9/4) M²_Pl a² ζ ζ'²
**NEGATIVE.** This is standard (Hamiltonian = -Lagrangian in conformal time for interaction terms).

### Step 3: In-in formula
⟨ζ³⟩ = -i ∫ ⟨[H_int, ζ³]⟩ dη'
Commutator: [H_int, ζ³] = H_int·ζ³ - ζ³·H_int
At tree level: = 2i·Im[F] where F = ⟨H_int·ζ*³⟩
So: B = 2·Im[∫ F dη']

### Step 4: Product
F = -(9/4)·a²·ζ_{k₁}(η')·ζ'_k(η')²·ext
where ext = ζ*_{k₁}(η_f)·ζ*_k(η_f)²

B = 2·Im[-(9/4)·ext·∫ a²ζζ'²] = -(9/2)·Im[ext·I]

### Step 5: Numerical result
Im[ext·I] < 0 (from diagnostic: -4.61e42)
So B = -(9/2)·(-4.61e42) > 0
And f_NL = (5/12)·B/PP > 0

### Why positive?

The sign of Im[ext·I] depends on the PHASE of the mode functions. For our BD vacuum:
- External: ext ∝ i (imaginary, positive coefficient)
- Integral: dominated by Im[I] < 0
- Product: Im[i·(real+i·Im[I])] = Im[i·real - Im[I]] = real part of I
  Plus: Im[i·i·Im[I]] = Im[-Im[I]] = 0

Actually the full expression:
Im[ext·I] = Re[ext]·Im[I] + Im[ext]·Re[I]
= (+small)·(large negative) + (large positive)·(small positive)
= (large negative) + (moderate positive)
= NET NEGATIVE → B POSITIVE → f_NL POSITIVE

### The sign question
Our positive f_NL from Term 1 is a genuine computational result, not a convention error. The question is whether Terms 3-6 flip the overall sign to negative (as Cai reports).

### Plausibility check
From rough estimates, T3 with coefficient 27/2 has OPPOSITE sign to T1 at horizon crossing (the η⁸ factor changes the phase structure). If T3 contributes ~ -6 × T1 (from the scaling ratio at |kη|~1), the total could be:
f_NL_intrinsic ≈ 0.31 - 1.87 + (other terms) ≈ -1.56 + corrections
Total: -1.56 + 1.25 = -0.31

This is NEGATIVE — consistent with Cai's sign — but the magnitude is ~0.3, not 4.4 (Cai) or 2.2 (L-B).

### Conclusion on sign
**The sign is NOT a pure convention issue.** Term 1 alone gives positive. The TOTAL (including T3-T6) is likely negative. The sign flip comes from the physical contribution of the χ-sector terms, which dominate over Term 1.
