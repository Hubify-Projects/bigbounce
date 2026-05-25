# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P4_v1_0_128
**Wall time**: 240.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=91923, completion=8865, reasoning=7848, total=100788

---

# Adversarial Peer-Review Findings: Provenance of Load-Bearing Scalars

## Finding PAPER-DEE-M1 (MAJOR)
**Section:** Abstract, line ~ “The real-space post-TTA Catalog~C dipole is $+0.43\sigma$ ($p\!=\!0.30$, $\sim\!0.6\%$ residual amplitude).”
**Issue:** The abstract claims a residual dipole amplitude of $\sim\!0.6\%$, but the main text only reports the dipole *significance* ($0.43\sigma$, $p=0.30$). No table, equation, or explicit artifact reference in the paper provides the best-fit dipole amplitude. The number cannot be reproduced from displayed values, and the reader cannot verify it without accessing an unspecified JSON output.
**Fix:** Either state the best-fit amplitude in the dipole analysis section (e.g., from `dipolar_analysis.log`/`summary.json`) and cite the artifact, or remove the “$\sim\!0.6\%$” from the abstract and use only the significance.

## Finding PAPER-DEE-M2 (minor)
**Section:** Abstract / Conclusions, “$9.5\sigma$ from $50/50$” monopole deviation.
**Issue:** The $9.5\sigma$ value is derived from $0.4974 \pm 0.000279$ and is arithmetically correct, but the paper never displays the exact calculation or a simple JSON key that independently reports the deviation. A single line in a provenance JSON (e.g., `global_cw_fraction.json`) confirming the computed $\sigma$ would harden the number’s traceability and prevent rounding disputes.
**Fix:** Add a field like `“sigma\_from\_parity”` to `global_cw_fraction.json` and reference it in the text.

## Finding PAPER-DEE-M3 (minor)
**Section:** Abstract and multi‑null verdict, “$+4.73\sigma$ at $\ell\!=\!2$ vs $+3.63\sigma$ at $\ell\!=\!1$” auto‑spectrum values.
**Issue:** These two numbers are quoted in the abstract and discussion but are not present as a standalone table or figure; they appear only in the narrative of the multi‑null battery. A reader wishing to verify them must extract the values from the `p4_multinull_battery.json` artifact, which is not a conventional table. A small inline table in the relevant subsection would close the provenance gap.
**Fix:** Insert a one‑line table or a sentence that directly links the $\ell\!=\!1$ and $\ell\!=\!2$ $\sigma$ values to the corresponding `p4_multinull_battery.json` keys.

## Finding PAPER-DEE-N1 (nit)
**Section:** Conclusions, “$0.32\%$ maximum regional asymmetry” vs. the sky‑balance table.
**Issue:** Table~\ref{tab:sky_balance} shows per‑region values with $|\Delta|$ up to $0.32\%$; this is correctly derived. However, the table’s footnote indicates the per‑region values are “manuscript‑only at this version freeze” and a dedicated per‑region JSON is queued for the next revision. Thus the $0.32\%$ number currently has no on‑disk artifact that can be independently cross‑checked.
**Fix:** Commit the per‑region JSON to the release tag before paper finalization, and reference it from the table.

## Finding PAPER-DEE-N2 (nit)
**Section:** Abstract, “$0.5\%$ is a tested non‑detection point at the present pipeline, not the operational floor.”
**Issue:** The number $0.5\%$ refers to the injection sweep amplitude with $P(\sigma\!>\!3)\!=\!0.15$. The abstract does not cite the sweep table (Table~\ref{tab:mc_injection}) or its companion artifact `wave_14_nn_injection_recovery.json`. Without that link the provenance is obscured.
**Fix:** Add a parenthetical reference to Table~\ref{tab:mc_injection} or the artifact path in the abstract.

## Finding PAPER-DEE-N3 (nit)
**Section:** Abstract, “post‑MASTER canonical‑mask direct‑MC residual is $+3.64\sigma$ … (the legacy $+1.85\sigma$ v1.0.62 baseline …)”  
**Issue:** The $+1.85\sigma$ baseline is mentioned but not referenced to its exact artifact (`canonical_n_master_l1_direct_v1062_baseline.json`). While the corrected $+3.64\sigma$ is well documented, the historical number lacks an immediate citation.
**Fix:** Insert a short footnote pointing to the v1.0.62 artifact so both numbers have equal provenance traceability.
