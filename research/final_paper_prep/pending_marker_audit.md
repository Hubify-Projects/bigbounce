# Pending Marker Audit — `main.tex`

**Date:** 2026-03-12
**File scanned:** `arxiv/main.tex`
**Patterns searched:** `PENDING`, `TBD`, `TODO`, `XXX`, `FIXME`, `placeholder` (case-insensitive)

---

## Summary

| Pattern | Count |
|---------|-------|
| PENDING | 4 |
| TBD | 2 |
| TODO | 0 |
| XXX | 0 |
| FIXME | 0 |
| placeholder | 0 |
| **Total** | **6** |

---

## Full Inventory

| # | Line | Section | Pattern | Surrounding Text (abbreviated) | Result Needed | Dependency |
|---|------|---------|---------|-------------------------------|---------------|------------|
| 1 | 364 | Sec. 3 — Observational Signatures / CMB $E$-$B$ (§3.1) | `TBD` | `…Isotropic birefringence (all ℓ; angle not derived, requires photon-torsion coupling) plus anisotropic low-ℓ component (amplitude and shape TBD).` | Anisotropic birefringence amplitude and angular shape for spin-torsion prediction. Requires deriving the photon-torsion coupling and computing the $C_\ell^{EB}$ power spectrum. | **Final referee pass** — this is a known theoretical limitation acknowledged as future work; no MCMC run will resolve it. Mark as "deferred to Paper II" or compute explicit coupling. |
| 2 | 437 | Sec. 3.4 — Independent Verification Results (§verification) | `pending` | `…A third (Planck-only) is in progress and a fourth (Planck+BAO) is pending; results will be incorporated when available.` | Completion of Planck+BAO MCMC chains (Cobaya v3.6.1). | **planck_bao** — directly blocked on this run completing and converging. |
| 3 | 458 | Sec. 3.4 — Independent Verification Results, Table II | `PENDING` | `Planck-only & \multicolumn{2}{c}{\textit{[PENDING---in progress]}}` | Posterior means ± 1σ for $H_0$, $\Delta N_\text{eff}$, $\sigma_8$, $\ln B$, worst $\hat{R}-1$, min ESS from the Planck-only MCMC run. | **planck_only** — run reportedly in progress. |
| 4 | 459 | Sec. 3.4 — Independent Verification Results, Table II | `PENDING` | `Planck+BAO & \multicolumn{2}{c}{\textit{[PENDING---not yet started]}}` | Same parameter set as above but for the Planck+BAO dataset combination. | **planck_bao** — run not yet started. |
| 5 | 475 | Sec. 3.4 — Independent Verification Results, Fig. caption | `pending` | `…Gray markers indicate pending dataset combinations (Planck-only, Planck+BAO).` | Replace gray placeholder markers in the comparison figure with actual data points once runs 3 & 4 complete. Update caption to remove "pending" language. | **planck_only** + **planck_bao** — figure regeneration blocked on both runs. |
| 6 | 779 | Sec. 6.5 — Model Comparison Table (§fullcomp) | `TBD` | `Forecast & N/A & Uncertain & Uncertain & Testable (amplitudes TBD)` | Quantitative forecast amplitudes for the spin-torsion signatures ($EB$ correlation amplitude, spin asymmetry amplitude, rotation-axis alignment). | **final comparison table** — needs either a Fisher forecast or explicit numbers from the theory sector. Could also be resolved by citing the qualitative status and removing "TBD". |
| 7 | 1306 | Appendix B — Complete Parameter Summary, footnote a | `PENDING` | `…Two additional dataset combinations (Planck-only, Planck+BAO) are \textit{[PENDING]}.` | Same as items 3–4: fill in or remove the pending note once MCMC results are available. | **planck_only** + **planck_bao** |

---

## Dependency Summary

| Dependency | Markers Blocked | Lines |
|------------|----------------|-------|
| **planck_only** | 3 | 458, 475, 1306 |
| **planck_bao** | 4 | 437, 459, 475, 1306 |
| **final comparison table** | 1 | 779 |
| **final referee pass** | 1 | 364 |

### Resolution Priority

1. **planck_only** (in progress) — unblocks 3 markers. Monitor convergence; once $\hat{R}-1 < 0.01$ and ESS > 1000, extract posteriors and fill Table II row + update figure.
2. **planck_bao** (not started) — unblocks 4 markers. Launch run as soon as GPU time is available. Same extraction pipeline as planck_only.
3. **final comparison table** (line 779) — can be resolved editorially by replacing "amplitudes TBD" with "amplitudes forecast-dependent" or by computing a simple Fisher forecast for the three signature channels.
4. **final referee pass** (line 364) — theoretical derivation deferred to Paper II. Can be resolved by softening language (e.g., "amplitude and shape to be determined in future work") without new computation.

---

## Notes

- No `TODO`, `XXX`, `FIXME`, or `placeholder` markers were found anywhere in the manuscript.
- The word "pending" also appears naturally in the cosmic birefringence subsection (line 977) in the phrase "remains qualitative pending an explicit photon-sector coupling" — this is expository prose, not a data placeholder, but it flags an open theoretical gap that should be tracked for Paper II.
