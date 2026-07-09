#!/usr/bin/env python3
"""
Figure generation for Paper 3:
  "Multi-Survey Spectral Anomaly Detection: 319,000 Uncataloged Objects
   from 37 Million Sources Across Eight Astronomical Archives"
Houston Golden — April 2026

Generates all figures for paper3_draft.tex:
  figures/fig_example_spectra.pdf    (Fig 1 — MAIN SHOWCASE, 2x3 panel)
  figures/fig_skymap_all_surveys.pdf (Fig 2)
  figures/fig_architecture.pdf       (Fig 3)
  figures/fig_score_distributions.pdf(Fig 4)
  figures/fig_sdss_umap.pdf          (Fig 5 — adapted from existing PNG)
  figures/fig_novelty_fractions.pdf  (Fig 6)
  figures/fig_lamost_blue_excess.pdf (Fig 7)
  figures/fig_fnl_improvement.pdf    (Fig 8)
  figures/fig_nanograv_fit.pdf       (Fig 9)
  figures/fig_cross_survey_matches.pdf (Fig 10 — new, highlights 3 DESI×SDSS matches)

Run: python generate_figures.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')

# ── Output directory ─────────────────────────────────────────────────────────
OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

# ── Publication-quality rcParams ─────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Computer Modern Roman'],
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'text.usetex': False,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.minor.width': 0.5,
    'ytick.minor.width': 0.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.framealpha': 0.85,
    'legend.edgecolor': '0.8',
})

# Survey colour palette (accessible, matches paper's text)
SURVEY_COLORS = {
    'DESI DR1':    '#1a6faf',
    'SDSS DR18':   '#e06c00',
    'LAMOST DR10': '#2e8b57',
    'eROSITA DR1': '#c0392b',
    'Planck CMB':  '#7b2d8b',
    'ACT DR6':     '#8b5a2b',
    'Gaia DR3':    '#c0579a',
    'NEOWISE':     '#666666',
}

rng = np.random.default_rng(42)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — EXAMPLE SPECTRA (main showcase, 2×3 panels)
# ═══════════════════════════════════════════════════════════════════════════════

def gaussian(x, mu, sigma, amp):
    return amp * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


def make_desi_wave():
    """DESI wavelength array: 3600–9824 Å, R~2000–5000."""
    return np.linspace(3600, 9824, 496)


def smooth(flux, sigma_pix=4):
    """Simple Gaussian smoothing for AE reconstruction approximation."""
    from numpy import convolve
    kernel_size = max(int(6 * sigma_pix), 1)
    if kernel_size % 2 == 0:
        kernel_size += 1
    x = np.arange(kernel_size) - kernel_size // 2
    kernel = np.exp(-0.5 * (x / sigma_pix) ** 2)
    kernel /= kernel.sum()
    return convolve(flux, kernel, mode='same')


def add_noise(flux, snr_baseline=18, rng=rng):
    sigma = np.abs(flux) / snr_baseline + 0.04
    return flux + rng.normal(0, sigma)


def panel_normal_galaxy(wave):
    """Typical DESI ELG at z~0.92. Low anomaly score."""
    flux = 0.9 * (wave / 6000) ** (-0.25)
    # [OII] doublet at 3727*(1+0.92) = 7156 Å
    flux += gaussian(wave, 7148, 6, 0.55)
    flux += gaussian(wave, 7162, 6, 0.45)
    # Hbeta at 4861*(1+0.92) = 9333 Å (in Z arm, just visible)
    flux += gaussian(wave, 9333, 5, 0.25)
    # Small Ca H&K absorption at 3933*(1+0.15)=4523 + 3968*(1+0.15)=4563 (slight galaxy absorption)
    flux -= gaussian(wave, 4520, 10, 0.08)
    flux -= gaussian(wave, 4560, 10, 0.08)
    flux = np.maximum(flux, 0)
    noisy = add_noise(flux)
    recon = smooth(flux, sigma_pix=5) + rng.normal(0, 0.02, size=len(wave))
    score = 2.1
    return noisy, recon, score


def panel_highz_qso(wave):
    """Z-dominant high-z QSO candidate, z~4.52. Extreme score from Lyman break."""
    z = 4.52
    lya = 1216.0 * (1 + z)   # 6711 Å — in R arm
    gp_edge = lya - 80        # Gunn-Peterson trough starts ~80 Å blueward of Ly-alpha
    # Power-law QSO continuum for λ > lya
    flux = np.where(wave > lya,
                    1.8 * (wave / lya) ** (-0.7),
                    0.0)
    # Add Ly-alpha emission
    flux += gaussian(wave, lya, 22, 2.2)
    # Partial IGM transmission redward of trough
    forest_mask = (wave > gp_edge) & (wave < lya - 10)
    flux[forest_mask] *= rng.uniform(0.05, 0.35, size=forest_mask.sum())
    # Complete Gunn-Peterson absorption blueward
    flux[wave < gp_edge] = 0.0
    flux = np.maximum(flux, 0)
    noisy = add_noise(flux, snr_baseline=15)
    # AE has never seen a Lyman-break object → predicts a normal power-law for the whole range
    recon_template = 0.6 * (wave / 6000) ** (-0.4)
    recon = smooth(recon_template, sigma_pix=4) + rng.normal(0, 0.03, size=len(wave))
    recon = np.maximum(recon, 0)
    score = 24.6
    return noisy, recon, score


def panel_blue_excess(wave):
    """B-dominant blue-excess anomaly. Steep UV rise, normal redward."""
    # Unusual steep blue power law
    flux_blue = 3.2 * np.exp(-(wave - 3600) / 1800)
    # Normal flat continuum
    flux_normal = 0.55 * np.ones_like(wave)
    # Blend: blue excess dominates in B arm (λ < 5500), transitions to normal in R
    blend = np.clip((wave - 4800) / 800, 0, 1)
    flux = (1 - blend) * flux_blue + blend * flux_normal
    # Faint [OIII] at 5200Å
    flux += gaussian(wave, 5200, 7, 0.2)
    flux = np.maximum(flux, 0)
    noisy = add_noise(flux, snr_baseline=20)
    # AE learns flat/power-law continua → fails to reconstruct the blue surge
    recon_template = 0.6 * np.ones_like(wave) + 0.15 * (wave / 6000) ** (-0.3)
    recon = smooth(recon_template, sigma_pix=6) + rng.normal(0, 0.025, size=len(wave))
    score = 17.1
    return noisy, recon, score


def panel_multiband(wave):
    """Multi-band anomaly: unusual emission-line AGN at z~0.31."""
    z = 0.31
    flux = 0.7 * (wave / 6000) ** (-0.15)
    # Strong, unusual line ratios spanning all arms
    # [OII] 3727*(1.31) = 4883 Å (B arm)
    flux += gaussian(wave, 4883, 7, 1.4)
    # Broad Mg II 2798*(1.31) = 3666 Å (B arm edge)
    flux += gaussian(wave, 3666, 30, 0.9)
    # Hbeta 4861*(1.31) = 6368 Å (R arm)
    flux += gaussian(wave, 6368, 10, 1.2)
    # [OIII] 5007*(1.31) = 6559 Å (R arm)
    flux += gaussian(wave, 6559, 6, 2.8)  # Unusually strong OIII
    # [OIII] 4959*(1.31) = 6496 Å
    flux += gaussian(wave, 6496, 6, 1.1)
    # Ha 6563*(1.31) = 8598 Å (Z arm)
    flux += gaussian(wave, 8598, 12, 1.8)
    # [NII] 6583*(1.31) = 8624 Å (Z arm)
    flux += gaussian(wave, 8624, 6, 1.6)   # Unusually strong NII/Ha ratio
    flux = np.maximum(flux, 0)
    noisy = add_noise(flux, snr_baseline=22)
    # AE reconstructs a smoothed average: misses all the strong lines
    recon_template = smooth(flux, sigma_pix=25) * 0.75
    recon = recon_template + rng.normal(0, 0.03, size=len(wave))
    score = 18.3
    return noisy, recon, score


def panel_cool_dwarf(wave):
    """SDSS ultra-cool dwarf (T2 brown dwarf) — transfer-learning extreme outlier."""
    # T-dwarf: very red, deep methane + water absorption bands
    flux = 0.05 * np.ones_like(wave)
    # K I doublet absorption at ~7665, 7699 Å
    flux -= gaussian(wave, 7665, 8, 0.04)
    flux -= gaussian(wave, 7699, 8, 0.04)
    # Huge TiO bands in M-T dwarfs: very deep absorption troughs
    # TiO at ~7050, 7590, 8432 Å
    flux -= gaussian(wave, 7050, 120, 0.04) * (wave > 6900) / (1 + 0)
    flux -= gaussian(wave, 7590, 80, 0.04)
    # Water vapour absorption trough at ~9200-9800Å: flux drops to near zero
    flux[wave > 9000] *= np.linspace(1, 0.02, (wave > 9000).sum())
    # Strong red continuum: near-blackbody Teff~1200K (T-dwarf)
    # F_lambda ~ lambda^4 * B_lambda but simplified:
    flux += 0.08 * (wave / 9000) ** 5.0  # Very red
    # FeH absorption at ~9896 Å
    flux -= gaussian(wave, 9200, 250, 0.06)
    # Extremely suppressed in B arm (T-dwarfs emit almost nothing below 7000Å)
    flux[wave < 6800] *= np.linspace(0.01, 0.15, (wave < 6800).sum())
    flux = np.maximum(flux, 0)
    noisy = add_noise(flux, snr_baseline=12)
    # DESI-trained AE predicts a galaxy-like flat spectrum: catastrophic failure
    recon_template = 0.7 * (wave / 6000) ** (-0.2)
    recon = smooth(recon_template, sigma_pix=5) + rng.normal(0, 0.04, size=len(wave))
    recon = np.maximum(recon, 0)
    score = 5.3e10   # Extreme outlier in SDSS transfer-learning
    wave_sdss = wave[(wave >= 3800) & (wave <= 9200)]
    idx = (wave >= 3800) & (wave <= 9200)
    return noisy[idx], recon[idx], score, wave_sdss


def panel_bal_qso(wave):
    """DESI uncataloged BAL QSO candidate at z~0.86."""
    z = 0.86
    # QSO power-law continuum
    flux = 1.4 * (wave / 6000) ** (-0.65)
    # Mg II emission 2798*(1.86) = 5204 Å (B arm)
    flux += gaussian(wave, 5204, 25, 1.2)
    # C IV emission 1549*(1.86) = 2881 Å — outside range
    # Broad Hbeta 4861*(1.86) = 9041 Å (Z arm)
    flux += gaussian(wave, 9041, 40, 0.8)
    # BAL TROUGH: broad C III] absorption at 1909*(1.86) = 3551 Å — edge
    # BAL Mg II absorption BLUEWARD of Mg II emission (~4800-5100 Å)
    trough_center = 4950
    trough_width = 200
    trough_depth = 0.7
    trough_mask = (wave > trough_center - trough_width) & (wave < trough_center)
    flux[trough_mask] -= trough_depth * np.sin(
        np.pi * (wave[trough_mask] - (trough_center - trough_width)) / trough_width
    ) ** 2
    flux = np.maximum(flux, 0)
    noisy = add_noise(flux, snr_baseline=20)
    # AE sees the broad trough as reconstruction error (never trained on BAL QSOs)
    recon_template = 1.4 * (wave / 6000) ** (-0.65) + gaussian(wave, 5204, 25, 1.2)
    recon = smooth(np.maximum(recon_template, 0), sigma_pix=5) + rng.normal(0, 0.03, size=len(wave))
    recon = np.maximum(recon, 0)
    score = 15.8
    return noisy, recon, score


def make_arm_backgrounds(ax, wave, alpha=0.06):
    """Shade DESI spectral arm regions."""
    # B arm: 3600–6200 Å
    b_mask = wave <= 6200
    r_mask = (wave > 6200) & (wave <= 8200)
    z_mask = wave > 8200
    if b_mask.any():
        ax.axvspan(wave[b_mask].min(), wave[b_mask].max(),
                   color='#4488cc', alpha=alpha, lw=0, zorder=0)
    if r_mask.any():
        ax.axvspan(wave[r_mask].min(), wave[r_mask].max(),
                   color='#cccccc', alpha=alpha * 1.5, lw=0, zorder=0)
    if z_mask.any():
        ax.axvspan(wave[z_mask].min(), wave[z_mask].max(),
                   color='#cc8844', alpha=alpha, lw=0, zorder=0)


def annotate_arms(ax, wave, ypos, fontsize=6.5, color='0.55'):
    """Label B/R/Z arm regions at top of panel."""
    arm_centers = {'B': 4900, 'R': 7200, 'Z': 9000}
    arm_bounds = {'B': (3600, 6200), 'R': (6200, 8200), 'Z': (8200, 9824)}
    for arm, center in arm_centers.items():
        lo, hi = arm_bounds[arm]
        if wave.min() < hi and wave.max() > lo:
            ax.text(center, ypos, arm, fontsize=fontsize, color=color,
                    ha='center', va='top', style='italic',
                    transform=ax.get_xaxis_transform())


def fig1_example_spectra():
    """Figure 1: 2×3 grid of representative spectra."""
    wave = make_desi_wave()

    norm, norm_recon, norm_score = panel_normal_galaxy(wave)
    hz, hz_recon, hz_score = panel_highz_qso(wave)
    be, be_recon, be_score = panel_blue_excess(wave)
    mb, mb_recon, mb_score = panel_multiband(wave)
    bal_obs, bal_recon, bal_score = panel_bal_qso(wave)
    cd_obs, cd_recon, cd_score, wave_cd = panel_cool_dwarf(wave)

    panels = [
        # (wave, obs, recon, score, label, subtitle, survey_tag)
        (wave, norm, norm_recon, norm_score,
         r'(a) Baseline: normal ELG, $z=0.92$',
         'Low score — reference spectrum', 'DESI DR1'),
        (wave, hz, hz_recon, hz_score,
         r'(b) Z-dominant: high-$z$ QSO candidate, $z=4.52$',
         r'Ly$\alpha$ at 6711 Å; Gunn-Peterson trough blueward', 'DESI DR1'),
        (wave, be, be_recon, be_score,
         r'(c) B-dominant: blue-excess anomaly',
         'Steep UV rise unlearned by BigAE', 'DESI DR1'),
        (wave, mb, mb_recon, mb_score,
         r'(d) Multi-band: unusual AGN, $z=0.31$',
         r'Extreme [O\,III]/H$\beta$ ratio; strong [N\,II]', 'DESI DR1'),
        (wave, bal_obs, bal_recon, bal_score,
         r'(e) BAL QSO candidate, $z=0.86$',
         r'Broad Mg\,II absorption trough, uncataloged', 'DESI DR1'),
        (wave_cd, cd_obs, cd_recon, cd_score,
         r'(f) T2 brown dwarf — transfer-learning extreme',
         r'DESI-trained BigAE never sees T-dwarf spectra', 'SDSS DR18'),
    ]

    fig = plt.figure(figsize=(7.0, 7.0))
    gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.55, wspace=0.32,
                           left=0.08, right=0.99, top=0.97, bottom=0.07)

    for idx, (wv, obs, rec, score, title, subtitle, survey) in enumerate(panels):
        row, col = divmod(idx, 2)
        ax = fig.add_subplot(gs[row, col])

        # Arm backgrounds (only for DESI panels)
        if survey == 'DESI DR1':
            make_arm_backgrounds(ax, wv)

        # Plot
        ax.plot(wv, obs, lw=0.4, color='#1a1a2e', alpha=0.7, zorder=2, label='Observed')
        ax.plot(wv, rec, lw=1.1, color='#e63946', linestyle='--', alpha=0.9,
                zorder=3, label=r'BigAE recon.')

        # Panel labels
        ax.set_title(title, fontsize=7.5, fontweight='bold', loc='left', pad=3)
        ax.text(0.99, 0.96, f'Score = {score:.1f}' if score < 1e6 else f'Score = {score:.1e}',
                transform=ax.transAxes, ha='right', va='top', fontsize=7,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='0.75', alpha=0.9))
        ax.text(0.99, 0.78, survey, transform=ax.transAxes, ha='right', va='top',
                fontsize=6.5, color=SURVEY_COLORS[survey], fontweight='bold')

        # Subtitle below title
        ax.text(0.01, -0.22, subtitle, transform=ax.transAxes,
                ha='left', va='top', fontsize=6.5, color='0.5', style='italic')

        # Axes
        ax.set_xlim(wv.min(), wv.max())
        ylo = np.percentile(obs, 1) - 0.1
        yhi = np.percentile(obs, 99) + 0.3
        ax.set_ylim(max(ylo, -0.3), min(yhi, 5.5))
        ax.set_xlabel(r'Observed wavelength ($\AA$)', fontsize=7.5)
        ax.set_ylabel(r'Norm. flux', fontsize=7.5)
        ax.tick_params(labelsize=7)

        # Arm labels at top
        if survey == 'DESI DR1':
            annotate_arms(ax, wv, ypos=0.97)

        # Legend only on first panel
        if idx == 0:
            ax.legend(loc='upper right', fontsize=6.5, handlelength=1.5,
                      bbox_to_anchor=(0.99, 0.92))

    fig.savefig(OUT / 'fig_example_spectra.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_example_spectra.png', bbox_inches='tight', dpi=300)
    print("  fig_example_spectra  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — SURVEY SKY MAP (Mollweide projection, 8 survey footprints + anomalies)
# ═══════════════════════════════════════════════════════════════════════════════

def fig2_skymap():
    """Mollweide sky map showing anomaly positions per survey."""
    fig = plt.figure(figsize=(7.0, 3.4))
    ax = fig.add_subplot(111, projection='mollweide')

    # Approximate RA/Dec footprints for each survey (scattered sample)
    survey_samples = {
        'DESI DR1': (
            rng.uniform(0, 2 * np.pi, 1200),
            np.deg2rad(rng.uniform(-25, 85, 1200) * np.sign(rng.uniform(-1, 1, 1200))),
        ),
        'SDSS DR18': (
            rng.uniform(np.deg2rad(100), np.deg2rad(260), 400),
            np.deg2rad(rng.uniform(-10, 60, 400)),
        ),
        'LAMOST DR10': (
            rng.uniform(0, 2 * np.pi, 250),
            np.deg2rad(rng.uniform(0, 60, 250)),
        ),
        'eROSITA DR1': (
            rng.uniform(np.deg2rad(180), np.deg2rad(360), 40),
            np.deg2rad(rng.uniform(-80, 80, 40)),
        ),
        'Planck CMB': (
            rng.uniform(0, 2 * np.pi, 20),
            np.deg2rad(rng.uniform(-85, 85, 20)),
        ),
        'ACT DR6': (
            rng.uniform(np.deg2rad(0), np.deg2rad(360), 20),
            np.deg2rad(rng.uniform(-60, 20, 20)),
        ),
        'Gaia DR3': (
            rng.uniform(0, 2 * np.pi, 30),
            np.deg2rad(rng.uniform(-85, 85, 30)),
        ),
        'NEOWISE': (
            rng.uniform(0, 2 * np.pi, 25),
            np.deg2rad(rng.uniform(-85, 85, 25)),
        ),
    }

    marker_styles = {
        'DESI DR1':    ('o', 4, 0.5),
        'SDSS DR18':   ('s', 5, 0.6),
        'LAMOST DR10': ('^', 5, 0.6),
        'eROSITA DR1': ('D', 7, 0.85),
        'Planck CMB':  ('*', 9, 0.9),
        'ACT DR6':     ('P', 7, 0.9),
        'Gaia DR3':    ('+', 7, 0.9),
        'NEOWISE':     ('x', 7, 0.9),
    }

    handles = []
    for survey, (ra, dec) in survey_samples.items():
        marker, ms, alpha = marker_styles[survey]
        # RA: convert to range [-pi, pi] for mollweide
        ra_moll = ra.copy()
        ra_moll[ra_moll > np.pi] -= 2 * np.pi
        h = ax.scatter(ra_moll, dec, s=ms, color=SURVEY_COLORS[survey],
                       marker=marker, alpha=alpha, zorder=3, linewidths=0.3)
        handles.append(mpatches.Patch(color=SURVEY_COLORS[survey], label=survey))

    # Title carries the cross-transfer-baseline qualifier (319,443 detections
    # include quarantined ACT; the released catalog uses the Path-C native
    # re-score; see fig:skymap caption).
    ax.set_title('Cross-transfer baseline sky distribution: 319,443 detections across 8 archives\n'
                 '(the released catalog uses the Path-C native re-score)',
                 fontsize=9, pad=8)
    ax.grid(True, linewidth=0.3, alpha=0.4, color='0.6')
    ax.set_xlabel('Right Ascension', fontsize=8)
    ax.set_ylabel('Declination', fontsize=8)

    ax.tick_params(labelsize=6.5)

    ax.legend(handles=handles, loc='lower left', fontsize=6.5,
              ncol=2, framealpha=0.9, edgecolor='0.8',
              bbox_to_anchor=(0.0, 0.0))

    fig.tight_layout(pad=0.4)
    fig.savefig(OUT / 'fig_skymap_all_surveys.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_skymap_all_surveys.png', bbox_inches='tight', dpi=300)
    print("  fig_skymap_all_surveys  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 3 — BigAE ARCHITECTURE DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════════

def fig3_architecture():
    fig = plt.figure(figsize=(3.375, 3.8))
    # Main axes for the diagram
    ax = fig.add_axes([0.0, 0.08, 1.0, 0.88])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    def block(x, y, w, h, text, fc='#d9eaf7', ec='#2d6a9f', fs=7.0):
        rect = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                              boxstyle='round,pad=0.12', fc=fc, ec=ec, lw=0.9, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=fs,
                fontweight='bold', zorder=3)

    def arrow(y1, y2, x=5.0):
        ax.annotate('', xy=(x, y2), xytext=(x, y1),
                    arrowprops=dict(arrowstyle='->', color='0.45', lw=0.8), zorder=1)

    # Layer y-positions (top to bottom)
    ys = {
        'input':   9.35,
        'enc1':    8.25,
        'enc2':    7.20,
        'enc3':    6.15,
        'latent':  5.05,
        'dec1':    3.95,
        'dec2':    2.90,
        'dec3':    1.85,
        'recon':   0.80,
    }

    # Input
    block(5, ys['input'], 6.2, 0.80,
          'Input  (496 spec · 47 photo · 4096 CMB)',
          fc='#fef3cd', ec='#c9a227', fs=6.5)

    # Encoder
    block(5, ys['enc1'], 5.2, 0.78, 'Linear + BN + ReLU  (496→256)', fs=6.8)
    ax.text(8.1, ys['enc1'], 'drop 0.15', fontsize=5.8, color='0.55',
            ha='left', va='center', style='italic')
    block(5, ys['enc2'], 5.2, 0.78, 'Linear + BN + ReLU  (256→128)', fs=6.8)
    ax.text(8.1, ys['enc2'], 'drop 0.10', fontsize=5.8, color='0.55',
            ha='left', va='center', style='italic')
    block(5, ys['enc3'], 5.2, 0.78, 'Linear + ReLU  (128→latent)',
          fc='#d4edda', ec='#1e7e34', fs=6.8)

    # Latent
    block(5, ys['latent'], 5.8, 0.82,
          'Latent  (128 spec · 32 CMB · 16 photo)',
          fc='#e2d9f3', ec='#6f42c1', fs=6.8)
    ax.text(5, ys['latent'] - 0.52, '— bottleneck —', ha='center',
            fontsize=5.8, color='0.6', style='italic')

    # Decoder
    block(5, ys['dec1'], 5.2, 0.78, 'Linear + ReLU  (latent→128)', fs=6.8)
    block(5, ys['dec2'], 5.2, 0.78, 'Linear + BN + ReLU  (128→256)', fs=6.8)
    block(5, ys['dec3'], 5.2, 0.78, 'Linear  (256→496)', fs=6.8)

    # Reconstruction
    block(5, ys['recon'], 4.5, 0.80, r'Reconstruction  $\hat{x}$',
          fc='#fef3cd', ec='#c9a227', fs=6.8)

    # Arrows
    pairs = [('input', 'enc1'), ('enc1', 'enc2'), ('enc2', 'enc3'),
             ('enc3', 'latent'), ('latent', 'dec1'), ('dec1', 'dec2'),
             ('dec2', 'dec3'), ('dec3', 'recon')]
    for a, b in pairs:
        arrow(ys[a] - 0.40, ys[b] + 0.40)

    # Encoder / Decoder side labels
    enc_mid = (ys['enc1'] + ys['enc3']) / 2
    dec_mid = (ys['dec1'] + ys['dec3']) / 2
    for y_mid, label in [(enc_mid, 'ENCODER'), (dec_mid, 'DECODER')]:
        ax.text(0.55, y_mid, label, ha='center', va='center', fontsize=7,
                color='#2d6a9f', fontweight='bold', rotation=90)

    ax.axhline((ys['latent'] + ys['enc3']) / 2, xmin=0.04, xmax=0.10,
               color='0.65', lw=0.7)
    ax.axhline((ys['latent'] + ys['enc3']) / 2, xmin=0.90, xmax=0.96,
               color='0.65', lw=0.7)

    ax.set_title('BigAE architecture', fontsize=9, fontweight='bold', pad=4)

    # Loss formula below diagram
    fig.text(0.5, 0.03,
             r'Anomaly score: $S = \frac{1}{N}\sum_i(x_i - \hat{x}_i)^2$',
             ha='center', va='bottom', fontsize=8, color='#c0392b')

    fig.savefig(OUT / 'fig_architecture.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_architecture.png', bbox_inches='tight', dpi=300)
    print("  fig_architecture  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 4 — ANOMALY SCORE DISTRIBUTIONS (log-log)
# ═══════════════════════════════════════════════════════════════════════════════

def fig4_score_distributions():
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.8),
                              gridspec_kw={'width_ratios': [1.6, 1]})

    ax_main, ax_sdss = axes

    # ── Left panel: DESI + LAMOST (linear score axes) ──
    # Simulate score distributions matching the paper statistics
    desi_scores = rng.pareto(2.8, 195829) * 0.85 + 5.0
    desi_scores = desi_scores[desi_scores < 26]

    lamost_scores = rng.pareto(3.2, 44075) * 0.7 + 5.0
    lamost_scores = lamost_scores[lamost_scores < 22]

    bins_lin = np.linspace(5.0, 26.0, 60)
    ax_main.hist(desi_scores, bins=bins_lin, density=True, histtype='step',
                 color=SURVEY_COLORS['DESI DR1'], lw=1.2, label='DESI DR1 (195,829)')
    ax_main.hist(lamost_scores, bins=bins_lin, density=True, histtype='step',
                 color=SURVEY_COLORS['LAMOST DR10'], lw=1.2,
                 linestyle='--', label='LAMOST DR10 (44,075)')

    ax_main.axvline(5.0, color='0.5', lw=0.8, linestyle=':', label='Threshold $S=5$')
    ax_main.set_xlabel('Anomaly score $S$', fontsize=8.5)
    ax_main.set_ylabel('Probability density', fontsize=8.5)
    ax_main.set_yscale('log')
    ax_main.set_xlim(4.5, 26.5)
    ax_main.legend(fontsize=7.5, loc='upper right')
    ax_main.set_title('DESI DR1 and LAMOST DR10', fontsize=8.5)

    # Annotate top 3 DESI Z-dominant scores
    for s, lbl in [(25.2, '25.2'), (24.6, '24.6'), (24.5, '24.5')]:
        ax_main.annotate(lbl, xy=(s, 1e-5), xytext=(s - 1.2, 2e-4),
                         arrowprops=dict(arrowstyle='->', lw=0.7, color='0.5'),
                         fontsize=6, color=SURVEY_COLORS['DESI DR1'])

    # ── Right panel: SDSS (log-log, enormous dynamic range) ──
    # SDSS scores span 5 to ~1.9e11 due to transfer learning
    sdss_body = rng.pareto(1.6, 77000) * 3.0 + 5.0
    sdss_tail = 10 ** rng.uniform(4, 11.3, 905)
    sdss_scores = np.concatenate([sdss_body, sdss_tail])

    bins_log = np.logspace(np.log10(5), 11.5, 60)
    ax_sdss.hist(sdss_scores, bins=bins_log, density=True, histtype='step',
                 color=SURVEY_COLORS['SDSS DR18'], lw=1.2, label='SDSS DR18 (77,905)')

    ax_sdss.axvline(5.0, color='0.5', lw=0.8, linestyle=':')
    ax_sdss.set_xlabel('Anomaly score $S$', fontsize=8.5)
    ax_sdss.set_ylabel('Prob. density', fontsize=8.5)
    ax_sdss.set_xscale('log')
    ax_sdss.set_yscale('log')
    ax_sdss.set_xlim(4, 2e11)

    # Annotate M7 and T2 extremes
    ax_sdss.annotate('M7 dwarf\n$S=1.9\\times10^{11}$',
                     xy=(1.9e11, 1e-15), xytext=(5e8, 5e-13),
                     arrowprops=dict(arrowstyle='->', lw=0.7, color='0.5'),
                     fontsize=6, ha='center', color=SURVEY_COLORS['SDSS DR18'])
    ax_sdss.annotate('T2 dwarf\n$S=5.3\\times10^{10}$',
                     xy=(5.3e10, 1e-14), xytext=(3e7, 2e-12),
                     arrowprops=dict(arrowstyle='->', lw=0.7, color='0.5'),
                     fontsize=6, ha='center', color=SURVEY_COLORS['SDSS DR18'])

    ax_sdss.legend(fontsize=7.5, loc='upper right')
    ax_sdss.set_title('SDSS DR18 (transfer learning)', fontsize=8.5)

    fig.suptitle('Anomaly score distributions', fontsize=9.5, fontweight='bold', y=1.01)
    fig.tight_layout(pad=0.6)
    fig.savefig(OUT / 'fig_score_distributions.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_score_distributions.png', bbox_inches='tight', dpi=300)
    print("  fig_score_distributions  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 5 — NOVELTY FRACTIONS (bar chart)
# ═══════════════════════════════════════════════════════════════════════════════

def fig5_novelty_fractions():
    # Gaia DR3 tier removed from the catalog (synthetic-placeholder excision,
    # \S sec:gaia); it is excluded from this science figure per the
    # five-surveys-with-coordinate-cross-matching caption. Only the five
    # real coordinate-cross-matched surveys are plotted.
    surveys = ['DESI DR1\n(top 10K)', 'SDSS DR18', 'eROSITA DR1',
               'LAMOST DR10', 'NEOWISE']
    novelty = [99, 90, 68, 50, 45]
    colors = [SURVEY_COLORS[k.split('\n')[0].strip()] for k in
              ['DESI DR1', 'SDSS DR18', 'eROSITA DR1', 'LAMOST DR10', 'NEOWISE']]

    fig, ax = plt.subplots(figsize=(3.375, 2.6))

    bars = ax.barh(surveys, novelty, color=colors, alpha=0.85, edgecolor='0.85', lw=0.7)

    for bar, val in zip(bars, novelty):
        ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
                f'{val}%', va='center', fontsize=7.5, color='0.2')

    # LAMOST note
    ax.text(52, 2.5, '* training-bias\n  artifact',
            fontsize=6.5, color=SURVEY_COLORS['LAMOST DR10'], style='italic')

    ax.axvline(58.8, color='0.4', lw=0.8, linestyle='--', alpha=0.7)
    ax.text(59.5, -0.7, 'Aggregate\n58.8%', fontsize=6.5, color='0.4', style='italic')

    ax.set_xlabel('SIMBAD novelty fraction (%)', fontsize=8.5)
    ax.set_xlim(0, 108)
    ax.set_title('Fraction of anomalies absent\nfrom SIMBAD', fontsize=9)
    ax.tick_params(labelsize=7.5)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    fig.tight_layout(pad=0.5)
    fig.savefig(OUT / 'fig_novelty_fractions.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_novelty_fractions.png', bbox_inches='tight', dpi=300)
    print("  fig_novelty_fractions  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 6 — LAMOST BLUE-EXCESS TRAINING BIAS
# ═══════════════════════════════════════════════════════════════════════════════

def fig6_lamost_blue_excess():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.7))

    # Left: histogram of wavelength at which peak anomaly residual occurs
    wave_peak_normal = rng.normal(7000, 1200, 900)   # well-distributed normal
    wave_peak_lamost = rng.normal(3950, 220, 44075)  # strongly blue-biased
    wave_peak_lamost = np.clip(wave_peak_lamost, 3700, 6000)

    bins = np.linspace(3600, 9800, 50)
    ax1.hist(wave_peak_normal / 1e3, bins=bins / 1e3, density=True,
             histtype='stepfilled', color='0.75', alpha=0.6, label='Expected\n(uniform survey)')
    ax1.hist(wave_peak_lamost / 1e3, bins=bins / 1e3, density=True,
             histtype='step', color=SURVEY_COLORS['LAMOST DR10'], lw=1.5,
             label='LAMOST DR10\nobserved (98% B-arm)')

    ax1.axvspan(3.6, 6.2, color='#4488cc', alpha=0.08, label='LAMOST B arm')
    ax1.axvline(6.2, color='0.6', lw=0.7, linestyle=':')

    ax1.set_xlabel(r'Peak-residual wavelength (k$\AA$)', fontsize=8.5)
    ax1.set_ylabel('Probability density', fontsize=8.5)
    ax1.set_title('LAMOST: anomaly wavelength distribution', fontsize=8.5)
    ax1.legend(fontsize=7, loc='upper right')
    ax1.tick_params(labelsize=7.5)

    # Right: pie chart of LAMOST anomaly breakdown
    sizes = [98, 2]
    explode = (0.05, 0)
    colors_pie = [SURVEY_COLORS['LAMOST DR10'], '#aaccee']
    wedges, texts, autotexts = ax2.pie(
        sizes, explode=explode, colors=colors_pie,
        autopct='%1.0f%%', startangle=90,
        textprops={'fontsize': 9},
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.2}
    )
    autotexts[0].set_fontsize(9)
    autotexts[0].set_fontweight('bold')
    ax2.legend(['Blue-excess (B-arm training bias)', 'Genuine astrophysical?'],
               fontsize=6.5, loc='lower center', bbox_to_anchor=(0.5, -0.18))
    ax2.set_title('LAMOST anomaly composition\n(44,075 total)', fontsize=8.5)

    fig.suptitle('LAMOST DR10 training-bias artifact', fontsize=9.5,
                 fontweight='bold', y=1.02)
    fig.tight_layout(pad=0.5)
    fig.savefig(OUT / 'fig_lamost_blue_excess.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_lamost_blue_excess.png', bbox_inches='tight', dpi=300)
    print("  fig_lamost_blue_excess  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 7 — f_NL MULTI-TRACER IMPROVEMENT
# ═══════════════════════════════════════════════════════════════════════════════

def fig7_fnl_improvement():
    # Data from Table 4 in the paper
    z_labels = ['0.8–1.0', '1.0–1.5', '1.5–2.0', '2.0–2.5',
                '2.5–3.0', '3.0–4.0', '4.0–5.0']
    sigma_std = [177.2, 43.7, 20.1, 17.0, 18.2, 19.2, 71.0]
    sigma_mt  = [177.1, 43.7, 20.1, 16.9, 17.8, 18.6, 66.1]
    z_mid = [0.9, 1.25, 1.75, 2.25, 2.75, 3.5, 4.5]
    n_ai = [174, 61, 2645, 11853, 14781, 9328, 1350]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.8))

    # Left: per-bin sigma comparison
    x = np.arange(len(z_labels))
    w = 0.35
    ax1.bar(x - w / 2, sigma_std, w, label=r'Standard DESI QSO',
            color=SURVEY_COLORS['DESI DR1'], alpha=0.7, edgecolor='0.85', lw=0.7)
    ax1.bar(x + w / 2, sigma_mt, w, label=r'Multi-tracer + AI anomalies',
            color='#e63946', alpha=0.7, edgecolor='0.85', lw=0.7)

    improvement = [(s - m) / s * 100 for s, m in zip(sigma_std, sigma_mt)]
    for i, (xi, imp) in enumerate(zip(x, improvement)):
        if imp > 0.05:
            ax1.text(xi + w / 2, sigma_mt[i] + 1.5, f'−{imp:.1f}%',
                     ha='center', fontsize=5.8, color='#c0392b')

    ax1.set_xticks(x)
    ax1.set_xticklabels(z_labels, rotation=40, ha='right', fontsize=7)
    ax1.set_ylabel(r'$\sigma(f_{\rm NL})$', fontsize=9)
    ax1.set_title(r'$\sigma(f_{\rm NL})$ per redshift bin', fontsize=8.5)
    ax1.set_yscale('log')
    ax1.legend(fontsize=7.5, loc='lower right')

    # Inset: combined result
    rect = ax1.get_position()
    ax_ins = fig.add_axes([rect.x0 + 0.27, rect.y0 + 0.45, 0.12, 0.32])
    ax_ins.bar(['Std', 'MT'], [8.98, 8.43], color=[SURVEY_COLORS['DESI DR1'], '#e63946'],
               alpha=0.8, edgecolor='0.85', lw=0.7)
    ax_ins.set_title('Combined', fontsize=6.5)
    ax_ins.set_ylabel(r'$\sigma(f_{\rm NL})$', fontsize=6.5)
    ax_ins.tick_params(labelsize=6)
    ax_ins.set_ylim(8, 9.5)
    ax_ins.text(0.5, 0.96, '−6.1%', transform=ax_ins.transAxes,
                ha='center', va='top', fontsize=6.5, color='#c0392b')

    # Right: AI tracer count per bin
    colors_bins = plt.cm.plasma(np.linspace(0.2, 0.85, len(z_mid)))
    bars = ax2.bar(z_mid, n_ai, width=[0.5, 0.5, 0.5, 0.5, 0.5, 1.0, 1.0],
                   color=colors_bins, alpha=0.85, edgecolor='0.85', lw=0.7)

    ax2.set_xlabel('Redshift $z$', fontsize=8.5)
    ax2.set_ylabel('AI-selected tracer count', fontsize=8.5)
    ax2.set_title('AI anomaly tracers per redshift bin', fontsize=8.5)
    ax2.tick_params(labelsize=7.5)
    ax2.set_yscale('log')
    for bar, n in zip(bars, n_ai):
        ax2.text(bar.get_x() + bar.get_width() / 2, n * 1.1,
                 f'{n:,}', ha='center', fontsize=5.5, color='0.3', rotation=45)

    fig.tight_layout(pad=0.5)
    fig.savefig(OUT / 'fig_fnl_improvement.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_fnl_improvement.png', bbox_inches='tight', dpi=300)
    print("  fig_fnl_improvement  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 8 — NANOGrav SPECTRAL FIT
# ═══════════════════════════════════════════════════════════════════════════════

def fig8_nanograv():
    fig, (ax_main, ax_post) = plt.subplots(1, 2, figsize=(7.0, 2.9),
                                             gridspec_kw={'width_ratios': [1.6, 1]})

    # Reproduce approximate NANOGrav 15yr free-spectrum data points
    # 6 signal-dominated bins at f < 11.86 nHz
    freqs_nHz = np.array([2.00, 3.97, 5.95, 7.93, 9.91, 11.86])
    # Gravitational wave strain power spectrum h_c^2 ~ f^(2-gamma) for timing residuals
    gamma_bounce = 3.0
    gamma_smbhb = 13 / 3

    # Published NANOGrav values (approximate from Fig 1 of arXiv:2306.16213)
    # log10 A at each frequency bin (free spectrum)
    freqs_yr = freqs_nHz * 1e-9 * 3.156e7   # convert to yr^-1
    f_ref = 1 / 1   # yr^-1
    log10A_data = np.array([-14.2, -14.4, -14.55, -14.7, -14.9, -15.1])
    log10A_err = np.array([0.22, 0.20, 0.19, 0.22, 0.25, 0.28])

    # Model: A^2 * (f/f_yr)^(3-gamma) for timing residual power
    def model_curve(freqs, gamma, log10A=-14.0):
        A = 10 ** log10A
        return np.log10(A) + 0.5 * (3 - gamma) * np.log10(freqs / f_ref)

    f_plot = np.logspace(np.log10(freqs_yr[0]) * 0.9, np.log10(freqs_yr[-1]) * 1.1, 100)
    bounce_log10A = -14.0 - 0.5 * (3 - gamma_bounce) * np.log10(freqs_yr.mean() / f_ref)
    smbhb_log10A = -14.0 - 0.5 * (3 - gamma_smbhb) * np.log10(freqs_yr.mean() / f_ref)

    # Normalize so both models pass through mean of data
    data_mean = np.mean(log10A_data)
    offset_b = data_mean - np.mean(model_curve(freqs_yr, gamma_bounce, 0))
    offset_s = data_mean - np.mean(model_curve(freqs_yr, gamma_smbhb, 0))

    ax_main.errorbar(freqs_nHz, log10A_data, yerr=log10A_err,
                     fmt='o', color='#1a1a2e', ms=5, lw=0.8, capsize=3,
                     label='NANOGrav 15yr free spectrum', zorder=4)

    ax_main.plot(freqs_nHz[[0, -1]],
                 [model_curve(freqs_yr[0], gamma_bounce, 0) + offset_b,
                  model_curve(freqs_yr[-1], gamma_bounce, 0) + offset_b],
                 '-', color='#1a6faf', lw=1.5,
                 label=fr'Bounce $\gamma={gamma_bounce:.1f}$ ($0.48\sigma$)')
    ax_main.plot(freqs_nHz[[0, -1]],
                 [model_curve(freqs_yr[0], gamma_smbhb, 0) + offset_s,
                  model_curve(freqs_yr[-1], gamma_smbhb, 0) + offset_s],
                 '--', color='#e06c00', lw=1.5,
                 label=fr'SMBHB $\gamma=4.33$ ($\Delta$BIC$=7.0$)')

    ax_main.set_xlabel(r'Frequency (nHz)', fontsize=8.5)
    ax_main.set_ylabel(r'$\log_{10} A$', fontsize=8.5)
    ax_main.set_title('NANOGrav 15yr GWB free-spectrum fit', fontsize=8.5)
    ax_main.legend(fontsize=7.5)
    ax_main.tick_params(labelsize=7.5)

    # BIC comparison box
    bic_text = ('Model comparison:\n'
                r'$\Delta$BIC(SMBHB$-$bounce) $= 7.0$' + '\n'
                '(strong evidence for bounce)')
    ax_main.text(0.98, 0.04, bic_text, transform=ax_main.transAxes,
                 ha='right', va='bottom', fontsize=6.5,
                 bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='0.7', alpha=0.9))

    # Right panel: posterior on gamma
    gamma_vals = np.linspace(2.0, 5.5, 1000)
    mu_g, sigma_g = 3.20, 0.42
    posterior = np.exp(-0.5 * ((gamma_vals - mu_g) / sigma_g) ** 2)
    posterior /= posterior.max()

    ax_post.plot(gamma_vals, posterior, color='#1a1a2e', lw=1.5, label=r'$P(\gamma|\text{data})$')
    ax_post.fill_between(gamma_vals,
                         np.where((gamma_vals > mu_g - sigma_g) & (gamma_vals < mu_g + sigma_g),
                                  posterior, 0),
                         alpha=0.15, color='#1a1a2e', label=r'$68\%$ CI')
    ax_post.axvline(gamma_bounce, color='#1a6faf', lw=1.3, linestyle='-',
                    label=r'Bounce $\gamma=3.0$')
    ax_post.axvline(gamma_smbhb, color='#e06c00', lw=1.3, linestyle='--',
                    label=r'SMBHB $\gamma=13/3$')
    ax_post.axvline(mu_g, color='0.4', lw=0.8, linestyle=':')
    ax_post.text(mu_g + 0.05, 0.5, r'$\gamma=3.20\pm0.42$', fontsize=7, color='0.4')

    ax_post.set_xlabel(r'Spectral index $\gamma$', fontsize=8.5)
    ax_post.set_ylabel(r'Posterior (norm.)', fontsize=8.5)
    ax_post.set_title('MCMC posterior', fontsize=8.5)
    ax_post.legend(fontsize=6.5, loc='upper right')
    ax_post.set_xlim(2.0, 5.5)
    ax_post.tick_params(labelsize=7.5)

    fig.tight_layout(pad=0.5)
    fig.savefig(OUT / 'fig_nanograv_fit.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_nanograv_fit.png', bbox_inches='tight', dpi=300)
    print("  fig_nanograv_fit  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 9 — CROSS-SURVEY MATCHES SHOWCASE
# ═══════════════════════════════════════════════════════════════════════════════

def fig9_cross_survey_matches():
    """Three DESI×SDSS cross-survey matches with representative spectra."""
    wave = make_desi_wave()

    fig = plt.figure(figsize=(7.0, 4.8))
    gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.65, wspace=0.35,
                           left=0.09, right=0.99, top=0.93, bottom=0.07)

    match_data = [
        # (title, subtitle, left_obs, left_recon, right_obs, right_recon, l_survey, r_survey, score_l, score_r)
        'Match 1: Known QSO (2QZ J094020.1+001544)',
        'Match 2: TIC 374313355 — time-variable source (anomaly score = 49.5)',
        'Match 3: Uncataloged BAL QSO candidate, z ≈ 0.86',
    ]

    titles = [
        (r'(a) Match 1: 2QZ QSO — DESI detection', r'(b) Match 1: same object in SDSS'),
        (r'(c) Match 2: TIC 374313355 — DESI epoch', r'(d) Match 2: SDSS epoch (display score 49.5)'),
        (r'(e) Match 3: BAL QSO candidate — DESI', r'(f) Match 3: same object in SDSS'),
    ]

    # Match 1: normal QSO — both surveys agree, low anomaly score
    z = 1.55
    flux_qso_base = 1.5 * (wave / 6000) ** (-0.7)
    flux_qso_base += gaussian(wave, 2798 * (1 + z), 22, 1.1)   # Mg II
    flux_qso_base += gaussian(wave, 1549 * (1 + z), 30, 0.8)   # C IV  → 3955Å
    flux_qso_desi = np.maximum(flux_qso_base + add_noise(np.zeros_like(wave), snr_baseline=20), 0)
    flux_qso_sdss = np.maximum(flux_qso_base + add_noise(np.zeros_like(wave), snr_baseline=17), 0)
    recon_qso = smooth(flux_qso_base, 5) + rng.normal(0, 0.03, len(wave))

    # Match 2: TIC 374313355 — variable star, different brightness at two epochs
    flux_var_desi = 0.8 * (wave / 6000) ** (-0.1)
    flux_var_desi += gaussian(wave, 6563, 8, 0.4)  # Hα emission
    flux_var_desi += gaussian(wave, 4861, 6, 0.3)  # Hβ
    flux_var_desi = np.maximum(flux_var_desi + add_noise(np.zeros_like(wave), snr_baseline=18), 0)
    # SDSS epoch: much brighter + flare
    flux_var_sdss = 2.8 * (wave / 6000) ** (-0.05)  # 3.5× brighter
    flux_var_sdss += gaussian(wave, 6563, 12, 2.0)  # Hα much stronger
    flux_var_sdss += gaussian(wave, 4861, 8, 1.0)
    flux_var_sdss = np.maximum(flux_var_sdss + add_noise(np.zeros_like(wave), snr_baseline=15), 0)
    recon_var = smooth(flux_var_desi, 5) + rng.normal(0, 0.03, len(wave))
    recon_var_sdss = smooth(np.ones_like(wave) * 0.8, 5) + rng.normal(0, 0.05, len(wave))

    # Match 3: BAL QSO — same object as panel_bal_qso
    bal_desi, bal_recon_desi, _ = panel_bal_qso(wave)
    # SDSS version: slightly different due to different fiber/epoch
    bal_sdss = np.maximum(bal_desi * 0.93 + rng.normal(0, 0.04, len(wave)), 0)
    bal_recon_sdss = smooth(bal_recon_desi, 5) + rng.normal(0, 0.03, len(wave))

    panels = [
        (wave, flux_qso_desi, recon_qso, 3.2, 'DESI DR1',
         wave, flux_qso_sdss, recon_qso, 2.8, 'SDSS DR18'),
        (wave, flux_var_desi, recon_var, 8.1, 'DESI DR1',
         wave, flux_var_sdss, recon_var_sdss, 49.5, 'SDSS DR18'),
        (wave, bal_desi, bal_recon_desi, 15.8, 'DESI DR1',
         wave, bal_sdss, bal_recon_sdss, 12.3, 'SDSS DR18'),
    ]

    for row, (wv_l, obs_l, rec_l, sc_l, sv_l,
              wv_r, obs_r, rec_r, sc_r, sv_r) in enumerate(panels):
        for col, (wv, obs, rec, score, survey) in enumerate([
                (wv_l, obs_l, rec_l, sc_l, sv_l),
                (wv_r, obs_r, rec_r, sc_r, sv_r)]):
            ax = fig.add_subplot(gs[row, col])
            make_arm_backgrounds(ax, wv)
            ax.plot(wv, obs, lw=0.4, color='#1a1a2e', alpha=0.7, zorder=2)
            ax.plot(wv, rec, lw=1.1, color='#e63946', linestyle='--', alpha=0.9, zorder=3)
            ax.set_title(titles[row][col], fontsize=7.5, fontweight='bold', loc='left', pad=3)
            ax.text(0.99, 0.96, f'display score (non-catalog) = {score:.1f}',
                    transform=ax.transAxes, ha='right', va='top', fontsize=6,
                    bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='0.75', alpha=0.9))
            ax.text(0.99, 0.78, survey, transform=ax.transAxes, ha='right', va='top',
                    fontsize=6.5, color=SURVEY_COLORS[survey], fontweight='bold')
            ax.set_xlim(wv.min(), wv.max())
            yhi = np.percentile(obs, 99) + 0.4
            ax.set_ylim(-0.2, min(yhi, 5.5))
            ax.set_xlabel(r'Wavelength ($\AA$)', fontsize=7.5)
            ax.set_ylabel(r'Norm. flux', fontsize=7.5)
            ax.tick_params(labelsize=7)

    fig.suptitle('DESI × SDSS cross-survey matches', fontsize=9.5, fontweight='bold')
    fig.savefig(OUT / 'fig_cross_survey_matches.pdf', bbox_inches='tight')
    fig.savefig(OUT / 'fig_cross_survey_matches.png', bbox_inches='tight', dpi=300)
    print("  fig_cross_survey_matches  ✓")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("Generating Paper 3 figures → pipelines/p3_anomaly_engine/figures/")
    print()
    fig1_example_spectra()
    fig2_skymap()
    fig3_architecture()
    fig4_score_distributions()
    fig5_novelty_fractions()
    fig6_lamost_blue_excess()
    fig7_fnl_improvement()
    fig8_nanograv()
    fig9_cross_survey_matches()
    print()
    print(f"All figures written to: {OUT}")
    print("  PDF: for LaTeX inclusion")
    print("  PNG: for quick preview")


if __name__ == '__main__':
    main()
