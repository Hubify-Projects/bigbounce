# Truth Audit — CN1 Wave — P2 v1.7.114 → v1.7.115
**Date:** 2026-07-12
**Paper:** P2 (Channel-Native f_NL Forecast)
**Versions:** v1.7.114 → v1.7.115
**Wave:** CN1

---

## Verdict Matrix

| Reviewer | Type | Verdict | Engaged new c15 content? |
|----------|------|---------|--------------------------|
| Claude (sub-agent, CN1r) | INT | MAJOR | YES — caught GR M123 metric mismatch |
| OpenAI | INT | REJECT | No |
| Grok (INT) | INT | MAJOR | No |
| Gemini | INT | REJECT | No |
| Grok | EXT | MINOR-REVISIONS | No — re-flagged old DP2 classes |
| ChatGPT | EXT | REJECT | No — re-flagged old DP2 classes |

---

## EXT Grok — Ledger Match Table

| # | Grok finding | Disposition | D-id |
|---|-------------|-------------|------|
| 1 | Fisher matrix formalism scope / galaxy catalog | Source-cited re-flag | DP2-13 |
| 2 | f_NL primordial definition / scale dependence | Source-cited re-flag | DP2-01 |
| 3 | Transfer function approximation | Source-cited re-flag | DP2-14 |
| 4 | Forecasting assumptions / survey specs | Source-cited re-flag | DP2-18 |
| 5 | GR projection proxy validation | Source-cited re-flag | DP2-34 |

All 5 Grok findings: SOURCE-CITED RE-FLAGS of pre-existing DP2 ledger entries. 0 genuinely-new.

---

## EXT ChatGPT — Ledger Match Table

| # | ChatGPT finding | Disposition | D-id |
|---|----------------|-------------|------|
| 1 | Primordial non-Gaussianity definition | Source-cited re-flag | DP2-01 |
| 2 | Scale-dependent bias derivation | Source-cited re-flag | DP2-15 |
| 3 | Fisher matrix assumptions | Source-cited re-flag | DP2-02 |
| 4 | Transfer function limitations | Source-cited re-flag | DP2-14 |
| 5 | Survey parameter assumptions | Source-cited re-flag | DP2-14 |
| 6 | Signal-to-noise claim | Source-cited re-flag | DP2-22 |
| 7 | Galaxy bias model | Source-cited re-flag | DP2-13 |
| 8 | Radial mode binning | Source-cited re-flag | DP2-19 |
| 9 | Covariance matrix approximation | Source-cited re-flag | DP2-19 |
| 10 | GR projection template validation | Source-cited re-flag | DP2-34 |
| 11 | Forecasting methodology scope | Source-cited re-flag | DP2-18 |
| 12 | Prior assumptions on b_phi | Source-cited re-flag | DP2-04 |
| 13 | Comparison to DESI constraints | Source-cited re-flag | DP2-16 |
| 14 | Transfer function pipeline | Source-cited re-flag | DP2-14 |

All 14 ChatGPT findings: SOURCE-CITED RE-FLAGS of pre-existing DP2 ledger entries. 0 genuinely-new.

---

## INT-Claude (CN1r) per-finding disposition

**Genuinely-new editable (1):**
- DP2-CN1-01: c15 channel-native Fisher — GR-projection template S_GR (`gr_reduced`) was built in **potential space** (bare P_phi legs, NO M123 transfer), while the f_NL primordial leg correctly carries M123 (density space). This made the A_GR Fisher weight vacuous: F_22≈2.8e-18 vs F_00≈2.5. The claimed ρ(f_NL,A_GR)≈−0.001 "near-orthogonal" result was a normalization artifact.

  **Fix applied:** S_GR promoted to density space (×M123); script re-run.
  
  **Corrected results:**
  - ρ(f_NL,A_GR) = **−0.42 (2×2) / −0.49 (3×3)** — moderately correlated, NOT orthogonal
  - b_φ-30%-prior σ_marg = **0.94 → 2.32σ**
  - "Both proxies overstated GR loss / closes DP2" claim **removed** (was the bug)
  
  **What still holds:**
  - Channel-native floor 2.32σ **still > retained conservative proxy floor 1.30σ** — conclusion survives
  - Cross-Fisher α=0.992 unchanged
  - −35/16 unchanged
  - Nothing fabricated

  **Status: CLOSED v1.7.115.**

---

## CRITICAL Adjudication: Did reviewers engage the NEW content?

**New c15 channel-native Fisher section — introduced in v1.7.114 → v1.7.115:**
- INT-Claude (CN1r): YES — read the c15 Fisher implementation, caught the S_GR potential-vs-density mismatch.
- OpenAI (INT): No evidence of engagement with new c15 content.
- Grok (INT): No evidence of engagement with new c15 content (MAJOR verdict based on pre-existing concerns).
- Gemini (INT): No evidence of engagement with new c15 content.
- Grok (EXT): NO — 5 findings all map to pre-existing DP2 classes.
- ChatGPT (EXT): NO — 14 findings all map to pre-existing DP2 classes.

**Trend evidence:** Consistent with P1U NJ1 wave: EXT (and most INT) reviewers did not engage new technical content introduced in this version. Only INT-Claude (running as a Claude Code sub-agent with full repo + context access) caught the metric-mismatch defect. This supports the value of INT-Claude as a complement to EXT reviewers for catching new errors in revised content.

---

## Honest Conclusion

- **Genuinely-new editable findings this wave:** 1 (c15 GR M123 metric mismatch)
- **Status:** CLOSED in v1.7.115
- **Streak:** RESET to 0 (directive-K: genuinely-new finding surfaced)
- **Readiness cap:** 74 (unchanged — EXT-formula)

**Integrity check:**
- No faked ACCEPT recorded.
- No finding dismissed without source-cited D-id.
- No fabrication: the corrected ρ=−0.42 values came from the re-run script with the fix applied; the prior ρ≈−0.001 was a confirmed artifact.
- INT-Claude was the only reviewer to engage the new c15 content — noted transparently.
- Conclusion validity: channel-native floor 2.32σ > proxy 1.30σ survives the fix independently of the now-removed "orthogonality" claim.
