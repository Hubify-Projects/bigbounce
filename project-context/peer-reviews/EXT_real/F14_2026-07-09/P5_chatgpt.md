--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://chatgpt.com/c/6a503b87-a058-83e8-9a4b-41a7bbc51a64) ---
Skip to contentNew chatSearch chatsPinnedChat historyChatGPT ProNew chat⇧⌘OSearch chats⌘KLibraryScheduledPluginsMorePinnedRelationship Counselor Soccer & Basketball Coach 2025BAMF SalesBAD® Fit (Bad.app)Big Bounce BookBAMF.com Agency AI Ops (2025)YoBe Minimalist Agentic HomepageBuilding OpenClaw on PiProjectsAI InvestingLA Sewer Project BattleFolder.mdH.computer (HoustonGolden.com redirect)You.mdShow moreChatsBAMF DEVPersonal accountShareYou said:f_P5.pdfPDFYou are an expert referee for Physical Review D. I am submitting the attached manuscript. Provide a rigorous, adversarial peer review as if for PRD. For EACH concern, classify it explicitly as MAJOR (blocks publication) or MINOR (should be addressed but does not block). Be specific: cite the section/equation/figure. Do not invent problems that are not there, and do not soften genuine problems. End with an explicit recommendation, using EXACTLY one of these verdict words: ACCEPT, MINOR REVISIONS, MAJOR REVISIONS, or REJECT.Show moreShow lessChatGPT said:Referee report
This manuscript presents a large DESI DR1 test of whether classifier-assigned spiral handedness differs between DESIVAST void and non-void populations, supplemented by several T-Web, density, sky-position, and external-catalog checks. The empirical result is broadly plausible: none of the reported void definitions yields a statistically significant difference. The manuscript is unusually transparent about post-hoc choices and known weaknesses. Nevertheless, the current version does not yet support its quoted primary bound or its headline formulation at PRD standard because the primary estimand is internally inconsistent, the principal observational comparison remains insufficiently adjusted for confounding, and the systematic-error envelope is not statistically well founded. f_P5
Major concerns
MAJOR — The manuscript gives two different quantities as the “primary” DESIVAST result.
Section VIII B explicitly designates the footprint-restricted contrast as the primary estimand:
ΔfCW=+0.0018,zΔ=0.78,p=0.43,\Delta f_{\rm CW}=+0.0018,\qquad z_\Delta=0.78,\qquad p=0.43,ΔfCW​=+0.0018,zΔ​=0.78,p=0.43,
using nnonvoid=253,276n_{\rm nonvoid}=253{,}276nnonvoid​=253,276.
However, the abstract, opening headline, Table XIII discussion, Section XV, and several interpretive statements repeatedly call the unrestricted contrast
ΔfCW=+0.0007,zΔ=0.31,p=0.76,\Delta f_{\rm CW}=+0.0007,\qquad z_\Delta=0.31,\qquad p=0.76,ΔfCW​=+0.0007,zΔ​=0.31,p=0.76,
the primary result. Section VIII B itself says that this broader all-z≤0.24z\leq0.24z≤0.24 comparison is demoted to a “sensitivity check.”
This is not a cosmetic discrepancy. The control population, point estimate, standard error, confidence interval, and interpretation differ. It also undermines the stated attempt to control post-hoc path selection in Section V B.
Required fix: Choose one estimand and use it consistently in the title-page headline, abstract, Section V B, Tables IV/X/XIII, discussion, conclusions, and quoted bound. If the footprint-restricted comparison is primary, the headline result must be +0.0018+0.0018+0.0018, not +0.0007+0.0007+0.0007. The unrestricted comparison should be labeled secondary everywhere. The five-member Bonferroni family must also be redefined so that all five entries correspond to comparable, same-selection-function estimands.
MAJOR — The primary void/non-void comparison is not adequately adjusted for observational confounding.
The manuscript itself states in Section VIII B that the appropriate analysis would be a regression or matched/IPW estimate such as
CW∼void+z+mr+R50+pmax⁡+imaging leg+morphology+sky,{\rm CW}\sim {\rm void}+z+m_r+R_{50}+p_{\max}+{\rm imaging\ leg}+{\rm morphology}+{\rm sky},CW∼void+z+mr​+R50​+pmax​+imaging leg+morphology+sky,
but then explicitly defers that analysis. Instead, it treats target-program balance, a footprint restriction, and a collection of one-variable sensitivity checks as an “adjustment set.”
That is insufficient. Void and non-void galaxy populations can differ simultaneously in redshift, apparent size, surface brightness, inclination, morphology, classifier confidence, imaging depth, and sky position. These quantities can affect classifier errors even when the overall bright/dark fractions are nearly identical. The T-Web covariate regression in Section VI B does not validate the DESIVAST primary estimator because it uses a different environment definition, parent population, and selection function.
This is especially important because the classifier has only 69.91% binary accuracy and the paper concedes that no environment-stratified confusion matrix exists. A small environment-dependent change in false-CW and false-CCW rates could easily be comparable to the quoted sub-percent contrast.
Required fix: Perform the DESIVAST analysis with a prespecified multivariable estimator. At minimum, report:
a logistic regression coefficient for void membership with redshift, magnitude, angular/physical size, morphology or inclination proxies, classifier confidence, imaging leg, target program, and appropriate sky-region terms;
a matched or inverse-probability-weighted estimate as a robustness check;
overlap and balance diagnostics;
uncertainty accounting for the matching/weighting procedure.
The unadjusted two-proportion comparison may remain as a descriptive result, but it should not carry the principal physical interpretation by itself.
MAJOR — The ≈0.9\approx0.9≈0.9 percentage-point “systematic envelope” is not statistically justified.
Table XI combines:
a two-sided 2σ2\sigma2σ counting interval,
the maximum shift under an FoG perturbation,
differences between distinct geometry or membership definitions,
a confidence-threshold shift,
a footprint shift,
and a match-radius shift,
by quadrature while simply asserting approximate independence.
These terms are neither demonstrated to be independent nor placed on a common probabilistic footing. Several are strongly correlated because they are computed from the same galaxies and related void definitions. Some are maxima across analysis variants rather than estimates of one-standard-deviation random uncertainties. The “sphere-PIS versus GALZONE” and “hole versus maximal sphere” terms partly represent changes of estimand, not noise affecting a single fixed estimand. Combining a 2σ2\sigma2σ statistical half-width with maximum systematic excursions in quadrature has no standard coverage interpretation.
Consequently, the claim that the analysis “disfavors” classifier-label differences above approximately 0.9 pp is not presently a calibrated confidence statement.
Required fix: Either:
construct a joint resampling or hierarchical uncertainty calculation that propagates membership, geometry, classifier, and sampling variations into a distribution for one clearly defined estimand; or
stop presenting 0.9 pp as an effective 2σ2\sigma2σ bound and instead report the counting interval plus a separate sensitivity table showing how the point estimate changes under each analysis variant.
A conservative envelope could be defined as the union of confidence intervals across prespecified admissible definitions, but it should not be called a 2σ2\sigma2σ quadrature uncertainty unless its coverage is established.
MAJOR — The author-defined “DESIVAST footprint” is not an adequate substitute for the actual survey selection function.
The footprint-restricted primary control is constructed in Section VIII E as the union of the angular projections of 101,863 void-hole spheres, intersected with their radial span. This is not the published DESIVAST angular/radial mask or a random-catalog-based estimate of the usable BGS selection function. By construction, it is spatially tied to where void holes were found and can exclude valid in-footprint regions that contain no hole while including complex projected regions that do not share identical completeness with the void sample.
Since this construction changes the result from +0.0007+0.0007+0.0007 to +0.0018+0.0018+0.0018 and is then declared primary, its validity is load-bearing.
Required fix: Define the same-selection-function control with the actual DESIVAST/BGS mask, vetoes, completeness information, and radial selection, preferably using the corresponding DESI random catalogs. Alternatively, construct matched non-void controls locally around each void in redshift and angular-selection space. Demonstrate balance between void and control samples. The angular-disc union may remain as a sensitivity analysis, not the principal footprint definition.
MAJOR — The headline language exceeds what is established about physical spiral chirality.
The manuscript repeatedly states that “spiral galaxy chirality shows no environment dependence,” while Appendix A and Sections XII–XIII correctly acknowledge that the measured quantity is the classifier-assigned CW fraction and that the classifier has only 69.91% binary accuracy. More importantly, no environment-conditioned confusion matrix is available, so nondifferential misclassification is unverified.
Algebraic cancellation of a global monopole does not cancel environment-dependent classification errors. The GZ1 global control in Paper IV also does not establish equal false-label rates inside and outside DESIVAST voids.
Required fix: Recast the title, abstract, and conclusions consistently as a null in classifier-assigned handedness labels, unless an environment-stratified human-label validation is added. A useful validation would compare classifier labels to high-consensus GZ1 or another human-labelled sample separately in void and matched non-void environments and report differential sensitivity/specificity. Without such a test, the manuscript must not imply a calibrated sub-percent constraint on physical handedness.
MAJOR — The multiple-testing treatment does not provide a valid simultaneous upper bound across the five primary estimators.
Bonferroni testing at ∣z∣<2.58|z|<2.58∣z∣<2.58 establishes that none of five null hypotheses is rejected at family-wise α=0.05\alpha=0.05α=0.05. It does not by itself justify the strength of a common upper bound across five correlated, differently defined estimands. The five analyses have substantially different memberships and, in the GALZONE cases, very different control populations. They are not repeated measurements of a single parameter without further assumptions.
The text recognizes that post-hoc selection can make a null bound look artificially tight, but then still quotes a single approximately 0.9 pp family-level bound.
Required fix: Report simultaneous confidence intervals for each estimator and clearly distinguish:
a family-wise non-rejection statement;
estimator-specific effect-size intervals;
any common parameter model, if one is intended.
If the authors want one bound across definitions, they must define the common estimand and show why each method estimates it, or quote the least constraining simultaneous interval rather than a preferred or quadrature-combined value.
Minor concerns
MINOR — The manuscript is excessively repetitive and obscures the actual inferential chain.
The same caveats—post-hoc designation, fixed-redshift-space status, classifier-label attenuation, Paper IV dependence, and 0.9 pp envelope—are repeated in the abstract, reader’s guide, Sections V, VIII, XII, XIII, XV, and Appendix A. The repetition makes it difficult to identify which statements are formal results and which are defenses or qualifications.
Required fix: Condense the paper substantially. A clean structure would be: data and estimand; primary DESIVAST analysis; systematic/covariate robustness; secondary T-Web analyses; limitations. Move the extended defense of Paper IV and the toy-model discussion to supplemental material.
MINOR — The argument extrapolating the FoG Monte Carlo beyond the tested perturbation is unsupported.
Section VIII states that moving the estimand by ≳0.5\gtrsim0.5≳0.5 pp would require roughly 1.3×1.3\times1.3× the maximum observed membership reassignment. This assumes approximately linear scaling between the number of membership changes and the chirality contrast, which is not demonstrated. The identities and handedness composition of switched galaxies matter, not merely their count.
Required fix: Delete this extrapolation or demonstrate it with simulations over several displacement amplitudes and report the resulting response curve.
MINOR — Several statements use “independent algorithms” too strongly.
VoidFinder, V2-REVOLVER, and V2-VIDE use the same DESI BGS galaxy field and survey mask; REVOLVER and VIDE are related ZOBOV-based watershed methods. Their outputs are valuable robustness variants but are not statistically independent measurements.
Required fix: Replace “three independent void-finding algorithms” with “three algorithmically distinct void definitions” or equivalent language and account for their correlations when discussing family-level inference.
MINOR — The use of Jeffreys credible intervals alongside frequentist zzz-tests and Bonferroni thresholds needs clearer separation.
Section V mixes Bayesian binomial intervals, asymptotic frequentist tests, and permutation ppp-values. This is not inherently wrong, but the manuscript occasionally refers to them collectively as if they had one common coverage interpretation.
Required fix: State explicitly which interval is used for effect-size reporting and which procedure controls Type-I error. For the primary two-sample contrast, a direct interval for the difference of proportions should be the main interval rather than separate one-sample Jeffreys intervals.
MINOR — The treatment of permutation resolution is marginal for some quoted numerical precision.
With NMC=1000N_{\rm MC}=1000NMC​=1000, permutation ppp-values have minimum resolution 1/10011/10011/1001 and standard errors of order 10−210^{-2}10−2. Reporting values such as 0.135, 0.413, or differences of 0.011 invites overinterpretation.
Required fix: Increase the number of permutations for final results, particularly for the global Phase-2 and HEALPix tests, or round permutation ppp-values to two significant digits and avoid detailed comparisons between random streams.
MINOR — The T-Web material is too extensive given that the manuscript demonstrates that its canonical labels are severely selection-function contaminated.
Section IX A reports that random weighting changes the void volume fraction from 17.6% to 0.75% and reassigns roughly 73% of matched galaxies. This establishes that the original T-Web environmental interpretation is not quantitatively reliable, even though the chirality null remains.
Required fix: Move most canonical T-Web results and the nine-cell sweep to an appendix or supplement. The randoms-weighted or shell-corrected version should be the only scientifically interpreted T-Web diagnostic.
MINOR — The statement that a genuine astrophysical signal “would propagate across” bright and dark target programs is too categorical.
Bright and dark programs probe different redshift, luminosity, morphology, and tracer populations. A real environment-conditioned effect need not have identical amplitude in both.
Required fix: Rephrase this as a diagnostic expectation under an explicitly stated population-invariant signal model, not a general criterion for astrophysical reality.
MINOR — The toy EFT appendix is disconnected from the empirical analysis and risks misleading readers.
Appendix B introduces a non-covariant, non-derived operator and an order-of-magnitude “bound” without a transfer function. The appendix carefully disclaims its status, but it adds little scientific value and may still be mistaken for a theory constraint.
Required fix: Remove it or move it to non-archival supplementary notes. It should not be part of the PRD paper unless developed into a proper model with a dimensionally and covariantly defined operator and an explicit observable mapping.
MINOR — Terminology surrounding “exclusion,” “bound,” and “environment independence” should be standardized.
A failure to reject the null is not evidence of exact independence. The manuscript sometimes correctly says “no detectable dependence” but elsewhere uses “environment-independence finding” or “excludes” effects at a quoted scale.
Required fix: Use “no statistically significant difference detected” and “sensitivity interval” consistently. Reserve “excluded” for a calibrated confidence interval under a specified model and systematic treatment.
Assessment of the central claim
The data support the narrower claim that no statistically significant difference is detected among the reported DESIVAST classifier-label contrasts, but the manuscript does not yet establish a calibrated ≈0.9\approx0.9≈0.9 pp bound on physical spiral chirality or a uniquely defined primary void/non-void estimand.
Recommendation
MAJOR REVISIONSSourcesDo you like this personality?InstantChatGPT can make mistakes. Check important info. gstackToo many requestsYou’re making requests too quickly. We’ve temporarily limited access to your conversations to protect your data.Please wait a few minutes before trying again.Got it
--- END UNTRUSTED EXTERNAL CONTENT ---
