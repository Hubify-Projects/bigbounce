# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-postretro
**Wall time**: 8.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29519, completion=1019, total=30538, search_context_size=low, cost={'input_tokens_cost': 0.08856, 'output_tokens_cost': 0.01528, 'request_cost': 0.006, 'total_cost': 0.10984}

---

## Finding 1 — **BLOCKER** — L218-219 / abstract / Sec. 6

**ID:** PAPER-PER-B1  
**Issue:** The paper attributes the published cosmic-birefringence “headline” to **Eskilt2022** as a “joint WMAP+Planck” analysis, but the surrounding metadata is internally fused: it says “joint WMAP+Planck” while also labeling the same reference as “Planck PR4/NPIPE + WMAP9” in one place and “WMAP9 + Planck 2018 (PR3)” in another. That is a citation-chain red flag: the cited paper’s dataset label is not stable across the manuscript, and the author’s own revision log shows prior corrections bouncing between PR3 and PR4/NPIPE, which is exactly the kind of attribution drift that signals a misread source chain.  
**Fix:** Pick one dataset label that matches the cited paper and use it everywhere; if the published paper is being paraphrased, cite the exact paper text and remove the PR3/PR4/NPIPE cross-talk from the manuscript body.

## Finding 2 — **MAJOR** — L364-366, L606-608, L644-646

**ID:** PAPER-PER-M2  
**Issue:** The manuscript claims the published Planck/ACT DR6 birefringence numbers support a “3.6σ” headline and then separately uses a “3.9σ” inverse-variance combination as an auxiliary check. That is only defensible if the cited papers actually report the same observables and covariance structure the manuscript assumes; here the paper itself admits the combination “neglects shared calibration systematics,” which means the derived significance is not a citation-backed result from the literature but a paper-side arithmetic construct.  
**Fix:** Make the distinction explicit in the main text: headline result from the cited literature only, auxiliary combination clearly labeled as the authors’ own recomputation with no direct literature status.

## Finding 3 — **MAJOR** — L102-104, L760-764, Table 1B caption

**ID:** PAPER-PER-M3  
**Issue:** The manuscript repeatedly says the DESI DR2 \(w_0w_a\) chain is “converged” and then uses that chain as an empirical anchor for Paper I(a), but the chain status text is a moving target across the document and is mixed with version-history prose in the rendered source. This is load-bearing buried attribution: the claim depends on an on-disk artifact and a specific convergence threshold, yet the paper does not give a stable, publication-facing citation or artifact reference that can be audited independently.  
**Fix:** Move the convergence claim to a clean methods sentence with one reproducibility pointer and one exact artifact identifier; remove the version-history narrative from the live manuscript body.

## Finding 4 — **minor** — L165-170 / Table 1 / L559-563

**ID:** PAPER-PER-m1  
**Issue:** The paper states the \(\Delta N_{\rm eff}\) proxy is “stock CAMB with no torsion modifications,” then uses that proxy as “bounce-class compatibility” language. That is defensible as an inference, but it is not what the cited torsion literature directly says; the manuscript overstates the degree to which the proxy is a cited result rather than the authors’ own mapping.  
**Fix:** Rewrite as an explicit inference: “consistent with the authors’ phenomenological proxy for bounce-class models,” not “predicts” or “confirms” from the cited torsion references.

## Finding 5 — **minor** — L657-662

**ID:** PAPER-PER-m2  
**Issue:** The ALP section cites **Fujita2021** as prior study support, but the manuscript’s own wording makes the section sound like an extension of that paper while simultaneously claiming the calculation is “our internal model-independent MCMC fit.” That is a source-role ambiguity problem: the cited paper is being used both as precedent and as evidence for numerical claims it did not produce.  
**Fix:** Separate precedent from result. Keep Fujita2021 as background only, and attach the numerical fit claims to the paper’s own chain artifact rather than the prior citation.

## Finding 6 — **nit** — L92-96 / Table 1B footnote / L777-783

**ID:** PAPER-PER-n1  
**Issue:** The manuscript’s citation-chain formatting is inconsistent: the same result is introduced with multiple labels (“joint WMAP+Planck,” “published joint WMAP+Planck value,” “Planck PR4 + ACT DR6 EB-spectrum likelihoods”), which makes the attribution trail harder to audit.  
**Fix:** Standardize each cited result to one canonical label and one canonical dataset phrase, then reuse it verbatim throughout the paper.
