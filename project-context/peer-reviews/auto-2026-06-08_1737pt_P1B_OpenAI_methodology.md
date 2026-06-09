# P1B auto-2026-06-08_1737pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7625 chars)
**Wall time**: 319.8s

---

Referee report on: “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Methodology rigor: statistical validity, derivation chains, dimensional analysis, internal arithmetic consistency, estimator declarations, error propagation, and figure/table audit.
- I audited all quoted scalars in the abstract and conclusions against the body, recomputed σ-levels and combinations, and checked dataset/likelihood consistency.

Findings

ESSENTIAL

P1B-E1
- Location: Table II footnote (b), p. 4; main text Sec. III (Physics interpretation), pp. 3–4.
- Issue: Incorrect wpivot variance formula and inconsistent definition of ap. The text states “wpivot ≡ w0 + (1 − ap) wa with ap chosen so that w0 and wa are decorrelated in the posterior covariance: ap = 1 − Cov(w0, wa)/Var(wa). … With w0 and wa formally decorrelated at zp, σ^2_wpivot = σ^2_w0 + (1 − ap)^2 σ^2_wa = (0.0301)^2.”
  - This is not the standard decorrelation condition and omits the cross term. For w(a) = w0 + (1 − a) wa, decorrelating w(a_p) from wa requires a_p = 1 + Cov(w0, wa)/Var(wa), and
    Var[w(a_p)] = Var[w0] − Cov(w0, wa)^2/Var(wa).
  - Using your numbers σ(w0)=0.0436, σ(wa)=0.1864, σ(w_p)=0.0301 implies Cov^2/Var(wa)=Var(w0)−Var(w_p)=0.001901−0.000906≈0.000995, which cannot be reproduced by σ^2_w0 + (1 − ap)^2 σ^2_wa. The stated variance identity in the footnote is therefore wrong and the sign in ap is inconsistent with the standard definition.
- Required fix: Replace the footnote with the correct derivation. Provide the measured Cov(w0,wa) (from your chain) and explicitly compute ap, zp, and Var[w(a_p)] with the correct formula including the cross term. Re-check that wpivot = −1.0344 ± 0.0301 holds under the correct relations and adjust σ-level claims accordingly.

P1B-E2
- Location: Section V A, p. 6 vs Table II caption and header, p. 4.
- Issue: Dataset inconsistency. Sec. V A states you analyze four stacks including “+DESI 2024 DR1 BAO,” while Table II and adjacent text throughout cite “DESI DR2” (and use DES-Y5). This is not a cosmetic label—DR1 vs DR2 materially changes constraints.
- Required fix: Reconcile and standardize dataset versions across the paper. For each table/figure, state precisely which dataset release (DR1 vs DR2), which likelihood variants, and whether DES-Y3 or DES-Y5 SN are used. If multiple stacks are used, list each explicitly in the main text (not only in the repository) and ensure captions match.

P1B-E3
- Location: Figure 3 header and caption, p. 6.
- Issue: Map-product mismatch. The plot title shows “NaMaster, Planck SMICA,” while the caption and Sec. IV repeatedly state “Planck Commander map” was used. SMICA vs Commander differences (beam, residuals) are substantive; this mismatch undermines reproducibility of the pipeline validation.
- Required fix: State unambiguously which CMB map is used for each resolution point and rerun or relabel as needed. If multiple component-separation maps were used, present them separately or clearly identify the series by marker/legend. Ensure all reported recovery numbers (β̂ and biases) correspond to the stated map.

P1B-E4
- Location: Sec. III, p. 5 (MB–H0 joint-posterior offset paragraph); Sec. III, p. 3–4 (Physics interpretation paragraph and Savage–Dickey discussion).
- Issue: Review-history/internal-process prose in the body. Examples:
  - “This addresses earlier reviewer concerns…”
  - “An earlier count erroneously quoted ‘98.6% quintom-B’…”
  - “prior caveat promised a Savage-Dickey ratio…”
- Required fix: Remove all references to prior drafts, promises, reviewer concerns, or internal process. PRD articles must read as a stand-alone final scientific record.

