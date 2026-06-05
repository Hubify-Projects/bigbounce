# P3 R10v3 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K
**Wall time**: 239.3s

---

# Referee Report: "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies..."

**Reviewer:** Brutal-honesty PRD referee
**Manuscript:** 20 pages, submitted to Physical Review D

---

## Overall Assessment

This paper presents an autoencoder anomaly-detection sweep across seven archives and attempts to bolt three cosmology applications (multi-tracer fNL, NANOGrav spectral index, bounce cosmology consistency) onto a catalog whose own validation gates fail in half the surveys. The headline "378,280 unique anomalies" is arithmetic concatenation, not science; the cosmology claims are central-value forecasts consistent with null at <1σ but framed as positive results in the abstract; and the entire enterprise is unsuitable for **Physical Review D** in its current form. PRD is a physics journal — a catalog paper with three failed injection-recovery gates, a <1σ fNL "improvement," and a +1.13σ "consistency" with bounce cosmology is not a physics result. This belongs (heavily revised) in MNRAS or ApJS as a methods/catalog paper, **not** PRD.

I list findings below. There is no cap.

---

## ESSENTIAL findings (must fix before any acceptance)

### P3-E1: Abstract overclaims a positive cosmology result that is statistically null
**Abstract, p.1:** "An empirical Landy–Szalay bias measurement on the 5,384 QSO-candidate sample yields αjk = 0.19 ± 0.65 (< 1σ from null); inserting this into the Fisher-positivity-respecting form ... gives a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fNL)std = 8.98 single-tracer baseline)."

The 1σ envelope **upper end equals the single-tracer baseline (8.98)**. This means the measurement is *literally consistent with zero improvement*. Quoting "σ(fNL) = 8.14" as a central forecast in the abstract is misleading; the result is a **null measurement of bias enhancement** that does not constrain fNL beyond the single-tracer baseline. The abstract must lead with "no improvement detected" rather than "7.9% improvement consistent with no improvement." Currently the wording is engineered to imply progress where there is none.

**Required fix:** Rewrite the abstract sentence as: "yields αjk = 0.19 ± 0.65, consistent with zero bias enhancement; the multi-tracer Fisher forecast is not improved relative to the single-tracer baseline σ(fNL) = 8.98 at the 1σ level."

### P3-E2: NANOGrav "consistency" is a null result framed as evidence
**Abstract & §V A, p.11:** "the matter-bounce prediction γ = 3.0 sits at +1.13σ (marginally consistent) and SMBHB γ = 4.33 at +4.61σ (Savage-Dickey BMB/SMBHB = 7.1×10³)."

A Bayes factor between two **point predictions** (γ = 3.0 vs γ = 4.33) does *not* test bounce cosmology — it tests two specific γ values against the posterior. SMBHB is not actually a delta-function at γ = 4.33; it has substantial astrophysical scatter (Sesana et al., Burke-Spolaor). The "decisive" 7.1×10³ Bayes factor is an artifact of treating SMBHB as a delta prior. Section VI F admits "Neither constitutes a detection" but the abstract and conclusions present these numbers as supportive. NANOGrav itself (Afzal et al., ref [28]) carefully marginalizes over SMBHB astrophysics; this paper does not. **The Bayes factor as quoted is not defensible.**

**Required fix:** Either (i) marginalize SMBHB over a physically motivated prior on γ, or (ii) remove the Bayes factor entirely and state only that γ = 3.0 is within 1.13σ of the posterior median.

### P3-E3: Three of six injection-recovery gates FAIL — catalog completeness is unknown for half the surveys
**§II D step 5; Fig. 7; Table I; §VI C:** LAMOST (5.8% recovery at 5σ), Gaia (5.2%), eROSITA (1.2%) all fail the 50% recovery gate. The paper labels these "FAIL-with-diagnostic" — this is a euphemism. At 1.2% recovery (eROSITA), **the catalog is detecting 1 of every 83 planted signals**. The "exploratory tier" framing for LAMOST is acknowledged, but Gaia and eROSITA anomalies are presented throughout the paper (Tables I, III; Figs. 1, 5) as if they were science-grade detections.

**Required fix:** Either (a) remove Gaia and eROSITA from the headline count of 378,280 and report only the gate-PASS surveys, or (b) restate the headline as "~13,000 gate-PASS anomalies + ~365,000 exploratory" and rewrite Section VII conclusions accordingly. The current presentation is misleading.

