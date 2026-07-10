# INT API Review — P5 v0.1.116-2026-07-10 — openai (gpt-5.5)
paper: P5  version: v0.1.116-2026-07-10  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-10T22:35:08.183554Z  |  latency: 58.5s  |  attempt: 1
usage: {"input_tokens": 74270, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2710, "output_tokens_details": {"reasoning_tokens": 1355}, "total_tokens": 76980}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Section II / Appendix A / Paper IV dependence: the analysis depends on per-galaxy chirality labels from a concurrently submitted companion paper with placeholder arXiv/DOI information, so the label provenance, training set, accuracy, and systematic calibration are not independently refereeable from the present manuscript as submitted.

2. [MAJOR] Abstract / Sections VIII, XII, XV: the headline wording repeatedly implies an environmental or physical spiral-chirality null, but the demonstrated result is narrower: a classifier-labelled CW-fraction null in fixed redshift space under specific DESIVAST membership definitions; the title, abstract, and conclusions must be rewritten to avoid overclaiming.

3. [MAJOR] Section V B / multiplicity and post-hoc primary choice: the “primary” DESIVAST path is explicitly post-hoc after a broad analysis tree, and the Bonferroni-5 treatment does not control the full garden-of-forking-paths exposure for the quoted upper bounds; non-rejection across five correlated estimators is not equivalent to a pre-specified equivalence/upper-limit test.

4. [MAJOR] Sections VIII B–E / DESIVAST VoidFinder membership: the primary VoidFinder membership is an author-constructed point-in-sphere union of 101,863 holes, not an official per-galaxy VoidFinder membership; the manuscript must quantify how this construction relates to the DESIVAST void definition and either make the catalog-native GALZONE estimators primary or provide a defensible official VoidFinder membership prescription.

5. [MAJOR] Section VIII B / footprint-restricted control sample: the “DESIVAST usable footprint” is defined as the union of hole-sphere angular discs intersected with a radial span, not the DESIVAST/BGS angular-radial completeness mask or a DESI random-catalog selection function; this can bias the non-void control and is not a valid same-selection-function control as claimed.

6. [MAJOR] Table XI / systematic envelope: the ≈0.9 pp “honest systematic envelope” is an ad hoc quadrature of counting intervals and disparate systematic excursions, many of which are correlated and not probabilistic errors; it should not be presented as an effective 2σ bound without a statistical model or coverage validation.

7. [MAJOR] Sections V B, VIII D, XV: the manuscript quotes several different limiting numbers—0.44 pp counting, 0.6 pp max excursion, 0.9 pp quadrature envelope, 1.1 pp Bonferroni simultaneous bound, and 2.26 pp de-attenuated physical bound—without consistently identifying which is the primary constraint; the abstract and conclusions must state one hierarchy clearly.

8. [MAJOR] Appendix A / classifier accuracy and attenuation: the 69.91% classifier accuracy and lack of a direct void/non-void confusion matrix mean environment-dependent relabeling remains a leading systematic; the de-attenuation factor is only valid under symmetric, environment-independent errors, which is not demonstrated for the DESIVAST void contrast.

9. [MAJOR] Sections IV, VII, IX A / T-Web analysis: the manuscript itself shows that the T-Web environment labels are dominated by radial/selection-function artifacts and that randoms weighting reassigns most galaxies; therefore the T-Web sections should be sharply shortened or moved to supplementary material and not used as substantive corroboration.

10. [MAJOR] Section XIII / redshift-space distortions: the paper acknowledges that anisotropic tidal-eigenvalue RSD effects are not quantified, yet repeatedly frames results as environmental constraints; the central claim must be explicitly restricted to redshift-space catalog classifications, and any real-space interpretation should be removed.

11. [MAJOR] Units and coordinate convention in Sections IV and VIII: the manuscript alternates between “Mpc/h” and “h⁻¹ Mpc” and gives a nonstandard explanatory footnote; because DESIVAST point-in-sphere membership depends directly on coordinate units, the authors must verify against DESIVAST documentation and state a single consistent convention.

12. [MAJOR] Data/code availability Appendix D–E: a pending Zenodo DOI and repository tag are insufficient for review; all artifacts, scripts, exact catalog versions, and the companion chirality labels used for the submitted numbers must be frozen and publicly accessible at submission, not promised for acceptance.

13. [MAJOR] Statistical interpretation throughout: many statements describe “null holds” or “environment independence” from p-values above thresholds; the authors should recast these as confidence/equivalence bounds on specified estimands and avoid interpreting non-significance as proof of independence.

14. [MINOR] Abstract and introduction: the abstract is far too long and contains excessive caveats, tables, and numerical details; it should be reduced to the estimand, sample, main contrast, systematic scale, and scope limitation.

15. [MINOR] Tables XIII–XIV / cross-references: the text sometimes says the full Bonferroni-5 family is in Table XIII, but Table XIII contains only the three sphere-PIS rows; references should consistently point to Table XIV or a single consolidated primary table.

16. [MINOR] Figures 6 and 8: the Mollweide figures appear visually cluttered, with overlapping labels/color bars in Fig. 8; these need to be regenerated at publication quality.

17. [MINOR] Monte Carlo p-values: p-values from only 1000 permutations should not be quoted to excessive precision; report appropriate Monte Carlo uncertainty or fewer significant digits.

18. [MINOR] Appendix B: the toy EFT mapping is speculative, non-covariant, and not used in the empirical analysis; it should be removed or moved to clearly marked supplementary material, especially for a PRD submission.

19. [MINOR] AI-assisted methodology statement: the disclosure is acceptable, but the emphasis on AI agents is not a substitute for reproducible archived code and should be shortened.

20. [MINOR] Style and formatting: the manuscript contains numerous corrupted hyphenation/line-break artifacts, repeated caveats, and redundant restatements that substantially obscure the scientific result.

(3) The central empirical claim is supported only in the narrow sense that the submitted counts show no statistically significant DESIVAST redshift-space void/non-void dependence of the classifier-labelled CW fraction, but the broader physical chirality and environmental-independence claims are not yet supported at publication standard.