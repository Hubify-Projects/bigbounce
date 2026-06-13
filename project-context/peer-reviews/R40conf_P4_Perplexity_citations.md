# P4 R40conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/chirality_catalog_paper.pdf` md5=1e2501db pages=23
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 39.1s

---

I can’t perform the requested **citation-forensics audit to PRD standards** from the material provided, because I do **not** have the rendered PDF pages or live arXiv/NASA ADS search results for the cited works. The text you supplied is enough to identify many **internal consistency and provenance problems**, but not enough to verify every bibliography entry against external databases or to inspect figures/tables “as rendered” page by page.

Below is a **limited referee-style audit of the supplied manuscript text only**. I am treating all findings as based on the excerpted paper text and am **not** using the reviewer metadata block as paper content.

- **P4-E1** — **Abstract / p.1** — The abstract makes multiple load-bearing numerical claims that are not consistently backed by the body as written.
  - Problem: “**+0.41σ** … and … **p = 0.31**” is presented as a primary result, but later the same estimator appears as **0.58σ** and **0.70σ** in robustness checks, and the text repeatedly warns these are distinct null procedures. The abstract still reads like a single significance result.
  - Required fix: Rewrite the abstract so each statistic is tied to one named estimator/null, with explicit non-comparability language at every juxtaposition.

- **P4-E2** — **Abstract / p.1** — The statement “**a block-bootstrap WLS template fit disfavors a clean cosmological dipole at the 1.7% reference amplitude at z ≈ −18**” is not self-contained.
  - Problem: The body later gives multiple exclusions: “**z ≈ −18.1**,” “**−16.9**,” “**−18.4**,” “**−19.4**,” plus a naive “**−264.5**” that is superseded. The abstract does not specify which estimator convention is meant.
  - Required fix: State the exact estimator, block scale, and covariance convention used for the quoted exclusion.

- **P4-E3** — **Abstract / p.1** — The claim “**99.32% of the raw pre-MASTER ℓ = 1 power**” is numerically ambiguous.
  - Problem: Later the manuscript says the same null reproduces **99.32%** of the observed pre-MASTER power, but also gives a separate post-MASTER claim of only **∼12%** reproduction. The abstract does not clearly separate pre- and post-deconvolution diagnostics.
  - Required fix: Explicitly separate pre-MASTER and post-MASTER diagnostics and name the exact field convention for each.

- **P4-E4** — **Abstract / p.1** — The paper claims “**equivariant-catalog high-confidence dipole fit (confidence > 0.6; N ≈ 9.5 × 10^5 spirals)**” but later the HC-broad sample is **949,584** and the unthresholded full spiral sample is **3,201,160**.
  - Problem: The abstract uses an approximate count without stating whether it is exactly the **HC-broad-0.6** subset or a rounded value.
  - Required fix: Replace the approximation with the exact count and a single consistent sample definition.

- **P4-E5** — **Abstract / p.1** — The phrase “**This ℓ = 1 observable is parity-even**” is asserted without definition in the body of how the observable transforms.
  - Problem: The manuscript later says parity-odd signal lives in the monopole and even-ℓ multipoles, which is a nonstandard statement in this context and appears internally inconsistent.
  - Required fix: Provide a precise symmetry argument or remove the claim.

- **P4-M1** — **p.2, Training Labels** — The arithmetic for training labels is not cleanly presented.
  - Problem: The paper gives **6,637 + 17,153 + 2,000 = 25,790**, then says after flip augmentation the pool is **26,616**, a difference of **826**. That difference is said to arise “entirely” from horizontal flips applied only to the training split, but the 80/20 split over the source manifest is not derived in-text.
  - Required fix: Show the exact split arithmetic and the number of flipped examples added to training.

