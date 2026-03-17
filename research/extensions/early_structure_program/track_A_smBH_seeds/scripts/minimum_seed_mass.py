#!/usr/bin/env python3
"""
Track A: SMBH Seed Minimum Mass Analysis
=========================================

Forward-model constraint analysis computing the minimum seed mass required
to grow observed high-redshift supermassive black holes via Eddington-limited
(Salpeter) accretion.

For each observed SMBH at (M_BH, z_obs), we invert the Salpeter growth
equation to find M_seed,min as a function of z_seed:

    M(t) = M_seed * exp[(1 - eps_rad) / eps_rad * Delta_t / t_Edd * f_duty]

so:

    M_seed,min = M_BH * exp[-(1 - eps_rad) / eps_rad * Delta_t / t_Edd * f_duty]

where Delta_t = t(z_obs) - t(z_seed) is the available growth time computed
from the cosmological age-redshift relation.

Two cosmologies are compared:
  - Planck 2018: H0=67.4, Om=0.315, OL=0.685
  - Framework (spin-torsion): H0=69.2, Om=0.285, OL=0.715, DNeff=0.24

References
----------
- Bogdan et al. 2024, arXiv: 2305.15458 (UHZ-1)
- Maiolino et al. 2024, arXiv: 2305.12492 (GN-z11)
- Larson et al. 2023, arXiv: 2303.08918 (CEERS-1019)
- Wang et al. 2021, arXiv: 2101.03179 (J0313-1806)
- Banados et al. 2018, arXiv: 1712.01860 (J1342+0928)
"""

import os
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Physical constants & growth parameters
# ---------------------------------------------------------------------------
EPS_RAD = 0.1          # radiative efficiency
T_EDD = 0.45           # Salpeter e-folding time [Gyr]
F_DUTY_VALUES = [0.5, 0.7, 1.0]

# Conversion
KM_PER_MPC = 3.0857e19  # km per Mpc
GYR_PER_SEC = 1.0 / (3.1557e16)  # Gyr per second


# ---------------------------------------------------------------------------
# Cosmological models
# ---------------------------------------------------------------------------
class FlatLCDM:
    """Flat Lambda-CDM cosmology for age-redshift relation."""

    def __init__(self, H0, Omega_m, Omega_Lambda, label="", **kwargs):
        self.H0 = H0  # km/s/Mpc
        self.Omega_m = Omega_m
        self.Omega_L = Omega_Lambda
        self.label = label
        # Hubble time in Gyr
        self.t_H = (1.0 / (H0 / KM_PER_MPC)) * GYR_PER_SEC

    def _integrand(self, a):
        """dt/da integrand for flat LCDM: 1 / [a * H(a)/H0]."""
        z = 1.0 / a - 1.0
        E = np.sqrt(self.Omega_m * (1 + z) ** 3 + self.Omega_L)
        return 1.0 / (a * E)

    def age_at_z(self, z):
        """Cosmic age at redshift z [Gyr]."""
        a_z = 1.0 / (1.0 + z)
        result, _ = quad(self._integrand, 0, a_z, limit=200)
        return self.t_H * result


PLANCK = FlatLCDM(H0=67.4, Omega_m=0.315, Omega_Lambda=0.685,
                  label="Planck 2018")
FRAMEWORK = FlatLCDM(H0=69.2, Omega_m=0.285, Omega_Lambda=0.715,
                     label="Framework")

COSMOLOGIES = [PLANCK, FRAMEWORK]

# ---------------------------------------------------------------------------
# Observed high-z SMBHs
# ---------------------------------------------------------------------------
SMBH_DATA = [
    {"name": "UHZ-1",       "M_BH": 4.0e7,  "z_obs": 10.1,
     "ref": "Bogdan+2024",  "arxiv": "2305.15458"},
    {"name": "GN-z11",      "M_BH": 1.6e6,  "z_obs": 10.6,
     "ref": "Maiolino+2024","arxiv": "2305.12492"},
    {"name": "CEERS-1019",  "M_BH": 1.0e7,  "z_obs": 8.68,
     "ref": "Larson+2023",  "arxiv": "2303.08918"},
    {"name": "J0313-1806",  "M_BH": 1.6e9,  "z_obs": 7.64,
     "ref": "Wang+2021",    "arxiv": "2101.03179"},
    {"name": "J1342+0928",  "M_BH": 8.0e8,  "z_obs": 7.54,
     "ref": "Banados+2018", "arxiv": "1712.01860"},
]

