# P1B v2B.0.7 exact-PDF truth audit

Binding: commit `b4a395936b542e9417fb3a49af6741040aacdf12`, exact PDF
SHA-256 `77a79089a6ab959e313639ef5cb48873cc5e1d507d2b4ec645338c38918f9582`.
Grok and Gemini used direct native-PDF APIs; Codex used GPT-5.6 Sol/high
through the ChatGPT-subscription CLI in the registry-scoped detached tree.
No OpenAI API or Anthropic route was used.

## Verdicts and dispositions

- **Grok REJECT:** the persistent archive is the disclosed DP1B-15 external
  submission gate. Paper version `v2B.0.7` and package version `0.1.5` are
  intentionally distinct namespaces. The scoped tree contains
  `CITATION.cff`, tests, code, and the retained workspace artifacts, so the
  contrary absence claims are falsified. The AI disclosure already identifies
  agent roles and human verification; no scientific closure is required.
- **Gemini MAJOR:** the archive item maps to DP1B-15. The suggested package
  cohesion rationale and explicit workspace protocol are useful editorial
  improvements and are added in v2B.0.8 without treating them as failed central
  claims.
- **Codex MINOR:** verified two real fail-closed defects. DP1B-24 records that
  Python equality allowed JSON metadata substitutions such as `true` for `1`.
  DP1B-25 records that a broadcastable malformed `decouple_cell()` result could
  compare against the exact window result and return a false zero residual.
  v2B.0.8/package 0.1.6 adds recursive JSON-type-strict equality, exact
  operator-shape and finite checks, and six regressions.

All repository-capable reviewers except Grok supported the central software
claim, and Grok's rejection depended on the disclosed archive gate plus
falsified absence claims. This is not a clean residual wave because DP1B-24/25
were genuinely new. Readiness remains 56 pending v2B.0.8 confirmation, archive
DOI, author metadata, and human review.
