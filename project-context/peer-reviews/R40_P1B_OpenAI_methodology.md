# P1B R40 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7031 chars)
**Wall time**: 603.8s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of this review
- Role: PRD methodology referee. Focus: estimator correctness, statistical interpretation, dimensional/arithmetic consistency, traceability of every quantitative claim, and reproducibility surfaces.
- I read the full 21-page manuscript with all figures, tables, equations, footnotes, and appendices. Below is a comprehensive issues list. Each item includes an ID, location, problem, and required fix, classified as ESSENTIAL, MAJOR, MINOR, or NIT.

Overall assessment
- The paper is careful in many places (clear scope statements, numerous caveats distinguishing in-sky detection significances from MC recovery-SNRs, explicit priors/likelihoods for MCMC, dimensional consistency for ALP formulas).
- However, there are several PRD-standard blocking issues: overuse of internal-execution-path references in the main text, incomplete data archiving (DOIs “pending”), reliance on a deliberately suboptimal unweighted pseudo-Cℓ estimator as the “canonical” baseline in a methods paper, and a w0wa posterior section that quotes marginal-tail σ-distances despite a known SN-overlap systematic and an unsampled ΛCDM point. These must be rectified.

Findings

ESSENTIAL

P1B-E1 (Sec. IV, pp. 7–9; Figs. 3 and surrounding text)
Problem: The pseudo-Cℓ estimator used for β is explicitly unweighted over multipole bins, yet the “pipeline-recovery SNR” reported (e.g., 20.32 and 25.71) is defined with inverse-variance per-bin weighting (Σb (CEB,th/σMC,b)^2)1/2. While you do state this SNR is not the significance of β̂ itself, the paper still places the (weighted) SNR next to an analysis built on an unweighted χ2 estimator. That mixes two different null procedures for the same observable (β) and invites misinterpretation.
Required fix: Report estimator-consistent performance metrics. Specifically:
- Provide the sampling distribution of β̂ from the same unweighted estimator across the 500 MC realizations and quote its standard deviation σβ (you have this for the fsky sweep and for the fsky=0.32 rerun, σβ=0.046°). Then report the estimator’s detection-level SNR as |βinj|/σβ and the corresponding z-score (e.g., 0.27°/0.046° ≈ 5.9; if you intend to use |β̂|/σβ ≈ 5.2, say so explicitly).
- If you keep the weighted-template SNR, clearly separate it from the unweighted-estimator performance and move it to a methods appendix, or adopt a consistent weighted estimator as the primary baseline. The current mixed reporting is not acceptable for a methods paper.

P1B-E2 (Sec. IV, p. 9; robustness battery paragraph)
Problem: You attribute the ≈12% multiplicative under-recovery largely to the unweighted fit and partially to the EE-only template (omitting −CBB). In a methods paper, retaining a knowingly biased unweighted + EE-only estimator as the “canonical” one (because it matches earlier public scripts) is not sufficient.
Required fix: Promote the inverse-variance-weighted estimator and the (CEE−CBB) template to the primary baseline and re-run the 500-MC validations to quote the corrected bias and scatter as your main result. Relegate the legacy unweighted/EE-only variant to a cross-check subsection. If you choose not to promote the improved estimator, you must provide a quantitative, reproducible correction formula (and uncertainty) for the observed ≈12% multiplicative bias and show that conclusions using the debiased estimator are unchanged.

P1B-E3 (Sec. V.C and Sec. III Physics-interpretation block; multiple instances on pp. 4–5 and 10; Table II caption)
Problem: You quote “+4.3σ” and “−3.6σ” departures for w0 and wa from ΛCDM in a chain that (i) treats DES-SN5YR and Pantheon+ as independent despite ~20% overlap with different Malmquist corrections, and (ii) has ΛCDM (w0,wa)=(-1,0) unsampled (you correctly say these are marginal-tail distances, not evidences). These σ-numbers are easy to misread as detection significances.
Required fix: Either remove all σ-distances for w0, wa in the main text (move them to an appendix labeled “posterior-tail distances; not evidences”), or add an explicit, boldfaced caveat immediately next to every such σ-number that (a) the SN overlap is unmodeled and (b) ΛCDM is unsampled, so these are not detection significances or Bayes factors. In addition, provide the two “SN-overlap control chains” you mention (Pantheon+ only; DES-SN5YR only) with their (w0,wa) shifts, or remove the w0wa claims entirely from the main text until that robustness is documented.

