# P3 auto-2026-06-08_1819pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (19135 chars)
**Wall time**: 549.3s

---

# Referee Report: Brutal-Honesty Review of P3

**Manuscript:** "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies..."

**Journal target:** Physical Review D

---

## Overall assessment

This is not a Physical Review D paper. It is a heterogeneous mega-catalog manuscript that splices together (i) an autoencoder-based source catalog from seven archives, (ii) an unrelated Fisher forecast for SPHEREx, and (iii) an unrelated NANOGrav spectral-index re-fit. The cosmology content that nominally justifies PRD scope is fragmentary, derivative, and in two places **inconsistent with its own arithmetic**. The catalog itself, while large, is built almost entirely from reconstruction-MSE rankings with **three of six injection-recovery gates failing at 5σ**, no spectroscopic follow-up of any object, and a "novelty" headline that the authors themselves admit overstates the discovery rate by a factor of ∼5.6. The body is saturated with internal-bookkeeping language ("Path-C," "cross-transfer baseline preserved as before/after diagnostic," "exploratory tier retained as methodological lesson," "quarantined as cross-transfer artifact") that reads as a review-log artifact, not a finished paper.

I recommend **REJECT**.

---

## ESSENTIAL findings

### P3-E1 — Arithmetic inconsistency in headline σ(f_NL) improvement (Abstract, §V, §VII)

The abstract, §V, and Conclusions all state: **"σ(f_NL) = 8.14 ... (7.9% improvement)"** with baseline σ(f_NL)^std = 8.98.

Direct recomputation:
- (8.98 − 8.14) / 8.98 = **9.35%**, not 7.9%.
- The Fisher form 1/σ² = F₀ + cα² with F₀ = 1/8.98², c = 0.0747, α = 0.19 gives σ = 8.139 (confirms 8.14).

So the σ(f_NL) value is internally consistent with α=0.19, but the **7.9% number is wrong by ≈1.5 percentage points** — it appears to be carried over from the older fixed-α=0.15 linear-scaling result (which is, in Appendix C Table VII, listed at 6.1% for α=0.15 and would extrapolate to ≈7.7% at α=0.19). The Fisher value supersedes the linear scaling, so the headline improvement should be 9.4%, not 7.9%. This error appears in the abstract, §V Fisher forecast paragraph, and the Conclusions item 5.

**Required fix:** Recompute. Reconcile all four locations. If 7.9% is correct, σ(f_NL) cannot be 8.14.

### P3-E2 — "Rate compression" framing is materially misleading

The abstract claims **"21.5× LAMOST rate compression and ∼6500× SDSS rate compression after native retraining"** as evidence the Path-C rebuild fixed cross-transfer artifacts. The body confirms this compression refers to applying a strict S>5 cut: LAMOST drops from 44,075 → 2,054; SDSS from 77,905 → 12.

But the **released** Path-C LAMOST catalog is 113,342 (top-1%) — *more* anomalies than the cross-transfer scan, not fewer — and the released Path-C SDSS catalog is 77,905 (top-N native slice at S≥0.1060). The "compression" exists only at a threshold that was *not* used to construct the published catalog. The headline arithmetic in the abstract is engineered: the diagnostic uses a strict cut, the catalog uses a percentile cut, and the reader is not warned at the point of the claim.

**Required fix:** Either (a) release the strict-cut catalogs (2,054 LAMOST, 12 SDSS) as the science result, or (b) remove the "compression" language from the abstract and acknowledge that the released native catalogs are *larger* than the cross-transfer scan they replaced.

### P3-E3 — Three of six injection-recovery gates FAIL at 5σ; catalog still presented as validated

§II D, §III, and Fig. 7 disclose that LAMOST (5.8%), Gaia (5.2%), and eROSITA (1.2%) **fail** the 50% recovery gate at 5σ. The authors retain these surveys via a "FAIL-with-diagnostic" label backed by IsolationForest cross-validation stability (Gaia 41.0%, eROSITA 81.5%). 41% IF-stability is **not** a validation — it is direct evidence that 59% of the Gaia top-1% set is detector-noise-dependent. The authors nonetheless count 113,342 LAMOST + 500 Gaia + 298 eROSITA = **114,140 objects** (∼30% of the headline) in catalogs that did not pass any quality gate.

**Required fix:** Either remove failed-gate surveys from the headline 378,280 count, or relabel the catalog's headline to exclude them ("validated-gate primary tier" with explicit count) so the abstract reflects what was actually validated.

### P3-E4 — Bibliography contains a future-dated, unverifiable reference

Reference [12], Nicolaou et al., is listed as "Mon. Not. Roy. Astron. Soc. (**2026**, in press)." The manuscript is dated June 2026. An "in press" citation to a journal in the manuscript's own month of submission, with no arXiv ID provided (compare [11] which has 2307.07664), is unverifiable. Either provide arXiv ID or remove.

### P3-E5 — Internal-audit / version-history language embedded throughout the body

