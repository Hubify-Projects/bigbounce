# P1B auto-2026-06-08_1520pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10323 chars)
**Wall time**: 718.6s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall assessment
The manuscript presents three distinct technical verifications: a stock-CAMB ΛCDM+ΔNeff MCMC proxy, a NaMaster pseudo-Cℓ pipeline bias-injection check, and an ALP-based birefringence consistency exercise. The author is careful about scope and repeatedly warns against over-interpretation. However, there are several methodology and arithmetic inconsistencies that must be corrected for PRD standards, including a hard arithmetic error in the wpivot variance calculation, dataset/citation inconsistencies, and an incoherent description of the model-independent β fit. I list all issues below, with precise locations, required fixes, and severity.

Findings

ESSENTIAL

P1B-E1 (Sec. IV B/Table II footnote b, p. 4): wpivot variance arithmetic is incorrect
- Text: “σ^2_wpivot = σ^2_w0 + (1 − ap)^2 σ^2_wa = (0.0436)^2 + (0.3320)^2 (0.1864)^2 = (0.0301)^2.” 
- Problem: The numeric evaluation of the stated expression is wrong. Using the printed numbers, (0.0436)^2 + [0.3320^2 × 0.1864^2] = 0.001900 + 0.003836 = 0.005736, implying σ_wpivot ≈ 0.0757, not 0.0301. In addition, the printed ap relation ap = 1 − Cov(w0,wa)/Var(wa) has a sign that does not decorrelate wpivot from wa; the standard decorrelation condition requires 1 − ap = −Cov/Var(wa). The currently printed combination of ap and σ_wpivot is internally inconsistent.
- Required fix:
  - Correct the wpivot decorrelation condition and provide the actual covariance elements used.
  - Recompute σ_wpivot with the correct formula (Var(wp) = Var(w0) − Cov(w0,wa)^2/Var(wa) when wp and wa are decorrelated), and show the numeric steps yielding 0.0301. If 0.0301 is retained, print the implied Cov(w0,wa) and check consistency with the rest of the chain’s covariance.
  - Update ap and zp consistently. As printed, ap = 0.668 and σ_wpivot = 0.0301 cannot both follow from the quoted σ’s unless a specific Cov is used (and then ap = 1 + Cov/Var(wa), not ap = 1 − Cov/Var(wa)).

P1B-E2 (Sec. V A, p. 6, and elsewhere): Dataset naming and citation inconsistencies (DESI DR1 vs DR2; DES-Y3 vs DES-Y5; Planck 2018 vs PR4/NPIPE)
- Text:
  - Sec. V A: “We analyze four dataset combinations: (1) Planck 2018 NPIPE [17]; (2) +DESI 2024 DR1 BAO [18]; (3) +Pantheon+; (4) +SH0ES H0 prior [7] + DES Y3 S8 [19].”
  - Table II (p. 4): “DESI DR2 BAO + Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native + DES-Y5 + Pantheon+.”
- Problems:
  - The body and Table II use DESI DR2 and DES-Y5, while Sec. V A lists DESI DR1 and DES Y3.
  - “Planck 2018 NPIPE [17]” is a mis-citation. Reference [17] is the 2018 parameters paper (A&A 641 A6), not the PR4/NPIPE reprocessing. You also use “PR4/NPIPE” elsewhere.
- Required fix:
  - Unify the dataset definitions throughout the manuscript. If the Table II chain uses DESI DR2 and DES-Y5, say so consistently in Sec. V A and everywhere those results are discussed.
  - Correct the Planck reference for PR4/NPIPE (cite the appropriate PR4/NPIPE release papers) and stop calling it “Planck 2018 NPIPE.” If you truly used CamSpec PR4 high-ℓ with PR4/NPIPE maps plus 2018 low-ℓ likelihoods, state the exact combination and cite each likelihood correctly.

P1B-E3 (Sec. III, p. 3): Nonexistent “Planck-only” column in Table I
- Text: “The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating samples, is reported separately in Table I, and is not aggregated...”
- Problem: Table I has exactly two columns (Full-tension and Planck+BAO+SN). There is no Planck-only column “reported separately.”
- Required fix: Either add the Planck-only column with its numbers or remove the claim that it is reported in Table I.