P1B-E4 (Appendix A, Data and Code Availability, p. 15; HuggingFace datasets in App. A; multiple “pending DOI” statements)
Problem: Reproducibility relies on external artifacts whose DOIs are “pending.” PRD requires stable, citable datasets/software for acceptance.
Required fix: Archive all frozen chains and MC artifacts in a repository with permanent DOIs (Zenodo, Dataverse, or equivalent) and replace “pending” with active DOIs. Freeze the exact commit (b22f8cc9) as a tagged release with an archived snapshot (DOI), and ensure the paper cites that release. Do not rely solely on mutable GitHub/HuggingFace links.

MAJOR

P1B-M1 (Sec. IV, p. 8; bins above ℓmax)
Problem: The text says “bins above the map band limit ℓmax=2Nside=1024 carry zero template weight (CEE,tmpl=0), so the 20-bin sum is effectively restricted...; restricting to ℓ≤1024 changes nothing.” Minimization is indeed unaffected, but χ2 includes a β-independent constant term from (CEB,meas)^2 in those bins. The current phrasing “carry zero template weight” is potentially misleading.
Required fix: Clarify explicitly that bins above 1024 contribute a β-independent constant to χ2 but do not affect the β̂ minimizer. As a cross-check, provide the β̂ values from a fit that excludes those bins entirely to demonstrate numerically that the best-fit β̂ is unchanged to within 10−3 degrees.

P1B-M2 (Throughout; e.g., Sec. III footnote 1 p. 3–4, Sec. IV pp. 7–9, Appendix A p. 15)
Problem: The main text is saturated with internal execution paths, filenames, and pod labels (e.g., reproducibility/p1_namaster_500mc/...; “pod1 namaster umap 2026-04-29”; “spin torsion.input.yaml”; “c15 converged”). This is not acceptable in the PRD main text.
Required fix: Move all internal paths, run-IDs, and pipeline file names into a concise, standalone Data Availability/Code appendix or a Supplemental Material document. In the main text, refer only to stable DOIs and a single top-level repository URL with a release tag.

P1B-M3 (Sec. III, pp. 4–5; MB–H0 joint-posterior offset check)
Problem: You quote a 0.156 mag offset and call it “~3.2σ relative to the chain’s σMB=0.049,” but also acknowledge this is not a properly conditioned tension statistic. As written it can still be misread as a frequentist tension.
Required fix: Either remove the “3.2σ” phrasing or replace it with an explicitly conditioned and appropriately defined tension statistic (e.g., along the MB−5log10 h degeneracy with the Pantheon+ covariance), or move the numerical “3.2σ” to an appendix and keep only a qualitative statement in the main text.

P1B-M4 (Sec. VI, pp. 10–14; ALP coupling benchmarks)
Problem: You state that the required Caγ “exceeds the standard KSVZ/DFSZ benchmark range, which predicts |Caγ| ~ O(1).” That benchmark is model-dependent (range and sign can vary). As written, “exceeds” reads too categorical.
Required fix: Qualify this statement with a citation-backed quantitative benchmark range for Caγ in KSVZ/DFSZ (e.g., typical |Caγ| ≲ 1–2 depending on charge assignments; cite a review). State explicitly that your posterior-favored Caγ ≳ 8–10 lies beyond these typical minimal values.

P1B-M5 (Sec. V, pp. 9–10; Release pairing)
Problem: Mixing PR4 (CamSpec high-ℓ) with 2018 low-ℓ/lensing is a known caveat; you provide a c15 rerun using PR4-consistent low-ℓ/lensing and quote a 0.04σ agreement in ΔNeff. However, only Planck+BAO+SN was rerun; the full-tension stack used for headlines was not.
Required fix: Provide the same PR4-consistent low-ℓ/lensing rerun for the full-tension combination and tabulate the shift in ΔNeff and H0; if comparable (<0.1σ), state it. Otherwise, change the headline to the PR4-consistent reruns or explicitly label which rows are PR4-consistent and which are mixed-release.

P1B-M6 (Appendix C, pp. 16–18; β-periodicity)
Problem: You correctly note β periodicity (β ≡ β + n×90° for E/B), and argue it is harmless since posterior support lies within |β| ≲ 0.7°. Please add an explicit verification figure or table showing the posterior mass within ±5σ of the principal branch center to rule out any leakage into the next image given your Gaussian summary likelihood.
Required fix: Add a short quantitative check (e.g., a 1D posterior plot with axis extended to ±10°) and state the total posterior weight outside |β|<5° is negligible.

MINOR