P1B-E5
- Location: References [15], p. 11 (last lines of the ref entry).
- Issue: Reference includes an internal cross-link to another manuscript with line numbers: “the value used at L256/L416 of P1B.” This is not appropriate in a reference entry.
- Required fix: Delete the “L256/L416 of P1B” language. If the value is used elsewhere in this manuscript, cite properly in the body.

P1B-E6
- Location: Sec. IV (Pipeline configuration and Independent verification), pp. 5–6; Eq. (1).
- Issue: Primary estimator for β is not fully specified. You report “500-MC sample mean of β̂,” but do not define how β̂ is estimated per realization:
  - precise EB pseudo-Cℓ estimator (e.g., maximum-likelihood fit to Cℓ^EB with what weighting?),
  - multipole bin weights and covariance model used in the fit,
  - whether Mℓℓ′ deconvolution is inverted and how bandpower window functions enter,
  - ℓ-range exclusions (e.g., low-ℓ cuts, beam deconvolution),
  - noise model in the covariance (you inject ΔP = 10 μK·arcmin but do not specify Nℓ shape).
  Without this, the pipeline-recovery SNR and bias claims are not reproducible from the text alone.
- Required fix: Add a precise definition of β̂, including the per-realization fitting functional, weighting, ℓ-binning, covariance model, and the exact ℓ range used. Report the per-realization σ(β̂) from the 500 MCs and the SEM used to compute SNRSE.

P1B-E7
- Location: Footnote 1, p. 3.
- Issue: Misstatement about where the third (Planck-only) run is reported. The text says “is reported separately in Table I,” but Table I has only two columns (Full-tension and Planck+BAO+SN) and does not include the Planck-only run.
- Required fix: Correct the text. Either add the Planck-only column to Table I or remove the claim that it is reported there.

MAJOR

P1B-M1
- Location: Sec. IV (Bias statement), p. 6; Fig. 3 caption.
- Issue: “The bias is 0.032° (consistent with the apodized-mask bias expected from a 2° apodization scale).” No analytic expectation or citation is provided for a 0.03–0.04° leakage bias at fsky=0.32 with C2 apodization and purify_b=True. As written, “expected” is unsupported.
- Required fix: Provide either (i) an analytic estimate or (ii) a literature citation demonstrating the size of residual leakage bias under your exact mask and purify settings. Alternatively, quantify the bias empirically across multiple masks/apodizations to show stability and scale with mask properties.

P1B-M2
- Location: Sec. IV (Independent verification and footnote 3), p. 6.
- Issue: SNR definitions use nonstandard notation and are not numerically auditable from the text. You state SNRSE≈20.32 (β=0.27°) and SNRreal≈0.91 but do not report the sample standard deviation σ(β̂) across the 500 realizations or the SEM explicitly. The formula text “SNRSE ≡ β/ˆ SE(β̂) = β̂ √N/σβ̂” contains a formatting error (“β/ˆ”) and ambiguous σβ̂ (per-realization scatter or something else?).
- Required fix: Provide the numerical values of σ(β̂) and SEM(β̂) for each injected β, and cleanly define SNRSE and SNRreal with unambiguous symbols. Consider including a small table of {β_inj, mean β̂, bias, σ(β̂), SEM, SNRreal, SNRSE}.

P1B-M3
- Location: Throughout Secs. II–V.
- Issue: Dataset-stack naming and scope drift. The paper’s main thrust is a stock-CAMB ΛCDM+ΔNeff proxy on four stacks (ending with a “full-tension” stack). But Table II (a w0wa fit) uses a different stack (DESI DR2 + DES-Y5 + Pantheon+ + Planck PR4) and occupies significant space without a complete link to the ΔNeff analyses.
- Required fix: Either (i) move the w0wa analysis to a dedicated section that clearly states it is an auxiliary result (and ensure it does not confuse the ΔNeff-focused results), or (ii) integrate it with a clear rationale for its inclusion, with dataset-stack reconciliation and exact YAML summaries in the main text.

P1B-M4
- Location: Figure 2 caption and labels, p. 5; Table I, p. 3.
- Issue: Sample-count inconsistency for the full-tension chain: Fig. 2 labels “175,545 samples,” but Table I reports 176,240. The discrepancy is small but should be reconciled. If thinning or burn-in removal differs, state so explicitly in each caption.
- Required fix: Harmonize sample counts across text/figures or annotate differences (raw accepted vs post-processed counts).

