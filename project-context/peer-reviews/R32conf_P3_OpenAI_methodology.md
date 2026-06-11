# P3 R32conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.93.pdf` md5=a3504a9b pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9595 chars)
**Wall time**: 375.7s

---

Referee report (methodology rigor) — Physical Review D

Manuscript: “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path‑C Unique Anomalies ...”

Overall assessment
The paper presents an ambitious, multi-survey autoencoder anomaly campaign with extensive internal audits and many caveats. However, as submitted it contains (i) methodology-exposition issues (internal version-history language, placeholders, and irreproducible score axes in a main table), (ii) at least one load‑bearing formula with a dimensional inconsistency even though the numerics later use the correct value, (iii) several places where queued robustness checks are not yet executed, and (iv) table/caption structures that mix baseline and final results in ways that are confusing for a reader. The paper is also overly long for the claimed contribution and reads as a lab log rather than a PRD methods paper in multiple sections.

Below I list specific findings with required fixes. I recomputed every ratio/percentage quoted in the abstract and conclusions from the numbers in the body; all arithmetic checks noted explicitly below.

Findings and required actions

ESSENTIAL

P3-E1 (Section V.b, p. 16; Table IV row (i), p. 20)
Problem: Dimensional/definition error in the Fisher “positivity-respecting” formula. You write 1/σ^2(fNL) = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747. This is dimensionally inconsistent if σstd = 8.98 is the baseline uncertainty: F0 must be 1/σstd^2, i.e., F0 = 1/(8.982) ≈ 0.01239, not 1/8.98 ≈ 0.111. Your subsequent numerical results (σ = 8.14 for α = 0.19; envelope [3.92, 8.98]) are consistent with F0 = 1/(8.98)^2, so the text is wrong even though the computation appears correct.
Required fix: Correct every occurrence of F0 to F0 = 1/σstd^2 = 1/(8.982) and state σstd once unambiguously. Re-derive all quoted σ(fNL) numbers and reprint their values (they should remain 8.14 and [3.92, 8.98] if the same F0 was actually used in code). Add one line showing the numeric mapping for α = 0.19: F0 + c α^2 = 0.012389 + 0.0747×0.0361 = 0.015086 ⇒ σ = 1/√(0.015086) = 8.14.

P3-E2 (Abstract, p. 1; Section IV.B, p. 13–14; Table V Planck row caption, p. 23; multiple)
Problem: Internal version-history and “earlier draft” language appears throughout the main text and captions, e.g., “an earlier draft quoted 264,938/264,738...”, “An earlier draft quoted 38,330 pixels... withdrawn...”, “an earlier draft listed 10.6 s... withdrawn.” PRD does not accept internal revision log prose in the scientific record.
Required fix: Remove all version-history references, “earlier draft”, “historically included”, “withdrawn”, “superseded” phrasings from the body, tables, and figure captions. Present only the final analysis, with prior variants (if needed) moved to a brief appendix paragraph without numerical prominence and with a single, neutral statement of why the earlier result was incorrect.

P3-E3 (Data availability, p. 21)
Problem: Placeholders remain: “will be made public with the arXiv posting,” “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
Required fix: Provide finalized, persistent DOIs (Zenodo) and public links. Freeze and cite exact commit hashes/tags for code and data. Replace every placeholder with the actual identifiers. If the release cannot be public at acceptance, PRD requires an explicit availability plan; otherwise this is non-compliant.

P3-E4 (Section III.E, pp. 10–11; Table I footnotes; Table III)
Problem: eROSITA score axis irreproducibility. You explicitly state that the published SBigAE scores/threshold 0.259 “could not be reconciled with the committed raw-score artifact on any of 16 monotone rescalings,” and that “Do not use SBigAE as a continuous science data product.” Yet Table III prominently lists SBigAE values, and Table I text still discusses the 0.259 “threshold.”
Required fix: Remove the SBigAE column from Table III and any table or figure that could be misread as a science axis. In Table I change the eROSITA threshold/rate entry to clearly read “membership list of top-298 by committed raw-score artifact; no reproducible score axis; not a measured rate.” Add a one-sentence summary explaining how downstream users should operate (membership-only). Ensure the main text never quotes numerical thresholds on an irreproducible axis.

