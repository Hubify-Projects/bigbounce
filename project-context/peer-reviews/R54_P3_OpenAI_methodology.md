# P3 R54 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R54_P3/paper3_draft.pdf` md5=84563f72 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8531 chars)
**Wall time**: 497.8s

---

Referee report (Methodology/Statistical Rigor) — Physical Review D

Scope of review
I audited the entire manuscript (29 pages), including abstract, all figures/tables, equations, and appendices, focusing on: estimator definitions; validation gates; reproducibility and provenance; statistical claims (σ, p-values, Bayes factors); arithmetic and percentage consistency; and dimensional correctness. I recomputed all headline ratios and many intermediate percentages; I checked cross-survey bookkeeping (dedup, thresholds) and cosmology inferences (Fisher forecast, PTA posterior).

Findings are grouped by severity: ESSENTIAL (blocking), MAJOR, MINOR, NIT. For each, I give an ID, page/section anchor, the issue (with direct quotation where applicable), and a concrete required fix.

ESSENTIAL

P3-E1 — eROSITA score axis irreproducible (membership-only tier)
- Location: Sec. III E (pp. 11–12), Table I note “#”, Table IV caption
- Issue: The paper states “the per-object SBigAE score axis is irreproducible… 16 monotone rescalings… the production top-5 values are non-monotone… the committed, reproducible selection is the n = 298 membership list.” As written, a published catalog component cannot be reproduced from the stated algorithm, and the paper still uses a non-reproducible axis value (“0.259 threshold”) textually as if it were operational.
- Required fix: Either (a) re-derive and publish a fully reproducible scoring axis and threshold for eROSITA (with committed code/seed and a frozen artifact so any reader can regenerate scores and reproduce the 298-member cut exactly), or (b) purge all non-reproducible score values from the text/tables and present the eROSITA contribution strictly as a membership list with a clearly marked “no reproducible score available” flag in the release schema, and ensure every place the eROSITA “rate” is referenced rephrases it as “predetermined fixed-count selection, not a measured rate.” The current text already gestures at this; PRD requires you to resolve the ambiguity and excise the irreproducible threshold from the main narrative and tables.

P3-E2 — Planck tier trained-and-scored on same patch bank; publish a held-out top-200
- Location: Sec. III F (p. 12)
- Issue: The Planck native CAE’s released top-200 is selected from a bank that includes its own training patches (“the native bank is scored in full — including the patches used for training — so the released top‑200 is not a held‑out selection”). You argue against memorization via an over-representation of validation patches among top‑200, but the published catalog remains an in-sample selection.
- Required fix: Publish the Planck tier based on a pure holdout: re-split the 2×10^5 bank into disjoint train/val/test, score only the test set, and release the top‑k from test. Retain the in-sample ranking as a diagnostic in the Supplement. At minimum, provide a second held-out-only top‑200 that you commit to as the catalog-grade Planck tier, and keep the in-sample tier quarantined as exploratory.

P3-E3 — Cramér’s V equation miswritten (missing square root in numeric substitution)
- Location: Sec. IV B (p. 15), paragraph beginning “A spatial uniformity test…”
- Issue: You define “Cramér’s V = √(χ^2/(N·(k−1)))” but then write “= 376,713/(378,280 × 24,047) ≈ 0.0064” (no square root in the numeric line). The 0.0064 value is √(376,713/(378,280×24,047)); the way it is typeset is formally inconsistent/dimensionally wrong.
- Required fix: Correct the displayed numeric substitution to include the square root explicitly (e.g., V = √[376,713/(378,280 × 24,047)] = 0.0064). This is a methodological statistic; the algebraic chain must be correct.

