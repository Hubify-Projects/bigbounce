# P3_v3147_R9 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1230pt
**Wall time**: 273.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=59942, completion=8781, reasoning=7760, total=68723

---

# Adversarial Peer Review — R9: P3 v3.1.47 (confabulation‑hunter)

## PAPER‑DEE‑B1: BLOCKER — GS asymmetric‑remap arithmetic is invalid under claimed Fisher‑positivity form  
**Location:** Version‑history notes and §6.4 deferral list, item (j).  
**Issue:** The negative error bar “fix” states that the 1σ α‑CI \([ -0.20, 3.86]\) (α = +1.83 ± 2.03) maps through \(\sigma(\alpha)=(F_0 + c\alpha^2)^{-1/2}\) (the form from caveat (i) with \(F_0=1/8.98^2\), \(c=0.0747\)) to \(\sigma\!\in\![2.04,\,3.40]\) centred on \(\sigma(1.83)=2.43\).  
- With the quoted \(F_0,c\), \(\sigma(0)=8.98\).  
- Since the α‑interval includes zero, the mapped σ interval must include \(8.98\); the lower bound would be \(\sigma(3.86)\approx1.1\).  
- The claimed narrow interval \([2.04, 3.40]\) is mathematically incompatible with the stated mapping unless \(F_0,c\) are entirely different and the α‑CI is furthermore truncated to exclude zero—neither of which is specified.  
**Fix:** Re‑compute the α→σ mapping properly for the GS case, using either a GS‑specific Fisher form with explicit anchors or a truncated credible interval that respects the positivity boundary. Remove the erroneous \([2.04, 3.40]\) claim until a correct remap is provided.

---

## PAPER‑DEE‑M1: MAJOR — 17.8 % genuine novelty fraction untraceable  
**Location:** Abstract (∼17.8 %), §4.1 “Archival cross‑match and genuine novelty fraction”, and §7 Conclusions.  
**Issue:** The paper states that 178 of the top‑1000 DESI anomalies remain unmatched after cross‑match against 20 all‑sky catalogs via CDS X‑Match, yielding a headline novelty fraction of 17.8 %. No companion artifact (JSON/parquet/script) documents this cross‑match; the data‑availability section does not include the matched catalog or the X‑Match query logs. This is a load‑bearing number in the abstract and conclusions that cannot be reproduced from the paper’s cited artifacts.  
**Fix:** Deposit the cross‑match result table (e.g., `desi_top1000_xmatch_20cats.parquet` or equivalent) together with the query script, and cite it explicitly in §4.1. Until then, qualify the 17.8 % figure as “preliminary—artifact pending”.

---

## PAPER‑DEE‑M2: MAJOR — Headline catalog size 378 280 remains arithmetically unreconciled  
**Location:** Abstract, §4.3, §7, and deferral (a) in §6.4 / version notes.  
**Issue:** The paper reports 388 493 survey‑level detections and 637 pairwise cross‑survey coincidences, which directly gives 387 856 unique objects—not 378 280. The 9 576‑object shortfall is acknowledged as an open deferral, yet the title, abstract, and conclusions continue to use 378 280 as the canonical unique‑anomaly count without an inline numeric resolution. This undermines the central catalog claim.  
**Fix:** Either recompute the union‑find cluster manifest to produce a consistent unique‑object count, or replace the headline with the arithmetic upper bound 387 856 and explicitly note that the exact number is pending. A paper submitted with a known‑incorrect headline cannot stand.

---

## PAPER‑DEE‑m1: minor — Liang+2023 baseline missing precise citation pin  
**Location:** Abstract (141× comparison), §7.  
**Issue:** The claim that Liang + 2023 found 2 685 anomalies on DESI EDR is used to compute the 141× scale factor. While the number is plausible, the paper does not give the exact table or section in Liang’s paper where this count appears, nor is there a corresponding validation artifact in this paper’s data release. This is a minor provenance gap for a supporting comparison.  
**Fix:** Add a parenthetical reference to the specific figure/table in Liang+2023, and optionally include a one‑line verify script that reads the Liang count from the public catalog (if available) to make the comparison reproducible.
