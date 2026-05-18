# P4_v1_0_104_R_INTERNAL R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1545pt
**Wall time**: 188.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=81747, completion=9813, reasoning=8595, total=91560

---

## Finding PAPER-DEE-B1 (BLOCKER)
**Section:** Abstract (multiple sentences) and §VII (Sensitivity Floor – injection‑recovery paragraph)  
**Issue:** The abstract states the empirical 50%‑recovery‑at‑3σ threshold is “on the N=471,049 HC‑spiral subsample” and that the 0.75% value “tracks the HC‑subsample shot‑noise budget” with a Fisher floor of ~0.76%.  The released injection‑recovery JSON (`injection_recovery_extended.json`) explicitly runs on the `p_eq>0.6` subsample (2,107,494 rows), **not** on the P>0.9 HC‑spiral subsample (N=471,049).  The abstract’s own ChatGPT‑B3 clarification note then contradicts the preceding sentence.  The body of §VII still describes the generator as loading the 471,049‑spiral sample, which is factually wrong and incompatible with the JSON.  This mis‑states the sample basis of the paper’s central sensitivity claim and invalidates the Fisher‑floor comparison as written.  
**Fix:**  
1. Correct the abstract to say the injection sweep used the `p_eq>0.6` subsample (N=2,107,494) and that the empirical 0.75% threshold corresponds to that sample (Fisher floor 0.36%).  Remove the incorrect “consistent with the N=471,049 … Fisher floor” sentence.  
2. Update §VII to match the JSON: replace “loads the 471,049‑spiral … subsample” with the actual 2,107,494‑row subset and adjust the Fisher comparison accordingly.

## Finding PAPER-DEE-M1 (MAJOR)
**Section:** Abstract (two locations) and Table III caption  
**Issue:** Two different pre‑MASTER significances are quoted for the same ℓ_eff=4 bandpower without clear reconciliation.  The abstract first says “the lowest pseudo‑Cℓ bandpower … reaches +6.48σ” (asymmetry‑map recompute, wave11c) and later says “Table III reports ℓeff=4 at +6.097σ” (NaMaster‑binned recompute, wave_14_pp).  The text does not explain that these come from different pipelines/nulls, creating an internal inconsistency for the reader.  
**Fix:** In the abstract, explicitly note that the +6.48σ is the raw anafast pseudo‑Cℓ on the asymmetry map and the +6.097σ is the NaMaster‑binned pseudo‑Cℓ from the canonical‑N recompute; choose one as the canonical pre‑MASTER reference to avoid confusion, or state the difference is due to binning/null definitions.

## Finding PAPER-DEE-M2 (MAJOR)
**Section:** §VII (Sensitivity Floor – paragraph beginning “We further verify the 0.2% minimum‑detectable‑dipole headline…”)  
**Issue:** The text claims the injection‑recovery generator “loads the 471,049‑spiral ‘HC‑spiral’ high‑confidence subsample defined by equivariant probability >0.9”.  The released artifact (`injection_recovery_extended.json`) and the paper’s own abstract clarification state the sweep used the `p_eq>0.6` subsample (2,107,494).  This is a direct contradiction inside the manuscript.  
**Fix:** Replace the quoted sentence with the correct sample description and size, referencing the JSON manifest’s `subsample` key.

## Finding PAPER-DEE-MIN1 (minor)
**Section:** Abstract (sensitivity claim)  
**Issue:** The phrase “consistent with the N=471,049 ideal‑statistical 3σ Fisher floor … i.e. the empirical 0.75% tracks the HC‑subsample shot‑noise budget” survives alongside the ChatGPT‑B3 clarification that the injection subsample is actually 2,107,494.  The clarification note states the in‑paper N=471,049 comparison is an “order‑of‑magnitude proxy”, but the preceding main text still presents a like‑for‑like match that does not exist.  
**Fix:** Remove the “consistent with …” claim and rephrase the sensitivity statement to anchor directly on the `p_eq>0.6` sample, stating the empirical/fisher ratio (~2) explicitly.

## Finding PAPER-DEE-MIN2 (minor)
**Section:** §VII (Sensitivity Floor) and Table III caption  
**Issue:** The 15‑cell LEE correction (Bonferroni) text is correctly placed under Table VIII, but the closure note promises a “max‑statistic null … queued for v1.0.105+”.  No action is required for now, but this creates a forward reference that may confuse reviewers expecting a complete analysis.  
**Fix:** Add “(deferred to v1.0.105+)” explicitly in the table footnote to match the closure intent, or remove the promise if the max‑statistic null is not planned.

## Finding PAPER-DEE-NIT1 (nit)
**Section:** Abstract (mode‑coupling‑removal chain)  
**Issue:** The sentence “the full mode‑coupling‑removal chain is (map choice + monopole‑subtraction + mask choice + MASTER), not pure MASTER on identical inputs” is clear, but the phrase “not pure MASTER on identical inputs” could be simplified to “not MASTER applied to a single fixed input” to avoid possible misinterpretation that the inputs are “identical” in some technical sense.  
**Fix:** Optional rewording for clarity.
