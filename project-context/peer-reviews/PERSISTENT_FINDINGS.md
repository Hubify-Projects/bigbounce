# Persistent Meta-Findings Tracker

Tracking META findings across 10 autoloop fires.
Rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt', 'auto-2026-06-05_1617pt', 'auto-2026-06-05_1717pt', 'auto-2026-06-05_1817pt', 'auto-2026-06-05_1919pt', 'auto-2026-06-06_0004pt', 'auto-2026-06-06_0021pt', 'auto-2026-06-08_1144pt', 'auto-2026-06-08_1354pt']

## Findings that persist ≥2 rounds (escalation candidates for Houston decision)

Persistent META findings indicate scientific issues that the v3.2 meta-reviewer
consistently surfaces. They are NOT mechanical bugs — they require Houston's
judgment on which fix to apply (mechanical text edit vs analysis rerun vs
text relabel).

### 🔴 LOAD-BEARING P3 — `dedup` (4/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1817pt', 'auto-2026-06-06_0004pt', 'auto-2026-06-06_0021pt']

Example (round auto-2026-06-05_1418pt, finding P3-META-E2):

> The footnote claims a “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938.” Summing these per-survey Path-C counts gives 195,829 + 77,905 + 298 + 500 + 419 + 200 = 275,151. Subtracting the global dedup count 10,213 produces 275,151 − 10,213 = 264,938 — exac

### 🔴 LOAD-BEARING P4 — `cross-match` (4/10 rounds)

Seen in rounds: ['auto-2026-06-05_1517pt', 'auto-2026-06-05_1717pt', 'auto-2026-06-05_1817pt', 'auto-2026-06-06_0004pt']

Example (round auto-2026-06-05_1517pt, finding P4-META-M6):

> “Sky coordinates are obtained by cross-matching against the Galaxy Zoo DESI predictions catalog [9].” The DESI Legacy DR8 source table already contains RA/Dec keyed by dr8_id. Pulling positions from a separate predictions table introduces the risk of coordinate drift, duplicates, or selection-functi

### 🔴 LOAD-BEARING P5 — `label` (4/10 rounds)

Seen in rounds: ['auto-2026-06-05_1517pt', 'auto-2026-06-05_1617pt', 'auto-2026-06-05_1717pt', 'auto-2026-06-06_0021pt']

Example (round auto-2026-06-05_1517pt, finding P5-META-M1):

> “For hypothesis tests we run two complementary nulls: (i) a label-shuffle permutation… (ii) a position-shuffle that preserves labels but scrambles positions.”

### 🔴 LOAD-BEARING P4 — `master` (4/10 rounds)

Seen in rounds: ['auto-2026-06-05_1717pt', 'auto-2026-06-06_0004pt', 'auto-2026-06-06_0021pt', 'auto-2026-06-08_1354pt']

Example (round auto-2026-06-05_1717pt, finding P4-META-m4):

> “the MASTER mode-coupling matrix does NOT include ℓ=0 on either the input or output side.” NaMaster typically handles ℓ ranges explicitly; removing ℓ=0 by pre-subtraction is fine, but excluding ℓ=0 from the coupling matrix should be documented with exact code options and checked for side effects at 

### 🔴 LOAD-BEARING P3 — `deduplication` (3/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1717pt', 'auto-2026-06-08_1354pt']

Example (round auto-2026-06-05_1418pt, finding P3-META-M8):

> “For the 7-way 5″ deduplication, the expected random coincidence contribution is ≲ 10 across all survey pairs against 637 observed multi-survey clusters (<2% contamination).” Given the large numbers of anomalies and heterogeneous footprints, ≲10 total random overlaps is implausibly low without a det

### 🔴 LOAD-BEARING P4 — `table_ii` (3/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1817pt', 'auto-2026-06-08_1354pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-M5):

> - Table III: “Joint χ2/dof (38 bandpowers) — 161.2/38 = 4.24”

### 🔴 LOAD-BEARING P4 — `binomial` (3/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt', 'auto-2026-06-05_1617pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-m11):

> The pixel-space dipole fit (NSIDE=64, pixels with >10 spirals) does not state whether pixels are inverse-variance weighted (∝ Nspiral) or equally weighted. For a binomial-derived asymmetry per pixel, equal weighting is suboptimal and can bias the amplitude uncertainty.

### 🔴 LOAD-BEARING P5 — `v-web` (3/10 rounds)

Seen in rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-05_1817pt', 'auto-2026-06-08_1144pt']

Example (round auto-2026-06-05_1617pt, finding P5-META-E2):

> All per-class “predicted” deviations use a single global ΔfCW = −0.0026 from Paper IV (σpred = 2Δf√N) even though the paper shows V-Web class and DESI target program are not independent and that the bright vs dark samples have opposite-signed offsets. Using a single Δf for all classes implicitly ass

### 🔴 LOAD-BEARING P1B — `leakage` (3/10 rounds)

Seen in rounds: ['auto-2026-06-05_1817pt', 'auto-2026-06-06_0004pt', 'auto-2026-06-08_1144pt']

Example (round auto-2026-06-05_1817pt, finding P1B-META-M5):

> The MC noise is isotropic (“ΔP = 10 μK·arcmin”) and does not include Planck-like hit-count anisotropy. Anisotropic noise combined with a sky mask can create EB leakage patterns and alter the β̂ bias/variance relative to an isotropic approximation.

### 🟡 RECURRING P4 — `monopole` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-E1):

> - Appendix A(a): “the headline dipole estimator … uses … the monopole-subtracted CW-deficit map fCW(n) − 0.5 on the subsample mask…”

### 🟡 RECURRING P4 — `leakage|master|monopole|post-master|pre-master` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1717pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-E3):

