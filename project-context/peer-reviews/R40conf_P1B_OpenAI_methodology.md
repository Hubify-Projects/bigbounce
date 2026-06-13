# P1B R40conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1b_mcmc_companion.pdf` md5=62374add pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5116 chars)
**Wall time**: 352.7s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall scope and framing
The manuscript presents three verification-style analyses: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy; (ii) a NaMaster pseudo-Cl MC pipeline-validation for birefringence angle recovery; (iii) a consistency check for a spectator ALP model against published cosmic-birefringence measurements. The authors repeatedly state careful scope limitations (proxy vs theory module, MC pipeline-validation vs sky significance, ALP consistency-not-prediction), which is appropriate.

However, I identified several methodological and arithmetic issues, including two load-bearing quantitative errors in the ALP energy-density section (a factor-of-3 error in the small-angle expression for Ωa, and a factor ≈2 error in ρcrit,0), an incorrect mass-prior conversion in Fig. 4, internal versioning/audit tags left in the text, and estimator-dependent language that currently overstates a “pipeline bias floor.” These must be corrected for PRD standards.

Findings (ESSENTIAL | MAJOR | MINOR | NIT)

ESSENTIAL

P1B-E1 — Sec. VI, “ALP dark-energy fraction Ωa,” p. 13, Eq. (9) small-θ approximation
• Problem: After Eq. (9) the text states: “For fa = MPl and small θi this gives Ωa ≈ m^2_a θ_i^2 /(2 H0^2 (1 + zosc)^3).”
• Issue: Missing factor of 1/3. Using ρa(zosc) ≈ ½ m_a^2 f_a^2 θ_i^2 and ρcrit,0 = 3 H0^2 MPl^2, one obtains
Ωa ≈ [½ m_a^2 f_a^2 θ_i^2]/[3 H0^2 MPl^2 (1 + zosc)^3] = (m_a^2 θ_i^2)/(6 H0^2 (1 + zosc)^3) for fa = MPl.
• Required fix: Correct the expression and all downstream statements that rely on it (including any tabulated Ωa thresholds, posterior fractions in Table IV if they were computed from this approximate form rather than from the stored per-step values). If the chains use the full numerical ODE and not this approximation, state explicitly that Eq. (9) is for intuition only and does not enter any numerical result; still correct the printed formula.

P1B-E2 — Sec. VI, “ALP dark-energy fraction Ωa,” p. 13, numerical value of ρcrit,0
• Problem: “ρcrit,0 = 3 H0^2 MPl^2 ≈ 8.1 × 10−11 eV^4.”
• Issue: For H0 = 67.68 km s−1 Mpc−1 ≈ 1.44 × 10−33 eV and MPl = 2.44 × 10^27 eV (reduced), ρcrit,0 ≈ 3 × (1.44 × 10−33)^2 × (2.44 × 10^27)^2 eV^4 ≈ 3.7 × 10−11 eV^4, not 8.1 × 10−11 eV^4. The stated value is off by about a factor of 2.
• Required fix: Correct the numerical value and ensure consistency with the chosen MPl convention (reduced vs unreduced). Update any dependent quantitative statements.

P1B-E3 — Fig. 4 caption, p. 14, mass prior to m/H0 conversion
• Problem: Caption states: “log10(ma/eV) ∈ [−35, −30] — the mass prior corresponds to m/H0 ≈ 7 × 10−3 to 7 × 10^2 for H0 = … = 1.44 × 10−33 eV.”
• Issue: m/H0 at 10^-35 eV is 10^-35 / 1.44×10^-33 ≈ 6.9×10^-2, not 7×10^-3. The low-end conversion is off by ×10.
• Required fix: Correct the conversion in the caption and anywhere else it appears. If any inference text relies on this mapping, revise accordingly.

