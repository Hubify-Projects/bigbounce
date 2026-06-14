# EXT12 Harvest — P3 — ChatGPT Pro Extended

- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc617-2480-83e8-bf48-cc78a7bce891
- PDF md5: 72bd3e5b (paper3_anomaly_catalog_v3.1.108.pdf)
- Submitted: ~17:27 PDT 2026-06-13
- Harvested: 2026-06-13 18:39 PDT
- EXT11 baseline: MINOR REVISIONS
- EXT12 verdict: **MINOR REVISIONS**

## Headline Verdict

Recommendation: MINOR REVISIONS — "would recommend ACCEPT after two small textual/method-definition fixes"

## EXT12 Progress

Items CLOSED in EXT12:
1. Abstract catalog-grade/exploratory scope — mostly closed. Abstract now explicitly states
   269,117 subset excludes LAMOST, distinguishes DESI/SDSS/Planck/NEOWISE from eROSITA/Gaia.
2. DESI S>5/top-1% wording — closed.
3. Table IX has prior-sensitivity note — partially closed.

## Remaining Open Items (2 minor)

**Minor 1 — DESI validation gate type incorrectly described.**
Abstract says "DESI, SDSS, Planck, and NEOWISE pass the injection-recovery and native-retrain
validation gates" but DESI's validation is k-fold/OOD Jaccard stability, NOT the 5σ
injection-recovery gate (SDSS, Planck, NEOWISE pass that gate; DESI passes a different one).

Proposed fix: "DESI passes the k-fold and OOD stability gates; SDSS and Planck pass
detector-sensitivity injection-recovery gates; NEOWISE passes the mask-geometry QA gate;
eROSITA and Gaia fail the 5σ injection-recovery gate and remain exploratory."

**Minor 2 — Table IX Bayes-factor label type.**
The table labels all entries as Savage-Dickey density ratios, but the qualitative behavior
(BMB/free nearly constant, BMB/SMBHB varies strongly) is inconsistent with standard
Savage-Dickey behavior under uniform prior width changes. Needs either relabeling as
"posterior-density/tail-sensitivity diagnostic" or re-explanation of why the ratio varies.

## Auto-Falsify Check

Pattern-052 (HD-* DO-NOW): No HD-* class findings.
The Bayes-factor table question is PARTIAL (Table IX note was added but labeling is still
inconsistent). This is NOT the same as the EXT11 Table IX BF ratio behavior item — that was
"distinguish prior-sensitivity regime from model-preference regime." EXT12 finds a RESIDUAL
issue with the Savage-Dickey labeling convention itself.

## EXT13 Closure Effort

~25 min: fix 1-sentence DESI validation description + relabel or explain Table IX convention.
High confidence ChatGPT → ACCEPT in EXT13.
