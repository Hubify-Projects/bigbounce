# P1B v2B.0.5 exact-PDF truth audit

Binding: commit `cab59a1a666a765933ff29730947050b4088b0ea`, PDF
SHA-256 `f9dcbd7e76da764d2cea6cc018a3fb3d6a3ed770f4ba048860c294d20eeee6ee`.
Grok and Gemini used direct native-PDF APIs; Codex used the ChatGPT
subscription in the registry-scoped detached tree. No OpenAI API or Anthropic
route was used.

## Verdicts and dispositions

- **Grok MAJOR:** the archive/DOI item is the disclosed DP1B-15 external gate.
  The claim that repository artifacts are non-public is contradicted by their
  public GitHub paths. Paper version `v2B.0.5` and package version `0.1.4` are
  distinct declared namespaces, not a mismatch. Coordinated receipt
  replacement limitations are explicitly stated in the manuscript and README.
- **Gemini MAJOR:** the archive item maps to DP1B-15. The orphaned Sharded
  result validation paragraph is a verified closure regression, DP1B-20,
  closed by restoring it before Author Contributions. The archive-isolation
  suggestion is implemented in the package README without claiming that an
  archive already exists.
- **Codex MAJOR:** archive and correspondence metadata map to DP1B-15. The
  printed `beta_deg` call is a verified executable-documentation defect:
  `windowed_bandpowers` accepts `beta_rad`. DP1B-21 closes it with
  `beta_rad=np.deg2rad(0.25)`.

The central exact-window, receipt, retained-example, and concurrency claims were
supported by all repository-level checks. This is not a clean wave: two valid
minor closure defects were found. v2B.0.6 closes them; readiness remains 56
pending another exact confirmation, archive/DOI, author contact, and human
review.
