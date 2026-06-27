# P3 R56 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R56_P3/paper3_draft.pdf` md5=08baa6e5 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (3053 chars)
**Wall time**: 304.8s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches”

Scope of review
- PRD methodology standards: statistical validity, estimator definition, derivation chains, effect-size reporting, dimensional consistency, internal arithmetic consistency, uncertainty propagation, and reproducibility.
- I read the full 30-page manuscript including figures, tables, equations, appendices, and the abstract. I recomputed all explicit ratios, percentages, and σ/p-values that are numerically checkable from the text.

Overall assessment
The paper presents an ambitious, multi-archive autoencoder anomaly survey at very large scale. There is substantial care in caveating transfer-learning pitfalls, providing stability metrics (Jaccard), and separating validated versus exploratory tiers. However, there are several methodology and reporting issues that do not meet PRD standards in the current form, notably: (i) an internally inconsistent masking/injection description in the NEOWISE gate; (ii) pervasive inclusion of run-log filenames and version tags in the body text; (iii) a “catalog-grade” headline that includes components that either fail the 5σ injection-recovery gate or are not reproducible; (iv) missing injection-recovery for the anchor DESI survey; (v) data availability placeholders; and (vi) an eROSITA scoring-axis inconsistency that crosses the “canonical S” nomenclature.

Below I list all findings. Severity classes: ESSENTIAL (must fix to be publishable), MAJOR (significant revision), MINOR (addressable in revision; not blocking), NIT (cosmetic).

Findings

P3-E1 (ESSENTIAL)
- Location: §III H (NEOWISE), p. 13; Fig. 10 caption, p. 22; Table I footnotes, p. 7–8
- Problem: Mask-geometry and “recovery” inconsistency. The text defines the catalog mask as |becl| < 80°, states that the raw anomalies include a 3.9% “polar-cap” fraction, and that an injection-recovery test plants synthetic sources at |becl| > {85°, 82°, 80.5°} and “recovers” them by applying the fixed catalog mask |becl| < 80°. This is contradictory: sources planted at |becl| > 80° lie in the polar caps and will be excluded by a |becl| < 80° mask. If “recovery” means “correctly excluded by the mask,” the success metric must be defined as the fraction removed, not “retained,” and this needs to be stated explicitly and consistently across the figure and text. At present, the sign of the inequality and the definition of recovery conflict.
- Required fix: Provide a precise, unambiguous definition of the NEOWISE mask selection and of “recovery” for the geometry QA gate. Use consistent inequalities in all places. If “recovered” = “removed by the mask,” state this explicitly and revise wording (“retains” vs “rejects”) and Fig. 10 caption accordingly. Include the exact numbers used in the calculation (k, n, p0) and make sure the 1000/1000 statement corresponds to the defined recovery event.

P3-E2 (ESSENTIAL)
- Location: Data availability, p. 23
- Problem: Data-release placeholders and future tense. The text says “will be publicly released with the arXiv posting,” “DOI will be minted at submission,” and references GitHub/HuggingFace without a stable DOI. PRD requires stable, citable data and code availability at acceptance, not promises.
- Required fix: Provide finalized, public DOIs (Zenodo or equivalent) for all data artifacts (catalogs, dedup manifests, chain files) and for the code. Replace future tense with present tense and include the exact DOIs and release tags. Remove “DOI inserted at submission” placeholders.

P3-E3 (ESSENTIAL)
- Location: Throughout; e.g., §II B p. 3; §III F p. 12; §IV C p. 16; Appendix E p. 26–27; numerous “pipelines/…/r23conf_*.json”, “r24conf_…”, “ext3_…”, “R54” strings
- Problem: Pervasive inclusion of internal run-log filenames, version tags, audit artifact paths (“r23conf”, “r24conf”, “ext3_fm1”, etc.) in the main text. PRD does not accept internal bookkeeping or version-history language in the body. These are distracting, brittle, and not peer-reviewable in the absence of immutable archives.
- Required fix: Move all internal file paths, run-log names, and version tags to a separate, citable online appendix or the data/code repository README. In the paper, replace with neutral references (e.g., “see Supplementary Table S1” or “see Data Release Manifest, DOI: …”). Remove all “conf”, “ext*”, and similar internal audit tags from the main text.