The body is permeated with bookkeeping prose that does not belong in a published paper. Examples (not exhaustive):
- "Path-C" branding (>50 instances) — implies the existence of Paths A and B.
- "Cross-transfer baseline preserved as before/after diagnostic" (§II D, Table I, Fig. 1 caption, Fig. 2 caption, Fig. 3 caption, §III A–F repeatedly).
- "ACT DR6 quarantined as a cross-transfer artifact" (abstract, §II D, Table I, §III F, Appendix F).
- "Retained as a methodological lesson" / "exploratory tier retained" (abstract, §III D, §VII).
- Table IV — literally a residual-caveat audit list inside the body, with header "C = resolved in paper."
- "What this appendix is not" (Appendix F) — explicit guard-rail prose against misuse.
- "9.7× improvement post-native-retrain" (Fig. 7 caption), "(9.7× improvement over emission-line variant)" (§III D) — relative-improvement framing of a failed gate.
- Repeated re-statements of the same gate decomposition ("3 PASS / 3 FAIL-with-diagnostic") in abstract, §II D, §III, §VI D, Fig. 7, §VII.

**Required fix:** Strip all version/round/diagnostic language. Present the final catalog as if no prior path existed. Move audit tables to supplementary material.

### P3-E6 — Headline σ values from incompatible procedures juxtaposed without "not directly comparable" warning

Throughout, the paper places side-by-side:
- α_jk = 0.19 ± 0.65 (jackknife from a single sample; 0.29σ from null);
- σ(f_NL) = 8.14 (Fisher forecast assuming zero observational systematics, central-value plug-in of α);
- "1σ envelope [3.92, 8.98]" (propagated by inserting α±σ_α into the Fisher form);
- NANOGrav +1.13σ (parameter-shift Gaussian-approx mean ± std) vs. +1.40σ (if using quantile form γ = 2.591⁺⁰·²⁹¹).

These are different statistical operations on different likelihoods. The paper uses Gaussian-approx σ=0.382 for the SMBHB-rejection significance and quantile σ for the credible interval, picking whichever is more favorable, without flagging at every juxtaposition that they are not directly comparable. The Savage-Dickey B_MB/SMBHB = 7.14×10³ "decisive on Jeffreys' scale" is then placed adjacent to the +1.13σ "marginally consistent" matter-bounce shift — these are not the same hypothesis being tested.

**Required fix:** Add explicit "not directly comparable" caveats at each juxtaposition. Choose one error bar (Gaussian or quantile) and use it consistently.

### P3-E7 — Fig. 1 contradicts the abstract on archive count

Fig. 1 title: **"Spatial distribution of all 319,443 anomalies across 8 archives"** — includes ACT DR6 — placed on page 4 as the lead spatial figure. The abstract states ACT DR6 is quarantined and the canonical catalog spans seven archives. The figure caption attempts to rescue this by noting "ACT DR6 is quarantined and excluded" but the title still says 8 archives, and the legend shows ACT DR6 as a populated category. A reader scanning the figure will count 8.

**Required fix:** Replot showing only the 7 retained archives, with the canonical 378,280 (or 378,080 point-source) population. The cross-transfer baseline plot belongs in a supplementary appendix at most.

### P3-E8 — Fig. 5 conflates "SIMBAD-unmatched" with "novelty fraction"

Fig. 5 x-axis is labeled **"SIMBAD novelty fraction (%)"** and the figure title is **"Fraction of anomalies absent from SIMBAD"**. These are not the same quantity, as the body explicitly states (§IV A): the SIMBAD-unmatched fraction "substantially overstates true catalog novelty." Labeling the axis "novelty fraction" and then disclaiming it in caption text is precisely the kind of figure-caption-vs-body inconsistency PRD reviewers flag.

**Required fix:** Relabel axis "SIMBAD-unmatched fraction (%)." The word "novelty" must not appear on a figure that does not measure novelty.

---

## MAJOR findings

### P3-M1 — "Largest" / "∼141×" framing depends on a non-like-for-like comparison

The abstract claims "∼141× the size of the largest prior single-survey anomaly catalog [11]" and "the DESI-only axis (195,829 anomalies) is a ∼73× like-for-like increase." Liang et al. [11] applied a normalizing-flow autoencoder to ∼250k DESI EDR spectra and reported 2,685 anomalies; here the authors apply a different (deterministic FC) autoencoder to 22.5M spectra. The 73× factor is *anomaly count* scaling with *sample size* scaling — i.e. the authors went 90× larger in input and got 73× more anomalies. This is not a methodological advance; it is a data-volume scaling. Reframe.

### P3-M2 — α_jk = 0.19 ± 0.65 is consistent with zero; abstract framing implies a measurement

The abstract says "yields α_jk = 0.19 ± 0.65 (< 1σ from null)" and immediately gives a "central forecast σ(f_NL) = 8.14". A measurement that is 0.29σ from null is a non-detection. The "central-value forecast" framing implies a number that the authors do not actually have. The honest version is: "No bias enhancement is detected (α = 0.19 ± 0.65, consistent with zero at 0.3σ). The Fisher forecast at the central value would yield σ(f_NL) = 8.14 but is consistent with the no-enhancement baseline 8.98." The current abstract phrasing leads with the apparent improvement.

### P3-M3 — NANOGrav fit is unrelated to the anomaly catalog

§V A re-fits a published NANOGrav 15-yr KDE free-spectrum likelihood with a single-template power law, with no use of the catalog presented in this paper. This belongs in a separate PTA-methods paper. It inflates the abstract with a "+4.61σ rejection of SMBHB" claim that has nothing to do with autoencoder anomaly detection. Remove or move to appendix only.

### P3-M4 — "Recommended catalog-grade subset is ∼265,000" is not derived

