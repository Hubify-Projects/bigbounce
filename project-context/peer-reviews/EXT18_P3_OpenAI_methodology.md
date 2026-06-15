# P3 EXT18 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=4a8c1172 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6794 chars)
**Wall time**: 346.9s

---

Referee report (methodology/statistics) for “Spectrally Unusual Sources at Scale: …”

Scope of this review
- Focus: statistical/methodological rigor, internal arithmetic consistency, derivation chains, dimensional analysis, significance claims, reproducibility.
- I read the full 30-page manuscript including figures, tables, equations, captions, appendices.

Findings

ESSENTIAL

P3-E1 — §III E (eROSITA), p. 11–12; Table I (caption/footnotes), p. 9
Problem: Non-reproducible primary score axis is used and a hard numeric threshold (0.259) is quoted repeatedly in the main text and Table I, yet the paper states explicitly that no committed score axis reproduces this value (non-monotone with raw, 16 monotone rescalings fail; Spearman ρ = −0.10 over top five). This violates PRD’s reproducibility bar for a load-bearing number.
Required fix: Either (a) re-run the eROSITA model to produce a reproducible, archived scoring axis and update the catalog/threshold accordingly; or (b) remove every numeric threshold and score reference for eROSITA from the main paper (retain only a membership-only list) and eliminate the 0.259 value from Table I and the abstract. In case (b), isolate eROSITA to an appendix and clearly exclude it from any global quantitative tallies beyond “count of members.”

P3-E2 — Data availability, p. 23 (end of paper) and Abstract p. 1
Problem: “will be publicly released with the arXiv posting,” “A Zenodo DOI will be minted at submission,” “frozen pre-submission” are version-history/placeholders. PRD requires finalized, citable artifacts at acceptance. Numerous in-text internal pathnames (“pipelines/…/r24conf…”, “ext3…”) are not archival references.
Required fix: Before acceptance provide (i) a minted DOI for the dataset(s) and code, (ii) frozen release tags/commit hashes that match the exact version used to generate every headline number, and (iii) move all internal pipeline paths and audit artifacts to a “Supplemental Material / Data Repository Guide.” Replace pathnames in the main text with stable references (DOIs, commit SHAs). Remove all “will be,” “pre-submission,” “frozen pre-submission” wording.

P3-E3 — Provenance/version-history language throughout (multiple pages)
Problem: The main text contains internal run logs, audit-artifact filenames, and release-process language (e.g., “artifact pipelines/p3_anomaly_engine/...”, “r24conf…”, “ext3_fm1_…”, “backed-up training log.json”), which are version-history/provenance notes per se. Per instruction 8, these must not appear in the body text of a PRD paper.
Required fix: Move all such provenance details to Supplemental Material. In the main text, retain only the methods/results with stable identifiers (dataset DOI, code commit hash, run configuration summary). Remove all internal filenames and audit tags from the body.

P3-E4 — Leakage in tabular-survey preprocessing not resolved for two surveys; Methods §II B p. 3–5, Gaia §III G p. 13, NEOWISE §III H p. 13
Problem: For eROSITA/NEOWISE/Gaia, the feature scalers were fit on the full sample (including validation tails), not only the training-split. You provide a robustness check only for eROSITA (Jaccard 0.76 top-298; Spearman 0.94). For Gaia/NEOWISE the checks are “queued.” Yet these surveys contribute to headline counts/rates and cross-survey tallies.
Required fix: Provide the same “train-split-only scaler” robustness experiment for Gaia and NEOWISE used for eROSITA (membership overlaps, Jaccard at top-1%, rank correlations), or remove Gaia/NEOWISE from any quantitative headline comparisons (retain as exploratory with explicit exclusion from totals that imply rate estimates). State clearly whether any headline number (including the 269,317 catalog-grade subset) changes under the corrected scaler protocol.

P3-E5 — Statistical gate thresholds and “PASS/FAIL” labels; §II D p. 5; §VI D(ii) p. 21–22; Fig. 10 p. 22; Abstract p. 1–2
Problem: Gate values (validation loss ≤ 0.30; injection-recovery ≥ 50% at 5σ; Jaccard ≥ 0.70 and ≥ 0.50) are introduced as heuristics after results exist. PASS/FAIL are used prominently (including in the abstract) without a pre-registered procedure or operating characteristics (type I/II error, power) and with mixed-test morphologies (e.g., NEOWISE mask “passes by construction”). This risks over-certifying internal QA as formal statistical validation.
Required fix: Recast all “PASS/FAIL” language as “QA checks” unless you (a) pre-declare and justify thresholds in the Methods before results, and (b) provide operating-characteristic curves (e.g., recovery vs amplitude with uncertainty bands, null rejection rates under Monte Carlo) for each gate. At minimum, add a table with the gate definitions, rationale, and an explicit statement that these are engineering QA checks, not formal hypothesis tests, and remove the PASS/FAIL framing from the abstract.

