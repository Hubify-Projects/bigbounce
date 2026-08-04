# P1A final-hash truth audit — 2026-08-03

**Exact input:** `arxiv/paper1a_ech_nogo.pdf`, SHA-256 `210be8f0b285034d88b9854c532eaac4a32147cea2621dedbaaac94540bbc7f0` (8 pages).  Portfolio preflight receipt passed at dispatch, then the packet-level global crosscheck became stale because other portfolio artifacts changed.

## Provider record

| Provider | Outcome | Audit use |
|---|---|---|
| Grok 4.3 fallback | Returned native-PDF report; self-critique was blocked by the stale global P4/P5 crosscheck | Audited below |
| Gemini | Failed: initial packet stale; fallback `gemini-2.0-flash` is retired | No review result |
| Perplexity | Failed: API quota exhausted | No review result |

## Finding dispositions

| Finding | Disposition | Exact evidence |
|---|---|---|
| E1 — future date/internal version | **FALSE PREMISE / VENUE STYLE OPINION** | The dated stamp is 24 July 2026, earlier than this 3 August audit; it is a reproducible manuscript revision marker, not a future claim. |
| E2 — remove AI disclosure | **FALSE / WOULD BREAK COMPLIANCE** | The rendered disclosure is active at `paper1a_ech_nogo.tex:4100`. IOP's reviewed policy requires disclosure when generative AI is used (`ACCELERATION_AUDIT_2026-07-24.md:160`). |
| E3 and M1 — arbitrary 100 cm^-3 benchmark | **ALREADY DISCLOSED / REFLAG** | Abstract and Eq. (10) call it deliberately elevated, not a physical density; §III supplies the exact conversion, 68.4-order comparison, omitted factors, and state/EoS limits. Earlier exact-PDF audits already checked the arithmetic. |
| E4 — contact coefficient lacks convention caveat | **FALSE PREMISE** | The same abstract identifies minimal ECH and immediately bounds the NJL/direct-channel convention and excluded sectors; §II–III gives the normalization bridge and Appendix A is an audit aid, not a missing premise. |
| E5 — scalar transparency lacks scope | **FALSE PREMISE** | The abstract explicitly says on-connection-shell, not off-shell, and names the excluded quantum/anomaly, non-minimal, propagating-torsion, and global/topological sectors. |
| M2 — omitted higher-order torsion terms | **FALSE PREMISE** | The minimal first-order action has no independent torsion-square term; torsion is algebraically eliminated. Extensions alleged by the finding are expressly outside scope. |
| N1/N2 | **VENUE OPINION / PASS** | Figure count is editorial; citation result is positive. |

## Decision

**0 genuinely-new-real defects.** This exact hash does **not** require manuscript reopening on the usable review findings. This is not a three-provider consensus: Gemini and Perplexity failures must remain visible, and a later re-run requires a freshly restamped portfolio receipt plus repaired provider routing/quota.
