# P3 auto-2026-06-08_1520pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (9883 chars)
**Wall time**: 501.1s

---

# Referee Report: P3 — "Spectrally Unusual Sources at Scale"

**Recommendation: REJECT**

This paper is a catalog/methods manuscript with weak, sub-1σ cosmological add-ons. It is not appropriate for *Physical Review D* in either scope or evidentiary standard. The paper is structurally a single-author internal project notebook with version-control residue throughout the body, multiple inflated headline claims that are recanted in the same paragraph, three injection-recovery FAILures relabeled as "FAIL-with-diagnostic" and silently included in the headline count, a "Bayes-factor" model comparison that is not a model comparison, and a "fNL forecast" whose 1σ envelope contains the no-improvement baseline. The data product itself may be useful — ApJS or MNRAS would be the appropriate venue — but the manuscript as written cannot be accepted by PRD.

---

## ESSENTIAL findings (acceptance-blockers)

### P3-E1 — Venue / scope mismatch (whole paper)
This is a catalog construction paper. The actual PRD-relevant content is (a) a Fisher forecast where the central improvement is 7.9% and the 1σ envelope **includes σ(fNL) = 8.98 (no improvement)**, and (b) a NANOGrav posterior comparison at +1.13σ ("marginally consistent"). Neither constitutes a physics result. There is no detection, no exclusion, no falsification. PRD's threshold for cosmology papers is not met. Recommend transferring to ApJS / MNRAS / OJAp.

### P3-E2 — Three injection-recovery FAILures included in the headline catalog (§II D Step 5, Fig. 7, Table IV)
LAMOST (5.8%), Gaia (5.2%), and eROSITA (1.2%) all fail the stated ≥50% gate at 5σ. The paper invents the term "FAIL-with-diagnostic" and keeps **113,342 LAMOST + 500 Gaia + 298 eROSITA = 114,140 unvalidated objects in the 378,280 headline count**. This is gate-gaming. Either the gate criterion is enforced (drop the failing surveys from the headline) or the gate is abandoned (drop the gate language). The current presentation is not acceptable.

### P3-E3 — LAMOST acknowledged-artifact catalog included in headline (§III D, §VI A, abstract)
The abstract itself states the LAMOST tier is "98% blue-excess training-bias artifact, injection-recovery gate FAIL". The paper then includes those 113,342 objects in the **378,280 headline**, and only in the recommendation sentence ("recommended catalog-grade subset is ∼265,000") does the reader learn the true catalog-grade size. The headline number is dishonest. Either report 265,000 as the headline and footnote the +113K as exploratory, or remove the LAMOST tier entirely.

### P3-E4 — Fisher forecast claims an improvement that is statistically null (§V, abstract)
With αjk = 0.19 ± 0.65 (point estimate <0.3σ from zero), the "7.9% improvement, σ(fNL) = 8.14" headline is not warranted. The 1σ envelope explicitly contains σ(fNL) = 8.98 (the no-improvement baseline). The abstract sentence "7.9% improvement consistent with no improvement at <1σ" is internally contradictory. A correct statement is: "the multi-tracer bias enhancement is consistent with zero; no improvement on σ(fNL) is established." Rewrite the abstract and §V conclusions accordingly.

### P3-E5 — "Savage–Dickey B_MB/SMBHB = 7.1×10³, decisive" is not a model comparison (§V A, abstract)
Matter-bounce (γ = 3) and SMBHB (γ = 13/3 ≈ 4.33) are not separate models in the fit; they are two fixed parameter values inside the **same** power-law template with a flat prior γ ∈ [0,7]. A Savage–Dickey ratio between two point-hypotheses inside one model is a parameter-shift, not a Bayes factor for distinct physical models. The "decisive" Jeffreys language is unjustified. Furthermore, B_MB/free = 3.23 is "barely worth mentioning" on Jeffreys' own scale; multiplying two unremarkable ratios does not produce decisive evidence. Either (i) compute a real model comparison (separate priors and marginalization for MB vs. an astrophysical SMBHB population spectrum with the appropriate spectral shape, eccentricity, finite-N modeling), or (ii) remove the Bayes-factor claim entirely.