### P3-E4: The "378,280 unique anomalies" headline conflates point sources and CMB map patches
**Abstract, §III, Table I, §VII conclusion 1:** The 378,080 + 200 stratification is mentioned but the headline number is used throughout. 200 64×64 CMB patches are not "anomalies" in the same sense as point-source detections — they are sky regions whose autoencoder reconstruction is poor. Adding them to a point-source count is a category error. The abstract correctly notes that "downstream analyses should use the 378,080 point-source tier" but then leads with 378,280 anyway.

**Required fix:** Use 378,080 as the headline throughout the abstract, title, and §VII. Move 200 Planck patches to a separate sentence.

### P3-E5: "~141× the largest prior single-survey anomaly catalog" comparison is dishonest
**Abstract, §VII conclusion 1:** Liang et al. [11] reports 2,685 anomalies (1.07% rate) from 250,000 spectra. The DESI scan here reports 195,829 anomalies (0.87%) from 22.5M spectra. **The 141× ratio is a sample-size ratio, not a methods improvement.** Both papers find ~1% anomaly rates; both use autoencoder reconstruction; this paper does not demonstrate any methodological advance over Liang et al. Calling the result "141× the largest prior" implies a discovery rate increase that is not real — it is the same rate scaled to a larger dataset that has been public for ~1 year.

**Required fix:** Either claim "~73× more spectra processed than Liang et al." (true) or "comparable anomaly rate scaled to the full DR1" (also true). Drop the "largest prior catalog" framing.

### P3-E6: The 17.8% genuine novelty fraction is a single-point estimate with no uncertainty
**Abstract, §IV A, §VII conclusion 2:** "Extended archival cross-matching of the top-1,000 DESI anomalies against 20 curated all-sky catalogs via CDS X-Match yields a genuine novelty fraction of ~17.8% (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested)."

So the entire "discovery rate" claim of the paper rests on **one cross-match of 1000 sources at the top score stratum**, with no error bar, no bootstrap, no extrapolation justification, and the authors explicitly admit the full-catalog rate is untested. This is the catalog's headline science claim. A single-sample point estimate with no error bar is not a measurement.

**Required fix:** Either (a) bootstrap an uncertainty estimate (Wilson interval at minimum: 17.8% ± ~2.4% for n=1000), or (b) extend the cross-match to a stratified sample across score deciles to characterize the score-dependent novelty fraction.

### P3-E7: DESI in-sample scoring inflates the anomaly headline
**§II B, §VI D (i):** The full 22.5M DESI scan includes the 47,000 training spectra. Yes, the 5-fold cross-validation Jaccard is 0.862 (PASS) — but this only tests training-sample robustness within the 47K pool. The 22.5M scan is **in-sample** for the training subset. More damningly, §II B states: "applying it to a random uncurated SPARCL sweep flags >50% of spectra (a catalog-curation effect, not a threshold artifact)." A 50% flag rate on unseen data versus 0.87% on the curated catalog is a **massive distribution shift signal**. The authors handwave this as "catalog curation"; the alternative interpretation — that the threshold is calibrated to the training curation and not to "anomalousness" per se — is not refuted.

**Required fix:** Provide a detailed reconciliation of the 0.87% (curated) vs >50% (uncurated SPARCL) anomaly rates, with explicit categorization of what flags the uncurated sources. Without this, the 0.87% rate is meaningless.

### P3-E8: σ values from different null procedures juxtaposed without "not directly comparable" warning
**Abstract, p.1:** "γ = 2.567 ± 0.382; the matter-bounce prediction γ = 3.0 sits at +1.13σ (marginally consistent) and SMBHB γ = 4.33 at +4.61σ" alongside "αjk = 0.19 ± 0.65 (< 1σ from null)" alongside "σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98]."

The 1.13σ (Gaussian posterior shift), 4.61σ (Gaussian posterior shift to delta SMBHB prior), 0.29σ (consistency of α with zero), and the 1σ Fisher envelope on σ(fNL) are four different statistical objects placed side-by-side as if comparable. The Fisher envelope is a forecast uncertainty, not a measurement uncertainty. The 4.61σ is contingent on the delta-prior assumption (P3-E2).

**Required fix:** At every juxtaposition of σ values, add explicit "not directly comparable" qualification with the type of null being tested.

