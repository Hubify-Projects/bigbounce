# P4_v1060 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_2100pt
**Wall time**: 20.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=54954, completion=1465, total=56419

---

# Adversarial Peer Review: Confabulation-Hunter Findings

**ROUND CONTEXT:** P4 v1.0.60 10th real cross-vendor verification. Target: confirm GPT-5.5 converges with other 4 vendors on clean state.

**MY FOCUS:** Paranoid about numbers without traceable sources. Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

**VERDICT:** No BLOCKER findings. 4 MAJOR findings, 1 minor, 1 nit.

## PAPER-DEE-M1: Abstract Fisher-floor arithmetic mismatch
**Location:** Abstract, lines ~55-65  
**Issue:** The abstract states: "Fisher-floor statistical Poisson asymptote is $|A_{\rm dipole}|\!\lesssim\!0.29\%$ at $3\sigmaunit$ under the convention $p_{\rm CW}(\hat n) = \tfrac12(1+A\cos\theta)$ (corresponding to a CW-fraction half-modulation uncertainty $\sigma\approx\!0.048\%$, with the factor of 2 absorbed into the amplitude definition)". The arithmetic doesn't track: $3 \times 0.048\% = 0.144\%$, not $0.29\%$. The factor of 2 is mentioned but the jump from $0.144\%$ to $0.29\%$ isn't explicitly shown.  
**Fix:** Add one line showing: $3 \times 0.048\% \times 2 = 0.288\% \approx 0.29\%$ to make the factor-of-2 propagation transparent. Or state directly: "The half-modulation $\sigma=0.048\%$ gives full-amplitude floor $3 \times 0.048\% \times 2 = 0.288\% \approx 0.29\%$."

## PAPER-DEE-M2: Table III $\ell_{\rm eff}=4$ significance unexplained
**Location:** Table III (multipole table), row for $\ell_{\rm eff}=4$  
**Issue:** The table shows $C_\ell = 3.210\times10^{-6}$, $\sigma_{\rm null}=0.804\times10^{-6}$, significance $+6.097\sigma$. This is a load-bearing number showing mask-coupled monopole leakage. However, no script/JSON is cited that produces these exact values (3.210, 0.804, 6.097). The companion artifact `wave_14_pp_namaster_verification.json` is cited for the bandpower table, but does it contain these exact floats?  
**Fix:** Explicitly state in table caption or footnote: "The values in this row are extracted from `r42_results/wave_14_pp_namaster_verification.json`, field `bandpower_4` with exact floats as shown." Add a verification note that the arithmetic $(3.210-0)/0.804 = 3.992$ not 6.097—so the significance likely uses a different null mean, which should be disclosed.

## PAPER-DEE-M3: Hemisphere max-statistic amplitude conversion
**Location:** Abstract lines ~85-90 and Sec. 5.2 (hemisphere)  
**Issue:** Abstract states: "equivalent full dipole-amplitude $\max|A| = 8.531\times 10^{-3} = 0.853\%$ where $p_{\rm CW}(\hat n) = \tfrac12 (1 + A\cos\theta)$". This conversion from CW-fraction half-difference 0.17% to full amplitude 0.853% is a factor of ~5, not the expected factor of 2. No derivation is given.  
**Fix:** Provide the conversion formula: hemisphere half-difference $\delta = (f_{\rm CW,N} - f_{\rm CW,S})/2$ relates to dipole amplitude $A$ via $A = 2\delta / \langle \cos\theta \rangle_{\rm hemisphere}$ where the average cosine factor accounts for geometry. Or cite the script that computes this 0.853% number.

## PAPER-DEE-M4: Bin flatness failure without error bars
**Location:** Sec. 6.3 (bin flatness), lines ~1520-1530  
**Issue:** Reports fracdev $\Delta=1.41\%$ fails $0.1\%$ bar, but no Poisson error bars are given for the bins. The high-fracdev bin has n=10,941 galaxies, so binomial error ~0.48%. The 1.41% spread could be dominated by this single bin's statistical fluctuation.  
**Fix:** Add per-bin Poisson errors to the statement or to Fig. 10 caption. State explicitly: "The 1.41% spread is driven by the smallest bin (n=10,941) with Poisson error ~0.48%, making the deviation ~3σ within that bin's own statistics."

## PAPER-DEE-M5 (minor): Catalog spiral count provenance
**Location:** Multiple sections referencing $N_{\rm spiral}=3,201,160$  
**Issue:** While a verification script `verify_canonical_numbers.py` is cited, the exact path to the source Parquet file that yields this count isn't given. The catalog is at HuggingFace, but which column/filter produces 3,201,160?  
**Fix:** Add one line: "The count is obtained from `catalog_production.parquet` column `class_eq` filtering for values in `{'CW','CCW'}` using `pandas` query, as implemented in `scripts/verify_canonical_numbers.py`."

## PAPER-DEE-N1 (nit): Abstract "0.5%" inequality direction
**Location:** Abstract lines ~50-55  
**Issue:** States: "The conservative, systematic-inclusive empirical injection-recovery sensitivity floor is $|A_{\rm dipole}|\!>\!0.5\%$ (at $A\!=\!0.5\%$ the per-pixel-shuffle MC gives $P(\sigma\!>\!2)\!=\!0.18$; explicit 50%-recovery at $3\sigmaunit$ is not demonstrated... hence the strict inequality)". The strict inequality $>0.5\%$ suggests the floor is above 0.5%, but the text implies 0.5% is the highest tested amplitude, so floor $\geq 0.5\%$ is more accurate.  
**Fix:** Change to $|A_{\rm dipole}|\!\geq\!0.5\%$ or rephrase: "floor lies above 0.5% (since 50%-recovery not reached at highest tested amplitude 0.5%)".

---
**Overall:** No BLOCKERs found. The paper has extensive provenance tracking (JSON artifacts, scripts, manifests). The MAJOR items are mostly clarity/derivation gaps rather than missing provenance. GPT-5.5 should converge with other vendors on clean state.