### P3-E6 — Inconsistency between ACT quarantine and use of ACT result in §IV D
Appendix F states the ACT cross-transfer scan fails both gate criteria and "must not be used as a tracer of CMB fluctuation statistics". Yet §IV D ("Planck × ACT cross-correlation: null result") **is** a use of that scan as a tracer of CMB statistics, and the conclusion ("CMB patch anomalies are dominated by survey-specific systematics") is drawn from a scan that the authors elsewhere declare invalid. Either remove §IV D or unquarantine ACT.

### P3-E7 — NANOGrav posterior inconsistent with the cited dataset (§V A, Appendix E)
The paper reports γ = 2.567 ± 0.382 and log10 A = −14.025 ± 0.380 from the NANOGrav 15-yr free-spectrum KDE product. NANOGrav 15-yr's own published HD-correlated result is γ ≈ 3.2 ± 0.6 and log10 A ≈ −14.6 ± 0.1 (much tighter on A). The reproduced amplitude uncertainty is ~3.8× too wide; the γ central value is ~1σ low. The reproduction of a public posterior should agree with the source paper. Either there is a likelihood-implementation bug (Eq. E1 normalization, frequency basis, choice of bins), or the wrong product was loaded. The +1.13σ matter-bounce claim depends on this posterior and cannot stand without independent reproduction.

### P3-E8 — Internal audit tags / version-control residue throughout body
The body contains pervasive internal-document residue that should not appear in a journal submission:
- "Path-C" rebuild protocol (Section II D, Table I "Path-C row", "Path-C unique", "Path-C-final catalog", "Path-C native-retrained", "Path-C residual caveats", "Path-C rebuild", "Path-C-compliant", "Path-C protocol"...). This is an internal project codename.
- "§VI D caveat (i)", "(ii)", "(f)", "(g)", "(j)", "(v)" cross-references that do not match any list rendered in §VI D (the body shows "(i)" and "(ii)" only; (iii)–(v) and (f)–(j) are referenced but missing from the rendered text).
- Table IV header text: "All ten items are closed (C = resolved in paper; derivations in companion data repository)" — internal audit-log language.
- "before/after diagnostic", "preserved as a sensitivity-check artifact", "8-way-with-ACT variant", "rebuild protocol", "two-part gate".
- "earlier 'strict subset' framing is replaced" (Table I footnote §) — replacement-history note.
- Reference [33]: "bibkey label retained as Heinrich2023 for arXiv-submission-year continuity" — internal bibkey bookkeeping inside the published bibliography.

All such tags must be removed and replaced with conventional method/uncertainty language.

### P3-E9 — Single-author institutional concerns; data unavailable to referees
The DESI DR1 dataset, Gaia DR3, eROSITA DR1, etc. are public; however the released catalog ("HuggingFace bigbounce-anomaly-catalog") is "private pending arXiv acceptance". A PRD referee cannot verify the central data product. The authors must (i) provide reviewer-access credentials at submission, or (ii) make the catalog public prior to refereeing. Author affiliation "Independent Researcher" with a corporate email (hubify.com) and a project codename ("BigBounce") that matches a specific theoretical preference (matter-bounce cosmology) raises a confirmation-bias concern: the entire anomaly campaign appears designed downstream of a preferred theoretical scenario.

### P3-E10 — TIC 374313355 misclaim (§IV C, Fig. 6 caption)
"appears in the TESS Input Catalog as variable" — appearance in the TIC is not a variability classification; the TIC is a target list, not a variability catalog. The score change from 8.1 (DESI) to 49.5 (SDSS) requires an actual lightcurve check (TESS SAP/PDC, ZTF, ASAS-SN) before the "time-variable source" claim can be made in the abstract.

### P3-E11 — "Largest" framing is misleading (abstract, §VII)
The "~141× the largest prior single-survey anomaly catalog" comparison sums DESI + SDSS + LAMOST(artifact) + eROSITA + Planck patches + Gaia + NEOWISE versus Liang et al.'s single-survey DESI EDR result. The honest like-for-like is the buried "DESI-only axis (195,829 anomalies) is a ∼73× like-for-like increase." Move the 73× to the headline and demote 141×.

---

## MAJOR findings