P3-E6 — Planck tier: training/validation overlap and lack of held-out scoring; §III F p. 12
Problem: The top-200 Planck patches are scored on a bank that includes training patches (152/200 in train; 48/200 in val), i.e., not held-out. While you argue the direction of the val-overrepresentation is opposite to memorization, the catalog still lacks a proper held-out evaluation.
Required fix: Reproduce the Planck ranking on a held-out-only bank (exclude all training patches) and report (i) top-200 overlap fraction with the published list, (ii) Spearman rank correlation across the full bank, and (iii) any performance changes in injection-recovery. If the held-out list differs materially, update the released Planck tier accordingly.

P3-E7 — Abstract-last drift: strength and ordering; Abstract p. 1–2 vs. body §III E, §II D, Table I
Problem: The abstract quotes the eROSITA threshold “0.259” and uses gate-PASS language and specific exception handling (e.g., ACT quarantined, “7-way positional dedup at 5″”). Several of these are later qualified as non-reproducible (eROSITA axis) or heuristic QA (gates). The abstract should not elevate provisional/irreproducible details to headline claims.
Required fix: Remove the non-reproducible eROSITA threshold from the abstract; recast gate statements to “quality checks as defined in §II D,” and ensure every abstract scalar is traceable and reproducible per the body.

MAJOR

P3-M1 — Weighted vs unweighted reconstruction loss; Eq. (1) p. 4; Limitations §VI C(7) p. 20
Problem: The primary anomaly score uses unweighted per-element MSE on standardized inputs, ignoring per-element noise variance. This can bias rankings toward low-S/N regions. You note this as a limitation but do not quantify impact on any validated tier.
Required fix: Provide a sensitivity analysis on a stratified DESI/SDSS subset comparing rankings under (i) unweighted MSE (current) vs (ii) inverse-variance weighted MSE using per-bin spectral noise, and report Kendall/Spearman rank correlations and top-k overlaps (k ∈ {100, 1%, 5%}). If materially different, update key results or restrict claims.

P3-M2 — Cross-survey match contamination control; §IV C p. 15–16
Problem: The expected random-coincidence controls use RA-only shifts at fixed Dec, which do not preserve footprint geometry/density. Despite caveats, the text proceeds to assert “expected random coincidences ≲ 10 across all survey pairs against 637 observed … (<2% contamination).”
Required fix: Replace RA-only shifts with sky-rotation/randomization controls that preserve survey footprints (e.g., spherical rotations, or footprint-masked randoms) and recompute expected random coincidences with uncertainties. If not feasible, remove the quantitative “≲ 10” and “<2% contamination” claims and restrict to qualitative statements.

P3-M3 — Multi-tracer Fisher: missing derivation of F0 and c; §V b p. 18–19; App. C p. 23–25
Problem: You use an empirical “positivity-respecting” form 1/σ^2 = F0 + c α^2 and state c = 0.0747 “from the 5-α refit,” but the 5 α points, their uncertainties, and the fit quality are not shown. Readers cannot verify c (load-bearing for 8.14 and the envelope).
Required fix: Add a plot/table of σ(fNL) (or 1/σ^2) vs α for the five sampled α values with error bars and the fitted curve, report fit residuals and uncertainty on c, and show that c > 0 at the quoted significance. Deposit the notebook/script producing these.

P3-M4 — Planck 100% injection-recovery at 5σ: missing uncertainty and plant distribution; §III F p. 12; Fig. 10 p. 22
Problem: “500/500 = 100%” is quoted without uncertainty (binomial CI) and without a distribution of recovery across sky locations/patch noise. This can be misread as absolute.
Required fix: Quote the 68%/95% binomial intervals for the recovery fraction and provide a brief description of the patch selection for injections (e.g., uniform over the |b| ≥ 20° bank). If injections were limited to the validation split, say so.

