# INT API Review — P5 v0.1.128-2026-07-14 — gemini (gemini-3.1-pro-preview)
paper: P5  version: v0.1.128-2026-07-14  model: gemini-3.1-pro-preview
provenance: commit=44303fe32212489e9bc37aadf748d143fb5f9cac+frozen-worktree  pdf=pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf  sha256=f1ba53bf236cbaecbd7b8d3b76b46411d43bd90fb7907650a742a5b4739dcc22
modality: native-PDF (inline_data base64)
UTC: 2026-07-14T11:03:05.685908Z  |  latency: 59.2s  |  attempt: 1
usage: {"promptTokenCount": 21689, "candidatesTokenCount": 1829, "totalTokenCount": 26371, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 369}, {"modality": "IMAGE", "tokenCount": 21320}], "thoughtsTokenCount": 2853, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**CENTRAL CLAIM:** 
The author claims a strictly controlled, exploratory null detection of environment-dependent spiral galaxy chirality in redshift space. Using DESI DR1 cross-matched with an 8.47M galaxy chirality catalog, and defining environments via the DESIVAST void catalog, the void-vs-non-void clockwise fraction contrast is bounded at $\Delta f_{CW} = +0.0018 \pm 0.0023$ (stat), consistent with null parity. The claim is rigorously supported by the data and is exceptionally well-fortified against multiplicity (look-elsewhere effects). The author correctly and explicitly restricts the claim to a classifier-labelled, fixed-redshift-space test, refusing to de-attenuate the result into a physical cosmological constraint due to known limitations in redshift-space distortions (RSD) and catalog-wide monopole systematics.

**MAJOR ISSUES:**

1. **Explicit dependency on an unpublished "Paper IV" (Page 33, Section XIII & Appendix A):** 
The entire dataset (labels, catalogs) and the global monopole subtraction reference ($\Delta f_{CW} = -0.0026$) rely on a companion paper ("Paper IV") submitted concurrently to arXiv. While the author correctly points out that the two-sample primary estimand ($\Delta f_{CW}$) is algebraically invariant to a uniform global monopole shift, all one-sample diagnostic residuals (Tables VI, VII, IX, XVI) strictly depend on this external value. 
*Fix:* The editorial office must track this dependency. If peer review of Paper IV results in changes to the catalog labels or the global monopole value, the author must explicitly update the diagnostic tables in this manuscript before final publication. Add a note to the production editor regarding this linked manuscript.

2. **Unresolved Bright/Dark Target-Program Bias in the T-Web Secondary Path (Page 12, Section VI.D & Page 22, Table XII):** 
The author notes a $\approx 2.1\sigma$ sign-flip between bright and dark targets in the T-Web filament class, which is attributed to imaging-leg systematics (BGS-selection-function). The primary DESIVAST analysis is shielded from this because it is 99.1% restricted to the volume-limited BGS-bright sample. However, the author explicitly admits that "no quantitative propagation simulation or selection-function mock is shown in the present work to demonstrate that the observed $|z| \approx 2.1\sigma$ sign-flip amplitude and sign pattern are fully reproduced" by these systematics. 
*Fix:* Ensure the Abstract and Section XV (Conclusions) explicitly state that the secondary T-Web analysis contains an unresolved target-class systematic, preventing its use as a clean environmental null, thereby reinforcing why the DESIVAST path is the sole load-bearing primary constraint.

**MINOR ISSUES:**

1. **Presentation of the $\approx 0.9$ pp non-probabilistic quadrature (Page 22, Table XI & Abstract):** 
The author is careful to state in the text and table caption that the $\approx 0.9$ pp quadrature is heterogeneous and "explicitly non-probabilistic." However, readers often skim tables and abstracts. Combining bounding excursions, geometry effects, and counting intervals in quadrature looks identical to a standard $1\sigma$ systematic error budget. 
*Fix:* Add a bolded, explicit warning in the Table XI caption: "**DO NOT interpret this quadrature scale as a $1\sigma$ confidence interval or a calibrated coverage bound.**"