### P3-M1 — Aggregate SIMBAD-unmatched 58.8% does not reconcile (Table I, §IV A, Fig. 5)
Computing the weighted aggregate from the per-survey rates and counts: 195,829×0.99 + 77,905×0.90 + 44,075×0.50 + 298×0.68 + 500×0.27 + 436×0.45 ≈ 286,557 unmatched of 319,043 with coordinates ≈ **89.8%, not 58.8%**. The 58.8% figure cannot be reproduced from the displayed inputs. Either the per-survey rates are wrong or the aggregate is wrong; recompute and reconcile.

### P3-M2 — Equation 2 "z-score" is degenerate for SDSS (Fig. 2 right panel)
Fig. 2 right panel shows SDSS scores reaching S = 1.9×10¹¹. A "z-score" of 10¹¹ is not a z-score in any meaningful statistical sense — the standardization assumes the validation MSE distribution is approximately Gaussian or at least has finite second moment relevant at this distance. The cross-transfer SDSS scores are clearly not in this regime. Either (i) report MSE itself, or (ii) state explicitly that "S" here is a label, not a standardized statistic, and that comparisons across surveys at this score range are not meaningful.

### P3-M3 — CMB native autoencoder fails criterion (a) of its own gate (§II D Step 1, §III F)
val_loss = 0.4437 versus criterion (a) ≤ 0.30. The paper invokes a two-part OR gate so that criterion (b) (injection-recovery 100%) rescues the retention. But a model with val_loss 1.5× the gate threshold has not learned the data distribution well; the 100% recovery of *injected Gaussian bumps at 5σ* is not evidence that natural CMB anomalies are detected reliably. The OR gate design itself is post-hoc. Document the original gate (before OR was added) and justify the criterion (b) sufficiency.

### P3-M4 — Spatial χ² uses inhomogeneous footprints (§IV B)
The paper acknowledges this in the very paragraph that quotes χ²_ν = 3.76: "the significant χ²_ν is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering". Then why is the number reported at all? Remove the χ² statistic or replace with a per-survey footprint-corrected analysis.

### P3-M5 — Novelty fraction is a single-sample point estimate at the top-1,000 stratum (abstract, §IV A)
The abstract states the novelty rate is 17.8% but acknowledges "(single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested)". A single-sample point estimate at a non-headline stratum cannot be the headline novelty rate. Either provide a stratified estimate (e.g., novelty rates at top-1K, top-10K, top-100K with bootstrap CIs) or move the 17.8% to a caveat.

### P3-M6 — Fig. 1 title contradicts the paper's headline count
Figure 1 title text: "Spatial distribution of all 319,443 anomalies across 8 archives". But the canonical Path-C count is 378,280 across 7 archives (ACT quarantined). The caption attempts to clarify but the figure itself is a cross-transfer/pre-Path-C artifact. Replace with a Path-C-current spatial distribution, or remove.

### P3-M7 — 17.8% novelty is asserted without inspection of the 178 candidates (§IV A)
The 178/1,000 "candidate genuinely novel population" are described purely by archival absence. No spectroscopic or imaging inspection of any subset is presented in this paper. For PRD, a novelty claim of this size requires at minimum image cutouts and per-object disposition for a random sub-sample.

### P3-M8 — 22.7% of DESI anomalies are "calibration-suspect" but counted in the headline (Table VI, §VI C)
44,436 B-dominant DESI anomalies are flagged as suspect. These are 22.7% of the DESI total. They remain in the catalog headline. Justify retention or exclude.

### P3-M9 — Threshold gerrymandering across surveys (Table I footnotes ♡, ♠)
DESI uses S>5.0 absolute; SDSS native re-score at S>5 yields 12 sources but the catalog uses top-1% percentile (77,905); LAMOST native at S>5 gives 2,054 but the catalog uses top-1% (113,342); eROSITA uses top-298 (~0.03%); Planck/Gaia/NEOWISE use top-1%. These six different threshold conventions are presented as a single "anomaly catalog". The two SDSS/LAMOST native rate-compressions (∼6500× and 21.5×) are headline diagnostics — these are the actual native anomaly counts. Using top-1% to inflate them back to 77,905 / 113,342 is post-hoc threshold selection. Reconcile to a single threshold convention or report the per-survey native counts at S>5 as the headline.