P3-E4 — Train/validation leakage in tabular survey scalers; missing checks for Gaia/NEOWISE
- Location: Sec. II B (pp. 3–4), paragraph “Tabular-survey feature preprocessing…”
- Issue: You acknowledge that for eROSITA, NEOWISE, Gaia the feature scalers were fit on the full sample (not just the training split), introducing validation/tail information leakage into normalization. You provide a bounded robustness check only for eROSITA; for Gaia and NEOWISE you state “remain queued” and yet publish top‑1% selections and downstream novelty fractions.
- Required fix: Refit scalers on the training-split only for Gaia and NEOWISE, retrain, and provide the same robustness metrics you computed for eROSITA (top‑k Jaccard, top‑1% Jaccard, Spearman ρ). If you cannot rerun in time, at minimum mark the Gaia/NEOWISE tiers as exploratory wherever they appear (not just once), and remove any quantitative claims that could be sensitive to extreme‑tail reorderings (e.g., top anomaly description) until the leakage check is completed. PRD requires that core selections not rely on acknowledged leakage without a quantified robustness bound for each affected survey.

P3-E5 — NEOWISE “PASS” injection-recovery is not a detector sensitivity test; avoid tallying it as a PASS
- Location: Sec. II D Step 5 (p. 5), Sec. III H (p. 13), Fig. 10 (p. 22), Table I Notes († and main text)
- Issue: You frequently summarize “3 PASS” in injection-recovery gates and include NEOWISE’s 100% “PASS,” but you also state it is “a masking-geometry sanity check that passes by construction.” Counting it alongside true detector sensitivity PASS (SDSS, Planck) confuses readers.
- Required fix: In every place a PASS count is tallied, explicitly break it out as “2 PASS (detector sensitivity) + 1 geometry QA PASS (NEOWISE).” In Fig. 10, visually demote or separate the NEOWISE curve (e.g., gray/hatched, legend note “geometry QA”) and change the figure caption’s PASS summary accordingly. In Table I and conclusions, never state “3 PASS” without the decomposition.

P3-E6 — Data availability/provenance placeholders
- Location: Abstract (p. 1), Data availability (p. 23)
- Issue: The manuscript uses future-tense placeholders (“will be publicly released with the arXiv posting”; “DOI inserted at submission”). For PRD acceptance these must be concrete. Many run-artifact paths are cited, but without a frozen, citable DOI/commit tag set.
- Required fix: Provide a minted DOI (Zenodo or equivalent) for all released datasets (catalog tables, dedup manifest, Planck patch bank index, PTA chains). Provide a frozen Git commit hash for the training/inference code used, and a manifest of SHA256 and sizes (already mentioned) in the Supplemental with an explicit version tag dated to this submission. Remove all future-tense placeholders.

MAJOR

P3-M1 — False-match baseline for SIMBAD needs backing
- Location: Sec. IV A (p. 14), “Expected false-match rates”
- Issue: You quote nSIMBAD ≈ 3.0×10^-5 arcsec^-2 leading to Pfalse ≈ 2.4×10^-3 at 5″. No method for estimating this surface density is reported (global count? epoch? mask?).
- Required fix: Add a short methods note: how nSIMBAD was computed (HEALPix map, footprint, magnitude cut if any), the epoch of the snapshot, and the uncertainty. Alternatively, compute and report a HEALPix-weighted local-density map and give the median and interquartile Pfalse. This grounds the “negligible” statement quantitatively.

P3-M2 — SDSS “headline 77,905” is a fixed-size slice; ensure it is never used as a rate
- Location: Table I (p. 7) and Sec. III C (p. 9)
- Issue: The 77,905 SDSS number is a continuity slice sized to match the cross-transfer count, not a top‑1% or S>5 threshold. While you explain this, the table’s “Rate 3.38%” in the cross-transfer block and “4.05%” native slice can be misread as comparable to DESI’s 0.87% rate.
- Required fix: In Table I, replace the SDSS “Rate (%)” cell for the native 77,905 slice with “— (fixed-size slice; not a rate)” and move the true native top‑1% and S>5 counts to a parenthetical note in the table or to a second line. Where a percentage is given, explicitly label it “fraction of scored pool retained by fixed-size slice,” not an anomaly rate.

