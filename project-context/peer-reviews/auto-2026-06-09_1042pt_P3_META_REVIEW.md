# P3 auto-2026-06-09_1042pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 551.1s

---

Meta-referee report — blind-spot findings not caught by the 5 prior reviews

P3-META-E1
- Severity: ESSENTIAL
- Section + page: §II.C GPU Inference Pipeline, p. 3
- Why missed: Reviewers focused on methodology and arithmetic; none audited the hardware spec itself.
- Specific problem (quote): “All inference was performed on a single NVIDIA H200 GPU pod with 80 GB of HBM3e memory.”
- Required fix: Correct the hardware description. As of 2025–2026, NVIDIA H200 SKUs ship with 141 GB HBM3e; 80 GB is an H100 configuration. State the exact GPU model and memory (e.g., “H100 80 GB” or “H200 141 GB”), or provide vendor documentation for an 80 GB H200 if such a SKU exists. This matters for reproducibility and for the plausibility of the stated throughput numbers.

P3-META-E2
- Severity: ESSENTIAL
- Section + page: §III.F Planck CMB, p. 7
- Why missed: Other reviews checked the Fisher math and training times; none reconciled the global S-definition against the Planck score range.
- Specific problem (quote): “Top-200 native anomaly patches (score range [0.558, 0.621]) form the catalog’s Planck CMB tier.” Earlier (§II.B, Eq. 2) the paper states “Throughout this paper, ‘S’ refers without exception to the per-survey standardized (‘z-scored’) reconstruction residual…”
- Required fix: Either (a) confirm these Planck “scores” are not S as defined in Eq. (2) and rename them (e.g., raw MSE), or (b) if they are z-scores S, explain how a top-1% selection yields S ≈ 0.56 when, by construction, a normal z-score’s top 1% is ~2.33. Provide μval, σval for the Planck model and show the score distribution to resolve this inconsistency.

P3-META-E3
- Severity: ESSENTIAL
- Section + page: §IV.D Planck × ACT Cross-Correlation: Null Result, p. 10
- Why missed: One referee flagged lack of a quantitative statistic and another the reliance on quarantined ACT, but none identified the footprint-conditioning problem.
- Specific problem (quote): “Planck anomalies concentrate at the south ecliptic pole… while ACT anomalies concentrate along the Galactic plane… This null result demonstrates that CMB patch anomalies… are dominated by survey-specific systematics.” The analysis appears not to restrict to the intersection of the two surveys’ usable sky, making the null result tautological.
- Required fix: Recompute the cross-correlation strictly on the common sky mask (Planck |b|≥20° and ACT DR6 footprint with its standard masks), and report the estimator, uncertainties, and p-value. If intersection masking eliminates most patches, state that the test is power-limited; otherwise remove the claim or move it to an appendix as a qualitative observation.

P3-META-E4
- Severity: ESSENTIAL
- Section + page: §II.D Step 4 and §III.H NEOWISE, pp. 4 and 9; Fig. 7 p. 13
- Why missed: Prior reviews critiqued injection–recovery design in general but did not catch the conflation here.
- Specific problem (quote): “NEOWISE ecliptic-pole mask (|becl| < 80°) retains 419/436 (96.1%)… Mask injection-recovery: 1000/1000 = 100% (gate PASS).” This “injection-recovery” is measuring whether a geometric mask can be re-applied, not the anomaly detector’s sensitivity; reporting it alongside algorithmic sensitivity gates is invalid.
- Required fix: Remove the NEOWISE “mask injection-recovery” from the sensitivity gate summary, or clearly separate it under “geometric selection checks.” Provide an actual algorithmic injection–recovery test in feature space for NEOWISE, or refrain from marking it PASS for the 5σ gate.

P3-META-E5
- Severity: ESSENTIAL
- Section + page: §III.E eROSITA DR1, p. 7
- Why missed: Other reviews focused on validation rates and overlaps; none checked institutional attributions.
- Specific problem (quote): “(western Galactic hemisphere only; eastern half under Rosatom proprietary control).” The Russian partner is Roscosmos (or IKI/RAS), not Rosatom.
- Required fix: Correct the institutional attribution and data-rights wording (e.g., “the eROSITA Russian (RU) half remains proprietary to IKI/Roscosmos at the time of writing”); cite the official eROSITA/RU data policy.

