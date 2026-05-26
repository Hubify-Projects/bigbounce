# P2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v3_P2_v1_7_37
**Wall time**: 157.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=33253, completion=10982, reasoning=9826, total=44235

---

## BLOCKER: Gauge-Frame vs. Physical-Frame Observable Reversal
**ID:** PAPER-GEM-B1
**Section:** Abstract & Sec X
**Concrete Issue:** The paper claims SPHEREx measures the gauge-frame $f_{\rm NL}$ and that the physical CFC frame is "not the on-sky observable." This is a fundamental violation of General Relativity in Large-Scale Structure. Galaxy surveys observe gauge-invariant quantities (redshifts and angles); scale-dependent bias strictly measures the physical-frame $f_{\rm NL}$, which is exactly zero for single-field inflation. The gauge-frame value of 0.015 is a coordinate artifact that cancels out entirely in physical LSS observables.
**Fix:** Reverse the claim. State that SPHEREx/MegaMapper measure the physical-frame $f_{\rm NL}$, making the true observational baseline for single-field inflation exactly zero, not 0.015.

## MAJOR: Mechanism-Independent Claim Overstates UV-Completion Independence
**ID:** PAPER-GEM-M1
**Section:** Sec I & Sec II.C
**Concrete Issue:** The claim that the bounce prediction depends *only* on the contracting phase assumes the NEC-violating bounce phase contributes exactly zero non-Gaussianity. Generic EFTs of bouncing cosmologies (e.g., Galileons, ghost condensates) generate large $f_{\rm NL}$ during the bounce itself due to $c_s \ll 1$ or higher-derivative operators. Relying on an LQC-specific suppression $(k\eta)^2 \sim 10^{-4}$ to dismiss bounce-phase contributions contradicts the claim of broad mechanism independence.
**Fix:** Downgrade "mechanism-independent" to "bounce-phase-independent under the assumption of trivial/LQC-like transmission." Explicitly note that generic NEC-violating EFTs can source their own $\mathcal{O}(1)$ non-Gaussianity.

## MAJOR: Hallucinated Citation and Model-Class Overreach for Birefringence
**ID:** PAPER-GEM-M2
**Section:** Sec VIII.E
**Concrete Issue:** The text cites a "2.9$\sigma$ ACT DR6 measurement of Diego-Palazuelos et al. 2025" for cosmic birefringence. ACT DR6 has no such standard published birefringence detection (ACT DR4 was null), making this a hallucinated or misattributed citation. Furthermore, claiming a generic Planck-scale ALP is "bounce-motivated" overreaches model-class boundaries; ALPs are generic to string theory and EFTs, not specific to bounces.
**Fix:** Remove the hallucinated ACT DR6 citation. Delete the claim that an ALP is "bounce-motivated" or reframe it strictly as a generic string/EFT signature orthogonal to the bounce mechanism.

## MAJOR: Incorrect EFT Bias Expansion in Galaxy Bispectrum
**ID:** PAPER-GEM-M3
**Section:** Sec VII.B
**Concrete Issue:** The text claims $\Delta b(k)$ propagates into the bispectrum estimator through cross-terms "$f_{\rm NL} b_\phi b_1^2 P(k_1) P(k_2)$". This is parametrically incorrect in the EFT of LSS. The tree-level galaxy bispectrum $P(k_1)P(k_2)$ terms are sourced by the non-linear bias $b_2$ (yielding $b_1 b_2 P P$), not $b_1^2$.
**Fix:** Correct the cross-term dependence from $b_1^2$ to $b_1 b_2$ (or $b_1 b_{s^2}$ for tidal bias) to match the standard tree-level galaxy bispectrum expansion.

## MAJOR: Bayesian Ockham Factor Ignored in QSFI Degeneracy
**ID:** PAPER-GEM-M4
**Section:** Sec VI.C
**Concrete Issue:** The paper claims that at the QSFI degenerate endpoint $\mu/H = 3/2$, "the Bayes factor against the bounce hypothesis collapses to $\mathrm{BF}\to 1$." This ignores the Bayesian Ockham factor. QSFI requires tuning its coupling parameter to exactly match the kinematic $-4.375$ amplitude of the bounce; the marginalized evidence for QSFI is heavily penalized by its prior volume, ensuring $\mathrm{BF} \gg 1$ in favor of the bounce even when shapes are identical.
**Fix:** Correct the statistical claim. State that while the shape mismatch vanishes, the Bayes factor remains $\gg 1$ due to the Ockham penalty on QSFI's tuned amplitude parameter.

## minor: Physical-Frame Consistency Relation Residuals
**ID:** PAPER-GEM-m1
**Section:** Sec X
**Concrete Issue:** The text states the physical-frame $f_{\rm NL}$ vanishes "at leading order in the slow-roll expansion, with parametrically $\mathcal{O}(\text{slow-roll})$ residuals". The vanishing of the physical squeezed limit is exact in slow-roll due to the equivalence principle; the residuals are spatial gradient corrections $\mathcal{O}(k_L^2/k_S^2)$, not slow-roll corrections.
**Fix:** Change "$\mathcal{O}(\text{slow-roll})$ residuals" to "spatial gradient $\mathcal{O}(k_L^2/k_S^2)$ residuals".
