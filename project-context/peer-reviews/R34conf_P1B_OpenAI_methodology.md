# P1B R34conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.59.pdf` md5=7fbac464 pages=19
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10731 chars)
**Wall time**: 362.1s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

General assessment
The manuscript documents three technical checks: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy using Cobaya, (ii) a NaMaster pseudo-Cl pipeline validation on synthetic CMB polarization skies, and (iii) a spectator-ALP consistency check for cosmic birefringence. The scope limitations are explicitly laid out, and many statistical caveats are properly flagged. The paper is commendably transparent about analysis choices and caveats, and most headline numerical values are arithmetically consistent with the body.

However, several essential methodological and presentation issues must be resolved before this can meet Physical Review D standards for methodology rigor and reproducibility. The most serious concerns are (a) unresolved data-pairing consistency for the Planck PR4/2018 mixed likelihood stack used to derive the ΔNeff and H0 results; (b) the use of partially overlapping SN samples (Pantheon+ and DES-SN5YR) without a joint covariance in the w0–wa fit while quoting multi-σ “departures” from ΛCDM; and (c) the heavy inclusion of version-history language, “earlier draft” corrections, and raw repository file paths in the body text, combined with the absence of a frozen DOI-tagged release and a clean, bug-free set of artifacts. Several additional major and minor issues are detailed below.

Findings

ESSENTIAL

P1B-E1
- Location: Multiple (title block p. 1; Abstract footnote a p. 1; Sec. IV pp. 6–8; Sec. VI pp. 9–11; Data and Code Availability pp. 12–14; Appendix A pp. 13–14)
- Problem: Pervasive version-history and internal process language appears throughout the paper, including “Dated: June 11, 2026 PDT — v1B.0.59,” “an earlier draft quoted… and is corrected here,” “the repository README is the authoritative source,” and numerous raw repository file paths (e.g., reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py; research/branch_R_alp_birefringence/...).
- Required fix: Remove all earlier-draft and process-log language from the main text. Move raw file paths and implementation details to a Supplement or a short “Code Availability” paragraph. Replace GitHub-relative path pointers with a single immutable, DOI-minted archival release (Zenodo or equivalent) and include exact commit SHA(s) in the manuscript. Retain only minimally necessary provenance in the main text.

P1B-E2
- Location: Sec. III, p. 3 (Scope statement and dataset description) and Table III, p. 18
- Problem: The ΛCDM+ΔNeff results are based on a mixed Planck PR4 (NPIPE CamSpec high-ℓ) + Planck 2018 (low-ℓ TT/EE + lensing.clik) pairing. The paper explicitly states no PR4-consistent low-ℓ/lensing pairing swap test has been performed, leaving any pairing-induced bias “unquantified.”
- Required fix: Run a pairing-consistency test and report any shifts in ΔNeff and H0 when using a fully PR4-consistent low-ℓ and lensing stack, or provide a published, peer-reviewed reference demonstrating that this standard Cobaya pairing is demonstrably unbiased at the quoted precision. If not feasible, the ΔNeff and H0 claims must be softened to reflect this unresolved systematic, and the mixed-pairing caveat must be elevated to the abstract.

P1B-E3
- Location: Sec. IV (NaMaster) and Fig. 3, pp. 6–7; Abstract p. 1; repeated in body
- Problem: Template-fit SNR values (e.g., 20.32, 25.71) and sky-measurement significances (2.7–2.9σ) are of different statistical nature. Although the text contains appropriate caveats, Fig. 3’s caption itself lacks an explicit “not directly comparable” statement where the 20–26 SNR numbers appear near claims of “published 2.7–2.9σ” elsewhere in the section/abstract.
- Required fix: Add an explicit, unmissable statement in the Fig. 3 caption and where both values appear in proximity that these significances are not directly comparable (MC template-fit pipeline SNR vs. sky-measurement detection σ), to avoid reader misinterpretation at the figure level.

