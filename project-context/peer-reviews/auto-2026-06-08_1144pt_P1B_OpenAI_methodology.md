# P1B auto-2026-06-08_1144pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6737 chars)
**Wall time**: 314.0s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
I reviewed the full manuscript, all tables/figure, equations, footnotes, and the abstract/conclusions, with emphasis on statistical validity, dimensional consistency, internal arithmetic, and the traceability of all quoted numerical results. Below I enumerate all issues found, each with a severity classification and required fix.

Findings

ESSENTIAL

P1B-E1 (Sec. VI, p. 7; Eq. (3))
Problem: Dimensional inconsistency and missing unit declaration in the birefringence formula.
Quoted: “β ≈ αEM × 8 / 4π × 1.07 ≈ 0.29°.”
Issue: As written, the RHS yields β in radians; the manuscript then reports a value in degrees without an explicit rad→deg conversion or unit statement for β in Eq. (3). This is a unit/notation error.
Required fix: State explicitly that the RHS gives β in radians, or include the factor (180/π) to convert to degrees. For example: “β [rad] ≈ (αEM/4π) Caγ (Δϕ/fa) → β [deg] = (αEM/4π) Caγ (Δϕ/fa) × 180/π.” Ensure consistent unit labeling for β throughout the manuscript and captions.

P1B-E2 (Secs. III and VII; p. 3 fn. 1; p. 8 Conclusions; Table I, p. 3)
Problem: Contradictory statements about a “third Planck-only” chain being “reported separately in Table I,” while Table I contains only two dataset columns (Full-tension and Planck+BAO+SN).
Quoted (p. 3 fn. 1): “The third (Planck-only) dataset combination … is reported separately in Table I …”
Quoted (p. 8): “… an additional 114,992-sample Planck-only run is still accumulating … and is reported separately in Table I …”
Issue: Table I does not include a Planck-only column or values. This is an internal inconsistency that prevents verification.
Required fix: Either (a) add the Planck-only column with the corresponding statistics (H0, ΔNeff, σ8, S8, Ωm, τ, ns, chain diagnostics) and correct R̂−1, or (b) remove all claims that the Planck-only run is reported in Table I and move all Planck-only remarks to a future-work note without implying tabulated results.

P1B-E3 (Dataset attribution consistency: Abstract, Secs. III–V; Table captions; References [15], [17]; multiple pages)
Problem: Inconsistent and confusing labeling of Planck data and likelihoods: “Planck 2018 NPIPE,” “Planck NPIPE CamSpec TTTEEE,” “Planck PR4 / NPIPE,” and references to Planck 2018 (PR3) [17] appear alongside use of PR4/NPIPE products (CamSpec PR4 and NPIPE maps).
Issue: PR3 (2018 legacy) and PR4 (NPIPE) are distinct releases. “Planck 2018 NPIPE” is a contradictory phrase. Reproducibility requires unambiguous dataset labeling and correct citations for the exact high-ℓ likelihood used (e.g., Efstathiou & Gratton CamSpec for PR4) and low-ℓ likelihood sets (PR4 vs PR3).
Required fix: Standardize nomenclature throughout:
- If using PR4/NPIPE for temperature/polarization and CamSpec PR4 likelihoods, explicitly state “Planck PR4 (NPIPE) high-ℓ CamSpec TTTEEE, low-ℓ TT/EE …” and cite the appropriate PR4/NPIPE and CamSpec papers, not only [17].
- If any PR3 components are used, delineate them clearly. Remove the phrase “Planck 2018 NPIPE” everywhere; replace by “Planck PR4 (NPIPE).” Update captions and the dataset list in Sec. V A accordingly.

