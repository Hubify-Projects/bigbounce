# P3 RC-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=8ed23638 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5497 chars)
**Wall time**: 597.0s

---

Referee report on: “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches”

Scope of review: methodology rigor, statistical validity, derivation chains, internal arithmetic consistency, dimensional analysis, and reproducibility. I audited scalar quantities in the abstract and conclusions against the body; recomputed quoted ratios/percentages; checked figure/table consistency; verified that distinct null procedures are not conflated.

Overall assessment: The paper presents a large anomaly-detection effort spanning multiple surveys with extensive internal QA. However, as a PRD methodology paper, several aspects are not yet acceptable: (i) key headline numbers in the abstract rely on an inexact “≥” lower bound caused by a preventable deduplication bookkeeping gap; (ii) data/code availability is not finalized (placeholders for DOIs; “will be released with the arXiv posting”); (iii) “recommended” tier currently includes components that explicitly fail the injection–recovery gate (eROSITA, Gaia), one of which has an irreproducible score axis; (iv) DESI—the anchor tier—has no injection–recovery sensitivity test, yet contributes to a “validated catalog-grade” subset in the abstract; (v) the main text contains numerous internal-run pathnames, build tags, and audit-file references that must not appear in a PRD article and should be moved to a formal Supplement or external data archive. Several additional methodological clarifications and minor arithmetic/notation corrections are also required.

Findings

ESSENTIAL

P3-E1 (Abstract, p.1; §II.D, p.6; Table I footnote ♠, p.9): Inexact “validated” headline count; missing exact re-dedup for validated-only subset
- Offending text: “validated catalog-grade subset of ≥268,519 unique anomalies (≥268,319 point-source) … the exact validated-only 5″ re-dedup of the 798 exploratory detections is not recomputable from the committed aggregate artifacts…”
- Problem: The abstract’s lead number for the validated subset is an inequality caused by a reversible pipeline bookkeeping choice. This is not acceptable for a catalog-class PRD article.
- Required fix: Recompute and report the exact unique-object count for the validated subset by re-running a deterministic deduplication on the four validated components only (DESI, SDSS, Planck, NEOWISE), or on the 6-way recommended tier with Gaia+eROSITA dropped upstream before dedup. Replace all “≥” validated-subset counts in the abstract/body with exact, reproducible values and deposit the script/output as part of the archived release.

P3-E2 (Data availability, p.24): Placeholders; missing stable DOI and frozen release identifiers
- Offending text: “will be publicly released with the arXiv posting”; “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Problem: PRD requires citable, stable artifacts at acceptance; placeholders and future-tense promises are not acceptable.
- Required fix: Provide: (i) a working DOI (Zenodo or equivalent) for the exact data release used in the paper; (ii) a permanent URL/DOI for the code at a frozen tag; (iii) a manifest with SHA-256 checksums matching the DOI contents; and (iv) confirmation that the in-paper numbers reproduce from those artifacts. Replace all “will be released/minted” language with the final identifiers.

P3-E3 (Multiple locations: p.3, p.4, p.5–6, p.9–13, p.15–17, p.20–23, p.25–28): Internal-run pathnames, audit tags, and ephemeral bookkeeping in main text
- Examples: “pipelines/p3_anomaly_engine/recovered_pod_scripts/…”, “r24conf_pod_session_batch.json”, “r43_4caveats_closure/result.json”, “r23conf_dedup_audits.json”, “gaia_expanded.py”, specific SPARCL seeds, etc.
- Problem: The main text is littered with internal file paths, run tags, and audit JSON filenames. These are not stable citations and do not belong in the PRD article body.
- Required fix: Move all such internal-provenance strings to a formal Supplementary Material (SM) or to the archived repository README/manifest (referenced by DOI). In the article, replace them with stable references (e.g., “see SM Sec. S2” or “see DOI:xxxx, artifact Y”). Ensure every load-bearing claim in the article body is backed by a stable citation, not a lab-internal path.