### P3-M10 — DESI in-sample scoring on training set (§II B, §VI D (i))
The DESI 22.5M scan includes the 47,000 training spectra. The Jaccard J̄ = 0.862 is computed on the same training pool (folded). This is **not** an out-of-sample completeness check; it is a training-set self-consistency check. The independent 100k OOD test "flags >50% of spectra" — this is the only OOD measurement and it indicates that the S>5 threshold produces a 50% anomaly rate on OOD data. The reconciliation that this is "a catalog-curation effect, not a threshold artifact" is asserted but not demonstrated. Provide a proper OOD completeness/purity table.

### P3-M11 — Reference [12] in press with future date
Nicolaou et al. listed as "Mon. Not. Roy. Astron. Soc. (2026, in press)". Verify and update; if not yet refereed, label as preprint with arXiv ID.

### P3-M12 — Hellings & Downs [25] not used in body
Reference [25] is in the bibliography but the in-text appears not to cite it. Verify.

### P3-M13 — log10 A = −14.025 ± 0.380 contradicts NANOGrav 15-yr published amplitude (Appendix E)
See E7. The amplitude uncertainty is 3–4× too wide compared to NANOGrav's own 15-yr posterior. Reproduce or remove.

### P3-M14 — "Genuine novelty fraction" and "Native-Trained Novelty Fractions" (plural) in title vs. one measurement
Title says "Native-Trained Novelty **Fractions**" (plural). The body reports a single fraction (17.8% from DESI top-1,000). Either provide multiple per-survey native-trained novelty fractions, or singularize the title.

### P3-M15 — "Native-trained" in title is misleading
DESI, the largest contributor (195,829), was NOT natively retrained under Path-C; it was the original training survey. SDSS, LAMOST, Planck were natively retrained. The title's "Native-Trained" framing implies all 378,280 anomalies come from native-retrained models, which is false.

---

## MINOR findings

### P3-Mi1 — "Dated: June 2026"
The paper is dated in the future. Update.

### P3-Mi2 — Affiliation
"Independent Researcher, Los Angeles, California, USA" — acceptable but unusual for a paper claiming the largest multi-archive anomaly campaign. Provide ORCID and verification of independent-researcher status.

### P3-Mi3 — Fig. 6 caption inconsistency
Fig. 6 panel (d) shows SDSS score 49.5 reconstruction far from data — this is a failed reconstruction by definition, not a credible match. Either show a better fit or remove the reconstruction overlay.

### P3-Mi4 — Eq. (E1) typesetting
"log10 ρi = ½ [2 log10 A − log10(12π²) + (γ−3) log10 f_yr − γ log10 f_i − log10 T_obs]" — note that 2 log10 A inside the ½ gives log10 A (not log10 A²); verify the normalization against Hellings–Downs / Phinney convention. A reader cannot reproduce the amplitude from this equation alone.

### P3-Mi5 — Figure 7 axis labeling
The injection-amplitude axis is "× noise σ" but the noise σ is per-survey defined differently (catalog-residual MSE for spectroscopy vs. patch RMS for CMB vs. IF subspace for eROSITA). Either rescale to a common axis or split the figure.

### P3-Mi6 — Table III "S_BigAE" and "S_IF,raw" presented in same row
The two scores are on radically different scales (0–1.1 vs. 0–34000). Tabulate either as ratio-to-threshold or normalize.

### P3-Mi7 — "(2026, in press)" / "Dated: June 2026" / "arXiv-submission-year continuity"
Multiple year-of-record inconsistencies. Standardize.

### P3-Mi8 — Page count
20 pages for a methods/catalog paper with a sub-1σ forecast and a +1.13σ consistency check is excessive. Recommend ≤10 pages if pursued as a Letter equivalent in an appropriate journal, or full-length in ApJS where catalog detail is welcome. PRD: not appropriate at any length.

### P3-Mi9 — "deduplicated total" / "Path-C unique" / "canonical catalog" / "headline 378,280"
At least four interchangeable names for the same quantity. Pick one and use it.

### P3-Mi10 — Acronym proliferation
"BAL QSO", "TIC", "SMICA", "SPARCL", "BGS/LRG/ELG/QSO/MWS", "HBM3e", "FoF" used without expansion. Define on first use.

### P3-Mi11 — Caveat-list missing items
§VI D footnote labels (i)–(v) and (a)–(j) referenced in body do not match the rendered items. Either provide the full list or remove cross-references.

### P3-Mi12 — Reference [33] bibkey footnote
"bibkey label retained as Heinrich2023 for arXiv-submission-year continuity" — internal note, remove.