Abstract: "recommended catalog-grade subset is ∼265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE)." Summing the cited surveys: 195,829 + 77,905 + 298 + 500 + 419 = 274,951 before deduplication. Subtracting the deduplication implied by the 7-way 5″ procedure would not bring this exactly to 265,000. The "∼265,000" appears nowhere in the body with a derivation. State the exact value.

### P3-M5 — SDSS native re-score covers 1,925,279 of 2,304,830 spectra (84%)

Footnote ‡ to Table I: "SDSS native re-score complete across **1,925,279** DR18 spectra." Table I row gives N_total = 2,304,830. The Path-C native catalog therefore does not cover ∼380,000 SDSS DR18 spectra (16%). This is never explained. Did these fail QA? Were they not native-trainable? The headline 77,905 SDSS Path-C count is drawn from a sub-catalog whose selection function is undocumented.

### P3-M6 — "12 high-z QSO candidates" reported without spectroscopic confirmation

§III B claims 12 z ≈ 6 quasar candidates with three signatures. The signatures (Gunn-Peterson trough, Z-arm dominance, line detection) **are themselves the anomaly-detection features**, so this is a circular selection. No external photometry, no Ly-α line wavelength measurement, no continuum-slope confirmation, and crucially no follow-up spectroscopy is reported. The claim "consistent with z = 6.0–6.23" is not a measurement of redshift. Reframe as "tentative candidates" and quantify expected contamination from low-z dust-reddened sources.

### P3-M7 — "TIC 374313355 ... time-variable source" inflated to a discovery

§IV C item 2 (and Conclusions) headline the cross-survey match TIC 374313355 with "SDSS anomaly score = 49.5." Fig. 6 (c,d) shows the SDSS spectrum is dramatically higher than DESI — but the reconstruction (red dashed) does not fit. The score 49.5 reflects model failure on a bright source, not necessarily astrophysical variability. The paper offers no light curve, no TESS photometry, no companion catalog cross-match for variability classification. A score of 49.5 in a paper where the catalog threshold is S > 5 is suspicious without instrumental-systematics analysis.

### P3-M8 — BAL QSO at z ≈ 0.86 is not localized in the paper

The "uncataloged BAL QSO at z ≈ 0.86" appears in the abstract, §IV C, and Conclusions but no coordinates, no DESI TARGETID, no redshift uncertainty, and no equivalent-width measurement of the Mg II trough are given. Fig. 6(e,f) shows a spectrum but the absorption identification is not labeled or measured. For a "highlighted discovery" the documentation is insufficient.

### P3-M9 — The NANOGrav posterior is reported with two contradictory error bars

§V A: "γ = 2.567 ± 0.382 (Gaussian-approximation: posterior mean ± sample standard deviation; equivalent quantile summary γ = 2.591⁺⁰·²⁹¹₋₀.₂₈₇)." The +1.13σ matter-bounce shift uses σ = 0.382; the credible interval uses σ ≈ 0.29. The footnote acknowledges this and chooses the wider σ for the parameter-shift test. This choice is statistically incorrect — a posterior-shift test should use the posterior-likelihood at γ=3.0, not pick the larger of two summary widths. Recompute properly (Savage-Dickey at γ=3 or full posterior integral).

### P3-M10 — Eq. (E1) is dimensionally ambiguous

The matter-bounce template log₁₀ ρᵢ has units issues that are not stated: ρᵢ is presumably PSD in seconds (or strain² per Hz), but ½[2log₁₀A − log₁₀(12π²) + (γ−3)log₁₀ f_yr − γ log₁₀ fᵢ − log₁₀ T_obs] mixes A (dimensionless characteristic-strain amplitude), frequencies (Hz⁻¹ logged), and T_obs (years vs. seconds?). State the units of A, fᵢ, T_obs, and ρᵢ explicitly. The factor 12π² is the convention-dependent normalization and the convention should be cited.

### P3-M11 — "Genuine novelty fraction ∼17.8%" is a single-sample point estimate

§IV A and the abstract correctly note "single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested." Yet the abstract leads with the number as if it characterizes the catalog. Either (a) extend the CDS X-Match to the full ∼195k DESI anomaly catalog (the limiting factor is web-service rate, not science), or (b) demote the 17.8% to an illustration and refrain from quoting it as the headline novelty rate.

### P3-M12 — eROSITA "Novel" SIMBAD column in Table III conflates absence with novelty

All five top-5 eROSITA sources are labeled "Novel" in Table III's SIMBAD column. This is the same conflation flagged in P3-E8: SIMBAD-absent ≠ novel. The very same paper argues (§IV A) that NED+VizieR resolves 100% of SIMBAD-absent samples for SDSS top-20. Re-cross-match the eROSITA top-5 against the 20-catalog X-Match suite (which the authors already use for DESI top-1,000) before labeling anything "Novel."

### P3-M13 — Spatial uniformity χ² is admitted to be uninterpretable, yet still reported

§IV B states explicitly: "Caveat on the χ² figure: the significant χ²ᵥ = 3.76 is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering." If it cannot be interpreted, do not report it as a result. Remove the χ² number.

### P3-M14 — The 5″ deduplication is acknowledged to under-match NEOWISE

§IV C: "NEOWISE has a ∼6″ PSF on the W1+W2 channels. A uniform 5″ radius is therefore strict ... NEOWISE-PSF-comparable (slightly tight)." The 378,280 headline number therefore depends on a dedup radius that is admitted to under-match one survey. State the headline as a range (e.g., 378,200–378,300 over 3″–7″ sensitivity) or rerun at the proper radius.

