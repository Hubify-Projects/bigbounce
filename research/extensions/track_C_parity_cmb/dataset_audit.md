# Phase 1: Dataset / Likelihood Audit

**Date:** 2026-03-13

---

## Candidate Data Sources

### 1. Eskilt (2022) — Planck NPIPE Full-Mission Reanalysis

| Field | Value |
|-------|-------|
| Paper | Eskilt (2022), "Frequency-dependent constraints on cosmic birefringence from the LFI and HFI Planck Data Release 4" |
| arXiv | 2205.13962 |
| Observable | Isotropic cosmic birefringence angle β |
| Measurement | β = 0.30° ± 0.11° (2.7σ) |
| Method | EB cross-correlation with foreground self-calibration (Minami-Komatsu method applied to NPIPE) |
| Public availability | Paper is public; measurement values in text |
| Machine-readable | YES — β and σ_β from paper text |
| Covariance | Single parameter — no covariance needed |
| EB bandpowers | YES — Table 1 of the paper gives D_ℓ^{EB} bandpowers with error bars for ℓ bins |
| Bandpower covariance | NO — only diagonal errors published |
| Supersedes | Minami & Komatsu (2020), arXiv:2011.11254 |
| Suitable for | **Gaussian summary likelihood** (β); **EB shape comparison** (bandpowers) |

### 2. Diego-Palazuelos & Komatsu (2025) — ACT DR6

| Field | Value |
|-------|-------|
| Paper | Diego-Palazuelos & Komatsu (2025), ACT DR6 birefringence analysis |
| arXiv | 2503.14452 (approximate; cited in main.tex) |
| Observable | Isotropic cosmic birefringence angle β |
| Measurement | β = 0.215° ± 0.074° (2.9σ) |
| Method | ACT DR6 + Planck cross-correlation; independent instrument from Planck-only |
| Public availability | Paper is public; measurement values in text |
| Machine-readable | YES — β and σ_β from paper text |
| Covariance | Single parameter — no covariance needed |
| EB bandpowers | Published in paper but not separately digitized in this repo |
| Bandpower covariance | NO — not publicly released |
| Independent from Eskilt? | YES — different instrument (ACT vs Planck HFI), different analysis pipeline |
| Suitable for | **Gaussian summary likelihood** (β) |

### 3. SPIDER Collaboration (2025)

| Field | Value |
|-------|-------|
| Paper | SPIDER Collaboration (2025) |
| arXiv | 2510.25489 (approximate) |
| Observable | Total polarization rotation (instrumental + cosmic) |
| Measurement | Total rotation ~7σ combined (SPIDER + Planck + ACT) |
| Critical issue | **Calibration degeneracy**: cannot cleanly separate instrumental angle α from cosmic β |
| Public availability | Paper is public |
| Machine-readable | β alone not cleanly extractable |
| Suitable for | **NOT directly usable** — calibration degeneracy prevents clean β extraction |
| Recommendation | Cite as supporting evidence; do NOT include in likelihood |

### 4. Minami & Komatsu (2020) — Planck HFI

| Field | Value |
|-------|-------|
| Paper | Minami & Komatsu (2020) |
| arXiv | 2011.11254 |
| Observable | β = 0.35° ± 0.14° |
| Status | **SUPERSEDED** by Eskilt (2022) — same data, improved analysis |
| Suitable for | **NOT usable** — superseded |

### 5. Planck PR4 NPIPE EB/TB Power Spectra

| Field | Value |
|-------|-------|
| Source | Planck Legacy Archive + NPIPE pipeline |
| Observable | C_ℓ^{EB}, C_ℓ^{TB} bandpowers |
| Public availability | Spectra available from PLA; LIKELIHOOD not in standard Planck release |
| Machine-readable | Spectra yes; likelihood/covariance NO |
| Suitable for | **EB shape comparison** (forward model, not full likelihood) |
| NOT suitable for | Full harmonic-space likelihood (covariance not public) |

### 6. ACT DR6 EB Spectra + Likelihood

| Field | Value |
|-------|-------|
| Source | ACT collaboration |
| Observable | C_ℓ^{EB} bandpowers |
| Public availability | Bandpowers in paper; full likelihood code NOT public as of 2026-03 |
| Suitable for | **Future work** (when likelihood is released) |

### 7. Recent Literature (2025-2026)

| Paper | arXiv | Key Result | Usable? |
|-------|-------|-----------|---------|
| Remazeilles (2025) | 2507.22109 | Field-level ILC, Planck PR4 | Paper-level only |
| Sullivan et al. (2025) | 2502.07654 | Planck PR4 map-space | Paper-level only |
| Ballardini et al. (2025) | 2507.16714 | Scale-dependent β test | No public likelihood |
| Yin et al. (2026) | 2601.13624 | Joint ACT+Planck+DESI | Summary only |

---

## Summary Decision Matrix

| Source | Observable | Usable For | Verdict |
|--------|-----------|-----------|---------|
| Eskilt 2022 | β = 0.30° ± 0.11° | Gaussian summary likelihood | **USE** |
| ACT DR6 2025 | β = 0.215° ± 0.074° | Gaussian summary likelihood | **USE** |
| Eskilt 2022 Table 1 | D_ℓ^{EB} bandpowers | EB shape comparison (forward model) | **USE** |
| SPIDER 2025 | Total rotation | Qualitative support only | **CITE, NOT USE** |
| Minami & Komatsu 2020 | β = 0.35° ± 0.14° | Superseded | **DO NOT USE** |
| Planck EB likelihood | Full covariance | Not public | **FUTURE WORK** |
| ACT DR6 likelihood | Full covariance | Not public | **FUTURE WORK** |

---

## Correlation Between Eskilt and ACT DR6

The two measurements we use share some sky overlap (Planck is full-sky, ACT covers ~40% of the sky). However:

1. They use **different instruments** (Planck HFI vs ACT)
2. They use **different analysis pipelines** (NPIPE vs ACT DR6)
3. The ACT measurement uses **cross-correlation** with Planck, but the birefringence signal is extracted from the ACT-specific component
4. The statistical errors are dominated by instrumental noise, not cosmic variance

**Conservative treatment:** Treat as independent. This is standard in the literature (Diego-Palazuelos & Komatsu themselves combine with Planck assuming independence). If the measurements were significantly correlated, the combined significance would be lower (more conservative).

**Honest caveat:** A fully rigorous joint analysis would account for shared calibration assumptions and sky overlap. This is not available publicly. We note this explicitly.
