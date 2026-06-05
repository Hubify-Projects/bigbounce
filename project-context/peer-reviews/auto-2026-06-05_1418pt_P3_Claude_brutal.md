# P3 auto-2026-06-05_1418pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (16647 chars)
**Wall time**: 507.5s

---

# Referee Report — Paper P3
**Title:** "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies..."
**Submission target:** Physical Review D
**Recommendation:** **REJECT** (see end)

This paper bundles (a) a large autoencoder anomaly catalog spanning seven archives, (b) a Fisher forecast for f_NL, and (c) a NANOGrav spectral-index fit relevant to bouncing cosmologies, into a single 20-page manuscript by an unaffiliated author. Brutal honesty: the central scientific claims do not survive scrutiny, the methodology contains documented failures presented in euphemistic language, and the paper is far too long for what it actually demonstrates. PRD's bar for a methods/cosmology paper is exceeded by neither the catalog (largely a scale claim) nor the cosmology (a 7.9% central forecast consistent with zero, plus a delta-function Bayes factor exercise on NANOGrav).

---

## ESSENTIAL findings (must be addressed before any further consideration)

### P3-E1 — The f_NL "improvement" is consistent with no improvement, but presented as a result (Abstract, §V)
The abstract states σ(f_NL) = 8.14 with 1σ envelope [3.92, 8.98] and a "7.9% improvement consistent with no improvement at <1σ; σ(f_NL)^std = 8.98 single-tracer baseline." The envelope upper edge equals the no-improvement baseline. The empirical input α_jk = 0.19 ± 0.65 is <0.3σ from zero. **This is a null result.** It must not be reported as a central forecast in the abstract. The Fisher-positivity construction 1/σ² = F₀ + cα² is mathematically chosen to prevent the result from going *worse* than the baseline, which artificially asymmetrizes the envelope and inflates the apparent central value. The headline "7.9% improvement" should be removed; the result is "no detection of multi-tracer enhancement at <1σ."

### P3-E2 — NANOGrav SMBHB "+4.61σ disfavoring" is methodologically invalid
The paper claims SMBHB γ = 4.33 sits at +4.61σ from the fit and computes B_MB/SMBHB = 7.1×10³ ("decisive"). This treats SMBHB as a delta function at γ = 4.33. The actual SMBHB GWB spectral index distribution from realistic population models has σ_γ ≳ 0.4–0.6 (e.g. Sesana 2013; Middleton et al. 2021), comparable to the posterior width itself. A proper Savage-Dickey requires marginalizing the SMBHB prior; a delta-function at the median expectation is not the same calculation. The "+4.61σ" and 7.1×10³ Bayes factor must be retracted or recomputed with realistic SMBHB priors. The published NANOGrav 15-yr paper does not find SMBHB disfavored at this level.

### P3-E3 — "Largest-scale application of autoencoder anomaly detection" overclaim
The opening sentence of the abstract is a load-bearing novelty claim. It is technically true only because of the conjunction "across seven astronomical archives." The DESI-only axis is 73× Liang et al. [11], but this is mostly a data-availability artifact (DR1 vs. EDR). The 141× figure is dominated by LAMOST (113,342 objects) which the authors themselves admit is 98% training-bias artifact and FAILS the injection-recovery gate. Subtracting LAMOST drops the headline to ~265,000, and the "recommended catalog-grade subset" footnote confirms this. The headline number is therefore inflated by a population the authors explicitly recommend not using downstream. Re-state the headline as the catalog-grade subset (~265k) and remove "largest-scale application" framing.

### P3-E4 — Path-C nomenclature and internal version tags leak into the paper
"Path-C rebuild," "Path-C unique," "Path-C native-retrained counts," "Path-C residual caveats," "8-way-with-ACT dedup variant ... preserved as a sensitivity-check artifact in the companion data repository" are version-control labels for internal review rounds (the abstract uses "Path-C" 5+ times). Readers cannot tell what Path-A or Path-B were. This is internal bookkeeping language unfit for a published paper. Rename to scientific terms (e.g. "native per-survey retraining") and remove all "Path-C" tags from titles, abstract, and section headings.

### P3-E5 — Injection-recovery gate failures presented as "FAIL-with-diagnostic"
At 5σ, LAMOST recovers 5.8%, Gaia 5.2%, eROSITA 1.2%. These are catastrophic failures — recovery essentially indistinguishable from random chance. Calling them "FAIL-with-diagnostic" while invoking unrelated cross-validation stability numbers (eROSITA 81.5%) is euphemism. The authors then report these surveys' anomaly catalogs as part of the headline count. Either (i) remove the failed-gate surveys from the headline, or (ii) explicitly label each affected catalog as "completeness unquantified, recovery <6%" in the abstract.