P1B-E4 — Sec. VI, p. 13, “H0 note (E8)” and Sec. V.B, p. 10, “Release-pairing note (E3/E4)” and Data Availability, p. 15, versioning strings
• Problem: Internal audit/version labels and commit/round metadata appear in the body text: “H0 note (E8)”, “Release-pairing note (E3/E4)”, “in-tex v1B.0.69 stamp”, “commit: b22f8cc9”, repository paths, etc.
• Issue: Internal review/audit tags and version-control bookkeeping do not belong in the scientific narrative and contravene standard PRD style.
• Required fix: Remove all internal audit tags and version stamps from the main text. If you wish to preserve provenance, move these to a clearly separated data-availability footnote or Supplemental Material appendix and refer to a permanent DOI or tagged release.

P1B-E5 — Abstract p. 1; Sec. IV p. 7–9 and Fig. 3; Conclusions p. 14 — “observed NaMaster pipeline bias floor”
• Problem: The text repeatedly refers to “the observed NaMaster pipeline bias floor” of 0.040° measured under an unweighted χ^2 estimator on synthetic skies.
• Issue: The bias magnitude is estimator-dependent (you show that inverse-variance weighting removes ≈80% of it), and scenario-dependent (synthetic ΛCDM, white, isotropic noise, no beam mismatch, no foregrounds). Labeling it a general “bias floor” risks overgeneralization.
• Required fix: Replace “bias floor” with precise, estimator- and configuration-dependent wording, e.g., “observed multiplicative under-recovery under the unweighted χ^2 estimator on the stated synthetic setup.” Report the uncertainty on the measured mean bias (standard error of the 500-MC mean; at fsky = 0.32, σβ ≈ 0.046° implies SEM ≈ 0.002°). Add an explicit sentence that the bias is not a universal floor and should not be applied to sky measurements.

P1B-E6 — Sec. VI, p. 13, H0 dependence of Ωa
• Problem: “Marginalizing H0 over the Planck 1σ interval shifts Ωa by ≲ 1% (Ωa ∝ H0^−2).”
• Issue: With Ωa ∝ H0^−2, a 1.6% 1σ shift in H0 implies ≈3.2% change in Ωa before considering zosc effects. The quoted “≲ 1%” is inconsistent unless numerically demonstrated including the zosc dependence.
• Required fix: Provide a quantitative calculation (e.g., evaluate Ωa for H0 shifted by ±1σ at representative posterior points including zosc re-solve) and state the resulting percent change. If the variation remains ≈3%, correct the text accordingly.

MAJOR

P1B-M1 — Sec. V.B, p. 10; Sec. III scope notes — Mixed Planck release pairing without a control
• Problem: The ΛCDM+ΔNeff chains pair PR4/NPIPE high-ℓ CamSpec with 2018 low-ℓ TT/EE and 2018 lensing; no PR4-consistent low-ℓ/lensing control run is provided.
• Required fix: Either (a) add a PR4-consistent low-ℓ and lensing control chain to demonstrate stability of ΔNeff and H0 at the quoted precision; or (b) clearly downgrade any precision statements that could be sensitive to pairing, and move the pairing limitation forward (abstract and conclusions) as a load-bearing caveat.

P1B-M2 — Sec. IV, p. 7–9; Fig. 3 — Estimator grid and bias characterization
• Problem: The β estimator uses a grid over β but the grid spacing is only mentioned once indirectly (“10^-3-degree fit-grid resolution”) and the bias characterization relies on three injection points.
• Required fix: State the β grid spacing explicitly in Sec. IV and demonstrate that the recovered β is insensitive to grid resolution at the ≲10^−3° level. Expand the injection set or clarify that the “worst case across injections” refers to exactly the three injected angles and is not an exhaustive sweep; alternatively, include a modest denser grid (e.g., 6–8 points spanning 0–0.4°) to support the monotonic multiplicative-bias claim.

