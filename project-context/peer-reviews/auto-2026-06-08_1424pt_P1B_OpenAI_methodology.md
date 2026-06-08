# P1B auto-2026-06-08_1424pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5490 chars)
**Wall time**: 637.4s

---

Referee report on P1B (Technical Verification Companion to the ECH Spin-Torsion Program)

Role focus: methodology rigor (statistical-method validity, derivation chains, dimensional analysis, internal arithmetic consistency, error propagation). I audited all numerical claims in the abstract/conclusions against the body, checked equations and units, recomputed quoted significances, inspected tables/figure captions for consistency, and assessed reproducibility.

Overall: The paper does a good job of disclaiming scope (proxy ΔNeff test; pipeline validation; ALP consistency) and avoids many common overclaims. However, there are several methodology-critical issues that must be fixed before PRD publication. The most serious are: (i) a wrong decorrelation/pivot formula (with an internally inconsistent numerical demonstration) in Table II footnote b; (ii) dataset/likelihood labelling and consistency errors (DESI DR1 vs DR2; DES Y3 S8 prior vs the reported S8 posterior); (iii) the birefringence estimator in the NaMaster analysis is under-specified (no explicit estimator, SNR definition, or MC uncertainty reported), preventing reproducibility; (iv) at least one reference entry contains internal line-number notes and mixed authorship that must be corrected.

Findings

ESSENTIAL

P1B-E1
- Location: Table II, footnote b (page 4)
- Problem: Incorrect decorrelation formula and inconsistent variance calculation. Quoted: “wpivot ≡ w0 + (1 − ap) wa with ap chosen so that w0 and wa are decorrelated in the posterior covariance: ap = 1 − Cov(w0, wa)/Var(wa). … With w0 and wa formally decorrelated at zp, σ^2_wpivot = σ^2_w0 + (1 − ap)^2 σ^2_wa = (0.0436)^2 + (0.3320)^2(0.1864)^2 = (0.0301)^2.”
  - Issues:
    - Choice of ap cannot “decorrelate w0 and wa” (they are the base parameters); the standard pivot choice is to make wpivot uncorrelated with wa, i.e., Cov(wpivot, wa) = 0. This gives 1 − ap = −Cov(w0,wa)/Var(wa), i.e., ap = 1 + Cov/Var(wa) (note the sign).
    - The variance formula for wpivot must include the cross term: Var(wpivot) = Var(w0) + (1 − ap)^2 Var(wa) + 2(1 − ap) Cov(w0,wa). The text drops the cross term.
    - The numerical demonstration is internally inconsistent: using only σ_w0 and σ_wa with ap = 0.668 gives sqrt((0.0436)^2 + (0.332)^2(0.1864)^2) ≈ 0.0757, not 0.0301. Achieving 0.0301 requires including the (negative) covariance term and the correct ap definition.
- Required fix: Correct the definition of ap (decorrelating wpivot from wa), include the cross-term in the variance, and explicitly report Cov(w0,wa). Provide the corrected numerical calculation yielding σ(wpivot) = 0.0301 if that is indeed obtained from the chain.

P1B-E2
- Location: Section V.A (page 6), Table II (page 4), Table I and Fig. 1 context (pages 3 and 5)
- Problem: Dataset/likelihood inconsistencies and S8 prior ambiguity.
  - Section V.A lists “+DESI 2024 DR1 BAO” as a dataset combination, while Table II explicitly uses “DESI DR2” and the text elsewhere references DR2 (e.g., Sec. III Physics interpretation heading says “DESI DR2 BAO + DES-Y5 + Pantheon+”).
  - The “full-tension” combination is described as including DES Y3 S8 [19]. However, Table I reports S8 = 0.814 ± 0.008 for the full-tension chain and S8 = 0.831 ± 0.018 for Planck+BAO+SN. If a DES Y3 prior S8 ≈ 0.776 ± 0.017 is applied, the combined posterior would be expected near ≈ 0.802 ± 0.012 (inverse-variance combination with the Planck+BAO+SN value), not 0.814 ± 0.008. The present S8 posterior looks incompatible with having applied a DES Y3 S8 prior at the stated value and width.
