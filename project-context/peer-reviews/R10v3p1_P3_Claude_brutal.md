# P3 R10v3p1 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (17245 chars)
**Wall time**: 538.1s

---

# Referee Report: "Spectrally Unusual Sources at Scale" (P3)

## Overall Assessment

This paper attempts to package three distinct projects — (1) a multi-archive autoencoder anomaly catalog, (2) an empirical bias measurement feeding an fNL forecast, and (3) a NANOGrav spectral-index MCMC — into a single submission. Each of the three has serious problems individually, and the combination does not constitute a coherent PRD contribution. The "largest-ever" framing is undermined by the authors' own admissions: half the anomaly catalog fails injection-recovery validation, the fNL "improvement" is consistent with zero at <1σ, and the NANOGrav analysis is a derivative re-fit of a public KDE product. The paper is also far too long (20 pages) for what it actually proves.

I recommend **REJECT**.

---

## ESSENTIAL Findings

### P3-E1: Headline σ(fNL) claim is statistically null, presented as a "forecast"
**Abstract, p.1; §V, p.10.** The abstract states "central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fNL)^std = 8.98 single-tracer baseline)." This is an explicit admission that the measurement is consistent with zero improvement. Quoting a "7.9% improvement" central value as a headline result when the 1σ envelope contains the null baseline (8.98) is statistically dishonest. PRD does not publish forecasts whose central value is <1σ from no-effect as a "result." The body (§V) compounds this by stating αjk = 0.19 ± 0.65 — a 0.29σ detection. **Required fix:** Remove the σ(fNL) = 8.14 number from the abstract and state plainly "the empirical bias measurement is consistent with no multi-tracer improvement (αjk = 0.19 ± 0.65, 0.29σ from null)."

### P3-E2: NANOGrav σ values from different null procedures juxtaposed without qualification
**Abstract; §V A, p.11.** "γ = 2.567 ± 0.382; matter-bounce γ = 3.0 at +1.13σ, SMBHB γ = 4.33 at +4.61σ (BMB/SMBHB = 7.1×10³)." The +1.13σ and +4.61σ are parameter-shift distances from a posterior mean, not detection significances — yet they are juxtaposed with a Bayes factor as if comparable. Additionally, "BMB/SMBHB = 7.1×10³" is presented in the abstract with no caveat that this is a Savage-Dickey ratio against a uniform prior over γ ∈ [0,7], which trivially penalizes the narrow SMBHB peak. **Required fix:** Add "not directly comparable" qualification at every juxtaposition of parameter-shift σ and Bayes factor; remove from abstract.

### P3-E3: "Largest-scale" / "141×" claim conflates incomparable quantities
**Abstract; §VII, p.13.** The claim that this is "∼141× the size of the largest prior single-survey anomaly catalog [11]" compares 378,080 unique anomalies (across 7 surveys, partly cross-transfer-contaminated) to Liang et al.'s 2,685 anomalies on DESI EDR. The 378,080 includes 113,342 LAMOST anomalies the authors themselves label "exploratory tier" / "98% blue-excess training-bias artifact, injection-recovery gate FAIL." Subtracting that and the equally-failed Gaia (500) and eROSITA (298, fails 5σ gate) yields a "catalog-grade" subset the authors recommend as ~265,000 — and even that includes SDSS native (77,905) where the injection-recovery is only 64%. The honest comparable "DESI-only axis (195,829)" gives ~73×, which is still a coarse comparison given different selection thresholds. **Required fix:** Remove "141×" from abstract; report only the DESI-only like-for-like figure, and only after explicit threshold equivalence is demonstrated.

### P3-E4: Three of six injection-recovery gates FAIL but objects are still released as "anomalies"
**§II D step 5; §VI D (ii); Fig. 7.** LAMOST (5.8%), Gaia (5.2%), and eROSITA (1.2%) all fail the 5σ recovery gate that the authors themselves established as the validation criterion. Releasing 113,342 LAMOST + 500 Gaia + 298 eROSITA = 114,140 "anomalies" (30% of the headline catalog) that fail the authors' own validation gate is not acceptable. The "FAIL-with-diagnostic" framing is rhetorical sleight-of-hand — a FAIL is a FAIL. **Required fix:** Either remove failed-gate surveys from the headline count or rename them explicitly as "candidate" tier with a clear disclaimer in every count, including the abstract.

### P3-E5: 17.8% genuine novelty fraction is unrepresentative
**Abstract; §IV A.** The 17.8% is measured on the top-1,000 DESI anomalies only, then quoted as the catalog's "genuine novelty fraction." The authors admit "full-catalog rate empirically untested." Quoting a single-stratum point estimate (no error bars) as the catalog novelty rate is misleading. The top-1,000 stratum is the highest-anomaly-score subset, where novelty would be expected to be highest. **Required fix:** Either measure the rate on a representative random sample of the full catalog with bootstrap uncertainties, or remove from abstract.