### P3-E9: Fisher form 1/σ² = F₀ + cα² with c > 0 means the empirical α = 0.19 produces σ < baseline by construction — circular
**§V, §VI D (i):** The "positivity-respecting" form 1/σ² = F₀ + cα² with c = 0.0747 > 0 **guarantees** that any nonzero α reduces σ(fNL). Inserting α = 0.19 ± 0.65 then propagating through this form gives σ ∈ [3.92, 8.98] where the lower bound corresponds to α ≈ ±0.84 (the 1σ extreme). But the formula is symmetric in α, so the "improvement" is an artifact of the parameterization: the 1σ envelope cannot exceed the baseline by construction. The "central forecast σ(fNL) = 8.14" is just the propagation of α² ≈ 0.036 through a positive coefficient. This is not a measurement of cosmological information; it is a positivity-padded forecast.

**Required fix:** Either show that the 5-α refit independently constrains c (i.e., that the empirical Landy–Szalay measurement gives nonzero α at >2σ before forecasting σ(fNL)), or remove the σ(fNL) = 8.14 central figure from the abstract.

### P3-E10: LAMOST retained as "exploratory tier" but contributes 113,342 of 378,280 (~30%) to the headline
**Abstract: "the recommended catalog-grade subset is ~265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE), which excludes the LAMOST exploratory tier (~113,000 objects retained as a methodological lesson: 98% blue-excess training-bias artifact, injection-recovery gate FAIL)."**

If the recommended subset is ~265K, then **the title of the paper should say 265K, not 378K**. The current title and abstract lead with a number that the authors themselves recommend against using. This is exactly the kind of headline inflation that PRD reviewers are supposed to catch.

**Required fix:** Retitle the paper with the recommended number, e.g., "A Multi-Survey Catalog of ~265,000 Path-C Unique Anomalies."

### P3-E11: NANOGrav fit uses published KDE free-spectrum likelihood, not raw timing residuals
**§V A, §VI C (5):** The matter-bounce template is fit to the *NANOGrav-derived* KDE free-spectrum product, not to raw residuals. This means the +1.13σ "consistency" already inherits the choice of free-spectrum binning, Hellings-Downs correlation assumptions, and NANOGrav's own marginalizations. The systematic uncertainty in γ_posterior from these upstream choices is not propagated. NANOGrav (Afzal et al. ref [28]) themselves perform parametric searches with marginalized chains; quoting a 0.382 uncertainty from a 30-bin KDE fit understates the true uncertainty.

**Required fix:** Either (a) report the comparison to NANOGrav's own parametric γ posterior (which is what the bounce community should be comparing against), or (b) explicitly state that the 0.382 uncertainty does not include the upstream NANOGrav modeling systematics.

### P3-E12: Page 4 figure caption disagrees with figure title
**Fig. 1, p.4:** Title in the figure itself reads "Spatial distribution of all 319,443 anomalies across 8 archives" but caption says "319,443 detections shown; canonical Path-C unique count is 378,280." The figure shows the *cross-transfer baseline*, not the Path-C result. ACT DR6 is labeled in the legend despite being "quarantined." This is confusing the reader; the headline number in the figure title contradicts the headline number in the abstract.

**Required fix:** Regenerate Fig. 1 from the Path-C unique catalog (378,080 point sources) and update the title. Either remove ACT from the legend or label it explicitly as the quarantined cross-transfer block.

### P3-E13: Internal audit tags / version artifacts in the body
Multiple instances of "Path-C" appear without ever being defined as anything other than internal versioning. The phrase "Path-C rebuild" appears ~30 times. This is internal-roadmap language, not science vocabulary. A reader of PRD has no idea what "Path-A" or "Path-B" were. Similarly: "Path-C-final," "before/after diagnostic," "preserved as a sensitivity-check artifact," "8-way-with-ACT variant," "v3.1.75" — these are workflow internals.

Also: §VI D Table IV header says "All ten items are closed (C = resolved in paper)" but only items (a)–(j) are listed, and "C =" is left as undefined notation in the table.

**Required fix:** Rename "Path-C rebuild" to something descriptive like "per-survey native retraining protocol." Drop "Path-C" entirely. Define table notation in Table IV.

### P3-E14: Fig. 8 caption refers to "single-tracer baseline σ(fNL) = 16.85" but §V says σ(fNL)std = 8.98
**Fig. 8 caption, p.16:** "the dotted dark-red line marks the single-tracer baseline (σ(fNL) = 16.85)" and "the dashed gray line marks the dense-tracer limit (σ(fNL) = 11.71); the baseline multi-tracer (σ(fNL) = 12.72)."

