# P1B auto-2026-06-05_1517pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 301.4s

---

Meta-referee report — new issues not caught by the five referees

P1B-META-E1
- Severity: ESSENTIAL
- Location: Sec. III, p. 2–3; Sec. V.A, p. 6; Ref. [17]
- Why missed: Reviewers noted “dataset/likelihood inconsistencies” in general, but none identified the specific cross-release mixing.
- Problem: The paper mixes Planck PR4/NPIPE high-ℓ CamSpec with PR3 low-ℓ “lowl.TT/lowl.EE” in the same chains: “Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing” while citing “Planck 2018 results” [17] for low-ℓ. This is not a supported release pairing; PR4/NPIPE low-ℓ likelihoods (and calibration conventions) differ from PR3. Cross-release mixing can bias both parameter means and uncertainties because calibration and covariance models are not harmonized across PR3 and PR4.
- Required fix: Use a self-consistent Planck likelihood stack (either PR3-only or PR4/NPIPE-only, including the appropriate low-ℓ likelihood, e.g., SimAll/NPIPE), or justify and validate the cross-release combination with explicit tests showing negligible impact (and cite the correct low-ℓ likelihood product). Update all citations accordingly.

P1B-META-E2
- Severity: ESSENTIAL
- Location: Sec. VI, p. 7 (“Convergence: R̂ − 1 < 0.01 for all runs”), Appendix C, p. 9 (ALP configurations and sample counts)
- Why missed: Others asked for ESS and details, but no one pointed out that R̂ is undefined with a single chain and the paper never states chain count for the ALP runs.
- Problem: The ALP MCMC reports “R̂ − 1 < 0.01 for all runs” with only “3 configurations, 9,720 total accepted samples (3,240 per configuration)” and no statement of number of chains per configuration. If each configuration used a single chain, R̂ is undefined; if multiple chains were used, the chain count and per-chain lengths are not given. With as few as ~3,240 accepted samples per configuration, claiming R̂ < 0.01 across parameters is not credible without multi-chain details.
- Required fix: Report the number of parallel chains per configuration, per-chain lengths, and min ESS. If only a single chain was run per configuration, remove R̂ claims and rerun with ≥4 parallel chains to substantiate convergence diagnostics.

P1B-META-M1
- Severity: MAJOR
- Location: Table I footnote a, p. 3 (list of nuisance parameters)
- Why missed: Reviewers flagged general reproducibility issues but not the specific mismatch between CamSpec and the nuisance list.
- Problem: The nuisance list includes “Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE,” which match Plik/PR3-style parameters more than CamSpec/NPIPE. CamSpec uses a different calibration scheme; “Aplanck” is not a CamSpec nuisance parameter. This suggests either the wrong nuisance set is described or the likelihood named is not the one actually used.
- Required fix: Replace the nuisance list with the correct set for the stated CamSpec/NPIPE likelihood (or state you used Plik and update the text accordingly). Provide a table of all nuisance parameters with priors per likelihood.

P1B-META-E3
- Severity: ESSENTIAL
- Location: Sec. IV, “Foreground and noise model,” p. 5–6; “Independent verification,” p. 5–6
- Why missed: Others asked for σβ and estimator details but did not diagnose the fixed-sky Monte Carlo underestimating uncertainty.
- Problem: The 500 Monte Carlo runs add white noise realizations (ΔP = 10 μK·arcmin) to a single fixed Commander Q/U map and measure β recovery. Because the CMB sky (including lensing B and E cosmic variance) is held fixed across realizations, the ensemble σβ underestimates the true sampling uncertainty. This inflates quoted SNRs (20.3, 25.7) and biases any “systematic floor” inference from the ensemble mean.
- Required fix: Run full-sky Monte Carlos that vary the CMB realizations (including lensing B) and noise jointly, or explicitly state that the reported SNR excludes cosmic variance and is not an estimate of total uncertainty. Provide σβ from both fixed-sky and full-sky ensembles and base “systematic floor” claims on the appropriate measure.

P1B-META-M2
- Severity: MAJOR
- Location: Sec. IV, “Beam and pixel window,” p. 5
- Why missed: One reviewer queried beam appropriateness for Commander, but none caught the pixel-window deconvolution step omission.
- Problem: “We degrade to Nside=512 and apply the corresponding pixel window function.” When downgrading from Nside=2048 to Nside=512, one must deconvolve the 2048 pixel window before convolving the 512 pixel window (or ensure ud_grade handles both). As written, the analysis risks either double-suppressing small scales or omitting deconvolution of the original window, affecting recovered spectra and β bias.
- Required fix: Specify the exact downgrade procedure (e.g., healpy.ud_grade with X flags), state whether the Nside=2048 pixel window was deconvolved before applying the Nside=512 window, and re-run if needed to correct any transfer-function mismatch. Include a transfer-function validation plot.

