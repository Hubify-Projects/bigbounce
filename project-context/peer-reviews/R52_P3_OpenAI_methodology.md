# P3 R52 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.112.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8687 chars)
**Wall time**: 507.5s

---

Referee report (PRD methodology: statistical rigor, internal consistency, reproducibility)

I have read the full 30‑page manuscript, including all figures, tables, equations, captions, appendices, and footnotes embedded in the main text. Below are detailed findings, classified by severity, with page references to the rendered PDF (page numbers in the supplied 30‑page file), direct quotes where relevant, and concrete required fixes.

ESSENTIAL

P3-E1 — Abstract (p.1) + Table I footnotes (pp.9–10) + §II D (p.5) + throughout: “catalog-grade” tier includes components that fail validation or are not reproducible
- Problem: The abstract defines and recommends a “catalog-grade” subset (269,317 total; 269,117 point-source after dropping Planck patches), obtained from a 6-way deduplication that explicitly includes eROSITA and Gaia. Yet in the same abstract and in §II D and Table I footnotes, eROSITA (1.2% injection recovery; score axis irreproducible) and Gaia (5.2% injection recovery; 41% cross‑validation stability) are defined as “exploratory” and “fail the 5σ injection‑recovery gate.” NEOWISE’s “PASS” is a geometry QA (mask application) that is not a detector-sensitivity test. Calling the combined 6‑way set “catalog-grade” is internally inconsistent with the stated validation semantics.
- Required fix: Either (a) redefine “catalog-grade” to include only surveys that clear detector-sensitivity validation (SDSS, Planck; and DESI by the stated Jaccard gates) and exclude eROSITA, Gaia, and the NEOWISE mask‑only QA from that label; or (b) keep the 6‑way dedup but rename it everywhere to “mixed-validation tier” (or similar), and explicitly state in the abstract and conclusions that it contains two FAIL components (eROSITA, Gaia) and one geometry‑PASS (NEOWISE), i.e., not catalog‑grade in a validation sense. Update counts accordingly. This change must propagate consistently to the abstract, Table I caption/footnotes, §II D, §VI 7, and the conclusions.

P3-E2 — §III E (pp.11–12) + Table I footnote § (pp.9–10) + Table IV (p.12): eROSITA selection axis irreproducible but used/labelled inconsistently
- Problem: The manuscript correctly states that the eROSITA “SBigAE” axis is irreproducible and the only committed selection is the n = 298 membership list (fixed top‑298 cap). However, Table I footnote § and nearby prose still use formulations like “canonical‑S top‑298 sources” and mix “production SBigAE” with “committed raw” and “IsolationForest” axes. This muddles what is and is not reproducible. Moreover, this membership‑only tier is included in the “catalog‑grade” number (see P3‑E1).
- Required fix: Purge all instances of “canonical‑S” in reference to eROSITA. Replace with “membership‑list top‑298” everywhere. Do not imply there is any reproducible score axis for eROSITA. If the 298 are included in any headline count, the abstracts/conclusions must plainly say “membership‑only, no reproducible per‑object score.” If you intend to treat eROSITA as catalog‑grade, you must re‑run and publish a reproducible selection axis or reclassify it as non‑catalog‑grade and remove it from that count (see P3‑E1).

P3-E3 — §III A (pp.6–7): Incorrect 95% CI quoted for DESI per‑class anomaly rate (GALAXY)
- Quote: “Wilson 95% binomial CIs: GALAXY 0.75% ± 0.02% on ∼ 4.9 × 10^6 … QSO 0.037% ± 0.003% on ∼ 1.5 × 10^6…”
- Problem: For p = 0.0075 on n ≈ 4.9×10^6, the 95% half‑width is ≈ 1.96√(p(1−p)/n) ≈ 7.6×10^−5 in fraction units, i.e., ±0.0076% in percent units, not ±0.02%. The QSO uncertainty is consistent; the GALAXY one is overstated by ≈2.6×.
- Required fix: Recompute and correct the GALAXY confidence interval. State the exact denominator and anomaly count used, name the interval type (Wilson/Clopper‑Pearson/normal), and propagate the corrected figure to any text that relies on it.

