# Undersell vs Oversell Audit

**Created:** 2026-03-20
**Purpose:** Identify every instance of underselling or overselling across all public-facing and internal materials. Specific wording fixes included.

---

## Systematic Audit Table

| # | Result | Current Framing | Assessment | Evidence | Suggestion |
|---|--------|----------------|------------|----------|------------|
| 1 | ECH perturbation transparency | "ECH is perturbation-transparent" (various phrasings across gates and verdicts) | WELL_CALIBRATED | Stated as a chain of identities with 5 explicit steps in both bispectrum and tensor gate verdicts | Could be strengthened to "theorem-level closure" in paper framing, but current internal treatment is honest |
| 2 | 14-barrier map | INCONSISTENT: articles.html and explained.html still say "13 structural barriers"; CLAUDE.md says "13"; index.html, paper.html, figures.html, dossier, activity.html all say "14" | UNDERSOLD + INCONSISTENT | Grep confirms both counts live on the website and in internal docs | Standardize to 14 everywhere. The 14th barrier (perturbation-transparency as a closure in its own right) was added when the ECH bispectrum and tensor gates completed, but not all references were updated. More importantly: emphasize this is CLASS-LEVEL closure, not just a numbered list |
| 3 | f_NL = -35/8 benchmark | "Verified and forecasted" (Paper 3 description); "parameter-free prediction" | WELL_CALIBRATED | Correctly attributes to Cai et al. in all recent verdicts. Paper 3 title says "Testing the Matter Bounce" not "Our prediction." Draft claims table correctly classifies "we independently derived" as TOO_STRONG_DO_NOT_USE | No change needed. Calibration is right. |
| 4 | Inflation anti-mimicry | "Hard-to-mimic for inflation" (mimicry verdict); focused paper draft uses "simplest explanation" | SLIGHTLY_OVERSOLD | The mimicry verdict itself is honest (says "not impossible, but requires engineering"). But the focused paper draft claim #10 says "Bounce provides cleanest explanation" -- this needs qualification | Change "cleanest explanation" to "simplest zero-parameter explanation." Emphasize that single-field exclusion is trivial (Maldacena theorem); multifield is the real competition, and it survives with 2+ tuned parameters |
| 5 | ALP birefringence | "Surviving positive result" (dossier); "bounce-independent but ECH-motivated" (paper.html) | WELL_CALIBRATED | The bounce-independence caveat is prominently stated in the ECH tensor gate verdict, the bounce evidence audit, and paper.html | No change needed |
| 6 | "Cleanest explanation" language | Claim #10 in focused paper draft: "Bounce provides cleanest explanation" | CHECK: PRESENT | Found in `research/focused_paper_full_draft/02_claim_discipline_table.md` row 10, classified as ROBUST | This is SLIGHTLY_OVERSOLD. "Cleanest" implies a comparison that has not been made rigorously against ALL alternatives. The bounce model is not the "cleanest explanation" for anything yet -- it is an alternative hypothesis with a parameter advantage. Better: "provides a zero-parameter prediction where inflation requires two or more tuned parameters" |
| 7 | "Evidence for contraction" | Not found in any current HTML page | NOT_PRESENT | Grep of all .html files for "evidence for contraction" and "evidence for a.*contraction" returned no matches | Good. This dangerous phrasing has been avoided. |
| 8 | Branch V as "ECH bounce" | CLAUDE.md: "Branch V matter bounce + ECH: f_NL = 5/12"; dossier markdown 02_branch_registry.md: "dust contraction + ECH bounce predicts f_NL = 5/12"; dossier 06_novelty_assessment.md: "Branch V matter bounce + ECH framework" | OVERSOLD in places | The f_NL = -35/8 prediction comes from generic matter contraction + Bunch-Davies vacuum + standard GR perturbation theory. ECH provides only the bounce mechanism (singularity resolution). The prediction does not depend on ECH. | Change all "Branch V matter bounce + ECH" to "Generic matter-bounce benchmark (f_NL = -35/8)." ECH provides the existence proof for a nonsingular transition; the prediction itself is mechanism-independent. Dossier HTML already partially corrected (says "Parameter-free f_NL = -35/8 from explicit bounce mechanism") but markdown source files lag behind. |
| 9 | Single-point-of-failure | Acknowledged in focused paper final verdict, post-submission roadmap, and canonical status | WELL_CALIBRATED | The project honestly acknowledges that the entire observational program rests on f_NL. PBH + GW second channel was explored and killed (frequency gate). | This honesty is a STRENGTH. Keep it prominent. |
| 10 | f_NL = 5/12 holdover | Still in CLAUDE.md, dossier 02_branch_registry.md (row 27), dossier 05_results_matrix.md (row 27), dossier 01_project_timeline.md, dossier 00_master_index.md | FACTUALLY_WRONG | The correct value is f_NL = -35/8 = -4.375. The 5/12 figure was from an early Branch V estimate before the Cai action audit. The repo_wide_sync_audit explicitly flagged this as "WRONG" but the corrections were not propagated to all files. | MUST_FIX. This is not an oversell/undersell issue -- it is a factual error. All references to f_NL = 5/12 must be corrected to f_NL = -35/8. |
| 11 | SPHEREx significance | "4-6 sigma" (consistent everywhere) | WELL_CALIBRATED | Hardened forecasts with GR marginalization support this range | No change needed |
| 12 | MegaMapper significance | "3-7 sigma" with "8.75 sigma under ideal conditions" | WELL_CALIBRATED | Claims table correctly classifies the 8.75 sigma as CONDITIONAL | No change needed, but ensure the "under ideal conditions" caveat is always present when 8.75 sigma appears |
| 13 | Bayes factor > 300 | Used for bounce vs standard single-field inflation | WELL_CALIBRATED | This is actually conservative -- the true BF is > 10^8 against single-field and > 300 even under sigma_GR = 1.0 | No change needed |
| 14 | "Tension reduction" holdovers | Retracted in Paper 1.2 and explained.html | NEEDS_VERIFICATION | explained.html explicitly says the H_0 tension reduction claim "has been retracted." Paper.html Paper 1 scope mentions MCMC constraints with Delta-N_eff | Verify no positive tension-reduction claims survive anywhere. The retraction is present; ensure no holdover language contradicts it. |
| 15 | Hybrid DE rejection | "7 disguised forms, all rejected" | WELL_CALIBRATED | The next_flagship_program verdict documents all 7 forms | No change needed |
| 16 | LQC formalism sensitivity | "Structurally closed" (final_lqc_formalism_audit) | WELL_CALIBRATED | 60-order scale hierarchy argument is correct and clearly stated | No change needed |