P1B-E4
- Location: Sec. V (Datasets and Configuration) and Sec. III caveat (e), pp. 4, 8; Table II, p. 18
- Problem: The w0–wa results use DES-SN5YR and Pantheon+ simultaneously without a joint covariance accounting for the ≈20% overlap, yet report multi-σ “departures” (w0: +4.3σ; wa: −3.6σ). The paper acknowledges this as a caveat, but the results are still presented as headline posterior distances from ΛCDM.
- Required fix: Either (i) provide a joint-covariance analysis or a rigorous overlap-handling method for DES-SN5YR + Pantheon+, or (ii) remove the combined-SN w0–wa posterior significance claims from the main text (retain as exploratory appendix with strong warning), or (iii) re-run with only one SN sample and present the results. Without a proper overlap treatment, the reported ΛCDM departures must not appear as principal results.

P1B-E5
- Location: Appendix A (Data and Code Availability), pp. 13–14
- Problem: The analysis acknowledges a “column-permutation bug” in a frozen diagnostic export, directing readers to a corrected JSON. This is not acceptable for PRD-level reproducibility.
- Required fix: Re-export and archive a fully corrected set of chains and diagnostics. Provide a single, clean, versioned, DOI-minted archive containing only verified, corrected artifacts. Remove instructions to work around corrupt files. Include checksums.

MAJOR

P1B-M1
- Location: Sec. IV, p. 6 (pipeline configuration), p. 8 (robustness battery)
- Problem: The mask apodization, sky fraction, and purification variations are tested, but the stated “beam/pixel-window cancellation” argument is asserted without direct quantitative test. The analysis uses no beam and does not deconvolve the HEALPix pixel window, relying on cancellation between skies and templates.
- Required fix: Provide a quantitative check that varying/removing a common beam and applying/not applying pixel-window deconvolution do not materially shift β̂ (e.g., at the 1–2 mdeg level), or state and bound the induced bias. A simple additional MC configuration suffices.

P1B-M2
- Location: Sec. VI, p. 9 and footnote 4
- Problem: The spectator-ALP ODE is integrated on a ΛCDM H(z) while the paper elsewhere discusses a quintom background. The manuscript asserts this background difference induces only “≲ few-percent” changes in Δϕ/fa, but no quantitative evidence is shown.
- Required fix: Provide a quantitative comparison: integrate once on the ΛCDM background and once on the w0–wa chain mean background (Sec. V, Table II), and report Δ(Δϕ/fa) percent shift. If negligible (<5%), state the number. Otherwise, propagate the difference to β and discuss.

P1B-M3
- Location: Abstract p. 1; Sec. III pp. 3–5; Table I p. 17; Fig. 2 p. 5
- Problem: The ΔNeff results are presented as “consistent with zero,” which is correct. However, given the unresolved PR4/2018 pairing caveat (E2), the one-sided upper limits quoted in Sec. III (ΔNeff < 0.31, 0.39 at 95%) should include an explicit note that they could shift under a consistent-pairing test.
- Required fix: After addressing E2, confirm that one-sided upper limits remain within quoted ranges. If not, update the limits and state the dependence on the pairing choice.

P1B-M4
- Location: Acknowledgments, p. 13
- Problem: The acknowledgment of using “Claude (Anthropic) as an AI research assistant” is acceptable only if it conforms to APS policy (no AI authorship; human verification of content). The current wording is unusual for PRD.
- Required fix: Confirm APS policy compliance and edit wording to the standard disclosure if APS requests it (e.g., “The author used an AI tool (Claude) to assist with language and organizational editing; all scientific content and conclusions are the author’s own and were independently verified.”). Check with the editor if additional disclosure is required.

MINOR

P1B-m1
- Location: Fig. 2, p. 5
- Problem: The axis label appears to read “Neff,” while the text and caption discuss ΔNeff. Tick marks run from about −1 to +1, i.e., ΔNeff.
- Required fix: Relabel the axis to ΔNeff to avoid ambiguity.

P1B-m2
- Location: Sec. IV, Fig. 3 caption, p. 7
- Problem: The caption lacks the explicit “not directly comparable” warning for the 20–26 SNR values versus sky detection significances mentioned nearby in the section text.
- Required fix: Add a parenthetical in the caption that these are MC template-fit SNR values and not sky-detection significances; not directly comparable to the 2.7–2.9σ Planck/ACT results.