### P3-E6 — Figure 7 mislabeled: claimed 3 PASS not shown
Figure 7 legend shows six curves: SDSS continuum, SDSS emission, LAMOST continuum, LAMOST emission, eROSITA latent, Gaia variability. The caption claims **three** surveys PASS the gate at 5σ: SDSS, Planck, NEOWISE. But Planck and NEOWISE are not in the figure. The figure thus shows only one PASS (SDSS 64%) and four FAILs. The PASS claim for Planck and NEOWISE uses different test types (Gaussian-bump injection on 64×64 maps, ecliptic-pole mask retention) that are not comparable to the spectroscopic continuum-dip recovery curves on the same plot. Either re-plot with the missing surveys or remove the "three PASS" claim from the caption.

### P3-E7 — DESI in-sample scoring conflated with held-out validation
The 195,829 DESI anomalies are scored on a catalog *that includes* the 47,000 training spectra. The 5-fold Jaccard stability (J̄ = 0.862) tests the top-1% of the 47k training pool (~546 objects in the union), not the headline 195,829 selection. The OOD test (production-vs-control J̄ = 0.732) is buried. The abstract says "DESI 5-fold Jaccard stability J̄ = 0.862 (≥ 0.70 gate, PASS)" without qualifying that this tests reproducibility of a 470-object slice of a 47k pool, not the 195k headline. State the actual sample size in the abstract or remove the gate claim.

### P3-E8 — The 17.8% novelty headline is a single-sample point estimate
Abstract: "yields a genuine novelty fraction of ∼17.8% (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested)." This is an honest disclosure but the number is then promoted as the headline novelty fraction throughout the paper (§IV A, Conclusions). Promoting a single bin's measurement to a catalog-level metric while disclosing that the catalog-level rate is "empirically untested" is incoherent. Either remove the 17.8% from the abstract or extend the cross-match to a randomly sampled sub-catalog (e.g. score-stratified 1000-object random samples) to bound the full-catalog rate.

### P3-E9 — Scope mismatch: three loosely related topics in one paper
The paper combines: (i) autoencoder anomaly catalog construction, (ii) Fisher f_NL multi-tracer forecast, (iii) NANOGrav free-spectrum power-law fit relevant to matter bounce. None of these is delivered to PRD-standard depth on its own:
- (i) is an engineering exercise dressed as a science result.
- (ii) is a null forecast with α consistent with zero.
- (iii) is a fit to a publicly released KDE likelihood with a Bayes-factor claim against an over-simplified alternative (P3-E2).

A focused 8–10 page paper on either the catalog *or* the cosmology applications would be appropriate. The current 20-page omnibus is not.

### P3-E10 — Single-author breadth-of-claim implausibility / data-availability deferred
The author lists "Independent Researcher" with no acknowledgment of internal/external collaborators despite spanning ML methodology, DESI/SDSS/LAMOST spectroscopy, X-ray catalogs, CMB analysis, two-point clustering, Fisher information, MCMC fitting of PTA data, and bounce cosmology. Combined with the data-availability note that the HuggingFace catalog is "private pending arXiv acceptance," reproducibility cannot be verified at review time. PRD does not accept "private pending acceptance" repositories for catalog papers; the data must be public or anonymously accessible to referees during review.

---

## MAJOR findings

### P3-M1 — Table I arithmetic and footnote audit
Cross-transfer baseline sum: 195,829 + 77,905 + 44,075 + 298 + 200 + 500 + 436 = 319,243, not 319,443. The +200 difference is the quarantined ACT block, footnoted but not explicit in the row. The table caption simultaneously claims ACT is "quarantined" and "is not listed in the main per-survey block" while the total row still includes those 200. State this transparently or remove ACT from the total.

### P3-M2 — Figure 1 caption inconsistent with paper claim
Figure 1 caption: "Spatial distribution of all 319,443 anomalies across 8 archives." The paper formally quarantines ACT (7 retained). The figure title and caption contradict the abstract.

### P3-M3 — "Matter-bounce prediction f_NL = -35/8" presented as the prediction
Cited to Cai et al. 2009 [14] and Wilson-Ewing [35]. f_NL = -35/8 is *one scenario's* prediction (specific matter-bounce realization with particular contraction dynamics). The paper repeatedly writes "the matter-bounce prediction f_NL = -35/8" as if singular. There is a family of bouncing-cosmology f_NL predictions spanning O(1)–O(10²) in magnitude. State the scenario specificity in §I, §V, and Conclusions.

### P3-M4 — Multi-tracer Fisher: positivity-respecting form is not a physical model
The form 1/σ² = F₀ + cα² with c = 0.0747 is constructed so the central value of α = 0 returns the single-tracer baseline. This guarantees σ ≤ σ_std for all α, which is fine. But the asymmetric envelope [3.92, 8.98] from α_jk = 0.19 ± 0.65 reflects only the algebraic propagation; α₂_jk has a χ²-distributed structure under the null. Treating the envelope as a Gaussian 1σ region misrepresents the actual posterior. Either compute the full posterior on σ(f_NL) or remove the envelope.