P3-E4 (Abstract p.1; §III.A p.6; §VI.D(i) p.21): DESI lacks an injection–recovery test yet is called “validated” in the lead subset
- Offending text (abstract): “validated catalog-grade subset … the four components that do not fail injection-recovery (DESI DR1, SDSS DR18, Planck and NEOWISE)”
- Problem: DESI did not execute an injection–recovery (authors rely on Jaccard stability and 0/200 top-rank visual checks). Calling DESI “does not fail injection–recovery” is misleading; it was not tested on detector sensitivity in the same sense as SDSS/Planck.
- Required fix: Either (a) run and report a DESI injection–recovery sensitivity analysis at the same 5σ convention used elsewhere, or (b) rephrase the abstract and all “validated” subset language to clearly state that DESI did not have an injection–recovery gate, and that its robustness is argued from cross-validation/holdout Jaccard and visual-inspection only. Do not claim DESI “passed” a gate it did not take.

P3-E5 (Abstract p.1; Table I and notes p.9–10; §III.E p.11–12; Conclusions p.22–23): “Recommended” tier includes components that fail the injection–recovery gate and, for eROSITA, an irreproducible score axis
- Offending text: “the recommended tier contains 269,317 unique entries… Two components beyond the validated core — Gaia DR3 and eROSITA DR1 (798 detections) — fail injection-recovery validation…”; “eROSITA tier released as … membership list only; per-object SBigAE score axis irreproducible”
- Problem: A “recommended” tier that includes failures of the primary validation gate (and one with an unreproducible score axis) is contradictory and potentially misleading to readers.
- Required fix: Restrict “recommended” to components that pass detector-sensitivity gates (DESI subject to P3‑E4 resolution, SDSS, Planck; and keep NEOWISE clearly labeled as geometry-QA only), or rename this tier explicitly (e.g., “recommended+exploratory-flagged”). For eROSITA, either: (i) provide a reproducible per-object score axis (or a monotone mapping that recovers the published threshold), or (ii) clearly separate eROSITA as “membership-only exploratory” outside of any “recommended” branding in the abstract and conclusions.

P3-E6 (Figures/Sections: §III.F p.12–13; Table VI note † p.25): Planck injection amplitude units and detectability calibration
- Offending text: 100% injection–recovery “at 5σ Gaussian-bump amplitude,” defined in standardized patch units; no mapping to physical μK.
- Problem: Without a μK calibration (or an L2-equivalent variance), the 100% recovery at “5σ” is not interpretable in CMB-temperature units; as a methods paper, readers need the dimensional connection.
- Required fix: Provide the per-patch standardization statistics and give the equivalent bump amplitude in μK (e.g., μK rms per patch class) or quote a conversion that places the 5σ plant in physically interpretable CMB units. State explicitly whether the amplitude is above/below known Planck noise levels and foreground residuals in the masked sky.

P3-E7 (Throughout, e.g., §II.D p.6; Table I notes p.9–10; §VI.D(ii) p.21–23): Gate thresholds not pre-registered; need sensitivity analysis
- Offending text: “gate values … are heuristic engineering thresholds … classification is insensitive to moderate threshold variation…”
- Problem: As a methodology contribution, gate choices (val-loss ≤0.30, ≥50% at 5σ, Jaccard ≥0.70/0.50) need quantitative robustness checks.
- Required fix: Provide a brief sensitivity analysis quantifying how survey classifications change under reasonable threshold variations (e.g., val-loss cut from 0.2–0.5; injection threshold 40–60%; Jaccard cut 0.6–0.8). A table summarizing classification stability is sufficient.

MAJOR

P3-M1 (p.15, §IV.B): Cramér’s V numeric substitution omits the square root in the displayed algebra
- Offending text: “Cramér’s V = √(χ²/(N·(k−1))) = 376,713/(378,280×24,048) ≈ 0.0064”
- Problem: The right-hand numeric expression shows the ratio without the square root, yet the reported value (0.0064) corresponds to applying the square root. This is confusing/incorrectly typeset.
- Required fix: Correct the displayed numeric substitution to include the square root explicitly: V = sqrt(376,713/(378,280×24,048)) ≈ 0.0064.

