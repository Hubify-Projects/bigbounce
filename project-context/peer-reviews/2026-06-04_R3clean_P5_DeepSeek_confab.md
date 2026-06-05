# P5 2026-06-04_R3clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 129.2s

---

## Referee Report: Confabulation-Hunter Findings

### ESSENTIAL Findings

**P5-E1: Inconsistent σ calculation for filament class**  
- **Section**: VI.A (Headline cosmic-web environment) and Abstract  
- **Problem**: Reported σ_from_half = -2.61 for filament class (n=408,187, f_CW=0.4980) is inconsistent with the paper's defined formula σ_from_half ≡ (n_CW - 0.5N)/(0.5√N). Calculation yields -5.74σ, not -2.61σ. This error propagates to the abstract's narrative about "tracking the catalog-monopole offset."  
- **Fix**: Recompute all σ_from_half values using the stated formula and correct all tables/text. Provide explicit derivation for the -2.61σ value if it relies on an unstated adjustment.  

**P5-E2: Misrepresented σ scales without qualification**  
- **Section**: Abstract, VI.A (Table II), VII  
- **Problem**: σ values from binomial deviations (σ_from_half), label-shuffle nulls, and residual σ_vs_monopole are presented interchangeably without clarifying they are on different statistical scales (e.g., abstract juxtaposes -2.61σ, -4.66σ, and p-values). This risks conflating binomial noise with permutation-based significance.  
- **Fix**: Qualify all σ values by type (e.g., "binomial σ_from_half" vs. "label-shuffle σ_max") in abstract, tables, and captions. Add a glossary of σ notations.  

---

### MAJOR Findings

**P5-M1: Untraceable headline scalars in abstract/conclusions**  
- **Section**: Abstract, Conclusions  
- **Problem**: Critical numbers lack explicit provenance:  
  - "791,635 chirality-relevant spirals" (no script/dataset link)  
  - DESIVAST void sample "56,981" (no script for point-in-sphere matching)  
  - Phase 2 sweep "max range 0.22 pp" (no JSON/script anchor)  
- **Fix**: Cite specific scripts (e.g., `pipelines/p5_desi_chirality/scripts/03_crossmatch.py` for matching; `env_finder/02_phase2_sensitivity_sweep.py` for sweep) and provide SHA-256 hashes for datasets.  

**P5-M2: Primary result obscured in abstract**  
- **Section**: Abstract  
- **Problem**: Abstract emphasizes V-Web fractions (n_void=428, statistically weak) but buries the primary DESIVAST-anchored result (n_void=56,981, Δf_CW=0.0007) in narrative text. This misrepresents the strongest evidence.  
- **Fix**: Restructure abstract to lead with DESIVAST void result and demote V-Web void to a cross-check. Explicitly state: "Primary constraint: |Δf_CW| < 0.002 across 56,981 DESIVAST voids."  

**P5-M3: Unvalidated DESIVAST void sample**  
- **Section**: VIII.B (DESIVAST-anchored void classifier)  
- **Problem**: The derivation of n_DESIVAST_void = 56,981 relies on a point-in-sphere test against 101,863 holes, but:  
  - No script/procedure is provided for the KDTree query.  
  - The 0/6 V-Web void concordance (n=6) is too small to generalize.  
- **Fix**: Publish the matching script; validate with separation histograms or confusion matrices. Clarify that 0/6 is illustrative, not statistically significant.  

**P5-M4: Arithmetic inconsistencies in residual analysis**  
- **Section**: VI.D (Within-class density-stratified cluster)  
- **Problem**: Reported cluster Q3 σ = -0.37 (Table IV) contradicts the paper's formula. With n=99,526, f_CW=0.4950 → σ_from_half = -3.94, not -0.37.  
- **Fix**: Recompute all within-class σ values; explain discrepancies (e.g., if residuals subtract σ_pred).  

---

### MINOR Findings

**P5-m1: Version-history artifacts**  
- **Section**: II (Relation to Paper IV)  
- **Problem**: Internal tags like "Paper IV (P4)" and "this work (P5)" appear without definition.  
- **Fix**: Define "P4"/"P5" at first use: "Paper IV (P4; Golden et al. in prep.)".  

**P5-m2: Paper length disproportionate to contribution**  
- **Section**: Entire paper  
- **Problem**: At 21 pages, the paper exhaustively reports 12+ null tests/classifiers, but the core result (DESIVAST void null) is established in 5 pages. The V-Web/Tempel/ASTRA cross-checks do not add independent evidence.  
- **Fix**: Condense to 15 pages by:  
  - Moving Phase 2 sweep details to an appendix.  
  - Cutting redundant cross-checks (e.g., §IX.B T-Web).  

---

### NIT Findings

**P5-n1: Duplicate phrasing**  
- **Section**: VI.E (Sky-position regional coherence)  
- **Problem**: "per-pixel per-pixel" (HEALPix description).  
- **Fix**: Replace with "per HEALPix pixel".  

**P5-n2: Unclear "decomposition" reference**  
- **Section**: Not found  
- **Problem**: The report instruction mentions "decomposition 99.3%/12%/88%/25%", but this is absent in the paper.  
- **Fix**: Remove the instruction or clarify intent.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper reports a significant null result (no environment-dependent chirality) anchored on a robust DESIVAST void sample (n=56,981), but it is undermined by critical errors:  
1. **ESSENTIAL**: Inconsistent σ calculations (e.g., filament class) invalidate the primary V-Web narrative.  
2. **MAJOR**: Untraceable scalars and obscured primary result risk confabulation.  
3. **Structural issues**: Overemphasis on weak V-Web voids and redundant cross-checks bloats the paper.  

Revise by:  
- Correcting all statistical derivations (P5-E1, P5-M4).  
- Explicitly anchoring abstract/conclusions to DESIVAST (P5-M2).  
- Publishing provenance for all load-bearing scalars (P5-M1, P5-M3).  
- Condensing to 15 pages by focusing on DESIVAST + robustness (P5-m2).  

With these fixes, the paper will meet PRD's standards for reproducibility and clarity.