# P1B auto-2026-06-05_1717pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7193 chars)
**Wall time**: 369.7s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

I have read the full manuscript, audited the numerical statements against the body text, and checked internal arithmetic, dimensional consistency, and statistical methodology as requested. Below I list all issues found, classified and with required fixes.

ESSENTIAL

- P1B-E1 (Sec. IV, pp. 5–6): β estimator and SNR not defined
  Quote: “Injecting the spectator-ALP fiducial β = 0.27° recovers β̂ = 0.238° (pipeline-recovery SNR = 20.32).”
  Problem: The paper never defines the β estimator (e.g., the EB-based quadratic estimator, its ℓ-weighting, treatment of bandpowers, and normalization) nor the variance used to compute “SNR.” Without a declared estimator and variance model (noise-only vs. noise+CV), the recovery/bias/SNR figures are not reproducible or auditable.
  Required fix: Provide the explicit β estimator formula used (e.g., the standard small-angle EB estimator: β̂ ∝ Σℓ (2ℓ+1) Cℓ^EB/Wℓ with the normalization Wℓ and binning), the ℓ-range and bin weights, and the definition of SNR (is it |mean(β̂)|/std(β̂) across MC, or mean/SEM?). State whether the MC variance includes CMB cosmic variance (currently it does not—the sky realization is fixed). Report the MC mean and standard deviation of β̂ for each injection and the standard error on the mean; plot the distributions or provide a table.

- P1B-E2 (Sec. V A, p. 6; Table II caption, p. 4; throughout): Dataset-version inconsistencies and incorrect/insufficient citations
  Quotes:
  • “We analyze four dataset combinations: (1) Planck 2018 NPIPE [17]…”
  • Table II caption: “DESI DR2 BAO + Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native + DES-Y5 + Pantheon+.”
  • Sec. V A point (2): “+DESI 2024 DR1 BAO [18]”; elsewhere, DR2 is used.
  Problems:
  - “Planck 2018 NPIPE” is internally contradictory. “2018” (PR3) and “NPIPE/PR4” are distinct releases; Ref. [17] is PR3 A6 and does not document NPIPE/PR4. If PR4/NPIPE is used at low-ℓ and CamSpec at high-ℓ, both must be properly cited with correct versions.
  - DESI BAO is alternately called DR1 (2024) in Sec. V A and DR2 in Table II/body text. DES S8 is invoked as “DES Y3 S8” in Sec. V A, while Table II uses “DES-Y5” (SN). These need to be made consistent and precisely referenced.
  Required fix: For each reported chain, list an unambiguous dataset stack in the paper (not only in a repository README): exact Planck release(s) and likelihood names/versions, DESI data release and paper, Pantheon+ reference, DES-SN5YR (if used) or DES Y3 S8 prior (if used), SH0ES prior (Riess 2022). Add the correct PR4/NPIPE references if used for low-ℓ and high-ℓ (CamSpec-NPIPE, if applicable) or adjust text to PR3 with proper CamSpec reference. Align DR1 vs DR2 everywhere. Align DES Y3 vs Y5 everywhere and cite appropriately.

- P1B-E3 (Sec. III, pp. 3–4; Sec. III, p. 4; Ref. [15] entry, p. 10; Abstract footnote a, p. 1; Sec. III, p. 4): Presence of internal process/version-review language and placeholders
  Quotes:
  • “An earlier count erroneously quoted ‘98.6% quintom-B’ weight…”
  • “This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood…”
  • “the prior caveat promised a Savage-Dickey ratio…”
  • Ref. [15]: “…the value used at L256/L416 of P1B…”
  • Abstract footnote a: “The repository README is the authoritative source for the dataset attribution in the executed pipeline.”
  Problems: PRD articles must not include internal revision history, reviewer exchanges, line-number references, or assertions that a repository README is “authoritative.” The paper itself must be authoritative and free of process chatter/placeholders.
  Required fix: Remove all internal/version-history/reviewer-response phrasing and any references to line numbers (“L256/L416”) or to promises made earlier. Replace “the repository README is the authoritative source” with a complete, self-contained dataset description inside the paper (see P1B-E2).