But §V says: "The single-tracer DESI QSO baseline is σ(fNL)std = 8.98" and central forecast σ(fNL) = 8.14. **These numbers do not match.** Either Fig. 8 is from a different forecast configuration than §V, in which case the figure is internally inconsistent with the abstract, or one of the numbers is wrong.

**Required fix:** Reconcile the σ(fNL) numbers between Fig. 8 and §V. State explicitly which Fisher configuration each refers to.

### P3-E15: Table I column "Path-C unique (primary) 378,280" sums incorrectly to the stated input
**Table I, p.7:** "Path-C unique (primary) 37,272,042  378,280  1.01  —"

378,280 / 37,272,042 = 1.0149% which rounds to 1.01% ✓ arithmetic OK.

But the row above (cross-transfer total) gives 37,292,042 (with 20K ACT patches) for 319,443 = 0.857%. The Path-C row says 37,272,042 (subtracting 20K ACT inputs). However, the Path-C SDSS native processed **1,925,279 spectra** (not 2,304,830 as in the cross-transfer SDSS row), and Path-C LAMOST processed **11.3M** (not 11.42M). The 37,272,042 input number is therefore wrong; it should be smaller by ~500K to reflect the actual native-processed inputs.

**Required fix:** Recompute the Path-C total input correctly, or document the discrepancy.

### P3-E16: 5σ NANOGrav γ analysis: prior γ ∈ [0,7] with point estimate at γ = 4.33 — Savage-Dickey ill-defined
**§V A:** Savage-Dickey requires a *nested* model where the null parameter is fixed at a single value within a continuous prior. The "SMBHB γ = 4.33" point is not naturally a nested null hypothesis for the matter-bounce model (γ = 3.0 is also not). Computing BMB/SMBHB = posterior(γ=3.0)/posterior(γ=4.33) is technically defined, but interpreting it as decisive evidence for bounce cosmology is wrong: it is evidence that γ_posterior favors 3.0 over 4.33, with no implication about either model class. Both could be ruled out by future data and the ratio would persist.

**Required fix:** Frame the Bayes factor as a *spectral-index point comparison* rather than a model-selection result. Remove "decisive on Jeffreys' scale."

---

## MAJOR findings (significant revision required)

### P3-M1: Page count vs contribution — 20 pages is too long
The paper is 20 pages for what is essentially: (i) a catalog (~3 pages), (ii) per-survey results (~6 pages, half of which document failed gates), (iii) a null cosmology result on fNL (~2 pages), (iv) a null NANOGrav consistency (~2 pages), and (v) extensive caveats (~5 pages). The "Path-C residual caveats" section (Table IV + commentary) is itself ~2 pages of qualifications. **Recommended maximum: 12 pages** for a methods/catalog paper of this scope, or split into two papers (catalog + cosmology).

### P3-M2: Spectrally Unusual Sources at Scale" title oversells what is largely a curated catalog with three failure-mode warnings
The title implies a discovery paper; the body is mostly a description of an autoencoder pipeline that produced anomaly scores, three of whose six surveys failed validation. A more honest title: "An Autoencoder Anomaly-Detection Pipeline Across Seven Astronomical Archives: Catalog, Failure Modes, and Multi-Tracer fNL Forecasts."

### P3-M3: The "BigAE" architecture is not novel
A "symmetric fully connected autoencoder with batch norm + ReLU + dropout" is the textbook baseline architecture for tabular/spectral autoencoders since ~2015. The name "BigAE" suggests something distinctive; the §II A description shows a 120K–660K parameter standard MLP autoencoder. Drop the branding, or justify what "Big" refers to (architecture is in fact small by 2024 standards).

### P3-M4: §IV B spatial uniformity χ² = 143,936 with χ²_ν = 3.76 is misleadingly reported
The text correctly notes that the χ² is dominated by inhomogeneous footprints. Then **why is it reported as a headline number?** The χ² test is uninformative here and should be removed, not "noted as a caveat." Reporting an uninterpretable χ² gives the impression of statistical rigor where none exists.

### P3-M5: Fig. 2 left-panel inset annotations show "24.5, 24.6, 25.2" near the same x-position but the text states these are three distinct objects
The annotations overlap and are visually indistinguishable. Either separate the labels or remove the inline annotations.

### P3-M6: Fig. 4 NEOWISE image shows a saturated source with diffraction spikes
The caption acknowledges "Physical interpretation uncertain: circumstellar dust excess, buried AGN, and evolved giant hypotheses are consistent." If the top anomaly cannot be physically characterized, the "score = 11.5" headline is not informative. Either provide a follow-up identification or move this figure to an appendix.