P1B-E4 (Sec. VI, p. 7; Appendix C, p. 9): Incoherent description of the “model-independent” βfree fit and configuration count
- Text: “βfree = 0.344° ± 0.096° (our internal model-independent MCMC fit ... with β as a free parameter, 9,720 accepted samples across the 3 ALP-MCMC configurations described in Sec. VI (configurations Caγ = 4, 8, 12 ... with β as a free parameter).”
- Problem: If β is sampled as a free parameter with no ALP model structure (βfree), Caγ is irrelevant and there is no reason to run or count “three configurations” with different Caγ. Appendix C also claims both the ALP-parametric and the βfree fits use the same EB-spectrum likelihood stack but does not reconcile why βfree would depend on Caγ.
- Required fix:
  - Separate clearly the model-dependent ALP fit (fixed Caγ, sampling θi and m/H0 and deriving β) from the model-independent βfree fit (sampling β directly).
  - Report the βfree result from a single, Caγ-independent configuration. If three runs were performed redundantly, state they are identical and pool them; otherwise, explain why they differ.
  - State the exact likelihood(s) used for βfree and how shared calibration covariance was handled.

P1B-E5 (Ref. [15], p. 10): Internal bookkeeping text in bibliography entry
- Text: “[15] ... reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B, arXiv:2201.07682 ...”
- Problem: “the value used at L256/L416 of P1B” is an internal line-number style note and is not acceptable in PRD references.
- Required fix: Remove all internal line/location notes from references. Keep only standard bibliographic information.

MAJOR

P1B-M1 (Sec. IV, p. 6): Misstated “∼12% amplitude-dependent component” for NaMaster bias
- Text: “... 0.342° injection actually gives 0.040°, a relative ∼12% amplitude-dependent component.”
- Problem: The change in bias magnitude from 0.032° to 0.040° is a 25% increase, not 12%. If you intend “incremental bias per incremental amplitude” (0.008°/0.072° ≈ 11.1%), say so explicitly. As written, the claim is numerically inconsistent.
- Required fix: Correct the arithmetic and explicitly define the metric you are quoting (relative change in bias magnitude vs. proportionality of bias to injection amplitude).

P1B-M2 (Sec. VI, pp. 6–7): Inconsistent Δφ/fa envelope versus posterior requirement
- Text: “Across the natural parameter range m/H0 ∈ [1, 3], θi ∈ [0.5, 2]: Δφ/fa ∈ [0.2, 1.1] … The MCMC posterior … implies Caγ (Δφ/fa) ≈ 10.3 which at Caγ = 8 corresponds to Δφ/fa ≈ 1.29, ∼ 17% above the natural envelope upper bound.”
- Problem: If the only sampled parameters are θi ∈ [0.5,2] and m/H0 ∈ [1,3] (fa fixed) and Δφ/fa is derived deterministically from the ODE, Δφ/fa should not exceed the pre-stated envelope computed over the same prior box unless the prior box or integration procedure actually allows larger values. As written, the envelope and the posterior-derived value are inconsistent.
- Required fix: Provide a figure or table showing Δφ/fa across the (θi, m/H0) grid used, including the true maxima within the prior box. If 1.29 is reachable, correct the earlier [0.2, 1.1] envelope; if not, revisit the βALP/βfree inference or the Caγ value.

P1B-M3 (Sec. III, p. 5): Unsubstantiated “agrees at 0.5σ in H0 and 0.4σ in σ8” cross-validation claim
- Text: “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.”
- Problem: No explicit numbers from Liu et al. [11] and from your run are displayed side-by-side to justify “0.5σ/0.4σ.” Moreover, your run is ΛCDM+ΔNeff whereas [11] fits an EC torsion cosmology—these are not identical models.
- Required fix: Quote the exact values and uncertainties from [11] and from your chain, compute the two-sided normalized differences, and state clearly that this is a numerical cross-check rather than a like-for-like model validation.

P1B-M4 (Sec. III, pp. 4–5): Over-strong wording on the MB–H0 degeneracy “exactly corresponds” to the 3.6σ Hubble tension
- Text: “This offset is ∼3.2σ relative to the chain’s σ_MB = 0.049 and corresponds exactly to the canonical 3.6σ Hubble tension manifesting in the MB axis …”
- Problem: You compare a 0.155 mag offset to σ_MB = 0.049 for a 3.2σ statement, then assert it “corresponds exactly” to the 3.6σ H0 tension. A rigorous mapping between these two axes should propagate uncertainties along the Pantheon+ degeneracy direction including the joint CMB+BAO constraint on H0, not just σ_MB alone.
- Required fix: Either provide a quantitative propagation showing the 0.155 mag offset maps to 3.6σ in the appropriate combined metric, or soften this to a heuristic statement and remove “exactly.”

P1B-M5 (Sec. IV, p. 6): Define the NaMaster “pipeline-recovery SNR”
- Text: “β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32).”
- Problem: The SNR definition is not given. The numbers imply σ_β ≈ 0.27°/20.32 ≈ 0.0133°, and similarly for the 0.342° injection. But readers cannot tell whether SNR = injected amplitude / std(recovered β across 500 MC), or recovered mean / std, or some other quantity.
- Required fix: Define the estimator for β, the SNR calculation, and report the mean and standard deviation of recovered β across the 500 realizations. Quote the uncertainty on the estimated bias (expected ∼ σ/√N_MC). Clarify whether this σ is per-sky realization or the sampling error on the mean bias.