- **P4-M2** — **p.2, Training Labels** — The manuscript states “**17,153/25,790 = 66.5%** derive from CE-ResNet predictions.”
  - Problem: This ratio is correct numerically, but the sentence then implies validation metrics “therefore partially reflect agreement with CE-ResNet rather than independent ground truth.” That inference is fine, but the paper does not quantify the extent of leakage or its effect on reported metrics.
  - Required fix: Add a quantitative ablation showing performance with and without CE-ResNet-derived labels.

- **P4-M3** — **p.3, Significance conventions** — The paper mixes multiple null conventions side by side and sometimes relies on “not directly comparable” language only in footnotes or nearby prose.
  - Problem: PRD-level rigor requires the caveat at every juxtaposition. The text repeatedly violates this requirement in figures, captions, and body prose.
  - Required fix: Add the “not directly comparable” caveat in every sentence or caption where distinct nulls appear together.

- **P4-M4** — **p.4, Eq. (2)** — The equivariant averaging equation is written in a way that is not clearly dimensionally or notationally defined.
  - Problem: The notation “\(P_{CW}^{eq} = \frac12 P_{CW}^{orig} + P_{CCW}^{flip}\)” appears to omit parentheses/swap operator clarity; the same holds for the other channels.
  - Required fix: Rewrite Eq. (2) with an explicit swap operator \(S\) and consistent vector notation.

- **P4-M5** — **p.4, Catalog tiers** — The statement “**Catalog B (Platt-calibrated, +0.4% excess)**” is unsupported in the excerpt.
  - Problem: No derivation or table is shown for this calibration shift.
  - Required fix: Provide the calibration method, calibration set, and the exact before/after counts or fractions.

- **P4-M6** — **p.5, Table II** — The global CW fraction table contains a likely internal inconsistency with the narrative.
  - Problem: Table II says Catalog C has **0.497353(279)**, i.e. **−0.265%** deviation, while the body later refers to **0.4974 ± 0.000279** and a “**0.26%** CW-bias residual.” These are consistent only if rounded carefully, but the paper alternates between “0.26%” and “0.265%” without stating the rounding convention.
  - Required fix: Standardize the reported precision and state the rounding rule once.

- **P4-M7** — **p.5, Table II / narrative** — The phrase “**3.2 × 10^6 / 1.27 × 10^5 ≈ 25**” is fine arithmetically, but the paper uses it as a sample-extension argument for comparison to Iye et al. without matching selection function.
  - Problem: Raw sample-size ratios do not justify comparative significance claims.
  - Required fix: Replace with a matched-footprint or matched-selection-function comparison, or downgrade the claim.

- **P4-M8** — **p.6, Section IV B** — The sentence “**a constant monopole cannot bias the uniform-weight real-space dipole estimator**” is asserted as a direct generative result but the scope is too broad.
  - Problem: The later text explicitly says multiplicative depth- or morphology-coupled modulations are not probed.
  - Required fix: Narrow the claim to the exact null tested.

- **P4-M9** — **p.7, Dipole Analysis** — The quoted primary dipole amplitude “**4.4 × 10−3 toward (l, b) = (293°, 12°)**” is presented without uncertainty on direction or amplitude.
  - Problem: The text says the axis is unconstrained under the null, but the amplitude is still treated as a load-bearing result.
  - Required fix: Give a confidence interval or state explicitly that amplitude is not physically interpretable beyond the null-consistent summary statistic.

- **P4-M10** — **p.7, Dipole Analysis** — The manuscript quotes multiple null values for the same primary estimator: **0.41σ**, **0.58σ**, **0.70σ**.
  - Problem: The paper says these come from distinct null procedures and are not comparable, but the prose still uses them in a cumulative robustness chain.
  - Required fix: Separate the estimators into a table with one row per null and no mixed-language comparison.

- **P4-M11** — **p.7–8, confidence-threshold sweep** — The sweep claims “**z = +4.3, +4.1, +4.0 at cuts 0, 0.4, 0.5** … collapsing to z = +0.41, +1.14, +0.51 at 0.6, 0.7, 0.8.”
  - Problem: The transition is used to attribute the excess to the low-confidence tail, but the manuscript does not provide the underlying counts per threshold in the main text.
  - Required fix: Add the per-threshold sample sizes and effect sizes.

