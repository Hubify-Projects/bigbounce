# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P4_v1_0_138
**Wall time**: 267.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=101060, completion=10110, reasoning=9333, total=111170

---

## Adversarial Provenance Audit — Paper4 v1.0.138

### Finding ID: PROV-B1
- **Classification:** BLOCKER
- **Location:** Table VII (Sky Region Balance) and its footnote, §IV.F; Abstract claim “9.5σ residual monopole … uniform across 7 equatorial coordinate slabs”.
- **Concrete issue:** The per-region CW fractions that underpin the load‑bearing uniformity argument are **not** backed by any on‑disk artifact. The footnote admits the cited artifact (`global_cw_fraction.json`) contains only the global value, and the per‑region numbers are “manuscript‑only at this version freeze”. No machine‑readable source exists to reproduce these numbers; the uniformity claim is therefore unverifiable from provided data.
- **Fix:** Generate a JSON (e.g., `sky_balance_per_region.json`) that outputs the per‑region CW/(CW+CCW) and spiral count directly from the canonical `catalog_production.parquet`, and update the footnote to reference it.

### Finding ID: PROV-M1
- **Classification:** minor
- **Location:** §VI.D, joint nuisance‑marginalized fit result; mapping statement “interpretation‑(i) reference A = 1.7% in f_CW corresponds to A_dipole = 0.034”.
- **Concrete issue:** The conversion factor 0.034 is asserted without derivation and appears inconsistent with the paper’s own relation A_p = (N_CW − N_CCW)/(N_CW+N_CCW) = 2 f_CW − 1. A full‑amplitude f_CW dipole of 1.7% should produce an A_p amplitude of 0.017, not 0.034. The arithmetic that converts the fitted A_dipole (4.55×10⁻³) to 0.23% f_CW implicitly relies on this unsourced factor; the reader cannot reproduce the mapping from displayed values alone.
- **Fix:** Provide the explicit derivation (e.g., show that the dipole basis {n_x,n_y,n_z} yields A_p = A_dipole (n̂·d̂) and that A_dipole = 0.034 corresponds to a specific convention, or correct the factor if it is an error) and cite the equation that defines the conversion.

### Finding ID: PROV-N1
- **Classification:** nit
- **Location:** Table III footnote d (power spectrum); the per‑row null means ⟨C_ℓ^null⟩ are omitted.
- **Concrete issue:** The footnote states that null means can be reverse‑engineered but are “not quoted here as a primary source”, and a dedicated column is deferred. This prevents immediate reproduction of the quoted z‑scores from the table alone, even though the data exist in the referenced JSON.
- **Fix:** Add a column for ⟨C_ℓ^null⟩ in the next revision, or provide the values in a compact footnote so that the arithmetic (z = (C_ℓ^meas − ⟨C_ℓ^null⟩)/σ_ℓ^null) is fully self‑contained.

### Additional notes
- **No other blocker‑grade provenance gaps found.** The remaining headline figures (‑0.12σ, +3.64σ, 99.3% reproduction, 0.75% injection‑recovery threshold, 21.4% argmax‑flip rate, 3.86× suppression factor, etc.) all point to identifiable JSON artifacts that are declared in the paper and should be present in the `paper4‑v1.0.134` release tag.