P3-M2 (p.10–11, §III.C; Table I note ♡): SDSS continuity slice vs. top-1% vs. S>5 thresholds
- Problem: The paper uses three SDSS thresholds for different purposes. While explained, it is easy for readers to conflate them.
- Required fix: Add a small boxed summary or a one-row table in §III.C stating, side by side, the three SDSS threshold definitions, counts, and use-cases (continuity baseline 77,905 at S≥0.1060; native top-1% 19,253; S>5 only 12). Explicitly reiterate that rates/novelty analyses should not mix these.

P3-M3 (p.13–14, §IV.A): SIMBAD unmatched fractions computed at 5″ per-survey vs. 3″ for the pooled aggregate
- Problem: The aggregate 58.8% unmatched uses 3″ while per-survey fractions use 5″. You note this, but the mixed radii complicate comparisons.
- Required fix: Provide the aggregate figure also at 5″ in the main text or SM, or else always state both radii where quoted side-by-side.

P3-M4 (p.12, §III.E; Table IV caption): eROSITA “membership list” presentation vs. usage
- Problem: The current presentation can still be interpreted as a ranked catalog with meaningful per-object anomaly scores.
- Required fix: In the main text and Table IV caption, reiterate that eROSITA’s per-object SBigAE scores are not reproducible, that only the membership list is canonical, and direct users to the reproducible raw and IF axes if they need a ranking.

P3-M5 (p.6–7, §III.A): DESI per-class anomaly-rate comparison lacks a figure/table
- Offending text: “galaxies are flagged … 0.75% vs. 0.037% … anomalies peak at z ∼ 0.75 compared to z ∼ 0.93…”
- Problem: Useful quantitative statements are not accompanied by a figure/table (CDF/PDF) to support the text.
- Required fix: Add a compact figure or table with the per-class rate summary (with CIs) and the redshift histograms (or summary stats) for anomalies vs. non-anomalies in the validated-TARGETTYPE subset.

P3-M6 (p.6, §III.A): Full-stream DESI training–test overlap remains in the production scoring
- Problem: While you present solid k-fold/OOD Jaccard checks, the production scoring includes training spectra.
- Required fix: Provide, in SM, the DESI S>5 anomaly rate computed on the subset excluding the 47k training spectra and report the relative change (expected to be negligible, but this confirms the claim).

P3-M7 (Abstract p.1; §VII p.22): “Largest”/“∼141×” novelty/process claims
- Problem: Strong “largest” statements rely on a single anchor [11]. PRD prefers precise, verifiable claims.
- Required fix: Rephrase to “to our knowledge, by processed-source count, anchored to [11] (2,685 anomalies on DESI EDR) we processed ~141× more point-source anomalies” or provide additional literature context confirming that no larger multi-archive effort exists.

P3-M8 (p.12–13, §III.F; Table VI note †): Planck top-200 scoring axis/units
- Problem: Per-patch reconstruction MSE is quoted on a survey-specific standardized axis; readers may not realize these are dimensionless.
- Required fix: State explicitly in §III.F that those MSE scores are dimensionless (standardized-patch units), and cross-reference the μK mapping from P3‑E6 once provided.

P3-M9 (p.19–20, §V A; Appendix E): Bayes factors vs. σ-shifts
- Problem: You appropriately caution that these are not directly comparable statistical objects; ensure this caveat appears at every juxtaposition.
- Required fix: At the end of §V A (main text), add a one-sentence reminder that σ-shifts and Bayes factors summarize different aspects of evidence and are not directly comparable (you already do this partly in the table note; mirror it in the main text).

MINOR

P3-n1 (p.5, Eq. 1): Units/definition clarity
- Comment: MSE is defined per-element on standardized inputs; note explicitly “dimensionless” once near Eq. (1).
- Fix: Add “(dimensionless; inputs are per-survey standardized)” after Eq. (1).