- **P4-M12** — **p.8, MASTER channel** — The paper states “**C1meas = 2.348×10−5** against a 500-MC null with mean **1.71×10−6** and σ = **2.99×10−6**, i.e. +7.28σ**.”
  - Problem: This arithmetic is consistent, but later Table III gives **24.74 × 10−6**, mean **1.93 × 10−6**, σ **3.12 × 10−6**, and z **+7.31** for the apodized case. The manuscript needs to make explicit that these are different footprints and normalizations.
  - Required fix: Add explicit normalization labels in the main text sentence, not only in Table III.

- **P4-M13** — **p.9, Table III** — The canonical unapodized row uses a different field normalization than the apodized row, but the caption still risks inviting direct comparison.
  - Problem: The table partially warns against cross-comparison, but the body repeatedly compares **+3.64σ** and **+7.28σ** in the same sentence.
  - Required fix: Move the non-comparability warning into the main text and remove mixed-significance phrasing.

- **P4-M14** — **p.9–10, Table IV / Fig. 8** — The monopole-only null “reproduces **99.32%** of the observed pre-MASTER pseudo-Cℓ power” but then “post-MASTER decoupled null gives **σ = +4.84**.”
  - Problem: The paper does not clearly explain why the pre-MASTER null is informative once MASTER deconvolution is applied.
  - Required fix: State the logic chain with exact estimator definitions and explain what scientific inference each stage supports.

- **P4-M15** — **p.10, Section IV D** — The text says the “**observed C1data** is a fixed scalar,” so “**mean of ratios** is identical to ratio of means.”
  - Problem: This is only true because the denominator is fixed, but the paper should state this explicitly to avoid confusion with stochastic denominators elsewhere.
  - Required fix: Add a one-sentence proof or explanatory note.

- **P4-M16** — **p.12, Section V A** — The comparison to Shamir reports a “**factor of ∼ 6–12**” discrepancy using “**pipeline best-fit 0.32% WLS template amplitude**.”
  - Problem: This depends on Shamir’s claimed **1.7%–4.0%** range, but the paper cites that range without a matched-footprint reanalysis.
  - Required fix: Downgrade from quantitative exclusion to qualitative inconsistency unless a matched-footprint estimator is shown.

- **P4-M17** — **p.12, Section VI A** — The Fisher derivation has an algebraic issue in presentation.
  - Problem: The equation shown as \( \sigma(A) = \sqrt{3/N_{\rm spiral}} = 2\sqrt{3}\,\sigma(f_{CW}) \) is dimensionally confusing as written because the intermediate relation between \(A\) and \(f_{CW}\) is not carefully derived in-text.
  - Required fix: Rewrite the derivation step by step, defining \(A\) and \(f_{CW}\) consistently.

- **P4-M18** — **p.13, Table V** — The injection-recovery probabilities are given only at coarse grid points and then used to bracket **A95**.
  - Problem: The text properly says the bracket is not measured, but later treats **A95 ∈ (1.0%, 1.5%]** as if it were a quasi-estimate.
  - Required fix: Keep the bracket language throughout and do not convert it into a point estimate.

- **P4-M19** — **p.13, Table V / text** — The axis protocol note says the sweep uses **θ-uniform** axes, while a separate spot check uses area-uniform axes.
  - Problem: The paper says the two agree “within MC error,” but no quantitative comparison interval is provided in the main text.
  - Required fix: Add a numerical comparison and, ideally, standardize on one convention.

- **P4-M20** — **p.14, Section VI B** — The claim that the dipole observable is parity-even and that the parity-odd signal lives in the monopole and even-ℓ multipoles is conceptually suspect.
  - Problem: As written, this is either nonstandard terminology or a mistake in parity assignment.
  - Required fix: Re-derive the parity classification carefully or remove the claim.