P1B-E4 (Sec. IV, pp. 5–6; Eq. (1) context)
Problem: Primary estimator for β in the NaMaster pseudo-Cℓ pipeline is not specified. The paper reports β̂ values and “SNR,” but does not explicitly define the estimator, the likelihood, or the weighting used to infer β from the deconvolved spectra.
Required fix: Pre-declare and define the estimator used to recover β (e.g., EB minimization, linearized small-angle estimator from the EB spectrum, or a full likelihood fit over EB/EE/BB), including:
- The explicit formula or likelihood used,
- The ℓ-range included and bin weights,
- Treatment of purification, coupling-matrix inversion, and covariance modeling (e.g., analytic vs. MC),
- How the “SNR” was computed from the 500 realizations (define σβ and whether SNR = mean(β̂)/std(β̂) or similar).
Without this, the β̂ and SNR figures cannot be independently validated.

P1B-E5 (Sec. IV, p. 6; MC uncertainties)
Problem: The manuscript reports point estimates and SNR for injected β, but does not report the Monte Carlo uncertainty on β̂ or the standard error on the mean bias with NMC = 500.
Required fix: Report for each injection (β = 0, 0.27°, 0.342°):
- The mean recovered β̂ ± standard deviation across the 500 realizations,
- The standard error on the mean bias (σ/√500),
- The definition of SNR being used.
Also provide (or cite in appendix/repo) histograms or summary statistics to allow readers to judge Gaussianity and robustness.

P1B-E6 (Sec. III, pp. 3–4; “MB–H0 joint-posterior offset check” and adjacent prose)
Problem: The manuscript contains meta-review and draft-history language inappropriate for a journal article and undermining neutrality.
Quoted: “This addresses earlier reviewer concerns … NOT a YAML alias failure …”
Quoted (Sec. II, p. 2–3): “An earlier count erroneously quoted ‘98.6% quintom-B’ weight …”
Quoted (Sec. V B, p. 6): “prior caveat promised a Savage-Dickey ratio …”
Required fix: Remove all references to earlier internal counts, reviewer concerns, or promises. Recast these passages as neutral methodological statements and present-only analysis, with clean derivations that stand on their own.

P1B-E7 (Sec. IV, p. 5; “ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check)”)
Problem: The characterization “conservative worst-case bias check” is misleading. ACT DR6 map polarization noise levels are generally lower than Planck’s; adopting 10 μK·arcmin is not clearly a “worst-case” for bias. Noise affects variance more than deterministic E→B leakage bias from masking/apodization.
Required fix: Either justify quantitatively why ΔP = 10 μK·arcmin is conservative for bias in this pipeline (with supporting tests at higher noise/Planck-like noise), or rephrase to simply state the noise level used and present bias-insensitivity tests versus noise (e.g., repeat at Planck-like noise and show similar bias).

P1B-E8 (Sec. IV vs Abstract and Sec. VI; multiple pages)
Problem: Frequent juxtaposition of sky-detection significances (2.4–2.9σ, 3.6σ) and pipeline SNRs without always re-stating non-comparability in each juxtaposition risks reader confusion.
While the paper correctly notes non-comparability in the Abstract and Sec. IV, the 3.9σ inverse-variance combination (Eq. (4), p. 7) is shown alongside 3.6σ in the same subsection.
Required fix: At every instance where pipeline SNR or the 3.9σ auxiliary combination is presented near sky-based significances, insert an explicit sentence that these are not directly comparable significance measures and the 3.9σ neglects shared systematics (hence is only an auxiliary cross-check).

P1B-E9 (Sec. IV and Appendix A; Reproducibility)
Problem: Reproducibility relies on a mutable GitHub repository without a stable archival DOI; PRD requires durable access to materials supporting quantitative claims.
Required fix: Archive the exact code/data snapshot used for all reported results on a citable repository (e.g., Zenodo) with a DOI and include the DOI in the manuscript. Ensure the NaMaster masks, binning files, seeds, and Cobaya YAMLs used for Tables I–II and Fig. 1 are part of that snapshot.

MAJOR