P3-E4 — §IV B (p.15): Cramér’s V numeric substitution inconsistent with the stated formula
- Quote: “Cramér’s V = √(χ^2/(N·(k−1))) = 376,713/(378,280 × 24,047) ≈ 0.0064”
- Problem: The middle term replaces √(χ^2 / (N(k−1))) with χ^2/(N(k−1)), but the final number 0.0064 corresponds to taking the square root. This is an explicit numeric/formula inconsistency in the text.
- Required fix: Correct the displayed middle step to show the square root applied to χ^2/(N(k−1)), i.e., 0.0064 = √(376,713/(378,280×24,047)). Ensure the equation is dimensionally and numerically consistent.

P3-E5 — Data availability (p.23): Placeholders and deferred DOIs/links
- Quote: “will be made public with the arXiv posting … A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Problem: PRD requires reproducibility at acceptance. Placeholder language cannot remain. The present text mixes internal repository paths in the main body with future‑tense promises.
- Required fix: Before acceptance, provide final, immutable DOIs for all released datasets and code, a tagged release commit hash, and a frozen manifest with checksums that match the figures/tables in this submission. Move long internal path strings from the main text into the Data Availability section or Supplementary Material.

P3-E6 — Abstract (p.1) + §II D Step 5 (pp.5–6) + §III H (p.13) + Fig. 10 caption (p.22): Counting NEOWISE “PASS” alongside detector‑sensitivity gates is misleading
- Problem: The injection‑recovery section headlines “3 PASS (SDSS 64%, Planck 100%, NEOWISE mask‑geometry 100%)”. The manuscript does note NEOWISE’s is a geometry QA that “passes by construction,” but the PASS headline appears repeatedly and risks conflating a masking‑geometry check with detector sensitivity.
- Required fix: Do not count the NEOWISE mask‑geometry QC as an injection‑recovery PASS in the main PASS/FAIL tally. Explicitly separate “detector‑sensitivity gates” (SDSS, Planck) from “geometry QA” (NEOWISE) wherever the PASS/FAIL tally is summarized (abstract, §II D, conclusions, Fig. 10 caption).

P3-E7 — “Largest to date” claim (abstract p.1, conclusions p.22): Needs substantiation or tempering
- Quote: “the largest-scale application of autoencoder anomaly detection across multiple astronomical archives of which we are aware… The point-source tier is ∼141× the size of the largest prior single‑survey anomaly catalog [11]…”
- Problem: The statement conflates multi‑archive and single‑survey baselines and asserts a superlative “largest‑scale” without a comprehensive literature justification. If you rely on [11] as the sole benchmark, make that scope explicit; otherwise, provide a short survey and clear search criteria supporting the superlative.
- Required fix: Either (a) qualify the claim to “to our knowledge, relative to [11]’s single‑survey benchmark” (and remove the absolute “largest‑scale” language), or (b) add a brief literature audit establishing the scope of “largest,” including any comparable multi‑archive anomaly catalogs, and demonstrate that the 378,080 point‑source tier exceeds them.

MAJOR

P3-M1 — §V (pp.18–19) and Table V(i) (p.21): Coefficient c = 0.0747 in the Fisher “positivity‑respecting” form is undeclared and irreproducible from the text
- Problem: The key mapping 1/σ^2(fNL) = F0 + c α^2 is used to headline σ(fNL) = 8.14 (central) and its envelope, but c = 0.0747 is only described as a “5‑α refit” with no tabulated fit inputs/outputs, figure, or artifact that a reader can check. Given that this scalar drives the cosmology‑relevant forecast, it must be auditable.
- Required fix: Provide the derivation of c with enough detail to reproduce it: the five α values used, their corresponding σ(fNL) values, the fit method, the goodness‑of‑fit, and a repository artifact (data table + script) keyed by a frozen commit. Alternatively, move the forecast to Supplementary Material and remove it from the abstract/conclusions if you cannot document c.

