# File Navigation Map

Key file paths organized by function. All paths are relative to the repository root.

---

## Canonical Manuscript

| Purpose | Path |
|---------|------|
| LaTeX source (canonical) | `arxiv/main.tex` |
| Compiled PDF | `arxiv/main.pdf` |
| Bibliography | `arxiv/references.bib` |
| Publication figures | `arxiv/figures/` |
| Submission-ready TeX | `submission/paper_1_2/main.tex` |
| Submission-ready PDF | `submission/paper_1_2/main.pdf` |

---

## Paper Structure & Claims

| Purpose | Path |
|---------|------|
| Final paper outline (28.5pp) | `research/final_phase/01_final_paper_structure.md` |
| 9-figure plan | `research/final_phase/02_figure_plan.md` |
| Claims lock (exact wording) | `research/final_phase/03_claims_lock.md` |
| Referee simulation | `research/paper_1_2_archive/referee_simulation.md` |
| Reader misinterpretation check | `research/paper_1_2_archive/reader_misinterpretation_check.md` |
| Claims alignment audit | `research/final_paper_prep/claims_alignment_audit_v1_6.md` |
| Supported/unsupported claims | `research/final_paper_prep/theory_claims_do_and_do_not_support.md` |

---

## MCMC & Reproducibility

| Purpose | Path |
|---------|------|
| Reproducibility README | `reproducibility/README.md` |
| Implementation map | `reproducibility/docs/IMPLEMENTATION_MAP.md` |
| Known gaps | `reproducibility/docs/KNOWN_GAPS.md` |
| Full-tension chains (FROZEN) | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/full_tension/` |
| Planck+BAO+SN chains (FROZEN) | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_bao_sn/` |
| Planck+BAO chains (PAUSED) | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_bao/` |
| Planck-only chains (RUNNING) | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_only/` |
| Cobaya configs | `reproducibility/cosmology/cobaya_*.yaml` (4 files) |
| Galaxy spin Stan model | `reproducibility/galaxy_spins/spin_fit_stan.py` |
| Figure generation scripts | `research/final_paper_prep/generate_*.py` |
| Parameter extraction | `research/final_paper_prep/extract_physical_parameters.py` |

---

## Structural Closure (Foundations A-G)

| Foundation | Phase 1 Verdict | Phase 2 Summary |
|------------|----------------|-----------------|
| A (PGT propagating torsion) | `research/foundation_A_pgt/phase1_verdict.md` | `research/foundation_A_pgt/phase2/11_phase2_summary.md` |
| B (Lock-breaking) | `research/foundation_B_lock_breaking/phase1_results.md` | `research/foundation_B_lock_breaking/phase2/02_nieh_yan_mag_analysis.md` |
| C (Environmental mass) | `research/foundation_C_environmental_mass/phase1_results.md` | — |
| D (Disformal) | `research/foundation_D_disformal_survival/phase1_results.md` | — |
| E (Global vacuum) | `research/foundation_E_global_vacuum/phase1_results.md` | `research/foundation_E_global_vacuum/phase2_curvature_constraint/` |
| F (Initial conditions) | `research/foundation_F_initial_conditions/phase1_results.md` | — |
| G (Vacuum selection) | `research/foundation_G_bounce_vacuum_selection/phase1_results.md` | `research/foundation_G_bounce_vacuum_selection/phase2_cyclic_sequestering/` |

---

## Post-Closure Branches (H-O)

| Branch | Phase 1 Results |
|--------|----------------|
| H (Tensor spectrum) | `research/branch_H_bounce_only/` |
| I (Compatible DE) | `research/branch_I_bounce_compatible_DE/` |
| J (State selection) | `research/branch_J_state_selection/phase1_results.md` |
| K (Scalar perturbations) | `research/branch_K_scalar_perturbations/phase1_results.md` |
| L (UV-IR bridge) | `research/branch_L_uv_ir_bridge/phase1_results.md` |
| M (PGT GW) | `research/branch_M_pgt_bounce_gw/phase1_results.md` |
| N (Baryogenesis) | `research/branch_N_baryogenesis_relics/phase1_results.md` |
| O (Hidden-sector vacuum) | `research/branch_O_hidden_sector_vacuum/phase1_results.md` |
| N+O joint summary | `research/branch_NO_joint_summary.md` |