P3-M3 — Visual-inspection “0/200 flagged” requires explicit protocol
- Location: Sec. III A (p. 8), paragraph “Spectral inspection of the top 200”
- Issue: You claim 0/200 visually flagged for DESI top-200 after checking against “11 known sky and telluric features.” Without a list and a decision rule, this is not reproducible.
- Required fix: Add an appendix or Supplemental table listing the 11 features, the matching tolerance, the S/N or residual thresholds used, and a link to the inspection log (object IDs and pass/fail with the reason). Otherwise, soften the claim to a qualitative survey.

P3-M4 — Use of internal path artifacts in main text
- Location: Multiple occurrences (e.g., pp. 4–6, 12, 15, 16, 23), “pipelines/p3_anomaly_engine/...json”
- Issue: Citing internal file paths in the main text is not standard PRD style. These belong in a documented Supplemental (or Methods Appendix) with a single pointer in the main text.
- Required fix: Consolidate all artifact paths and checksums into a Supplemental “Provenance Manifest” and replace in-text path dumps with a single reference (e.g., “see Supplemental S.3, Items A12–A18”).

P3-M5 — Fisher forecast details for bias measurement need minimally more detail
- Location: Sec. V (pp. 18–19)
- Issue: The Landy–Szalay and Fisher blocks are summarized briefly. For reproducibility, readers need the multipole(s) used, k-range mapping from θ-bins, masking/footprint handling, and random catalog generation details (e.g., 26,920 randoms: how constructed?).
- Required fix: Add a short methods appendix with: θ-bin edges; mask/apodization; random generation method; how the jackknife regions were defined; and the mapping from α to the Fisher block (what baseline power spectrum, bias priors, assumed volumes). The positivity-respecting quadratic mapping is clearly given; the rest needs operational parameters.

MINOR

P3-m1 — Aggregation at different cone radii (3″ vs 5″) may confuse
- Location: Sec. IV A (pp. 13–14), Fig. 6 caption
- Issue: You use 5″ for per-survey SIMBAD rates but 3″ for the pooled 58.8% figure. You do say this explicitly, but the figure caption should highlight it more prominently.
- Required fix: Add a bold parenthetical in Fig. 6 caption: “Note: pooled value computed at 3″; per-survey bars at 5″.”

