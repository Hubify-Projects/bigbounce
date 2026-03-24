#!/usr/bin/env python3
"""
F1.3 — Bispectrum Injection / Recovery Test (Tier 3A)

Validates whether the template-recast methodology correctly predicts the
amplitude recovery from a local-template estimator when the true signal
is the matter-bounce bispectrum.

WHAT THIS SCRIPT DOES:
  1. Generates Gaussian random fields on a 2D grid
  2. Injects non-Gaussianity with either local or bounce shape
  3. Measures the bispectrum of the non-Gaussian field
  4. Fits local and bounce templates to the measured bispectrum
  5. Compares recovered f_NL values across three injection scenarios:
     A. LOCAL injection  → local recovery → calibration baseline
     B. BOUNCE injection → local recovery → should get r * (Test A value)
     C. NULL injection   → any recovery   → should get 0 ± noise

PURPOSE:
  Validate that the ratio of recovered amplitudes (B vs A) matches the
  analytically computed template overlap r = 0.84-0.88.  This upgrades
  the F1.1 TRIAGE_RECAST to INJECTION_VALIDATED.

METHODOLOGY:
  This is a RATIO test.  The absolute normalization of the bispectrum
  estimator is convention-dependent and involves FFT normalization factors.
  What matters physically is:
    r = f_NL^{local estimator on bounce signal} / f_NL^{local estimator on local signal}
  This ratio cancels all normalization factors and directly tests the
  shape overlap.

APPROACH:
  Uses 2D Fourier-space fields with boosted amplitude (A_s = 0.1) to
  achieve high S/N per realization.  The boosted amplitude does NOT
  affect the shape overlap ratio, which is a geometric property of the
  templates.  This is a methodology validation, not a real CMB analysis.

References:
  Cai et al. (2009): matter-bounce bispectrum
  Planck 2018 IX (1905.05697): local f_NL constraint
  Phase 1 robustness audit: template overlap r = 0.876 (CMB Fisher)

Author: Houston Golden
Date: 2026-03-22
"""

import json
import time
import numpy as np
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════

OUTDIR = Path(__file__).parent.parent / "outputs"
OUTDIR.mkdir(exist_ok=True)

N_GRID = 128            # grid size (NxN)
L_BOX = 1.0             # box length
K_FUND = 2 * np.pi / L_BOX

F_NL_INJECT = -35.0 / 8.0  # = -4.375 (canonical matter-bounce)

# Boosted amplitude for high S/N.  Does NOT affect the ratio r.
A_S = 0.1

N_REALIZATIONS = 200    # Monte Carlo realizations
BASE_SEED = 20260322

# Verified Cai polynomial coefficients (from Phase 1 robustness audit)
PREFACTOR = 3.0 / 256.0
C_BOUNCE = (2, 7, 3, -12, -69, 19)

N_KBINS = 10


# ═══════════════════════════════════════════════════════════════════════
# BOUNCE SHAPE FUNCTION
# ═══════════════════════════════════════════════════════════════════════

def bounce_BNL(k1, k2, k3):
    """
    BNL for the matter-bounce bispectrum (scalar inputs).
    Squeezed → -4.375, Equilateral → -3.984, Folded → -2.250.
    """
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    if pk2 < 1e-30:
        return -4.375
    sk3 = k1**3 + k2**3 + k3**3
    if sk3 < 1e-30:
        return -4.375

    s9 = sum(k**9 for k in ks)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)

    bracket = (C_BOUNCE[0]*s9 + C_BOUNCE[1]*s72 + C_BOUNCE[2]*s63
               + C_BOUNCE[3]*s54 + C_BOUNCE[4]*s522 + C_BOUNCE[5]*s432)
    AT = (PREFACTOR / pk2) * bracket
    return (10.0 / 3.0) * AT / sk3


# ═══════════════════════════════════════════════════════════════════════
# PRECOMPUTE SHAPE RATIO TABLE
# ═══════════════════════════════════════════════════════════════════════