P3-E5 (Abstract p. 1; §II.D step 5 p. 5; Fig. 10 caption p. 21; Conclusions p. 20)
Problem: Injection–recovery gate counting. You repeatedly summarize as “3 PASS (SDSS 64%, Planck 100%, NEOWISE mask-geometry 100%) and 3 FAIL,” but NEOWISE is a geometry QA (passes by construction) and not a detector sensitivity test. Although you mention this nuance in some places, the shorthand “3 PASS” appears in the abstract and conclusions and is misleading in a headline position.
Required fix: Everywhere a tally appears, state unambiguously “2 PASS (detector sensitivity: SDSS continuum‑dip 64%; Planck 100%) + 1 mask-geometry QA that trivially passes by construction (NEOWISE)” or similar. Do not present “3 PASS” without this decomposition anywhere (abstract, conclusions, figures, or tables).

P3-E6 (Section II.B.a, p. 3)
Problem: For eROSITA, NEOWISE, and Gaia, feature scalers are fit on the full sample (not train split), leaking validation information and potentially reordering extreme tails. You state a robustness test is “queued.”
Required fix: Run the stated robustness check now. Report Jaccard overlap and Spearman rank correlations for top‑k tails (e.g., top‑1%, top‑298 for eROSITA, top‑1% for NEOWISE and Gaia) between train‑split‑only and full‑sample scalers. If any significant reordering occurs, quantify its impact on the released selections.

P3-E7 (Table I, pp. 8–9; Fig. 2, p. 6; Section III overall)
Problem: The main summary table mashes together cross‑transfer baselines and Path‑C native results, with extensive footnoting to explain the replacements. This is confusing and invites mis-citation of the wrong numbers.
Required fix: Split presentation: (i) a clean main table with only the Path‑C native‑retrained, final per‑survey numbers and thresholds; (ii) move cross‑transfer baseline counts to an appendix table for “before/after diagnostic,” clearly labeled non‑science results. Adjust Fig. 2 caption to refer only to the appendix baseline.

P3-E8 (Abstract p. 1; Section III.A p. 5–7)
Problem: The DESI science‑class–restricted recount is critical to calibrate the “73×” headline. It is described textually; a reader cannot see the full denominator and cuts at a glance.
Required fix: Add a small table summarizing the DESI recount: total DESI anomalies (195,829 detections; 190,015 clusters), total primary-class target rows under your bitmask (20,299,155), 1″/2″/5″ match counts (2,468/2,531/3,390), the restricted rate (0.012%), and the like‑for‑like comparison to Liang et al. This removes any ambiguity and ensures the abstract’s qualification is traceable in one place.

P3-E9 (Table V Planck row caption, p. 23)
Problem: Version-log language and missing training-time: “the total training wall‑clock ... was not preserved... an earlier draft listed 10.6 s, which is inconsistent... and has been withdrawn.”
Required fix: Delete all version-log prose. Either (a) re‑run and report an actual training‑time, or (b) omit the training‑time cell for Planck with a neutral “not recorded” and no narrative.

MAJOR

P3-M1 (Section III.E pp. 10–11; Table I footnotes)
Problem: You rely heavily on internal file names (“.../r24conf_erosita_axis_sweep.json”) in the scientific narrative. While reproducibility pointers are welcome, the main text should not depend on internal audit file names for load‑bearing claims.
Required fix: Move these file-name pointers to a Reproducibility appendix or to the Data‑release README. In the body, summarize the result in prose and point to a DOI/commit and a high‑level “Reproducibility notes” section.

P3-M2 (Section IV.B, p. 13–14)
Problem: You report χ^2 = 376,713 for dof = 24,048 (χ^2_ν = 15.7) for spatial non‑uniformity under a simple model, but no effect size beyond χ^2_ν is given, and the test is dominated by obviously inhomogeneous survey footprints.
Required fix: Either remove the χ^2 test entirely (recommended), or add a single effect‑size statement relevant to the hypothesis actually being probed (e.g., fraction of variance explained by footprint mask vs residuals) and emphasize prominently that this test is not interpretable as astrophysical clustering. As is, it invites misuse.

P3-M3 (Section II.D, p. 5; throughout)
Problem: Gate criteria are heuristic (e.g., 50% at 5σ; Jaccard ≥ 0.70; val loss ≤ 0.30). You disclose this but do not provide a sensitivity analysis except to note most gates are well away from thresholds (with the SDSS 64% vs 50% as a borderline).
Required fix: Provide a minimal robustness sweep: show that moving the sensitivity gate to 60% leaves SDSS as PASS and others as FAIL; or otherwise characterize the stability of the PASS/FAIL labels to modest threshold shifts.

