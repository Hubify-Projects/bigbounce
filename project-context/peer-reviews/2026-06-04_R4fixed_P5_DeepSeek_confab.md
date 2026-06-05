# P5 2026-06-04_R4fixed — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 329.7s

---

## Referee Report for Paper P5

### ESSENTIAL Revisions

- **P5-E1: Abstract, Headline σ Values**  
  Problem: The abstract presents σ values from binomial deviations (-2.61σ filament, -4.66σ cluster) alongside a joint z-test (|z| ≈ 3.4σ for bright/dark filament split) without qualifying that these represent distinct statistical procedures (binomial σ vs. difference-in-proportions z-score). This risks conflating scales.  
  Fix: Explicitly label all σ statistics with their methodological origins (e.g., "binomial σfrom half" or "z-test σ") and add a footnote: "σ values are not directly comparable across statistical methods without calibration."

- **P5-E2: Section VI.D (Tracer-Program Stratification), σ Values**  
  Problem: The 3.4σ joint z-test for the filament bright/dark split (|z| ≈ 3.4σ) is presented adjacent to binomial σfrom half values (e.g., bright σ = -2.80) without clarifying that these σ metrics are methodologically distinct and not directly comparable.  
  Fix: Add: "Note: The |z| ≈ 3.4σ from the two-sample z-test and the binomial σfrom half = -2.80 are derived from different null hypotheses; direct numerical comparison is invalid."

### MAJOR Revisions

- **P5-M1: Abstract, Void CW Fraction (0.4836)**  
  Problem: The void CW fraction (fCW = 0.4836, n=428) is presented as a headline figure but lacks traceable provenance in the abstract. The companion JSON (`cw_fraction_by_env__desi_env_vweb.csv`) is cited only in Section VI.A.  
  Fix: In the abstract, append: "Source: pipelines/p5_desi_chirality/results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv".

- **P5-M2: Section VIII.B (DESIVAST Void n=56,981)**  
  Problem: The load-bearing scalar nDESIVAST_void = 56,981 lacks a traceable script path. The KDTree query method is described, but no driver script is cited.  
  Fix: Provide the script path: e.g., "Driver: pipelines/p5_desi_chirality/scripts/08_desivast_void_match.py".

- **P5-M3: Section VI.D (Joint z-Test |z| ≈ 3.4σ)**  
  Problem: The |z| ≈ 3.4σ statistic for the filament bright/dark split lacks provenance for the input nCW values. The fCW values are given, but exact nCW integers are omitted, preventing independent reproduction of the z-test.  
  Fix: Report exact nCW_bright and nCW_dark for the filament class in the text or companion JSON and cite the script: `pipelines/p5_desi_chirality/scripts/09_systematics.py`.

- **P5-M4: Section VIII.C (Three-Algorithm DESIVAST)**  
  Problem: The |∆fCW| < 0.002 results for VoidFinder, V2-REVOLVER, and V2-VIDE lack driver script provenance. The JSON artifact is cited, but the analysis script is not.  
  Fix: Reference the script: e.g., "Driver: pipelines/p5_desi_chirality/scripts/10_desivast_three_algorithm.py".

### MINOR Revisions

- **P5-m1: Abstract, Phase 2 Sweep Range (0.22 pp)**  
  Problem: The maximum CW fraction range (0.22 pp) cites Table VI but not the underlying CSV.  
  Fix: Add: "Source: pipelines/p5_desi_chirality/env_finder/reports/02_phase2_sweep.csv".

- **P5-m2: Section V.A (Label-Shuffle p=0.372)**  
  Problem: The redshift label-shuffle p-value (p=0.372) cites a JSON but not the script generating it.  
  Fix: Add driver path: "Driver: pipelines/p5_desi_chirality/scripts/07_analysis_redshift.py".

- **P5-m3: Section IV.B (Volume Fractions)**  
  Problem: The volume fractions {void 0.244, wall 0.413, filament 0.333, cluster 0.010} cite a JSON but not the script.  
  Fix: Reference the script: "Driver: pipelines/p5_desi_chirality/env_finder/01_compute_vweb.py".

- **P5-m4: Section VI.D (Tracer-Program fCW)**  
  Problem: The fCW values for bright/dark/backup/other lack exact nCW integers, relying on fCW ≈ nCW/n.  
  Fix: Report nCW for each tracer program in the companion JSON or a table.

### NITPICKS

- **P5-N1: Section III.B (DESI DR1 Row Counts)**  
  Problem: The parent sample size (14,622,283 galaxies) cites a script but not the SHA-256 sidecar, limiting exact reproducibility.  
  Fix: Specify the sidecar hash in the script or appendix.

- **P5-N2: Section IX.B (T-Web Volume Fractions)**  
  Problem: The T-Web volume fraction comparison cites Ref. [11] but does not explicitly state if its data are publicly archived.  
  Fix: Add: "T-Web data available at [URL] or via request to authors."

- **P5-N3: Section XIII (Limitations, RSD Bound)**  
  Problem: The scalar displacement heuristic (σv/(aH) ≲ 5–8 Mpc/h) lacks a citation for the typical pairwise velocity dispersion (σv ≲ 400 km s⁻¹).  
  Fix: Add a reference (e.g., a DESI velocity dispersion study).

---

## Summary recommendation  
**MINOR REVISIONS**  

Justification: The paper presents a rigorous, null-aligned analysis of environment-dependent chirality with extensive cross-checks and robust statistical treatment. The core conclusions are well-supported, and reproducibility is prioritized through script/JSON citations. However, traceability gaps for load-bearing scalars (e.g., nDESIVAST_void, joint z-test inputs) and unqualified σ comparisons require revision. All fixes are tractable: adding missing script paths, clarifying σ methodologies, and reporting exact nCW values. The length (21 pages) is appropriate for the scope, and the abstract accurately reflects the paper's null result. Confabulation risks are low due to strong provenance scaffolding, but consistency in statistical reporting needs tightening.