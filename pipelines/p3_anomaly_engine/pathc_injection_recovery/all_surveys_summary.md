# Path-C injection-recovery — all-surveys summary

_Generated 2026-04-20 · aggregates fires #85, #95, #98, #119, #120, #121 · 6/8 surveys covered · 3 gate PASS + 3 gate FAIL-with-diagnostic._

| Survey | Fire | Feature space | Injection | Gate @ 5σ | Pass | XV diagnostic | Headline |
|---|---|---|---|---:|:---:|---:|---|
| SDSS DR18 | #85 / #98 | 496-bin BigAE reconstruction MSE (128-dim latent,  | emission-line (fire #85) + continuum-dip | 64.0 % cont-dip / 7.2 % em-line | ✅ | — | CONTINUUM-DIP GATE PASS (64 |
| LAMOST DR10 | #85 / #98 | 496-bin BigAE reconstruction MSE (128-dim latent,  | emission-line (fire #85) + continuum-dip | 5.8 % cont-dip / 0.6 % em-line | ❌ | — | GATE FAIL-with-diagnostic (continuum-dip 5 |
| Planck CMB | #95 | 64×64 patch reconstruction MSE (128-dim latent, na | per-patch gaussian noise at α·σ | 100.0 % | ✅ | — | GATE PASS (100 |
| NEOWISE | #119 | Ecliptic-latitude spatial mask |β_ecl| < 80° | polar-cap anomaly injection + uniform-sp | spec 1.5 % (theory 1.5 %), sens 100.0 % @ 85° | ✅ | — | GATE PASS (specificity 1 |
| Gaia DR3 | #120 | 22-dim variability + astrometric | additive translation along 5 variability | 5.2 % | ❌ | 41.0 % | GATE FAIL-with-41 %-XV-diagnostic |
| eROSITA DR1 | #121 | 16-dim autoencoder latent (`lat_00..lat_15`) + | random unit-direction α·σ displacement o | 1.2 % | ❌ | 81.5 % | GATE FAIL-with-81 |

**Remaining 2/8 surveys:**
- **DESI DR1** — Awaits criterion #4 5-fold checkpoint suite so injection can run across all 5 folds and measure cross-fold recovery stability (staged fire #117, launch-gated on SDSS+LAMOST native re-scores freeing the A100).
- **ACT DR6** — Cross-transfer baseline only — not native-retrained under Path-C. Legitimately out of scope for native injection-recovery; participates in criterion #7 dedup via cross-transfer top-200.

**Cross-survey interpretation:** Six of eight surveys have Path-C injection-recovery validators on disk (SDSS / LAMOST / CMB / NEOWISE / Gaia / eROSITA). Three pass the strict 5σ or mask-analog gate (SDSS continuum-dip, CMB, NEOWISE); three fail-with-rigorous-diagnostic (LAMOST emission-line with 9.7× continuum-dip improvement, Gaia with 41 % XV, eROSITA with 81.5 % XV). The FAIL-with-diagnostic category is legitimate Path-C coverage per the fire-#85 / fire-#98 convention — each failure comes with a physics-grounded mechanism (128-latent in-manifold reconstruction / 22-dim non-variability-axis dominance / random-direction-latent subspace sampling) and a scientifically-relevant companion metric. The Gaia 41 % vs eROSITA 81.5 % XV spread is qualitatively diagnostic: Gaia needs a training-sample-conditioned footnote, eROSITA reports as final with a stability footnote. Paper 3 §pathc_caveats table structure should foreground this PASS / FAIL-with-diagnostic dichotomy and provide the full amplitude-sweep curves in an appendix.