P3-M5 — SIMBAD cross-match “consistency with random” (DESI top-10k); §III A p. 6
Problem: You infer the 0.2% SIMBAD match among the top-10k “is consistent” with a 0.24% false-match expectation but do not propagate uncertainty or state the exact counts (20/10,000 vs expectation 24). A formal test is trivial here.
Required fix: Quote the exact count and a binomial 68/95% CI for 20/10,000, and explicitly note that 24 expected falls within the CI (or report the simple p-value for the observed deviation).

P3-M6 — RA/Dec spatial test: Cramér’s V notation; §IV B p. 15
Problem: The text typesets Cramér’s V as “Cramér’s V = 376,713/(378,280 × 24,047) ≈ 0.0064” while the definition requires a square root. The numeric value matches the square-rooted ratio; the displayed algebraic fraction omits √, potentially misleading.
Required fix: Correct the displayed formula to include the square root explicitly: V = sqrt(χ²/(N (k−1))). Ensure consistent notation.

P3-M7 — Page-length and density of operational details in main text
Problem: The paper devotes extensive space to operational/logistics details (pod provisioning JSONs, per-run patience values, retrieval failures by tarball, etc.) that belong in Supplementary. This obscures the methodological core and stretches the paper (30 pages).
Required fix: Move operational/logfile/provenance details to Supplemental Material. Condense the main text to ≤18–20 pages by focusing on methods, core results, and validated checks. Retain the necessary numbers but push internal-file narratives to the repository guide.

MINOR

P3-m1 — Threshold labeling, Table I caption p. 9
Problem: The table calls Planck/Gaia/NEOWISE “1.00% rates” though these are predetermined fixed-count selections, not measured rates. You note this in the caption, but the column still invites misinterpretation.
Required fix: Change the cells to “fixed 1.00% (predetermined count)” or “fixed-count” to prevent misreading in isolation.

P3-m2 — Abstract wording on “largest-scale” claim; Abstract p. 1
Problem: Claim “largest-scale application … of which we are aware” lacks a precise literature criterion. You benchmark to [11] inside, but the abstract would benefit from that anchor.
Required fix: Add “(cf. largest prior single-survey anomaly catalog of 2,685 objects in [11])” in the abstract when making the claim.

P3-m3 — Notation collision (“Z” vs z and Z arm); Eq. (2) p. 4, §III B p. 7–8
Problem: You point out that S is a z-score and spectral redshift is z, while Z denotes DESI NIR arm. This is handled, but reinforce by avoiding phrases like “Z column” for redshift (use “redrock Z” or “zredrock” consistently).
Required fix: Standardize wording to avoid “Z” alone for redshift in the main text.

P3-m4 — Injection-recovery figure legend; Fig. 10 p. 22
Problem: Legend uses “FAIL*” with an asterisk; explanation is in the caption, but add a legend key or footnote marker in the panel for standalone readability.
Required fix: Add a small in-panel note defining “FAIL*” as “gate not cleared; XV diagnostic supports detector stability.”

P3-m5 — Minor arithmetic checks (all consistent but add explicit counts)
- §III C p. 8: “77,905 = 4.05% of 1,925,279” — use 4.046% or round to 4.05% and state 77,905/1,925,279 = 0.04046.
- §IV A p. 14: Aggregate 58.8% at 3″ is 235/400 = 58.75%; okay; suggest adding the exact 235/400.

NIT

P3-n1 — Typographic artifacts (soft hyphenation), e.g., “calibra￾tion,” “informa￾tion” across the PDF; throughout.
Required fix: Re-export without forced line-break artifacts.

P3-n2 — Minor symbol artifacts in §IV B p. 15 (“Cram´er’s V = p χ2 p /(N · (k − 1))”) likely from missing sqrt markup.
Required fix: Correct LaTeX for √.

P3-n3 — Figure 3 right panel axis label “Probability density” vs “Prob. density” inconsistency between left/right.
Required fix: Harmonize axis labeling.

