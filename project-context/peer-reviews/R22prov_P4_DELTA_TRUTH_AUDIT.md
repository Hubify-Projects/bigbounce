# P4 R22prov — DELTA truth audit (findings NOT already in R-v166-c1 disposition)

**Context:** Two independent 5-vendor rounds ran on v1.0.166 within hours
(autoloop R-v166-c1 + main-session R22prov). R22prov confirms the R-v166-c1
consensus set and adds the deltas below. These fold into the v1.0.167 wave as
a DELTA PASS after the main closure agent lands, plus 4 compute items → pod
batch C9. Verdicts per /peer-review-truth-audit.

| # | Finding (vendor) | Verdict | Fix class |
|---|---|---|---|
| D1 | χ²=161.2/38 bandpowers: provenance of 38 not shown (META-M5) | VERIFIED | List binning scheme + ℓ-ranges in App A or move χ² out of Table III |
| D2 | No shot-noise (N_ℓ) debias; absolute C_ℓ amplitudes not interpretable as debiased (META-M7) | VERIFIED (design) | Caveat sentence: amplitudes are raw (not noise-debiased); significances are null-relative. Full N_ℓ estimate → C9 |
| D3 | ℓ=1 +7.28σ vs App D σ_ℓ=1=+3.63; ℓ=2 +4.73 vs +6.10 — same-name different-estimator collisions (OpenAI E8/m7) | VERIFIED | Unique estimator names + one comparison table (extends C6/C13) |
| D4 | +7.28σ quoted from N_MC=500 → σ of the σ ≈6%; rank-p floor is 1/501 (OpenAI E5) | VERIFIED | Quote empirical rank p≤0.002 alongside; exact σ from C9 10k-perm run |
| D5 | Table III (×10⁻⁶ sr) vs Table IV (1.696×10⁻², no units) scale mismatch (OpenAI E9) | VERIFIED | State Table IV units + reconcile normalization conventions |
| D6 | fsky drift 0.49005/0.491/0.494 + mask threshold drift >10 vs ≥5 (OpenAI M5, META-M9) | VERIFIED | Merges into C8 + S6 frozen-mask table — verify agent covered all sites |
| D7 | LEE double-counting: direct max-stat MC already includes look-elsewhere; Bonferroni/BH on top is a second penalty; also 3.05σ vs z=+4.42 unreconciled (META-E3, META-m11) | VERIFIED — NOTE: partially CONFLICTS with R-v166-c1 C9. Resolution (full-delegation): max-stat MC p_LEE is the principled primary; BH/Bonferroni demoted to "additional conservative cross-check"; label 3.05σ vs +4.42 as distinct estimators in one place | Delta text fix |
| D8 | p=0.030 → "≈1.9σ" is one-sided; two-sided ≈2.17σ; sidedness unstated (META-M10) | VERIFIED | State one-sided explicitly at every mapping site |
| D9 | Bootstrap N behind p=0.30 not stated for the headline dipole (Grok E4) | VERIFIED | Specify N + sidedness (extends C11) |
| D10 | Fisher floor: σ_A=2σ(f)=0.0558%, not 0.048% (Grok M4) | VERIFIED — cross-check for S5 derivation | Confirm agent's S5 result matches 0.0558%-based arithmetic |
| D11 | "C² 2° apodization" undefined (META-m13) | VERIFIED | Define: NaMaster C2 cosine-squared roll-off, 2° apodization scale |
| D12 | Release tag future-stamped; no DOI (META-m14) | VERIFIED | Cite commit hash + queue Zenodo DOI |
| D13 | A50/A95 from HC-subsample injections under pp-shuffle null used to frame full-catalog falsification (META-M4) | VERIFIED | Caveat sentence (extends C10) |
| D14 | Depth-stratified null preserves marginal depth only — possibly anti-conservative for leg-coherent systematics (META-m15) | VERIFIED (caveat) | One-sentence scope note on C6/C9-family nulls |
| D15 | WLS collinearity handling unreported (META-m12) | VERIFIED — implementation used SVD pinv (joint_nuisance scripts) | Document SVD pinv + condition handling in App D.f |
| D16 | Abstract should state raw 2.31σ → 0.43σ post-TTA lineage (Grok E3) | VERIFIED | Fold into C7 abstract (one clause) |
| D17 | "Dated: June 2026" flagged as future placeholder (Gemini E1, Grok N1/N4) | **FALSIFIED** — June 2026 is the actual current date; reviewer training-cutoff artifact | No action |
| D18 | Condense to ≤10pp (Grok M1) | OPINION — matches C18 disposition | No additional action |

## Compute items → pod batch C9 (extends META-M3/M5/M6)

- C9a: 10k-permutation MASTER nulls (apodized Wp=N_all + canonical) → exact
  Table III bandpower null means (closes C4), tight rank-p for +7.28σ (D4),
  χ² bandpower provenance (D1)
- C9b: injection-recovery completeness through the apodized-footprint MASTER
  channel at A ∈ {0.5%, 0.75%, 1.7%, 3%}, ≥1k inj/amplitude (META-M5, Grok-M2,
  C10 recovery curve, D13)
- C9c: W_p sweep {N_spiral, N_all, uniform} (META-M6)
- C9d: per-null shuffle-pool verification — code inspection + assert (META-M3)
- C9e: shot-noise N_ℓ estimate for the A_p auto-spectrum (D2)