---

## Extension Branches (P-W)

| Branch | Key File |
|--------|----------|
| P (PGT observables) | `research/branch_P_pgt_bounce_program/phase1_results.md` |
| Q (Sourced parity) | `research/branch_Q_sourced_parity/phase1_results.md` |
| R (ALP birefringence) | `research/branch_R_alp_birefringence/phase1_results.md` |
| R Phase 2 MCMC | `research/branch_R_alp_birefringence/phase2_mcmc/` |
| S (Photon-torsion vertex) | `research/branch_S_photon_torsion_vertex/phase1_results.md` |
| T (Axion bridge) | `research/branch_T_sourced_axion_bridge/phase1_results.md` |
| U (Two-field ALP) | `research/branch_U_twofield_alp_de/phase1_results.md` |
| V (Matter bounce + ECH) | `research/branch_V_bounce_evidence/final_verdict.md` |
| Vb (Perturbation gate) | `research/branch_Vb_ech_perturbation_gate/` |
| W (Curvaton tilt) | `research/branch_W_alp_curvaton_tilt/phase1_results.md` |

---

## Special Programs

| Program | Key File |
|---------|----------|
| Next-gen bounce signals | `research/project_nextgen_bounce_signals/final_verdict.md` |
| Chiral GW frequency gate | `research/project_chiral_bounce_GW/phase0_results.md` |
| IR vacuum 4-route closure | `research/paper2/ir_vacuum_program/00_executive_summary.md` |
| Negative-result supplement | `research/paper2/ir_vacuum_program/supplement_negative_results.pdf` |
| Extensions program | `research/extensions/final_report.md` |

---

## Strategic Documents

| Purpose | Path |
|---------|------|
| Post-AG pivot summary | `research/post_AG_pivot/final_pivot_summary.md` |
| Program reset memo | `research/program_reset_bounce_first.md` |
| Foundation map v2 | `research/foundation_map_v2.md` |
| Salvage audit verdict | `research/program_salvage_audit/final_verdict.md` |
| ALP salvage verdict | `research/paper1_salvage_alp/final_verdict.md` |
| Branch opening criteria | (in memory: `feedback_branch_opening_criteria.md`) |

---

## Peer Review & Audit Trail

| Purpose | Path |
|---------|------|
| Revision tracker (8 rounds) | `project-context/peer-reviews/REVISION_TRACKER.md` |
| Initial comprehensive audit | `project-context/peer-reviews/2026-03-02_1917PST_comprehensive-audit.md` |
| Claims classification table | `project-context/peer-reviews/2026-03-02_1917PST_claims-table.md` |
| Data provenance audit | `research/data_audit/dataset_provenance_final_check.md` |
| Numerical consistency report | `research/final_paper_prep/numerical_consistency_report.md` |
| LaTeX compile readiness | `research/final_paper_prep/latex_compile_readiness.md` |

---

## Versioning

| Purpose | Path |
|---------|------|
| Current version | `version.json` (v1.6.0-preaudit) |
| Version history | `versions/manifest.json` (through v1.2.0; needs update) |

---

## Archives

| Purpose | Path |
|---------|------|
| Paper 1.01 snapshot | `research/paper_1_01_archive/` |
| Paper 1.2 development | `research/paper_1_2_archive/` |
| Paper 2 track archives | `research/paper2/archives/` |
| Submission archives | `submission/archives/` |

---

## Web Infrastructure

| Purpose | Path |
|---------|------|
| Main web presentation | `index.html` |
| Interactive data viz | `interactive-data.html` |
| Version history page | `versions.html` |
| Dev server | `server.js` |
| Deployment config | `netlify.toml` |
