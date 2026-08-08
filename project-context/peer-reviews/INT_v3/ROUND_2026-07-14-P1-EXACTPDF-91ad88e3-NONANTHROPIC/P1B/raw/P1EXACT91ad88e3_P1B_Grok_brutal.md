# P1B P1EXACT91ad88e3 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1B/frozen/arxiv/paper1b_mcmc_companion.pdf` md5=246b407b pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 140.7s

---

**Referee Report**

**Paper:** Reproducible Cosmological Proxy and Pipeline Checks… (P1B, commit 91ad88e3, 21 pp.)

**Classification of findings**

**P1B-E1 (ESSENTIAL)**  
Section I (p. 1) and abstract: “This paper reports three limited numerical studies… It does not implement, test, or verify a torsion-modified cosmology.” The entire manuscript is framed as a reproducibility companion whose scientific claim is that it finds *no* evidence for the theory advertised in the title and companion Paper I(a). PRD requires a demonstrable advance in understanding; a 21-page technical note whose principal result is “our null proxies are consistent with null” does not meet that bar.

**P1B-E2 (ESSENTIAL)**  
Abstract (p. 1) states “11.6 % of fixed-coupling draws and 6.1 % of broad-coupling draws within the published 1σ band.” No table, figure, or equation in the body (Secs. VI–VII, App. C) shows the Monte-Carlo integration that produces these exact percentages. The numbers are therefore untraceable and unverifiable from the supplied material.

**P1B-E3 (ESSENTIAL)**  
Abstract and Sec. III (p. 3) quote one-sided 95 % upper limits \(\Delta N_{\rm eff}<0.31\) (full-tension) and \(<0.40\) (Planck+BAO+SN). These are obtained only after an *ad-hoc* post-processing renormalization that discards the \(\Delta N_{\rm eff}<0\) tail and rescales the surviving weights so the integral equals unity. No justification is given for why this procedure is statistically preferred to the standard two-sided credible interval or to the raw chain quantiles. The quoted limits are therefore not reproducible from the published chains without undocumented post-processing.

**P1B-E4 (ESSENTIAL)**  
Sec. IV and Fig. 3 (pp. 7–8) report pipeline-recovery biases of \(-0.032^\circ\) and \(-0.040^\circ\). These numbers are obtained with an *unweighted* \(\chi^2\) estimator on foreground-free synthetic skies. The text explicitly states that the inverse-variance-weighted estimator used in the published birefringence analyses shifts the bias by \(\sim 12\%\). The headline numbers in the abstract are therefore not the ones that would be obtained with the analysis actually applied to real data.

**P1B-M1 (MAJOR)**  
The manuscript is 21 pages long. The claimed contribution consists of (i) a stock-CAMB run with one extra parameter, (ii) 500 Monte-Carlo realizations on synthetic skies, and (iii) a standard ALP MCMC. No new observable, no new likelihood, no new theoretical prediction. Recommended maximum length for such a technical note is \(\leq 8\) pages (including appendices).

**P1B-M2 (MAJOR)**  
Multiple load-bearing statements rely on the companion Paper I(a) whose arXiv identifier is still placeholder “[arXiv:XXXX.XXXXX]”. A standalone reader cannot reconstruct the minimal-contact-operator derivation, the \(\rho_{\rm tor}/\rho_{\rm rad}\) scaling, or the BBN suppression argument. The paper therefore fails the standalone-reader test.

**P1B-M3 (MAJOR)**  
Table II and Fig. 1 present joint posteriors that include the SHOES \(M_B\) anchor and the DES-Y3 \(S_8\) Gaussian prior. The text never quantifies the shift in \(\Delta N_{\rm eff}\) or \(H_0\) when these external anchors are removed. The reader cannot judge whether the quoted consistency with \(\Delta N_{\rm eff}=0\) is driven by Planck or by the tension-relieving datasets.

**P1B-N1 (MINOR)**  
Caption of Fig. 2 states “No evidence for a recombination-era \(\Delta N_{\rm eff}\) shift appears in this stock-CAMB proxy run.” The sentence is repeated almost verbatim in the abstract and Sec. III. Redundant phrasing.

**P1B-N2 (MINOR)**  
Several axis labels in the corner plot (Fig. 1) use non-standard abbreviations (\(n_s\), \(\tau\)) without a legend on the same page; readers must flip to Table I.

**P1B-NIT1 (NIT)**  
Inconsistent use of “post-burn-in” versus “post-burnin” across figure captions and footnotes.

**Summary recommendation: REJECT**

The manuscript is a long technical appendix whose only scientific conclusion is that three deliberately theory-agnostic null tests return null results. It contains untraceable numerical claims in the abstract, relies on an unpublished companion for essential derivations, applies undocumented post-processing to headline limits, and reports pipeline biases obtained with an estimator that differs from the one used on real data. These defects are fatal for Physical Review D.