P3-E4 (ESSENTIAL)
- Location: Abstract p. 1; §II D p. 5–6; Table I footnotes p. 7–8; §VII Conclusions p. 22
- Problem: “Catalog-grade” tier includes components (Gaia and eROSITA) that do not clear the 5σ injection-recovery gate (Gaia 5.2%, eROSITA 1.2%) and, for eROSITA, have an irreproducible per-object score axis. Although flagged as “exploratory,” they are included in the 269,317 “catalog-grade” headline number in the abstract and conclusions. This is inconsistent with the term “catalog-grade.”
- Required fix: Either (a) exclude Gaia and eROSITA from the “catalog-grade” headline (and adjust all counts: 269,317 and 269,117) and reserve them for an exploratory appendix; or (b) rename the headline tier everywhere (abstract, text, tables, conclusions) to a neutral term such as “6-survey primary union (two exploratory components flagged)” and explicitly enumerate which components pass the sensitivity gate. The wording “catalog-grade” must be reserved for components that clear the stated validation criteria.

P3-E5 (ESSENTIAL)
- Location: §II D step 5 p. 5; §III A p. 6–8; §VI D (i) p. 21
- Problem: No injection–recovery test reported for DESI, the anchor survey. The text explicitly says, “DESI injection-recovery was not executed; its catalog robustness rests on the two Jaccard metrics.” For PRD methodology paper standards, the primary detection channel must be sensitivity-validated on the anchor dataset, not only stability-validated.
- Required fix: Execute and report a DESI injection–recovery test (continuum-dip and emission-line variants consistent with the SDSS/LAMOST tests), with identical 5σ gate criteria. Alternatively, explicitly downgrade DESI’s status in the headline claims and in the conclusions (and any “catalog-grade” designation), stating that DESI passes stability gates only and that sensitivity remains unquantified.

P3-E6 (ESSENTIAL)
- Location: §III E p. 10–11; Table I footnotes p. 7–8; Table I note “S > 0.259”
- Problem: Inconsistent nomenclature around eROSITA scoring axis. The paper shows that the published eROSITA SBigAE axis is irreproducible and that the membership list (n = 298) is canonical. However, Table I and subsequent text refer to “S > 0.259” and (later) “canonical-S top-298” in one place. This creates a logical inconsistency: eROSITA has no reproducible canonical-S axis in this paper.
- Required fix: Remove “S > 0.259” and any “canonical-S” references in the context of eROSITA. Consistently refer to the “membership-only top-298 list (ranked by committed raw-score artifact)” across the paper and tables. If an alternative reproducible axis (e.g., raw-score, retrained IF) is used for any comparison, label it explicitly and do not conflate it with canonical S.

P3-E7 (ESSENTIAL)
- Location: Abstract p. 1–2; §VII Conclusions p. 22
- Problem: Multiple “version-history”/“cross-transfer baseline preserved” statements (“quarantined,” “preserved as historical-baseline record,” etc.) appear in what should be a clean, final scientific narrative. PRD requires the abstract and conclusions to summarize final, reproducible results only.
- Required fix: Remove all baseline/run-history language from the abstract and conclusions. Keep cross-transfer baseline material in a dedicated appendix (as partly done for ACT) and ensure the abstract/conclusions only report Path-C native, reproducible results.

P3-M1 (MAJOR)
- Location: Table I and caption/footnotes, p. 7–8
- Problem: Table I conflates cross-transfer and native-retrained rates and thresholds within a single table row, relying on very long footnotes to disambiguate. The “Rate (%)” column for SDSS reflects the cross-transfer rate (3.38%) while the native continuity-slice is 4.05% on a different denominator. This will confuse readers and invites misquotation.
- Required fix: Split Table I into two tables: (i) cross-transfer baseline (clearly marked as non-science, verification only), and (ii) Path-C native-retrained results (primary). Ensure the “Rate (%)” column in the primary table reflects only native-retrained denominators and cuts. Move all cross-transfer counts, SDSS “continuity slice,” and LAMOST transfer baselines to the baseline table or appendices.

