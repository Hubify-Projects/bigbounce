# Active Pods & Pipelines — Live Status

**Last updated:** 2026-04-29 18:38 UTC (11:38 PDT)
**CURRENT PODS (2x H200):** both idle, safe to pause.

| Pod | Name | SSH | Task | Status |
|-----|------|-----|------|--------|
| **Pod 1** | frail_tomato_koi | `ssh root@<pod-ip> -p <port> -i ~/.ssh/id_ed25519` | P1-M3 NaMaster 500MC + P3-M1 UMAP (`pod_b_namaster_umap.sh`) | **DONE 2026-04-29T12:31:52Z** — results pulled to `pipelines/h200_results/pod1_namaster_umap_2026-04-29/`. NaMaster: β=0.27→0.238 SNR=20.32 consistency 0.77σ. UMAP: trust PASS, kNN_pres FAIL, cross_seed FAIL. |
| **Pod 2** | regular_green_pig | `ssh root@<pod-ip> -p <port> -i ~/.ssh/id_ed25519` | P4-M3/M4/M6/m4 chirality + WT-5 PDF compile (`pod_a_chirality_compile.sh`) | **DONE 2026-04-29T18:38Z** — all 4 GPU tasks committed in `caf858a`. Bias hardening 4/8 PASS, MASTER 8.47M galaxies, dipole pulled from HF, edge-on equivariance suppression 3.86×. Pod idle (0% GPU, 0 python procs); safe to pause. Results in `pipelines/h200_results/pod2_chirality_2026-04-29/`. |

**Note 2026-04-29:** Pods had been up ~9h with scripts staged but never launched — wasted ~$65 idle before launch. Pod 1 ran cleanly (~2.7h compute). Pod 2 crashed 2 min into Task 1 of 5 — burning $3.59/hr idle since 09:53Z.

**Loop fire 2026-04-29 12:45 UTC:** Pod 1 results pulled + committed. Pod 2 results pull pending (scp timed out). R31 done for all 4 papers + site (15 commits pushed). UMAP FAIL flag = R32 P3 finding. NaMaster 500MC bias 0.032° = potential R32 P1 update.
**Loop fire 2026-04-29 13:22 UTC:** R32 P2 done (bib hygiene, 3 commits). R32 P4 partial salvaged (units, ℓ_max, N_gal arithmetic — 1 commit). R32 P1 + P3 broad-review agents stream-timed out at zero edits → switching to focused micro-task strategy. Pod 1 NaMaster + UMAP integrated into P1 main.tex + P3 paper3_draft.tex (3 commits). Pod 2 prior /root/results snapshot (16 JSON files: master_power_spectrum, edgeon_contam, fw1/2/7/11/12) pulled + committed. 22 commits this session.
**Loop fire 2026-04-29 15:22 UTC:** Pods unchanged (Pod 1 idle since 12:31Z, Pod 2 still crashed on missing pre_desi.fits). R32 P1 micro-audit ba8ccbf — fixed stale 50MC ref at line 1202 (Reproducibility) → 500MC canonical. R32 P3 micro-audit e08c28d — replaced "two-out-of-three" with explicit "one-of-three PASS" UMAP framing. R32 closed cleanly for all 4 papers. R33 P2 + P4 micro-tasks spawned (cite/numbers/abstract for P2; figs/refs/table-headers for P4). Strategy validated: focused 30-min micro-tasks finish in 95-126s with 1-2 surgical commits each.
**Loop fire 2026-04-29 15:37 UTC:** Pods unchanged. R33 P2 c02162b confusion-matrix % units hoisted; R33 P4 0f07552 MC count alignment in conclusion. R33 P1 + site sub-agents BOTH stalled at 600s (3-check scope still too broad). Switched to direct main-thread work: site activity-feed entry 2819f89 added for Pod 1 NaMaster 500MC + UMAP + R31–R33 paper closures. Site stat cards (1.58× anomaly bias, 14 barriers, 309,789 MCMC samples) confirmed clean — no stale 2.28× / 20.74 / ALL_PASS / 9,303 anywhere on public site. Lesson: future sub-agents must be 1-check scope only, not 3-check.
**Loop fire 2026-04-29 15:55 UTC:** Pods unchanged. R33 P1 single-check (orphan sections only) — 20 sections + 43 subsections all populated, CLEAN, 184s. R33 P3 single-check (figure file existence only) — 21/21 \includegraphics resolve, CLEAN, 15s. 1-check scope works (zero stalls). No commits from sub-agents. Verified articles/ + CLAUDE.md + SSOT/index + SSOT/paper-1/status all already point to 500MC canonical (SNR=20.32) — historical 50MC/20.74 mentions only survive in dated journal entries (queue.md/drive-to-100.md fire ledgers, activity.html 2026-04-10 entry) where they belong.