### P3-M7: Fig. 6 panel (d) "Match 2: SDSS epoch (score 49.5)" shows the reconstruction (red) flat at ~1 while the spectrum (black) sits at ~3
The reconstruction is failing catastrophically. The caption frames this as "consistent with a stellar flare or accretion event," but a score of 49.5 on a 5σ-threshold catalog (10× the threshold) on an object the model cannot reconstruct at all is more likely a calibration issue (e.g., flux normalization mismatch between DESI and SDSS). The cross-survey "match" rests on three objects, one of which the model cannot reproduce.

### P3-M8: §IV D Planck × ACT null cross-correlation conflates two distinct failure modes
The "null" is presented as a clean negative result: "CMB patch anomalies from autoencoder analysis are dominated by survey-specific systematics rather than primordial cosmological signals." But the ACT analysis is the **cross-transfer** one that fails both gates and is quarantined (Appendix F). The null is therefore not informative — it is the expected outcome when one survey's autoencoder is undertrained. Section IV D should not be cited as evidence about CMB anomaly detection writ large.

### P3-M9: Empirical Landy–Szalay measurement on 5,384 QSO candidates — sample selection not described
**§V:** "An empirical Landy–Szalay angular two-point analysis on the full 5,384 QSO-candidate sample..." How was the 5,384 sample selected from the 195,829 DESI anomalies? The "1,122-object Gold+Silver subset" (§V b) is also undefined. These selections drive the α measurement; they cannot be left as labels.

### P3-M10: "Genuine novelty" cross-match against 20 catalogs — list incomplete
**§IV A:** The text says "20 curated all-sky catalogs" but only lists ~17 (Gaia DR3, SDSS DR12/DR16, DESI Legacy DR9, DES DR2, Pan-STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS). State all 20 or fix the count.

### P3-M11: TIC 374313355 score 49.5 is the highest SDSS anomaly cross-matched — but Fig. 2 right panel shows SDSS native scores reach 1.9×10¹¹
The narrative says (Fig. 2 right) that SDSS cross-transfer scores reach S = 1.9×10¹¹ for M7/T2 dwarfs, while TIC 374313355 SDSS score is 49.5. The 49.5 is therefore not extreme in the SDSS distribution — many ultra-cool dwarfs have scores ~10⁹ higher. Yet it's framed as "the highest of any cross-matched object" (Fig. 6 caption). Reconcile.

### P3-M12: §III F Planck native CMB autoencoder val_loss = 0.4437 vs. gate criterion ≤ 0.30
**§III F:** "The native retrain converged at val_loss = 0.4437 (criterion (a) FAIL, but criterion (b) PASS: 500/500 = 100% injection-recovery at 5σ Gaussian-bump amplitude)."

This is paper-thin gate-passing. The two-part gate is an "OR" — pass either criterion. But injection of Gaussian bumps with the same amplitude as the training bumps is **not** an independent test of anomaly detection; it tests that the autoencoder hasn't completely failed at its training task. 100% recovery on a planted Gaussian when the model is itself trained to reconstruct CMB-like noise is unsurprising. The val_loss = 0.4437 (15× over criterion (a)) means the autoencoder is poorly trained.

### P3-M13: NEOWISE 100% gate PASS is on the mask, not on detection
**Fig. 7 / §III H:** "NEOWISE ecliptic-pole mask (PASS, 1000/1000 = 100%)." The mask injection-recovery (testing that masked sources are excluded at the boundary) is **not** the anomaly-detection injection-recovery (testing that planted anomalies are recovered). These are different tests; the figure conflates them.

### P3-M14: §III G Gaia DR3 results are 2 sentences
The Gaia analysis processed 50,000 variable stars and produced 500 anomalies (top 1%), of which the injection-recovery is 5.2% (FAIL) and cross-validation stability is 41% (FAIL). Yet Gaia contributes 500 objects to the headline 378,280 and is included in the recommended ~265K subset. Two sentences of analysis for a survey contributing to the headline is insufficient.

### P3-M15: §VI E "Comparison with prior work" is one paragraph
Compare-and-contrast with Liang et al., Nicolaou et al., and Baron & Poznanski should occupy ~1 page. What did they find, what did this paper find, what is genuinely different? Currently the comparison reduces to "our rate is consistent with Liang et al.'s rate" — which is a null methodological contribution.

