# P4_v1101 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0400pt_P4_v1101_R19_R-round_real
**Wall time**: 102.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=83641, completion=10511, reasoning=9606, total=94152

---

## PAPER-GEM-M1
**Classification:** MAJOR
**Location:** Section 6.8, "For a parity-odd scalar field on the sphere ($A(\hat n) \equiv -A(-\hat n)$, which is the symmetry behavior of the projected CW-fraction asymmetry..."
**Issue:** The text conflates the parity transformation operator $P$ with the antipodal map on the sphere. Writing $A(\hat n) \equiv -A(-\hat n)$ defines a field that is identically antisymmetric across the sky (which would mean the universe has a maximal dipole by definition). The correct statement is that under a parity transformation, the *transformed* field relates to the original field via $A^P(\hat n) = -A(-\hat n)$.
**Fix:** Change to "For a pseudoscalar field on the sphere, the parity-transformed field is $A^P(\hat n) = -A(-\hat n)$."

## PAPER-GEM-M2
**Classification:** MAJOR
**Location:** Section 4.6, "The $w_{\rm CW}(\theta)$ result is a fourth complementary diagnostic... consistent with the chirality field carrying no primordial parity-violating signal"
**Issue:** The 2-point correlation function of a pseudoscalar field, $\langle A(\hat{n}_1) A(\hat{n}_2) \rangle$, is parity-even (the two minus signs cancel under parity transformation). A non-zero $w_{\rm CW}(\theta)$ would detect spin-spin clustering (intrinsic alignments)—a standard parity-conserving prediction of $\Lambda$CDM tidal torque theory—not parity violation.
**Fix:** Clarify that $w_{\rm CW}(\theta)$ is a parity-even observable that bounds standard spin-spin intrinsic alignments, and remove the claim that it directly tests for a "parity-violating signal".

## PAPER-GEM-m3
**Classification:** minor
**Location:** Section 6.8, "(dim-7 operators in the EFT, parameterized by $g_*$ in their notation)"
**Issue:** This parenthetical immediately follows "EFT-of-LSS framework", implying $g_*$ is an EFT of LSS operator. Cabass et al. use the EFT of LSS to model late-time transport, but the dimension-7 parity-odd operators parameterized by $g_*$ belong to the primordial EFT of Inflation. 
**Fix:** Change to "(dimension-7 operators in the EFT of Inflation, parameterized by $g_*$)".

## PAPER-GEM-m4
**Classification:** minor
**Location:** Section 6.1 (Discussion of $A_p$ normalization)
**Issue:** The paper correctly notes that $A_p$ normalizes out $N_{\rm spiral}$ density correlations, but misses a massive theoretical physics consequence: because $A_p$ is a dimensionless ratio of counts in the same pixel, the $O(10^{-3})$ kinematic Doppler aberration and magnification bias effects (which severely contaminate standard number-count dipoles like NVSS/WISE) cancel out exactly to leading order. 
**Fix:** Add a sentence noting that the dimensionless ratio $A_p$ cancels leading-order GR kinematic and projection effects (aberration, magnification bias), making the chirality dipole theoretically cleaner than number-count dipoles.

## PAPER-GEM-n5
**Classification:** nit
**Location:** Table III caption, "anchors the dipole-parity null"
**Issue:** Section 6.8 correctly establishes that the dipole of a pseudoscalar field is parity-even, making this an isotropy test. Calling it a "dipole-parity null" contradicts the paper's own careful symmetry classification.
**Fix:** Change "dipole-parity null" to "dipole-isotropy null".

---
**Bottom-line for Houston external review:** 
The v1.0.101 closures hold perfectly (the GZ1 dilution arithmetic and 1-dof $\chi^2$ fixes are mathematically sound). The pure propagation tail of pipeline bugs is genuinely exhausted. The remaining findings above are localized theoretical-physics precision corrections (EFT boundaries, symmetry definitions) rather than data-pipeline failures. Once these text fixes are applied, the manuscript is fully ready for external journal submission.