### P3-M5 — Spatial χ² interpretation contradicted in same paragraph
§IV B reports χ²_ν = 3.76 indicating non-uniformity, then within the same paragraph admits "the significant χ²_ν = 3.76 is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering." If so, the χ² test is invalid and should not be reported as a result. Remove the test or implement the per-survey selection-function corrections it requires.

### P3-M6 — eROSITA injection-recovery 1.2% vs. IF-stability 81.5% conflict
The paper presents 81.5% IsolationForest cross-validation stability as a "PASS-equivalent" mitigation for the 1.2% injection-recovery FAIL. These are not measuring the same property — IF-stability measures consistency of the *detector* on the same data; injection-recovery measures *completeness* against planted signals. A detector can be perfectly stable and perfectly insensitive. The phrasing "FAIL at 5σ ... but highest XV-stability of any Path-C survey" misleads.

### P3-M7 — NANOGrav fit: matter-bounce γ = 3.0 at +1.13σ is not a result
A 1.13σ deviation in either direction is the textbook definition of "no evidence." Yet the conclusion uses this to claim "bounce predictions are not yet excluded." This is true of essentially any prediction within 2σ of any data; it is not a scientific finding. Either remove the NANOGrav section or recast as "the data does not currently distinguish bounce from SMBHB at the present S/N" without the inflated Bayes factor.

### P3-M8 — "Genuine novelty" cross-match methodology underdescribed
The CDS X-Match against "20 curated all-sky catalogs" produces 82.2% archival ID rate. Different catalogs have different angular-resolution and completeness limits; for a faint optical anomaly at S/N near the DESI floor, absence from all 20 is largely determined by the depth of the shallowest covering catalog. No quantification of expected false-novelty rate from depth incompleteness is provided. The 17.8% is an upper bound on novelty, not a measurement.

### P3-M9 — Table III "two scores per source" with IF raw on a 0–3.5×10⁴ scale
SIF,raw values 34,182, 16,270, etc. are presented as scores but the scale is not standardized. Without normalization (e.g. percentile rank), these numbers convey no information to the reader. Either convert to percentile or remove the column.

### P3-M10 — Equation (E1) dimensional check
log₁₀ ρᵢ = ½[2 log₁₀ A − log₁₀(12π²) + (γ−3) log₁₀ f_yr − γ log₁₀ fᵢ − log₁₀ T_obs]. This is the timing-residual power spectral density relation. The factor of ½ is unusual — standard form has no ½, with ρᵢ having units of [time²·time] (squared residual × inverse frequency bin). Either the ½ converts from amplitude to power and this should be written as P(f) not ρ², or it is an error. Clarify.

### P3-M11 — "Quasi-matter bounce model" cited inconsistently
The abstract says "quasi-matter bounce" with predictions f_NL = -35/8 and γ_GW = 3.0. §V A's Appendix-E note correctly states these decouple in the broader bouncing-cosmology family, but the abstract and §I treat them as joint predictions of one model.

### P3-M12 — SPHEREx σ(f_NL) ≈ 0.7 claim
§I says "σ(f_NL) ≈ 0.7 bispectrum-only forecast" referencing Heinrich et al. [33]. That paper's headline forecast depends strongly on assumed nuisance parameters; reporting "≈ 0.7" without specifying the configuration (bispectrum-only, fixed bias, ideal systematics) is misleading. Heinrich et al.'s realistic forecast is degraded substantially.

### P3-M13 — "Native-trained novelty fractions" in title
The title phrase "Native-Trained Novelty Fractions" suggests novelty fractions are a primary product. The actual paper provides one number (17.8%) from one survey, one bin, one cross-match procedure. Title overpromises.

### P3-M14 — SDSS rate compression "~6500×" is a methodological artifact, not a result
"21.5× LAMOST rate compression and ~6500× SDSS rate compression after native retraining" — these compression ratios are between two checkpoints (cross-transfer vs. native) of the *author's own pipeline*. They are diagnostics of the cross-transfer failure, not measurements of anything physical. Stop presenting them as headline numbers in the abstract.

### P3-M15 — "180/1,000 ... 17.8%" — Wilson interval needed
A single binomial measurement of 178/1000 has 95% Wilson interval roughly [15.5%, 20.4%]. Reporting "∼17.8%" without uncertainty understates statistical width.

### P3-M16 — Page count
20 pages with two large figure appendices for a paper whose science content (after pruning Path-C diagnostics, ACT quarantine, and version-tagged residuals) fits in 10–12. Recommended maximum: 12 pages including all figures and appendices.

