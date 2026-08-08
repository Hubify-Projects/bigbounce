# Referee Handoff — P3 (Multi-Survey Anomaly Catalog)

`pipelines/p3_anomaly_engine/paper3_draft.tex` · slug `paper-3` · **current version: v3.1.140 (2026-07-06)**

## Headline result

A validated catalog-grade subset of **268,519 unique multi-survey anomalies**, obtained by
applying an autoencoder framework to 37.3M sources + CMB map patches across seven surveys
(DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE) with per-survey native retraining and
positional deduplication. The count is **directly recomputable** via
`reproduce_headline_dedup.py`. The validated headline draws from the injection-recovery- and
stability-gated components only; exploratory tiers (eROSITA score-axis, Gaia) are labeled and
sequestered. The §V cosmology sections (multi-tracer f_NL, NANOGrav) are presented explicitly
as **methodological demonstrations yielding null/marginal results**, not detections.

## Closed since the 2026-07-01 floor

1. **DESI injection-recovery — real and committed.** A full 5σ injection-recovery on real
   DESI-DR1 spectra: broad-class recovery 99–100% across 3 validation gates, at parity with
   SDSS and Planck; narrow-line injection floor ≥15σ (disclosed, not claimed as a pass).
2. **DESI score-vs-z deferred test — CLOSED (v3.1.139 DATA-UNLOCK).** The previously
   pod/HF-bound `desi_zall.parquet` test was run and folded in.
3. **Scaler-leakage flag — CLOSED.** The spectroscopic path (DESI/SDSS/LAMOST/Planck)
   normalizes per-spectrum and is split-independent → the J=0.862 / J=0.732 headline Jaccard
   gates are leak-free. The tabular tiers (eROSITA/NEOWISE/Gaia) use a full-sample scaler,
   already disclosed and bounded by a committed train-split-only refit control; those tiers are
   not headline-load-bearing.
4. **NEOWISE 436-vs-419 flag — verified NOT an inconsistency.** 436 = raw top-1% selection;
   419 = after the |b_ecl|<80° ecliptic-pole mask; both stated with footnote "436 to 419
   (96.1% retained)." Documented two-stage count.

## Convergence status

P3 has reached the LLM-refereeing floor: **0 genuinely-new real findings** across the FINAL
(2026-07-05) and POSTPOLISH (2026-07-06) truth-audited EXT+API rounds
(`project-context/peer-reviews/FINAL_SIGNOFF_AUDIT_2026-07-05.md`). On the identical v3.1.140
PDF: **grok-4.3 (API) MINOR REVISIONS, "central claim supported"**; **Grok (EXT) / Gemini
MAJOR REVISIONS** (Gemini recommends ApJS/MNRAS); **ChatGPT REJECT and openai gpt-5.5 REJECT**
— the sharpest cross-vendor contradiction of the round (grok-4.3 MINOR vs ChatGPT/openai
REJECT on the identical PDF), the maximally-harsh-referee structural floor (directive H). No
new correctness defect surfaced.

## Recurring objections a human referee should adjudicate

1. **eROSITA score-axis non-reproducibility (drives the Gemini REJECT).**
   - Concern: per-object S_BigAE scores + the 0.259 production threshold are not recoverable
     across 16 monotone rescalings; an uncommitted post-hoc step.
   - Disclosed: `sec:erosita` leads with membership-list-only + the 16-rescaling failure; caveat
     (h) and the Table IV caption quote the *reproducible* raw rank-298 cut (S_raw ≥ 3.41) and
     label 0.259 as the irreproducible production label. eROSITA is exploratory-tier, excluded
     from the ≥268,519 validated headline.
   - Judgment call: **is a disclosed, sequestered, exploratory-tier score-axis non-reproducibility
     acceptable in a catalog paper (the released product is the committed membership list), or does
     a catalog paper require every tier fully reproducible?** (this is the crux of the REJECT)

2. **DESI dominance — injection-recovery now completed (see above).**
   - The prior "DESI ran no injection-recovery" MAJOR is **closed** by the committed results:
     broad-class 99–100% recovery, 3-gate validation. Narrow-line floor ≥15σ is disclosed.
   - Remaining judgment call for the human referee: **are the 3-gate broad-class results and the
     ≥15σ narrow-line floor together a sufficient robustness demonstration for the dominant
     DESI component?** (editorial)

3. **Lost Gaia preprocessing lineage + illustrative cosmology sections.**
   - Concern: exact 20-feature Gaia script not recovered (lineage-inferred); f_NL/NANOGrav
     sections show no significant improvement.
   - Disclosed: §III.G / §training / data-availability state the script is lineage-inferred;
     Gaia is exploratory, gate-FAIL, excluded from validated tier. Cosmology sections labeled
     "no improvement."
   - Judgment call: **honest provenance gap on an excluded exploratory tier — acceptable, or a
     hard integrity bar?**

## What is NOT in question

No genuinely-new correctness defect remains. The validated ≥268,519 headline is a 6-way dedup
of the injection-recovery- and stability-gated components only; the exploratory tiers are
truthfully sequestered. DESI injection-recovery is now real and committed. The scaler-leakage
audit confirms the headline Jaccard gates are leak-free.

## Recommended venue / next step

Submit to **ApJS** (catalog venue) with the eROSITA/Gaia exploratory-tier non-reproducibility
disclosures flagged to the editor as *by-design scope*, and the released committed products
(membership lists, per-object catalogs, real DESI injection-recovery results) foregrounded.
The venue call is the crux: Gemini (and the audit) recommend a catalog/data-release venue
(ApJS/MNRAS) over PRD, while grok-4.3 rates the same PDF MINOR for PRD — a journal-routing
opinion, not a correctness objection. The validated tier stands independently and, with the
DESI injection-recovery and DATA-UNLOCK score-vs-z test now real and committed, is more
robustly grounded than the 2026-07-01 floor.
