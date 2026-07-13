# EXT P4 ChatGPT — M26 (recovered orphan)

- **reviewer:** ChatGPT (Extended Thinking Pro)
- **venue prompt:** P4
- **chat URL:** https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a54ca46-d5cc-83e8-80ac-6aa145fb1c0c
- **status:** harvested-recovered (orphaned by ext_submit poll timeout; landed server-side, recovered 2026-07-13)
- **verdict (raw line 1):** REJECT

---

## Raw ChatGPT response (verbatim)

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract, title, Secs. III B and IV C — The headline null is not obtained from “8.5 million DESI galaxies” or even from the full 3.20-million-spiral Catalog C, but from the p
eq
	​

>0.6 subset of 949,584 spirals, roughly 30% of the classified spirals. The unthresholded Catalog C instead gives a z≃4.2–4.4 dipole excess. The threshold is justified in the manuscript precisely because the excess disappears at 0.6; a commit on the same analysis branch, without an independently archived pre-unblinding record, is not a credible preregistration. The cut must be defined from external validation or blinded data, the threshold scan must be included in the inference, and the title and abstract must state that the null applies only to the selected subset.

[MAJOR] Sec. III D, Fig. 7, and Sec. VI — The claim that equivariant TTA “collapses” the real-space dipole from 2.31σ to 0.41σ is confounded by changing the catalog, confidence selection, and effective mask. On the unthresholded equivariant Catalog C, the manuscript reports a larger 4.3σ excess. Catalogs A, B, and C must be compared on exactly the same galaxies, confidence criterion, pixel mask, weighting, and null realization before the change can be attributed to equivariance.

[MAJOR] Sec. VI B and Table VIII — The injection–recovery experiment injects a signal only into the already classified hard-label map. It does not propagate a dipole through the ViT, the not-spiral decision, the confidence cut, orientation dependence, or the depth-, PSF-, morphology-, and imaging-leg-dependent confusion matrix. The full-catalog mirror test merely verifies the algebraic Z
2
	​

 property imposed by Eq. (2); it is not an end-to-end dipole injection. Consequently, A
50
	​

 and A
95
	​

 are detection efficiencies for the observed-label field, not sensitivities to a physical galaxy-chirality dipole.

[MAJOR] Secs. V and VI B and Appendix D, Table XV — The quoted z≃−7.6 disfavoring of a 1.7% dipole compares A
ref
	​

=0.017 directly with the observed-label estimate A
best
	​

=0.00455. Under the manuscript’s own conservative transfer factor g=0.398, a 1.7% physical dipole would produce approximately 0.0068 in the observed field, giving only about a 1.4σ difference using σ
boot
	​

=0.00163, before additional selection and triage effects. The reported −7.6 therefore tests an undiluted observed-label template, not the claimed physical Shamir-scale signal. Moreover, equality of algebraic “asymmetry units” does not make amplitudes from different masks and estimators directly comparable.

[MAJOR] Secs. IV C–IV D and Appendix D — The data contain several highly significant coherent structures: the full-sample real-space excess, 7–8σ MASTER residuals, and a hemisphere maximum with p
LEE
	​

≤10
−4
. Roughly 47% of the harmonic residual amplitude remains unexplained by the stated forward model. Calling these results “systematics diagnostics” does not establish that they are non-cosmological. In particular, A
50
	​

 and A
95
	​

 are power thresholds, not confidence limits, so the fact that a residual lies below them does not bound its cosmological content or make it irrelevant to the null conclusion.

[MAJOR] Sec. VI A and Appendix D — The assertion that survey- or pseudo-label-induced structure can only add low-ℓ power, making the null conservative, is false. A systematic dipole is a vector and can partially or fully cancel a cosmological dipole; spatially varying confidence selection and not-spiral triage can likewise attenuate a signal anisotropically. The claim that only uniform dilution can hide a real signal is therefore unjustified. A simultaneous likelihood for cosmological and systematic dipole components is required.

[MAJOR] Sec. IV C — The primary pixel-permutation null assumes exchangeability of A
p
	​

 across pixels despite orders-of-magnitude variation in galaxy count and hence variance. It destroys the relation between noise, depth, mask geometry, and sky position. The alternative label shuffle still assumes spatially exchangeable classification errors and does not account for intrinsic spatial correlations or survey-dependent confusion. In addition, the mask N
spiral
	​

(p)≥10 is defined using classifier outputs and is therefore data-dependent. The analysis should use an independently defined survey mask and a binomial or multinomial count likelihood with explicit spatial covariance and nuisance fields.