- **P4-M21** — **p.14, Section VI C** — The manuscript says the “**citable artifact**” is the versioned release tag because the DOI has not yet been minted.
  - Problem: This is acceptable for a draft, but for a PRD submission the reproducibility handle should be frozen, and the stated commit hash should map unambiguously to the submitted version.
  - Required fix: Provide a frozen archive DOI or repository snapshot hash tied to the submission.

- **P4-M22** — **p.15, Appendix A** — The analysis-footprint definitions are overly tangled.
  - Problem: The text alternates between **canonical mask**, **analysis footprint**, **Nall ≥ 1**, and **spirals-only** conventions. This makes the reader reconstruct which field is being used in each estimator.
  - Required fix: Add a single explicit notation table for all masks, weights, and normalizations.

- **P4-M23** — **p.15, Appendix A** — The “**effective sky fraction**” formula is given, but the paper also says the values “depend on pixel resolution” and then asserts invariance under rescaling.
  - Problem: Those are different notions and need clearer separation.
  - Required fix: Distinguish resolution dependence from normalization invariance.

- **P4-M24** — **p.16, Table VII** — The table lists **Canonical (Nspiral(p) ≥ 10)** sky fraction **0.49005** and **Footprint (Nall ≥ 1)** **0.494**, plus weighted/apodized values.
  - Problem: The table is useful, but the main text later uses **0.4801** for the HC canonical mask without a clear bridge.
  - Required fix: Explain the HC-mask re-evaluation explicitly in the body where the number first appears.

- **P4-M25** — **p.17, Appendix B** — The claimed validation accuracy **93.7%** and CW per-class validation accuracy **94.9%** are not accompanied by confusion matrices for the validation split.
  - Problem: The paper gives the GZ1 confusion matrix but not the validation confusion matrix.
  - Required fix: Provide the validation confusion matrix and class-wise F1 or recall.

- **P4-M26** — **p.17, Appendix B** — The statement that T1 “**validates the implementation**” rather than being an independent statistical test is correct, but the table still lists it as a passing bias-hardening test.
  - Problem: This could mislead readers about the evidentiary weight of the test suite.
  - Required fix: Separate implementation checks from substantive bias tests in the table.

- **P4-M27** — **p.17–18, Appendix B** — The flip-probability recovery paragraph is alarming and underexplained.
  - Problem: The manuscript says “**for 2.9% of rows ... a recovered flip probability falls outside [0, 1] by up to 0.09**,” then claims this is not float32 rounding and affects raw-catalog rows only.
  - Required fix: This needs a full technical explanation, because probabilities outside \([0,1]\) are not acceptable without a clear postprocessing definition.

- **P4-M28** — **p.18, Table IX** — The confusion matrix arithmetic should be checked against the stated total.
  - Problem: The entries sum to **240,919** exactly, which is good, but the text claims the training-overlap galaxies “do not change the matrix at the quoted precision” without showing the comparison.
  - Required fix: Provide the disjoint-subset matrix or a delta table.

- **P4-M29** — **p.18–19, Appendix C** — The phrase “**the principled look-elsewhere correction, incorporating the 648 tested directions and their correlations exactly**” is too strong.
  - Problem: A Monte Carlo max-statistic null approximates the correction; “exactly” is too strong without a proof of exact combinatorial equivalence.
  - Required fix: Replace “exactly” with “by Monte Carlo max-statistic calibration” unless a formal proof is provided.

- **P4-M30** — **p.19–20, Appendix D / Table X** — The WLS fit has severe conditioning issues.
  - Problem: The text says the nuisance subspace is exactly rank-8 and the condition number is **4.5×10^16**. That is numerically unstable and demands stronger justification for the quoted fit coefficients and \(z\)-values.
  - Required fix: Provide a stability analysis, regularization sensitivity, and an explanation of why the fit is still trustworthy.

