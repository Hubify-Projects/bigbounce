# EXT P5 ChatGPT — M25 (recovered duplicate; verdict already covered by recorded 6a54c84c MAJOR-REVISIONS row) (recovered orphan)

- **reviewer:** ChatGPT (Extended Thinking Pro)
- **venue prompt:** P5
- **chat URL:** https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a54c7b1-7bd4-83e8-944d-72a7072adc11
- **status:** harvested-recovered (orphaned by ext_submit poll timeout; landed server-side, recovered 2026-07-13)
- **verdict (raw line 1):** MAJOR REVISIONS

---

## Raw ChatGPT response (verbatim)

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Section VIII B/E, definition of the primary control sample: the “DESIVAST usable footprint” is constructed from the union of the detected hole-sphere angular discs and their radial span, rather than from the published BGS completeness mask and random catalog. This construction is endogenous to where voids were found and does not match fibre-assignment completeness, imaging depth, angular vetoes, or the radial selection function; the manuscript itself explicitly concedes that “footprint ≠ selection function” but later describes the estimator as selection-function matched. The primary contrast must be recomputed using the official DESIVAST/BGS mask and randoms, or with explicitly matched non-void controls. 

ext_P5_M25

[MAJOR] Section VIII B and the deferred analysis in Section VIII D, confounding of the primary contrast: the raw void/non-void proportion difference is not adjusted for redshift, apparent magnitude, size, surface brightness, morphology, inclination, classifier confidence, imaging leg, or local spectroscopic completeness. Void and non-void galaxies will generally have different distributions in these variables, all of which can affect CW/CCW classification. The bright/dark program balance alone is not an adequate adjustment. A pre-specified regression, inverse-probability weighting, or matched-control analysis is required for the primary DESIVAST result, not only for the secondary T-Web sample.

[MAJOR] Table X and Section VIII B, uncertainty model: the quoted two-sample binomial standard error treats tens of thousands of galaxies as independent Bernoulli trials. Galaxies share voids, imaging fields, observing conditions, and large-scale structures, while classifier residuals may be spatially correlated. The principal confidence interval therefore requires a void-level and sky-block bootstrap or jackknife, or a hierarchical/cluster-robust model; the HEALPix diagnostic scans do not replace clustered uncertainty estimation for the primary statistic.

[MAJOR] Table XI, the claimed “≈0.9 pp effective 2σ envelope”: the quadrature sum mixes a 95% statistical half-width with maximum observed shifts from model choices, membership definitions, and perturbation experiments. These terms are neither demonstrated to be independent nor shown to represent Gaussian one- or two-sigma uncertainties; several are correlated manifestations of the same geometry/membership ambiguity. Consequently, the resulting 0.9 pp number has no defined frequentist coverage or Bayesian credibility and cannot be advertised as a 2σ bound.

[MAJOR] Sections V B and XII, inconsistent upper limits: Section V B correctly finds that the least-constraining Bonferroni-5 simultaneous interval permits an absolute contrast of approximately 1.1 pp, whereas the abstract and discussion instruct model-builders to use the smaller 0.9 pp envelope. These are different statistical statements, and the preferred post-hoc estimator cannot supersede the simultaneous family interval. Under the manuscript’s own attenuation factor, the family-wise physical scale would already be approximately 2.8 pp rather than 2.26 pp, before addressing the other systematics.

[MAJOR] Section V B and Table XIV, non-common estimands in the “Bonferroni-5 family”: the three sphere point-in-sphere rows use a 678,945-galaxy low-redshift parent, whereas the two GALZONE rows use a 145,789-galaxy catalog-valid parent and different membership semantics. These tests do not estimate the same population contrast, so treating them as five interchangeable measurements of one bound is not justified. Moreover, the primary path was selected after inspecting a much larger analysis tree; Bonferroni correction over only these five rows does not remove the selection bias in a post-hoc upper limit. The paper should either define one estimand and apply all viable membership algorithms to a common parent or present a clearly exploratory multiverse analysis without a single exclusion limit.

