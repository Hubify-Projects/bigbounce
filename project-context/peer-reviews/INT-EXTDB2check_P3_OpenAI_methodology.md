# P3 INT-EXTDB2check — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=5bf37274 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5931 chars)
**Wall time**: 382.5s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches”

Scope of review
- Methodological rigor: statistical validity, derivation chains, internal arithmetic, error propagation, cross-checks of all scalar claims in the abstract and conclusions, and figure/table consistency.
- I read all 30 pages, figures, tables, and appendices as rendered here and recomputed the stated rates, fractions, and uncertainties from the provided numbers.

Overall assessment
The manuscript is ambitious and unusually transparent. It documents a very large cross-archive anomaly sweep, with extensive caveats. Many critical reproducibility caveats are stated explicitly (e.g., eROSITA’s irreproducible score axis; DESI lacks an injection–recovery gate; NEOWISE’s “PASS” is mask-geometry only). However, several issues require correction before this can meet PRD methodological standards: tier definitions are inconsistent with the stated validation gates; core reproducibility placeholders remain; one numerical formula in the text is miswritten; and some validation results are “queued” rather than present. Below I list all required fixes, classified by severity.

Findings

ESSENTIAL

P3-E1
- Location: §IV.B, page 15 (paragraph beginning “A spatial uniformity test...”). 
- Problem: The expression for Cramér’s V is miswritten numerically. The text states “Cramér’s V = sqrt(χ2)/sqrt(N·(k−1)) = 376,713/(378,280×24,048) ≈ 0.0064.” The numerical substitution uses χ2 and N·(k−1) without square-roots, which would give ≈4.1×10−5, not 0.0064. The reported value 0.0064 matches the correct sqrt(χ2)/sqrt(N·(k−1)) formula but the displayed numeric substitution is wrong.
- Required fix: Correct the numerical substitution to show sqrt(χ2) and sqrt(N·(k−1)) explicitly (e.g., 613.8 / 95,385 ≈ 0.0064), or remove the explicit numbers and retain only the formula and value.

P3-E2
- Location: Abstract (page 1), and Table I footnote ♠ (page 9–10), and §VII Conclusions (page 22–23).
- Problem: Tier labeling inconsistency. The “recommended tier” (269,317 unique) is defined to include Gaia and eROSITA, but the same abstract states that these two components fail the injection–recovery gate and are “exploratory addendum rather than catalog-grade.” Keeping them in the “recommended” tier is internally inconsistent with your own validation criteria. Later, you also define a “validated catalog-grade subset” that excludes them.
- Required fix: Either (a) exclude Gaia and eROSITA from the “recommended” tier and reserve “recommended” for the validated trio/quartet (DESI, SDSS, Planck, and geometry-gated NEOWISE), or (b) rename the 269,317-tier to “primary” or “complete” and reserve “recommended” for the validated subset only. Reflect this consistently in the abstract, Table I, §II.D, and §VII, and in every place that count is quoted.

P3-E3
- Location: Data availability (page 24).
- Problem: Placeholder language and missing final persistent identifiers. The text states “will be made public with the arXiv posting” and “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).” PRD requires that the deposited artifacts be accessible and citable at acceptance.
- Required fix: Replace all placeholders with the final DOIs/URLs and a frozen version tag/commit hash for code and data. If the HF dataset is not yet public, delay acceptance until it is and insert the permanent links.

