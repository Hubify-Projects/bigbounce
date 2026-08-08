# P2 v1.7.120 exact-PDF provenance

## Frozen artifact

- Paper: P2
- Version: v1.7.120
- Frozen PDF: `proof/02_full_draft.v1.7.120.pdf`
- PDF SHA-256: `2111e62f6eb2423dc1880fad5fa90c8da1feac75ff4b44891573f6d90762cc06`
- Frozen TeX SHA-256: `e9df08c5e46aa91bde70dd8ccc72a7adb5af23b7d4e2099780401b1092f2fa5c`
- Frozen BibTeX SHA-256: `9f9aa52364f751f8d0d1cd351777ceb4b81720933ae0f6af345b550202e77f93`
- Frozen Fig. 2 SHA-256: `85eb82fbe4d9167b5a7b84e2f0fa77e3f8663c656a1a5fa0c996d02f27f17cd5`
- Frozen figure generator SHA-256: `73663c873281b8d8c35a2be248ad762a06cf4012b302665dc8c80a7655785cef`
- Review label: `WORKTREE-v1.7.120-e9df08c5`

## Raw review reports

| Report | Model | SHA-256 |
|---|---|---|
| `API_P2_openai.md` | OpenAI `gpt-5.5` | `b4b5af95aa9a35093516d0ac5e748afc3cba838f68759200584684a5fcded656` |
| `API_P2_gemini.md` | Google `gemini-3.1-pro-preview` | `a7ed17c861ada8bd5387d00ac700fb428e6e6a076732885d3bb21beaeb09a88e` |
| `API_P2_grok.md` | xAI `grok-4.3` | `aeaad8f86ffddc3b9471c5b2e82554e90e03716b745e81395e2d11bd937e27e9` |
| `RAW_P2_codex_gpt-5.6-sol_high.md` | Codex `gpt-5.6-sol`, high | `78a1636fb4c45af7d0df7c5ce9689a62b8639efb8b82e629ea4bae10d570468f` |

Direct-vendor reports used native PDF transport and no cross-vendor fallback.
The independent Codex session used ChatGPT-subscription login with API-key
environment variables removed, sandbox read-only, and exact frozen artifacts.
Codex session ID: `019f607f-9c12-7f42-ad28-65f0406b546a`.

No Anthropic or Claude model, dispatch, or fallback was used.

## Audit artifacts

- PDF audit: `audit/P2_v1.7.120_pdf_audit.md`
- Contact sheet SHA-256: `2ee2ae0d8dca3c4fe02cf1889308e1bac912cecf66618a2637aa82ef392a941d`
- Exact orbit/sign checker SHA-256: `678463f2e070db915e1480066e9672d01207afbf1d631deb1ac84978caa8f6cd`
- Raw direct-vendor dispatch log: `manifest.jsonl`

The manifest contains one successful attempt per model and pins every review to
the same PDF hash. No API keys or secret values are recorded.
