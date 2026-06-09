# P1B auto-2026-06-08_1819pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 255.1s

---

# META-REVIEW: P1B (Technical Verification Companion)

The five prior reviewers correctly identified the headline pathologies (scope mismatch, σ_wpivot algebra, sample-count gymnastics, future-dated references, ALP fine-tuning, internal date stamps). Below are issues that survive the union of those reviews.

---

## ESSENTIAL

### P1B-META-E1 — The ALP-MCMC likelihood stack and the "headline observation" use *different* datasets, never reconciled
**Section:** Appendix C (likelihood stack) vs §VI "Headline observational constraint" vs abstract footnote `a`, pp. 1, 7, 9.
**Why missed:** Reviewer 1 (Brutal) noted the PR3-vs-PR4 ambiguity, but missed that the *experiment combination itself* changes (WMAP9 → ACT DR6). Reviewer 5 (Citations) flagged the references but not the swap.
**Problem:** The abstract footnote and §VI both anchor the comparison to "Eskilt & Komatsu joint **WMAP9 + Planck PR3**" giving 0.342° ± 0.094° (3.6σ). But Appendix C states the actual ALP-MCMC uses "Planck PR4 + **ACT DR6** EB-spectrum likelihoods." This is not a PR3↔PR4 calibration update; it is a swap of WMAP9 for ACT DR6 — two different experiments with different sky coverage, noise, and EB systematics. The "βALP = 0.336° vs βobs = 0.342° at <1σ" agreement claim therefore compares a model fit on (Planck PR4 + ACT) to an observational headline derived from (Planck PR3 + WMAP9). The two are not the same target.
**Required fix:** Either (a) rerun the ALP-MCMC on the WMAP9 + Planck PR3 likelihood that produced the 3.6σ headline, or (b) re-derive a headline β value from PR4 + ACT DR6 and quote *that* as the comparison target, or (c) drop the abstract's "consistent with the published joint WMAP+Planck value" claim entirely.

### P1B-META-E2 — Two different "published observation" reference values are used in different sections without reconciliation
**Section:** §IV intro (p. 5) vs Eq. (4) §VI (p. 7) vs §VI headline (p. 7) vs abstract.
**Why missed:** All five reviewers treated the birefringence reference value as a single number; none constructed the cross-section reference-value audit.
**Problem:** The paper invokes *three different* reference β values from the literature, in three different sections, none clearly the privileged comparator:
- §IV intro: "β = 0.30° ± 0.11° (Planck NPIPE) and β = 0.215° ± 0.074° (ACT DR6)"
- §VI Eq. (4): "β_combined = 0.241° ± 0.061°" (their own inverse-variance combination, 3.9σ)
- §VI Headline / Abstract: "β = 0.342° ± 0.094° (3.6σ)" (Eskilt-Komatsu)

The inverse-variance combination 0.241° and the Eskilt-Komatsu joint 0.342° differ by 1.0σ — a real ~30% discrepancy in inferred central value driven by the choice of which Planck-vintage dataset is combined with which auxiliary experiment. The paper acknowledges that Eq. (4) "neglects shared calibration systematics" but does not explain why a ~1σ shift to higher β results when those systematics are included properly in the joint analysis. A non-specialist reading the abstract would not know that the model has been compared to a value that is 1σ above the simplest inverse-variance combination of the two individual measurements cited in §IV.
**Required fix:** Pick one observational reference value, justify the choice, and remove or footnote-only the others.

