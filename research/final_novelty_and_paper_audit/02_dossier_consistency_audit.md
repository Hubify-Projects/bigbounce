# Dossier Consistency Audit

**Created:** 2026-03-20
**Purpose:** Systematic check of the project dossier (markdown source files + HTML dashboard) for inaccuracies, stale data, and ECH-specific language that should be generic.

---

## 1. Inaccuracies Found

### 1.1 f_NL = 5/12 Holdovers (FACTUAL ERROR)

| File | Line/Location | Current Text | Should Be |
|------|--------------|--------------|-----------|
| `02_branch_registry.md` Branch V | One-line significance | "f_NL = 5/12 (SPHEREx testable), low-ell cutoff" | "f_NL = -35/8 = -4.375 (parameter-free, SPHEREx 4-6 sigma)" |
| `05_results_matrix.md` Row 27 | Result column | "f_NL = 5/12 (parameter-free); SPHEREx 2.5-sigma" | "f_NL = -35/8 (parameter-free, 3 methods); SPHEREx 4-6 sigma" |
| `01_project_timeline.md` | Branch V entry | "f_NL = 5/12 (SPHEREx at 2.5-sigma)" | "f_NL = -35/8 (SPHEREx 4-6 sigma)" |
| `00_master_index.md` | Branch V summary | "f_NL = 5/12, testable by SPHEREx" | "f_NL = -35/8, testable by SPHEREx at 4-6 sigma" |
| `06_novelty_assessment.md` Branch V entry | Rating justification | "Parameter-free f_NL = 5/12 from ECH-mediated bounce" | "Parameter-free f_NL = -35/8 from matter contraction; ECH provides nonsingular transition" |

**Note:** The dossier HTML (index.html) has been partially corrected -- it reads "f_NL = -35/8" for Branch V. But the source markdown files still contain the old 5/12 value.

### 1.2 Barrier Count Inconsistency

| File | Current | Correct |
|------|---------|---------|
| `07_publication_packaging_options.md` (3 places) | "13 barriers" | "14 barriers" |
| `08_open_questions_and_next_moves.md` (2 places) | "13 barriers" | "14 barriers" |
| `00_master_index.md` (1 place) | "13 barriers" | "14 barriers" |

The dossier HTML uses 14 consistently. Only the markdown source files lag.

### 1.3 Status Errors

| File | Item | Current Status | Correct Status |
|------|------|---------------|----------------|
| `05_results_matrix.md` Row 27 | Branch V | ACTIVE | COMPLETE (Paper 3 drafted, all calculations done) |
| `05_results_matrix.md` Row 28 | Branch Vb | ACTIVE | COMPLETE (perturbation-transparency theorem proven) |
| `02_branch_registry.md` Branch V | Status | "ACTIVE (Phase 1 to begin)" | COMPLETE |
| `02_branch_registry.md` Branch Vb | Status | ACTIVE | COMPLETE |
| `02_branch_registry.md` Branch R | Status | "ACTIVE / PROMISING" | COMPLETE (Paper 2 drafted) |

### 1.4 Missing Results from Focused-Path Work

The following results, completed after the dossier was initially written, are NOT reflected in the dossier markdown files:

| Missing Result | Should Appear In | Location |
|----------------|-----------------|----------|
| Cai action audit (3 mismatches resolved) | 05_results_matrix.md | New row or Branch V update |
| Bayesian discrimination (BF > 300) | 05_results_matrix.md | New row |
| GR marginalization framework | 05_results_matrix.md | New row or Paper 3 update |
| Inflation mimicry comparison | 05_results_matrix.md | New row |
| Focused paper draft completion | 02_branch_registry.md | Paper 3 entry or update to Paper-1.2 |
| 800,000 MC realizations | 05_results_matrix.md | New row or forecast update |
| LQC formalism sensitivity closure | 08_open_questions_and_next_moves.md | Remove from "open" list |
| PBH + GW channel death | 08_open_questions_and_next_moves.md | Add to closed list |
| Wilson-Ewing viability filtering | 05_results_matrix.md | New row |
| Convention resolution (no hidden factor) | 05_results_matrix.md | Note under Cai audit row |

The dossier HTML (index.html) incorporates most of these. The markdown source files do not.

---

## 2. ECH-Specific Overhang

Places where the dossier still uses ECH-specific language for what is now a generic matter-bounce result:

### In 02_branch_registry.md