P1B-M3 — Sec. VI, p. 11–12 — Naive inverse-variance combination (3.9σ) vs correlated-joint (3.6σ)
• Problem: You retain the 3.9σ “upper bound” from an uncorrelated inverse-variance combination of Planck and ACT DR6.
• Required fix: Either remove this number from the main text (keep only the properly correlated 3.6σ headline), or provide a quantitative demonstration of the impact of plausible positive correlations (e.g., show the combined significance for a few ρ values) to justify the “upper bound” statement.

P1B-M4 — Data and Code Availability, p. 15 — Pending DOIs and moving-target provenance
• Problem: The manuscript relies on repository commit hashes and states “DOI assignment is pending.”
• Required fix: Prior to acceptance, provide permanent DOIs (e.g., Zenodo) for the frozen chains and artifacts cited in the paper, and cite those in the manuscript. If this cannot be completed now, relegate volatile commit-level details to Supplementary Material and commit to providing DOIs in the final version.

P1B-M5 — Sec. IV, p. 9 — Multiplicative under-recovery “~12%”
• Problem: The under-recovery is quoted as “∼12%,” but no uncertainty is given.
• Required fix: Provide a confidence interval (e.g., based on bootstrap over realizations or standard error propagation from recovered means) for the multiplicative bias.

MINOR

P1B-m1 — Table IV, p. 21 — Percentile notation
• Problem: Entries such as “6.0/40.5/238” and “0.22/0.41/0.70” are not labeled in the table header.
• Required fix: Indicate explicitly that these triplets are the 16th/50th/84th percentiles (or provide the exact percentile levels).

P1B-m2 — Sec. IV, p. 7–8 — Units and normalization of χ^2
• Problem: The χ^2 in Eq. (1) is an unweighted sum of squared bandpower differences and thus has units of (µK^2)^2.
• Required fix: Add a sentence clarifying that χ^2 is used only as a minimization objective and is not interpreted as a normalized goodness-of-fit statistic.

P1B-m3 — Sec. IV, p. 8 — Pixel window and beam statements
• Problem: You assert cancellation of the Nside=512 pixel window and note no beam deconvolution. While reasonable here, it would help to add a short quantitative check.
• Required fix: Add a brief robustness test or citation showing that including an identical common beam/pixel-window deconvolution in both map and template leaves β unchanged at the ≤10^−3° level.

P1B-m4 — Sec. V.C, Table II, p. 20 — “quintom-B” label
• Problem: The chain’s marginalized tail-distances are repeatedly highlighted; the model-comparison caveat is present but the “quintom-B” phrasing might be over-interpretation given the overlap-uncorrected SN product likelihood.
• Required fix: Tone down wording to “phenomenological CPL trajectory consistent with a phantom-crossing behavior,” and keep the SN-overlap caveat next to every such statement.

P1B-m5 — Sec. IV, Fig. 3b, p. 7 — Error bars
• Problem: The canonical fsky=0.32 point initially lacked σβ; you state a rerun measured σβ=0.046°.
• Required fix: Include the 500-MC standard error on the mean (≈0.002°) explicitly in the caption or main text for all points.

P1B-m6 — Sec. VI, p. 12 — Coupling prior truncation
• Problem: The [1, 30] Caγ prior initially truncated ≈28% of the posterior mass; you later expand to [4, 60]. The text is clear, but a compact summary figure/table would help.
• Required fix: Add a one-line table or inset showing the fraction of posterior mass near the edges for each prior to document prior robustness.

P1B-m7 — Various — Repository path noise in main text
• Problem: Inline long file paths (e.g., reproducibility/…/c10_robustness_battery.json) distract from the scientific narrative.
• Required fix: Move long paths to a short “Artifact index” in Supplemental Material or Data Availability and refer to artifact IDs in the main text.

NIT

P1B-n1 — Sec. III footnote 1, p. 3–4 — Typographical polish
• Problem: Overlong burn-in reconciliation footnote with small numerical inconsistencies (123,368 vs 123,129) explained but heavy to read.
• Fix: Condense.

P1B-n2 — Sec. IV, p. 6 — Minor repetition
• Problem: Phrasing “This is a methods validation, not a competitive sky detection” appears multiple times.
• Fix: Keep once in Sec. IV opening and once in Conclusions; remove elsewhere.