# Seed-channel mass ranges [M_sun]
SEED_CHANNELS = {
    "Pop III remnants":       (10, 300,   "#2196F3", 0.15),
    "Direct collapse (DCBH)": (1e4, 1e5,  "#FF9800", 0.15),
    "Runaway / PBH":          (1e5, 1e6,  "#F44336", 0.15),
}

# Colors for SMBHs
SMBH_COLORS = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e"]


# ---------------------------------------------------------------------------
# Core calculation
# ---------------------------------------------------------------------------
def minimum_seed_mass(M_BH, t_obs, t_seed, f_duty):
    """
    Compute the minimum seed mass via inverted Salpeter growth.

    Parameters
    ----------
    M_BH : float
        Observed black hole mass [M_sun].
    t_obs : float
        Cosmic age at observation redshift [Gyr].
    t_seed : float
        Cosmic age at seed formation redshift [Gyr].
    f_duty : float
        Duty cycle fraction (0 < f_duty <= 1).

    Returns
    -------
    M_seed_min : float
        Minimum seed mass [M_sun].
    """
    delta_t = t_obs - t_seed
    if delta_t <= 0:
        return np.inf
    growth_factor = (1.0 - EPS_RAD) / EPS_RAD * delta_t / T_EDD * f_duty
    return M_BH * np.exp(-growth_factor)


# ---------------------------------------------------------------------------
# Plot 1: Minimum seed mass vs z_seed
# ---------------------------------------------------------------------------
def plot_min_seed_vs_zseed():
    """
    For each SMBH and each cosmology, plot M_seed,min(z_seed) at f_duty = 1.0.
    """
    z_seed_arr = np.linspace(12, 30, 200)
    f_duty = 1.0

    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

    for ax, cosmo in zip(axes, COSMOLOGIES):
        # Pre-compute ages
        t_seed_arr = np.array([cosmo.age_at_z(z) for z in z_seed_arr])

        for smbh, color in zip(SMBH_DATA, SMBH_COLORS):
            t_obs = cosmo.age_at_z(smbh["z_obs"])
            m_seed = np.array([
                minimum_seed_mass(smbh["M_BH"], t_obs, ts, f_duty)
                for ts in t_seed_arr
            ])
            # Mask where z_seed < z_obs (nonsensical)
            mask = z_seed_arr > smbh["z_obs"]
            ax.semilogy(z_seed_arr[mask], m_seed[mask], lw=2, color=color,
                        label=f'{smbh["name"]} ($z={smbh["z_obs"]}$)')

        # Seed-channel bands
        for ch_name, (m_lo, m_hi, ch_col, alpha) in SEED_CHANNELS.items():
            ax.axhspan(m_lo, m_hi, color=ch_col, alpha=alpha, zorder=0)
            ax.text(29.5, np.sqrt(m_lo * m_hi), ch_name, fontsize=7,
                    ha="right", va="center", color=ch_col, fontweight="bold")

        ax.set_xlabel("Seed formation redshift $z_{\\rm seed}$", fontsize=12)
        ax.set_title(cosmo.label, fontsize=13, fontweight="bold")
        ax.set_ylim(1e-1, 1e10)
        ax.set_xlim(12, 30)
        ax.legend(fontsize=8, loc="upper left")
        ax.grid(True, alpha=0.3)

    axes[0].set_ylabel("Minimum seed mass $M_{\\rm seed,min}$ [$M_\\odot$]",
                       fontsize=12)
    fig.suptitle(
        "Minimum SMBH Seed Mass from Salpeter Growth ($f_{\\rm duty}=1.0$)",
        fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, "minimum_seed_mass_vs_zseed.pdf")
    fig.savefig(outpath, bbox_inches="tight", dpi=200)
    fig.savefig(outpath.replace(".pdf", ".png"), bbox_inches="tight", dpi=200)
    print(f"  Saved: {outpath}")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Plot 2: Growth time consistency diagram
