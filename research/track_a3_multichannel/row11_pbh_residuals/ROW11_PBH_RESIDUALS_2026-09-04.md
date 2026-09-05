# Ledger row 11 — PBH channel residuals (items a, b)

Date: 2026-09-04 · Track A3 multichannel · status: IN PROGRESS

## Scope
- (a) Locate the Choudhury et al. 2025 sign disagreement on the compaction-function
  f_NL response operator-by-operator; settle whether negative local f_NL suppresses
  or enhances PBH abundance at fixed Gaussian amplitude; name the responsible term.
- (b) Extend the compaction γ_cr scan to [0.2, 1.0] and report
  A(-35/16)/A(-35/8) inside the in-lab shape's coverage γ_cr ∈ [0.267, 0.630];
  state whether "1.7-1.9" survives, changes, or is dropped.
- (c) second-order δN threading identity — NOT in this session's scope.

## Method
Small-f_NL analytic expansion of the compaction threshold + numerical check in
`row11_choudhury_sign.py`; independent γ_cr grid rerun in
`row11_gammacr_extension.py` (new outputs, committed outputs untouched).
No tuning: the amplitude solver targets a fixed reference abundance only.

## Verdicts
(filled in below as the work lands)
