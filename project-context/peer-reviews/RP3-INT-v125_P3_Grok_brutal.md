# P3 RP3-INT-v125 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=c4700948 pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 69.8s

---

**Referee Report**

**P3-E1 (ESSENTIAL, Abstract + §IIID p.5)**  
Abstract states “a Native-Trained Novelty Fraction from 37.3 Million Sources”. Body (§IV A) computes the 17.8 % figure from a 1 000-object top-stratum cross-match against 18 catalogs; the 37.3 M denominator never enters that calculation. The abstract claim is therefore not traceable to the quoted number.  
*Fix*: Replace with the actual measured fraction and its sample definition, or remove the phrase.

**P3-E2 (ESSENTIAL, §IIID p.5 & Table I)**  
The 17.8 % (Wilson 68 % CI 17.8 % ± 1.2 %) is presented as “genuine novelty fraction”. It is the complement of the archival cross-match rate on a deliberately high-score slice; it is not a catalog-wide purity. No statement quantifies how the fraction would change under a different score threshold or under the full 378 k catalog.  
*Fix*: Add explicit scope limitation and a threshold-sensitivity test.

**P3-M1 (MAJOR, §IIID & §VA)**  
All per-survey anomaly scores \(S\) are normalized to each survey’s own validation split (Eq. 2). The text repeatedly juxtaposes raw \(S\) values or rates across surveys (e.g., DESI 0.87 % vs SDSS 3.38 %). Although a parenthetical disclaimer exists, it is not repeated at every comparison. PRD requires an explicit “not directly comparable” qualifier at every such juxtaposition.  
*Fix*: Insert the qualifier at each occurrence or move all cross-survey rate comparisons to a single, clearly labeled subsection.

**P3-M2 (MAJOR, §VA & Fig. 9)**  
The multi-tracer \(\sigma(f_\mathrm{NL})\) improvement (8.98 → 8.14) is stated to lie “within the \(1\sigma\) envelope”. The envelope shown is the single-tracer Fisher forecast; the actual posterior width after marginalization over the measured \(\alpha_{jk}\) uncertainty is not recomputed. The claim that “no statistically significant improvement” is therefore not demonstrated at the stated precision.  
*Fix*: Provide the full multi-tracer posterior width or withdraw the quantitative statement.

**P3-M3 (MAJOR, §IIID & Table I footnote ¶)**  
The 798 Gaia + eROSITA objects are labeled “exploratory” because they fail the 5\(\sigma\) injection-recovery gate, yet they are added to the “recommended tier” (269 317). The tier definition is therefore internally inconsistent with the gate criteria used for the validated subset.  
*Fix*: Either remove the 798 from the recommended tier or redefine the tier to include an explicit “exploratory” sub-tier.

**P3-N1 (MINOR, throughout)**  
Several figure captions (Figs. 3, 7) and Table I omit units on the anomaly-score axis or on the SIMBAD-unmatched column.  
*Fix*: Add units.

**P3-N2 (MINOR, §IIID)**  
The 58.8 % aggregate SIMBAD-unmatched fraction pools four surveys with different selection functions and depths. No weighted or stratified version is shown.  
*Fix*: Add a footnote or supplementary table giving the survey-weighted value.

**P3-NIT1 (NIT)**  
Minor typographic inconsistencies in Table I column headers (“\(N^\uparrow_\mathrm{anom}\)” vs “\(N_\mathrm{anom}^\uparrow\)”).

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a large, carefully processed multi-survey anomaly catalog with unusually explicit handling of training-set bias and cross-survey non-comparability. However, three essential traceability and definitional inconsistencies (abstract novelty fraction, tier membership of injection-recovery failures, and the multi-tracer Fisher claim) plus the repeated cross-survey score juxtapositions without uniform qualification fall below PRD standards for a data-product paper. These items are straightforward to correct; once addressed the work would be suitable for PRD.