- P1B-E4 (Sec. III, footnote 1, p. 3; Conclusions, p. 8; Table I, p. 3): Inconsistent claim that the Planck-only run is “reported separately in Table I”
  Quotes:
  • Footnote 1: “The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating samples, is reported separately in Table I…”
  • Conclusions: “…an additional 114,992-sample Planck-only run is still accumulating … and is reported separately in Table I…”
  Problem: Table I contains only two columns (Full-tension; Planck+BAO+SN). The claimed Planck-only run is not reported there.
  Required fix: Either add the Planck-only column to Table I with all metrics or delete both statements claiming it is “reported separately in Table I” and clearly state that it is not tabulated.

- P1B-E5 (Sec. IV, p. 5): Beam model for Commander CMB map is not correctly specified; potential mismatch
  Quote: “The Planck Commander Q/U maps are provided at Nside = 2048 with the Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz); we degrade to Nside = 512… NaMaster’s NmtField is initialized with beam = b^Planck_ℓ w^pix_ℓ.”
  Problem: The Commander CMB map is a CMB component-separation product with an effective beam not equal to the single-frequency 143 GHz Gaussian beam. Using 5′@143 GHz as the beam can bias deconvolution. No justification or reference for the adopted beam is provided.
  Required fix: Specify the exact effective beam for the Commander CMB map used (provide reference or the beam transfer function used), and update the pipeline description accordingly. If an approximate Gaussian was used, quantify the induced bias on β̂ via MC and include it in the systematic floor.

MAJOR

- P1B-M1 (Sec. IV, pp. 5–6): Purification and E→B leakage control inadequately documented
  Quote: “spin-2 B-mode purification (purify b=True, purify e=False) … suppress E→B leakage … mask uses C2 apodization at 2° scale.”
  Problems: The specific purification options and their impact on EB leakage require evidence. The “C2 apodization” is not defined or referenced. No quantitative leakage residuals or null tests are shown.
  Required fix: Define “C2 apodization” (or cite NaMaster documentation precisely). Provide a leakage test: e.g., inject pure-E skies (β=0) and show the distribution of β̂; or report EB residual spectra pre/post-purification. Include a plot or table quantifying leakage and its contribution to the quoted 0.032–0.040° bias.

- P1B-M2 (Sec. IV, p. 6): Bias characterization is asserted without uncertainty; amplitude-dependent component not quantified
  Quote: “The pipeline-recovery bias is Δβ̂ = 0.032° at β = 0.27° and Δβ̂ = 0.040° at β = 0.342° … a relative ∼12% amplitude-dependent component.”
  Problem: No uncertainties are reported on the bias estimates. With 500 MC realizations and a fixed-sky setup, the standard error on the mean should be quoted. The 12% “amplitude dependence” needs a test across at least 3–4 injection amplitudes with uncertainties.
  Required fix: Report mean ± SEM of β̂ for each injection amplitude. If claiming amplitude dependence, test multiple β values and fit a slope with uncertainty; otherwise, rephrase this as a qualitative observation.

- P1B-M3 (Sec. III, p. 3; Fig. 1 caption, p. 5; Sec. V A, p. 6): Full-tension combination contents not precisely enumerated in the paper
  Quotes:
  • Abstract/throughout: “full-tension dataset combination includes the SH0ES H0 prior … and DES Y3 S8.”
  • Fig. 1 caption: “over Planck+BAO+SN+H0+S8.”
  Problem: The exact S8 prior used (central value, covariance) and its reference are not specified in the paper text near the full-tension results; similarly, the exact SH0ES prior form (is it the Riess 2022 H0 Gaussian via MB, as said elsewhere?) should be clearly summarized in the main text for reproducibility without following a repository.
  Required fix: In Sec. V A (or Table I caption), explicitly list the S8 prior used (DES Y3 value and its uncertainty), the SH0ES prior form and parameterization (e.g., MB with mean −19.253, σ=0.027, via H0.riess2020Mb mapping), and the precise BAO and SN datasets.

