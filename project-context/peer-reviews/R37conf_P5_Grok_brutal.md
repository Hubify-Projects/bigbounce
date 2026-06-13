# P5 R37conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.72.pdf` md5=544b6af2 pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 80.9s

---

**Referee Report**

**Paper:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample (Houston Golden)

**Journal target:** Physical Review D

**Findings (adversarial audit)**

**P5-E1 (ESSENTIAL)**  
Section: Title page / first paragraph (rendered p. 1)  
Problem: “Dated: June 2026 — v0.1.72-2026-06-13” and repeated internal version strings (“v1.0.166”, “v0.1.72”) appear in the body.  
Required fix: Remove all version-control strings, internal tags, and future dates from the manuscript.

**P5-E2 (ESSENTIAL)**  
Section: Throughout (e.g., p. 2, 4–5, 7, 10, 12, 15–17, 19–22)  
Problem: Dozens of literal pipeline paths (“pipelines/p5_desi_chirality/outputs/… .json”, “desi_env_vweb.parquet”) and commit-style filenames are embedded in the scientific text. These are internal bookkeeping artifacts.  
Required fix: Delete every such string; replace with archival data-product DOIs or table numbers only.

**P5-E3 (ESSENTIAL)**  
Section: Abstract-level text (p. 1) and §VIII (p. 16)  
Problem: The headline claim “the CW fraction shows no environment dependence beyond the catalog-monopole offset” rests on the DESIVAST primary path (n_void = 56,981). The V-Web secondary path (n = 428) is repeatedly stated to be “sample-size limited” and “dominated by counting noise.” The abstract does not carry the same explicit caveat that appears in the body’s final calibrated statement.  
Required fix: Rewrite the abstract sentence to match the body’s weakest (void-bin) calibrated statement exactly, including the n = 428 qualifier.

**P5-E4 (ESSENTIAL)**  
Section: §V (p. 6) and Table III (p. 8)  
Problem: σ_from half values for different classes (n = 428 vs n ≈ 4 × 10^5) are placed side-by-side in the same table and figure without an explicit “not directly comparable” qualifier at every juxtaposition. Instruction 7 violation.  
Required fix: Add the qualifier in every table/figure caption and every paragraph that lists multiple σ_from half numbers.

**P5-E5 (ESSENTIAL)**  
Section: §II (p. 3) and repeated citations to “Paper IV [3]”  
Problem: The entire statistical framework (monopole offset Δf_CW = −0.0026, σ_pred formula, look-elsewhere corrections) is imported from an unpublished companion (“not yet peer-reviewed”). The paper is not standalone.  
Required fix: Either (a) make the present manuscript self-contained by reproducing the necessary derivations and numbers, or (b) withdraw until Paper IV is public and peer-reviewed.

**P5-M1 (MAJOR)**  
Section: §VIII.A and Table VIII (p. 17)  
Problem: The DESIVAST void sample (n = 56,981) yields Δf_CW = +0.0007 (null). The V-Web void sample (n = 428) yields −0.68σ. The paper treats the former as the “primary” result while the latter is the only direct tidal-tensor measurement. No quantitative reconciliation of the two is provided.  
Required fix: Supply a single, pre-registered decision rule that explains why the smaller but methodologically cleaner V-Web measurement is subordinated.

**P5-M2 (MAJOR)**  
Section: Fig. 3 (p. 9) and Table III (p. 8)  
Problem: The void bin (n = 428) 95 % Jeffreys interval is [0.435, 0.530] and comfortably contains 0.5. The paper nevertheless headlines “no environmental signal.” With this n the test has essentially no power to detect any plausible effect size.  
Required fix: Add an explicit power calculation or state the minimum detectable |Δf_CW| at 80 % power.

**P5-M3 (MAJOR)**  
Section: §VI.A (p. 7) and multiple “earlier draft” sentences (p. 6, 11, 12, 17)  
Problem: Repeated references to “an earlier draft quoted |σ| = 11.32”, “R7”, “R8”, and superseded numbers remain in the text.  
Required fix: Remove all draft-history language.

**P5-N1 (MINOR)**  
Section: Table I (p. 4)  
Problem: p_99 separation = 0.30″ is listed without units in the column header; the value itself is given with a double prime. Inconsistent formatting.  
Required fix: Standardize units.

**P5-N2 (MINOR)**  
Section: Fig. 1 caption (p. 4)  
Problem: “median 0.168” redshift is given without stating whether it is the median of the full matched sample or the chirality-relevant subsample.  
Required fix: Clarify.

**P5-NIT1 (NIT)**  
Multiple figure captions contain parenthetical pipeline paths that survived editing.

**Summary recommendation**  
**REJECT**

The manuscript contains multiple internal version-control strings, literal pipeline paths, and “earlier draft” language that have no place in a PRD submission. It is not self-contained: every load-bearing statistical claim is imported from an unpublished companion paper. The single most cited environmental bin (V-Web voids) contains only 428 galaxies and is explicitly dominated by counting noise, yet the abstract presents a global “no environmental dependence” conclusion without the corresponding power caveat. These are not cosmetic issues; they violate PRD standards for reproducibility, self-containment, and honest reporting of statistical limitations. The paper must be rewritten after Paper IV is public, all internal artifacts removed, and the abstract brought into exact register with the weakest calibrated statement in the body.