P3-M2 — §III C (pp.8–10), Table I footnotes (pp.9–10), §II B (pp.3–5): Threshold heterogeneity and post‑hoc slicing need a unifying, predeclared rationale
- Problem: Four thresholding families are used: DESI fixed S>5; SDSS “continuity slice” at S ≥ 0.1060 sized to match a cross‑transfer count; SDSS top‑1% at a different knee S ≥ 0.2051; LAMOST top‑1% S ≥ 0.4613; eROSITA fixed top‑298 (membership‑only); Gaia/NEOWISE fixed top‑1%; Planck fixed top‑200 patches. While heterogeneity can be justified, calling one of the SDSS slices a “continuity slice sized to equal the cross‑transfer count” reads as post‑hoc and risks p‑hacking optics, especially for a headline catalog.
- Required fix: Provide a concise, survey‑agnostic thresholding policy and explicitly map each survey’s choice to that policy, or move the continuity‑slice outputs out of any headline claims and keep only thresholds with a clear, predeclared rationale (e.g., fixed percentile; fixed S; fixed count not used as a rate). Clarify which thresholds feed the dedup headline, which feed the “catalog‑grade” (after P3‑E1), and which are purely diagnostic.

P3-M3 — §IV C (p.15–16): Cross‑match control using RA‑only shifts is not geometry‑preserving; the inference drawn needs revising
- Quote: “RA‑shifted‑control expectation of 2.75 (mean of ±0.5°, ±1.0° shifts) … we caution that RA‑only shifts … are a heuristic control…”
- Problem: You nonetheless compare the observed 4 matches to 2.75 in the main body. For clustered/non‑uniform footprints, RA‑only shifts bias the null. A geometry‑preserving null (random rotations or great‑circle jitter outside footprints) is needed or the inference should be relegated to Supplementary with no numerical comparison.
- Required fix: Either (a) implement a geometry‑preserving null (e.g., random sky rotations constrained to the common footprint) and recompute the expectation with uncertainty bands, or (b) drop the numeric comparison from the main text and confine RA‑shift counts to a methods note without an inference.

P3-M4 — §IV A (p.14) and Table I footnote ∥ (pp.9–10): “≲10 random coincidences” claim for 7‑way 5″ dedup lacks derivation
- Problem: The statement “expected random coincidence contribution is ≲10 across all survey pairs” is a quantitative assertion with no computation shown.
- Required fix: Provide a back‑of‑the‑envelope calculation (areal densities per survey, effective overlapping areas, matching radius) with assumptions clearly stated, or remove the claim.

P3-M5 — §III H (p.13): NEOWISE polar‑cap excess quantified only as a ratio without a significance estimate
- Quote: “3.9% polar‑cap fraction represents a 2.6× excess over the uniform‑null expectation (1.52%)…”
- Problem: The significance (e.g., binomial z‑score or p‑value) is not given. Using n = 436, p0 = 0.0152, k = 17 yields z ≈ 4.0 (two‑sided p ≈ 6×10^−5). This is straightforward to include.
- Required fix: Add the corresponding significance (z/p) with the null and n explicitly stated.

P3-M6 — §III A (pp.6–8): “B‑dominant anomalies … calibration‑suspect” is asserted without a quantitative diagnostic
- Problem: The paper labels the ~44k DESI B‑dominant anomalies as “calibration‑suspect,” but no quantitative test or external cross‑check is provided (e.g., correlation with airmass, sky lines, photometric colors).
- Required fix: Either add a brief quantitative diagnostic (even a simple correlation with known blue‑arm systematics or a color‑based sanity check), or rephrase to clearly mark this as a hypothesis needing follow‑up.

P3-M7 — Scope and length (entire paper; 30 pages): Over‑breadth for a PRD methodology article
- Problem: The manuscript combines a 7‑archive anomaly catalog, validation methodology, cross‑survey analyses, DESI high‑z candidates, Fisher forecasts for fNL (two different normalizations), and a NANOGrav MCMC spectral‑index analysis with Bayes factors. This breadth dilutes the methodological narrative and forces many key derivations (e.g., c in §V) into terse statements without on‑page reproducibility.
- Required fix: Reduce the main text to ≤ 25 pages focused on the core methodological contributions (catalog construction, validation gates, dedup geometry, and cross‑survey consistency) and move the cosmological application material (Fisher forecast, NANOGrav MCMC) and long pipeline‑path details to Supplementary Material with permanent DOIs. Ensure all headline cosmology numbers still have on‑page derivations if kept in the main text.

MINOR

