# P4_v1058 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_1900pt
**Wall time**: 152.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=54340, completion=2047, total=56387

---

# Adversarial Peer Review: Cosmology Paper v1.0.58

**ROUND CONTEXT:** P4 v1.0.58 8th REAL cross-vendor verification round. Target: confirm GPT-5.5 + DeepSeek converge on the same clean external-review-gate state.

**YOUR FOCUS:** Paranoid about numbers without traceable sources. Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

## Findings

### PAPER-DEE-B1: Abstract Provenance for σ_dipole=0.43
**Line:** Abstract (~line 50)
**Issue:** The abstract states "real-space dipole fit yields σ_dipole=0.43 (p=0.30 at N_MC=10,000; canonical results file outputs/dipole/summary.json)". While a file path is given, there is no explicit citation or hash/checksum for the `summary.json` file. The provenance of this central result (σ_dipole=0.43) relies on an internal pathname without a versioned, immutable artifact (e.g., a DOI, commit hash, or checksum). This violates the principle of traceability for a load-bearing scalar.
**Fix:** Provide a cryptographic hash (SHA256) of the `outputs/dipole/summary.json` file in the manuscript or supplementary material. Reference a specific, versioned release tag (e.g., `paper4-v1.0`) in the public repository where this exact file can be found.

### PAPER-DEE-M1: Discrepancy in N_spiral for Sensitivity Calculation
**Line:** Sec. 8.1 (Sensitivity Floor), Eq. (σ_pix) ~line 1553
**Issue:** The sensitivity calculation uses `N_spiral / N_pix = 3,201,160 / 768 ≈ 4,168` spirals per pixel. However, the text earlier (line 1553) states an "earlier-snapshot evaluation 1/(2√4,326) ≈ 0.76%" used `N_spiral^snap = 3,321,795`. The derivation of the final `0.2%` floor involves a `~40%` rounding margin. The jump from the idealized `0.14%` to `0.2%` is justified as absorbing `N_eff` and `f_sky` corrections, but the arithmetic is not transparent. The `0.2%` figure is a headline sensitivity claim; its derivation from first principles (`N_spiral`, `f_sky`, `N_pix`) should be explicitly shown in a footnote or appendix, not buried in narrative justification.
**Fix:** Add a short derivation in the text or a footnote: `σ(A_dip) = 1/(2√(N_spiral * f_sky / (3 * N_pix))) * 1.4 ≈ 0.2%`, showing the substitution of `N_spiral=3,201,160`, `f_sky=0.46`, `N_pix=768`, and the `1.4` empirical inflation factor.

### PAPER-DEE-M2: Ambiguous "Central ~9" Factor vs. Shamir
**Line:** Abstract (~line 80) and Sec. 6.1 (~line 1300)
**Issue:** The abstract claims Shamir's ~3% asymmetry is "disfavored ... by a factor of ~6–12 ... central case ~9". Sec. 6.1 states "factor of ~6–12 smaller (depending on which Shamir 2–4% comparator is used; central ~9)". This "central ~9" is not derived from any displayed values. If Shamir's window is 2–4%, the ratio to this paper's 0.32% maximum regional asymmetry is ~6.25 (2/0.32) to ~12.5 (4/0.32). The "central ~9" appears to be the geometric mean (~8.84) but is presented without calculation or justification. For a headline comparative statement, the derivation should be explicit.
**Fix:** Explicitly state the calculation: `0.32%` vs. `2%` → factor `~6.25`; vs. `4%` → factor `~12.5`; the "central" factor could be the mean (`~9.4`) or geometric mean (`~8.84`). Specify which is used and why.

### PAPER-DEE-M3: Inconsistent MC Counts for Different Analyses
**Line:** Multiple footnotes and sections (e.g., footnote 2, Sec. 5.2)
**Issue:** The paper uses three different Monte Carlo counts for significance testing: `N_MC = 10,000` for the simple dipole bootstrap, `N_MC = 500` for the post-MASTER deconvolution null, and `N_MC = 1,000` for pre-MASTER pseudo-C_ℓ at ℓ≥2. The justification (footnote 2) is that the 500-count is due to higher computational cost. However, the `σ_dipole=0.43 (p=0.30)` result depends on the `N_MC=10,000` ensemble. For a critical null result, the MC convergence should be demonstrated or at least the uncertainty on the p-value (`~1/√N_MC`) should be noted. The p-value `0.30` with `N_MC=10,000` has an uncertainty of ~±0.005, which is acceptable, but the choice of different `N_MC` for different tests without a uniform criterion is a minor methodological inconsistency.
**Fix:** Add a sentence justifying the 500-MC choice for the expensive MASTER deconvolution (e.g., "500 realizations yield a relative standard error on σ_null of ~3.2%, sufficient given the |0.12σ| deviation"). For the `p=0.30` result, note that the binomial uncertainty on the p-value is ~0.005, which does not affect the null conclusion.

### PAPER-DEE-minor1: "0.29%" Fisher Floor vs. "0.2%" in Text
**Line:** Abstract (~line 60) and Sec. 8.1 (~line 1570)
**Issue:** The abstract states "Fisher-floor statistical Poisson asymptote is |A_dipole| ≲ 0.29% at 3σ". In Sec. 8.1, the derived "ideal full-sky ratio" gives `0.146%` which is then rounded up to `0.2%` as a "conservative two-sig-fig statement". The abstract's `0.29%` is nearly double the `0.146%` ideal value. The text explains the `0.29%` includes the factor-of-2 correction for the `A/2` vs. `A` convention (line 60: "updated factor-of-2 accounting"). This is confusing: the abstract `0.29%` and the text `0.2%` refer to the same quantity but with different conventions and rounding. For clarity, the abstract should use the same rounded value (`0.2%`) as the text, or the text should explicitly derive the `0.29%` figure.
**Fix:** In Sec. 8.1, after deriving the `0.146%` ideal value, explicitly apply the factor-of-2 correction (since `A_dip` in the paper's convention is the full amplitude, not the half-amplitude) to obtain `0.292% ≈ 0.29%`, then state the conservative rounding to `0.2%` accounts for `f_sky` and `N_eff`. The abstract should then cite the `0.29%` Fisher floor and the `>0.5%` empirical floor.

### PAPER-DEE-minor2: Missing Explicit Citation for "0.43σ" in Conclusions
**Line:** Conclusions, point 1 (~line 1780)
**Issue:** The conclusions state "the simple real-space dipole, 0.43σ, is retained as a complementary cross-check". This number is load-bearing. While it is presumably the same `σ_dipole=0.43` from the abstract and Sec. 5.2, the conclusions do not cite a specific result line or table. For a standalone reading of the conclusions, the provenance should be immediately clear.
**Fix:** Add a parenthetical citation: "(Sec. 5.2; σ_dipole=0.43, p=0.30)".

## Summary
- **BLOCKERs:** 1 (PAPER-DEE-B1). The provenance of the central `σ_dipole=0.43` result is not fully traceable without a checksum or versioned artifact.
- **MAJORs:** 2 (PAPER-DEE-M1, PAPER-DEE-M2). The sensitivity calculation derivation is opaque, and the "central ~9" factor vs. Shamir is not explicitly derived.
- **minor:** 2 (PAPER-DEE-minor1, PAPER-DEE-minor2). Inconsistency between abstract/text on Fisher floor, and missing citation in conclusions.

**Overall:** The paper is close to external-review-gate state. The single BLOCKER is addressable by providing a cryptographic hash for the key result file. The MAJORs require explicit derivations for clarity. With these fixes, the manuscript would satisfy the `feedback_99_pct_readiness_cap` gate.