P1B-M6 (Table I footnote a, p. 3): Nuisance-parameter labeling is confusing
- Text: “all 17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: Aplanck, …, Mb for the SNIa absolute magnitude) …”
- Problem: Mb is not a Planck likelihood nuisance parameter; it is a Pantheon+/SN nuisance. The phrasing conflates likelihood components. Also, for the Planck+BAO+SN column, verify the total sampled parameter count and list are accurate (do DES/BAO likelihoods add any nuisance?).
- Required fix: Separate the Planck nuisance list from non-Planck nuisance parameters, and report the correct partition per dataset combination.

P1B-M7 (Sec. IV, pp. 5–6): Foreground/noise modeling justification for the NaMaster test
- Text: Commander CMB-only map is used with ACT-like polarization noise (ΔP = 10 μK·arcmin) and fsky = 0.32; recovered SNR ≳ 20.
- Problem: While you emphasize this is a methods test, adding ACT-level noise to a Planck map is an unusual hybrid choice and leads to very high SNRs. The paper needs a one-sentence rationale for this choice and an explicit statement that the SNR does not reflect a sky-detection and is not directly comparable to Planck/ACT sky SNRs.
- Required fix: Add a brief justification for the chosen noise level and reiterate non-comparability with sky SNRs at the point where SNR is first reported.

MINOR

P1B-m1 (Abstract and Sec. IV, pp. 1, 5): “2.4–2.9σ” phrasing for Planck/ACT birefringence
- Text: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3].”
- Problem: The cited numbers elsewhere are 2.7σ (Planck PR4) and 2.9σ (ACT DR6). If 2.4σ is intended from a specific split or cross-check, cite it explicitly; otherwise use the correct central values.
- Required fix: Replace “2.4–2.9σ” with the precise quoted significances (e.g., “2.7σ (Planck PR4) and 2.9σ (ACT DR6)”) and cite the exact table/section of [2,3] supporting them.

P1B-m2 (Sec. III/Table I, p. 3): Consistency of chain counts and thinning
- Text: Figure 1 caption reports 119,617 post-burnin samples after thinning; footnote 1 gives different numbers and explains thinning.
- Problem: The explanation is adequate but could be tightened.
- Required fix: Add a parenthetical in the figure caption defining that additional GetDist thinning was applied for plotting only, with the post-burnin sample count without thinning given for reference.

P1B-m3 (Throughout): MB vs Mb notation
- Problem: Mixed case (“MB” in text, “Mb” as parameter name).
- Required fix: Standardize to a single convention and note the mapping to the code parameter name once.

P1B-m4 (Acknowledgments, p. 8): AI tool acknowledgment
- Text: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant...”
- Problem: Not a methodology concern, but PRD typically discourages tool-credit phrasing that could be misread as co-authorship contribution.
- Required fix: Optional: rephrase to “The author used commercially available LLM tools during manuscript preparation; all scientific content was verified by the author.”