### P3-M16: Appendix C Table VII presents linear σ(fNL) scaling, but §V uses a quadratic Fisher form
**Table VII vs §V Fisher form:** Table VII shows σ(fNL) = 8.43 at α = 0.15 (linear-scaling forecast). §V says σ(fNL) = 8.14 at α = 0.19 with the quadratic positivity-respecting form. These are different functional forms applied to different α values. Table VII is presented as "sensitivity to α" but it uses a different model than the headline result. State the form explicitly in the table caption.

### P3-M17: Multi-tracer matter-bounce scenario "γ = 3.0 and fNL = -35/8 decouple in the broader bouncing-cosmology landscape"
**§V:** "All forecasts assume the scalar-only w = 0 matter-bounce class; fNL = −35/8 and γGW = 3.0 decouple in the broader bouncing-cosmology landscape."

This admission undercuts the cosmology section. If the two observables decouple in the broader landscape, then a γ-posterior consistent with 3.0 says nothing about fNL = -35/8 and vice versa. The "bounce cosmology consistency" framing of §V A is then misleading: at best the paper shows that one specific class (w=0 matter bounce) is not yet excluded.

### P3-M18: "Spearman r = 0.0005, p = 0.92" — what is the sample size?
**§IV B:** A Spearman correlation with r = 0.0005 and p = 0.92 implies a sample where any real correlation would be detected only at very low strength. Without N, the reader cannot evaluate.

### P3-M19: §VI D (i) "Fisher positivity-respecting form" is introduced as a fix — but the original linear form is never shown
The reader cannot evaluate whether the change from a linear to a quadratic form was forced by theory or convenience. Show the original Fisher derivation and the algebraic step that produces 1/σ² = F₀ + cα². Otherwise this looks like ad-hoc reparameterization to avoid σ(fNL) > baseline.

### P3-M20: The release statement says "private pending arXiv acceptance"
**§Data availability, p.14:** Catalog data deposited on HuggingFace, "private pending arXiv acceptance." A referee cannot evaluate the catalog because it is not accessible. PRD review standards generally require reviewer access to deposited data.

---

## MINOR findings (address but paper can proceed)

### P3-Mi1: Date "(Dated: June 2026)" on p.1
This appears to be a future date (paper is being reviewed now). Update to actual submission date.

### P3-Mi2: "Houston Golden¹, *" with "¹Independent Researcher, Los Angeles, California, USA"
No co-authors on a 20-page paper claiming to scan 37.3M sources, deploy autoencoder retraining for 7 surveys, perform Landy–Szalay analysis, run NANOGrav MCMC, and compute Fisher forecasts. This is unusual; flag for editorial check.

### P3-Mi3: Eq. (2) defines S = (MSE − μ_val)/σ_val but then "S > 5" is described as MSE ≈ 0.143
Reconcile units explicitly: if μ_val = 0.0287 and S = 5 corresponds to MSE = 0.143, then σ_val ≈ 0.0229. State σ_val.

### P3-Mi4: Fig. ?? appears in §II A "architecture shown schematically in Fig. ??" and §II B "Fig. ??"
Two broken LaTeX references on p.2. Also in §III B "Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts." Three broken refs total.

### P3-Mi5: Inconsistent decimal formatting
"DESI 5-fold Jaccard stability J̄ = 0.862" (3 digits) vs "OOD control-vs-control 0.874" (3 digits) vs "production-vs-5-seed-control Jaccard J̄prod×ctrl = 0.732" (3 digits). OK, but §VI D (i) says "J̄prod×ctrl = 0.732" while §VII conclusion 6 says "OOD control-vs-control 0.874" — what are these two different numbers? Inconsistent.

### P3-Mi6: "TIC 374313355" — Score 49.5 (SDSS) vs 8.1 (DESI)
The factor-of-6 score difference between epochs is presented as evidence of variability. But the DESI score 8.1 is in DESI's S units (validation z-scores from DESI training pool); SDSS 49.5 is in SDSS's transfer-learning S units (DESI training pool applied to SDSS spectra). **These are different score scales** (different μ_val, σ_val) and cannot be directly compared. The "variability" claim needs to be made in physical flux units, not in autoencoder scores.

### P3-Mi7: Table II "Uncategorized 41,065 52.7%"
The "Uncategorized" category being the modal class undermines the per-category classification utility of Table II. Either characterize what "Uncategorized" means physically or remove the table.

### P3-Mi8: §III B "12 candidates with z = 6.0–6.23" — no follow-up planned/confirmed
The most scientifically interesting result is presented without any follow-up commitment. State whether spectroscopic follow-up has been proposed/scheduled.

