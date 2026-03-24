# Current-Data Extraction Master Plan

**Date:** 2026-03-23
**Version:** 1.0

---

## Two Parallel Tracks

### Track A — Theory / Estimator / Forecast Hardening

| Phase | Goal | Status | Priority |
|-------|------|--------|----------|
| Phase 1 | Normalization audit (-35/8 vs -35/16) | **92% complete** | DONE for now |
| Phase 2 | General-ε derivation + consistency relation | Not started | HIGH |
| Phase 3 | Estimator-level overlap validation | Not started | HIGH |
| Phase 4 | Direct bounce-specific Fisher forecast | Not started | MEDIUM |

### Track B — Current-Data Empirical Pipelines

| Pipeline | Goal | Status | Priority |
|----------|------|--------|----------|
| F1 | Bounce-specific bispectrum extraction (CMB) | Scaffolding | HIGHEST |
| F2 | LSS tracer-enhanced PNG extraction | Scaffolding | HIGH |
| F3 | CMB residual / EB robustness support | Scaffolding | MEDIUM-HIGH |

---

## Execution Order

```
Phase 1 (DONE) ─────────────────────────────────────────────
                                                              │
Phase 2 (general-ε)   ── can run on RunPod CPU ──┐          │
                                                   │          │
F1-A (baseline repro)  ── local, no data needed ──┤          │
                                                   │          │
F3-A (data manifest)   ── local, verify URLs ─────┤  ← START │
                                                   │   HERE   │
F2-A (baseline sample) ── needs DESI download ────┤          │
                                                   │          │
Phase 3 (overlap)      ── search for PolyBin ─────┤          │
                                                   ↓          │
                   ┌─── All F*-A milestones pass ──┘          │
                   │                                           │
F1.2-F1.6 (bounce template → final output)                    │
F2.2-F2.7 (enhanced tracers → combined)                       │
F3.2-F3.6 (EB nulls → support)                                │
Phase 4 (direct Fisher forecast)                               │
                   │                                           │
                   ↓                                           │
              INTEGRATION ─────────────────────────────────────┘
```

### What can run in parallel

- F1-A (Planck recast baseline) — local, immediate
- F3-A (data manifest + URL verification) — local, immediate
- Phase 2 (general-ε) — RunPod CPU if needed

### What blocks

- F2-A requires DESI DR1 catalog access (may need RunPod for download)
- F1.3+ requires simulation products (PLA download)
- F3.2+ requires map products (PLA download)

---

## Compute Plan

### Local machine (immediate)

| Task | Pipeline | Time |
|------|----------|------|
| F1-A: Fisher recast baseline | F1 | 1 hour |
| F3-A: Data manifest + URL verification | F3 | 30 min |
| Phase 2: Mode function computation (mpmath) | Theory | 2-4 hours |
| Phase 3: Search for public estimator code | Theory | 1 hour |
| F2-A: Sample design document | F2 | 1 hour |

### RunPod CPU pod (when needed)

| Task | Pipeline | Pod type | Time | Cost |
|------|----------|----------|------|------|
| DESI catalog download + cross-match | F2 | 32-core CPU | 4 hours | ~$3 |
| Planck map download | F3 | Any CPU | 2 hours | ~$2 |
| FFP10 simulation subset download | F1/F3 | Any CPU | 4 hours | ~$3 |
| Mock generation with PNG injection | F2 | 32-core CPU | 4 hours | ~$3 |
| General-ε Hankel integrals (if slow) | Phase 2 | 32-core CPU | 2 hours | ~$2 |
| NaMaster EB estimation suite | F3 | 64-core CPU | 8 hours | ~$6 |

### RunPod GPU (only if justified)

| Task | Pipeline | Justification |
|------|----------|---------------|
| Neural tracer model | F2 | Only if XGBoost is insufficient AND standard features exhausted |
| Patch CNN quality scorer | F3 | Only if classical scoring is insufficient |

**Default: NO GPU.** Escalate only with documented justification.

---

## Gating Logic

### F1 gates
- F1.1 MUST reproduce f_NL^local = -0.9 ± 5.1 within tolerance → THEN F1.2
- F1.3 injections MUST recover within 10% bias → THEN F1.4
- F1.5 nulls MUST show no false bounce preference → THEN F1.6

### F2 gates
- F2.1 baseline sample MUST be documented with sky coverage, n(z), contamination → THEN F2.2
- F2.3 leakage audit MUST show no dominant nuisance correlation → THEN F2.4
- F2.5 mock injections MUST show improvement is real → THEN F2.6

### F3 gates
- F3.1 data files MUST be verified with checksums and correct format → THEN F3.2
- F3.2 null baseline MUST recover zero within tolerance → THEN F3.3
- F3.3 injections MUST recover known signal → THEN F3.4

---

## Success Criteria

### Minimum viable outcome
- F1 at Level 1 (baseline reproduced) with honest recast onto bounce template
- F2 at Level 1 (baseline sample documented)
- F3 at Level 1 (data manifest verified)
- Phase 2 at "numerically validated" level
- Integration memo with honest assessment

### Good outcome
- F1 at Level 3+ (injection validated, partial robustness)
- F2 at Level 2+ (enhanced sample with mock validation)
- F3 at Level 3+ (EB nulls pass, partial robustness)
- All three pipelines contributing independent information
- Combined constraint modestly tighter than Planck alone

### Excellent outcome
- F1 at Level 5 (publication-ready bounce-specific extraction)
- F2 at Level 4+ (enhanced tracers with full audit)
- F3 at Level 4+ (EB robustness passed)
- Combined pre-SPHEREx constraint σ(f_NL) < 4
- Clear honest statement about what current data say

---

## Fail Conditions (project-level)

- Cannot reproduce ANY published baseline → fundamental methodology problem
- All improvements disappear on robustness checks → no real gain from current data
- Combination assumptions are indefensible → cannot combine pipelines

These would be honest negative results. Document them clearly.