### P3-E6: Figure 1 caption inconsistent with title text
**Fig. 1, p.4.** The figure title reads "Spatial distribution of all 319,443 anomalies across 8 archives" but the caption begins "Cross-transfer baseline map. Mollweide projection of the initial cross-transfer anomaly baseline (319,443 detections shown; canonical Path-C unique count is 378,280..." The figure title contradicts the canonical catalog count by ~59,000 objects and refers to 8 archives when ACT is "quarantined." **Required fix:** Regenerate the figure using the Path-C native catalog (378,280) and update the title.

### P3-E7: Internal audit tags ("R7", "Path-C", "before/after diagnostic") in main body
**Throughout, especially Table IV (p.13), §II D, §III.** "Path-C rebuild," "before/after diagnostic," "preserved as the §II D before/after baseline," and similar internal-bookkeeping language is reviewer-process artifact, not science. Table IV is captioned "All ten items are closed (C = resolved in paper; derivations in companion data repository)" — this reads like an internal action-item tracker, not a PRD discussion section. **Required fix:** Strip all internal audit language and rewrite the methods as a single coherent description of what was actually done.

### P3-E8: "Path-C" branding has no scientific meaning
**Throughout.** "Path-C" is referenced ~25 times in the body but never defined other than as "rebuild protocol." This is internal version-control jargon. There is no Path A or Path B in the paper. **Required fix:** Replace "Path-C" with "native-retrain protocol" or similar descriptive phrase, or remove the label.

### P3-E9: Table III column SIF,raw values are unphysical for an IsolationForest
**Table III, p.8.** "SIF,raw" is described as "IsolationForest raw isolation-score value (anomaly score on a ∼ 0–3.5×10⁴ scale)." Standard sklearn IsolationForest scores are bounded between roughly -0.5 and +0.5 (or 0 and 1 after normalization). Values of 34,182, 16,270, etc. are impossible for a standard IF. Either this is a different quantity or the description is wrong. **Required fix:** Explain what these numbers actually are; if a custom score, define it formally.

### P3-E10: SDSS "~6500× rate compression" arithmetic
**Abstract; §III C.** Cross-transfer SDSS gives 77,905 anomalies; "Path-C native" gives "only 12 sources at S > 5." 77,905 / 12 = 6,492 ≈ 6500×. But the headline SDSS count (Table I) is still 77,905 (top-1% slice at S ≥ 0.1060, not S > 5). So the "6500×" is comparing two different thresholds (S > 5 cross-transfer vs S > 5 native), while the released catalog uses a 1% percentile cut. This is genuinely confusing: at the released threshold, what is the rate compression? **Required fix:** Report SDSS rate compression at a single, consistent threshold definition.

### P3-E11: Fisher positivity equation is undermotivated
**§V, p.10; §VI D (i).** The "Fisher-positivity-respecting" form 1/σ(fNL)² = F₀ + cα² with c = 0.0747 is asserted as a quadratic in α, but the standard multi-tracer Fisher has a different α-dependence (typically goes as α² at small α and saturates, but the exact form depends on tracer parameters). The c value is "verified positive via 5-α refit" — five points is not a fit, it's interpolation. **Required fix:** Either derive the equation from first principles in an appendix or replace with a standard linear-bias propagation with clear approximation caveats.

### P3-E12: NANOGrav fit ignores HD-correlation matrix structure
**§V A; Appendix E.** The paper fits a power-law GW template to the published 30-bin KDE free-spectrum likelihood using a 32-walker emcee chain. This is a likelihood re-fit, not a new measurement. The NANOGrav collaboration already published their own power-law constraints on γ from the same dataset; the authors do not compare to or cite that result. The +1.13σ γ=3 figure has no independent meaning. **Required fix:** Cite NANOGrav's own γ measurement (γ ≈ 3.2 ± 0.6 in NANOGrav 23 PL fits) and reconcile.

### P3-E13: Three-result paper / scope problem
The paper combines (a) an anomaly catalog, (b) an fNL forecast that is null, and (c) a NANOGrav re-fit that duplicates published work. None of these three is strong enough to stand alone as a PRD paper, and combining them does not produce a coherent contribution. **Required fix:** Split into (a) a catalog/data paper for a methodology journal (RNAAS, ApJS) and a separate cosmology paper if the empirical bias measurement can be made convincing.

---

## MAJOR Findings

### P3-M1: Abstract is bloated and contains caveats
**Abstract, p.1.** The abstract is ~500 words and contains parenthetical caveats ("consistent with no improvement at <1σ"), explanatory clauses about why surveys were retained or quarantined, and internal references ("Path-C", "8-way-with-ACT variant"). PRD abstracts should be ~250 words, declarative, and state results without internal-process commentary.

