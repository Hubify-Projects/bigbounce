# Referee Handoff — P3 (Multi-Survey Anomaly Catalog)

`pipelines/p3_anomaly_engine/paper3_draft.tex` · slug `paper-3`

## Convergence status
P3 has reached the RS11 LLM-refereeing floor: **0 genuinely-new real findings**.
RS11 verdicts — **Grok MAJOR REVISIONS**, **Gemini REJECT**. The Gemini REJECT is the honest
outlier to weigh: it re-flags the eROSITA score-axis irreproducibility and the lost Gaia preprocessing
script — both of which the paper *already discloses* as exploratory-tier limitations, and both of which
concern components explicitly excluded from the validated headline. RS10's one genuinely-new item (a
LAMOST misread) was corrected this round — Gemini now reads it correctly ("author correctly sequesters"),
so that closure held. No new correctness defect.

## Recurring objections a human referee should adjudicate

1. **eROSITA score-axis non-reproducibility (drives the REJECT).**
   - Concern: per-object S_BigAE scores + the 0.259 production threshold are not recoverable across 16
     monotone rescalings; an uncommitted post-hoc step.
   - Disclosed: `sec:erosita` leads with membership-list-only + the 16-rescaling failure; caveat (h) and the
     Table IV caption quote the *reproducible* raw rank-298 cut (S_raw≥3.41) and label 0.259 as the
     irreproducible production label. eROSITA is exploratory-tier, excluded from the ≥268,519 validated headline.
   - Judgment call: **is a disclosed, sequestered, exploratory-tier score-axis non-reproducibility acceptable in
     a catalog paper (the released product is the committed membership list), or does a catalog paper require
     every tier fully reproducible?** (venue/scope — this is the crux of the REJECT)

2. **DESI dominance without injection-recovery.**
   - Concern: DESI (~73% of the count) ran no injection-recovery; "validated" = passed-gates-run.
   - Disclosed: `sec:desi` + caveat (i) + abstract lead with "no injection-recovery executed; robustness from
     5-fold J=0.862 + OOD J=0.732" citing `held_out_rescore_result.json`; no component is claimed an
     injection-recovery PASS unless stated (only SDSS + Planck are).
   - Judgment call: **are two Jaccard stability gates a sufficient robustness substitute for injection-recovery on
     the dominant component, for a catalog paper?** (editorial)

3. **Lost Gaia preprocessing lineage + illustrative cosmology sections.**
   - Concern: exact 20-feature Gaia script not recovered (lineage-inferred); f_NL/NANOGrav sections show no
     significant improvement.
   - Disclosed: §III.G / §training / data-availability all state the script is lineage-inferred; Gaia is
     exploratory, gate-FAIL, excluded from validated tier. Cosmology sections labeled "no improvement."
   - Judgment call: **honest provenance gap on an excluded exploratory tier — acceptable, or a hard integrity bar?**

## What is NOT in question
No genuinely-new correctness defect remains. The validated ≥268,519 headline is a 6-way dedup of the
injection-recovery- and stability-gated components only; the exploratory tiers are truthfully sequestered.
The RS10 LAMOST misread is corrected and the closure held.

## Recommended venue / next step
Submit to **ApJS** (catalog venue) with the eROSITA/Gaia exploratory-tier non-reproducibility disclosures flagged
to the editor as *by-design scope*, and the released committed products (membership lists, per-object catalogs)
foregrounded. Given the Gemini REJECT hinges entirely on disclosed exploratory-tier limitations, the honest
framing is: the validated tier stands independently; the exploratory tiers are labeled and separable.
