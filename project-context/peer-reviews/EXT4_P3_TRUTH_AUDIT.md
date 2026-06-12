# EXT4 P3 — Truth Audit

**Round**: EXT4 (true-external native-PDF, 3 vendors via in-thread project chats: ChatGPT Pro Extended · Grok Heavy · Gemini Thinking) · **Paper version reviewed**: v3.1.95 (md5 799d13fc, 28pp) · **Current tex**: v3.1.96 (adds FM1 eROSITA scaler-refit result computed 2026-06-11; was queued at v3.1.95 review snapshot)
**Date**: 2026-06-11 PT
**Recommendations**: ChatGPT MAJOR · Grok ACCEPT · Gemini MAJOR

## Verdict legend
VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION

## Findings table

| # | Leg | Finding | Verdict | Evidence (tex lines / artifacts) | Disposition |
|---|-----|---------|---------|----------------------------------|-------------|
| 1 | ChatGPT FB1 | **DESI recount must propagate through downstream DESI rates, novelty, QSO-candidate cosmology, and source/object vocabulary** | **PARTIAL (close-the-gap, multi-site)** | See per-site sub-audit immediately below this table | Close at multiple sites; one new scope-qualifier sentence per genuine downstream rate site |
| 1a | ChatGPT FB1 (per-class rates) | "galaxies anomalous at ∼20× rate of QSOs (0.75% vs 0.037%)" needs recount qualifier | **ALREADY-QUALIFIED → CLOSE NOW (one-line strengthen)** | L555 — denominator named ("∼6.5M validated-TARGETTYPE subset, BGS/LRG/ELG/QSO/MWS"), 16M filler explicitly excluded; SPECTYPE vs TARGETTYPE distinction stated | Add cross-reference to §III.A recount table: "(this validated-TARGETTYPE breakdown does not contradict the science-class recount of \S\ref{sec:desi}; the ∼6.5M denominator here is the BGS/LRG/ELG/QSO/MWS bitmask subset, distinct from the broader 20.3M science-class denominator of Table~\ref{tab:recount}.)" |
| 1b | ChatGPT FB1 (12 high-z QSO candidates) | "Applying these three cuts to the full 195{,}829 DESI anomaly catalog yields 12 candidates" — should propagate recount | **ALREADY-QUALIFIED for the SAMPLE; PARTIAL for the PROVENANCE flag** | L559 — Redrock template-fit caveat is stated verbatim ("spectroscopic-pipeline template fits at low continuum S/N, not photometric estimates, and independent confirmation by visual inspection or re-observation is still required"); the 12 are drawn from anomaly catalog as a top-cut, target-class agnostic by design | Add one inline pointer: "(the 12-candidate cut operates on the anomaly score and Z-arm dominance regardless of TARGETTYPE; per the recount of \S\ref{sec:desi} the parent 195{,}829 includes non-primary-class spectra.)" |
| 1c | ChatGPT FB1 (5,384 QSO-candidate cosmology sample) | "f_NL result on 5,384 QSO-candidate sample" needs recount propagation or de-scope | **PARTIAL → CLOSE NOW** | L339, L792, L821 — sample defined as $5{,}384$ QSO-candidate sample with GOLD ($W_1-W_2>1.0$, $S>10$, no Gaia parallax) + SILVER ($W_1-W_2>0.8$, $S>7$) tier definitions; no current sentence flags that the parent stream is full-spectra-stream rather than science-target-stream | Add one disclosure sentence at §V.A intro: "The 5{,}384-object QSO-candidate sample is drawn from the full DESI anomaly catalog by joint NEOWISE color + anomaly-score + Gaia-parallax cuts and is therefore well-defined irrespective of DESI TARGETTYPE bits; the recount of \S\ref{sec:desi} affects the *parent population framing* but not the selection function of this sample." |
| 1d | ChatGPT FB1 (Conclusion item 5 + §VII intro) | Conclusion "Cosmological applications" item should carry the recount caveat once | **ALREADY-PRESENT in §I + §III.A + §VI.E + abstract** | L910 (Conclusion item 5) is the bare numerical result; recount caveat already in abstract (L339), §III.A (L492), §VI.E (L887) | OPINION — repetition would be redundant; not a closure-grade ask |
| 1e | ChatGPT FB2 (source/object vocabulary, title) | Title still says "37.3 Million Sources and Map Patches"; should be "Spectra, Sources, and Map Patches" | **OPINION (Houston-default decision class)** | L46-47 title; the 378{,}080 point-source stratum is itself a real point-source count (185k SDSS native + LAMOST native + Gaia + NEOWISE + eROSITA + DESI), and Table I row 1 names DESI's $N_{\rm total}$ as "spectra" already (L463 "Optical spec."); body L358 says "spectra, sources, and map patches" semantics in inverse order | Houston-decision — title change is a submission-day call; not a referee-blocker on its own |
| 2 | ChatGPT B1 | "Catalog-grade" tier still mixes Gaia (training-sample-conditioned) + eROSITA (membership-only) | **OPINION (re-raise of prior round)** | Both surveys are explicitly footnoted as exploratory/membership-only at L480-481 (footnote $^\S$) and abstract L339; tier name is the disclosed framing | No edit; FM95-1 maps to same item |
| 3 | ChatGPT B3 | Table I Planck 20{,}000 → 200 = 1.00% structurally confusing despite footnote | **OPINION** | L458-485 caption rescues; footnote chain is the disclosed framing | No edit |
| 4 | ChatGPT B5/FM95-3 | DOI placeholder + Zenodo to-be-minted | **HOUSTON-DECISION (HD-11, ruled multi-round)** | L926 "DOI inserted at submission" | No edit; submission-day call |
| 5 | ChatGPT B6 | "v3.1.71 cross-vendor clean-round" not in PDF text | **OPINION (out-of-scope)** | Internal QA artifact; not a manuscript deliverable per Houston's standing framing | No edit |
| 6 | ChatGPT M1 | Table I still too dense | **OPINION (re-raise; pattern-052 STALE class)** | Deliberate post-R23-R31 design choice (single audited table); R32conf row 7 = OPINION | No edit |
| 7 | ChatGPT M2 | Method should be "6-way point-source FoF + appended Planck map-patch tier" | **OPINION** | L479 + L729 already state the stratification is exact and Planck contributes zero positional overlaps | No edit |
| 8 | ChatGPT FM1 | Full-sample scaling robustness "queued, not closed" | **STALE-AT-EXT4 / VERIFIED-IN-v3.1.96** | v3.1.95 said queued (the version the referee saw); v3.1.96 line 394 now reports the FM1 result inline ("retraining the production architecture under identical seeds with the scaler fit on the training split alone vs.\ the full sample gives top-298 membership overlap $257/298$ (Jaccard $0.76$), top-$1\%$ Jaccard $0.64$, full-catalog Spearman $\rho = 0.94$; … scaler-fit effect is at or below the model-retrain reproducibility floor"); artifact `ext3_fm1_erosita_scaler_refit.json` committed 2026-06-11 15:42 | No edit; finding resolved by v3.1.96 |
| 9 | ChatGPT FM95-4 | Front-load the recount warning in §VI.E DESI-vs-Liang comparison | **VERIFIED → CLOSE NOW (one-line reorder)** | L887 currently: "Our DESI anomaly rate of 0.87% is numerically close to the 1.07% rate of Liang \etal\ … but the science-class-restricted recount … shows the two rates are measured on different populations"; the "but" comes mid-sentence | Lead-clause reorder: open with "The science-class-restricted recount of \S\ref{sec:desi} shows our DESI $0.87\%$ rate and Liang \etal's $1.07\%$ rate are measured on different populations …" |
| 10 | ChatGPT minor (Table V row d) | "$B_{\rm mb/SMBHB}=7.14\times 10^3$ decisive" → add "only vs.\ idealized circular-orbit SMBHB" inline in the row | **PARTIAL → CLOSE NOW (one-line)** | Table V caveat row (c) is "Fisher fiber"; row (d) is the SMBHB Bayes factor; abstract + §V.A both carry "decisive only against the idealized circular-orbit SMBHB reference" verbatim; one-row tightening is mechanical | Add "(only vs.\ idealized circular-orbit SMBHB; see \S\ref{sec:nanograv})" to the Bayes-factor table row |
| 11 | ChatGPT minor (Conclusion item 2 ordering) | Lead with 17.8% genuine novelty, not 58.8% SIMBAD-unmatched | **PARTIAL → CLOSE NOW (one-line reorder)** | L904 Conclusion item 2: currently "58.8% SIMBAD-unmatched … genuine novelty fraction $\sim\!17.8\%$" | Swap order to lead with 17.8% genuine novelty; preserve the 58.8% pooled number after |
| 12 | ChatGPT minor (§III.A 0% artifact) | "0% artifact rate" → "0/200 visually flagged; binomial upper limit …" | **PARTIAL → CLOSE NOW (one-line)** | L887 already has the "(0% artifact rate in top 200)" parenthetical | Tighten to "$0/200$ visually flagged; binomial upper limit $\leq 1.5\%$ at 95\% CL" |
| 13 | ChatGPT minor (Fig 1 / §II.A force-include) | Main-text "concentrate" should clarify the 83 are visual markers, not unbiased density evidence | **PARTIAL → CLOSE NOW (one-line)** | L372 — caption discloses force-inclusion; main-text "concentrate" reads as density claim | Add "(the $83$ overplotted stars are a force-included display set, not an unbiased density test)" to the main-text sentence |
| 14 | ChatGPT minor (Table I footnotes too long) | Move long threshold/tiering explanation to a schema table | **OPINION** | Deliberate single-table design | No edit |
| 15 | ChatGPT minor (§V.A NANOGrav row) | Table V row + Conclusion should consistently say "not a cosmological detection" | **PARTIAL → CLOSE NOW (one-line)** | L910 conclusion item 5 says "decisive only vs. circular-orbit SMBHB reference" but does not append "and is not a cosmological detection"; abstract has it verbatim | Append "(not a cosmological detection)" to conclusion item 5 SMBHB clause |
| 16 | Grok M1 | "Stale arithmetic 264,938 / 264,738 from headline-minus-LAMOST sentence" should be excised | **PARTIAL → CLOSE NOW (correction-note class HOUSTON-DECISION HD-6 KEEP applies; but the sentence is bloating the abstract)** | L339 abstract carries the parenthetical "(an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic, which double-removes the 4,379 LAMOST detections that merge into catalog-grade clusters at 5″)"; L485 Table I footnote ♠ carries the same | Per HD-6 standing rule (correction-note retention until submission-day call): KEEP in v3.1.96 internal; flag as submission-day excise candidate in the closure ledger. The retention is by-design, not a finding. |
| 17 | Gemini B1 | "Replace 'novel' with 'SIMBAD-unmatched' at three lingering p.10/11/20 locations" + "purge S_BigAE column from Table III" | **FALSIFIED** | tex grep for "203 novel" / "novel X-ray" / "novel eROSITA" returns ONLY pre-history comment lines (L94, L159, L160 — version-history `%` comments, not body content). All three active sites L615, L671, L917 read "203 SIMBAD-unmatched eROSITA membership-list sources" verbatim. Table III in Gemini's count = `tab:erosita_top` (L617-630) — the rendered table has columns Rank / IAU Name / $S_{\rm IF,raw}$ / Dec / SIMBAD; **no $S_{\rm BigAE}$ column is present** (stripped in v3.1.94 per R32conf row 4). The "1.084, 0.815" values Gemini quotes are not in the current rendered table. Gemini is reviewing stale-version content or extraction artifacts. | No edit |
| 18 | Gemini B2 | "Table IV row (c) says fiber inert at σ=0.05 but §V C still says 'forecast assumes zero observational systematics'" | **FALSIFIED** | L823-824 §V.C reads in full: "The forecast assumes zero observational systematics (fiber-assignment, photo-$z$, foreground); the fiber-assignment axis is bounded by the nuisance-Fisher block at $\|\Delta\sigma/\sigma\| < 0.01\%$ at $\sigma_{\delta_{\rm fiber}} = 0.05$ (Table~\ref{tab:caveats}~(c))." The cross-reference to caveat (c) AND the explicit quantitative bound at σ=0.05 are both already in §V.C. There is no contradiction. | No edit |
| 19 | Gemini M (Fig 9 caption) | "Caption text says '3.8 < z < 5.0' but left panel plots bins from z=0.8 down" | **FALSIFIED (already-fixed in v3.1.94)** | L810 Fig 9 caption reads "redshift-binned DESI anomaly subsample over $0.8 < z < 5.0$" — Gemini's quoted "3.8 < z < 5.0" is a stale-PDF / OCR misread. R32conf row 16 closed the Fig 9 caption rewrite in v3.1.94. | No edit |
| 20 | Gemini M (LAMOST sample truncation transparency) | "11,418,594 vs 1.13×10^7 baseline leaves unquantified ~84,394 gap" | **FALSIFIED (already-disclosed)** | L478 Table I footnote ‡ AND L485 footnote ♠ AND L608 §III.D body all state explicitly: "re-score pool $11{,}334{,}161$ spectra of $11{,}418{,}594$; $84{,}433$ ($0.74\%$) lost to per-night tarball download failures and unreadable FITS extractions during the shard-wise re-score; exact counts in `pipelines/p3_anomaly_engine/lamost_native/rescore_summary.json`." The gap is named, quantified ($84{,}433$, not $84{,}394$ — Gemini's arithmetic from the rounded $1.13\times 10^7$), source-attributed, and artifact-cited. | No edit |
| 21 | Gemini minor (Table I 2988 / 0.03#) | "eROSITA row reads N_anom='2988' and Rate='0.03#'" | **FALSIFIED (PDF extraction artifact)** | L466 tex reads exactly: `eROSITA DR1   & X-ray phot.    &    930{,}203   &      298$^\S$  & 0.03$^\#$ & 68        \\`. The "2988" Gemini cites = `298` with the footnote `^\S` flattened by PDF extraction. The "0.03#" Gemini cites = `0.03$^\#$` with the footnote symbol mis-rendered. Same superscript-flattening class as the perennial $F_0 = 1/8.98^2 \to 1/8.982$ misread. Pattern-052 auto-falsify (re-raise of a class falsified ≥4 rounds running with primary tex evidence). | No edit |
| 22 | Gemini minor (Appendix C "ma maps") | "Figure 11 ma maps the re-sulting..." typo | **FALSIFIED (PDF extraction artifact)** | L1029 tex reads `Figure~\ref{fig:shotnoise_sensitivity} maps the resulting`. There is no doubled "ma" syllable in source. The "ma ma" string is a PDF text-extraction layout-flow stutter; pdftotext (or Gemini's OCR pipeline) is breaking a hyphenated/justified line. | No edit |
| 23 | Grok ACCEPT (with single polish) | "Stale 264,938 / 264,738 sentence in abstract + Table I footnote" | **Duplicate of #16** | See #16 — HD-6 KEEP; flag submission-day | No edit |
| 24 | All three legs | F₀ dimensional error / "1/8.982" / extraction-flattening complaints | **N/A this round** | None of the three EXT4 legs raised this perennial extraction-artifact complaint, confirming the v3.1.94 prophylactic `$F_0 = 1/8.98^2 = 0.01239$` numeric expansion (R33conf row 3) is killing the class permanently | — |

## Per-site sub-audit for ChatGPT FB1 (recount propagation)

ChatGPT named five specific downstream sites in FB1. For each, the verdict + line citation:

| Site | Reads-as-bare or qualified? | Verdict | Action |
|------|------------------------------|---------|--------|
| Per-class rates (galaxies 0.75% vs QSO 0.037%) §III.A L555 | Qualified — denominator named (∼6.5M validated TARGETTYPE) + 16M filler excluded explicitly + SPECTYPE/TARGETTYPE axis disambiguation | ALREADY-QUALIFIED | One-line cross-ref to Table~recount adds completeness (#1a) |
| Top-10,000 DESI novelty estimate §IV.A | Qualified at the abstract + §IV.A: stated as "top-$1{,}000$ score stratum", Wilson CI, "full-catalog rate empirically untested" (L339, L904) | ALREADY-QUALIFIED | No edit needed (the 17.8% never claimed to be science-target-restricted) |
| Top-200 artifact audit §III.A | Already framed as visual-inspection of top-200 anomalies; the $0/200$ count is a property of the top-200 list, not a science-class claim | ALREADY-QUALIFIED | #12 binomial-CL one-liner sharpens |
| 12 high-z QSO candidates §III.B L559 | Provenance qualifier exists ("Redrock template-fit at low continuum S/N, independent confirmation required"); parent-population recount qualifier does not | PARTIAL | Add one inline pointer (#1b) |
| 5,384 QSO-candidate cosmology sample §V.A | Sample-construction details fully disclosed (W1-W2 cuts, S thresholds, no-Gaia-parallax) but the parent-population recount caveat is NOT cross-referenced at this site | PARTIAL | Add one disclosure sentence (#1c) |

**Net call on ChatGPT FB1**: PARTIAL. The recount is correctly propagated at the headline level (abstract + §III.A + §VI.E + Conclusion), correctly absent where the downstream selection is target-class agnostic by construction (per-class rates, 12 high-z, 5,384 QSO-candidate), and warrants 3 one-line cross-reference adds to close the gap completely.

## Counts summary

- **Total findings audited**: 24
- **VERIFIED / PARTIAL (closure-actionable)**: 7 (rows 1a, 1b, 1c, 9, 10, 11, 12, 13, 15 — multiple sub-items in row 1)
- **FALSIFIED**: 6 (rows 17, 18, 19, 20, 21, 22 — all Gemini "MAJOR" + Gemini minors; entirely stale-PDF / extraction-artifact / version-skew misreads)
- **OPINION (re-raise / design choice / out-of-scope)**: 6 (rows 2, 3, 5, 6, 7, 14)
- **STALE-AT-EXT4 / VERIFIED-IN-v3.1.96**: 1 (row 8 = ChatGPT FM1)
- **HOUSTON-DECISION ruled classes**: 2 (rows 4 = HD-11 DOI, 16/23 = HD-6 correction-note KEEP)

**Genuinely-NEW substantive findings for the gap metric**: **2**
   - ChatGPT FB1 (recount propagation to 12 high-z QSO + 5,384 QSO-candidate sites; the abstract+§III.A+§VI.E sites were already-propagated)
   - ChatGPT FM95-4 (front-load the recount warning in §VI.E lead clause)

   The 5 closure-actionable "minor" rows (10, 11, 12, 13, 15) are polish on items already present in scope, not new substantive findings. Grok found zero new findings (single polish item is HD-6 ruled). All 6 Gemini findings are falsified on tex primary evidence.

## Round outcome

- 2 NEW substantive findings → recount-propagation gap is real but small and 1-line-each closable
- 0 arithmetic errors; 0 closure-introduced regressions vs R33conf v3.1.94 closures
- Gemini leg is operating on PDF-extraction artifacts and stale version content for 6/6 of its findings — would have been flagged by R32conf-class truth-audit
- Grok ACCEPT verdict reduces to ACCEPT-with-1-HD-6-flagged-polish after audit
- ChatGPT MAJOR verdict reduces to MINOR-revision after audit (FB1 is real but is 3 one-line cross-refs; FB2 is OPINION-titlecase; new MAJOR items FM95-1/2/3/4 are re-raises or now-closed-in-v3.1.96)

## Closure plan (concrete tex edits, all single-line / single-sentence)

### CLOSE NOW (8 items, single restamp wave → v3.1.97)

**Edit 1 (row 1a — §III.A per-class rates cross-ref)** — at L555, after "anomalous at $\sim$20 times the rate of QSOs (0.75\% vs.\ 0.037\%), with anomalies peaking at $z \sim 0.75$ compared to $z \sim 0.93$ for normal spectra.", insert: "(This validated-\texttt{TARGETTYPE} per-class breakdown is consistent with the science-class recount of Table~\ref{tab:recount}: the $\sim\!6.5$M denominator here is the BGS/LRG/ELG/QSO/MWS bitmask subset, a stricter cut than the $20.3$M science-class denominator used for the recount rate.)"

**Edit 2 (row 1b — §III.B 12 high-z QSO candidates parent-population pointer)** — at L559, after "Applying these three cuts to the full 195{,}829 DESI anomaly catalog yields 12 candidates with Redrock template-fit redshifts $z = 6.0$--$6.23$", insert: "(the 12-candidate cut operates on the anomaly score and Z-arm dominance regardless of \texttt{TARGETTYPE}; per the recount of \S\ref{sec:desi} the parent $195{,}829$ includes non-primary-class spectra, but the selection function of the 12-candidate set itself is target-class agnostic by construction.)"

**Edit 3 (row 1c — §V.A 5,384 QSO-candidate sample parent-population disclosure)** — at L792, prepend the Landy-Szalay paragraph with: "The $5{,}384$-object QSO-candidate sample is drawn from the full $195{,}829$ DESI anomaly catalog by joint NEOWISE $W_1-W_2$ color $+$ anomaly-score $+$ no-Gaia-parallax cuts and is therefore well-defined irrespective of DESI \texttt{TARGETTYPE} bits; the science-class recount of \S\ref{sec:desi} affects the parent-population framing but not this sample's selection function."

**Edit 4 (row 9 — §VI.E lead-clause reorder)** — replace L887 sentence "Our DESI anomaly rate of 0.87\% is numerically close to the 1.07\% rate reported by Liang \etal~\cite{Liang2023} on the DESI EDR, despite differences in model architecture and a $\sim$90$\times$ increase in sample size --- but the science-class-restricted recount (\S\ref{sec:desi}) shows the two rates are measured on different populations:" with: "The science-class-restricted recount (\S\ref{sec:desi}) shows our DESI $0.87\%$ rate and Liang \etal's~\cite{Liang2023} DESI-EDR $1.07\%$ rate are measured on different populations:"

**Edit 5 (row 10 — Table V row (d) SMBHB inline qualifier)** — append to the $B_{\rm MB/SMBHB} = 7.14\times 10^{3}$ Table V row: "(only vs.\ idealized circular-orbit SMBHB; see \S\ref{sec:nanograv})"

**Edit 6 (row 11 — Conclusion item 2 reorder)** — at L904, swap clauses: lead with "Genuine novelty fraction $\sim\!17.8\%$ at the DESI top-$1{,}000$ score stratum against 18 curated all-sky catalogs (single-sample point estimate; Wilson 68\% sampling interval $\pm 1.2\%$; full-catalog extrapolation empirically untested); 58.8\% SIMBAD-unmatched (per-survey: 27\% Gaia to 99\% DESI top-10K)."

**Edit 7 (row 12 — §III.A 0% artifact binomial CL)** — at L887 "(0\% artifact rate in top~200)" → "($0/200$ visually flagged; binomial 95\% upper limit $\leq 1.5\%$)"

**Edit 8 (row 13 — §II.A force-include disclosure in main text)** — at L372, after "high-score anomalies concentrate in distinct islands and lobes of the embedding rather than scattering uniformly through the bulk population", insert "(the $83$ overplotted stars are a force-included display set, not an unbiased density-concentration test;)" before "the 83 gold-tier anomalies".

**Edit 9 (row 15 — Conclusion item 5 SMBHB qualifier)** — at L910, after "decisive only vs.\ circular-orbit SMBHB reference; see environmental caveat in \S\ref{sec:nanograv}", append ", and is not a cosmological detection."

### KEEP (HD-6 ruled, HD-11 ruled — submission-day decisions)

- Row 4 (DOI placeholder)
- Rows 16 + 23 (264,938 / 264,738 correction-note prose)

### Outcome

- **Effective post-audit verdict**: P3 v3.1.97 = MINOR-revision close. After 8 one-line/one-sentence edits all sites are clean; readiness oscillates back up from the EXT4-receipt dip per the readiness-cap-99 rule. Recommend immediate restamp → v3.1.97 (pdf-restamp bundle) followed by `bigbounce-post-bump-sync`.
- **Pattern-052 evidence**: Gemini leg's 6/6 PDF-extraction misreads confirm pattern-052 applies to vendor PDF-OCR pipelines as well — the prophylactic numeric expansion of $F_0$ at v3.1.94 killed the perennial F₀ class across all three EXT4 legs (none re-raised it). The same prophylactic treatment of the eROSITA Table footnote symbols (replacing `$^\S$` / `$^\#$` with named superscripts, e.g. `\textsuperscript{S}` / `\textsuperscript{\#}`) would harden against the row-21 class going forward; logged as a future-polish item.