P1B-M1 (Sec. V A, p. 6; datasets)
Problem: Dataset-version mismatch and inconsistency. Sec. V A lists “DESI 2024 DR1 BAO,” whereas Table II and earlier text invoke DESI DR2. Similarly, several places toggle between PR3/PR4 Planck labelling.
Required fix: Harmonize the dataset description with the actual runs reported: explicitly state DR1 or DR2 consistently (with correct citations), and align Sec. V A with Table II and Sec. II/III usage. If multiple versions were used in different runs, state clearly which result used which version.

P1B-M2 (Sec. III Table I footnote a; pp. 3–4)
Problem: Mislabeling of nuisance parameters. The text calls all 10 listed nuisance terms “Planck likelihood nuisance,” but Mb is a SN Ia nuisance, not a Planck nuisance. Some listed CamSpec nuisance parameters correspond to specific cross-spectrum amplitudes and noise parameters whose definitions differ between PR3 and PR4.
Required fix: Correct the labeling to e.g., “9 Planck CamSpec/low-ℓ nuisance parameters plus 1 SN Ia absolute magnitude parameter Mb,” and provide a reference or appendix table enumerating the precise nuisance set used for the specific likelihood versions employed.

P1B-M3 (Sec. VI, p. 7; parameter-envelope claim)
Problem: The envelope β ≈ 0.17–0.43° is attributed to a “joint-trajectory scan” over (Caγ, m/H0, θi) but no figure/table is provided. The contrast with the “naïve” product [0.027, 0.44]° requires substantiation.
Required fix: Provide a contour/heatmap figure or a table showing Δϕ/fa as a function of (m/H0, θi) and overplot lines of constant Caγ Δϕ/fa, to justify the stated restricted envelope [0.17, 0.43]°. Alternatively, include this as a supplemental figure with a clear description in the text.

P1B-M4 (Sec. III, pp. 3–4; SH0ES-tension discussion)
Problem: The text states the MB–H0 posterior compromise “corresponds exactly to the canonical 3.6σ Hubble tension,” yet the computed offset (0.155 mag with σMB = 0.049) corresponds to ~3.2σ in that axis. While the H0-tension significance of 3.6σ is correct for the quoted values, “exactly” is inaccurate in the MB projection.
Required fix: Replace “corresponds exactly” with a precise statement: quantify the ~3.2σ offset in the MB direction and separately the 3.6σ in H0 using the given uncertainties. Avoid implying equality between these two.

P1B-M5 (Sec. IV; pipeline details)
Problem: The mask description is minimal (“fsky = 0.32, C2 apodization at 2°”). For a methods paper, the exact mask source and construction should be specified to ensure reproducibility and to interpret leakage-bias claims.
Required fix: Provide the mask provenance (e.g., which Commander/Planck confidence mask or a custom mask), its resolution, thresholding, apodization kernel, and include the exact mask file in the archived repository. If custom, include the generation script.

P1B-M6 (Sec. VI, p. 7; ALP-MCMC size and diagnostics)
Problem: The ALP-MCMC runs total 9,720 accepted samples across 3 configurations with R̂ − 1 < 0.01 claimed, but no acceptance rates or autocorrelation lengths are provided. Given the small sample sizes per configuration (3,240), diagnostics should be shown.
Required fix: Report per-configuration acceptance fractions, minimum effective sample sizes for the key parameters (β, m/H0, θi), and, if possible, integrated autocorrelation times. Provide small corner plots or summary statistics in an appendix or repository to substantiate convergence.

P1B-M7 (Sec. II and Table II caption; “phantom crossing required”)
Problem: While w0 > −1 and w0 + wa < −1 imply a crossing between z = 0 and large z in Chevallier-Polarski-Linder parameterization, the manuscript should add a one-line justification or reference that this logic holds for the chosen zpivot and parametrization.
Required fix: Add a sentence explaining that with CPL w(a) = w0 + wa(1 − a), w(a) = −1 is crossed between a = 0 and 1 when w0 > −1 and w0 + wa < −1, which is satisfied by the reported mean values.

MINOR