- P1B-M4 (Sec. III, pp. 3–5; Sec. V B, p. 6): Frequentist “σ” distances used as “headline results” for w0 and wa without a dedicated, robust model-comparison analysis; chain also unsamples ΛCDM
  Quote: “The headline result is w0 = −0.812 ± 0.044 (+4.3σ from −1) and wa = −0.667 ± 0.186 (−3.6σ from 0)… robust ln B computation is left to a follow-up analysis.”
  Problem: The chain does not sample the ΛCDM point, by authors’ own admission, and a Bayes factor is not computed. While the authors include many caveats, the text still elevates the tail distances to a “headline result,” which risks misinterpretation as model preference absent evidence calculations. This is a methodological companion; either move the w0wa topic to the companion paper with its own robust evidence computation, or downweight it here.
  Required fix: Demote the w0wa “headline result” in this paper and confine it to a short, clearly marked methodological sanity-check paragraph with the existing caveat (unsampled LCDM point; tail distance only; no Bayes factor). Alternatively, provide a small nested-sampling (e.g., MultiNest) evidence computation on the same stack sufficient to quote a preliminary ln B with error bars.

- P1B-M5 (Sec. III, p. 4): SH0ES tension arithmetic is mixed across chains; clarify per-chain values
  Quotes:
  • “The full-tension chain returns H0 = 67.69 ± 1.06 … exhibiting the canonical 3.6σ Hubble tension…”
  • Elsewhere H0 = 67.185 ± 0.455 is quoted (DR2 + CMB + SN, no SH0ES).
  Problem: The 3.6σ figure is correct for the full-tension chain (difference 5.35; σcomb ≈ 1.48; ~3.6σ). But the narrative alternates between chains. Readers need a clean separation of which σ applies to which chain.
  Required fix: Add a compact table or bullet list that, for each dataset combination, reports H0, its σ, and the tension in σ with SH0ES (or “N/A” if SH0ES prior is included). Keep these distinct in text.

- P1B-M6 (Sec. VI, pp. 6–7; Appendix C, p. 9): ALP likelihood construction insufficiently specified
  Quote: “Planck PR4 + ACT DR6 EB-spectrum likelihoods … combined with shared calibration covariance.”
  Problem: This is not a standard Cobaya likelihood; details are missing. The shared calibration covariance between experiments must be provided or referenced with numbers; otherwise the βALP and βfree results cannot be independently verified.
  Required fix: Provide either (i) a brief technical appendix with the EB likelihood functional form, the employed bandpowers, covariance matrices, and the inter-experiment calibration covariance terms, or (ii) a precise citation to a public likelihood package release identical to what you use, with version and DOI.

- P1B-M7 (Sec. IV, p. 5): Code options are mis-typed and/or ambiguous
  Quote: “purify b=True, purify e=False”
  Problem: NaMaster options are purify_b and purify_e. As written, it is ambiguous whether these are typos or a paraphrase.
  Required fix: Use the exact NaMaster option names (purify_b, purify_e) and state their boolean values.

MINOR

- P1B-m1 (Abstract footnote a, p. 1): Repository-README authority claim
  Quote: “The repository README is the authoritative source for the dataset attribution…”
  Fix: Replace with a statement that the paper itself provides a complete dataset description (see P1B-E2), with the repository as a convenience, not an authority.

- P1B-m2 (Sec. IV, p. 5): fsky value lacks derivation
  Quote: “fsky = 0.32”
  Fix: State the mask source and sky fraction computation (e.g., HEALPix pixel count after apodization thresholding), or provide the exact number of unmasked pixels at Nside=512.

