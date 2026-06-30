# P3 INT-M2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=f6b8d9a5 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6054 chars)
**Wall time**: 360.9s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog …” (30 pages)

Scope of review
- Journal: Physical Review D
- Role: Methods/statistics referee
- Focus: estimator definition and validation, numerical consistency, significance and error propagation, internal bookkeeping, reproducibility, and whether headline claims are supported by the body.

Overall assessment
The manuscript presents a very large-scale multi-survey autoencoder anomaly sweep, a careful validation protocol (“Path-C”), and two cosmology-oriented applications (multi-tracer fNL forecast and a PTA spectral-index refit). The authors devote unusual care to caveats, cross-checks, and disclosures, which is commendable. However, several essential methodological and bookkeeping issues must be resolved before this work meets PRD standards. In particular, (a) the “recommended-tier” object count is internally inconsistent with the stated deduplication geometry and must be reconciled with a transparent 6-way dedup recomputation; (b) the Planck tier mixes training and scored patches in its published top-200 and should be re-scored on a held-out bank or reclassified; (c) one released component (eROSITA) is explicitly irreproducible on its published score axis; and (d) the paper embeds extensive run-log/internal-artifact language in the main text and lacks a frozen DOI/commit for all load-bearing resources. These are not cosmetic.

Findings (ESSENTIAL / MAJOR / MINOR / NIT)

ESSENTIAL

P3-E1. Section II D/Table I/§IV C/Abstract, pages 1, 9–10, 15–17: Inconsistent deduplication accounting for the “recommended tier”
- What: The paper asserts “recommended tier = 269,317 unique (269,117 point-source) by independent 6-way 5″ dedup.” Summing the six contributing surveys (DESI 195,829 + SDSS 77,905 + eROSITA 298 + Planck 200 + Gaia 500 + NEOWISE 419) gives 375,151 detections. If 6-way 5″ dedup of those six inputs produced 269,317 unique objects, it would imply 105,834 collapsed detections across the six surveys (~28% compression), which contradicts the 7-way 5″ dedup geometry (§IV C) showing only 10,213 collapsed detections (2.629% compression). Removing one survey (LAMOST) cannot increase the number of collapsed detections by an order of magnitude.
- The text also derives 269,317 indirectly as 378,280 (7-way unique) − 108,963 (LAMOST-only uniques) and claims consistency with an independent 6-way rerun, but no 6-way compression statistics (multi-survey vs intra-survey) are shown; §IV C reports only the 7-way audits and an SDSS-threshold sensitivity run, not a 6-way rerun.
- Required fix: Provide a full 6-way 5″ dedup recomputation artifact (counts per input tier, number of collapsed detections split into intra-survey and cross-survey, multi-member cluster size histogram, and the exact unique-object list). Reconcile the 269,317 count with these recomputed numbers and the 7-way geometry (it is not acceptable to rely solely on subtracting the LAMOST-only contribution from the 7-way unique set while simultaneously claiming an “independent 6-way dedup”). If 269,317 arose by subtraction rather than a true 6-way rerun, say so explicitly and remove language implying an independent recomputation. If a true 6-way rerun exists, include its collapsed-detection count and show it is not in gross conflict with the 7-way 10,213 figure.

P3-E2. Section III F (Planck CMB tier), pages 12–13: Published anomaly set contains training patches
- What: The top-200 Planck anomaly patches are selected from a 2×10^5 bank scored with the same native autoencoder; 152/200 of the published anomalies lie in the training split, only 48/200 in held-out validation. Although the authors note that this is “standard practice for autoencoder anomaly scoring,” for a catalog-grade anomaly set this violates a basic hold-out principle and risks training-set peculiarities driving the selection.
- Required fix: Either (a) restrict the Planck catalog-tier anomalies to a held-out score bank disjoint from training (retrain if needed) and report the revised top-200, or (b) clearly downgrade the Planck tier to exploratory status (like Gaia/eROSITA), and remove it from the “validated catalog-grade subset” language in the abstract and conclusions. In both cases, keep the injection–recovery result but make explicit that catalog membership was not determined on held-out data in the current draft.

