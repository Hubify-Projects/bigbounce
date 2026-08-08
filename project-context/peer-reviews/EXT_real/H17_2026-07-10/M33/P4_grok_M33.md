VERDICT: MINOR REVISIONS

ISSUES:

[MINOR] Abstract & Sec. IV C: The pre-specified HC cut 
𝑝
𝑒
𝑞
>
0.6
p
eq
	​

>0.6 (N=949584) is justified post-sweep as excluding the depth-correlated low-confidence tail that drives the unthresholded z≈4.2–4.4 excess; while the commit-hash pre-registration record is cited, the a-priori motivation for exactly 0.6 (vs. 0.5 or 0.7) should be stated more explicitly in the main text without reference to the later sweep results.
[MINOR] Sec. IV D & Appendix D: The imaging+morphology forward model accounts for only ≈52–54% of the canonical-mask post-MASTER ℓ=1 residual amplitude (|a1|≈6.95×10^{-3}); although the unmodeled remainder is correctly bounded below the real-space A50≈0.75% floor and does not affect the primary null, the paper should add a one-paragraph quantitative statement on the maximum cosmological dipole fraction still allowed in that remainder (even if the full per-galaxy morphology-purity map is deferred).
[MINOR] Sec. V A: The amplitude-level tension with Shamir (1.7–4% in Ap units) is clearly stated, but the explicit caveat that a matched-footprint Ganalyzer reanalysis is still required for a likelihood-level exclusion should appear in the abstract and conclusions as well as the discussion, to prevent misreading as a direct statistical refutation of Shamir’s estimator.
[MINOR] Sec. VI B & Table VIII: The injection-recovery reports both θ-uniform and area-uniform axis draws; while they agree within MC error, the primary convention (area-uniform isotropic draw) and the precise definition of A95 (log-interpolated 95%-recovery threshold) should be stated once in the main text rather than only via artifact references.
[MINOR] Data Availability & reproducibility: The public catalog, model weights, and run scripts are declared, but the exact commit hash that freezes the p_eq>0.6 selection and the generator script (pipelines/p2_chirality/run_dipole_catalog_c.py) should be given explicitly in the Data Availability paragraph for immediate verifiability.

The central claim—that the real-space chirality dipole on the pre-specified high-confidence subsample is consistent with null at +0.41σ (p=0.31) and that a clean Shamir-scale dipole is disfavored by the block-bootstrap WLS template fit—is supported by the primary estimator, the injection-recovery calibration, the model-independent GZ1 cross-check, and the full systematics battery.
