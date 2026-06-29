# P3 RC-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=8ed23638 pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 209.9s

---

**Referee Report (P3)**

**P3-E1** (Abstract, p. 1; §I, p. 2)  
The abstract headline “269,317 Recommended-Tier (378,280 Total)” is not reproduced by any single, unambiguous calculation in the body. The body repeatedly qualifies the same numbers with “≥”, “conservative lower bound”, “after 7-way dedup”, “excluding LAMOST exploratory tier”, and “Path-C unique”.  
**Required fix**: Replace the abstract sentence with the exact arithmetic that produces 269,317 and 378,280 from the six native-retrain catalogs after the 5″ deduplication step, or remove the headline numbers.

**P3-E2** (Abstract, p. 1; §V, p. 17–18)  
Abstract states the catalog “demonstrate[s] utility beyond source discovery” via \(f_{NL}\) constraints. Body (§V A) shows the multi-tracer improvement is only \(0.29\sigma\) from null and the de-biased central value is identical to the single-tracer baseline within the quoted uncertainty.  
**Required fix**: Remove or qualify the cosmological-utility claim in the abstract to match the body’s final calibrated statement.

**P3-E3** (§II D, p. 5; Table I, p. 9)  
The paper repeatedly juxtaposes \(S > 5\) rates from different surveys without the explicit qualifier “not directly comparable” at every instance. Table I footnote already concedes non-comparability, yet the main text and abstract do not.  
**Required fix**: Insert the qualifier at every cross-survey numerical comparison or convert all rates to a common, explicitly labeled scale.

**P3-M1** (Entire manuscript)  
30-page length with 8 tables, 12 figures, and extensive internal bookkeeping language (“Path-C”, “gate PASS/FAIL”, “reproducibility floor”, “committed production state”). PRD methods papers of comparable scope are typically ≤15 pages.  
**Required fix**: Condense to ≤18 pages; move all per-survey training logs, exact gate thresholds, and version-history prose to a companion data-release note.

**P3-M2** (§III A–H, p. 6–13; Fig. 3)  
SDSS and LAMOST anomaly-score distributions are shown on incompatible scales (log vs linear) with no conversion provided. The claim that the Path-C native retrain “compresses” the SDSS tail is therefore unquantified.  
**Required fix**: Supply a single, normalized cumulative distribution or explicit conversion factor.

**P3-M3** (§V A, p. 17–18; Fig. 9)  
The Fisher-forecast improvement is reported as “6.1 % central-value change” while the actual shift is \(0.29\sigma\) from the null and lies inside the 1\(\sigma\) envelope of the single-tracer baseline. Effect size (Cramér’s V or fractional amplitude) is never stated.  
**Required fix**: Replace the percentage language with a proper effect-size statement and the explicit statement that no detection is claimed.

**P3-M4** (Fig. 2, p. 7; Table I)  
The figure caption states “ACT DR6 excluded from science results” yet the table still lists the cross-transfer count. The visual and tabular presentations are inconsistent.  
**Required fix**: Remove the ACT row from Table I or add an explicit “verification baseline only” flag to both figure and table.

**P3-N1** (p. 1, multiple footnotes)  
Repeated use of internal project tags (“Path-C”, “§III E”, “pipelines/p3_anomaly_engine”) in the main text. These are not defined for a standalone reader.  
**Required fix**: Replace with descriptive phrases or move to a methods appendix.

**P3-N2** (Table I, p. 9)  
SIMBAD-unmatched fractions are labeled “novelty” while the text correctly notes they measure database coverage, not discovery. Caption and column header are therefore misleading.  
**Required fix**: Rename column “SIMBAD-unmatched fraction (database-coverage diagnostic)”.

**P3-NIT1** (Throughout)  
Inconsistent use of “z-scored” vs “standardized” for the anomaly score \(S\). Minor notation cleanup required.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a technically ambitious multi-survey anomaly search whose headline numbers cannot be unambiguously reconstructed from the text, whose cosmological claims exceed what the data demonstrate, and whose length and internal bookkeeping language are incompatible with PRD standards. The methodological transparency is commendable but does not compensate for the absence of a single, reproducible definition of the delivered catalog or for the over-statement of the \(f_{NL}\) result. A substantially shortened version that (i) fixes the abstract–body drift, (ii) enforces consistent cross-survey language, and (iii) removes all unverifiable “largest” and “utility” claims could be reconsidered.