> - “The monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cℓ at ℓ = 1 … MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage: the post-MASTER ℓ = 1 on the strict-superset subsample mask is −0.122σ; the canonical-mask post-MASTER residual is +3.64σ…”

### 🟡 RECURRING P4 — `label` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-06_0004pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-M6):

> - Appendix A(c): “Null distribution: 500 per-pixel random-label permutation realizations.”

### 🟡 RECURRING P5 — `radial|selection_function` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-08_1144pt']

Example (round auto-2026-06-05_1418pt, finding P5-META-E1):

> The pipeline deposits raw galaxy counts into a 256^3 grid, computes a single global mean density “ρ̄cell = 4.64 galaxies/cell” inside the dilated mask, and defines δ = ρ/ρ̄ − 1. There is no correction for the DESI spectroscopic selection function (radial n(z) and angular completeness), no use of a r

### 🟡 RECURRING P5 — `tidal_tensor` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-08_1354pt']

Example (round auto-2026-06-05_1418pt, finding P5-META-M4):

> The power spectrum of a CIC-deposited discrete field includes a Poisson shot-noise term. The text proceeds to smooth δ and solve for Φ(k) without subtracting shot noise or demonstrating that Gaussian smoothing sufficiently suppresses it. The resulting tidal tensor will be contaminated by grid-scale 

### 🟡 RECURRING P1A — `abstract` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1517pt', 'auto-2026-06-08_1144pt']

Example (round auto-2026-06-05_1517pt, finding P1A-META-E1):

> The manuscript repeatedly misidentifies the Holst term (linear in curvature) with the Pontryagin density (quadratic in curvature). In the abstract: “the Holst dual contraction ϵμνρσRμνρσ reduces on the Levi-Civita connection to the Pontryagin density ∝ R R̃ — generically non-zero pointwise but a tot

### 🟡 RECURRING P1B — `label` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1517pt', 'auto-2026-06-05_1817pt']

Example (round auto-2026-06-05_1517pt, finding P1B-META-m1):

> The derived-parameter label “109As” is ambiguous (is it 10^9 As or a typographical error?). Standard practice is ln(10^10 As) or 10^9 As explicitly.

### 🟡 RECURRING P4 — `leakage` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1517pt', 'auto-2026-06-06_0021pt']

Example (round auto-2026-06-05_1517pt, finding P4-META-M1):

> T5 “metadata leakage” tests |r(pCW, RA/Dec)|<0.10. Correlating with RA or Dec separately is not rotation-invariant on the sphere and is largely uninformative for a generic dipole at an arbitrary orientation. A true dipole aligned off the equator can show near-zero linear correlation with either RA o

### 🟡 RECURRING P1B — `table_ii` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']

Example (round auto-2026-06-05_1617pt, finding P1B-META-m1):

> “Appendix B: Claims Classification” heading appears, but the appendix body is empty; the only content is a separate Table III on the next page.

### 🟡 RECURRING P4 — `fsky` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1717pt', 'auto-2026-06-05_1817pt']

Example (round auto-2026-06-05_1717pt, finding P4-META-E1):

> Implausible sky fractions. The paper repeatedly states “fsky = 0.659” for the headline “subsample mask” and “fsky = 0.49005” for the “canonical mask.” DESI Legacy DR8’s imaging footprint is O(10^4) deg^2 (≲ 0.4 of the sky). fsky ≈ 0.66 implies ≈27,000 deg^2, far larger than the DESI Legacy footprint

### 🟡 RECURRING P5 — `table_iv` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1717pt', 'auto-2026-06-06_0004pt']

Example (round auto-2026-06-05_1717pt, finding P5-META-m2):

> Table IV bins “cluster” and “filament” by “V‑Web per‑galaxy density,” but the paper never defines this quantity precisely (is it 1+δ, log(1+δ), or the smoothed δ rescaled; is it measured at the galaxy via interpolation or cell mean?). Without a definition, the quartile labels and their physical inte

### 🟡 RECURRING P4 — `binomial|monopole` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1817pt', 'auto-2026-06-06_0021pt']

Example (round auto-2026-06-05_1817pt, finding P4-META-M1):

> Ambiguity in the monopole-only generative null trials parameter. The text: “per-pixel CW count is drawn from Binomial(ntotal, pglobalCW) on the exact canonical mask,” but “ntotal” is undefined here. If ntotal denotes N(p)all (CW+CCW+NS), it is inappropriate for a CW/CCW binomial and will bias both t

### 🟡 RECURRING P5 — `table_ii` (2/10 rounds)

Seen in rounds: ['auto-2026-06-05_1817pt', 'auto-2026-06-06_0021pt']

Example (round auto-2026-06-05_1817pt, finding P5-META-M1):

> “filament bright (n = 416,701) … filament dark (n = 21,203).” These two counts sum to 437,904, exceeding the filament total n = 408,187 reported in Table II for the headline sample. The section does not state that a different superset (812,793) is being used here, creating an internal inconsistency 

### 🟡 RECURRING P1B — `fsky` (2/10 rounds)

Seen in rounds: ['auto-2026-06-06_0004pt', 'auto-2026-06-08_1354pt']

Example (round auto-2026-06-06_0004pt, finding P1B-META-E7):

> “The mask uses C2 apodization at 2° scale… fsky = 0.32…”

### 🟡 RECURRING P3 — `cross-match` (2/10 rounds)

Seen in rounds: ['auto-2026-06-06_0021pt', 'auto-2026-06-08_1144pt']

Example (round auto-2026-06-06_0021pt, finding P3-META-M6):

> “cross-matched against 20 curated all-sky catalogs via CDS X-Match (… NVSS, VLASS, 4XMM, Chandra, …) using a 5-arcsec cone; archival-ID rate 82.2%.”