# ---------------------------------------------------------------------------
def plot_growth_time_consistency():
    """
    Plot M_seed,min vs available growth time for multiple duty cycles.
    Uses z_seed = 20 as fiducial seed formation redshift.
    """
    z_seed = 20.0
    f_duty_plot = [0.5, 0.7, 1.0]
    linestyles = ["--", "-.", "-"]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

    for ax, cosmo in zip(axes, COSMOLOGIES):
        t_seed = cosmo.age_at_z(z_seed)

        for fd, ls in zip(f_duty_plot, linestyles):
            for smbh, color in zip(SMBH_DATA, SMBH_COLORS):
                t_obs = cosmo.age_at_z(smbh["z_obs"])
                dt = t_obs - t_seed
                if dt <= 0:
                    continue
                m_seed = minimum_seed_mass(smbh["M_BH"], t_obs, t_seed, fd)
                marker_label = (f'{smbh["name"]}' if fd == f_duty_plot[0]
                                else None)
                ax.semilogy(dt * 1e3, m_seed, marker="o", ms=8, color=color,
                            label=marker_label, zorder=5)
                # annotate duty cycle
                ax.annotate(f"$f_d={fd}$", (dt * 1e3, m_seed),
                            fontsize=6, ha="left", va="bottom",
                            xytext=(4, 4), textcoords="offset points")

        # Seed-channel bands
        for ch_name, (m_lo, m_hi, ch_col, alpha) in SEED_CHANNELS.items():
            ax.axhspan(m_lo, m_hi, color=ch_col, alpha=alpha, zorder=0)

        ax.set_xlabel("Available growth time $\\Delta t$ [Myr]", fontsize=12)
        ax.set_title(cosmo.label, fontsize=13, fontweight="bold")
        ax.set_ylim(1e-2, 1e10)
        ax.legend(fontsize=8, loc="upper right")
        ax.grid(True, alpha=0.3)

    axes[0].set_ylabel("Minimum seed mass $M_{\\rm seed,min}$ [$M_\\odot$]",
                       fontsize=12)
    fig.suptitle(
        "Growth Time Consistency ($z_{\\rm seed}=20$)",
        fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, "growth_time_consistency.pdf")
    fig.savefig(outpath, bbox_inches="tight", dpi=200)
    fig.savefig(outpath.replace(".pdf", ".png"), bbox_inches="tight", dpi=200)
    print(f"  Saved: {outpath}")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
def write_summary_table():
    """
    For each SMBH, compute M_seed,min at z_seed = 20 for each duty cycle
    under both cosmologies. Write CSV.
    """
    z_seed = 20.0
    rows = []
    header = ("Object,z_obs,M_BH_Msun,"
              "Planck_fd0.5,Planck_fd0.7,Planck_fd1.0,"
              "Framework_fd0.5,Framework_fd0.7,Framework_fd1.0")
    rows.append(header)

    for smbh in SMBH_DATA:
        vals = [smbh["name"], f'{smbh["z_obs"]:.2f}', f'{smbh["M_BH"]:.2e}']
        for cosmo in COSMOLOGIES:
            t_obs = cosmo.age_at_z(smbh["z_obs"])
            t_seed = cosmo.age_at_z(z_seed)
            for fd in F_DUTY_VALUES:
                ms = minimum_seed_mass(smbh["M_BH"], t_obs, t_seed, fd)
                vals.append(f"{ms:.4e}")
        rows.append(",".join(vals))

    outpath = os.path.join(OUTPUT_DIR, "seed_mass_summary.csv")
    with open(outpath, "w") as f:
        f.write("\n".join(rows) + "\n")
    print(f"  Saved: {outpath}")

    # Also print to console
    print("\n  === Minimum Seed Mass Summary (z_seed = 20) ===")
    for row in rows:
        print(f"  {row}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Track A: SMBH Seed Minimum Mass Analysis")
    print("=" * 50)

    print("\nGenerating Plot 1: Minimum seed mass vs z_seed ...")
    plot_min_seed_vs_zseed()

    print("\nGenerating Plot 2: Growth time consistency ...")
    plot_growth_time_consistency()

    print("\nWriting summary table ...")
    write_summary_table()

    print("\nDone. All outputs in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
