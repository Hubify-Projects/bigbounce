#!/usr/bin/env python3
"""
Chain 1A: Narrow symmetric P(k) bump → PBH mass spectrum → exclusion test.

Model:
  P_R(k) = A_cmb(k/k_*)^{n_s-1} + A_b exp[-ln^2(k/k_b)/(2 s_k^2)]

Parameters (sampled):
  theta = {log10(A_b), log10(M_b/g), s_k}

Fixed collapse parameters (Chain 1A benchmark):
  delta_c = 0.45, K_c = 3, gamma_c = 0.36

Output:
  1. Viability map in (M_b, A_b) space
  2. f_PBH(M) curves for representative samples
  3. Figure: viable region vs SMBH-seed-relevant masses

This is a DIAGNOSTIC chain.  Grid scan first, MCMC only if needed.
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add scripts dir to path
sys.path.insert(0, os.path.dirname(__file__))

from build_spectrum import pr_spectrum
from variance_rd import k_to_M_H, M_H_to_k, sigma_H, M_SUN_G
from critical_collapse import (fpbh_total, fpbh_density, dbeta_dlnM,
                                DELTA_C, K_C, GAMMA_C)
from bounds_loader import load_all_bounds, envelope_bound
from likelihood_pbh import log_likelihood_pbh, is_viable

# ========================================================================
# Grid scan parameters
# ========================================================================
N_Ab = 80
N_Mb = 100
N_sk = 3  # s_k values to scan

LOG10_Ab_MIN, LOG10_Ab_MAX = -4.0, -0.5
LOG10_Mb_MIN, LOG10_Mb_MAX = 15.0, 40.0
SK_VALUES = [0.1, 0.3, 0.5]

# SMBH seed relevant masses
SMBH_MASS_MIN_G = 1e2 * M_SUN_G   # 10^2 M_sun in grams
SMBH_MASS_MAX_G = 1e5 * M_SUN_G   # 10^5 M_sun in grams

# Framework-predicted scale
K_BOUNCE = 5.86e14  # Mpc^{-1}
M_BOUNCE = k_to_M_H(K_BOUNCE)

print("=" * 70)
print("CHAIN 1A: Narrow P(k) Bump → PBH Exclusion Test")
print("=" * 70)
print(f"\nGrid: {N_Ab} x {N_Mb} x {N_sk} = {N_Ab * N_Mb * N_sk} points")
print(f"log10(A_b) range: [{LOG10_Ab_MIN}, {LOG10_Ab_MAX}]")
print(f"log10(M_b/g) range: [{LOG10_Mb_MIN}, {LOG10_Mb_MAX}]")
print(f"s_k values: {SK_VALUES}")
print(f"\nSMBH seed masses: {SMBH_MASS_MIN_G/M_SUN_G:.0e} to "
      f"{SMBH_MASS_MAX_G/M_SUN_G:.0e} M_sun "
      f"({np.log10(SMBH_MASS_MIN_G):.1f} to {np.log10(SMBH_MASS_MAX_G):.1f} "
      f"log10 g)")
print(f"Framework bounce scale: M = {M_BOUNCE:.2e} g "
      f"(log10 = {np.log10(M_BOUNCE):.1f})")

# ========================================================================
# Run grid scan
# ========================================================================
log10_Ab_grid = np.linspace(LOG10_Ab_MIN, LOG10_Ab_MAX, N_Ab)
log10_Mb_grid = np.linspace(LOG10_Mb_MIN, LOG10_Mb_MAX, N_Mb)

results = {}

for i_sk, s_k in enumerate(SK_VALUES):
    print(f"\n--- s_k = {s_k} ---")

    viability = np.zeros((N_Ab, N_Mb))
    fpbh_map = np.full((N_Ab, N_Mb), np.nan)
    max_violation = np.full((N_Ab, N_Mb), np.nan)

    for i_ab, log_Ab in enumerate(log10_Ab_grid):
        A_b = 10 ** log_Ab
        for i_mb, log_Mb in enumerate(log10_Mb_grid):
            M_b = 10 ** log_Mb
            k_b = M_H_to_k(M_b)

            # Build spectrum
            def pr_func(k):
                return pr_spectrum(k, A_b, k_b, s_k)

            # Compute sigma at horizon scale
            try:
                sig_H = sigma_H(k_b, pr_func)
            except Exception:
                continue

            if sig_H <= 0 or not np.isfinite(sig_H):
                continue

            # Compute f_PBH and mass function
            f_pbh, psi_func, M_arr, db_arr = fpbh_total(M_b, sig_H)

            if not np.isfinite(f_pbh) or f_pbh <= 0:
                fpbh_map[i_ab, i_mb] = 0.0
                viability[i_ab, i_mb] = 1  # trivially viable (no PBHs)
                continue

            fpbh_map[i_ab, i_mb] = f_pbh

            # Normalize mass function for constraint test
            psi_arr = db_arr / np.trapezoid(db_arr, np.log(M_arr)) if np.trapezoid(db_arr, np.log(M_arr)) > 0 else np.zeros_like(db_arr)

            # Evaluate constraints
            neg2lnL, violations = log_likelihood_pbh(f_pbh, M_arr, psi_arr)
            max_viol = max(violations.values()) if violations else 0.0
            max_violation[i_ab, i_mb] = max_viol

            if neg2lnL == 0:
                viability[i_ab, i_mb] = 1  # viable
            else:
                viability[i_ab, i_mb] = 0  # excluded

        if (i_ab + 1) % 20 == 0:
            n_viable = np.sum(viability[:i_ab + 1, :] == 1)
            n_tested = np.sum(np.isfinite(fpbh_map[:i_ab + 1, :]))
            print(f"  [{i_ab + 1}/{N_Ab}] viable: {n_viable}, "
                  f"tested: {n_tested}")

    results[s_k] = {
        'viability': viability,
        'fpbh_map': fpbh_map,
        'max_violation': max_violation,
    }

    n_viable = np.sum(viability == 1)
    n_excluded = np.sum(viability == 0)
    n_fpbh_nonzero = np.sum(fpbh_map > 0)
    print(f"  Total: {n_viable} viable, {n_excluded} excluded, "
          f"{n_fpbh_nonzero} with f_PBH > 0")

# ========================================================================
# Analysis: where are the viable regions?
# ========================================================================
print("\n" + "=" * 70)
print("VIABLE REGION ANALYSIS")
print("=" * 70)

for s_k in SK_VALUES:
    v = results[s_k]['viability']
    fm = results[s_k]['fpbh_map']

    viable_mask = v == 1
    # Among viable points with nonzero PBH production:
    interesting_mask = viable_mask & (fm > 1e-30) & np.isfinite(fm)

    if np.any(interesting_mask):
        viable_Mb = log10_Mb_grid[np.any(interesting_mask, axis=0)]
        viable_Ab = log10_Ab_grid[np.any(interesting_mask, axis=1)]
        print(f"\ns_k = {s_k}:")
        print(f"  Viable region with f_PBH > 0:")
        print(f"    log10(M_b/g): {viable_Mb.min():.1f} to {viable_Mb.max():.1f}")
        print(f"    log10(A_b): {viable_Ab.min():.1f} to {viable_Ab.max():.1f}")

        # Check overlap with SMBH seed masses
        smbh_overlap = (viable_Mb >= np.log10(SMBH_MASS_MIN_G)) & \
                       (viable_Mb <= np.log10(SMBH_MASS_MAX_G))
        if np.any(smbh_overlap):
            print(f"    ** OVERLAPS SMBH seed masses **")
        else:
            print(f"    Does NOT overlap SMBH seed masses "
                  f"({np.log10(SMBH_MASS_MIN_G):.1f} to "
                  f"{np.log10(SMBH_MASS_MAX_G):.1f})")

        # Check if framework scale is in viable region
        log_M_bounce = np.log10(M_BOUNCE)
        bounce_viable = (log_M_bounce >= viable_Mb.min()) & \
                        (log_M_bounce <= viable_Mb.max())
        print(f"    Framework bounce scale (log10 M = {log_M_bounce:.1f}): "
              f"{'IN viable region' if bounce_viable else 'NOT in viable region'}")

        # f_PBH range in viable region
        f_viable = fm[interesting_mask]
        print(f"    f_PBH range: {f_viable.min():.2e} to {f_viable.max():.2e}")
    else:
        print(f"\ns_k = {s_k}: No viable points with nonzero f_PBH "
              f"(all either excluded or trivially empty)")

# ========================================================================
# Figure 1: Viability map (M_b, A_b) for each s_k
# ========================================================================
fig, axes = plt.subplots(1, len(SK_VALUES), figsize=(6 * len(SK_VALUES), 5),
                         sharey=True)
if len(SK_VALUES) == 1:
    axes = [axes]

for ax, s_k in zip(axes, SK_VALUES):
    v = results[s_k]['viability']
    fm = results[s_k]['fpbh_map']

    # Plot: log10(f_PBH) where viable, gray where excluded
    plot_data = np.where(v == 1, np.log10(np.clip(fm, 1e-30, None)), np.nan)

    im = ax.pcolormesh(log10_Mb_grid, log10_Ab_grid, plot_data,
                       cmap='viridis', shading='auto', vmin=-20, vmax=0)

    # Overlay excluded region
    excluded = np.where(v == 0, 1.0, np.nan)
    ax.pcolormesh(log10_Mb_grid, log10_Ab_grid, excluded,
                  cmap='Reds', alpha=0.3, shading='auto', vmin=0, vmax=1)

    # SMBH seed mass range
    ax.axvspan(np.log10(SMBH_MASS_MIN_G), np.log10(SMBH_MASS_MAX_G),
               color='green', alpha=0.15, label='SMBH seeds')

    # Framework scale
    ax.axvline(np.log10(M_BOUNCE), color='purple', ls='--', lw=2,
               label=f'Bounce (N_tot=92)')

    # Asteroid window
    ax.axvspan(20, 24, color='orange', alpha=0.08, label='Asteroid window')

    ax.set_xlabel(r'log$_{10}$(M$_b$ / g)', fontsize=12)
    ax.set_title(f's_k = {s_k}', fontsize=13)
    if ax == axes[0]:
        ax.set_ylabel(r'log$_{10}$(A$_b$)', fontsize=12)
    ax.legend(loc='upper left', fontsize=8)

plt.colorbar(im, ax=axes[-1], label=r'log$_{10}$(f$_{\rm PBH}$)')
plt.suptitle('Chain 1A: PBH Viability Map\n'
             '(colored = viable, red = excluded by PBH bounds)',
             fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('../outputs/plots/chain1a_viability_map.pdf',
            dpi=150, bbox_inches='tight')
plt.savefig('../outputs/plots/chain1a_viability_map.png',
            dpi=150, bbox_inches='tight')
print("\nFigure saved: chain1a_viability_map.pdf/png")

# ========================================================================
# Figure 2: Representative f_PBH(M) curves
# ========================================================================
fig2, ax2 = plt.subplots(figsize=(10, 7))

# Plot constraint envelope
log_M_plot = np.linspace(14, 40, 500)
log_f_env = envelope_bound(log_M_plot)
ax2.fill_between(log_M_plot, log_f_env, 0, alpha=0.15, color='red',
                 label='PBH excluded')
ax2.plot(log_M_plot, log_f_env, 'r-', lw=1.5)

# Pick a few representative viable points from the middle s_k
s_k_rep = SK_VALUES[len(SK_VALUES) // 2]
v = results[s_k_rep]['viability']
fm = results[s_k_rep]['fpbh_map']
interesting = (v == 1) & (fm > 1e-20) & np.isfinite(fm)

if np.any(interesting):
    # Sample a few points across the viable mass range
    viable_indices = np.argwhere(interesting)
    n_show = min(5, len(viable_indices))
    step = max(1, len(viable_indices) // n_show)
    colors = plt.cm.cool(np.linspace(0, 1, n_show))

    for idx, c in zip(viable_indices[::step][:n_show], colors):
        i_ab, i_mb = idx
        A_b = 10 ** log10_Ab_grid[i_ab]
        M_b = 10 ** log10_Mb_grid[i_mb]
        k_b = M_H_to_k(M_b)

        def pr_func(k, _Ab=A_b, _kb=k_b, _sk=s_k_rep):
            return pr_spectrum(k, _Ab, _kb, _sk)

        sig_H = sigma_H(k_b, pr_func)
        f_pbh, psi_func, M_arr, db_arr = fpbh_total(M_b, sig_H)

        # Plot mass function
        df_dlnM = fpbh_density(M_arr, M_b, sig_H)
        valid = df_dlnM > 1e-30
        if np.any(valid):
            ax2.plot(np.log10(M_arr[valid]), np.log10(df_dlnM[valid]),
                     color=c, lw=1.5,
                     label=f'M_b={log10_Mb_grid[i_mb]:.0f}, '
                           f'A_b=10^{log10_Ab_grid[i_ab]:.1f}, '
                           f'f={f_pbh:.1e}')

# Annotations
ax2.axvspan(np.log10(SMBH_MASS_MIN_G), np.log10(SMBH_MASS_MAX_G),
            color='green', alpha=0.1, label='SMBH seeds')
ax2.axvline(np.log10(M_BOUNCE), color='purple', ls='--', lw=2,
            label=f'Bounce scale')
ax2.axvspan(20, 24, color='orange', alpha=0.05, label='Asteroid window')

ax2.set_xlabel(r'log$_{10}$(M / g)', fontsize=13)
ax2.set_ylabel(r'log$_{10}$(df$_{\rm PBH}$/d ln M)', fontsize=13)
ax2.set_title(f'Representative PBH Mass Functions (s_k = {s_k_rep})',
              fontsize=14)
ax2.set_xlim(14, 40)
ax2.set_ylim(-25, 1)
ax2.legend(loc='lower right', fontsize=8, ncol=1)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../outputs/plots/chain1a_mass_functions.pdf',
            dpi=150, bbox_inches='tight')
plt.savefig('../outputs/plots/chain1a_mass_functions.png',
            dpi=150, bbox_inches='tight')
print("Figure saved: chain1a_mass_functions.pdf/png")

# ========================================================================
# Save summary
# ========================================================================
summary_path = '../outputs/tables/chain1a_summary.txt'
with open(summary_path, 'w') as f:
    f.write("CHAIN 1A SUMMARY\n")
    f.write(f"Date: 2026-03-13\n")
    f.write(f"Grid: {N_Ab} x {N_Mb} x {N_sk}\n")
    f.write(f"Collapse: delta_c={DELTA_C}, K_c={K_C}, gamma_c={GAMMA_C}\n")
    f.write("=" * 50 + "\n\n")

    for s_k in SK_VALUES:
        v = results[s_k]['viability']
        fm = results[s_k]['fpbh_map']
        viable_with_pbh = (v == 1) & (fm > 1e-30) & np.isfinite(fm)

        f.write(f"s_k = {s_k}:\n")
        f.write(f"  Viable points (all): {np.sum(v == 1)}\n")
        f.write(f"  Excluded points: {np.sum(v == 0)}\n")
        f.write(f"  Viable with f_PBH > 0: {np.sum(viable_with_pbh)}\n")

        if np.any(viable_with_pbh):
            viable_Mb = log10_Mb_grid[np.any(viable_with_pbh, axis=0)]
            f.write(f"  Mass range: {viable_Mb.min():.1f} to "
                    f"{viable_Mb.max():.1f} (log10 g)\n")
            f.write(f"  f_PBH range: {fm[viable_with_pbh].min():.2e} to "
                    f"{fm[viable_with_pbh].max():.2e}\n")

            smbh_overlap = (viable_Mb >= np.log10(SMBH_MASS_MIN_G)) & \
                           (viable_Mb <= np.log10(SMBH_MASS_MAX_G))
            f.write(f"  SMBH overlap: {'YES' if np.any(smbh_overlap) else 'NO'}\n")

            log_M_bounce = np.log10(M_BOUNCE)
            bounce_in = (log_M_bounce >= viable_Mb.min()) & \
                        (log_M_bounce <= viable_Mb.max())
            f.write(f"  Bounce scale in viable region: "
                    f"{'YES' if bounce_in else 'NO'}\n")
        f.write("\n")

    f.write("FRAMEWORK-PREDICTED BOUNCE SCALE:\n")
    f.write(f"  k_bounce = 5.86e14 Mpc^-1\n")
    f.write(f"  M_bounce = {M_BOUNCE:.2e} g = {M_BOUNCE/M_SUN_G:.2e} M_sun\n")
    f.write(f"  log10(M_bounce/g) = {np.log10(M_BOUNCE):.1f}\n")

print(f"Summary saved: {summary_path}")

print("\n" + "=" * 70)
print("CHAIN 1A COMPLETE")
print("=" * 70)
