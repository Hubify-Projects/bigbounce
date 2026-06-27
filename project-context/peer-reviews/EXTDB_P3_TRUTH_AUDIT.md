# EXTDB P3 Truth Audit — De-biased (neutral) referee round

Round: EXTDB (DE-BIASED). Providers: ChatGPT (Instant/gpt-4o), Gemini (Flash), Grok (Expert). **All three returned MAJOR REVISIONS.**
Source audited: `pipelines/p3_anomaly_engine/paper3_draft.tex` (current; v3.1.115, 2026-06-26). Date: 2026-06-27.
Auditor stance: verdict-first vs source. Patterns 061 (in-text verdict), 063 (number = extraction-artifact-FALSIFIED until checked vs SOURCE+artifact), 064 (Grok harsh). Calibration June 2026: arXiv valid; catalog extensiveness is NOT a defect.

## Headline conclusion

**The unanimous de-biased MAJOR is REAL as a peer-review signal but is NOT an integrity defect.** There is **no new fabrication and no suppressed caveat** in P3. Every load-bearing fact the three reviewers flag is **already disclosed in the paper — most of it verbatim in the ABSTRACT.** The R54 Table IX fabrication and the R56 clipped-footnote issues do **not** recur here; the de-bias surfaced nothing of that class.

What the de-bias *correctly* did: it stripped the "wow, unusually transparent" halo that inflated prior external rounds to ACCEPT, and graded P3's **framing** on a neutral bar. Under that bar, a paper whose **title + abstract front-load `378,280` and `~73×`** while the validated reality is `269k` / `~0.9×` legitimately earns a MAJOR for emphasis — even though the corrective caveat sits in the same sentence. That is an **editorial/framing** disagreement, not dishonesty. Calling it fabrication would *inflate* a false-positive; dismissing the framing critique would *bury* a real signal. Neither is warranted.

**One genuinely actionable convergent item survives** (see C1 below): two components that FAIL validation (Gaia, eROSITA) are still summed inside the number the paper labels **"catalog-grade" (269,317)**. 3/3 reviewers want that resolved. It is real, but numerically tiny (798 of 269,317 ≈ 0.3%) and editorial, not a data-integrity breach.

---

## Convergent MAJOR claims (deduplicated), verdict vs source

### C1 — eROSITA irreproducible scoring axis  [CONVERGENT 3/3: ChatGPT B3, Gemini B1, Grok M1] — VERIFIED-as-disclosed; partial real fix
Claim: production threshold 0.259 is unrecoverable; raw rank-298 = 3.41; per-object S_BigAE non-monotone in committed raw (ρ=−0.10); cannot support score-weighted downstream use.
Source check (§sec:erosita, L874; Table IV L876–889; abstract L579): **every one of these facts is stated by the paper itself**, with the same numbers (0.259, 3.41/3.4119, 16 monotone rescalings, ρ=−0.10, "undocumented post-hoc rescaling step whose code was never committed"). eROSITA is released as an n=298 **membership-list-only** product, S_BigAE column **not printed**, flagged exploratory (1.2% recovery, gate FAIL). Verdict: the *facts* are VERIFIED and serious, but **disclosed, not suppressed** — this is the opposite of the R54 fabrication. The residual editorial ask (Grok M1 verbatim): "state whether the 269,317 catalog-grade count includes or excludes the eROSITA tier." **It currently INCLUDES it** (abstract L579). → this is the real open item, folded into C-RESIDUAL below.

### C2 — Headline `378,280` / `~73×` vs validated `269k` / `~0.9×`  [CONVERGENT 3/3: ChatGPT B2, Gemini M2, Grok M2] — VERIFIED-as-disclosed; framing OPINION
Claim: title/abstract front-load the inclusive count and 73× scale; like-for-like is 2,468 science-target clusters ≈0.9× Liang (2,685); ~98.7% of DESI clusters on sky/filler spectra.
Source check (abstract L579; §sec:desi L745; Table II tab:recount L747): **the 0.9×, the 2,468, the ≈98.7%, and the "not a like-for-like comparison" are all in the abstract in the SAME sentence as the 73×**, and §IV.A devotes a full paragraph + a 5-row reconciliation table to it. The contested number is not unbacked — `ext3_b2_targettype_recount.json` is cited. Verdict: the underlying recount is VERIFIED-true and fully disclosed; the dispute (keep 73× with adjacent caveat vs delete it from the headline) is **editorial OPINION**. Per calibration, the full-stream count is a real thing they scanned (extensiveness ≠ defect), so keeping it WITH the adjacent 0.9× is defensible — but 3/3 convergence on "demote" is a legitimate emphasis signal.

### C3 — NEOWISE injection-recovery is mask-geometry QA, not a sensitivity test  [CONVERGENT 2/3: ChatGPT B4, Gemini B2] — FALSIFIED/STALE
Claim (esp. Gemini B2): NEOWISE is "grouped as a completed sensitivity pass," which is "scientifically invalid."
Source check (abstract L581; §sec:neowise L904): the paper says **verbatim** "NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by construction, not a detector-sensitivity test," and L904 spells out the |b_ecl| construction and "should be read as a different kind of gate." This was closed at R24conf (v3.1.82, META-M2, 4 sites). Verdict: **FALSIFIED** — the de-bias reviewers did not read the disclaimer that already states their exact point. The factual observation is correct but the "invalidly grouped as PASS" framing is false against source.