P1B-m1 (Sec. III, p. 5; “canonical 3.6σ Hubble tension”)
Problem: For H0=67.68±1.06 vs 73.04±1.04, the Gaussian tension is 3.61σ; for H0=67.78±1.09 it is 3.49σ. You use “∼3.6σ” generically.
Required fix: Quote the tensions for each stack separately (3.61σ and 3.49σ) or say “~3.5–3.6σ,” and indicate the exact formula used (Gaussian two-sample z).

P1B-m2 (Sec. IV, p. 8; σβ and SNR language)
Problem: You state “per-realization angle-recovery ratio β/σ̂β = 5.2,” but given σβ=0.046°, |βinj|/σβ ≈ 5.9 while |β̂|/σβ ≈ 5.2. The symbol β is ambiguous.
Required fix: Specify whether this is |βinj|/σβ or |β̂|/σβ and be consistent throughout. I recommend reporting both, since the estimator is biased.

P1B-m3 (Sec. IV, p. 7; units in σpix conversion)
Problem: The σpix derivation is correct but mixes two equivalent formulas back-to-back. It may confuse readers.
Required fix: Keep one canonical relation: σpix [µK] = ΔP [µK·arcmin]/sqrt(Ωpix [arcmin^2]) with Ωpix = 4π/Npix × (180/π×60)^2, and give the Nside=512 numerical Ωpix and σpix once.

P1B-m4 (Sec. VI, Eq. (9), p. 13; piecewise definition)
Problem: You later handle the zosc ≤ 0 case by holding ρa=V(θi). For clarity, Eq. (9) should be presented as a piecewise definition to avoid confusion.
Required fix: Recast Eq. (9) as a two-branch expression (zosc>0 and zosc≤0) or add an explicit sentence below the equation.

P1B-m5 (Sec. IV, p. 7; “no pixel-window mismatch enters the β estimate”)
Problem: The cancellation argument is correct for identical Wℓ factors, but it relies on the assumption that both the measured spectra and template carry the same pixel window in the same way post-decoupling.
Required fix: Add a one-sentence qualifier: “Because both the decoupled spectra and the template are evaluated at the same Nside=512 without pixel-window deconvolution, the identical Wℓ factors cancel in the β minimizer.”

P1B-m6 (Fig. 3 caption, p. 7)
Problem: You plot the fsky=0.32 point without σβ, then cite a later rerun that measured σβ=0.046°.
Required fix: Either update Fig. 3(b) to include the fsky=0.32 σβ from the rerun or add a parenthetical note in the caption stating that the canonical point’s σβ=0.046° comes from a dedicated rerun.

P1B-m7 (Sec. III footnote 1, pp. 3–4; burn-in)
Problem: Two different burn-in fractions (20% vs. 30%) are intermingled in the narrative, making the counts hard to follow.
Required fix: Standardize on a single burn-in fraction for reporting headline sample counts in the main text. Move the reconciliation details to the reproducibility appendix.

P1B-m8 (Sec. VI, p. 11; H0 value in eV)
Problem: You state H0=67.7 km s−1 Mpc−1 = 1.44×10−33 eV. Correct but derived with ħ; adding “(using ħ)” would prevent confusion.
Required fix: Add “(using ħ to convert s−1 to eV)” in the parenthetical.

P1B-m9 (Abstract vs. body; cosmic birefringence significance)
Problem: Abstract states “primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ” but later the ALP MCMC uses the Eskilt–Komatsu 3.6σ WMAP+Planck constraint as primary. While both statements are correct, the juxtaposition in the abstract can confuse.
Required fix: In the abstract, add one clause explicitly distinguishing these: “We adopt the 3.6σ WMAP+Planck joint constraint (Eskilt & Komatsu) for the ALP likelihood; Planck-only and ACT DR6 stand at 2.7–2.9σ.”

NIT

P1B-n1 (Typos/formatting: scattered)
- Occasional hyphenation artifacts (e.g., “lensing.clik;” broken lines around punctuation). These appear to be PDF export/justification issues.
Required fix: Clean up linebreak hyphenations before submission.

P1B-n2 (Conclusions, p. 14; repeated phrase)
Problem: “median m ≃ 40.5 H0, Ωa < 0.01 (safe), Ωa < 0.01” — duplicated cut.
Required fix: Remove the duplicate “Ωa < 0.01.”

P1B-n3 (References)
Problem: Ref. [4] cited as “arXiv:2509.13654 (2025)” — please verify exact arXiv number and year formatting at submission time.
Required fix: Update to the correct arXiv ID and, if available, journal info.

