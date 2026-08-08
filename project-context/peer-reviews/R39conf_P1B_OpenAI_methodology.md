# P1B R39conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1b_mcmc_companion.pdf` md5=06410d7c pages=20
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7621 chars)
**Wall time**: 297.1s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

I have read the full manuscript, all figures, tables, equations and captions. I recomputed the quoted numerical results wherever possible, checked dimensional consistency and estimator definitions, and audited the abstract and conclusions against the body. Below are my findings, classified by severity, with page-specific citations and required fixes.

ESSENTIAL

P1B-E1 (Data availability and immutable artifacts) — Sec. “Data and Code Availability,” p. 14; Appendix A, p. 14–15; Appendix A “HuggingFace datasets”
Problem: The paper repeatedly states “DOI assignment is pending (identifiers will be inserted at submission)” and references a mutable GitHub repository (“in-tex v1B.0.68 stamp,” “matching version-stamp commit in the repository git log”). This is not acceptable for PRD reproducibility. The manuscript also contains extensive in-text references to internal file paths and run folders.
Required fix: Provide immutable, citable archival identifiers (DOIs) for: (i) the exact code snapshot used (e.g., Zenodo archive of the GitHub repo with a tag), (ii) the frozen chains and NaMaster/ALP artifacts, and (iii) configuration YAMLs and scripts. Replace all “pending” language with final DOIs and include the exact commit SHA(s) in the manuscript. Move internal path listings (e.g., reproducibility/…, pipelines/…) to a curated Supplementary Material or data descriptor; keep the paper text free of repository plumbing.

P1B-E2 (Internal versioning/audit tags in the body) — Sec. “Data and Code Availability,” p. 14; Appendix A, p. 14–15; various
Problem: The manuscript includes internal versioning/audit language (e.g., “in-tex v1B.0.68 stamp,” “entry for the v1B.0.59 closure wave,” “closure wave,” “spin torsion.input.yaml”) and operational commentary (“Column-permutation warning for JSON artifacts,” “artifact-level process discussion is kept in the repository”). PRD does not publish build logs and internal workflow notes in the body text.
Required fix: Remove internal audit/version-process prose from the main text. If absolutely needed, place a concise reproducibility note in Supplementary Material that lists the immutable DOIs and commit hashes without internal codenames, and delete the “column-permutation bug” narrative from the paper (it belongs only in the repository CHANGELOG).

P1B-E3 (Release-pairing consistency of Planck likelihoods) — Sec. III, pp. 3–5; Sec. V.A, p. 9; Table I, p. 18
Problem: The main ΛCDM+ΔNeff results use PR4/NPIPE high-ℓ CamSpec paired with 2018 low-ℓ TT/EE and 2018 lensing. The authors acknowledge they did not run a pairing-swap test and that any pairing-induced bias is “unquantified.” At the quoted precision on ΔNeff and H0, release-mixing can matter.
Required fix: Add a release-consistent control: either (i) PR4+PR4-only (NPIPE high-ℓ, PR4 low-ℓ EE/TT and lensing) or (ii) 2018+2018-only (all three likelihoods from 2018), using the identical priors. Report the shifts in ΔNeff, H0, S8 relative to the mixed pairing at the 0.1σ level. If PR4-consistent low-ℓ/lensing likelihoods are unavailable, state this explicitly and include a quantitative robustness bracket using Planck-only runs under both pairings.

P1B-E4 (Apples-to-apples verification chain) — Sec. V.B “Independent re-run cross-check,” p. 10
Problem: The “independent re-run” uses lollipop.lowlE (2020) instead of the 2018 low-ℓ EE likelihood used in the frozen chains. The presented 0.04σ agreement is thus not an exact apples-to-apples verification but a test under a different likelihood stack.
Required fix: Re-run the verification chain with the exact same Planck low-ℓ and lensing likelihoods as in the frozen Planck+BAO+SN chain (or, alternately, re-freeze all results with the lollipop low-ℓ and adjust claims). Clearly state identical likelihood stacks when presenting numerical agreement.