### P3-M2: Anomaly score S notation footnote is intrusive
**§II B, p.2.** A six-line parenthetical inside the formal definition of S explaining that "z-scored" is the statistical z and not redshift is rambling. Use a footnote.

### P3-M3: Table I footnotes longer than table
**Table I, p.7.** The footnotes (¶†‡∥§) span ~50 lines and contain methodological substance that should be in the body. Footnote § even introduces new empirical results (284/298 = 95.3% overlap, hypergeometric p≈0). Tables should have brief footnotes.

### P3-M4: Fig. 2 right panel shows "S = 1.9×10¹¹" as a serious physical quantity
**Fig. 2, p.5.** The caption explains this is a "cross-transfer artifact... eliminating the 10⁴–10¹¹ tail," yet the headline panel displays the artifact prominently. This figure showcases known-bad numbers as if they were results.

### P3-M5: "BAL QSO at z ≈ 0.86" novelty claim unverified
**§IV C; Fig. 6.** The "Uncataloged BAL QSO at z ≈ 0.86" is presented as a discovery (absent from SIMBAD, Milliquas, NED), but the §IV A discussion already establishes that SIMBAD-unmatched ≠ genuinely novel, and only 17.8% of top-1,000 anomalies pass the deeper CDS X-Match novelty test. The BAL QSO has not been put through that test in the paper.

### P3-M6: Cross-survey 637 coincidences — false-match rate analysis incomplete
**§IV A; §IV C.** The "<2% contamination" estimate "expected random coincidence contribution is ≲10 across all survey pairs against 637 observed multi-survey clusters" lacks derivation. Different survey pairs have wildly different source densities; an aggregate ≲10 is implausible without per-pair computation.

### P3-M7: Spatial χ² test "dominated by survey footprints" admitted but not corrected
**§IV B, p.10.** The authors admit χ²_ν = 3.76 is "dominated by the inhomogeneous footprints of the seven retained archives" but report it anyway. Either do the selection-function correction or remove the test.

### P3-M8: Path-C CMB native model fails criterion (a) but passes (b)
**§II D step 1; §III F.** The two-part gate "validation loss ≤ 0.30 or injection-recovery ≥ 50%" is structured so that CMB only had to pass one of two. The val_loss = 0.4437 (criterion a) FAIL is not minor — it is 47% over the threshold. The OR structure of the gate is convenient.

### P3-M9: Reference [11] (Liang et al.) reports 2,685 / 250,000 = 1.07%, paper compares to total
**§I; §VI E.** The comparison "73× the largest prior single-survey anomaly catalog" uses anomaly counts, but Liang et al. processed 250,000 spectra vs the authors' 22.5M. The relevant comparison is sample size (90×, which the authors do quote elsewhere) not anomaly count.

### P3-M10: Bibliography label inconsistency
**Ref [33].** "Heinrich2023 for arXiv-submission-year continuity" — internal bibkey commentary in the rendered paper is unprofessional and indicates copy-paste from working notes.

### P3-M11: "Quarantined" ACT DR6 is cited in Planck × ACT null cross-correlation
**§IV D, p.10.** A "null result" is reported between Planck and ACT, where ACT is itself an admitted cross-transfer failure. The null is meaningless — you cannot draw any inference from null cross-correlation when one input is known to be dominated by autoencoder failure modes.

### P3-M12: Reproducibility data link non-functional at submission
**§VII Data availability.** "private pending arXiv acceptance" — PRD requires reproducibility material to be accessible to referees during review. As submitted, none of the catalogs, weights, MCMC chains, or scripts can be checked.

### P3-M13: Section VII conclusions repeat the abstract
The seven numbered conclusion bullets re-state the abstract verbatim with marginal additions. PRD conclusions should add interpretive depth, not repeat.

### P3-M14: σ(fNL)^GS forecast not propagated coherently
**§V; Table IV row (j).** The Gold+Silver "central 1.95" with envelope [0.94, 8.98] is reported next to αGS = +1.83 ± 2.03 — a 0.9σ value. Quoting σ(fNL) = 1.95 (a factor 4.6× improvement) from a 0.9σ measurement is over-interpretation that arXives the same flaw as P3-E1.

### P3-M15: Figure 7 contains arbitrary "amplitude" axis without physical units for spectral surveys
**Fig. 7, p.13.** "Injection amplitude (× noise σ)" for SDSS continuum-dip vs eROSITA latent-IF vs Gaia variability-axis are six different physical quantities pretending to share an axis. Plotting them on the same x-axis is misleading.