### P3-Mi13 — Companion repository
Multiple results ("per-survey recovery curves", "per-family image gallery", "5σ subspace injection details", "fitter script") deferred to companion repository. PRD requires the paper to be self-contained for evaluation. Either fold critical content into appendices or provide reviewer access.

---

## NIT findings

### P3-N1 — "z-scored ('z' here is the statistics term...; spectroscopic redshift is always written z..." — six lines of disclaimer to avoid a single symbol clash. Rename S to e.g. Z_s or A_s and drop the disclaimer.
### P3-N2 — "Pearson r = 0.006, p = 0.21" — with r = 0.006, the p = 0.21 likely means the sample is small or the test is awkwardly specified. Spell out the sample size.
### P3-N3 — Multiple uses of "headline" as adjective/noun ("headline 378,280", "headline novelty", "headline σ(fNL)"). Tighten.
### P3-N4 — "~141×" and "~73×" rounded but underlying ratios are 140.9 and 72.9 — present once with one decimal.
### P3-N5 — Fig. 9 panel labels show "AE=83518" and "AE=17663" — at the cross-transfer scale where SDSS scores reach 10¹¹, these AE labels are uninterpretable.
### P3-N6 — "BigBounce" project name in repo URL appears in the body; remove project-codename branding from the published version.

---

## Summary recommendation

**REJECT.**

The paper is a single-author catalog product wrapped around two sub-1σ cosmological tags: a Fisher forecast whose 1σ envelope contains the no-improvement baseline, and a NANOGrav consistency check at +1.13σ supported by a Bayes-factor framing that is not a model comparison. The headline 378,280 unique-anomaly count includes 113,342 LAMOST objects that the abstract itself labels as a 98% training-bias artifact and three injection-recovery FAILures relabeled as "FAIL-with-diagnostic". The reproduced NANOGrav posterior disagrees with the published 15-yr amplitude uncertainty by ~3–4×, calling the entire spectral-index analysis into question. The body is saturated with internal version-control residue ("Path-C", "before/after diagnostic", "bibkey retained for continuity", broken §VI D caveat cross-references). The released catalog is private at submission time, so the central data product cannot be verified. Even at a fully corrected version, the paper's actual physics content does not meet PRD's threshold and belongs at ApJS or MNRAS. I recommend rejection from PRD with a strong suggestion to (i) restructure as a catalog paper for an astronomy methods journal, (ii) drop or dramatically rework the fNL and NANOGrav sections, (iii) enforce the gates the paper defines for itself rather than redefining FAIL, and (iv) decouple the project from its theoretical-preference branding.

---

## PASS 2 — self-critique findings (what initial review missed)

# Supplemental Findings — Fresh-Eyes Pass on P3

A second careful pass against the document, focused on the audit classes A–J, surfaces additional issues that the initial review missed. Most are arithmetic / stale-figure / caption-vs-body discrepancies that materially affect the headline.

---

## NEW ESSENTIAL findings

### P3-E12 — Abstract "7.9% improvement" arithmetic does not match the stated inputs (A, F, J)
The abstract reports "central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] **(7.9% improvement** consistent with no improvement at <1σ; σ(fNL)^std = 8.98)". With the displayed inputs, (8.98 − 8.14)/8.98 = **9.4%**, not 7.9%. The 7.9% figure does not appear anywhere in §V where it should be derived.

Where the 7.9% comes from: Appendix C Fig. 8 caption reports "Baseline multi-tracer = 12.72" and "Ideal (dense limit) = 11.71" → (12.72 − 11.71)/12.72 = **7.94%**. This is the canonical 5-tracer ideal-vs-degraded-multi improvement, an entirely different Fisher configuration from the DESI-only α-driven calculation that produces σ = 8.14. The headline cosmological percentage in the abstract is stale from the wrong calculation. Either:
(i) Replace with the correct 9.4% derived from the α = 0.19 single-tracer Fisher-positivity form, or
(ii) Drop the percentage entirely (it is < 1σ anyway).

This is the second case (after P3-E4) where the abstract's principal cosmological number is wrong. Compounded with E7 (NANOGrav posterior reproduction failure) and E5 (Bayes-factor misframing), three of the four cosmological numbers in the abstract do not survive a check against their own displayed inputs.

---

## NEW MAJOR findings