P1B-E5 (“Systematic floor” claim for NaMaster bias) — Sec. IV, pp. 6–9; Fig. 3, p. 7
Problem: The text “The worst-case |bias| = 0.040° is carried forward as the NaMaster systematic floor” promotes a configuration-specific Monte Carlo bias (unweighted fit, one noise level, one binning, one ℓ-range, no beam, no anisotropic noise) to a general “systematic floor.” While you do show limited robustness (apodization, purification, sky fraction), the dependence on noise properties, binning scheme, ℓ-range, and beam mismatch is not explored. Calling it a “floor” overgeneralizes.
Required fix: Either (a) expand the robustness suite to quantify the bias under: alternative binning/ℓ-ranges, anisotropic/1/f noise realizations, multiple noise levels, and modest beam mismatch; report the spread in the recovered bias and a justified “floor” with uncertainty; or (b) relax the claim and present 0.040° strictly as “observed bias in this specific configuration,” removing “systematic floor” phrasing. In either case, provide an uncertainty on the bias estimate from the 500-MC mean (SE ≈ σβ/√N) alongside the central value.

P1B-E6 (Spectator ALP energy-density calculation) — Sec. VI, pp. 10–13; Appendix C, p. 16; Table IV, p. 20
Problem: The “spectator-safe” fraction Ωa < 0.01 = 13% is quoted, but the precise definition and computation of Ωa are not given. In particular, the expression for ρa today in the anharmonic potential, the onset of oscillations, and the mapping from sampled (ma, θi, fa) to Ωa(z=0) are not specified in the text.
Required fix: Add a short subsection in Sec. VI (or Appendix C) specifying exactly how Ωa is computed in post-processing: the potential used (V = m^2 f_a^2 [1 − cos(ϕ/fa)]), the treatment of anharmonic corrections to the onset-of-oscillations and energy density, whether linearized or full-ODE energy density is integrated, and the cosmology assumed for H(z). Provide one worked numerical example (e.g., at the posterior median m and θi) showing Ωa evaluation end-to-end. This is necessary to reproduce the quoted 13% and the θi ≤ 0.1 “sliver” characterization.

P1B-E7 (Abstract/conclusions provenance language) — Abstract, p. 1; Sec. VII Conclusions, p. 13–14
Problem: The abstract and conclusions contain process/internal phrasing that does not belong in the scientific narrative of a PRD paper (e.g., “The worst-case bias … is carried forward as the pipeline-recovery bias floor — both are MC pipeline-recovery figures, not sky-measurement systematics,” and in Sec. VII “planned” release-pairing run, see E3).
Required fix: Calibrate the abstract and conclusions to report only results that are fully supported by completed analyses within the paper. Remove “planned” analyses in conclusions; promote them to firm results or move to “Future work” statements that do not affect headline claims.

MAJOR

P1B-M1 (ℓ-range/binning robustness for NaMaster pipeline) — Sec. IV, pp. 6–9; Fig. 3, p. 7
Problem: The estimator is evaluated in 20 linear bins over 30 ≤ ℓ ≤ 1536 (maps limited to ℓ ≤ 1024). You state “an ℓ-range robustness sweep is not part of the present MC suite.” Given the unweighted-fit bias is shown to be driven by high-ℓ noise-dominated bins, the ℓ-range/binning choice is consequential.
Required fix: Add at least one robustness test that removes the highest-ℓ bins (e.g., 30–512) and/or uses logarithmic binning to de-weight high-ℓ, and report the recovered β and bias. This is especially important if any “floor” language remains.

P1B-M2 (Explicit EOM and numerical details for ALP) — Sec. VI, pp. 10–12; Appendix C, p. 16
Problem: While the EOM is written, details of the ODE integrator settings are only alluded to (“fixed-step fourth-order Runge–Kutta re-integration … zinit = 3000, θ̇ = 0”). There is no statement of the step size/control, integration variable (ln a vs a), or stopping condition. For PRD reproducibility without external code, more detail is required.
Required fix: Provide a concise description of the ODE integration used to produce Δϕ/fa(m, θi): integration variable, initial conditions (θi definition epoch, whether θ̇ = 0 is enforced in radiation era), step-size control/tolerance, and the ΛCDM H(z) parametrization used. A one-paragraph numerical methods note suffices.

P1B-M3 (Coupling benchmarks) — Sec. VI, pp. 11–12
Problem: The statement “Even the lower end exceeds the standard KSVZ/DFSZ benchmark range, which predicts |Caγ| ∼ O(1)” lacks a reference and does not specify the sign conventions and normalization used for Caγ in those models.
Required fix: Cite a standard reference for axion/ALP photon couplings (e.g., PDG or a review) and explicitly state the normalization of Caγ in your convention and the benchmark values for comparison.