### P3-M15 — Abstract claim "scalar-only w=0 matter-bounce class" and SPHEREx 3–5σ projection is not derived in this paper

The abstract and §V state SPHEREx will detect f_NL = −35/8 at 3–5σ. This number is from Heinrich et al. [33], not from this paper. The authors do not provide a new forecast specific to their anomaly tracer. Remove "3–5σ" from the abstract and §V, or actually derive it.

---

## MINOR findings

### P3-m1 — Author affiliation
Single author listed as "Independent Researcher" with personal email (houston@hubify.com). PRD generally requires institutional affiliation or, if independent, a clear statement of conflict-of-interest and funding. The Hubify-Projects GitHub repo is referenced; clarify whether Hubify is a commercial entity.

### P3-m2 — Page count
20 pages is excessive for the scientific content. Strip the audit prose and the manuscript shrinks to ∼10 pages. Recommended max: 12 pages for the catalog + 1 appendix.

### P3-m3 — Fig. 9 (taxonomy gallery) labels report "AE" scores ranging 3,768 to 83,518
These appear to be raw MSE×10⁴ or similar; they are inconsistent with the canonical-S axis defined in §II B. The figure caption does not explain. Either relabel axes/labels as canonical S or define the AE quantity.

### P3-m4 — Duplicate / repeated phrases
- "before/after diagnostic" appears ∼14 times.
- "Path-C native retrain" appears ∼20 times.
- "exploratory tier" / "methodological lesson" repeated in abstract, §III D, §VI A, §VII.

### P3-m5 — Table II "Uncategorized" 52.7% renders the table nearly useless
A spectral classification table where the majority category is "Uncategorized" should not be presented as a result.

### P3-m6 — Table I footnotes are longer than the table
The Table I footnote block runs ∼50 lines and contains material that belongs in §III. Compress.

### P3-m7 — "Bounce-physics connection" appendix (Appendix E)
Reads like an apologia for why the catalog is in a "bounce" paper. The connection is not load-bearing; the catalog is independent of bounce theory.

### P3-m8 — "Hubify-Projects/bigbounce" repository
The branding "bigbounce" appears in the data URL but never in the body; this is internal-project naming leaking through.

### P3-m9 — Reference [33] "publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity"
This is a build-system note embedded in the bibliography. Remove.

### P3-m10 — Aggregate SIMBAD-unmatched 58.8%
The number 58.8% appears in Table I row and Fig. 5 dashed line, but Fig. 5 is sorted by per-survey rate (27%–99%) and the aggregate is across an inhomogeneous mixture. State weighting.

### P3-m11 — Footnote ‡ on Table I uses ∼6500× and 21.5× rate-compression diagnostic
Same as P3-E2: presented as a science result, actually a threshold-arithmetic artifact.

### P3-m12 — Inference throughput numbers in Table V do not check
DESI: 22.5M spectra at 1,142 spectra/s = 19,705 s = 5.47 h. ✓ (matches §II C). But the table reports "Train time (s) ∼3,600" for the 47k-spectrum DESI training — that's 76 epochs/min for a 660k-parameter network, implausibly fast on H200 unless heavily I/O-bound. Verify.

### P3-m13 — "ESS ≈ 5,500 (> 50τ per walker, convergence satisfied)"
With τ ≈ 58 and 10,000 production samples per walker, ESS per walker = 10,000/58 ≈ 172, summed over 32 walkers = 5,517. ✓ The "> 50τ per walker" criterion check is right but irrelevant — what matters is ESS, which is fine.

### P3-m14 — Eq. (1) and Eq. (2) — fine, but Eq. (1) double-counts a label
Eq. (1) defines MSE per-element; Eq. (2) defines S as standardized MSE. Acceptable.

### P3-m15 — Appendix C Table VII assumes linear scaling but body uses non-linear Fisher
Table VII gives σ(f_NL) at α=0.05–0.50 by "linear scaling of the fiducial 7-bin Fisher result at α = 0.15." But §V switches to the positivity-respecting form 1/σ² = F₀ + cα². The two are inconsistent at large α. Either drop Table VII or recompute under the Fisher-form.

### P3-m16 — Appendix F runs 1.5 pages explaining why ACT is excluded
The paper would be cleaner with one sentence in §II D and no appendix.

---

## NIT

### P3-n1 — Date "June 2026" on a manuscript submitted in mid-2026
Acceptable but should be replaced with submission date.

### P3-n2 — "BigAE" should be set as `\textsc{BigAE}` consistently; sometimes appears as "BIGAE" in section headers.

### P3-n3 — "DESI×SDSS" vs "DESI × SDSS" inconsistent spacing.

### P3-n4 — Fig. 6 panel (c,d) annotations: "Score = 8.1" and "Score = 49.5" — both labeled as "DESI epoch" and "SDSS epoch" but the score-label colors are inconsistent with the panel-color scheme.

### P3-n5 — Reference [12] Nicolaou et al. — no arXiv ID.

### P3-n6 — "(z-scored)" parenthetical in §II B (Eq. 2 surroundings) explicitly clarifies a notation ambiguity that the authors created themselves. Better: pick non-overlapping symbols.

---

## Recommended maximum length

If essential issues are addressed and the NANOGrav / SPHEREx-projection content is stripped: **10–12 pages** for the catalog methods + 2-page appendix for reproducibility scripts. The cosmology forecasts belong in separate companion papers.

---

## Summary recommendation

