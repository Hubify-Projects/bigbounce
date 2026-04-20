#!/usr/bin/env python3
"""
NEOWISE Path-C ecliptic-mask injection-recovery — P3-PATHC-INJECTION-RECOVERY (criterion #6)
============================================================================================
NEOWISE is not a retrained-BigAE survey under Path-C (the intervention is a
spatial mask, not a new model), so the spectral injection-recovery protocol used
for SDSS DR18 + LAMOST DR10 does not apply directly. Instead, this script runs
the NEOWISE analog: *mask injection-recovery*. We ask two questions:

  (A) Specificity: when the true population is isotropic (uniform on the sphere),
      how many sources does the `|β_ecl| < 80°` mask incorrectly reject?
      Expected answer: 1.52 % (spherical cap area with |latitude| > 80°,
      formula `1 - sin(θ)`). Any substantial deviation indicates the mask is
      mis-specified against the null hypothesis.

  (B) Sensitivity: when a known *polar-cap-injected* anomaly population is
      mixed into the isotropic background (simulating the scan-pattern
      systematics that motivated the mask in the first place), what fraction
      of the injected anomalies does the mask reject?
      Expected answer: ≥ 99 % at injection latitude |β_ecl| > 85°,
                       ≥ 90 % at injection latitude |β_ecl| > 82°.

The gate for criterion #6 is: BOTH (A) within ±0.3 % of the 1.52 % theoretical
and (B) ≥ 95 % recovery of the 85°-injected population. Passes demonstrate
that the Path-C ecliptic mask is both specific (does not over-reject the clean
catalog) and sensitive (catches the polar-cap artifact population that fire #84
observed at 2.57× the isotropic expectation).

Outputs written to this directory:
  - `neowise_mask_injection_recovery.json` — gate result + per-latitude-band stats

Run (local CPU, < 2 s):
    python3 pipelines/p3_anomaly_engine/pathc_neowise_ecliptic/neowise_mask_injection_recovery.py
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from astropy.coordinates import BarycentricTrueEcliptic, SkyCoord
import astropy.units as u

ROOT = Path(__file__).resolve().parent
OUT_JSON = ROOT / 'neowise_mask_injection_recovery.json'

SEED = 20260420
MASK_LATITUDE_DEG = 80.0           # Path-C mask: |β_ecl| < 80° retained
N_BG_ISOTROPIC = 100_000           # isotropic-sky injection pool
N_INJ_PER_BAND = 1_000             # injected anomalies per polar band
INJ_BANDS_DEG = [85.0, 82.0, 80.5] # injection |β_ecl| thresholds
GATE_SPECIFICITY_TOLERANCE = 0.003 # ±0.3 % of theoretical 1.52 % rejection
GATE_SENSITIVITY_85 = 0.95         # ≥ 95 % recovery of |β_ecl|>85° pop.


def sample_uniform_sphere(n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Sample n points uniformly on the celestial sphere. Returns (ra_deg, dec_deg)."""
    ra = rng.uniform(0.0, 360.0, size=n)
    # Area-preserving latitude sample: sin(dec) ~ Uniform(-1, 1)
    dec = np.degrees(np.arcsin(rng.uniform(-1.0, 1.0, size=n)))
    return ra, dec


