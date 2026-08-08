# EXT22 P2 gemini — chat: https://gemini.google.com/u/0/app/4235f3855427f430

Recommendation: MINOR REVISIONS

Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

1. Summary of the Paper
This manuscript presents a thorough sensitivity recast of the upcoming SPHEREx all-sky survey and the proposed Stage-V spectroscopic facility MegaMapper to constrain the primordial non-Gaussianity (PNG) signature predicted by matter bounce cosmologies. The author focuses on the robust local-type non-Gaussianity prediction of fNLlocal = −35/8 = −4.375 native to a matter-dominated contracting phase. A significant achievement of this work is a rigorous operator-algebra normalization audit that resolves a lingering factor-of-two discrepancy in the literature between Cai et al. and Li et al., confirming that the full in-in commutator calculation uniquely yields the −35/8 value. By analyzing the template mismatch between the matter-bounce bispectrum and standard local templates across various noise-weighting schemes, the author determines a noise-weighted template overlap of r ≈ 0.84 ± 0.02. The paper carefully maps out a conservative, multi-layered systematic budget—incorporating parameters such as polynomial null-space scatter, scale-dependent bias (bϕ) marginalization, and relativistic projection effects—concluding that SPHEREx can realistically test this framework at a ~2.6–5σ significance level.

2. BLOCKERS
None identified. The paper is exceptionally clear about its scope as a sensitivity recast rather than an independent experimental forecast. It explicitly avoids overstating its dimensional check derivations as full galaxy-field survey covariances, meaning there are no hidden structural flaws or missing controls that obstruct publication.

3. MAJORS

Clarification of Bayes Factor Bookkeeping in Section VI & Table II:
The text describes a comprehensive four-corner Bayes-factor prior grid evaluated under both the r→1 bookkeeping endpoint and the noise-weighted r ≈ 0.84 template-mismatch rebooking. While the prose explicitly runs through the three-step calculation to reproduce the abstract headline of BF ≈ 9 (using an effective uncertainty σeff ≈ 0.83), Table II explicitly displays the r→1 endpoint values (e.g., BF ∼ 10 and BF ∼ 17) while adding the rebooked numbers in the table footnotes and captions.
To improve readability for a broader audience, the author should adjust Table II to include parallel columns or explicit side-by-side sub-labels highlighting both bookkeeping spaces directly within the visual grid, rather than forcing the reader to reconstruct the rescaled grid from the explanatory text and footnotes.

4. MINORS

Contextualizing Equation 7:
In Section IV, Equation 7 is presented as a heuristic primordial-field scaling check in the curvature perturbation. The author properly notes that it does not serve as a full galaxy-field survey covariance derivation. To prevent readers from misapplying this scaling, a brief, explicit sentence should be added at the end of this paragraph directing readers to Section 3 of Heinrich et al. (2024) for the complete multi-tracer galaxy covariance framework.

Folded Configuration Limit Details:
Table I and Figure 1 note that the folded row sits on the degenerate boundary k1 = k2 + k3 and is evaluated as the limit of the sequence k1 = 2k, k2 = k3 = k. The author should state the numerical epsilon value or step size used for this limit evaluation within the text or caption to match the rigorous reproducibility standards demonstrated elsewhere in the paper.

Highlighting Schematic Bounds of κϵ:
In Section VIII.B, the upper endpoint of the parameter κϵ ≈ 80 is described as a schematic scaling bound rather than a strictly derived coefficient. The author should explicitly reiterate this qualitative distinction in the summary rows of Table IV where the ϵ-correction is listed, ensuring that future meta-analyses do not mistake the 0.6%–8% range as an exact parameter sweep boundary.

5. Strengths

Rigorous Theoretical Audit: The source-to-source convention audit resolving the factor-of-two discrepancy between the Cai et al. and Li et al. bispectrum normalizations is exceptionally well-executed. Verifying the halving via the standard in-in commutator identity symbolically provides needed clarity to the community.

Commendable Transparency and Scoping: The manuscript stands out for its high level of scientific honesty. It systematically avoids over-claiming results, explicitly distinguishing between its idealized multi-tracer bispectrum baseline derived from existing work and its own subordinate joint scale-dependent bias Fisher matrix.

Outstanding Open-Science Standard: Providing named, verifiable code artifacts (such as null_space_analysis.py, c9j_bf_template_rescale.py, and phase3_bispectrum_shape_overlap.json) in a public GitHub repository sets a premier standard for reproducibility in theoretical cosmology forecasting.
