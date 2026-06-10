# P1B R23conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 683.5s

---

META-REFEREE REPORT — new issues not caught by the five prior referees

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: Sec. IV “Noise model and injections,” p. 6
- Why others missed it: Everyone audited SNRs and bias attribution but not the unit-normalization step that actually sets the noise amplitude.
- Specific problem (quote): “Each realization adds white noise at the ACT-like level ΔP = 10 μK·arcmin …”
- Issue: The paper never specifies how ΔP in μK·arcmin is converted to per-pixel RMS at Nside = 512 for Q and U, nor whether Q and U use the same σpix or a √2 factor is applied anywhere. Without stating σpix = ΔP × [ (π/180/60)/√Ωpix ] and Ωpix = 4π/Npix, reproducibility of all EB scatter/SNR numbers is underdetermined.
- Required fix: Add the explicit conversion from ΔP (μK·arcmin) to per-pixel RMS (μK) at Nside = 512, state whether the same σpix is used for Q and U, and give the numeric σpix actually injected (≈ 1.45 μK at Nside = 512 for ΔP = 10 μK·arcmin).

P1B-META-E2
- Severity: ESSENTIAL
- Section + page: Cross-reference inconsistency, Sec. IV (p. 5) vs Sec. VI (pp. 8–9)
- Why others missed it: Reviewers focused on the ACT citation and significance fusion, not on this internal cross-reference contradiction.
- Specific problem (quote): Sec. IV: “Birefringence measurements are adopted from the published literature: β = 0.30° ± 0.11° (Planck NPIPE) and β = 0.215° ± 0.074° (ACT DR6). The spectator ALP analysis (Sec. VI) uses these published values.” Sec. VI instead adopts βobs = 0.342° ± 0.094° (WMAP+Planck) for the ALP likelihood and uses the ACT/Planck numbers only as an auxiliary cross-check.
- Required fix: Reconcile the statements. In Sec. IV, change to: “The ALP analysis in Sec. VI uses the Eskilt & Komatsu joint WMAP+Planck summary likelihood (β = 0.342° ± 0.094°); the Planck NPIPE and ACT values are quoted only for context and an auxiliary inverse-variance cross-check.”

P1B-META-M1
- Severity: MAJOR
- Section + page: Sec. IV “Noise model and injections” (β-recovery method), p. 6
- Why others missed it: Attention centered on SNR definition and mask effects, not on the estimator optimality.
- Specific problem (quote): “The angle is recovered … by an unweighted χ² template fit of the decoupled CEBℓ band-powers…”
- Issue: Using an unweighted fit across bins with very different variances can bias the amplitude estimate low (especially when noise-only high-ℓ bins are included). No test is shown that an inverse-covariance weighting (or excluding ℓ > ℓmax,signal) yields the same β̂. This is a hidden-conditioning risk for the reported 12% multiplicative under-recovery.
- Required fix: Either (a) switch to inverse-variance (or full-covariance) weighting and report β̂ and bias under that estimator, or (b) add a robustness test showing that weighted and unweighted fits agree within the quoted 0.04° floor and that including/excluding noise-only bins (>1024) does not change β̂ at a material level.

P1B-META-M2
- Severity: MAJOR
- Section + page: Sec. IV “Simulated skies,” p. 6
- Why others missed it: One reviewer noted the Cℓ template mismatch; none flagged the unrealistic BB shape itself.
- Specific problem (quote): “plus a lensing-like BB component (CℓBB = 0.05 CℓEE).”
- Issue: A constant 5% of EE across all ℓ is not lensing-like; the true BB/EE ratio is strongly ℓ-dependent. This nonphysical BB spectrum can distort the EB template mismatch and the inferred amplitude-independent bias attribution.
- Required fix: Replace the BB mock with a realistic ΛCDM lensing BB spectrum (from CAMB/CLASS) and recheck the bias. At minimum, add a test varying the BB amplitude and shape to demonstrate the 12% multiplicative under-recovery is insensitive to reasonable BB modeling.

