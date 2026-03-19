# 00: Cancellation Target Lock

## The Problem

The full Maldacena cubic action at ε = 3/2 has 6 terms. After substituting the constraint variable χ_k = -(3/2)a²ζ'_k/k², Term 6 produces a **k₁⁻² divergence** in the squeezed limit that no other term cancels.

This divergence is NOT a numerical artifact. It is algebraically present in the integrand.

## The Divergence Structure

For each term, define D = power of k₁ in f_NL (should be 0 for finite f_NL):

| Term | Vertex | χ factor | Dot product | D(f_NL) |
|------|--------|----------|-------------|---------|
| T1 | a²ε²ζζ'² | none | none | **0** ✓ |
| T2 | a²ε²ζ(∂ζ)² | none | none | **0** ✓ |
| T3 | -2a²εζ'(∂ζ)(∂χ) | χ_{k₁}/k₁² → k₁⁻² | (k·k₁) → k₁² | **0** ✓ |
| T4 | (a²ε/2)d(ε/H)/dη·ζ²ζ' | none | none | **0** ✓ |
| T5 | (ε/2)∂²ζ(∂χ)² | χ_{k₁}/k₁² → k₁⁻² | (k·k₁) → k₁² | **0** ✓ |
| T6 | (ε/4)d(ε/H)/dη·∂²ζ·χ² | χ_{k₁}/k₁² → k₁⁻² | **NONE** | **-2** ✗ |

Terms 3 and 5 have dot products (k_b·k_c) that provide k₁² to cancel the 1/k₁² from χ_{k₁}.
Term 6 has NO such dot product. The 1/k₁² divergence survives.

## Why This Happens

The vertex ∂²ζ·χ² connects:
- One leg with ∂² (Laplacian) → provides -k_a²
- Two legs with χ (plain, no spatial derivatives) → each provides 1/k²

When χ carries the long mode k₁: factor 1/k₁² with no compensating dot product.

## The Resolution: Boundary Terms from the Growing Mode

The standard in-in formula ∫_{-∞}^{η_f} dη' ⟨[H_int(η'), ζ³(η_f)]⟩ is INCOMPLETE for the matter bounce.

For inflation (frozen modes), the perturbations are constant after horizon crossing, and the in-in integral captures everything. For the matter bounce (growing modes), ζ grows as |η|⁻³ after horizon crossing, and the cubic interaction generates additional **boundary contributions at η_f** that are not captured by the standard bulk integral.

These boundary terms:
1. Contain the same k₁⁻² structure as T6
2. Have opposite sign
3. Cancel the divergence
4. Leave a finite remainder that contributes to f_NL

This is why Cai et al. define their shape function A_T to be explicitly time-independent — their formalism automatically includes both bulk and boundary contributions.

## Success Criteria

- **Full success:** Demonstrate the cancellation explicitly and extract the finite coefficient
- **Partial success:** Identify the boundary-term structure and show it has the right k₁-scaling to cancel T6's divergence
- **Failure:** If the divergence persists after including boundary terms → serious problem with the Maldacena action for matter contraction