P1B-M4 (Consistency of Planck+BAO+SN S8 tension calculation) — Sec. III(d), p. 5; Table I caption, p. 18
Problem: You quote S8 tensions and overlap integrals. While your arithmetic checks out for the pairwise 2.5–2.6σ calculation, the overlap integral computation method is only described informally. The figure/overlay artifact is not provided in the paper.
Required fix: Either include a small inset figure showing the 1D S8 posteriors and their overlap, or move the overlap statistic to Supplementary Material and keep in the text only the standard σ-level difference (with the simple combined error).

MINOR

P1B-n1 (Figure axes units) — Fig. 1 and Fig. 2, p. 6
Problem: The corner-plot axes for H0, σ8, S8, Ωm, ns do not carry units (H0) or definitions (S8).
Required fix: Add “km s−1 Mpc−1” to the H0 axis labels and remind the reader that S8 ≡ σ8 (Ωm/0.3)1/2 either in the caption or an axis note.

P1B-n2 (Noise model detail) — Sec. IV, p. 7
Problem: The white-noise model sets identical σpix for Q and U with “no √2 factor.” While this may be fine (common in CMB mapmaking), a brief justification would aid readers.
Required fix: Add a sentence noting the convention used for ΔP and that Q and U are drawn with identical per-pixel RMS corresponding to ΔP via σpix = ΔP / √Ωpix.

P1B-n3 (ACT DR6 citation details) — Ref. [4], p. 16–17
Problem: The ACT DR6 preprint is listed as arXiv:2509.13654 (year 2025). Please verify the bibliographic details (authors, title, arXiv ID and year) to ensure they match the cited numbers.
Required fix: Confirm and correct [4] to the final arXiv/journal entry at proof stage.

P1B-n4 (CMB-S4 σ(Neff)) — Sec. III “Key finding,” p. 5
Problem: You cite σ(Neff) ∼ 0.03 from the 2016 CMB-S4 book. More recent forecasts exist.
Required fix: Either update the citation to a current CMB-S4 forecast paper or qualify the number as “representative” with the 2016 citation.

P1B-n5 (Acknowledgment of AI tool) — Acknowledgments, p. 14
Problem: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant…” PRD has evolving policies on AI tool acknowledgments; this sentence is not methodologically problematic but may need to be removed or adjusted at editorial request.
Required fix: Be prepared to remove or rephrase per PRD editorial policy.

P1B-n6 (Terminology: “floor” vs “bound”) — Sec. IV, pp. 8–9; Conclusions, p. 14
Problem: Even with additional robustness, “systematic floor” can be misread as an instrument/system-imposed lower bound. Since the study is synthetic and method-specific, “pipeline bias observed in MC” is clearer.
Required fix: Prefer “observed pipeline bias” or “configuration-specific bias” unless a more general lower bound is actually justified by expanded tests (see E5/M1).

NIT

P1B-N1 (Typographic consistency) — Throughout
Problem: Low-ℓ sometimes appears as “low-ℓ” vs “lowl”; space around “km s−1 Mpc−1 ;” minor punctuation issues.
Required fix: Standardize typographic conventions (low-ℓ, spaces before semicolons, etc.) across the manuscript.

P1B-N2 (Hyphenation and unicode) — Throughout
Problem: Frequent use of long dashes and unicode degree signs can create typesetting inconsistencies.
Required fix: Ensure journal-compliant LaTeX macros are used for dashes and degrees.

Quantitative cross-checks performed

- Hubble tension: (73.04 − 67.68)/√(1.06^2 + 1.04^2) = 3.61σ — consistent with the stated ~3.6σ.
- NaMaster under-recovery: 0.238/0.27 = 0.8815 → 11.85% multiplicative bias; 0.302 − 0.342 = −0.040° — matches text.
- fsky scaling of σβ: 0.029°×√(0.85/0.32) ≈ 0.047° — matches the rerun 0.046°.
- Birefringence normalization: α/(4π) = 7.297×10−3/(4π) = 5.81×10−4; × 8 × 1.06 = 4.93×10−3 rad → 0.282° — consistent.
- Coupling–displacement product: βobs = 0.342° = 5.966×10−3 rad; (β)/(α/4π) ≈ 10.27 — consistent with 10.3.
- w0wa pivot: with Cov(w0,wa)=−0.00729 and Var(wa)=(0.1864)^2, 1 − ap = 0.210, zp = 0.27; σwpivot ≈ 0.0193 — consistent.

Abstract–body consistency