### P3-M17 — Affiliation address
"Los Angeles, California, USA" with email at hubify.com (a commercial domain). PRD typically requires institutional affiliation or explicit "independent researcher" with a note on lack of conflict.

### P3-M18 — TIC 374313355 score = 49.5 alongside SDSS native max ~14
SDSS native re-score "12 sources at S > 5" per §III C, but Fig 6 panel (d) shows TIC 374313355 at S = 49.5 in SDSS DR18. Is this score on the cross-transfer scale or the native scale? Inconsistent.

### P3-M19 — Reference [33] Heinrich et al. arXiv:2311.13082 publication-year cosmetics
The note "publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity" is internal bookkeeping that should not appear in a published bibliography.

### P3-M20 — Bayes factor "decisive on Jeffreys' scale"
log₁₀ B = +3.85 from a delta-function-vs-broad-prior calculation does not warrant "decisive" framing. Jeffreys' scale was designed for properly-marginalized hypotheses with sensible priors; comparison to a delta function inflates the factor by arbitrary amounts.

---

## MINOR findings

### P3-Mi1 — Duplicate phrasing in §III A
"Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE classification ... galaxies are flagged as anomalous at ∼20 times the rate of QSOs (0.75% vs. 0.037%), with anomalies peaking at z ∼ 0.75 compared to z ∼ 0.93 for normal spectra. The three highest-scored anomalies are Z-dominant" — duplicates the preceding paragraph almost verbatim. Delete one copy.

### P3-Mi2 — "z-scored" disambiguation paragraph
The "(note: 'z-scored' here is the statistics term…; spectroscopic redshift is always written z…; the anomaly score S is never called 'z' in this paper to avoid ambiguity)" inline aside is bizarre and belongs in a footnote at most.

### P3-Mi3 — Fig 2 caption "three main spectroscopic surveys"
But the figure only shows DESI, LAMOST, SDSS. Mark this clearly; the word "three" suggests three subplots when only two are shown.

### P3-Mi4 — Fig 9 panel labels printed as "AE = 83518" etc.
The panel label scale (AE = 9240, 17663, 83518) is on a different normalization from the rest of the paper's S values (max ~25 in DESI). Either rescale or document the relationship.

### P3-Mi5 — Acronym "BigAE" never expanded
First use should expand. "Big Auto-Encoder"? Unstated.

### P3-Mi6 — "Path-C rebuild protocol" never defined in abstract before use
The abstract refers to "A Path-C rebuild protocol resolves cross-transfer artifacts" without telling the reader what Path-C means. See P3-E4.

### P3-Mi7 — "Brutal honesty" prose in Conclusions
"The LAMOST 98% blue-excess artifact demonstrates that unsupervised anomaly rankings are only as reliable as the training set is representative; multi-architecture validation and training-set diversity are mandatory for future large-scale campaigns." This is a textbook ML truism, not a "methodological lesson."

### P3-Mi8 — eROSITA "Rosatom proprietary control"
Geopolitical aside is gratuitous; cite the formal DR1 release scope description instead.

### P3-Mi9 — Reference [12] "MNRAS (2026, in press)"
2026 in-press for a paper submitted in (apparently) 2025 is unverifiable. Confirm.

### P3-Mi10 — "(Fig. ??)" broken references
§II A: "architecture shown schematically in Fig. ??". §II B: "(Fig. ??)". §III B: "Figure ??". Three broken figure references. Page 2, 2, 5.

### P3-Mi11 — Section §VI D table contains internal IDs "(a)", "(b)" ... "(j)" with cryptic resolutions like "C = resolved in paper" — looks like a residual to-do tracker, not a results table.

### P3-Mi12 — "checksum 1812395110" appears in §VI D (i)
Internal reproducibility hash. Move to data repository or appendix; not appropriate in main text.

### P3-Mi13 — "GPU-blocked at the time of submission" (Appendix F)
Project-management language. Replace with "deferred to future work."

### P3-Mi14 — Bibliography uniformity
Reference [1] DESI Collaboration cites only "DESI DR1 documentation" — no journal, no arXiv ID, no DOI. Reference [2] no volume number. Standardize.

### P3-Mi15 — Figure 8 axis labels
"Multi-tracer Fisher σ(f_NL) vs. tracer number density n̄" — the figure y-axis values (~11–17) do not match §V's headline σ(f_NL) ≈ 8.14. The appendix uses a different fiducial. Explain or remove discrepancy.

---

## NITS

### P3-N1 — "Independent Researcher, Los Angeles" — no acknowledgments to co-authors but acknowledgments section thanks RunPod (commercial GPU rental). Reads as a self-promotion.

### P3-N2 — "houston@hubify.com" — commercial domain in a single-author PRD submission.

### P3-N3 — Wording "The catalog, model weights, and reproducibility scripts are publicly released" at end of abstract, contradicted by §VII data-availability "private pending arXiv acceptance."

