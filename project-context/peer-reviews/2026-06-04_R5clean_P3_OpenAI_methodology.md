# P3 2026-06-04_R5clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 31.9s

---

Referee report on P3 (“Spectrally Unusual Sources at Scale …”)  
Round 2026-06-04_R5clean – Methodology / statistics / internal-consistency audit  
Paper length: 49 pp (PRD methods norm 15–30 pp)

--------------------------------------------------------------------
FINDINGS  
Keys: ESSENTIAL (E), MAJOR (M), MINOR (m), NIT (n)

E-1  (Sec. I, Abstract p. 1)  
Problem “largest-scale application … 378 280 unique anomalies” is asserted before the paper shows that the 378 280 arithmetic is correct and free of ACT contamination; yet ACT counts are still quoted in several later sentences.  
Fix Present the logically final deduplicated number only after Sec. II.D has been read, and delete every sentence that still cites the cross-transfer 319 443 or “with-ACT 378 480” counts.

E-2  (whole MS)  
Problem Thresholds differ by survey (DESI S>5 absolute; SDSS/LAMOST top-1 %; Planck top-1 %; eROSITA top-298, etc.).  Anomalies are therefore on incommensurable scales but are compared, stacked and fed to a single Fisher pipeline as if homogeneous.  
Fix Define one canonical decision rule (e.g. 99.5 % per-survey quantile, or S>5 after z-standardisation) and rescore every survey, or prove analytically that the present non-uniform thresholds do not bias (i) the cross-survey coincidence statistics, (ii) the α measurement and (iii) the Fisher information.

E-3  (§II.D Step 6, Table I)  
Problem SIMBAD–unmatched fractions are reported graphically (Fig. 9) although authors concede later (p. 19) that these overstate novelty by ~5.6×.  The graph is therefore misleading.  
Fix Replace Fig. 9 with genuine-novelty fractions (17.8 % for the DESI top-1000 and analogous numbers for all other surveys) or remove the figure.

E-4  (§V)  
Problem σ(fNL) forecasts mix two incompatible error propagations: (a) quadratic Fisher form 1/σ 2 = F0 + cα 2 and (b) linear extrapolation σ = 8.98 – 3.66α.  The linear propagation is kept in many places even after being declared “unphysical”.  
Fix Delete every σ(fNL) obtained with the linear formula, recompute the 1 σ and 95 % intervals with the quadratic form only, and propagate those consistently through the text, tables and figures.

E-5  (§V last ¶)  
Problem The catalogue’s single cosmological “result” is a Landy–Szalay α = 0.19 ± 0.65 measured without a pre-registered scale choice, without blinding and after multiple sub-sample explorations.  This is undisclosed look-elsewhere tuning.  
Fix State explicitly which angular bins, random catalogue depth and jack-knife partition were defined in advance (show a dated protocol) or label the result exploratory and remove it from the abstract and conclusions.

E-6  (§VI.D(i))  
Problem The DESI 5-fold stability test re–scores the training spectra (i.e. in-sample).  That cannot demonstrate robustness to genuine out-of-distribution data.  
Fix Repeat the 5-fold experiment on a hold-out draw that was never used for training any fold and report that Jaccard.

E-7  (CMB sections, pp. 13–15)  
Problem The 100 % injection-recovery at 5 σ on Planck patches is numerically impossible given the reported clean-validation 99 th-percentile MSE of 0.519 and planted values 0.80–1.78 – that range does not cross five standard-deviations consistently.  
Fix Provide the exact σval used, show a histogram of planted-versus-clean scores and re-compute the recovery fractions reproducibly.

E-8  (§III.F, Appendix F)  
Problem ACT DR6 is “formally quarantined” yet is still used in the Planck×ACT null-test and in several narrative statements.  Including a data set that fails the own quality gate violates the declared protocol.  
Fix Remove every quantitative use of ACT or, if the null-test is kept, perform a Path-C-compliant native ACT retrain that passes both gates.