I re-read the abstract after the full body. All numerical values in the abstract (ΔNeff, H0, SH0ES, β recovery values, bias magnitudes, m ≃ 36 H0, Ωa tuning, 3.6σ Planck/WMAP result) are traceable to the body and internally consistent within rounding. The abstract repeatedly emphasizes scope limitations; this matches the body.

Stand-alone-readership

The paper is largely self-contained for its three tasks (ΔNeff proxy, NaMaster validation, ALP check). However, the heavy reliance on repository paths and internal artifact labels in the body (rather than a clean methods summary with consolidated references to immutable archives) undermines stand-alone readability and must be fixed (E1–E2).

Length

For a PRD methods paper, 20 pages are acceptable given three distinct analyses. However, once the internal-operations prose is moved to Supplementary Material, the main text could likely be shortened by 2–3 pages without loss of substance.

## Summary recommendation
MAJOR REVISIONS

The core numerical results are sound, internally consistent, and carefully scoped. However, publication in PRD requires (i) immutable, citable archival artifacts and removal of “pending”/internal-version language; (ii) a release-pairing control for the Planck likelihood stack at the quoted precision; (iii) a clarification or expansion regarding the NaMaster “systematic floor” claim; and (iv) a precise in-paper definition of the ALP energy-density calculation that underlies the “spectator-safe” subset. Addressing these essential and major issues should be straightforward for the authors and will bring the manuscript to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes pass)

P1B-E8 (ALP likelihood-to-Ωa mapping: fixed H0 vs marginalization) — Sec. VI, Fig. 4 caption, Appendix C
Problem: The ALP chains use a Gaussian summary likelihood on βobs, independent of cosmology, but Ωa depends explicitly on H0 via ρcrit ∝ H0^2. The text and Fig. 4 caption fix H0 = 67.7 km/s/Mpc (= 1.44×10−33 eV) for the mass-prior mapping, but it is not stated whether this same fixed H0 is used when computing Ωa for the “spectator-safe” fractions (13% with Ωa < 0.01, 44% with Ωa < 0.1). Using a fixed H0 rather than marginalizing over the MCMC ΛCDM posterior (or over a prior) can shift those fractions at the percent level and is required to reproduce the 13% figure precisely.
Required fix: State explicitly whether Ωa(z=0) is evaluated with a fixed H0 (and what value), or marginalized over an H0 distribution. If fixed, quantify the sensitivity of the Ωa-fractions to a ±1σ shift in H0. Include the exact H0 used in the Ωa post-processing.

P1B-M5 (Estimator comparability claim needs evidence) — Sec. IV (“Canonical estimator choice”), pp. 8–9
Problem: The manuscript asserts the unweighted χ2 template fit “matches the estimator configuration used in the public NaMaster driver scripts released by the published birefringence analyses (e.g., [5]).” Eskilt & Komatsu [5] do make specific weighting choices and treat covariances in their public pipeline. Without a concrete pointer, this “same as published” claim is not verifiable.
Required fix: Cite the exact public script/function and commit/DOI (or line numbers) from [5]’s repository demonstrating that the EB–template fit is unweighted across bins. If the published pipeline uses a different weighting or covariance treatment, rephrase to “we adopt an unweighted fit for simplicity,” and do not claim equivalence.

P1B-M6 (Rotation periodicity/likelihood topology not fully specified) — Sec. VI, p. 11–12; Appendix C
Problem: The text notes β ≡ β + n × 90° degeneracy and argues it is harmless because support is |β| ≲ 0.7°. However, the likelihood actually has multiple stationary points (including sign and 45°-shift ambiguities in EB/TB depending on the estimator). With a Gaussian summary likelihood, the handling of multi-modal periodic structure is not documented.
Required fix: Add a sentence clarifying that the Gaussian summary likelihood is defined on the principal branch β ∈ (−45°, +45°], that no multi-modal structure is modeled, and that this approximation is valid because the posterior mass is confined to |β| ≪ 45°. If any wrapping was disabled in code, state it explicitly.

P1B-M7 (Planck lensing interface inconsistency in the “independent re-run”) — Sec. V.B, p. 10; Table III
Problem: The “independent re-run” uses planckpr4lensing with lollipop.lowlE, while the frozen Planck+BAO+SN chain uses planck 2018 lensing.clik and lowl.EE (2018). This compounds two differences (low-ℓ EE and lensing) in the verification. The body text highlights only the low-ℓ EE difference.
Required fix: Either (i) redo the verification run with exactly the same low-ℓ and lensing likelihoods as the frozen chain, or (ii) explicitly acknowledge both changes (low-ℓ EE and lensing) and refrain from presenting the 0.04σ agreement as a direct apples-to-apples verification.

