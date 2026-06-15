# EXT18 Peer Review — P3 (Multi-Survey Anomaly Catalog)

- **Reviewer:** Claude_brutal (Claude Code sub-agent, Anthropic leg — API leg failed on credit balance, run as fallback sub-agent with native PDF read)
- **Paper:** P3 — "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies…"
- **Round:** EXT18
- **Version:** v3.1.111
- **Pages read:** 1–30 (full PDF, all figures/tables/appendices)
- **Date:** 2026-06-14

Brutal, figure-and-equation-aware read. Counts recomputed; V/χ² statistics recomputed; abstract↔body cross-checked.

---

## Summary of arithmetic verification (PASSED)

The bulk of the catalog bookkeeping is internally consistent and was recomputed independently:

- Headline: 378,080 point-source + 200 Planck = **378,280** — consistent on title, abstract, Table I, §IV C, Conclusions, Data availability (p23). PASS.
- Per-survey native sum: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = **388,493** survey-level detections. Matches stated value. PASS.
- Dedup: 637 multi-survey + 9,576 intra-survey = 10,213 collapsed; 388,493 − 10,213 = **378,280**. PASS.
- Cramér's V (p15): √(376,713 / (378,280 × 24,047)) = √(4.141×10⁻⁵) = **0.0064**. PASS.
- χ²_ν = 376,713 / 24,048 = **15.66 ≈ 15.7**. PASS.
- Catalog-grade tier 269,317 − 200 Planck = **269,117**. PASS.
- Fisher: 1/√0.01509 = **8.14**; envelope edges 3.92 / 8.98 recompute correctly; 6.1% and 9.4% improvements recompute. PASS.
- Savage-Dickey: 3.23/(4.52×10⁻⁴) = **7.14×10³**, log₁₀ = +3.85. PASS.
- Survey-level ratios (141×, 73×, 21.5×, 6500×, 96.1%, 0.03%, 0.87%, 3.38%) all recompute. PASS.

The count discipline in this paper is unusually careful and the per-survey/per-tier provenance footnotes are thorough. The one bookkeeping exception is MINOR-1 below.

---

## MINOR Findings

### MINOR-1 — Cluster-size histogram does not sum to 9,553 (p16)
**Location:** §IV C "Friends-of-friends chain audit" / cluster-accounting reconciliation, p16.
The committed size histogram is given as: "9,124 clusters of size 2, 313 of size 3, 73 of size 4, 22 of sizes 5,8 [sic], 6 of size 6, 3 of size 7, 2 each of sizes 8–9, 1 each of sizes 10–11, 3 of size 12, 1 of size 17." Summing the cluster counts:
9,124 + 313 + 73 + 22 + 6 + 3 + 2 + 1 + 3 + 1 = **9,548**, not the stated **9,553** (short by 5).
The text asserts this histogram "sums to 9,553 clusters." The collapsed-detection total Σ(size−1) = 10,213 is the load-bearing number and reconciles elsewhere, so this is presentation, not a headline error — but a referee who checks the histogram (as I did) finds it off by 5. The "22 of sizes 5,8" phrasing is also garbled (likely "22 of size 5").
**Required fix:** Re-state the size histogram so the cluster counts sum exactly to 9,553 and fix the "sizes 5,8" typo. If 9,548 is in fact correct, then "9,553" and the downstream "9,553 − 637 = 8,916" must be corrected.

### MINOR-2 — Abstract is a wall of caveats; readability cost (p1)
**Location:** Abstract.
The abstract runs ~1.5 pages and front-loads a dozen gate-pass/gate-fail provenance clauses (Jaccard gates, injection-recovery gates, score-axis irreproducibility, LAMOST blue-excess, eROSITA membership-only, ACT quarantine) before a reader reaches the science. This is admirably honest but the central result — "largest multi-survey anomaly catalog, 378,280 objects, 17.8% genuine novelty fraction at the top-1,000 stratum" — is buried. No factual error; a PRD editor will likely ask for compression.
**Required fix:** Tighten the abstract to ~250 words: lead with scale + the honest novelty number, push the per-survey gate-pass/fail ledger to one summary sentence pointing to Table I / §VI.

