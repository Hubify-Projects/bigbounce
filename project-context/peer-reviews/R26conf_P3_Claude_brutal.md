# P3 R26conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper3_anomaly_catalog_v3.1.84.pdf` md5=2539e13c pages=25
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique

---

## PRIORITY ARITHMETIC — count web ledger reconciliation

**Headline numbers in abstract (pp.1):**
- 378,280 unique anomalies = 378,080 point-source + 200 Planck CMB patches
- 269,317 catalog-grade unique entries (6-way dedup of DESI+SDSS+eROSITA+Planck+Gaia+NEOWISE, NO LAMOST) including the 200 Planck patches
- 269,117 object-level subset (drops the 200 patches): 269,317 − 200 = 269,117 ✓
- Earlier-draft superseded: 264,938 / 264,738 (catalog-grade and object-level pre-correction)
- Correction delta: 269,317 − 264,938 = 4,379 ✓ — and 269,117 − 264,738 = 4,379 ✓
- 4,379 = the LAMOST detections that merge into catalog-grade clusters at 5″, which a headline-minus-LAMOST naive subtraction double-removes. Arithmetic is internally consistent at the abstract level.
- LAMOST exploratory tier retained as methodological lesson: ∼113,000 objects, "98% blue-excess training-bias artifact, injection-recovery gate FAIL". Disclosed deliberately — no flag.

**Cross-transfer baseline vs Path-C unique (p.4, Fig.2 caption):**
- Cross-transfer baseline = 319,443 detections across 8 archives (ACT DR6 included for completeness; quarantined for science).
- Canonical Path-C unique = 378,280 after per-survey native retrains + 7-way 5″ dedup.
- **GAP A — apparent contradiction reader will hit**: how does an 8-way baseline of 319,443 detections become a 7-way unique count of 378,280 (LARGER) after dedup? Dedup never grows the count; the resolution is that native retrains *replace* the cross-transfer detections per survey (especially SDSS 12 → 77,905 native; LAMOST cross-transfer → native explodes), so the 319,443 is not the input to the dedup — the per-survey *native* tallies are. Paper says this in §III but **the figure caption juxtaposes 319,443 and 378,280 with the word "after… dedup," which is misleading**. **M1: rewrite Fig.2 caption to make explicit that dedup is applied to the native per-survey counts, not to the 319,443 cross-transfer baseline.**

**388,493 figure resolved (§IVC, p.12):** "7-way positional deduplication at 5″ identifies 637 multi-survey coincidences across 388,493 survey-level detections. 637 multi-survey clusters + 9,576 intra-survey duplicates = 10,213 total collapsed, yielding the 378,280 unique-object headline (2.629% compression)."

**Ledger:**
- Survey-level detections (after native retrains, ACT excluded): 195,829 (DESI) + 77,905 (SDSS) + 113,342 (LAMOST) + 298 (eROSITA) + 200 (Planck) + 500 (Gaia) + 419 (NEOWISE NEOWISE-masked) = 388,493 ✓
- Subtract 10,213 dedup compression → 378,280 ✓ (matches headline)
- Of the 378,280: 378,080 point-source + 200 Planck patches ✓
- Catalog-grade (drop LAMOST 113,342; keep its 4,379 LAMOST-into-cluster merge contributions): 378,280 − 113,342 + 4,379 = 269,317 ✓ — **the 4,379 reconciles exactly**. This arithmetic is correct and the abstract's "headline-minus-LAMOST subtraction double-removes the 4,379" framing is the right pedagogical hook.
- Object-level subset (drop 200 Planck patches): 269,317 − 200 = 269,117 ✓
- Earlier-draft pre-correction: 264,938 / 264,738. Delta 4,379 ✓ both ways.
- ACT DR6 bookkeeping (Table I footnote ‖): cross-transfer 200 ACT patches contributed zero positional overlaps → 8-way anomaly-detection input sum 388,693 → 388,493 by subtracting 200 ACT → 378,280 unique. **388,693 vs 388,493 = the 200 ACT patches removed by quarantine.** Clean.

**LEDGER STATUS: RECONCILES END-TO-END. No arithmetic finding.** This is a vastly improved state vs prior rounds.

**N1 — 24,049 HEALPix occupied-pixel rerun (§IVB, p.11):** χ² = 376,713, dof = 24,048, χ²_ν = 15.7 against the prior (now-withdrawn) 38,330-pixel / χ²_ν = 3.76 artifact. Disclosure is explicit, audit JSON `r24conf_pod_session_batch.json` cited, Spearman r=0.0005 (lat) and Pearson r=0.006 (dust) reported as null. **All-clear, but see M2 on caveat framing.**

