# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify-v2_P3_v3_1_63
**Wall time**: 112.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=66391, completion=6627, reasoning=5639, total=73018

---

# Adversarial Peer Review — P3 v3.1.63 (provenance of load-bearing scalars)

## PAPER-DEE-B1 (BLOCKER) — Unverifiable baseline σ(f_NL)
**Locations:** Abstract (σ=8.98, σ=8.14, σ=8.27), §5, Conclusions.  
**Issue:** The forecast improvement percentages hinge on the “standard DESI‑QSO σ(f_NL)=8.98” and the multi‑tracer σ=8.43 at α=0.15. No script or output JSON/artifact is cited that produces these numbers. The paper mentions two Fisher‑pipeline runs but provides no file path that would let a reader recompute 8.98 or 8.43. The `f_0=1/8.98²` and `c=0.0747` therefore float without verifiable provenance.  
**Fix:** Either (a) deposit the specific Fisher run outputs that yield 8.98 and 8.43 as companion JSON artefacts and reference them explicitly, or (b) regenerate the baseline with the released `fisher_with_systematics.py` and add the output digest to the reproducibility bundle.

## PAPER-DEE-B2 (BLOCKER) — Phantom “98% blue‑excess” claim for *native* LAMOST
**Location:** Abstract (“the native LAMOST autoencoder retains a ~98% blue‑excess instrumental contamination signature in the released anomaly scores”).  
**Issue:** The body (§3.3, §6.1) documents a 21.5× anomaly‑rate reduction after native retraining and does **not** report a 98% blue‑excess fraction on the native top‑1% slice. The 98% figure applies only to the **cross‑transfer** baseline. The abstract statement is quantitatively false for the released native catalogue and is unsupported by any on‑disk measurement.  
**Fix:** Replace with the actual residual signature (if measured) or state the native catalogue’s spectral‑morphology breakdown explicitly. If the claim is a drafting error, delete it.

## PAPER-DEE-M1 (MAJOR) — Genuine novelty fraction 17.8% has no traceable output
**Locations:** Abstract (“genuine novelty fraction of ∼17.8%”), §4.1, Conclusions.  
**Issue:** The 17.8% rate is obtained by cross‑matching the DESI top‑1 000 against 20 catalogues via CDS X‑Match. No script, log, or result file is referenced in the paper; the data‑availability section defers the “deeper NED+VizieR sweep” to a companion release. A headline discovery‑rate number without a companion artefact is unreproducible from the submitted manuscript alone.  
**Fix:** Add the exact cross‑match script (or CDS X‑Match query log) and the output table (e.g. `desi_top1000_cds_xmatch.parquet`) to the release bundle, and cite the artefact in §4.1.

## PAPER-DEE-M2 (MAJOR) — Fisher sensitivity table lacks on‑disk artefact
**Locations:** Table III (Sensitivity to α), Appendix “Sensitivity”, Conclusions (legacy fixed‑α forecast).  
**Issue:** The σ(f_NL) values for α∈{0.05,…,0.50} are described as “linear scaling from the fiducial 7‑bin Fisher result at α=0.15”. The underlying 7‑bin Fisher output that yields σ=8.43 is already unverifiable (see BLOCKER B1), so the entire table is untraceable.  
**Fix:** Once the baseline Fisher run is made verifiable, deposit the per‑α output (or the scaling script) as `alpha_sensitivity_table.json`.

## PAPER-DEE-MI1 (minor) — Cross‑transfer baseline 319,443 includes quarantined ACT
**Location:** Abstract (“initial cross‑transfer baseline identified 319,443 anomaly detections”).  
**Issue:** The 319,443 total (Table I) includes ACT’s 200 patches, while the Path‑C headline explicitly excludes ACT. The abstract juxtaposes 319,443 and 388,493 as if they are directly comparable step‑changes, but one includes a now‑quarantined survey.  
**Fix:** Add a parenthetical “(ACT‑inclusive)” or note that the 319,443 figure is the pre‑quarantine baseline, not a direct predecessor of the 388,493 sum.
