# P3 2026-06-04_R6clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 13.2s

---

**Referee Report for P3 (Physical Review D)**

**P3-E1 (ESSENTIAL)**  
**Location**: Abstract (opening paragraph, pp. 1–2)  
**Problem**: The abstract is not an abstract. It is a 1.5-page technical summary containing repeated numerical definitions (“378,080 point-source tier”, “200 Planck CMB-patch tier”, “∼113,000/∼265,000 split”), explicit instructions on which number downstream users must cite, and multiple self-referential caveats (“the 378,280 headline aggregates the two tiers for survey-coverage completeness only and should never be quoted as a single object-density statistic”).  
**Required fix**: Replace the entire block with a conventional 150–250 word abstract that states the principal result (a catalog of N unique anomalies from M sources) and the main methodological claim without usage instructions or tier arithmetic.

**P3-E2 (ESSENTIAL)**  
**Location**: Abstract and repeated throughout §§I–VII  
**Problem**: The manuscript contains pervasive version-history and “supersedes” language that belongs in a review response, not a journal article. Examples: “the Path-C rebuild… supersedes this with 388,493 survey-level detections”, “the prior linear-extrapolation σ(fNL)=8.27±2.37 is superseded by the corrected formula”, “the local-linear approximation fails at the α=0 stationary point”, “the linear-extrapolation value 10.64 is the unphysical artifact”.  
**Required fix**: Remove every occurrence of “supersedes”, “prior… is superseded”, “unphysical artifact of the local-linear mapping”, and similar audit-log phrasing. Present only the final methodology and results.

**P3-E3 (ESSENTIAL)**  
**Location**: Abstract (p. 1) and §V (multiple paragraphs)  
**Problem**: Multiple distinct σ(fNL) values derived from different procedures (jackknife α, Fisher-positivity-respecting α² form, local-linear extrapolation, Gold+Silver subset) are presented with numerical envelopes that are not on the same statistical footing. The text itself acknowledges that the linear-propagation envelope produces unphysical results, yet still quotes the superseded numbers.  
**Required fix**: Report a single, clearly labeled central value and credible interval obtained from one consistent procedure. All alternative calculations must be moved to an appendix or removed.

**P3-M1 (MAJOR)**  
**Location**: Entire manuscript (49 pages)  
**Problem**: The paper is grossly over-length for its actual contribution (release of a large anomaly catalog plus a single empirical α measurement). The text is dominated by repetitive tier definitions, before/after diagnostics, injection-recovery tables, and self-referential caveats.  
**Required fix**: Condense to ≤20 pages. Move all per-survey processing details, full injection-recovery curves, UMAP stability tests, and the NANOGrav MCMC appendix to a companion data-release paper or online supplement. Retain only the catalog summary statistics, the cross-match novelty result, and the final α measurement.

**P3-M2 (MAJOR)**  
**Location**: Abstract and §IV A  
**Problem**: The headline claim of a “genuine novelty fraction of ∼17.8%” is immediately qualified in the same paragraph as “a single-sample point estimate measured at the top-1,000 score stratum; the full-catalog rate is empirically untested”. The title and opening sentence nevertheless present 378,280 “Path-C Unique Anomalies” as the primary deliverable.  
**Required fix**: Either (a) remove the novelty-fraction claim from the abstract and title until a score-stratified measurement exists, or (b) state explicitly that the 17.8% figure applies only to the top-1,000 DESI objects and is not a catalog-wide property.

**P3-M3 (MAJOR)**  
**Location**: §II D and repeated in §§III, VI D  
**Problem**: The manuscript is structured as a running commentary on its own revision history (“Path-C rebuild protocol”, “before/after native retrain baseline”, “the cross-transfer scan is preserved as the Path-C ‘before / after’ baseline”). This is not journal-clean prose.  
**Required fix**: Rewrite the methods section to describe only the final per-survey native-retraining pipeline. Delete all references to the earlier cross-transfer scan except as a one-sentence methodological motivation.

**P3-N1 (NIT)**  
**Location**: Multiple locations (e.g., abstract, §V)  
**Problem**: Duplicate or near-duplicate phrasing of the 378,080 + 200 stratification and the instruction that downstream users must use the point-source tier.  
**Required fix**: State the tier definition once in the abstract and once in §II; remove all subsequent repetitions.

**P3-N2 (NIT)**  
**Location**: §VI D (multiple sub-items)  
**Problem**: The “Path-C residual caveats” section is written in the style of an internal checklist (“(a) Analysis caveats and their resolutions”, “(i) DESI in-sample training–test overlap”).  
**Required fix**: Convert to conventional scientific prose or move to supplementary material.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript is a data-release paper whose scientific payload is a large anomaly catalog plus one empirical bias-enhancement measurement. In its present form it is 49 pages of repetitive tier arithmetic, version-history language, and self-correcting Fisher derivations that violate Physical Review D standards for both length and narrative cleanliness. The abstract is unusable, multiple σ(fNL) values are presented on inconsistent statistical footings, and the text reads as an extended response to previous referee comments rather than a finished journal article. A radically shortened version (≤20 pages) that reports only the final catalog statistics, the 17.8% top-1,000 novelty point estimate (properly caveated), and the single headline α measurement could be reconsidered; the current submission cannot.