### P3-M16: Figure 9 "AE" scores up to 83,518 displayed in image captions
**Fig. 9, p.17.** Border-color taxonomy plus extreme "AE" scores (e.g., AE=83518) reinforces that the figure shows cross-transfer-inflated scores from the previously-disclaimed artifact regime.

### P3-M17: Author claims "0% artifact rate" in DESI top-200
**§III A; §VI A.** "Spectral inspection of the top 200 confirms a 0% artifact rate" — by whom, against what reference, with what blinding? No protocol given for visual inspection. PRD expects rigorous artifact diagnostics, not a vibe check.

### P3-M18: Page count
20 pages for a paper whose primary contribution is a catalog (which belongs in a data journal) plus two derivative cosmology analyses is at least 2× too long. **Recommended max: 10 pages** if the catalog is the main contribution, or split.

---

## MINOR Findings

### P3-Mi1: "z-scored" footnote could be one sentence
§II B, p.2.

### P3-Mi2: Fig. 1 dot density at ~378k objects makes spatial structure unreadable
Use HEALPix density map instead.

### P3-Mi3: Table II "Uncategorized" 52.7% is largest class; not useful
Table II, p.8.

### P3-Mi4: Inconsistent rounding in abstract: "~17.8%" vs "82.2% (822/1,000)" in §IV A
Pick a precision and use consistently.

### P3-Mi5: §III A Spearman ρ = -0.03, p = 0.12 — quoting a non-significant correlation as if reassuring
The p-value just means undetected, not zero.

### P3-Mi6: Acknowledgments thank "RunPod" — commercial advertising not appropriate
§ Acknowledgments.

### P3-Mi7: Eq. (E1) reference label is on the wrong side and dimensions implicit
Appendix E.

### P3-Mi8: NANOGrav 15-yr citation [18] uses incomplete author list
"G. Agazie et al." — fine, but cited as the data source AND the GW background detection.

### P3-Mi9: Bibliography entry [33] format inconsistent
Multi-line publication-year note suggests draft state.

### P3-Mi10: "Houston Golden, Independent Researcher" — author affiliation
Not a concern for PRD per se, but the paper claims access to H200 80GB GPUs without explaining institutional access path.

---

## NIT Findings

### P3-N1: "Native CMB convolutional autoencoder" — "native" used in two senses
Sometimes means "per-survey trained" sometimes "ConvNet vs MLP."

### P3-N2: Tables use both "Cross-transfer" and "cross-transfer" inconsistently

### P3-N3: Inconsistent use of em-dash vs en-dash throughout

### P3-N4: "Headline finding" used as a section signpost in every survey subsection — repetitive

### P3-N5: Caption of Fig. 4: "Score = 11.5" presented as physically meaningful but is on the per-survey z-scaled axis without units explained in the caption

---

## Bibliography Audit

- [11] Liang et al. 2023, MNRAS 525, 1078, arXiv:2307.07664 — citation appears correct; quoted statistic "1.07%" matches.
- [18] NANOGrav 15-yr — ApJL 951, L8 (2023) — correct.
- [33] Heinrich, Doré, Krause 2024 JCAP 074 — the in-line note "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]" is a draft artifact and **must be removed**.
- [9] Qu et al. ACT DR6 — citation OK; but the paper "quarantines" ACT, making this citation marginal.

---

## Recomputation Audit

- 378,080 + 200 = 378,280 ✓
- 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493 ✓
- 388,493 - 10,213 = 378,280 ✓
- 77,905 / 12 = 6,492 → "~6500×" ✓ (but threshold mismatch noted in P3-E10)
- αjk = 0.19 ± 0.65 → 0.19/0.65 = 0.29σ ✓
- γ = 2.567 ± 0.382; (3.0 - 2.567)/0.382 = 1.133 ✓
- γ = 2.567 ± 0.382; (4.33 - 2.567)/0.382 = 4.615 ✓
- 17/436 = 3.9% ✓
- 17.8% (178/1000) ✓
- 284/298 = 95.3% ✓

Arithmetic is mostly internally consistent. The problem is what the numbers mean, not their values.

---

## Summary recommendation

**REJECT**

This is a 20-page submission that combines three projects, none of which independently meets the PRD bar. The headline anomaly catalog is partly composed of objects from surveys that fail the authors' own validation gates (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2% recovery — admitted in the text and Fig. 7). The fNL "forecast" is statistically null (αjk = 0.19 ± 0.65, 0.29σ from zero) yet presented as a 7.9% improvement. The NANOGrav re-fit duplicates already-published collaboration analyses without citing them. The manuscript is laden with internal version-control language ("Path-C," "before/after diagnostic," "FAIL-with-diagnostic," "quarantined"), and the abstract uses inflation-marketing framings ("141×", "largest-scale", "decisive") that the body's own caveats undermine. The most salvageable contribution — the DESI-only 195,829-object anomaly catalog with the 17.8% top-1000 novelty fraction — is a data-paper contribution suitable for ApJS or RNAAS, not PRD. The empirical bias measurement is interesting in principle but, as reported, supports no claim; it should be re-attempted with higher-S/N tracers and resubmitted as a focused cosmology paper after the catalog is properly published elsewhere.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report: Fresh-Eyes Re-Examination

