# Active Pods & Pipelines — Live Status

**Last updated:** 2026-04-04 UTC
**H200 QUEUE v2 ACTIVE — 50 experiments, 10 phases, ~$1,768 budget**

---

## Pod: H200 — Queue v2 — ACTIVE
| Field | Value |
|-------|-------|
| **Pod ID** | `o76k3jfzbfh25e` (sleepy_blush_crane) |
| **SSH** | `ssh root@205.196.19.52 -p 11781 -i ~/.ssh/id_ed25519` |
| **Machine** | NVIDIA H200 (143 GB VRAM) |
| **Pipeline** | Research Queue v2 — 50 experiments — Phase 1 starting |
| **Status** | ACTIVE — setting up |
| **Cost** | $3.59/hr |

### Queue v2 Phases
| Phase | Experiments | Est. Hours | Est. Cost | Status |
|-------|------------|------------|-----------|--------|
| 1: Re-run broken | 6 | 8h | $29 | STARTING |
| 2: Validation + QC | 6 | 10h | $36 | Pending |
| 3: Cross-survey | 6 | 6h | $22 | Pending |
| 4: Science extraction | 7 | 68h | $244 | Pending |
| 5: New high-impact surveys | 4 | 50h | $180 | Pending |
| 6: Additional surveys | 8 | 120h | $431 | Pending |
| 7: Speculations | 5 | 28h | $100 | Pending |
| 8: Advanced architectures | 4 | 52h | $187 | Pending |
| 9: Full-scale scans | 2 | 144h | $517 | Pending |
| 10: Papers | 2 | 6h | $22 | Pending |

---

## Historical Pods (ALL EXITED)

| Pod | ID | Result |
|-----|----|--------|
| H200 Queue v1 | 7zong4jdj46yjp | 10 experiments complete (6 QC fail). 33.5M sources, 328K anomalies. Terminated Apr 4 (credits). |
| H200 Beast (DESI) | rtv8cegaw1618r | 22.5M spectra, 195,829 anomalies. Complete + backed up. |
| H100 (Chirality) | ulfxypratod4vr | 8.47M galaxies classified. Complete + backed up. |
| RTX A4000 (MCMC) | fn19oivkjowmq4 | 50.9K samples, P(quintom-B)=98.6%. Converged + backed up. |

---

## Backup Locations
| Location | What's there | Last updated |
|----------|-------------|-------------|
| **Local disk** | All chains, anomaly catalogs, scripts, figures, h200 results | 2026-04-04 |
| **GitHub** (main) | Full repo, committed results | 2026-04-04 |
| **Backblaze B2** | MCMC chains, scripts, figures | 2026-04-03 |
| **HuggingFace** | 3 datasets: MCMC, anomaly detector, chirality catalog | 2026-04-03 |
| **Convex** | Chirality catalog (8.47M rows) | 2026-03-28 |