- P1B-m3 (Sec. IV, p. 5): “Conservative worst-case bias check” characterization of noise
  Quote: “ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check).”
  Problem: At Nside=512 and ℓmax=1024 over 32% sky, ACT polarization noise ≲10 μK·arcmin is not necessarily “worst-case,” and the Commander beam usage may dominate. The adjective is unnecessary and possibly misleading.
  Fix: Remove “conservative worst-case” or justify it quantitatively (e.g., compare to Planck NPIPE polarization noise at the used multipoles).

- P1B-m4 (Sec. VI, p. 7): Units and constants in Eq. (3)
  Quote: “β ≈ αEM × 8/(4π) × 1.07 ≈ 0.29°.”
  Comment: The computation is consistent (0.000581 × 8.56 = 0.00497 rad = 0.285°). Add a parenthetical “(in radians, β ≈ [αEM/(4π)] Caγ Δφ/fa)” to make units explicit.

- P1B-m5 (Sec. III, p. 5): Figure 1 caption dataset naming
  Quote: “Planck+BAO+SN+H0+S8.”
  Fix: If this is the “full-tension” combination, label it as such and ensure exact dataset versions are listed in the main text (P1B-E2/P1B-M3).

- P1B-m6 (Appendix A, p. 8): Runtime claims
  Quote: “∼4–12 h per configuration on 4 CPU cores.”
  Comment: This is fine but not necessary for PRD; optional.

- P1B-m7 (Acknowledgments, p. 8): AI assistant mention
  Quote: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant…”
  Comment: PRD has no formal prohibition, but this is unusual. If retained, add a statement that all scientific inferences and code were verified by the author and that no proprietary models were used to generate results.

NITS

- P1B-n1 (Typos/formatting, multiple): Use consistent hyphenation and symbols (e.g., TT/EE vs TT+EE; low-ℓ vs lowl). Replace unicode en dash/em dash with commas where it improves readability in equations/parameters.
- P1B-n2 (Reference formatting, p. 10): Several references include commentary and internal notes (e.g., [15] “the value used at L256/L416 of P1B”). Remove all commentary; keep standard citation style only.
- P1B-n3 (Terminology): Define “quintom-B” when first used or avoid ad hoc labels.
- P1B-n4 (Clarity): In Sec. VI, the paragraph mixing βALP and βfree MCMC is confusing (βfree is said to be fitted in the same three configurations with Caγ fixed, which is irrelevant if β is free). Separate the model-dependent (Caγ fixed; m, θi sampled) and model-independent (β-only) fits cleanly, with their respective sample counts and diagnostics.

Arithmetic/consistency checks performed

- Table I values are self-consistent: S8 from σ8 and Ωm matches within rounding; ΔNeff and H0 values match abstract.
- Burn-in/sample arithmetic: 176,240×0.7=123,368; 132,949×0.7≈93,064; sum ≈216,432 (matches text).
- SH0ES tension for full-tension chain: ΔH0=5.35; σcomb ≈ 1.48 → 3.6σ (as claimed).
- MB–H0 degeneracy constant: −28.571 (Riess-anchor) vs −28.416 (chain mean) → Δ=0.155 mag; 0.155/0.049 ≈ 3.16σ (matches text).
- Planck NPIPE β=0.30±0.11 → 2.73σ; ACT DR6 0.215±0.074 → 2.90σ; inverse-variance combo 0.241±0.061 → 3.93σ (matches).
- ALP birefringence normalization: α/(4π)=5.81×10^−4; CaγΔφ/fa≈10.3 for β=0.342° (correct).

Length and scope

For a “technical verification companion,” the manuscript is acceptable in length (10 pages). However, the inclusion of an extended w0wa analysis as a “headline result” dilutes the paper’s stated scope (ΔNeff proxy + NaMaster validation + ALP-consistency). Either compress the w0wa content to a short methodological note with strong caveats (preferred here) or move it to the main paper with a proper evidence computation.