### P1B-META-E3 — The pseudo-Cℓ pipeline never explains how β is extracted from EB
**Section:** §IV "Data Methods: CMB E-B Analysis" pp. 5–6.
**Why missed:** All five reviewers focused on bias size, SNR semantics, and Commander-map suitability; none asked the more basic question of what estimator turns EB band-powers into β̂.
**Problem:** Section IV describes the mask (fsky = 0.32, C2 apodization at 2°), beam (5' FWHM), purification (purify_b=True), mode-coupling matrix (NmtWorkspace.compute_coupling_matrix), binning (Δℓ = 20, ℓ ∈ [30, 1024]), and noise level (∆_P = 10 µK·arcmin). The recovery quantity β̂ then appears as if by magic in Eq. (1): "β̂_NaMaster = 0.238° (500-MC sample mean of β̂)." There is no specification of the estimator — is it a template fit to EB ∝ sin(4β)·(C_ℓ^EE − C_ℓ^BB), is it the Minami-Komatsu likelihood, is it a simple χ²-minimization over band powers, is the calibration angle α profile-marginalized? Without this, the recovery cannot be reproduced, and the comparison to published Planck/ACT pipelines is impossible.
**Required fix:** State the explicit β-estimator (likelihood form, marginalized parameters, ℓ-range cuts, miscalibration treatment) in §IV before reporting Eq. (1).

---

## MAJOR

### P1B-META-M1 — The Monte Carlo noise level corresponds to a per-realization β-precision *worse* than the published single-sky measurement
**Section:** §IV, footnote 3, p. 6.
**Why missed:** Reviewer 1 correctly diagnosed that SNR_SE ≠ SNR_real, but none of the reviewers ran the back-of-envelope on the actual implied per-realization σ_β̂.
**Problem:** From footnote 3: SNR_SE = β̂√N / σ_β̂ with N = 500 and SNR_SE = 20.32 at β̂ = 0.238°. Solving: σ_β̂ = β̂√N / SNR_SE = 0.238° × √500 / 20.32 ≈ **0.262° per realization**. But the published Planck NPIPE result is σ = 0.11° on a single real sky. The MC pipeline at ACT-noise level (10 µK·arcmin) achieves a per-realization β-precision that is *2.4× worse* than the real Planck measurement at Planck-noise level (~40 µK·arcmin polarization). This indicates either (i) the bandpower coverage / estimator is much less efficient than the published pipeline, or (ii) the noise injection is mis-scaled, or (iii) the SNR_SE quoted is not what the formula in footnote 3 implies. Either way, the pipeline cannot be claimed to "recover" the published sensitivity.
**Required fix:** Quote σ_β̂ explicitly per realization, compare to the published Planck/ACT per-sky uncertainty, and explain the gap.

### P1B-META-M2 — "Planck Commander map" at fsky = 0.32 with ACT noise is a non-physical hybrid configuration
**Section:** Abstract, §IV.
**Why missed:** All five reviewers accepted the experimental setup at face value.
**Problem:** Commander is a Planck component-separated, foreground-cleaned product designed to be used over the *high-Galactic-latitude full sky* (typically fsky ≈ 0.7–0.8). Masking it to fsky = 0.32 throws away ~60% of the Commander signal-to-noise. Simultaneously injecting ACT noise (10 µK·arcmin) onto a Planck-derived map produces a hybrid that corresponds to no published experiment: it is neither Planck (which uses ~50 µK·arcmin polarization noise) nor ACT (which has its own component-separated map). The "MC validation" is therefore validating against a self-defined hybrid noise + mask configuration whose connection to either published measurement is unstated.
**Required fix:** Either run the MC at Planck noise level with the Commander-natural mask, or use the ACT DR6 map directly with ACT noise; do not mix.

### P1B-META-M3 — βfree "model-independent" terminology is incorrect
**Section:** §VI ALP-MCMC paragraph, p. 8; Appendix C.
**Why missed:** All reviewers took the "model-independent" label at face value.
**Problem:** βfree = 0.344° ± 0.096° is described as a "model-independent MCMC fit to the Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter." But Appendix C states the βfree fit aggregates "9,720 accepted samples across the 3 ALP-MCMC configurations" (C_aγ ∈ {4, 8, 12} held fixed in each). Fixing C_aγ at three discrete benchmark values and floating β within each is not model-independent — it is a specific ALP class with one nuisance parameter swept. A truly model-independent β extraction would have β floating with no ALP assumption (i.e., directly from the EB likelihood as Minami-Komatsu do). The terminology overstates the result's generality.
**Required fix:** Rename "βfree" to "βALP free amplitude" and clarify that the fit is internal to the ALP class.

### P1B-META-M4 — DESI DR2 χ² = 10.6 ± 1.8 is implausibly low for the DR2 data volume
**Section:** Table II, p. 4.
**Why missed:** All five reviewers focused on the w0wa headline numbers, none on the goodness-of-fit decomposition.
**Problem:** DESI DR2 BAO has ~14 data points (DM/rd, DH/rd, DV/rd across 7+ redshift bins). For a global fit successfully matching the BAO data, χ² ≈ 10–14 would be expected with ~12 dof after fitting cosmology, giving χ²/dof ~ 1. A χ² of 10.6 is low but not crazy — *however*, the ±1.8 quoted as the "posterior variance of χ²" suggests this is the chain spread of the goodness-of-fit, not the goodness-of-fit-with-uncertainty. The two are conceptually distinct and conflating them in a table caption labeled "Goodness-of-fit decomposition" misleads. More critically: DESI DR2 is widely known to pull w0wa specifically *because* its BAO constraint deviates from the Planck-inferred sound horizon at the ~2σ level; a χ² of 10.6 with the quintom fit suggests this deviation is fully absorbed by w0wa — exactly the headline DESI result. The paper does not acknowledge that the low χ²_BAO is *because* DESI BAO is what's driving the w0wa departure, not an independent goodness-of-fit measure.
**Required fix:** Discuss the DESI BAO χ² in context of the known w0wa pull, and report dof and reduced χ² per channel.

### P1B-META-M5 — Reference [17] is the Planck *2018* (PR3) cosmological parameters paper, not the NPIPE reference
**Section:** §V A, p. 6; reference [17].
**Why missed:** Reviewer 5 noted reference errors broadly but not this specific misattribution.
**Problem:** §V A states "We analyze four dataset combinations: (1) Planck 2018 NPIPE [17]" — but ref. [17] is "Planck Collaboration, Planck 2018 results. VI. Cosmological parameters, A&A 641, A6 (2020), arXiv:1807.06209" which is the **PR3** (2018) cosmological parameters paper. NPIPE is the Planck PR4 reprocessing (Akrami et al. 2020, A&A 643, A42; arXiv:2007.04997), a completely different reference. The dataset label "Planck 2018 NPIPE" with citation [17] is contradictory in the most basic way: PR3 ≠ NPIPE. The abstract advertises the data as "Planck NPIPE CamSpec TTTEEE" — implying PR4 — but the cited dataset is PR3. Which was actually used?
**Required fix:** Cite the correct NPIPE paper (Akrami et al. 2020 or the NPIPE CamSpec likelihood paper, Rosenberg et al. 2022) and confirm which Planck vintage was used in the chains.

---

## MINOR

### P1B-META-m1 — "WP4 reheating" and "WP4 decay" bands in Fig. 2 are never defined
**Section:** Figure 2a legend, p. 5.
**Why missed:** All reviewers focused on the posterior comparison, none on the prior-band labels.
**Problem:** The figure shows two reference bands labeled "WP4 reheating [0.05, 0.40]" and "WP4 decay [0.01, 0.25]" — these "WP4" predictions appear nowhere in the paper text. The reader cannot interpret whether the posteriors are excluding, accommodating, or null relative to these bands without knowing what WP4 is (presumably "Work Package 4" of a project, but uncited).
**Required fix:** Define WP4 in the figure caption and cite the source.

### P1B-META-m2 — Age of universe = 13.763 ± 0.019 Gyr in the quintom fit is not discussed
**Section:** Table II, p. 4.
**Why missed:** Reviewers focused on w0, wa, H0 only.
**Problem:** The Planck-2018 ΛCDM age is 13.797 ± 0.023 Gyr. The Table II quintom fit returns 13.763 ± 0.019 Gyr — a **1.1σ shift to a younger universe** that is a direct consequence of the phantom-crossing w0wa. This is a physically interpretable signature of the quintom model that affects the recombination-to-now integral; it deserves at least a sentence noting that the quintom posterior implies the universe is ~30 Myr younger than ΛCDM and explaining why.
**Required fix:** Add one sentence interpreting the age shift as a consequence of the w0wa posterior.

### P1B-META-m3 — Fig. 3 axis range vs body text
**Section:** Figure 3, p. 6.
**Why missed:** All reviewers commented on figure content but not the axis-text contradiction.
**Problem:** Figure 3 legend includes "Planck+ACT (Eskilt): 0.34 ± 0.09°" — but the Eskilt-Komatsu joint analysis at 0.342° ± 0.094° uses **Planck + WMAP9**, not Planck + ACT (per abstract footnote a's own disambiguation). The Figure 3 legend therefore mis-attributes the reference value to the wrong experiment combination.
**Required fix:** Correct the Figure 3 legend to "Planck PR3 + WMAP9 (Eskilt+Komatsu)".

### P1B-META-m4 — The MCMC engine for the ALP-MCMC reaches R̂-1 < 0.01 in only 3,240 samples per configuration
**Section:** Appendix C.
**Why missed:** Reviewers checked sample-count consistency but not the per-configuration MCMC convergence plausibility.
**Problem:** Appendix C says "convergence threshold R̂ − 1 < 0.01 across all 3 configurations (achieved at N_tot = 9,720 accepted samples post burn-in)." That's 3,240 samples per (C_aγ = 4, 8, 12) configuration. For a 2-D posterior (θ_i, m/H_0) in Cobaya with Metropolis-Hastings, R̂ − 1 < 0.01 typically requires Ω(10⁴) samples per chain across ≥ 4 chains. 3,240 samples sounds like a single chain that has not been properly Gelman-Rubin tested across multiple independent chains. The "R̂ − 1 < 0.01" claim should be auditable.
**Required fix:** State the number of independent chains, their per-chain length, and the actual R̂ − 1 value achieved.

---

## NIT

### P1B-META-N1 — "Eq. 1–3" in Fig. 3 caption refers to equations not present
**Section:** Figure 3 caption.
**Problem:** Caption ends "this is the NaMaster systematic floor adopted in Eq. 1–3." But Eq. 1 is the recovery value (β̂ = 0.238°), Eq. 2 is the ALP field displacement, and Eq. 3 is the birefringence formula. None of those *adopts* the NaMaster systematic floor; it is invoked only in surrounding text. The cross-reference is incorrect.
**Required fix:** Strike or correct the "adopted in Eq. 1–3" pointer.

### P1B-META-N2 — "Caγ" is sometimes "Cαγ" in formulas
**Section:** Eq. (3), §VI throughout.
**Problem:** Eq. (3) shows "α_EM × 8 / (4π)" without the C_aγ symbol; the surrounding prose uses C_aγ. Notational inconsistency that obscures whether the coupling constant is a fitted parameter or a symbol.
**Required fix:** Standardize.

---

## Meta-review recommendation

**REJECT**

Across all six reviews, the blocker count is large and structurally diverse: (1) the title-vs-content scope mismatch (R1, R3, R4); (2) a basic σ_wpivot arithmetic error implying |ρ| > 1 (R1 P1B-E9); (3) an entire unannounced DESI w0wa analysis carrying the strongest statistical claims in the paper (R1, R3, R5); (4) future-dated and fabricated references including the Planck-NPIPE reference [17] being the PR3 paper (R5, meta-M5); (5) sample-count, version, date, and Cobaya-version inconsistencies (R1, R3, R5); (6) editorial annotations leaking into the bibliography (R1 P1B-E10); (7) a likelihood-stack swap between the ALP-MCMC and the "observed" headline (meta-E1); (8) two mutually inconsistent reference β-values used in different sections (meta-E2); (9) no description of how β is actually estimated from EB band-powers (meta-E3); (10) implied per-realization σ_β̂ inconsistent with the experimental setup (meta-M1); (11) the spectator/fine-tuning self-contradiction (R1, R4, R5); (12) deferred Bayes factors with headline "+4.3σ" language for an unsampled point (R1, R4). Confidence that the paper would survive external PRD peer review: ~3%. Even after correcting the bibliographic and arithmetic errors, the structural issue — that the "Technical Verification Companion" verifies nothing about the ECH program by its author's own admission — is unfixable within revision. The companion-paper concept itself requires reformulation; folding the genuinely usable content (Table I posteriors, NaMaster pipeline notes) into Paper I(a) as an appendix is the only realistic path to publication.