P1B-m1 (Sec. III, p. 3; wording of null-test scope)
Problem: The proxy ΔNeff test is appropriately scoped, but the sentence “The spin-torsion framework alone does not resolve cosmological tensions at the present data precision” is a broad claim not strictly supported solely by ΔNeff = 0 ± 0.17 null; it is more a fair inference than a demonstrated theorem.
Required fix: Rephrase as “Within the stock-CAMB ΛCDM+ΔNeff extension used here, current data do not resolve the H0 tension.”

P1B-m2 (Table I, p. 3; units and headers)
Problem: H0 column has units but “σ8, S8” lack explicit definitions in the table.
Required fix: Add a table footnote defining S8 = σ8 (Ωm/0.3)1/2 for completeness.

P1B-m3 (Sec. IV, p. 5; purification settings)
Problem: You specify purify_b=True, purify_e=False. It would help to state explicitly that you verified E→B leakage suppression vs. the non-purified case.
Required fix: Add a clause indicating the effect of purification on recovered β̂ bias/variance (e.g., a one-line quantitative comparison to non-purified runs or a reference).

P1B-m4 (Sec. III, p. 3; GetDist thinning)
Problem: “getdist-thinned” should be capitalized and a citation to GetDist can be added for completeness.
Required fix: Write “GetDist-thinned” and include a standard GetDist citation.

P1B-m5 (Sec. VI, p. 7; Caγ range commentary)
Problem: The statement about KSVZ/DFSZ “O(1)” couplings and the need for “nonminimal model building” would benefit from a reference.
Required fix: Add a reference discussing photon-coupling ranges for KSVZ/DFSZ and possible enhancement mechanisms (e.g., clockwork models).

P1B-m6 (References)
Problem: The Planck PR4/NPIPE and CamSpec PR4 citations appear incomplete (only [15], [17] are given). ACT DR6 citation [3] is a 2025 “arXiv preprint” placeholder.
Required fix: Add the official PR4/NPIPE and CamSpec PR4 references (e.g., Efstathiou & Gratton, 2021/2022, and Planck NPIPE data release papers). For ACT DR6, update to the final published citation if available, or ensure the arXiv citation is accurate.

NIT

P1B-n1 (Acknowledgments, p. 8)
Problem: Inclusion of specific commercial compute instances and AI-assistant brand names is nonstandard for PRD and not scientifically relevant.
Required fix: Remove “RunPod H200 instances” and brand names (or generalize to “cloud compute resources” and “an AI assistant was used for drafting, with all results verified by the author,” if needed by journal policy).

P1B-n2 (Typographic consistency)
Problem: Occasional inconsistencies in capitalization and hyphenation (“NaMaster,” “GetDist,” “Cℓ” vs “Cl,” “CamSpec”).
Required fix: Standardize capitalization and notation throughout.

P1B-n3 (Length)
Problem: 10 pages is reasonable for a methods companion; no reduction needed. If trimming, the “Forward” paragraph at the end of Conclusions reads more like a status note and could be shortened or moved to an appendix.

Audits and arithmetic checks

- Table I numbers in Abstract and body match. R̂ − 1 and ESS are sensible for quoted 1σ errors.
- Burn-in/sample-count arithmetic (309,189 raw; 70% post-burn): 216,432 matches the manuscript’s calculation.
- Full-tension post-burn-in 176,240 × 0.7 = 123,368 vs quoted 123,129 is a 0.19% discrepancy plausibly due to chain truncation; acceptable with stated caveat.
- w0 departure: (−0.8122 + 1)/0.0436 = +4.31σ; wa: 0.6666/0.1864 = 3.58σ; both consistent with text rounding.
- wpivot: (−1.0344 + 1)/0.0301 = −1.14σ; consistent.
- χ2 channel sums: 10.6 + 10983.9 + 3043.0 = 14037.5; reported 14037.4 ± 5.6 total is consistent within rounding.
- Inverse-variance combination: 0.30 ± 0.11 and 0.215 ± 0.074 → β = 0.2415 ± 0.0614°, significance ~3.93σ; consistent with 0.241 ± 0.061 (3.9σ) reported.
- β = 0.342° → radians 0.342 × π/180 = 5.97×10−3; Caγ Δϕ/fa ≈ β/[α/(4π)] = 0.00597/5.8×10−4 ≈ 10.3; correct.
- Eq. (3) value: (α/(4π))×Caγ×Δϕ/fa = 5.8×10−4 × 8 × 1.07 = 0.00497 rad = 0.285°; reported 0.29°, OK after unit fix.

