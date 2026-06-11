# EXT3 P3 Truth Audit — v3.1.91

**Paper:** paper3_anomaly_catalog · v3.1.91 · compiled 2026-06-11
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Gemini 3.5 Thinking (MAJOR REVISIONS — escalated from EXT2 MINOR), Grok Heavy (ACCEPT)
**Mode:** EXT3 in-thread DELTA review (closure verification + fresh pass)
**Audit date:** 2026-06-11 · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.91) + `site/public/papers/paper3_anomaly_catalog_v3.1.91.pdf` (spot extraction checks for artifact adjudication only) + EXT2_P3_TRUTH_AUDIT.md

---

## Verdict Table — Fresh Findings (EXT3)

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| FM1 | ChatGPT | MAJOR | Full-sample feature scaling (eROSITA/NEOWISE scalers fit on full sample; Gaia lineage-inferred) may leak tail information into anomaly rankings; paper asserts "affects validation MSE scale but not within-survey ranking" without proof | **VERIFIED (genuinely new)** | tex l.311 documents exactly this: column standardization "fit on the *full* 930K sample (not the training split)" (eROSITA), "robust median/IQR transform fit on the full sample" (NEOWISE, Gaia-lineage), then asserts no ranking effect. The assertion is unproven — per-column scale constants reweight feature contributions to MSE, so train-split-only refit *could* reorder tails. Bounded robustness check (Jaccard/rank-corr re-run) or soften the assertion to a stated assumption. Affected tiers: eROSITA (membership-only), NEOWISE, Gaia (exploratory) — not DESI/SDSS/LAMOST spectra. |
| FM2 | ChatGPT | MAJOR | Planck native top-200 may include training/validation patches; train/score disjointness never stated | **VERIFIED (genuinely new)** | l.527: the 2×10⁵-patch native bank is used "for training and re-scoring, with the Planck tier held at … 200 (the top-ranked patches of the native re-score)". No held-out statement anywhere. Standard AE-anomaly practice scores the full bank, but the disclosure ask is legitimate: state the overlap (or re-score a held-out bank). One-paragraph disclosure fix minimum. |
| FM3 | ChatGPT | MAJOR | §II.B still says eROSITA uses "a data-driven IsolationForest score-knee threshold" — contradicts §III.E (0.259 reproduced on *no* axis incl. IsolationForest; membership-only release) | **VERIFIED (genuinely new)** | l.326: "eROSITA uses a data-driven IsolationForest score-knee threshold" vs l.507: "0.259 is reproduced on neither the raw, the full-sample-standardized, nor the IsolationForest axes … membership list itself --- not any score axis --- is the committed, reproducible selection." Direct internal inconsistency the R31conf sweep missed (it fixed Table I's threshold-family text at l.375 but not the §II.B sentence). One-sentence fix per ChatGPT's proposed wording. |
| FM4 | ChatGPT | MAJOR | "DESI anomalies … pass every validation test" overreaches vs limitations (no independent architecture on DESI; full-scan count; recount queued); "stable DESI anomaly rate" inference premature | **VERIFIED (genuinely new, wording-level)** | l.731: "DESI anomalies (0.87%, multi-band, 0% artifact rate in top 200) pass every validation test" — contradicts limitation (1) at l.740 ("no independent method was applied to DESI, SDSS, or LAMOST") and the queued TARGETTYPE recount (l.256, l.408). Replace with the enumerated internal checks (k-fold, OOD Jaccard, top-200 visual). |
| Cm1 | ChatGPT | MINOR | Table III SIMBAD column value "Novel" perpetuates the ambiguity NM5 fixed in prose | **VERIFIED** | l.515–519 print "Novel" in the SIMBAD column; caption defines Novel = no SIMBAD 5″ counterpart, while §IV.A rules SIMBAD absence ≠ discovery. Rename cells to "No SIMBAD 5″ match"/"SIMBAD-unmatched". |
| Cm2 | ChatGPT | MINOR | Title "Native-Trained Novelty Fractions" (plural) | **HOUSTON-DECISION re-raise** | EXT2 NB2 verdict unchanged; title at l.46–48 unmodified. Re-raise without new evidence. Default fix on file (singular retitle). |
| Cm3 | ChatGPT | MINOR | Fig 2 embedded PNG title "all 319,443 anomalies across 8 archives" | **PARTIAL re-raise** | Known from EXT2 minors table: caption correct, baked-in PNG title string requires figure regen. Still pending. |
| Cm4 | ChatGPT | MINOR | Appendix C shot-noise paragraph mixes sign conventions ("+1.27% over" / "−4.97% vs") | **VERIFIED** | l.921–926: "σ_fNL = 12.56 (+1.27% over the baseline-multi 12.72)" — 12.56 < 12.72, so the "+" is an improvement-sign convention attached to a σ that *decreased*; "13.35 (−4.97% vs. baseline-multi)" — σ *increased*. Reads inverted. Rewrite as "σ decreases/increases by X%". |
| Cm5 | ChatGPT | MINOR | NANOGrav environmental caveat should add a targeted environmental-coupling/spectral-turnover SMBHB reference | **PARTIAL/OPINION** | l.721–722 already cites Sesana2016 + Burke-Spolaor2019 for the γ~2.5–3 flattening. Adding a targeted turnover reference (e.g. Kelley et al. 2017) is an enrichment, not a gap. |
| Gf1 | Gemini | BLOCKER-residual | "203 novel X-ray sources" still printed at §IV.A (p.11), §III.E (p.10), Data Availability (p.20) | **FALSIFIED** | tex l.507, l.563, l.809 all read "203 SIMBAD-unmatched eROSITA membership-list sources" (NM5 closure landed v3.1.90, changelog l.76–77). PDF extraction check: zero occurrences of "203 novel", two of "203 SIMBAD-unmatched". Gemini is quoting a stale/hallucinated state of the very PDF it reviewed. |
| Gf2 | Gemini | BLOCKER-residual | Table III still physically lists continuous S_BigAE values; purge the column | **HOUSTON-DECISION re-raise** | Identical to EXT2 Gemini B1 residual. Column retained *by design* under the bold "Do not use as a continuous science data product" caption (tab:erosita_top). EXT2 noted 2-reviewer consensus favors strip — still open in the HOUSTON queue, no new evidence this round. |
| Gf3 | Gemini | BLOCKER | Table IV item (c) "fiber inert at σ=0.05" contradicts §V.C "forecast assumes zero observational systematics" | **PARTIAL re-raise (severity over-called)** | l.716 (§V.C zero-systematics sentence) and l.754 (caveat (c) fiber bound) both still present; the EXT2-prescribed one-clause cross-reference in §V.C was in the EXT2 minor batch and was NOT applied in v3.1.90/91. Not a contradiction (stated idealization + robustness bound), but the clause fix remains legitimately open. MINOR-severity, not BLOCKER. |
| Gf4 | Gemini | MAJOR | Fig 9 caption says "3.8 < z < 5.0" — physically impossible vs plotted bins from z=0.8 | **AUTO-FALSIFIED (2nd raise of EXT2-FALSIFIED Gm1)** | tex l.702: "$0.8 < z < 5.0$"; PDF extraction: "0.8 < z < 5.0", zero hits for "3.8". FALSIFIED at EXT2 with commit provenance (in place since v3.1.81). Re-raised verbatim without new evidence → auto-FALSIFIED per protocol. |
| Gf5 | Gemini | MAJOR | LAMOST native pool truncation (~84,394 spectra) unquantified between 11,418,594 ingest and 1.13×10⁷ re-score pool | **STALE (closed in the very PDF reviewed)** | v3.1.91 changelog Gm2 closure: l.500 discloses "11,334,161 spectra of the 11,418,594 in DR10: the remaining 84,433 (0.74%) were lost to per-night tarball download failures and unreadable FITS extractions" + artifact `lamost_native/rescore_summary.json`; mirrored at Table I caption l.375 + footnote ‡ l.395. PDF contains "84,433" twice and "11,334,161". Gemini reviewed v3.1.91 and missed its own EXT2 finding's closure. |
| Gf6 | Gemini | MINOR | Table I eROSITA reads "2988" and "0.03#" — typos | **AUTO-FALSIFIED (2nd raise of EXT2-FALSIFIED Gm3)** | tex l.383: `298$^\S$ & 0.03$^\#$` — § and # are defined footnote markers (l.397, l.400). pdftotext renders them "298§"/"0.03#", proving the extractor concatenates marker glyphs. Re-raise of an EXT2-FALSIFIED extraction artifact → auto-FALSIFIED. |
| Gf7 | Gemini | MINOR | Appendix C stutter "Figure 11 ma maps the re- sulting" | **AUTO-FALSIFIED (2nd raise of EXT2-FALSIFIED Gm4)** | tex l.921: "Figure~\ref{fig:shotnoise_sensitivity} maps the resulting"; PDF: "maps the resulting", zero hits for "ma maps". Extraction artifact, re-raised → auto-FALSIFIED. |
| Gk1 | Grok | MINOR | Abstract "~73× … (not a like-for-like comparison)" phrasing awkward / mis-parsable | **OPINION** | l.256 carries the v3.1.91 NM1 fix verbatim; Grok's rewrite is style polish on a correct sentence. |
| Gk2 | Grok | MINOR | Table I footnote ♠ retains the stale "earlier draft quoted 264,938/264,738" correction-note sentence | **HOUSTON-DECISION re-raise** | Same as EXT2 Gk2: deliberate correction-note retention per Houston transparency policy (HD-6 analog). Note the sentence now also appears in the abstract provenance parenthetical (l.256). Default: keep; optional compress. |

## Verdict Table — Contested Closure Claims (ChatGPT PARTIAL/NOT-ADDRESSED rows)

| # | ChatGPT claim | Audit verdict | Evidence |
|---|----------------|---------------|----------|
| B1 PARTIAL (catalog-grade still contains Gaia + eROSITA; title still 378,280) | **HOUSTON-DECISION re-raise** | Factually accurate description, but Gaia retention = EXT1 HD-8 (Houston-ruled keep-with-disclaimer); title framing = EXT2 NB2/B1 HOUSTON queue. No new evidence. |
| B2 PARTIAL (DESI headline = full 22.5M scan; recount queued) | **VERIFIED residual — now THRICE-flagged** | l.408 + l.256 disclose the scope and the queued TARGETTYPE-restricted recount. The ~1 hr DR1 query has been queued since EXT1, flagged at EXT1, EXT2, EXT3. The disclosed-scoping is honest, but the recount itself is the single largest substantive residual. DO-NOW. |
| B3 PARTIAL (Table I Planck 20,000 → 200 = 1.00% bookkeeping rate) | **PARTIAL re-raise** | l.384 unchanged; EXT2 B3 narrow residual (re-rate as 0.10% native or footnote the cell) was minor-batch and not applied in v3.1.90/91. Caption Note (predetermined counts) half-covers it. Still open, minor. |
| B5 PARTIAL (DOI not minted; artifacts not in sandbox) | **HOUSTON-DECISION (HD-11, ruled)** | Zenodo DOI is deliberately mint-at-submission. Manifest + schema-flag table added v3.1.91 (changelog NB1). Known reviewability limitation. |
| B6 NOT ADDRESSED (v3.1.71 clean-round manifest absent from PDF) | **STALE re-raise (3rd)** | Twice ruled OPINION/STALE (EXT1 F6, EXT2 B6): internal QA record, not a manuscript requirement. No action. |
| M1 PARTIAL (Table I structurally confusing) | **OPINION** | Footnote apparatus is now complete and honest (ChatGPT concedes); residual is layout taste. |
| M2 PARTIAL ("7-way dedup" framing) | **OPINION re-raise (EXT1 F10)** | Stratification note makes the 378,080+200 split exact; suggested "6-way FoF + appended patches" is polish. |
| M3/M5 PARTIAL (cosmology/NANOGrav prominence) | **HOUSTON-DECISION re-raise (HD-9 ruled)** | Caveats now at every site (l.721–722, l.784, l.802, abstract). Placement is a journal-targeting call. |
| M7 PARTIAL (Gaia in catalog-grade) | **HOUSTON-DECISION re-raise (HD-8 ruled)** | Same as B1. |
| NB2 PARTIAL (title plural) | **HOUSTON-DECISION re-raise** | See Cm2. |
| NM2 PARTIAL (SDSS categories rest on cross-transfer set) | **PARTIAL** | l.458 labels the UMAP/HDBSCAN input as "the full 77,905-object cross-transfer anomaly set", so the diagnostic framing is present at the computation site; the cool-dwarf physical-category narrative still leans on it. Residual = label at each downstream use or recompute on the native slice. |
| NM5 PARTIAL (Table III "Novel" column value) | **VERIFIED residual** | Same as Cm1 — prose fixed at all 3 sites, table cells not. |
| All ChatGPT CLOSED rows (B4, M4, M6, M8–M11, NB1, NM1, NM3, NM4, NM6–NM8) | **CONFIRMED** | Cross-checked against v3.1.90/91 changelogs + tex: eROSITA membership-only (l.507), App C superseded label, 2+1 injection split (abstract l.256), 18 catalogs (l.561, l.568), Redrock provenance, schema sentence — all verified in place. |

## Grok ACCEPT — over-crediting check

Grok's per-item closure table is **accurate** (spot-checked: "203 SIMBAD-unmatched … at every occurrence" ✓ l.507/563/809; abstract leads with 269,317 ✓ l.256; LAMOST denominator 11,334,161 disclosed ✓ l.375/500; like-for-like scope note ✓ l.256; Redrock/TARGETTYPE split ✓ l.447). **However**, "No new majors… all reproducibility, tiering, and over-claim issues are resolved" over-credits the fresh pass: Grok missed FM3 (a real internal inconsistency at l.326 — same document, two incompatible eROSITA threshold descriptions), FM1/FM2 (real disclosure/robustness gaps in the preprocessing paragraph it never audited), FM4 ("every validation test"), and the still-queued TARGETTYPE recount that the paper itself labels open. ACCEPT is defensible only modulo those; calibrated reading = minor revisions.

## Consensus

1. **No reviewer raised a new BLOCKER.** ChatGPT explicitly: "No wholly new blockers." Gemini: "None identified." Grok: none.
2. **Gemini's MINOR→MAJOR escalation is unsupported.** Its editorial verdict ("author's editorial pass failed to execute several intended text changes") rests on 5 load-bearing claims: 203-novel residual (FALSIFIED), Fig 9 z-range (auto-FALSIFIED, 2nd raise), "2988"/"0.03#" (auto-FALSIFIED, 2nd raise), "ma maps" (auto-FALSIFIED, 2nd raise), LAMOST gap (STALE — closed in the reviewed PDF). Surviving content: S_BigAE column (HOUSTON re-raise) + fiber cross-ref clause (real, minor). Effective Gemini severity ≈ MINOR.
3. **ChatGPT residual blocker-class set, de-duplicated:** DESI TARGETTYPE recount (thrice-flagged, queued, ~1 hr) — the only remaining substantive catalogue-definition item not Houston-ruled. Everything else fresh is FM1/FM2 robustness-disclosure + sentence-level fixes.
4. **2-reviewer overlap:** Table III eROSITA column (ChatGPT Cm1 "Novel" relabel + Gemini Gf2 strip + EXT2 consensus) — the column should be stripped or relabeled in one edit.

## Action Plan (VERIFIED/PARTIAL, hardest first)

1. **DESI TARGETTYPE-restricted recount (B2 — thrice-flagged)** — run the queued ~1 hr DR1 query; add the science-target split/recount to §III.A and reconcile the 73× benchmark sentence (l.256, l.408). File: `pipelines/p3_anomaly_engine/paper3_draft.tex` + new artifact JSON.
2. **FM1 scaler-robustness check** — refit eROSITA/NEOWISE scalers on training split only (scripts at `pipelines/p3_anomaly_engine/recovered_pod_scripts/`); report top-298/top-1% Jaccard + Spearman vs published; add one results sentence at l.311 (or soften the no-ranking-effect assertion to a stated assumption with this test queued).
3. **FM2 Planck train/score disjointness** — state whether the released top-200 intersects the native training split (l.527); report the overlap count; if material, re-score a held-out bank.
4. **FM3 §II.B eROSITA sentence** — l.326: replace "data-driven IsolationForest score-knee threshold" with the membership-only fixed top-298 framing (ChatGPT's wording is correct as drafted).
5. **FM4 validation-language fix** — l.731: "pass every validation test" → enumerate (5-fold Jaccard, OOD, top-200 visual); drop/condition the stable-rate inference.
6. **Table III edit (Cm1 + Gf2 consensus)** — relabel "Novel" cells → "No SIMBAD 5″ match"; execute the Houston-queued S_BigAE column strip decision in the same edit (l.515–519).
7. **§V.C fiber cross-ref clause (Gf3, EXT2 carryover)** — l.716: append "; the fiber-assignment axis is bounded by the nuisance-Fisher block at |Δσ/σ|<0.01% (Table VI(c))".
8. **App C sign-convention rewrite (Cm4)** — l.923–925.
9. **Planck rate-cell footnote (B3 residual, EXT2 carryover)** — l.384.
10. **Minor batch** — Fig 2 PNG title regen (Cm3); NM2 downstream labels (l.458 narrative); optional targeted SMBHB turnover citation (Cm5).

**HOUSTON-DECISION queue (unchanged + 1):** title plural/378,280 (NB2/B1); Gaia in catalog-grade (HD-8, ruled); S_BigAE column strip (now 3-reviewer/2-round consensus to strip — recommend ruling YES and folding into item 6); correction-note retention (HD-6/Gk2, ruled keep); DOI timing (HD-11, ruled); cosmology/NANOGrav placement (HD-9, ruled).

---

## GAP METRIC

| Category | Count | Items |
|----------|-------|-------|
| (a) Genuinely new vs EXT2 | **5** (all ChatGPT) | FM1 (scaler leakage), FM2 (Planck train/score disjointness), FM3 (§II.B vs §III.E inconsistency), FM4 ("every validation test"), Cm4 (App C signs). EXT2 baseline was 11 genuinely-new → **55% shrink**; Gemini and Grok contributed **zero** genuinely-new findings this round. |
| (b) Re-raises | **Gemini 6** (Gf4/Gf6/Gf7 of EXT2-FALSIFIED = auto-FALSIFIED; Gf1 of a CLOSED item; Gf2/Gf3 of HOUSTON/PARTIAL) · **ChatGPT ~10** closure-row re-raises of HOUSTON/STALE/OPINION rulings (B1, B5, B6, M1, M2, M3, M5, M7, NB2, Cm2) + 4 legitimate open-residual re-raises (B2, B3, NM2, NM5) · **Grok 1** (Gk2, HOUSTON-ruled) |
| (c) Policy residue | **6** | DOI mint-at-submission (HD-11); title wording (NB2/B1); Gaia tier membership (HD-8); NANOGrav/cosmology placement (HD-9); correction-note retention (HD-6); v3.1.71 QA manifest (not a manuscript artifact). |
| Reviewer findings FALSIFIED this round | **4** (all Gemini) | Gf1, Gf4, Gf6, Gf7 — three are *second* raises of EXT2-FALSIFIED extraction artifacts; one (Gf1) misreports the reviewed PDF's own text. Plus 1 STALE (Gf5, closed in-PDF). Gemini's entire escalation rationale is falsified. |

**Internal-loop note:** R31conf fixed the Table I threshold-family text but missed the equivalent §II.B sentence (FM3) — same-fact-all-sites sweeps must include the methods prose, not just tables/abstract. Also: preprocessing-paragraph assertions ("does not affect ranking") need an evidence-or-assumption tag in internal review.

## EXIT-CRITERION ASSESSMENT

**Not yet externally clean, but one bounded wave from it.** Modulo HOUSTON-DECISION + policy residue, the substantive residual set is: the thrice-flagged DESI TARGETTYPE recount (~1 hr compute), two bounded robustness/disclosure checks (FM1, FM2), and five sentence/table-level edits (FM3, FM4, Cm1/Gf2, Gf3 clause, B3 footnote, Cm4). **No new blockers from any reviewer; no headline number, Fisher form, or NANOGrav statistic was challenged — all three re-verified the arithmetic clean.** Grok is at ACCEPT; Gemini's MAJOR is falsified down to ≈MINOR; ChatGPT's MAJOR reduces, after removing Houston-ruled and stale re-raises, to the recount + FM1–FM4. Clear EXT4 expectation: with the recount executed and FM1–FM4 landed, the remaining external surface is policy-only.

---

*Verdict counts (fresh + contested closures): VERIFIED 8 · PARTIAL 6 · OPINION/STALE 6 · FALSIFIED 4 (+1 STALE-closed) · HOUSTON-DECISION 9 (incl. re-raises).*
*Protocol: FALSIFIED = claim contradicted by current source/PDF · AUTO-FALSIFIED = re-raise of a previously-FALSIFIED claim without new evidence · STALE = resolved before/in the reviewed version · OPINION = editorial preference · HOUSTON-DECISION = framing choice with no single correct answer.*