def build_bnl_ratio_table(k_centers):
    """
    BNL_bounce(k1,k2,k3) / BNL_local for all bin triplets.
    BNL_local = -35/8 everywhere.
    """
    n = len(k_centers)
    ratio_table = np.zeros((n, n, n))
    valid_table = np.zeros((n, n, n), dtype=bool)

    for i in range(n):
        for j in range(i, n):
            for l in range(j, n):
                ki, kj, kl = k_centers[i], k_centers[j], k_centers[l]
                if kl > ki + kj or ki > kj + kl:
                    continue
                bnl = bounce_BNL(ki, kj, kl)
                r = bnl / (-35.0 / 8.0)
                for ii, jj, ll in [(i,j,l), (i,l,j), (j,i,l), (j,l,i), (l,i,j), (l,j,i)]:
                    ratio_table[ii, jj, ll] = r
                    valid_table[ii, jj, ll] = True

    return ratio_table, valid_table


# ═══════════════════════════════════════════════════════════════════════
# FIELD GENERATION
# ═══════════════════════════════════════════════════════════════════════

def make_kgrid(N, L):
    """k-space grid and power spectrum."""
    kx = np.fft.fftfreq(N, d=L/N) * 2 * np.pi
    ky = np.fft.fftfreq(N, d=L/N) * 2 * np.pi
    KX, KY = np.meshgrid(kx, ky)
    K = np.sqrt(KX**2 + KY**2)
    K[0, 0] = 1.0
    Pk = A_S / K**2
    Pk[0, 0] = 0.0
    return KX, KY, K, Pk