P3-n2 (p.4–5, §II.B): Standardization on full sample for tabular surveys
- Comment: You provide a robustness check for eROSITA and note queued checks for NEOWISE/Gaia.
- Fix: Move the eROSITA robustness numbers into a small SM table and either run the queued checks (preferred) or clearly mark them as outstanding.

P3-n3 (p.8, Fig. 3): Axis and legend clarifications
- Fix: Add “dimensionless” to the S-axis labels and “density-normalized histograms” in the caption to avoid misreading y-axes as counts.

P3-n4 (p.18, Fig. 8): “display score (non-catalog)” annotations
- Comment: These might confuse casual readers.
- Fix: Add a first-sentence caption note: “Panel annotations are display-only scores from the figure-generation script and are not catalog selection scores.”

P3-n5 (p.9, Table I): Footnote symbols ♡, ♠, ♢, # etc.
- Fix: Replace nonstandard symbols with lettered footnotes (a), (b), … to conform with PRD style.

P3-n6 (p.7, Fig. 2): Caption clarity on ACT points shown but quarantined
- Fix: Add in the first sentence: “ACT DR6 points are plotted only as a historical baseline; ACT contributes zero objects to the final catalog.”

P3-n7 (p.11, Fig. 4): Clarify the score axis
- Fix: Add “scores on DESI-trained cross-transfer axis” to the caption.

P3-n8 (p.22–23, Fig. 10 caption): Emphasize that NEOWISE is a geometry-QA gate
- Fix: Already present; consider bolding “geometry-QA” once for emphasis (PRD allows italics/bold sparingly).

P3-n9 (Appendix C/E figures): Notation normalization
- Fix: Where two σ(fNL) baselines appear (8.98 vs 16.85) ensure every figure/caption states “not directly comparable normalization; only relative changes transfer”.

NIT (cosmetic/editorial)

P3-c1: Consistent use of “arcsec” vs. “′′”
- Fix: Use “arcsec (′′)” once and pick one style thereafter.

P3-c2: Hyphenation/spacing (e.g., “re-score”, “cross-transfer” mixed)
- Fix: Normalize.

P3-c3: Ellipses and em-dashes: standardize to PRD style.

P3-c4: Replace “queued for the data release” (p.7) with a neutral “deferred to SM” or complete the analysis before resubmission.

Arithmetic/consistency checks performed

- DESI anomaly rate: 195,829/22,504,897 ≈ 0.00870 (0.87%). OK.
- DESI science-target recount: 2,468/190,015 ≈ 1.30% → “∼98.7% not science-targets.” OK.
- Benchmark comparison: 2,468/2,685 ≈ 0.92 (≈0.9×). OK.
- Recommended-tier arithmetic: 269,317 total; minus 200 Planck → 269,117 point-source; minus 798 (Gaia+eROSITA) → 268,519 (unique) and 268,319 (point-source). OK.
- Path-C sum and compression: 388,493 inputs − 10,213 collapsed = 378,280; 10,213/388,493 = 2.629%. OK. Radius sweep unique-count deltas consistent (≤0.086%).
- NEOWISE mask excess: 17/436 = 3.90% vs. 1.52% null → factor ≈ 2.57, z ≈ 4.07; p ~ 2–6×10−5. OK.
- Novelty: 178/1000 = 17.8%; SE ≈ 1.21% → “Wilson 68% ±1.2%.” OK.
- Planck train/val over-representation test: 152/200 in train vs. 85% expected; z ≈ −3.56; one-sided p ~ 1.9×10−4 (two-sided ~3.8×10−4). OK.
- Fisher envelope: α̂=0.19±0.65; F0=1/8.98²; c=0.0747 → σ(fNL)=8.14; envelope [3.92, 8.98] from α in [0.84, 0]. OK.
- NANOGrav γ: 3.0 is +1.13σ from mean 2.567 (σ=0.382); 4.33 is +4.61σ; Bayes factor 3.23/(4.52×10−4)=7.14×10³. OK.
- Cramér’s V computation: numeric value (0.0064) matches sqrt form; displayed algebra is misstated. See P3‑M1.

