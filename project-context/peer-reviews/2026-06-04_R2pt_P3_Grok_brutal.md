# P3 2026-06-04_R2pt — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 16.1s

---

**Referee Report: P3 (Physical Review D)**

**P3-E1 (ESSENTIAL)**  
Section: Entire manuscript (50 pp)  
Problem: The manuscript is 50 pages long. PRD methods/catalog papers are typically 15–30 pages. The contribution (a multi-survey anomaly catalog plus one Fisher forecast) does not justify this length; the text is dominated by internal pipeline documentation, repeated caveats, and before/after diagnostics.  
Required fix: Condense to ≤22 pages. Remove all pipeline paths, companion-artifact citations, version strings, and non-essential appendices. Retain only the core methods, catalog summary, and validated results.

**P3-E2 (ESSENTIAL)**  
Section: Abstract (first paragraph) + §V  
Problem: Multiple σ(fNL) values are presented from different null procedures (linear extrapolation, Fisher-positivity-respecting α² form, jackknife, Gold+Silver subset) without explicit qualification that they are not on the same scale. The text itself notes that the linear form produces unphysical results outside a narrow anchor region.  
Required fix: State a single, clearly labeled headline forecast with its exact assumptions and error budget; move all variants to a table with explicit caveats or remove them.

**P3-E3 (ESSENTIAL)**  
Section: Abstract + §I + §VII  
Problem: The abstract does not accurately summarize what the paper proves. It is dominated by tier distinctions, retractions (“RETRACTED”), and instructions on what not to use, rather than a concise statement of the delivered catalog and its validated properties.  
Required fix: Rewrite the abstract to state only the final Path-C catalog size, the single headline σ(fNL) result with its measured α, the genuine novelty fraction (17.8 % at top-1000), and the injection-recovery gate outcomes, without internal audit language.

**P3-E4 (ESSENTIAL)**  
Section: Throughout (e.g., “Path-C”, “Wave 14-VVV”, “Wave 14-KKKK”, “§VI D caveat (i)”, “companion artifact pipelines/…”, “v3.1.74”, “2026-06-04_R2pt”)  
Problem: The manuscript contains extensive version-history language, internal audit tags, review-log artifacts, and pipeline-path placeholders. These are not journal-clean.  
Required fix: Remove every instance. Replace with standard section references or delete.

**P3-E5 (ESSENTIAL)**  
Section: Abstract + §IV A + §VI C  
Problem: The 17.8 % genuine novelty fraction is a single-sample point estimate at the top-1000 DESI stratum only. The text explicitly states the full-catalog rate is untested and could be higher or lower. The abstract and conclusions present it without this qualification.  
Required fix: State the 17.8 % figure with its exact scope and uncertainty; do not allow it to stand as a catalog-wide claim.

**P3-M1 (MAJOR)**  
Section: §II D + §III + Table I  
Problem: The paper reports six injection-recovery gates but only three pass the formal ≥50 % threshold at 5σ. The three failures are retained with “informative cross-validation diagnostics,” yet the headline catalog still aggregates all surveys.  
Required fix: Either (a) restrict the catalog-grade sample to the three surveys that pass the gate or (b) clearly segregate the catalog into “gate-pass” and “diagnostic-only” tiers with separate headline numbers.

**P3-M2 (MAJOR)**  
Section: §V + Appendix C  
Problem: The multi-tracer Fisher forecast assumes zero observational systematics (fiber assignment, photo-z, PSF, foregrounds, completeness). The text acknowledges this but still presents the numerical improvement as the primary result.  
Required fix: Downgrade the forecast to an idealized upper bound and state the required systematic budget explicitly.

**P3-M3 (MAJOR)**  
Section: §III D + §VI A  
Problem: 98 % of the LAMOST anomalies are identified as a training-bias artifact. The native retrain still fails the 5σ continuum-dip gate (5.8 %). The contribution is retained in the headline aggregate “for completeness.”  
Required fix: Remove LAMOST from the headline 378,280 count or move it to an explicitly labeled exploratory appendix with zero weight in any downstream statistic.

**P3-M4 (MAJOR)**  
Section: §I + §VII  
Problem: Claims of “largest-scale,” “first multi-survey,” and “unprecedented” are not benchmarked against the full literature (Baron & Poznanski 2017, Liang et al. 2023, Nicolaou et al. 2026). The 141× scaling is an aggregate across six surveys, not a like-for-like methodology comparison.  
Required fix: Provide a concise, quantitative literature comparison table and remove all superlative language.

**P3-N1 (MINOR)**  
Section: Fig. 3 caption  
Problem: The figure is labeled “[Cross-transfer baseline map — superseded by Path-C native counts]” — internal review language.  
Required fix: Remove the bracketed clause.

**P3-N2 (NIT)**  
Section: Multiple figure captions and table footnotes  
Problem: Repeated use of phrases such as “see §VI D caveat (i)” and “companion artifact …” clutters the text.  
Required fix: Replace with standard citations or delete.

**P3-N3 (NIT)**  
Section: §IV C  
Problem: The three highlighted DESI×SDSS matches are presented as representative while the full 637-cluster manifest is relegated to a parquet file.  
Required fix: State the total number of clusters once and move the three examples to a short table.

## Summary recommendation  
**REJECT**

The manuscript cannot be accepted in its current form. It is more than twice the typical PRD length for this class of paper, is saturated with internal audit and version-control language, presents multiple inconsistent σ(fNL) numbers without clear qualification, and contains an abstract that does not honestly summarize the delivered results. The central catalog claim is also compromised by the inclusion of surveys that fail the stated validation gates. A complete rewrite that is (i) ≤22 pages, (ii) free of all pipeline artifacts and retractions, and (iii) restricted to the three gate-passing surveys would be required before reconsideration.