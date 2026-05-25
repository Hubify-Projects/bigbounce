# P5 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P5_v0_1_30
**Wall time**: 260.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=23875, completion=9904, reasoning=9233, total=33779

---

## Finding 1 — MAJOR  
**ID:** PAPER‑DEE‑T1  
**Section:** \S VII.E (Tempel cross‑validation) and corresponding Abstract  
**Issue:** The reported filament‑class concordance of **0.026 pp** does not reproduce from the displayed table values. Table VI gives \(f_{\mathrm{CW}}^{\mathrm{Tempel}} = 0.4982\); Table II gives \(f_{\mathrm{CW}}^{\mathrm{V-Web,filament}} = 0.4980\). The difference is \(0.0002 = 0.020\) pp, not 0.026 pp. This is a load‑bearing external‑classifier validation claim. Moreover, no immutable JSON/CSV artifact is cited for the Tempel per‑class \(f_{\mathrm{CW}}\) values—only scripts are referenced—so the exact provenance is not traceable.  
**Fix:** Replace the table values with the full‑precision numbers used for the concordance calculation (e.g., \(0.49824\) vs \(0.49798\)), and deposit a static JSON/CSV artifact containing these values. Alternatively, correct the concordance to 0.020 pp and update the text and Abstract.

---

## Finding 2 — minor  
**ID:** PAPER‑DEE‑P2  
**Section:** \S VIII Phase 2 sensitivity sweep  
**Issue:** The text states *“The largest single‑cell \(|\sigma_{\mathrm{from\,half}}|\) across the entire sweep is 11.32 (filament at \(R_s\!=\!10, \lambda_{\mathrm{th}}\!=\!0\))”*. This value does not appear in the Phase‑2 table (Tab. IV) or in any figure; it is only claimed to reside in `02_phase2_sweep.csv`. A reader cannot verify the most extreme deviation of the sweep without externally parsing that file.  
**Fix:** Add a summary column or supplementary table showing per‑cell \(|\sigma|_{\max}\) or at least footnote the 11.32 value with an explicit pointer to the CSV row.

---

## Finding 3 — minor  
**ID:** PAPER‑DEE‑D3  
**Section:** Abstract vs. \S3.2 (Data)  
**Issue:** The Abstract claims *“DESI Data Release~1 redshift catalog (\(16.4 \times 10^6\) \texttt{ZWARN=0} input rows)”*. The body gives \(16{,}361{,}731\) as *“the full DR1 input”* but does not state the row count after the \texttt{ZWARN=0} restriction alone (the next stated step yields \(14{,}622{,}283\) after further spectro‑type and redshift cuts). The provenance of the 16.4M \texttt{ZWARN=0} figure is therefore ambiguous—no table or JSON artifact explicitly supports that exact number.  
**Fix:** Cite the precise \(N\) after \texttt{ZWARN=0} in a data‑summary artifact (e.g., in `p5_matched_chirality_desi_summary.json`) and align the Abstract’s rounding to it.