- **P4-M31** — **p.20, Table X** — The caption says the leg fraction templates are “nearly collinear,” yet the table reports enormous naive \(z\)-values for some nuisance terms and “not individually meaningful.”
  - Problem: The fit is likely underdetermined in the nuisance sector.
  - Required fix: Report marginalized posterior uncertainties for the parameters of interest only, and suppress misleading nuisance \(z\)-scores.

- **P4-M32** — **p.20, Appendix D** — The direct cross-spectrum claim \(r_{\ell=2} = -0.65, z=-2.89\) is used as a discriminator.
  - Problem: The paper does not provide the exact null distribution or whether this is one-sided or two-sided in the narrative.
  - Required fix: State the null, sidedness, and whether the result is corrected for multiple multipoles.

- **P4-M33** — **p.21, Appendix E** — The edge-on contamination estimate “**65.7% of visually identified edge-on systems receive CW/CCW labels rather than not spiral**” is a potentially important systematic, but the follow-up effect on the primary result is only estimated qualitatively.
  - Problem: The manuscript says the effect is a “**5–8% sensitivity penalty**” but does not propagate it into the primary uncertainties.
  - Required fix: Quantify the impact on the dipole limit and report the recalculated threshold.

- **P4-M34** — **p.21, Data Availability** — The repository statement is inconsistent.
  - Problem: The text says the repository state is commit **53b41d12** and release tag **v2026.04**, but the “immutable archival snapshot” will only be deposited at journal submission and the DOI has not been minted.
  - Required fix: Provide a frozen archival DOI or a fully immutable submitted snapshot, not a provisional tag alone.

- **P4-M35** — **p.21, Data Availability** — The HuggingFace catalog URL text is malformed in the excerpt.
  - Problem: The displayed text appears split as “datasets/bamfai/galaxy- chirality- catalog.”
  - Required fix: Ensure the manuscript contains the correct repository identifier and that the submitted PDF does not have line-break corruption in the citation handle.

- **P4-M36** — **p.22–23, References** — The bibliography is not audited here against arXiv/ADS, but the internal evidence already suggests several entries need external verification.
  - Problem: The paper relies on exact arXiv IDs, years, journal citations, and claimed statistics from prior work, but I cannot verify them from the supplied text alone.
  - Required fix: Check every reference against arXiv and ADS for title, authors, venue, year, DOI, and any quoted statistical values.

- **P4-M37** — **Cross-paper / body text** — The manuscript repeatedly uses internal bookkeeping language such as “**artifact c12 r24conf local batch.json**,” “**pipeline**,” “**canonical provenance**,” and “**version-stamp commit**.”
  - Problem: Much of this is acceptable in an appendix, but some of it reads like internal audit prose rather than paper prose and will not survive PRD scrutiny unless properly encapsulated.
  - Required fix: Move all audit-log references into a concise reproducibility appendix and keep the main paper free of implementation bookkeeping.

- **P4-M38** — **Cross-paper / body text** — The paper’s abstract says the catalog is “**publicly released with model weights and reproducibility scripts**,” while the Data Availability section says the archive DOI is not yet minted.
  - Problem: This is not a contradiction by itself, but it is incomplete for a submission claiming public release.
  - Required fix: Specify the exact frozen artifact that corresponds to the submitted manuscript.

## Summary recommendation
**MAJOR REVISIONS**

This manuscript contains a technically interesting result, but the supplied text shows too many places where the same quantity is reported under multiple null conventions, several load-bearing claims are not self-contained, the WLS/template machinery appears numerically fragile, and the provenance/reproducibility section is not yet publication-grade. I would not recommend acceptance until the manuscript is simplified, all significance conventions are made unambiguous, the conditioning and null calibrations are tightened, and every bibliography entry plus quoted prior statistic is externally verified against arXiv/ADS.