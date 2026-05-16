# P4_v1084_R5 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1840pt
**Wall time**: 293.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=72221, completion=9788, reasoning=7713, total=82009

---

## Finding 1 — Baseline `w_CW` significance at 0.50° is inconsistent between the main table and the brick-boundary control paragraph (MAJOR)

- **ID:** PAPER-DEE-B1
- **Section:** §4.7 (Two-Point Chirality Correlation) and the brick-boundary control sub-paragraph
- **Concrete issue:** Table 4 explicitly reports `w_CW` at θ = 0.50° as −0.0111 with null σ = 0.0046, giving −2.41 σ (confirmed by the text immediately above the Figure). The brick‑boundary control sub‑paragraph introduced in v1.0.84, however, refers to “the −2.6 σ excursion at θ = 0.50° in the baseline sample”. The two values (−2.41 σ vs. −2.6 σ) cannot both be correct for the same 50 000‑galaxy baseline sample. The control test’s conclusion depends on the baseline significance to quantify the shift; a 0.19 σ discrepancy undermines the “decisive” claim.
- **Fix:** Re‑compute the baseline `w_CW` from the exact same run as the interior sample and report the value (or reconcile the two numbers). If the baseline was re‑calculated with a different seed or binning, state that explicitly and ensure both values appear in the control‑test artifact. Align the text with the artifact’s actual baseline σ.

---

## Finding 2 — Provenance of the pre‑MASTER pseudo‑`C_ℓ` +6.48 σ headline is not traceable to the same data vector that collapses to −0.12 σ (MAJOR)

- **ID:** PAPER-DEE-B2
- **Section:** Abstract; §4.3 (Dipole Analysis) and footnotes
- **Concrete issue:** The abstract narrates a collapse “on the same data” from a raw pseudo‑`C_ℓ` at ℓ = 1 of +6.48 σ to a MASTER‑deconvolved −0.12 σ. The −0.12 σ belongs to the analysis subsample mask (`f_sky` = 0.659, `n` = 5 547 858 pixel‑weighted). The +6.48 σ figure appears only in a re‑compute footnote that uses a different mask (`f_sky` ≈ 0.491, canonical mask) and a separate verification script (`wave11c_nspiral_recompute_2026‑05‑01/results.json`). The paper does not state the pre‑MASTER pseudo‑`C_ℓ` value or its σ on the subsample mask, so the claimed collapse cannot be verified from the displayed numbers. A scalar that is load‑bearing for the abstract lacks a single traceable provenance that directly produces the sequence.
- **Fix:** Either (a) report the pre‑MASTER pseudo‑`C_ℓ` at ℓ = 1 computed on the identical subsample‑mask map that gives −0.12 σ post‑MASTER, with an artifact that records both values in one file; or (b) rewrite the abstract to separate the masks clearly (e.g., “+6.48 σ on the canonical mask; after MASTER and a larger‑`f_sky` mask the significance drops to −0.12 σ”). The “same data” phrase must be qualified.

---

## Finding 3 — DECaLS high‑confidence bin residual at +3.76 σ/+4.06 σ is flagged as systematic but lacks a per‑leg depth/PSF cross‑check (MAJOR)

- **ID:** PAPER-DEE-B3
- **Section:** §4.6 (Signal‑hunt diagnostics), per‑leg × confidence sub‑stratification
- **Concrete issue:** The DECaLS‑only `p_eq ∈ [0.8, 1.0)` bin yields a dipole significance of +3.76 σ (isotropic null) / +4.06 σ (monopole‑preserving null) against a local per‑leg null, and the paper correctly notes this is “not consistent with a pure classifier‑confidence‑correlated label‑noise systematic”. The attribution to “known DECaLS‑vs‑BASS+MzLS depth/PSF differences” is qualitatively plausible, but no per‑leg PSF cross‑correlation or binned depth‑stratification is performed; the global PSF‑cross‑power test reaches only |z| = 2.72 σ and does not isolate DECaLS. A journal referee would ask for a quantitative test before accepting the “systematic” interpretation of a 4 σ excursion.
- **Fix:** Either add a DECaLS‑only cross‑power of `f_CW` against per‑pixel depth or PSF ellipticity, or reframe the statement as “the DECaLS HC residual is unexplained and requires a dedicated follow‑up; it does not alter the global subsample‑mask MASTER null at ℓ = 1”. The paper already says “left for future work”, which is acceptable, but the current wording (“most plausibly attributed”) overstates the evidence.

---

## Finding 4 — The monopole‑mask null’s hemisphere max‑amplitude residual +4.42 σ is not explicitly documented as a load‑bearing artifact (minor)

- **ID:** PAPER-DEE-B4
- **Section:** Abstract; §4.5 (Monopole+Mask Leakage Generative Null), Table I
- **Concrete issue:** The abstract states “the monopole‑only null recovers ∼49% of the observed amplitude (residual +4.42 σ)”. Table I lists the hemisphere max‑amplitude data value, null mean, and z‑score, and cites `monopole_mask_null_results.json`. However, that JSON artifact’s description in the text only explicitly enumerates pre‑MASTER and post‑MASTER statistics; the hemisphere max‑amplitude row’s presence in the JSON is not confirmed by a field‑level excerpt in the paper. A reviewer reading the artifact should be able to locate the exact field that produces the 49% recovery.
- **Fix:** In the artifact description (or a footnote), explicitly list the JSON keys that store the hemisphere max‑amplitude data, null mean, and null std, and state the computation of the recovery fraction. No new computation is required—just a documentation patch.

---

## Finding 5 — The `p_CW` value in the abstract and monopole‑mask null references are rounded differently, causing an apparent 0.26 % vs. 0.265 % discrepancy (nit)

- **ID:** PAPER-DEE-B5
- **Section:** Abstract; §4.2, Table 1, Table 7
- **Concrete issue:** The abstract (and Table 1) reports the uniform monopole as 0.4974 (0.26% deficit). The monopole‑mask null simulation uses `p_CW^global = 0.4974` in its caption but the “canonical‑N” calculation of σ uses `p_CW = 0.49735` (0.265% deficit). The two‑digit rounding is fine for narrative, but the 9.5 σ significance is derived from 0.49735, not 0.4974, and the null simulation’s input `p` is stated as 0.4974. If the null was actually run with 0.4974 instead of 0.49735, the pre‑MASTER C₁ null mean could shift at the 10⁻⁴ level—negligible, but a provenance stickler will ask which one was used.
- **Fix:** Use a single canonical value (0.497353, from the HuggingFace dataset card) in all numerical inputs, and round only for display. State that the null was seeded with the exact global monopole from the catalog.

---

## Finding 6 — The brick‑interior sample’s +2.32 σ at θ = 3.16° is declared a statistical fluctuation without reporting its own null variance (minor)

- **ID:** PAPER-DEE-B6
- **Section:** §4.7, brick‑boundary control sub‑paragraph
- **Concrete issue:** The paper explains the +2.32 σ as consistent with the √(50000/18024) ≈ 1.67× larger null variance of the smaller‑N interior sample, but does not tabulate the interior‑sample null σ to support that scaling. The reader must trust that the expected null power indeed scales as 1/√N_pairs, which holds for Poisson pairs but may be affected by the non‑uniform footprint. Providing the actual null σ from the brick‑interior run would close the loop.
- **Fix:** Include the null standard deviation at θ = 3.16° from the interior‑sample shuffle in the artifact’s readout, and add a one‑sentence statement: “The interior‑sample null σ at this bin is 0.0010 (or whatever), confirming the expected √N scaling.” No re‑analysis needed.