- Required fix: Unify dataset labels (DR1 vs DR2) across the paper and references, and explicitly list the exact likelihoods active in each reported chain (Planck likelihood names/versions, BAO release, SN set, H0 prior, S8 prior with the exact mean and σ). If the DES Y3 S8 prior was not actually included in the “full-tension” chain, correct the text; if it was included, demonstrate via a simple two-constraint combination or a table of prior vs posterior pulls that the reported S8 = 0.814 ± 0.008 is consistent with the combined likelihoods. Provide the YAML block or a summary table to remove ambiguity.

P1B-E3
- Location: Section IV (pages 5–6), Eq. (1)
- Problem: Birefringence estimator and SNR are not specified, preventing reproducibility and preventing a reader from auditing the quoted “pipeline-recovery SNR = 20.32”.
  - The paper does not state the β estimator used (e.g., linearized EB estimator β̂ ∝ ∑_ℓ EB_ℓ/EE_ℓ with MASTER deconvolution), the weighting scheme, the bandpower covariance used for the fit, nor how the SNR was computed (per-realization detection significance? mean/SE?).
  - No MC scatter or standard error on the recovered bias is provided; only point recovers are reported.
- Required fix: Explicitly write down the β estimator, the weight matrix/covariance used, the binning, the fit range, and the SNR definition. Report the mean and standard deviation of β̂ over the 500 MCs, and the standard error on the mean for the reported bias (e.g., β̂ = 0.238° ± σMC with σ̄ = σMC/√500). Provide a figure/table of the EB spectrum fit or a histogram of β̂ to demonstrate Gaussianity. Without this, the 20.32 “σ” is not auditable.

P1B-E4
- Location: References [15] (page 10)
- Problem: Reference contains internal line-number note and authorship appears inconsistent. Quoted: “Phys. Rev. Lett. 128, 091302 (2022), reports beta = 0.30 +/- 0.11 deg …; the value used at L256/L416 of P1B, arXiv:2201.07682.”
  - The “the value used at L256/L416 of P1B” is an internal manuscript bookkeeping artifact and must not appear in the bibliography.
  - Verify the correct author list for the PRL 128, 091302 (2022) Planck PR4 birefringence paper; the current author string (“P. Diego-Palazuelos, J. R. Eskilt, Y. Minami, M. Tristram, et al.”) seems unlikely for that PRL and should be corrected to match the citation’s journal entry.
- Required fix: Remove internal notes from references and correct the full bibliographic information (authors, title, journal, year, arXiv ID) to match the cited paper.

P1B-E5
- Location: Section III (page 3–4), Table II heading text (page 4)
- Problem: Presence of internal revision-log commentary. Quoted: “An earlier count erroneously quoted ‘98.6% quintom-B’ weight; in the actual converged chain …”
- Required fix: Remove all references to earlier draft counts or internal review history. State only the current chain’s results.

P1B-E6
- Location: Sections II–V and references [17] (pages 2–7, 10)
- Problem: Planck likelihood naming and citations are inconsistent (Planck 2018 PR3 vs NPIPE/PR4 vs CamSpec). E.g., Section V.A says “Planck 2018 NPIPE [17]” while [17] is “Planck 2018 results. VI. cosmological parameters” (PR3), not PR4/NPIPE; elsewhere, “Planck PR4/NPIPE” is referenced.
- Required fix: Precisely state which Planck release and which high-ℓ likelihood are used in each chain (PR3 Plik? PR4/NPIPE CamSpec TTTEEE? low-ℓ EE/TT version? lensing likelihood version) and correct the citations accordingly.

MAJOR

P1B-M1
- Location: Section IV (page 5)
- Problem: Beam/transfer treatment under map degradation is underspecified. The text says: “we degrade to Nside = 512 and apply the corresponding pixel window function. NaMaster’s NmtField is initialized with beam = b^Planck_ℓ w^pix_ℓ.” It is unclear whether an additional Gaussian smoothing was applied prior to degrading to Nside = 512 to control aliasing, and what exact beam for the Commander CMB Q/U map is assumed (Commander CMB map’s effective resolution is not simply “143 GHz 5 arcmin FWHM”).
- Required fix: Specify the exact effective beam of the input Commander CMB polarization map used, any additional smoothing applied during degradation, and confirm that the effective beam entering NaMaster matches the actual data (b_ℓ). Provide the Commander product ID and its documented beam. If a mismatch exists, recompute the bias with the correct beam.

