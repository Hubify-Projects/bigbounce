# Truth-audit — P4 M26-EXT ChatGPT (RECOVERED orphan)

- **paper:** P4 (`pipelines/p2_chirality/chirality_catalog_paper.tex`), v1.0.239 (byte-unchanged)
- **reviewer/leg:** ChatGPT (Extended Thinking Pro), EXT
- **raw:** `M26/P4_chatgpt_M26.md` — verdict line 1: `VERDICT: REJECT` (11 MAJOR / 3 MINOR)
- **provenance:** leg orphaned by an ext_submit poll-timeout; landed server-side, recovered + harvested in commit 02d68a8f. Raw read verbatim. Chat URL `.../c/6a54ca46-…` reviews the DESI galaxy-chirality dipole catalog (Shamir, p_eq>0.6, A_ref=0.017) ✓ — correct paper.
- **method:** `tools/ledger_match.py P4` (12/17 auto-MATCHED) + full §3 Opus source-cited truth-audit vs the tex + `DISPOSITIONS/P4.md`.

## Verdict: 0 genuinely-new. Documented P4 ChatGPT REJECT↔MAJOR oscillation band on byte-unchanged v1.0.239.

| # | sev | finding | disposition |
|---|-----|---------|-------------|
| 1 | MAJOR | Headline null from p_eq>0.6 subset (949,584) not 8.5M / commit ≠ prereg | **DP4-07** (RE-FLAG; §prereg declares HC 0.6 a-priori; confidence-cut sweep stable; GZ1-human null) |
| 2 | MAJOR | TTA "collapse" 2.31σ→0.41σ confounded by catalog/selection/mask changes | **DP4-08/-07** (RE-FLAG; flip-TTA labeled flip-equivariance only, not rotation; 21.4% D4 = stability check) |
| 3 | MAJOR | Injection into hard-label map only; A50/A95 = detection efficiencies not physical | **DP4-09** (RE-FLAG; §sensitivity states injections bypass ViT/triage; g = disclosed bridge) |
| 4 | MAJOR | z≃−7.6 vs 1.7% dipole ≈1.4σ under g=0.398 dilution | **DP4-01/-14** (RE-FLAG; z is a template-disfavor statistic not detection significance; Shamir factor-2 CLOSED) |
| 5 | MAJOR | Coherent structures / 7–8σ MASTER / 47% residual "diagnostics" unproven non-cosmological | **DP4-17** (OPEN-COMPUTE; 47% disclosed, bounded a-fortiori below A50/A95) |
| 6 | MAJOR | Systematic dipole is a vector — can cancel a cosmological dipole | **DP4-16** (OPEN-COMPUTE; density-stratified null + block-bootstrap don't assume uniform dilution) |
| 7 | MAJOR | Pixel-permutation null assumes exchangeability across varying counts | **DP4-16** (OPEN-COMPUTE; exchangeability limits disclosed; primary rests on block-bootstrap + injection floor) |
| 8 | MAJOR | NSIDE=8 block bootstrap not a calibrated test of A=0.017 | **DP4-14** (RE-FLAG; "not a calibrated frequentist exclusion" stated verbatim §wls_fit footnote) |
| 9 | MAJOR | "joint nuisance-marginalized" fit omits PSF/depth/reddening templates | **DP4-17** (OPEN-COMPUTE; full joint likelihood is disclosed future work) |
| 10 | MAJOR | External validation 58.7%/69.91% not sub-percent spatial control | **DP4-15/-08** (OPEN-COMPUTE/RE-FLAG; spatially-resolved confusion needs image-level compute, disclosed) |
| 11 | MAJOR | 21.4% D4 argmax flips — not rotation invariant | **DP4-08** (RE-FLAG; flip-equivariance-only + 21.4% stability check disclosed) |
| — | MAJOR | +3.64σ (p=0.030) vs +7.93σ (p=3e-4) "recomputation" changes | **DP4-10** (RE-FLAG; empirical-null rank fractions; declared different estimators/nulls) |
| 12 | MINOR | Recovery curve 100 injections / coarse grid | **DP4-09** (RE-FLAG; N_inj=100/0.5% grid disclosed future work L1091) |
| 13 | MINOR | Amplitude conventions inconsistent / ECE Jensen bound / DOI mutable | **DP4-13/-08/-21** (RE-FLAG; σ reader's note + ECE Jensen L1345 + DOI Houston-gated at submission) |
| 14 | MINOR | Birefringence/Chern–Simons model-specific claims | **DP4-12** (RE-FLAG; §parity_translation states transfer function "not derived in this paper") |

**ledger_match UNMATCHED (5):** #2/#6/#13/#14/#15 below the lexical threshold (re-worded); each Opus-adjudicated to the D-ids above (same structure as the W1-EXT / M5-EXT ChatGPT REJECTs).

## Result
0 genuinely-new editable findings; every MAJOR is a source-cited re-flag (RE-FLAG-DISCLOSED / OPEN-COMPUTE / definitional). Grok half already counted M26-EXT → **clean-wave streak HOLDS 10**. **Cap 80→74:** the recovered ChatGPT is a REJECT (contributes 0), replacing the prior M25-era MAJOR-carry (6): Grok minor 12 + ChatGPT reject 0 + Gemini minor 12 = 50+24 = 74 (honest formula tracks the latest-per-reviewer verdict word). No bump (byte-unchanged v1.0.239). directive_g.sh not run. Integrity: raw read verbatim; no ACCEPT faked; no un-sourced dismissal; no fabrication.
