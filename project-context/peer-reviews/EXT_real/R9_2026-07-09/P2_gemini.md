Gemini said
Physical Review D Referee Report

Manuscript Title: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Author: Houston Golden

Summary of the Manuscript

The manuscript evaluates the viability of testing a matter-dominated contracting phase preceding a nonsingular bounce using upcoming large-scale structure surveys. The author resolves a longstanding factor-of-two discrepancy in the literature regarding the local-type non-Gaussianity prediction, definitively correcting the value to f
NL
local
	​

=−35/16 by re-summing the cubic-action vertices and identifying a spurious polynomial term in prior work. The author then recasts existing SPHEREx and MegaMapper forecasts to account for the template mismatch between the matter-bounce bispectrum shape and the standard local template, deriving a template overlap factor of r≈0.84 under realistic noise weighting.  
PDF
+ 3

The resulting analysis predicts a pre-systematic SPHEREx detection significance of roughly 2.6 to 2.75 standard deviations, which degrades to a 1.3 to 2.75 envelope after a comprehensive systematic budget. Finally, the manuscript performs a closed-form Bayesian model comparison, concluding that a SPHEREx detection at the corrected amplitude would favor the bounce scenario over tuned multifield inflationary alternatives with a Bayes factor of approximately 9 to 14.  
PDF
+ 1

General Impression and Recommendation

Recommendation: Accept with Minor Revisions

This is a rigorously structured and highly detailed paper that makes a concrete contribution to the theoretical cosmology literature. Resolving the Cai vs. Li algebraic discrepancy is a valuable service to the community, and the careful attention to template-overlap mismatch and systematic accounting elevates the recasted forecast beyond a naive parameter substitution. The author is commendably transparent about the limitations of the analysis, explicitly labeling the work as a sensitivity recast rather than a full independent joint-covariance forecast. The manuscript is well-suited for Physical Review D, provided the author addresses a few specific theoretical and methodological concerns to tighten the robustness of the physical claims.  
PDF

Major Comments

Reliance on Bounded Systematics for Bounce Transmission: The entirety of the f
NL
local
	​

 prediction hinges on the assumption of faithful third-order (cubic) bispectrum transmission through the nonsingular bounce. The author notes this has only been formally verified at linear order. While the author relies on single-clock nonlinear adiabaticity and degree-of-freedom counting to bound the cubic-order systematic to ≤10
−3
 , this remains an order-of-magnitude scaling estimate rather than a rigorously derived transfer function. The manuscript would benefit from a clearer acknowledgment that without a full numerical evaluation of the O((kη
bounce
	​

)
2
) coefficient, this transmission assumption remains a critical vulnerability in the model's predictive power.  
PDF
+ 4

Fisher Forecast Assumptions: To validate the imported SPHEREx baseline, the author constructs an in-house tree-level galaxy-bispectrum Fisher forecast. However, this independent validation holds the nonlinear bias parameters b
2
	​

/b
s
2
	​

 fixed at their fiducial values rather than marginalizing over them. Omitting higher-order bias marginalization in a bispectrum Fisher matrix often artificially tightens constraints; the author must explicitly justify why holding these fixed still provides a conservative or adequate validation ratio for the fully marginalized Heinrich baseline.  
PDF
+ 1

GR Projection Marginalization Proxy: The author adopts an additive-quadrature heuristic for the systematic budget, noting that a true joint Fisher marginalization over correlated nuisances (like GR projection effects) would typically loosen the constraint. To proxy this, the author transfers a correlation coefficient of ρ=−0.868 computed from a separate scale-dependent bias (SDB) Fisher matrix. Because the bispectrum and SDB channels respond differently to relativistic projections, porting a correlation matrix directly from the power spectrum channel to the bispectrum channel is mathematically precarious. A brief theoretical justification of why this proxy remains a safe bound for the 3D bispectrum is necessary.  
PDF
+ 2

Theoretical Prior Boundaries: The Bayesian model comparison strongly depends on the assumed theoretical prior. The author recommends a Gaussian bounce prior of σ
theory
	​

=1.0 to encompass the O(ϵ) corrections. However, the upper endpoint for the κ
ϵ
	​

 scaling coefficient is admittedly a "schematic scaling bound, not a derived coefficient". If the true κ
ϵ
	​

 exceeds this estimate, the theoretical prior would need to widen significantly, depressing the Bayes factor.  
PDF
+ 3

Minor Comments

Nomenclature and Conventions: The author is thorough in addressing the Komatsu-Spergel constant c=2 normalization. However, when referencing the physical-frame consistency relation later in the manuscript, the distinction between gauge-frame and physical-frame observations is slightly convoluted. A single table or consolidated paragraph cleanly separating the expected values in these two frames would aid readability.  
PDF
+ 1

Appendix A Discrepancy: The exact identification of the +(99/128)Σk
i
3
	​

 spurious term in Cai et al.'s final polynomial is excellent forensic work. The author should consider whether this warrants a formal erratum submitted to the original journal of publication by the original authors, though this is outside the scope of the immediate manuscript acceptance.  
PDF

Formatting Typo: In Section VI, under the numerical self-consistency check, there appears to be a minor formatting artifact or missing parenthesis near the Bayes factor approximation derivations for the Gaussian-bounce prior corners. Please review the typesetting of the closed-form standard normal CDF integrations.  
PDF

--- MANIFEST: P2 (v1.7.104) | Gemini Pro | native PDF | chat 3cbeaa866eddc6af | verdict minor-revisions ('Accept with Minor Revisions'; praised vertex-algebra correction) | 2026-07-09