P3-M2 (MAJOR)
- Location: §II D p. 5; §VI D (ii) p. 22; gate thresholds throughout
- Problem: Validation gate thresholds (val-loss ≤0.30; ≥50% injection–recovery at 5σ; Jaccard ≥0.70/0.50) are acknowledged as heuristic and not preregistered. The text argues insensitivity because most pass/fail margins are wide, except SDSS’s 64% vs 50%. For PRD, a short, formal sensitivity analysis to threshold variation should be included.
- Required fix: Add a sensitivity analysis showing that small-to-moderate changes to gate thresholds (e.g., 40–60% at 5σ; Jaccard gates ±0.05; val-loss halved/doubled) do not flip pass/fail outcomes except where explicitly noted. Present this compactly in a table or figure.

P3-M3 (MAJOR)
- Location: §III E p. 10–11; Table IV p. 12
- Problem: eROSITA contributes statistics (e.g., 68% SIMBAD-unmatched) but lacks a reproducible per-object score axis and fails the 5σ injection–recovery gate. Although labeled membership-only and exploratory, these numbers are highlighted alongside validated tiers in multiple places.
- Required fix: Consistently segregate eROSITA results as exploratory in all summaries, figures, and conclusions; avoid including them in any pooled statistics unless the pooling is recomputed both with and without eROSITA and labeled accordingly.

P3-M4 (MAJOR)
- Location: §V b (Fisher forecast) p. 17; §VI C (4), p. 20
- Problem: GR projection-correction bound “|Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1” is labeled as an “internal order-of-magnitude bound” without a derivation or external reference. For PRD, bounds must be either derived in-text or supported by a citable calculation.
- Required fix: Provide a brief derivation or a citation to a calculation showing that the GR terms at the Fisher-weighted scales produce the quoted fractional change in σ(fNL), or remove the quantitative bound and replace with a qualitative statement.

P3-M5 (MAJOR)
- Location: §III A p. 6–8; §VII p. 22
- Problem: The strong claim that the DESI B-dominant subset (≈22.7%) may be a calibration artifact is plausible but currently unsupported by any direct test. The text proposes a diagnostic (e.g., u−g colors) but does not perform it.
- Required fix: Either (a) perform and report a simple photometric cross-check (color cuts or external flags) to test whether the B-dominant subset correlates with known calibration/systematic axes; or (b) soften the claim to a hypothesis and remove the “consistent with” language from the conclusions until tested.

P3-M6 (MAJOR)
- Location: §V (multi-tracer fNL), p. 17–19; §VII p. 22
- Problem: The paper juxtaposes several “σ” values from different null procedures (empirical αjk → Fisher σ(fNL), prior fixed-α forecast, and NANOGrav parameter-shift σ for γ) across sections. While local caveats exist, a reader could still misinterpret them as directly comparable improvements/detections.
- Required fix: At every place where two different “σ” values are juxtaposed (e.g., empirical σ(fNL) envelope and the NANOGrav +1.13σ parameter shift; or the fixed-α vs empirical σ(fNL) lines), add explicit, in-line “not directly comparable” qualifiers. The conclusions already contain such a caveat; extend this practice consistently wherever the numbers are adjacent.

P3-M7 (MAJOR)
- Location: §III G (Gaia) p. 12–13; Table I p. 7–8
- Problem: Gaia preprocessing script for the production run is not recoverable; stability is low (41%), and yet Gaia is included in the “catalog-grade” headline (see P3-E4). This presents a reproducibility issue.
- Required fix: Either (a) reconstruct the exact production preprocessing (or replace with a fully recoverable preprocessing and re-run, then report stability), or (b) exclude Gaia from the catalog-grade/headline tier and segregate as exploratory with a clear label across the paper.