P3-n1 — §IV C (p.15): “maximum unique‑count variation of 0.086%” phrasing is ambiguous
- Problem: The text appears to report the maximum deviation from the 5″ central value (|378,604 − 378,280| / 378,280 ≈ 0.0856%; |378,145 − 378,280| / 378,280 ≈ 0.0357%), not the full range relative to the center (which would be ≈ 0.121%). The phrase “maximum unique‑count variation” could be misread.
- Required fix: Specify explicitly “maximum absolute deviation from the 5″ count is 0.086%,” or report both one‑sided deviations.

P3-n2 — §II B (pp.3–5): “score‑knee” is used repeatedly but never defined algorithmically
- Required fix: Define “score‑knee” (e.g., derivative‑based elbow on the empirical CDF, or a fixed percentile) and cite/apply a consistent algorithm.

P3-n3 — §III A (p.6): 0/200 visual‑flagged anomalies — interval method not specified
- Required fix: Note the interval method for the “95% upper limit ≤ 1.5%” (e.g., Clopper‑Pearson), or simply state the value without the inequality.

P3-n4 — §II C Table VI † footnote (p.24): Missing Planck training wall‑clock time
- Problem: The text says “was not preserved in the run logs.”
- Required fix: Either remove the claim that all training times are tabulated, or add the missing number if available.

P3-n5 — §IV A (p.13–14): SIMBAD unmatched aggregate (235/400 = 58.8% at 3″) — clarify radius mismatch versus per‑survey 5″ default
- Required fix: Add one sentence explaining the reason for the 3″ pooled run and the qualitative impact of using 5″ (aggregate would be weakly lower).

P3-n6 — Figures: Units and symbols
- Check and fix: Fig. 3 right axis “Anomaly score S” spanning up to 10^11 is fine but add a note in the caption that this is the DESI‑trained cross‑transfer axis for SDSS to avoid confusion; currently present in text — echo in the caption for standalone clarity.

P3-n7 — §V A (pp.18–19) and Appendix E (pp.25–26): MCMC posterior summaries use both “±σ” and asymmetric quantiles; ensure consistent labeling
- Required fix: In the main text, explicitly state which uncertainty is used for sigma‑shift computations (you do: ±0.382), and identify the quantile summary as 68% HPD or equal‑tailed.

P3-n8 — Bibliography formatting
- Minor inconsistencies (e.g., Ref. [12] “Mon. Not. Roy. Astron. Soc. 547, Issue 2 (2026)”): verify final bibliographic data (volume, page) match journal style.

NIT

P3-N1 — §IV B (p.15): Typographical glitch in square‑root symbol “p χ2 p”
- Required fix: Correct typesetting to √χ^2.

P3-N2 — Internal path strings scattered in main text (multiple pages)
- Required fix: Move long path strings to SI/Data Availability to improve readability.

P3-N3 — Occasional hyphenation artifacts in parsed text (e.g., “re‑score,” “vali‑ dation”)
- Required fix: Proofread final PDF.

Abstract‑last drift sweep (pattern‑045): After re‑reading the abstract against the body, most claims are correctly caveated in the body. The two exceptions are P3‑E1 (catalog‑grade label inconsistency) and P3‑E6 (PASS tally). These must be fixed in the abstract as well as in‑body.

Provenance surfaces (patterns‑046/047): The Data Availability section contains future‑tense placeholders; fix per P3‑E5.

Uncomputed quantitative claims (pattern‑048): Addressed by P3‑M4, P3‑M5, P3‑M3.

Standalone‑reader test: The paper is self‑contained, except for the missing definition of “score‑knee” (P3‑n2) and the undeclared derivation of c (P3‑M1).

Effect sizes: The paper generally provides effect sizes; the Cramér’s V numeric mismatch is noted (P3‑E4) and should be corrected. The NEOWISE polar‑cap significance needs a p‑value (P3‑M5).

Page count recommendation: Reduce to ≤ 25 pages for focus (P3‑M7), moving the cosmology applications and extended pipeline details to SI with DOIs.

## Summary recommendation
MAJOR REVISIONS

The core methodological contribution (a large multi‑archive anomaly catalog with a transparent validation/rebuild protocol) is promising, and many internal numbers check out. However, the paper cannot be accepted in its current form because (i) the “catalog‑grade” label is applied inconsistently to a set that includes FAIL and non‑reproducible components, (ii) a key cosmology‑facing scalar (c in the Fisher mapping) is not reproducible from the text, (iii) there are quantitative inconsistencies (DESI GALAXY CI; Cramér’s V display), and (iv) several claims require stronger methodological discipline (threshold policy, cross‑match nulls, NEOWISE PASS counting). Address the ESSENTIAL and MAJOR items above, provide final DOIs, and streamline the scope to focus on the methodological advances.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit focusing on A–J). Only new items are listed; none of the issues in the initial review are repeated.