P3-E4
- Location: §III.E eROSITA (pages 11–12), Table I notes (#) (page 9–10), §VII (page 22–23).
- Problem: eROSITA per-object score axis is irreproducible (“membership-only”), and the production threshold 0.259 cannot be recovered from any committed artifact. Yet eROSITA is included in the “recommended” tier (see P3-E2).
- Required fix: Either (a) re-derive and publish a reproducible anomaly score axis (or monotone mapping) for eROSITA and a defensible threshold with documented code and artifacts, or (b) move eROSITA entirely out of any “recommended” or “validated” tier and keep it only in an “exploratory membership-only” appendix with explicit exclusion from headline recommended counts. This change must propagate to the abstract, Table I, and §VII.

P3-E5
- Location: §III.F Planck CMB (pages 12–13) and figure/table descriptions.
- Problem: The Planck top-200 tier is selected from a scored bank that includes training patches. Although you present a helpful check showing an over-representation of held-out (validation) patches among the top-200 (48/200 vs ≈30 expected), the released ranking still contains 152/200 training patches. For an anomaly selection that will be used scientifically, PRD requires that the reported catalog be based on a held-out evaluation to preclude any concern about memorization or train-test leakage.
- Required fix: Re-score and publish a Planck top-200 based on a strictly held-out set (no training patches included in the scored set), or explicitly move the Planck tier into “exploratory” status. If you retain the current Planck tier, the abstract and §VII must state unambiguously that the tier is scored on a set including training patches and justify why your injection–recovery and held-out over-representation check suffice methodologically.

MAJOR

P3-M1
- Location: DESI validation, §III.A (pages 6–7) and §VI.D(i) (pages 20–21).
- Problem: DESI is part of the “validated” subset, but no injection–recovery test was executed; the validation rests on two Jaccard stability gates and a 0/200 top-rank visual-inspection null. This is stated clearly but still leaves a detector-sensitivity gap versus SDSS/Planck.
- Required fix: Either (a) execute and report a DESI injection–recovery curve (continuum dip and emission-line variants, like SDSS/LAMOST), including the exact 5σ recovery fraction and seeds, or (b) explicitly relabel DESI as “validated by stability gates, not by injection–recovery” wherever the “validated subset” appears (abstract, Table I notes, §VII) so readers cannot conflate different validation classes.

P3-M2
- Location: §II.B (pages 3–5) and §III.G–H (pages 13).
- Problem: For the tabular surveys (eROSITA, NEOWISE, Gaia), the scalers are fit on the full sample (not on the training split), and only eROSITA has a bounded robustness check. Gaia and NEOWISE checks remain “queued,” which is unacceptable at acceptance given that the scaling choice can reorder tail rankings.
- Required fix: Provide the same bounded robustness checks for NEOWISE and Gaia that you reported for eROSITA (membership overlap at the published threshold, top-x% Jaccard, and full-catalog rank correlation under train-split-only scalers), or refit scalers on training splits and reissue their anomaly lists with updated diagnostics.

P3-M3
- Location: §IV.A novelty assessment (pages 13–14) and abstract (page 1).
- Problem: The 17.8% genuine novelty fraction for DESI top-1,000 is well stated, but the exact CDS X-Match configuration (catalog list, radii, epoch handling, and query reproducibility) is not accompanied by a frozen artifact. This is core to a claim in the abstract and conclusions.
- Required fix: Provide a script or manifest (frozen in the data release) that exactly reproduces the 1,000-object cross-match against the stated 18 catalogs, including the cone radii, epoch/PM handling if any, and the returned counts. Add the artifact path/DOI to §IV.A.

P3-M4
- Location: Reproducibility surfaces throughout (e.g., repeated “pipelines/...json” references) and Data availability (page 24).
- Problem: The manuscript relies heavily on internal artifact paths as the basis for rebuttable claims (“audit artifact ...json”). This is excellent for transparency, but these artifacts must be accessible externally, immutable, and versioned to be suitable for PRD.
- Required fix: Move the critical audit artifacts to the public data release (with DOIs) and cite them with stable links. Provide a brief index of which artifacts support which numerical claims (e.g., a table mapping claim → artifact file).

P3-M5
- Location: §III.H NEOWISE (page 13) and abstract (page 1).
- Problem: NEOWISE is retained in the “validated” subset, but its test is a geometry QA that “passes by construction.” The abstract flags this as geometry-QA, but the label “validated catalog-grade” can still be misread as detector-sensitivity validation.
- Required fix: Clarify in every place the “validated catalog-grade subset” is named that NEOWISE’s gate is geometry-QA only, not a detector-sensitivity validation, and that the “validated” label here has mixed provenance (detector-sensitivity for SDSS/Planck; stability-only for DESI; geometry-only for NEOWISE). Alternatively, adopt new labels for each validation class and avoid collapsing them into a single “validated” bucket.

MINOR

P3-m1
- Location: §IV.A (page 14, “Expected false-match rates”).
- Problem: The global SIMBAD density used (3.0 × 10−5 arcsec−2) should be traceable or justified. 
- Required fix: Add a sentence explaining how this density was estimated (e.g., object count/area at the query epoch) and note any latitude/footprint non-uniformities; optionally add the HEALPix-weighted local-density false-match map in the data release.

P3-m2
- Location: §IV.C (page 16) “RA-shifted-control expectation of 2.75”.
- Problem: RA-only shifts do not preserve footprint geometry. You note this, but the number is still presented as a heuristic expectation.
- Required fix: Provide a geometry-preserving null (e.g., random great-circle rotations) or move the heuristic number into the supplement with a stronger caveat.

P3-m3
- Location: Figures 3, 4, 8 (pages 8, 11, 18).
- Problem: Several panels include “display score (non-catalog)” values that could be confused with catalog selection thresholds.
- Required fix: Add a uniform panel footnote in each figure stating that display scores are for visualization only and not the canonical selection axis; you did this in Fig. 8 caption, but repeat consistently.

P3-m4
- Location: §III.C Table III (page 10–11).
- Problem: The physical-category census is explicitly for the cross-transfer SDSS set, not the native-retrained tier, but that distinction could be missed by readers.
- Required fix: Add a parenthetical in the table caption that these counts characterize the cross-transfer failure mode, not the native tier.

P3-m5
- Location: Throughout (e.g., §II.D, Fig. 2 caption).
- Problem: Frequent use of internal pipeline language (“Path-C,” “quarantined,” “artifact ...json”) in the main text can distract.
- Required fix: Consider moving low-level file-path references to a short “Reproducibility artifact index” in an appendix or the data release README, and keep the main text focused on methods/results.

NIT

P3-n1
- Location: §III.F (page 12–13), Table VI footnote † (page 25).
- Problem: Minor wording/formatting inconsistencies (“— see Table VI footnote” with em-dash spacing; “— a masking-geometry sanity check...” phrasing repeats between text and caption).
- Required fix: Harmonize dash usage and tighten repeated phrasing.

P3-n2
- Location: Bibliography entries [12], [33], etc. (pages 29–30).
- Problem: Journal/issue/year formatting varies (some future-dated; one entry lists “Mon. Not. Roy. Astron. Soc. 547, Issue 2 (2026)” without pages).
- Required fix: Standardize to PRD bib format with full volume/page or arXiv-only until in press.

P3-n3
- Location: Hyphenation artifacts throughout (e.g., “cu­ rated,” “vali­dated”).
- Required fix: Reflow the PDF to remove hyphenation artifacts before final submission.

Arithmetic and statistical checks performed
- All headline ratios and counts I checked match the reported values: 
  - DESI 195,829/22,504,897 = 0.870%; SDSS 77,905/2,304,830 = 3.38%; LAMOST 44,075/11,418,594 = 0.386%; eROSITA 298/930,203 = 0.032%; Planck 200/20,000 = 1%; Gaia 500/50,000 = 1%; NEOWISE 436/43,518 = 1.00%.
  - Path-C native counts sum to 388,493; dedup compression 10,213 → 378,280 unique (2.629% compression).
  - Recommended 269,317 minus flagged (798) equals 268,519; point-source subtraction with Planck (−200) matches 269,117 and 268,319.
  - Novelty fraction 178/1000 = 17.8%; SE≈1.21% for 68% Wilson, consistent with ±1.2%.
  - Fisher forecast recomputation with F0=1/8.98^2 and c=0.0747 at α=0.19 gives σ≈8.14; envelope [3.92, 8.98] verified.
  - NANOGrav γ deviations: (3.0−2.567)/0.382=+1.13σ; (4.33−2.567)/0.382=+4.61σ; Bayes factor ratio 3.23/(4.52×10−4)=7.14×10^3.
  - NEOWISE polar-cap over-density: k=17 vs np0=6.63; z≈4.05; p≈(2–6)×10−5 depending on one/two-sided; your quoted 6×10−5 is acceptable.

Distinct σ/p-null procedures
- You carefully separate different “σ” concepts (forecast σ(fNL), parameter-shift σ for γ, χ2 tests) and in critical juxtapositions explicitly state non-comparability (e.g., the shot-noise Fisher normalization note; the “not a detection” flags). This satisfies the instruction, except for P3-E1’s Cramér’s V numeric miswrite, which must be corrected.

Length
- At 30 pages the paper is long for the claimed methodological contribution. A tighter 24–26 page version is achievable by moving detailed pipeline paths/artifact listings and some extended footnotes (e.g., long Table I notes) into a Supplement or data-release README, without loss of scientific content. This is a recommendation, not a condition.

## Summary recommendation
MAJOR REVISIONS

The work is potentially publishable after substantial revisions to resolve the tier-definition inconsistency, correct the Cramér’s V numeric expression, replace reproducibility placeholders with final DOIs and artifacts, supply the missing scaler-robustness checks for Gaia/NEOWISE (or refit), address the eROSITA irreproducible score axis by removing it from any “recommended” tier or re-deriving a reproducible axis, and either provide a strictly held-out Planck top-200 or clearly downgrade its status. These changes are essential for PRD’s methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass)