### P3-M16 — Fig. 2 left panel uses stale cross-transfer LAMOST count (B, J)
The legend reads "LAMOST DR10 (44,075)" — the cross-transfer baseline count that the Path-C narrative explicitly supersedes with the 113,342 native count. The figure is captioned as displaying "anomaly score distributions for the three main spectroscopic surveys" without flagging that the LAMOST distribution shown is the pre-rebuild (artifact-dominated) population. A reader inspecting the figure to interpret LAMOST anomalies is being shown the diagnostic-only, Path-C-superseded distribution. Replace with the native-retrained distribution or label as cross-transfer-only.

### P3-M17 — Fig. 6 panels (c)(d) and §IV C "score = 49.5" are cross-transfer-scale numbers (B, J)
The TIC 374313355 SDSS-side panel shows "Score = 49.5". The Path-C SDSS native re-score at S > 5 yields only **12 sources catalog-wide** (§III C, the ∼6500× rate-compression diagnostic). A single source at canonical-S = 49.5 in the native scale would be the most extreme SDSS anomaly by an enormous margin and would dominate every downstream statistic.

The 49.5 must therefore be on the cross-transfer scale (where SDSS scores reach 10¹¹, per Fig. 2 right). The §IV C narrative and Conclusion item 4 — which cite "TIC 374313355 (score = 49.5)" as a cross-survey validation highlight of the Path-C catalog — are using a number that the paper elsewhere quarantines as a diagnostic. Either re-score TIC 374313355 in the native frame and report the native S, or remove the score = 49.5 figure from the discovery narrative.

### P3-M18 — Fig. 7 caption claims three PASS surveys but figure shows only six spectral/photometric curves (B)
Caption: "Three surveys PASS the gate at 5σ: SDSS DR18 continuum-dip (PASS, 64%), Planck CMB native (PASS, 500/500 = 100%), and NEOWISE ecliptic-pole mask (PASS, 1000/1000 = 100%)". The legend enumerates: SDSS continuum-dip, SDSS emission-line, LAMOST continuum-dip, LAMOST emission-line, eROSITA latent IF, Gaia variab. IF — **six curves, none of which are Planck or NEOWISE**. The figure visually displays only one of the three PASS results claimed in its caption (SDSS). The figure does not support two of three PASS claims; the reader must take Planck-100% and NEOWISE-100% on faith. Either add the missing curves or restrict caption claims to what is plotted.

### P3-M19 — Table VII is computed with the deprecated linear-propagation Fisher form (A, I)
Table VII caption: "Values are derived by linear scaling from the fiducial full 7-bin Fisher result at α = 0.15". §VI D caveat (i) explicitly states this linear-propagation form **fails** inside the 1σ interval that crosses zero. Cross-check at the listed Table VII α values using the Fisher-positivity form (F₀ = 1/8.98², c = 0.0747) used in §V:

| α | Table VII σ (linear) | Fisher-positivity σ | Δ |
|---|---|---|---|
| 0.05 | 8.80 | 8.93 | −0.13 |
| 0.10 | 8.61 | 8.72 | −0.11 |
| 0.15 | 8.43 | 8.43 | 0 (calibration point) |
| 0.20 | 8.25 | 8.06 | +0.19 |
| 0.30 | 7.88 | 7.23 | +0.65 |
| 0.50 | 7.15 | **5.67** | +1.48 |

Table VII materially overestimates σ (i.e., understates the improvement) at α ≥ 0.20, by ~20% at α = 0.50. Readers using Table VII for sensitivity work will get systematically wrong answers in the regime where the multi-tracer technique becomes interesting. Recompute Table VII with the Fisher-positivity form or label as deprecated.

### P3-M20 — Abstract "∼265,000 catalog-grade subset" arithmetic not reproducible (A)
Abstract: "the recommended catalog-grade subset is ∼265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE)". Sum from per-survey native counts in Table I footnote ||:
195,829 + 77,905 + 298 + 500 + 419 = **274,951**.

To reach 265,000 requires ~9,950 of intra-survey dedup specifically within these five surveys (out of the 9,576 total intra-survey duplicates reported across all seven surveys, with ACT excluded). The arithmetic is plausible only if essentially all intra-survey duplicates occur in these five and none in LAMOST — but LAMOST is the largest exploratory-tier survey and presumably has its own intra-survey duplication. Provide the per-survey dedup breakdown or correct the recommended subset count.