P1B-m3
- Location: Sec. VI, p. 10
- Problem: The text calls ACT DR6 “published” while citing an arXiv preprint (Ref. [4]).
- Required fix: Replace “published Planck/ACT DR6 2.7–2.9σ” with “reported Planck (published)/ACT DR6 (preprint) 2.7–2.9σ” and keep the caution about shared calibration systematics.

P1B-m4
- Location: Title block p. 1
- Problem: “Dated: June 11, 2026 PDT — v1B.0.59” includes timezone and an internal version code.
- Required fix: Remove timezone and internal version code from the manuscript header. PRD will insert received/accepted dates.

P1B-m5
- Location: Sec. III footnote 1, p. 3
- Problem: Confusing burn-in narrative: both 20% (GetDist readout) and 30% (author’s conservative choice) are discussed for the same chains.
- Required fix: State a single, final burn-in fraction used for all quoted results and move reconciliation detail to a short appendix paragraph.

P1B-m6
- Location: Sec. IV, p. 6
- Problem: The noise modeling paragraph mixes sr-to-arcmin^2 conversions and shorthand. It is correct numerically (Ωpix ≈ 47.21 arcmin^2; σpix ≈ 1.455 µK), but the algebraic equivalence sentence could be clearer.
- Required fix: Present one clean conversion line; optionally move ancillary equivalence to a footnote.

P1B-m7
- Location: Sec. VI, p. 10
- Problem: The αEM/(4π) numeric prefactor is given only implicitly. While consistent, readers may appreciate the explicit value used.
- Required fix: Add αEM/(4π) = 5.806×10−4 (for αEM = 1/137.036) to the line presenting the β computation.

NITS (cosmetic/editorial)

P1B-n1
- Location: Throughout
- Problem: Repetitive use of “canonical” and overlong footnotes (e.g., footnote 3 in Sec. IV).
- Required fix: Trim for concision; consider moving lengthy footnotes to an appendix.

P1B-n2
- Location: Table I, p. 17
- Problem: Spacing artifacts in decimals (e.g., “0 .827 ± 0 .010”) likely from typesetting/PDF extraction.
- Required fix: Ensure consistent decimal formatting in the final typeset version.

P1B-n3
- Location: Sec. VI, p. 9–11
- Problem: Multiple references to “committed EOM grid” and “artifact c10b_alp_envelope_scan.json” in the main text hamper readability.
- Required fix: Move file-name-level provenance to a short appendix and cite only the DOI-tagged archive in the main text.

Arithmetic, dimensional and internal-consistency spot checks
- ΔNeff means/σ in abstract and Table I match and are self-consistent.
- H0 tension: (73.04 − 67.68)/sqrt(1.04^2+1.06^2) ≈ 3.6σ; the text’s 3.6σ is correct.
- S8 tension (w0–wa chain): (0.8245 − 0.776)/sqrt(0.0089^2+0.017^2) ≈ 2.53σ; quoted 2.5σ is consistent.
- MB–H0 degeneracy constant calculations: both −18.571 and −18.415 recompute; 0.156 mag offset; “3.2σ” relative to σMB=0.049 is correct.
- Inverse-variance combination (Planck+ACT): β = 0.241° ± 0.061°, 3.9σ vs 0; matches recomputation; caveat about correlated systematics included (good).
- ALP birefringence normalization: β = (αEM/4π) Caγ Δϕ/fa with αEM/(4π) ≈ 5.806×10−4; with Caγ=8 and Δϕ/fa=1.06 gives β≈0.282°; matches.
- NaMaster MC: σpix ≈ 1.455 µK at Nside=512 for ΔP=10 µK·arcmin; correct. Multiplicative under-recovery ≈12% (0.238/0.27 and 0.302/0.342); correct.
- LiteBIRD forecast: 0.27°/0.03° = 9σ; correct, and the manuscript notes non-discrimination relative to current central value; good.

Scope and claims calibration
- The manuscript is careful to state scope limitations for each of the three analyses. However, the w0–wa “departures” from ΛCDM must not be presented as headline results unless the SN overlap is handled correctly (P1B-E4), and the mixed Planck likelihood pairing must be shown to be harmless at the quoted precision (P1B-E2).

