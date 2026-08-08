# P1B EXT20 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 105.4s

---

**REFEREE REPORT**

**Manuscript:** Technical Verification Companion to the ECH Spin-Torsion Program: \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model  
**Journal:** Physical Review D  
**Recommendation:** REJECT

The manuscript is a 21-page technical appendix whose primary conclusions are (i) a stock-CAMB \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) run returns a null result for extra radiation, (ii) a Monte-Carlo pipeline test recovers injected rotation angles with a known bias floor of \(\sim0.04^\circ\), and (iii) a spectator ALP can be tuned to reproduce the published WMAP+Planck birefringence angle. None of these statements constitutes a test of the Einstein-Cartan-Holst (ECH) spin-torsion framework advertised in the title. The paper repeatedly and correctly states that it does *not* test the theory (pp. 3, 4, 10, 14). Under PRD standards this is fatal: a methods/companion paper must still deliver a substantive, self-contained advance. It does not.

**ESSENTIAL findings (paper cannot be accepted without correction)**

- **P1B-E1 (Abstract, p. 1)**: The abstract opens with quantitative \(\Delta N_{\rm eff}\) posteriors (“\(-0.020\pm0.169\) full-tension”) without the explicit qualifier that appears on p. 3: “this run … carries *no torsion modifications to the Boltzmann equations*”. The abstract therefore misrepresents the scope. Required fix: rewrite the abstract to state that the reported numbers are *not* constraints on ECH.
- **P1B-E2 (Title + §I, pp. 1–2)**: The title claims a “verification companion to the ECH Spin-Torsion Program,” yet the text states the opposite (p. 3: “NOT a spin-torsion theory module”; p. 10: “Not a distinctive ECH prediction”). This is an irreconcilable framing error.
- **P1B-E3 (Fig. 2 & §III, p. 5)**: The two frozen-dataset posteriors for \(\Delta N_{\rm eff}\) are presented side-by-side with a 3.6\(\sigma\) Hubble-tension claim, yet the caption and text acknowledge they are “not directly comparable” to published sky measurements. No quantitative statement of the residual tension after marginalization over the known pipeline bias (\(\Delta\hat\beta=0.040^\circ\)) is supplied.
- **P1B-E4 (§VI, p. 10)**: The birefringence “consistency check” uses a spectator ALP whose required coupling \(C_{a\gamma}\gtrsim9\) and misalignment tuning (\(\theta_i\sim0.1\)) lie outside both the KSVZ/DFSZ range and the natural prior midpoint. The paper concedes the result is “not a distinctive ECH prediction.” No calculation demonstrates that the ECH action itself produces the observed angle; the claim is therefore unsupported.
- **P1B-E5 (Data Availability, p. 15)**: The reproducibility manifest lists HuggingFace DOIs that are still “pending.” The commit hash b22f8cc9 predates the stated paper version (v1B.0.74). These are unrecoverable artifacts under PRD policy.

**MAJOR findings (significant revision required)**

- **P1B-M1 (Length)**: 21 pages of largely negative results and pipeline bookkeeping exceed any reasonable page limit for a companion note. A letter-format version \(\leq10\) pages would be the maximum defensible length.
- **P1B-M2 (§IV, Figs. 3–4)**: The NaMaster bias floor (\(\Delta\hat\beta=0.040^\circ\)) is reported as an empirical number but is never propagated into the final \(\beta\) significance quoted from Eskilt & Komatsu. The 3.6\(\sigma\) headline therefore cannot be audited from the supplied material.
- **P1B-M3 (Table II, p. 20)**: The \(w_0w_a\) posterior is presented with a “+4.3\(\sigma\)” marginal-tail departure from \((-1,0)\). No Savage-Dickey ratio or nested-sampling evidence is computed; the \(\sigma\) value is an extrapolation distance only. This is a quantitative claim without the required effect-size statistic.
- **P1B-M4 (§II, p. 2)**: The statement that “the spin-torsion framework alone does not resolve cosmological tensions” is asserted without a single ECH-modified Boltzmann run. The null result is therefore a statement about stock CAMB, not about the theory under test.

**MINOR / NIT findings (selected)**

- **P1B-N1 (Title page)**: Date “June 14, 2026” is chronologically impossible for a submission; appears to be a preprint artifact.
- **P1B-N2 (Multiple locations)**: Repeated use of the phrase “not a … module / prediction / test” creates defensive tone and could be condensed.
- **P1B-N3 (Eq. 1, p. 7)**: The \(\chi^2(\beta)\) estimator is unweighted; the text later shows that an inverse-variance weighting changes the recovered angle by \(0.026^\circ\). This systematic should be quantified in the main text, not only in an artifact note.

**Summary recommendation: REJECT**

The manuscript does not test the ECH framework it purports to verify, repeatedly states that its own results are *not* theory tests, and presents a 21-page null-result appendix whose headline numbers are either from unmodified CAMB or from a spectator ALP tuned outside the model’s natural parameter space. Under Physical Review D standards this does not meet the threshold for publication. A substantially rewritten, condensed letter that (a) removes all ECH-specific framing from the abstract and title, (b) supplies the missing bias propagation and evidence ratios, and (c) limits itself to pipeline-validation methodology might be reconsidered, but the present document is not salvageable in its current form.