P1B-n3 — Sec. VI, p. 11 — Humorous aside
• Problem: “numerically coincident with, and unrelated to, the §IV injection angle β = 0.27°.”
• Fix: Remove aside; keep pivot definition crisp.

P1B-n4 — Units and typography
• Problem: Inconsistent spaces in “km s−1 Mpc−1” and sporadic “H0.riess2020Mb” formatting.
• Fix: Standardize.

Checks of arithmetic and dimensional consistency (spot-audits)

- Hubble-tension significance in abstract: (73.04 − 67.68)/sqrt(1.06^2+1.04^2) ≈ 3.61σ — consistent with “∼3.6σ.”
- ΔNeff posteriors, H0 posteriors, and Fig. 2 values are mutually consistent within rounding.
- NaMaster multiplicative under-recovery: 0.238/0.27 ≈ 0.88; 0.302/0.342 ≈ 0.88; “∼12%” shortfall is correct; add CI (MAJOR above).
- Planck+ACT naive combination: 0.241 ± 0.061 → 3.93σ; reported as an optimistic upper bound (request stronger handling; MAJOR).
- CPL pivot calculation: Using provided σ and Cov, ap and wpivot reproduce to the quoted digits.
- H(z=0.5) fractional change ≈ +1.7% recomputes correctly for the chain’s w0, wa, and Ωm.
- Birefringence amplitude from αEM/(4π) Caγ Δφ/fa converts to 0.28° as stated.

Bibliography spot-checks
- Eskilt & Komatsu (PRD 106, 063503 (2022), arXiv:2205.13962) and Planck NPIPE PR4 birefringence results are correctly cited and the quoted statistics match their abstracts.
- DESI DR2 BAO (2025) citation style is acceptable; ensure final bibliographic details are up-to-date at acceptance.

Length and focus
At 21 pages this is long for a primarily verification companion. With the above fixes, much of the repository/process material can be moved to Supplemental/Data Availability. A leaner main text of ≈14–16 pages focusing on methods, results, and key limitations would strengthen readability.

## Summary recommendation
MAJOR REVISIONS

The paper’s framing and many methodological caveats are careful, but there are critical arithmetic errors in the ALP energy-density section (factor-of-3 error in the small-angle Ωa expression; incorrect ρcrit,0), an incorrect mass-prior conversion in Fig. 4, and overgeneralized phrasing of an estimator-dependent NaMaster bias as a “floor.” Internal audit/version tags also need to be removed from the main text. After correcting these issues, adding uncertainty quantification for the measured MC bias, clarifying the β grid and injection coverage, and providing stable archival DOIs, the manuscript could meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS ONLY (relative to my initial report)

ESSENTIAL

P1B-E7 — Table I text, “overlap integral” values for S8 tension
• Problem: The manuscript quotes posterior-overlap integrals R min(p1, p2) dS8 = 0.05 (Planck+BAO+SN vs DES-Y3) and 0.12 (full-tension posterior vs DES-Y3). For a separation of Δ = 0.051 with σ1 = 0.010 and σ2 = 0.017, a standard equal-variance proxy gives an overlap coefficient ≈ 0.19; unequal-variance analytic expressions or a quick numerical check typically yield ~0.1–0.2, not 0.05.
• Required fix: Provide the exact numerical procedure (grid, normalization, and densities used) and recompute the overlaps. If 0.05 and 0.12 remain, show the intersection point(s) and the integral on a plot; otherwise update the numbers and any accompanying σ-language.

MAJOR

P1B-M6 — Sec. V.B “Independent re-run cross-check” — likelihood-stack inconsistency
• Problem: The re-run is described as “same likelihood stack,” but it switches to planck 2020 lollipop.lowlE and planckpr4lensing, whereas the frozen chains use planck 2018 lowl.EE and planck 2018 lensing.clik.
• Required fix: Correct the description to acknowledge the differences, and either: (a) rerun with exactly the same low-ℓ EE and lensing as the frozen chains, or (b) quantify the shift induced by these swaps (e.g., run A/B tests) and state that the agreement within 0.04σ is after these differences.