Length and focus
- The paper is long (19 pages) relative to its core contributions. Much of the repository path detail and version-history narrative belongs in a supplement. A tighter main text (≈12–14 pages) with an online supplement would be more appropriate for PRD while preserving reproducibility.

## Summary recommendation
MAJOR REVISIONS

The paper contains solid methodological work, and most numerical claims are internally consistent and well-caveated. However, essential issues remain before PRD standards are met: (i) the Planck PR4/2018 pairing-consistency test for the ΔNeff/H0 results is missing; (ii) the w0–wa analysis combines partially overlapping SN samples without a joint covariance while quoting multi-σ departures; and (iii) the reproducibility record must be finalized with a clean, DOI-minted archive and removal of internal version-history/process language from the main text. Addressing these, along with the listed major/minor corrections, would make the manuscript suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (after a fresh, adversarial pass)

ESSENTIAL

P1B-E6
- Location: Sec. III (proxy configuration, p. 3) and Table I (ΔNeff results, p. 17)
- Problem: Helium treatment with variable Neff is not documented rigorously enough for PRD standards. The text says “YHe follows the CAMB BBN-consistent default (no explicit override)” while allowing ΔNeff down to −1 (Neff ∈ [2.046, 5.046]). BBN-consistency fits (and their validity ranges) matter when Neff is varied, and going as low as Neff ≈ 2.046 risks stepping outside calibrated domains of approximate BBN fits depending on the code path. Without an explicit statement of the BBN engine, its validity range, and a cross-check with a free-YHe run, the ΔNeff posteriors and one-sided limits (ΔNeff < 0.31, 0.39) are under-specified.
- Required fix: Specify exactly which BBN-consistency module is used (e.g., PArthENoPE-based) and its validity range versus Neff. Add a control run freeing YHe (or restricting to Neff ≥ 3.046) to quantify the impact on ΔNeff and H0. If differences exceed the quoted precision, update the limits and elevate the caveat to the abstract.

MAJOR

P1B-M5
- Location: Sec. IV (NaMaster configuration, pp. 6–8)
- Problem: The beam/pixel-window “cancellation” argument is asserted but not comprehensively tested. You tested apodization, purification, and sky fraction, and you quote a null impact when restricting to ℓ ≤ 1024. However, you did not explicitly quantify the shift when (i) inserting a nontrivial, common beam (e.g., 1–2 arcmin FWHM) and (ii) toggling pixel-window deconvolution both on/off in the decoupled spectra and the template. This matters because the canonical result is a small absolute bias (−0.032°), so a 1–2 mdeg methodological bias from beam/pixel choices is material.
- Required fix: Add two MC configurations: common Gaussian beam on/off and pixel-window deconvolution on/off. Report Δβ̂ at the 1–2 mdeg level. If non-negligible, incorporate it into the bias budget or the “systematic floor.”

P1B-M6
- Location: Sec. IV (Robustness battery, p. 8)
- Problem: The canonical estimator is deliberately kept unweighted to “match published drivers,” yet you show the inverse-variance-weighted fit reduces the bias from −0.032° to −0.006° (~80% reduction). For a methods-validation paper, continuing with an estimator known to be significantly biased is hard to justify as the baseline, and labeling 0.040° a “systematic floor” risks conflating correctable estimator bias with irreducible systematics.
- Required fix: Either adopt the inverse-variance-weighted fit as the baseline (and report the smaller bias) or, at minimum, rename “NaMaster systematic floor” to “NaMaster unweighted-estimator bias floor,” and clearly state that it can be reduced by weighting. Provide both results side-by-side in Fig. 3 or the main text.

P1B-M7
- Location: Sec. IV (Pipeline configuration, p. 6)
- Problem: Single ℓ-range. You note only one binning/ℓ-range is exercised. Since the estimator bias is multiplicative and driven by high-ℓ noise weighting, a modest ℓmax sweep is an important control.
- Required fix: Add an ℓmax sweep (e.g., ℓmax ∈ {768, 1024, 1280} with identical seeds and masks) and report Δβ̂. If stable at the <1–2 mdeg level, state that bound.

