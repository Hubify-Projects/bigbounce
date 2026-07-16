# P1B v1B.0.111 exact-PDF truth audit

Exact artifact: commit `59517e43ab185d3e185681fd61065f99a11d1616`,
PDF SHA-256
`defc8cafd0f71688838fd9bae8ee7a5f9e9d11b94f01a58b2787007bb5139533`.
The board used Grok direct API, Gemini direct API, and the authenticated Codex
subscription. OpenAI API and Anthropic were not used.

## Board

| Leg | Wrapper verdict | Truth-audited result |
|---|---|---|
| Grok 4.3 | MINOR REVISIONS | One useful style suggestion; two stale/mistaken requests; no new scientific major |
| Gemini 3.1 Pro | MAJOR REVISIONS | Standing venue/scope opinion plus already-disclosed limitations; no newly demonstrated numerical defect |
| Codex subscription, GPT-5.6 Sol high | MAJOR REVISIONS | One real provenance major and two real semantic/numerical minors |

## Verified findings

1. **REAL / MAJOR — stale BBN provenance prose.** The manuscript says the
   public YAMLs declare a PArthENoPE predictor. The executed CAMB 1.6.5 receipt
   and all four hash-bound public YAMLs instead bind
   `PRIMAT_Yp_DH_ErrorMC_2021.dat`. The paper must describe the executed table.
2. **REAL / MINOR — NaMaster estimator ambiguity.** The displayed `0.270°`
   is the grid fit to the 500-realization mean bandpowers. The separate mean of
   the 500 realization-level angle fits is `0.269914°`, with signed bias
   `-0.000086°` and standard error `0.000573°`. Both are consistent and the
   scientific conclusion is unchanged, but they must not be called the same
   estimator.
3. **REAL / MINOR — cosine-flat angular prior.** A prior uniform in
   `cos(theta_i)` has density proportional to `sin(theta_i)` and median
   `theta_i=pi/2`; the notation table's “midpoint near 0.5” is false.
4. **REAL / MINOR editorial — repeated scope disclaimers.** Grok correctly
   observes defensive repetition. This is a presentation issue, not a
   scientific contradiction; it should be handled in the subsequent
   journal-style compression pass rather than by deleting necessary scope
   boundaries during this numerical closure.

## Falsified, stale, or standing items

- Grok requests an inline signed-band equation, but the exact expression
  `|beta-0.342°|<0.094°` is already rendered in the prior-predictive method.
- Grok quotes post-burn counts `123,129` and `93,066`; the current S8 contract
  is separately bound to the exact 30%-burn overlay and does not support
  changing the verified Planck+BAO+SN count to that stale rounded value.
- Gemini's three majors demand a different paper—an ECH Boltzmann module,
  real-sky systematics analysis, or standalone-method novelty. They are venue
  and scope judgments, not evidence that the manuscript's bounded calculations
  are wrong. Its full-EB limitation is already explicit and remains a standing
  limitation rather than a paper-only closure.
- Grok's template-score concern is editorial. The manuscript already labels
  the score heuristic and distinguishes it from a sky significance.

## Closure rule

The three mechanically detectable defects above must become fail-closed P1B
science-contract checks before v1B.0.112 is released. Readiness remains 56
until the corrected exact PDF is re-reviewed; no acceptance is inferred.