P3-M4 (Section V, pp. 16–18; Appendix C p. 22)
Problem: Two different σ(fNL) normalizations co-exist (the main redshift‑binned Fisher with σstd = 8.98 and the simplified shot‑noise Fisher where the single‑tracer baseline is 16.85). You flag non‑comparability in Appendix C but the adjacency in the main text can still confuse.
Required fix: Add an explicit “not directly comparable” warning the first time both numbers are mentioned together in the main text. Ensure every figure or table that displays both clearly labels the normalization context.

P3-M5 (Section III.C, p. 9–10; Fig. 4 p. 10)
Problem: The SDSS cross‑transfer set (77,905) is extensively analyzed (UMAP/HDBSCAN, emission‑line taxonomy) though you also show it is a cross‑transfer domain‑shift artifact relative to the native retrain (12 at S>5; 19,253 at top‑1%).
Required fix: Make clear at the start of §III.C that all taxonomy/cluster results refer to the cross‑transfer set and are presented only as diagnostics of the failure mode; not as properties of the final SDSS tier. Consider moving the taxonomy table to an appendix to avoid confusion.

P3-M6 (Terminology, multiple pages)
Problem: “Gold-tier” is used in two distinct meanings (an 83‑object visualization set in Fig. 1 vs the 116‑object GOLD QSO‑candidate tier used in §V).
Required fix: Rename one of these to avoid collision (e.g., “Gold‑viz (83)” versus “GOLD‑QSO (116)”) and ensure the figure caption and §V text use the disambiguated names consistently.

P3-M7 (Section IV.C, p. 14–15)
Problem: The 7‑way dedup uses a 5″ hard radius; you provide a small sensitivity sweep (3″, 5″, 7″). Good. The RA‑only shift control for pairwise DESI×SDSS expected chance matches is not geometry‑preserving near survey edges.
Required fix: Either (a) add a great‑circle random-rotation control to support the “no significance” statement; or (b) remove the RA‑shift number from the text and retain only the conservative qualitative conclusion that the observed three matches are spectroscopically confirmed and not consistent with random at face value.

P3-M8 (Length and focus)
Problem: The manuscript reads partly as a lab notebook with long footnotes and internal audit artifacts in the main body. At 28 pages for the main text, the presentation is unfocused for PRD standards of a methods paper.
Required fix: Reduce to ≤20 pages by moving cross‑transfer baselines, long audit footnotes, and many repository‑file references to appendices or the data‑release notes. Keep the main text focused on final Path‑C methodology and results.

MINOR

P3-m1 (Abstract, p. 1)
Problem: The abstract contains several numbers that will be mis‑cited if not tightened, e.g., the catalog‑grade tier count (269,317 including 200 Planck patches; 269,117 point‑source after dropping patches).
Required fix: State the catalog‑grade number in the abstract only for the point‑source subset that most readers will use (269,117) and move the with/without‑patch distinction to the body.

P3-m2 (Section II.B, p. 4)
Problem: DESI MSE threshold presentation: you give μval ≈ 0.0287 and state S>5 corresponds to MSE ≈ 0.143, but σval is not shown.
Required fix: Add σval used for DESI (≈0.0229 implied by your threshold) to make the mapping checkable.

P3-m3 (Section IV.A, p. 12; Fig. 6 p. 13)
Problem: SIMBAD-unmatched aggregate fraction (58.8%) is given at 3″, while per‑survey unmatched fractions elsewhere use 5″ unless stated; the caption notes this but the mixed radius can still mislead.
Required fix: Standardize radii in figure labels or print both radii explicitly in the figure legend (“aggregate at 3″; per-survey at 5″”).

P3-m4 (References, p. 27)
Problem: Ref. [12] is listed as “Mon. Not. Roy. Astron. Soc. 547, Issue 2 (2026), arXiv:2506.17376.” Please verify journal/volume/issue/year pair is accurate (if in press, mark “in press” with arXiv only).

P3-m5 (Typos/formatting)
- Occasional double spaces and em-dash spacing; standardize.
- Use consistent symbol formatting for arcseconds (″) and degrees (°) in tables and captions.