P1B-M2
- Location: Section IV (page 5)
- Problem: “ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check).” Lower noise increases SNR and helps expose systematic biases; calling 10 μK·arcmin “worst case” is misleading (ACT DR6 polarization white-noise levels are ≲ 10 μK·arcmin; Planck’s are higher).
- Required fix: Rephrase this sentence to accurately describe the rationale for the chosen noise level (e.g., “Chosen to achieve high SNR per realization so that any pipeline bias is measured with small MC error”). If the intent was to test bias robustness to different noise levels, add at least one additional MC set at a higher noise representative of Planck polarization and report whether the bias changes.

P1B-M3
- Location: Section VI (pages 6–8), Eq. (2) and parameter ranges
- Problem: The numerical ALP field-displacement range Δφ/fa ∈ [0.2, 1.1] and the specific value “0.65 for m = H0, θi = 1” are asserted without any tabulated output, figure, or code pointer for the ODE integration. While the back-of-envelope β scaling checks out, the precise Δφ/fa envelope is load-bearing for the implied Caγ range and for the spectator fine-tuning discussion.
- Required fix: Provide either (i) a small table/figure showing Δφ/fa vs m/H0 for a few θi values (including θi ≪ 1 relevant to the spectator limit), or (ii) a code pointer and exact initial conditions/ODE tolerances used so a reader can reproduce (2) and the stated [0.2, 1.1] envelope.

P1B-M4
- Location: Section VI (page 7)
- Problem: “Independent cross-validation.—Liu et al. [11] … Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.” No comparator numerical values from [11] are given, so the stated σ-agreement cannot be audited.
- Required fix: Quote the H0 and σ8 constraints from [11] and compute the differences divided by the combined errors to support the 0.5σ/0.4σ claims.

P1B-M5
- Location: Abstract and multiple places (pages 1, 5–6)
- Problem: The paper juxtaposes “pipeline-recovery SNR” values (20–26σ) with published sky-detection significances (2.4–2.9σ and 3.6σ). While you include scope disclaimers, the SNR definition is still not explicitly non-comparable at every juxtaposition.
- Required fix: In each location where pipeline SNR appears near sky-detection σ (Abstract; Sec. IV opening; Conclusions), insert an explicit parenthetical “not directly comparable to sky-detection significance; this SNR refers to recovery of injected MC signals under our noise assumptions.”

MINOR

P1B-n1
- Location: Section III (pages 3–5)
- Problem: The “MB–H0 joint-posterior offset” section states: “corresponds exactly to the canonical 3.6σ Hubble tension…” The computed offset along the SN degeneracy is 3.2σ (0.155/0.049 ≈ 3.16), not “exactly” 3.6σ.
- Required fix: Soften wording to “consistent with” rather than “exactly,” or recompute the mapping if you wish to quantify a 3.6σ equivalence.

P1B-n2
- Location: Section VI (page 6)
- Problem: Units consistency for m ~ H0 are assumed (natural units). This is standard but should be explicitly stated once for clarity.
- Required fix: Add a one-line note that all cosmological-field equations are in natural units (c = ħ = 1), so m and H have the same units.

P1B-n3
- Location: Section IV (page 5)
- Problem: Mask description is terse. “C2 apodization at 2° scale” without specifying the base mask and resulting fsky computation method leaves ambiguity.
- Required fix: Identify the base mask product and show how fsky = 0.32 was computed (e.g., fraction of unmasked pixels after apodization thresholding).

P1B-n4
- Location: Section V.B (page 6)
- Problem: Version drift note “v3.5 original; v3.6.1 verification” without stating whether results changed.
- Required fix: Add a sentence confirming that upgrading Cobaya from v3.5 to v3.6.1 did not change posterior means/uncertainties beyond sampling noise, or quantify any differences.

P1B-n5
- Location: Table III (page 10)
- Problem: The “Claims classification” table is unconventional for PRD and includes terse entries (e.g., “Scope Defn.”) that are not self-explanatory.
- Required fix: Either move this to supplementary materials or expand entries to be self-contained, or remove it.

NIT

P1B-nt1
- Location: Throughout
- Problem: Occasional stylistic meta-language (“promised a Savage-Dickey ratio… the KDE estimator fails catastrophically”), informal emphasis (ALL CAPS “NOT”), and symbols (≠) in a claims table.
- Required fix: Adjust tone to standard PRD style; avoid ALL CAPS, and replace symbols or slang with formal phrasing.