### P3-Mi9: "Spearman rank correlation ρ = −0.03 (p = 0.12 on a stratified subsample of 2,670 spectra)"
A p-value of 0.12 with N=2670 means the test has very weak power; the conclusion "no practically significant score–SNR dependence" is reasonable but should also be quoted as a 95% CI on ρ.

### P3-Mi10: §IV A "100% archival-identification rate (20/20 resolved)"
N=20 sample with no error bar. Cite Wilson/Jeffreys interval: 100% out of 20 has 95% CI lower bound ~83.2%, not literally 100%. Acknowledge the binomial uncertainty.

### P3-Mi11: §VI A "the simplest check—a comparison impossible with a single-survey analysis"
This claim is false. Single-survey analyses routinely include training-bias diagnostics (PSF residuals, fiber position checks, color cuts). The LAMOST blue-excess could have been caught with a single-survey color diagnostic. Reframe.

### P3-Mi12: "matter-bounce fNL = −35/8 = −4.375"
The value -35/8 is repeated ~6 times in the paper. State once and refer back.

### P3-Mi13: §III A "0% artifact rate" in top 200 DESI anomalies
Visual inspection of 200 spectra by one author is not a 0% artifact rate; it is "no artifacts identified by visual inspection." The two are different statements.

### P3-Mi14: Fig. 5 dashed line marks "58.8% Aggregate" but the aggregate is acknowledged as not the headline novelty figure
The figure design draws the eye to 58.8% while the text emphasizes 17.8%. Either annotate 17.8% as well or redesign.

### P3-Mi15: §III C "12 sources at S > 5 vs. cross-transfer 77,905, a ~6500× anomaly-rate reduction"
77,905 / 12 = 6,492. The phrase "~6500×" is fine but stated as "~ 6500×" with extra space; also stated as "∼ 6500×" elsewhere. Inconsistent typography.

### P3-Mi16: "Hubify-Projects/bigbounce" GitHub link
The project name "bigbounce" with the author affiliated to "hubify.com" suggests a personal-website infrastructure; ensure the link will remain stable.

### P3-Mi17: Table III "SBigAE 1.084" vs §III E "top anomaly... S = 1.084"
On the same page, score "1.084" appears as both SBigAE and S — confirm this is the canonical S of Eq. (2). §III E uses "S > 0.259" as the threshold; values 1.084, 0.815, 0.591, 0.498, 0.439 are all above this. OK but explain why these are not on the same z-score scale as DESI S > 5.

### P3-Mi18: §V "30-region jackknife"
Sample size of 30 regions for a jackknife variance estimate is on the low end for a precision claim of 0.65 uncertainty on α. State the regions' angular size.

### P3-Mi19: "Quasi-matter bounce model predicts fNL = −35/8" — citation [13, 14, 35]
Ref [13] (Wands 2010) is a review of local non-Gaussianity from inflation, not from bounce cosmology. The matter-bounce fNL = -35/8 prediction is from refs [14] (Cai et al.) and [35] (Wilson-Ewing). Remove ref [13] from this citation cluster.

### P3-Mi20: Repeated text in §III A
The paragraph "Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE classification..." then "galaxies are flagged at ∼20 times the rate of QSOs (0.75% vs. 0.037%), with anomalies peaking at z ∼ 0.75 compared to z ∼ 0.93 for normal spectra" duplicates content from the immediately preceding paragraph: "Galaxies are flagged at ∼20× the QSO rate (0.75% vs. 0.037%); anomalies peak at z ∼ 0.75 vs. z ∼ 0.93 for normal spectra. The three highest-scored anomalies (S = 25.2, 24.6, 24.5) are Z-dominant, consistent with high-z Gunn–Peterson absorption." Verbatim duplicate of "highest-scored anomalies are Z-dominant" claim too. **Two consecutive paragraphs say almost the same thing.**

### P3-Mi21: Abstract "(Path-C unique)" — what does Path-C mean to a reader?
The abstract uses "Path-C" without defining it. Define on first use or drop.

### P3-Mi22: §I "the total data volume accessible to a single research group now exceeds tens of millions of sources"
Sociological observation in introduction; remove.

### P3-Mi23: §VII conclusion 5: "matter-bounce γ = 3.0 at +1.13σ, SMBHB γ = 4.33 at +4.61σ (BMB/SMBHB = 7.14×10³)"
Already flagged (P3-E2). Conclusion should say "consistent at 1.13σ, SMBHB disfavored as a point estimate."

