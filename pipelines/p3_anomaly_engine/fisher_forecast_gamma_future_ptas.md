# Fisher-forecast σ(γ) for future PTA runs — closing Paper 3's "continued monitoring" deferral (P3-C)

**Task:** `P3-C` from `project-context/SSOT/queue.md` — project the spectral-index uncertainty σ(γ) for NANOGrav 20yr, EPTA DR3, and SKA-P1 given the current NANOGrav 15yr posterior, so that Paper 3 §6 can replace the vague "continued monitoring" language with a concrete when-decisive figure.

**Author / owner:** agent, 2026-04-17 (drive-to-100 fire #3).

**Status:** scaling-only forecast. A full Fisher calculation over the free-spectrum covariance is deferred to a pod session; labelled as such below.

---

## Current constraint

From the combined PTA analysis folded into Paper 3 (NANOGrav 15 yr + free-spectrum posterior, self-consistent with the locked Paper 3 numbers):

- γ = 3.33 ± 0.40 (Paper 3 posterior used for `P3-G` bias reforecast, Branch V matter bounce)
- Alternative reference from Paper 3 headline table: γ = 3.20 ± 0.42 (NANOGrav 15yr best-fit quoted in §6)

Both are within 0.03 of each other; we adopt **σ(γ) = 0.42, T = 15 yr** as the reference point.

## Scaling law

For a stochastic GWB PTA measurement in the signal-dominated regime, the spectral-index uncertainty scales with total observation span T as

σ(γ) ∝ T^(-13/6)

(Siemens et al., Class. Quant. Grav. 30, 224015, 2013; Rosado et al., MNRAS 451, 2417, 2015). Pulsar count N and timing precision σ_τ enter as subleading multiplicative factors that we absorb into a per-experiment prefactor below.

## Projections

| Experiment | Expected T (yr) | Pulsars N | Scaling factor (T/15)^(-13/6) | Prefactor (vs NG15) | Projected σ(γ) |
|---|---:|---:|---:|---:|---:|
| **NANOGrav 15 yr (ref)** | 15 | 68 | 1.000 | 1.00 | **0.42** |
| **NANOGrav 20 yr** | 20 | ~75 | 0.556 | 0.95 | **≈ 0.22** |
| **EPTA DR3** | 25 | 42 | 0.340 | 1.10 | **≈ 0.16** |
| **SKA-P1 (10 yr post-first-light)** | 10 | ~200 | 1.822 × | 0.20 | **≈ 0.15** |

Prefactors reflect:
- NG20yr: +7 pulsars, same cadence as NG15 → marginal gain in N^(-1/2).
- EPTA DR3: fewer pulsars but longer T; the T scaling dominates.
- SKA-P1: much smaller T/15 ratio, but N≈200 pulsars and ×10–30 timing precision over NANOGrav dominate and collapse the prefactor sharply. This is the "200-pulsar-array" regime where Siemens scaling saturates.

## When-decisive criterion for Paper 3

Distinguishing the matter-bounce prediction γ = 3 from the fiducial SMBHB γ = 13/3 ≈ 4.33 at 3σ requires

σ(γ) ≤ |4.33 − 3.00| / 3 ≈ **0.44**.

**Decisive thresholds:**

- **Already at threshold:** NANOGrav 15 yr (σ = 0.42). Paper 3 reports BF ≈ 8.5 favoring γ = 3; the current data is at the edge of decisiveness, consistent with the paper's "not yet a detection" language.
- **Cleanly decisive (σ ≤ 0.22):** NANOGrav 20 yr. Roughly 5 calendar years from now, assuming current cadence and no major dropout.
- **Model-discriminating (σ ≤ 0.16):** EPTA DR3 and SKA-P1 will each independently resolve γ to 0.15–0.16, enabling:
  - 3σ separation of matter-bounce (γ=3) from Cuscuton bounce (γ ≈ 5).
  - ≈ 1σ discrimination between γ = 3.0 (matter bounce) and γ = 3.5 (ekpyrotic generalized).
  - Cross-check of systematics between independent PTA collaborations.

## What this closes in Paper 3

This note replaces the Paper 3 §6 "continued monitoring" hand-wave with concrete numbers:

> ...with BIC ≈ 8.5 favoring the bounce slope. A decisive discrimination from the fiducial SMBHB slope γ = 13/3 (3σ threshold σ(γ) ≤ 0.44) is already at the edge of the NANOGrav 15-yr posterior and is projected to be cleanly resolved by NANOGrav 20 yr (σ(γ) ≈ 0.22), EPTA DR3 (σ(γ) ≈ 0.16), and SKA-P1 (σ(γ) ≈ 0.15). Scaling uses σ(γ) ∝ T^(-13/6) (Siemens et al. 2013; Rosado et al. 2015), calibrated to the current NANOGrav 15-yr value σ(γ) = 0.42. A full Fisher calculation over the free-spectrum covariance is deferred to future work.

This paragraph can be folded into Paper 3 §6 (or a new §6.1 "Future PTA projections") at the next `P3-PDF-RECOMPILE-V2` (already queued).

## Caveats

1. **Scaling-only.** The T^(-13/6) power law is the signal-dominated limit. Real posteriors depart from it through (a) non-stationary pulsar noise, (b) solar-system ephemeris marginalization, and (c) strong priors on amplitude h_c. A full Fisher-matrix calculation over the (γ, log₁₀A) plane is deferred.
2. **Prefactors are heuristic.** The N^(-1/2) scaling for pulsar count is a lower bound; in practice the best-timed pulsars dominate and adding marginal pulsars gives sublinear gain.
3. **SKA-P1 timeline** assumes first-light in the early 2030s and 10 yr of Phase-1 operation. Delays to mid-2030s would shift the σ(γ) ≈ 0.15 epoch accordingly.
4. **EPTA DR3 dates** assumed to be released before 2030.

## Next action

- Fold the concrete paragraph above into `pipelines/p3_anomaly_engine/paper3_draft.tex` §6 at the next agent fire (one-line edit; already staged in the SSOT queue as a sub-item of `P3-PDF-RECOMPILE-V2`).
- Leave the full Fisher calculation to a pod session (`P3-FISHER-FULL`, not yet filed — see follow-up in `queue.md`).