Summary recommendation
MAJOR REVISIONS

The manuscript contains several essential reproducibility and presentation issues that must be addressed before it meets PRD methodological standards. In particular, the β estimator/SNR definition and Commander beam treatment must be specified; dataset versions and citations must be made internally consistent; internal process/reviewer language must be removed; and the contradictory Table I reference must be fixed. With these corrected, and with clearer documentation of the EB likelihood used in the ALP fits, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

- P1B-E6 (Sec. IV, Table II caption p. 4; Sec. V A p. 6; χ2 breakdown p. 4): Simultaneous use of two supernova compilations without stated cross-covariance
  Quote: Table II caption lists “DESI DR2 BAO + Planck … + DES-Y5 + Pantheon+,” and the χ2 breakdown shows a single “SN 3043.0 ± 1.6 DES-Y5 + Pantheon+.”
  Problem: DES-SN5YR (DES-Y5) and Pantheon+ are not statistically independent; combining them requires a joint covariance accounting for shared calibration/standardization systematics and overlapping low-z anchors. The manuscript provides no cross-covariance or justification that double-counting is negligible.
  Required fix: Either (i) analyze DES-Y5 and Pantheon+ separately and report separate chains, or (ii) provide the explicit joint SN covariance and a citation describing its construction. If neither is available, remove the combined-SN chain/result from the paper.

- P1B-E7 (Appendix B/Table III, p. 10; Sec. IV, pp. 5–6): Promised “MC bias table” not present
  Quote: Claims table says “β̂NaMaster = 0.238° (500-MC) … MC bias table,” but no such table appears in the paper.
  Problem: The paper cites a non-existent table; readers cannot verify the per-injection mean, standard deviation, SEM, or per-bin contributions.
  Required fix: Add a table (or figure) listing, for each injected β, the MC mean(β̂), std(β̂), SEM, and any bin-by-bin contributions; or delete the “MC bias table” claim and fold those numbers into the main text.

MAJOR

- P1B-M8 (Sec. IV, pp. 5–6): Simplified noise model may invalidate the quoted SNR/bias without justification
  Quote: “500 MC realizations … at ACT-noise level ΔP = 10 μK·arcmin … on the Commander CMB-only map.”
  Problems:
  - The MC uses homogeneous white noise, not the anisotropic noise properties of Planck/ACT (scan strategy, hit-count, and 1/f). Over fsky=0.32 with a complex mask, anisotropy can couple to EB and affect β̂ bias/variance.
  - No justification is given that homogeneous noise is adequate for the quoted few-hundredths of a degree bias.
  Required fix: Justify the white-noise approximation quantitatively (e.g., compare to an anisotropic noise MC based on realistic hit maps), or incorporate an anisotropic noise model. Update the bias/systematic floor accordingly.

- P1B-M9 (Sec. IV, p. 5): Map downgrade procedure not specified; potential aliasing bias
  Quote: “We degrade to Nside=512 and apply the corresponding pixel window function.”
  Problem: Down-grading a high-resolution Q/U map to Nside=512 without describing pre-smoothing to the target beam can alias small-scale power into large-scale EB, biasing β̂. The text does not state whether the original beam was deconvolved/reconvolved to a common beam before ud_grade, nor how band-limits were enforced.
  Required fix: Describe the exact downgrade path (healpy.ud_grade vs spherical-harmonic smoothing; deconvolution/reconvolution beams; bandlimit). Quantify the impact on β̂ in MC and include it in the systematic error budget.

- P1B-M10 (Table II, p. 4): χ2 contributions lack degrees-of-freedom/context
  Quote: “χ2BAO 10.6 ± 1.8; χ2CMB 10983.9 ± 5.3; χ2SN 3043.0 ± 1.6.”
  Problem: Without the number of data points and nuisance-parameter penalties per block, these χ2 values are not interpretable (good/bad fit cannot be assessed). This is especially important given the apparent DES-Y5+Pantheon+ combination.
  Required fix: Provide the number of data points, effective DoF (after nuisance parameters), and p-values for each block and total; clarify whether χ2 includes priors.

