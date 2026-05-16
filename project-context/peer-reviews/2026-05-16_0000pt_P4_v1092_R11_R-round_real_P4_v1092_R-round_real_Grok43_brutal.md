# P4_v1092 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0000pt_P4_v1092_R11_R-round_real
**Wall time**: 32.5s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=72988, completion=3585, reasoning=2691, total=76573

---

**PAPER-GRO-B1**  
**Classification:** BLOCKER  
**Location:** Abstract (lines ~40-55) and Sec. \ref{sec:monopole_mask_null} (Table \ref{tab:monopole_mask_null} and surrounding text)  
**Issue:** The statement that the monopole-only null "reproduces 99.3% of the observed pre-MASTER pseudo-C_ℓ power" and thereby "explains" prior literature claims at the percent level is false confidence; this holds only under the present ViT-Small pipeline on DESI Legacy data, with no matched reanalysis of Shamir's Ganalyzer on the identical footprint, selection, or magnitude cuts.  
**Fix:** Replace the explanatory sentence with: "This demonstrates a quantifiable leakage channel under the present pipeline; a like-for-like reanalysis under Shamir's exact Ganalyzer pipeline on this footprint is required to determine what fraction of any specific prior detection it accounts for."

**PAPER-GRO-B2**  
**Classification:** BLOCKER  
**Location:** Table \ref{tab:face_on} (the +4.31σ row) and the "Reconciliation with the headline +0.43σ" paragraph in Sec. \ref{sec:signal_hunt}  
**Issue:** The +4.31σ (monopole-preserving null) for full Catalog C versus the headline +0.43σ (per-pixel shuffle) real-space dipole are presented as reconciled in a footnote, but the main prose does not explicitly state these are different estimators with different null constructions on the same data, creating the appearance of contradictory results that a referee will flag.  
**Fix:** Insert one sentence immediately after the table: "The +4.31σ value is a weighted least-squares fit under a monopole-preserving null; the headline 0.43σ is a Healpix dipole fit under per-pixel shuffle. Both are consistent with no directional dipole beyond the uniform monopole."

**PAPER-GRO-B3**  
**Classification:** MAJOR  
**Location:** Abstract (sensitivity paragraph) and Sec. \ref{sec:sensitivity} (Fisher vs. empirical discussion)  
**Issue:** The load-bearing sensitivity is framed as the empirical 0.75% 50%-rec-3σ threshold, yet the paper never demonstrates that the 9.5σ residual monopole has zero dipole projection on the DESI footprint; without the PSF/ellipticity cross-power test completed and shown to be null at ℓ=1, the effective sensitivity to a true dipole is not established at the claimed level.  
**Fix:** Add a one-sentence limitation: "The 0.75% empirical threshold assumes the residual monopole has no dipole projection; the pending PSF cross-correlation test (currently |z|≤2.73 at ℓ=2-64) is required to confirm this."

**PAPER-GRO-B4**  
**Classification:** MAJOR  
**Location:** Abstract (first paragraph) and Sec. \ref{sec:intro} (Shamir comparison)  
**Issue:** The central claim is presented as identifying a "real, quantifiable systematic-failure mode that prior literature did not subtract," but this is not new: Iye et al. (2021) and Tadaki et al. (2020) already reported nulls after bias correction on smaller samples; the present work's contribution is incremental sample size and one additional leakage diagnostic, not a resolution of the controversy.  
**Fix:** Change the abstract sentence to: "This work provides a larger-sample null with explicit leakage-channel quantification under one pipeline, consistent with prior null results from Iye et al. and Tadaki et al."

**PAPER-GRO-B5**  
**Classification:** minor  
**Location:** Sec. \ref{sec:tta} (TTA discussion) and multiple bias-audit sites  
**Issue:** Residual language still implies TTA "cancels by construction" at the ensemble level while acknowledging the 9.5σ monopole survives; the softening from R10 is incomplete and leaves a reviewer hook.  
**Fix:** Replace remaining "by construction" phrasing with "at the ensemble-mean level only; per-galaxy argmax labels retain ~21% rotational uncertainty."

No sixth finding reaches even minor grade. The paper is otherwise reproducible and scoped, but the above five items are the load-bearing problems that must be closed before external review.
