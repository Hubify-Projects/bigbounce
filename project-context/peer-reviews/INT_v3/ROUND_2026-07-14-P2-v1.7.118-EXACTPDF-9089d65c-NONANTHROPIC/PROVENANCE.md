# P2 v1.7.118 exact-PDF non-Anthropic review provenance

- Review commit: `9089d65c64752e3a2c69778b72d97ef7c45b4443`
- Commit subject: `docs(p2): close fresh-panel editorial findings`
- Commit timestamp: `2026-07-14 02:46:24 -0700`
- Visible manuscript version: `v1.7.118`
- Review PDF: `proof/02_full_draft.v1.7.118.pdf`
- PDF SHA-256: `01107b3d731b945b2aa9ea04ce4e8188282770a87b495c4a1f7ad5b71a4db71a`
- Frozen TeX SHA-256: `7c4d9186b7af18900bf41e5982622f1e343c6dd253e9eaea98a39df59ac47fa4`
- Frozen BibTeX SHA-256: `9f9aa52364f751f8d0d1cd351777ceb4b81720933ae0f6af345b550202e77f93`
- PDF pages: 10

Before dispatch, `git diff --exit-code 9089d65c --` passed for the live PDF, TeX, and BibTeX files. The three frozen files are byte copies of those committed inputs and have the hashes above.

## Authorized review legs

1. OpenAI direct native-PDF API: GPT-5 (`gpt-5-2025-08-07`).
2. xAI direct native-PDF API: `grok-4.3`.
3. Google direct native-PDF API: `gemini-2.5-pro`.
4. Codex CLI authenticated by ChatGPT subscription: `gpt-5.6-sol`, high reasoning, read-only ephemeral session.

Anthropic/Claude dispatch and fallback are prohibited for this wave. The direct-vendor runner retries only the same pinned vendor/model; it does not cross-fallback. The Codex leg unsets `OPENAI_API_KEY`, `CODEX_API_KEY`, and `ANTHROPIC_API_KEY` so authentication is exclusively the local ChatGPT login.

Raw reports are immutable evidence. Truth-audit synthesis is recorded separately and does not rewrite any raw response.

## Raw-report integrity

| Leg | Raw report SHA-256 |
|---|---|
| OpenAI GPT-5 | `eaea3b8e021c19b266e543827f8f1a6ef6b0977d870da69071c54eb7db972e30` |
| Grok 4.3 | `7f019a05e2580c7b6a94c11439845fd76634ac355c1613326081bd0065386c15` |
| Gemini 2.5 Pro | `39463dd1b4137ea4abec1d8ce84104db5ba1237d55d5955fc76ef1145e45ccd5` |
| Codex `gpt-5.6-sol` high | `e1f7033f09f69a5fab82023076ea4b6bdc65806a20263ac911039c516e46e08d` |

Truth audit: `P2_v1.7.118_exactpdf_truth_audit.md`. Bounded closure evidence:
`P2_v1.7.119_closure.md`.
