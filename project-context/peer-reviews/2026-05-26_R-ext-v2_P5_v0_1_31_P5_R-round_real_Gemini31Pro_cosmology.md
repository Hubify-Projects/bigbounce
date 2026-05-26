# P5 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v2_P5_v0_1_31
**Wall time**: 35.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=26849, completion=2862, reasoning=2081, total=29711

---

## PAPER-GEM-M1: MAJOR
**Section:** X.B (Bounce vs. inflation discrimination) and Bibliography
**Issue:** The paper discusses "primordial parity-violating scenarios," "matter-bounce," and "inflation-class models" without citing a single theoretical paper on parity violation. The bibliography is entirely observational/methodological. Claims about constraining parity-violating physics are unmoored from the standard literature (e.g., Chern-Simons gravity, ALPs, or recent LSS parity anomaly papers).
**Fix:** Add citations to standard theoretical reviews and foundational papers on parity-violating inflation/bounce models and LSS angular momentum generation (e.g., Alexander & Yunes 2009, Kamionkowski & Palmer 2014, or recent Philcox/Hou LSS parity works) to ground the theoretical claims.

## PAPER-GEM-M2: MAJOR
**Section:** XI (Limitations)
**Issue:** The paper tests 2D projected chirality against 3D environment but ignores physical-frame projection effects. Tidal Torque Theory (TTT) explicitly predicts environment-dependent 3D spin alignments; projecting this to 2D can create a spurious CW/CCW imbalance if the survey selection function couples to galaxy inclination or weak lensing shear/magnification alters the observed morphology.
**Fix:** Explicitly address Tidal Torque Theory (TTT) and GR projection effects (lensing/magnification) in Section XI as physical mechanisms that couple 3D environment to 2D observed chirality, noting that the null result bounds these effects at the survey limit.

## PAPER-GEM-m1: minor
**Section:** X.B (Bounce vs. inflation discrimination)
**Issue:** Model-class scope boundary error. The text frames environmental chirality as a potential "bounce vs. inflation discriminator." However, parity-violating sectors (e.g., $f(\phi) F \tilde{F}$ or Chern-Simons) that would source such a signal can be embedded in *both* paradigms; the signal constrains the parity-violating sector, not the kinematic background (bounce vs. expansion).
**Fix:** Remove the claim that environmental chirality discriminates between bounce and inflation; reframe it strictly as a constraint on parity-violating sectors regardless of the background cosmology.

## PAPER-GEM-m2: minor
**Section:** XI (Limitations) and VII (Phase 2 sensitivity sweep)
**Issue:** Section XI claims RSD displacement ($\sim 5-8$ Mpc/$h$) is safely smaller than the $R_s = 25$ Mpc/$h$ smoothing scale. However, the Phase 2 sweep (Table V) tests $R_s = 10$ Mpc/$h$, where the Kaiser/FoG displacement is of order the smoothing scale, meaning the $R_s = 10$ cell is highly sensitive to RSD boundary-crossing artifacts.
**Fix:** Acknowledge in Section VII or XI that the $R_s = 10$ Mpc/$h$ Phase 2 cell is marginally sensitive to RSD-induced environment misclassification, even though the null result holds.

## PAPER-GEM-n1: nit
**Section:** V.A (Look-elsewhere correction)
**Issue:** Equation (2) uses the continuous Gaussian approximation for the Bonferroni threshold. This approximation breaks down in the extreme tails for the binomial distribution of the low-$N$ void class ($n=428$).
**Fix:** Add a half-sentence noting that Eq. (2) assumes Gaussianity, which justifies the reliance on the empirical max-stat MC null (Eq. 3) for the low-$N$ bins.