### P3-N4 — Repeated use of "headline" as a noun is journalistic, not scientific.

### P3-N5 — Em-dash overuse throughout.

---

## Summary recommendation

**REJECT**

This manuscript does not meet PRD's standards on multiple essential axes. The headline f_NL result is consistent with no improvement (P3-E1); the NANOGrav Bayes factor compares against a delta-function SMBHB prior in a way that inflates the conclusion by orders of magnitude (P3-E2); the "largest-scale" framing is propped up by a survey (LAMOST) the authors themselves identify as a 98% training-bias artifact (P3-E3); injection-recovery gates fail catastrophically on three of six surveys whose anomaly catalogs are nevertheless included in the headline count (P3-E5); a primary figure (Fig. 7) does not match its caption (P3-E6); internal version-control language ("Path-C") infests the abstract, title implications, and main text (P3-E4); and three only-loosely-related contributions are bundled into 20 pages at a depth insufficient for any single one (P3-E9). The work is potentially salvageable as two separate, much shorter papers — a focused anomaly-catalog data release with honest completeness disclosures, and a separate null-result methodological note on multi-tracer biasing — but it cannot be accepted in current form, and the scope of revision exceeds what "major revisions" can capture.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Second Pass (Fresh Eyes)

After re-examining the paper with the audit categories above, several substantial issues escaped the initial review. I focus on arithmetic mismatches, internal inconsistencies between abstract/body/appendices, and figure-caption conflicts. Findings are numbered P3-A# (arithmetic/audit) to distinguish from the first pass.

---

## NEW ESSENTIAL findings

### P3-A1 — Abstract σ(f_NL) = 8.14 and "7.9% improvement" are arithmetically inconsistent

Direct check: (σ_std − σ) / σ_std = (8.98 − 8.14) / 8.98 = **9.35%**, not 7.9%.

Where does 7.9% come from? Appendix C's *linear-scaling* formula: ∂σ/∂α ≈ −3.66 ⇒ σ ≈ 8.98 − 3.66 × 0.19 = **8.28** ⇒ (8.98 − 8.28)/8.98 = 7.8% ≈ 7.9%. So:

- σ = 8.14 is from the Fisher-positivity formula 1/σ² = F₀ + cα² with c = 0.0747.
- 7.9% is from the linear scaling σ ≈ 8.98 − 3.66α.

These are different formulas with different baselines. The abstract reports the central value from one and the relative improvement from the other. Caveat (i) in §VI D explicitly notes the two formulas disagree near α = 0 — the abstract then conflates them anyway. Either σ = 8.14 with 9.35% improvement, or σ = 8.28 with 7.9% improvement; not both.

### P3-A2 — Figure 8 (Appendix D) uses a completely different Fisher baseline than the main text

The figure annotations are explicit:
- "Ideal (dense limit) σ = **11.71**"
- "Baseline multi-tracer σ = **12.72**"
- Single-tracer baseline shown at σ = **16.85**

But the main text uses σ_std = **8.98** (single-tracer DESI QSO baseline) and reports central multi-tracer σ in the range 8.14–8.43. The Appendix D figure thus characterizes a fundamentally different Fisher analysis (different k_max, different fiducial tracer count, different binning) and presents its sparse-tracer degradation curve as if it informs the headline §V result. The 15–30% Heinrich et al. penalty cited as applicable to σ = 8.14 was actually computed on the σ = 12.72 system. This connection is unjustified and must be either reconciled or removed. As presently written, Appendix D does not support the conclusions §V draws from it.

### P3-A3 — NANOGrav posterior σ inconsistent with quoted 68% CI

§V A: "γ = 2.567 ± 0.382 (median 2.591, 68% CI [2.304, 2.882])."

Direct check of the 68% CI half-width: (2.882 − 2.304) / 2 = **0.289**, not 0.382. The mean and median nearly coincide (2.567 vs 2.591), so the posterior is approximately symmetric and σ_RMS should approximately equal the half-CI. A factor 0.382 / 0.289 = 1.32 discrepancy between the two suggests either (i) σ is mis-quoted, (ii) the CI is from a different chain/diagnostic, or (iii) the posterior has very heavy tails (in which case quoting "γ = 2.567 ± 0.382" and computing "+1.13σ" using σ_RMS is methodologically wrong; one should use the CI).

If σ = 0.289 (matching the CI), then:
- Matter-bounce deviation: (3.0 − 2.567)/0.289 = **+1.50σ** (not +1.13σ).
- SMBHB deviation: (4.33 − 2.567)/0.289 = **+6.10σ** (not +4.61σ).

The sign and magnitude of the SMBHB tension changes substantially depending on which σ is used. The headline "decisive" Bayes factor (already objected to in P3-E2) is further undermined by this ambiguity. Reconcile the two numbers before any cosmological inference is drawn.

