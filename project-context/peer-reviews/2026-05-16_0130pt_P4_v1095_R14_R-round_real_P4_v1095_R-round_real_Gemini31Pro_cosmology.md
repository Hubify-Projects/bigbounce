# P4_v1095 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0130pt_P4_v1095_R14_R-round_real
**Wall time**: 59.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=82423, completion=7072, reasoning=5630, total=89495

---

I have completed the adversarial physics and convergence review of v1.0.95. 

**VERDICT: CONVERGED AND READY FOR EXTERNAL REVIEW.**
The manuscript contains **0 BLOCKERs** and **0 MAJORs**. The 4 specific R14 residual closures (Ivezic bibitem, §III.C splice, 900-fit arithmetic, abstract 99.3% rewrite) were implemented cleanly without introducing new regressions. The theoretical physics framing (Sec. VI.H) is exceptionally rigorous, correctly identifying the dipole as an axial vector (parity-even) rather than a polar vector, and appropriately refusing to map the morphology dipole to the scalar EFT amplitude $g_*$ without a derived transfer function. 

Below are 3 minor/nit findings for final polish before submission.

## PAPER-GEM-M1: Abstract Map Contradiction (minor)
**Location:** Abstract, Lines 104-105 vs Lines 118-119
**Issue:** The abstract introduces a contradiction regarding which map was used for the 99.3% leakage reproduction. Line 105 claims it was "on the asymmetry map", but Line 119 and Table IV explicitly state it was on the "un-monopole-subtracted CW-fraction map". The asymmetry map has its monopole mean-subtracted prior to decomposition, which would suppress the exact monopole-leakage channel being demonstrated.
**Fix:** Change "on the asymmetry map" in L105 to "on the un-monopole-subtracted CW-fraction map".

| Line | Paper Says | Artifact/Truth Says | Verdict |
| :--- | :--- | :--- | :--- |
| 104-105 | "reproducing $99.3\%$ of the observed pre-MASTER pseudo-$C_1$ power on the asymmetry map" | Table IV: "Pre-MASTER pseudo-$C_\ell^{(\ell=1)}$ is computed on the un-monopole-subtracted CW-fraction map, by design" | NOVEL |

## PAPER-GEM-N1: Null Mean Rounding Inconsistency (nit)
**Location:** Table IV, footnote a
**Issue:** The footnote rounds the null mean to $1.685 \times 10^{-2}$ but quotes the reproduction fraction as $99.3\%$. Mathematically, $1.685 / 1.696 = 99.35\%$ (which rounds to 99.4%). The 99.3% figure comes from the unrounded $1.6846 / 1.696 = 99.32\%$.
**Fix:** Change $1.685$ to $1.6846$ in the footnote to match the abstract and the exact arithmetic.

| Line | Paper Says | Artifact/Truth Says | Verdict |
| :--- | :--- | :--- | :--- |
| Table IV fn a | "The null mean $1.685\!\times\!10^{-2}$ recovers $99.3\%$ of the observed $1.696\!\times\!10^{-2}$" | $1.6846 / 1.696 = 0.9932$ ($99.3\%$). <br> $1.685 / 1.696 = 0.9935$ ($99.4\%$). | NOVEL |

## PAPER-GEM-N2: Pseudoscalar Field vs Axial Vector Dipole (nit)
**Location:** Section VI.H, Line 1968
**Issue:** The text states "a chirality dipole is by symmetry an isotropy-breaking pseudoscalar projection". While physically sound in context, it compresses the terminology: the *field* $A(\hat n)$ is a pseudoscalar field, but its $\ell=1$ dipole moment is an axial vector. 
**Fix:** Change "a chirality dipole is by symmetry an isotropy-breaking pseudoscalar projection" to "the chirality field is a pseudoscalar projection... whose dipole moment is an axial vector".

| Line | Paper Says | Artifact/Truth Says | Verdict |
| :--- | :--- | :--- | :--- |
| 1968 | "a chirality dipole is by symmetry an isotropy-breaking pseudoscalar projection $\langle\vec L\!\cdot\!\hat n\rangle$" | The field $A(\hat n)$ is a pseudoscalar projection; the dipole moment $\vec D$ is an axial vector. | NOVEL |

## PAPER-GEM-V1: R14 Closure Verification (VERDICT)
**Location:** Global
**Issue:** Verification of the 4 persistent residuals flagged in R13. All closures hold perfectly. The GPT/Grok unresolved items from R13 have also been thoroughly addressed in the text.

| Line | Paper Says | Artifact/Truth Says | Verdict |
| :--- | :--- | :--- | :--- |
| 2180 | `\bibitem{Ivezic:2019} ... The preprint arXiv:0805.2366 ... is the older LSST Science Book ... NOT the preprint of this specific ApJ reference-design article` | R14 directive: "removed arXiv:0805.2366 from the ApJ-only citation" | HOLDS |
| 474 | `under direct addition 1.0 + 0.5 = 1.5 pp; the observed 1.2 pp gap falls within this [1.118, 1.5] pp range. We do not separately estimate...` | R14 directive: "cleaned to single sentence" | HOLDS |
| 1699 | `900 injection fits ($N_{\rm inj}\!=\!100$ axes $\times$ $9$ amplitudes... calibrated against $N_{\rm MC,null}\!=\!1000$` | R14 directive: "CORRECTED to 900 injection fits... calibrated against N_MC,null=1000" | HOLDS |
| 104 | `inflate raw pseudo-$C_\ell$ chirality bandpowers (reproducing $99.3\%$ ... with a residual $+1.68\sigmaunit$, and $\sim\!49\%$ of the hemisphere maximum ... with a residual $+4.42\sigmaunit$` | R14 directive: "abstract 'can mimic large raw chirality dipoles' softened to 'inflate raw pseudo-Cl chirality bandpowers...'" | HOLDS |