P3-META-M1
- Severity: MAJOR
- Section + page: §III.E and Table I footnote § (and §VI.D (f)), pp. 7, 6, 13
- Why missed: Reviewers challenged the overlap metric but not the null model.
- Specific problem (quote): “284 of 298 canonical-S top-298 sources (95.3%) are also in the IsolationForest top-9,303… enrichment 95.3× over random-independence; hypergeometric two-sided p ≈ 0.” The independence null is inappropriate because the IF is trained on the 16-d BigAE latent features; the detectors are strongly dependent by design.
- Required fix: Drop claims of “95.3× enrichment over random-independence” and the associated p-value. If you wish to quantify agreement, report symmetric set-similarity metrics (e.g., Jaccard) and/or train IF on an independent feature space; otherwise present the 284/298 overlap descriptively without implying statistical significance under independence.

P3-META-M2
- Severity: MAJOR
- Section + page: §V.a–b, p. 11–12
- Why missed: Other reviews focused on F0 and propagation; none noted that α itself is never formally defined.
- Specific problem (quote): “A Landy–Szalay… yields the bias ratio b ≡ bQSO cand/bfull anomaly… We adopt αjk = 0.19 ± 0.65… Under the Fisher-positivity-respecting form 1/σ(fNL)^2 = F0 + c α^2…” The manuscript never explicitly defines α as a function of the measured ratio b (e.g., α ≡ b − 1), nor shows how c was calibrated from the fiducial Fisher setup given that α comes from a two-sample angular measurement.
- Required fix: Provide an explicit definition of α and the mapping from the Landy–Szalay measurement to the Fisher control parameter (e.g., α ≡ b − 1, with b estimated as …). Show how c is obtained under that definition from the baseline Fisher matrices. Without this, the end-to-end chain (measurement → α → σ forecast) is not reproducible.

P3-META-M3
- Severity: MAJOR
- Section + page: §III.B Confirmed High-z QSO Candidates, p. 5
- Why missed: Reviewers commented on missing tables but not on the selection physics.
- Specific problem (quote): “Z-arm dominated anomaly scores, meaning rZ > rB and rZ > rR… mean Z-arm sub-score ⟨rZ⟩ = 3.9… all twelve pass the S > 5 catalog cut.” The per-arm residuals rB,R,Z are used to select high-z candidates, but DESI arm-throughput/SNR differences and the autoencoder’s spectral weighting can bias rZ upwards independently of astrophysical redshift effects.
- Required fix: Calibrate rB,R,Z against arm-specific SNR/throughput (e.g., normalize residuals per arm by that arm’s validation variance) and re-validate that the “Z-dominant” selection is not an instrumental or modeling bias. Document the normalization used for rB,R,Z in the main text.

P3-META-M4
- Severity: MAJOR
- Section + page: §IV.C Cross-Survey Matches, p. 10
- Why missed: Others noted radius choice but not epoch propagation consequences at scale.
- Specific problem (quote): “Gaia DR3 is sub-0.1″… and additionally carries proper-motion solutions that we do not propagate to the survey epochs… a uniform 5″ radius is therefore strict for Gaia…” Not propagating Gaia positions to the spectroscopic epochs systematically reduces true associations for high proper-motion sources and biases the 637 “multi-survey coincidences” downward in a way that depends on sky region and stellar type.
- Required fix: Quantify the loss rate from ignoring proper motion (e.g., by re-matching a bright, high-μ Gaia subsample with epoch propagation) and bracket the possible undercount. Alternatively, restrict the coincidences analysis to extragalactic/low-μ subsets where the effect is negligible.