NIT

P3-n1 (Equation labels, p. 3)
Problem: Clarify that “z-scored” refers to statistical z and is distinct from redshift z, once, at first mention (you already do later).

P3-n2 (Units in Appendix E, p. 25)
Problem: Define fyr explicitly at first use in Eq. (E1) (“reference frequency per PTA convention, e.g., 1/yr”) to avoid ambiguity.

Arithmetic audits of abstract/conclusion scalars (spot-checked)

- Total unique 378,280 = 388,493 (per-survey native sum) − 10,213 (collapsed): OK.
- Point‑source tier 378,080 = 378,280 − 200 Planck patches: OK.
- DESI anomaly rate 195,829/22,504,897 = 0.870%: OK.
- SDSS cross-transfer rate 77,905/2,304,830 = 3.38%: OK.
- LAMOST cross-transfer rate 44,075/11,418,594 = 0.386%: OK.
- eROSITA 298/930,203 ≈ 0.032%: OK (predetermined count).
- NEOWISE mask retention 419/436 = 96.1%: OK.
- DESI science‑class restricted rate 2,468/20,299,155 = 0.0122%: OK.
- “73×” DESI vs Liang 2,685: 195,829/2,685 = 72.9: OK, and caveat present. Like‑for‑like 2,468/2,685 ≈ 0.92×: you quote ≈0.9×; OK.
- “~141×” point‑source tier vs 2,685: 378,080/2,685 = 140.8: OK.
- “~100×” catalog‑grade 269,117 vs 2,685: 100.2×: OK.
- Novelty 178/1,000 = 17.8% (Wilson 68% ± ~1.2%): OK.
- NANOGrav γ shift: (3.0 − 2.567)/0.382 = +1.13σ; (4.33 − 2.567)/0.382 = +4.61σ: OK.
- Bayes factor BMB/SMBHB = 3.23 / (4.52×10^−4) = 7.14×10^3: OK.
- NEOWISE polar‑cap area fraction for 10° caps: 1 − cos 10° = 1.52%: OK; observed 17/436 = 3.90% ≈ 2.6×: OK.
- Dedup sensitivity sweep unique‑count variation ≤0.086%: matches reported numbers: OK.

Stand‑alone reader test
The main narrative is self‑contained, but several essential results (eROSITA axis behavior, SDSS recount) are entangled with internal file‑name references and version history. Please implement the presentation fixes above to make the paper stand alone without consulting repository internals.

Effect sizes and null procedures
You consistently flag when numbers are not directly comparable (e.g., σ normalizations, SIMBAD vs archival novelty), and most statistical claims carry effect sizes. After correcting P3‑E1 and clarifying P3‑M4, this will be acceptable.

## Summary recommendation
MAJOR REVISIONS

The core methodology and most computations check out, and the paper’s main numbers are arithmetically consistent. However, the dimensional error in the Fisher summary (text), the inclusion of an irreproducible eROSITA score axis in a main table, placeholders for data availability, and pervasive version‑history/log language in the scientific narrative do not meet PRD standards. Addressing the essential and major items above — especially removing internal‑log prose, finalizing data DOIs, correcting the Fisher formula text, restructuring the main table, executing the queued robustness check, and clarifying the injection‑recovery tally — is required before the manuscript can be considered further.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh‑eyes pass)

I focused on the ten classes (A–J) you requested. Items below are new; I do not repeat anything from my first report.

ESSENTIAL

P3-E10 (A, H — binomial uncertainty on recovery fractions missing; N not stated at point of use)
Across the paper you quote single percentages for injection–recovery (e.g., SDSS 64%, LAMOST 5.8%, eROSITA 1.2%, Gaia 5.2%; Fig. 10 and multiple text locations) without the binomial N and uncertainty at the evaluation point. Section II.D.5 says “500 planted signals per survey at six amplitudes,” but the 5σ evaluation N (per survey and per morphology) is never reported where the percentages are used.
Required fix: For every quoted recovery percentage at 5σ, report the actual numerator/denominator and a binomial uncertainty (e.g., Wilson 68% CI). Example: “SDSS continuum‑dip 64% (320/500; 68% CI [59.7, 68.1]%)”, “LAMOST continuum‑dip 5.8% (29/500; [4.0, 8.2]%), emission‑line 0.6% (3/500; [0.2, 1.8]%),” “eROSITA 1.2% (≈60/5000 if that is the effective N; otherwise give exact N),” etc. Do the same for the Planck 500/500 and the NEOWISE mask 1000/1000 figures so readers can judge statistical precision.