ESSENTIAL

P3-E8 — Table I “SIMBAD-unmatched (%)” denominators are heterogeneous and not stated
- Problem: The per-survey SIMBAD-unmatched percentages in Table I appear to be computed on different bases: e.g., DESI is discussed in-body for the “top 10,000”; eROSITA is a 298-member “membership-only” tier; SDSS percentages elsewhere are given for the full 77,905 cross-transfer set and also for “top-100.” The table does not state the exact denominator, match radius, or whether each percentage is computed on the full tier, a subset (e.g., top-N), or membership-only lists. This makes inter-survey comparisons misleading.
- Required fix: For each survey’s Table I SIMBAD-unmatched entry, state in a footnote the exact denominator (e.g., “all 195,829 DESI anomalies,” or “top-10,000”), the match radius used, and whether the selection is a membership-only tier. If different radii/denominators are used across surveys, say so explicitly in the caption and warn against cross-survey comparison.

P3-E9 — Fig. 3 (left) caption vs thresholds used: miscue from showing only the DESI S=5 line
- Problem: Fig. 3 (left) overlays DESI and LAMOST native score distributions but shows a single vertical line at S=5 (the DESI hard cut). LAMOST’s actual selection in the paper is a top-1% native slice at S ≥ 0.4613, not S=5. Presenting only S=5 on a shared panel where the green curve corresponds to a different, percentile-based cut invites misinterpretation.
- Required fix: Add a second vertical line for the LAMOST native threshold (S ≥ 0.4613) or explicitly annotate in the caption that the displayed S=5 line applies only to DESI and that LAMOST uses a different, percentile-based threshold. Ensure this clarification also appears where Fig. 3 is discussed in the main text.

MAJOR

P3-M8 — Fig. 10 comparability: injection “amplitude (× noise σ)” is not commensurate across surveys
- Problem: Fig. 10 overlays recovery curves for spectroscopic continuum-dip and emission-line plants (SDSS/LAMOST), a CMB Gaussian-bump plant (Planck), and IsolationForest-based injections (eROSITA latent IF; Gaia variability IF), all on a common x-axis labeled “Injection amplitude (× noise σ).” The underlying “σ” and plant morphologies differ materially across detectors and data types, so the curves are not on a common sensitivity scale.
- Required fix: Add a prominent disclaimer (caption and §VI D (ii)) that these recovery fractions are not directly comparable across surveys because the plant definitions and “σ” baselines differ. Ideally, report within-survey detection thresholds in native, survey-specific units or provide a normalization explanation that justifies cross-curve comparison (otherwise, restrict claims to within-survey behavior).

P3-M9 — §IV A (p.14): “Uniform-density analytic expectation ∼ 2.3” random DESI×SDSS coincidences at 3″ lacks derivation
- Problem: The text asserts a uniform-density analytic expectation of ∼2.3 random matches at 3″ but provides no calculation (source densities, overlap area, or footprint mask).
- Required fix: Add the back-of-the-envelope calculation (per-survey surface densities within the common footprint, match radius, and area), including uncertainties; otherwise, move the “∼2.3” figure to a methods note without numerical comparison.

P3-M10 — §V: “1σ envelope” terminology risks misinterpretation as a credible interval
- Problem: The text labels [3.92, 8.98] as a “1σ envelope” for σ(fNL) built from the noisy α estimate via the convex mapping 1/σ2 = F0 + c α2. Although you note it is not a probabilistic 68% interval, the “1σ” phrasing can be read as a confidence interval by non-expert readers.
- Required fix: Rename consistently to “propagated-α envelope (not a credible interval)” in §V, Table V(i), and the conclusions; add a one-sentence reminder in §V that this is the image of α̂ ± σα under a convex mapping, not a posterior interval for σ(fNL).

MAJOR (method/clarity)

