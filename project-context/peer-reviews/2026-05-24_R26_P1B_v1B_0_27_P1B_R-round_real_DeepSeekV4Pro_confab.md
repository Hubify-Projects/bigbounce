# P1B R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-24_R26_P1B_v1B_0_27
**Wall time**: 149.5s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=22072, completion=6725, reasoning=6034, total=28797

---

## PAPER-DEE-B1 (BLOCKER) — ALP field-displacement range has no traceable provenance
**Section:** §VI (Cosmic Birefringence: Spectator ALP Consistency Check), lines ~700–720.  
**Issue:** The load-bearing scalars `Δφ/f_a ≈ 0.65` (fiducial) and `Δφ/f_a ∈ [0.2, 1.1]` (natural range) are stated as results of numerical integration of the ALP equation of motion, but **no script, notebook, or precomputed dataset is cited** that produces these numbers. The reproducibility appendix (§A) lists no ALP EOM integration code. The entire spectator-ALP consistency argument (β range, required C_{aγ} span) collapses without these numbers.  
**Fix:** Provide the integration script (e.g., `alp_eom_integration.py`) in the reproducibility repository and cite it explicitly in §VI, or include a table of precomputed `Δφ/f_a` values with a direct link to the generating artifact.

## PAPER-DEE-M1 (MAJOR) — CMB-S4 σ(N_eff) forecast lacks a citation
**Section:** Abstract (line ~50) and Conclusions (§VIII).  
**Issue:** The scalar `σ(N_eff) ∼ 0.03` is presented as a future precision test, but **no reference is given** for this sensitivity figure. While it is a common forecast, a traceable source (e.g., CMB-S4 Science Book, arXiv:1610.02743) is required for a verification companion that otherwise demands explicit provenance.  
**Fix:** Add a citation to the CMB-S4 forecast document at both occurrences.

## PAPER-DEE-M2 (minor) — Table I posterior means not linked to a specific on-disk JSON
**Section:** Table I (Stock-CAMB ΛCDM+ΔN_eff results).  
**Issue:** The headline numbers `ΔN_eff = -0.020 ± 0.169`, `H_0 = 67.68 ± 1.06`, etc., are not accompanied by a pointer to the exact JSON file (e.g., `full_tension_physical_parameters.json`) from which they were extracted. The version-history preamble mentions such a file, but the table caption and body text do not connect the reader to it.  
**Fix:** Add a footnote to Table I: “Posterior means sourced from `reproducibility/cosmology/frozen/full_tension_physical_parameters.json`; see repository.”

## PAPER-DEE-N1 (nit) — Abstract “500 Monte Carlo realizations” lacks seed/reproducibility handle
**Section:** Abstract (line ~40).  
**Issue:** The phrase “500 Monte Carlo realizations” is a procedural scalar, but the abstract does not mention the random seed or the driver script that guarantees exact reproducibility. The body later references a driver script path, but the abstract is the first point of contact for a paranoid reader.  
**Fix:** Append “(driver script and seeds in `pipelines/h200_results/pod1_namaster_umap_2026-04-29/`)” to the abstract sentence.