### MINOR-3 — "uncataloged BAL QSO at z ≈ 0.86" stated as confirmed vs. "candidate" (p1, p16, p22)
**Location:** Abstract ("an uncataloged BAL QSO at z ≈ 0.86"), p16 item 3 ("Uncataloged BAL QSO at z ≈ 0.86: broad Mg II absorption confirmed in both DESI and SDSS"), Conclusions p22 ("one uncataloged BAL QSO").
The object is variously "confirmed" (Mg II in two surveys) yet the paper elsewhere repeatedly stresses that all high-z/QSO candidates "remain unconfirmed pending visual inspection or re-observation" (p7–8). "Confirmed in both independent surveys" overstates: appearing in two surveys' anomaly catalogs by positional dedup is consistency, not spectroscopic confirmation of the BAL classification.
**Required fix:** Use "BAL QSO candidate" consistently, or define explicitly what "confirmed" means here (two-survey Mg II trough morphology, not external validation).

---

## Honesty / framing assessment (the brutal read)

The framing is **honest**, and notably so for a paper of this kind:

- The title says "Path-C Unique Anomalies" and "Novelty Fraction," not "novel anomalies." The body consistently distinguishes the 58.8% SIMBAD-unmatched fraction (a *database-coverage* metric) from the 17.8% *genuine novelty fraction* against 18 curated catalogs via CDS X-Match, and repeatedly warns readers/headlines to quote 17.8%, not 58.8% (abstract, §IV A, Fig 6, Conclusions). This is the single most over-claimable number in the paper and it is handled correctly.
- Significance claims are appropriately **descriptive, not detection**: the χ²/Cramér's V spatial result is explicitly attributed to footprint geometry and flagged as "must not be cited as evidence of astrophysical clustering" (p15). The f_NL forecast is labeled an "image of the ±1σ interval … not a 68% probabilistic interval" and the de-biased central estimate returns *zero* improvement (no multi-tracer detection claimed). The NANOGrav γ result is "+1.13σ … does not constitute a detection." The Planck×ACT null is flagged as geometry-driven and "non-diagnostic." Correct posture throughout.
- Cross-survey caveats are honestly stated: eROSITA score-axis is **irreproducible** (n=298 membership-list only, no monotone rescaling recovers the 0.259 threshold — §III E, Table IV); Gaia preprocessing is "lineage-inferred, not directly recovered" and rates "best-available rather than fully reproducible"; LAMOST 98% blue-excess is called a training-bias **artifact** and the LAMOST tier is exploratory; ACT DR6 is formally quarantined (Appendix F) and contributes zero objects. None of these failure modes are hidden.
- The abstract matches the body on all headline numbers (378,280; 269,317/269,117; 17.8%; 8.14; γ=2.567±0.382; B=7.14×10³).

Searched for leftover audit tags, duplicate phrases, and self-flattering language. No leftover internal audit tags (TODO/FIXME/AUDIT/reviewer-tier labels) appear in the rendered text. The repeated "Score-axis note" / "Normalization note" boilerplate in Fig 3, Fig 8, Fig 9, Fig 11 captions is intentional reader-protection, not accidental duplication. No N4-style novelty overclaim; the paper claims "largest multi-archive anomaly search … of which we are aware," appropriately hedged.

I could not find a substantive overclaim. The risks that *would* sink a paper like this — selling SIMBAD-unmatched as discovery, selling the spatial χ² as clustering, selling the f_NL/NANOGrav numbers as detections, hiding the eROSITA/LAMOST/ACT failures — are all explicitly defused in the body.

---

## ESSENTIAL Findings
None.

## MAJOR Findings
None.

---

## FINAL VERDICT: **MINOR REVISIONS**

The paper is scientifically honest, the catalog bookkeeping is sound (one histogram that fails to sum, MINOR-1), the significance claims are correctly framed as descriptive/forecast rather than detection, and the abstract matches the body. The only substantive fix is the 9,553 cluster-histogram reconciliation (MINOR-1). MINOR-2 (abstract length) and MINOR-3 (BAL "confirmed" vs "candidate") are polish. Accept after these three minor items; no re-review of methods or re-run required.