[MAJOR] Appendix D and Fig. 10 — The NSIDE =8 block bootstrap is not a calibrated test of A=0.017. Resampling small sky blocks with replacement destroys the global coherence and fixed geometry of an ℓ=1 mode, while the tested parameter is the positive-definite norm of a three-component vector with an unspecified direction. The plotted bootstrap distribution is generated around the observed field, not under the reference-amplitude hypothesis. A valid exclusion requires parametric sky simulations under specified amplitudes and axes, followed by profiling or marginalization over direction and nuisance parameters.

[MAJOR] Appendix D, Table XV — The quantity described as a “joint nuisance-marginalized” primary fit does not include the principal PSF, depth, reddening, or measured morphology templates discussed elsewhere; its displayed design contains only dipole components, imaging-leg fractions, density, density squared, and a constant. The leg templates are also exactly rank deficient with the constant. Thus the z≃−7.6 statistic is not obtained after the systematic marginalization claimed in the abstract and discussion.

[MAJOR] Sec. II and Appendix B, Tables XIII–XIV — The external validation does not establish sub-percent spatial control. The overall three-class accuracy is 58.7%, the quoted chirality accuracy is 69.91%, and the sky-dependent confusion analysis has only two large declination cells plus confidence bins. It conditions on galaxies already retained as CW or CCW, but differential probabilities for true CW and CCW galaxies to be sent to not-spiral or to fail the confidence cut also bias the selected f
CW
	​

. A full spatially conditioned 3×3 confusion and completeness model is required, with object-level disjointness demonstrated against both the GZ1 and CE-ResNet-derived training sets.

[MAJOR] Sec. III D and Appendix B — The classifier is not adequately rotation invariant: 21.4% of per-galaxy argmax labels change between Z
2
	​

 and D
4
	​

 TTA on the tested samples. Apparent chirality is invariant under in-plane rotation, so this is a relevant physical symmetry, not merely an auxiliary stability test. Spatially varying PSF orientation or image construction can convert this dependence into a sky pattern. The production catalog should use a rotation-equivariant architecture or full rotation-averaged inference, and the effect must be measured specifically on the primary p
eq
	​

>0.6 sample.

[MAJOR] Secs. IV C–IV D, Table V, and the Conclusions — The manuscript calls the 10
4
-permutation canonical result a recomputation of the same canonical unapodized field, yet the result changes from +3.64σ with rank p=0.030 to +7.93σ with rank p=3×10
−4
. Differences in null, subtraction, or weighting may make them different estimators, but then one is not a convergence recomputation of the other. A controlled comparison holding the field, mask, weighting, subtraction, and randomization scheme fixed is needed; declaring the numbers “not comparable” does not resolve which null is scientifically appropriate.

[MINOR] Sec. VI B and Table VIII — The recovery curve uses only 100 injections per amplitude and a coarse grid around the claimed 95% crossing. Binomial uncertainty is not incorporated into the bracket A
95
	​

∈(1.0%,1.5%], and axis-averaged completeness is not a worst-direction guarantee. A substantially larger injection ensemble, finer amplitude grid, and completeness as a function of dipole direction are needed.

[MINOR] Secs. VI A–VI B and Table XV — The amplitude conventions remain internally inconsistent. Sec. VI A describes A
95
	​

≲1.5% as an f
CW
	​

-unit quantity corresponding to ≲3% in A
p
	​

, whereas Tables VIII and XV state that the injected full amplitude A is numerically identical to the A
p
	​

 dipole amplitude. The physical-threshold discussion also risks double-counting edge-on dilution after stating that the GZ1-derived transfer factor already contains such misclassification.

[MINOR] Appendix B, calibration subsection — The claimed ECE lower bounds combine the catalog-wide mean confidence, 0.951, with accuracies measured on the GZ1 cross-match. Jensen’s inequality gives the stated lower bound only when confidence and accuracy averages are evaluated on the same objects. Calibration metrics and reliability diagrams must be computed entirely on the held-out matched sample.

[MINOR] Data Availability — The analysis is tied to a mutable live main branch, while the DOI, immutable release, and exact commit hashes are explicitly still absent. All load-bearing arrays, masks, scripts, trained weights, and catalog versions must be frozen and archived before the work can be independently reproduced.

[MINOR] Sec. VI C — The discussion asserts that cosmic-birefringence and gravitational Chern–Simons mechanisms would generically produce or align a late-time morphology dipole, while simultaneously acknowledging that no transfer function is derived. Those model-specific claims should be removed or replaced by an explicit calculation; the present measurement constrains only the phenomenological projected chirality field.

(3) No—the manuscript establishes a non-detection only for a classifier-defined, data-selected observed-label subset, while the broader cosmological null, sub-percent physical sensitivity, and Shamir-scale exclusion are not supported by the present analysis. 

ext_P4_M26