**N2 — SMICA preprocessing footnote (§IIIF Planck CMB, p.9):** "20,000-patch input quoted above (and as N_total in Table I) is the original cross-transfer patch budget, on which the 200-patch tier is a top-1% selection; the Path-C native pipeline extracts an independent, 10× larger 2×10⁵-patch bank from the same |b|≥20° masked SMICA map for training and re-scoring, with the Planck tier held at the same canonical count of 200 (the top-ranked patches of the native re-score). All patch positions in the native bank are drawn at |b|≥20° by construction (the extraction script rejects positions inside the Galactic cut), so the scored set and the training set share the same masked sky domain: no masked-to-unmasked domain transfer occurs in the published tier." **Clean, addresses the historical pattern-009 SMICA-preprocessing gap. All-clear.**

---

## §III/IV findings

### P3-M1 — Fig.2 caption misleads reader on dedup input
**Severity**: Minor.
**Location**: p.5 Fig.2 caption: "319,443 detections; canonical Path-C unique count is 378,280 after per-survey native retrains and 7-way deduplication."
**Issue**: Reads as if dedup *reduces* 319,443 → 378,280. Dedup cannot grow a count. The actual chain is: 319,443 (cross-transfer 8-way baseline, DESI-trained) is *replaced* by the 388,493 native retrain sum (7-way, ACT quarantined), which then deduplicates to 378,280. Reader-trip hazard. Fix: insert "(the 378,280 count is taken not on this 319,443 baseline but on the per-survey native-retrained tallies summing to 388,493; see §IVC)" in the caption.

### P3-m1 — Table I "Total (cross-transfer, ACT-incl.)" row is computed on a mixed basis
**Severity**: minor.
**Location**: Table I, p.7.
**Issue**: 319,443 row sums per-survey **cross-transfer** N_anom, but the same column lists 195,829 for DESI which is the *DESI-native* number (DESI is the anchor; cross-transfer ≡ native for DESI). The row label says "cross-transfer" but DESI is native. Add a single dagger noting "DESI row = native (anchor survey); other rows = cross-transfer baseline."

### P3-N1 — "200" Planck CMB count is a *fixed-size* selection, not a detection
**Severity**: Nit/clarity.
**Location**: Table I row "Planck CMB" 200§*; abstract opening sentence "378,080 point-source + 200 Planck CMB map patches."
**Issue**: Table I footnote ⋆ says clearly "anomaly count reflects a fixed top-1% selection... 1.00% rates should not be interpreted as independent measurements of the intrinsic anomaly frequency." The abstract does not echo this, and a reader will think 200 Planck patches were *detected*. Add 6 words to the abstract: "200 Planck CMB map-patch sky regions (fixed top-1% selection)."

### P3-N2 — eROSITA "threshold 0.259 reproduces on none of 16 monotone rescalings" disclosed but framed as transparency-not-failure
**Severity**: Substantial — major-or-minor judgment call.
**Location**: §IIIE eROSITA, p.8.
**Issue**: The paper plainly states the production eROSITA threshold (0.259) cannot be reproduced from the canonical-S axis or 16 monotone rescalings of the committed raw score. The defense: "the released 298-source membership list is, however, exactly the committed-raw top-298 (the minimum released score equals the rank-298 raw threshold 3.4119)... the committed, reproducible selection is the n=298 membership list itself — not any score axis." Calibration notes say this artifact-anchored framing is deliberate. **All-clear at the disclosure level**, but: classify as **m2 — clarify that downstream meta-analyses using eROSITA S values cannot be performed because the score axis is irreproducible; only the 298-object membership is reproducible.** A reader doing IF-style re-isolation will need this loud.

### P3-m3 — LAMOST exploratory contribution 108,963 → 378,280 inflates "biggest" claim
**Severity**: minor.
**Location**: Table I footnote ⋆ (p.7, .tex line 303), Abstract.
**Issue**: 269,317 catalog-grade + 108,963 LAMOST exploratory = 378,280. The "141×" largest-prior-catalog claim is computed on 378,280, but ~29% of that count is the LAMOST exploratory tier which the paper itself classifies as "98% blue-excess training-bias artifact, injection-recovery gate FAIL." The catalog-grade-only multiplier (269,317 / 2,685 Liang) = ~100×, not 141×. **Both numbers are defensible; recommend the abstract also cite the catalog-grade multiplier** ("∼100× catalog-grade / ∼141× including the LAMOST exploratory lesson tier") so the comparison is honest. Reviewers will compute this themselves.