**REJECT**

This manuscript fails the PRD bar on three independent grounds: (1) at least one load-bearing arithmetic number in the abstract (the 7.9% f_NL improvement) is inconsistent with the displayed Fisher result; (2) half the survey catalogs (LAMOST, Gaia, eROSITA) fail the authors' own 5σ injection-recovery gate and are nonetheless counted toward the 378,280 headline; and (3) the manuscript is structurally a hybrid of an autoencoder catalog paper, a Fisher forecast, and a PTA spectral-index fit, with the two cosmological pieces neither derived here nor connected to the catalog. The body is saturated with internal-audit language ("Path-C," "before/after diagnostic," "quarantined cross-transfer artifact," "exploratory tier retained as a methodological lesson") that is incompatible with a finished paper. The "novelty" headline (17.8%) is acknowledged to be a single-sample point estimate; the "SPHEREx 3–5σ" projection is cited, not derived; and the highlighted "discoveries" (12 z≈6 candidates, TIC 374313355, uncataloged BAL QSO) lack the most basic follow-up or coordinate documentation expected of a discovery claim. The catalog itself may be useful as a community data product, but as a PRD article the manuscript needs to be split, recomputed, and rewritten from scratch.

---

## PASS 2 — self-critique findings (what initial review missed)

# Second-Pass Referee Report: Additional Findings

After re-reading with the checklist, I found multiple new issues — especially in the arithmetic and figure-vs-body consistency categories. The initial pass was not complete.

---

## NEW ESSENTIAL findings

### P3-E9 — The "1σ envelope [3.92, 8.98]" is mathematically inconsistent with the stated Fisher form

The abstract, §V, and §VI D (i) all claim that inserting α_jk = 0.19 ± 0.65 into the Fisher-positivity-respecting form

$$1/\sigma(f_{\rm NL})^2 = F_0 + c\,\alpha^2, \qquad F_0 = 1/8.98^2,\ c = 0.0747$$

yields **central σ = 8.14, 1σ envelope [3.92, 8.98]**.

Direct computation:
- At α = 0.19: σ = 8.139 ✓ (matches 8.14)
- At α = 0.19 + 0.65 = 0.84: 1/σ² = 0.01240 + 0.0747×0.7056 = 0.06511 → **σ = 3.92** ✓
- At α = 0.19 − 0.65 = −0.46: 1/σ² = 0.01240 + 0.0747×0.2116 = 0.02821 → **σ = 5.95**, **not 8.98**

Under the *symmetric-in-α²* Fisher form the paper itself writes down, any non-zero |α| *improves* σ. The propagated 1σ envelope is therefore **[3.92, 5.95]**, not [3.92, 8.98]. The 8.98 upper bound is the no-improvement floor (the σ value at α = 0), inserted artificially as a ceiling. This is not what "1σ envelope" means.

The same error occurs in the Gold+Silver re-measurement (§V): α_GS = 1.83 ± 2.03 with "1σ envelope [0.94, 8.98]." At α = 1.83 − 2.03 = −0.20, σ = 8.06, not 8.98. Again the 8.98 is an artificial ceiling.

**Required fix:** Either (a) report the correct envelopes [3.92, 5.95] and [0.94, 8.06], or (b) explicitly state that the upper bound is being capped at the no-improvement baseline and relabel "1σ envelope" as "1σ envelope with no-improvement floor." The current presentation makes the forecast look worse on the down side and unchanged on the up side, which is statistically the opposite of how a parameter envelope works.

### P3-E10 — Appendix C and §V use two different "single-tracer baselines"

§V and Table VII: σ(f_NL)^std = **8.98** (DESI QSO single-tracer baseline).

Appendix C Fig. 8 caption: "the dotted dark-red line marks the **single-tracer baseline (σ(f_NL) = 16.85)**" with "dense-tracer limit (σ(f_NL) = 11.71)" and "baseline multi-tracer 12.72."

These are two different baselines used to characterize the same forecast. The body's 7.9%/9.4% improvement is referenced to 8.98; the figure's shot-noise penalty range is referenced to 16.85, 12.72, and 11.71. The figure's "+1.27% to −4.97% under 15–30% shot-noise penalty" claim cannot be compared to the body's "+7.9% headline" because they use different denominators.

The body claims the 6.1% / 7.9% DESI-only improvement "is consistent with the shot-noise-degraded value across the full 15–30% Heinrich-et al. penalty range," but this consistency check is on a Fisher diagram with σ_std = 16.85, not σ_std = 8.98. The two figures cannot both be the canonical 5-tracer Fisher referenced in the same sentence.

**Required fix:** Reconcile to a single σ_std value. Either redo Fig. 8 with σ_std = 8.98, or use 16.85 throughout (and recompute the 7.9% improvement against the right baseline).

### P3-E11 — Fig. 3 title contradicts body's "3 latent-space populations" claim

Fig. 3's panel title states **"77,905 anomalies (score > 5.0), 14 clusters, 99.4% clustered."**

§III C body: "UMAP/HDBSCAN clustering of the top-50,000 cross-transfer anomalies yields **3 latent-space populations** (Fig. 3), dominated by cool dwarfs (84%)."

§VII Conclusions item 3: "SDSS anomalies cluster into **3 UMAP/HDBSCAN populations** (84% cool dwarfs M7–T2)."

