# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1640pt_P4_v1_0_115_R20
**Wall time**: 142.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=83217, completion=9208, reasoning=7862, total=92425

---

# Adversarial Peer Review — R20 Cross-Vendor (confabulation-hunting mode)

## Finding 1: BLOCKER — Abstract misstates historical v1.0.62 baseline sigma for canonical-mask residual

- **ID:** PAPER-DEE-B1
- **Section:** Abstract (line ~“the legacy +3.64σ v1.0.62 baseline …”)
- **Issue:** The abstract claims “the legacy +3.64σ v1.0.62 baseline was on uncorrected A_p field”.  However, the paper’s own NaMaster configuration appendix (Sec. VI — “NaMaster MASTER configuration”) and the v1.0.112 sigma‑reconciliation block explicitly state that the v1.0.62 baseline produced **σ = +1.85**, not +3.64.  The corrected value (+3.64σ) supersedes the +1.85, but the abstract falsely assigns +3.64 to the historical baseline.  This is a direct internal contradiction that misrepresents the result’s evolution.
- **Fix:**  Replace “the legacy +3.64σ v1.0.62 baseline” with “the legacy +1.85σ v1.0.62 baseline”.  The sentence should then read that the corrected value (+3.64σ under proper monopole subtraction) replaces the earlier +1.85σ.

---

## Finding 2: MAJOR — “∼0.6% residual amplitude” in abstract lacks any on‑disk provenance or in‑paper derivation

- **ID:** PAPER-DEE-M1
- **Section:** Abstract (line “+0.43σ (p=0.30, ∼0.6% residual amplitude”)
- **Issue:** The abstract quotes a residual dipole amplitude of ≈0.6% for the post‑TTA Catalog C real‑space dipole.  Nowhere in the main text (Sec. IV, “Dipole Analysis”) is the fitted amplitude reported as a percentage; only the significance (+0.43σ) appears.  No JSON artifact is cited specifically for this amplitude value, and no equation or table lets a reader reproduce it from displayed numbers.  An unsourced scalar in the abstract violates the reproducibility requirement.
- **Fix:**  Either (1) add the fitted dipole amplitude (with uncertainty) to Sec. IV and reference the artifact `catalog_c_post_tta_dipole_summary.json` that contains it, or (2) delete “∼0.6% residual amplitude” from the abstract.

---

## Finding 3: minor — Abstract’s sudden +4.73σ ℓ=2 / +3.63σ ℓ=1 numbers appear without a direct artifact pointer

- **ID:** PAPER-DEE-M2
- **Section:** Abstract (ℓ=2 > ℓ=1 broadband‑structure clause)
- **Issue:** The abstract quotes auto‑spectrum significances (+4.73σ at ℓ=2, +3.63σ at ℓ=1) from the multi‑null battery, but no inline artifact reference is given.  The main text does eventually cite `p4_multinull_battery.json`, yet the abstract—which is dense with load‑bearing scalars—omits any pointer.  A reader cannot immediately determine whether these numbers exist on disk.
- **Fix:**  Append a brief parenthetical artifact reference, e.g., “(artifact `p4_multinull_battery.json`)”, or move the detailed numerical list to the conclusions where a single citation can cover the battery.

## Finding 4: minor — “99.3% reproduction” relies on a table ratio that is not independently cross‑checked against shot‑to‑shot variation

- **ID:** PAPER-DEE-M3
- **Section:** Abstract (pre‑MASTER leakage reproduction)
- **Issue:** The 99.3% figure is computed as 1.6846 × 10⁻² / 1.696 × 10⁻², a single‑realization ratio of means.  The null‑mean uncertainty is ±6.8 × 10⁻⁵, so the ratio’s own sampling noise is not propagated.  The abstract presents this as a precise percentage without conveying that the numerator is a sample mean.  This is a presentation flaw, not a computational error.
- **Fix:**  Quote an interval, e.g., “reproduces 99.3%±0.4% (1σ sampling) of the observed amplitude”, or state that the residual is consistent with zero within the null’s uncertainty.

## Finding 5: nit — Abstract claims “the +3.64σ replaces it as the canonical canonical-mask number” while the number itself is unchanged

- **ID:** PAPER-DEE-N1
- **Section:** Abstract (v1.0.107+ convention statement)
- **Issue:**  Because the abstract mistakenly says the legacy baseline was also +3.64σ (see B1), the phrase “the +3.64σ replaces it” becomes nonsense—a number replacing itself.  With the correct legacy value (+1.85σ) the statement is clear, but the current wording is confusing.
- **Fix:**  Once B1 is corrected, the replacement logic is self‑explanatory and requires no further edit.

## Finding 6: nit — Abstract’s “f_sky=0.49005” mask fraction given to 5 significant figures without direct citation

- **ID:** PAPER-DEE-N2
- **Section:** Abstract (pre‑MASTER mask description)
- **Issue:**  The sky fraction 0.49005 appears as a precise 5‑digit number.  The memo box in Sec. III‑D (Table 2 caption) states that this value derives from `monopole_mask_null_results.json`, but the abstract itself does not anchor this precision to any artifact.  While the number is reproducible from the HEALPix pixel count, a reader skimming the abstract may wonder whether it is a rounded artefact.
- **Fix:**  Either quote the fraction to 3 significant digits (0.490) in the abstract, or add a brief parenthetical “(see Tab. II and companion JSON)” the first time it appears.