After a second pass focused on arithmetic recomputation, figure/body consistency, equation propagation, and stale-number detection, I find a substantial number of issues my initial report missed. These are serious enough to reinforce the REJECT recommendation independent of the initial findings.

---

## NEW ESSENTIAL Findings

### P3-E14: BROKEN LATEX REFERENCES in main text — multiple "Fig. ??" appear in the rendered PDF
**§II A (p.2):** "architecture shown schematically in Fig. ??"
**§II B (p.2):** "into per-band contributions r_B, r_R, r_Z computed over the blue (3600–6200 Å), red (6200–8200 Å), and near-infrared (8200–9800 Å) subsets (Fig. ??)"
**§III B (p.4):** "Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts (128×128 pixels ≈ 54″ per side) for all 12 candidates."

These are unresolved `\ref` macros. A PRD submission with broken cross-references in the body text fails minimum copy-editing standards before scientific review. **Required fix:** Compile cleanly and resolve all references.

### P3-E15: Table VII (Appendix C) and §V Fisher form give inconsistent σ(fNL) at α ≠ 0.15
**§V, p.10; Table VII, p.15.**
- §V uses 1/σ² = F₀ + cα² with F₀ = 1/8.98² = 0.01240, c = 0.0747.
- Table VII uses linear scaling: σ ≈ 8.98 × (1 - (6.1%/0.15)α).

Cross-check at α = 0.50:
- Linear (Table VII): σ = 7.15 (20.4% improvement) — matches the table.
- Quadratic (§V): 1/σ² = 0.01240 + 0.0747 × 0.25 = 0.03108, σ = 5.67 (36.9% improvement).

These do not agree except at the single calibration point α = 0.15 where both yield σ = 8.43. The paper switches between linear and quadratic propagation without acknowledging the discrepancy, and the central headline σ(fNL) = 8.14 uses the quadratic form which gives a much more optimistic improvement curve than Appendix C presents. **Required fix:** Reconcile or remove one of the two parameterizations.

### P3-E16: Fig. 8 cosmological setup is inconsistent with §V — different σ_std baseline
**Fig. 8, p.16; §V, p.10.**
- §V quotes single-tracer baseline σ(fNL)^std = 8.98.
- Fig. 8 caption: "the dotted dark-red line marks the single-tracer baseline (σ(fNL) = 16.85); ... Baseline multi-tracer = 12.72; Ideal (dense limit) = 11.71".

These are different by a factor of ~2× and live in unrelated parameter spaces. The text in Appendix C-1 references "the canonical 5-tracer Fisher of §V" — but §V never describes a 5-tracer Fisher configuration anywhere. The shot-noise analysis is therefore disconnected from the headline forecast. Either Fig. 8 is from a different forecast that should be cited as such, or §V's forecast and Fig. 8 are inconsistent versions of the same calculation. **Required fix:** Reconcile or drop Fig. 8 and Appendix C-1.

### P3-E17: Fisher-positive form structurally cannot produce σ > σ_std — envelope is biased
**§V, p.10; §VI D (i).** The form 1/σ² = F₀ + cα² with c > 0 guarantees σ(α) ≤ σ_std for all α, equality only at α = 0. The reported "1σ envelope [3.92, 8.98]" therefore cannot represent realistic uncertainty in the multi-tracer forecast — observational systematics, negative bias correlations, or selection effects could plausibly make the multi-tracer analysis WORSE than single-tracer, but the assumed functional form prohibits that outcome by construction. This is an optimistic structural assumption disguised as a Fisher result. **Required fix:** Use a parameterization that admits σ > σ_std as physically possible, or explicitly state that the envelope is one-sided optimistic.

### P3-E18: Aggregate SIMBAD-unmatched 58.8% does not reproduce from per-survey numbers
**Table I (p.7); Fig. 5 (p.9).** Per-survey rates (99% DESI, 90% SDSS, 50% LAMOST, 68% eROSITA, 45% NEOWISE, 27% Gaia) with per-survey N values yield a weighted-average unmatched fraction of 89.8% (using full N) or 77.1% (using DESI top-10K only). Simple unweighted average of 6 values: 63.2%. None match the headline 58.8%. The number appears in Table I total row, Fig. 5 dashed line, and §VI C limitations list, but its derivation is not given and I cannot reproduce it from the data shown. **Required fix:** Derive or correct the aggregate.

