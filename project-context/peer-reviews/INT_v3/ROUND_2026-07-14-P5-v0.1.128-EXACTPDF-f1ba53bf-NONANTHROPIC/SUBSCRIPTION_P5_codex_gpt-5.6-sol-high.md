VERDICT: MAJOR REVISIONS

CENTRAL CLAIM: The narrow claim—a post-hoc, classifier-labelled, fixed-redshift-space non-detection—is supported by the displayed primary counts: for the footprint-restricted DESIVAST sample, \(f_{\rm CW}^{\rm void}=28339/57081=0.496470\), \(f_{\rm CW}^{\rm nonvoid}=126202/253276=0.498279\), and \(\Delta f_{\rm CW}=+0.001809\) with \(z_\Delta=0.781\). The abstract and conclusions appropriately disclaim a physical-handedness, real-space, or cosmological-model constraint. However, the manuscript repeatedly describes this as a controlled environmental-dependence test even though its primary non-void control is explicitly not completeness-, redshift-, imaging-, or morphology-matched. That unresolved selection problem, together with incomplete row-level provenance for the highlighted covariance result, prevents acceptance in its present form.

MAJOR ISSUES:

1. PDF pp. 19–21, §VIII B–C, Table X; p. 35, §XV. The primary estimator is \(\Delta f_{\rm CW}=f_{\rm CW}^{\rm nonvoid}-f_{\rm CW}^{\rm void}\) on \(n_{\rm void}=57{,}081\) and \(n_{\rm nonvoid}=253{,}276\), under the null \(\Delta f_{\rm CW}=0\). The “footprint” is constructed from the union of hole-sphere angular discs and their radial span. The manuscript itself correctly discloses that this is not the published DESIVAST/BGS completeness mask, does not use DESI randoms, and does not match fibre completeness, imaging depth, radial selection, morphology, or classifier confidence; it further states that the appropriate logistic/IPW or matched-control analysis is deferred. This is not a demonstrated arithmetic error, but it is an unresolved limitation of the load-bearing estimand: near-identical bright/dark fractions control only one confounder, while the raw two-sample interval has no protection against differential redshift/sky/imaging/classifier-label structure that could create or mask an environmental contrast. Required fix: construct a same-selection-function control using the official DESIVAST/BGS mask and DESI randoms, or matched/IPW controls in redshift, angular position/imaging leg, magnitude/size/morphology, and classifier confidence. Report the adjusted void coefficient or contrast with angular/redshift block- or void-cluster-robust uncertainty. The adjusted result must replace or directly accompany Table X as the primary estimator.

2. PDF p. 19, §VIII B (“Cluster-aware sampling sensitivity”); p. 39, Appendix C. The abstract-highlighted region bootstrap assigns galaxies to 3,756 nearest maximal-void centres and reports \(SE=0.002328\), but Appendix C discloses that the DESI FITS used for this computation has a different SHA-256 from the earlier sidecar and that the historical per-row snapshot is unavailable. Reproducing aggregate parent and arm counts does not establish identical galaxy identities, coordinates, void assignments, or bootstrap-region membership, which are precisely the inputs determining spatial covariance. This is a demonstrated provenance gap, not evidence that the reported SE is numerically false. Required fix: archive and checksum the exact derived bootstrap input table, including stable object ID, coordinates/redshift, chirality label, void/control flag, and region ID; pin it and the driver to an immutable commit/DOI; then regenerate the bootstrap result. If the exact row-level input cannot be recovered, the precise bootstrap claim should be removed from the abstract and treated as non-reproducible sensitivity evidence.

MINOR ISSUES:

1. PDF pp. 20–22, Eq. (4) and Table XI. The “Counting CI (2σ)” entry of 0.44 pp is not the primary Table X uncertainty. From the displayed primary integers, \(SE=0.23166\) pp, so \(2SE=0.4633\) pp and the normal 95% half-width is 0.4540 pp. The 0.44 pp value corresponds approximately to the unrestricted \(k=20\) sensitivity control. Correct the primary entry and recompute the quadrature summary; using the primary uncertainty gives approximately 0.95–0.96 pp, which rounds to 1.0 pp rather than 0.9 pp at one decimal.

2. PDF p. 7, §V B. The quoted 0.77/0.63/0.50/1.12/0.86 pp values are called simultaneous “half-widths,” but they are maximum absolute interval endpoints relative to zero. For example, the V2-REVOLVER GALZONE interval is \([-1.12,+0.38]\) pp, whose half-width is 0.75 pp, not 1.12 pp. Rename these “simultaneous absolute bounds” and separately state the actual interval half-widths.

3. PDF p. 17, §VIII. The statement that moving the estimator by at least 0.5 pp “would require” more than 1.3 times the observed membership reassignment extrapolates linearly from a maximum 0.37 pp shift. No monotonic or linear relation between reassignment count and chirality contrast is demonstrated; adversarial or spatially structured flips need not follow that scaling. Remove this claimed bound or support it with targeted/injection simulations.