The figure shows 14 HDBSCAN clusters labeled 0–13. The body collapses these into 3 "physical categories" (the right panel of Fig. 3). The text never explains the 14-to-3 collapse, never gives the cluster-to-category mapping, and uses "3 clusters" and "3 populations" interchangeably. A reader who looks only at the figure will count 14; a reader who reads the body will see 3 with no derivation of how 14 became 3.

**Required fix:** Either present 14 clusters consistently with a mapping table to the 3 physical categories, or remove the cluster numbers from the figure and present only the 3 categories.

### P3-E12 — Fig. 6 "Match 1" has anomaly scores below the DESI catalog threshold

§IV C, item 1: "Known QSO at z ≈ 1.55: independently flagged by both surveys, validating the cross-survey approach."

Fig. 6(a,b) labels: DESI score **3.2**, SDSS score **2.8**.

DESI's catalog threshold is S > 5.0 (Table I, §III A). A DESI score of 3.2 is *below* the threshold and would not be in the 195,829-source anomaly catalog. The object cannot have been "flagged by DESI." Either:
- (a) The score in the figure is a different quantity from the canonical S (in which case the figure axis is mislabeled and the cross-survey match claim is unsupported), or
- (b) The match is real but Match 1 is not actually a DESI anomaly (in which case calling it a "cross-survey match" misrepresents the 637 cluster count in §IV C).

Combined with P3-E1 / P3-E9, this is now the third arithmetic/labeling inconsistency in the f_NL/cross-survey-match block of the paper.

**Required fix:** Clarify what the score values in Fig. 6 panels represent and reconcile with the catalog threshold. If Match 1 is below threshold, remove it from the highlighted cross-survey matches.

### P3-E13 — Aggregate "58.8% SIMBAD-unmatched" cannot be reproduced from per-survey rates

Table I bottom row: "Total (cross-transfer, ACT-incl.) 37,292,042 319,443 0.86 **58.8**".
Fig. 5: dashed line marked at **58.8%** with label "Aggregate."

Computing weighted aggregate from the per-survey rates and Nanom in Table I:
- N_anom × rate sum: 195,829×0.99 + 77,905×0.90 + 44,075×0.50 + 298×0.68 + 500×0.27 + 436×0.45 = 286,555
- Sum N_anom (excluding Planck which has —): 319,043
- Weighted aggregate = **89.8%**, not 58.8%.

Unweighted (per-survey mean) = (99+90+50+68+27+45)/6 = **63.2%**.

Median of the six rates = (50+68)/2 = **59.0%**, closest to 58.8 but still not exact.

The 58.8% does not correspond to any standard aggregation of the per-survey rates. It appears to be either an undocumented median-like statistic or a stale number from a prior version. The body claims it as the "aggregate" — a term that normally implies a weighted mean.

**Required fix:** Define the aggregation method, or recompute and update the value (likely to ~89.8% if Nanom-weighted, which would make the SIMBAD-novelty headline *worse* and reframe the comparison to the 17.8% CDS X-Match rate as a ∼5× overstatement rather than ∼5.6×).

---

## NEW MAJOR findings

### P3-M16 — §VI D "caveats (i)–(v)" referenced repeatedly but only (i) and (ii) are written

The body uses two parallel labeling systems for caveats:
- **Table IV** uses **(a)–(j)** for ten "Path-C residual caveats."
- **§VI D body text** uses **(i)–(v)** lowercase roman: (i) "DESI in-sample training–test overlap" and (ii) "Injection-recovery synthesis" are written out; (iii), (iv), (v) are *never present in §VI D* but are referenced from elsewhere in the paper.

External references that point into the missing roman-numeral caveats:
- Table I footnote §: "§VI D caveat (v)" — IsolationForest cross-validation stability
- §III H: "§VI D (v)"
- §VI D (ii) header text mentions "(iv)" — "see caveat (iv)"
- §V: "§VI D caveat (i)" and "§VI D caveat (j)" — mixing the two label systems in one sentence
- §III E: "§VI D (f)" — refers to Table IV (f)

The reader has no way to find caveats (iii), (iv), or (v). The two label systems are not synchronized. §V caveat (j) is in Table IV but not in §VI D; §VI D caveat (v) is in §VI D's promised list but missing from the printed text.

**Required fix:** Unify the label system, write out caveats (iii)–(v), and audit every "§VI D (·)" reference for accuracy.

### P3-M17 — "20 curated all-sky catalogs" but body lists only 18

§IV A: "an extended cross-match of the DESI DR1 top-1,000 anomalies (ranked by score) against **20 curated all-sky catalogs** via CDS X-Match (Gaia DR3, SDSS DR12/DR16, DESI Legacy Imaging DR9, DES DR2, Pan-STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS)."

Counting the parenthetical list (treating SDSS DR12 and DR16 as separate): Gaia DR3, SDSS DR12, SDSS DR16, DESI Legacy DR9, DES DR2, PS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS = **18**.

This is the primary novelty figure of the catalog (17.8% genuine-novelty fraction). The denominator of the cross-match comparison is misstated.

**Required fix:** Either list the missing two catalogs or correct "20" to "18."

### P3-M18 — Eq. (E1) γ-coefficient on log f_i

Eq. (E1) writes the matter-bounce template log₁₀ ρ_i with coefficient **−γ log₁₀ f_i**. The textbook NANOGrav residual-PSD form is

$$P(f) = \frac{A^2}{12\pi^2 f_{\rm yr}^3}\left(\frac{f}{f_{\rm yr}}\right)^{-\gamma}.$$

