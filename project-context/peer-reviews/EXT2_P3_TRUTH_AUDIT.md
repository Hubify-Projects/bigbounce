# EXT2 P3 Truth Audit — v3.1.89

**Paper:** paper3_anomaly_catalog · v3.1.89 · compiled 2026-06-10
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Gemini 3.5 Thinking (MINOR REVISIONS), Grok Heavy (MINOR REVISIONS)
**Mode:** EXT2 in-thread DELTA review (closure verification + fresh pass)
**Audit date:** 2026-06-10 · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.89) + `pipelines/p3_anomaly_engine/paper3_draft.pdf` (pdftotext spot checks) + on-disk artifacts

---

## Verdict Table — Fresh Findings

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| NB1 | ChatGPT | BLOCKER | Data-release score schema internally inconsistent: Data Availability promises "per-object canonical-$S$ scores" while eROSITA is membership-only (axis irreproducible) and Planck is ranked by raw per-patch MSE | **VERIFIED** | tex l.782 says "per-object canonical-$S$ scores" with no exception; l.284 declares the two exceptions globally; §III.E (l.471) + Table III caption (l.474) make eROSITA membership-only. The Data Availability sentence contradicts the released schema; no formal `score_axis`/`membership_only` schema table exists. Real catalog-product fix. |
| NB2 | ChatGPT | BLOCKER | Title "Native-Trained Novelty Fractions" (plural) unsupported — only one deep novelty measurement exists (DESI top-1,000, 17.8%) | **PARTIAL → HOUSTON-DECISION** | Title l.48 uses the plural; abstract (l.220) and §IV.A (l.525, l.704) scope 17.8% correctly as a single-sample point estimate and demote SIMBAD fractions to coverage diagnostics. The substance is fully disclosed; the title wording is a framing call. Default: retitle to singular ("…and a DESI Top-1,000 Archival-Novelty Estimate") or "Anomaly Fractions". |
| NM1 | ChatGPT | MAJOR | DESI "~73× like-for-like" benchmark is not like-for-like: 195,829 is the full 22.5M-spectrum scan incl. ~16M filler/sky-fiber/calibration spectra; Liang et al. is a science-target catalog | **VERIFIED** | "like-for-like" at l.220 (abstract) and l.758 (conclusions). l.372 confirms only ~6.5M of 22.5M carry validated TARGETTYPE and the 195,829 count "is not restricted to the validated-TARGETTYPE subset." Recompute on science-target subset or drop "like-for-like". |
| NM2 | ChatGPT | MAJOR | SDSS remains half native product, half cross-transfer diagnostic: UMAP/HDBSCAN clusters, cool-dwarf physical interpretation computed on the 77,905 cross-transfer set while the native slice is the released product | **VERIFIED** | l.422: "UMAP/HDBSCAN clustering of the full 77,905-object cross-transfer anomaly set… dominated by cool dwarfs (84%)" sits beside "the 77,905-object native continuity slice… supersedes the cross-transfer count." Astrophysical-category claims rest on the superseded scan. Either recompute clustering on the native slice or label the populations cross-transfer-diagnostic at each use. |
| NM3 | ChatGPT | MAJOR | "20 curated all-sky catalogs" list enumerates only 18 layers | **VERIFIED** | l.532 full enumeration: Gaia DR3, SDSS DR12, SDSS DR16, Legacy DR9, DES DR2, PS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS = **18**. Either list the missing 2 layers or correct to 18 and confirm the 17.8% denominator. |
| NM4 | ChatGPT | MAJOR | High-z QSO redshift provenance ambiguous: "pipeline-inferred" vs "photometric-pipeline estimates" for objects selected from DESI spectra | **VERIFIED** | l.415 "pipeline-inferred z=6.0–6.23 (spectroscopic confirmation required)"; l.417 "these redshifts are photometric-pipeline estimates." Which pipeline (Redrock Z/ZWARN/DELTACHI2 vs photometric vs custom line-fit) is never stated. Real reliability-relevant ambiguity. |
| NM5 | ChatGPT | MAJOR | "203 novel eROSITA X-ray sources" contradicts the paper's own novelty definition (novel ≡ SIMBAD-unmatched only) | **VERIFIED** | Phrase at l.471, l.527, l.773 while §IV.A (l.525) rules SIMBAD absence is "not discovery." Replace with "203 SIMBAD-unmatched eROSITA membership-list sources". |
| NM6 | ChatGPT | MAJOR | TARGETTYPE (target-selection) and Redrock SPECTYPE (spectral class) conflated | **VERIFIED** | l.372 defines validated TARGETTYPE = BGS/LRG/ELG/QSO/MWS; l.411 then says "validated TARGETTYPE classification ('GALAXY','QSO','STAR' from the Redrock pipeline)" — two different axes under one term. Split the language (and ideally the table). |
| NM7 | ChatGPT | MAJOR | Table IV caption "All ten items are closed" too strong — several entries are documented caveats, not closures | **VERIFIED (presentation)** | l.711 caption: "All ten items are closed (C = resolved in paper…)". Items like (c) fiber-nuisance and OOD behavior are bounds/caveats. Retitle "Residual caveats and current handling". |
| NM8 | ChatGPT | MAJOR | Appendix E deposits MCMC chain/fitter "in the companion data repository~[18]" — [18] is the NANOGrav data paper, not the project repo | **VERIFIED** | l.956: "Chain, posterior figure, and fitter script are deposited in the companion data repository~\cite{NANOGrav2023}." Wrong citation; point at the project DOI/GitHub artifact. |
| Gm1 | Gemini | MAJOR | Figure 9 caption says "3.8 < z < 5.0" for 40,192 tracers spanning bins from z=0.8 — "physically impossible clerical error" | **FALSIFIED** | tex l.666 reads "$0.8 < z < 5.0$" (in place since v3.1.81, commit ccb8e852) and the compiled PDF reads "0.8 < z < 5.0" (pdftotext check). Reviewer misread/hallucination. No edit needed. |
| Gm2 | Gemini | MAJOR | LAMOST denominator gap: Table I N_total 11,418,594 vs native re-score across 1.13×10⁷ (top-1% = 113,342 ⇒ pool 11,334,200); ~84k spectra unaccounted | **VERIFIED** | l.346 (11,418,594), l.339/l.359 ("113,342 of 1.13×10⁷"). No retrieval-failure/quality-cut disclosure for LAMOST, unlike SDSS (l.422 discloses 3,394 failed retrievals). Add one disclosure sentence + exact pool count. ChatGPT's minor #4 is the same gap (consensus). |
| Gm3 | Gemini | MINOR | Table I eROSITA N_anom reads "2988" and rate "0.03#" — "severe typo" | **FALSIFIED** | l.347 source: `298$^\S$ & 0.03$^\#$` — § and # are footnote markers, defined at l.359–364 (the # footnote is the eROSITA membership-only rate disclosure added in R29). Gemini's PDF extractor concatenated marker glyphs. No edit needed. |
| Gm4 | Gemini | MINOR | Appendix C broken fragment "Figure 11 ma maps the re- sulting" | **FALSIFIED** | tex l.886 "Figure~\ref{fig:shotnoise_sensitivity} maps the resulting"; compiled PDF reads "Figure 11 maps the resulting" (pdftotext l.2056). Extraction artifact. |
| Gk1 | Grok | MINOR | Abstract should lead with one clean catalog-grade sentence; downstream users quote the first number | **OPINION** | Abstract (l.220) already leads with the 269,317 catalog-grade tier (HD-7 applied at v3.1.89, commit dc3c6d84). Grok's exact-sentence suggestion is style polish; title still leads with 378,280 (see NB2/B1 Houston items). |
| Gk2 | Grok | MINOR | Table I footnote ♠ retains stale subtraction-arithmetic language ("earlier draft quoted 264,938/264,738…") | **VERIFIED (text) → HOUSTON-DECISION (disposition)** | l.365 retains the correction note. It is not stale bookkeeping — it is a deliberate correction-note per Houston's transparency policy (cf. EXT1 HD-6). Default: keep; optionally compress to one clause + JSON cross-ref. |
| Gk3 | Grok | MINOR | Dedup radius sweep + FoF chain audit should be cross-referenced from Table I footnote for reproducibility | **PARTIAL** | Sweep is in the body (§IV.C; 3″/5″/7″ → 378,604/378,280/378,145) with artifact cited; Table I footnote ¶ has no pointer. One-sentence footnote addition. |

