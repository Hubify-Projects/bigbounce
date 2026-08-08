# Infrastructure Plan — Extension Tracks

**Date:** 2026-03-13

---

## Summary

Only **Track C (Parity/CMB)** is approved for implementation. Tracks A and B are FUTURE WORK ONLY.

Track C requires **zero additional infrastructure**. All analyses are Gaussian constraint sampling and forward modeling, runnable on any laptop with Python + numpy/scipy/matplotlib.

---

## Track C Compute Requirements

| Resource | Requirement | Available? |
|----------|-------------|------------|
| CPU | Single core, <1 min total | Local Mac |
| RAM | <100 MB | Local Mac |
| Storage | <10 MB output | Local disk |
| GPU | Not needed | N/A |
| Network volume | Not needed | N/A |
| Pod deployment | Not needed | N/A |
| CAMB | Optional (for EB shape comparison) | pip install camb |

**No RunPod pod, network volume, backup cron, or off-pod sync is needed.**

---

## Existing Infrastructure (Paper-1 MCMC)

The following infrastructure remains allocated for Paper-1 chains:

| Resource | Status | Purpose |
|----------|--------|---------|
| RunPod CPU5 pod (<pod-ip>:<port>) | ACTIVE | planck_only chains running |
| Network volume | ACTIVE | Chain storage + backups |
| Hourly backup cron | RUNNING | On-volume tarballs |
| Local sync | Manual | rsync every 12-24h |

**Do NOT deploy additional pods for Track C.**

---

## If Future Tracks (A, B) Are Ever Approved

Should Tracks A or B be promoted from FUTURE WORK, they would need:

### Track A (SMBH Seeds) — if approved:
- No MCMC needed (forward model only)
- Single-core Python on local machine
- Estimated runtime: minutes
- No infrastructure beyond local disk

### Track B (PBH Relics) — if approved:
- Would require substantial theoretical work first (perturbation spectrum through bounce)
- If/when a forward model exists: single-core Python, no MCMC
- If full MCMC warranted: reuse Paper-1 pod architecture
- Estimated timeline: months of theoretical work before any code

---

## Budget

| Item | Cost | Duration |
|------|------|----------|
| Track C analysis | $0 (local compute) | Hours |
| Paper-1 pod (already running) | ~$2-4/day | Until planck_bao freezes (~2 weeks) |
| **Total new cost for extensions** | **$0** | **N/A** |
