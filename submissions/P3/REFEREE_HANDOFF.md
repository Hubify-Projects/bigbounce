# Referee Handoff — P3 (Multi-Survey Anomaly Catalog)

`pipelines/p3_anomaly_engine/paper3_draft.tex` · slug `paper-3` · **current version: v3.1.132 (2026-07-02)**

## 2026-07-02 closures (new since 2026-07-01 handoff)

1. **DESI never-sensitivity-tested MAJOR — CLOSED** (commits `6b9db47f`, `da5f5e9f`, v3.1.130)
   - Full 5σ injection-recovery on real DESI-DR1 spectra completed and folded in.
   - Results: broad-class recovery 99–100% (3 injection gates); narrow-line injection floor
     ≥15σ (disclosed, not claimed as a pass). Gates validated at parity with SDSS and Planck
     injection-recovery.
   - The paper now carries real committed injection-recovery results for the dominant DESI
     component; "no injection-recovery executed" language updated to reflect the completed run.
   - Abstract / §III / `pathc_caveats(i)` updated for internal consistency (v3.1.132 reconciles
     a contradiction introduced when the fold-in was committed, commit `6d8d5b9c`).

2. **Scaler-leakage flag — CLOSED** (commit `4e1f918d`, v3.1.131)
   - Gemini RS10 flagged the 5-fold J=0.862 / OOD J=0.732 DESI gates as carrying full-sample
     scaler leakage. Audit of committed pipeline (`outputs/scaler_leakage_audit_2026-07-02.json`)
     confirmed the flag confuses two distinct P3 pipelines:
   - **Spectroscopic path** (DESI/SDSS/LAMOST/Planck): normalizes per-spectrum (each 496-bin
     vector / its own nonzero-bin median). A row-wise transform computed from each spectrum alone
     is split-independent → no train/held-out leakage. The J=0.862 / J=0.732 numbers are
     already leak-free and unchanged.
   - **Tabular-tier leakage** (eROSITA/NEOWISE/Gaia): a full-sample StandardScaler IS used on
     tabular tiers; this is already disclosed (Sec Training) and bounded by committed
     train-split-only refit control (`erosita_scaler_refit.json`): top-1% J(A,B)=0.643,
     confirming the tabular gates are not headline-load-bearing. The J=0.862 / J=0.732 headline
     is unaffected.

3. **§IID/§III internal consistency — CLOSED** (subsumed in v3.1.130/131/132 wave)
   - DESI injection-recovery fold-in resolved the prior §IID/§III inconsistency on DESI's
     validated status. The abstract summary block and §III/pathc_caveats now agree.

## Convergence status (as of RS11 / 2026-07-02 floor)

P3 has reached the LLM-refereeing floor: **0 genuinely-new real findings** across RS11.
RS11 verdicts — **Gemini REJECT, Grok MAJOR REVISIONS**. The Gemini REJECT re-flags the
eROSITA score-axis irreproducibility and the lost Gaia preprocessing script — both of which the
paper already discloses as exploratory-tier limitations excluded from the validated headline.
The RS10 LAMOST misread was corrected in RS10 closure and held through RS11 (Gemini now reads
it correctly: "author correctly sequesters"). No new correctness defect.

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
   - The prior "DESI ran no injection-recovery" MAJOR is **closed** by the 2026-07-02 results:
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
Given the Gemini REJECT hinges entirely on disclosed exploratory-tier limitations — and given
that the previously-absent DESI injection-recovery is now real and committed — the honest
framing is: the validated tier stands independently and is now more robustly grounded than
the 2026-07-01 floor.