## Verdict Table — Contested Closure Claims (PARTIAL/REGRESSION/NOT-ADDRESSED only)

| # | Reviewer claim | Audit verdict | Evidence |
|---|----------------|---------------|----------|
| B1 (ChatGPT: PARTIAL — "catalog-grade" still includes Gaia exploratory + eROSITA membership-only; title/conclusion foreground 378,280) | **PARTIAL, mostly HOUSTON-DECISION** | Abstract now leads with 269,317/269,117 (HD-7 done). Gaia retention in catalog-grade was ruled at EXT1 (HD-8 default: keep, with feature-column disclaimer — applied at l.782). Residual real item: tier *name* "catalog-grade" vs contents; title still 378,280. Houston call on rename vs keep. |
| B2 (ChatGPT: PARTIAL — 195,829 still full-scan count entering "point-source object detections"; no TARGETTYPE split table) | **VERIFIED residual** | l.372 discloses the scope choice but no TARGETTYPE breakdown table exists. This was already queued at EXT1 ("P3 F3: DESI TARGETTYPE split table — ~1 hr DR1 query"). Still not executed — now twice-flagged externally. DO-NOW. |
| B3 (ChatGPT: PARTIAL — Table I lists Planck 20,000 → 200 = 1.00% while native top-200 comes from the 200,000-patch bank) | **PARTIAL (re-raise of EXT1 F4 FALSIFIED, with a narrow new residual)** | EXT1 audited the denominator "inconsistency" as FALSIFIED (both numbers real, documented, l.491). The narrow new point — the Table I *rate cell* (l.348: 1.00) uses the cross-transfer denominator while the tier is native top-200 of 2×10⁵ — is genuine but already half-covered by the caption Note ("predetermined counts… should not be interpreted as measurements"). Either re-rate as 0.10% native or footnote the cell. |
| B5 (ChatGPT: PARTIAL — DOI not minted; manifest not in review sandbox; no one-command repro) | **PARTIAL → HOUSTON-DECISION (HD-11)** | `DATA_RELEASE_MANIFEST.md` exists on disk (5.4 KB, frozen pre-submission) and is cited at l.782; Zenodo DOI is deliberately mint-at-submission (EXT1 HD-11, Houston-ruled). Reviewer cannot see the repo — known reviewability limitation, not a new gap. One genuinely new sub-ask: a single reproduce-the-headline-counts command in the manifest. |
| B6 (ChatGPT: NOT ADDRESSED — v3.1.71 cross-vendor clean-round manifest absent from PDF) | **STALE re-raise** | EXT1 F6 verdicted OPINION/STALE: internal QA record (tex changelog l.211), not a manuscript requirement. Re-raised unchanged. No action. |
| M2 (ChatGPT: PARTIAL — "7-way positional deduplication" framing over a mixed point-source/map-patch population) | **OPINION re-raise (EXT1 F10)** | Stratification note (l.360) makes the 378,080 + 200 split exact and Planck contributes zero overlaps. The suggested "6-way FoF + 200 appended patches" phrasing is fine polish, not an error. |
| M3 (ChatGPT: PARTIAL — cosmology still prominent) | **HOUSTON-DECISION re-raise** | SPHEREx forecast is now conditional-labeled (l.680, l.748); de-biased null is in abstract. Placement (§V + App C scope) is a journal-targeting call (MNRAS vs PRD/JCAP). |
| M4 (ChatGPT: PARTIAL — App C still says even α=0.05 yields an improvement) | **VERIFIED residual** | l.851: "Even the most conservative plausible enhancement (α = 0.05) yields a…" — conflicts with the de-biased no-improvement framing despite the "Superseded" header (l.842–844). Delete/rewrite that sentence or add a positivity-form companion column. |
| M5 (ChatGPT: PARTIAL — NANOGrav still abstract/conclusion-level) | **HOUSTON-DECISION re-raise (EXT1 HD-9: keep in body)** | Environmental-SMBHB caveat now present at every site (l.220, l.683, l.748). Placement was Houston-ruled. |
| M7 (ChatGPT: PARTIAL — Gaia still inside catalog-grade 269,317) | **HOUSTON-DECISION (EXT1 HD-8 default applied)** | Houston ruled "keep with disclaimer" 2026-06-10. Re-raise without new evidence. |
| M9 (ChatGPT: PARTIAL — "establishing that the anomaly signal is not driven by Galactic foreground" too strong) | **VERIFIED residual** | l.564 still uses "establishing…" immediately before the necessary-but-not-sufficient caveat. Replace with "we find no first-order latitude or dust correlation within the surveyed footprints." |
| Gemini B1 (PARTIAL/REGRESSION — Table III still physically lists corrupted S_BigAE values) | **PARTIAL — no regression** | Table III (l.473–486) still prints S_BigAE 1.084…0.439, now under a bold "Do not use as a continuous science data product" caption. Values were always there; warnings were added (REGRESSION label wrong). Residual = EXT1 A1 hard-form option: strip the column (replace with committed-raw MSE or percentile rank). HOUSTON-DECISION: warned column vs removal; Gemini+ChatGPT(NB1) both push removal — 2-reviewer consensus favors strip. |
| Gemini B2 (PARTIAL — Table IV item (c) "fiber inert at σ=0.05" conflicts with §V.C "assumes zero observational systematics") | **PARTIAL** | l.680 states the zero-systematics assumption and the very next sentence summarizes the 4n+1 nuisance Fisher block; l.718 carries the fiber-specific |Δσ/σ|<0.01% bound. Not a contradiction (assumption + robustness bound), but §V.C never cites the fiber bound. One cross-reference clause closes it. |
| Grok closure rows (all CLOSED) | **CONFIRMED** | B1/B2/B3-Grok closures verified against l.220, l.471, l.360; Liang2023 now ApJ Lett. 956, L6, arXiv:2307.07664 (l.1040–1043) ✓; NEOWISE geometry-QA decomposition at every site ✓. |

