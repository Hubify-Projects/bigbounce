# P4 2026-06-04_1733pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 158.9s

---

## Referee Report: Paper P4, v1.0.151

### ESSENTIAL Findings  
**P4-E1: Abstract/conclusions lack explicit provenance links for headline scalars**  
- **Section**: Abstract, Conclusions (Sec. VII)  
- **Problem**: Load-bearing scalars (-0.12σ, +0.43σ, +3.64σ, 99.3%, 12%, 88%, 25%, 0.75%) lack inline references to supporting JSON/scripts. While artifacts exist (e.g., `master_power_spectrum.json` for −0.12σ), the abstract/conclusions do not cite them, violating traceability standards.  
- **Fix**: Add explicit parenthetical citations for each scalar (e.g., "−0.12σ [JSON: master_power_spectrum.json]").  

**P4-E2: Inadequate qualification of σ-scale differences**  
- **Section**: Abstract, Sec. IV C, VII  
- **Problem**: σ values from incompatible null procedures presented without scale reconciliation:  
  - Real-space dipole (+0.43σ, per-pixel shuffle null)  
  - MASTER dipole (−0.12σ, label-shuffle null)  
  - Canonical residual (+3.64σ, binomial null)  
  No discussion of why these σ are directly comparable despite different null variances (e.g., bootstrap σ is 3× wider than binomial).  
- **Fix**: Add cautionary text (e.g., Sec. VII) clarifying σ scales are not interchangeable and specify null-dependent sensitivity floors.  

**P4-E3: Version-control artifacts in body text**  
- **Sections**: III E ("Retraction note: earlier drafts..."), IV C ("older snapshot value 2.75σ... retained only as historical"), VI G ("prior text... retracted")  
- **Problem**: Version-tracking language (retractions, snapshot references) violates journal prose standards.  
- **Fix**: Remove all versioning narratives; report only final canonical results.  

### MAJOR Findings  
**P4-M1: Excessive length unjustified by contribution**  
- **Section**: Entire paper (57 pp vs. PRD 15-30 pp norm)  
- **Problem**: Length driven by redundant diagnostics (e.g., 5 independent anchors for interpretation (ii) in Sec. VI G) and narrative asides (e.g., Sec. III E retraction rationale). Core methods-result contribution fits within 30 pp.  
- **Fix**: Condense to 30 pp by:  
  (a) Moving bias-hardening suite (Sec. III F), D4-TTA validation (Sec. III E), and signal-hunt diagnostics (Sec. IV E) to supplementary materials.  
  (b) Replacing legacy-snapshot comparisons with a summary table.  

**P4-M2: Decomposition narrative inconsistency**  
- **Section**: Sec. VI G, Table VIII  
- **Problem**: Table VIII claims 25% of the 88% residual explained by "leg-as-proxy," but Sec. VI G states this is a "partial-closure lower bound," not a measured fraction. Overstates precision.  
- **Fix**: Relabel Table VIII "leg-as-proxy" entry as "≥25%" and add caveat: "Lower bound from geometric proxy, not full template fit."  

**P4-M3: Unresolved provenance for regional CW fractions**  
- **Section**: Sec. IV B, Table XIII  
- **Problem**: Per-region CW fractions (e.g., RA [0°,90°): 0.4968) lack supporting JSON/scripts. Only global fraction has artifact (`global_cw_fraction.json`).  
- **Fix**: Add per-region JSON artifact (e.g., `regional_cw_fractions.json`) and cite in Table XIII caption.  

### MINOR Findings  
**P4-m1: Ambiguous "N" in dipole estimators**  
- **Section**: Table II, Sec. IV C  
- **Problem**: N_map_weighted = 5,547,858 (TTA-duplicated count) used for MASTER noise normalization but not explicitly defined in abstract/methods. Risk of confusion with N_spiral = 3,201,160.  
- **Fix**: Clarify in Sec. III A: "N_map_weighted includes test-time augmentation duplicates."  

**P4-m2: Undefined "strict-superset mask"**  
- **Section**: Abstract, Sec. III A  
- **Problem**: Critical mask term ("strict-superset mask") used for load-bearing null lacks mathematical definition.  
- **Fix**: Define in Sec. III A: "Union of all contiguous pixels with >0 galaxies, excluding isolated islands."  

**P4-m3: Duplicate phrase**  
- **Section**: Sec. VI G ("the canonical-mask canonical-mask residual")  
- **Problem**: Duplicated "canonical-mask."  
- **Fix**: Remove duplicate.  

### NIT Findings  
**P4-n1: Inconsistent rounding of uncertainties**  
- **Section**: Sec. IV B (σ = 0.000279 reported as 0.0003)  
- **Problem**: Inconsistent rounding of binomial σ (0.000279 → 0.0003) while reporting 0.4974 ± 0.0003.  
- **Fix**: Report as ±0.00028 or ±0.0003 uniformly.  

**P4-n2: Redundant statements in abstract**  
- **Section**: Abstract  
- **Problem**: "The ℓ = 1 subsample-mask null is the load-bearing scientific result" repeated verbatim in Conclusions.  
- **Fix**: Remove redundancy.  

---

## Summary recommendation  
**MAJOR REVISIONS**  

### Justification  
The paper presents a significant null result with rigorous systematics control, but requires substantial revisions to meet PRD standards:  
1. **Provenance gaps** (E1, M3) undermine reproducibility; explicit artifact links for all headline scalars are essential.  
2. **Inadequate σ-scale qualification** (E2) risks misinterpretation of diagnostics vs. headline results.  
3. **Version-history artifacts** (E3) and **length** (M1) reduce clarity; condensing to 30 pp and removing draft narratives are necessary.  
4. **Deployment-ready contributions** (equivariant TTA, catalog release) are commendable but obscured by presentation issues.  

Addressing E1-E3 and M1 is non-negotiable for acceptance. With revisions, this will be a high-impact null measurement.