Recommended maximum page count
No reduction required; 10 pages is acceptable for a methods companion. If needed, move the “Forward” status paragraph to an appendix.

Summary recommendation
MAJOR REVISIONS

The manuscript contains solid technical elements and appropriate scoping for several null and consistency checks. However, there are multiple essential issues that must be corrected before PRD publication: a dimensional/units error in the birefringence equation, a critical inconsistency in the reporting of the “Planck-only” chain vs. Table I, dataset-attribution inconsistencies (PR3 vs PR4/NPIPE) affecting reproducibility, absence of a clearly defined β estimator and MC uncertainty reporting for the NaMaster pipeline, and the presence of meta-review/draft-history language. Addressing these, along with the listed major and minor corrections, will materially improve clarity, reproducibility, and methodological rigor to meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS

Below are new issues identified on a fresh pass, organized with the same severity taxonomy. I do not repeat any items from the initial review.

ESSENTIAL

P1B-E10 (Sec. VI fn. 4; internal cross-reference)
Problem: Misreferenced equation. The footnote says “spectator-status restriction θi ≪ 1 (Eq. (1)-adjacent disclaimer),” but Eq. (1) in this paper is the NaMaster β̂ result from Sec. IV, unrelated to ALP backreaction.
Required fix: Correct the reference to the intended equation or text (likely Eq. (2) in Sec. VI or an explicit sentence in the main text). Ensure all in-text Eq. references point to the correct section/equation.

P1B-E11 (Appendix B/Table III; cross-reference to non-existent artifact)
Problem: Table III entry “β̂NaMaster = 0.238° (500-MC) … MC bias table” implies a tabulated MC-bias summary exists. No such table is present in the paper or appendices.
Required fix: Either add the referenced bias table (mean β̂, σβ, bias vs. injection) or remove the claim that a “MC bias table” is provided.

P1B-E12 (Sec. IV; SNR definition vs. MC realism)
Problem: The 500-realization MC varies only instrument noise (the sky signal is fixed to the Commander map). For EB-based β estimators, cosmic variance from the lensed CMB contributes to σβ; noise-only resampling underestimates the true estimator variance. The reported “SNR” therefore overstates recoverability for a full sky+noise ensemble.
Required fix: Either (a) add lensed CMB+noise simulations with realistic beams/masks and recompute σβ (preferred), or (b) explicitly label the exercise as “noise-resampling only,” remove SNR claims, and report just the mean bias with its standard error, clarifying non-comparability to sky-measurement significances.

MAJOR

P1B-M8 (Sec. IV; map downgrading and anti-aliasing)
Problem: The manuscript degrades the map from Nside=2048 to 512 and applies only the pixel window. Without explicit pre-smoothing or band-limiting, downgrading can alias high-ℓ power into lower multipoles, biasing EB and β̂.
Required fix: State the anti-aliasing procedure (e.g., Gaussian smoothing to the Nside=512 band limit) used prior to downgrade, and verify that β̂ bias is stable with/without the smoothing. If not applied, add a smoothing step and recompute the MC validation.

P1B-M9 (Secs. II and Table II; CPL crossing and pivot details)
Problem: The paper uses wpivot and asserts phantom crossing but does not provide the CPL pivot redshift zp or the expression for wpivot. This prevents independent verification of the crossing logic with the quoted parameters.
Required fix: Specify the CPL form w(a)=w0+wa(1−a), the pivot definition wpivot=w0+wa(1−ap), and the pivot redshift zp (or ap). Include a one-line derivation showing that w0>−1 and w0+wa<−1 implies a crossing for 0<a<1 given the adopted zp.