P3-m2 — Hearts/spades symbols in Table I footnotes are non-standard
- Location: Table I footnotes (p. 7)
- Issue: Non-standard symbols (♡, ♠, ♢, #) can cause encoding issues.
- Required fix: Convert to numeric or alphabetic footnote markers, consistent with PRD style.

P3-m3 — Equation/notation consistency
- Location: Eq. (1) and surrounding text (pp. 3–4)
- Issue: You use xˆ and x̂ inconsistently in the text (“xˆ = BigAE(x)”; later “|xi − xˆi|”).
- Required fix: Standardize to a single hat notation (x̂).

P3-m4 — Length and density
- Location: Whole manuscript (29 pages)
- Issue: For a methods paper with one primary architecture, the level of in-text internal artifact references and long footnotes makes the paper denser than necessary for the core claims.
- Required fix: Consider moving the bulk of internal-provenance notes, alternative dedup radii sweeps, and training-log minutiae to a Supplemental, reducing the main text by ~15–20% without loss of content.

P3-m5 — Minor arithmetic verifications (all OK but suggest in-text clarifiers)
- Location: Various
- Checks: I confirmed numerous ratios: 195,829/22,504,897 = 0.870% (DESI); 77,905/2,304,830 = 3.38% (SDSS cross-transfer); 113,342/11,334,161 ≈ 1.00% (LAMOST native top‑1%); 298/930,203 ≈ 0.032% (eROSITA); dedup compression 10,213/388,493 = 2.629%; DESI science-bit match 2,468/20,299,155 = 0.0122%. All consistent. Suggest adding one-line arithmetic for the dedup compression percentage in the text.

NIT (cosmetic/typographic)

P3-n1 — Hyphenation artifacts (“over￾plotted,” “valida￾tion”)
- Location: Multiple pages (PDF hyphenation artifacts)
- Fix: Clean typesetting.

P3-n2 — Duplicate phrasing scan
- Location: Various
- Issue: I did not observe egregious duplicates (e.g., “canonical canonical”). No action unless copyedit finds any.

P3-n3 — Clarify units once for Planck patch MSE
- Location: Sec. III F (p. 12)
- Fix: State explicitly “per-patch standardized MSE, unitless” next to the [0.558, 0.621] range.

Checks of headline statistical claims (audit)

- Abstract headline counts/rates: 378,280 total = 378,080 point-source + 200 Planck (OK); 269,317 catalog-grade point-source subset (OK from 6-way dedup; you document sensitivity excluding LAMOST).
- “141× larger than prior catalog [11]”: 378,080/2,685 ≈ 141.0× (OK). “Catalog-grade alone ~100×”: 269,117/2,685 ≈ 100.2× (OK). “DESI-only 73×”: 195,829/2,685 ≈ 72.9× (OK, caveat given that not like-for-like).
- DESI science-class-restricted recount: 2,468 vs. 2,685 ≈ 0.92× (you state ≈0.9×; OK).
- Jaccard gates: DESI k-fold J̄ = 0.862 (≥0.70 PASS) and production×control 0.732 (≥0.50 PASS) (OK).
- Injection-recovery: SDSS 64%, LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%, Planck 100%, NEOWISE 100% (geometry) (OK; see P3-E5 for presentation).
- NEOWISE polar-cap anomaly: k=17 of n=436 vs p0=1.52% → z≈4.07; p ≈ 6×10^-5 (your numbers are consistent).
- SIMBAD false-match at 5″: with n≈3×10^-5 arcsec^-2 → Pfalse ≈ 0.00236 (0.236%); 0.24% quoted (OK; see P3-M1).
- Dedup robustness to radius: counts 378,604 / 378,280 / 378,145; maximum deviation 324/378,280 = 0.0857% (OK; you report 0.086%).
- PTA posterior: γ = 2.567 ± 0.382; distance to 3.0 is +1.13σ; to 4.33 is +4.61σ (OK). Savage–Dickey factors as quoted (prior-sensitive; OK).
- Fisher forecast: baseline σ(fNL)std = 8.98; with α̂=0.19, c=0.0747 → σ=8.14; de-biased to 8.98; 1σ envelope [3.92, 8.98] (OK). You clearly indicate convexity/noise bias and “not a detection.”

Overall, the internal arithmetic/percentages are careful and largely correct. The two substantive methodology blockers are eROSITA irreproducibility (P3‑E1) and the Planck in-sample publication (P3‑E2). The scaler leakage (P3‑E4) needs to be either corrected or bounded for Gaia/NEOWISE before acceptance.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript is careful and unusually transparent about gates, caveats, and arithmetic. However, PRD requires full reproducibility for published catalog components and rigor in selection protocols. Publishing a tier whose score axis is unreproducible (eROSITA) and a Planck tier selected from a set that includes training patches are both unacceptable in their current form. Additionally, the tabular-scaler leakage for Gaia/NEOWISE must be either corrected or bounded as you did for eROSITA. These are fixable. Once addressed, and with minor presentation clarifications (Cramér’s V equation; injection-recovery PASS tally; SIMBAD density method), the paper can meet PRD’s methodological bar.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P3-E7 — Spectroscopic injection-recovery “σ” undefined; gate not reproducible
- Location: Sec. II D Step 5 (p. 5), Sec. III C/D, Fig. 10 caption
- Issue: For SDSS and LAMOST you report continuum-dip/emission-line recovery “at 5σ,” but the definition of σ (noise model) and the plant construction are not specified: per-pixel vs per-arm? pipeline inverse-variance vs empirical RMS? spectrum-level aggregation (e.g., χ2-weighted)? Planck’s σ definition is explicit; the spectroscopic ones are not.
- Required fix: Provide an explicit formula for σ used in spectroscopic plants (including how per-wavelength variances are obtained and aggregated), the injection waveform(s) and widths, normalization, and how recoveries are adjudicated relative to the survey’s S threshold. Without this, the 5σ gate is not reproducible.

P3-E8 — “Catalog-grade” label includes components that fail core validation gates
- Location: Abstract (p. 1), Table I note ♠/#/⋆, Sec. VII bullet 1–2 (p. 22–23)
- Issue: The “catalog-grade tier” of 269,317 unique entries explicitly includes Gaia (41% XV-stability; 5σ FAIL) and eROSITA (1.2% recovery; membership-only; 5σ FAIL), i.e., exploratory components by your own gate logic. Calling the union “catalog-grade” is misleading.
- Required fix: Either (a) redefine “catalog-grade” to include only detectors that clear a sensitivity gate (DESI, SDSS native, Planck native), and move Gaia/eROSITA to an “exploratory” tier, or (b) retain the 269,317 union but rename it to “primary deduplicated tier (with per-object validity flags)” and reserve “catalog-grade” for the strictly validated subset. Update abstract, Table I summary rows, conclusions.

P3-E9 — Planck table denominator ambiguity can mislead rate interpretation
- Location: Table I (p. 7), note ♢; Sec. III F (p. 12)
- Issue: The table shows Ntotal = 20,000 and Rate = 1.00% for Planck while the released native tier is selected from a 200,000-patch bank (where the same 200 corresponds to 0.10%). Despite the footnote, readers will naturally read “1.00%” as the operative rate.
- Required fix: Replace the single “Rate (%)” cell with “— (fixed-count 200/200k = 0.10% on native bank; legacy 1.00% on the 20k cross-transfer bank)” or split Planck into two lines (cross-transfer input vs native). Avoid any single percentage that can be construed as a measured detection rate.

MAJOR

P3-M6 — Abstract overstates injection-recovery PASS for NEOWISE without decomposition
- Location: Abstract (p. 1), sentence “SDSS, Planck, and NEOWISE pass injection-recovery...”
- Issue: In the main text you repeatedly clarify NEOWISE’s “PASS” is a geometry QA (guaranteed by construction), not a detector-sensitivity pass. The abstract lacks this qualifier.
- Required fix: Amend the abstract to “SDSS and Planck pass detector-sensitivity injections; NEOWISE passes a masking-geometry QA check (by construction).”

P3-M7 — Figure 11 normalization mismatch not conveyed inside the figure
- Location: Appendix C Fig. 11
- Issue: The figure’s σ(fNL) axis uses an internal normalization (single-tracer baseline 16.85) that is not comparable to the §V baseline (8.98). The note appears only in the caption text block on the next page; the figure itself can be misread in isolation.
- Required fix: Add an in-figure annotation (“internal normalization; not comparable to §V”) or a bold subtitle under the panel title indicating the normalization caveat.

P3-M8 — “We test Planck×ACT cross-correlation” but no statistic reported
- Location: Sec. IV D (p. 17–18)
- Issue: The section is framed as a test yet reports no scalar statistic, only a narrative null with caveats. PRD readers expect at least a defined metric (e.g., cross-K function, two-point estimate with randoms) even if you conclude “non-diagnostic.”
- Required fix: Either supply a simple, reproducible scalar cross-correlation diagnostic and its value (plus a geometry-aware null), or rephrase to “We inspected…” and move it to an appendix as a qualitative check.

P3-M9 — Inconsistent use of S/score nomenclature for eROSITA (“SBigAE” vs canonical S)
- Location: Sec. III E (pp. 11–12), Table IV caption
- Issue: The term “SBigAE” is introduced for the irreproducible production axis, while S is defined canonically in Eq. (2). This risks confusion about what “S” means on eROSITA rows and in any combined plots.
- Required fix: Standardize terminology: use “S (canonical)” everywhere else, and for eROSITA label the column “production-axis score (irreproducible)” or drop the column entirely per P3-E1. State explicitly in the main text that eROSITA contributes no canonical S.

P3-M10 — Missing operational details for Landy–Szalay/randoms beyond counts
- Location: Sec. V (pp. 18–19)
- Issue: You give random-count and jackknife-region count but omit mask/apodization, angular-binning edges, and the random-catalog generation procedure (footprint tiling, veto masks).
- Required fix: Add a brief methods paragraph (or appendix) with θ-bin edges, mask/apodization recipe, random generation (including selection-function weighting), and jackknife-partition scheme. This is needed to reproduce αjk.

P3-M11 — Per-survey SIMBAD false-match density lacks uncertainty and footprint handling
- Location: Sec. IV A (“Expected false-match rates,” p. 14)
- Issue: You provide a single global nSIMBAD with no method or uncertainty; crowding varies strongly across the sky.
- Required fix: Report HEALPix-binned local SIMBAD densities (median and IQR) over the relevant footprints and give the per-object or per-survey median Pfalse with spread. This grounds the “negligible” claim.

MINOR

P3-m6 — Figure–text unit clarity for Planck MSE
- Location: Sec. III F (p. 12), “range [0.558, 0.621]”
- Issue: The body does not immediately state the units/normalization of the Planck MSE axis.
- Required fix: Add “(per-patch standardized MSE; unitless)” inline where the range is first quoted (you already say this in a footnote later).

P3-m7 — Heterogeneous “S” definitions across figures need on-plot qualifiers
- Location: Fig. 3 (both panels), Fig. 8 (panel labels)
- Issue: The right panel of Fig. 3 uses DESI-trained cross-transfer S on SDSS; Fig. 8 shows “display scores” that are not catalog S. While the captions note this, on-plot labels can still mislead.
- Required fix: Add small on-plot legends: “S (DESI-trained, transfer axis)” for Fig. 3 right; “display-only (non-catalog) value” on Fig. 8 panels.

P3-m8 — MAE vs MSE terminology for per-arm residuals
- Location: Sec. II B (p. 4), per-band rB,rR,rZ definition
- Issue: The main loss is MSE, but rX are mean absolute residuals (MAE). This is correct but could confuse readers scanning quickly.
- Required fix: Say “mean absolute residual (MAE)” explicitly when introducing rX.

P3-m9 — Minor cross-reference clarity
- Location: Sec. II C/II D vs Table V caveat (b)
- Issue: The >50% OOD-flag claim for SPARCL is reconciled via Table V (b), but the path is hard to follow.
- Required fix: Add an inline parenthetical “(see Table V(b) for the OOD/control reconciliation and exact denominators).”

P3-m10 — Prime/arcsecond glyph consistency
- Location: Throughout (e.g., 5′′, 10◦×10◦)
- Issue: Mixed use of Unicode primes/degree marks can vary across typesetters.
- Required fix: Standardize to LaTeX \arcsec, \deg, etc., to avoid encoding artifacts.

NIT

P3-n4 — Notation spacing for Jaccard bars
- Location: Sec. II B/C and Table V (e.g., J¯CV, J¯ prod×ctrl)
- Fix: Remove stray spaces (“J¯CV”, “J¯prod×ctrl”) for consistency.

P3-n5 — “Largest to our knowledge” claim could cite a survey for multi-archive scale
- Location: Abstract (p. 1)
- Fix: Add a parenthetical supporting comparison for “largest multi-archive autoencoder sweep” (e.g., a short literature sentence or explicit search scope) to preempt editorial queries. Not a blocker, but easy polish.

Explanation
I focused on fresh classes of problems your prior review did not target: reproducibility of the spectroscopic injection gate (σ definition), tier labeling vs gate outcomes (“catalog-grade”), denominator clarity for Planck’s rate, abstract-level overstatement for NEOWISE, and several figure/normalization mismatches that can confuse readers. I did not repeat earlier findings (eROSITA irreproducible axis, Planck in-sample selection, Cramér’s V numeric line, scaler leakage, PASS tallying, data/DOI placeholders, etc.). Where arithmetic was rechecked, no new inconsistencies emerged beyond presentation/clarity items noted above.