### C4 — DESI flagship tier lacks injection-recovery  [CONVERGENT 2/3: ChatGPT B4, Grok M3] — VERIFIED-as-disclosed; optional improvement
Claim: DESI (195k, S>5) has no injection-recovery test.
Source check (abstract L581): "DESI injection-recovery was not executed; its catalog robustness rests on the two Jaccard metrics" — stated plainly, plus 5-fold J̄=0.862, OOD J̄=0.732, and 0/200 visual (≤1.5% UL). Verdict: VERIFIED-true and disclosed. Grok M3 (MEDIUM) is the fair version: either run it or add one sentence arguing the existing gates suffice. Real but non-blocking; not a defect.

### C5 — Exploratory tiers (LAMOST/Gaia/eROSITA) folded into headline counts  [CONVERGENT 3/3: ChatGPT B1, Gemini B3, Grok M2] — VERIFIED-as-disclosed (overlaps C1/C2/C-RESIDUAL)
Source check (abstract L579–581): the 378,280 is labeled "explicitly exploratory"; LAMOST (~113k) explicitly EXCLUDED from the recommended subset; per-survey validity flags described. Verdict: disclosed. Residual = Gaia+eROSITA still inside the 269k "catalog-grade" label (C-RESIDUAL).

### C6 — IsolationForest not an independent cross-check / single-architecture dependence  [2/3: Gemini M3, ChatGPT M5] — Gemini M3 STALE; ChatGPT M5 VERIFIED-as-disclosed limitation
Source check (§sec:erosita L874): "284/298 = 95.3% ... a **descriptive internal-consistency overlap, not independent confirmation, since the IF is trained on the 16-d BigAE latent and the two detectors share the same learned representation**." The 95.3× independence-null enrichment was removed at v3.1.80 (META-M5). Verdict: Gemini M3 **STALE/FALSIFIED** (already reframed exactly as asked). ChatGPT M5 (no independent architecture confirmation for DESI/SDSS) is a real, **acknowledged** limitation (§VI.B model-dependence) — legitimate but disclosed, not a defect.

### Non-convergent MAJORs (single-provider), briefly
- ChatGPT M1 (non-uniform thresholds → rate is bookkeeping): VERIFIED-true & disclosed (Table V row h lists per-survey thresholds; abstract calls the total exploratory). OPINION on emphasis.
- ChatGPT M3 (17.8% novelty is DESI top-1000 only): VERIFIED-as-disclosed — abstract L579 says verbatim "a single-sample point estimate on the DESI top-1,000 score stratum, not a survey-wide rate."
- ChatGPT M4 / Grok m3 (cosmology over-attached): OPINION (placement). fNL null already led honestly.
- Gemini M1 (Gaia 41% stability → strip catalog-grade): VERIFIED-true & disclosed (§sec:gaia L899, "treat as exploratory"); feeds C-RESIDUAL.
- Gemini m4 / Grok m3 (fNL de-biased = zero improvement, abstract must lead with null): VERIFIED-as-disclosed — abstract L583 leads with "de-biased point estimate returns the single-tracer baseline σ=8.98 exactly (no multi-tracer improvement at current S/N)"; 9.4% explicitly "a noise-driven forecast ... not a detection."
- Gemini m1 (full-sample scaler leakage on tabular surveys): VERIFIED-as-disclosed (leakage direction disclosed §II.B, v3.1.92).

---

## C-RESIDUAL — the one real, actionable, convergent fix

**Gaia DR3 (500 obj, 5.2% recovery, 41% XV-stability, FAIL) and eROSITA DR1 (298 obj, 1.2% recovery, irreproducible axis, FAIL) are counted inside the number the paper labels "catalog-grade" (269,317 / 269,117 point-source).** 3/3 reviewers independently object that a tier labeled *catalog-grade* should not include components that fail the validation gate. This is the genuine load-bearing convergent ask. It is editorial (not a fabrication, and the flags are disclosed), and numerically tiny (798/269,317 ≈ 0.3%), but the **label is self-favoring**: "catalog-grade" overstates the validation status of two of its components.

### Exact .tex fix (honest open finding for P3)
In the abstract (L579) and §sec:pathc, add the clean validated-only count and lead with it:
- Compute and state the **validated-only count that excludes Gaia (500) + eROSITA (298)**: 269,117 − 798 = **268,319 point-source validated-only** (verify exact dedup-overlap before stamping; do the 6-way dedup recount rather than naive subtraction).
- Rename the 269,317 tier from "**catalog-grade**" to "**recommended tier (two components Gaia+eROSITA exploratory-flagged)**," OR keep "catalog-grade" but make it the validated-only 268k number and report Gaia+eROSITA as a separate exploratory addendum.
- Optionally (C2 emphasis): demote `~73×` and the inclusive `378,280` from the *title* to the body, leading the headline with the validated `269k`/`0.9×` framing. This is OPINION-tier but 3/3-supported.

No fabrication or suppression found. Do **not** classify C1/C2/C3 as integrity breaches — they are disclosed. Close C3 and Gemini M3 as STALE/FALSIFIED. Treat C-RESIDUAL as a genuine MINOR→editorial-MAJOR honest-framing fix.