Length and structure

- The main text (30 pages) reads like an internal technical report with many operational details. For PRD, I recommend tightening the main manuscript to ≤20 pages by moving most run-log references, pathnames, and extended audit artifacts to a SM. Keep all load-bearing quantitative results in the article; move provenance minutiae to the archive/SM.

Abstract-last drift sweep

- Abstract claims cross-check to body: all multipliers (141×, 100×, 73×), DESI rate (0.87%), science-target recount (2,468; 0.9×), validated/recommended counts, novelty (17.8% ±1.2%), gate outcomes (2 PASS + NEOWISE geometry), and cosmology (σ(fNL)=8.14, envelope; γ shifts; Bayes factor) are traceable and numerically consistent. The single unacceptable element is the inexact “≥268,519” validated subset (P3‑E1) and the conflation of “validated” with DESI (no injection–recovery) and with a “recommended” tier that includes components failing injection–recovery (P3‑E4/E5). These require correction/clarification in the abstract.

Standalone-reader test

- Most symbols are defined in-text. However, several load-bearing details are deferred to “companion data repository” and internal artifact names. Move sufficient method details into a SM such that a reader can reconstruct the gates/thresholds, dedup, and Fisher steps without opening external code, and ensure all external artifacts are referenced by DOI.

## Summary recommendation
MAJOR REVISIONS

Justification: The methodological contribution is potentially valuable, with thorough internal QA and transparent caveats. However, PRD standards require exact, reproducible headline numbers; finalized, citable data/code artifacts; and a clear separation of validated vs. exploratory components. The present manuscript uses an inexact validated-subset count in the abstract; includes internal-run pathnames throughout; lacks a DESI injection–recovery test while branding the subset as “validated”; and presents a “recommended” tier that includes surveys failing the core gate (and one irreproducible axis). Addressing the ESSENTIAL items (exact validated count; final DOIs; cleanup of internal artifacts; DESI injection–recovery or rewording; eROSITA/Gaia tiering) plus the listed MAJOR fixes will bring the paper into PRD methodological compliance.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P3-E8 (Totals/denominators; Table I rows “Total …” and “Path-C unique”; §III F; Table VI note †)
- Issue: The Path-C “Ntotal” summary (37,272,042) does not reflect the 2×10^5 native Planck patch bank actually used for the released tier (it still reflects the 20,000 cross-transfer bank), and the SDSS row mixes a native re-score selection (77,905 at S≥0.1060 on a 1,925,279-spectrum pool) with an Ntotal of 2,304,830 from the full DR18 input.
- Why it matters: Readers will assume Ntotal in the totals row encodes the true processed counts for the released catalog. Mixing cross-transfer inputs (Planck 20k) with native-release inputs (Planck 200k; SDSS 1.93M) in the same table/total obscures denominators and makes the rate column and the “Total Ntotal” hard to interpret.
- Required fix: Present two parallel denominator columns or two summary rows: (a) cross-transfer inputs (as-is), and (b) Path-C native processed inputs (update Planck to 200k; SDSS to 1.93M). In the “Path-C unique (primary)” total row, ensure Ntotal reflects the native inputs actually used in the released analysis. State explicitly which Ntotal is used for any rate shown.

P3-E9 (Planck rate presentation; Table I, §III F)
- Issue: The Planck “1.00%” rate in the main table reflects the cross-transfer 20k bank, whereas the released tier is the top-200 of a 200k native re-score (i.e., 0.10%). Although footnoted, the headline table cell will be read as the operative rate.
- Required fix: Show both rates clearly (e.g., “1.00% on 20k cross-transfer bank; 0.10% on 200k native bank”) or replace the table cell by “fixed-count 200/20k (cross-transfer) and 200/200k (native)” to avoid implying a measured detection rate.

