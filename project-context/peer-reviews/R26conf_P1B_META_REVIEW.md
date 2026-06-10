# P1B R26conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 516.2s

---

Meta-referee report (new issues only)

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: Sec. IV (Data Methods: CMB E–B analysis), pp. 6–8; Fig. 3 footnote
- Why others missed it: Prior reviews focused on pixel-window/beam handling and estimator weighting but did not examine bandpower covariance structure.
- Specific problem (quote): “The angle is recovered … by an unweighted χ² template fit of the decoupled C^EB_b bandpowers to sin(2β)cos(2β) C^EE_b on a β grid.” “SNRtmpl ≡ [∑_b (C^EB,th_b/σ^MC_b)^2]^{1/2}.”
- Required fix: Use the full bandpower covariance (including off-diagonal terms from MASTER mode coupling and masking) both for the inverse-variance weighting in the β fit and for the template SNR; or explicitly demonstrate with MC that the off-diagonal terms are negligible at the quoted 10^−3–10^−2 deg bias level (provide the measured correlation matrix and show that diagonal-only weighting is sufficient).

P1B-META-E2
- Severity: ESSENTIAL
- Section + page: Sec. VI (Cosmic Birefringence: Spectator ALP), p. 9 (Eq. 2) and surrounding text
- Why others missed it: Reviewers checked the Δφ/fa arithmetic but not the emissivity-time weighting implicit in CMB polarization generation.
- Specific problem (quote): “ALP field evolution.—Numerical integration … yields the field displacement from recombination to today: Δφ/fa ≈ 0.42 (m = 2H0, θi = 1).” The analysis equates β to (gaγ/2) [φ(today) − φ(recombination)], i.e., a single Δφ from z* ≃ 1100 to 0.
- Required fix: Justify the “recombination-to-today” approximation by computing an effective β that correctly weights polarization generated at reionization (low-ℓ EE) and recombination (acoustic EE) along the line of sight (visibility-function weighting). Provide a two-epoch or full line-of-sight check showing the bias from using a single Δφ is < few percent for the m ∼ H0 regime; otherwise update the predicted β accordingly.

P1B-META-M1
- Severity: MAJOR
- Section + page: Sec. IV (Data Methods), p. 7 (“Noise model and injections.”)
- Why others missed it: The Q/U noise normalization was noted but not challenged for convention.
- Specific problem (quote): “draws independent Gaussian realizations with the same σpix for Q and U (no √2 factor).” with ΔP = 10 μK·arcmin used directly as σpix = ΔP/√Ωpix.
- Required fix: Cite the polarization-noise convention you adopt (whether ΔP is per Stokes Q and per U, or for the combined polarization field) and verify against ACT-like definitions. If ΔP refers to polarization map depth such that σ(Q)=σ(U)=ΔP is not correct, include the √2 (or other) factor and rerun the MC; report the impact on the bias/SNR. Absent a citation, the current “no √2” assumption is under-justified.

P1B-META-M2
- Severity: MAJOR
- Section + page: Sec. IV (Method), pp. 6–8
- Why others missed it: Estimator definition was reviewed, but the test design omitted a key degeneracy stress test.
- Specific problem (quote): “The test confirms the algebraic pseudo-Cℓ E→B deconvolution … NOT the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α … (the synthetic CMB-only skies contain no galactic foregrounds…).”
- Required fix: Add a robustness test injecting a nonzero, uniform instrument angle α alongside β (and/or a pure-α case) and demonstrate the estimator’s response (showing the β–α degeneracy in this pipeline and that the quoted “systematic floor” is not conflating α with β). Even for a methods validation, a controlled α-injection test is needed to qualify what the pipeline is (and is not) measuring.

P1B-META-M3
- Severity: MAJOR
- Section + page: Sec. IV (Method), pp. 6–8
- Why others missed it: Reviewers focused on weighting and mask choices; they did not question the “conservative worst-case” claim about noise statistics.
- Specific problem (quote): “Each realization adds white noise … (a conservative worst-case bias check; no 1/f or anisotropic component).”
- Required fix: Substantiate or withdraw the “conservative” claim. Add a test with anisotropic/striped or 1/f-like polarization noise (common in ground-based surveys) to show whether the β recovery bias increases relative to the white-noise case. If such noise patterns increase bias, update the stated systematic floor; if not, document the quantitative comparison.

P1B-META-M4
- Severity: MAJOR
- Section + page: Sec. IV (Method), pp. 6–8
- Why others missed it: No one addressed split-map cross spectra.
- Specific problem (quote): The pipeline uses a single NmtField; no mention of map splits or cross-spectra to avoid auto-spectrum noise terms in EB.
- Required fix: Demonstrate that auto-spectrum EB noise terms are null in this setup (mask + mode coupling + Q/U noise model) to below the quoted floor, or, preferably, rerun with split-map cross-spectra (simulated half-mission/season splits) to guarantee zero noise bias by construction and re-quote the floor.

P1B-META-M5
- Severity: MAJOR
- Section + page: Sec. III (ΛCDM+ΔNeff MCMC), p. 3
- Why others missed it: The ΔNeff results were audited, but prior choice scrutiny was not.
- Specific problem (quote): “nnu with a flat prior Neff ∈ [2.046, 5.046] (i.e. ΔNeff ∈ [−1, +2]).”
- Required fix: Justify the inclusion of ΔNeff < 0 (i.e., Neff < 3.046) for a “radiation-like degree of freedom” proxy (which physically represents extra radiation). At minimum, report prior-to-posterior volume effects and a sensitivity test with a non-negative ΔNeff prior (e.g., [0, +2]) to show the headline ΔNeff and H0/S8 constraints are robust to the lower bound.

