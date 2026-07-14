# P1A v1A.0.122 — normalized truth audit of the exact-PDF CQG Note confirmation board

## Artifact and routing provenance

- Source/review commit: `0bb7fddf231f8dfb2778f332e2500d618fb6339e`
- Source SHA-256: `9f83351baa7a47dc11771927a12e05259c70a0d74040b46d43e56390cbfc9adc`
- PDF SHA-256: `e2607d1a8476aa8df9e5e89b04595655b81048be34cabb4bec273e59c4c87e04`
- PDF: 7 pages; review profile `CQG-NOTE`
- Allowed routes only: ChatGPT-subscription Codex CLI, Gemini native PDF, and Grok native PDF. No OpenAI API or Anthropic/Claude request was dispatched.

| Valid route | Model / modality | Verdict | Severity tags | Time |
|---|---|---:|---:|---:|
| ChatGPT-subscription Codex CLI | `gpt-5.6-sol`, high; exact source/PDF/Git plus all seven attached page renders | **MINOR REVISIONS** | 0 MAJOR / 2 MINOR | 444 s |
| Gemini native PDF | `gemini-3.1-pro-preview`; inline native PDF | **ACCEPT** | 0 MAJOR / 0 MINOR | 31.3 s |
| Grok native PDF | `grok-4.3`; native file upload | **ACCEPT** | 0 MAJOR / 0 MINOR | 13.5 s |

## Normalized verdict

**MINOR REVISIONS: 0 major, 2 valid minor reproducibility/provenance defects.**

All three reviewers support the narrow central scientific claim and close the substantive v1A.0.121 clarity findings. The two native-PDF API reviewers could inspect the rendered manuscript but not the repository implementation behind its artifact links. The subscription Codex leg had the stronger source/artifact modality and found two concrete mismatches. Those findings survive truth audit, so the normalized board cannot be laundered into ACCEPT.

This verdict is not journal acceptance and authorizes no readiness uplift.

## Finding 1 — active artifact exceeds the declared cutoff scope

**Adjudication: VALID MINOR.**

The manuscript states at active source lines 2647--2653 and 4767--4770 that only three rows at `Lambda=M_Pl` are evaluated and no cutoff above `M_Pl` is evaluated. The exact script pinned by v1A.0.122 instead says it evaluates six rows and loops over both `M_Pl` and `M_Pl/sqrt(gamma_BI)`. The exact pinned JSON lists six rows, three at `Lambda/M_Pl=1.9104017997521754`. Hash comparison proves that commit `b587cb7bb8e075aa9d0245ba8257fcef7ff196b8` contains the same six-row script and JSON reviewed locally.

The scalar sign, coefficient, threshold equation, and three displayed `M_Pl` values are not wrong. The defect is a reproducibility-scope contradiction. Closure must make the active machine-readable artifact emit only the three declared `M_Pl` rows, while preserving the legacy six-row artifact in Git/review history.

## Finding 2 — mixed immutable and mutable artifact links

**Adjudication: VALID MINOR.**

The Data and Code Availability section uses commit-pinned links, but active source macro `artifactnamed` targets `blob/main`. Its three active uses occur at source lines 2655, 4721, and 4802. PDF annotation inspection confirms mutable reader-facing links on pages 3, 6, and 7. Thus the v1A.0.122 closure pinned the dedicated availability links but not every occurrence.

Closure must point every reader-facing reproducibility occurrence at the immutable commit that actually contains the corrected script/JSON. A two-commit sequence is mandatory: first commit the artifact correction; then pin the manuscript to that predecessor commit. A self-referential pin would be impossible and must not be fabricated.

## External gates kept separate

1. Alternate-regulator calculation: open and adequately disclosed; blocks regulator-independent scope only.
2. Matched physical Lorentzian stress tensor/observable: open and adequately disclosed; blocks running-based phenomenology only.
3. State-specific renormalized axial-current expectation value: open and adequately disclosed; blocks physical finite-density stress/equation-of-state inference only.
4. Commit-pinned GitHub URLs: local objects exist, but all four tested immutable URLs returned HTTP 404 before the serialized push. This blocks remote release/reproducibility status only.
5. Immutable archive/DOI: not completed; release gate only.
6. Independent human CQG review/editorial decision: not run; journal-status gate only.

## Process acceleration and next-run improvement

Gemini and Grok ran concurrently: their serial sum was 44.8 s and their critical path was 31.3 s, saving 13.5 s (30.1%). All three legs were launched together; their runtime sum was 488.8 s and the board completed in 444 s, saving 44.8 s (9.2%) versus serial dispatch.

Content-addressed API packets failed closed on commit/PDF mismatch, and attaching the seven already-audited page renders gave the subscription referee complete visual coverage without a new render. The subscription leg nevertheless consumed 2,243,865 reported input tokens (2,003,968 cached) because the LaTeX source contains extensive historical commented blocks. A future confirmation packet should include a generated, hash-bound active-source projection alongside the canonical source; that preserves auditability while preventing historical dead text from dominating the review context.