MAJOR

P3-M10 (Numeric inconsistency; §III F vs. “Arithmetic checks” block)
- Issue: The Planck train/validation over-representation p-value is quoted as “≈4×10−4” in §III F, while the recomputation notes elsewhere give ≈1.9×10−4 (normal approximation) or ≈3.8×10−4 (two-sided). This is a small but visible inconsistency.
- Required fix: Pick one tail convention, recompute once, and carry the same number everywhere (with method stated: one- vs two-sided; exact vs normal approx).

P3-M11 (Mixed denominators within SDSS row; Table I and §III C)
- Issue: The SDSS row shows Ntotal = 2,304,830 (full DR18 input), but the 77,905 continuity slice is 4.05% of the 1,925,279-spectrum native re-score pool, not of 2,304,830; the rate shown (3.38%) corresponds to the cross-transfer selection, not the native continuity slice. This interleaves three denominator contexts in one row.
- Required fix: Add a compact subtable (or replace the single “Rate” cell) that lists, side-by-side, for SDSS: (i) cross-transfer S>5 (77,905/2,304,830 = 3.38%); (ii) native continuity slice (77,905/1,925,279 = 4.05%); (iii) native top-1% (19,253/1,925,279 = 1.00%); (iv) native S>5 (12/1,925,279). Make denominators explicit so no rate is read against the wrong N.

P3-M12 (PTA likelihood normalization/units; Appendix E, Eq. (E1))
- Issue: The reference frequency f_yr (1/yr) and the units of ρi are not explicitly defined in the main text around Eq. (E1). It is also not stated whether A is the dimensionless strain amplitude normalized at f_yr.
- Required fix: Define f_yr ≡ 1 yr−1, state the units/normalization of ρi and A, and reference the standard mapping to the characteristic strain spectrum used by ceffyl (or cite the exact convention from the NANOGrav product).

MINOR

P3-n10 (Consistency note; Table I and captions)
- Issue: Several cells blend “predetermined count” selections with percentages. Even though footnotes explain this, readers scanning the table can miss it.
- Fix: Where a row reflects a fixed-count/preset-percentile rather than a measured rate (Planck, Gaia, NEOWISE, eROSITA), prepend “fixed-count” or “preset-percentile” in the “Rate” cell or add a distinct column “Selection type” with values “fixed-count,” “preset-percentile,” or “data-driven.”

P3-n11 (Figure–body clarity; Fig. 11 vs. §V)
- Issue: The caption to Fig. 11 correctly notes the σ(fNL) normalization differs from §V, but §V references this figure indirectly (“shot-noise figure in Appendix C”) without an immediate reminder.
- Fix: Add a parenthetical in §V where the figure is invoked: “(normalization not directly comparable to §V; see Fig. 11 caption).”

P3-n12 (Symbol definition; §III F, Table VI note †)
- Issue: “KCMB” is used without first-definition in the main text.
- Fix: Define KCMB as Kelvin CMB temperature units at first mention.

P3-n13 (Precision formatting; §IV C, FoF audit)
- Issue: Reporting a maximum intra-cluster separation of “4.999″” reads like a formatting/rounding artifact.
- Fix: Round sensibly (“<5.0 arcsec”) or report with a standard uncertainty (e.g., to 0.1″) to avoid implying binary-threshold artifacts.

NIT

P3-c5 (Totals-row labeling)
- Suggestion: Label the two summary rows explicitly as “Cross-transfer baseline (inputs/counts)” and “Path-C native (unique objects; native inputs listed per row)” to prevent misinterpretation of which Ntotal applies where.

Explanation
These items address denominator/totals consistency (now that native Planck used 200k patches and SDSS native re-score used 1.93M spectra), a small but real p-value inconsistency, and missing PTA likelihood unit definitions. They were not covered in the initial report and materially improve clarity and methodological rigor without repeating earlier points.