# P1B auto-2026-06-09_1042pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 409.4s

---

META-REVIEW: blind-spot findings not caught by the 5 prior referees

P1B-META-E1
Severity: ESSENTIAL
Section/page: Sec. III (p. 2–3) vs Table II footnote b (p. 4)
Why others missed it: Several reviewers noted dataset-label ambiguity, but none identified the concrete release-mixing at the Planck likelihood level.
Problem (quote and analysis): The ΔNeff proxy run is described as “Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing” (p. 2–3), i.e., PR4/NPIPE at high-ℓ, but Table II footnote b explicitly says “planck 2018 lowl.EE + planck 2018 lowl.TT” (PR3 low-ℓ). Mixing PR4/NPIPE high-ℓ CamSpec with PR3 low-ℓ lowl.* is a release-mismatch that can shift τ, APlanck, and large-scale polarization calibrations in subtle ways. It also risks double-counting or miscalibrating polarization-angle and transfer-function choices across releases.
Required fix: State explicitly which Planck release is used at low-ℓ and high-ℓ for each chain. If you mix PR3 low-ℓ with PR4/NPIPE high-ℓ, justify this choice (with a stability test showing negligible impact on posteriors within quoted errors) or re-run with a self-consistent single-release stack (all-PR3 or all-PR4/NPIPE).

P1B-META-E2
Severity: ESSENTIAL
Section/page: Table I footnote a (p. 3)
Why others missed it: One reviewer flagged Mb’s misclassification, but no one noticed the resulting parameter-count inconsistency.
Problem (quote and analysis): “all 17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb for the SNIa absolute magnitude)…” Mb is not a Planck nuisance, and counting it inside the “10 Planck likelihood nuisance” makes the arithmetic inconsistent: 7 cosmological + 10 (including Mb) = 17 implies only 9 Planck nuisances were used, contrary to the wording. This also undermines the reported “Worst R̂−1” and “Min ESS” since readers cannot infer the true dimensionality per likelihood.
Required fix: Provide an exact parameter table per chain: list cosmological and each likelihood’s nuisances separately (Planck-CamSpec, low-ℓ, lensing, SN Mb, BAO if any). Correct the total counts and recompute “Worst R̂−1” and “Min ESS” against the accurate parameter set.

P1B-META-E3
Severity: MAJOR
Section/page: Sec. IV (p. 5–6)
Why others missed it: Reviewers focused on estimator and beam details; none flagged the omission of cosmic variance in the MC scheme.
Problem (quote and analysis): “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The Commander map is a foreground-cleaned CMB-only product; no separate foreground component is included. The β injections rotate Q+iU … before adding noise.” The MC holds the CMB sky fixed and varies only noise. For a rotation-induced EB estimator, sample variance of the E field propagates into B via the constant-β mixing and into the pseudo-Cℓ coupling through the mask. Using a fixed CMB realization underestimates the per-realization scatter and can bias both the “pipeline-recovery bias” and SNR_real inferences.
Required fix: Add a second MC suite that draws CMB realizations (E/B with a ΛCDM spectrum) in addition to instrument noise, with the same mask/beam/binning. Report the bias and scatter with and without CMB variance and carry forward the larger of the two as the calibration floor (or add it in quadrature).

P1B-META-E4
Severity: MAJOR
Section/page: Sec. IV (p. 5–6)
Why others missed it: Estimator-formula omissions were noted, but no one called out the cross-spectra vs auto-spectra issue that affects noise bias.
Problem (quote and analysis): The methods state “Spectra are band-power-binned…” but never specify whether EB bandpowers are built from cross-spectra between independent splits (detset/half-mission) or from auto-spectra. For EB-based rotation estimators, auto-spectra can carry noise–systematics couplings that are not removed by purification; standard practice is to form cross-spectra to avoid noise bias. Because the paper’s MC varies only noise on a single sky (see E3), noise-bias cancellation cannot be validated without explicit split-crossing.
Required fix: Specify whether the EB spectra used in the β fit are cross-spectra between independent splits; if not, justify the auto-spectra choice and show with MC that any noise bias is negligible compared to the 0.032–0.040° bias floor. Preferably, re-run with split cross-spectra and update the calibration.

P1B-META-M5
Severity: MAJOR
Section/page: Sec. IV (p. 5)
Why others missed it: One reviewer queried the beam model; none examined purification choices against constant-β physics.
Problem (quote and analysis): “We use NaMaster’s spin-2 B-mode purification (purify_b=True, purify_e=False).” Purification alters the E→B leakage structure by projecting out ambiguous B modes on a masked sky. A constant rotation induces a specific EB coupling that can be partially absorbed by the purification operator if not calibrated. No test is shown that the choice purify_b=True, purify_e=False leaves the EB slope for a constant β invariant to better than the quoted 0.032–0.040° bias.
Required fix: Provide a calibration test toggling purify_b/e in the MC (purify_b off/on; optionally purify_e on) and quantify the induced change in β̂ and its bias. Carry the worst-case difference as an additional systematic or adopt the configuration that demonstrably minimizes bias and variance for constant β.