P1B-M5
- Location: Sec. IV (Foreground and noise model), p. 5.
- Issue: You treat the Commander CMB map as “CMB-only” and inject ACT-level white polarization noise (ΔP=10 μK·arcmin) on top. In reality, the Commander product contains instrument noise already; adding additional noise changes the effective SNR of the map. For a pipeline-validation claim this is acceptable, but the setup should be explicit to avoid confusion.
- Required fix: State clearly whether you use a noise-subtracted template or simply treat the provided Commander Q/U as noiseless sky. If the latter, explain the motivation and show that the pipeline-recovery bias is insensitive to the assumed ΔP within a reasonable range.

MINOR

P1B-n1
- Location: Abstract and Sec. IV, pp. 1, 5.
- Issue: “published Planck/ACT DR6 2.4–2.9σ” — given your cited numbers are 0.30±0.11° (2.73σ) for Planck and 0.215±0.074° (2.90σ) for ACT DR6, “2.7–2.9σ” would be more accurate.
- Required fix: Replace “2.4–2.9σ” with “2.7–2.9σ” (or justify the 2.4 figure with a specific alternative Planck analysis).

P1B-n2
- Location: Sec. III (Planck-only run), p. 3.
- Issue: You quote R̂−1≈0.05 for the accumulating Planck-only run. While fine as a status remark, it is unusual to include unconverged chain diagnostics in the main text.
- Required fix: Either remove or move to a brief footnote clarifying that it is not used for any reported parameter inference.

P1B-n3
- Location: Throughout: MB vs Mb, capitalization and symbols.
- Issue: Inconsistent capitalization of the SN Ia absolute magnitude (MB vs Mb). 
- Required fix: Standardize to MB.

P1B-n4
- Location: Sec. V A, p. 6.
- Issue: “Planck 2018 NPIPE” mixes the 2018 parameter paper with the PR4/NPIPE data release; mildly confusing.
- Required fix: Use “Planck PR4 (NPIPE)” consistently when referring to NPIPE-era products; reserve “Planck 2018” for PR3.

P1B-n5
- Location: Sec. IV footnote 3, p. 6.
- Issue: Minor typesetting error: “SNRSE ≡ β/ˆ SE(βˆ) …”
- Required fix: Correct to “SNRSE ≡ β̂ / SE(β̂) = β̂ √N / σ[β̂].”

P1B-n6
- Location: Acknowledgments, p. 9.
- Issue: Reference to a commercial cloud instance model (“RunPod H200 instances”) is extraneous.
- Required fix: Remove hardware branding unless required for reproducibility.

NITS

P1B-N1
- Location: Abstract and Sec. VII, pp. 1, 8.
- Issue: Occasionally “Planck/ACT DR6 2.4–2.9σ [2,3];a” extra semicolon spacing/footnote marker formatting.
- Required fix: Clean punctuation/spacing around references and footnotes.

P1B-N2
- Location: Eq. (3), p. 7.
- Issue: Units implied but not stated. β is in radians in the formula, later reported in degrees.
- Required fix: Add “(β in radians)” or multiply by 180/π explicitly in the displayed equation or the surrounding text.

P1B-N3
- Location: Table III, p. 10.
- Issue: “β̂NaMaster = 0.238° (500-MC)” — add that this is for βinj = 0.27° to avoid ambiguity.
- Required fix: Append “for βinj = 0.27°”.

Checks that passed or were internally consistent
- ΔNeff posteriors in Table I match abstract/conclusions.
- H0 values match between table and abstract.
- Inverse-variance combination of Planck and ACT DR6 birefringence (0.241 ± 0.061°, 3.94σ) recomputes correctly and is explicitly marked as auxiliary due to shared systematics.
- Product Caγ Δφ/fa≈10.3 from βobs=0.342° with αEM/(4π)≈5.8×10−4 is numerically consistent.
- Eq. (3) yields β≈0.29° for Caγ=8 and Δφ/fa≈1.07 (in radians) — dimensionally and numerically consistent.
- “309,189 raw samples” total matches 176,240 + 132,949 and the burn-in arithmetic is consistent with the stated 30% removal and getdist thinning for Fig. 1.

