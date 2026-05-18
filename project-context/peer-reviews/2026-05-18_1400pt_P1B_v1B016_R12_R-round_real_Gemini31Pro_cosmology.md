# P1B_v1B016_R12 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1400pt
**Wall time**: 46.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=18741, completion=6826, reasoning=6141, total=25567

---

## PAPER-GEM-M1: Stale Savage-Dickey Claim in Appendix B
**Classification:** MAJOR
**Location:** Appendix B, Table 3 (Claims Classification)
**Issue:** The R11 closure successfully purged the KDE-based Savage-Dickey plan from the 4 main text sites because the LCDM point is unsampled in the Metropolis-Hastings tails. However, a 5th site was missed: Table 3 still explicitly lists "v1B.0.13+ Savage-Dickey" as the status for the $\ln B$ model comparison, contradicting the core R11 nested-sampling closure.
**Fix:** Change "v1B.0.13+ Savage-Dickey" to "v1B.0.17+ Nested Sampling" (or similar) in Table 3.

## PAPER-GEM-M2: Cobaya Termination State Contradiction
**Classification:** MAJOR
**Location:** Section 8 (Conclusions), "Forward" paragraph
**Issue:** The text claims "The 16-rank mpirun process remains alive on the pod" for the iter2 chain. This contradicts the "CONVERGED" state reported in Tables 1B and 2 ($\hat R - 1 = 0.00820 < 0.01$); standard Cobaya behavior automatically terminates the MPI process once the `Rminus1_stop` threshold is crossed. 
**Fix:** Remove the "remains alive" claim and explicitly state the chain has terminated upon successfully reaching the convergence threshold.

## PAPER-GEM-m3: Stale Version in Cross-Paper Status Table
**Classification:** minor
**Location:** Section 7, Table 4
**Issue:** The cross-paper status table lists P1(b) at version "v1B.0.13", but the current manuscript is v1B.0.16.
**Fix:** Update the P1(b) row in Table 4 to reflect "v1B.0.16".

## PAPER-GEM-m4: Parameter Nomenclature Typo in Table 1B
**Classification:** minor
**Location:** Table 1B caption
**Issue:** The sampled parameter list in the caption includes "$w$", but the standard nomenclature correctly used in the table rows and surrounding text is "$w_0$".
**Fix:** Change "$w$" to "$w_0$" in the Table 1B caption parameter list.

## PAPER-GEM-m5: Inconsistent Nested-Sampling Deferral Targets
**Classification:** minor
**Location:** Sections 3, 5.2, 7.1, and Appendix A
**Issue:** The nested-sampling $\ln B$ run is cited as "queued for v1B.0.15+" in Sec 3, Sec 5.2, and App A, but is cited as "queued for v1B.0.16+" in Sec 7.1. Since the current document is already v1B.0.16, both targets are stale and internally inconsistent.
**Fix:** Unify the deferral target to "v1B.0.17+" across all instances.