### P3-Mi24: "Heinrich et al. [33] (σ(fNL) ≈ 0.7 bispectrum-only forecast)"
A bispectrum-only forecast of 0.7 is dramatically tighter than this paper's 8.14 forecast. The juxtaposition without context (multi-tracer bispectrum vs. multi-tracer power spectrum) is misleading. Either explain the regime or remove the Heinrich comparison.

### P3-Mi25: §VI D Table IV header "All ten items are closed (C = resolved in paper..."
But the table has 10 rows labeled (a)–(j). The "C =" notation is never instantiated in the table — the third column does not show "C" markers. Remove the "C =" notation.

### P3-Mi26: Appendix F "The 8-way-with-ACT dedup variant, which would have produced 388,693 − 10,213 = 378,480 unique objects"
This is the only place this specific arithmetic appears. 388,493 (sum of survey counts excluding ACT) + 200 (ACT) = 388,693. 388,693 − 10,213 = 378,480 = 378,280 + 200 (zero ACT overlaps). OK, arithmetic checks. But report this in Table I rather than burying it.

### P3-Mi27: Reference [33] note: "publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity"
Internal-bookkeeping prose in the reference list. Remove.

### P3-Mi28: §V A "emcee 32 walkers × 10,000 production + 2,500 burn-in"
Total samples = 32 × 10,000 = 320,000. With autocorrelation time τ ≈ 58, effective sample size ≈ 320,000 / 58 ≈ 5,517. OK. Report explicitly.

### P3-Mi29: Caveats labeled (a)–(j) in Table IV but text references (i), (ii), (iv), (v), (f), (g), (h), (i), (j) in §VI D
The numeric labels (i)–(v) in §VI D do not map to the alphabetic labels (a)–(j) in Table IV consistently. Cross-reference is unclear.

### P3-Mi30: Figure 9 "DESI DR1 Spectral Anomalies" — labels include AE values like 83518
The "AE" abbreviation for autoencoder score is not used elsewhere; reader sees "AE=83518" without knowing what this means. The score 83518 is also wildly outside the S < 25 range stated elsewhere — what is the scale? Reconcile with the canonical S of Eq. (2).

---

## NIT findings

### P3-N1: "(Dated: June 2026)" — future date
### P3-N2: Inconsistent use of "× " vs "x" for multiplication ("~141×" vs "20× the QSO rate")
### P3-N3: "BigAE" alternately styled as "BIGAE" in §II A and §II A
### P3-N4: §V title "COSMOLOGICAL APPLICATIONS" plural but only one analysis (fNL); NANOGrav is separate subsection
### P3-N5: Acknowledgments do not state funding source
### P3-N6: HuggingFace dataset link "private pending arXiv acceptance" — should be public-on-publication for PRD
### P3-N7: ApJ Suppl format conventions used in references; PRD prefers Phys. Rev. D format. Standardize.
### P3-N8: §III E lists "Top 5 sources" in Table III; only 5 of 298 anomalies. Justify selection (highest score? Brightest?).
### P3-N9: §IV C "9,576 intra-survey duplicates" — what survey contributes the bulk? DESI alone scoring its own training spectra likely causes this. Document.
### P3-N10: §VI D (h) "Thresholds: DESI S > 5.0; SDSS/LAMOST top-1%; eROSITA S > 0.259" — Table I caption has the same content with footnotes. Don't repeat in two places.

---

## Summary recommendation

**REJECT** (with invitation to resubmit a substantially scoped-down version to a more appropriate journal).

This paper has the structural shape of a methods/catalog paper inflated to PRD scope by appending two cosmology subsections (multi-tracer fNL, NANOGrav γ) whose central claims are statistically null and whose headlines (σ(fNL) = 8.14, BMB/SMBHB = 7.1×10³) are products of parameterization choices rather than measurements. The catalog itself has three of six injection-recovery gates fail, the headline 378,280 number is recommended-against by the authors themselves (~265K is the catalog-grade subset), DESI scoring is in-sample with a 50× anomaly-rate jump on uncurated data, the "genuine novelty" rate is a single-point estimate at one score stratum, and the comparison to prior work shows the same ~1% anomaly rate at ~73× larger sample with no methodological advance. The author should: (1) split this into a catalog/methods paper for MNRAS or ApJS at ≤12 pages, dropping the cosmology sections; (2) separately, if and when the fNL and NANOGrav analyses produce ≥2σ results with proper systematic propagation, submit those to PRD or JCAP. As written, the paper is not a physics result and does not meet PRD's significance threshold.