---

## NEW MINOR findings

### P3-Mi14 — Withdraw P3-Mi4
Eq. (E1) is dimensionally consistent with the standard PTA characteristic-strain → free-spectrum-rms convention (verified by expansion against h_c² = A²(f/f_yr)^(3−γ) and ρ²(f) = h_c²/(12π²f³T_obs)). The initial concern about normalization is withdrawn.

### P3-Mi15 — Table I "Path-C unique" rate of 1.01% is a meaningless aggregate
378,280 / 37,272,042 = 1.01%, but this combines DESI absolute S > 5 (0.87%), SDSS top-1% native (4.0%), LAMOST top-1% native (1.0%), eROSITA top-0.03% (0.03%), Planck top-1% patches (1.0%), Gaia top-1%, and NEOWISE top-1%-after-mask. The seven selection criteria are not comparable, so the "1.01% Path-C rate" should not be reported as a survey-aggregate quantity. Remove from Table I or footnote as "construction-dependent average, not an astrophysical rate".

### P3-Mi16 — "Dated: June 2026" + Ref. [12] "(2026, in press)"
The paper's date and a key citation are both forward-projected to mid-2026. Combined with the "bibkey retained for arXiv-submission-year continuity" tag in Ref. [33], the document appears to be staged against a future arXiv timestamp. Date should reflect actual submission month, and forward-dated references should carry explicit preprint/arXiv IDs.

### P3-Mi17 — "≈ 0.143 on the rescaled scale" anchoring (§II B)
The text states µ_val ≈ 0.0287 and S > 5 corresponds to MSE ≈ 0.143. Working backward: σ_val = (0.143 − 0.0287)/5 = 0.02286. This is **0.80 × µ_val**, i.e., the validation MSE distribution has a coefficient of variation of 80%. For a Gaussian-like loss distribution that should be << 1. A CoV of 0.8 indicates a very heavy-tailed validation loss distribution, in which case the "z-score" interpretation of Eq. 2 (already a concern, P3-M2) breaks down even for the DESI native case. Either show the validation MSE histogram or justify the standardization.

### P3-Mi18 — "Mean Z-arm sub-score ⟨rZ⟩ = 3.9 across the 12 selected candidates; all objects have total score S > 5 by construction"
A per-arm sub-score of 3.9 with a total S > 5 is consistent only if the other arms also contribute (e.g., rB and rR not vanishing). But the same paragraph describes these as Z-arm dominated (rZ > rB and rZ > rR). With rZ = 3.9 < 5 = catalog threshold, the rZ-dominated condition + S > 5 implies rB + rR also significant. The "Z-dominated" + "Gunn-Peterson trough blueward of Lyα" interpretation is then in tension with non-trivial blue-arm contribution to S. Resolve.

### P3-N7 — Repeated "Path-C" appears ~50 times throughout body
Project-codename diction (already P3-E8) is repeated to the point of impeding readability. Each use of "Path-C" should be replaced with "the native-retrain rebuild" or analogous methodological description.

### P3-N8 — Acknowledgments thank "RunPod" by name
Vendor branding in acknowledgments is unconventional. Standard practice: "computations were performed on cloud GPU resources" or specify hardware (NVIDIA H200) without vendor.

---

## Summary of fresh-eyes increment

The second pass adds **one essential** (P3-E12: abstract's headline 7.9% improvement traces to the wrong calculation in Appendix C), **five major** (Fig. 2/6/7 stale-or-mislabeled figures, Table VII Fisher-form inconsistency, catalog-grade subset arithmetic), and **five minor/nits**. With these added to the original review, the count of arithmetic/citation errors in the cosmological abstract sentences is now three of four (P3-E4 forecast statistical insignificance, P3-E5 Bayes-factor framing, P3-E7 NANOGrav posterior reproduction, P3-E12 7.9% arithmetic). The figure-vs-body audit reveals systematic Path-C / cross-transfer cross-contamination in Figs. 2, 6, and 7 — exactly the contamination problem the Path-C protocol was constructed to eliminate. The recommendation remains **REJECT**, now strengthened: the cosmological abstract numbers do not survive arithmetic check, and the figures supporting the Path-C narrative are themselves built on pre-Path-C numbers.