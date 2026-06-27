# P3 R55 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R55_P3/paper3_draft.pdf` md5=120624c4 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5496 chars)
**Wall time**: 468.8s

---

Referee report (methodology/statistics) for “Spectrally Unusual Sources at Scale …” (30 pages)

Overall scope assessed: autoencoder-based multi-survey anomaly detection, catalog assembly/validation, limited cosmology applications (multi-tracer fNL Fisher forecasting; PTA spectral-index re-fit). I audited the derivations, all quoted scalars, percentages, σ, p-values, and cross-checked internal arithmetic and dimensional consistency across the abstract, figures, tables, and body.

Findings are itemized below. Severity codes:
- ESSENTIAL: must be fixed before the paper can be considered
- MAJOR: significant revision required
- MINOR: should be addressed but not blocking if resolved clearly
- NIT: cosmetic/editorial

ESSENTIAL

P3-E1 — Data availability placeholders and unreleased artifacts
- Location: Section “Data availability,” p. 23
- Text: “... will be made public with the arXiv posting ... A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Problem: PRD requires persistent, citable artifacts at submission. Placeholders (“will be,” “inserted at submission”) are not acceptable. Further, multiple internal run-paths and file names are cited as evidence (e.g., pipelines/.../*.json) but no frozen DOI/commit hashes are provided in the manuscript to guarantee that the exact numbers/figures/tables can be reproduced.
- Required fix: Replace all placeholders with working, permanent DOIs/links (Zenodo/OSF/GitHub release tags), list exact commit hashes, and include a fixed “data release manifest” (with file sizes and SHA-256 hashes) referenced in the text. Ensure all load-bearing claims (counts, thresholds, figures) are reproducible from that frozen release without requiring “pod-side” or unrecoverable scripts.

P3-E2 — Planck tier not evaluated on a held-out set; training overlap in the released Top-200
- Location: §III F, p. 12 (and Fig./Table references)
- Text: “... 152 of the 200 in the training split and 48 in the 15% validation split ... the anomaly tail exhibits a statistically significant over-representation toward held-out patches ... arguing against training-set memorization.”
- Problem: The released Planck Top-200 are drawn from the same 2×10^5 bank used for training. Even if gross overfitting is not observed, the evaluation is not out-of-sample. This undermines the statistical validity of the Planck tier and, through the 7-way dedup, propagates to the headline catalog counts. The “over-representation toward held out” is not a substitute for a proper held-out test.
- Required fix: Rebuild the Planck anomaly tier using a train/validation/test split, where the released Top-N are selected strictly from a segregated test set never used in training/validation. Report revised counts, thresholds, and dedup numbers. Alternatively, perform k-fold cross-validation (retrain per fold; score held-out folds only) and assemble the aggregate Top-200 strictly from out-of-fold scores; update the paper everywhere those numbers appear.

P3-E3 — eROSITA selection axis irreproducible; threshold in paper cannot be recovered
- Location: §III E, pp. 11–12; Table IV p. 12; Abstract p. 1
- Text: “... the production run’s 0.259 threshold could not be reconciled with any tested score axis ... the selection is therefore best read as the fixed top-298 cap ...”
- Problem: A non-reproducible threshold is used (0.259) and is reported in the paper/abstract. This violates PRD’s reproducibility standards for a load-bearing catalog component that contributes to headline counts.
- Required fix: Remove the unrecoverable 0.259 threshold from the paper (including Abstract). Define the eROSITA tier by a fully reproducible selection rule explicitly documented in this paper (e.g., “top-298 by committed raw-score axis with threshold = 3.4119”), and ensure the committed artifacts allow any reader to regenerate the same ranked list. If this cannot be done, eROSITA must be excluded from any “catalog-grade” counts and clearly confined to an “exploratory, membership-only appendix,” and all aggregate counts that included it must be recomputed and relabeled.

P3-E4 — “Catalog-grade” label conflicts with inclusion of exploratory/invalidated components
- Location: Abstract p. 1; Table I footnote ♠ pp. 7–8; §VII Conclusions p. 22–23
- Text: “... the recommended catalog-grade tier contains 269,317 unique entries ... [includes Gaia and eROSITA components marked exploratory and mask-QA-only NEOWISE pass].”
- Problem: The “catalog-grade” count (269,317) includes Gaia (41% cross-validation stability; preprocessing step not fully recoverable) and eROSITA (membership-only; irreproducible score axis; 1.2% injection-recovery). These are self-described as exploratory in the body. Labeling the union as “catalog-grade” is internally inconsistent and may mislead readers.
- Required fix: Either (a) rename that 269,317 tier to “6-way union (validated+exploratory),” and add a second, clearly labeled “validated-only” count that excludes exploratory/QA-only components (Gaia, eROSITA, and, unless revalidated per E2, Planck); or (b) restrict the “catalog-grade” label to surveys that pass the sensitivity gate and are fully reproducible, and recompute the corresponding unique-object count. Update Abstract, Conclusions, and all locations that currently present 269,317 as “catalog-grade.”

P3-E5 — Internal version tags, pipeline paths, and audit-artifact placeholders in the main text
- Location: Numerous (e.g., p. 3, p. 5, p. 6–7, p. 12, p. 15–16, p. 24)
- Text examples: “pipelines/p3_anomaly_engine/.../r24conf_pod_session_batch.json”, “..._R54.json”, “ext3_fm2_planck_top200_train_overlap.json,” “recovered_pod_scripts,” “queued,” etc.
- Problem: The manuscript is peppered with internal file paths, run labels, and audit placeholders that are not appropriate for a final journal article and create ambiguity about the canonical analysis state.
- Required fix: Move all internal path references and audit logs to a formal “Reproducibility Appendix” or to the archived data release documentation. In the body of the paper, reference only stable DOIs or release tags, not ephemeral pathnames. Eliminate “queued” tasks (see P3-M5) or resolve them.

P3-E6 — Full-sample scaler fitting leaks validation information in tabular surveys; incomplete leakage quantification
- Location: §II B pp. 3–4
- Text: For eROSITA/NEOWISE/Gaia, scalers are fit on the full sample (not on the training split), “we assume it does not materially reorder...; eROSITA bounded robustness check shows ∼15–17% extreme-tail churn ... The corresponding checks for the NEOWISE and Gaia tiers remain queued.”
- Problem: Validation leakage (scalers fit on the full sample) compromises the definition of S and the reported validation MSE/thresholds. A robustness check is provided only for eROSITA; for NEOWISE and Gaia it is “queued,” yet both contribute to headline counts.
- Required fix: Recompute NEOWISE and Gaia with scalers fit on the training split only; rerun training and publish the quantified changes in the top-1% membership, tail churn, and any resulting changes in dedup counts. If infeasible, exclude these from any “validated” tier and clearly mark as exploratory-only in all aggregate counts (cf. P3-E4).

P3-E7 — Novelty/scale “largest” claim not substantiated by a formal literature audit
- Location: Abstract p. 1; Table I caption p. 7
- Text: “... the largest application of autoencoder anomaly detection by total sources processed in a single multi-archive framework of which we are aware;” “largest multi-archive anomaly search reported to date ...”
- Problem: Statements of first/largest require a documented literature survey and precise definition of the comparison class (e.g., “autoencoder,” “multi-archive,” “single framework,” etc.). The paper cites [11] for single-survey scale but does not survey multi-archive anomaly searches and anomaly methods other than autoencoders.
- Required fix: Either provide a formal, explicit audit (table or paragraph) delimiting the comparison set with citations and quantitative counts, or soften all such claims to non-assertive language (e.g., “to our knowledge ... appears among the largest by [specific metric]”).

MAJOR

P3-M1 — PASS/FAIL gate thresholds are ad hoc; emphasize continuous metrics and sensitivity
- Location: §II D pp. 5–6; §VI D (ii) p. 21–22
- Problem: Validation gates (val-loss ≤ 0.30 within ≤100 epochs; injection-recovery ≥50% at 5σ; Jaccard ≥0.70/0.50) are acknowledged as heuristic. While many outcomes are far from the thresholds, SDSS’s 64% inject-recover vs 50% is close; classification can flip under modest criterion changes.
- Required fix: Present the continuous validation metrics as primaries (full curves/histograms), and relegate the binary PASS/FAIL to a summarizing sentence with explicit sensitivity (e.g., “PASS for any gate threshold in [45%, 55%]”). For SDSS, quantify uncertainty (bootstrap over plants) on the 64% to show separation from 50% is statistically meaningful.

P3-M2 — Cross-survey random-coincidence control is not geometry-preserving
- Location: §IV A p. 14–15
- Text: “RA-shifted-control expectation of 2.75 ... RA-only shifts at fixed Dec do not exactly preserve sky density or footprint geometry ... reported as a methods-note heuristic only; no statistical significance is assigned ...”
- Problem: A non-geometry-preserving null is used, even while being caveated. As it feeds into the random-coincidence bound (≲10) used to argue that 637 observed multi-survey clusters are overwhelmingly real, a geometry-preserving control should be employed.
- Required fix: Replace RA shifts with rotation-scrambled or survey-footprint-respecting randomizations (e.g., spherical rotations or HEALPix per-survey mask random draws) and recompute the expected coincidences. If not completed, drop the numeric “2.75” and “≲10” and state the conclusion qualitatively, or keep only bounds demonstrably independent of the specific null.

P3-M3 — “Catalog-grade” vs “exploratory” usage inconsistent in abstract/conclusions (clarity)
- Location: Abstract p. 1; §VII p. 22–23
- Problem: The abstract’s wording “the full 378,280 catalog and the LAMOST tier are also explicitly exploratory” is confusing, given that the body elevates a 269,317 “catalog-grade” subset yet includes exploratory components in that figure. This increases the risk of misquotation of the wrong tier for downstream use.
- Required fix: Harmonize the tier naming and counts across abstract and body: define “validated-only” and “exploratory” tiers unambiguously; give both unique-object counts; require downstream users to cite the validated-only tier for science. Remove or restate the ambiguous sentence.

P3-M4 — Pending/“queued” analyses in a published manuscript
- Location: §II B pp. 3–4; §IV A p. 14–15
- Text: “The corresponding checks for the NEOWISE and Gaia tiers remain queued;” “... a great-circle/rotation-scrambled control is deferred...”
- Problem: A submitted PRD manuscript should not carry “queued” or “deferred” work where those results directly bear on validation/reliability of released components.
- Required fix: Complete these analyses and integrate the results (or explicitly demote/remit those components/claims so they do not affect any headline or “catalog-grade” count). Remove “queued/deferred” language throughout.

P3-M5 — eROSITA/NEOWISE/Gaia: clarity on which numbers are data-driven rates vs fixed quotas
- Location: Table I caption p. 7 and table body; Abstract p. 1
- Problem: Planck/Gaia/NEOWISE (top-1%) and eROSITA (top-298) are fixed-count selections, not detection rates; while you do state this in places, the table aggregates these into total “rates” in summary rows that can be misread.
- Required fix: Add a prominent per-row marker and a footnote in the table body, and reiterate in the abstract, that these counts are predetermined selections and not rate measurements. Consider removing the “Rate (%)” column entries for fixed-quota tiers to prevent misinterpretation.

MINOR

P3-n1 — Cramér’s V numeric presentation
- Location: §IV B p. 15
- Text: “Cramér’s V = √(χ^2/(N · (k−1))) = 376,713/(378,280 × 24,047) ≈ 0.0064”
- Problem: The numeric equality as written drops the square-root symbol in the evaluation step, which is confusing. The final value 0.0064 is consistent with taking the square root.
- Required fix: Write “= sqrt(376,713/(378,280 × 24,047)) ≈ 0.0064” to avoid misinterpretation.

P3-n2 — Consistency of “score” terminology in figures
- Location: Fig. 8 caption p. 17; Fig. 12 caption p. 26
- Problem: Multiple “display score (non-catalog)” annotations on spectra/images could be misconstrued as selection scores.
- Required fix: Add a bold, uniform disclaimer at the start of each such caption that these are non-catalog display metrics and should not be compared to S or thresholds; or remove the display-score labels from the figure overlays.

P3-n3 — Equation E1 units/dimensions
- Location: Appendix E p. 25
- Comment: The log10 ρi expression is dimensionally consistent for PTA power-law parameterization if ρ is per-frequency-bin “power” (dimensionless in this KDE-likelihood context). A one-sentence statement clarifying the adopted normalization (e.g., consistency with NANOGrav’s free-spectrum conventions for ρi) would help standalone readers.
- Required fix: Add a brief clarification sentence about normalization to the appendix.

P3-n4 — Throughput/training-time reporting for Planck native retrain
- Location: Table VI p. 24, Planck row
- Problem: “... the total training wall-clock for this run was not preserved in the run logs.” This is not central to science but undermines the completeness of the computational report.
- Required fix: Re-run or recover the wall-clock training time (or remove training-time columns entirely for that row and note “not recorded”).

NIT

P3-z1 — Page-length and presentation
- Location: Whole manuscript (30 pages)
- Comment: The paper reads more like a technical report with numerous internal path references, which impedes readability. The methodology would be clearer if audit-path minutiae were consolidated into a single reproducibility appendix or a separated online supplement.
- Recommendation: Target ≤24 pages in the main paper by moving long table footnotes, pipeline-path citations, and appendices D–F into a dedicated online supplement; keep only what is necessary for a PRD reader to follow and validate the scientific methodology and results.

P3-z2 — Minor typography
- Location: Throughout
- Examples: Mixed use of primes and arcsec symbols (5′′), occasional line-break hyphen artifacts (e.g., “re￾leased”), and special symbols in footnotes (♡, ♠, ♢) may not survive production cleanly.
- Fix: Standardize arcsecond symbol and remove special-symbol footnote markers in favor of numeric/lettered footnotes compatible with PRD style.

Numerical/consistency audit summary

- Headline counts:
  - Native per-survey anomaly totals sum: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493 (verified).
  - Dedup compression: 388,493 − 10,213 = 378,280 unique objects (verified). Point-source vs map-patch split 378,080 + 200 = 378,280 (verified).
  - “Catalog-grade” 269,317 unique (includes Planck 200) implies 269,117 point sources (statement is internally consistent), but see P3-E4 for labeling consistency.

- Ratios/percentages in abstract/body verified:
  - 141×: 378,080 / 2,685 ≈ 141.0 (verified).
  - ~100×: 269,117 / 2,685 ≈ 100.2 (verified).
  - DESI ~73×: 195,829 / 2,685 ≈ 72.9 (verified).
  - Science-class-restricted DESI vs benchmark: 2,468 / 2,685 ≈ 0.92 (“≈0.9×” acceptable).
  - DESI anomaly rate: 195,829 / 22,504,897 ≈ 0.00870 → 0.87% (verified).
  - Dedup radius sensitivity: 3″/5″/7″ unique = 378,604 / 378,280 / 378,145; max deviation from 5″ is |324|/378,280 ≈ 0.0857% (reported 0.086%; verified).
  - SDSS “~6500× rate compression” (S>5): 77,905 / 12 ≈ 6,492 (verified).
  - LAMOST rate compression S>5: 44,075 → 2,054, factor ≈ 21.5 (verified).
  - Novelty fraction: 178/1,000 = 17.8%, Wilson 68% half-width ≈ 1.2% (approximate; verified).
  - Landy–Szalay αjk = 0.19 ± 0.65 → 0.29σ from null (0.19/0.65 ≈ 0.292; verified).
  - Fisher mapping: F0 = 1/(8.98)^2 ≈ 0.01239, c = 0.0747, α = 0.19 → σ ≈ 8.14; envelope [α+σα=0.84 → σ≈3.92; α−σα=-0.46 clip→8.98] (verified).
  - NANOGrav γ posterior: deviations +1.13σ and +4.61σ computed from 2.567 ± 0.382 (verified); Bayes factor BMB/SMBHB ≈ 7.14×10^3 from Table IX (verified).
  - SIMBAD false-match rate: n ≈ 3.0×10^-5 arcsec^-2 at 5″ → Pfalse ≈ π(5″)^2 n ≈ 0.00236 → ≈0.24% per source (verified).

- Equations and dimensional checks:
  - Eq. (1) MSE(x): dimensionless under stated per-feature normalization (ok).
  - S definition Eq. (2): standardized residual (ok).
  - PTA Eq. (E1): consistent with free-spectrum likelihood parameterization (ok; clarify normalization per P3-n3).

- Statistical juxtaposition hygiene:
  - The manuscript generally keeps non-comparable σ values distinct and includes caveats where needed (e.g., Fisher forecast vs PTA posterior; fixed-α vs empirical αjk); good. Keep this rigor when revising phrasing per P3-E4/P3-M5.

## Summary recommendation
MAJOR REVISIONS

The paper makes a substantial technical contribution. However, multiple issues prevent PRD acceptance as-is: (i) non-reproducible eROSITA selection axis reported in the text (and in the abstract), (ii) Planck Top-200 released without a held-out evaluation (training overlap), (iii) the “catalog-grade” tier includes exploratory/insufficiently validated components and is labeled inconsistently, and (iv) data-release placeholders and pervasive internal run-path references that do not meet PRD reproducibility standards. Addressing the ESSENTIAL items (E1–E6) and the major clarity/soundness concerns (M1–M5) is required. The remaining items are minor/editorial.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

[None]

MAJOR

P3-M6 — NEOWISE cutout angular size in Fig. 5 caption is numerically wrong
- Location: Fig. 5 caption (p. 13)
- Text: “DESI Legacy Survey DR9 grz composite, 256 × 256 pixels (108′′ × 108′′).”
- Problem: At the stated LS DR9 scale 0.262″/px, a 256×256 cutout spans 256 × 0.262″ ≈ 67.1″ per side, not 108″. The 108″ figure is inconsistent with earlier text that correctly computes 128×128 → 33.5″ (p. 8).
- Required fix: Correct the caption to 67″ × 67″ (or specify a different pixel scale if used), and check all other cutout-size annotations for consistency.

P3-M7 — Table semantics: “Ntotal” shown for “Path-C unique” row is ill-defined
- Location: Table I, final summary row “Path-C unique (primary)” (pp. 7–8)
- Problem: The Ntotal column in a “unique-object” summary row suggests a processed-input count (37,272,042) but a unique-object row should not carry an input-tally column. This mixes concepts and invites misinterpretation (e.g., as a denominator for the unique count).
- Required fix: Remove Ntotal from the “Path-C unique” row or replace it with “—” and add a note that Ntotal is only defined for per-survey processed inputs, not for a deduplicated union row.

MINOR

P3-n5 — Cramér’s V: off-by-one in k and missing sqrt in the worked numeric
- Location: §IV B (p. 15)
- Text: “Cramér’s V = √(χ2/(N·(k−1))) = 376,713/(378,280 × 24,047) ≈ 0.0064”
- Problems:
  - k−1 should equal the stated dof = 24,048, not 24,047 (off-by-one).
  - The evaluated expression drops the outer square root (you already fixed this partially in P3-n1; this item is about the k mismatch).
- Required fix: Write V = sqrt(376,713/(378,280 × 24,048)) ≈ 0.0064.

P3-n6 — Stale/inconsistent random-coincidence control numbers (2.3 vs 2.75)
- Location: §IV A main text (p. 14–15) vs. footnote 1 on p. 15
- Text: Main text: RA-shifted control mean = 2.75; Footnote 1: “∼2.3 expected coincidences…”
- Problem: Two different RA-shifted control baselines are used for the same exercise; one of them is stale. This inconsistency propagates into the ≲10 total-coincidence bound.
- Required fix: Harmonize to a single, geometry-preserving control (see P3-M2 from your first report) and update all derived numbers consistently. If RA-shift figures are retained temporarily, use a single value everywhere and label as heuristic.

P3-n7 — Reporting a p-value from a stratified design is misleading without qualification
- Location: §III A (p. 8)
- Text: “Spearman ρ = −0.03 (p = 0.12) on a stratified subsample…”
- Problem: You note the sample is deliberately stratified in SNR, so the quoted p-value does not have the usual population interpretation. Presenting it inline risks misreading.
- Required fix: Either drop the p-value or restate as “ρ = −0.03; under the stratified design, a permutation test yields p ≈ 0.12 (not a population-level p-value).”

P3-n8 — PTA Appendix: define fyr explicitly
- Location: Appendix E, Eq. (E1) (p. 25)
- Problem: The symbol fyr appears but is not explicitly defined; readers will infer it is 1 yr−1, but this should be stated.
- Required fix: Add “where fyr ≡ 1 yr−1 is the reference frequency” and keep the P3-n3 normalization clarification.

P3-n9 — Mixed norms for per-arm residuals vs global score; add a sensitivity note
- Location: §II B (p. 4) and Table VII (p. 24)
- Problem: The global anomaly score uses L2 (MSE) while per-arm residuals rB,rR,rZ use L1 (mean absolute residual). Although you state they are used only for within-object dominance, the cross-object family counts (e.g., B-dominant vs multi-band in Table VII) are built from these metrics.
- Required fix: Add a brief sensitivity check or statement confirming that per-arm dominance tallies are unchanged (or very weakly changed) if per-arm residuals are computed with the same L2 norm as the global score.

P3-n10 — Table I notation “Nanom” mentioned in text is not a header label
- Location: Table I notes (pp. 7–8)
- Problem: The caption refers to “Table I Nanom values,” but the actual column header reads “N anom” (typeset space) or “N_anom.” Minor but confusing.
- Required fix: Standardize to “N_anom” (or “N anomalies”) in both the table header and caption text.

NO ADDITIONAL FINDINGS IN OTHER CLASSES

- Arithmetic spot checks (A): Apart from the issues above, recomputed ratios, rates, CI widths, σ mappings, and envelope endpoints remain numerically consistent with the displayed inputs.
- Figure-caption vs body (B): Aside from Fig. 5’s cutout size, captions and body statements agree on numbers/axes.
- Equation dimensions (C): No further dimensional mismatches found beyond the PTA normalization/definition items already noted (P3-n3, P3-n8).
- Cross-references (D): Section, table, and footnote pointers resolve correctly for the sampled cases.
- Null-comparability (E): Your manuscript already flags most non-comparable σ values; no new juxtaposition issues found beyond those in the first report.
- Abstract faithfulness (F): No new abstract/body mismatches beyond placeholders/reproducibility and “catalog-grade” clarity already flagged.
- Novelty claims (G): Covered by P3-E7 in the first report.
- Hedges quantified (H): Instances sampled now carry numbers; no new unquantified hedges identified.
- Appendix/main-text consistency (I): Configs and numbers align except for the PTA symbol definition now flagged.
- Stale numbers (J): Besides the 2.3 vs 2.75 control mismatch, no further stale-number pairs were identified.