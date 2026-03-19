# 00: Target Lock

## Quantity Being Computed

f_NL^total = f_NL^intrinsic + 5/4

where f_NL^intrinsic = -(5/8) · Im[G* · J_combined] / |G|²

G* = ghat*(r·xf) · ghat*(xf)²
|G|² = |ghat(r·xf)|² · |ghat(xf)|²
J_combined = ∫ dη' [SUM of all 6 Maldacena vertex integrands] (single complex integral)

## Terms Included

All 6 terms of the Maldacena cubic action at ε = 3/2, after substituting the constraint χ_k = -(3/2)η⁴ζ'_k/k².

| Term | Status | Notes |
|------|--------|-------|
| T1: (9/4)a²ζζ'² | VERIFIED (+0.311 intrinsic) | Stable in float64 |
| T2: (9/4)a²ζ(∂ζ)² | Verified (negligible) | ~0.00002 |
| T3: -3a²ζ'(∂ζ)(∂χ) | UNRESOLVED | Large coefficient, UV-unstable separately |
| T4: (9/16)a²ζ²ζ' | Verified (small, -0.002) | Marginal stability |
| T5: (3/4)∂²ζ(∂χ)² | UNRESOLVED | Finite but UV-unstable |
| T6: (9/32)∂²ζχ² | UNRESOLVED | k₁⁻² divergence in Re (proven harmless in Im) |

## Success Criteria

| Outcome | f_NL range | Interpretation |
|---------|-----------|----------------|
| Matches Cai | -4.4 ± 0.2 | Flagship confirmed at 35/8 level |
| Matches L-B | -2.2 ± 0.2 | Flagship alive at 35/16 level |
| Negative, |f_NL| > 1 | Flagship alive, need to determine exact value |
| Positive ~+1.56 | T3-T6 contribute ~zero → Cai wrong, flagship weakened |
| Something else entirely | Investigate |
