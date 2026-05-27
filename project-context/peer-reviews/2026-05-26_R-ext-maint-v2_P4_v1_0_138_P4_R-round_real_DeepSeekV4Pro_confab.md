# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint-v2_P4_v1_0_138
**Wall time**: 292.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=101060, completion=7747, reasoning=7366, total=108807

---

## PAPER-DEE-B1 (MAJOR)
**Section: Conclusions; Table V (Sky Region Balance)**  
The factor‑of‑\({\sim}6\)–\(12\) smaller amplitude claimed against Shamir’s \(3\%\) asymmetry rests on a *maximum regional asymmetry* of \(0.32\%\) taken from the per‑region CW fractions in Table V. The table’s own footnote admits that “those per‑region values are manuscript‑only at this version freeze” and the cited artifact (`global_cw_fraction.json`) provides only the global CW fraction, not the individual region numbers. Consequently the key comparison scalar has no on‑disk provenance and cannot be reproduced from the displayed values alone.  
**Fix:** Supply a JSON artifact (or a script that reads the public catalog) that computes the per‑region CW fractions and spiral counts, or update the table to reference a reproducibly generated output.

## PAPER-DEE-B2 (minor)
**Section: Abstract (interpretation (i) reference amplitude); §IV.D (canonical‑mask injection sweep)**  
The abstract states that interpretation (i) corresponds to a clean cosmological dipole at amplitude \(\sim1.7\%\). This number is derived by interpolating between the injection‑recovery brackets \(A=1.5\%\) and \(A=2.0\%\) in `canonical_mask_injection_sweep.json`. The raw sweep is available, but the *interpolated 1.7 % value* is not stored as a separate provenance artifact; a reader must recreate the interpolation to verify the claim.  
**Fix:** Add a line to the sweep artefact that records the effective injected amplitude corresponding to the observed \(\sigma=+3.64\), or deposit a minimal JSON that captures the derived scalar and the interpolation method.
