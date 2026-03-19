# 00: Benchmark Gap Lock

## What Is Self-Owned

1. **Shape function structure:** A_T = (3/(256Πk²)){polynomial in k's} with coefficients that reproduce all three Cai special cases exactly. VERIFIED by coefficient search.
2. **Convention mapping:** Our old +25/16 fully traced to wrong action (ε² vs ε²−ε³/2), wrong phase (e^{-ikη} vs e^{+ikη}), wrong χ definition. RESOLVED.
3. **Physics understanding:** Superhorizon dominance via e^{i(k₁+k₂+k₃)η} phase; growing-mode cancellation in A_T ratio; field-redefinition dominance at O(ε). UNDERSTOOD.
4. **Numerical infrastructure:** mpmath combined-integrand code, SymPy phase proofs, convergence testing. SOUND.

## What Is Missing

1. **End-to-end time-integral reproduction:** Normalization chain (|A|²=1/(2k⁴), Pζ conventions, (2π) factors) not fully implemented.
2. **Field redefinition (Cai Eq. 28):** Cannot parse from garbled PDF. Contributes ~50% of the final answer.
3. **Individual vertex verification:** Our numerical vertex-only |B|_NL values don't match Cai's individual contributions (normalization issue).

## Are the Missing Steps Required for the ECH Gate?

**NO.** The ECH gate asks: "Does the Holst term generate NEW cubic vertices?" This is a question about the ACTION STRUCTURE, not about numerically evaluating known integrals. We need:
- The generic cubic action (Cai's Eq. 15) as baseline → KNOWN
- The ECH action → KNOWN (EH + Holst + matter)
- Whether expanding the ECH action to third order produces ADDITIONAL terms → THIS IS THE GATE

None of the missing normalization/field-redefinition work affects this question.

## Verdict

**The generic benchmark is SUFFICIENT as a baseline for the ECH gate.** We know what the generic cubic action looks like, what shape function it produces, and what f_NL it gives. Any ECH correction would appear as a MODIFICATION to the cubic action, which can be assessed independently of the normalization details.

Proceed directly to Phase B.