Internal arithmetic and consistency spot-checks (passed)
- Dedup compression: 388,493 − 378,280 = 10,213 (2.629%) — correct.
- Point-source vs CMB strata: 378,080 + 200 = 378,280 — correct.
- DESI rate: 195,829 / 22,504,897 = 0.8699% — matches 0.87%.
- LAMOST rate reduction: 44,075/2,054 ≈ 21.46× — matches 21.5× (S > 5 channel).
- SDSS compression: 77,905/12 ≈ 6,492× — “∼6500×” — correct.
- NEOWISE pole-cap excess: 17/436 = 3.90%; uniform |becl| > 80° fraction = 1 − sin 80° = 1.519% → factor ≈ 2.57 — “2.6×” — correct.
- SIMBAD false-match at 5″: π(5″)² × 3×10⁻⁵ arcsec⁻² ≈ 0.00236 = 0.236% — matches.
- Planck top-200 throughput: 200k/25.3 s ≈ 7,905 patches/s — “∼8,000” — correct.
- χ²/dof: 376,713/24,048 ≈ 15.66 — matches 15.7.
- Cramér’s V: sqrt(376,713/(378,280×24,047)) ≈ 0.00644 — matches 0.0064.
- Multi-tracer envelope from α̂ = 0.19 ± 0.65 with F0 = 1/8.98², c = 0.0747 → σ = 8.14; envelope [3.92, 8.98] — consistent.
- NANOGrav Δσ: (3.0 − 2.567)/0.382 = 1.13σ; (4.33 − 2.567)/0.382 = 4.61σ — correct.

Stand-alone reader test
- Most definitions are present. However, the Fisher-block and the 5-α refit (P3-M3) need to be self-contained. The eROSITA axis reproducibility must be rectified (P3-E1). The Planck held-out issue needs resolution (P3-E6).

Effect sizes and non-comparability disclaimers
- You properly flag non-comparability of σ, Jaccard, injection-recovery, and Bayes-factor metrics across contexts in most places, and flag the NEOWISE mask as geometry-only. Ensure every juxtaposition (e.g., in the Conclusions summary list) retains those caveats (addressed by P3-E5).

Recommended maximum page count
- Recommend ≤ 18–20 pages in main text by moving provenance/logistics (file paths, pod provisioning, per-run logs) to Supplemental Material without reducing methodological content.

## Summary recommendation
MAJOR REVISIONS

The manuscript presents an ambitious, well-instrumented multi-survey anomaly-detection effort with many careful caveats. However, several issues block PRD acceptance: (1) a non-reproducible primary score axis (eROSITA) is used with hard thresholds in the main text; (2) data/code availability and internal versioning are not finalized (numerous in-text pipeline paths and placeholders); (3) scaler leakage robustness is missing for Gaia/NEOWISE; (4) Planck tier lacks a held-out confirmation; and (5) the gating “PASS/FAIL” framing needs to be downgraded to QA checks or formally justified. Addressing these, plus the methodological clarifications and minor fixes above, will bring the paper within PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND PASS

ESSENTIAL

P3-E8 — Conflicting guidance on which object tier is “recommended”
Location: Abstract p.1–2; Table I footnote ♠; §IV C
Issue: The abstract first directs “Downstream object-level analyses … should use the 378,080 point-source tier” but then declares “the recommended catalog-grade point-source subset is 269,117 unique entries” (i.e., excluding the LAMOST exploratory tier and the 200 Planck patches). The body repeats both notions (six-way catalog-grade = 269,317 including Planck; 269,117 after dropping Planck), yet still advises using the 378,080 point-source tier for downstream science.
Required fix: Provide a single, unambiguous recommendation. If the 269,117 is the vetted catalog-grade set, say that all downstream science should use it; otherwise justify why users should prefer the larger, exploratory-including 378,080. Make all tallies, figures, and conclusions consistently reference the chosen “recommended” tier.

P3-E9 — Gaia production preprocessing is not reproducible from committed artifacts
Location: §II B (tabular preprocessing), §III G
Issue: The exact 20-feature Gaia DR3 production preprocessing script “was not recovered”; analyses rest on a lineage-inferred 21-feature successor. For PRD reproducibility, the production code and exact feature list used to generate the published 50K/500 anomaly set must be archived.
Required fix: Archive and cite the exact Gaia production preprocessing code (or re-run Gaia with an archived script and replace all Gaia numbers/tables accordingly). If unavailable, mark Gaia as non-reproducible and remove it from any headline quantitative totals (similar to your “membership-only” handling for eROSITA).

MAJOR

P3-M8 — Misuse of p-values on a non-random, stratified subsample
Location: §III A (DESI S vs SNR), p. 6
Issue: You report Spearman ρ = −0.03 with p = 0.12 on a purposefully stratified (log-uniform-in-SNR) subsample of 2,670. A classical p-value assumes random sampling from the population; it is not interpretable under this design.
Required fix: Remove the p-value or replace it with a design-respecting uncertainty (e.g., permutation within SNR strata) and emphasize the effect size only (|ρ|). If kept, explicitly state that this p-value is not a population-level significance test.

