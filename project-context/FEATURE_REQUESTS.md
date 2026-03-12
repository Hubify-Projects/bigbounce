# BigBounce Feature Requests

**Every feature request MUST be logged here.**

Last Updated: 2026-03-06

---

## Session: 2026-03-05 (Report Truth Audit)

### Global Monitor Report Truth Audit
| Status | DONE |
|--------|------|
| Request | "Do a non-destructive report truth audit. Audit which metrics are host/container-level vs pod/job-level. Disable/relabel unreliable ESS ETA predictions. Verify backups for real. Produce corrected status report with experiment-only metrics. Write to global_status_corrected.txt and warnings_corrected.txt." |
| Notes | Completed 2026-03-06. All 7 pods verified alive via SSH. Metrics classified (5 infrastructure-only, 10 pod/job-level). ESS ETAs suppressed as LOW CONFIDENCE. Real backups created on all 7 pods (previously dry-run only). Corrected reports written. CPU#2 "DOWN" confirmed as false alarm. |

---

## Session: 2026-03-05 (Global Research Monitor)

### Unified Global Research Monitor
| Status | DONE |
|--------|------|
| Request | "Set up a unified global research monitor across ALL BigBounce pods. One command / one report for live status of every active computation. Automatic backups and frozen artifact packs for every track." |
| Notes | Built: pod_registry.yaml (7 pods), global_status.py (845 lines), global_backup.py (452 lines), global_artifact_index.py (481 lines), run_all_monitors.sh, run_all_monitors.py, hourly_loop.sh. First pass run complete. All files in research/global_monitor/. |

---

## Session: 2026-03-05 (Paper 2 — Four-Track Research Program)

### Paper 2 Research Program — 4 Parallel RunPod Tracks
| Status | DONE |
|--------|------|
| Request | "Run four parallel research tracks (A/B/C/D) on separate RunPod pods. Track A: WP4 ΔNeff microphysics (CPU). Track B: WP5 spin amplitude derivation (CPU). Track C: P7 CNN spin classifier (GPU). Track D: P6 CMB EB pipeline (CPU/RAM)." |
| Notes | All 4 pods deployed (RTX A5000, secure cloud). All first runs completed successfully. Pod IDs: bpou58tmt95jjb (A), mz3srzbzxxv1yj (B), pkysk4lbaqnhm0 (C), uktt3hghbs1djo (D). |

### Provenance Fix — Shared Resource Cleanup
| Status | DONE |
|--------|------|
| Request | "Fix provenance + placeholder issues in shared resources. Remove XXXXX placeholders, validate Planck maps, create galaxy spin artifact." |
| Notes | 3 placeholder arXiv IDs resolved. Planck maps specified as PR4/NPIPE. Galaxy spin CSV created with sha256. |

### P7 CNN Spin Classifier — Full Code Package
| Status | DONE |
|--------|------|
| Request | "Write all code files for Track C — P7 CNN Spin Classifier." |
| Notes | ResNet-18 classifier, parity augmentation, 4 bias audits, toy dipole fit. All files under research/paper2/p7_cnn_spin_classifier/. |

### WP5 Spin Amplitude — Full Code Package
| Status | DONE |
|--------|------|
| Request | "Write all code files for Track B — WP5 Spin Amplitude." |
| Notes | A₀ ≈ ε_PO × 0.015, requiring ε_PO ≈ 0.2 for observed A₀ ~ 0.003. All files under research/paper2/wp5_spin_amplitude/. |

### WP4 ΔNeff Microphysics — Full Code Package
| Status | DONE |
|--------|------|
| Request | "Write all code files for Track A — WP4 ΔNeff Microphysics." |
| Notes | Reheating + decay toy models, parameter scans. All files under research/paper2/wp4_dneff_microphysics/. |

---

## Session: 2026-03-05 (Multi-Node MCMC Orchestration)

### Multi-Node CPU MCMC Campaign
| Status | IN_PROGRESS |
|--------|-------------|
| Request | "Move to high-core-count CPU pods to accelerate convergence and produce canonical results." |
| Notes | 3 Paper 1 pods running: GPU (32 cobaya, 28 chains), CPU#1 (16 cobaya, 16 chains), CPU#2 (16 cobaya, 17 ΛCDM chains). R-hat still 0.08-1.0, far from 0.01 target. |

### Freeze Packager Pipeline
| Status | IN_PROGRESS |
|--------|-------------|
| Request | "Freeze packager with ESS gate, per-chain spread gate, per-dataset freezing, ablation builder." |
| Notes | freeze_packager.py v2 deployed to all 3 pods with 30-min check loops. GPU has 48h time cap. |

---

## Session: 2026-03-04 (BigBounce v1.0 → v1.2.0)

### Full Site + PDF Update with New Research
| Status | DONE |
|--------|------|
| Request | "BigBounce v1.0 update: fix 6 research issues, add 8 new citations, recompile PDF, sync HTML pages." |
| Notes | Completed through v1.2.0 (32 pages, 57 bib entries). Live on bigbounce.hubify.app. |

### Post-Convergence Paper Update
| Status | PENDING |
|--------|---------|
| Request | "After MCMC convergence: generate triangle plots (GetDist), download all data, update paper Table IV + new figures, recompile PDF, new mcmc-results.html page, commit as v1.3.0." |
| Notes | Blocked on R-hat convergence to <0.01. GPU Full Tension closest at H0=0.083. |
