# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-direct-P1B
**Wall time**: 8.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=24038, completion=880, total=24918, search_context_size=low, cost={'input_tokens_cost': 0.07211, 'output_tokens_cost': 0.0132, 'request_cost': 0.006, 'total_cost': 0.09131}

---

## PAPER-PER-B1 — **BLOCKER**
**Section:** Bibliography / all citation-dependent claims  
The paper’s reference list is not present, so none of the cited works can be verified inside the provided source. That makes every claim “supported” by citations un-auditable here, and the paper itself does not supply the actual bibliography entries needed to check arXiv IDs, titles, authors, or venues.  
**Fix:** Include the full `references.bib` contents or an inline bibliography appendix with complete metadata for every cited work.

## PAPER-PER-B2 — **MAJOR**
**Section:** Sec. 3, Table `verification`, footnote `fn:rhat_csv`; Sec. 7, Table `mcmc_inventory`  
The manuscript asserts “all 17 sampled parameters” but the table body plus surrounding text are internally inconsistent about the parameter count and chain composition. The paper alternates between 7+10, 8+9, and “17 total” for different chains, while the iter2 chain explicitly says 8 cosmological + 9 nuisance parameters and the frozen chains explicitly say 7 cosmological + 10 nuisance parameters; the text then reuses “17 sampled parameters” across contexts without clearly separating the two distinct parameterizations.  
**Fix:** Split the parameter-count statements by chain and state them once per chain, with a compact enumerated parameter list for each configuration.

## PAPER-PER-B3 — **MAJOR**
**Section:** Sec. 5, “Model-comparison statistics: not reported in this paper” and surrounding caveats  
The paper says Bayes-factor / AIC / BIC statistics are not reported because the chain readout is inconsistent and Savage-Dickey is invalid, but it still repeatedly makes strong model-comparison-like claims elsewhere (“canonical quintom signature,” “quintom-B territory,” “empirical anchor for Paper I(a)”). That is a scope leak: the paper rejects formal comparison metrics but continues to present interpretive preference claims as if they were supported by the same chain.  
**Fix:** Separate descriptive posterior summaries from any model-preference language, or add a dedicated, reproducible comparison analysis with the same likelihood stack.

## PAPER-PER-B4 — **MAJOR**
**Section:** Sec. 4 and Sec. 6, NaMaster and ALP numerical claims  
The manuscript presents injected-recovery SNRs, birefringence angles, and ALP parameter ranges as validated results, but the text gives no reproducible chain-to-claim mapping for the key numbers beyond narrative assertions. In particular, the ALP range logic mixes \(\Delta\phi/f_a\), \(\theta_i\), and \(C_{a\gamma}\) in ways that are only loosely explained, so the claim that \([0.17,0.43]^\circ\) follows from the stated parameter box is not transparently derived.  
**Fix:** Add explicit derivation steps or a compact table showing how each quoted range/value is computed from the sampled parameters and numerical integration outputs.

## PAPER-PER-B5 — **minor**
**Section:** Abstract; Sec. 4; Sec. 6  
The paper repeatedly uses “published Planck/ACT DR6 \(2.4\)–\(2.9\sigma\)” and “published joint Planck+ACT value \(3.6\sigma\)” as background facts, but the exact source mapping is muddled: one citation is used for the joint value, another for the individual experiments, and the sentence structure blurs which significance belongs to which dataset. This is a citation-forensics clarity problem even if the numbers themselves are plausible.  
**Fix:** State each measurement next to its own citation in one sentence, without cross-combining the single-experiment and joint-analysis significances.

## PAPER-PER-B6 — **nit**
**Section:** Preamble comments / version-history block  
The source contains a large audit-history/comment log that is not part of the scientific manuscript and reads like internal revision notes. Even if stripped before submission, it is a serious hygiene issue in the working source and obscures the actual paper text for reviewers.  
**Fix:** Move the audit log to a separate developer-only file and keep the LaTeX source clean.