P3-M9 — Catalog-level DESI stability not quantified
Location: §II B–C; §II D (Step 1); §VI D(i)
Issue: You provide 5-fold Jaccard stability on the 47k training pool and a 103k OOD control, but do not quantify top-k stability of the full 22.5M DESI catalog across independent seed retrains (production vs seed-controls on the full scan).
Required fix: Report catalog-level stability (e.g., Jaccard overlap of S>5 sets) across ≥3 seed retrains on the full DESI stream (or on disjoint large sky chunks with matched coverage), with uncertainty. If infeasible, clearly state this limitation near the DESI headline rate and confine “stability PASS” claims to the training/OOD subsets only.

P3-M10 — “No tri-survey clusters” claim lacks sensitivity check
Location: §IV C (FoF audit)
Issue: You assert “exactly 637 clusters span two surveys (none spans three or more).” You provide a radius sweep for total unique counts but not for the existence of triads.
Required fix: Report the count of ≥3-survey clusters under the same {3″, 5″, 7″} sweep (expected to be tiny but nonzero once radii/PSFs differ) or qualify that the “none” statement is only demonstrated at 5″.

P3-M11 — “Zero positional overlaps” between Planck patches and point-source catalogs is not a meaningful dedup statistic
Location: Table I footnote ∥; §III F; §IV C
Issue: Reporting “zero positional overlaps” at 5″ between 10°×10° Planck patches (center coordinates) and point sources invites misinterpretation. Patch-vs-object association requires an aperture/footprint-based logic, not a 5″ cone.
Required fix: Either (a) exclude Planck from the positional dedup accounting entirely (treat as a disjoint stratum only), or (b) define and report a patch-appropriate association metric (e.g., object within the patch footprint). Clarify in the text that “zero overlaps” at 5″ is geometry-trivial and not informative.

P3-M12 — Unsubstantiated numeric bounds in systematics section
Location: §V(c), Table V (c,e)
Issue: Claims like “fiber nuisance |Δσ/σ| < 0.01% at σδfiber = 0.05” and “GR projection |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1” are presented as internal bounds without derivations or references.
Required fix: Provide a short derivation (or a cited, configuration-matched reference) and the null procedures used to compute these bounds, or rephrase as qualitative expectations without percentages.

MINOR

P3-m6 — Total-row “rate” entries are misleading composites
Location: Table I, two total rows
Issue: You compute total “rates” (0.86%, 1.01%) while the numerator aggregates fixed-count tiers and data-driven rates. Despite a caption caveat, the table cell invites misreading.
Required fix: Replace total-row rates with “N/A (composite of fixed-count + data-driven thresholds)” or omit the column for total rows.

P3-m7 — Provide explicit counts and CIs for additional binomials you cite informally
Locations:
- §III A (DESI top-200 “0/200 visually flagged”): add a 95% binomial CI for 0/200.
- §III C (SDSS SIMBAD-unmatched “90%”): add exact numerator/denominator and the cone radius used.
Rationale: These tighten claims and align with the improvements requested in P3-M5 of the first review.

P3-m8 — Figure/body alignment spot checks (new minor polish)
- Fig. 7 bottom-right red dashed line appears to mark S ≈ 15; the text references “101 objects exceeding S = 15.” Consider noting this tie-in in the caption for clarity.
- Fig. 9 inset “6.1%” improvement is the fixed-α reference; add a brief in-caption pointer to §V that the primary empirical result shows no improvement at current S/N.

P3-m9 — Terminology precision for Redrock “Z”
Location: §III A/B
Issue: Occasional “Z column” phrasing risks clashing with DESI Z arm. Use “Redrock template-fit redshift z (Z in the table schema)” consistently (extends P3-m3 guidance).

NIT

P3-n4 — “Cramér’s V” typesetting
Location: §IV B
Issue: Residual math-mode artifacts (“p χ2 p /(N · (k − 1))”) appear besides the already-noted missing square root.
Required fix: Clean LaTeX to V = sqrt(χ²/(N (k−1))) with consistent symbols.

Explanation
The initial review focused on reproducibility (eROSITA axis), gating, data/code availability, leakage, Planck hold-out, Fisher-fit documentation, several arithmetic checks, and abstract fidelity. This second pass targeted overlooked comparability, clarity, figure–text alignment, and hidden statistical assumptions (e.g., p-values under stratified sampling), plus table presentation that could mislead in isolation.