[MAJOR] Appendix A and Section XII B, conversion to a physical-chirality bound: an overall binary accuracy and approximate global error symmetry do not establish a common misclassification matrix in void and non-void environments. The directly relevant void validation has a directional-error-asymmetry uncertainty of roughly ±3.7 pp, much larger than the claimed sub-percent label bound. Thus neither cancellation of classifier bias nor division by 2a−1 is validated at the required precision. The 2.26 pp physical bound should be removed unless an environment-stratified measurement-error model is fitted and its uncertainty propagated.

[MAJOR] Section VIII, redshift-space-distortion bound: independently perturbing galaxy distances while holding published holes fixed is not a physical RSD reconstruction, and moving existing galaxies and holes coherently without rerunning VoidFinder does not capture changes in void centers, radii, merging, topology, or survey-edge classification. The reported 0.024 pp shift was also calculated for the unrestricted contrast rather than the footprint-restricted primary estimand. It therefore cannot be inserted as a 0.02 pp systematic on the primary result; a defensible bound requires reconstructed mocks and rerunning the void finder and the complete primary estimator.

[MAJOR] Sections IV, VII, and IX A, validity of the secondary T-Web analysis: the canonical density field uses a global mean despite a factor of approximately 640 radial selection variation, no random-catalog completeness correction, and a zero-padded FFT in a highly non-periodic survey volume. The randoms-weighted rebuild changes roughly 73% of matched-galaxy class assignments and reduces the in-window void volume fraction from 17.6% to 0.75%. This demonstrates that the canonical labels primarily trace survey selection and boundaries, not a stable physical cosmic web. The canonical T-Web results should not be presented as physical robustness evidence; the analysis should be rebuilt from the outset with survey randoms, appropriate boundary treatment, and adequate grid resolution.

[MAJOR] Sections XII B–C and Appendix B, theoretical interpretation: no quantitative bounce or inflation model is connected to the measured projected CW/CCW statistic, and projected winding is observer-dependent rather than a direct intrinsic three-dimensional chirality observable. The manuscript provides no transfer function from a primordial parity-violating field to galaxy spin, viewing orientation, morphology selection, and the DESIVAST contrast. In addition, for a pseudoscalar ϕ, the two parity-odd contractions in the proposed toy operator multiply to a parity-even quantity, so the asserted parity character is not established. Claims of constraints on bounce/inflation physics and the stated ≳25Mpc/h model scale should be removed or replaced by a covariant model with a derived observable prediction.

[MAJOR] Sections II, XIII, and Appendix A, dependence on Paper IV: the per-galaxy labels, training construction, pseudo-label provenance, calibration, and principal validation data originate in an unpublished companion manuscript carrying an arXiv placeholder. The present appendix is not an independent validation of those inputs. Review of this paper must be coordinated with Paper IV, with a stable archival catalog and weights available before acceptance, including independent test-set construction and checks for training/validation overlap and environment-dependent classification error.

[MINOR] Sections III and XV, sample definition: the chirality sample permits SPECTYPE=QSO as well as GALAXY, although the physical observable is spiral-galaxy winding. The manuscript should report the number of QSO-classified objects in every primary sample and demonstrate that excluding them leaves the result unchanged.

[MINOR] Organization and statistical language: the primary analysis appears only in Section VIII after extensive discussion of a known selection-contaminated secondary classifier. The manuscript should be substantially shortened, lead with the DESIVAST estimator, move exploratory T-Web/Tempel/ASTRA material to supplementary material, and consistently distinguish “failure to reject” from evidence of environment independence and observed point-estimate ranges from confidence bounds.

(3) The central qualitative claim—no detected void/non-void dependence in the current classifier labels—is supported, but the advertised 0.9-pp classifier-label limit and 2.26-pp physical-chirality limit are not supported by the present analysis.