## ChatGPT minors (quick verdicts)

| Item | Verdict |
|------|---------|
| Abstract length / audit-log style | OPINION (HD-2 family; shorten at journal submission) |
| Fig 2 embedded PNG title "all 319,443 anomalies across 8 archives" | PARTIAL — caption (l.328) correctly says cross-transfer baseline; the title string baked into the PNG needs figure regen to verify/fix |
| Ref [1] DESI DR1 "Astron. J. (accepted 2025)" | VERIFIED (l.991) — update bibliographic record before submission if final |
| "0% artifact rate" → report 0/200 + binomial UL | PARTIAL — l.376 already states the 0/200 method in full; add Wilson/binomial upper limit ("<1.5% at 95%") |
| Conclusion item 2: put 17.8% before 58.8% | PARTIAL — abstract fixed; conclusions/limitations (l.704) still introduce 58.8% first within item (6) |
| Conclusion item 5: tie "decisive" to circular-orbit reference everywhere | STALE — l.683, l.748, abstract all carry the tether |

---

## Consensus Findings (2+ reviewers)

1. **eROSITA S_BigAE column should be stripped from Table III** — Gemini B1 + ChatGPT NB1 (and EXT1 A1 hard option). The membership-only de-scope is complete in prose; the corrupted values still print.
2. **LAMOST denominator disclosure** — Gemini major Gm2 + ChatGPT minor #4. ~84k-spectrum gap between 11,418,594 and the 11.33M re-score pool is undisclosed.
3. **DESI non-science spectra in the headline count** — ChatGPT B2 + NM1 (same root cause). TARGETTYPE split table closes both.
4. **DOI minting** — all three (standing HD-11, submission-day).

