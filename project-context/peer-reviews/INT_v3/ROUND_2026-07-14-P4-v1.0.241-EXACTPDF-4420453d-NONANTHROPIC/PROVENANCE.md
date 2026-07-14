# P4 v1.0.241 exact-PDF non-Anthropic review provenance

- Review commit: `4420453d2ae3614bc08bd22eec9454df3b3546b5`
- Commit subject: `feat(p4): add paired Stage-B recovery closure`
- Commit timestamp: `2026-07-14 02:06:42 -0700`
- Visible manuscript version: `v1.0.241`
- Review PDF: `proof/chirality_catalog_paper.v1.0.241.pdf`
- PDF SHA-256: `d6eded1df29da5d2ccf6acb1e04277876289ae1547a1b8a3d2fda819ae7097f2`
- Frozen TeX SHA-256: `5e4c2869037ed1e9f383df59c95772e4c9a902314ebd33a9d163a490906e4b48`
- Frozen BibTeX SHA-256: `61b9ca8a0eae79078bb6bcd4205c582b5f4f2ed0a16ece16a01837cc4718248d`
- Frozen Stage-B JSON SHA-256: `86eb8871419cae550f2fbbef7e985bed45af51cf4cbe3384981afa81605bd714`
- Frozen Stage-B generator SHA-256: `295e097e3269ce5bd0c023f053a98ac911b223790c5739015d41f4c2e5a1b98d`
- Frozen M44 closure report SHA-256: `c5ef595e4a13c8f9438519dacce9acc9934c7913753e3c2c03891e35207a57fb`
- PDF pages: 35

Before dispatch, `git diff --exit-code 4420453d --` passed for the live PDF,
TeX, BibTeX, Stage-B JSON, and Stage-B generator. The proof files are byte copies
of those committed inputs. The current `site/public/p4-chirality.pdf` is not
byte-identical and was deliberately not dispatched; it is a stale served mirror.

## Authorized review legs

1. OpenAI direct native-PDF API: `gpt-5.5`.
2. xAI direct native-PDF API: `grok-4.3`.
3. Google direct native-PDF API: `gemini-3.1-pro-preview`.
4. Codex CLI authenticated by ChatGPT subscription: `gpt-5.6-sol`, high
   reasoning, read-only ephemeral session.

Anthropic/Claude dispatch and fallback were prohibited. The direct-vendor
runner had `ANTHROPIC_API_KEY` unset and retried only the same vendor/model. The
Codex leg ran with `OPENAI_API_KEY`, `CODEX_API_KEY`, and `ANTHROPIC_API_KEY`
unset, proving ChatGPT-subscription authentication rather than API fallback.

## Raw-report integrity

| Leg | Verdict | Raw report SHA-256 |
|---|---|---|
| OpenAI `gpt-5.5` | REJECT | `019d454bc67400e011511decf23be68a333a6ac99820232319e7da606e3a6e52` |
| Grok `grok-4.3` | MINOR REVISIONS | `aaad10a510386c3892dad6dd10dcf5af795deac3ac6da1f397dfb827b0ab80da` |
| Gemini `gemini-3.1-pro-preview` | MINOR REVISIONS | `103c51ed17ac034f9623b4b47c00c6ab7d19b60dcc88d19b9231bac14bc39934` |
| Codex `gpt-5.6-sol` high | MAJOR REVISIONS | `fca7c370a0009e2b7189e2650da21db9935e0f0d49a4e3c1f70fd4dc15513f04` |

Raw reports are preserved verbatim. `P4_v1.0.241_exactpdf_truth_audit.md`
contains the separate ledger-first adjudication and closure contract.