Arithmetic and dimensional checks (spot-audit summary)
- H0–SH0ES tension: 67.68±1.06 vs 73.04±1.04 gives z ≈ 3.61σ; 67.78±1.09 vs 73.04±1.04 gives ≈3.49σ. Your “~3.6σ” umbrella is acceptable once clarified (see P1B-m1).
- S8 tension (Planck+BAO+SN 0.827±0.010 vs DES-Y3 0.776±0.017): Δ=0.051; σcomb≈0.0197 ⇒ 2.59σ. Earlier you write ~2.6σ with Δ=0.049; ensure the same S8 pair is used when quoting a single number (P1B-m1).
- β prefactor: α/(4π) ≈ 0.000581, Caγ=8, Δφ/fa=1.06 ⇒ β ≈ 0.00493 rad ≈ 0.282°. Correct.
- CaγΔφ/fa for β=0.342°: 0.342°=0.005966 rad; / (α/4π)= ~10.27 (~10.3 in text). Correct.
- Pivot wpivot calculation reproduces −0.952±0.019 with ap=0.790 (zp=0.27). Correct.
- σpix from ΔP=10 µK·arcmin and Nside=512: Ωpix≈47.3 arcmin2 ⇒ σpix≈10/√Ωpix≈1.45 µK. Correct.
- ALP Ωa scaling Ωa ≈ m2θi2/(6H0^2 (1+zosc)^3) for fa=MPl, small θi: correct.

Length and focus
- For the three claimed contributions, 21 pages is on the long side, largely due to extensive run-paths and audit-log prose embedded in the main text. I recommend trimming the main text to ~15 pages by moving operational details (filenames, run IDs, seed bases, pathnames, chain-count reconciliations) to a concise supplementary or to a cleaned Data Availability appendix (P1B-M2).

## Summary recommendation
MAJOR REVISIONS

The paper is careful about scope and contains valuable, well-qualified checks, but it does not meet PRD methodological standards in its current form. The most important fixes are: adopt an estimator-consistent performance metric (or promote the weighted/(CEE−CBB) estimator as baseline), de-emphasize or relocate marginal-tail σ claims for w0wa given the known SN-overlap and unsampled ΛCDM point, clean the main text of internal execution-path details, and provide stable DOIs for all frozen artifacts. Addressing these will make the work suitable for PRD consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P1B-E5 (Sec. IV, Eq. (1) and surrounding text, pp. 7–9)
Problem: The “χ2” minimized is an unweighted sum of squared residuals without any variance normalization. As written, it is not a statistical χ2 (has units of power squared, not dimensionless), yet it is repeatedly called χ2 and used as such. This is a dimensional and nomenclature mismatch that can mislead readers about optimality and uncertainty propagation.
Required fix: Rename the minimized objective to “unweighted sum of squares” S(β) and state explicitly it is not a statistical χ2. If you keep χ2 notation anywhere, include the variance (or full covariance) in the definition. Also add a one-line dimensional check.

P1B-E6 (Sec. IV, end of “Robustness battery and bias attribution,” p. 9)
Problem: You compare the internal MC pipeline bias (|Δβ̂| ≤ 0.040°) to the observational uncertainty σobs
β = 0.094° and conclude it is “well below” σobs
β. This juxtaposes two different null procedures (internal MC bias vs. external sky-measurement error), contradicting your own caution elsewhere that these are not directly comparable.
Required fix: Remove that comparison or rephrase to avoid any implication of direct comparability. If you want to contextualize the bias, compare it only to the estimator’s own MC scatter σβ for the same configuration.

MAJOR

P1B-M7 (Sec. VI, Ωa definition and use, pp. 12–13; Table IV)
Problem: For θi ≳ O(1) the cosine potential is anharmonic; onset and dilution deviate from the quadratic approximation. You mention verification “against full EOM integration,” but give no quantitative error budget. Since the “spectator-safe” classification (Ωa < 0.01) is central to claims, unquantified anharmonic corrections can misclassify samples.
Required fix: Provide a quantitative validation (table or plot) of Eq. (9) versus full EOM across the posterior (e.g., fractional error in Ωa at representative θi and ma). If errors exceed a few percent in any posterior-support region, use a piecewise or corrected expression (include the standard anharmonic correction factor) and recompute the subset fractions in Table IV.

P1B-M8 (Sec. III, MB–H0 discussion pp. 4–5; Data provenance)
Problem: Mixed SH0ES vintages: you use the H0.riess2020Mb likelihood (2020 anchor) while quoting H0 = 73.04 ± 1.04 km s−1 Mpc−1 from Riess et al. 2022. Using a 2020 MB prior with a 2022 H0 comparison is a data-vintage mismatch that can bias the MB–H0 tension narrative.
Required fix: Either update to the 2022 MB anchor (and cite it) or justify and quantify the impact of using the 2020 MB prior (show that key posteriors and the MB–H0 consistency check are unchanged within <0.1σ). Clearly label the vintage in the main text.

