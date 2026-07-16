# P1B v2B.0.4 exact-PDF truth audit

Review binding:

- commit: `f9307445092f16da7634013a89b1ee03bcba8f6d`
- PDF SHA-256: `dfe16983718fc8073f256c86a653d6fc3de7ae5fc99788b015e71b33360748b4`
- Codex modality: ChatGPT-subscription CLI, registry-scoped detached tree
- direct providers: xAI/Grok and Google/Gemini native-PDF
- Anthropic: not used
- OpenAI API: not used

## Verdicts

| Reviewer | Raw verdict | Truth-audited result |
|---|---|---|
| Grok 4.3 | MAJOR REVISIONS | One disclosed external gate; two contradicted/overstated artifact claims |
| Gemini 3.1 Pro Preview | MAJOR REVISIONS | Archive/contact gates retained; CRediT and healpy disclosure closed; runtime request non-dispositive |
| Codex GPT-5.6 Sol high | MINOR REVISIONS | Three valid, novel, mechanically preventable findings |

## Per-finding dispositions

### Grok

1. **Archive identifier — VERIFIED, disclosed external gate → DP1B-15.**
   The manuscript explicitly states that no persistent identifier exists and
   forbids submission until package 0.1.3 is archived
   (`arxiv/paper1b_namaster_proof.tex:271-274`). This is a real release gate,
   not a hidden manuscript defect or a completed claim.
2. **The 1.41e-18 scalar is non-retained — DISCLOSED RE-FLAG.**
   The paper already says the original workspace tensor was not retained and
   that the scalar is neither a self-contained reproducibility claim nor a
   universal bound (`arxiv/paper1b_namaster_proof.tex:183-195`). No falsified
   reproducibility claim is present.
3. **Worked examples are external/unretained — CONTRADICTED.**
   The minimal example is executable without paper data
   (`packages/namaster-proof/examples/synthetic_window.py`); the real PyMaster
   example, output, receipt, and regression are retained under
   `packages/namaster-proof/examples/` and
   `packages/namaster-proof/tests/test_retained_integration.py`; the physical
   campaign artifacts are retained under
   `reproducibility/p1_namaster_500mc/results/`. Optional dependencies are
   disclosed, not missing evidence.

### Gemini

1. **Archive identifier — VERIFIED, disclosed external gate → DP1B-15.**
2. **CRediT roles and contact — PARTLY VERIFIED.**
   A CRediT-compatible author-contribution section is mechanically closeable
   and is added in v2B.0.5. Correspondence details remain author-supplied human
   metadata and stay open under DP1B-15; no email is invented.
3. **healpy version disclosure — VERIFIED MINOR.**
   Retained production receipts consistently bind healpy 1.19.0. v2B.0.5 states
   that tested version beside PyMaster 2.6.
4. **Receipt overhead benchmark — NON-DISPOSITIVE SUGGESTION.**
   The reviewer says this “would benefit” the reader, not that a claim is false.
   Filesystem-dependent microbenchmark timing is not required to support the
   exact-window or content-binding claims and no unmeasured speed claim is made.

### Codex subscription

1. **Non-standard JSON constants — VERIFIED NOVEL MINOR → DP1B-17.**
   Python's default encoder emits `NaN`/`Infinity`, and its decoder accepts
   them. v2B.0.5/package 0.1.4 uses `allow_nan=False` before either file is
   written and strict decoding during verification, with rejection regressions.
2. **CI path-filter gap — VERIFIED NOVEL MINOR → DP1B-18.**
   `test_legacy_equivalence.py` imports two production helpers outside the
   package tree, while the workflow previously triggered only on package and
   workflow paths. Both helper paths now trigger the package CI.
3. **Mask coordinate documentation — VERIFIED NOVEL MINOR → DP1B-19.**
   The README described Galactic latitude plus declination, while
   `make_native_latitude_window` applies both cuts to one native HEALPix
   latitude. v2B.0.5 corrects the coordinate contract and disclaims a survey
   footprint.

## Closure decision

This is not a clean wave: three genuinely novel valid minor findings were found.
They are closed in v2B.0.5/package 0.1.4 with regression coverage. Readiness
remains 56 because archive, correspondence metadata, fresh confirmation, and
human review remain open. A new exact-PDF board is required.