P1B-M8
- Location: Sec. IV (Noise model), Fig. 3
- Problem: Only isotropic white noise is tested. This is acceptable for a first check, but the known ACT/Planck noise is anisotropic with mild 1/f. Because bin weighting is central to your bias story, even a simple anisotropic (hit-count–like) or 1/f toy model could alter the unweighted-fit bias.
- Required fix: Add one anisotropic-noise and one simple 1/f toy configuration to quantify Δβ̂ (even at coarse level). State bounds or include any observed shifts in the bias budget.

P1B-M9
- Location: Sec. VI (ALP MCMC), Appendix C
- Problem: MCMC diagnostics for the ALP chains are under-reported. You give accepted-sample counts and R̂ − 1, but not effective sample sizes (ESS) or autocorrelation times, and one key configuration has only 720 accepted samples (βfree). For PRD reproducibility standards, ESS should be reported.
- Required fix: Report per-parameter ESS (and/or autocorrelation times) for all ALP chains, especially β, θi, log10 ma, and Caγ in the continuous-prior run. If ESS is low (e.g., <O(10^3) for key parameters), extend the chains or use more efficient sampling (e.g., slice/DEMetropolisZ).

P1B-M10
- Location: Sec. VI (ALP background choice), footnote 4
- Problem: You state that replacing ΛCDM H(z) with the w0–wa background changes Δϕ/fa by “≲ few percent,” but do not quantify it. This is especially straightforward given your own w0–wa chain (Table II).
- Required fix: Integrate the ALP EOM once on ΛCDM and once on the Table II w0–wa mean background, for a representative set of (θi, m/H0), and report the percent change in Δϕ/fa (and corresponding β). If <5%, state the number; if larger, propagate.

P1B-M11
- Location: Sec. VI (ALP mass–H0 conversion), Fig. 4 caption
- Problem: You adopt H0 = 67.7 km/s/Mpc to map log10(ma/eV) to m/H0 but your own cosmology chain gives H0 = 67.185 ± 0.455. While small, this uncertainty slightly shifts the m/H0 scale and the “saturation” regime.
- Required fix: State that the H0 uncertainty induces only a ~1% rescaling in m/H0 and is negligible for the present β-level constraints, or propagate it explicitly (trivial to do).

MINOR

P1B-m8
- Location: Sec. VI (periodicity statement), p. 10
- Problem: You write “β ≡ β + n × 90° for E/B,” without units. Readers could momentarily conflate degrees/radians.
- Required fix: Clarify: “β ≡ β + n × 90° (≡ β + n × π/2 radians).”

P1B-m9
- Location: Sec. IV (binning), p. 6
- Problem: You specify bin edges via np.linspace(30, 1536, 21). NaMaster expects integer ℓ-edges; linspace returns floats by default.
- Required fix: State explicitly that edges are integer-cast before passing to NaMaster (or specify the exact integer edges). This avoids ambiguity for re-implementers.

P1B-m10
- Location: Fig. 3 caption, p. 7
- Problem: Units are not repeated in the y-axis description of recovered β for panel (b).
- Required fix: Add “deg” in-panel or in-caption for all reported β and σβ values.

P1B-m11
- Location: Sec. IV, footnote 3
- Problem: Residual “earlier draft” phrasing remains in the footnote (“quoted in an earlier draft of this footnote”), separate from the global version-history issue (P1B-E1).
- Required fix: Remove “earlier draft” wording in the footnote and keep only the final, checked numbers.

P1B-m12
- Location: Sec. III (Planck nuisance list), Table I note
- Problem: The presence of Aplanck as a nuisance for a CamSpec PR4 high-ℓ likelihood may confuse readers (CamSpec’s calibration handling differs from Commander/SimAll). You also include calTE, calEE, amp143, amp217, etc., which is fine if it matches the PR4 CamSpec block.
- Required fix: Add a one-line reference (or appendix table) mapping your nuisance list to the exact PR4 CamSpec likelihood version you used, to confirm the parameterization matches the likelihood release.