E-9  (all tables & text)  
Problem Four-significant-figure central values (e.g. α = 0.19, σ=0.65 is later quoted as 0.19±0.65) give a false impression of precision.  
Fix Round every scalar so that no more than two significant digits are retained when the quoted uncertainty is >20 %.

E-10 (whole MS)  
Problem Version-control artefacts still present: “fw6_stability.json”, “wave14_injection_recovery_results.json”, etc.  
Fix Delete every internal path/filename from the public manuscript or move them to a data-release README.

E-11  (length)  
Problem 49 pages is ∼2× a PRD methods paper.  The ACT appendix, full image galleries (10 pages) and extended training logs belong in the data-release, not the manuscript.  
Fix Cut to ≤30 pages (main text 25 pp + ≤5 pp appendices).

M-1 (Sec. II.B)  
Problem The canonical anomaly score S is defined using the validation split of the training pool.  If the validation distribution is non-representative, S becomes survey-dependent and non-transferable.  
Fix Show that µval, σval computed on the training validation split match those from a 1 % random draw of the full survey (KS test p > 0.05) for all three spectroscopic surveys.

M-2 (§III.C)  
Problem 77 905 SDSS cross-transfer anomalies collapse to 12 when a native model is adopted – a 6500× swing.  This shows that the autoencoder is dominated by spectrograph-to-spectrograph calibration, not intrinsic spectra.  
Fix Move every scientific conclusion based on the cross-transfer SDSS catalogue to an appendix or discard; base all cross-survey rates on the native SDSS catalogue only.

M-3 (§III.D)  
Problem LAMOST native re-score retains 113 342 “exploratory” anomalies even though injection-recovery is only 5.8 % at 5 σ.  
Fix Provide a convincingly clean subset (e.g. S > 10 & continuum-dip recall > 50 %) and move the rest to a technical appendix; otherwise the LAMOST tier must not be counted in the 378 080 point-source headline.

M-4 (§IV.B)  
Problem The χ2 sky-uniformity test assumes Poisson with equal expected counts per HEALPix pixel, ignoring very inhomogeneous selection functions.  
Fix Compute the expected map by convolving survey masks with depth maps and redo the test, or drop the claim.

M-5 (Sec. V.A, Bayesian factors)  
Problem Per-bin KDEs are treated as independent, but correlation between free-spectrum bins is known to be non-negligible (NANOGrav docs).  
Fix Re-evaluate the Savage-Dickey ratio using the released 30×30 covariance or explicitly show that off-diagonal terms change ln B by <1.

M-6 (data availability statement)  
Problem “Repository private pending acceptance” does not meet PRD reproducibility.  
Fix Upload all catalogues, weights and scripts to a citable public Zenodo or DOE-Data server now, not post-acceptance.

m-1  Duplicate phrase examples: “canonical canonical-mask” (§I p.3), “prior prior fiducial” (§V).  
m-2  Several equations lack numbers; Eqs. (1) and (2) are numbered but later references “Eq. 2” do not compile.  
m-3  Mismatched parentheses in footnote symbols (Table I legend lines 28-33).  
m-4  Cite the exact DR numbers (e.g. DESI DR1.1) once; the phrasing oscillates between DR1, DR 1, DR 1.0.  
m-5  Fig. 12 y-axis label missing units (should be σ(fNL)).  
n-1  Typo “Celeast” → “Celest” p. 17.  
n-2  Page-wide equations overrun margins in two-column proofs.

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The catalogue is potentially valuable, but the manuscript in its current form is methodologically inconsistent, exceeds PRD length norms and mixes incomparable statistical thresholds.  The key cosmological numbers rely on post-hoc choices and on a CMB component that fails the authors’ own quality gates.  All essential items (E-1 – E-11) must be corrected; the paper should be shortened and the anomaly-definition made uniform before the work can be re-evaluated.