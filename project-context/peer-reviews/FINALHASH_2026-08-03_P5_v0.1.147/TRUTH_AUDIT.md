# P5 exact-final-hash truth audit

- Candidate: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf`
- Exact SHA-256: `3c1c484118d21ecab9a26655135df9d982c27d375095c2693b4376a86317b18e`
- Receipt: `project-context/SSOT/final-acceptance/portfolio-preflight-2026-08-03.json` (`PASS`, HEAD `97258772`)
- Round: `FINALHASH_2026-08-03_P5_v0.1.147`; context `AJ exact final candidate`
- Raw outputs: sibling flat files `FINALHASH_2026-08-03_P5_v0.1.147_P5_{Gemini_cosmology,Grok_brutal,Perplexity_citations}.md`

## Provider outcomes and evidence limits

| Route | Outcome |
|---|---|
| Grok | **Completed** on fallback (`grok-4.3`); exact hash and 46-page identity in header; pass 2 added no findings. The implementation rasterizes at most 25 pages, so pages 26–46 were not visually supplied. |
| Gemini | **Failed** before provider dispatch. Primary and fallback packet builds hit the parallel receipt-evaluator race. |
| Perplexity | **Failed** before provider dispatch. Primary and fallback packet builds hit the same race. |
| OpenAI API / Anthropic | **Unavailable by design** in this engine run; the tool explicitly disables both routes. |

The main-process receipt verification passed before dispatch. The worker-only “stale receipt” messages are a concurrency artifact: `verify_receipt()` runs an evaluator containing process-global stdout redirection simultaneously in three threads. HEAD and canonical P5 source/PDF remained clean and hash-matched.

## Finding-by-finding adjudication

| Finding | Truth-audit verdict | Exact-PDF/source basis and prior disposition |
|---|---|---|
| E1 post-hoc focal path invalidates inference | **RE-FLAG-DISCLOSED; fatal premise falsified** | Abstract and §5 explicitly say exploratory, post-hoc, and not preregistered. Table `hierarchy_sensitivity` places all three paths side-by-side; every CI contains zero, and the demoted unrestricted path has the more null-favorable `p=0.76` versus focal `0.66085`, so the ranking did not select the largest p-value. Prior full chronology/adjudication: `INT_v3/TRUTH_AUDIT_RESWEEP_2026-07-23.md`; the requested consolidation table was closed in v0.1.145. |
| E2 abstract hides the three paths | **FALSIFIED** | Abstract names the any-hole, T-Web, Tempel, and ASTRA paths as sensitivity/secondary diagnostics and discloses the hierarchy change. The side-by-side table states `p=0.76` and `0.66085`; an abstract need not duplicate the full sensitivity table. |
| E3 title/abstract misrepresent physical scope | **FALSIFIED** | Title explicitly says “Classifier-Labelled.” Abstract closes with “catalog-specific non-detection for classifier labels, not a physical-handedness, real-space, or cosmological constraint.” The suggested “No Environment Dependence” title would be stronger and less accurate than the present “Test.” |
| M1 internal-review language | **RE-FLAG-DISCLOSED / no defect** | “Demoted,” “sensitivity,” and “whole-tree family-wise” describe the transparent statistical hierarchy. Compiled source contains no `R7/R8` review tags. Removing the hierarchy history would weaken the required post-hoc disclosure. |
| M2 mixed nulls lack comparability qualification | **FALSIFIED / re-flag** | §5 distinguishes analytic monopole comparisons from label-shuffle nulls and says different null hypotheses are not conflated. Captions repeatedly state when rows are not comparable or are not pooled. Prior audit `R52_P5_TRUTH_AUDIT.md` F3 reached the same source-grounded verdict. Repeating one exact stock sentence at every juxtaposition is a prompt preference, not a missing control. |
| M3 length | **EDITORIAL OPINION** | Exact candidate is 46 line-numbered AASTeX pages with extensive diagnostics, robustness tests, artifact tables, and appendices. Grok only received pages 1–25 and therefore could not assess the full organization. No AJ page-limit defect is established. |
| M4 abstract scalars omit post-inspection provenance | **FALSIFIED** | The abstract states the exact hierarchy-change/post-inspection caveat immediately after the focal scalar and names the demoted paths. |
| N1 histogram caption mismatch | **FALSIFIED** | “Peaks at z≈0.15–0.2 (median 0.168)” is consistent with a visible peak slightly above 0.15; peak bin and median are different descriptors and both lie in the stated interval. |
| N2 duplicated phrases | **FALSIFIED / cosmetic** | Exact-source searches find neither `canonical canonical-mask` nor `the the` in compiled prose. Repetition of “post-hoc” is deliberate disclosure. |
| N3 future draft date | **FALSIFIED** | August 3, 2026 is the actual candidate date, not a future date; “Draft version” is AASTeX-generated review furniture. |
| Additional: no frozen reproducibility section | **KNOWN GATE, not new** | Data and Code Availability and Appendix artifact registers occur after the 25-page Grok image cap. They bind public inputs and retained artifacts while explicitly stating that the exact v0.1.147 public tag/Zenodo snapshot remains a pre-submission task. |
| Additional: no effect sizes | **FALSIFIED** | The focal effect size `Delta f_CW=+0.00145442`, SE, CI, and multiple fractional-amplitude/systematic-budget scales are reported. Cramér’s V accompanies the large contingency statistic where applicable. |
| Additional: Paper IV makes result non-standalone | **FALSIFIED / re-flag** | The manuscript includes a self-contained Paper IV classifier appendix; the focal contrast uses public labels and is reproducible from public inputs alone. It independently re-measures the monopole and explicitly limits Paper IV-dependent diagnostics. |

## Net decision

- Genuinely-new-real defects: **0**.
- Known pre-submission gate: create/verify the immutable v0.1.147 Git tag and Paper V Zenodo snapshot, replace the explicit availability placeholders, then rebuild/re-audit (already tracked; not newly found).
- Reopen P5: **NO**. The sole completed vendor report adds no new real finding. This round is not multi-provider/full-document evidence because two providers failed and Grok saw only pages 1–25; that coverage limitation must travel with the no-reopen decision.

## Recovered full-document Gemini attempts (FINALHASH2 / FINALHASH3)

- Both attempts passed the exact-PDF hash and fresh portfolio-receipt gate at stable HEAD `e28b1671`; the candidate remained SHA-256 `3c1c484118d21ecab9a26655135df9d982c27d375095c2693b4376a86317b18e` (46 pages).
- `FINALHASH2`: native-full-PDF `gemini-3.1-pro-preview` reached the provider deadline (`DeadlineExceeded`) after roughly 600 seconds. The runner then invoked `gemini-3.5-flash`, but the enclosing bounded host session ended before that fallback could complete. No report file was written.
- `FINALHASH3`: a bounded retry used native-full-PDF `gemini-3.5-flash` as the primary model. It also reached `DeadlineExceeded` at 600 seconds. The duplicate same-model fallback was intentionally terminated; no report file was written.
- No additional provider call is warranted. The earlier failed/partial flat outputs remain preserved under the original `FINALHASH_2026-08-03_P5_v0.1.147` names; neither recovered attempt produced findings that could be truth-audited.

### Recovered-attempt net

- Genuinely-new-real findings: **0 returned** (provider unavailable; this is not an acceptance signal).
- Reopen P5: **NO CHANGE / NO** based on the completed Grok report and the existing source-grounded audit above.
- Evidence limitation remains: there is **no completed full-document Gemini report**, and the only completed vendor leg saw rasterized pages 1–25 of 46. This limitation must remain attached to the no-reopen decision.