P3-M8 (MAJOR)
- Location: §IV A (novelty), p. 13–14; Fig. 6 p. 15; Abstract p. 1
- Problem: The genuine novelty fraction 17.8% (178/1000) is a top-stratum point estimate and correctly caveated locally. However, the abstract and conclusions present it as a headline without immediately reminding readers that it pertains only to the DESI top-1000 stratum.
- Required fix: In the abstract and conclusions, append “measured on the DESI top-1000 score stratum only; not a survey-wide rate” to the novelty sentence, mirroring the careful wording already used in §IV A.

P3-M9 (MAJOR)
- Location: §III F (Planck), p. 11–12
- Problem: The Planck top-200 are scored on a set that includes training patches (not held out). While you state this clearly, the anomaly list should then also include and mark which patches were in the training split (152/200 reported). For PRD reproducibility, readers should receive a patch-level training/validation flag.
- Required fix: Add a per-patch flag in the released Planck tier indicating whether the patch was in the training or validation split. Mention this explicitly in the data-release summary.

P3-M10 (MAJOR)
- Location: §III C and Table III p. 11–12
- Problem: The SDSS taxonomy in Table III is computed on the cross-transfer anomaly set, not the native slice. The caption mentions this, but the main text uses this taxonomy to characterize the SDSS anomalies broadly.
- Required fix: Add a one-sentence, in-body clarification near §III C that the reported taxonomy quantifies the transfer-learning failure mode and should not be read as the physical census of the native-retrained SDSS tier. If possible, provide at least a brief summary taxonomy for the native SDSS continuity slice (even if coarse), or clearly state that it is not computed.

P3-M11 (MAJOR)
- Location: Abstract p. 1
- Problem: “largest application of autoencoder anomaly detection by total sources processed … of which we are aware” is a priority/novelty claim. The paper anchors the size benchmark to [11], but does not survey broader autoencoder anomaly catalogs (beyond SDSS/DESI) that might use different data domains.
- Required fix: Rephrase to “to our knowledge, larger than the largest published single-survey anomaly catalog we benchmark against [11]” and restrict the claim scope accordingly.

P3-M12 (MAJOR)
- Location: §IV B (spatial uniformity), p. 14–15
- Problem: The χ² uniformity test assumes a uniform per-occupied-pixel mean with Poisson variance but does not provide the counts k (bins) used in the χ² normalization within the text (although I could infer k=24,049). For PRD, state the exact k and N used in the χ² and Cramér’s V calculations and provide a short rationale for the choice of “occupied pixels only.”
- Required fix: Add the explicit values (k, N) and a sentence motivating the occupied-pixels restriction; otherwise, report the full-footprint χ² as a secondary check.

P3-M13 (MAJOR)
- Location: §IV C (dedup radius sweep), p. 15–16
- Problem: The dedup sensitivity sweep gives unique-counts 378,604 / 378,280 / 378,145 for 3″/5″/7″. The text reports a maximum relative change of 0.086%, which matches (324/378,280). However, the text also lists multi-survey clusters as 619/637/661 without reconciling that these numbers correspond to the same sweep. To assist reproducibility, provide a compact table or an appendix entry tying unique-counts, multi-survey clusters, and intra-survey duplicates for each radius.
- Required fix: Add a small table or pointer to a DOI’d artifact listing these quantities for each radius.

P3-M14 (MAJOR)
- Location: §III A (DESI) p. 6–8; Table II p. 9
- Problem: The DESI science-class recount is careful but mixes denominators (full-stream 22.5M, science-bit 20.3M rows, validated-TARGETTYPE ~6.5M). It is currently correct, but the reader must jump across paragraphs/tables to track denominators.
- Required fix: Add a one-paragraph “Denominator map” at the end of §III A that explicitly enumerates the four denominators with their corresponding rates, as you do in Table II, keeping the narrative self-contained.

