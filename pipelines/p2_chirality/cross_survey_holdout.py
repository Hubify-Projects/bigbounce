#!/usr/bin/env python3
"""
Cross-survey validation for the production chirality catalog.

Run AFTER the production catalog (Catalog C) is complete. Cross-matches
against the CE-ResNet external catalog and computes CW/CCW balance
statistics sliced by survey field, sky region, redshift bin, and
confidence bin. Runs a spatial dipole null test with bootstrap
resampling.

Outputs:
    - JSON report: cross_survey_holdout_report.json
    - Summary table printed to stdout

Usage:
    python cross_survey_holdout.py \
        --catalog chirality_catalog_c_v2_20260323.parquet \
        --ceresnet /workspace/external_catalogs/pre_desi.fits \
        --output cross_survey_holdout_report.json \
        --match-radius 2.0 \
        --n-bootstrap 10000
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
from astropy.io import fits
from scipy.spatial import cKDTree


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def load_catalog_c(path: str | Path) -> pd.DataFrame:
    """Load the production chirality catalog (parquet)."""
    df = pd.read_parquet(path)
    required = {
        "id_str", "ra", "dec",
        "p_cw_eq", "p_ccw_eq", "p_ns_eq",
        "class_eq", "confidence_eq", "is_spiral", "qc_flag",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Catalog C is missing columns: {missing}")
    return df


def load_ceresnet(path: str | Path) -> pd.DataFrame:
    """
    Load the CE-ResNet external catalog from FITS.

    Expected columns (case-insensitive): RA, DEC, SURVEY, Z (or REDSHIFT),
    CLASS (CW/CCW/EDGE-ON/...).
    """
    with fits.open(path) as hdul:
        data = hdul[1].data  # type: ignore[index]
        cols = {c.name.upper(): c.name for c in hdul[1].columns}

    # Normalize column names
    ra_col = cols.get("RA", cols.get("RA_J2000", None))
    dec_col = cols.get("DEC", cols.get("DEC_J2000", None))
    z_col = cols.get("Z", cols.get("REDSHIFT", cols.get("Z_BEST", None)))
    survey_col = cols.get("SURVEY", cols.get("SURVEY_NAME", None))
    class_col = cols.get("CLASS", cols.get("PRED_CLASS", cols.get("CHIRALITY", None)))

    if ra_col is None or dec_col is None:
        raise ValueError("CE-ResNet catalog must contain RA and DEC columns")

    df = pd.DataFrame({
        "ra_ext": np.array(data[ra_col], dtype=np.float64),
        "dec_ext": np.array(data[dec_col], dtype=np.float64),
    })

    if z_col is not None:
        df["z_ext"] = np.array(data[z_col], dtype=np.float64)
    else:
        df["z_ext"] = np.nan

    if survey_col is not None:
        raw = data[survey_col]
        df["survey"] = np.array([s.strip() if isinstance(s, str) else s.decode().strip()
                                 for s in raw])
    else:
        df["survey"] = "UNKNOWN"

    if class_col is not None:
        raw = data[class_col]
        df["class_ext"] = np.array([s.strip().upper() if isinstance(s, str)
                                     else s.decode().strip().upper()
                                     for s in raw])
    else:
        df["class_ext"] = "UNKNOWN"

    return df


# ---------------------------------------------------------------------------
# Cross-matching
# ---------------------------------------------------------------------------

def crossmatch_radec(
    ra1: np.ndarray,
    dec1: np.ndarray,
    ra2: np.ndarray,
    dec2: np.ndarray,
    radius_arcsec: float = 2.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Cross-match two catalogs by RA/DEC using a cKDTree on unit-sphere
    Cartesian coordinates.

    Returns (idx1, idx2, sep_arcsec) for matched pairs within radius.
    """
    def radec_to_xyz(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
        ra_rad = np.deg2rad(ra_deg)
        dec_rad = np.deg2rad(dec_deg)
        x = np.cos(dec_rad) * np.cos(ra_rad)
        y = np.cos(dec_rad) * np.sin(ra_rad)
        z = np.sin(dec_rad)
        return np.column_stack([x, y, z])

    xyz1 = radec_to_xyz(ra1, dec1)
    xyz2 = radec_to_xyz(ra2, dec2)

    # Convert angular radius to Cartesian chord length
    chord_max = 2.0 * np.sin(np.deg2rad(radius_arcsec / 3600.0) / 2.0)

    tree2 = cKDTree(xyz2)
    dists, indices = tree2.query(xyz1, k=1, distance_upper_bound=chord_max)

    matched = np.isfinite(dists)
    idx1 = np.where(matched)[0]
    idx2 = indices[matched]

    # Convert chord distance back to arcsec
    sep_rad = 2.0 * np.arcsin(dists[matched] / 2.0)
    sep_arcsec = np.rad2deg(sep_rad) * 3600.0

    return idx1, idx2, sep_arcsec


# ---------------------------------------------------------------------------
# Balance statistics
# ---------------------------------------------------------------------------

def cw_ccw_balance(classes: pd.Series) -> dict:
    """Compute CW/CCW counts and asymmetry for a series of class labels."""
    n_cw = (classes == "CW").sum()
    n_ccw = (classes == "CCW").sum()
    n_total = n_cw + n_ccw
    if n_total == 0:
        return {"n_cw": 0, "n_ccw": 0, "n_total": 0, "asymmetry": None, "f_cw": None}
    asymmetry = (n_cw - n_ccw) / n_total
    return {
        "n_cw": int(n_cw),
        "n_ccw": int(n_ccw),
        "n_total": int(n_total),
        "asymmetry": float(asymmetry),
        "f_cw": float(n_cw / n_total),
    }


def balance_by_group(df: pd.DataFrame, group_col: str, class_col: str = "class_eq") -> dict:
    """Compute CW/CCW balance per group."""
    results = {}
    for name, group in df.groupby(group_col, observed=True):
        spirals = group[group[class_col].isin(["CW", "CCW"])]
        key = str(name)
        results[key] = cw_ccw_balance(spirals[class_col])
    return results


# ---------------------------------------------------------------------------
# Spatial slicing helpers
# ---------------------------------------------------------------------------

def assign_ra_quadrant(ra: pd.Series) -> pd.Series:
    """Assign RA quadrant: Q1 [0,90), Q2 [90,180), Q3 [180,270), Q4 [270,360)."""
    bins = [0, 90, 180, 270, 360]
    labels = ["Q1_0-90", "Q2_90-180", "Q3_180-270", "Q4_270-360"]
    return pd.cut(ra, bins=bins, labels=labels, right=False, include_lowest=True)


def assign_dec_band(dec: pd.Series) -> pd.Series:
    """Assign DEC band: south (< -30), equatorial (-30 to 30), north (> 30)."""
    conditions = [
        dec < -30,
        (dec >= -30) & (dec <= 30),
        dec > 30,
    ]
    choices = ["south_lt-30", "equatorial_-30to30", "north_gt30"]
    return pd.Series(np.select(conditions, choices, default="equatorial_-30to30"),
                     index=dec.index)


def assign_redshift_bin(z: pd.Series) -> pd.Series:
    """Assign redshift bin: z<0.2, 0.2-0.5, 0.5+."""
    conditions = [
        z < 0.2,
        (z >= 0.2) & (z < 0.5),
        z >= 0.5,
    ]
    choices = ["z_lt_0.2", "z_0.2-0.5", "z_gte_0.5"]
    return pd.Series(np.select(conditions, choices, default="z_unknown"),
                     index=z.index)


def assign_confidence_bin(conf: pd.Series) -> pd.Series:
    """Assign confidence bin: low (<0.6), medium (0.6-0.8), high (>=0.8)."""
    conditions = [
        conf < 0.6,
        (conf >= 0.6) & (conf < 0.8),
        conf >= 0.8,
    ]
    choices = ["conf_low", "conf_medium", "conf_high"]
    return pd.Series(np.select(conditions, choices, default="conf_unknown"),
                     index=conf.index)


# ---------------------------------------------------------------------------
# Dipole null test
# ---------------------------------------------------------------------------

def compute_dipole(ra_deg: np.ndarray, dec_deg: np.ndarray,
                   signal: np.ndarray, nside: int = 16) -> dict:
    """
    Compute the dipole amplitude and direction from a scalar signal on the
    sky using healpy.

    signal: +1 for CW, -1 for CCW (or asymmetry weight per pixel).

    Returns dipole amplitude, (l, b) direction, and the monopole.
    """
    npix = hp.nside2npix(nside)
    pixel_map = np.zeros(npix, dtype=np.float64)
    pixel_counts = np.zeros(npix, dtype=np.float64)

    theta = np.deg2rad(90.0 - dec_deg)  # colatitude
    phi = np.deg2rad(ra_deg)
    pixels = hp.ang2pix(nside, theta, phi)

    np.add.at(pixel_map, pixels, signal)
    np.add.at(pixel_counts, pixels, 1.0)

    # Mean signal per pixel (avoid division by zero)
    mask = pixel_counts > 0
    pixel_map[mask] /= pixel_counts[mask]
    pixel_map[~mask] = hp.UNSEEN

    # Extract monopole + dipole (ell=0,1)
    alm = hp.map2alm(pixel_map, lmax=1, use_pixel_weights=False)
    cl = hp.alm2cl(alm, lmax=1)

    monopole = np.sqrt(cl[0] / (4.0 * np.pi)) if len(cl) > 0 else 0.0
    dipole_power = cl[1] if len(cl) > 1 else 0.0
    dipole_amplitude = np.sqrt(3.0 * dipole_power / (4.0 * np.pi))

    # Dipole direction from alm components
    # a_{1,-1}, a_{1,0}, a_{1,1}
    a10 = alm[hp.Alm.getidx(1, 1, 0)] if len(alm) > hp.Alm.getidx(1, 1, 0) else 0.0
    a11 = alm[hp.Alm.getidx(1, 1, 1)] if len(alm) > hp.Alm.getidx(1, 1, 1) else 0.0

    # Cartesian dipole components
    dz = np.real(a10) * np.sqrt(3.0 / (4.0 * np.pi))
    dx = -np.real(a11) * np.sqrt(6.0 / (4.0 * np.pi))
    dy = -np.imag(a11) * np.sqrt(6.0 / (4.0 * np.pi))

    dipole_l = np.rad2deg(np.arctan2(dy, dx)) % 360.0
    dipole_b = np.rad2deg(np.arcsin(dz / (np.sqrt(dx**2 + dy**2 + dz**2) + 1e-30)))

    return {
        "monopole": float(monopole),
        "dipole_amplitude": float(dipole_amplitude),
        "dipole_l_deg": float(dipole_l),
        "dipole_b_deg": float(dipole_b),
        "nside": nside,
        "n_occupied_pixels": int(mask.sum()),
    }


def bootstrap_dipole(
    ra_deg: np.ndarray,
    dec_deg: np.ndarray,
    signal: np.ndarray,
    n_bootstrap: int = 10000,
    nside: int = 16,
    rng_seed: int = 42,
) -> dict:
    """
    Bootstrap the dipole amplitude to assess significance.

    Shuffles the CW/CCW labels to build the null distribution, then
    computes the p-value of the observed dipole amplitude.
    """
    observed = compute_dipole(ra_deg, dec_deg, signal, nside=nside)
    obs_amp = observed["dipole_amplitude"]

    rng = np.random.default_rng(rng_seed)
    null_amps = np.empty(n_bootstrap, dtype=np.float64)

    for i in range(n_bootstrap):
        shuffled = rng.permutation(signal)
        result = compute_dipole(ra_deg, dec_deg, shuffled, nside=nside)
        null_amps[i] = result["dipole_amplitude"]

    p_value = float(np.mean(null_amps >= obs_amp))
    null_mean = float(np.mean(null_amps))
    null_std = float(np.std(null_amps))
    sigma = float((obs_amp - null_mean) / null_std) if null_std > 0 else 0.0

    return {
        "observed_dipole_amplitude": obs_amp,
        "observed_dipole_l_deg": observed["dipole_l_deg"],
        "observed_dipole_b_deg": observed["dipole_b_deg"],
        "null_mean": null_mean,
        "null_std": null_std,
        "sigma": sigma,
        "p_value": p_value,
        "n_bootstrap": n_bootstrap,
        "nside": nside,
    }


# ---------------------------------------------------------------------------
# Summary printing
# ---------------------------------------------------------------------------

def print_summary_table(report: dict) -> None:
    """Print a human-readable summary table to stdout."""
    header = f"{'Slice':<35} {'N_CW':>7} {'N_CCW':>7} {'Total':>7} {'Asym':>8} {'f_CW':>7}"
    sep = "-" * len(header)

    print("\n" + "=" * len(header))
    print("CROSS-SURVEY HOLDOUT VALIDATION REPORT")
    print("=" * len(header))

    match_info = report.get("match_summary", {})
    print(f"\nCatalog C rows:     {match_info.get('n_catalog_c', '?'):>10}")
    print(f"CE-ResNet rows:     {match_info.get('n_ceresnet', '?'):>10}")
    print(f"Matched pairs:      {match_info.get('n_matched', '?'):>10}")
    print(f"Match radius:       {match_info.get('match_radius_arcsec', '?'):>10} arcsec")
    print(f"Median separation:  {match_info.get('median_sep_arcsec', '?'):>10} arcsec")

    for section_name, section_key in [
        ("BY SURVEY FIELD", "by_survey"),
        ("BY RA QUADRANT", "by_ra_quadrant"),
        ("BY DEC BAND", "by_dec_band"),
        ("BY REDSHIFT BIN", "by_redshift_bin"),
        ("BY CONFIDENCE BIN", "by_confidence_bin"),
    ]:
        data = report.get(section_key, {})
        if not data:
            continue
        print(f"\n--- {section_name} ---")
        print(header)
        print(sep)
        for name, stats in sorted(data.items()):
            n_cw = stats.get("n_cw", 0)
            n_ccw = stats.get("n_ccw", 0)
            n_total = stats.get("n_total", 0)
            asym = stats.get("asymmetry")
            f_cw = stats.get("f_cw")
            asym_str = f"{asym:+.4f}" if asym is not None else "N/A"
            fcw_str = f"{f_cw:.4f}" if f_cw is not None else "N/A"
            print(f"{name:<35} {n_cw:>7} {n_ccw:>7} {n_total:>7} {asym_str:>8} {fcw_str:>7}")

    dipole = report.get("dipole_null_test", {})
    if dipole:
        print("\n--- SPATIAL DIPOLE NULL TEST ---")
        print(f"  Observed amplitude:  {dipole.get('observed_dipole_amplitude', 0):.6f}")
        print(f"  Direction (l, b):    ({dipole.get('observed_dipole_l_deg', 0):.1f}, "
              f"{dipole.get('observed_dipole_b_deg', 0):.1f}) deg")
        print(f"  Null mean +/- std:   {dipole.get('null_mean', 0):.6f} +/- "
              f"{dipole.get('null_std', 0):.6f}")
        print(f"  Sigma:               {dipole.get('sigma', 0):.2f}")
        print(f"  p-value:             {dipole.get('p_value', 1):.4f}")
        print(f"  N bootstrap:         {dipole.get('n_bootstrap', 0)}")
        verdict = "CONSISTENT WITH NULL" if dipole.get("p_value", 1) > 0.05 else "SIGNIFICANT"
        print(f"  Verdict:             {verdict}")

    print("\n" + "=" * len(header) + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Cross-survey holdout validation for the production chirality catalog."
    )
    parser.add_argument(
        "--catalog",
        type=str,
        required=True,
        help="Path to the production Catalog C parquet file.",
    )
    parser.add_argument(
        "--ceresnet",
        type=str,
        default="/workspace/external_catalogs/pre_desi.fits",
        help="Path to the CE-ResNet external catalog (FITS).",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="cross_survey_holdout_report.json",
        help="Path for the output JSON report.",
    )
    parser.add_argument(
        "--match-radius",
        type=float,
        default=2.0,
        help="Cross-match radius in arcseconds (default: 2.0).",
    )
    parser.add_argument(
        "--n-bootstrap",
        type=int,
        default=10000,
        help="Number of bootstrap iterations for dipole null test (default: 10000).",
    )
    parser.add_argument(
        "--nside",
        type=int,
        default=16,
        help="HEALPix NSIDE for dipole computation (default: 16).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for bootstrap reproducibility (default: 42).",
    )
    args = parser.parse_args()

    # ---- Load catalogs ----
    print(f"Loading Catalog C from {args.catalog} ...")
    cat_c = load_catalog_c(args.catalog)
    print(f"  {len(cat_c):,} rows loaded.")

    print(f"Loading CE-ResNet from {args.ceresnet} ...")
    ceresnet = load_ceresnet(args.ceresnet)
    print(f"  {len(ceresnet):,} rows loaded.")

    # ---- Cross-match ----
    print(f"Cross-matching with radius = {args.match_radius} arcsec ...")
    idx1, idx2, sep = crossmatch_radec(
        cat_c["ra"].values, cat_c["dec"].values,
        ceresnet["ra_ext"].values, ceresnet["dec_ext"].values,
        radius_arcsec=args.match_radius,
    )
    print(f"  {len(idx1):,} matched pairs found.")

    if len(idx1) == 0:
        print("ERROR: No cross-matches found. Check coordinate systems and match radius.",
              file=sys.stderr)
        sys.exit(1)

    # Build matched dataframe
    matched = cat_c.iloc[idx1].reset_index(drop=True).copy()
    ext_matched = ceresnet.iloc[idx2].reset_index(drop=True)
    matched["survey"] = ext_matched["survey"].values
    matched["z_ext"] = ext_matched["z_ext"].values
    matched["class_ext"] = ext_matched["class_ext"].values
    matched["sep_arcsec"] = sep

    # ---- Assign spatial / property bins ----
    matched["ra_quadrant"] = assign_ra_quadrant(matched["ra"])
    matched["dec_band"] = assign_dec_band(matched["dec"])
    matched["z_bin"] = assign_redshift_bin(matched["z_ext"])
    matched["conf_bin"] = assign_confidence_bin(matched["confidence_eq"])

    # ---- Restrict to spirals with good QC for balance stats ----
    spirals = matched[(matched["is_spiral"]) & (matched["qc_flag"] == 0)].copy()
    print(f"  {len(spirals):,} spirals with qc_flag==0 in matched set.")

    # ---- Compute balance per slice ----
    report: dict = {
        "match_summary": {
            "n_catalog_c": int(len(cat_c)),
            "n_ceresnet": int(len(ceresnet)),
            "n_matched": int(len(idx1)),
            "n_spirals_qc0": int(len(spirals)),
            "match_radius_arcsec": args.match_radius,
            "median_sep_arcsec": float(np.median(sep)) if len(sep) > 0 else None,
        },
        "overall": cw_ccw_balance(spirals["class_eq"]),
        "by_survey": balance_by_group(spirals, "survey"),
        "by_ra_quadrant": balance_by_group(spirals, "ra_quadrant"),
        "by_dec_band": balance_by_group(spirals, "dec_band"),
        "by_redshift_bin": balance_by_group(spirals, "z_bin"),
        "by_confidence_bin": balance_by_group(spirals, "conf_bin"),
    }

    # ---- Dipole null test ----
    print(f"Running dipole null test (n_bootstrap={args.n_bootstrap}, nside={args.nside}) ...")
    # Encode CW as +1, CCW as -1
    cw_mask = spirals["class_eq"].values == "CW"
    ccw_mask = spirals["class_eq"].values == "CCW"
    dipole_signal = np.zeros(len(spirals), dtype=np.float64)
    dipole_signal[cw_mask] = +1.0
    dipole_signal[ccw_mask] = -1.0

    dipole_result = bootstrap_dipole(
        spirals["ra"].values,
        spirals["dec"].values,
        dipole_signal,
        n_bootstrap=args.n_bootstrap,
        nside=args.nside,
        rng_seed=args.seed,
    )
    report["dipole_null_test"] = dipole_result

    # ---- External catalog agreement ----
    # Where both catalogs have CW or CCW labels, compute agreement rate
    both_spiral = spirals[
        spirals["class_ext"].isin(["CW", "CCW"])
    ].copy()
    if len(both_spiral) > 0:
        agree = (both_spiral["class_eq"] == both_spiral["class_ext"]).sum()
        disagree = len(both_spiral) - agree
        report["external_agreement"] = {
            "n_compared": int(len(both_spiral)),
            "n_agree": int(agree),
            "n_disagree": int(disagree),
            "agreement_rate": float(agree / len(both_spiral)),
        }
    else:
        report["external_agreement"] = {
            "n_compared": 0,
            "n_agree": 0,
            "n_disagree": 0,
            "agreement_rate": None,
        }

    # ---- Write JSON report ----
    output_path = Path(args.output)
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nJSON report written to {output_path}")

    # ---- Print summary ----
    print_summary_table(report)


if __name__ == "__main__":
    main()