P1B-nt2
- Location: Abstract and Sec. IV (pages 1, 5)
- Problem: “Planck Commander CMB polarization map” beam phrasing (“5 arcmin FWHM at 143 GHz”) may be misleading since Commander’s effective beam is documented per product, not per raw channel.
- Required fix: Rephrase to cite the exact Commander product and its documented effective beam.

P1B-nt3
- Location: Bibliography [3], [15] (page 10)
- Problem: Check author lists and years align with the exact cited datasets (ACT DR6, Planck PR4). “arXiv:2509.13654” implies a 2025 September submission; ensure title/authors correspond to the ACT DR6 birefringence analysis.
- Required fix: Verify and correct bibliographic entries.

Checks of arithmetic and dimensional consistency

- ΔNeff posteriors in Abstract and Table I match.
- H0 values and their 3.6σ tension with SH0ES: recomputed as (73.04 − 67.69) / sqrt(1.06^2 + 1.04^2) ≈ 3.60σ — consistent.
- MB–H0 constant computations are correct to rounding; the 3.2σ mapping is accurate, but wording (“exactly”) should be softened.
- Equation (3) β estimate using β ≈ αEM C/(4π) Δφ/fa: with α/(4π) ≈ 5.806×10^−4, C = 8, Δφ/fa ≈ 1.07 gives β ≈ 0.285° — consistent with 0.29°.
- Caγ Δφ/fa ≈ 10.3 from β = 0.342°: 0.342° = 5.97×10^−3 rad; dividing by α/(4π) ≈ 5.8×10^−4 gives ≈ 10.3 — consistent.
- Inverse-variance combination of Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°): β_comb ≈ 0.241 ± 0.061°, 3.92σ — consistent with text (3.9σ).
- Dimensional checks: ρ_a ∼ m^2 f_a^2 θ_i^2 has mass^4 units; Ω_a scaling with H0^2 M_Pl^2 is consistent up to O(1) factors — acceptable.

Use of multiple σ notions

The manuscript generally distinguishes pipeline SNR from sky-detection significance and labels the ΔNeff null test clearly. However, the lack of an explicit SNR definition (P1B-E3) still leaves room for confusion. Please address as per P1B-M5.

Length

At 10 pages, the manuscript is acceptable for a methods companion, provided the essential clarifications and corrections are made. No reduction needed if the above items are addressed.

Summary recommendation

MAJOR REVISIONS

Justification: The paper contains an incorrect and internally inconsistent covariance/pivot derivation (Table II, footnote b), dataset/likelihood inconsistencies (DESI DR1 vs DR2; S8 prior vs posterior), and an under-specified birefringence estimator/SNR that prevents reproducibility. At least one reference includes internal manuscript notes and likely mis-specified authorship. These are fixable, but they are essential for methodological rigor at PRD. Once corrected, the paper’s core claims (ΔNeff null proxy, pipeline validation plainly scoped, ALP consistency) can be supported.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (fresh-eyes)

ESSENTIAL

P1B-E7
- Location: Sec. III footnote 1 (page 3) and Conclusions (page 8) vs Table I (page 3)
- Problem: Internal inconsistency about the “Planck-only” chain. The text twice states “reported separately in Table I,” but Table I contains only two columns (Full-tension; Planck+BAO+SN) and no Planck-only column.
- Required fix: Either add the Planck-only column to Table I with its current status, or correct the text to say that the Planck-only chain is not shown in Table I.

P1B-E8
- Location: Dataset naming across Sec. V.A (page 6), Table II caption/footnote (page 4), and main text (pages 2–4)
- Problem: Inconsistent DES and BAO dataset labels beyond what was flagged previously. The body and Table II use “DES-Y5” for SNe and “DESI DR2,” while Sec. V.A lists “DES Y3 S8” and “DESI 2024 DR1 BAO.” This mixes Y3 vs Y5 and DR1 vs DR2 in different places and for different observables.
- Required fix: Provide a single authoritative mapping for each reported chain that specifies: BAO release (DR1 vs DR2), SN set (DES-Y5 vs Pantheon+), any S8 prior (DES Y3 or otherwise) with mean/σ, and Planck likelihood versions. Align all mentions accordingly.