P1B-META-M6
Severity: MAJOR
Section/page: Sec. IV (p. 5)
Why others missed it: A reviewer noted general beam-model issues; none assessed resolution/Nyquist consistency.
Problem (quote and analysis): “We degrade to Nside = 512 … bin from ℓmin = 30 to ℓmax = 1024.” ℓmax=1024 sits exactly at the 2×Nside Nyquist boundary for HEALPix. With a 5′ beam and 512-pixelization (~6.9′), mode-coupling near ℓ~1000 is sensitive to both the exact pixel/beam transfer and apodization. Using ℓmax right at the pixel Nyquist without a safety margin (e.g., ℓmax ≤ 1.5 Nside) invites aliasing and window-function mis-modeling, which can leak into EB and bias β̂ at the few×10⁻² deg level—comparable to the quoted bias floor.
Required fix: Repeat the MC with a conservative ℓmax cut (e.g., 768) and/or Nside=1024 and show β̂ stability within ±0.01° across these choices. Alternatively, adopt a documented transfer-function model (map-specific effective beam+pixel) and present a stability plot justifying ℓmax=1024 at Nside=512.

P1B-META-M7
Severity: MAJOR
Section/page: Sec. VI (p. 7–8) and Appendix C (p. 9–10)
Why others missed it: Reviewers discussed parameter ranges and couplings, but not the ODE-integration protocol itself.
Problem (quote and analysis): The ALP evolution is summarized as “Numerical integration of ϕ¨+3Hϕ˙+m²fa sin(ϕ/fa)=0 in a ΛCDM background yields ∆ϕ/fa ≈ …” with no details on initial redshift, stopping criteria, timestep control, treatment of the transition between radiation and matter domination, or the exact H(z) implementation. Because the quoted ∆ϕ/fa range [0.2, 1.1] drives Caγ requirements by a factor ≥5, the integration protocol is load-bearing. Small integration/initialization differences (e.g., starting after φ has begun to roll vs while still Hubble-frozen) can shift ∆ϕ/fa by O(10–30)%.
Required fix: Add a short methods box (or appendix) specifying: initial redshift and θi definition epoch, ODE integrator and tolerances, background H(z) source (analytic ΛCDM vs sampled posterior), and when ∆ϕ is evaluated (from recombination to today or earlier). Provide a grid/table confirming that ∆ϕ/fa is numerically stable to better than ±10% over these choices.

P1B-META-m8
Severity: MINOR
Section/page: Sec. IV (p. 5)
Why others missed it: Focus was on noise level and beam; this is a finer pixel/beam consistency point.
Problem (quote and analysis): “Planck-2018 effective Gaussian beam (5′ FWHM at 143 GHz); we degrade to Nside=512 and apply the corresponding pixel window function. NaMaster’s NmtField is initialized with beam=bℓ^Planck wℓ^pix.” If the Commander (or SMICA) product is already delivered at a common resolution/transfer, layering a single-channel 5′ Gaussian on top of a degraded Nside pixel window can double-count smoothing or mis-model the effective transfer. This is distinct from the general “beam model” concern: the combination “component-separated common beam + ad hoc 5′ + HEALPix wℓ” needs a transfer-function audit.
Required fix: Either use the published effective transfer function for the chosen component-separated map (preferred) or document that replacing the single 5′ Gaussian with the official transfer modifies β̂ by <0.01°. Include a one-line test/plot.

P1B-META-m9
Severity: MINOR
Section/page: Sec. VI, Eq. (4) (p. 7)
Why others missed it: One reviewer noted the missing “σ,” but not the pairing choice.
Problem (quote and analysis): The inverse-variance combination uses Planck NPIPE-only (0.30° ± 0.11°) with ACT DR6 (0.215° ± 0.074°). Given the narrative elsewhere stresses the WMAP+Planck joint result (3.6σ) to account for shared calibration systematics, a fair auxiliary “two-experiment” combination would be WMAP+Planck joint with ACT, not Planck-only with ACT. Using Planck-only plus ACT yields a different baseline covariance structure and may be perceived as cherry-picked, even with the “auxiliary” caveat.
Required fix: If retaining this auxiliary check, either (a) combine the joint WMAP+Planck result with ACT under an explicit, documented correlation model, or (b) drop the display equation and keep the qualitative statement that naive uncorrelated combinations can overstate significance.

P1B-META-N10
Severity: NIT
Section/page: Sec. IV (p. 5); throughout
Why others missed it: It’s a small notation issue overshadowed by larger concerns.
Problem (quote and analysis): The text alternates between symbols β̂ (estimator mean) and βinj (injected angle) but sometimes uses β̂ where βinj is intended in defining SNRSE, and vice versa (“SNRSE ≡ β/ˆ SE(β̂)”). This makes it hard to tell whether bias and SNR are referenced to the injected value or to the recovered sample mean.
Required fix: Standardize notation: define βinj, β̂ (per realization), and 〈β̂〉 (MC mean), and write SNRSE = 〈β̂〉 / SE(〈β̂〉), SNRreal = βinj / SD(β̂). Use these consistently in text and captions.

Meta-review recommendation
REJECT

Given the union of all six reviews (the five prior plus this meta-review), there are multiple independent, load-bearing blockers: (i) numerically incorrect wpivot decorrelation and σ propagation; (ii) inconsistent dataset/likelihood labeling and, importantly, mixed-release Planck likelihood usage without justification; (iii) missing estimator/likelihood specification for the EB analysis; (iv) unverifiable/future-dated references; (v) lack of robust model-comparison metrics for the w0wa claim; (vi) pipeline-calibration MC that omits CMB sample variance and does not specify cross-spectra; (vii) parameter-count inconsistencies; and (viii) several figure/caption contradictions. My confidence that the paper, as written, would survive external (non-bigbounce) peer review is low: ≥8 essential/major blockers would need substantial re-analysis and rewrite, including re-running chains with consistent likelihoods, adding missing methodological detail, and removing or relocating out-of-scope claims.