P1B-M8 (Template/ℓ-range treatment creates silent constraints from bins above the map band limit) — Sec. IV, pp. 7–8
Problem: The minimization includes bins up to ℓ = 1536 while synfast maps carry signal only to ℓmax = 1024. The template CEE,tmpl is set to zero above ℓmax, making those bins contribute a β-independent constant to χ2. This is fine in principle, but it should be stated that these bins play no role in the minimization and do not affect the recovered β. The current text only says “changes nothing,” without stating why.
Required fix: Add a one-line analytic justification (∂χ2/∂β = 0 for bins with CEE,tmpl = 0), and state that these bins are effectively excluded from the fit. Optionally, report the recovered β with those bins dropped to show numerical identity (to machine precision).

P1B-m7 (Pixel window cancellation assumption needs a precise statement) — Sec. IV, p. 7
Problem: The manuscript asserts that the Nside = 512 HEALPix pixel window “cancels identically” between decoupled bandpowers and the template because both are at Nside = 512. Cancellation is exact only if the same window and synthesis/convention are used in both the map-making and template evaluation. This is likely true here, but not documented.
Required fix: State explicitly that both map spectra and the CEE template were evaluated using the same HEALPix pixel window function and convention, and that neither was deconvolved. If a healpy default was relied upon, cite the function and version.

P1B-m8 (H0−MB degeneracy relation: notation/constant) — Sec. III, “MB–H0 joint-posterior offset check,” p. 5
Problem: The dimensionless form “MB − 5 log10(H0/[km s−1 Mpc−1]) + 10 = const” is used alongside “MB − 5 log10(h) = const.” While equivalent, the origin of the “+10” is not shown, which may confuse readers.
Required fix: Add a brief parenthetical derivation showing MB − 5 log10(H0) + 10 = MB − 5 log10(h), so the constant is identical in either form.

P1B-m9 (Numerical example for CPL H(z) difference should quote inputs) — Sec. III “Physics interpretation,” p. 4
Problem: The text states “H(z = 0.5) differs by ≈ +1.7%” for the CPL posterior mean but does not show the Ωm and H0 values actually used in that computation. Reproducing the figure requires those numbers.
Required fix: Append “for Ωm = 0.314 and H0 = 67.19 km/s/Mpc” (or the exact values used) to the sentence so readers can reproduce the 1.7% result directly.

P1B-m10 (Planck low-ℓ/lensing interface choices for w0wa chain) — Table III; Table II
Problem: The w0wa chain uses planck 2018 lensing.native (not .clik). The choice can shift posteriors slightly, but is not motivated in the text.
Required fix: Add a short note explaining why the native lensing likelihood was chosen for the w0wa chain and whether it produces any measurable shift versus .clik for this stack (a one-line test or citation suffices).

P1B-n7 (Repository label vs citation label mismatch for SH0ES) — Sec. III(c), p. 5; Ref. [9]
Problem: The likelihood name H0.riess2020Mb is used, but the cited reference [9] is Riess et al. 2022. This may confuse readers about which calibration is actually used.
Required fix: Clarify in text that the Cobaya likelihood is labeled “riess2020Mb” but corresponds to the 2022 SH0ES calibration values you quote, and confirm the exact MB prior numbers again at proof stage.

P1B-N3 (Figure axis labeling for β SNR comparisons) — Sec. IV; Fig. 3 caption, p. 7
Problem: The caption quotes “template-fit SNR” values (20.32, 25.71), while the body later discusses per-realization β/σβ ratios (e.g., 8.1, 7.2). The caption should explicitly say “template-fit SNR (not the significance of βˆ per realization),” to avoid misinterpretation by readers scanning figures only.
Required fix: Add a parenthetical in Fig. 3 caption clarifying that SNR refers to the matched-template significance computed from per-bin MC scatter, not |βˆ|/σβ.

Why these are new: These items were not included in the initial report. They focus on additional reproducibility clarifications (H0 treatment for Ωa; explicit estimator/source equivalence), likelihood stack comparability nuances beyond those already flagged, and small but important documentation/notation fixes that affect a reader’s ability to reproduce and interpret the results without relying on the mutable repository.