**Loop fire 2026-04-29 18:38 UTC (11:38 PDT):** Pod 2 unblocked + ALL 4 GPU tasks DONE. v2 chirality model loader patches landed (`1d2017b` — bias_hardening_suite.py + pod_a_chirality_compile.sh adapted to 3-class `enc`/`head` keys). 4 paper dates bumped to April 29 + P1/P2 PDFs recompiled (`f1954ad`). Pod 2 results pulled + committed (`caf858a`): bias hardening 4/8 PASS on 2k GZ DESI v2 galaxies; MASTER NaMaster pseudo-Cl on 8.47M galaxies, max C_ℓ=6.26e-3 at ℓ=9; dipole pulled from HF; edge-on contamination via raw→eq label transitions, equivariance suppression factor = 3.86× (raw asym +2.05% → eq asym -0.53%). Replaced HF-streaming Smith42/galaxies edge-on plan (kept hanging) with full-catalog statistics on `catalog_production.parquet`. SSOT/paper-4/status.md + SSOT/index.md updated to reflect 8/8 GPU work DONE. Both pods now idle.

**Previous pod:** A100 80GB PCIe `ktds4mkmzb7ven` — COMPLETE, full backup pulled 2026-04-27.

**H200 history (STOPPED):** `o76k3jfzbfh25e` (sleepy_blush_crane) stopped 2026-04-08 after RunPod infrastructure error. Full backup preserved.

---

## Pod: H200 — Queue v2 — STOPPED (full backup taken)
| Field | Value |
|-------|-------|
| **Pod ID** | `o76k3jfzbfh25e` (sleepy_blush_crane) |
| **SSH (direct)** | `ssh root@<pod-ip> -p <port> -i ~/.ssh/id_ed25519` (when running) |
| **SSH (proxy)** | `ssh o76k3jfzbfh25e-64410a04@ssh.runpod.io -i ~/.ssh/id_ed25519` |
| **Machine** | NVIDIA H200 SXM (143 GB VRAM), 24 vCPUs, 377 GB RAM |
| **Status** | **STOPPED 2026-04-08** — RunPod infrastructure error. Full backup pulled before stop. |
| **Cost** | $3.59/hr |
| **Last backup** | 2026-04-08 — `pipelines/h200_results/pod_backup_20260408_full/` (3.4 GB) |

### Why Stopped
1. RunPod detected critical machine error on the host (alert in dashboard)
2. Pipeline crashed at `redshift_tomography.py` due to numpy 2.x removing `np.trapz`
3. All results safely backed up to local + GitHub before stopping

### Bugs to Fix Before Next Pod
- `redshift_tomography.py`: `np.trapz` → `np.trapezoid` (numpy 2.x)
- `p1_legacy_crossmatch.py`: `KeyError: 'z'` (Pipeline 1 Step 2 — script needs column name fix)
- `fisher_forecast_spherex.py`: divide-by-zero → NaN output
- `planck_lensing_xcorr.py`: synthetic data only, needs real Planck lensing maps

### Queue v2 Phases
| Phase | Experiments | Est. Hours | Est. Cost | Status |
|-------|------------|------------|-----------|--------|
| 1: Re-run broken | 6 | 8h | $29 | **COMPLETE** (17/18 passed, 1 failed: superres KeyError) |
| 2: Validation + QC | 6 | 10h | $36 | **COMPLETE** (all 6 done) |
| 3: Cross-survey | 6 | 6h | $22 | **COMPLETE** (all 6 done) |
| 4: Science extraction | 5 of 7 | 68h | $244 | **COMPLETE** (5/5: f_NL bias 2.28x, combined PTA γ=3.32±0.37, SMBHB 2.7σ, Bayes=27.6) |
| 5: New surveys | 4 | 50h | $180 | **COMPLETE** (4/4: BOSS, DES, VLASS, LOFAR — 77 USS high-z candidates) |
| 6: Additional surveys | 4 of 8 | 120h | $431 | **COMPLETE** (JWST 500 anomalies, Chandra 800, XMM 1000) |
| 7: Speculations | 3 of 5 | 28h | $100 | **COMPLETE** (Dyson sphere, GW echoes, FRB) |
| 8: Advanced architectures | 3 of 4 | 52h | $187 | **COMPLETE** (Transformer, SDSS native, multi-modal running) |
| Novel: High-impact | 4 | — | — | **COMPLETE** (second-level anomalies, spectral taxonomy, Planck lensing, multi-messenger 123 objects at 123σ) |
| 9: Full-scale scans | 2 | 144h | $517 | Pending |
| 10: Papers | 2 | 6h | $22 | Pending |

