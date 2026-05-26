# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v3_P3_v3_1_62
**Wall time**: 164.5s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=65509, completion=7876, reasoning=6535, total=73385

---

# Adversarial Peer Review — Provenance Audit

Findings focus on load-bearing scalars in abstract and conclusions with unclear or missing on-disk artifacts.

## Finding 1 — PAPER-DEE-B1 (BLOCKER)
**Section(s):** §5 (Cosmological Applications), Abstract, Conclusions; especially the Fisher forecast anchor values `σ(fNL)=8.98` (single‑tracer DESI QSO baseline) and `σ(fNL)=8.43` at `α=0.15`.  
**Issue:** The `f_NL` Fisher‑forecast pipeline is entirely built on two anchor numbers — `σ(f_NL)=8.98` (standard DESI QSO constraint) and `σ(f_NL)=8.43` (multi‑tracer at prior fiducial `α=0.15`). No script, configuration file, or output artifact is cited that reproduces either of these numbers from survey specifications, and no standalone Fisher‑matrix run is described that a reviewer could re‑execute. Without a reproducible source for the baseline sensitivity, every derived `σ(f_NL)` value (8.14, 8.27, 3.92, the entire envelope, and all improvement percentages) is an assertion, not a reproducible computation.  
**Fix:** Provide a minimal script (e.g., `pipelines/p3_anomaly_engine/fisher_anchors.py`) that, given DESI QSO forecast parameters and the Heinrich‑2023 prescription, outputs `σ(f_NL)=8.98` and the multi‑tracer anchor at `α=0.15`, or cite a published DESI baseline document with the exact value. Store the script and its output artifact alongside the paper.

## Finding 2 — PAPER-DEE-M1 (MAJOR)
**Section(s):** §4.1 (SIMBAD cross‑match), Conclusions item 2, Abstract.  
**Issue:** The aggregate SIMBAD‑unmatched fraction of **58.8 %** is presented as a headline metric. It cannot be reproduced from the per‑survey data in the paper: the DESI full‑catalog unmatched fraction is only reported for the top‑10 000 (≈99 %), not for the complete 195 829‑anomaly sample, and the weighting scheme (number of objects with SIMBAD‑matchable coordinates per survey) is not disclosed. Without a per‑survey match table or a script that computes the aggregate, the 58.8 % figure is unverifiable.  
**Fix:** Either (i) provide a CSV/JSON artifact listing SIMBAD match status for every anomaly in the cross‑transfer baseline, together with a script that reproduces the aggregate fraction, or (ii) limit the claim to a “sum‑of‑top‑N” number that is directly calculable from the data already in the paper, e.g., “the 319 443 cross‑transfer anomalies have a combined SIMBAD‑unmatched fraction of XX % using the per‑survey numbers where full matching was performed.”

## Finding 3 — PAPER-DEE-M2 (MAJOR)
**Section(s):** §4.1 (“Archival cross‑match and genuine novelty fraction”), Abstract, Conclusions item 2.  
**Issue:** The primary catalog novelty figure — **17.8 %** (178/1 000) for the DESI DR1 top‑1 000 anomalies cross‑matched against 20 curated all‑sky catalogs via CDS X‑Match — is stated without a companion artifact that contains the 822‑matched‑vs‑178‑unmatched list. No file name (e.g., `desi_top1000_cds_xmatch.json`) is given, and the text says the full characterization is “detailed in the companion data release,” which does not exist at the point of review. The number therefore lacks a traceable source.  
**Fix:** Deposit the CDS X‑Match output for the top‑1 000 DESI anomalies (matching object IDs and the 822‑matched tally) as a supplementary table or JSON file and reference it explicitly, e.g., `data/desi_top1000_novelty.json`. Until that artifact is public, the 17.8 % figure should either be removed or labelled as an unverifiable pre‑computation.

## Finding 4 — PAPER-DEE-m1 (minor)
**Section:** §7 Conclusions, item 5 (cosmological applications).  
**Issue:** The conclusions quote the multi‑tracer Fisher forecast as `σ(f_NL) = 8.27 ± 2.37` (the local‑linear approximation), while the abstract and caveat (i) of §6.4 establish the canonical positivity‑respecting forecast as `σ(f_NL) = 8.14` with envelope `[3.92, 8.98]`. The two numbers appear interchangeably, creating an internal contradiction about which `σ(f_NL)` is the paper’s headline.  
**Fix:** In the conclusions, replace the local‑linear `8.27 ± 2.37` with the positivity‑respecting `8.14` (or explicitly state that the 8.27 is the linear‑approximation reference and not the canonical forecast). Consistency with the abstract is required.

## Finding 5 — PAPER-DEE-m2 (minor)
**Section:** Abstract (first line); Table I (survey_summary).  
**Issue:** The abstract states “37.3 million sources and CMB map patches,” but the survey_summary table’s Path‑C row lists the total number of processed sources as **37 272 042**. The discrepancy of ~28 000 is small but the number is a headline claimed scale. No indication is given whether “37.3 million” is a rounded value or includes some additional sources not counted in the table.  
**Fix:** Either replace “37.3 million” with the exact table figure (37 272 042) or mark it as “∼37.3 million” and add a footnote pointing to the precise total, clarifying any inclusion (e.g., ACT DR6 patches, training pools) that accounts for the difference.