P1B-m13
- Location: Sec. IV (mask description), p. 6
- Problem: The ACT-like footprint is defined as |b| > 20° and dec ∈ [−65°, +25°] and apodized with 2° FWHM, yielding fsky = 0.32. This implies a specific apodization kernel and effective sky fraction after apodization, which can vary slightly with thresholding.
- Required fix: State whether fsky = 0.32 refers to the post-apodization effective area (e.g., sum of W^2 over sky) and specify the exact fsky definition used (NaMaster convention vs unweighted area).

P1B-m14
- Location: Sec. VI (ALP MCMC, continuous-prior results)
- Problem: You report coupling posterior fractions (e.g., “69% in [9, 51]”) but do not provide an accompanying figure for Caγ’s 1D posterior or ESS for that parameter.
- Required fix: Add a 1D Caγ posterior plot in a supplement and report its ESS alongside Fig. 4 for completeness.

ARITHMETIC/SPOT-CHECKS ADDED IN THIS PASS

- One-sided ΔNeff limits verification: For the full-tension chain (μ = −0.020, σ = 0.169), truncation at 0 gives a 95th percentile at x ≈ −0.02 + 2.00×0.169 ≈ 0.318 ≈ 0.32 (paper quotes 0.31; small rounding difference). For Planck+BAO+SN (μ = 0.058, σ = 0.179), truncation at 0 gives x ≈ 0.058 + 1.85×0.179 ≈ 0.389 (paper: 0.39). Consistent.

- w0–wa phantom crossing redshift: 1 − a× = (−1 − w0)/wa = (−1 + 0.8122)/(−0.6666) = 0.2818 → a× = 0.7182 → z× = 1/a× − 1 = 0.392. Matches “z× ≈ 0.39.”

- m/H0 conversion bounds: With H0 = 67.7 km/s/Mpc = 1.44×10−33 eV, the prior log10(ma/eV) ∈ [−35, −30] corresponds to m/H0 ≈ [10−35/1.44×10−33, 10−30/1.44×10−33] ≈ [0.0069, 694] = [7×10−3, 7×10^2]. Matches Fig. 4 caption.

FIGURE-CAPTION VS BODY-CLAIM CHECKS ADDED IN THIS PASS

- Fig. 3 vs body: Body text quotes β̂ = 0.237° (fsky = 0.85, σβ = 0.029°) and 0.236° (fsky = 0.65, σβ = 0.033°); caption shows these σβ values but does not show the recovered means at 0.237° and 0.236° explicitly. Not an error, but consider adding the recovered means in the caption for clarity.

EQUATION DIMENSIONAL CONSISTENCY ADDED IN THIS PASS

- Rotation template: You correctly note that an EE-only template sin(2β)cos(2β) CEE misses the −CBB term (small for lensed ΛCDM). You later quantify the impact; dimensions are consistent. No new dimensional issues found.

INTERNAL CROSS-REFERENCES

- No new broken cross-references identified beyond those in the first review. Equation (4) (inverse-variance βcomb) is referenced correctly; Table II footnote b correctly connects the pivot calculation to zp = 0.27.

NULL PROCEDURE COMPARABILITY

- No additional juxtapositions found beyond the Fig. 3 caption case (already raised in the first review and reiterated here as P1B-m10).

ABSTRACT FAITHFULNESS

- The abstract’s sentence “the worst-case bias … is carried forward as the pipeline systematic floor” should be softened per P1B-M6 (it is an estimator-choice bias floor, not an irreducible systematic). Otherwise, the abstract remains consistent with the body.

STALE NUMBERS

- Footnote 3 retains “quoted in an earlier draft” verbiage (P1B-m11). No new stale numeric mismatches detected; the updated ALP Δϕ/fa correction appears consistently propagated.

SUMMARY

The most important NEW items are (i) the helium/BBN-consistency treatment for variable Neff (P1B-E6), and (ii) the need to treat the NaMaster “systematic floor” as an estimator-choice bias and to test beam/pixel/ℓmax/noise-model sensitivities quantitatively (P1B-M5–M8). Additional MCMC diagnostics for the ALP chains (ESS) and small clarifications (units, bin edges) are also recommended. These are in addition to, not replacements for, the essential issues in the initial review.