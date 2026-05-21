# paper4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P4_v1_0_122
**Wall time**: 121.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=94828, completion=12564, reasoning=11885, total=107392

---

No BLOCKER or MAJOR theoretical physics or methodological issues were found in this verification pass. The paper's handling of the EFT mapping ($g_*$ vs LSS operators), the parity-even nature of the pseudoscalar dipole, and the bounds on UV-completion independence are exceptionally rigorous. 

Below are minor textual and mathematical corrections.

## PAPER-GEM-M1: Mangled copy-paste artifact across multiple sections
**Classification:** minor
**Location:** Abstract (L108), Sec IV.D (L662), Fig 6 caption (L771)
**Issue:** A broken sentence fragment resulting from a bad merge appears in three places. In Sec IV.D and Fig 6: "Under this three-discriminator framework not assigned a physical interpretation in this manuscript, not as a primordial signal; it supersedes...". In the Abstract: "Under this three-discriminator framework), with the..."
**Fix:** Clean up the grammar. Example: "Under this three-discriminator framework, the canonical-mask residual is not assigned a physical interpretation as a primordial signal; it supersedes..." (and remove the stray `),` in the abstract).

## PAPER-GEM-M2: Math formula mismatch for two-sided Bonferroni p-value
**Classification:** minor
**Location:** Sec IV.D, v1.0.122 closure of GPT-5 R22 MAJ-3 (approx L715)
**Issue:** The text writes the formula `5 \times \mathrm{erfc}(2.89/\sqrt{2})/2 \approx 0.02`. The inclusion of `/2` computes the one-sided tail ($\approx 0.01$). The numerical result $0.02$ correctly corresponds to the two-sided Bonferroni penalty.
**Fix:** Remove the `/2` from the formula so it matches the two-sided numerical result: `5 \times \mathrm{erfc}(2.89/\sqrt{2}) \approx 0.02`.

## PAPER-GEM-N1: Incorrect Table cross-reference in Figure 8 caption
**Classification:** nit
**Location:** Figure 8 caption (approx L1080)
**Issue:** The caption references "Table VI caption" when pointing the reader to the monopole-only null simulation details. The monopole-only null is Table V (Table VI is the per-imaging-leg systematics).
**Fix:** Change "Table VI" to "Table V".

## PAPER-GEM-N2: Imprecise attribution of non-zero pseudo-Cl null mean
**Classification:** nit
**Location:** Table III, footnote d
**Issue:** The footnote states the null means are non-zero "because the... null... is itself mode-coupled by the monopole+mask geometry." While the monopole contributes heavily to the low-$\ell$ inflation, the pseudo-$C_\ell$ expectation for pure white noise on a cut sky is *already* non-zero (proportional to $f_{\rm sky} \times N_{\rm shot}$) even without a monopole.
**Fix:** Change to "mode-coupled by the mask geometry and the residual monopole."