P3-META-M5
- Severity: MAJOR
- Section + page: Abstract and §III–IV totals, pp. 1, 6–10
- Why missed: Prior reviews tackled percentile non-comparability but not this aggregate-rate interpretation.
- Specific problem (quote): “Path-C unique (primary) … 378,280 … Rate 1.01%.” Several contributing surveys (Planck, Gaia, NEOWISE) use fixed top-1% selections by construction; aggregating them into a catalog-wide “1.01% rate” suggests an empirical anomaly frequency when a nontrivial fraction of that rate is predefined by design.
- Required fix: Remove the catalog-wide “Rate 1.01%” or qualify it explicitly as a bookkeeping fraction driven in part by fixed-count selections. Present empirical rates only for surveys where a data-driven threshold is used.

P3-META-m1
- Severity: MINOR
- Section + page: Appendix E, first line and Eq. (E1), pp. 16–17
- Why missed: One referee flagged dimensional inconsistency; none noted symbol definition.
- Specific problem (quote): “log10 ρi = …” The symbol ρi is introduced without definition (PSD? power per frequency bin?); units and normalization are not specified anywhere in the appendix.
- Required fix: Define ρi explicitly (e.g., “the model power spectral density in bin i, with units of …”), including the normalization convention and units used for fi and Tobs (e.g., years), or replace with a standard PTA likelihood reference and equation.

P3-META-m2
- Severity: MINOR
- Section + page: Appendix D (UMAP/HDBSCAN), p. 15
- Why missed: Reviewers questioned cluster counts but not the precision claim.
- Specific problem (quote): “UMAP stability: trustworthiness 0.9797 ± 5×10−5 across 20 independent seeds.” Reporting ±5×10−5 as a seed-to-seed empirical uncertainty for UMAP trustworthiness is unrealistically precise for a stochastic embedding of 195k outliers and suggests underestimation of run-to-run variability.
- Required fix: Report the empirical standard deviation across seeds with appropriate significant figures (likely at the 1e−3–1e−2 level) and describe the sampling procedure (same hyperparameters, same random initializations, etc.). Alternatively, provide the per-seed values in supplemental material.

P3-META-m3
- Severity: MINOR
- Section + page: §IV.A (false-match rates), p. 9
- Why missed: Others checked arithmetic; none checked provenance of the surface density.
- Specific problem (quote): “For SIMBAD at 5″ (nSIMBAD ≈ 3.0 × 10−5 arcsec−2), Pfalse ≈ 2.4 × 10−3 per source…” The SIMBAD surface density nSIMBAD is asserted without derivation or citation; its value sets the false-match estimate.
- Required fix: Provide a brief derivation or reference for nSIMBAD (e.g., measured on the same sky mask), and include uncertainty. If nSIMBAD varies strongly across the footprint, present a range or a Monte Carlo false-match estimate instead of a single number.

P3-META-m4
- Severity: MINOR
- Section + page: §III.C Table II note vs. §III.A text, pp. 6 and 5
- Why missed: Others caught SIMBAD rate inconsistencies elsewhere but not this cross-survey tension.
- Specific problem (quote): Table II note ties “Uncategorized 52.7%” to SIMBAD entries lacking type, implying >40k SDSS matches; elsewhere SDSS SIMBAD-unmatched is given as 90%. While those blocks are about different surveys (SDSS vs DESI), the proximity of claims invites confusion.
- Required fix: Clarify in Table II that “Uncategorized” refers to the internal emission-line taxonomy and is not a SIMBAD classification; remove the SIMBAD wording from that note, or present SDSS SIMBAD-match counts alongside the taxonomy to avoid ambiguity.

Meta-review recommendation
REJECT

Given the union of all six reviews, there are multiple essential errors and cross-consistency failures: hardware misreporting (H200 80 GB), a score-definition contradiction for Planck (top 1% with S ~ 0.56), an invalid cross-correlation test on non-overlapping sky, a conflation of geometric masking with algorithmic sensitivity (NEOWISE 100% “injection-recovery”), an improper independence null in the eROSITA overlap, and a missing formal definition linking the measured bias ratio to the Fisher control parameter α. In addition, a factual institutional error (Rosatom vs Roscosmos), several presentation inconsistencies, and data-access issues remain. My confidence that the paper would survive external (non–bigbounce) peer review is low: at least 8–10 blockers (including several ESSENTIAL items) require substantial reanalysis and rewriting, beyond editorial fixes.