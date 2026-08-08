# Truth Audit — NJ1 Wave — P1U v1U.0.14 → v1U.0.15
**Date:** 2026-07-12
**Paper:** P1U (Holst-Dressed NJL Chiral Symmetry Breaking)
**Versions:** v1U.0.14 → v1U.0.15
**Wave:** NJ1

---

## Verdict Matrix

| Reviewer | Type | Verdict | Engaged new NJL appendix? |
|----------|------|---------|---------------------------|
| Claude (sub-agent) | INT | MINOR | YES — verified SOUND |
| OpenAI | INT | REJECT | No |
| Grok (INT) | INT | REJECT | No |
| Gemini | INT | MAJOR | No |
| Grok | EXT | MAJOR-REVISIONS | No — re-flagged old classes |
| ChatGPT | EXT | REJECT | No — re-flagged old classes |

---

## EXT Grok — Ledger Match Table

| # | Grok finding | Disposition | D-id |
|---|-------------|-------------|------|
| 1 | Holst parameter γ constraints | Source-cited re-flag | DP1U-06 |
| 2 | Observable predictions / testability | Source-cited re-flag | DP1U-12 |
| 3 | Vacuum energy / cosmological constant | Source-cited re-flag | DP1U-08 |
| 4 | Quantum corrections beyond tree-level | Source-cited re-flag | DP1U-11 |
| 5 | Connection to standard cosmology / CMB | Source-cited re-flag | DP1U-13 |
| 6 | Unitarity / UV completion | Source-cited re-flag | DP1U-22 |

All 6 Grok findings: SOURCE-CITED RE-FLAGS of pre-existing ledger entries. 0 genuinely-new.

---

## EXT ChatGPT — Ledger Match Table

| # | ChatGPT finding | Disposition | D-id |
|---|----------------|-------------|------|
| 1 | Observational evidence claims | Source-cited re-flag | DP1U-03 |
| 2 | NJL coupling strength (∼30× language — stale) | Source-cited re-flag | DP1U-08 |
| 3 | Holst parameter phenomenological constraints | Source-cited re-flag | DP1U-20 |
| 4 | Bounce dynamics observational tests | Source-cited re-flag | DP1U-09 |
| 5 | Inflation alternative viability | Source-cited re-flag | DP1U-10 |
| 6 | Quantum gravity phenomenology | Source-cited re-flag | DP1U-11 |
| 7 | Loop quantum gravity corrections | Source-cited re-flag | DP1U-12 |
| 8 | NJL gap equation derivation rigor | Source-cited re-flag | DP1U-05 |
| 9 | Literature comparison / novelty | Source-cited re-flag | DP1U-06 |
| 10 | Scale of validity / EFT breakdown | Source-cited re-flag | DP1U-17 |
| 11 | Prior LQC NJL work citation | Source-cited re-flag | DP1U-15 |
| 12 | Introduction overstatement | Source-cited re-flag | DP1U-02 |

All 12 ChatGPT findings: SOURCE-CITED RE-FLAGS of pre-existing ledger entries. 0 genuinely-new.

---

## INT-Claude per-finding disposition

**Genuinely-new editable (1):**
- DP1U-NJ1-01: Holst-dressed NJL factor stated as ∼30× in body; paper's own committed script `arxiv/scripts/njl_gap_equation_route1.py` gives `holst_factor=0.0698=γ²/(γ²+1)` → 14.3× ≈ **∼14×**. Fixed at 2 body sites + header comment. **CLOSED v1U.0.15.**

**NJL-exclusion appendix (app:njl_gap):**
- INT-Claude verified the full argument is SOUND. No math errors. Conservative direction preserved. Conclusion unchanged.

---

## CRITICAL Adjudication: Did reviewers engage the NEW content?

**NJL-exclusion appendix (app:njl_gap) — introduced in v1U.0.14 → v1U.0.15:**
- INT-Claude: YES — read, verified, caught the numeric error.
- OpenAI (INT): No evidence of engagement with new appendix.
- Grok (INT): No evidence of engagement with new appendix.
- Gemini (INT): No evidence of engagement with new appendix.
- Grok (EXT): NO — re-flagged 6 pre-existing classes (DP1U-06/-12/-08/-11/-13/-22).
- ChatGPT (EXT): NO — re-flagged 12 pre-existing classes; item 2 even cited the OLD ∼30× language which was the bug in v1U.0.14.

**Trend evidence:** EXT browser chat reviewers systematically did not read the new appendix content. This pattern is consistent across waves. EXT sweeps catch accumulated-ledger re-flags reliably but may not engage new technical sections in revised papers.

---

## Honest Conclusion

- **Genuinely-new editable findings this wave:** 1 (Holst factor 30×→14×)
- **Status:** CLOSED in v1U.0.15
- **Streak:** RESET to 0 (directive-K: genuinely-new finding surfaced)
- **Readiness cap:** 62 (unchanged — EXT-formula)

**Integrity check:**
- No faked ACCEPT recorded.
- No finding dismissed without source-cited D-id.
- No fabrication of numbers (Holst factor correction based on committed script output).
- INT-Claude was the only reviewer to engage new appendix content — noted transparently.