NITPICKS

P1B-n1 (Sec. III, p. 3): Replace “Λstrong ∼ MPl/√γBI” with a proper citation and brief discussion of dimensions. γBI is dimensionless; the scale should be explicitly tied to the Holst/Immirzi sector.
P1B-n2 (Sec. IV, p. 5): Spell out C2 apodization reference (NaMaster option name) at first occurrence for readers not familiar with the code.
P1B-n3 (Sec. V, p. 6): Define S8 explicitly as S8 = σ8 (Ωm/0.3)^0.5 when first reported.
P1B-n4 (Refs. [2], [3], [15], p. 10): Check year/journal consistency with the current versions (e.g., ACT DR6 birefringence preprint status). Ensure each quoted statistic in the text appears in the cited paper’s abstract or tables.

Additional cross-checks that passed
- ΔNeff, H0, σ8 numbers in Table I are arithmetically consistent with the text. The 3.6σ H0 tension computed from 67.69 ± 1.06 vs 73.04 ± 1.04 matches 3.60σ.
- Inverse-variance combination of Planck and ACT β yields 0.241° ± 0.061° and 3.94σ, consistent with the printed 0.241° ± 0.061° (3.9σ).
- ALP birefringence normalization β = (αEM/4π) Caγ Δφ/fa used in Eq. (3) numerically reproduces the quoted 0.29° at Caγ = 8 and Δφ/fa ≈ 1.07 (0.00498 rad ≈ 0.285°).

Length
At 11 pages, the paper is acceptable for PRD given it serves as a companion technical verification. However, tightening Sec. II–V to remove repetitions and to correct dataset descriptions would improve clarity. No hard page cap recommended beyond fixing the essential/major issues above.

Summary recommendation
MAJOR REVISIONS

Justification: There is a clear arithmetic error in the wpivot variance computation and a sign/formula inconsistency in the pivot definition; dataset/citation inconsistencies (DESI DR1 vs DR2, DES-Y3 vs Y5, Planck 2018 vs PR4/NPIPE) must be reconciled; the “model-independent” βfree fit is described incoherently; and the NaMaster bias percentage is miscomputed. These are core methodology and reporting issues that must be corrected to meet PRD standards. The scope discipline and many numerical cross-checks are good, but the essential fixes require a careful revision and, in a couple of places, additional quantitative substantiation.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

P1B-E6 (Abstract p. 1; Sec. V A p. 6; Table I p. 3): Inconsistent count of dataset combinations
- Text:
  - Abstract: “309,189 frozen samples across two converged dataset combinations, plus a third Planck-only combination ongoing.”
  - Sec. V A: “We analyze four dataset combinations…”
  - Table I: only two columns are shown (Full-tension; Planck+BAO+SN).
- Problem: The manuscript alternately claims two, three, and four dataset combinations without presenting a consistent accounting or all corresponding results.
- Required fix:
  - State unambiguously how many dataset combinations were actually analyzed, which are “frozen,” which are ongoing, and which are reported in figures/tables. If four combinations exist (as per Appendix A), list them explicitly in Sec. V A and show their outputs or explain why only two are tabulated.
  - If a Planck-only run is ongoing, do not claim it is “reported” anywhere unless a column or figure is actually included (see P1B-E3 from the initial report).

P1B-M8 (Sec. IV, p. 5): Commander map beam specification is likely incorrect and incomplete for a component-separated CMB map
- Text: “The Planck Commander Q/U maps are provided at Nside = 2048 with the Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz); we degrade to Nside = 512 and apply the corresponding pixel window function. NaMaster’s NmtField is initialized with beam=b_l^Planck w_l^pix.”
- Problems:
  - Component-separated CMB maps (e.g., Commander/PR4) have their own effective transfer function/beam, not simply “5 arcmin at 143 GHz.” Using a single-frequency channel beam for a CMB-only product is not justified without citing the product’s effective beam.
  - The degradation procedure (e.g., additional smoothing and exact scheme for map downgrade) that determines the final effective beam at Nside = 512 is not specified. Simply multiplying by the pixel window w_l^pix does not capture any extra smoothing applied during downgrade.