2. **$k=5$ NN Density Proxy is a 2D Projection (Page 10, Section VI.C):** 
The angular separation to the $k=5$ nearest spiral is used as a "projected-density proxy." The matched catalog has a long redshift tail extending to $z=3.83$. An angular NN search over a deep lightcone is heavily diluted by chance line-of-sight projections, making it a very weak proxy for true 3D overdensity. 
*Fix:* Add a sentence in Section VI.C clarifying that the $k=5$ proxy is strictly a 2D line-of-sight integrated metric, which dilutes genuine 3D environmental contrasts compared to the 3D T-Web/DESIVAST metrics.

3. **RSD Anisotropic Deformation (Page 34, Section XIII):** 
The author bounds RSD scalar displacements using a FoG Monte Carlo and a first-order Zel'dovich reconstruction (finding a negligible $0.024$ pp shift). However, they acknowledge that anisotropic eigenvalue deformation (which shifts T-Web class boundaries) is "not separable from the sweep-induced shift without a reconstructed-position rerun."
*Fix:* The Abstract currently states "its anisotropic RSD channel remains unquantified." This is slightly ambiguous. Update the Abstract to read: "the T-Web anisotropic RSD deformation channel remains unquantified," clarifying that this limitation specifically affects the T-Web cosmic-web finder, whereas the DESIVAST void-membership is bounded by the Zel'dovich reconstruction.

**REPRODUCIBILITY AND STATISTICAL CHECKS:**

*   **Arithmetic and Estimator Checks:**
    *   *Table X (Primary Estimand):* Void $n=57,081$, $n_{CW}=28,339$. $f_{CW} = 28339 / 57081 = 0.49647$. Correct. Non-void $n=253,276$, $n_{CW}=126,202$. $f_{CW} = 126202 / 253276 = 0.498278$. Correct. 
    *   *Difference:* $\Delta f_{CW} = 0.498278 - 0.496470 = 0.001808$. The quoted $+0.0018$ is exact.
    *   *Standard Error:* $\sqrt{(0.25/57081) + (0.25/253276)} = 0.002316$. The quoted $SE = 0.0023$ and $z = 0.001808 / 0.002316 = 0.78$ are exact.
    *   *Table V (T-Web Void counting):* Void $n=428, n_{CW}=207 \implies f_{CW}=0.4836$. $\sigma_{\text{from half}} = (207 - 214) / (0.5 \times \sqrt{428}) = -0.676$. The quoted $-0.68$ is exact.
    *   *Multiplicity (Bonferroni-5):* For $\alpha=0.05$ over 5 tests (two-sided), the threshold is $z = \Phi^{-1}(1 - 0.025/5) = 2.5758$. Quoted as $2.58$. Correct.
    *   *Multiplicity (Bonferroni-9 Phase 2):* Threshold is $z = \Phi^{-1}(1 - 0.025/9) = 2.77$. Correct.

*   **Statistical Logic Check:** The subtraction of the catalog-wide monopole ($\Delta f_{CW} = -0.0026$) via $\sigma_{pred} = 2 \cdot \Delta f_{CW} \cdot \sqrt{N}$ correctly propagates the fractional offset to a standard normal scale for the one-sample tests. The author correctly identifies that $\Delta f_{CW}$ between environments naturally cancels this global offset, preserving the integrity of the two-sample null tests even if the monopole estimate shifts in future data releases.

*   **Provenance:** The manuscript sets a platinum standard for reproducibility. Appendix D and Table XXII provide exact file paths, git tags (`v0.1.128-2026-07-14`), random seeds (`20260515`), and SHA-256 hashes for all intermediate datasets and analysis drivers. While the external data (Paper IV catalog) cannot be verified from this PDF alone, the methodological scaffolding provided is exhaustive.