P1B-META-M3
- Severity: MAJOR
- Section + page: Sec. IV “Mode-coupling matrix and binning,” pp. 6–7; method used in β-fit paragraph
- Why others missed it: One review asked to clarify that SNR templates zero CEE,b beyond 1024; no one checked if the β-fit itself excludes noise-only bins.
- Specific problem (quote): “Spectra are band-power-binned into 20 linear bins spanning 30 ≤ ℓ ≤ 3Nside = 1536 (bins above the map band limit ℓ = 1024 carry noise only).”
- Issue: It is unspecified whether those noise-only bins are included in the β-χ² fit (as stated, the fit is “unweighted,” which would down-weight the signal by adding pure-noise bins). This can contribute to the measured 12% multiplicative bias.
- Required fix: State explicitly whether β fits exclude bins with ℓ > 1024 or, if included, confirm CEE,b = 0 and show that including them does not change β̂ within the 0.04° floor. Provide numbers for with/without high-ℓ bins.

P1B-META-M4
- Severity: MAJOR
- Section + page: Sec. III, “MB–H0 joint-posterior offset check,” p. 5
- Why others missed it: Reviewers recalculated the 3.2σ but did not check the degeneracy form.
- Specific problem (quote): “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const along the SN distance-modulus degeneracy.”
- Issue: The standard SN degeneracy is MB − 5 log10(h) (with h = H0/100 km s−1 Mpc−1). Using H0 instead of h is dimensionally inconsistent and misstates the form of the constraint. While the absolute offset cancels in differences, the paper should present the correct quantity.
- Required fix: Replace by “MB − 5 log10(h) ≈ const” (or equivalently MB − 5 log10(H0) + 10 = const), and recompute the two constants with h to demonstrate the same 0.156 mag offset; update the text accordingly.

P1B-META-M5
- Severity: MAJOR
- Section + page: Sec. IV “Scope note,” p. 6; Sec. IV “Sky-fraction sweep,” p. 7
- Why others missed it: The fsky sweep was checked; the apodization scale was not.
- Specific problem (quote): The analysis fixes a single apodization, “Gaussian smoothing … 2° FWHM,” and later attributes the multiplicative under-recovery to “apodization-induced power suppression.”
- Issue: No test varies the apodization length (e.g., 0.5°, 1°, 3°) to demonstrate that the bias scales as expected with apodization rather than being dominated by other effects (e.g., template mismatch or binning). This is a missing test that materially supports the claimed attribution.
- Required fix: Add an apodization-scale sweep (≥ two additional FWHM values) at fsky ≈ 0.32 and report β̂ and bias; show that the 12% multiplicative bias and ~0.03–0.04° absolute floor behave consistently with apodization expectations.

P1B-META-M6
- Severity: MAJOR
- Section + page: Sec. IV “Mask,” p. 6
- Why others missed it: Focus was on sign-symmetry and SNR; not on selection logic.
- Specific problem (quote): “An ACT-like footprint (Galactic cut |b| > 20° plus declination cut dec ∈ [−65°, +25°]), apodized by Gaussian smoothing of the binary mask at 2° FWHM… No E/B purification is applied.”
- Issue: The footprint and the “no purification” choice are post-hoc and unregistered. There is no pre-specified rationale (beyond being “ACT-like”) and no sensitivity test showing that β̂ and the bias do not depend materially on footprint geometry or purification choice. This opens the door to selection-induced bias in a methods validation.
- Required fix: Document the pre-specification (if any) of the footprint and purification setting; otherwise, add a minimal robustness panel: repeat the 500-MC β = 0.27° injection on (i) a larger Galactic cut (|b| > 30°) and (ii) with purify_b=True, and report β̂ shifts. Clarify that the canonical mask was not chosen after inspecting outcomes.