P3-M11 — §III F (Planck): binomial p-value for 48/200 validation top-patches does not account for patch correlations
- Problem: The p ≈ 4×10−4 over-representation of validation-split patches assumes independence of the 10°×10° tiles. The text acknowledges “may be mildly correlated,” but still quotes a binomial p-value.
- Required fix: Either (a) estimate an effective number of independent patches (e.g., via spatial jackknife or correlation length) and recompute a corrected significance, or (b) remove the p-value and keep the qualitative statement without formal significance.

MINOR

P3-n9 — §V/Appendix C cross-normalization: annotate all places where σ(fNL)=8.98 (main Fisher) and σ(fNL)=16.85 (shot-noise fig) are juxtaposed
- Problem: You correctly warn once that these normalizations are not comparable. Elsewhere (Appendix C Fig. 11 caption and main §V text) the values reappear near each other and can be conflated.
- Required fix: Add a brief parenthetical “not on the same normalization; only relative changes are comparable” wherever both values are mentioned.

P3-n10 — Table V (j): “prior ±7.43 dropped” is unclear/stale
- Problem: The phrase “prior ±7.43 dropped” in Table V (j) has no prior definition in the paper and reads like a remnant from an earlier draft.
- Required fix: Clarify or remove the “±7.43” text; if it referred to a prior symmetric uncertainty on σ(fNL), state explicitly what it was and why it was dropped.

P3-n11 — §III F (Planck): scoring on train+validation set called “standard practice” without a held-out result
- Problem: While autoencoder anomaly scoring often uses in-sample scoring, releasing a top-200 set drawn from train+val invites memorization concerns.
- Required fix: Provide, if possible, the top-N list restricted to validation patches (or an independent test bank) as a sanity check in SI, or explicitly recommend users treat the released set as exploratory until a held-out replication is provided.

P3-n12 — §IV B/Fig. 7: “no score–latitude trend” quantitative summary missing for the DESI-only panel
- Problem: The combined-catalog result reports Spearman r = 0.0005, p = 0.92. Fig. 7 (DESI) asserts no trend qualitatively but lacks the corresponding DESI-only statistic.
- Required fix: Add the DESI-only Spearman r and p to the caption or main text for completeness.

P3-n13 — §III A visual QA: 0/200 flagged — clarify multiple-testing setup
- Problem: You compare peak residuals against 11 features per spectrum for 200 spectra. The family-wise error context is not stated.
- Required fix: Briefly note that this was a targeted check (not a formal multiple-hypothesis test) and reaffirm that the 0/200 result is a qualitative QA, not a formal contamination bound.

P3-n14 — Appendix E notation: identify the 68% interval type explicitly
- Problem: The main text uses ±0.382 for sigma-shift and Appendix E gives asymmetric “68% CI” numbers; it’s not stated whether the interval is equal-tailed or HPD.
- Required fix: State “equal-tailed 68% credible interval” (or HPD) in Appendix E and mirror that label in §V A.

P3-n15 — Fig. 3 (right) caption: echo the axis-scale caveat inline
- Problem: The body notes the SDSS axis is the DESI-trained cross-transfer scale; the caption already explains much, but adding a short parenthetical “cross-transfer S (DESI μ,σ)” would make the figure self-contained.
- Required fix: Add “(cross-transfer S on DESI μval, σval)” to the Fig. 3 (right) caption.

P3-n16 — §II D Step 1: explicitly list which surveys pass by (a) vs (b)
- Problem: The text mixes both gate branches but does not summarize in one place which survey passed which branch (DESI Jaccard only, SDSS (a), LAMOST (a), Planck (b), etc.). This hinders quick audit of validation uniformity.
- Required fix: Add a one-line summary table or sentence mapping each survey to gate (a) or (b) (and to “exploratory” where applicable).

EXPLANATION
I focused on arithmetic checks, figure/body consistency, dimensional and null-procedure comparability, and places where denominators, radii, or normalizations change silently. The new items above address: (i) denominator/radius ambiguity in Table I SIMBAD percentages, (ii) a misleading single-threshold line in Fig. 3 for two surveys with different cuts, (iii) cross-curve incomparability in Fig. 10’s injection axes, (iv) an un-derived “2.3” random-match expectation, (v) the ambiguous “1σ envelope” label for a non-probabilistic construction, plus several clarity/minor reproducibility points. These are in addition to (and independent of) the essential/major issues already identified in the initial review.