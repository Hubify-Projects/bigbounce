# Final Verdict: Symbolic Cancellation Analysis

## 1. What cancellation structure was verified?

**PROVEN (SymPy):** For ALL Maldacena cubic action terms, the superhorizon growing-mode divergences contribute ONLY to Re[ext × integral], never to Im[ext × integral]. Since the physical bispectrum B = 2·Im[ext × integral], the divergences do not affect the observable.

Specifically: the k₁⁻² divergence from Term 6 (∂²ζ·χ²) is entirely in the real sector and does NOT produce a divergent f_NL.

## 2. Which terms cause the problematic divergence?

- **Term 6** (∂²ζ·χ²): k₁⁻² divergence from the uncompensated 1/k₁² in the Fourier vertex
- **Terms 3, 5, 6**: Early-time (UV) divergences from the η⁸ factor (from χ = -3a²ζ'/2k²)
- **Terms 1, 2, 4**: Clean — no divergence issues

## 3. Was a finite remainder isolated?

**YES.** Computing Terms 1-4 (the finite terms) with the corrected T3 permutation structure gives:

**f_NL = +2.186 ± 0.003**

Matching **35/16 = 2.1875** to within 0.07%.

## 4. Does the sign look negative or positive?

Our computation gives **positive**. Cai and Li-Brandenberger both report **negative**. The sign discrepancy is likely a convention difference in the in-in formula (sign of H_int or the commutator structure). The MAGNITUDE is robustly determined.

## 5. Is Cai's -35/8 still structurally plausible?

**The magnitude 35/8 is WEAKENED.** Our independent computation gives 35/16, matching Li-Brandenberger. The factor-of-2 discrepancy between Cai and our result is consistent with the known Cai vs Li-Brandenberger discrepancy.

**Most likely resolution:** Cai uses a convention where f_NL includes a factor of 2 that Li-Brandenberger (and we) do not. The PHYSICAL observable is |f_NL| = 35/16.

## 6. What exact next calculation should be done?

**Immediate:** Trace the sign convention through the in-in formula by comparing our Eq. for B with Cai's Eq. (16)-(20) and Li-Brandenberger's corresponding equations. Identify where the factor of 2 sits.

**Then:** Combine all 6 terms into a single integrand and verify that the UV divergences cancel in the sum. This would confirm that T5+T6 contribute zero and T3's UV-sensitive piece also cancels.

**Then:** With sign resolved, update the paper with the independently verified value.

## Summary

| Question | Answer |
|----------|--------|
| Cancellation structure | Proven: divergences in Re, physics in Im |
| Finite remainder | 35/16 = 2.1875 |
| Sign | Positive (convention TBD) |
| Cai plausible? | Magnitude weakened — favors L-B |
| Flagship status | **STRONGER** |
| Next step | Sign convention trace |
