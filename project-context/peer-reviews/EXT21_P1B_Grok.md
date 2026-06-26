# EXT21 P1B Grok — chat: https://grok.com/c/f47dc835-8384-445b-8bd6-0cba875344b9

Referee Report: MNRAS / Phys. Rev. D / JCAP
Paper: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
Author: Houston Golden
Date of report: June 2026
Recommendation: MINOR REVISIONS

Summary

This companion paper supplies the numerical verification layer for the structural no-go analysis of minimal Einstein–Cartan–Holst (ECH) dark-energy routes presented in the concurrently submitted Paper I(a). It reports three scoped analyses: (1) a stock-CAMB ΛCDM+∆Neff MCMC proxy (Cobaya v3.6.1, 309 k frozen samples) demonstrating consistency with ∆Neff = 0 and no resolution of the Hubble tension; (2) a 500-realization NaMaster pseudo-Cℓ Monte-Carlo validation of the E→B deconvolution pipeline on synthetic ΛCDM skies (ACT-like mask, white noise), characterizing an empirical multiplicative under-recovery bias of ~12 % and worst-case absolute bias floor |∆β̂| = 0.040°; and (3) a spectator-ALP consistency check (Gaussian summary likelihood on the published Eskilt & Komatsu β = 0.342° ± 0.094° (3.6σ) measurement) showing that the observed rotation lies within the prior envelope but requires both non-minimal photon coupling (Caγ ≳ 9) and ~25× misalignment tuning (θi ~ 0.1) to remain spectator-safe (Ωa < 0.01). All three analyses are explicitly framed as proxies or consistency checks, not as direct tests of torsion-modified Boltzmann physics or as distinctive ECH predictions. Reproducibility materials (YAML configurations, committed frozen chains, driver scripts, robustness batteries, and planned HuggingFace datasets) are exemplary.

The work is technically sound, conservatively scoped, and transparently caveated. No load-bearing claim lacks supporting evidence from the committed artifacts, and the paper repeatedly flags what it does not claim.

BLOCKERS
None.

MAJORS
None.

MINORS

Scope reinforcement (abstract & §I). The paper already states repeatedly that the analyses are not direct tests of the spin-torsion sector and that the ALP signal is not an ECH prediction. A single additional sentence in the abstract or at the end of §I explicitly linking these null/consistency results back to the structural-closure conclusions of Paper I(a) would further reduce any risk of misreading. (Example phrasing: "These proxy and consistency checks leave the 13 structural barriers and perturbation-transparency theorem of Paper I(a) unaltered.") This is a presentation polish item, not a scientific gap.

Notation and cross-reference hygiene. Minor inconsistencies exist in angle notation (β vs. β̂ vs. βinj) and in the precise wording of "pipeline bias floor" versus "multiplicative under-recovery" between §IV and the abstract. A quick global pass to align terminology and ensure every numerical claim in the text has an explicit pointer to the relevant table/figure/artifact would eliminate any residual ambiguity. (The existing robustness battery and bias-attribution discussion are already strong.)

Footnote length and reader navigation. Several footnotes (especially fn. 1 on sample-count stratification, fn. 3 on PR3/PR4 disambiguation, and fn. 6 on spectator tuning) are long and contain important quantitative detail. Consider moving one or two of the longest quantitative derivations into short appendices or supplementary material if length permits; otherwise they are acceptable. No scientific content needs to change.

Reproducibility manifest (Appendix A). The Data Availability statement and version-stamp (v1B.0.74) are excellent. A one-line confirmation that the exact commit SHA corresponding to the in-text \paperVersion macro has been tagged in the public repository would close the loop for future readers. (This is a submission-day housekeeping item.)

All of the above are style, clarity, or future-proofing items. None requires new calculations, new runs, or reinterpretation of existing results.

Strengths (≥3)

- Outstanding reproducibility and transparency. Full Cobaya YAMLs, frozen chains (309 k samples), NaMaster driver scripts, 500-realization robustness batteries, and planned HuggingFace dataset DOIs are committed or queued. The "column-permutation warning" and corrected parameter_summary_CORRECTED.json documentation set a high bar rarely met in cosmology papers. This alone makes the work a model for the field.

- Rigorous and repeated scoping. The manuscript explicitly and repeatedly states the limitations of each analysis: stock-CAMB proxy (no torsion Boltzmann module), NaMaster validation (synthetic skies lack galactic foregrounds; not a sky measurement), and ALP check (not derived from ECH; requires spectator fine-tuning). These disclaimers are load-bearing and correctly placed in the abstract, §I, §III, §IV, §VI, and the conclusions. The paper does not over-claim.

- Thorough empirical validation and bias characterization. The NaMaster section includes sky-fraction sweeps, apodization-scale tests, purification tests, template-weighting tests, and BB-shape tests that cleanly attribute the ~12 % multiplicative bias to the unweighted χ² estimator plus crude CBB template. The worst-case |∆β̂| = 0.040° is carried forward conservatively. This level of pipeline validation is appropriate and well documented.

- Honest treatment of systematics and tuning. The SN-overlap Malmquist caveat (caveat (e)), the spectator-status ~25× misalignment tuning (fn. 6 and Table IV readout), the non-minimal Caγ requirement, and the fact that the same β arises in standard GR are all stated plainly and quantitatively. The LiteBIRD forecast is correctly caveated as a null-detection significance, not a model-discrimination forecast. This intellectual honesty strengthens the paper.

- Clean separation of proxy tests from theory. The work correctly frames the ∆Neff run as a bounce-class compatibility check (minimal matter-bounce predicts ∆Neff ≈ 0) rather than a posterior-preference test, and the ALP exercise as a consistency check rather than an ECH-derived prediction. This framing aligns with the structural no-go results of the companion Paper I(a).

Overall Assessment

The paper is a high-quality, conservatively written technical companion that meets the standards of MNRAS, Phys. Rev. D, or JCAP. The scientific content is sound, the scoping is exemplary, and the reproducibility infrastructure is best-in-class. The requested minor revisions are limited to presentation and navigation polish; they do not affect any numerical result, interpretation, or claim. I recommend MINOR REVISIONS and look forward to seeing the revised manuscript.
