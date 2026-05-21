# paper4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P4_v1_0_122
**Wall time**: 364.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=89589, completion=14259, reasoning=12252, total=103848

---

# Adversarial Peer Review — Provenance Audit

## PAPER-DEE-M1 (MAJOR) — Abstract/Conclusions monopole significance inconsistent with displayed fraction

**Location:** Abstract (line “$0.4974 \pm 0.000279$” and “$9.5\sigma$”) and Conclusions (item 1, same numbers).

**Issue:** The abstract and conclusions quote the equivariant CW fraction as $0.4974 \pm 0.000279$ and state the deviation from 50/50 is $9.5\sigma$. Using the displayed value $0.4974$ gives $(0.5-0.4974)/0.000279 = 9.32\sigma$, not $9.5\sigma$. The paper’s own derivation (Sec. IV.B) uses the unrounded fraction $0.49735$ to obtain $9.47\sigma \approx 9.5\sigma$. The headline significance cannot be reproduced from the number actually shown in the abstract.

**Fix:** Either report the more precise fraction $0.49735 \pm 0.000279$ in the abstract and conclusions, or round the significance to $9.3\sigma$ to match the displayed $0.4974$.

---

## PAPER-DEE-M2 (MAJOR) — Per‑region asymmetry numbers lack a released provenance artifact

**Location:** Abstract (“maximum regional asymmetry is 0.32%”) and Conclusions (same claim), referencing Table VII.

**Issue:** The 0.32% maximum regional asymmetry and the seven per‑region CW fractions in Table VII are a load‑bearing comparator against Shamir’s claims. The only verification artifact cited for that table is `global_cw_fraction.json`, which the footnote explicitly states “does not independently verify the per‑region numerators / denominators … those per‑region values are manuscript‑only at this version freeze.” No JSON, script, or dataset on disk produces the 0.32% number; it exists only in the manuscript.

**Fix:** Provide a dedicated per‑region JSON artifact (e.g., `per_region_cw_fraction.json`) under the release tag, or clearly mark the number as unverifiable in the current release and remove it from the abstract until the artifact is available.

---

## PAPER-DEE-m1 (minor) — Conclusions misstate injection‑recovery probability

**Location:** Conclusions, item 1 (“P(σ>3)=0.50 at A=0.75%”).

**Issue:** The conclusions say $P(\sigma>3)=0.50$ at $A=0.75\%$, but Table IX (and the abstract) report $P(\sigma>3)=0.55$ at that amplitude. The discrepancy is small but the conclusions’ number is not the one displayed in the table.

**Fix:** Change “0.50” to “0.55” to match Table IX.

---

## PAPER-DEE-n1 (nit) — Trials‑correction formula contains an extraneous factor

**Location:** End of §IV.D, v1.0.122 closure paragraph (“5×erfc(2.89/√2)/2≈0.02”).

**Issue:** The intended family‑wise Bonferroni p‑value for a two‑tailed test is $5 \times \operatorname{erfc}(2.89/\sqrt{2}) \approx 0.02$. The printed expression includes a spurious division by 2, making the formula inconsistent with the stated result (though the result itself is numerically correct).

**Fix:** Remove the “/2” from the expression, or rewrite as “$5 \times$ (two‑tailed $p$) $\approx 0.02$”.
