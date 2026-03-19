# 00: Model-Comparison Target Lock

## Bounce Benchmark
- f_NL = -35/8 = -4.375 (FIXED, 0 free parameters)
- This is a delta-function prior at -4.375

## Inflation Competitor Classes

| Class | f_NL prediction | Free params for f_NL | Prior range |
|-------|----------------|---------------------|-------------|
| Standard single-field (SSFSR) | +0.015 (fixed) | 0 | Delta at +0.015 |
| Non-attractor single-field | +5/2 natural, range [-10, +10] | 2 (transition + duration) | Flat [-10, +10] |
| Standard curvaton | [-1.25, +∞) | 1 (r_dec) | Flat [0.01, 1] via r_dec |
| Self-interacting curvaton | [-∞, +∞) | 2 (r_dec + λ/m²) | Flat [-15, +15] |
| Rapid-turn multifield | [-∞, +∞) | 3 (R_fs + Ω + N_turn) | Flat [-15, +15] |

## Observable
Single observable: measured f_NL^local ± σ(f_NL) from a galaxy survey.

## Comparison Criterion
Bayes factor: B = P(data | bounce) / P(data | inflation_class)
- B > 10: Strong bounce preference
- B > 100: Very strong bounce preference
- 3 < B < 10: Moderate bounce preference
- 1/3 < B < 3: Inconclusive
- B < 1/3: Inflation preferred
