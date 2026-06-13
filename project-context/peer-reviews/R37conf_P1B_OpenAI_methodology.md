# P1B R37conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.65.pdf` md5=bac8d620 pages=20
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6644 chars)
**Wall time**: 309.3s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall assessment
The manuscript presents three technical components: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy run; (ii) a NaMaster pseudo-Cl pipeline validation for birefringence recovery on synthetic skies; and (iii) a spectator-ALP consistency check against a Gaussian summary likelihood for β. The paper is careful in several places about scope, caveats, and the distinction between pipeline Monte Carlo SNR and sky detection significance. Many numerical statements are traceable and arithmetically consistent. However, several methodology and presentation issues must be addressed to meet PRD standards, particularly around (a) the supernova overlap handling in the w0wa cross-check (currently quoted with σ-levels in a main table without the needed joint covariance), (b) adoption of a demonstrably biased unweighted estimator as the “canonical” baseline for the NaMaster validation while using its output to define a “systematic floor,” and (c) reproducibility archiving and versioning (stable DOIs). Below I list detailed findings by severity.

Findings

ESSENTIAL

P1B-E1 — Section III, Table II (page 19) and Section III discussion (pages 4–5)
Problem: The w0wa “DESI DR2 + Planck NPIPE + DES-Y5 + Pantheon+” posterior is presented in a main table with σ-level tail distances (e.g., “w0 −0.8122 ± 0.0436 (+4.3σ), wa −0.6666 ± 0.1864 (−3.6σ)”), while the body text acknowledges that the SN product likelihood double-counts ~20% overlapping SNe and does not include a joint-covariance treatment for the DES-SN5YR × Pantheon+ overlap. Although caveats are discussed in the text, the table formatting elevates these into headline numbers a reader may treat as primary. PRD requires either correct data treatment or that such provisional results be quarantined from the main results and their σ-levels removed or clearly demoted.
Required fix: Either (a) rerun the w0wa analysis with an overlap-corrected SN joint covariance and update Table II; or (b) move the w0wa posterior to an appendix and remove σ-level annotations from the main text/table, labeling the results strictly as a provisional internal cross-check. Also add a one-sentence warning in Table II caption explicitly stating “This table uses a product SN likelihood without overlap covariance and the σ-distances are therefore not suitable for model preference.”

P1B-E2 — Section IV, Eq. (1) and associated text (pages 7–9), Abstract (page 1), Conclusions (page 13)
Problem: The birefringence recovery adopts an unweighted χ² template fit (no σb² weighting) that the authors show induces a ~12% multiplicative bias on β (−0.032° at 0.27°, −0.040° worst case at 0.342°). Despite demonstrating that inverse-variance weighting removes ~80% of the bias (β̂ = 0.264°, bias −0.006°), the paper designates the unweighted fit as the “canonical baseline” and then carries the 0.040° number forward as a “NaMaster systematic floor.” Using a known-suboptimal estimator as canonical while elevating its induced bias to a “systematic floor” is not methodologically sound. A floor defined by an avoidable estimator bias is not a property of NaMaster; it is a property of the estimator choice.
Required fix: Make the inverse-variance-weighted estimator the baseline in Sec. IV (recompute the 500-MC results with weighting; report the resulting bias and scatter; update Fig. 3 and text accordingly), and explicitly retire the 0.040° “systematic floor” language. If you wish to retain an unweighted-estimator replication for comparison with prior code, present it clearly as a “historical-replication configuration,” not as canonical, and state that this bias is avoidable. If you keep both, present both sets of numbers side by side with a clear recommendation to use the weighted estimator for future work.

P1B-E3 — Data and Code Availability (page 14) and Appendix A (pages 14–15)
Problem: Reproducibility relies on mutable GitHub repositories and HuggingFace datasets with “DOI assignment pending.” PRD requires stable, citable archival records for data/code underlying main claims (particularly frozen chains, NaMaster artifacts, and ALP chains).
Required fix: Deposit all frozen chains, masks, scripts, and artifacts used to generate the primary numbers and figures in a stable repository with DOIs (e.g., Zenodo) and cite those DOIs in the paper. Include an immutable tag/commit hash for the code version used to produce the results, and ensure the paper references those permanent identifiers, not moving branches or “pending” notes.

MAJOR

P1B-M1 — Planck PR4/2018 pairing (pages 3, 6, 13; Table III page 19)
Problem: The high-ℓ CamSpec likelihood is PR4/NPIPE while the low-ℓ and lensing likelihoods are Planck 2018. You note this is the standard Cobaya pairing and that a pairing-swap test was not performed. Given ΔNeff and H0 are the main quantitative outcomes from the ΛCDM+ΔNeff proxy, PRD would expect a release-consistency check.
Required fix: Add a control run with PR4-consistent low-ℓ/lensing (or, if unavailable, a run using 2018-only across all Planck blocks) and report the shifts in ΔNeff and H0. If not feasible, quantify a bound on possible shifts using literature benchmarks and state that bound numerically in the Results section.