P3-E11 (B — caption/body mismatch: saturation/clipping not disclosed)
Figure 7 (map colored by anomaly score S) uses a color scale apparently capped near S ≈ 14, while the body text in §III.A states DESI scores extend to S = 25.2 and that 101 objects exceed S = 15. The caption/body do not disclose that the color scale saturates below the maximum.
Required fix: State explicitly in the Fig. 7 caption if the colormap is clipped/saturated (e.g., “colorbar saturates at S = 14 for readability”), or rescale to display the full dynamic range. Ensure any dashed reference line in the bottom-right panel (appears near S ≈ 10) is explained in the caption.

P3-E12 (C, H — Planck train/validation split over‑representation called “mild” but is a >3σ effect)
§III.F: You report that, under the deterministic 85/15 split, 152/200 top patches fall in the training split and 48/200 in validation, adding “the anomaly tail mildly over‑represents held‑out patches.” Under a Binomial(n = 200, p = 0.15) null, 48 validation patches is a 3.6σ excess (μ = 30, σ ≈ 5.05).
Required fix: Quantify this with a binomial p‑value or z‑score and rephrase “mildly” (e.g., “a 3.6σ excess of validation patches”). This strengthens your anti‑memorization argument and avoids understating the effect.

MAJOR

P3-M9 (G — unsupported “largest multi‑archive” claim)
The abstract/introduction repeatedly claim this is the “largest‑scale application across multiple archives” yet the only size benchmark cited is the largest single‑survey catalog [11]. No multi‑archive effort is compared.
Required fix: Either (i) add an explicit literature comparison showing the size of prior multi‑archive anomaly catalogs (or state none exist to your knowledge after a documented search), or (ii) soften to “to our knowledge, among the largest…,” and move the single‑survey comparison to a separate sentence.

P3-M10 (E — σ comparability: Planck CMB patch score axis vs canonical S juxtaposed without a local reminder)
In several places you list “per‑object canonical‑S scores … and Planck per‑patch raw MSE” together (e.g., Data availability paragraph; §III.F first paragraph) without a local “not comparable” qualifier. Earlier you do explain that Planck is on a different axis, but the mixed listing without a reminder invites casual mis‑comparison.
Required fix: When Planck raw‑MSE scores appear in any list or table alongside canonical S, add an inline parenthetical “(Planck on raw per‑patch MSE; not comparable to canonical S).”

P3-M11 (B, D — Figure 10 labeling vs. text)
Fig. 10 overlays curves for “SDSS DR18 (continuum‑dip)”, “SDSS DR18 (emission‑line)”, “LAMOST DR10 (continuum‑dip)”, “LAMOST DR10 (emission‑line)”, “eROSITA (latent IF)”, “Gaia (variab. IF)”, but the legend and caption do not specify the absolute N underlying each curve at each amplitude step. The body text later cites single percentages at 5σ.
Required fix: Add to the caption (or a supplemental note referenced in the caption) the evaluation N at each amplitude per curve, or at minimum at 5σ per survey/morphology. This avoids the impression that all curves share identical N.

P3-M12 (H — “statistically consistent” SIMBAD statement needs the uncertainty stated)
§III.A: For the DESI top‑10,000, you state the 0.2% SIMBAD match rate is “statistically consistent” with the 0.24% random‑match expectation. The back‑of‑envelope is correct (20 observed vs 24 expected), but the text does not show the uncertainty that justifies “consistent.”
Required fix: Quote a simple Poisson/binomial uncertainty on the expected or observed count (e.g., “observed 20 vs 24±4.9 expected; consistent within 1σ”). This pattern should be followed wherever “consistent with” is used.

P3-M13 (I — NEOWISE mask test methodology summarized differently in main text vs Fig. 10)
§III.H emphasizes (correctly) that the NEOWISE mask “passes by construction,” planting at |becl| > {85°, 82°, 80.5°} and using a fixed mask of |becl| < 80°. In Fig. 10, the language “injection amplitude (× noise σ)” is generic and could mislead readers into thinking NEOWISE used the same amplitude injections as the other curves.
Required fix: In Fig. 10 caption, add an explicit sentence immediately after the legend explaining that the NEOWISE “100%” curve is from a geometry‑only injection and not comparable to detector‑sensitivity curves.