P1B-M10 (Secs. III, V A; DES Y3 S8 prior details)
Problem: The “full-tension” combo includes a DES Y3 S8 prior but the exact prior mean, σ, and source (e.g., DES Y3 3×2pt baseline value) are not stated.
Required fix: Provide the exact S8 prior value and uncertainty and a citation (or YAML snippet) so the combination can be reproduced. Clarify whether this is a single-parameter Gaussian prior (not the full 3×2pt likelihood).

P1B-M11 (Secs. III, V A, Table I; Planck lensing likelihood specificity)
Problem: The text alternates among “lensing,” “lensing.native,” and PR3/PR4 labels without specifying which official Planck lensing likelihood variant is used (e.g., PR3 2018 lensing vs. PR4/NPIPE lensing, and whether “native” means the full likelihood or a derived product).
Required fix: Name the exact Planck lensing likelihood used (release, version, and code tag) and cite the corresponding paper. Update Table I headers or footnotes to reflect whether lensing is active in each column.

P1B-M12 (Sec. III; “Independent cross-validation” with Liu et al.)
Problem: The claim “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” is not substantiated with side-by-side numbers or matched datasets/priors. Given likely differences in data stacks and parameterizations, this is not verifiable as stated.
Required fix: Provide a small table listing H0 and σ8 with uncertainties for both analyses, ensuring datasets/priors are as closely matched as possible, or remove the σ-level quantification.

MINOR

P1B-m7 (Table I footnote a; dangling “k=7” reference)
Problem: The footnote says “references to ‘k=7’ elsewhere in this paper…” but no other instance of “k=7” appears.
Required fix: Remove the dangling remark or add the missing reference where “k=7” is actually used.

P1B-m8 (Sec. IV; apodization kernel)
Problem: The mask apodization is described only as “C2 apodization at 2°,” which is ambiguous (cosine-squared? exact kernel form?).
Required fix: Specify the exact apodization function and parameters as used in NaMaster (e.g., apodization_type='C2', apodization_scale=2 deg) and include the mask-generation script in the archived repository.

P1B-m9 (Table I header vs. text; lensing label)
Problem: The “Planck+BAO+SN” column header omits “+lensing,” while the text indicates lensing is included in the Planck likelihood set.
Required fix: Amend the column header or add a footnote clarifying whether Planck lensing is active in that column.

P1B-m10 (Sec. IV; Commander beam specification)
Problem: The text assumes a 5-arcmin Gaussian beam at 143 GHz for the Commander CMB map. The effective beam of the delivered CMB map product can differ from a single-channel 143-GHz beam.
Required fix: State the effective beam of the specific Commander CMB product used (per Planck documentation) and ensure the same beam is used to initialize NmtField.

NIT

P1B-n4 (Ref. [15] annotation style)
Problem: Reference [15] includes internal commentary (“the value used at L256/L416 of P1B”), which is not standard PRD style.
Required fix: Remove meta commentary; keep only the bibliographic citation.

P1B-n5 (Hyphenation artifacts)
Problem: Occasional soft-hyphen artifacts (e.g., “NaMas­ter”) appear.
Required fix: Clean typesetting to ensure consistent rendering (NaMaster, CamSpec, Cℓ).

P1B-n6 (Sec. VII; job-control jargon)
Problem: “The 16-rank mpirun process terminated automatically…” is operational detail not needed in the main text.
Required fix: Remove or move to an appendix; describe convergence without HPC command jargon.

Explanation of coverage
This fresh pass focused on latent cross-reference errors, figure-method mismatches, hidden assumptions in the NaMaster validation (anti-aliasing, sky variance), and missing dataset likelihood specifics (lensing variant, S8 prior), which often escape a first read. These additions complement, and do not duplicate, the items raised in the initial review.