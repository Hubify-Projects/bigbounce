# P1B v2B.0.6 CI-closure truth audit

Binding: commit `6d40f1a117f4f443c3e07ec8845c65c2aeadb85f`, exact PDF
SHA-256 `33da2a70bd559766b0988de5885f12333ef02b86e8a45bcf0a8057dbd8f80c9a`.
This focused retry used GPT-5.6 Sol/high through the Codex ChatGPT-subscription
CLI only. Direct Grok/Gemini were deliberately not rerun because they had
already reviewed the unchanged PDF and their only major deduction was the
disclosed external archive gate. No OpenAI API or Anthropic route was used.

## Disposition

- **Windows CI closure — VERIFIED.** The reviewer confirmed that the
  independent example now runs under explicitly selected Bash in the Windows
  matrix.
- **Fractional multipole inputs — VERIFIED MINOR, DP1B-23.**
  `field_harmonic_kwargs(lmax=512.5, ...)` retained a fractional limit, while
  `bandpower_edges(..., lmax=512.5, ...)` silently truncated its integer edge.
  This contradicted the documented deterministic integer-support contract.
  v2B.0.7/package 0.1.5 rejects non-integral and boolean inputs without
  coercion and adds seven boundary regressions.

The central software claim remains supported. This focused leg is not a
multi-provider clean wave and does not increase readiness.