P3-E3. Section III E/Table I caption and Table IV, pages 11–12: eROSITA score axis irreproducibility in a released tier
- What: The eROSITA “recommended” component is released as a fixed n=298 membership list; the per-object SBigAE score axis used for selection is explicitly irreproducible (16 monotone rescales + 3 IF retrains fail to recover the production axis; top-5 are non-monotone in the raw score), and the paper states provenance was lost. Yet the abstract lists this tier inside the “recommended” count and not solely as exploratory.
- Required fix: Move the eROSITA component out of the “recommended” tier: list it strictly as an “exploratory, membership-only” component in the abstract and main headline results. Clearly separate any counts or novelty rates that include eROSITA from the “validated catalog-grade subset.” Alternatively, re-derive a reproducible axis and selection under full provenance (with code and artifacts) and demonstrate that the recovered membership is stable.

P3-E4. Abstract and Conclusions (pages 1–2, 21–23): Mixing validated and exploratory components in headline “recommended” tier
- What: The abstract leads with a “validated catalog-grade subset ≥268,519” (correctly excluding Gaia+eROSITA), but the next paragraph states “the recommended tier contains 269,317 unique entries,” which still includes Gaia and eROSITA that “fail injection-recovery validation.” This invites confusion between “recommended” and “validated.” PRD abstracts must not conflate validated and exploratory material.
- Required fix: Harmonize terminology. Either reserve “recommended” exclusively for validated components (DESI, SDSS, Planck with the caveat in E2, and NEOWISE geometry-QA) and move Gaia/eROSITA into “exploratory addendum,” or keep “recommended” but state unambiguously in the abstract that it includes two exploratory components that fail validation and are excluded from the validated catalog-size figure. Remove any ambiguity in the Conclusions too.