---

## Specific Wording Fixes Needed

### Priority 1: Factual Corrections (MUST_FIX)

1. **CLAUDE.md line 20:** "Branch V matter bounce + ECH: f_NL = 5/12" --> "Generic matter-bounce benchmark: f_NL = -35/8 = -4.375 (parameter-free, SPHEREx 4-6 sigma)"

2. **research/project_master_dossier/02_branch_registry.md Branch V:** "f_NL = 5/12 (SPHEREx testable)" --> "f_NL = -35/8 (parameter-free, SPHEREx 4-6 sigma, Paper 3 complete)"

3. **research/project_master_dossier/05_results_matrix.md row 27:** "f_NL = 5/12" --> "f_NL = -35/8"; status "ACTIVE" --> "COMPLETE"

4. **research/project_master_dossier/01_project_timeline.md:** "f_NL = 5/12" --> "f_NL = -35/8"

5. **research/project_master_dossier/00_master_index.md:** "f_NL = 5/12" --> "f_NL = -35/8"

### Priority 2: Consistency Fixes (SHOULD_FIX)

6. **CLAUDE.md line 18:** "13 structural barriers" --> "14 structural barriers"

7. **CLAUDE.md line 32:** "13 barriers" --> "14 barriers"

8. **articles.html line 34:** "13 structural barriers" --> "14 structural barriers"

9. **explained.html line 291:** "13 structural barriers" --> "14 structural barriers"

10. **All dossier markdown references to "13 barriers"** --> "14 barriers" (07_publication_packaging_options.md, 08_open_questions_and_next_moves.md, 00_master_index.md)

### Priority 3: Framing Improvements (NICE_TO_HAVE)

11. **Anywhere "Branch V matter bounce + ECH"** --> "Generic matter-bounce benchmark (f_NL = -35/8); nonsingular transition demonstrated via ECH/LQC"

12. **Focused paper claim #10 "cleanest explanation"** --> "simplest zero-parameter explanation; inflation requires 2+ tuned parameters to reach same value"

13. **Any surviving "ECH predicts f_NL"** --> "Matter contraction produces f_NL = -35/8; ECH/LQC provides the nonsingular bounce mechanism"

---

## Summary Assessment

| Category | Count |
|----------|-------|
| WELL_CALIBRATED | 9 |
| SLIGHTLY_OVERSOLD | 2 |
| SLIGHTLY_UNDERSOLD | 1 |
| FACTUALLY_WRONG | 1 (f_NL = 5/12 holdover) |
| INCONSISTENT | 1 (13 vs 14 barriers) |

The project's calibration is generally good. The honest self-correction culture (retracted tension claims, acknowledged single-point-of-failure, bounce-independence of birefringence) is genuine and well-documented. The two main issues are: (a) stale f_NL = 5/12 in several markdown files that were not updated after the Cai action audit, and (b) inconsistent barrier count between old (13) and current (14) references. Both are correctable with a single find-and-replace session.
