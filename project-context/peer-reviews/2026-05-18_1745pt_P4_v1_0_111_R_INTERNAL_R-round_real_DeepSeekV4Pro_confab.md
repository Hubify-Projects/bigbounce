# P4_v1_0_111_R_INTERNAL R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1745pt
**Wall time**: 152.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=85108, completion=9313, reasoning=7693, total=94421

---

# Peer Review — Chirality Catalog Paper v1.0.111

**Focus:** Traceability of load‑bearing scalars in abstract and conclusions.  
**Classification key:** BLOCKER / MAJOR / minor / nit  

Below are **6 findings** (the maximum allowed). They address the five requested verification points and the instruction to flag headline figures with no on‑disk provenance or arithmetic that cannot be reproduced from displayed values.

---

## **PAPER‑DEE‑B1** — BLOCKER  
**Section:** Abstract (sensitivity claim)  
**Issue:** The abstract states the empirical 50%-recovery-at‑3σ threshold “on the $N = 471{,}049$ HC‑spiral subsample” and then **immediately contradicts itself** in the same paragraph: the P4‑EXT ChatGPT‑B3 clarification explicitly says the injection sweep was run on the $p_{\rm eq} > 0.6$ HC‑spiral subsample (`config.hc_threshold = 0.6`, $N = 2{,}107{,}494$), **NOT** on the in‑paper $P>0.9$ HC subsample ($N = 471{,}049$).  
The headline sensitivity is therefore attributed to the wrong sample, and the abstract’s simultaneous placement of the threshold on $N=471{,}049$ is **factually incorrect**.  
**Fix:** Remove all references to the $471{,}049$ sample in the sensitivity statement. Specify the sample on which the empirical $0.75\%$ threshold is actually measured ($p_{\rm eq}>0.6$, $2.1$M), and adjust the Fisher‑floor comparison accordingly (as the later clarification does). The abstract must be internally consistent.

---

## **PAPER‑DEE‑B2** — MAJOR  
**Section:** Abstract / §IV.D (closure logic) — “sky‑rotation null gives $+2.56\sigma$”  
**Issue:** The abstract and the v1.0.108 multi‑null battery discussion claim that a **sky‑rotation null** yields $+2.56\sigma$ and that this is part of the evidence against a primordial dipole. **No artifact, table, or script is cited** that produces this number. The described 4‑null battery (`p4_multinull_battery.json`) enumerates only (1) apodized mask, (2) multipole‑spectrum diagnostic, (3) bootstrap resample, and (4) $p_{\rm eq}$ quartile stratification; the sky‑rotation null is **absent** from that list and from any other traceable output. The $+2.56\sigma$ value is therefore unverifiable.  
**Fix:** Either provide the missing artifact (e.g., a dedicated JSON file showing the null distribution and the derived $z$‑score) or remove the sky‑rotation claim from the paper. If it is part of the same battery, update the battery description to include it.

---

## **PAPER‑DEE‑B3** — MAJOR  
**Section:** Abstract (99.3% reproduction claim) — arithmetic traceability  
**Issue:** The statement “reproduces $\mathbf{99.3\%}$ of the observed pre‑MASTER pseudo‑$C_1$ power” is derived as the ratio $1.6846\times10^{-2} / 1.696\times10^{-2}$ from Table IV. The two numbers are themselves drawn from `monopole_mask_null_results.json`. While the arithmetic is correct, the **provenance of the observed $C_1 = 1.696\times10^{-2}$** is not explicitly cited in the abstract; the table gives the data value, but the abstract mentions the pre‑MASTER observed value without pointing to the artifact that records it. A careful reader cannot trace the observed $C_1$ to a specific JSON file without cross‑referencing the table, and the table’s caption only links to the null‑simulation artifact, not to the raw data‑measurement artifact.  
**Fix:** In the abstract or immediately adjacent sentence, cite the exact artifact that contains the observed pre‑MASTER $C_1$ (e.g., the raw `monopole_mask_null` output or a separate data‑extraction JSON) so the provenance chain is complete: observed value → table → artifact.

---

## **PAPER‑DEE‑B4** — minor  
**Section:** §IV.D (multi‑null battery) — numerical inconsistency in $\ell=2>\ell=1$ argument  
**Issue:** The paper argues that the observed pattern $\ell=2$ significance ($+4.73\sigma$) exceeds $\ell=1$ ($+3.63\sigma$) is incompatible with a clean cosmic dipole. The $+4.73\sigma$ and $+3.63\sigma$ are given with three significant figures, but the **uncertainties on these $z$‑scores are not quantified**. The null distributions used to compute them may have finite statistical uncertainty (e.g., from 200 or 500 MC realizations), which could blur the difference. A formal test of $\ell=2 > \ell=1$ would require propagating that uncertainty, but the paper treats the ordering as qualitatively decisive.  
**Fix:** State the standard error of the $z$‑score from the MC ensemble (e.g., $\pm0.1\sigma$) or note that the qualitative conclusion stands regardless of the ordering uncertainty. This is minor because the cross‑spectrum and quartile evidence are independent, but it slightly weakens the logical tightness.

---

## **PAPER‑DEE‑B5** — nit  
**Section:** Abstract — the $0.75\%$ threshold’s Fisher‑floor ratio  
**Issue:** After the correction (PAPER‑DEE‑B1), the abstract still contains messy residual text: “the like‑for‑like HC‑subsample Fisher floor is $3\sqrt{3/N}\approx 0.76\%$ at $N=471{,}049$, which the $0.75\%$ HC empirical threshold tracks essentially exactly (ratio $\approx\!1.0$ …)”. This sentence compares the empirical threshold (derived from the $p_{\rm eq}>0.6$ sample) to the Fisher floor of the $471k$ sample, which is a **cross‑sample comparison** and is acknowledged as such in the next sentence. The juxtaposition may confuse readers.  
**Fix:** Move the like‑for‑like comparison to the $p_{\rm eq}>0.6$ sample: state that for that sample the empirical $0.75\%$ corresponds to a $\sim\!2\times$ degradation relative to its Fisher floor, as already noted later. Remove the misleading “ratio $\approx\!1.0$” sentence from the abstract.

---

## **PAPER‑DEE‑B6** — nit  
**Section:** §IV.D (closure logic) — “bootstrap‑null result is the canonical honest framing”  
**Issue:** The text states that the bootstrap null is **tautological** and is dropped from the interpretation, yet it still lists the bootstrap result ($-0.22\sigma$) as the “canonical honest framing”. The phrase “canonical honest framing” is ambiguous: it might be interpreted as the primary null, which contradicts the explicit statement that the bootstrap is not a discriminator.  
**Fix:** Clarify that the bootstrap result is reported only for transparency as a diagnostic of sampling variance, not as a discriminator. Remove “canonical honest framing” or rephrase to “reported for completeness only”.
