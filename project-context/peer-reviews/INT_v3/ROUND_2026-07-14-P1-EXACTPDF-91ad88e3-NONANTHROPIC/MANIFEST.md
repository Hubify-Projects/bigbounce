# Exact-PDF non-Anthropic review manifest

Round: `P1EXACT91ad88e3`  
Frozen commit: `91ad88e36121da128175415f55be44d5e458f9f1`  
Date: 2026-07-14  
Mutation policy: review evidence only; no manuscript, SSOT, site, Convex, PDF-version, or publication-state edits.

## Frozen inputs

| Paper | Version | Source SHA256 | PDF SHA256 | Pages |
|---|---|---|---|---:|
| P1A | v1A.0.116 | `e39f601b986909603edf032c9e80e236e442144af82fda9bf332b1873299d30c` | `69bf8e8980ac67801347ce520d19556804e53a5138a33f8139bfa6d182450d2f` | 6 |
| P1B | v1B.0.105 | `8998919b7000f445b5c964e255895f9eb9921c32e835651d16b0b7d8b9c0b1e2` | `2d35148497808b619500aca39d3be67d074b07647c3f68b5ce7c4b4d7db24d35` | 21 |

The TeX/PDF pairs were extracted from the exact commit and reviewed from the frozen directories. PDFs were also rendered at 150 DPI page-by-page for visual review.

## Reviewer matrix

| Leg | Model | Access | P1A | P1B | Fallback |
|---|---|---|---|---|---|
| OpenAI methodology | `gpt-5-2025-08-07` | native PDF + high reasoning + self-critique | complete | complete | none |
| Google cosmology | `gemini-2.5-pro` | native PDF | complete | complete | none |
| xAI adversarial | `grok-4.3` | rasterized full PDF | complete | complete | none |
| Codex subscription | `gpt-5.6-sol`, high | frozen source + all rendered pages + commit artifacts | complete | evidence complete; synthesis retry complete | none |

Provider allowlist was OpenAI, Google, and xAI. Anthropic and Perplexity were explicitly forbidden in the dispatcher. No Claude/Anthropic call or fallback occurred.

### P1B Codex run status

The first P1B Codex run completed 66 logged evidence items over 61 minutes and emitted a 1.5 MB event stream, including exact-chain recomputations and a substantive checkpoint. It did not emit a final report after a 12-minute post-tool grace window and was interrupted (exit 129). The partial event/stderr logs remain immutable evidence. A bounded no-tool GPT-5.6-sol/high retry synthesized only the supplied frozen evidence and completed successfully. Its event log contains a deprecated-feature warning for `--disable web_search`; it made no web or shell calls and returned the final report.

## Evidence map

- `API_DISPATCH_RESULTS.json`: direct-vendor models, wall times, success, and no-fallback policy.
- `P1A/raw/`, `P1B/raw/`: every prompt, raw report, Codex event stream, stderr log, partial log, and retry log.
- `P1A/VERDICT_MATRIX.md`, `P1B/VERDICT_MATRIX.md`: every labeled finding truth-adjudicated.
- `P1A/ARTIFACT_CHECKS.md`, `P1B/ARTIFACT_CHECKS.md`: independent algebra, exact-chain, figure, and implementation checks.
- `SHA256SUMS.txt`: content hashes for the complete proof directory, excluding the checksum file itself.

## Integrity limits

This directory proves what was reviewed and how findings were adjudicated. It does not claim journal acceptance, external human peer review, or that the frozen papers are publication-ready. The matrices explicitly preserve genuine blockers and distinguish them from stale readings, requested new work, submission metadata, and venue opinion.