### P3-A4 — "21.5×" and "~6500×" rate compressions characterize the S > 5 tail only; they are not catalog-size compressions

Abstract: "21.5× LAMOST rate compression and ~6500× SDSS rate compression after native retraining."

Tracing the numbers:
- LAMOST: cross-transfer S > 5 yields 44,075; native S > 5 yields 2,054. Ratio 44075/2054 = 21.5. ✓
- SDSS: cross-transfer S > 5 yields 77,905; native S > 5 yields 12. Ratio 77905/12 ≈ 6493. ✓

But the **published catalogs use top-1% thresholds, not S > 5**:
- LAMOST native catalog = 113,342 objects (larger than cross-transfer 44,075, a 2.6× *expansion*).
- SDSS native catalog = 77,905 objects (identical to the cross-transfer count by construction; both are top-1% slices).

So the published LAMOST catalog *grew* and the SDSS catalog stayed the *same size*. The "21.5×" and "6500×" describe only the high-S tail behavior under a non-canonical threshold the published catalogs do not use. Presenting these as headline rebuild results in the abstract is misleading. The actual catalog-level effect of native retraining is: zero size change for SDSS top-1%, 2.6× growth for LAMOST top-1%.

### P3-A5 — The "1σ envelope" on σ(f_NL) is a Fisher-positivity construction artifact, not a confidence interval

The envelopes [3.92, 8.98] for the main forecast and [0.94, 8.98] for the Gold+Silver subset both have upper edges equal to σ_std = 8.98. This is because:

For the GS case, α_GS,jk = 1.83 ± 2.03 has 1σ interval α ∈ [−0.20, +3.86] crossing zero. Under 1/σ² = F₀ + cα², σ takes its maximum at α = 0 (where σ = σ_std = 8.98). So the envelope upper edge is the baseline by construction.

Practical consequence: any α with 1σ interval crossing zero produces an envelope upper edge of 8.98. A null result (α consistent with zero at any significance) yields the same upper edge. The "envelope" therefore does **not** decrease as data quality improves until α is detected away from zero — i.e., the envelope is informative only for non-null detections of α, exactly the regime the paper does not have. Reporting [0.94, 8.98] as a 1σ envelope when α is consistent with zero conveys no statistical content.

This should be labeled as a projected envelope under a positivity-constrained model, not a 1σ Gaussian uncertainty, and the asymmetry should be flagged explicitly as a construction artifact.

### P3-A6 — Figure 7 superimposes three categorically incomparable test types on a single recovery-fraction-vs-injection-amplitude axis

The figure shows recovery curves for spectroscopic continuum/emission injection (SDSS, LAMOST) and photometric latent/variability-axis injection (eROSITA, Gaia). The caption then states "Three surveys PASS the gate at 5σ" and lists Planck (Gaussian-bump injection on 64×64 maps) and NEOWISE (ecliptic-pole **mask retention**) as part of that pass count.

NEOWISE's "1000/1000 = 100% at |b_ecl| > {85°, 82°, 80.5°}" is not a signal-injection-and-recovery test. It is a test of whether a mask removes objects from the catalog — i.e., a passive cut-application test with no planted signal, no noise σ, no completeness metric. Calling it an "injection-recovery PASS" is a category error.

Planck uses Gaussian-bump injection on flat 2D map patches; the noise σ for that test is map-pixel noise, not the spectroscopic continuum noise on the x-axis of Fig. 7 for the other curves. The shared x-axis ("Injection amplitude (× noise σ)") therefore conflates units across very different statistical regimes. This should be three separate panels, and NEOWISE should not appear in this figure at all.

---

## NEW MAJOR findings

### P3-A7 — "73×" and "141×" novelty multipliers do not isolate methodological improvement from data-volume growth

Abstract: "The point-source tier is ~141× the size of the largest prior single-survey anomaly catalog [11]; the DESI-only axis (195,829 anomalies) is a ~73× like-for-like increase."

Liang et al. [11] reports 2,685 anomalies from ~250,000 DESI EDR spectra (1.07% rate). This paper reports 195,829 from 22.5M DESI DR1 spectra (0.87% rate). The DESI DR1/EDR data-volume ratio is 22.5M/0.25M = **90×**. So the 73× catalog growth corresponds to a per-spectrum anomaly *rate that is lower* than Liang's. The 73× factor reflects data availability (DR1 vs EDR), not methodological scaling. The "like-for-like" framing is unsupported — the appropriate comparison would be at fixed input volume or fixed per-spectrum rate, not at total anomaly count.

### P3-A8 — Two-estimator α inconsistency under-disclosed

§V reports two bias estimators on the same data: α_geo = 0.27 and α_jk = 0.19 ± 0.65. The paper "adopts α_jk as the headline." But α_geo = 0.27 propagates through 1/σ² = F₀ + cα² to:
1/σ² = 0.0124 + 0.0747 × 0.0729 = 0.01785 ⇒ σ = 7.49 (16.6% improvement).

