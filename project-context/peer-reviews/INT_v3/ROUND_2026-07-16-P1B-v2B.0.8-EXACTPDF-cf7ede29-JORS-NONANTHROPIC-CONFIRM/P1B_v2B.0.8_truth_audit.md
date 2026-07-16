# P1B v2B.0.8 exact-PDF truth audit

Binding: commit `92aa27549f542a0eda62477436535441ada87533`, exact PDF
SHA-256 `cf7ede299ee5d6c28209817c7a0ee195000fe8dd77c276e830d8d04f5d2c3195`.
Grok and Gemini used direct native-PDF APIs. The GPT-5.6 Codex-subscription leg
was started but intentionally interrupted at Houston's request for usage
conservation; its exit is recorded as absent/exit 130 and no Codex verdict is
claimed. No OpenAI API or Anthropic route was used.

## Dispositions

- **Grok REJECT:** the persistent archive is the known DP1B-15 external gate.
  The claimed v2B.0.8/package-0.1.6 mismatch is false: these are intentionally
  distinct manuscript and software-release namespaces. The scoped repository
  contains `CITATION.cff`, the package tests, and the retained PyMaster-linked
  artifacts; no absence finding is accepted.
- **Gemini MAJOR:** the archive item maps to DP1B-15. The suggested JORS
  heading and Availability-template normalization are editorial improvements,
  not executable or scientific defects, and do not justify a readiness change.
- **Codex:** absent by deliberate interruption; no result inferred.

The direct-provider legs found no new executable defect after v2B.0.8. The
central software claim remains supported by the committed 41-test package,
exact-window shape checks, retained physical artifacts, and compile/visual
audits. This is not a complete multi-provider clean wave because the Codex leg
was interrupted and DP1B-15 remains open. Readiness remains 56.
