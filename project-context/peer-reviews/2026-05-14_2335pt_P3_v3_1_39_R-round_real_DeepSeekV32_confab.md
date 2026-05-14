# P3_v3_1_39 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_2335pt
**Wall time**: 45.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=54408, completion=1360, total=55768

---

## PAPER-DEE-B1
**BLOCKER** – Abstract & Table 1: Headline count 378,280 is not traceable from displayed values.  
**Line/Context**: Abstract states 378,280 = 378,080 point-source + 200 Planck. Table 1 footnote says 388,493 survey-level detections → 378,280 after dedup (10,213 duplicates). However, 388,493 - 10,213 = 378,280, but the sum of per-survey native counts in the footnote (DESI 195,829 + SDSS 77,905 + LAMOST 113,342 + eROSITA 298 + Planck 200 + Gaia 500 + NEOWISE 419) = 388,493. This sum includes LAMOST's 113,342, which the text labels "exploratory tier" and says the "catalog-grade tier" is ~265,000. The arithmetic that produces the final 378,280 from a mix of catalog-grade and exploratory tiers is not shown; the partition is not defined in a reproducible way.  
**Fix**: Provide a single clear arithmetic chain from per-survey native counts to the final 378,280, explicitly listing which surveys contribute to the "catalog-grade" vs. "exploratory" subtotals and how the 10,213 duplicates are distributed across them. The released parquet must contain a column flagging catalog-grade vs. exploratory membership.

## PAPER-DEE-M1
**MAJOR** – Section 4.1 & Abstract: Genuine novelty fraction 17.8% is a single-sample point estimate from DESI top-1,000, but abstract and conclusions present it as a headline metric without the crucial caveat that it is not a full-catalog rate.  
**Line/Context**: Abstract says "genuine novelty fraction of ~17.8% (objects absent from all major catalogs)" and calls it a "single-sample point estimate". Conclusions repeat the 17.8% figure without reiterating the limited scope. This invites misinterpretation as a global catalog property.  
**Fix**: In abstract and conclusions, explicitly state "17.8% measured on the DESI top-1,000 anomalies only; full-catalog rate untested". Add a warning that this is neither an upper nor lower bound for the full catalog.

## PAPER-DEE-M2
**MAJOR** – Section 3.2 (SDSS) and Table 1: SDSS native retrain results are inconsistently reported, making the 77,905 figure load-bearing without clear provenance.  
**Line/Context**: Table 1 lists SDSS cross-transfer N_anom = 77,905, but text says native retrain yields only 12 sources at S>5, a ~6500× reduction. The 77,905 is retained as a "top-1% continuity slice" but the threshold for this slice (S ≥ 0.1060) is defined only in the text, not in the table. The released parquet `sdss_dr18_pathc_native.parquet` presumably contains the 77,905, but it's unclear if this is the native or cross-transfer set.  
**Fix**: In Table 1, replace the cross-transfer 77,905 with the native retrain's 12 (S>5) and add a separate row or footnote for the native top-1% slice (19,253 at S ≥ 0.2051). Clarify in the data release which parquet corresponds to which threshold.

## PAPER-DEE-M3
**MAJOR** – Section 5 (Cosmological Applications): The empirical α = 0.19 ± 0.65 is derived from a sample of 5,384 QSO candidates, but the text notes only 12 are spectroscopically confirmed at high-z; the rest are photometric candidates. The α measurement thus averages over a heterogeneous redshift distribution, not the high-z regime relevant for the f_NL forecast.  
**Line/Context**: Section 5 states: "The 5,384-candidate sample contains only 12 spectroscopically confirmed z≈6 candidates ... the angular two-point measurement averages over this heterogeneous redshift distribution." This invalidates the direct insertion of α into the high-z multi-tracer Fisher forecast.  
**Fix**: Either restrict the α measurement to the confirmed high-z subset (with appropriate error bars) or clearly state that the forecast using the full-sample α is not representative of the high-z tracer population. Move the heterogeneous redshift warning to the same paragraph where α is inserted into the Fisher pipeline.

## PAPER-DEE-m4
**minor** – Section 3.1 (DESI): The 0.87% anomaly rate (195,829 / 22,504,897) is presented as an emergent property, but the threshold is an absolute S > 5 cut anchored to validation MSE. The validation MSE (μ_val ≈ 0.0287) and the conversion to MSE ≈ 0.143 for S=5 are given, but the σ_val used in the z-scoring is not provided, preventing independent reproduction of the 0.87% rate.  
**Line/Context**: Equation 2 and surrounding text define S = (MSE - μ_val)/σ_val, but σ_val is not stated for DESI.  
**Fix**: Report σ_val for each survey in a table or footnote, or provide the script that computes the S > 5 threshold from the validation set.

## PAPER-DEE-m5
**minor** – Bibliography: Several citations have incomplete or inconsistent arXiv IDs. For example, Cai:2009fn points to arXiv:0808.0810, not the published version; WilsonEwing2012 points to arXiv:1211.6269, but the year in the label is 2012. This matches the fused-metadata pattern mentioned in the review context.  
**Line/Context**: Bib entries for Cai:2009fn, WilsonEwing2012, and others.  
**Fix**: Verify each arXiv ID against ADS, ensure the year in the label matches the arXiv submission year, and provide the canonical journal reference if available.

**Summary**: No new BLOCKERs beyond the arithmetic opacity of the 378,280 headline count. The major issues involve inconsistent reporting of SDSS results, overinterpretation of the novelty fraction, and a mismatch between the α measurement sample and the cosmological forecast regime.
