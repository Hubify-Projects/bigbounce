# P4_v1090 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2300pt_P4_v1090_R9_R-round_real
**Wall time**: 126.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=80529, completion=14674, reasoning=13118, total=95203

---

## PAPER-GEM-B1: Physics Contradiction on Polar vs Axial Vector
**Classification:** MAJOR
**Location:** Sec VI.G (Parity-odd galaxy-trispectrum amplitude)
**Issue:** The text explicitly calls the chirality dipole a "preferred polar-vector direction on the sky" to argue it tests isotropy rather than parity, but in the very next sentence clarifies that "the dipole vector itself is an axial vector, not a polar vector". A dipole of a pseudoscalar field (like chirality) is a pseudovector (axial vector), making the first sentence a direct physics contradiction.

*   **Cite:** Sec VI.G
*   **Paper-says:** "A nonzero chirality dipole therefore strictly tests \emph{isotropy} (the existence of a preferred polar-vector direction on the sky)... the dipole vector itself is an axial vector, not a polar vector"
*   **Artifact-says:** N/A (Theoretical physics definition)
*   **Verdict:** NOVEL
*   **Fix:** Change "preferred polar-vector direction on the sky" to "preferred axial-vector direction on the sky".

## PAPER-GEM-B2: Sensitivity Overclaim Regression (0.5% Floor)
**Classification:** BLOCKER
**Location:** Sec VI.B and Sec VII
**Issue:** The prompt explicitly notes that the 0.5% empirical floor was supposed to be migrated to 0.75% everywhere because 0.5% is a non-detection point. However, the text still claims 0.5% as the empirical detection threshold/floor in two concluding sections.

*   **Cite:** Sec VI.B and Sec VII
*   **Paper-says:** "below the empirical detection threshold $|A_{\rm dipole}|>0.5\%$" (Sec VI.B) and "above the empirical sensitivity floor $|A_{\rm dipole}|>0.5\%$" (Sec VII).
*   **Artifact-says:** `injection_recovery_extended.json` reports P(sigma>3)=0.15 at A=0.50% (non-detection).
*   **Verdict:** REGRESSION / STILL-UNRESOLVED
*   **Fix:** Update the remaining "0.5%" empirical threshold references in Sec VI.B and Sec VII to "0.75%".

## PAPER-GEM-B3: Sample Size Definition Contradiction (N=949,584)
**Classification:** BLOCKER
**Location:** Sec IV.J, Sec VI.D, Table V, Table VIII
**Issue:** The definition and galaxy count of the N=949,584 subsample is mathematically contradictory across sections. Sec IV.J defines it as "HC-broad... counts confident-NS galaxies", which would be ~5 million galaxies (62% of 8.47M), not 949k. Sec VI.D and Table VIII define it as "HC-spiral ($p_{\rm eq}>0.6$)", but Table V's sum of spirals with max probability >0.6 is 944,826. 949,584 cannot simultaneously be the broad cut including NS, the spiral-only cut, and contradict the Table V sum.

*   **Cite:** Sec IV.J, Sec VI.D, Table V, Table VIII
*   **Paper-says:** "HC-broad cut ($\max(p_{\rm CW,eq}, p_{\rm CCW,eq}, p_{\rm NS,eq}) > 0.6$, N = 949,584)... which counts confident-NS galaxies" vs "HC-spiral ($p_{\rm eq}>0.6$) | 949,584"
*   **Artifact-says:** N/A (Internal text contradiction)
*   **Verdict:** NOVEL
*   **Fix:** Reconcile the 949,584 count. If it is the count of spirals with $\max(p_{CW}, p_{CCW}) > 0.6$, correct Sec IV.J to remove the "counts confident-NS galaxies" claim and fix the Table V binning discrepancy.

## PAPER-GEM-B4: Physics Error on Power Spectrum Parity
**Classification:** MAJOR
**Location:** Sec VI.G (Symmetry classification)
**Issue:** The text claims "the even-$\ell$ pseudo-$C_\ell=|a_{\ell m}|^2$ bandpowers... are anisotropy and systematics diagnostics rather than direct parity-odd tests". Specifying "even-$\ell$" implies odd-$\ell$ $C_\ell$ are parity-odd. In reality, $|a_{\ell m}|^2$ is parity-even for ALL $\ell$ because the modulus squared discards the sign flip $a_{\ell m} \to (-1)^{\ell+1} a_{\ell m}$. The auto-power spectrum of a single field cannot test parity violation.

*   **Cite:** Sec VI.G
*   **Paper-says:** "the even-$\ell$ pseudo-$C_\ell=|a_{\ell m}|^2$ bandpowers reported throughout this work are anisotropy and systematics diagnostics rather than direct parity-odd tests"
*   **Artifact-says:** N/A (Theoretical physics definition)
*   **Verdict:** NOVEL
*   **Fix:** Change "the even-$\ell$ pseudo-$C_\ell=|a_{\ell m}|^2$ bandpowers" to "the pseudo-$C_\ell=|a_{\ell m}|^2$ bandpowers at all $\ell$".

## PAPER-GEM-B5: Epistemological Overclaim ("rules out")
**Classification:** minor
**Location:** Sec IV.E (Signal-Hunt Diagnostics)
**Issue:** The text uses overly definitive language for a methods paper when interpreting the non-monotonic behavior across confidence bins, claiming it "rules out" a primordial dipole.

*   **Cite:** Sec IV.E
*   **Paper-says:** "rules out the primordial-dipole interpretation by behavior alone"
*   **Artifact-says:** N/A (Tone/Epistemology)
*   **Verdict:** STILL-UNRESOLVED
*   **Fix:** Soften "rules out" to "strongly disfavors" or "is inconsistent with".

## PAPER-GEM-B6: Theoretical Physics/EFT Scope Boundary
**Classification:** minor
**Location:** Sec VI.G (Parity-odd galaxy-trispectrum amplitude)
**Issue:** When contrasting the chirality dipole with the parity-odd 4PCF (which maps to a scalar EFT amplitude $g_*$), the text states the dipole "would require a background vector or tensor source rather than a scalar EFT operator." While true, it should explicitly clarify that this means it cannot be generated by the standard scalar parity-odd EFT of LSS without introducing new degrees of freedom.

*   **Cite:** Sec VI.G
*   **Paper-says:** "which would require a background vector or tensor source rather than a scalar EFT operator."
*   **Artifact-says:** N/A (Physics context)
*   **Verdict:** NOVEL
*   **Fix:** Append "in the standard EFT of LSS" to clarify the scope boundary.