The two estimators of the *same quantity* give 7.9% and 16.6% improvements. The choice of estimator changes the headline by 2×. No justification is given for selecting α_jk over α_geo; this should be a pre-registered choice or both should be reported in the abstract.

### P3-A9 — Equation (E1): the ρᵢ definition is convention-dependent and dimensionally ambiguous

The relation log₁₀ ρᵢ = ½[2 log A − log(12π²) + (γ−3) log f_yr − γ log fᵢ − log T_obs] derives from ρᵢ² = (A²/12π²) f_yr^(γ−3) f_i^(−γ) (1/T_obs). The ρᵢ here is the bin-integrated residual amplitude, with units [time²·Hz × Hz] → [time²] if A is dimensionless. But A in standard NANOGrav convention has units that depend on the f_yr reference. The equation should explicitly state (i) the units of A (yr^((γ−3)/2)? dimensionless?), (ii) that ρ_i² is the bin-power integral, and (iii) the f_i grid. As written, a reader cannot reproduce the likelihood evaluation from Eq (E1) alone.

### P3-A10 — Inconsistent σ(f_NL) baselines across §V, Appendix C, Appendix D

Three different "single-tracer baselines" appear:
- §V (main): σ_std = 8.98.
- Appendix C Table VII: same fiducial, σ_std = 8.98. ✓ consistent.
- Appendix D Fig 8: single-tracer baseline = 16.85, multi-tracer baseline = 12.72.

The Heinrich et al. SPHEREx-only forecast is σ ≈ 0.7 (cited in §I). So the paper presents σ values 0.7, 8.98, 16.85 for nominally the same observable. Each is from a different fiducial setup, but the relationships between them are not stated. A table or paragraph reconciling the three Fisher baselines and clarifying which applies to which claim is required.

---

## NEW MINOR findings

### P3-Mi16 — Fig 9 panel "AE" values span four orders of magnitude (5.30 to 83,518)

The DESI canonical S range is 5.0–25.2 (Table VI, body). Panel labels in Fig 9 report AE = 5.30, 9240, 6075, 17663, 8280, 5731, 6512, 3768, 4058, 83518. Values like 83,518 cannot be DESI canonical-S scores. These appear to be raw MSE × scale factors or values from a different score axis (possibly the cross-transfer scale). Either rescale all values to canonical S or label the axis used. As displayed, the figure's headline scores are uninterpretable.

### P3-Mi17 — Spearman ρ = −0.03 on 2,670 spectra check

For n = 2,670, standard error on ρ is ~1/√(n−1) ≈ 0.0194. |ρ|/SE = 1.55, two-sided p ≈ 0.12. ✓ checks out.

### P3-Mi18 — Spelling/conjunction: "DESI×SDSS cross-matches include a time-variable source ... and an uncataloged BAL QSO"

The abstract lists two but §IV C lists three (the known 2QZ QSO is the third). The abstract's phrasing "Three DESI×SDSS cross-matches include ..." with two examples is grammatically OK but the third (known QSO at z ≈ 1.55) is the actual confirmation of the cross-match approach. Worth noting since it is the only non-novel detection and validates the methodology.

### P3-Mi19 — "5,384 QSO-candidate sample" un-sourced in abstract

The 5,384 figure is not derived from any number shown in Table I, §III A, or Appendix B. Where does the QSO-candidate selection from the 195,829 DESI anomalies come from? Not shown in the body in a way that yields 5,384.

### P3-Mi20 — 7-way dedup numbers consistent but require justification of 5″ radius

For surveys with positional accuracies ranging from ~0.05″ (Gaia) to ~10″ (eROSITA), a single 5″ matching radius will produce false matches for the X-ray catalog and miss matches for Gaia at the survey's intrinsic precision. Use survey-pair-dependent matching tolerances; report the sensitivity of the 637 cross-matches to the choice of radius.

### P3-Mi21 — Cross-transfer baseline total arithmetic

Verified: 195,829 + 77,905 + 44,075 + 298 + 200 + 500 + 436 = 319,243; adding quarantined ACT (200) → 319,443. ✓ All values match.

### P3-Mi22 — Path-C total: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493

Verified ✓. Minus 10,213 dedup = 378,280 ✓. All canonical sums check out arithmetically; the headline number is internally consistent, even if its scientific interpretation is challenged (P3-E3).

### P3-Mi23 — Table II count sums to 77,905

41,065 + 25,733 + 6,099 + 1,232 + 1,164 + 780 + 547 + 520 + 384 + 381 = 77,905 ✓.

### P3-Mi24 — Polar-cap solid-angle calculation