P3-Min1 (MINOR)
- Location: §II B p. 3–4; Eq. (2)
- Problem: For DESI, μval is given (0.0287) but σval is not. The reported S>5 threshold MSE ≈ 0.143 implies σval ≈ 0.02286. Including σval values for DESI (and optionally the other native-retrained surveys) would improve reproducibility.
- Required fix: Report σval for DESI (and optionally for other native retrains) in a small table or footnote.

P3-Min2 (MINOR)
- Location: §IV A p. 13–14
- Problem: Expected false-match calculation for SIMBAD at 5″ uses a global source density nSIMBAD ≈ 3.0×10−5 arcsec−2; you then note spatial non-uniformity. Provide a one-line formula Pfalse = π r² n and state that for r=5″ this gives Pfalse≈2.36×10−3; the text’s 2.4×10−3 matches this but the explicit formula would help readers replicate.
- Required fix: Add the explicit formula in-line.

P3-Min3 (MINOR)
- Location: §III F p. 12; Table VI footnote p. 24
- Problem: The Planck injection amplitude convention (standardized-patch units, no post-plant renormalization) is good but easy to miss. Consider pulling that sentence from the table footnote into the main text for visibility.
- Required fix: Move or duplicate the amplitude-convention sentence into §III F.

P3-Min4 (MINOR)
- Location: Figures 1–12, various pages
- Problem: Some figure captions could be more explicit about axes units (e.g., Fig. 1 colorbar is S units; Fig. 3 right is “S” on log–log but the y-axis label could state “probability density” explicitly).
- Required fix: Minor caption edits to ensure all axes and colorbars have units or qualitative labels.

P3-N1 (NIT)
- Location: Throughout
- Problem: Occasional overuse of “exactly” (e.g., “returns … exactly”) where values are rounded.
- Required fix: Tweak wording to “returns … to within rounding” or omit “exactly.”

P3-N2 (NIT)
- Location: Linebreak hyphenation artifacts (e.g., “per￾survey,” “per￾object”) likely from PDF extraction.
- Required fix: Proofread final typeset version to remove hyphenation artifacts.

Arithmetic checks performed (representative)
- DESI anomaly rate: 195,829 / 22,504,897 = 0.87%.
- DESI science-bit fraction: 2,468 / 190,015 = 1.30%.
- Science-bit rate on 20,299,155 denominator: 2,468 / 20,299,155 = 0.0122%.
- “∼6500× rate compression” SDSS: 77,905 / 12 = 6,492.
- LAMOST 21.5× rate compression (S>5): 44,075 / 2,054 = 21.46.
- Path-C sum of native-retrained detections: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; dedup 388,493 − 10,213 = 378,280.
- Catalog-grade = 378,280 − 108,963 (LAMOST-only contributions) = 269,317; point-source = 269,317 − 200 = 269,117.
- “∼141×” prior catalog: 378,080 / 2,685 = 140.8.
- DESI “∼73×”: 195,829 / 2,685 = 72.9.
- Novelty fraction: 178/1,000 = 17.8%; binomial σ ≈ sqrt(p(1−p)/n) ~ 1.21% (matches “±1.2%”).
- NEOWISE polar-cap excess: expected cap area fraction f = 1 − cos 10° ≈ 0.0152; observed 17/436 = 0.0390 ⇒ 2.56×; z ≈ (17 − 6.64)/sqrt(6.54) ≈ +4.05 (p ~ 5×10−5).
- Fisher positivity form: with F0 = 1/8.98² ≈ 0.01239, c=0.0747, α=0.19 gives σ(fNL) = 8.14; envelope [3.92, 8.98] using α±σ and α≥0 clipping.
- NANOGrav γ shifts: (3.0 − 2.567)/0.382 = +1.13σ; (4.33 − 2.567)/0.382 = +4.61σ; Bayes factor ratio 3.23 / (4.52×10−4) = 7.14×10^3.

