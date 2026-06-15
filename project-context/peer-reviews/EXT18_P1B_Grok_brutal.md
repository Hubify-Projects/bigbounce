# P1B EXT18 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=5a3c98e9 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 118.9s

---

**Referee Report**

**P1B-E1**  
**Title page (p. 1)**  
**Problem**: The submission carries the date stamp “(Dated: June 13, 2026)”. A manuscript cannot be submitted to PRD with a publication date in the future.  
**Required fix**: Remove or correct the date.  

**P1B-E2**  
**Abstract / Scope statements (pp. 1–2 and throughout)**  
**Problem**: The text repeatedly states that the work is “NOT a spin-torsion theory module”, “not a distinctive ECH prediction”, and “not a competitive sky detection”. These disclaimers are required because the central results (the \(\Delta N_{\rm eff}\) posterior, the \(\beta\) recovery bias, the spectator-ALP \(\beta\)) are either null results or are reproduced by standard GR+ALP. The abstract therefore over-states the novelty of the verification exercise.  
**Required fix**: Rewrite the abstract to state only what is actually demonstrated (a null \(\Delta N_{\rm eff}\) test and a pipeline-validation exercise) without implying a new test of ECH.  

**P1B-E3**  
**Sections I, II, VI and all cross-references to “Paper I(a)”**  
**Problem**: The argument is not self-contained. Every load-bearing claim (“the 3.6\(\sigma\) headline”, the spectator-safe cut \(\Omega_a<0.01\), the \(\beta=0.342^\circ\pm0.094^\circ\) prior) is imported by citation to an unpublished companion. A standalone reader cannot verify the central numbers.  
**Required fix**: Either (a) reproduce the necessary likelihood definitions and priors inside this manuscript or (b) withdraw the paper until the companion is public.  

**P1B-E4**  
**Data Availability section (p. 15)**  
**Problem**: The reproducibility paragraph contains internal version-control strings (“v1B.0.72”, commit “b22f8cc9”, “HuggingFace dataset pending DOI”, “RunPod H200 instances”). These are production artifacts, not archival metadata.  
**Required fix**: Replace with stable, version-stamped DOIs or remove.  

**P1B-M1**  
**Figure 3 and §IV (pp. 7–8)**  
**Problem**: The pipeline-recovery bias \(\Delta\hat\beta=-0.032^\circ\) to \(-0.040^\circ\) is presented as a “methodology cross-check”. The caption and text never state the quantitative tolerance on this bias that would be required for the published 3.6\(\sigma\) claim to remain valid.  
**Required fix**: Supply an explicit bias budget (e.g., “bias must be < 0.01° for the 3.6\(\sigma\) result to be unaffected”).  

**P1B-M2**  
**Table I and §III (p. 19)**  
**Problem**: The one-sided 95 % upper limits on \(\Delta N_{\rm eff}\) are obtained by post-processing a two-sided chain after discarding the negative tail. The paper never demonstrates that the resulting one-sided credible interval is insensitive to the choice of prior boundary at \(\Delta N_{\rm eff}=-1\).  
**Required fix**: Show the limit under both a flat prior and a log-flat prior, or justify the truncation.  

**P1B-M3**  
**Length**  
**Problem**: 21 pages of technical verification material whose headline results are all null or “consistent with zero”. PRD does not publish 21-page methodology appendices as regular articles.  
**Required fix**: Condense to a 6–8 page Methods Note or move the bulk to an archival repository.  

**P1B-N1**  
**Multiple figure captions (pp. 6, 8)**  
**Problem**: Captions contain future production dates (“April 2026”, “pod run 2026-04-29”). These are internal bookkeeping entries.  
**Required fix**: Delete.  

**P1B-N2**  
**Equation (1) (p. 7)**  
**Problem**: The \(\chi^2(\beta)\) estimator is written without the usual inverse-variance weighting or pixel-window correction. The text later states that an inverse-variance re-fit changes the recovered angle by 0.006°. The equation as printed is therefore not the estimator actually used for the quoted numbers.  
**Required fix**: Either correct the displayed equation or label it “illustrative”.  

**P1B-N3**  
**Table II footnote a (p. 20)**  
**Problem**: The +4.3\(\sigma\) and –3.6\(\sigma\) tail distances are explicitly labelled “not a Bayes-factor or ln B exclusion”. The same numbers are nevertheless placed in the main table under the heading “vs \(\Lambda\)CDM”. This juxtaposition violates the journal’s requirement that headline significances be accompanied by an effect-size or model-comparison statistic.  
**Required fix**: Move the tail distances to a supplementary table or add an explicit “posterior-tail distance only” qualifier in the table header.  

**Summary recommendation**  
**REJECT**

The manuscript contains an impossible future date, is not self-contained, and consists of 21 pages whose principal quantitative results are all null or reproduced by standard \(\Lambda\)CDM+ALP. Even after the date and internal-audit artifacts are removed, the paper would still require either wholesale condensation or the simultaneous publication of the entire companion series before it could be considered by PRD.