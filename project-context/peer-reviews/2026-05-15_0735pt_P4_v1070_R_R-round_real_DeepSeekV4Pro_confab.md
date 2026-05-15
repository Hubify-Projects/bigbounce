# P4_v1070_R R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0735pt
**Wall time**: 147.1s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=60252, completion=6197, reasoning=4987, total=66449

---

## Adversarial Peer Review — DeepSeek-V4-Pro (reasoning, high)

This audit follows the instruction to be paranoid about load‑bearing scalars whose provenance cannot be traced to an on‑disk JSON/script/dataset.  The paper is extremely thorough in providing companion artifacts, but two issues affect how headline sensitivity numbers are communicated.

---

### PAPER‑DEE‑B1 (MAJOR) – Empirical injection‑recovery floor is derived on a high‑confidence subsample, not the full catalog; abstract & conclusions obscure this

**Location:** Abstract (lines 66‑75) and Sec. VII.D (sensitivity floor)  
**Issue:** The abstract states *“the systematic‑inclusive empirical injection‑recovery sensitivity floor is |A_dipole| > 0.5%”* and presents this as the primary publication‑grade sensitivity.  However, the injection‑recovery sweep (Table 6) was performed on the *HC‑spiral subsample* (N=471 049), a strict high‑confidence cut, not on the full canonical spiral sample (N=3 201 160).  The abstract does not mention this subsample, leaving the impression that the full catalog’s empirical floor is ≥0.5%.  In reality, the full catalog would have better sensitivity; the >0.5% bound is conservative only for the smaller, cleaner subset.  The mismatch between the sample used for the empirical floor and the sample that carries the headline null dipole must be disclosed in the abstract and conclusions.  
**Fix:** Add an explicit qualifier (e.g., “on the 471 k HC‑spiral confidence cut”) in the abstract and wherever the empirical floor is cited as the primary sensitivity figure.  If the full‑catalog empirical floor is desired, repeat the injection on the 3.2M spiral pool.

---

### PAPER‑DEE‑M1 (minor) – Duplicate bibliographic entry for Walmsley et al. 2023

**Location:** Bibliography, items `Walmsley:2023` and `Walmsley:2023GZDESI`  
**Issue:** The same paper (Galaxy Zoo DESI: detailed morphology measurements…) appears twice with different cite keys.  The text uses both keys, apparently to distinguish a generic reference from the GZ DESI featured‑galaxy fraction comparison.  This duplication is confusing and could mislead readers about the number of independent sources.  
**Fix:** Merge into a single bib entry and use the same key throughout.  If a separate label for the GZ DESI specific use is necessary, give it a distinct short identifier (e.g., `Walmsley:GZDESI2023`) while still referencing the same published work.

---

### PAPER‑DEE‑M2 (minor) – Abstract describes dipole estimators as “full‑sky” despite partial coverage

**Location:** Abstract (lines 40–43)  
**Issue:** The abstract calls the real‑space dipole and the subsample‑mask MASTER result “full‑sky estimators” even though DESI Legacy covers f_sky ≈ 0.46–0.66.  The phrase “full‑sky” is technically incorrect and may be read as claiming all‑sky coverage, which is not the case.  
**Fix:** Replace “full‑sky” with a more precise term such as “larger‑coverage” or “contiguous‑mask” to accurately describe the masks used.

---

### PAPER‑DEE‑M3 (minor) – Hemisphere LEE rejection abstracted without noting the conservative correction’s null result

**Location:** Abstract (lines 48–53) and Sec. VII.B  
**Issue:** The abstract reports *“A 3.05σ local hemisphere asymmetry rejects the random‑label null at p_LEE ≤ 10⁻⁴”* but omits that a conservative Bonferroni/Benjamini‑Hochberg look‑elsewhere correction reduces the significance to <1σ, consistent with null.  The paper later discusses both methods, but the abstract’s selective mention of the more dramatic rejection could mislead a reader who does not reach the detailed discussion.  
**Fix:** Add a brief note in the abstract (e.g., “under a conservative multiplicity correction the significance is <1σ”) or re‑phrase to indicate that the rejection depends on the null‑construction and does not survive all look‑elsewhere treatments.

---

### PAPER‑DEE‑N1 (nit) – Fisher‑floor derivation uses NSIDE=8 while injection‑recovery uses NSIDE=64

**Location:** Sec. VII.C lines (around Eq. 11) vs. injection‑recovery Table  
**Issue:** The analytic Fisher asymptote assumes an NSIDE=8 pixelization (768 pixels), whereas the empirical injection‑recovery is performed at NSIDE=64.  While both resolutions are adequate for a dipole search, the differing pixel counts affect the exact numerical factors in the Fisher calculation.  The paper acknowledges that the Fisher value is an asymptote, but a reader comparing the two numbers directly might be confused.  
**Fix:** Add a sentence clarifying that the Fisher floor is a low‑resolution idealisation and that the injection‑recovery at NSIDE=64 gives the actual per‑pixel variance used in the empirical threshold; the two are not intended to be identical.

---

**Verdict on publishability:** The paper is essentially ready for arXiv after addressing the MAJOR finding (clarify the sample used for the empirical floor) and the minor bibliographic and wording issues.  No load‑bearing math error was found that would alter the central null‑dipole conclusion.