P1B-M9 (Sec. IV, robustness battery, p. 9; “purify_b=True” test)
Problem: You report identical β̂ (to 10−3 deg) with and without B-mode purification. That is plausible only if E→B leakage is negligible or swamped by other effects, but no leakage diagnostic is shown.
Required fix: Add a leakage diagnostic: e.g., run a pure-E input sky and report the recovered spurious EB (or β̂) with and without purification, and/or plot the EE→BB coupling matrix elements. Quantify the leakage contribution to the bias budget.

P1B-M10 (Sec. IV, estimator optimality, pp. 7–9)
Problem: Beyond variance weighting, the current estimator tacitly assumes diagonal, equal-variance bandpowers. Pseudo-Cℓ bandpowers are correlated; ignoring covariance can bias β̂ and its uncertainty.
Required fix: Either justify the diagonal-equal-variance assumption by showing the MC-estimated bandpower covariance is near-diagonal and uniform over the used bins, or adopt an (approximate) inverse-covariance-weighted estimator and re-quote bias and σβ.

P1B-M11 (Sec. IV, “Mode-coupling matrix and binning,” p. 7)
Problem: Only one binning and ℓ-range are exercised; you explicitly state no ℓ-range robustness sweep is done. For a methods paper, estimator stability against binning/ℓmin is required.
Required fix: Add a short robustness sweep varying the bin edges and ℓmin (e.g., ℓmin = 20/40; 10/30/40 equal-width bins) and show β̂ shifts are negligible compared to σβ.

MINOR

P1B-m10 (Appendix C, run3 “βfree,” p. 17)
Problem: With a Gaussian summary likelihood σβ = 0.094°, the model-independent βfree posterior returns 0.344° ± 0.10°. The 6% broadening over the input σ is unexpected for a single-parameter Gaussian fit and may reflect limited ESS (≈265) or implementation details.
Required fix: Verify that βfree reproduces the input σ within Monte Carlo error. If the width remains inflated, briefly explain (e.g., prior truncation effects, sampler settings) and/or increase ESS.

P1B-m11 (Sec. IV, SNRtmpl definition, fn. 4, p. 8)
Problem: The SNRtmpl formula is written inline with ambiguous bracketing.
Required fix: Write it unambiguously (e.g., SNRtmpl = [Σb (CEB,th
b /σMC
b )2]1/2) and define σMC
b explicitly as the per-bin standard deviation across MC realizations.

P1B-m12 (Sec. IV, “ACT-like noise,” p. 7)
Problem: You adopt ΔP = 10 µK·arcmin as “ACT-like” without a citation.
Required fix: Cite an ACT DR6 performance reference for typical polarization white-noise levels or add a brief rationale explaining the choice as conservative.

P1B-m13 (Sec. VI, β periodicity, p. 16 and App. C)
Problem: You correctly note β ≡ β + n×90°. For completeness, mention that sin(4β) also implies mirrored extrema within each 90° interval; you rely on a narrow posterior, but a one-liner clarifies why no secondary modes appear.
Required fix: Add a sentence noting the sin(4β) symmetry and that the posterior support remains confined to |β| ≪ 45°, precluding alias peaks.

P1B-m14 (Table IV, “θi ≤ 0.1 (strict)” line, p. 21)
Problem: Caγ percentiles are quoted from a sliver with only 42 raw samples (0.47%); estimates from so few draws are unstable.
Required fix: Add bootstrap errors on these percentiles or move the strict-slice quantiles to an appendix labeled “indicative only,” without numerical percentiles in the main table.

NIT

P1B-n4 (Terminology consistency, Sec. IV)
Problem: Mixed use of “template-fit SNR,” “pipeline-recovery SNR,” and “per-realization |β̂|/σβ” can confuse.
Required fix: Add a one-line glossary at first use distinguishing these three quantities and use consistent symbols throughout.

P1B-n5 (Figure/axis units cross-check)
Problem: Fig. 3(b) caption now mentions σβ = 0.046° for fsky = 0.32 only in text; the plotted point still lacks its error bar.
Required fix: Update the plot to include the σβ error bar at fsky = 0.32 or add an explicit parenthetical in the caption pointing to the rerun value.

Rationale for “fresh-eyes” classification
- These items were not covered in the initial review and arose from re-checking arithmetic consistency, estimator dimensionality, internal comparability of null procedures, and completeness of the ALP energy-density treatment. Most are straightforward to address and will materially improve methodological rigor and clarity.