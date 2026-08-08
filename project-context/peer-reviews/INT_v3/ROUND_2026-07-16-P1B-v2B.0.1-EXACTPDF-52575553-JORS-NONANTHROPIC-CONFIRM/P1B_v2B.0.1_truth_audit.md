# P1B v2B.0.1 Exact-PDF Confirmation Truth Audit

## Bound board

- Commit: `c7b6476794b9ba50c1ad81106d4ca57159ab6ff3`
- PDF SHA-256:
  `5257555381604e6083cb73624f5c2079118c3ea80fe0c3d9f3290bd10dfaf176`
- Grok 4.3: REJECT
- Gemini 3.1 Pro: MAJOR REVISIONS
- Codex subscription, GPT-5.6 Sol high: MAJOR REVISIONS
- OpenAI API used: no
- Anthropic used: no

## Confirmation result

The first-board code closures hold. No reviewer found a regression in exact
spectrum-support enforcement, finite-input validation, weight shape/sign
checks, or narrowed two-file receipt guarantees.

### Verified and closed in the next patch

1. The retained `SUPERSEDED.md` still said the completed physical rerun was
   unfinished. It now points to `physical_spectrum_v2/` as current.
2. The manuscript incorrectly associated the physical run's recorded residual
   with the package's zero-tolerance legacy comparison. It now distinguishes
   the production driver's `1e-10` gate from the separate zero-tolerance test.
3. Artifact paths are now full direct repository hyperlinks.
4. The remaining “changed receipts” wording is narrowed to changes in protected
   binding fields or caller-asserted metadata.
5. An independent real-PyMaster integration example now constructs an actual
   workspace, recovers an injected 0.25 degree angle exactly, measures operator
   equivalence at `6.776e-21`, and demonstrates the effective-ell shortcut
   recovering 0.315 degree instead. Its retained JSON and receipt are covered
   by the 24th regression test.

### Verified and still open

1. A persistent software archive identifier remains required before JORS
   submission.
2. Correspondence email and final affiliation/location are author-supplied
   submission metadata and were not invented.

### Falsified or modality-limited findings

1. Grok and Gemini said no code URL was present. The exact PDF contained an
   active direct package hyperlink; their native-PDF modalities did not expose
   the link target as plain text.
2. Grok said the physical artifacts did not exist and the test suite was
   unavailable. Both are present in the bound public commit; this was a
   PDF-only access limitation, not repository evidence.

## Readiness effect

No readiness increase is taken from a closure patch. P1B remains 56 pending a
new exact confirmation, persistent archive identifier, and human review.