P1B-E9
- Location: Appendix A (pages 8–9) vs Appendix C (page 9)
- Problem: Reproducibility contradiction for the ALP-EB likelihood. Appendix C claims dedicated MCMC fits using “Planck PR4 + ACT DR6 EB-spectrum likelihoods … combined with shared calibration covariance,” yet Appendix A says, “No CMB polarization map analysis code is provided beyond the NaMaster driver script; all published birefringence values are literature citations.”
- Required fix: Either (i) provide the EB-spectrum likelihood code/config (or an explicit pointer to the public Eskilt & Komatsu/ACT DR6 likelihoods used, with commit/tag, and how the shared calibration covariance was implemented), or (ii) remove the ALP-EB MCMC claims and restate them as literature-based inference only. Also deposit the ALP-EB likelihood YAML(s) and sampler configs alongside the reported chains.

MAJOR

P1B-M6
- Location: Conclusions (page 8) and Table II footnote a (page 4)
- Problem: Broken/incorrect internal cross-references. Conclusions say “see §VI body text” for the NaMaster pipeline bias, but the pipeline bias is in §IV, not §VI. Table II footnote a refers to “§ Headline-result discussion,” which does not exist as a titled section.
- Required fix: Correct both cross-references: point the pipeline-bias pointer to §IV, and either name and point to the correct section that contains the “headline-result discussion” or remove the nonexistent-section reference.

MINOR

P1B-n6
- Location: Sec. III (pages 4–5), “MB–H0 joint-posterior offset check”
- Problem: Dimensional clarity. The degeneracy is written as MB − 5 log10(H0) ≈ const, but strictly the dimensionless form uses h ≡ H0/(100 km s−1 Mpc−1). Using H0 directly implies an implicit unit choice inside the log.
- Required fix: State explicitly that H0 is in km s−1 Mpc−1 and the constant absorbs the 100 km s−1 Mpc−1 factor, or rewrite the relation with h to avoid logging a dimensionful quantity.

P1B-n7
- Location: Sec. VI (pages 6–7)
- Problem: The stated “required Caγ spans ∼ 9–51” is presented immediately after reporting ALP MCMC runs with Caγ fixed to {4, 8, 12}. The 9–51 interval is not a sampled posterior range but a derived requirement from Caγ Δφ/fa ≈ 10.3 using the Δφ/fa envelope.
- Required fix: Clarify that 9–51 is an inferred requirement from the Δφ/fa envelope (not the MCMC posterior), and show the algebra or a small table mapping representative Δφ/fa values to the implied Caγ.

P1B-n8
- Location: Appendix C (page 9)
- Problem: R̂ reporting for ALP MCMC is ambiguous. “R̂ − 1 < 0.01 across all 3 configurations (achieved at Ntot = 9,720 accepted samples post burn-in).” It is unclear whether each configuration had multiple chains (required for R̂), or whether R̂ was computed improperly across configurations with different fixed Caγ.
- Required fix: Report, per configuration: number of chains, chain lengths, and R̂ per sampled parameter. If there was only one chain per configuration, drop R̂ or rerun with ≥2 chains to make R̂ meaningful.

P1B-n9
- Location: Fig. 1 caption (page 5) vs footnote 1 (page 3)
- Problem: Sample-count presentation is confusing. The caption cites 119,617 post-burn-in samples for the full-tension plot after GetDist thinning, while footnote 1 gives 123,368 as the 70% post-burn-in figure before thinning.
- Required fix: Add one clarifying sentence in the caption noting the thinning factor/method so readers do not mistake the discrepancy for an arithmetic error.

NIT

P1B-nt4
- Location: Sec. IV (page 5), NaMaster configuration line
- Problem: Typographical/formatting roughness in code-like text: “beam=b^Planck_ℓ w^pix_ℓ” and options like “purify b=True, purify e=False” appear as prose. This reads as pseudo-code and is easy to misinterpret.
- Required fix: Present these as explicit variable names or as a short code snippet (or plain-text variable definitions), e.g., “beam = b_ell^Planck × w_ell^pix; purify_b = True; purify_e = False,” to avoid ambiguity.

Explanation
These items were not covered in the initial review. They involve internal contradictions (Planck-only chain not in Table I), new cross-reference errors, a critical reproducibility gap for the ALP EB-likelihood MCMC, and several clarity/dimensional-consistency issues that PRD typically requires to be fixed.