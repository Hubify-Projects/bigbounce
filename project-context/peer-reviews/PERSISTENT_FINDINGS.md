# Persistent Meta-Findings Tracker

Tracking META findings across 5 autoloop fires.
Rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt', 'auto-2026-06-05_1617pt', 'auto-2026-06-05_1717pt', 'auto-2026-06-05_1817pt']

## Findings that persist ≥2 rounds (escalation candidates for Houston decision)

Persistent META findings indicate scientific issues that the v3.2 meta-reviewer
consistently surfaces. They are NOT mechanical bugs — they require Houston's
judgment on which fix to apply (mechanical text edit vs analysis rerun vs
text relabel).

### 🔴 LOAD-BEARING P1B — `lee` (5/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt', 'auto-2026-06-05_1617pt', 'auto-2026-06-05_1717pt', 'auto-2026-06-05_1817pt']

Example (round auto-2026-06-05_1418pt, finding P1B-META-E1):

> “17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb for the SNIa absolute magnitude).”

### 🔴 LOAD-BEARING P1B — `master` (3/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1617pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P1B-META-M6):

> The paper adopts a “NaMaster systematic floor” of ~0.04° from the pipeline test, but does not propagate any comparable systematic into its internal βfree fit (0.344° ± 0.096°). If the same pseudo-Cℓ machinery or masking is used in the EB likelihood, a comparable configuration-dependent bias may appl

### 🔴 LOAD-BEARING P3 — `dedup|deduplication` (3/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P3-META-M8):

> “For the 7-way 5″ deduplication, the expected random coincidence contribution is ≲ 10 across all survey pairs against 637 observed multi-survey clusters (<2% contamination).” Given the large numbers of anomalies and heterogeneous footprints, ≲10 total random overlaps is implausibly low without a det

### 🔴 LOAD-BEARING P4 — `leakage|master|monopole` (3/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1617pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-E3):

> - “The monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cℓ at ℓ = 1 … MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage: the post-MASTER ℓ = 1 on the strict-superset subsample mask is −0.122σ; the canonical-mask post-MASTER residual is +3.64σ…”

### 🔴 LOAD-BEARING P4 — `binomial` (3/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt', 'auto-2026-06-05_1617pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-m11):

> The pixel-space dipole fit (NSIDE=64, pixels with >10 spirals) does not state whether pixels are inverse-variance weighted (∝ Nspiral) or equally weighted. For a binomial-derived asymmetry per pixel, equal weighting is suboptimal and can bias the amplitude uncertainty.

### 🟡 RECURRING P3 — `dedup` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1817pt']

Example (round auto-2026-06-05_1418pt, finding P3-META-E2):

> The footnote claims a “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938.” Summing these per-survey Path-C counts gives 195,829 + 77,905 + 298 + 500 + 419 + 200 = 275,151. Subtracting the global dedup count 10,213 produces 275,151 − 10,213 = 264,938 — exac

### 🟡 RECURRING P4 — `monopole` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-E1):

> - Appendix A(a): “the headline dipole estimator … uses … the monopole-subtracted CW-deficit map fCW(n) − 0.5 on the subsample mask…”

### 🟡 RECURRING P4 — `master` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-E2):

> - Appendix A(a): “The NaMaster weight (mask) map assigns Wp = N(p)all = NCW + NCCW + NNS … a standard survey-depth proxy.”

### 🟡 RECURRING P4 — `table_ii` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1817pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-M5):

> - Table III: “Joint χ2/dof (38 bandpowers) — 161.2/38 = 4.24”

### 🟡 RECURRING P5 — `tidal_tensor` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P5-META-M4):

> The power spectrum of a CIC-deposited discrete field includes a Poisson shot-noise term. The text proceeds to smooth δ and solve for Φ(k) without subtracting shot noise or demonstrating that Gaussian smoothing sufficiently suppresses it. The resulting tidal tensor will be contaminated by grid-scale 

### 🟡 RECURRING P1B — `table_ii` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1617pt, finding P1B-META-m1):

> “Appendix B: Claims Classification” heading appears, but the appendix body is empty; the only content is a separate Table III on the next page.

### 🟡 RECURRING P5 — `monopole` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-05_1817pt']

Example (round auto-2026-06-05_1617pt, finding P5-META-M5):

> The Methods promise two nulls (“(i) label-shuffle; (ii) position-shuffle”), but only label-shuffle p-values are reported. Position-shuffle results are not shown anywhere, despite being methodologically different (and important when labels may carry global monopoles).

### 🟡 RECURRING P4 — `fsky` (2/5 rounds)

Seen in rounds: ['auto-2026-06-05_1717pt', 'auto-2026-06-05_1817pt']

Example (round auto-2026-06-05_1717pt, finding P4-META-E1):

> Implausible sky fractions. The paper repeatedly states “fsky = 0.659” for the headline “subsample mask” and “fsky = 0.49005” for the “canonical mask.” DESI Legacy DR8’s imaging footprint is O(10^4) deg^2 (≲ 0.4 of the sky). fsky ≈ 0.66 implies ≈27,000 deg^2, far larger than the DESI Legacy footprint
