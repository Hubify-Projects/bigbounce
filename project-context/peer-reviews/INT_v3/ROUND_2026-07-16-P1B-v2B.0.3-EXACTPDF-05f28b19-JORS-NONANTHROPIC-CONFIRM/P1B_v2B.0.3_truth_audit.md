# P1B v2B.0.3 Exact-PDF Confirmation Truth Audit

## Binding

- Commit: `70853e35f3cba34f05f309d2178c517ff880fa74`
- Exact PDF SHA-256:
  `05f28b195ba4ee62c57acc0314a3c9566f27375a5ec3e22287473918191b6911`
- Providers: Codex CLI through ChatGPT subscription, direct xAI/Grok API, and
  direct Google/Gemini API.
- OpenAI API used: **no**
- Anthropic used: **no**

## Verdict-first audit

Grok returned REJECT, Gemini MAJOR, and Codex-subscription MAJOR. The
exact-window numerical claims and the v2B.0.3 verifier-race closure held. One
new publisher-side concurrency defect is verified.

| Finding | Disposition | Evidence / closure |
|---|---|---|
| Missing archive DOI | **OPEN EXTERNAL GATE → DP1B-15** | Explicit submission blocker, not an undisclosed manuscript defect. |
| Manuscript v2B.0.3 conflicts with software 0.1.2 | **FALSIFIED** | Manuscript and software use separate, explicitly named version namespaces. |
| Mutable GitHub artifact links | **OPEN EXTERNAL RELEASE GATE → DP1B-15** | Current hashes bind bytes, but submission still requires an immutable archive. |
| Nonstandard JORS section arrangement | **EDITORIAL** | The required software, implementation, quality-control, availability, reuse, license, funding, and competing-interest content is present. No scientific or software claim changes. |
| No minimal public-API snippet | **EDITORIAL, ADOPTED** | v2B.0.4 adds a compact executable-style three-line example for reader usability. |
| Concurrent publishers can cross-bind metadata and bytes | **VERIFIED MAJOR → DP1B-16** | Package 0.1.2 wrote publisher A's result, then derived size/digest by re-reading the shared pathname. Publisher B could replace the path before those reads, allowing A's metadata to authenticate B's bytes. Package 0.1.3 derives receipt fields from A's immutable serialized bytes; a deterministic interleaving regression requires the resulting mixed pair to fail validation. |

## Recursive-improvement consequence

The v2B.0.2 closure protected verifier-side snapshot coherence. This round
extends the same invariant to publisher-side provenance: content metadata must
be derived from the producer's immutable in-memory snapshot, never from a shared
pathname after publication. The new finding becomes an executable regression in
the same closure unit. Readiness remains 56 pending exact v2B.0.4 confirmation,
archive publication, correspondence metadata, and human software review.