- P1B-M11 (Sec. V A, p. 6; Appendix A, p. 8): Mixed software versions without per-result attribution
  Quote: “Cobaya (v3.5 original; v3.6.1 verification).”
  Problem: It is unclear which results derive from which Cobaya version, and whether CAMB versions, Planck likelihood builds, and nuisance-parameter sets were identical. This impairs reproducibility and can lead to small but non-negligible shifts (e.g., in τ, ns).
  Required fix: For every reported chain, state the exact software versions (Cobaya, CAMB, likelihoods), commit hashes if applicable, and confirm that the quoted numbers are from the same vetted version (preferably v3.6.1). If not, re-run to unify.

MINOR

- P1B-m8 (Sec. III, p. 4): Agreement with SH0ES quoted using posterior σ of MB while the prior is active
  Quote: “MB = −19.263 ± 0.049 … agreeing with the Riess+2020 SH0ES value … at 0.2σ.”
  Problem: The “0.2σ” uses the posterior σ (0.049) of a chain that already includes the SH0ES prior; this is not a meaningful external-agreement metric. Relative to the SH0ES prior width (0.027), the offset is ~0.37σ.
  Fix: Either remove the “0.2σ” phrasing or compute agreement relative to the prior uncertainty (and state that the prior is included).

- P1B-m9 (Sec. III, p. 5): “Independent cross-validation” with Liu et al. lacks the comparison numbers
  Quote: “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.”
  Problem: The Liu et al. best-fit values and uncertainties are not quoted, so the claimed σ-level cannot be checked.
  Fix: Provide the Liu et al. H0 and σ8 values with uncertainties and show the arithmetic of the σ differences.

- P1B-m10 (Sec. III, p. 5; Sec. VII, p. 8): CMB-S4 σ(Neff) ≃ 0.03 stated without citation
  Fix: Add a CMB-S4 forecast citation (e.g., CMB-S4 Collaboration white paper/Science Case) and align the quoted precision with that reference.

- P1B-m11 (Sec. IV, p. 5; Reproducibility paragraph): Path-like internal directory names in the main text
  Quote: “pipelines/h200_results/pod1_namaster_umap_2026-04-29/”
  Fix: Move such implementation paths to Appendix A or the repository README; keep the manuscript text free of environment-specific paths.

NITS

- P1B-n5 (Multiple): “NPIPE 2018” phrasing recurs inconsistently
  Problem: “Planck 2018 NPIPE” mixes PR3 (2018) with NPIPE/PR4 terminology. Even when you fix global dataset citations (see original P1B-E2), ensure all stray instances are corrected for internal consistency.

- P1B-n6 (Sec. IV, p. 5): Spacing and symbol consistency for Cℓ and EB/TB conventions
  Fix: Use consistent formatting for Cℓ, TT/TE/EE/BB/EB throughout; avoid mixing “TT+EE” and “TT/EE” within the same paragraph.

- P1B-n7 (Sec. VI, p. 7): “strictly requires unrotated galactic foregrounds” wording
  Comment: The Minami–Komatsu approach leverages foreground EB/TB to break α–β degeneracy; “strictly requires” is a stronger phrasing than needed. Consider softening to “is commonly broken using foreground EB/TB information, which a CMB-only Commander map removes.”

Explanation

These issues were not covered in the initial review and emerged on a second pass focused on arithmetic comparability, dataset independence, and methodological completeness. The most critical new finding is the apparent simultaneous use of DES-Y5 and Pantheon+ without a stated joint covariance (P1B-E6), which must be addressed to avoid double-counting supernova information. The NaMaster downgrade/noise modeling (P1B-M8/M9) are also important for the credibility of the quoted β̂ bias at the 0.03–0.04° level. The remaining items improve clarity, reproducibility, and presentation.