P1B-META-M3
- Severity: MAJOR
- Location: Sec. IV, “Foreground and noise model,” p. 5; “Pipeline configuration,” p. 5
- Why missed: One reviewer noted vagueness of “SNR consistent with ACT-noise floor,” but not the inconsistent beam/noise pairing.
- Problem: The test uses Planck-like beam (5′ FWHM) while injecting ACT-like white noise (ΔP = 10 μK·arcmin). This hybrid pairing is unphysical for any single experiment and complicates interpretation of SNR (e.g., comparing to “ACT-noise floor”). It is not a controlled “worst case” because β SNR also depends on beam (E/B attenuation) not just noise.
- Required fix: Either (a) use a consistent instrument model (Planck-like beam with Planck-like noise; ACT-like beam with ACT-like noise) or (b) clearly justify the hybrid choice and remove claims that the SNR is “consistent with the ACT-noise floor.”

P1B-META-E4
- Severity: ESSENTIAL
- Location: Table II caption and body text, p. 4; Sec. V, p. 6
- Why missed: Reviewers criticized evidence omission and dataset labeling, but not the statistical independence of the SN datasets.
- Problem: The w0wa likelihood stack combines “DES-Y5 + Pantheon+” without mentioning any cross-covariance or overlap handling. These SNe samples are not statistically independent (overlapping calibration/standardization systematics; in some cases overlapping events across earlier DES releases). Combining them as independent likelihoods risks double-counting correlated information and artificially tightening posteriors (e.g., the exceptionally tight Age ±0.019 Gyr noted by another referee).
- Required fix: Document overlap and shared-systematic covariance between DES-Y5 and Pantheon+. Either supply the joint covariance and use a combined likelihood that accounts for correlations or remove one SN dataset to avoid double counting. Recompute the w0wa posteriors accordingly.

P1B-META-M4
- Severity: MAJOR
- Location: Sec. IV, “EB estimator,” implicit throughout pp. 5–6
- Why missed: Others asked for estimator details but not the small-angle linearization check.
- Problem: The β estimator implicitly relies on the small-angle expansion (EB ∝ 2β EE to leading order). At β ≈ 0.3°, the linear approximation is fine, but the paper neither states the estimator form nor verifies that any non-linear correction (O(β^3)) is negligible under masking and binning. Without this, the claimed “bias floor” could include unquantified estimator non-linearity.
- Required fix: State the explicit EB→β estimator (linear vs. iterative non-linear fit) and quantify the size of non-linear corrections at β ≈ 0.3° under your mask and binning (e.g., by injecting 0.5° and verifying linearity of recovery).

P1B-META-m1
- Severity: MINOR
- Location: Table II, p. 4 (“109As 2.087 ± 0.030”)
- Why missed: Others focused on larger issues; this is notation-level.
- Problem: The derived-parameter label “109As” is ambiguous (is it 10^9 As or a typographical error?). Standard practice is ln(10^10 As) or 10^9 As explicitly.
- Required fix: Clarify the parameter as either ln(10^10 As) or 10^9 As, and adjust the number accordingly to match the definition.

P1B-META-m2
- Severity: MINOR
- Location: Sec. IV, “Independent verification,” p. 5–6
- Why missed: Others challenged SNR but not the composition of the Monte Carlo distribution.
- Problem: The ensemble standard deviation used to form SNR appears to reflect noise-only dispersion around a fixed sky (see E3). If reported SNR is based on the standard error of the mean over 500 realizations rather than the per-realization σβ, it overstates the effective detection capability.
- Required fix: Report both the per-realization σβ and the standard error on the mean across realizations; make clear that any “systematic floor” is read from the ensemble mean while the “sensitivity” must use per-realization σβ.

P1B-META-m3
- Severity: MINOR
- Location: Sec. III, footnote a list of nuisances vs. Fig. 1 caption, pp. 3 & 5
- Why missed: Attention centered on chain counts.
- Problem: The figure caption references “Planck+BAO+SN+H0+S8” while the nuisance list in Table I footnote a is purely Planck and SN (no BAO/SH0ES-specific nuisance), suggesting either the caption is shorthand or the nuisance list is incomplete for the stated stack including H0 and S8.
- Required fix: Provide a complete nuisance-parameter table per dataset component (Planck high-ℓ, low-ℓ, lensing, BAO, SN, SH0ES/S8) and ensure captions match the actual likelihood components and nuisances used.

Meta-review recommendation
REJECT

Given the union of all six reviews, there are multiple essential blockers: (i) cross-release Planck likelihood mixing (PR3 low-ℓ with PR4/NPIPE high-ℓ), (ii) ALP MCMC convergence claims without documented multi-chain runs, (iii) likely underestimation of β uncertainty due to fixed-sky Monte Carlo, (iv) inconsistent nuisance parameterization for the stated Planck likelihood, and (v) potential double counting of supernova information (DES-Y5 + Pantheon+) without a joint covariance. These are in addition to the already-identified issues (scope misalignment, omissions of evidence metrics, dataset labeling errors, estimator opacity, and numerous internal inconsistencies). My confidence that the manuscript, in its current form, would not survive external (non–bigbounce) peer review is very high. Substantial methodological corrections, reproducibility clarifications, and restructuring would be required before reconsideration.