ESSENTIAL

P3-E6
- Location: Abstract (page 1), Table I footnote ♠ (pages 9–10), §IV.C (page 16).
- Problem: Recommended-tier dedup radius/cardinality inconsistency. The abstract says “After … 7-way positional deduplication at 5′′, the recommended tier contains 269,317 unique entries,” but the body and Table I footnote ♠ repeatedly state the recommended tier excludes LAMOST and is produced by an independent 6-way 5′′ dedup of only the six included surveys. These two statements are mutually inconsistent about the deduplication basis for the 269,317 figure.
- Required fix: Make it explicit and consistent that the 269,317 recommended tier is from a 6-way dedup (DESI, SDSS, eROSITA, Planck, Gaia, NEOWISE), not a 7-way dedup. Update the abstract and any other location that currently says “7-way” for the recommended tier.

MAJOR

P3-M6
- Location: §II.D Step 5 (page 5), §III.A/C/D/E/G (pages 6–13), Fig. 10.
- Problem: Injection–recovery amplitude/units under-specified for non-CMB surveys. For the Planck CAE you define precisely how “5σ” is constructed after per-patch standardization. For DESI/SDSS/LAMOST continuum-dip and emission-line plants, and for the tabular IF tests (Gaia, eROSITA), the manuscript does not explicitly define σ (raw flux noise vs. standardized feature units, pre/post scaling, per-wavelength or per-object) nor the planting procedure relative to the standardization step. Since your PASS/FAIL gates hinge on the “5σ” point, this is insufficient for replication.
- Required fix: Add exact, survey-specific injection definitions (how σ is computed; where the plant is inserted relative to any standardization; whether re-standardization occurs; seeds and files), and deposit planting/recovery scripts with DOIs. Mirror the Planck-level clarity for the spectroscopic and tabular cases.