P1B-META-M6
- Severity: MAJOR
- Section + page: Sec. III (ΛCDM+ΔNeff MCMC), p. 3
- Why others missed it: Yp handling was mentioned but not stress-tested.
- Specific problem (quote): “YHe follows the CAMB BBN-consistent default (no explicit override…).”
- Required fix: Add a robustness check demonstrating that allowing Yp to vary (BBN-relaxed or with a standard BBN prior width) does not shift ΔNeff/H0/S8 beyond the stated precision; briefly cite which BBN prescription (e.g., PArthENoPE/PRIMAT) the CAMB default follows, as ΔNeff–Yp degeneracy can bias ΔNeff constraints if not examined.

P1B-META-M7
- Severity: MAJOR
- Section + page: Appendix C (ALP-MCMC), p. 14
- Why others missed it: They checked chain lengths and R̂ but not prior symmetry for β.
- Specific problem (quote): “model-independent βfree … β: uniform prior on [−1°, 2°].”
- Required fix: Use a symmetric prior around zero (e.g., [−2°, 2°]) or justify the asymmetry; report that results are unchanged under a symmetric prior. An asymmetric β prior is unnecessary here (the data are far from the edges) but it is a formal bias.

P1B-META-m1
- Severity: MINOR
- Section + page: Sec. IV (Method), pp. 6–8; “Restricting the fit to bins with ℓ ≤ 1024 changes nothing (0.238°): the noise-only bins above the band limit carry zero template weight.”
- Why others missed it: Earlier reviews flagged pixel-window issues, not this internal logic.
- Specific problem: This statement conflicts with the prior attribution that the unweighted fit’s bias is “equal weighting of noise-dominated high-ℓ bins” (if ℓ>1024 bins have zero template weight, the relevant “noise-dominated” bins must be below 1024; the text should make that clear).
- Required fix: Clarify explicitly that the high-ℓ “noise-dominated” bins referenced are within the physical band limit (≲1024), and that bins above the band limit have zero template weight because the template C^EE_b used in the fit is zero there (state whether the template is theory or the decoupled bandpowers).

P1B-META-m2
- Severity: MINOR
- Section + page: Sec. IV (Method), p. 6
- Why others missed it: The degree–radian convention was caught, but the TB channel was not discussed.
- Specific problem: The estimator uses only EB; no test is shown that including TB (which also rotates under β) would yield consistent β and/or reduce bias.
- Required fix: Add a short TB+EB joint-fit check (same synthetic skies) and report whether β is consistent and whether the systematic floor changes; this is a standard cross-check for uniform-rotation estimators.

P1B-META-m3
- Severity: MINOR
- Section + page: Sec. IV (Method), pp. 6–8
- Why others missed it: Focus remained on mask and apodization.
- Specific problem: Only one ℓ-binning is used; but the bias attribution relies on high-ℓ behavior.
- Required fix: Add a simple binning robustness test (e.g., 15 vs 30 bins over the same ℓ range) to show the −0.032° to −0.040° bias is not a binning artifact.

P1B-META-m4
- Severity: MINOR
- Section + page: Sec. VI (ALP), pp. 10–11
- Why others missed it: Coupling ranges were discussed, but α_EM scale choice was not.
- Specific problem: The normalization takes αEM at zero-momentum without stating the scale. While the numerical impact is small, the convention should be explicit to avoid ambiguity in reproductions.
- Required fix: State explicitly the αEM value and scale used (e.g., αEM(0) = 1/137.036), and confirm the β shift from using αEM(m_e) or αEM(m_Z) would be negligible at the quoted precision.

P1B-META-m5
- Severity: MINOR
- Section + page: Sec. IV (Method), p. 6
- Why others missed it: Reproducibility paths dominated attention.
- Specific problem: The map is analyzed as a single NmtField with purify_b=False; NaMaster documentation recommends iter_n (pure-B E/B purification) or split maps for certain masks to control E→B leakage. The paper later shows purification does not change β, but does not state the NaMaster default n_iter used (it can affect leakage control).
- Required fix: Report the NaMaster n_iter value used (default) and confirm via robustness that varying n_iter does not change the recovered β within the systematic floor.

Meta-review recommendation
MAJOR REVISIONS

Rationale: The manuscript is close, but several method-level blind spots remain: (i) diagonal-only weighting and omission of the EB bandpower covariance in the β estimator and SNR; (ii) unsubstantiated “conservative” noise claim without anisotropic/1/f tests; (iii) no α-injection stress test; (iv) reliance on a single Δφ (recombination→today) for β without visibility-function weighting; (v) asymmetric prior for βfree; and (vi) ΔNeff prior/BBN handling not robustness-tested. These are correctable with targeted additions and clarifications.

Union-of-reviews summary
Across the five prior reports plus this meta-review, there are ~10–14 essential/major items that must be addressed (future-dated/unverifiable citations; estimator specification/weighting; Planck-release pairing; w0wa phrasing/crossing; chain cross-identity; removing internal “correction notes”; data availability; ACT DR6 use; covariance and anisotropic-noise tests; α-injection test; visibility weighting for β; prior symmetry for β; ΔNeff prior/BBN robustness). My confidence the paper could pass external peer review after these changes is moderate-to-high, provided the authors (1) restrict to verifiable datasets/citations, (2) upgrade the β estimator to covariance-aware inverse-variance weighting (or document why diagonal-only suffices), (3) run the missing noise/α tests, and (4) add the ALP visibility-weighting justification/results.