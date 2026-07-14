# P2 v1.7.119 frozen exact-PDF non-Anthropic confirmation

## Frozen review object

- Review anchor: commit `44b4350def21ee7df8f836808edf73900dfb2535` (`fix(p2): close exact-panel scientific defects`)
- Canonical TeX: `research/focused_paper_source_integration/02_full_draft.tex`
- Canonical PDF: `research/focused_paper_source_integration/02_full_draft.pdf`
- Canonical bibliography: `research/focused_paper_source_integration/focused_paper_refs.bib`
- Visible PDF identity: P2 `v1.7.119`, dated July 14, 2026, 10 US-Letter pages

Immediately before freezing, `git diff --quiet 44b4350d -- <path>` returned success for each of the three canonical files. Their worktree SHA-256 values also exactly matched the bytes obtained with `git show 44b4350d:<path>`. The frozen copies are therefore the committed closure object, not a later worktree approximation.

| Frozen object | SHA-256 |
|---|---|
| `proof/02_full_draft.v1.7.119.tex` | `a1671b4c2e217af3ab11b5c56ef2fd5e766929ac24141f39314daf9ca8a6e00d` |
| `proof/02_full_draft.v1.7.119.pdf` | `4434dc8b26ed84324e3fdcf486a9205e49989e5e4dda5efd18436a68ccfd0590` |
| `proof/focused_paper_refs.v1.7.119.bib` | `9f9aa52364f751f8d0d1cd351777ceb4b81720933ae0f6af345b550202e77f93` |

## Independent panel

No Anthropic or Claude model was dispatched. The three API calls used only their named native-PDF vendor path; retries, if required, were constrained to the same vendor/model. All three completed on attempt 1, so no fallback occurred. Raw verdict labels are preserved without normalization.

| Lane | Authentication/transport | Model and settings | Raw verdict | Evidence SHA-256 |
|---|---|---|---|---|
| OpenAI direct | OpenAI Files API `input_file` | `gpt-5.5` | `MINOR REVISIONS` | `a08b8dad40a605b81736d9c2a42601ee9fa313434eb3b8b5c47ebd6b8dec7057` |
| Gemini direct | Gemini inline native PDF | `gemini-3.1-pro-preview` | `ACCEPT` | `0f198a4efd8221681a160e289d2ccbfac55619d6f3b2759c42797b57572bf64b` |
| Grok direct | xAI native PDF file ID | `grok-4.3` | `ACCEPT` | `08398d1693e6ba329d46a624ab34a61fc8a75b8100027b110c9bb7c1761ec5fe` |
| Codex subscription | `codex login status`: `Logged in using ChatGPT`; API-key variables removed; read-only ephemeral CLI | `gpt-5.6-sol`, reasoning `high`; session `019f6062-53a5-73b3-9f6f-75be71bc5991` | `MINOR REVISIONS` | `b044d77b057e19d313fc1a544ff12bfa1cc0d23b0d146b717f3e554d8af8b61f` |

The Codex subscription report completed at `2026-07-14T11:42:11Z`. It was counted only after the CLI exited successfully and the report existed on disk.

## Exact checks

- Full PDF audit: `audit/P2_v1.7.119_pdf_audit.md`
- Ten-page contact sheet SHA-256: `2aea6c788950dffd17766033dca1c06355cc36d84f1ec080043bbbcc3eda5d2e`
- Orbit/sign checker SHA-256: `678463f2e070db915e1480066e9672d01207afbf1d631deb1ac84978caa8f6cd`
- Captured checker output SHA-256: `33022eb4ec109c9dd99da46073ef59df20a9af18e95e67d9a5c029917ff224fd`

The checker was rerun for this frozen round. It proves the six-permutation `(5,2,2)` identity, reproduces the Cai field-redefinition equality only under consistent orbit counting, and confirms that the Hamiltonian convention gives `+2 Im`; the v1.7.119 source explicitly supplies the equivalent interaction-Lagrangian extra-minus definition.

## Interpretation boundary

This is a confirmation panel, not a readiness mutation. It does not alter the paper, SSOT, site, Convex, version registry, or readiness score. Raw reports are evidence; the disposition in `P2_v1.7.119_confirmation_truth_audit.md` is the truth-audited result.
