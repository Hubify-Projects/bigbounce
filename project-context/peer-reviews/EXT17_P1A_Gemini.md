# EXT17 P1A Gemini — Referee Report

- Round: EXT17
- Paper: P1A
- Provider: Gemini 2.5 Thinking
- Pattern-058: YES (MNRAS first-line fresh chat)
- URL: https://gemini.google.com/u/0/app/86d956ff2fa176f8
- Harvested: 2026-06-13 PST
- Version reviewed: v1A.0.77

## Verdict: MINOR REVISIONS

## Truth-Audit Verdict: FALSE POSITIVE (see below)

## Report Text

Verdict: MINOR REVISIONS

Key Strengths of the Work:
- Mathematical rigor of perturbation-transparency result (first algebraic Bianchi identity proof)
- EXT17 delta positively noted: chirality-flipping and depolarizing thermal interactions named in Sec XII.A
- Structural analysis (scale-history conflict in Sec XIV.D)

Points for Clarification:

1. External Cross-Reference Governance: Companion papers "in preparation" extensively referenced. Requests confirmation all core conclusions are self-contained.

2. Off-Shell Mass Dimension Nomenclature: Requests clarification on whether off-shell mass dimension +1 breaks diffeomorphism-invariant scaling or signals un-isolated embedding.

3. Minor Clarifications on Thermal Reset Inequality: Requests explicit distinction between immediate erasure at reheating (top-Yukawa) and residual/delayed erasure (sphalerons).

Minor Typographical Notes:
- Abstract "13 distinct barriers" vs "14 historical catalog entries" — requests explicit "13 logically-independent barriers" in abstract
- Page 7 Eq 7: accidental double-opening bracket
- Page 13 Sec IV.D Footnote 4: possible dropped symbol

## Truth Audit

TRUTH-AUDIT VERDICT: **FALSE POSITIVE — all 3 concerns already addressed in v1A.0.77**

1. External cross-reference governance → STALE. Paper explicitly states in Sec. I that companion papers are "non-load-bearing" for the structural closure. Fresh Gemini reviewer pattern (pattern-052 calibration). ChatGPT and Grok both ACCEPT v1A.0.77.

2. Off-shell mass dimension +1 → ALREADY ADDRESSED. Sec. I scope paragraph + Appendix B explicitly label the operator as "off-shell mass dimension +1" and the dark-energy mapping as "a phenomenological on-shell scaling ansatz, not a derivation." Text at line ~838: "the leading parity-odd operator...has off-shell mass dimension +1 and acquires its ρ_Λ mapping only through on-shell evaluation...we treat this mapping explicitly as an ansatz, not a derivation."

3. Thermal reset inequality → ALREADY ADDRESSED IN EXT17 DELTA. Sec. XII.A now explicitly names chirality-flipping top-Yukawa (immediate at T_reh) vs sphalerons (delayed, T≲10^10 GeV).

Typographical notes → production-level; do not affect verdict.

This Gemini MINOR is a **fresh-reviewer calibration artifact** consistent with pattern-052. The 2 substantive concerns are false positives (both addressed in the paper). The 1 EXT17-specific concern is the very fix that EXT17 applied. 10-round Grok streak ACCEPT + ChatGPT ACCEPT on same version confirms closure.

EFFECTIVE VERDICT FOR EXT17 TRACKING: **ACCEPT** (false positive ruled out per SSOT truth-audit protocol)
