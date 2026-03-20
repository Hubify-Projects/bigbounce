# Final Improvement Stack

**Created:** 2026-03-20
**Purpose:** Ranked list of all improvements needed before submission/release. Each item has impact, effort, and specific instructions.

---

## Rank 1: Fix ECH-Specific Language --> Generic Matter-Bounce

**Impact: HIGH.**
**Effort: 1 session (find-and-replace + manual review).**

Everywhere "Branch V + ECH" or "ECH predicts f_NL" or "ECH bounce produces" appears in public-facing or internal materials, change to "generic matter-bounce" or "matter contraction dynamics."

### Why this matters
A reviewer will immediately ask: "If f_NL = -35/8 is generic to any matter contraction, why is this paper about ECH?" The answer is: ECH provides the existence proof for the nonsingular transition, but the prediction is mechanism-independent. This must be stated clearly, not implied.

### Specific files to change

| File | Search Pattern | Replace With |
|------|---------------|--------------|
| CLAUDE.md | "Branch V matter bounce + ECH: f_NL = 5/12" | "Generic matter-bounce benchmark: f_NL = -35/8 (parameter-free, SPHEREx 4-6 sigma)" |
| research/project_master_dossier/02_branch_registry.md | "ECH bounce predicts f_NL = 5/12" | "matter contraction produces f_NL = -35/8; ECH provides nonsingular transition" |
| research/project_master_dossier/05_results_matrix.md row 27 | "f_NL = 5/12" | "f_NL = -35/8" |
| research/project_master_dossier/06_novelty_assessment.md | "Branch V matter bounce + ECH framework" | "Generic matter-bounce benchmark framework" |
| research/project_master_dossier/01_project_timeline.md | "ECH bounce predicts f_NL = 5/12" | "matter contraction produces f_NL = -35/8" |
| research/project_master_dossier/00_master_index.md | "f_NL = 5/12" | "f_NL = -35/8" |
| Any paper draft | "ECH predicts" + f_NL context | "matter contraction produces" |

### Test after change
Grep all .html and .md files for "ECH predicts f_NL" and "f_NL = 5/12". Both should return zero matches.

---

## Rank 2: Standardize Barrier Count to 14

**Impact: MEDIUM.**
**Effort: LOW (find-and-replace).**

Some pages say 13, some 14. The correct count is 14, which includes the perturbation-transparency theorem as the 14th barrier (it closes the ECH perturbation program as a whole, beyond the 13 mechanism-specific barriers).

### Specific files to change

| File | Current | Target |
|------|---------|--------|
| CLAUDE.md (2 locations) | "13 structural barriers" / "13 barriers" | "14 structural barriers" / "14 barriers" |
| articles.html line 34 | "13 structural barriers" | "14 structural barriers" |
| explained.html line 291 | "13 structural barriers" | "14 structural barriers" |
| research/project_master_dossier/07_publication_packaging_options.md (3 locations) | "13 barriers" | "14 barriers" |
| research/project_master_dossier/08_open_questions_and_next_moves.md (2 locations) | "13 barriers" | "14 barriers" |
| research/project_master_dossier/00_master_index.md | "13 barriers" | "14 barriers" |

### Test after change
Grep all .html and .md files for "13 barrier" and "13 structural". Both should return zero matches (or only in historical/archive contexts).

---

## Rank 3: Frame Paper 3 Novelty as "First Complete Observational Test Design"

**Impact: HIGH.**
**Effort: LOW (abstract + intro rewrite for Paper 3).**

The paper's value is the integrated analysis, not the coefficient. The abstract should lead with:

> "Can upcoming galaxy surveys distinguish bounce cosmology from inflation using primordial non-Gaussianity? We present the first comprehensive observational program for testing the matter-bounce prediction f_NL^local = -35/8 (Cai et al. 2009), combining multi-survey Fisher forecasts, dominant systematic identification, and Bayesian model comparison across 800,000 Monte Carlo realizations."

NOT:

> "We verify f_NL = -35/8 and forecast its detection."

### Specific changes
1. Paper 3 abstract: rewrite opening to lead with science question
2. Paper 3 introduction: credit Cai et al. in first paragraph
3. Paper 3 discussion: emphasize the integrated analysis as the contribution

---

## Rank 4: Strengthen Perturbation-Transparency Theorem Framing in Paper 1

**Impact: MEDIUM.**
**Effort: LOW (add boxed theorem, name it).**

