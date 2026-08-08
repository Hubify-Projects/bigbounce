# Pattern 070 — Cross-vendor agreement weighting in the truth-audit

**Class:** referee-variance-calibration
**First observed:** EXT RS5 (2026-07-01)

## Principle
LLM referees are high-variance. Weight the truth-audit priority by how many
INDEPENDENT vendors flag the SAME issue:
- **2-3 vendors flag the same concern** → almost certainly REAL. Prioritize; close it.
- **Single-vendor-only (esp. the harsh outlier)** → likely referee variance.
  Still read the source and cite why, but the prior is FALSE-POSITIVE.

## RS5 evidence
ChatGPT was the harsh outlier: it REJECTED P1A and P3 and returned 6-9 MAJORs
per paper, while Grok/Gemini gave the SAME papers major/minor-rev with far fewer
majors (P4: ChatGPT 7 MAJOR vs Grok+Gemini 0 MAJOR each). Source-cited audits
confirmed the ChatGPT-only majors were overwhelmingly FALSE-POSITIVE re-flags of
disclosed/scoped content; the genuinely-real items were the ones a 2nd vendor
also raised (e.g. Grok's P3 tier-1 wording bug).

## Rule
Never fake-accept to escape a harsh outlier, and never thrash rewriting a
single-vendor phantom. Use agreement as the signal; use the source citation as
the proof. (Extends pattern-064 grok-harsh-outlier — the outlier vendor rotates.)