def sample_polar_cap(n: int, lat_min_deg: float, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Sample n points uniformly in the spherical cap `|ecliptic_lat| > lat_min_deg`.

    Returns ecliptic (lon, lat) directly — the caller converts to ICRS if needed.
    Splits sampling between the two hemispherical caps (north & south)."""
    half = n // 2
    # North cap: sin(lat) ~ Uniform(sin(lat_min), 1)
    u_n = rng.uniform(np.sin(np.radians(lat_min_deg)), 1.0, size=half)
    lat_n = np.degrees(np.arcsin(u_n))
    # South cap: sin(lat) ~ Uniform(-1, -sin(lat_min))
    u_s = rng.uniform(-1.0, -np.sin(np.radians(lat_min_deg)), size=n - half)
    lat_s = np.degrees(np.arcsin(u_s))
    lat = np.concatenate([lat_n, lat_s])
    lon = rng.uniform(0.0, 360.0, size=n)
    return lon, lat


def ra_dec_to_ecliptic_lat(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    sc = SkyCoord(ra=ra_deg * u.deg, dec=dec_deg * u.deg, frame='icrs')
    return sc.transform_to(BarycentricTrueEcliptic()).lat.deg


def ecliptic_to_ra_dec(lon_deg: np.ndarray, lat_deg: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    sc = SkyCoord(lon=lon_deg * u.deg, lat=lat_deg * u.deg, frame=BarycentricTrueEcliptic())
    icrs = sc.transform_to('icrs')
    return icrs.ra.deg, icrs.dec.deg


def apply_mask(ecl_lat_deg: np.ndarray, cut_deg: float = MASK_LATITUDE_DEG) -> np.ndarray:
    """True = retained by Path-C mask (|β_ecl| < cut_deg)."""
    return np.abs(ecl_lat_deg) < cut_deg


def main() -> None:
    rng = np.random.default_rng(SEED)

    # --- (A) Specificity: isotropic-sphere rejection rate -------------------
    ra_bg, dec_bg = sample_uniform_sphere(N_BG_ISOTROPIC, rng)
    elat_bg = ra_dec_to_ecliptic_lat(ra_bg, dec_bg)
    retained_bg = apply_mask(elat_bg)
    bg_reject_frac = float((~retained_bg).sum() / N_BG_ISOTROPIC)
    theory_reject_frac = float(1.0 - np.sin(np.radians(MASK_LATITUDE_DEG)))  # ≈ 0.01519
    specificity_pass = abs(bg_reject_frac - theory_reject_frac) <= GATE_SPECIFICITY_TOLERANCE

    # --- (B) Sensitivity: polar-cap injection recovery per band --------------
    band_results: dict[str, dict[str, float]] = {}
    for lat_min in INJ_BANDS_DEG:
        lon_inj, lat_inj = sample_polar_cap(N_INJ_PER_BAND, lat_min, rng)
        # Convert through ICRS and back to exercise the same astropy path the
        # real mask code uses (integration test — not just an analytic identity).
        ra_inj, dec_inj = ecliptic_to_ra_dec(lon_inj, lat_inj)
        elat_recovered = ra_dec_to_ecliptic_lat(ra_inj, dec_inj)
        retained = apply_mask(elat_recovered)
        rejected_frac = float((~retained).sum() / N_INJ_PER_BAND)
        band_results[f'|b_ecl|>{lat_min:g}deg'] = {
            'n_injected': N_INJ_PER_BAND,
            'rejected_by_mask': int((~retained).sum()),
            'recovery_fraction': rejected_frac,
        }

    sens_85 = band_results[f'|b_ecl|>{INJ_BANDS_DEG[0]:g}deg']['recovery_fraction']
    sensitivity_pass = sens_85 >= GATE_SENSITIVITY_85

    gate_pass = bool(specificity_pass and sensitivity_pass)

    summary = {
        'task': 'P3-PATHC-INJECTION-RECOVERY (criterion #6) — NEOWISE mask analog',
        'seed': SEED,
        'mask_cut_deg': MASK_LATITUDE_DEG,
        'specificity': {
            'theory_reject_fraction': theory_reject_frac,
            'observed_reject_fraction': bg_reject_frac,
            'n_isotropic_sample': N_BG_ISOTROPIC,
            'tolerance': GATE_SPECIFICITY_TOLERANCE,
            'pass': bool(specificity_pass),
            'note': (
                'Isotropic-sphere rejection rate must match the spherical-cap '
                'area fraction `1 - sin(80°)` ≈ 1.52 %. This validates the mask '
                'does not over-reject the clean NEOWISE catalog.'
            ),
        },
        'sensitivity': {
            'bands': band_results,
            'gate_band': f'|b_ecl|>{INJ_BANDS_DEG[0]:g}deg',
            'gate_threshold': GATE_SENSITIVITY_85,
            'observed_at_gate_band': sens_85,
            'pass': bool(sensitivity_pass),
            'note': (
                'Polar-cap-injected anomaly population at |β_ecl| > 85° must '
                'be rejected at ≥ 95 % by the Path-C mask. This validates the '
                'mask catches the scan-pattern-systematic population motivating '
                'fire #84 (2.57× observed pole excess vs isotropic).'
            ),
        },
        'gate_pass': gate_pass,
        'interpretation': (
            'gate_pass=True ⇒ Path-C NEOWISE mask is both specific (clean-catalog '
            'false-positive rate matches theory) and sensitive (polar-cap '
            'injected anomalies are fully caught). Criterion #6 bullet for '
            'NEOWISE row is satisfied; remaining surveys (eROSITA, Gaia) '
            'deferred as non-spectral feature extractors.'
        ),
    }

    OUT_JSON.write_text(json.dumps(summary, indent=2))
    print(f'wrote {OUT_JSON}')
    print(f'  specificity: observed={bg_reject_frac:.4f} theory={theory_reject_frac:.4f} '
          f'Δ={bg_reject_frac - theory_reject_frac:+.4f} pass={specificity_pass}')
    for band, r in band_results.items():
        print(f'  sensitivity {band}: rejected {r["rejected_by_mask"]}/{r["n_injected"]} '
              f'= {r["recovery_fraction"]:.3f}')
    print(f'  gate_pass={gate_pass}')


if __name__ == '__main__':
    main()