|b_ecl| > 80° fraction of sphere = 1 − sin(80°) for each pole, ×2 = 2(1 − sin 80°) = 2(0.0152) = 0.0304... wait. Solid-angle cap from pole to angle θ_pole: Ω = 2π(1 − cos θ_pole). Both polar caps with |b| > 80° span θ_pole < 10° each: Ω = 2 × 2π(1 − cos 10°) = 4π × 0.01519. Sphere = 4π. Fraction = **1.519%**. Paper says 1.52%. ✓ And 17/436 = 3.90%; 3.90/1.52 = 2.57 ≈ 2.6×. ✓ Arithmetic correct.

### P3-Mi25 — Bayes factor arithmetic

3.23 / (4.52×10⁻⁴) = 7,146 ≈ 7.14×10³ ✓. log₁₀ = 3.854 ≈ +3.85 ✓. (Decisiveness interpretation still problematic per P3-E2.)

### P3-Mi26 — NANOGrav σ deviation arithmetic checks (assuming quoted σ = 0.382)

(3.0 − 2.567)/0.382 = 1.133 ≈ +1.13σ ✓.
(4.33 − 2.567)/0.382 = 4.615 ≈ +4.61σ ✓.
Arithmetic is internally consistent. (But σ itself is inconsistent with the CI — see P3-A3.)

### P3-Mi27 — Anomaly rate Table I cross-checks

DESI: 195,829 / 22,504,897 = 0.8702% ≈ 0.87% ✓.
SDSS: 77,905 / 2,304,830 = 3.380% ≈ 3.38% ✓.
LAMOST: 44,075 / 11,418,594 = 0.386% ≈ 0.39% ✓.
eROSITA: 298 / 930,203 = 0.0320% ≈ 0.03% ✓.
All Table I rates check out.

### P3-Mi28 — Liang et al. comparison: per-spectrum rate is *lower* in this work

This paper: 0.87% on DESI DR1; Liang et al.: 1.07% on DESI EDR. The threshold S > 5 and Liang's normalizing-flow detector are different methods, so direct rate comparison is not strictly fair, but the abstract's "consistent with the 1.07% rate" framing in §VI E should acknowledge that 0.87 < 1.07 and that the lower rate is at least partly due to a more stringent threshold being imposed by the author's MSE-z-score parameterization. This is not a "stable property of the DESI population" — it's a threshold-dependent quantity.

---

## NIT additions

### P3-N6 — "Empirical Landy–Szalay" terminology
LS is the standard estimator; calling its application "empirical" suggests there's a non-empirical alternative. Just say "Landy–Szalay angular two-point analysis."

### P3-N7 — "Native-Trained" in title
The neologism "Native-Trained" (vs. "natively trained" or "per-survey trained") is not standard in the ML or anomaly-detection literature. The title's "Native-Trained Novelty Fractions" reads as jargon.

### P3-N8 — "Path-C unique" appears in Table I row header
Internal version label leaks into a published table. Already P3-E4.

### P3-N9 — Appendix F internal language
"GPU-blocked at the time of submission," "Path-C-final catalog," "Path-C protocol forbids retaining a survey on a checkpoint" — project-internal phrasing throughout.

---

## Summary of the second pass

The second-pass arithmetic audit reveals that the abstract's headline f_NL improvement is internally inconsistent (P3-A1), the supporting Appendix D figure uses a different Fisher baseline entirely (P3-A2), the NANOGrav posterior σ does not match its quoted 68% CI (P3-A3), and the "rate compression" headlines describe a tail behavior that the published catalogs do not exhibit (P3-A4). The Fisher-positivity envelope is shown to be a construction artifact rather than an uncertainty (P3-A5), and Figure 7 conflates three incompatible test types under a misleading common axis (P3-A6).

Combined with the first-pass essentials (overclaim of "largest," delta-function Bayes factor against SMBHB, version-tagged nomenclature, gate-failed surveys in the headline), the manuscript exhibits a consistent pattern: every quantitative claim that could be checked either has an arithmetic discrepancy with adjacent numbers, mixes formulas/baselines without disclosure, or relies on a non-standard statistical construction that inflates the apparent result.

**Updated recommendation: REJECT** — the second pass strengthens the original conclusion. Beyond the scientific and scoping concerns of the first pass, the paper does not satisfy basic numerical-consistency standards expected of a PRD submission. A revision would need to: (i) reconcile P3-A1 through P3-A4 with single, consistent numbers throughout abstract/body/appendices; (ii) re-do or remove Fig. 7 with comparable test types only; (iii) re-do the NANOGrav statistic with consistent σ; and (iv) drop the f_NL forecast or re-frame it explicitly as a null result. After these changes the resulting paper would be roughly 8–10 pages and could be considered as a shorter methods note, possibly at PRD or a more appropriate venue (MNRAS for the catalog; JCAP for any remaining cosmology fragment).