### P3-E19: "0.874 OOD control-vs-control PASS" appears in conclusion but not derived in body
**§VII conclusion item 6, p.14:** "DESI 5-fold Jaccard stability J¯ = 0.862 (PASS); OOD control-vs-control 0.874 (PASS)." The body (§II B) reports J̄_prod×ctrl = 0.732 and J̄ = 0.862 for 5-fold, but never derives 0.874. This is a phantom number in the conclusions, likely stale from an earlier draft. **Required fix:** Derive or remove.

### P3-E20: SDSS native threshold inconsistent with LAMOST native — both labeled "top-percentile"
**§III C; §III D; Table I footnote ‡.** LAMOST native cut at S ≥ 0.4613 yields 113,342 anomalies = 0.992% ≈ 1% (consistent with top-1%). SDSS native cut at S ≥ 0.1060 yields 77,905 anomalies = 4.05% (NOT 1%). Yet both are described as "top-percentile" Path-C native catalogs. The SDSS native catalog size was chosen to match the cross-transfer count of 77,905, not a uniform top-1% threshold. This is methodologically asymmetric and undocumented. **Required fix:** Either apply a uniform percentile threshold, or document why SDSS native uses 4.05% while LAMOST uses 1%.

---

## NEW MAJOR Findings

### P3-M19: NEOWISE mask threshold inconsistent between §II D, §III H, and Fig. 7
- §II D step 4: "|b_ecl| < 80°"
- §III H: same 80° threshold
- Fig. 7 caption: "PASS, 1000/1000 = 100% at |b_ecl| > {85°, 82°, 80.5°}"