P3-M7
- Location: Fig. 10 + caption (page 22) vs body text (§III.F, §III.H).
- Problem: Figure–caption/body mismatch. The caption claims two detector-sensitivity PASS (SDSS and Planck) “brought into the same axis,” and also discusses NEOWISE “mask geometry” injection. The plotted curves, however, only show SDSS/LAMOST/eROSITA/Gaia families; there is no visible Planck curve (100% at 5σ) and the NEOWISE geometry-QA is not meaningfully representable on the x-axis used (amplitude ×σ). This risks confusing readers about what is actually plotted.
- Required fix: Either add the Planck curve (and a clearly separated panel for the NEOWISE mask-QA) or limit the figure to the spectral/tabular detectors and confine Planck/NEOWISE gating to text. Make the figure and caption consistent.

P3-M8
- Location: Abstract (page 1), Table I footnote ♠ (pages 9–10), §II.D (page 5), §VII (pages 22–23).
- Problem: “Validated catalog-grade subset” count (≥268,519) is produced by subtracting the 798 exploratory detections from the recommended 269,317, not by an actual validated-only re-deduplication manifest. You state this explicitly (“not recomputable from the committed aggregate artifacts”), but the result is still treated as a headline quantity.
- Required fix: Run and deposit the validated-only union-find 5′′ dedup (DESI, SDSS, Planck, NEOWISE only), and cite its exact unique count with a DOI to the cluster manifest. If this cannot be produced, avoid presenting ≥268,519 as a catalog-grade headline and clearly label it as a bound by subtraction.

MINOR

P3-m6
- Location: §III.E (pages 11–12), Table I notes (#) (pages 9–10), elsewhere.
- Problem: Symbol reuse for thresholds. You sometimes write eROSITA’s top-cut as “S > 0.259” while “S” is globally defined as the canonical per-survey z-scored MSE. In §III.E you note that the eROSITA production axis is irreproducible and not the canonical S, but the shorthand “S > 0.259” appears elsewhere and is confusing.
- Required fix: Use a distinct symbol for the irreproducible eROSITA production axis (e.g., τeROSITA or Sprod), and replace any stray “S > 0.259” with the unambiguous symbol plus a reminder that it is not the canonical S.

P3-m7
- Location: Abstract first sentence and Conclusions §VII point 1 (pages 1, 22–23).
- Problem: “Largest … of which we are aware” claim is not concretely supported beyond comparing to [11], which is single-survey. Since the claim is about “a single multi-archive framework,” readers need a crisp baseline.
- Required fix: Add a short justification (e.g., a sentence listing prior multi-archive anomaly sweeps, if any, and their processed-source counts), or narrow the claim to “largest number of sources processed relative to prior single-survey anomaly catalogs [11].”

P3-m8
- Location: §IV.A footnote 1 (page 14).
- Problem: The ≲10 expected-random-coincidences estimate for the 7-way 5′′ dedup is asserted without the ΩAB basis for each survey pair (only DESI×SDSS is sketched).
- Required fix: Deposit a small artifact (table or JSON) with the areas used for each pair and the resulting expected coincidences, and cite it. This keeps the helpful sanity check reproducible.

P3-m9
- Location: §III.F (pages 12–13).
- Problem: Wording about correlation and the binomial p-value: you correctly note spatial correlation inflates the effective sample size and thus the simple binomial p≈4×10−4 is a lower bound on the true tail probability. Consider adding a one-liner clarifying that “lower bound” here means “optimistic significance (smaller p) relative to a correlation-aware estimate,” to avoid misreadings.

NO OTHER NEW ARITHMETIC OR CONSISTENCY ERRORS FOUND

- I rechecked additional rates, sums, overlaps, and envelope computations not covered in my first review (e.g., Table III sums to 77,905; the radius-sweep unique-object variations and compressions; NEOWISE mask fractions and binomial z; Planck train/val over-representation calculation; all consistent). Aside from the Cramér’s V numeric substitution already flagged in P3-E1, I did not find new numerical miscomputations.