P1B-META-M7
- Severity: MAJOR
- Section + page: Sec. VI “Birefringence value” and “MCMC parameter estimation,” pp. 9–10
- Why others missed it: Reviewers addressed the Gaussian-summary likelihood and coupling ranges, not this specific consistency gap.
- Specific problem (quote): “The prediction spans β ≈ 0.17–0.43° over Cαγ ∈ [4,12], m/H0 ∈ [1,3], θi ∈ [0.5,2]…” and later “the spectator-consistent corner θi ∼ 0.1 … requires ~25× misalignment tuning… pushing the required coupling well above KSVZ/DFSZ O(1).”
- Issue: The paper never quantifies the required Cαγ range in the explicitly “spectator-safe” subset (e.g., θi ≤ 0.1, Ωa ≪ 1). Readers are told qualitatively it is “well above” O(1) but are not given the actual numeric band (which, by the paper’s own Δφ/fa scaling, is significantly above the [9,51] stated for θi ∈ [0.5,2]). This leaves the main takeaway for the spectator case under-specified.
- Required fix: Provide the explicit Cαγ range required to match βobs in the θi ≤ 0.1 (or Ωa ≤ 0.01) subset (e.g., a posterior slice or an analytic estimate using the measured Caγ Δφ/fa ≈ 10.3). State the fraction of prior/posterior mass that survives in this spectator-safe region after imposing βobs.

P1B-META-m1
- Severity: MINOR
- Section + page: Sec. IV “Mode-coupling matrix and binning,” p. 6
- Why others missed it: Attention focused on references and arithmetic; this is a reproducibility nit.
- Specific problem (quote): “The Mℓℓ′ matrix is computed via NmtWorkspace.compute coupling matrix…”
- Issue: The API and options (spin-2 field flags, n_iter, binner settings, bandpower window definition) are not stated. These choices can change deconvolution at the sub-percent level relevant to the 12% bias discussion.
- Required fix: Add the essential NaMaster configuration details (spin=2, mask normalization, n_iter or defaults, binning edges, and whether isotropic approximation is used) or point to a committed config file in the repository.

P1B-META-m2
- Severity: MINOR
- Section + page: Sec. V.A “Datasets and Configuration,” p. 7; Table III
- Why others missed it: Focus was on the DESI DR2 citation provenance; this is a clarity nit.
- Specific problem (quote): “The exact Cobaya likelihood blocks of all five chains are listed in Table III.”
- Issue: Table III lists five configurations but the text sometimes calls the four ΛCDM+ΔNeff chains “all four,” while the “iter2 w0wa” chain is methodologically separate. The present tense “are listed” is fine; but the paper elsewhere mixes “four ΛCDM+ΔNeff chains” and “five chains total.” This can confuse readers about which posterior numbers feed which sections.
- Required fix: Add one sentence clarifying that Table I summarizes only the two frozen ΛCDM+ΔNeff chains, while Table II corresponds to the separate iter2 w0wa chain, and that the Planck-only and Planck+BAO exploratory rows are not part of Table I.

P1B-META-N1
- Severity: NIT
- Section + page: Sec. IV (several places)
- Why others missed it: They focused on numerical issues; this is stylistic but aids clarity.
- Specific problem (quote): “MASTER mode coupling” (uppercase) is used informally; NaMaster is lowercase in text and uppercase in code; MASTER refers to the Hivon et al. 2002 formalism, not the package.
- Required fix: Use “MASTER (Hivon et al. 2002) mode-coupling” once with a citation, and “NaMaster” consistently for the package.

Meta-review recommendation
MAJOR REVISIONS

Rationale: Beyond the serious citation-provenance problems already flagged by Reviewer 5, this meta-review adds several methodology and cross-reference gaps that materially affect reproducibility and interpretation: the missing ΔP→σpix normalization (E1), the internal contradiction about which birefringence measurement drives the ALP likelihood (E2), and multiple untested conditionings in the NaMaster validation (M1–M6). These are fixable but require concrete methodological additions and targeted reruns.

Union-of-reviews blocker count and survival outlook
Across all six reviews, I count multiple Essentials (fabricated/future-dated references; negative-β contradiction; mass-prior conversion error; ΔP normalization; ACT/WMAP+Planck cross-ref; abstract-significance sourcing) and many Majors (estimator weighting; BB modeling; bin-inclusion; apodization dependence; spectator-range quantification; evidence reporting). Given these, my confidence that the paper would pass independent, external peer review without substantial revision is low. With a focused revision that (i) replaces speculative citations with real, public sources, (ii) harmonizes all cross-references, and (iii) adds the missing methodological details and robustness checks listed above, the paper could meet PRD’s standards as a technical companion.