Working through carefully, log₁₀ ρ_i = ½ log₁₀(P/T_obs) gives the coefficient −γ on log₁₀ f_i, consistent with the equation as printed — so the equation **is dimensionally correct** for residual amplitude (not for h_c). I withdraw the dimensional concern raised in P3-M10. However, the paper still does not state that ρ_i is the residual amplitude in seconds (or whatever unit convention) and does not give the f_yr value used. State unit conventions explicitly.

### P3-M19 — SDSS native rescore covers 1,925,279 spectra but Table I uses N_total = 2,304,830

Table I row for SDSS DR18: **N_total = 2,304,830**, **N_anom = 77,905**, **rate = 3.38%**.

But footnote ‡ states: "SDSS native re-score complete across **1,925,279** DR18 spectra (top-77,905)."

Therefore the actual Path-C native rate is 77,905 / 1,925,279 = **4.05%**, not 3.38%. The 3.38% in Table I is the cross-transfer rate using the full 2.3M denominator. The "Path-C unique" denominator in the last row (37,272,042) presumably uses the full 2.3M as well, inflating the apparent SDSS coverage by ∼20%.

This compounds P3-M5: not only is the missing 380k SDSS spectra coverage gap undocumented, but the rate denominator in Table I does not match the Path-C-native procedure that produced N_anom.

### P3-M20 — Fig. 2 caption "twelve orders of magnitude"

Fig. 2 right caption: "spanning **twelve orders of magnitude** from the threshold (S = 5) to S = 1.9 × 10¹¹."

log₁₀(1.9×10¹¹ / 5) = log₁₀(3.8×10¹⁰) = **10.58 orders**, not 12. Minor but the kind of inflation that adds up.

### P3-M21 — Self-comparison: paper's own DESI 1.07% (Liang) vs. 0.87% (this work) used inconsistently

§VI E: "Our DESI anomaly rate of 0.87% is consistent with the 1.07% rate reported by Liang et al. [11] on the DESI EDR." But the 0.87% is from a strict S>5 cut on a DESI-trained autoencoder, while Liang et al. use a normalizing-flow architecture with a different threshold criterion. Comparing rates from incommensurable thresholds and calling them "consistent" without quantifying the threshold-dependence is not a valid robustness claim.

### P3-M22 — "Top 10K" denominator switch for DESI SIMBAD-unmatched ∼99%

Table I row for DESI: SIMBAD-unmatched = "**∼99**." Body §III A: "Cross-matching the **top 10,000** anomalies against six databases (SIMBAD, NED, AllWISE, Milliquas, Gaia DR3, SDSS) finds only 0.2% in SIMBAD." So the 99% figure is from the top-10K (i.e., the SIMBAD-novel fraction of the top-stratum), not the full 195,829-source population. Table I row presents it as the DESI N_anom = 195,829 unmatched fraction, which is not what was measured.

In Fig. 5, "DESI DR1 (top 10K)" is correctly labeled. But the Table I aggregate computation (P3-E13) would use whichever fraction was applied to N_anom = 195,829, an inconsistency that propagates.

### P3-M23 — Quoted CSV throughputs in Table V do not reconcile with §II C

Table V lists DESI training time **∼3,600 s** for 47,000 spectra. At a 660K-parameter network, batch 512, 100–150 epochs converged: ∼5 min/epoch implies ∼80 s/epoch on H200. For 47K spectra at batch 512 ≈ 92 batches/epoch, that's 1.16 batches/s on H200 — implausibly slow if the network is GPU-resident. More likely the 3,600 s includes I/O, and the actual GPU-busy time is much smaller. The figure as quoted is inconsistent with the "≲10 s of GPU time" budget claimed for the photometric surveys, suggesting the spectroscopic training time is I/O-dominated. Disclose.

### P3-M24 — Posterior median vs mean reporting inconsistency

§V A: "γ = 2.567 ± 0.382 (Gaussian-approximation: posterior **mean** ± sample standard deviation; equivalent quantile summary γ = **2.591**⁺⁰·²⁹¹₋₀.₂₈₇)."

The Gaussian mean = 2.567 and the median = 2.591 differ by 0.024, which is 6.3% of σ. For a posterior that the paper later treats as "non-Gaussian and slightly asymmetric" enough to justify two different error bars, the mean-median split should be reported as a skewness diagnostic, not hidden in the body. More importantly, the +1.13σ shift to γ=3.0 is computed against the **mean** (2.567), giving 1.13σ. Against the **median** (2.591), it is (3.0−2.591)/0.382 = 1.07σ or against the quantile σ (0.289) it is (3.0−2.591)/0.289 = 1.41σ. The "+1.13σ" headline is the *most favorable* of three plausible numbers.

### P3-M25 — "ratios are robust" claims at sub-σ delta

Throughout §V and §V A, multi-σ ratios are computed at very small parameter shifts:
- α_jk = 0.19 against α_fid = 0.15: "consistent at 0.06σ" (with σ_α = 0.65). This consistency claim is statistically trivial — the two values differ by 0.04 against an uncertainty of 0.65, so essentially any value in [−1, +1] would pass. "Consistent at 0.06σ" is presented as if it validates the fiducial.
- α_jk = 0.19 against zero: "0.29σ from null." Same issue — the uncertainty dominates entirely.

The headline framing should be: "α is unconstrained by current data; both the fiducial value and zero are within < 0.3σ." Not: "α_jk is consistent with the fiducial α = 0.15 at 0.06σ."