P3-E5. Data availability/provenance (Section “Data availability,” page 24): No frozen DOI/commit; heavy dependence on unreleased artifacts
- What: The paper repeatedly references internal run-logs and JSON artifacts (“pipelines/.../*.json”), states that the HF dataset “will be made public with the arXiv posting,” and that a Zenodo DOI “will be minted at submission.” For PRD, all load-bearing resources (catalogs, weights, scripts) must be accessible at acceptance with frozen version identifiers. The Gaia feature preprocessing for the 50k-source run is also “not recovered,” replaced by lineage inference, which is not sufficient for reproducibility.
- Required fix: Provide (i) a minted DOI (Zenodo or equivalent) for the exact catalog and all supporting artifacts, and (ii) a tagged code release (GitHub release tag + commit hash) that reproduces all survey-native retrains and scorings that are part of the validated tier. For Gaia, either provide the exact preprocessing script used for the 50k run or clearly exclude Gaia from any tier that requires per-object scores. Update the Data availability section accordingly and remove future-tense language.

MAJOR

P3-M1. Section III F and Fig. 10 caption, pages 12–13 and 23: Injection–recovery pass language and comparability across tests
- What: Different injection tests probe different detectors (continuum-dip vs. emission-line vs. Gaussian patch vs. geometry mask). The paper generally distinguishes these, but a flat list “2 detector-sensitivity PASS + NEOWISE geometry-QA” appears in the abstract and §II D. Ensure that every juxtaposition calling these all “PASS at 5σ” makes the non-comparability explicit (only SDSS and Planck constitute detector-sensitivity PASS; NEOWISE is a geometry-QA).
- Required fix: Where the three tests are juxtaposed (Abstract, §II D, Fig. 10 caption), append an explicit “not directly comparable: NEOWISE is a masking QA, not a detector-sensitivity test; DESI had no injection–recovery; SDSS emission-line recovery fails, only continuum-dip passes 50% @5σ.” Most of this language exists in-body; ensure it is present at every summary juxtaposition.

P3-M2. Section III F (Planck), page 12: Validation loss criterion and pass/fail gate logic
- What: The “two-part gate” in §II D Step 1 requires val loss ≤ 0.30 or ≥50% injection–recovery at 5σ. Planck reports val loss 0.4437 (fails (a)) and 100% injection–recovery (passes (b)). This is fine, but the top-200 are not held-out (see E2). The conclusions list Planck among the “validated components.” Given the non-held-out selection, this is borderline.
- Required fix: If the Planck tier is to remain “validated,” qualify it everywhere with “validated by 100% injection–recovery; not held-out” (Abstract, Conclusions). Alternatively, move Planck to exploratory as in E2. Do not rely solely on Step-1’s (b) to justify “catalog-grade” status if the selection itself is not evaluated on held-out data.

P3-M3. Section II B (“recovered production specification”) and throughout, pages 3–5 and many places: Internal run logs/artifacts and version-history language in the main text
- What: The paper is saturated with internal paths, log filenames, hash-like references (e.g., “pipelines/p3_anomaly_engine/...log.json”), and audit-provenance language (“committed artifacts,” “backed-up training log”). This is not PRD style and makes the paper read like a lab notebook. Such details belong in a data-release note or Supplement.
- Required fix: Move these implementation-provenance strings to a short “Reproducibility and artifacts” appendix or a separate data release note. In the main text, summarize the essential methodological points (e.g., scaler fit on full vs. train split) without file-path noise. Keep only those artifact references strictly necessary to support a quantitative claim.

P3-M4. Abstract and §VI E/F, pages 1–2, 21–23: “largest application”/scale claims
- What: The paper asserts it is “the largest application of autoencoder anomaly detection by total sources processed” anchored to Liang et al. [11]. This superlative should be carefully bounded. If larger-scale unpublished or different-architecture surveys exist, the claim could be over-broad.
- Required fix: Soften to “to our knowledge, by total sources processed; anchored to [11] as the largest prior published single-survey catalog.” Ensure that the benchmark used (2,685) is the appropriate comparator for each multiplier (141×, 100×, 73×), as you mostly do, and avoid calling these “catalog-size increases” outside the like‑for‑like comparison.

P3-M5. Section III C/Table I footnote ♡, page 10: SDSS native continuity slice as a headline number
- What: The 77,905 SDSS native “continuity slice” is defined to match the cross-transfer count, not a data-driven threshold and not the stated “top-1%,” which is 19,253. While the paper discloses this clearly, the presence of this fixed-size slice as the “SDSS headline” in Table I risks misinterpretation in pooled statistics (e.g., totals).
- Required fix: Prominently mark this line in Table I as “fixed-size continuity slice (4.05%) — not a detection rate; native top-1% set = 19,253; S>5 set = 12.” You partly do this in footnotes; add a short superscript in the table cell itself to avoid misreading.

MINOR

P3-n1. Section III A, page 6: Binomial CI calculation disclosure
- What: For the quoted Wilson 95% CIs (0.75% ± 0.008%, 0.037% ± 0.003%), add whether these are approximate normal or Wilson intervals, and confirm the denominators (∼4.9M, ∼1.5M) used. Numbers check out; formalize the method label.

P3-n2. Section IV A, page 14: False-match computations
- What: You quote nSIMBAD ≈ 3.0×10^−5 arcsec^−2 and Pfalse ≈ 2.4×10^−3 at 5″. Provide the source or calculation for nSIMBAD (e.g., measured density on the sky footprint) in a footnote or appendix.

P3-n3. Section III H, page 13: NEOWISE mask QA
- What: The binomial z ≈ 4.0 and p ≈ 6×10^−5 are fine. Add the exact cap area fraction formula reference used (2 caps of angular radius 10° → 1.52%), since you label it as a “uniform-sphere null” and used that in the p-value.

P3-n4. Section V, pages 17–19: fNL forecast positivity form
- What: Excellent that you use a positivity-respecting mapping and state the noise bias. Since you provide F0 and c numerically, please add a one-line pointer to the derivation of c (the “5‑α refit” already cited) in the main text, not only in Table V caveat (i).

P3-n5. Section V A, page 20: “Decisive only vs. circular-orbit SMBHB reference”
- What: You already include the environmental caveat; consider moving the caveat sentence up one line so readers see it before the Bayes factor rather than after.

P3-n6. Section II B Eq. (1), page 4: Clarify weighting
- What: You note loss is unweighted. Add a sentence that you verified score–S/N correlation is negligible for DESI (ρ ≈ −0.03) and state whether similar checks were performed for SDSS/LAMOST. If not, state not done.

P3-n7. Length and structure
- What: At 30 pages with heavy operations-provenance prose in the main text, the manuscript could be streamlined. Recommend ≤20 pages for the main text (push run-log pathnames and audit details to appendices).

NIT

P3-nt1. Typographic/style
- Several occurrences of accent artifacts (e.g., “Cram´er’s”). Clean with journal style.
- Use consistent capitalization for “Gaussian-bump” vs “Gaussian bump.”
- Consistent use of primes/arcsecond symbol (5′′) vs "5″".

P3-nt2. Figure labelling
- Fig. 8 panels burn in “display score (non-catalog)” values. Add “non-catalog visualization score” in the caption more prominently to preclude confusion with S.

Internal arithmetic/consistency spot checks (passed)
- Totals: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; minus 10,213 collapsed = 378,280. OK.
- “73×” (DESI-only vs 2,685) = 195,829/2,685 = 72.9. OK.
- “141×” (full point-source vs 2,685) = 378,080/2,685 = 140.8. OK.
- Recommended point-source ~100× = 269,117/2,685 = 100.2. OK.
- Genuine novelty fraction 178/1,000 = 17.8% (Wilson 68% ±1.2%). OK.
- NEOWISE polar-cap baseline 1.52% (two caps of 10°): OK; binomial z ~ 4.1: OK.
- fNL positivity mapping with αjk = 0.19 ± 0.65 gives σ = 8.14, envelope [3.92, 8.98]. OK.
- NANOGrav γ = 2.567 ± 0.382; Δ from 3.0 ≈ 1.13σ; Bayes factors reproduced. OK.
- DESI S>5 MSE threshold computation from µval ≈ 0.0287: OK.

Abstract-last drift sweep
- Most abstract statements are traceable and properly caveated in body text. Two exceptions require action (E1/E4): (i) the “recommended tier” vs “validated subset” conflation; (ii) Planck inclusion without “not held-out” qualifier.

Provenance surface audit
- “will be made public,” “DOI will be minted,” numerous pipeline pathnames in the body: must be fixed per E5/M3.

Standalone-reader test
- The paper is largely self-contained; however, relying on companion repository artifacts for basic bookkeeping (e.g., 6-way dedup numbers) should be avoided—either summarize those numbers in the paper or relocate the strong assertions until the artifacts are frozen and cited by DOI.

## Summary recommendation
MAJOR REVISIONS

The manuscript presents a substantial and careful piece of work at impressive scale, with many good practices (explicit gates, strong caveats, error propagation). However, several core methodological and bookkeeping issues must be corrected: the inconsistency in the “recommended-tier” dedup accounting, the inclusion of training patches in the Planck anomaly tier (or reclassification), the release of an irreproducible eROSITA score axis within a “recommended” count, and the lack of frozen, citable artifacts/DOIs with main-text overuse of internal run-log language. Resolving these items, and tightening presentation to PRD style, would make the paper suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P3-E6. DESI catalog scored on data that include the training spectra (hold-out principle)
- What: The DESI headline catalog (195,829 anomalies) is scored on the full 22.5M, explicitly including the 47,000 training spectra (VI D(i)). While you provide k-fold and OOD Jaccard checks, the released top lists still include in-sample items. For a “catalog-grade” anomaly set, selection on held-out data is the norm, not merely validation by stability metrics.
- Required fix: Either (a) re-score DESI excluding all training spectra and report the impact on the published top lists (overlap of top-K, churn statistics), or (b) clearly downgrade DESI to “validated by stability gates; selection not held-out,” mirroring the Planck caveat requested in P3‑E2. If (a) is chosen, include a small table quantifying how many of the top-N anomalies (N = 100, 1,000) were training spectra and their replacement rate under a held-out re-score.

MAJOR

P3-M6. Figure 6 mixes cross-match radii in a single panel
- What: The per-survey SIMBAD-unmatched bars are computed at 5″ (per Table I and text), but the dashed “Aggregate 58.8%” line in Fig. 6 comes from a separate 3″ run. Mixing apertures in one figure invites misinterpretation.
- Required fix: Replot the aggregate at 5″ to match the bars, or explicitly split the figure into 5″ and 3″ panels. If you retain the 3″ aggregate, add “(3″ aperture)” in the legend and annotate each bar with its own aperture to avoid cross-aperture comparison.

P3-M7. Cramér’s V expression is dimensionally inconsistent as printed
- What: §IV B prints “Cramér’s V = √χ2/√(N·(k−1)) = 376,713/(378,280 × 24,048) ≈ 0.0064.” The numeric evaluation shown uses χ2/(N·(k−1)) without the square roots, but the final value (0.0064) corresponds to applying the square roots. This is confusing and, as written, dimensionally inconsistent.
- Required fix: Correct the printed evaluation to show V = sqrt[χ2/(N·(k−1))] and, if desired, give the intermediate sqrt values (√χ2 ≈ 613.8; √(N·(k−1)) ≈ 95,421; V ≈ 0.00643).

MINOR

P3-m8. “No clusters span three or more surveys”: provide an overlap matrix
- What: §IV C states that none of the 9,553 multi-member clusters span three or more surveys. Given seven inputs and the presence of bright QSOs likely to appear in DESI, SDSS, and NEOWISE, “zero” is surprising (though not impossible with your strict top-1%/fixed-count tiers).
- Required fix: Add a 7×7 pairwise-overlap table and explicitly list the count of 3+ survey clusters (zero) with a brief rationale (e.g., NEOWISE under-matching at 5″, survey selection disjointness). This will dispel concerns of a labeling or FoF bookkeeping error.

P3-m9. Planck gradient-mode robustness: 13% turnover is not negligible
- What: The Planck top-200 re-score after removing a best-fit per-patch plane retains 187/200 (ρ = 0.973), i.e., 13 changes. The text says “not driven by DC or gradient modes,” but a 6.5% replacement fraction is material for a 200-object tier.
- Required fix: Quantify this explicitly in §III F (e.g., “13/200 changed; sky distribution, MSE range, and summary properties of the 13 replacements are consistent with the full set”), or soften the language from “not driven” to “modestly affected.”

P3-m10. Novelty-vs-archive cross-match method details incomplete
- What: The 17.8% “genuine novelty” uses CDS X-Match to 18 catalogs; bandwidth/radius is clear (5″), but for reproducibility it would help to fix the exact X-Match options (cone mode vs table, epoch handling, duplication resolution).
- Required fix: Add a one-sentence methods note (matching mode and options) and include the query script in the frozen artifacts referenced in P3‑E5.

P3-m11. Expected false-match count for 7-way dedup lacks the effective overlap areas
- What: The analytic “≲10” random-coincidence estimate requires the effective overlap solid angle ΩAB for each survey pair. These ΩAB are not given, so the estimate is not reproducible from the paper.
- Required fix: Provide ΩAB (or the footprint fractions used) in an appendix table, or state the simplifying assumptions (e.g., DESI×SDSS overlap area approximated by …) that lead to ≲10.

P3-m12. PTA KDE Bayes factor: specify kernel and bandwidth for reproducibility
- What: Appendix E says a Gaussian KDE is used to evaluate posterior densities at γ = 3.0 and 4.33, but does not state the bandwidth selection rule. Bayes factors can be bandwidth-sensitive.
- Required fix: State the KDE kernel and bandwidth (e.g., Scott/Silverman/global h), and add a brief robustness note (e.g., factors vary by <X% under ±20% bandwidth).

P3-m13. RA-only shift control for DESI×SDSS
- What: §IV A uses ±0.5°, ±1.0° RA shifts at fixed Dec as a control; you correctly note it is not geometry-preserving.
- Required fix: Either (a) replace with a rotation-scrambled control (recommended), or (b) clearly label the RA-shift estimate as a heuristic and defer any inference to a future, geometry-preserving null, avoiding language that could be read as a significance test.

P3-n8. Minor citation/metadata check
- What: Ref. [12] lists “MNRAS 547, Issue 2 (2026), arXiv:2506.17376.” Please verify the final bibliographic details on acceptance (volume/issue/year may change before publication).

P3-n9. fNL positivity form: pointer to c-derivation in main text
- What: You give F0 and c numerically and mention the 5‑α refit in Table V, caveat (i). For discoverability, add a one-line pointer in §V to the exact appendix/json artifact where the 5‑α grid fit is performed.

P3-n10. Figure 6 caption
- What: To prevent misreading, add “Bars at 5″; dashed aggregate at 3″” (or harmonize apertures per P3‑M6).

NO OTHER DISCREPANCIES FOUND

- Arithmetic spot checks beyond those in the first review re-confirmed (e.g., novelty CI, Bayes factor, Planck p-value, DESI per-class Wilson CIs, multi-radius sensitivity percentages). Apart from the Cramér’s V notational slip, all recomputable figures were internally consistent with the numbers printed in-body or in captions.