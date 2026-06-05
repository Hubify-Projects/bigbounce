# P4 2026-06-04_R3clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 206.0s

---

## Referee Report: P4 (2026-06-04_R3clean)

### ESSENTIAL Revisions  
**P4-E1: Abstract/Conclusions – Decomposition provenance**  
- **§**: Abstract, Conclusions (Sec. VII), Table VIII  
- **Problem**: The decomposition 99.3% (monopole leakage) / 12% (post-MASTER monopole-only null) / 88% (residual) / 25% (leg-as-proxy) lacks full traceability. The 25% leg-as-proxy contribution (Table VIII) is labeled "DIRECT" but lacks an explicit artifact reference in the table. The companion artifact (`pipelines/p2_chirality/outputs/canonical_provenance/morphology_template_l1_projection.json`) is only cited in prose (Sec. IV D), violating the requirement for scalar-by-scalar JSON provenance.  
- **Fix**: Add a dedicated column in Table VIII citing the exact artifact path for each entry. For the 25% value, specify the field in the JSON (e.g., `leg_proxy_induced_fraction`).  

**P4-E2: Arithmetic consistency – 12% residual calculation**  
- **§**: Sec. IV D, Table VIII  
- **Problem**: The 12% value (post-MASTER monopole-only null) is rounded from 12.2% (8.0e-7 / 6.55e-6 = 0.122). Rounding to 12% without qualification misrepresents precision. The subsequent 88% (100% – 12%) inherits this error.  
- **Fix**: Report as 12.2% ± [uncertainty] or state the rounding explicitly. Recompute the 88% residual using the exact fraction.  

### MAJOR Revisions  
**P4-M1: Paper length**  
- **§**: Entire document (56 pages)  
- **Problem**: Exceeds PRD typical length (15-30 pp for methods/catalog papers) without commensurate novel methodology. Redundancy exists (e.g., multiple dipole estimators in Table II explained in 4 pages; systematics discussed in 5 sections).  
- **Fix**: Condense to ≤30 pp by:  
  (a) Moving Sec. III (Methods), Sec. VIII (NaMaster appendix), and legacy pipeline details to supplementary materials.  
  (b) Consolidating Tables II, VI, VII, XVI into a single estimator-summary table.  
  (c) Removing circular discussions (e.g., repeated monopole-attribution in Sec. IV B, VI A).  

**P4-M2: Version-history artifacts in prose**  
- **§**: Abstract ("v1.0.154"), Sec. II B ("v1.0.76"), Sec. IV D ("v1.0.153")  
- **Problem**: Internal version tags (e.g., "v1.0.154") in body text are review artifacts inappropriate for publication.  
- **Fix**: Remove all version tags from the body. Retain immutable release tags *only* in Data Availability (§IX).  

**P4-M3: σ-value comparability**  
- **§**: Abstract, Sec. IV C, Table II  
- **Problem**: The abstract presents σ values (-0.12σ, +0.43σ, +3.64σ) without null-procedure context, violating the paper’s own note (Abstract: "σ values [...] are not directly comparable"). Table II mitigates this but is buried in §IV.  
- **Fix**: In the abstract, append each σ with its null type (e.g., "−0.12σ [MASTER label-shuffle null]"). Add a footnote to Table II summarizing null differences.  

### MINOR Revisions  
**P4-m1: Confidence-stratified dipole provenance**  
- **§**: Sec. IV E, Table X  
- **Problem**: The +3.29σ value for max(peq) ∈ [0.5, 0.6) cites `pathA_signal_hunt_results.json` but the artifact lacks the per-bin σ calculations.  
- **Fix**: Include per-bin σ computation code in the GitHub release or add derived fields to the JSON.  

**P4-m2: Duplicate phrases**  
- **§**: Sec. IV D ("canonical canonical-mask" ×2), Sec. VI G ("interpretation (ii)" ×7)  
- **Problem**: Redundant phrasing distracts from content.  
- **Fix**: Replace duplicates (e.g., "canonical mask" → "canonical footprint"; use acronyms for interpretations).  

**P4-m3: Abstract accuracy**  
- **§**: Abstract  
- **Problem**: Claims "diagnostic evidence for a Depth/Morphology-Correlated Canonical-Mask Residual" but the residual is attributed to systematics, not proven.  
- **Fix**: Replace "diagnostic evidence" with "evidence consistent with" to reflect the systematic-attribution narrative.  

### NITPICKS  
**P4-N1: Incomplete JSON references**  
- **§**: Table VIII  
- **Problem**: "DIRECT" status lacks artifact paths (e.g., for the 99.3% leakage).  
- **Fix**: Add hyperlinks or exact filenames for all "DIRECT" entries.  

**P4-N2: Spurious precision**  
- **§**: Sec. IV B (σ = 0.000279)  
- **Problem**: Overly precise uncertainty (0.000279) implies false rigor; the true uncertainty is dominated by spatial correlations.  
- **Fix**: Report σ = 0.0003 (1 sig-fig) and cite the bootstrap test.  

**P4-N3: Ambiguous "load-bearing"**  
- **§**: Sec. III A, Conclusions  
- **Problem**: Overuse of "load-bearing" (×11) without quantitative criteria.  
- **Fix**: Define "load-bearing" in a footnote (e.g., "primary estimator for cosmological null").  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

### Justification  
The paper presents a landmark chirality catalog and robust null result but requires significant revision to meet PRD standards. The 56-page length is excessive for the claimed contribution, and key scalars (e.g., the 25% leg-proxy) lack immediate provenance in tables. Version tags in the body prose are unprofessional, and σ values are inadequately contextualized in the abstract. However, the core science is sound: the monopole-mask leakage channel (99.3%) is rigorously demonstrated, the dipole null (-0.12σ) is well-supported, and the data release enhances reproducibility. Condensing the paper, excising version history, and clarifying scalar provenance will solidify this as a high-impact contribution.