- Required fix:
  - Cite the exact Commander product used (PR4/NPIPE CMB Q/U map identifier and DOI) and its effective beam/transfer function. If an additional Gaussian smoothing was applied before/after downgrade, state the FWHM and incorporate it into b_l.
  - Provide the exact NaMaster initialization (code snippet) showing how the final b_l was constructed (component-sep transfer function × any downgrade smoothing × pixel window). If the 5 arcmin 143-GHz beam was not the correct choice, recompute the MC test with the proper b_l (this affects E→B leakage and recovered β bias).

P1B-M9 (Eq. (3), Sec. VI, p. 6): Ambiguous angle units in birefringence normalization
- Text: “β ≈ αEM × 8/(4π) × 1.07 ≈ 0.29°.”
- Problem: The formula as written returns β in radians; the result is quoted in degrees without stating the rad→deg conversion. A few lines later, β is handled explicitly in radians.
- Required fix:
  - State explicitly that Eq. (3) yields β in radians, and show the conversion to degrees. Ensure consistent unit handling for β throughout (equations in radians; reported values in degrees).

P1B-M10 (Sec. IV, p. 5–6): Mischaracterization of ACT-noise choice as a “conservative worst-case bias check”
- Text: “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check).”
- Problem: Lower noise inflates SNR; it is not “conservative worst-case” for SNR. For a mask-induced E→B bias test, the mean bias is largely noise-independent, while the scatter is noise-dependent. The stated rationale is misleading.
- Required fix:
  - Rephrase to: “We use ACT-like ΔP = 10 μK·arcmin to stress-test the estimator variance; note this increases SNR relative to Planck-like noise. The mean bias is set by mask/beam and is approximately noise-independent.” Add the sentence already emphasized elsewhere that these SNRs are not sky-detection SNRs and are not comparable to Planck/ACT sky measurements at face value.

P1B-M11 (Fig. 1 caption vs Sec. V A, pp. 5–6): Figure-dataset labeling vs body text
- Text:
  - Fig. 1 caption: “Full-tension … over Planck+BAO+SN+H0+S8.”
  - Sec. V A: four dataset combinations are listed, with inconsistent naming (DR1 vs DR2; DES Y3 vs Y5; “Planck 2018 NPIPE”).
- Problem: The figure’s dataset composition (“full-tension”) is not matched to a clear, consistently named definition in the body. This impedes reproducibility and interpretability.
- Required fix:
  - Define “full-tension” once (list the exact likelihoods/priors, including the numerical SH0ES prior form and the precise S8 prior used) and use the same label in the figure caption and in Sec. V A. Ensure DESI release and DES Y3/Y5 usage match across the text, Table I, and the figure.

P1B-M12 (Sec. III, Sec. V A, Appendix A): Missing explicit numerical priors for SH0ES and S8 in the full-tension run
- Text: Full-tension includes “SH0ES H0 prior” and “DES Y3 S8,” but only MB is numerically audited; the S8 prior value is never given.
- Problem: The exact form and numbers for the priors matter (e.g., H0 vs MB anchoring; S8 mean and σ; whether Gaussian or other). This is needed for replication and to interpret Figure 1’s label “+S8.”
- Required fix:
  - State both prior parameterizations explicitly: either MB prior or H0 prior (with mean and σ), and the exact S8 prior value and σ used (and reference). Confirm the mapping to Cobaya parameter names in the YAML for both.

P1B-M13 (Sec. V A, p. 6; Appendix A, p. 8): Mixed Cobaya versions without clarity on which version produced the reported results
- Text: “Cobaya (v3.5 original; v3.6.1 verification).”
- Problem: It is unclear which version’s chains are plotted/reported in Table I and Fig. 1. Small version differences can affect results and reproducibility.
- Required fix:
  - State conclusively which Cobaya version and CAMB version produced each reported result (Table I, Fig. 1, Table II). Provide git commit hashes or release tags in the repository README for the exact runs.