### P3-N3 — 24,049 occupied HEALPix χ²_ν = 15.7 framed as primarily-footprint, not anomaly clustering — caveat is correct but visibility is low
**Severity**: nit.
**Location**: §IVB, p.11 .tex line 502.
**Issue**: The χ²_ν = 15.7 figure is structurally an N1-level all-clear (reproducible artifact JSON cited, prior 38,330/3.76 explicitly withdrawn), AND the paper clearly states "the significant χ²_ν = 15.7 is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering." But the inline statement still leads "is strongly non-uniform (χ²=376,713, χ²_ν=15.7)" which a skimming reader will misread as a clustering detection. Tighten by reordering: lead with "consistent with survey-footprint inhomogeneity, NOT a clustering detection" before the χ² number.

### P3-N4 — Fig.3 right-panel SDSS x-axis to S = 1.9×10¹¹ is fine but the bimodal-structure caption uses two distinct score scales (S_cross-transfer ≤ 10¹¹ vs S_native ≤ 14) that a casual reader will not separate
**Severity**: nit.
**Location**: Fig.3 caption, p.6.
**Issue**: Caption already explains the dual scale ("SDSS native re-score compresses the same objects to S<14"). Could be tightened with a two-x-axis figure (top axis: native; bottom: cross-transfer). Not a blocker.

### P3-N5 — Appendix C Fig.11 normalization disclaimer is the right disclosure, but the ~1.5 σ(f_NL) gap between Fig.11's 16.85 single-tracer baseline and §V's 8.98 single-tracer baseline will trip every careful reader
**Severity**: nit-to-minor.
**Location**: Appendix C, Fig.11 caption, p.21.
**Issue**: Caption already says "the σ(f_NL)=16.85 single-tracer baseline and σ(f_NL)=11.71 dense-tracer limit quoted here are internal to the shot-noise Fisher implementation underlying this figure ... they are not on the same absolute normalization as the redshift-binned Fisher of §V ... Only the relative quantities of this figure — the +7.93% dense-limit improvement and the 15–30% shot-noise penalty mapping — carry over to the §V forecast." This is the right disclosure but the visual mismatch is jarring. Consider also re-rendering Fig.11 in *relative* (Δσ/σ_std) units to remove the absolute-axis confusion entirely. Optional polish.

---

## Pass-2 self-critique (vs `pipelines/p3_anomaly_engine/paper3_draft.tex`)

Cross-checked the .tex against the PDF for the priority items:

1. **Count web ledger.** .tex line 299 footnote ‖ confirms 388,493 = sum of 7 native counts; 388,693 → 388,493 by ACT-200 subtraction; 388,693 → 378,480 (8-way); 388,493 → 378,280 (7-way; canonical). Line 303 footnote ⋆ confirms the 269,317 catalog-grade is computed by *direct independent* 6-way 5″ dedup (not by 378,280 − 113,342 subtraction), and that the same dedup machinery reproduces 378,280 exactly. **Verified: my M1 finding on Fig.2 caption is still valid (the visible figure caption text is what trips a reader); my P3-m3 LAMOST-exploratory framing finding stands.**
2. **24,049 px rerun.** .tex line 502 confirms 49,152 total Nside=64 pixels, 24,049 occupied (≈ 49% sky coverage consistent with the union of seven survey footprints). χ² = 376,713, dof = 24,048 (= 24,049 − 1), χ²_ν = 376,713/24,048 = 15.665 → "15.7" stated. Artifact JSON cited. Caveat ("dominated by footprint inhomogeneity, not intrinsic clustering") is explicit. **P3-N3 still applies as ordering nit.**
3. **SMICA preprocessing.** Verified in body (§IIIF, .tex lines around §planck): 2×10⁵-patch native bank, |b|≥20° mask enforced at extraction, training and scored domains identical, top-200 native re-score patches all on |b|≥20°. Table V caption (.tex confirms) reports SMICA R3.00 full-mission temperature, gnomview 10°×10° 64×64 patches at 9.375′/pix, per-patch standardization (mean subtracted → DC removed, divided by patch std, NaN→0, clipped to ±10), no apodization, and the 187/200 retention check that confirms ranking is not driven by residual DC or large-scale gradient modes. **N2 all-clear stands.**
4. **No 388,493 inconsistency.** Verified at .tex line 299, 523, 692, 909, 525 — number is internally consistent every place it appears.
5. **264,938 / 264,738 superseded numbers.** Appear in .tex line 71 (comment block only) and in body abstract line 161 as "an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic, which double-removes the 4,379 LAMOST detections that merge into catalog-grade clusters at 5″." This is the correct correction framing. **All-clear, deliberate per calibration.**
6. **N4-novelty claim audit.** Scanned headline and conclusions — paper claims "largest multi-archive anomaly detection campaign to date" + "first multi-survey BigAE framework" + cosmological-application tier "demonstrate utility beyond source discovery." No N4 self-claim. **All-clear per /never-claim-n4.**
7. **Future-work language audit.** Scanned for trigger phrases. Found: "remains a refinement for a future catalog revision" (Budavári–Szalay, §IVC, .tex 525), "central 9.4% improvement is a forecast pending higher-S/N follow-up, not a detection" (abstract), "multi-PTA joint chains are deferred to a dedicated PTA paper" (Appendix E, p.21). All three are properly classified as TRULY-BLOCKED (Budavári–Szalay needs proper-motion epoch propagation that doesn't exist for legacy surveys; higher-S/N for f_NL needs SPHEREx; multi-PTA joint chains are a separate paper). **No future-work-defer violation.**
8. **Visual / overflow check (latex-audit-lite via PDF Read).** No column-overflow file paths spotted; \artifact{} macro used consistently; references render cleanly; HuggingFace URL present and clickable; all tables fit (Table I uses footnote symbols, Table IV is full-width). **PASS.**

Self-critique on my own findings: M1 (Fig.2 caption misleads) is the strongest finding. The other 7 are minor/nit. **No BLOCKER, no MAJOR.** This is the cleanest P3 PDF I've seen across rounds — count web reconciles end-to-end, the four historical pain points (LAMOST tier framing, SMICA preprocessing, 24,049 rerun, eROSITA score axis) are all explicitly addressed in-paper.

---

## Explicit all-clears (with arithmetic)

| Claim | Arithmetic | Verdict |
|---|---|---|
| 378,280 = 378,080 + 200 | 378,080 + 200 = 378,280 | ✓ |
| 378,280 = 388,493 − 10,213 | 388,493 − 10,213 = 378,280 | ✓ |
| 10,213 = 637 + 9,576 | 637 + 9,576 = 10,213 | ✓ |
| 388,493 = 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 | sum = 388,493 | ✓ |
| 388,693 = 388,493 + 200 (ACT included) | ✓ | ✓ |
| 378,480 = 388,693 − 10,213 (8-way variant) | ✓ | ✓ |
| 269,317 catalog-grade (6-way independent dedup, paper says NOT 378,280 − 113,342) | 269,317 + 108,963 = 378,280 ✓; 108,963 = 113,342 − 4,379 ✓ | ✓ |
| 269,117 object-level = 269,317 − 200 Planck patches | 269,317 − 200 = 269,117 | ✓ |
| Earlier-draft 264,938 / 264,738 superseded; delta = 4,379 | 269,317 − 264,938 = 4,379 ✓; 269,117 − 264,738 = 4,379 ✓ | ✓ |
| 24,049 occupied / 49,152 total Nside=64 pixels | 24,049 / 49,152 = 48.9% sky coverage (plausible for union of 7 surveys) | ✓ |
| χ²_ν = 376,713 / 24,048 = 15.665 → "15.7" | ✓ | ✓ |
| 17.8% genuine-novelty Wilson 68% CI ±1.2% on n=1,000 | √(0.178·0.822/1000) = 0.0121 → ±1.2% | ✓ |
| 0.087% radius sensitivity (3″/5″/7″ sweep) | max(|378,604−378,280|, |378,145−378,280|) / 378,280 = 324/378,280 = 0.0857% → "0.086%" | ✓ |
| 5,500 ESS = 32 walkers × 10,000 / 58 τ | 320,000/58 = 5,517 → "~5,500" | ✓ |
| 200 Planck patches = top 1% of 20,000 | 200/20,000 = 0.01 | ✓ |
| 4,379 LAMOST→catalog-grade overlap at 5″ | derived from 113,342 − 108,963 | ✓ |

**Ledger reconciles end-to-end. Zero arithmetic findings.**

---

## Summary recommendation + counts line

**Counts:** 0 BLOCKER, 0 MAJOR (E#), 1 minor-clarity (M1: Fig.2 caption dedup-input wording), 3 minor (m1 Table I row label, m2 eROSITA S-axis warning, m3 catalog-grade multiplier in abstract), 5 nit (N1 24,049 rerun all-clear, N2 SMICA all-clear, N3 χ²_ν ordering, N4 Fig.3 dual-scale, N5 Fig.11 abs-vs-rel normalization), 8 explicit all-clears verified by arithmetic.

**Recommendation:** ACCEPT WITH MINOR REVISIONS. The count web reconciles end-to-end; the four historical pain points are all explicitly addressed; the disclosure tone is appropriately self-critical (LAMOST as methodological lesson, eROSITA S-axis irreproducibility, 24,049 footprint-dominated caveat, Fig.11 normalization disclaimer all visible to the reader). M1 is the only finding worth a recompile cycle; everything else is polish.

**Path forward:** Fix Fig.2 caption (M1) and abstract catalog-grade multiplier (m3) in a single editorial pass; the other minors/nits can roll into the next revision without blocking submission.