## Action Plan (VERIFIED/PARTIAL, hardest first)

1. **DESI TARGETTYPE split table + like-for-like recompute (B2, NM1, NM6)** — run the queued DR1 query (~1 hr): break 195,829 by science TARGETTYPE (BGS/LRG/ELG/QSO/MWS) vs filler/sky/calibration; add table to §III.A; recompute the Liang benchmark on the science-target subset or drop "like-for-like" (l.220, l.758); separate TARGETTYPE vs Redrock SPECTYPE language (l.372, l.411). File: `pipelines/p3_anomaly_engine/paper3_draft.tex`.
2. **eROSITA Table III column strip (Gemini B1, NB1)** — replace the S_BigAE column with committed-raw MSE or empirical percentile rank (artifact `r24conf_erosita_axis_sweep.json` already carries the raw axis); keep the warning caption. l.473–486.
3. **Score-schema sentence in Data Availability (NB1)** — amend l.782: "per-object canonical-$S$ scores *where applicable* (DESI/SDSS/LAMOST/Gaia/NEOWISE); Planck is ranked by raw per-patch MSE; eROSITA is membership-only" + add the schema-flag table (score_axis / membership_only) to the release manifest.
4. **LAMOST denominator sentence (Gm2)** — state the exact re-score pool and why ~84k of 11,418,594 dropped (retrieval failures/quality cuts), §III.D + Table I footnote ♠. Mirror the SDSS disclosure pattern (l.422).
5. **Appendix E citation fix (NM8)** — l.956: cite the project repo/DOI, not [18].
6. **20-vs-18 catalog list (NM3)** — l.532: enumerate all 20 or correct to 18; verify the 17.8% denominator matches.
7. **High-z QSO redshift source (NM4)** — l.415–417: state Redrock Z/ZWARN/DELTACHI2 (or actual source) for the 12 candidates; reconcile "pipeline-inferred" vs "photometric-pipeline".
8. **"203 novel" → "203 SIMBAD-unmatched" (NM5)** — l.471, l.527, l.773.
9. **Foreground wording (M9)** — l.564: "establishing" → "we find no evidence for first-order latitude or dust correlation within the surveyed footprints."
10. **App C α=0.05 sentence (M4)** — l.851: delete or de-bias-qualify.
11. **Table IV caption (NM7)** — l.711: "Residual caveats and current handling."
12. **Minor batch** — Planck rate-cell footnote (B3 residual, l.348); fiber cross-ref clause in §V.C (Gemini B2, l.680); dedup-sweep footnote pointer (Gk3); 0/200 binomial UL (l.376); ref [1] record check (l.991); Fig 2 PNG title regen; conclusions 17.8-first ordering (l.704).