Recommended page-length
- The manuscript is concise (11 pages) for a methods companion. No length reduction is necessary if the ESSENTIAL/MAJOR issues are resolved.

Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains several critical methodology and presentation issues that must be corrected for PRD: (i) an incorrect and misleading derivation for the pivot parameter variance (and inconsistent ap definition), (ii) key dataset inconsistencies (DR1 vs DR2; SMICA vs Commander in Fig. 3), (iii) inclusion of review-history/internal-process language in the main text and references, and (iv) insufficient specification of the primary β estimator used in the NaMaster pipeline validation. These affect the paper’s rigor and reproducibility and must be addressed. Once corrected, the core ΔNeff and pipeline-validation content appears sound and carefully caveated, and the numerical cross-checks largely reconcile.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

P1B-E8
- Location: Multiple places: Sec. IV→“see §VI body text”; Sec. VI fn. 5→“Eq. (1)-adjacent disclaimer”; Table II fn. (a)→“§ Headline-result discussion.”
- Issue: Broken/mismatched internal cross-references. The cited sections/titles do not exist or do not contain the promised content (pipeline bias belongs to Sec. IV, not VI; there is no section titled “Headline-result discussion”). Fn. 5 pointing to “Eq. (1)-adjacent disclaimer” is opaque.
- Required fix: Replace with correct section/eq. numbers. Add a short, unambiguous cross-reference map for all in-text “see §…” pointers.

P1B-E9
- Location: Fig. 2(b) and caption, p. 5.
- Issue: Unexplained overplots and inconsistent labels on the ΔNeff axis: “WP4 reheating [0.05, 0.40], WP4 decay [0.01, 0.25], SM (Neff = 0), BBN 2 upper (0.41), ACT DR6 central (0.40).” 
  - “SM (Neff = 0)” appears to label Neff rather than ΔNeff (should be “ΔNeff = 0”).
  - “WP4” quantities are undefined in the text and not cited; “BBN 2 upper (0.41)” is unclear (2σ? which analysis? for ΔNeff or Neff?).
  - “ACT DR6 central (0.40)” is unexplained in a ΔNeff context.
- Required fix: Define each overplotted reference (what it is, which paper, ΔNeff vs Neff), and correct mislabeling (“ΔNeff,” not “Neff”). Provide citations and clarify whether these overlays are directly comparable to your posteriors.

P1B-E10
- Location: Table I footnote (a), p. 3.
- Issue: Misclassification of nuisance parameters. The list is labeled “10 Planck likelihood nuisance,” but includes MB (SN Ia absolute magnitude), which is not a Planck nuisance parameter.
- Required fix: Correct the accounting: separate Planck nuisances from SN nuisance(s), and report counts by likelihood.

P1B-E11
- Location: Sec. IV (Pipeline configuration), p. 5.
- Issue: Beam specification for the Commander CMB map is likely incorrect. Text states “Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz).” Commander’s CMB map is a component-separation product, not a single-frequency 143 GHz map; its effective transfer function/beam differs from a pure 143 GHz channel.
- Required fix: State the correct effective beam/transfer function for the specific Commander product used (with citation), or disable beam deconvolution and forward-model it in theory. Document exactly what beam NaMaster deconvolves.

P1B-E12
- Location: Sec. V A (dataset naming) and References [17].
- Issue: Mis-citation of Planck releases. The text repeatedly says “Planck 2018 NPIPE,” but Ref. [17] is PR3 (2018 A6). NPIPE is PR4 (2020–2022). Low-ℓ references and CamSpec versions are also mixed.
- Required fix: Replace/add the proper PR4/NPIPE citations for every PR4 product used (high-ℓ CamSpec PR4, low-ℓ SimAll if applicable, PR4 lensing). Ensure low-ℓ references match the actual versions used (PR3 vs PR4) and justify any PR3/PR4 mixing explicitly.

P1B-M6
- Location: Fig. 3 graphic overlay vs body text, p. 6.
- Issue: In-plot annotations appear to show uncertainties ~0.09° for Planck/Planck+ACT overlays, while the body uses 0.30±0.11° (Planck) and 0.342±0.094° (joint). This is inconsistent and not explained.
- Required fix: Make all overlayed reference values in Fig. 3 numerically consistent with the text (state exact numbers and their sources), or explicitly note any rounding/alternative estimates in the caption.

