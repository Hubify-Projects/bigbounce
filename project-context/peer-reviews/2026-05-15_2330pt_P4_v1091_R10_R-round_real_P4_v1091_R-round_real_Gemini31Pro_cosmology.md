# P4_v1091 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2330pt_P4_v1091_R10_R-round_real
**Wall time**: 98.9s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=81445, completion=11811, reasoning=9865, total=93256

---

## Finding 1: Incomplete Propagation of 0.5% -> 0.75% Sensitivity Floor
**Classification:** BLOCKER
**ID:** PAPER-GEM-B1
**Section:** Sec 5.4, Sec 6.6, Sec 8 (Conclusions)

**Issue:** The global sweep to replace the 0.5% sensitivity floor with the empirical 0.75% threshold was incomplete. While the abstract and early sections correctly identify 0.75% as the 50%-recovery threshold and 0.5% as a non-detection point, Sections 5.4, 6.6, and 8 revert to claiming 0.5% as the systematic-inclusive threshold/bound. 

**Fix:** Replace ">= 0.5%" with ">= 0.75%" in Sec 5.4 and Sec 6.6. In Sec 8, change "threshold of ~0.5% at 3sigma" to "threshold of ~0.75% at 3sigma".

| Truth-Audit | Details |
| :--- | :--- |
| **Cite** | Sec 5.4, Sec 6.6, Sec 8 |
| **Paper-says** | "with >= 0.5% empirical systematic-inclusive" (Sec 5.4); "amplitude >= 0.5% on this footprint" (Sec 6.6); "threshold of ~0.5% at 3sigma" (Sec 8) |
| **Artifact-says** | `injection_recovery_extended.json` confirms 50% recovery is at 0.75%, while 0.5% yields only 15% recovery. |
| **Verdict** | REGRESSION / STILL-UNRESOLVED |
| **Fix Proposal** | Standardize all remaining threshold claims to 0.75%. |

## Finding 2: Impossible Negative Null Mean in Table III Footnote Arithmetic
**Classification:** BLOCKER
**ID:** PAPER-GEM-B2
**Section:** Table III, Footnote d

**Issue:** The footnote attempts to reverse-engineer the null mean using the displayed z-score, resulting in `<C_ell^null> \approx 3.210 - 0.804 * 6.097 = -1.69`. A pseudo-$C_\ell$ auto-power spectrum is positive definite ($|a_{\ell m}|^2 \ge 0$); a negative null mean across 1000 MC realizations is mathematically impossible unless the values are already noise-subtracted, which contradicts the table's "before shot-noise subtraction" unit definition. This is an LLM arithmetic confabulation.

**Fix:** Remove the confabulated arithmetic example. Extract the true positive null mean directly from the NaMaster MC log.

| Truth-Audit | Details |
| :--- | :--- |
| **Cite** | Table III, Footnote d |
| **Paper-says** | "e.g. ell_eff=4 has <C_ell^null> \approx 3.210 - 0.804 * 6.097 = -1.69" |
| **Artifact-says** | Auto-power spectra cannot have a negative mean. The z-score computation in the script likely uses a different baseline or the table values are mislabeled. |
| **Verdict** | NOVEL |
| **Fix Proposal** | Delete the `-1.69` example. Check the actual MC log for the true $\mu$ and $\sigma$ to ensure the $z=6.097$ is correct. |

## Finding 3: N=949,584 vs 944,826 Cross-Table Discrepancy
**Classification:** MAJOR
**ID:** PAPER-GEM-M1
**Section:** Sec 6.4 vs Table V

**Issue:** The text in Sec 6.4 defines the `HC-spiral-0.6` sample as having $n=949,584$. However, summing the corresponding high-confidence bins ($p \ge 0.6$) in Table V yields $193,560 + 131,364 + 619,902 = 944,826$. This leaves 4,758 galaxies unaccounted for under the exact same probability cut.

**Fix:** Recompute the Table V bins to ensure they sum to the canonical 949,584, or explicitly document the filtering step that removes the 4,758 galaxies from the Table V stratification.

| Truth-Audit | Details |
| :--- | :--- |
| **Cite** | Sec 6.4, Table V |
| **Paper-says** | "HC-spiral-0.6: n=949,584" vs Table V sum = 944,826 |
| **Artifact-says** | `face_on_robustness_results.json` confirms $n=949,584$ for the $p>0.6$ cut. |
| **Verdict** | NOVEL |
| **Fix Proposal** | Align Table V bin counts with the JSON artifact totals. |

## Finding 4: Mashed-Sentence Oxymoron in Bandpower Definition
**Classification:** MAJOR
**ID:** PAPER-GEM-M2
**Section:** Sec 4.3

**Issue:** The text describes the $\ell_{\rm eff}=4$ bandpower as a "non-dipole bandpower / mode-coupling diagnostic... following the standard pseudo-Cl convention for cut-sky ell=1 recovery". This is an oxymoron resulting from a poorly merged text revision. A non-dipole bandpower ($\ell \in [2,6]$) is not used for $\ell=1$ recovery.

**Fix:** Delete the phrase "following the standard pseudo-Cl convention for cut-sky ell=1 recovery" from the parentheses.

| Truth-Audit | Details |
| :--- | :--- |
| **Cite** | Sec 4.3 |
| **Paper-says** | "reported as a non-dipole bandpower... following the standard pseudo-Cl convention for cut-sky ell=1 recovery" |
| **Artifact-says** | N/A (Logical contradiction) |
| **Verdict** | REGRESSION |
| **Fix Proposal** | Truncate the sentence after "parity-even pseudo-power spectrum". |

## Finding 5: Overly Strong Exclusion Language
**Classification:** minor
**ID:** PAPER-GEM-m1
**Section:** Sec 8 (Conclusions), Item 1

**Issue:** The conclusion states "our null dipole result rules it out at the empirical level". For a methods paper establishing a systematic floor, "rules out" is too definitive, especially given the lack of a matched-pipeline reanalysis of Shamir's specific data.

**Fix:** Soften "rules it out" to "is inconsistent with it" or "strongly disfavors it".

| Truth-Audit | Details |
| :--- | :--- |
| **Cite** | Sec 8, Item 1 |
| **Paper-says** | "our null dipole result rules it out at the empirical level" |
| **Artifact-says** | N/A (Tone/Scope issue) |
| **Verdict** | STILL-UNRESOLVED |
| **Fix Proposal** | Change to "is inconsistent with it at the empirical level". |

## Finding 6: Artifact Name Mismatch
**Classification:** minor
**ID:** PAPER-GEM-m2
**Section:** Sec 3.6 vs Sec 6.4

**Issue:** The paper cites `wave_14_oo_cw_flatness_morphology.json` in Sec 3.6, but cites `wave_14_oo_bin_flatness.json` in Sec 6.4 for what appears to be the exact same morphology flatness test. 

**Fix:** Unify the artifact citations to the single correct filename that exists on the repository's default branch.

| Truth-Audit | Details |
| :--- | :--- |
| **Cite** | Sec 3.6, Sec 6.4 |
| **Paper-says** | `wave_14_oo_cw_flatness_morphology.json` vs `wave_14_oo_bin_flatness.json` |
| **Artifact-says** | Only one of these files likely exists as the canonical output of `wave_14_oo_bin_flatness.py`. |
| **Verdict** | NOVEL |
| **Fix Proposal** | Replace the Sec 3.6 reference with `wave_14_oo_bin_flatness.json`. |