| Location | Current | Recommended |
|----------|---------|-------------|
| Branch V title | "Branch V -- Bounce Evidence Program (Matter Bounce + ECH)" | "Branch V -- Matter-Bounce f_NL Benchmark" |
| Branch V significance | "FLAGSHIP: dust contraction + ECH bounce predicts f_NL = 5/12" | "FLAGSHIP: generic matter contraction predicts f_NL = -35/8; ECH/LQC provides nonsingular transition" |
| Branch V goal | "Identify minimal extensions producing detectable bounce signatures" | "Package the generic matter-bounce f_NL prediction into a complete observational test" |

### In 05_results_matrix.md

| Location | Current | Recommended |
|----------|---------|-------------|
| Row 27, Branch | "Branch-V" | Keep, but update significance column |
| Row 27, One-Line Significance | "Flagship: explicit bounce mechanism with testable predictions" | "Flagship: generic matter-bounce f_NL = -35/8 tested against inflation; SPHEREx 4-6 sigma" |

### In 06_novelty_assessment.md

| Location | Current | Recommended |
|----------|---------|-------------|
| Branch V entry | "Branch V matter bounce + ECH framework" with N3 rating | Keep N3 for the integrated framework, but note that the f_NL prediction itself is N2 (verified, not discovered) |
| Contingency note | "Contingent on Phase 1 calculation succeeding" | Remove -- Phase 1 is complete, calculation succeeded |

### In 01_project_timeline.md

| Location | Current | Recommended |
|----------|---------|-------------|
| Branch V entry | "ECH bounce predicts f_NL = 5/12" | "Matter contraction produces f_NL = -35/8; ECH provides existence proof for nonsingular transition" |

### In 00_master_index.md

| Location | Current | Recommended |
|----------|---------|-------------|
| Branch V summary | "Matter bounce + ECH ... f_NL = 5/12" | "Generic matter-bounce benchmark f_NL = -35/8, verified from 3 methods, SPHEREx 4-6 sigma" |
| Top-value assets | Check for "Branch V matter bounce + ECH" | Update to "Generic matter-bounce forecast package" |

---

## 3. Recommended Edits (Prioritized)

### MUST_DO (Factual Errors)

1. **Update 05_results_matrix.md Row 27:** f_NL from 5/12 to -35/8; status from ACTIVE to COMPLETE; significance updated; SPHEREx from 2.5-sigma to 4-6 sigma.

2. **Update 05_results_matrix.md Row 28:** Branch Vb status from ACTIVE to COMPLETE (perturbation-transparency proven).

3. **Update 02_branch_registry.md Branch V:** All fields updated with correct f_NL value, COMPLETE status, revised significance.

4. **Update 02_branch_registry.md Branch Vb:** Status to COMPLETE.

5. **Update 02_branch_registry.md Branch R:** Status to COMPLETE (Paper 2 drafted).

### SHOULD_DO (Consistency)

6. **Standardize barrier count to 14** in 07_publication_packaging_options.md, 08_open_questions_and_next_moves.md, 00_master_index.md.

7. **Update 06_novelty_assessment.md:** Remove "contingent on Phase 1" note for Branch V. Update f_NL value.

8. **Update 01_project_timeline.md:** Correct Branch V entry.

9. **Update 00_master_index.md:** Correct Branch V summary.

### NICE_TO_HAVE (Completeness)

10. **Add new rows to 05_results_matrix.md** for: Cai action audit, Bayesian discrimination, inflation mimicry, Wilson-Ewing viability, convention resolution, focused paper completion.

11. **Update 08_open_questions_and_next_moves.md:** Remove LQC formalism from open list (now closed). Add PBH + GW to dead list. Note focused paper completion.

12. **Fix all ECH-specific language** in generic-benchmark entries across all dossier markdown files.

---

## 4. Dossier HTML vs Markdown Sync Status

The dossier HTML (research/project_master_dossier/index.html) is MORE up-to-date than the markdown source files. Specifically:

| Feature | HTML Status | Markdown Status |
|---------|-------------|-----------------|
| f_NL = -35/8 | Correct | WRONG (still 5/12) |
| 14 barriers | Correct | Mixed (some 13, some 14) |
| Branch V COMPLETE | Partially updated | WRONG (still ACTIVE) |
| Paper 3 existence | Referenced | Not documented |
| Bayesian discrimination | Referenced | Not documented |
| Focused paper draft | Referenced | Not documented |

**Recommendation:** The HTML is the public-facing version and is largely correct. The markdown files are internal reference. Fixing the markdown is lower priority than ensuring the HTML and the actual papers are correct. However, any future agent consulting the dossier markdown will inherit stale information, so fixing them reduces error propagation.