**HOUSTON-DECISION queue:** NB2 title wording; "catalog-grade" tier name + 378,280 in title (B1); correction-note retention (Gk2, HD-6 analog); Zenodo DOI timing (HD-11, ruled); NANOGrav/cosmology placement (M3/M5, HD-9 ruled).

---

## GAP METRIC

| Category | Count | Items |
|----------|-------|-------|
| (a) Genuinely new (neither EXT1 nor R29 caught) | **11** | NB1 (schema sentence), NB2 (title plurality), NM1 (73× like-for-like), NM2 (SDSS cross-transfer interpretation), NM3 (18-vs-20 list), NM4 (z provenance), NM5 ("203 novel"), NM6 (TARGETTYPE/SPECTYPE), NM7 (Table IV "closed"), NM8 (App E mis-cite), Gm2 (LAMOST denominator). Plus 3 new minors (ref [1] record, 0/200 binomial UL, Fig 2 PNG title). |
| (b) Re-raises of audited-FALSIFIED items | **1 strict** (B3 — EXT1 F4 FALSIFIED) **+ 2 re-raises of OPINION/STALE** (B6 — EXT1 F6; M2 — EXT1 F10) | All re-raised without new evidence except B3's narrow rate-cell residual. |
| (c) Closure-verification disputes | **3** | Gemini B1 "PARTIAL/REGRESSION" vs Grok "CLOSED" (audit: PARTIAL, no regression); ChatGPT B3 PARTIAL vs EXT1 FALSIFIED; ChatGPT B6 NOT-ADDRESSED vs EXT1 STALE. |
| Reviewer findings FALSIFIED this round | **3** | Gm1 (Fig 9 z-range), Gm3 (eROSITA "2988"), Gm4 ("ma maps") — all Gemini PDF-extraction/misread artifacts. |

**Internal-loop note:** the genuinely-new cluster is dominated by *cross-surface consistency* failures (Data Availability vs schema; title vs measured quantity; enumerated list vs claimed count; citation target vs deposited artifact). Internal rounds verify claims in place but do not diff claim-sites against each other. Add a "same-fact, all-sites" sweep to the internal checklist.

## Post-Audit Recommendation

**CONDITIONAL MINOR.** Grok/Gemini's MINOR is better calibrated than ChatGPT's MAJOR once the three FALSIFIED Gemini items and the five Houston-ruled re-raises are removed. The genuinely blocking work is small and concrete: the TARGETTYPE split query (~1 hr compute, twice-flagged), the Table III column strip, the schema sentence, and the LAMOST denominator sentence. Everything else is wording-level. No reanalysis of any headline number is required; the 378,280/269,317 arithmetic, Fisher positivity form, and NANOGrav numbers were re-verified clean by all three reviewers.

---

*Verdict counts (fresh + contested closures): VERIFIED 13 · PARTIAL 9 · OPINION/STALE 6 · FALSIFIED 3 · HOUSTON-DECISION 7 (several overlap PARTIAL).*
*Protocol: FALSIFIED = claim contradicted by current source/PDF · STALE = resolved pre-EXT2 · OPINION = editorial preference · HOUSTON-DECISION = framing choice with no single correct answer.*