def generate_gaussian_field(rng, N, L, K, Pk):
    """Generate Gaussian random field in 2D."""
    sigma_k = np.sqrt(Pk / 2.0)
    zeta_k = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) * sigma_k
    # Reality condition
    for i in range(N):
        for j in range(N // 2 + 1, N):
            zeta_k[i, j] = np.conj(zeta_k[(-i) % N, (-j) % N])
    zeta_k[0, 0] = 0.0
    zeta_k[0, N//2] = np.real(zeta_k[0, N//2])
    zeta_k[N//2, 0] = np.real(zeta_k[N//2, 0])
    zeta_k[N//2, N//2] = np.real(zeta_k[N//2, N//2])
    zeta_x = np.fft.ifft2(zeta_k).real * N**2
    return zeta_x, zeta_k


def inject_local_ng(zeta_G_x, f_NL):
    """zeta = zeta_G + (3/5) f_NL (zeta_G^2 - <zeta_G^2>)"""
    zeta_G2 = zeta_G_x**2 - np.mean(zeta_G_x**2)
    return zeta_G_x + (3.0 / 5.0) * f_NL * zeta_G2


def inject_bounce_ng(zeta_G_k, f_NL, K, N, L, k_edges, k_centers, ratio_table):
    """
    Inject bounce-shape non-Gaussianity.

    The bounce bispectrum = local bispectrum * BNL_ratio(k1,k2,k3).
    We implement this by decomposing the quadratic convolution into k-bin
    pairs, each weighted by the BNL ratio averaged over the output bin.

    zeta(x) = zeta_G(x) + (3/5) f_NL * SUM_{a,b} r_avg(a,b) * F_a(x)*F_b(x)

    where F_a(x) = IFFT[zeta_G(k) * mask_a(k)].
    """
    n_bins = len(k_centers)
    bin_map = np.digitize(K.ravel(), k_edges) - 1
    bin_map = np.clip(bin_map, 0, n_bins - 1).reshape(N, N)

    # Per-bin fields in real space
    fields_x = []
    for b in range(n_bins):
        mask = (bin_map == b)
        fk = np.zeros((N, N), dtype=np.complex128)
        fk[mask] = zeta_G_k[mask]
        fx = np.fft.ifft2(fk).real * N**2
        fields_x.append(fx)

    # Average BNL ratio over output bin
    r_avg = np.ones((n_bins, n_bins))
    for a in range(n_bins):
        for b in range(n_bins):
            vals = ratio_table[a, b, :]
            mask_valid = np.abs(vals) > 0
            if mask_valid.any():
                r_avg[a, b] = np.mean(vals[mask_valid])

    # Accumulate: SUM_{a<=b} multiplicity * r(a,b) * F_a * F_b
    zeta_NG_x = np.zeros((N, N))
    for a in range(n_bins):
        for b in range(a, n_bins):
            product = fields_x[a] * fields_x[b]
            weight = r_avg[a, b]
            mult = 1.0 if a == b else 2.0
            zeta_NG_x += mult * weight * product

    zeta_NG_x -= np.mean(zeta_NG_x)

    zeta_G_x = np.fft.ifft2(zeta_G_k).real * N**2
    return zeta_G_x + (3.0 / 5.0) * f_NL * zeta_NG_x


# ═══════════════════════════════════════════════════════════════════════
# BISPECTRUM MEASUREMENT (cubic estimator via bin-filtered fields)
# ═══════════════════════════════════════════════════════════════════════

def measure_bispectrum(field_k, K, N, k_edges, k_centers):
    """
    Measure binned bispectrum B(b1, b2, b3) via the triple-product method:
      B(a,b,c) propto SUM_x f_a(x) * f_b(x) * f_c(x)
    where f_a(x) = IFFT[field(k) * mask_a(k)].
    """
    n_bins = len(k_centers)
    bin_map = np.digitize(K.ravel(), k_edges) - 1
    bin_map = np.clip(bin_map, 0, n_bins - 1).reshape(N, N)

    fields_x = []
    n_modes = []
    for b in range(n_bins):
        mask = (bin_map == b)
        fk = np.zeros((N, N), dtype=np.complex128)
        fk[mask] = field_k[mask]
        fx = np.fft.ifft2(fk).real * N**2
        fields_x.append(fx)
        n_modes.append(int(mask.sum()))

    bispec = {}
    for a in range(n_bins):
        for b in range(a, n_bins):
            for c in range(b, n_bins):
                ka, kb, kc = k_centers[a], k_centers[b], k_centers[c]
                if kc > ka + kb or ka > kb + kc:
                    continue

                triple = np.sum(fields_x[a] * fields_x[b] * fields_x[c])
                n_tri = max(n_modes[a] * n_modes[b] * n_modes[c], 1)

                bispec[(a, b, c)] = {
                    'B': float(triple),
                    'k1': ka, 'k2': kb, 'k3': kc,
                    'n_modes': (n_modes[a], n_modes[b], n_modes[c]),
                    'n_tri': n_tri,
                }

    return bispec


def fit_fnl_estimator(bispec_meas, template_type, k_centers, ratio_table, Pk_centers):
    """
    Optimal (matched-filter) f_NL estimator.

    f_NL_hat = SUM_i w_i B_i T_i / SUM_i w_i T_i^2

    The template T_i encodes the SHAPE of the bispectrum (local or bounce).
    For local: T propto P(k1)P(k2) + cyc
    For bounce: T propto r(k1,k2,k3) * [P(k1)P(k2) + cyc]

    The absolute normalization cancels in the ratio test.
    """
    numerator = 0.0
    denominator = 0.0

    for (a, b, c), data in bispec_meas.items():
        B_meas = data['B']
        n_tri = data['n_tri']

        P1, P2, P3 = Pk_centers[a], Pk_centers[b], Pk_centers[c]
        T_local = P1 * P2 + P1 * P3 + P2 * P3

        if template_type == 'local':
            T = T_local
        elif template_type == 'bounce':
            r = ratio_table[a, b, c] if ratio_table[a, b, c] != 0 else 1.0
            T = T_local * r
        else:
            raise ValueError(f"Unknown template: {template_type}")

        if abs(T) < 1e-50:
            continue

        w = float(n_tri)
        numerator += w * B_meas * T
        denominator += w * T * T

    if abs(denominator) < 1e-100:
        return 0.0

    return numerator / denominator


# ═══════════════════════════════════════════════════════════════════════
# SINGLE REALIZATION
# ═══════════════════════════════════════════════════════════════════════

def run_single(seed, injection_type, f_NL_inj, KX, KY, K, Pk,
               k_edges, k_centers, ratio_table, Pk_centers):
    rng = np.random.default_rng(seed)
    N, L = N_GRID, L_BOX

    zeta_G_x, zeta_G_k = generate_gaussian_field(rng, N, L, K, Pk)

    if injection_type == 'null':
        zeta_x = zeta_G_x.copy()
    elif injection_type == 'local':
        zeta_x = inject_local_ng(zeta_G_x, f_NL_inj)
    elif injection_type == 'bounce':
        zeta_x = inject_bounce_ng(zeta_G_k, f_NL_inj, K, N, L,
                                   k_edges, k_centers, ratio_table)
    else:
        raise ValueError(f"Unknown injection: {injection_type}")

    zeta_k = np.fft.fft2(zeta_x) / N**2

    bispec = measure_bispectrum(zeta_k, K, N, k_edges, k_centers)
    if len(bispec) < 3:
        return None

    f_local = fit_fnl_estimator(bispec, 'local', k_centers, ratio_table, Pk_centers)
    f_bounce = fit_fnl_estimator(bispec, 'bounce', k_centers, ratio_table, Pk_centers)

    return {
        'f_NL_local_fit': float(f_local),
        'f_NL_bounce_fit': float(f_bounce),
        'n_bins_used': len(bispec),
    }


# ═══════════════════════════════════════════════════════════════════════
# ENSEMBLE
# ═══════════════════════════════════════════════════════════════════════

def run_ensemble(injection_type, f_NL_inj, n_real, label, KX, KY, K, Pk,
                 k_edges, k_centers, ratio_table, Pk_centers):
    print(f"\n  {'='*60}")
    print(f"  TEST {label}: injection={injection_type}, f_NL_inj={f_NL_inj}")
    print(f"  {'='*60}")

    f_local_all, f_bounce_all = [], []
    t0 = time.time()

    for i in range(n_real):
        seed = BASE_SEED + i * 7 + hash(injection_type) % 100000
        result = run_single(seed, injection_type, f_NL_inj, KX, KY, K, Pk,
                            k_edges, k_centers, ratio_table, Pk_centers)
        if result is not None:
            f_local_all.append(result['f_NL_local_fit'])
            f_bounce_all.append(result['f_NL_bounce_fit'])

        if (i + 1) % 50 == 0:
            print(f"    ... {i+1}/{n_real} ({time.time()-t0:.1f}s)")

    elapsed = time.time() - t0
    n_success = len(f_local_all)
    print(f"    Done: {n_success}/{n_real} in {elapsed:.1f}s")

    if n_success < 5:
        return None

    f_local = np.array(f_local_all)
    f_bounce = np.array(f_bounce_all)

    stats = {
        'injection_type': injection_type,
        'f_NL_injected': float(f_NL_inj),
        'n_realizations': int(n_success),
        'local_estimator': {
            'mean': float(np.mean(f_local)),
            'median': float(np.median(f_local)),
            'std': float(np.std(f_local)),
            'sem': float(np.std(f_local) / np.sqrt(n_success)),
        },
        'bounce_estimator': {
            'mean': float(np.mean(f_bounce)),
            'median': float(np.median(f_bounce)),
            'std': float(np.std(f_bounce)),
            'sem': float(np.std(f_bounce) / np.sqrt(n_success)),
        },
    }

    print(f"    Local  estimator: {stats['local_estimator']['mean']:+.4f} "
          f"+/- {stats['local_estimator']['sem']:.4f} "
          f"(std={stats['local_estimator']['std']:.4f})")
    print(f"    Bounce estimator: {stats['bounce_estimator']['mean']:+.4f} "
          f"+/- {stats['bounce_estimator']['sem']:.4f} "
          f"(std={stats['bounce_estimator']['std']:.4f})")

    return stats


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("F1.3 — BISPECTRUM INJECTION / RECOVERY TEST")
    print("Tier 3A: Template-recast methodology validation")
    print("=" * 70)
    print(f"\nGrid: {N_GRID}x{N_GRID}, Realizations: {N_REALIZATIONS}")
    print(f"A_s: {A_S} (boosted for high S/N — ratio test is amplitude-independent)")
    print(f"Canonical f_NL = {F_NL_INJECT}")
    print(f"Bounce coefficients: {C_BOUNCE}")

    t_start = time.time()

    # ─── Sanity checks ───
    print("\n  Shape function sanity checks:")
    for name, ks in [("Squeezed", (0.001, 1, 1)),
                     ("Equilateral", (1, 1, 1)),
                     ("Folded", (1, 0.5, 0.5))]:
        bnl = bounce_BNL(*ks)
        ratio = bnl / (-35.0/8.0)
        print(f"    BNL({name:12s}) = {bnl:+.4f}  (ratio = {ratio:.4f})")
    print(f"    Expected: sq=-4.375, eq~-3.98, fold=-2.25")

    # ─── Setup ───
    KX, KY, K, Pk = make_kgrid(N_GRID, L_BOX)

    k_nonzero = K[K > 0].ravel()
    k_min = k_nonzero.min() * 0.99
    k_max = k_nonzero.max() * 0.4
    k_edges = np.logspace(np.log10(k_min), np.log10(k_max), N_KBINS + 1)
    k_centers = np.sqrt(k_edges[:-1] * k_edges[1:])
    Pk_centers = A_S / k_centers**2

    print(f"\n  k-bins: {N_KBINS} bins from {k_edges[0]:.1f} to {k_edges[-1]:.1f}")

    # ─── BNL ratio table ───
    print("  Precomputing BNL ratio table...")
    ratio_table, valid_table = build_bnl_ratio_table(k_centers)
    print(f"    {int(valid_table.sum())} valid bin triplets")

    # ─── Run three tests ───
    args = (KX, KY, K, Pk, k_edges, k_centers, ratio_table, Pk_centers)

    stats_A = run_ensemble('local', F_NL_INJECT, N_REALIZATIONS, 'A', *args)
    stats_B = run_ensemble('bounce', F_NL_INJECT, N_REALIZATIONS, 'B', *args)
    stats_C = run_ensemble('null', 0.0, N_REALIZATIONS, 'C', *args)

    t_total = time.time() - t_start
    print(f"\n  Total time: {t_total:.1f}s")

    # ═══════════════════════════════════════════════════════════════
    # ANALYSIS
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("ANALYSIS")
    print("=" * 70)

    test_results = {}

    # ─── Test A: self-consistency ───
    mean_A = stats_A['local_estimator']['mean'] if stats_A else 0.0
    sem_A = stats_A['local_estimator']['sem'] if stats_A else 1.0

    if stats_A:
        # The absolute value will have an FFT normalization offset.
        # What matters: (1) it should be negative (correct sign), and
        # (2) null test should be ~0 relative to this.
        print(f"\n  Test A (local injection -> local estimator):")
        print(f"    Injected:  f_NL = {F_NL_INJECT:+.4f}")
        print(f"    Recovered (raw): {mean_A:+.4f} +/- {sem_A:.4f}")
        print(f"    Sign: {'CORRECT (negative)' if mean_A < 0 else 'WRONG'}")

        # Calibration factor (expected due to FFT normalization)
        cal_A = mean_A / F_NL_INJECT if abs(F_NL_INJECT) > 0 else 0
        print(f"    Calibration factor: {cal_A:.2f} (FFT convention)")
        print(f"    NOTE: Absolute calibration does not affect the ratio test.")

        test_A_sign = mean_A < 0
        test_A_nonzero = abs(mean_A / sem_A) > 5.0  # must be significantly non-zero
        test_A_pass = test_A_sign and test_A_nonzero
        print(f"    Sign correct: {test_A_sign}")
        print(f"    Significance: {abs(mean_A/sem_A):.1f}sigma (need >5)")
        print(f"    PASS: {'YES' if test_A_pass else 'NO'}")
        test_results['A_local_detection'] = bool(test_A_pass)
    else:
        test_results['A_local_detection'] = False
        cal_A = 1.0

    # ─── Test B: ratio recovery (the KEY test) ───
    mean_B_local = stats_B['local_estimator']['mean'] if stats_B else 0.0
    sem_B_local = stats_B['local_estimator']['sem'] if stats_B else 1.0
    mean_B_bounce = stats_B['bounce_estimator']['mean'] if stats_B else 0.0
    sem_B_bounce = stats_B['bounce_estimator']['sem'] if stats_B else 1.0

    if stats_A and stats_B:
        # KEY: r = (local estimator on bounce) / (local estimator on local)
        if abs(mean_A) > 1e-10:
            r_measured = mean_B_local / mean_A
        else:
            r_measured = float('nan')

        # Error on ratio via error propagation
        if not np.isnan(r_measured) and abs(mean_A) > 1e-10 and abs(mean_B_local) > 1e-10:
            r_err = abs(r_measured) * np.sqrt(
                (sem_B_local / abs(mean_B_local))**2 +
                (sem_A / abs(mean_A))**2
            )
        else:
            r_err = float('nan')

        # Predicted values
        r_pred = 0.876
        r_pred_err = 0.02

        # Tension
        if not np.isnan(r_measured) and not np.isnan(r_err):
            r_tension = abs(r_measured - r_pred) / np.sqrt(r_err**2 + r_pred_err**2)
        else:
            r_tension = float('inf')

        r_in_range = 0.80 <= r_measured <= 0.95 if not np.isnan(r_measured) else False

        print(f"\n  Test B (bounce injection -> local estimator) — KEY RATIO TEST:")
        print(f"    Local  estimator on bounce: {mean_B_local:+.4f} +/- {sem_B_local:.4f}")
        print(f"    Bounce estimator on bounce: {mean_B_bounce:+.4f} +/- {sem_B_bounce:.4f}")
        print(f"    Local  estimator on local (Test A): {mean_A:+.4f} +/- {sem_A:.4f}")
        print(f"")
        print(f"    *** AMPLITUDE RATIO ***")
        print(f"    r_measured = B_local / A_local = {r_measured:.4f} +/- {r_err:.4f}")
        print(f"    r_predicted (CMB Fisher)       = {r_pred} +/- {r_pred_err}")
        print(f"    r_predicted (generic)          = 0.84 +/- 0.02")
        print(f"    Tension with r={r_pred}:         {r_tension:.2f}sigma")
        print(f"    In range [0.80, 0.95]:           {'YES' if r_in_range else 'NO'}")

        test_B_ratio = bool(r_tension < 3.0 or r_in_range)
        test_results['B_ratio_recovery'] = test_B_ratio
        print(f"    PASS: {'YES' if test_B_ratio else 'NO'}")

        # Bounce estimator on bounce should give larger signal than local estimator
        # (because it's a better matched template)
        bounce_over_local = abs(mean_B_bounce) / abs(mean_B_local) if abs(mean_B_local) > 1e-10 else 0
        print(f"\n    Bounce estimator / local estimator on bounce signal:")
        print(f"      |bounce_est| / |local_est| = {bounce_over_local:.4f}")
        print(f"      (Should be > 1 if bounce template is better matched)")
        test_B_bounce_better = bool(bounce_over_local > 0.99)
        test_results['B_bounce_better_matched'] = test_B_bounce_better
        print(f"      PASS: {'YES' if test_B_bounce_better else 'NO'}")

    else:
        test_results['B_ratio_recovery'] = False
        test_results['B_bounce_better_matched'] = False
        r_measured, r_err, r_tension = float('nan'), float('nan'), float('nan')
        r_in_range = False

    # ─── Test C: null ───
    if stats_C:
        mean_C = stats_C['local_estimator']['mean']
        sem_C = stats_C['local_estimator']['sem']
        null_tension = abs(mean_C) / sem_C if sem_C > 1e-20 else float('inf')

        # Also check that null is much smaller than signal
        if abs(mean_A) > 1e-10:
            null_frac = abs(mean_C) / abs(mean_A)
        else:
            null_frac = float('inf')

        print(f"\n  Test C (null injection):")
        print(f"    Recovered (local): {mean_C:+.4f} +/- {sem_C:.4f}")
        print(f"    Tension with zero: {null_tension:.1f}sigma")
        print(f"    Null / Signal fraction: {null_frac:.4f} ({null_frac*100:.2f}%)")
        test_C_pass = bool(null_tension < 3.0)
        test_C_small = bool(null_frac < 0.05)  # null should be <5% of signal
        test_results['C_null_consistent'] = test_C_pass
        test_results['C_null_small'] = test_C_small
        print(f"    Consistent with zero: {'YES' if test_C_pass else 'NO'}")
        print(f"    Small vs signal (<5%): {'YES' if test_C_small else 'NO'}")
    else:
        test_results['C_null_consistent'] = False
        test_results['C_null_small'] = False
        null_tension = float('nan')

    # ═══════════════════════════════════════════════════════════════
    # VERDICT
    # ═══════════════════════════════════════════════════════════════
    # Core criterion: the ratio r must match the prediction
    core_pass = test_results.get('B_ratio_recovery', False)
    support_pass = (test_results.get('A_local_detection', False) and
                    test_results.get('C_null_consistent', False))
    all_pass = all(test_results.values())

    level = "INJECTION_VALIDATED" if (core_pass and support_pass) else "INJECTION_FAILED"

    print(f"\n  {'='*60}")
    print(f"  VERDICT: {level}")
    print(f"  {'='*60}")
    for name, passed in test_results.items():
        print(f"    {name}: {'PASS' if passed else 'FAIL'}")

    if level == "INJECTION_VALIDATED" and stats_A and stats_B:
        print(f"\n  VALIDATED: The template-recast methodology is confirmed.")
        print(f"    A local estimator applied to a bounce-shape signal recovers")
        print(f"    r = {r_measured:.3f} +/- {r_err:.3f} of the amplitude,")
        print(f"    consistent with the predicted r = {r_pred} +/- {r_pred_err}.")
        print(f"")
        print(f"    This validates the F1.1 recast:")
        print(f"      f_NL^bounce(Planck) = f_NL^local / r = -0.9/0.876 = -1.0 +/- 5.8")
        print(f"")
        print(f"    The recast is now INJECTION_VALIDATED (upgraded from TRIAGE_RECAST).")

    # ═══════════════════════════════════════════════════════════════
    # SAVE OUTPUT
    # ═══════════════════════════════════════════════════════════════
    def sanitize(v):
        """Make JSON-safe."""
        if isinstance(v, (np.bool_, bool)):
            return bool(v)
        if isinstance(v, (np.integer,)):
            return int(v)
        if isinstance(v, (np.floating, float)):
            if np.isnan(v) or np.isinf(v):
                return None
            return float(v)
        return v

    def sanitize_dict(d):
        if d is None:
            return None
        return {k: sanitize(v) if not isinstance(v, dict) else sanitize_dict(v)
                for k, v in d.items()}

    output = {
        "pipeline": "F1",
        "stage": "F1.3",
        "level": level,
        "description": "Bispectrum injection/recovery test validating template-recast methodology",
        "configuration": {
            "grid_size": N_GRID,
            "n_kbins": N_KBINS,
            "n_realizations": N_REALIZATIONS,
            "f_NL_injected": float(F_NL_INJECT),
            "A_s": A_S,
            "A_s_note": "Boosted for high S/N. Ratio test is amplitude-independent.",
            "bounce_coefficients": list(C_BOUNCE),
            "seed": BASE_SEED,
        },
        "test_A_local_injection": {
            "injection": "local",
            "f_NL_injected": float(F_NL_INJECT),
            "estimator_raw_mean": sanitize(mean_A),
            "estimator_raw_sem": sanitize(sem_A),
            "calibration_factor": sanitize(float(cal_A)),
            "pass": bool(test_results.get('A_local_detection', False)),
        },
        "test_B_bounce_injection": {
            "injection": "bounce",
            "f_NL_injected": float(F_NL_INJECT),
            "local_estimator_mean": sanitize(mean_B_local),
            "local_estimator_sem": sanitize(sem_B_local),
            "bounce_estimator_mean": sanitize(mean_B_bounce),
            "bounce_estimator_sem": sanitize(sem_B_bounce),
            "ratio_measured": sanitize(float(r_measured)),
            "ratio_measured_err": sanitize(float(r_err)),
            "ratio_predicted": 0.876,
            "ratio_predicted_err": 0.02,
            "ratio_tension_sigma": sanitize(float(r_tension)),
            "ratio_in_range_0p80_0p95": bool(r_in_range),
            "pass_ratio": bool(test_results.get('B_ratio_recovery', False)),
            "pass_bounce_better": bool(test_results.get('B_bounce_better_matched', False)),
        },
        "test_C_null": {
            "injection": "null",
            "estimator_raw_mean": sanitize(stats_C['local_estimator']['mean']) if stats_C else None,
            "estimator_raw_sem": sanitize(stats_C['local_estimator']['sem']) if stats_C else None,
            "tension_with_zero": sanitize(float(null_tension)),
            "pass": bool(test_results.get('C_null_consistent', False)),
        },
        "all_tests": {k: bool(v) for k, v in test_results.items()},
        "core_tests_pass": bool(core_pass and support_pass),
        "all_tests_pass": bool(all_pass),
        "ensemble_stats": {
            "test_A": sanitize_dict(stats_A),
            "test_B": sanitize_dict(stats_B),
            "test_C": sanitize_dict(stats_C),
        },
        "timing_seconds": round(time.time() - t_start, 1),
        "caveats": [
            "2D grid (not 3D CMB spherical harmonics) -- validates methodology, not full pipeline",
            "Boosted A_s for high S/N -- does NOT affect the ratio r (geometric property)",
            "Bounce injection uses binned BNL approximation (10 k-bins, angle-averaged)",
            "Absolute f_NL calibration has FFT-convention offset; only the RATIO is tested",
            "No beam, noise, or mask effects",
            "This validates the RATIO recovery, not absolute calibration",
        ],
    }

    outfile = OUTDIR / "F1_injection_recovery.json"
    with open(outfile, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  Output saved: {outfile}")

    return output


if __name__ == "__main__":
    main()
