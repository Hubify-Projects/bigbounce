# A3-3 — Scalar-induced GWs at nHz from the lab's own curvature spectrum

**Date:** 2026-09-04 · **Ledger:** `NEXT_SCIENCE_LEDGER.md` row 3 (A3-3)
· **Audit item:** `DA3M-R4-02` (MAJOR, SCIENCE) in
`project-context/peer-reviews/INT_v3/A3M_v3M.0.9_R4_TRUTH_AUDIT_2026-09-04.md`
· **Script:** `sigw_nhz_from_lab_spectrum_2026_09_04.py` (to be committed with outputs)

## Plan (header committed before the computation; results appended below)

1. Derive f ↔ k for a mode re-entering in radiation domination; evaluate over the
   NANOGrav band f ∈ [2, 60] nHz.
2. Evaluate the lab's Δ²_ζ(k) (A_s = 2.1e−9, k_* = 0.05 Mpc⁻¹, n_s = 0.9649; plus the
   pure-dust n_s = 1 bracket) at those k, with the A2 scale-independent bounce transfer;
   report kη_B at nHz for each committed background/T_B to test the transfer's
   kη_B ≲ 1e−2 validity domain.
3. Compute Ω_GW(f) with the Kohri–Terada (arXiv:1804.08577) radiation-era kernel,
   numerically integrated over the broad spectrum; fit the local slope across the band
   → γ_pred via Ω_GW ∝ f^{5−γ}; compare amplitude to NANOGrav 15 yr.
4. Determine what nHz spectral shape would give γ=3 (P_R ∝ k), the k_B / T_B / H_B it
   would require, and compare with §V's T_B ≳ 1e8–1e10 GeV.
5. VERDICT (A) null/tension, or (B) a consistent γ=3 statement under stated assumptions.

**Integrity:** no tuning toward γ=3; every number emitted by the committed script.