P1B-M2 — NaMaster Fig. 3 and text (pages 7–9)
Problem: Panel (a) reports 500-MC mean recovered β̂ at three injected angles but omits uncertainty bars on the means for the canonical fsky=0.32 point (with a post-hoc claim that a rerun yields σβ=0.046° and |β̂|/σβ ~5.2). As presented, the central plot markers have no associated sampling error.
Required fix: Include standard error bars (σβ/√N) for all plotted mean points, including fsky=0.32 (computed from your stated rerun). Add these numbers to the caption. If the canonical results were re-run to obtain σβ, clearly mark which points are from the rerun and ensure consistency with the numbers quoted in the text.

P1B-M3 — “Systematic floor” generality (pages 7–9, 13)
Problem: The “worst-case |bias|=0.040° is carried forward as the NaMaster systematic floor” could be misconstrued as general to NaMaster. The measured bias is a function of estimator, ℓ-binning, Nside, mask/apodization, and noise level; you already demonstrate its estimator dependence.
Required fix: Rephrase throughout as “estimator- and configuration-dependent bias measured in this MC setup; not a general NaMaster floor.” Quantify each configuration ingredient (Nside, ℓ-bins, mask, ∆P) explicitly where the floor is stated.

P1B-M4 — Abstract/Conclusions numerical audit language (pages 1 and 13)
Problem: The abstract and conclusions include several quantitative statements that are careful but dense. For example, “the spectator-safe (Ωa < 0.01) subset is tuned… see Table IV” and “median m ≃ 36 H0 at fixed Caγ=8.” While traceable to the body, require explicit numeric references to avoid ambiguity.
Required fix: In the abstract and conclusions, add the explicit β values and uncertainties (when referring to subsets), and state the key posterior numbers with their uncertainties once (e.g., “m/H0 median 36, 16–84% [X, Y] at fixed Caγ=8”) so a reader need not search the appendices for quantitative detail.

P1B-M5 — Use of product SN likelihood in “goodness-of-fit” breakdown (Table II, page 19)
Problem: Table II reports χ²SN for a product SN likelihood that double-weights overlapping events. Although you correctly say the channel χ² are not independent, the SN χ² itself is biased by construction.
Required fix: Add a sentence in the Table II caption: “The SN χ² is computed from a product of DES-Y5 and Pantheon+ likelihoods without overlap covariance; its value is therefore not interpretable as a standard goodness-of-fit statistic.”

MINOR

P1B-m1 — S8 tension arithmetic consistency (pages 5 and 18)
Problem: Two different S8 tensions are reported in different contexts (iter2 chain vs Planck+BAO+SN). The numbers are consistent once one notices they refer to distinct chains, but this is easy to miss.
Required fix: Where S8 tensions are quoted, explicitly state the chain (“iter2 w0wa chain” vs “Planck+BAO+SN ΔNeff chain”) next to the numbers.

P1B-m2 — Terminology consistency (pages 7–9)
Problem: “Template-fit SNR” vs “per-realization angle SNR |β̂|/σβ” are distinct. The text clarifies this in a footnote but the main narrative risks casual conflation.
Required fix: Promote a short explicit sentence in the main text (not only a footnote): “Template-fit SNR (matched-filter SNR of EB bandpowers) is not the significance of β̂; the latter scales as |β̂|/σβ per realization.”

P1B-m3 — Beam/pixel window discussion (page 7)
Problem: You state no beam is applied and that pixel-window smoothing is common to map and template, so it cancels. This is fine for the synthetic test, but it reads as a blanket statement.
Required fix: Add a clause: “For this synthetic test only; on real data, beam and pixel-window mismatches must be controlled separately.”

P1B-m4 — Notation clarity (pages 10–12)
Problem: In Sec. VI you alternate between θi and “misalignment initial condition” without always restating that θi ≡ ϕi/fa. Also, “median m ≃ 36 H0 at fixed Caγ=8” would benefit from brackets ([16–84%]) for completeness.
Required fix: Add a brief parenthetical “θi ≡ ϕi/fa” upon first use in Sec. VI; provide a 16–84% credible interval for m/H0 wherever a median is quoted.

P1B-m5 — References formatting (pages 16–17)
Problem: Some references include informal annotations (“reports beta = 0.30 +/- 0.11 deg”). PRD style typically avoids claims in the reference list.
Required fix: Move such annotations to the main text; ensure the reference list conforms to PRD formatting.

NIT