P1B-m5 (Conclusions, p. 8): Broken internal cross-reference
- Text: “worst-case 0.040° at injection β = 0.342°; see §VI body text.”
- Problem: The NaMaster bias-amplitude discussion is in Sec. IV, not Sec. VI.
- Required fix: Change the reference to “§IV.”

P1B-m6 (Throughout; Table I footnote a, p. 3): Stray “k = 7” mention without context in this paper
- Text: “references to ‘k = 7’ elsewhere in this paper refer to the cosmological-parameter count only…”
- Problem: No other “k = 7” reference appears; this reads as leftover text and confuses the reader.
- Required fix: Remove or adjust to the actual usage within this manuscript.

P1B-m7 (Appendix C, p. 9): Units of the βfree prior and likelihood need to be stated explicitly
- Text: “β: uniform prior on [−2°, 2°]; sampled as a free amplitude…”
- Problem: It is not stated whether the EB-spectrum likelihood is implemented internally in radians or degrees. Mixing units between prior, sampling, and likelihood can cause silent inconsistencies.
- Required fix:
  - State the internal unit convention used by the likelihood and by Cobaya for β, and confirm that the prior boundaries are applied in the same units.

P1B-m8 (Sec. IV, p. 5): NaMaster field initialization is ambiguous
- Text: “NmtField is initialized with beam=b_Planck_ℓ w_pix_ℓ.”
- Problem: This conflates (or at least does not clearly separate) the instrument beam and pixel window in the code API. Readers cannot tell precisely how b_ℓ and w_ℓ are passed.
- Required fix:
  - Provide the exact NaMaster calls (or a code excerpt) showing how the beam and pixel window are supplied. This will also help resolve P1B-M8 (proper beam handling for a component-separated CMB map).

P1B-m9 (Sec. VI, p. 7): Claims about model-building routes for enhancing Caγ lack citations
- Text: “chiral-fermion-loop enhancement, clockwork constructions…”
- Problem: No references are given to support these statements.
- Required fix:
  - Add references to representative models/mechanisms that can raise Caγ to the stated ranges.

P1B-m10 (Appendix A, p. 8): Repository scope clarity
- Text: The repository includes galaxy-spin code not used in this manuscript.
- Problem: While this is a companion program, mixing unrelated pipelines in a single repo can confuse reproducibility claims for this specific paper.
- Required fix:
  - Either separate the reproducibility materials for this paper into a dedicated subfolder with a top-level README specific to this manuscript, or clearly mark which folders are relevant for this paper to avoid confusion.

P1B-m11 (Appendix C, p. 9): Small-sample convergence claim for ALP MCMC needs basic diagnostics
- Text: “R̂ − 1 < 0.01 … at Ntot = 9,720 accepted samples across 3 configurations.”
- Problem: With ~3,240 accepted samples per configuration, reporting R̂ alone may be insufficient. Readers need assurance that β (or CaγΔφ/fa) posterior moments are stable.
- Required fix:
  - Report the effective sample size (ESS) and integrated autocorrelation time for the key parameter(s) (β in the βfree fit; CaγΔφ/fa or Δφ/fa in the model-dependent fit). Alternatively, lengthen the runs and provide ESS ≥ O(10^3) for those parameters.

P1B-n5 (Sec. IV, p. 5): Add product DOI/link for the exact PR4/NPIPE Commander polarization map used
- Required fix:
  - Provide the ESA/Planck data product identifier (and beam/transfer function file if separate) so readers can fetch the same map.

P1B-n6 (Sec. IV, p. 6): State sign convention for Q/U rotation
- Text: “rotate Q+iU via e^{2iβ}(Q+iU).”
- Problem: Birefringence sign conventions differ across the literature.
- Required fix:
  - State the adopted convention and confirm alignment with the Planck/ACT likelihoods you reference.

Explanation
The initial review focused on wpivot arithmetic/sign consistency, dataset naming/citation mismatches, model-independent β reporting, and several numerical inconsistencies. This fresh pass adds:
- A hard bookkeeping inconsistency about the number of dataset combinations actually analyzed and reported.
- A methodological issue with the effective beam/transfer function used for a component-separated CMB map in the NaMaster test.
- Additional unit handling, cross-referencing, prior specification, and reproducibility details that PRD typically requires for clarity and replication.