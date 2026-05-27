# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify-v3_P3_v3_1_63
**Wall time**: 125.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=66418, completion=6475, reasoning=5621, total=72893

---

## PAPER-DEE-B1: Fisher baseline \(\sigma(f_{\rm NL})=8.98\) and \(\sigma(f_{\rm NL}|_{\alpha=0.15})=8.43\) lack traceable provenance  

**Classification:** BLOCKER  
**Section:** Abstract, §5 (Cosmological Applications), §7 (Conclusions)  

**Issue:** The paper’s entire cosmological forecast chain — the linear slope \(3.66\), the Fisher‑positivity coefficient \(c=0.0747\), the central \(\sigma(f_{\rm NL})\) values, and the sensitivity table — rests on two anchor numbers: the single‑tracer DESI‑QSO baseline \(\sigma(f_{\rm NL})=8.98\) and the multi‑tracer result at \(\alpha=0.15\) (\(\sigma=8.43\)). Neither number is accompanied by a citation to an executable script, a JSON output, or a verifiable dataset that produced those exact values. The text merely states “the standard DESI~QSO constraint of \(\sigma(f_{\rm NL}) = 8.98\)” without computational provenance. Without an auditable Fisher pipeline, the reader cannot reproduce the central forecast of the paper.  

**Fix:** Provide a self‑contained reproducibility script (e.g., `pipelines/p3_anomaly_engine/fisher_baseline.py`) that computes 8.98 from the survey parameters, and deposit its output JSON together with the corresponding configuration. The script must be referenced in the abstract or §5.

---

## PAPER-DEE-B2: Genuine novelty fraction (17.8%) derived from CDS X‑Match web service, no on‑disk artifact  

**Classification:** MAJOR  
**Section:** Abstract, §3.6 (SIMBAD Cross‑Match and Novelty Assessment), §7  

**Issue:** The “genuine novelty fraction” of 17.8% (178/1 000) is a headline discovery‑rate number. It originates from a cross‑match of the DESI top‑1 000 anomalies against 20 curated all‑sky catalogs via the CDS X‑Match online service. No local, version‑controlled script or deposited data table is provided to enable reproduction of the 822‑match / 178‑novel partition. A web‑service query changes over time and cannot be guaranteed to return identical results; therefore the number is not verifiable from the paper alone.  

**Fix:** Deposit the matched‑status table (anomaly identifier, binary hit/miss per catalog) as a `.parquet` file in the data release, and include a script that can reproduce the cross‑match against a locally cached copy of the 20 catalogs. If local caching is infeasible, at minimum document the precise CDS X‑Match query parameters, the date of the query, and the returned status list.

---

## PAPER-DEE-M1: Aggregate SIMBAD‑unmatched fraction (58.8%) lacks weighting methodology and artifact  

**Classification:** MAJOR  
**Section:** Abstract, Fig. 4, §3.6, §7  

**Issue:** The abstract and conclusions quote “58.8% of anomalies with SIMBAD‑matchable coordinates lack SIMBAD counterparts, weighted across all surveys.” The paper does not specify the weighting scheme (by survey, by anomaly count, by sky area?), nor does it cite a table or script that computes the weighted aggregate. The per‑survey fractions are plotted, but the aggregate cannot be reconstructed from the displayed values alone.  

**Fix:** Provide a table of per‑survey total anomalies and SIMBAD‑match counts, and a short Python snippet (or a spreadsheet) that computes the weighted aggregate, deposited alongside the paper. Alternatively, remove the single‑number aggregate and report only per‑survey fractions.

---

**Summary:** One BLOCKER (unverifiable Fisher baseline anchors), two MAJOR (non‑reproducible novelty fraction and untraceable SIMBAD aggregate). No other load‑bearing scalars in the abstract/conclusions were found to lack a path to an on‑disk artifact.
