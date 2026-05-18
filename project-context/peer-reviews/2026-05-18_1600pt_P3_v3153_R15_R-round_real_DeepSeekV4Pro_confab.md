# P3_v3153_R15 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1600pt
**Wall time**: 516.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=62750, completion=16052, reasoning=14926, total=78802

---

# Adversarial Peer Review — R15 Verification

Findings are classified **BLOCKER** / MAJOR / minor / nit. Focus: NEW load‑bearing math errors only.

---

## PAPER‑DEE‑B1 — BLOCKER (regression)  
**Section:** §7 (Conclusions), item 4 (Cosmological applications)  
**Issue:** The conclusions still quote the unphysical local‑linear forecast `σ(fNL) = 8.27 ± 2.37` as the sole multi‑tracer Fisher result, without any mention of the Fisher‑positivity‑respecting central value `σ = 8.14` or its envelope `[3.92, 8.98]`. This directly contradicts the R14 GEM‑B1 closure, which replaced the unphysical phrasing in the body; the conclusions were not updated.  
**Fix:** Replace the entire sentence in §7 item 4 with the positivity‑respecting primary result: *“Inserting the empirical α into the Fisher‑positivity‑respecting form gives a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98]; the local‑linear approximation 8.27 ± 2.37 is retained only for reference.”*

---

## PAPER‑DEE‑M1 — MAJOR (conflicting central‑value designation)  
**Section:** Abstract, penultimate paragraph  
**Issue:** The abstract first states *“Inserting the empirical central value … yields a central forecast σ(fNL) = 8.14”*, then later says *“the σ(fNL) = 8.27 figure should be read as a central‑value forecast”*. The two statements appoint different numbers as the central forecast, leaving readers unsure which is the paper’s primary cosmological deliverable.  
**Fix:** Reword the final sentence to *“the σ(fNL) = 8.27 local‑linear reference value should be read as a legacy comparison, not the canonical forecast”* and explicitly designate the posit‑res‑ form as the primary.

---

## PAPER‑DEE‑M2 — minor (unreproducible linear central)  
**Section:** Abstract and §5 (Cosmological Applications)  
**Issue:** The local‑linear central is reported as `σ = 8.27`. With α_jk = 0.19 and the stated slope 3.66, `σ = 8.98 − 3.66·0.19 = 8.2846`, which rounds to 8.28, not 8.27. The discrepancy (0.01) is not explained by any stated precision.  
**Fix:** Either correct the value to 8.28 or explicitly note the rounding convention that yields 8.27 (e.g., using a slightly different α central value).

---

## PAPER‑DEE‑M3 — minor (inconsistent Fisher coefficient)  
**Section:** Abstract, §5, §6.4 caveat (i)  
**Issue:** The Fisher‑positivity form uses `c = 0.0747`. From the anchors `σ(0) = 8.98` and `σ(0.15) = 8.43`, the correct coefficient is `c = (1/8.43² − 1/8.98²) / 0.15² ≈ 0.0741`. The quoted 0.0747 corresponds to `σ(0.15) ≈ 8.42`, inconsistent with the stated anchor. The impact on σ(0.19) is negligible but the internal arithmetic is not self‑consistent.  
**Fix:** Recompute c from the declared anchors and state the consistent value (≈0.0741) or update the anchor σ(0.15) to match c = 0.0747.

---

## PAPER‑DEE‑N1 — nit (missing provenance for 17.8% novelty)  
**Section:** Abstract, §3.1 (SIMBAD cross‑match), §6.3  
**Issue:** The 17.8% genuine novelty fraction (178/1000) from the 20‑catalog CDS X‑Match is a load‑bearing headline scalar but no companion artifact (JSON/CSV) is cited, unlike other key numbers (e.g., B10_ood_results_100k.json). Traceability is broken.  
**Fix:** Deposit the cross‑match result table (e.g., `desi_top1000_xmatch_20catalogs.csv`) and cite its filename in the data‑availability statement or inline.

---

## PAPER‑DEE‑N2 — nit (static dedup arithmetic still carries)  
**Section:** Abstract, §4.3, deferral (a)  
**Issue:** The 378,280 headline relies on a dedup collapse of 10,213 detections, but the reported cross‑survey coincidences (637 pairs) would only remove 637, leaving 387,856. The unresolved 9,576‑object shortfall is a known carry (R3–R14), not new, but remains a load‑bearing arithmetic incompatibility.  
**Fix:** No new action required for this round; the deferral is acknowledged. Ensure the final cluster‑manifest artefact resolves the discrepancy before journal submission.