P3-M14 (F — Abstract fidelity: “catalog‑grade subset” usage)
The abstract’s long parenthetical around the catalog‑grade subset still mixes the with‑patch and without‑patch variants in one breath. Most readers will use the point‑source subset.
Required fix: Make the abstract state a single catalog‑grade number for point sources only (269,117) and move the with‑patch figure and the 6‑way/7‑way bookkeeping to the body, to prevent mis‑citation. (This is stricter than P3‑m1 and addresses abstract readability/faithfulness.)

MINOR

P3-m6 (C — per‑band residual definitions mix L1 and L2 without a reminder)
§II.B.b defines S on per‑element MSE (L2) while the per‑arm diagnostics rB,rR,rZ are mean absolute residuals (L1). You note they’re “used only for within‑object arm‑dominance,” but the metric change is easy to miss.
Fix: Add a short parenthetical at first use: “rX uses mean absolute residuals (L1) whereas S uses MSE (L2); rX are diagnostics only, not selection scores.”

P3-m7 (A — rounding consistency in Table VI vs text)
Table VI “R‑dominant 0.02%, Z‑dominant 0.01%, Artifact 0.05%” sums with the other rows to 99.98%, which is fine under rounding; however, in §III.A the text rounds these to “34 R‑dominant (0.02%), 19 Z‑dominant (0.01%), 96 artifact (0.05%)” and elsewhere you state “96 artifact suspects (0.05%).” Consider adding an “rows sum to 100% within rounding” note to avoid reader confusion.

P3-m8 (D — reference cross‑check)
The introduction cites “bispectrum‑only forecast ≈ 0.7” for SPHEREx [15]. That number is not shown later where fNL forecasts are treated. Add a parenthetical citation with a precise pointer to the location in [33] (or [15] if appropriate) where 0.7 appears, or restate it with context to avoid an orphaned claim.

P3-m9 (B — Figure 3 right‑panel annotation vs body)
Fig. 3 annotates the extreme SDSS objects with “S = 1.9×10^11” etc., which are on the DESI‑trained cross‑transfer axis (per caption). To avoid readers confusing this with the native SDSS axis later in §III.C, add to the caption a one‑line reminder: “These extreme values vanish under the SDSS native retrain (all S < 14).”

P3-m10 (E — mixed radii in SIMBAD Fig. 6)
You note in text that the pooled 58.8% aggregate was computed at 3″ while per‑survey rates are 5″, but the figure legend does not carry both radii.
Fix: Amend Fig. 6 legend to “Aggregate (3″); per‑survey (5″)” so the radius difference is unambiguous at the point of viewing.

P3-m11 (J — stale phrasing around “top‑200 validation overlap expected 170/30”)
§III.F uses “≈170/30 expected” against the 85/15 split. Since the observed is 152/48 and you now quantify it (see P3‑E12), change “≈170/30 expected” to “expected 170/30 under the split” and give the exact binomial uncertainty for the expected validation count (σ ≈ 5.05) to keep the statement numerically tidy.

NITS

P3-n3 (C, E — define units in Eq. E1 and symbols on first use)
Appendix E Eq. (E1) uses fyr and Tobs without unit declaration in the main text. Add “fyr = 1/yr; Tobs = 16.03 yr” on first mention in the appendix (you currently give Tobs later, not at the equation), and remind that fi are in cycles/yr.

P3-n4 (D — internal cross‑references)
A few “§VI D (ii)” cross‑references are used as load‑bearing pointers for the eROSITA/Gaia XV‑stability claims. Add a parenthetical summary right where first cited (e.g., “(XV‑stability 81.5%; details §VI D(ii))”) so readers don’t have to resolve the reference to understand the claim.

Brief rationale
The new items above focus on quantitative faithfulness (uncertainty/denominator disclosure for recovery fractions; significance of the Planck split test), clarity at the figure/caption interface (score saturation, radius labeling, cross‑transfer axis reminders), and a few remaining presentation issues (unsupported “largest multi‑archive” superlative; metric clarity; abstract focus). These are orthogonal to the issues in my initial review and, once corrected alongside the previously listed Essential/Major items, should considerably tighten the paper to PRD standards.