P1B-M7 — Sec. VI “ALP dark-energy fraction Ωa” — validity of the onset/redshifting approximation
• Problem: Ωa is computed using ρa(zosc) ≈ V(ϕi) and post-onset redshifting as matter, Eq. (9). For m ≲ few H0 and zosc ≲ O(1), the field may not undergo many oscillations before today; the cycle-averaged, matter-like redshifting approximation can be biased.
• Required fix: Quantify the discrepancy between Eq. (9) and full EOM integration across representative posterior samples (especially m/H0 ~ 1–5). Report the median and 16–84% fractional error and revise the Ωa-based subset fractions if needed, or state explicitly that Table IV uses full-EOM Ωa and Eq. (9) is intuition-only.

P1B-M8 — Sec. IV bias characterization — weighting details
• Problem: The “inverse-variance-weighted” estimator that reduces bias by ≈80% is invoked, but the source of the variances is not specified (analytic vs MC-estimated; whether they include cosmic variance; independence from the fitted realization).
• Required fix: Specify σb used for the weights (formula and how obtained), and show that using weights estimated from independent MC (vs the same realizations) yields consistent β and bias reduction.

MINOR

P1B-m8 — Table IV header labeling
• Problem: The column header reads “m/H0 (Caγ = 8)” for the c5 continuous-prior chain where Caγ is sampled freely.
• Required fix: Relabel to “m/H0” (no fixed coupling) or split the table by configuration if the numbers mix fixed- and free-Caγ runs.

P1B-m9 — S8 tension language consistency
• Problem: The text alternates between “2.5σ” and “2.6σ” for the Planck+BAO+SN vs DES-Y3 S8 tension.
• Required fix: Pick one rounded figure and use it consistently; ideally, quote the exact Δ/σ value once and refer to it thereafter.

P1B-m10 — Sec. IV β-search specification
• Problem: The β grid spacing is mentioned indirectly, but the scan range (min/max β) is never given.
• Required fix: State the β-grid endpoints and confirm that the recovered β is stable to grid extension at the ≤10−3° level (in addition to spacing stability).

P1B-m11 — Footnote 4 and Sec. IV wording on “noise”
• Problem: SNRtmpl uses σb from the MC scatter of EB bandpowers. This includes cosmic variance from rotated E as well as map noise, not “single-realization noise” only.
• Required fix: Clarify that σb includes sky variance from the simulated CMB plus instrumental noise; adjust the “single-realization noise” phrasing.

P1B-m12 — Sec. IV, ℓ > 1024 bins and “effectively restricted” claim
• Problem: Bins with ℓ > 1024 have CEE,tmpl = 0, so their χ2 contribution is constant in β. The text says the fit is “effectively restricted” to ℓ ≤ 1024, but does not explain why.
• Required fix: Add one sentence explaining that terms with zero template are β-independent constants and therefore do not affect the minimization, justifying the “effectively restricted” statement.

NIT

P1B-n5 — Fig. 3 mask definitions vs prose
• Problem: The fsky ≈ 0.85 “Planck-like” mask claim may be optimistic relative to typical Planck common polarization masks (often ≲0.8 after point-source cuts).
• Fix: Rephrase as “Planck-like Galactic cut (|b| > 5°; no point-source excisions), yielding fsky ≈ 0.85 in this toy setup.”

Explanation
I focused this second pass on consistency and arithmetic issues I did not re-check previously. The new items above address a likelihood-stack mismatch in the “same stack” re-run, numerical plausibility of quoted S8 overlap integrals, the validity regime of the Ωa approximation near oscillation onset, incomplete weighting details for the reduced-bias estimator, and several presentation/labeling clarifications. These are distinct from the errors and issues already raised in my initial report.