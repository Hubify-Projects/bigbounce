# P1B v1B.0.106 exact-PDF review truth audit

## Immutable review target

- Science commit: `d49249877bfd0f04cbd55bf93518d27a6b0fbfd9`
- PDF: `arxiv/paper1b_mcmc_companion.pdf`
- PDF SHA-256: `7cb825572d6474e5d0fb88fa61157df31cf5b88730243f11cf39fc25e2512013`
- Profile: `JCAP-COMPUTATIONAL`
- Policy: OpenAI-family review used the ChatGPT-subscription Codex CLI only. The xAI/Grok and Google/Gemini legs were direct-provider API calls with sanitized receipts. Anthropic was not used.

## Preserved raw reviews

| Leg | Verdict | Raw response | SHA-256 |
|---|---|---|---|
| xAI Grok 4.3 | ACCEPT | `../ROUND_2026-07-09/API_P1B_grok.md` | `e076f5542b29b3da66040452705b796cf4344b066978719522a4c0097a5e7dfa` |
| Google Gemini 3.1 Pro Preview | REJECT | `../ROUND_2026-07-09/API_P1B_gemini.md` | `2ce81ce3ff49c84f7ea2cb2f75e097252963a18324ba1f246cd59bd08815c62c` |
| Codex gpt-5.6-sol high, ChatGPT subscription | MAJOR REVISIONS | `../../INT_api/H17_2026-07-10/intwave_P1B_codex_2327.md` | `26eb57e57d07046b39e1badaefdbd5e2c4ac0af510e15a5d99f26c932602fd31` |

The split board is not averaged. Each technical claim was checked against the repository and calculations. Grok's ACCEPT does not override reproduced defects; Gemini's venue/novelty rejection does not by itself falsify the computations.

## Finding-by-finding adjudication

1. **REAL / MAJOR — reproduction entry point.** `reproduce_cosmology.sh` resolves a nonexistent nested `cosmology/cosmology` path, requests Cobaya 3.5.4 while the paper reports 3.6.1, and does not produce all advertised derived artifacts.
2. **REAL / MAJOR — incomplete provenance manifest.** The 46-entry v106 manifest omits load-bearing frozen cosmology products and ALP code/results, contradicting the manuscript's manifest-completeness wording.
3. **REAL / MAJOR — mask-label mismatch.** The executed auxiliary masks are pure Galactic-latitude cuts at 8.6269, 20.4873, and 42.8436 degrees, not the stated Planck/ACT-like geometries with a declination selection.
4. **REAL / MAJOR — ALP method mismatch.** The retained chain values come from nonlinear cosine-ODE integration to the present, not the printed onset/dilution approximation. A 20-point recomputation agrees with stored `Omega_a` to maximum absolute `8.3e-7`; the printed approximation would instead give only 2.0265% below `Omega_a<0.01`.
5. **PARTLY REAL / MAJOR — subset interpretation.** The `Omega_a<0.01` subset has theta quantiles (0.149, 0.211, 0.267). The `theta<=0.1` sliver is a distinct 0.3275%-weight subset with beta 0.117 +/- 0.047 degrees. The 11.6% and 6.1% prior-predictive fractions are not spectator-conditioned, and a 25x energy-density ratio is not a demonstrated prior-volume tuning cost.
6. **PARTLY REAL / MINOR — torsion scaling.** The two numbers are valid order-of-magnitude `rho_tor/rho_rad` ratios, not normalized physical `Delta N_eff` predictions.
7. **REAL / MINOR — diagonal S/N.** The reported 20.01 uses marginal variances and must be labeled a diagonal-SNR heuristic, not a covariance-aware matched-template significance.
8. **PARTLY REAL / MINOR — c15 scope.** The nonconverged, changed-likelihood run is a corroborative sensitivity check, not an empirical bound on likelihood-pairing bias.
9. **REAL / MINOR — numerical consistency.** The current diagnostics support worst `Rhat-1=0.000971`; c14 supports beta `0.328 +/- 0.100` degrees; and rounding 1.06 cannot explain a change from 4.93e-3 to 4.65e-3.
10. **REAL / MINOR — software acknowledgments.** Future/unverifiable AI version labels should be removed or replaced with versioned, auditable tooling statements.

## Scientific disposition

The Codex MAJOR REVISIONS verdict is warranted. The stock-CAMB null posterior and canonical exact-window recovery remain numerically supported. The damage is bounded to reproducibility claims, mask scope, the ALP method/subset interpretation, and several secondary labels/numbers. P1B remains at readiness 56 with no acceptance claim until a versioned closure is compiled, visually audited, and re-reviewed against its exact PDF.

## Closure gate

- Repair or honestly narrow the reproduction and manifest claims.
- Make the executed mask labels exact.
- Describe the implemented ALP ODE and separate the two conditional subsets.
- Scope the torsion ratio, diagonal S/N, and c15 sensitivity claims.
- Correct all three numerical inconsistencies and the acknowledgment issue.
- Bump to v1B.0.107, regenerate the manifest, compile, run all-page PDF QA, and preserve hashes.
- Run at most one exact-PDF confirmation wave after closure; do not loop until a preferred verdict appears.
