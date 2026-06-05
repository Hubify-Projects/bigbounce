# P1B 2026-06-04_R2pt — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 10.1s

---

**Referee Report for HUBIFY-2026-001B (P1B)**

**P1B-B1 (ESSENTIAL)**  
Section: Abstract (p. 1) and throughout (e.g., Sec. III p. 3, Sec. VI p. 7, Sec. VIII p. 8).  
Problem: The abstract and body contain extensive internal audit tags, version-history language, review-log artifacts, and queued-task prose (e.g., “v1B.0.42”, “R-upgraded-round4 GEM-m2”, “queued for v1B.0.15+”, “in flight for Paper I(a) Table II”, “stale.csv (R̂−1 ∈ [0.23,0.86])”, “truth-audit falsification”, “audit on-record at shoes yaml audit.md”, “log marker MCMC DONE ITER2 OMP6”, “Wave 14”, “R12 GEM-M2 closure”). These are review artifacts, not journal prose.  
Required fix: Remove every instance of version numbers, dates, audit logs, “queued”, “in flight”, “stale”, “GEM”, and cross-paper coordination language from the body, footnotes, and tables. Retain only the final scientific content.

**P1B-B2 (ESSENTIAL)**  
Section: Abstract (p. 1) and Sec. I (p. 2).  
Problem: The abstract states three analyses are “reported as a null-consistency test”, “NOT the physical separation”, “not a competitive sky detection”, “not a distinctive ECH prediction”, and “requires fine-tuning”. The body repeats that none of the three analyses actually tests the ECH spin-torsion framework. The abstract therefore does not honestly represent a positive claim that the paper proves.  
Required fix: Rewrite the abstract to state only what is actually demonstrated: three null-consistency and pipeline-validation exercises performed in unmodified ΛCDM+ALP, each carrying explicit scope disclaimers that they do not test the ECH theory.

**P1B-B3 (ESSENTIAL)**  
Section: Sec. III (p. 3), Table I, Sec. V (p. 6), Table II.  
Problem: Marginal-tail extrapolations (“+4.3σ”, “−3.6σ”) are presented alongside pipeline-recovery SNRs (20.32σ, 25.71σ) and literature values (2.4–2.9σ, 3.6σ) without explicit qualification that they derive from different procedures and are not on the same statistical scale.  
Required fix: Add a single, prominent paragraph stating that all quoted σ values are method-specific and not directly comparable; remove or clearly segregate the marginal-tail extrapolations.

**P1B-M1 (MAJOR)**  
Section: Entire manuscript (12 pp).  
Problem: The paper is a technical-verification companion whose only load-bearing results are (a) ∆Neff consistent with zero in stock CAMB and (b) a NaMaster bias check at the 0.04° level. Both are negative or null findings. The manuscript length and framing exceed the actual incremental contribution.  
Required fix: Reduce to a concise methods note (≤6 pages) or withdraw; the current length is not justified by the scope disclaimers that dominate the text.

**P1B-M2 (MAJOR)**  
Section: Sec. VI (p. 7) and fn. 4.  
Problem: The spectator-ALP consistency claim is presented while simultaneously stating that the spectator regime requires ∼25× fine-tuning of θi and that the same β arises in standard GR. The text therefore does not establish a distinctive or robust consistency check.  
Required fix: Either remove the ALP section or reframe it strictly as an auxiliary parameter-space illustration with no claim of model support.

**P1B-M3 (MAJOR)**  
Section: Sec. VII (p. 8) and Table III.  
Problem: The cross-paper status table and “forward” paragraph contain live coordination language and version pinning that belong in an internal project tracker, not a journal article.  
Required fix: Delete Sec. VII and Table III entirely; any necessary cross-reference must be reduced to a single static citation.

**P1B-N1 (MINOR)**  
Section: Multiple locations (e.g., p. 3, p. 5).  
Problem: Repeated near-duplicate disclaimer sentences about the limited scope of the ∆Neff proxy and the NaMaster validation.  
Required fix: Consolidate into one clear scope statement per section.

**P1B-N2 (NIT)**  
Section: Table II caption and body text.  
Problem: Minor arithmetic-rounding note (“0.1-unit GetDist artifact”) and repeated footnotes about the same convergence diagnostics.  
Required fix: Remove or shorten.

## Summary recommendation
**REJECT**

The manuscript consists almost entirely of null results, pipeline validations, and explicit disclaimers that none of the reported analyses tests the ECH spin-torsion framework. It is further compromised by pervasive internal review artifacts, version-history language, and audit prose that have no place in a journal submission. Even after removal of those artifacts, the remaining scientific content does not constitute a substantial, self-contained contribution suitable for Physical Review D.