P1B-n1 — Version-history language in the body (pages 14–15)
Problem: The paper body includes internal version stamps (“in-tex v1B.0.65,” “closure wave,” “COUNT_EXPLANATION.md”). PRD papers should avoid internal repository process language in the manuscript proper.
Required fix: Remove or move all version-history and internal bookkeeping prose to the repository README or supplemental material; in the paper, cite only stable DOIs/commit hashes.

P1B-n2 — Acknowledgment of AI assistant (page 14)
Problem: “Acknowledges the use of Claude (Anthropic) as an AI research assistant” is unusual in PRD acknowledgments and may prompt editorial questions.
Required fix: Check PRD policy; if retained, keep to a single neutral sentence or remove.

P1B-n3 — Redundant phrasing (minor)
Problem: Several instances of repetitive qualifiers such as “canonical mask” appear.
Required fix: Light edit for concision.

Arithmetic and dimensionality spot-checks
- H0 tension with SH0ES: |73.04 − 67.68| / sqrt(1.06² + 1.04²) = 3.62σ, consistent with “~3.6σ.”
- MB–H0 constant: −19.253 − 5 log10(0.7304) = −18.571; chain mean −19.263 − 5 log10(0.6768) = −18.415; offset 0.156 mag; 0.156/0.049 = 3.18σ; text correctly notes this is not a properly conditioned tension statistic.
- Template-fit SNR scaling with fsky: 20.32 × sqrt(0.85/0.32) = 33.14, consistent with quoted 33.12.
- Multiplicative under-recovery: 0.238/0.27 = 0.881 and 0.302/0.342 = 0.883 (~12% low).
- ∆P → σpix: Nside=512 gives Ωpix ≈ 47.21 arcmin²; σpix = 10 / sqrt(47.21) = 1.455 μK; consistent.
- ALP β: (αEM/4π) Caγ ∆ϕ/fa = 0.000581 × 8 × 1.06 = 0.00493 rad = 0.283°, consistent with 0.28°.
- Inverse-variance combination of Planck NPIPE and ACT DR6: β = 0.241° ± 0.061° (3.9σ), as stated with proper caveat on correlations.

Length and scope
This is a 20-page “technical verification companion.” For PRD, this is acceptable provided the essential revisions are addressed. If the w0wa content remains provisional, it should be compressed or moved to an appendix until overlap-corrected results are available.

## Summary recommendation
MAJOR REVISIONS

The core ΛCDM+ΔNeff proxy and the ALP consistency check are carefully executed and numerically sound. However, before the paper can meet PRD methodological standards, the authors must: (i) correct the SN-overlap issue by either rerunning w0wa with a joint-covariance SN combination or removing σ-level claims from main results; (ii) adopt the inverse-variance-weighted EB estimator as baseline for the NaMaster validation (or refrain from using the biased unweighted estimator to define any “systematic floor”); and (iii) provide stable DOI-backed archival deposits for all data/code artifacts cited. Additional smaller presentation and clarification edits are also required as detailed above. With these changes, the work would meet PRD’s rigor bar for a methods-focused companion.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B — ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT (NEW ONLY)

ESSENTIAL

P1B-E4 — Weighted estimator specification missing (Sec. IV, pages 7–9)
Problem: You report that an “inverse-variance-weighted fit” removes ~80% of the β bias (β̂ = 0.264°, bias −0.006°), but the paper never specifies how the weights σb were obtained (analytic MASTER covariance, MC-estimated per-bin scatter, or a hybrid). Without an explicit covariance/weighting definition, the magnitude of the bias reduction and any quoted SNR based on those weights are not reproducible and may be circular (using the same MC both to set σb and to assess performance).
Required fix: Define precisely how σb (or the full bandpower covariance) is computed for the weighted fit. If MC-derived, state the number of realizations used for σb estimation, how you avoid bias from using the same MC twice, and whether off-diagonal bin-bin covariance is included. If analytic, provide or cite the MASTER variance formula and all ingredients (Cℓ, fsky, apodization, noise model). Report results with this fully specified weighting.

MAJOR

P1B-M6 — ALP mass “prior-edge” wording vs reported posterior (Sec. VI, Fig. 4, pp. 11–13)
Problem: The text states that “the ma marginal piles toward the upper (heavier) edge of its prior range,” but the headline fixed-Caγ=8 posterior reports a median m ≃ 36 H0 and Fig. 4 does not show clear piling at the upper prior edge (m/H0 up to ~7×10^2). As written, the “piles to the edge” claim overstates the evidence.
Required fix: Quantify the mass posterior (median and 16–84% credible interval) everywhere you claim edge behavior. If the 84% quantile is well below the prior maximum, soften the language (“skewed to heavier masses” instead of “piles to the edge”) or provide the tail percentile (e.g., fraction of posterior mass above m/H0 > 300).