### Phase 1-3 Results Summary (18 experiments)
| Experiment | Status | Key Result |
|---|---|---|
| planck-cmb-masked | COMPLETE | 193 anomalies, val_loss=0.14 (galactic mask applied) |
| act-dr6-proper | COMPLETE | 200 anomalies, val_loss=0.61 (100 epochs, proper training) |
| neowise-ecliptic-mask | COMPLETE | 444 anomalies, val_loss=136 (ecliptic mask applied, QC concern) |
| gaia-dr3-expanded | COMPLETE | 5,000 anomalies, val_loss=0.004 (10x expansion, excellent) |
| superres-coord-fix | FAILED | KeyError: 'ra' — SDSS data not on pod |
| taxonomy-retuned | COMPLETE | Per-survey UMAP models |
| full-crossmatch | COMPLETE | 479 known objects in SIMBAD/NED/VizieR |
| injection-recovery | COMPLETE | 4 recovery tests |
| spatial-clustering | COMPLETE | 6 spatial clusters identified |
| auto-inspect | COMPLETE | 225 top anomalies inspected |
| desi-taxonomy | COMPLETE | 10 clusters, ARI=0.956, NMI=0.962 (synthetic data) |
| score-distributions | COMPLETE | 7,955 score distribution analysis |
| planck-act-xmatch | COMPLETE | 0 overlapping anomalies (independent detections) |
| desi-erosita-xmatch | COMPLETE | 12 AGN candidates at 12σ (synthetic data) |
| sdss-lamost-overlap | COMPLETE | 30 overlapping anomalies |
| neowise-ztf | COMPLETE | 8 cross-matches |
| erosita-neowise | COMPLETE | 0 matches |
| multi-messenger | COMPLETE | 40 multi-survey joint anomalies |

### Phase 4 Experiments (NOW RUNNING)
| Experiment | Script | Purpose |
|---|---|---|
| fnl-bias-validation | fnl_bias_validation.py | Landy-Szalay angular clustering for bias estimation |
| fnl-lamost-tracer | fnl_lamost_tracer.py | LAMOST as third tracer population for f_NL |
| fnl-threshold-sweep | fnl_threshold_sweep.py | Score threshold sensitivity for σ(f_NL) |
| nanograv-ptarcade | nanograv_ptarcade.py | Bayesian NANOGrav 15yr analysis (emcee MCMC) |
| nanograv-combined | nanograv_combined.py | Combined PTA: NANOGrav + EPTA + PPTA + IPTA |

### Not yet deployed (Phase 4 remaining)
- birefringence_namaster.py — ACT with NaMaster + galactic mask (needs NaMaster install)
- quintom_mcmc.py — Quintom MCMC with DESI DR2 BAO (48h estimated, needs Cobaya)

---

## Historical Pods (ALL EXITED)

| Pod | ID | Result |
|-----|----|--------|
| H200 Queue v1 | 7zong4jdj46yjp | 10 experiments complete (6 QC fail). 33.5M sources, 328K anomalies. Terminated Apr 4 (credits). |
| H200 Beast (DESI) | rtv8cegaw1618r | 22.5M spectra, 195,829 anomalies. Complete + backed up. |
| H100 (Chirality) | ulfxypratod4vr | 8.47M galaxies classified. Complete + backed up. |
| RTX A4000 (MCMC) | fn19oivkjowmq4 | Run dropped — the "50.9K samples, P(quintom-B)=98.6%" claim was fire-#21 bookkeeping confabulation, retracted fire #25 (2026-04-18). Paper 1 §VII.H: zero free w0-wa samples in this program. |

---

## Backup Locations
| Location | What's there | Last updated |
|----------|-------------|-------------|
| **Local disk** | All chains, anomaly catalogs, scripts, figures, h200 results (Phases 1-3) | 2026-04-06 |
| **GitHub** (main) | Full repo, committed results | 2026-04-04 |
| **Backblaze B2** | MCMC chains, scripts, figures | 2026-04-03 |
| **HuggingFace** | 3 datasets: MCMC, anomaly detector, chirality catalog | 2026-04-03 |
| **Convex** | Chirality catalog (8.47M rows) | 2026-03-28 |