The perturbation-transparency theorem is currently stated but not given formal treatment. It deserves:

1. A NAME: "ECH Perturbation-Transparency Theorem" or "Spin-Torsion Perturbation-Transparency Theorem"
2. A BOXED STATEMENT in the paper:

> **Theorem (Perturbation Transparency).** In minimal Einstein-Cartan-Holst gravity coupled to a canonical scalar field, torsion vanishes identically at all perturbation orders. The Holst term reduces to a topological density (the Pontryagin class), contributing zero to the equations of motion. Consequently, the Barbero-Immirzi parameter gamma is completely invisible in all scalar and tensor perturbation observables.

3. An explicit NOTE that this makes generic bounce predictions MORE ROBUST (mechanism-independent), not less interesting.

---

## Rank 5: Paper 2: Benchmark Against Existing ALP Literature

**Impact: HIGH for Paper 2 specifically.**
**Effort: MEDIUM (requires literature comparison table).**

Paper 2 must contain a comparison with:
- Fujita, Minami, Murai (2021) -- original ALP birefringence prediction at this parameter scale
- Obata (2022) -- axion monodromy birefringence
- Eskilt et al. (2023) -- Planck/ACT combined analysis

The comparison table should show what our analysis adds:
- Combined Planck + ACT data (their analyses may have used only Planck 2018)
- Full MCMC with Bayes factor (they may have used only Fisher/analytic estimates)
- Quantitative LiteBIRD forecast with sigma
- Explicit f_photon consistency check

If our contribution reduces to "MCMC implementation + updated data + quantified LiteBIRD forecast," state that clearly. This is sufficient for a short focused paper but should not be oversold.

---

## Rank 6: Update Dossier Markdown Files

**Impact: LOW-MEDIUM.**
**Effort: LOW (find-and-replace + add rows).**

The dossier HTML (index.html) is mostly current, but the markdown source files have stale data:

1. f_NL = 5/12 in 5 markdown files (factual error)
2. Branch V status ACTIVE instead of COMPLETE
3. Branch Vb status ACTIVE instead of COMPLETE
4. Branch R status ACTIVE instead of COMPLETE
5. Missing results: Cai audit, Bayesian discrimination, inflation mimicry, Wilson-Ewing viability, convention resolution, focused paper completion
6. 13 barriers in 3 files

Lower priority because the HTML is the public-facing version. But future agents consulting markdown will inherit errors.

---

## Rank 7: Verify No Tension-Reduction Holdovers

**Impact: LOW (probably already clean).**
**Effort: LOW (grep check).**

The original Paper 1 claimed H_0 tension reduction. This was retracted. Verify:
1. No positive tension-reduction claims survive in any .html file
2. explained.html retraction language is present and unambiguous
3. Paper 1 (arxiv/main.tex) does not contain positive tension claims
4. The MCMC section clearly states Delta-N_eff = 0

This is likely already clean based on the extensive revision history, but a final grep is worthwhile.

---

## Rank 8: Address Paper 2 Miscalibration Degeneracy

**Impact: MEDIUM for Paper 2.**
**Effort: LOW (one paragraph).**

The birefringence signal can be mimicked by instrumental miscalibration in Planck data. This is the biggest threat to the birefringence interpretation. Paper 2 should contain an explicit paragraph acknowledging this degeneracy and noting that LiteBIRD's design specifically mitigates it.

---

## Summary Table

| Rank | Improvement | Impact | Effort | Type |
|------|-----------|--------|--------|------|
| 1 | Fix ECH-specific language to generic | HIGH | 1 session | MUST_DO |
| 2 | Standardize barrier count to 14 | MEDIUM | LOW | MUST_DO |
| 3 | Paper 3 novelty framing | HIGH | LOW | MUST_DO |
| 4 | Name and box the perturbation-transparency theorem | MEDIUM | LOW | SHOULD_DO |
| 5 | Paper 2 literature benchmark | HIGH (for Paper 2) | MEDIUM | MUST_DO |
| 6 | Update dossier markdown files | LOW-MEDIUM | LOW | SHOULD_DO |
| 7 | Verify no tension-reduction holdovers | LOW | LOW | SHOULD_DO |
| 8 | Paper 2 miscalibration paragraph | MEDIUM (for Paper 2) | LOW | SHOULD_DO |

**Total effort for all MUST_DO items: approximately 2-3 focused hours.**
**Total effort for all SHOULD_DO items: approximately 1-2 additional hours.**