P1B-M7
- Location: Sec. VI and App. C (ALP-MCMC likelihood stack).
- Issue: “Shared calibration covariance” between Planck PR4 and ACT DR6 EB spectra is invoked but not specified. The exact nuisance model/matrix is essential for reproducibility and affects β constraints.
- Required fix: Provide the explicit cross-experiment calibration model: parameterization, priors, and the numerical covariance matrix (or the nuisance-parameter sampling scheme) used in the joint EB likelihood. Cite the source if adopted from a public likelihood.

P1B-M8
- Location: Sec. III (Planck NPIPE CamSpec + low-ℓ + lensing) and Table II caption.
- Issue: PR3/PR4 low-ℓ mixing not justified. You list “planck 2018 lowl.EE + planck 2018 lowl.TT” alongside PR4 CamSpec high-ℓ. Mixing PR3 low-ℓ with PR4 high-ℓ is nontrivial and typically discouraged without justification.
- Required fix: Either harmonize to PR4 low-ℓ (e.g., SimAll PR4) or justify the PR3/PR4 mixture and its impact. Name the exact Cobaya likelihood tags used (e.g., planck_npipe_highl_CamSpec.TTTEEE, planck2018_lowl.EE, etc.) in the main text.

P1B-M9
- Location: Sec. III (Independent cross-validation), p. 5.
- Issue: Unsupported “agreement at 0.5σ in H0 and 0.4σ in σ8” with Liu et al. No comparator numbers, errors, or definition of the σ metric are given; the dataset/model stacks differ.
- Required fix: Quote Liu et al.’s values and uncertainties, specify which of your stacks are being compared, and define the tension metric. Add a caveat on null-procedure comparability across different models/likelihoods.

P1B-M10
- Location: Sec. IV (Mask statement), p. 5.
- Issue: fsky=0.32 is stated, but it is unclear whether this is the simple sky fraction or the effective fsky after C2 apodization. This quantity governs EB leakage expectations.
- Required fix: Report both the unapodized and effective apodized fsky (and how computed). If you are appealing to an “expected” leakage scaling with fsky, use the effective number.

P1B-m6
- Location: Sec. VI (ALP displacement envelope), p. 7.
- Issue: The stated “natural envelope” Δφ/fa ∈ [0.2, 1.1] is central to later coupling inferences, but no supporting figure/table is provided. Given later claims that the posterior prefers Δφ/fa ≈ 1.29 (above the envelope), documentation is needed.
- Required fix: Add a small figure or table showing Δφ/fa across the scanned (m/H0, θi) grid, with the path along which the MCMC posterior concentrates. This also clarifies the “∼17% above envelope” statement.

P1B-m7
- Location: Sec. IV (Beam/pixel handling), p. 5.
- Issue: It is implied that NaMaster deconvolves bℓ wpixℓ. Deconvolution amplifies noise; the β̂ covariance model then depends on this choice.
- Required fix: State explicitly whether beam/pixel are deconvolved or forward-modeled, and ensure the covariance used in the β̂ fit matches that choice.

P1B-n7
- Location: Table II footnote (a), p. 4.
- Issue: “see § Headline-result discussion” appears, but no such section exists.
- Required fix: Remove or replace with the correct section reference.

P1B-n8
- Location: Sec. IV, Fig. 3 caption.
- Issue: Caption says “Planck Commander map,” while the plot title mentions “Planck SMICA” (previously flagged as P1B-E3). Additionally, the caption doesn’t specify whether error bars are SEM or per-realization scatter.
- Required fix: Beyond resolving the SMICA/Commander mismatch (P1B-E3), specify in the caption what the vertical error bars represent.

Why these are new
- These items focus on cross-references, figure annotation consistency, beam/likelihood versioning, and calibration-covariance specification that were not covered in the initial review. Several are critical for reproducibility (beam model, PR3/PR4 mixing, calibration covariance) and for reader comprehension (Fig. 2 overlays, Fig. 3 annotations). They also address subtle but important null-procedure comparability and internal-referencing hygiene expected in PRD.

Summary
Please address all ESSENTIAL/MAJOR findings from the first report plus the new items above. These additional corrections are necessary to ensure rigorous provenance of datasets/likelihoods, internal consistency of figures and references, and full reproducibility of the EB estimator and ALP-likelihood combinations.