Length and focus
The paper (30 pages) is long for the claimed contribution. Much of the baseline/run-log detail and many internal-file-path annotations should move to an online supplement or a data/code README. A lean main text focused on the validated Path-C native results, with a clean, reproducible method and results narrative, would likely fit within 20–22 pages.

## Summary recommendation
MAJOR REVISIONS

The work is ambitious and many core numbers check out, but several issues prevent publication in PRD as-is: (1) an internally inconsistent NEOWISE masking/injection description; (2) headline “catalog-grade” counts include components that are either irreproducible or fail sensitivity gates; (3) missing DESI injection–recovery; (4) pervasive inclusion of internal run-log/version artifacts; (5) data availability placeholders; and (6) an eROSITA scoring-axis nomenclature inconsistency. Addressing the ESSENTIAL and MAJOR items above, and trimming the main text to focus on validated, reproducible results with finalized DOIs, would bring the paper in line with PRD methodology standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (new items only)

P3-M15 (MAJOR)
- Location: Table I (Planck row) vs §III F
- Problem: In the primary per-survey table, Planck’s Ntotal is 20,000 and the “Rate” column reports 1.00% (top-200/20,000), but the released tier is explicitly the top-200 of a 2×10^5 native re-score bank (0.10%). A footnote explains the bookkeeping, but presenting a cross-transfer denominator in the main results table is misleading and invites misquotation.
- Required fix: In the primary “Path-C native” table, replace Planck’s denominator with the native 2×10^5 bank and list the corresponding 0.10% bookkeeping rate, or leave the Rate cell blank/“fixed-count” with a clear note. Move the 20,000-patch cross-transfer rate to the baseline table (see P3-M1).

P3-M16 (MAJOR)
- Location: Title and Abstract
- Problem: The title phrase “a Native-Trained Novelty Fraction” and the abstract’s headline novelty sentence can be read as a survey-wide/native-multi-archive metric, but the only quantified novelty fraction (17.8%) is measured on the DESI top-1,000 score stratum only.
- Required fix: Qualify in the title or abstract that the quantified novelty fraction is measured on the DESI top-1,000 anomalies (not survey-wide or multi-archive), or rephrase to “a measured novelty fraction on the DESI top-1,000 score stratum.”

P3-Min5 (MINOR)
- Location: §IV B (spatial analysis), p. 14–15
- Problem: Cramér’s V algebraic presentation drops the square root in the numerical step. The text reads “Cramér’s V = √[χ²/(N·(k−1))] = 376,713/(378,280 × 24,048) ≈ 0.0064.” The middle equality (a plain ratio) equals ~4.1×10−5, not 0.0064; the final 0.0064 is the square-rooted value.
- Required fix: Correct the displayed numerical step to include the square root explicitly: V = √(376,713/(378,280×24,048)) ≈ 0.0064.

P3-Min6 (MINOR)
- Location: Appendix E, Eq. (E1)
- Problem: Dimensional clarity in logs. Eq. (E1) writes separate terms like log10 f_yr, log10 f_i, log10 Tobs. Logs of dimensionful quantities should be expressed as logs of explicit ratios to reference units (e.g., log10(f_i/f_yr), log10(Tobs/1 yr)) to avoid ambiguity.
- Required fix: Rewrite Eq. (E1) using explicit dimensionless ratios (e.g., (f_i/f_yr)^−γ, (Tobs/1 yr)−1), or add a sentence defining these terms as logs of ratios to the stated reference scales.

P3-Min7 (MINOR)
- Location: §IV A (archival matching), p. 13–14
- Problem: Two different random-match controls are used/described in close proximity: an analytic expectation at 3″ for DESI×SDSS (~2.3) and an empirical RA-shift control that yields 2.75 expected (also at 3″). The text warns these are heuristics, but the mix of methods obscures the baseline used for the 4 observed matches in the released catalogs.
- Required fix: Present a single, consistent baseline for the DESI×SDSS 3″ comparison in the main text (analytic or RA-shifted), and move the alternative to a supplement. Report both n, r, and method in one place (and keep the final comparison anchored to the same control used for the quoted 4 observed matches).