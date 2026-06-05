# P1B 2026-06-04_R5clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 199.7s

---

### Referee Report for PAPER P1B  

**Overall Assessment**  
The paper presents three verification analyses supporting a companion paper on Einstein-Cartain-Holst (ECH) cosmology. While the technical scope is clear, the manuscript contains significant confabulation risks, particularly regarding numerical provenance, internal artifacts, and unresolved inconsistencies. The reproducibility framework is noted but insufficiently validated. Below are detailed findings requiring revision.  

---

#### **Findings**  

**ESSENTIAL**  
- **P1B-E1: Abstract ∆Neff and H0 values lack direct provenance**  
  - Section: Abstract (p. 1)  
  - Problem: The abstract reports ∆Neff = −0.020 ± 0.169 (full-tension) and ∆Neff = +0.065 ± 0.17 (Planck+BAO+SN), but these values are not traceable to specific scripts/data in the reproducibility repository. The GitHub repo requires regeneration of chains, but no pre-computed chains or scripts validating these exact numbers are provided.  
  - Fix: Provide direct links to:  
    (a) Cobaya output files (e.g., `.csv`/`.txt`) for the frozen chains yielding these values.  
    (b) Scripts reproducing the abstract’s posterior means/errors without regeneration.  

- **P1B-E2: Inconsistent β recovery in NaMaster analysis**  
  - Section: IV (p. 5)  
  - Problem: The pipeline-recovery bias is claimed as "stable" at 0.032° (abstract), but the text states it scales with amplitude (0.040° at β = 0.342°). This contradicts the narrative of stability and lacks quantification of amplitude-dependence.  
  - Fix: Report a systematic floor (e.g., "bias ≤ 0.040°") and add a table showing bias/SNR for all injections (β = 0, 0.27°, 0.342°).  

**MAJOR**  
- **P1B-M1: Internal audit artifacts in body text**  
  - Section: III (p. 3, Table I footnote; p. 4, "Key finding")  
  - Problem: Version-control language appears (e.g., "Sample-count stratification (reconciliation)" in Table I footnote; "earlier count erroneously quoted" in Sec. III). These are inappropriate for publication.  
  - Fix: Remove all reconciliation notes, audit tags, and version-history references (e.g., "iter2"). Report final numbers without historical context.  

- **P1B-M2: Arithmetic inconsistency in ALP fine-tuning**  
  - Section: VI (p. 6) and Abstract  
  - Problem: The abstract claims the ALP requires θ_i ≪ 1 (∼25× tuning), but the MCMC uses θ_i ∈ [0.5, 2] (natural range). This contradicts the spectator-consistency disclaimer.  
  - Fix: Restrict ALP-MCMC priors to θ_i ∈ [0.01, 0.1] for spectator compliance or clarify that the MCMC samples the dark-energy-ALP regime (excluded from claims).  

- **P1B-M3: Unqualified σ values in pipeline vs. sky detection**  
  - Section: Abstract, IV (p. 5)  
  - Problem: The pipeline-recovery SNR (20.32σ) and published sky-detection significance (2.4–2.9σ) are presented adjacently without explicit caveats, risking conflation.  
  - Fix: Add bold disclaimer: "Pipeline SNRs reflect MC-injection recovery, not physical sky significance (2.4–2.9σ from [2,3])."  

**MINOR**  
- **P1B-m1: Unreproducible χ² decomposition**  
  - Section: III (p. 4, Table II footnote)  
  - Problem: χ² total = 14037.4 ± 5.6 is derived from GetDist, but no script for this decomposition is in the reproducibility repo.  
  - Fix: Add script to compute χ² decomposition from chain samples.  

- **P1B-m2: Ambiguous dataset attribution for β = 0.342°**  
  - Section: Abstract, VI (p. 6)  
  - Problem: The abstract cites β = 0.342° ± 0.094° (3.6σ) from "published joint WMAP+Planck" [2], but the text notes the actual analysis used Planck PR4/NPIPE via a code repository.  
  - Fix: Clarify in abstract: "β = 0.342° ± 0.094° (3.6σ) from Planck PR4/NPIPE reanalysis of [2]."  

**NIT**  
- **P1B-n1: Duplicate phrasing**  
  - Section: I (p. 2), Abstract  
  - Problem: "Scope of this paper" appears identically in Abstract and Introduction.  
  - Fix: Remove redundancy; retain only in Introduction.  

- **P1B-n2: Overlong footnote**  
  - Section: First-page footnote (p. 1)  
  - Problem: Disambiguation footnote spans 10+ lines, disrupting readability.  
  - Fix: Move to Appendix or shorten to 3 lines.  

---

#### **Paper Length**  
The paper is 10 pages, below PRD’s typical 15–30 pp for methods papers. However, the content is dense and technically focused. **No reduction recommended.**  

---

### Summary Recommendation  
**MAJOR REVISIONS**  

**Justification**  
The paper’s core technical contributions (MCMC proxy, pipeline validation, ALP check) are valuable but undermined by critical confabulation risks. Essential issues include untraceable abstract numbers (P1B-E1), inconsistent bias reporting (P1B-E2), and internal artifacts (P1B-M1). Major revisions must address numerical provenance, remove audit language, resolve ALP fine-tuning contradictions, and qualify σ-value contexts. The reproducibility repository requires expansion with static outputs (not just regeneration scripts) for all headline figures. Until these are resolved, the paper cannot be accepted.