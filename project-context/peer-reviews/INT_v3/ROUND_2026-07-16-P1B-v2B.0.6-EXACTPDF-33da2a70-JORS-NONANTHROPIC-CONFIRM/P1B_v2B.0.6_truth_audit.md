# P1B v2B.0.6 exact-PDF truth audit

Binding: commit `a92e88b98973db6998d6bd6cffdf66b91420c9dc`, PDF
SHA-256 `33da2a70bd559766b0988de5885f12333ef02b86e8a45bcf0a8057dbd8f80c9a`.
Grok and Gemini used direct native-PDF APIs; Codex used GPT-5.6 Sol/high
through the ChatGPT subscription CLI in the registry-scoped detached tree.
No OpenAI API or Anthropic route was used.

## Verdicts and dispositions

- **Grok MAJOR:** the persistent archive is the disclosed external submission
  gate DP1B-15. Manuscript version `v2B.0.6` and package release `0.1.4` are
  explicitly distinct namespaces, so the claimed mismatch is false. A code
  block would be editorially helpful but the printed call and repository
  examples are executable; it is not a scientific or software defect.
- **Gemini MAJOR:** the archive item maps to DP1B-15. Suggested JORS heading
  normalization and code-block presentation are editorial improvements, not
  evidence that the central software claim fails. Artifact locations are
  already direct repository links with hashes and extraction instructions.
- **Codex MINOR:** verified a real cross-platform CI defect, DP1B-22.
  `.github/workflows/namaster-proof.yml` included `windows-latest`, but its
  independent-example step used POSIX line continuation and `${RUNNER_TEMP}`
  without selecting Bash. Commit `be218ed7` explicitly selects Bash and adds a
  regression guard.

All reviewers supported the central exact-window and content-bound validation
claim. This is not a clean residual wave because DP1B-22 was genuinely new.
Readiness remains 56. The archive DOI and author contact remain explicit
external/human gates, and another exact-PDF confirmation is required after the
CI closure is packet-bound.
