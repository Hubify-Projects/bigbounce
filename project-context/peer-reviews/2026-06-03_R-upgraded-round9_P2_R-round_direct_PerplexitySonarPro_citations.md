# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-03_R-upgraded-round9
**Wall time**: 9.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=36262, completion=886, total=37148, search_context_size=low, cost={'input_tokens_cost': 0.10879, 'output_tokens_cost': 0.01329, 'request_cost': 0.006, 'total_cost': 0.12808}

---

## PAPER-B1 — **BLOCKER** — intro, abstract, §2.1, §A.1, §A.2

The paper’s core citation chain on the Cai/Li-Brandenberger factor-of-two is internally inconsistent and likely mis-cites the source papers’ exact normalization chain. The text alternates between “commutator doubling,” “Planck/Komatsu-Spergel convention,” and “single time-ordering” as if these were the same issue; the appendix then claims the missing factor is both a normalization difference and an operator-algebra identity, which needs source-level verification against the actual papers, not just narrative reconciliation.  

**Fix:** Verify the exact \(f_{\rm NL}\) normalization and in-in ordering directly from Cai et al. and Cai & Brandenberger, then rewrite the chain so each factor of two is sourced to one specific paper statement or equation, not inferred post hoc.

## PAPER-B2 — **BLOCKER** — abstract, §2.1, §A.2

The arXiv/paper metadata for several cited references is presented as verified in prose, but the manuscript does not show any reliable cross-checkable bibliographic evidence in-text. This is especially risky for the newer 2025–2026 citations and for entries used to support key numeric claims, because fused metadata or wrong arXiv IDs would propagate directly into the paper’s strongest claims.  

**Fix:** Audit every cited paper against arXiv/ADS/publisher records and add a corrected bibliography pass; explicitly confirm author list, title, venue, year, and arXiv ID for each citation that supports a quantitative claim.

## PAPER-B3 — **MAJOR** — abstract, §2.1, §4, §5

The paper repeatedly cites SPHEREx, MegaMapper, and Heinrich et al. forecast numbers as if they were directly interchangeable across estimator types and fiducial models, but the text itself admits the forecasts are bispectrum-only, SDB-only, or joint Fisher analyses with different statistics. The resulting significance chain mixes observables and priors, then reuses the same \(r\) overlap factor outside the bispectrum context, which is not justified in the cited material.  

**Fix:** Separate the forecasts into distinct blocks by observable and statistic, and cite each number only in the context in which the original source derived it; do not transfer \(r\) or \(\sigma(f_{\rm NL})\) across unrelated Fisher matrices without a source-backed derivation.

## PAPER-B4 — **MAJOR** — §3, §4, §6

The manuscript asserts exact or near-exact agreement with multiple external forecast papers while simultaneously applying substantial ad hoc corrections: template mismatch, \(\epsilon\)-corrections, \(b_\phi\) marginalization, GR degradation, and convention reversal. The combined chain is presented as a single citation-backed result, but the underlying literature does not obviously support this composite significance estimate as written.  

**Fix:** Recast the forecast as a new in-house sensitivity study and clearly label which pieces come from published forecasts versus which are the paper’s own extrapolations; cite the original sources only for the inputs they actually provide.

## PAPER-B5 — **minor** — abstract, §2.1, §5

Several citations are used for claims that are broader than what the referenced papers likely state, especially where the manuscript infers “robustness,” “exactly half,” or “complete observational package” from a single source. These are the kind of claims that often come from a narrow calculation in the cited paper, not from the generalized conclusion the manuscript attributes to them.  

**Fix:** Tighten claim language to the exact scope of each citation and remove global wording unless multiple independent sources support it.

## PAPER-B6 — **nit** — bibliography/in-text

The paper uses many “et al.” citations and heavily compressed source chains, which makes citation forensics hard and increases the chance of fused metadata errors. This is not itself a fatal problem, but it is a reliability risk in a manuscript whose main contribution is citation-driven numerical synthesis.  

**Fix:** Add a short citation audit table in the appendix listing the highest-impact references, with verified title, year, venue, and arXiv ID.