4. PDF pp. 21–22, §VIII B and Table XII. The dark-program contrast is \(215/469=0.45842\) versus \(2955/5845=0.50556\), giving a 4.71 pp difference and \(|z|=1.97\). Calling it simply “not a sign” is too categorical for a nominal two-sided \(p\approx0.049\), even though it is low-powered and not multiplicity-corrected. Report the exact statistic and corrected interpretation as a suggestive but non-significant residual.

5. PDF p. 26, Fig. 8. The top Mollweide panel is embedded inside an extraneous Cartesian frame with 0–1 ticks, and labels/colorbar elements crowd the space between panels. Re-render the figure without the outer axes and verify label separation.

6. PDF p. 35, §XV. The five-member Bonferroni family is fully tabulated in Table XIV, not Table XIII. Also replace “consistent with parity” for the two-sample result with “consistent with zero void/non-void contrast”; parity against \(f_{\rm CW}=0.5\) and environmental homogeneity are different null hypotheses.

7. PDF pp. 6 and 16. The manuscript sometimes calls VoidFinder, V2-REVOLVER, and V2-VIDE “three independent void-finding algorithms,” although the footnote correctly explains that REVOLVER and VIDE are two pruning prescriptions within the same ZOBOV/V2 watershed family. Use “three definitions spanning two algorithmic families” consistently.

REPRODUCIBILITY AND STATISTICAL CHECKS:

- SHA-256 was verified before review as exactly `f1ba53bf236cbaecbd7b8d3b76b46411d43bd90fb7907650a742a5b4739dcc22`. The PDF reports 41 pages, and all 41 rendered pages were visually inspected.

- Primary Table X recomputation: \(28339/57081=0.49646993\), \(126202/253276=0.49827856\), \(\Delta=0.00180863\), unpooled binomial \(SE=0.00231659\), \(z=0.78073\), and normal 95% CI \([-0.0027318,+0.0063491]\). These agree with the displayed rounded values.

- Unrestricted \(k=20\) control recomputation: \(28286/56981=0.49641108\), \(309173/621964=0.49709147\), \(\Delta=0.00068039\), \(SE=0.00218841\), \(z=0.31090\), and 95% CI \([-0.0036088,+0.0049696]\). These also agree.

- The Table X one-sample statistics recompute to \(-1.687\), \(-1.733\), \(-1.713\), and \(-4.588\) for the exact void, exact footprint-control, \(k=20\) void, and unrestricted non-void rows, respectively.

- From Table XX’s exact cells, Pearson \(\chi^2=3.54688\) with 3 d.o.f. and \(p=0.31473\), agreeing with \(3.55\) and \(0.31\). From Table XXI, \(\chi^2=4932.51\) and Cramér’s \(V=0.077958\), agreeing with the displayed 4933 and 0.078.

- The Bonferroni thresholds recompute correctly: 2.5758 for \(K=5,\alpha=0.05\); 2.7729 for \(K=9,\alpha=0.05\); 3.0902 for \(K=5,\alpha=0.01\); 2.4977 and 3.0233 for \(K=4\) at \(\alpha=0.05\) and 0.01; and 4.0679 for \(K=1054,\alpha=0.05\).

- The reported bootstrap-to-binomial SE ratio is arithmetically consistent: \(0.002328/0.0023166\approx1.005\), with variance ratio approximately 1.010. The bootstrap replicates and region assignments cannot be verified from the PDF alone.

- The quadrature inputs printed in Eq. (4) sum in squares to 0.8979 pp², whose square root is 0.9476 pp. The operation is correct for the printed inputs, but the primary counting term is misidentified as noted above. The manuscript properly states that this calculation is not a likelihood, confidence interval, or calibrated systematic-error model.

- For 0 successes in 6 trials, the one-sided 95% Clopper–Pearson upper bound is \(1-0.05^{1/6}=0.3930\), agreeing with 39%.

- The classifier attenuation arithmetic is correct: \(2(0.6991)-1=0.3982\). However, the PDF’s void-stratified error-asymmetry interval is much wider than the reported environmental contrasts. The manuscript explicitly acknowledges that environment-dependent relabelling at the headline scale is not excluded; this is a disclosed limitation rather than a demonstrated error.

- The PDF alone cannot verify the DESIVAST membership joins, V2/GALZONE \(z_\Delta\) values, permutation \(p\)-values, regression coefficients, randoms-weighted T-Web rebuild, RSD reconstruction, 20,000 bootstrap replicates, classifier validation, repository contents, hyperlinks, claimed immutable tag, or pending Zenodo archive. Exact CW counts are not printed for four of the five Table XIV estimators, preventing full independent recomputation of their contrasts and uncertainties from the PDF.

- Apart from Fig. 8’s extraneous axes, no clipped equations, overflowing tables, overlapping columns, missing pages, or unreadable references were found in the rendered manuscript.