---

## NEW MINOR findings

### P3-m16 — Hubify-Projects/bigbounce repo URL
Already noted in P3-m8 that "bigbounce" branding leaks; additional finding: the repo URL `huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog` uses a third branding token ("bamfai") not introduced anywhere in the paper. Three distinct project-identity strings (Hubify, bigbounce, bamfai) in the same data-availability paragraph.

### P3-m17 — "0.039%" vs "3.9%" mention near NEOWISE polar fraction
The NEOWISE ecliptic-pole fraction "17/436 = 3.9%" is computed correctly, but the body's repeated juxtaposition with the 1.52% uniform-null expectation invites confusion (3.9 vs 1.52 — which is the small number?). Add explicit units (% of catalog) at each mention.

### P3-m18 — "Stratified subsample of 2,670 spectra"
§III A: "ρ = −0.03 (p = 0.12 on a stratified subsample of 2,670 spectra, log-uniform in SNR)." Why 2,670? Where does this number come from? No derivation. If this is an effective sample size after stratification, state the original sample and the stratification bins.

### P3-m19 — Table III dec/Dec column header inconsistency
Table III column header reads "Dec" (uppercase D), elsewhere in the paper "δ" is used. Standardize.

### P3-m20 — "Trustworthiness 0.9797 ± 5×10⁻⁵" with "PASS > 0.90"
Appendix D: trustworthiness is reported at 0.9797 with uncertainty 5×10⁻⁵ over 20 seeds. The 0.90 PASS threshold is arbitrary (commonly 0.95 or 0.99 is used in the t-SNE/UMAP literature for "good" trustworthiness). State the source of the 0.90 threshold.

### P3-m21 — Fig. 7 caption thresholds {85°, 82°, 80.5°}
Three NEOWISE mask thresholds appear in the caption with no explanation of which is the canonical mask. Body §III H states |b_ecl| < 80°. Reconcile.

### P3-m22 — "intermediate batch-size retry on the LAMOST scan"
§II C mentions an "intermediate batch-size retry" but never explains what failed or what was changed. Either drop the mention or document.

### P3-m23 — "single ∼11 h pod-restart-with-resume after a network blip during the SDSS pass"
Same as P3-m22 — operational detail with no scientific consequence; either drop or move to acknowledgments.

### P3-m24 — "Companion data repository" cited >15 times
Many key derivations are deferred to the companion repository (per-band reconstructions, taxonomy galleries, recovery curves, plant files, per-survey architecture diagrams, MCMC chains, full per-family galleries, per-survey recovery curves). At some point the manuscript is no longer self-contained. PRD reviewers will object.

### P3-m25 — Equation (E1) numbering and reference
Eq. (E1) is the only equation in any appendix and is given an "E1" label. But this is the only equation that requires a label since it is referenced as "Eq. (E1)" in §V A — yet I find no in-text "Eq. (E1)" reference; the equation is described in prose around it but never cross-referenced by label. Consider removing the (E1) label or adding the reference.

### P3-m26 — α=0.15 "prior fiducial" with no citation
§V states "consistent with the prior fiducial α = 0.15 at 0.06σ." Where does the prior fiducial α = 0.15 come from? No citation. If this is the assumed value from an earlier draft of the same paper, it cannot serve as a prior; it's circular.

### P3-m27 — "DESI-only axis (195,829 anomalies)"
Abstract: "the DESI-only axis (195,829 anomalies) is a ∼73× like-for-like increase." The Liang et al. comparison sample was 250,000 DESI EDR spectra; this work uses 22.5M DESI DR1 spectra. The ratio 195,829/2,685 = 73, but the data-size ratio is 22.5M/250K = 90. Calling a sub-data-scaling ratio "like-for-like" is misleading: the same anomaly rate (∼1%) applied to 90× more spectra gives 90× more anomalies, not because of methodology but because of data volume. P3-M1 noted this but the abstract still says "like-for-like."

### P3-m28 — "Spectra/s" inference rates for photometric surveys
Table V: eROSITA 122K sources/s, Gaia 40K sources/s, NEOWISE 27K sources/s. These differ by ∼4.5× even though all are forward passes through MLPs of comparable size. Unexplained; likely reflects batch-size differences or padding. Document.

---

## Summary of new findings

| Class | Count |
|------|-------|
| New Essential | 5 (P3-E9 to E13) |
| New Major | 10 (P3-M16 to M25) |
| New Minor | 13 (P3-m16 to m28) |

The most consequential new findings are:
1. **P3-E9**: The 1σ envelopes on σ(f_NL) are not the propagated envelopes the paper claims they are. The upper bound 8.98 is an artificial no-improvement floor. The actual envelope is [3.92, 5.95], which weakens the central forecast significantly when reported honestly.
2. **P3-E10**: Appendix C Fig. 8 and §V use incompatible single-tracer baselines (16.85 vs 8.98). One of the two f_NL forecasts is wrong.
3. **P3-E13**: The "aggregate 58.8% SIMBAD-unmatched" cannot be reproduced from per-survey rates by any standard aggregation; the correctly-weighted aggregate is closer to 90%.

Together these compound the original P3-E1 (the 7.9% / 9.4% inconsistency) into a pattern: the cosmological forecast section is built from inconsistent and partially incorrect arithmetic. The combination warrants the original rejection recommendation with stronger emphasis on the cosmology block as the load-bearing failure.