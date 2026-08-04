# P1B final-hash truth audit — 2026-08-03

**Exact input:** `arxiv/paper1b_namaster_proof.pdf`, SHA-256 `2fb957101604066382ddb604da41b9fe3bc2a48ae4a799ca25c2b34eaac6267a` (6 pages). Portfolio preflight receipt passed at dispatch, then concurrent packet construction hit stale global receipt state.

## Provider record

| Provider | Outcome | Audit use |
|---|---|---|
| Gemini 2.5 Pro | Returned native-PDF report and pass-2 no-new result | Audited below |
| Grok | Failed before dispatch: packet receipt stale | No review result |
| Perplexity | Failed before dispatch: packet receipt stale | No review result |

## Finding dispositions

| Finding | Disposition | Exact evidence |
|---|---|---|
| E1 — future date/internal revision | **FALSE PREMISE / VENUE STYLE OPINION** | 24 July 2026 predates this audit. §10 explicitly distinguishes the manuscript stamp `v2B.0.16` from software version `0.1.7`; this is transparent document provenance, not a false software-version claim. |
| E2 — placeholder DOI/future deposit | **FALSE PREMISE** | PDF §10 gives live Zenodo DOIs `10.5281/zenodo.21481753` and `10.5281/zenodo.21481842`, both deposited 21 July 2026 (past). JORS kit verifies both resolve HTTP 200 at `JORS_SUBMISSION_KIT_P1B_2026-07-24.md:195,270–272`. |
| M1 — `SHA-250` typo | **HALLUCINATED / FALSE** | The exact rendered PDF says `SHA-256` throughout its receipt description and validation-artifact paragraph; no `SHA-250` token occurs in the source or PDF text. |
| N1 — repeated Windows wording | **FALSE PREMISE** | PDF §10 says Linux and Windows; CI covers Linux Python 3.10–3.13 and Windows Python 3.12. No duplicated-Windows phrase occurs. |

## Decision

**0 genuinely-new-real defects.** This exact hash does **not** require manuscript reopening on the usable Gemini review. This is not a multi-provider consensus: Grok and Perplexity failed solely at the stale-receipt gate, so a later board-grade rerun needs a fresh receipt and successful additional provider legs.