P1B-M7 — Neutrino-mass scheme sensitivity not assessed (Sec. III, V; Tables I, III)
Problem: The ΛCDM+ΔNeff results fix Σmν=0.06 eV with one massive eigenstate. ΔNeff constraints and H0 can shift at the ~0.1–0.2σ level under alternate standard choices (e.g., three degenerate masses or Σmν free). No control run is provided.
Required fix: Add a control run (Planck+BAO+SN) with three degenerate massive neutrinos (Σmν=0.06 eV) and report the shifts in ΔNeff and H0. If computationally infeasible, cite literature bounds on the expected shift and state them numerically in your Results.

P1B-M8 — BBN-consistency domain for YHe vs Neff not documented (Sec. III, page 3)
Problem: You assert that Neff ∈ [2.046, 5.046] “remains within the calibrated domain of the CAMB BBN module” but provide no citation/verification. Outside the nominal calibration range, BBN-YHe extrapolation can bias ΔNeff.
Required fix: Cite the validated Neff–YHe calibration domain for the PArthENoPE-based CAMB predictor you used (versioned source), or add a free-YHe control run to demonstrate negligible impact on ΔNeff/H0 at your precision.

P1B-M9 — Beam-mismatch test deferred but needed to bound bias (Sec. IV, pages 7–9)
Problem: The synthetic validation applies no beam and argues partial cancellation between map and template. While acceptable for a first check, the paper still uses the MC-derived bias to characterize pipeline behavior. No quantitative bound is given for a plausible beam mismatch.
Required fix: Add a minimal beam-mismatch control (e.g., Gaussian beam FWHM offset by ±5–10% between injected skies and template deconvolution) and report the induced shift in β̂. If deferred, state a numerical bound from literature or an upper limit from a small MC, to prevent over-interpretation of the quoted bias.

MINOR

P1B-m6 — Table IV percentile labeling ambiguous (page 20)
Problem: Entries like “m/H0 4.7/37.7/264” and “Caγ 14.2/26.2/46.4” appear to be 16/50/84 percentiles but are not labeled, while the last row explicitly says “16/50/84=…”.
Required fix: Add “(16/50/84 percentiles)” to the column header or each affected row to remove ambiguity.

P1B-m7 — “Natural-prior midpoint θi ∼ 0.5” terminology inconsistent (Sec. VI, pages 10–12; Appendix C)
Problem: You sometimes refer to θi ∼ 0.5 as the “natural-prior midpoint,” but elsewhere the θi prior spans [0.01, π] (midpoint ~1.57). It appears 0.5 is the midpoint of a narrower exploratory grid (θi ∈ [0.5, 2]).
Required fix: Clarify that “0.5” refers to the midpoint of the exploratory grid, not the full prior; when quoting “25×” misalignment tuning, state explicitly which reference value (0.5) is used and why.

P1B-m8 — Weighted-template SNR definition depends on σb source (Sec. IV, footnote 4 and main text)
Problem: You define SNRtmpl with σMC_b, but the main text also references an “inverse-variance-weighted” fit without specifying whether those σb are the same. This risks conflation.
Required fix: State explicitly whether the σb used for SNRtmpl and those used for the inverse-variance fit are identical or distinct, and how each is computed.

P1B-m9 — “0.000° at βinj=0” rounding (Sec. IV, page 8)
Problem: Reporting an exact 0.000° recovery at βinj=0 can be misread as machine-precision cancellation rather than rounding of the 500-MC mean.
Required fix: Add “(rounded to three decimals)” or quote with one more decimal/significant figure to indicate a finite residual consistent with noise.

P1B-m10 — Mask/sky-fraction reproducibility (Sec. IV, Fig. 3 caption)
Problem: The text describes ACT-like, Planck-like, and DR6-like masks with apodization, but fsky values are only quoted approximately in the prose.
Required fix: State the exact fsky used for each mask in the caption (to three decimals) and archive the exact binary/apodized masks with the DOI deposit.

NIT

P1B-n4 — Additional process-language in main text (Sec. IV Reproducibility paragraph; Appendix A)
Problem: Terms like “pod run,” specific internal paths, and artifact filenames remain in body text.
Required fix: Move such operational details to supplemental/README and keep the manuscript to stable DOIs, commit hashes, and method summaries (complements P1B-n1 but applies to additional locations).

P1B-n5 — Cite/source of the “Planck-2018 semi-analytic EE template” (Sec. IV, pages 7–8)
Problem: The phrase “semi-analytic fit to the Planck-2018 EE spectrum” is not referenced nor archived.
Required fix: Provide a citation or deposit the exact template file used (and its generation script) with the DOI archive.

EXPLANATION
These items were not covered in the first report and emerged from a targeted second-pass check focusing on arithmetic/consistency, estimator specification, and claims-versus-evidence alignment. No previously listed issues are repeated here.