The figure caption uses three different thresholds (with > inequality, opposite direction from the body's <), with no body explanation for why three values were tested or which corresponds to the catalog. **Required fix:** Use consistent threshold notation throughout.

### P3-M20: Per-band scores r_B, r_R, r_Z introduced without definition
**§II B, p.2.** "we additionally decompose the score into per-band contributions r_B, r_R, r_Z computed over the blue (3600–6200 Å), red (6200–8200 Å), and near-infrared (8200–9800 Å) subsets". No equation relating r_B/r_R/r_Z to S is provided. Yet §III B uses them: "rZ = 5.30" with "mean ⟨rZ⟩ = 3.9 across the 12 selected candidates; all objects have total score S > 5". If mean rZ = 3.9 and S > 5 is required, the relationship between sub-scores and total cannot be additive equally — readers cannot verify the high-z candidate selection. **Required fix:** Define the per-band score formula.

### P3-M21: SDSS injection-recovery PASS uses better-of-two protocol, LAMOST FAILs both
**§II D step 5; Fig. 7.** SDSS continuum-dip = 64% (PASS), SDSS emission-line = 7.2% (FAIL). LAMOST continuum-dip = 5.8% (FAIL), LAMOST emission-line = 0.6% (FAIL). The headline "3 PASS / 3 FAIL" gives SDSS the credit of its higher-performing variant. If gates required passing both injection types, SDSS would also FAIL. The protocol is asymmetric — pick-the-better-of-two for SDSS but neither for LAMOST. **Required fix:** Define and apply a symmetric pass criterion.

### P3-M22: Emission-line plant recovery as low as 0.6% means narrow-line anomalies are missed
**§VI D (ii), p.13.** Authors admit: "narrow in-distribution features are reconstructed accurately whereas broad continuum deformations elevate MSE effectively." Translation: the autoencoder is BLIND to narrow emission-line anomalies — which are precisely the scientifically interesting population (high-z Lyα, AGN broad lines, etc.). LAMOST emission-line recovery of 0.6% means 99.4% of injected narrow-line anomalies are MISSED. This is a fundamental completeness ceiling for the entire scientific use case (rare-line-emitter searches) but is mentioned only as a methodological aside. **Required fix:** Add this as a primary limitation in §VI C; reassess novelty claims given known blindness to narrow emission features.

### P3-M23: Pearson p-value (Galactic correlations) computed on pixels but reported as if on sources
**§IV B, p.10.** "no correlation with Planck dust intensity (Pearson r = 0.006, p = 0.21)". For r = 0.006 with N = 195,829 sources, p ≈ 0.008 (significant). With N = 38,330 pixels (Nside=64), p ≈ 0.24 (matches reported 0.21). The text doesn't say which N is used. Readers cannot reproduce or interpret without this critical detail. **Required fix:** State the sample size for each correlation.

### P3-M24: "5,384 QSO-candidate sample" and "1,122-object Gold+Silver subset" undefined in §V
**§V, p.10.** Both sample selections appear without prior definition. The reader has no idea how the 5,384 QSO candidates were selected from the 195,829 DESI anomalies, what "Gold" and "Silver" subdivisions mean, or what cuts produced 1,122 from 5,384. These are the inputs to the headline αjk = 0.19 ± 0.65 measurement. **Required fix:** Specify selection criteria explicitly.

### P3-M25: Table I total row mixes accounting standards (ACT in input total, NEOWISE pre-mask in anomaly total)
**Table I, p.7.** Total N_total = 37,292,042 = 37,272,042 (7 retained) + 20,000 (ACT inputs). N_anom total = 319,443 = 319,243 (7 retained, with NEOWISE pre-mask 436) + 200 (ACT cross-transfer). The "total" row therefore INCLUDES ACT inputs and outputs even though ACT is "quarantined" elsewhere, and uses NEOWISE pre-mask 436 rather than post-mask 419. The aggregated numbers reported in the total row do not correspond to either the cross-transfer-only baseline or the Path-C final catalog cleanly. **Required fix:** Reconstruct Table I with consistent accounting.

### P3-M26: §V references "1,122-object Gold+Silver" σ(fNL)^GS = 1.95 from α_GS = 1.83 ± 2.03 = 0.9σ measurement
**§V, p.10; §VI D (j).** The Gold+Silver re-measurement gives α_GS,jk = 1.83 ± 2.03, which is 0.9σ from null — even less significant than the headline 0.29σ. Yet σ(fNL)^GS = 1.95 (4.6× improvement) is reported as a central value. Repeating the P3-E1 mistake: a 0.9σ measurement does not justify a quoted improvement at 4.6×. **Required fix:** Match the disclosure standard required of any null result.

### P3-M27: Savage-Dickey "decisive on Jeffreys' scale" — applies to point-vs-prior, not point-vs-point
**§V A, p.11.** B_MB/free = 3.23 and B_SMBHB/free = 4.52×10⁻⁴ are Savage-Dickey ratios of point hypotheses against the uniform-γ prior. Their ratio B_MB/SMBHB = 7.14×10³ is mathematically the ratio of posterior densities at the two test points — not the same as a true Bayes factor between two model classes (which would require integrating over the SMBHB γ distribution from astrophysical priors, not assuming a delta function at 4.33). Calling 7.14×10³ "decisive" on Jeffreys' scale applies that scale outside its standard interpretation domain. **Required fix:** Drop "decisive" label or compute a proper model-class Bayes factor with astrophysical priors on SMBHB γ.

### P3-M28: NANOGrav γ = 2.567 ± 0.382 not compared to NANOGrav's own power-law fit
**§V A; ref [28].** Ref [28] (Afzal et al. 2023, NANOGrav 15-yr new physics) reports power-law fits to the same data. The authors do not cite this comparison or reconcile their γ with the collaboration's result. As a "verification" of bounce predictions, this is a derivative analysis at best. **Required fix:** Compare to and cite [28] explicitly.

### P3-M29: Eq. (E1) — formula correct but T_obs sign convention non-standard for some conventions
**Appendix E.** The standard NANOGrav free-spectrum coefficient relates to PSD via ρ² = P(f)/T_obs (so log10 ρ has -½ log10 T_obs); the displayed equation places the -log10 T_obs inside the prefactor consistent with this. Minor: confirm convention against the ceffyl product documentation explicitly.

### P3-M30: Acknowledgments use of "RunPod" repeated
Already flagged in P3-Mi6 but escalating: in an unfunded independent-researcher submission to PRD, commercial-platform acknowledgments may be acceptable but warrant a disclosure of any commercial relationship.

---

## NEW MINOR Findings

### P3-Mi11: Fig. 2 left panel caption "S = 24.6/25.2" labels overlap visually unreadable
Three labels stack at the same x position — caption text says "S > 24" but the labels are illegible in the rendered version.

### P3-Mi12: Mean ⟨rZ⟩ = 3.9 vs top candidates rZ = 5.30, 5.18
With 12 candidates and two having rZ > 5, the average rZ = 3.9 implies the other 10 candidates have ⟨rZ⟩ ≈ 3.6. Distribution should be shown.

### P3-Mi13: Inconsistent reporting of NEOWISE polar fraction
"17 objects concentrate in the 10°-radius polar caps" — but |b_ecl| ≥ 80° corresponds to caps of half-angle 10°. The two formulations should be unified.

### P3-Mi14: Fig. 1 says "8 archives" in title but 7 are retained
Fig. 1 figure title is now-stale — body text never has "8 archives" as the operative count.

### P3-Mi15: §VI D Table IV "(b) DESI OOD: training-pool cut flags 52.8% of OOD (61× headline)"
Cross-references "§II" for resolution but the §II B paragraph cites 52.8% via "> 50%" and "see §VI D (b) for the full OOD reconciliation". Each section points to the other; the actual reconciliation is at neither location.

### P3-Mi16: Reference [11] arXiv 2307.07664 — sample size in body is "∼ 250,000 DESI EDR spectra" but Liang et al. processed a slightly different sample size (~250k DESI EDR Bright Galaxy Survey).

### P3-Mi17: Two definitions of "score knee" (eROSITA threshold)
The "score-knee threshold" terminology used for eROSITA is never operationally defined.

### P3-Mi18: "Quasi-matter bounce" vs "matter bounce" interchanged
"the quasi-matter bounce model predicts fNL = −35/8 = −4.375" (introduction) but later "matter bounce" throughout (§V, §VI F). These may be the same model class but should be terminologically unified.

---

## NEW NIT Findings

### P3-N6: Inconsistent ellipsis style ("∼ 250,000" vs "~ 113,000" vs "∼113,000")
### P3-N7: "Fisher positivity-respecting" appears 4× — verbose phrasing
### P3-N8: §II D enumeration uses different sentence-fragment style than rest of paper (e.g., "Native retrain (two-part gate)." vs full sentences elsewhere)
### P3-N9: Equation (E1) reference "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]" — additional reviewer-process residue in ref [33]
### P3-N10: Trailing dashes ("—") used as full punctuation in abstract — unusual style for PRD

---

## Recomputation Audit (additions)

- F₀ = 1/8.98² = 0.012401 ✓
- At α=0.19, σ from quadratic = 8.137 ≈ 8.14 ✓
- At α=0.84, σ = 3.917 ≈ 3.92 ✓
- At α=-0.46, σ = 5.954 (not in envelope; range maximum is at α=0 → 8.98) ✓
- Table VII at α=0.50: linear gives 7.15 (20.4% improvement); quadratic gives 5.67 (36.9% improvement) — **DISAGREE**
- σ_GS at α=1.83: 1/σ² = 0.01240 + 0.0747×3.349 = 0.2625 → σ = 1.952 ≈ 1.95 ✓
- σ_GS at α=3.86: σ = 0.943 ≈ 0.94 ✓
- BMB/BSMBHB = 3.23/4.52e-4 = 7146 ≈ 7.14×10³ ✓; log10 = 3.854 ≈ +3.85 ✓
- (3.0-2.567)/0.382 = 1.133 ✓
- (4.33-2.567)/0.382 = 4.615 ✓
- Aggregate Table I N_total = 37,272,042 + 20,000 (ACT) = 37,292,042 ✓; **ACT inputs included despite quarantine**
- Aggregate Table I N_anom = 319,243 + 200 (ACT) = 319,443 ✓; **uses NEOWISE pre-mask 436**
- SDSS native 77,905/1,925,279 = 4.05%, NOT top-1% as described
- LAMOST native 113,342/11,418,594 = 0.992% ≈ 1% ✓
- 0.4437/0.30 - 1 = 47.9% over CMB val_loss threshold ✓
- Pearson r=0.006 at N=38,330 pixels: t = 1.175, p ≈ 0.24 (matches paper's 0.21 ± rounding); at N=195,829 sources: p ≈ 0.008 — **paper does not specify which N**

---

## Updated Summary

The fresh-eyes pass uncovered an additional **6 essential and 12 major issues** that the initial review missed. The most serious new findings are:

1. **Broken LaTeX cross-references** in the rendered body — minimum-standard compile failure.
2. **Two inconsistent forecast equations** (linear in Appendix C vs quadratic in §V) giving different σ at every α except calibration.
3. **Fig. 8 lives in a parameter space disconnected from §V** — different baseline σ, undefined "5-tracer" setup.
4. **Fisher-positive form structurally one-sided** — cannot represent worse-than-baseline outcomes.
5. **Aggregate SIMBAD 58.8% not reproducible** from per-survey data.
6. **Phantom "0.874" Jaccard** in conclusions never derived in body.
7. **Per-band r_B/r_R/r_Z scores undefined** despite being used to select high-z candidates.

These compound the issues in the initial review. The paper has structural arithmetic inconsistencies between its main-text and appendix forecasts, broken references in the rendered body, and undefined quantities that downstream selections depend on. Beyond the scientific concerns of the first pass, the manuscript also fails basic typesetting and arithmetic-self-consistency checks expected of any submission.

**Recommendation remains: REJECT.** A revised version would require, at minimum: (i) all LaTeX references resolved; (ii) one coherent fNL forecast (not two contradictory parameterizations); (iii) reproducible aggregate statistics; (iv) all sample selections (5,384 QSO; Gold/Silver) defined; (v) elimination of internal version-control language; (vi) symmetric injection-recovery gating; (vii) explicit comparison to NANOGrav's own γ measurement; (viii) abstract restricted to claims supported at >1σ; and (ix) split into separate catalog and cosmology papers in venue-appropriate journals.