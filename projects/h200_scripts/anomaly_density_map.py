#!/usr/bin/env python3
"""
Full-Sky Anomaly Density Map — Multi-Survey HEALPix Analysis.

Loads anomaly catalogs from SDSS, LAMOST, and eROSITA, builds a HEALPix
NSIDE=64 density map of anomalies per total sources per pixel (for catalogs
with RA/DEC), cross-correlates with Planck dust and galactic latitude, and
tests whether anomaly rate is spatially uniform (real signal) or structured
(systematic).

Output: density_map_summary.json, anomaly_density_healpix.fits, checkpoint.json
"""

import numpy as np
import json
import os
import time
import glob as glob_mod

try:
    import healpy as hp
    HAS_HEALPY = True
except ImportError:
    HAS_HEALPY = False
    print("WARNING: no healpy — spatial mapping disabled")

try:
    import pyarrow.parquet as pq
    HAS_PARQUET = True
except ImportError:
    HAS_PARQUET = False
    print("FATAL: pyarrow required"); raise

from scipy import stats

# ── Configuration ────────────────────────────────────────────────────────────
NSIDE = 64
NPIX  = hp.nside2npix(NSIDE) if HAS_HEALPY else 0
ANOMALY_THRESHOLD = 5.0
MIN_OBJECTS_PER_PIXEL = 20   # minimum for stable rate estimate

BASE     = "/workspace/bigbounce"
OUT_DIR  = os.path.join(BASE, "outputs", "density_map")
PLANCK_DIR = os.path.join(BASE, "outputs", "planck_cmb")

SDSS_GLOB    = os.path.join(BASE, "outputs", "sdss_batch_*.parquet")
LAMOST_GLOB  = os.path.join(BASE, "outputs", "lamost", "lamost_batch_*.parquet")
EROSITA_FILE = os.path.join(BASE, "outputs", "erosita", "erosita_anomalies.parquet")

os.makedirs(OUT_DIR, exist_ok=True)


# ── Checkpoint helpers ───────────────────────────────────────────────────────
CKPT_PATH = os.path.join(OUT_DIR, "checkpoint.json")

def load_checkpoint():
    if os.path.exists(CKPT_PATH):
        with open(CKPT_PATH) as f:
            return json.load(f)
    return {"done_surveys": [], "status": "RUNNING"}

def save_checkpoint(ckpt):
    with open(CKPT_PATH, "w") as f:
        json.dump(ckpt, f, indent=2)


# ── Catalog loaders ──────────────────────────────────────────────────────────
def try_read_column(table, candidates):
    """Try multiple column name variants, return numpy array or None."""
    for c in candidates:
        if c in table.schema.names:
            return table.column(c).to_numpy().astype(np.float64)
    return None


def load_parquet_batch(pattern, survey_name, ra_cols, dec_cols, score_col="anomaly_score"):
    """Load batches matching glob pattern, extract RA/DEC/score."""
    files = sorted(glob_mod.glob(pattern))
    if not files:
        print(f"  [{survey_name}] No files at {pattern}")
        return None, None, None, 0, 0

    all_ra, all_dec, all_score = [], [], []
    total = 0
    has_coords = None

    for i, fpath in enumerate(files):
        table = pq.read_table(fpath)
        n = table.num_rows
        total += n

        score = try_read_column(table, [score_col, "anomaly_score", "score"])
        if score is None:
            score = np.zeros(n, dtype=np.float64)

        ra  = try_read_column(table, ra_cols)
        dec = try_read_column(table, dec_cols)

        if has_coords is None:
            has_coords = (ra is not None and dec is not None)

        if has_coords and ra is not None and dec is not None:
            all_ra.append(ra)
            all_dec.append(dec)
        all_score.append(score)

        if (i + 1) % 20 == 0 or i == len(files) - 1:
            print(f"  [{survey_name}] {i+1}/{len(files)} files, {total:,} rows")

    scores = np.concatenate(all_score)
    n_anom = int(np.sum(scores > ANOMALY_THRESHOLD))

    if has_coords and all_ra:
        ra_arr  = np.concatenate(all_ra)
        dec_arr = np.concatenate(all_dec)
        valid = np.isfinite(ra_arr) & np.isfinite(dec_arr)
        return ra_arr[valid], dec_arr[valid], scores[valid], total, n_anom
    else:
        return None, None, scores, total, n_anom


def load_single_parquet(fpath, survey_name, ra_cols, dec_cols):
    """Load a single parquet file."""
    if not os.path.exists(fpath):
        print(f"  [{survey_name}] File not found: {fpath}")
        return None, None, None, 0, 0

    table = pq.read_table(fpath)
    n = table.num_rows
    score = try_read_column(table, ["anomaly_score", "score"])
    if score is None:
        score = np.zeros(n, dtype=np.float64)

    ra  = try_read_column(table, ra_cols)
    dec = try_read_column(table, dec_cols)
    n_anom = int(np.sum(score > ANOMALY_THRESHOLD))

    if ra is not None and dec is not None:
        valid = np.isfinite(ra) & np.isfinite(dec)
        return ra[valid], dec[valid], score[valid], n, n_anom
    else:
        return None, None, score, n, n_anom


# ── HEALPix mapping ─────────────────────────────────────────────────────────
def build_healpix_maps(ra, dec, scores, nside=NSIDE):
    """Assign sources to HEALPix pixels, compute total and anomaly counts."""
    npix = hp.nside2npix(nside)
    total_map   = np.zeros(npix, dtype=np.float64)
    anomaly_map = np.zeros(npix, dtype=np.float64)

    pixels = hp.ang2pix(nside, ra, dec, lonlat=True, nest=False)
    np.add.at(total_map, pixels, 1)

    anom_mask = scores > ANOMALY_THRESHOLD
    np.add.at(anomaly_map, pixels[anom_mask], 1)

    return total_map, anomaly_map


# ── Galactic latitude analysis ───────────────────────────────────────────────
def galactic_latitude_test(total_map, anomaly_map, nside=NSIDE):
    """Test anomaly rate vs |galactic latitude| — systematic would correlate."""
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    # Convert to galactic coordinates
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    ra_deg  = np.degrees(phi)
    dec_deg = 90.0 - np.degrees(theta)
    coords = SkyCoord(ra=ra_deg * u.deg, dec=dec_deg * u.deg, frame="icrs")
    gal_lat = coords.galactic.b.deg

    occupied = total_map > MIN_OBJECTS_PER_PIXEL
    if occupied.sum() < 10:
        return {"status": "insufficient_data", "n_pixels": int(occupied.sum())}

    rate = anomaly_map[occupied] / total_map[occupied]
    abs_b = np.abs(gal_lat[occupied])

    r_pearson, p_pearson   = stats.pearsonr(abs_b, rate)
    r_spearman, p_spearman = stats.spearmanr(abs_b, rate)

    return {
        "n_pixels": int(occupied.sum()),
        "pearson_r": round(float(r_pearson), 6),
        "pearson_p": float(f"{p_pearson:.4e}"),
        "spearman_r": round(float(r_spearman), 6),
        "spearman_p": float(f"{p_spearman:.4e}"),
        "interpretation": (
            "UNCORRELATED with galactic latitude — anomalies likely astrophysical"
            if abs(r_pearson) < 0.15 else
            "CORRELATED with galactic latitude — possible Galactic contamination"
        ),
    }


# ── Planck dust cross-correlation ────────────────────────────────────────────
def planck_dust_correlation(anomaly_rate_map, nside=NSIDE):
    """Cross-correlate anomaly rate with Planck 353 GHz dust map if available."""
    dust_candidates = [
        os.path.join(PLANCK_DIR, "HFI_SkyMap_353-psb_2048_R3.01_full.fits"),
        os.path.join(PLANCK_DIR, "planck_dust_353.fits"),
        os.path.join(PLANCK_DIR, "dust_map.fits"),
    ]
    # Also search for any FITS file in Planck dir
    dust_candidates += sorted(glob_mod.glob(os.path.join(PLANCK_DIR, "*.fits")))

    dust_map = None
    dust_file = None
    for candidate in dust_candidates:
        if os.path.exists(candidate):
            try:
                dust_map = hp.read_map(candidate, field=0, verbose=False)
                dust_file = candidate
                break
            except Exception:
                continue

    if dust_map is None:
        return {"status": "no_planck_dust_map", "searched": PLANCK_DIR}

    # Degrade dust map to our NSIDE
    dust_nside = hp.npix2nside(len(dust_map))
    if dust_nside != nside:
        dust_map = hp.ud_grade(dust_map, nside)

    occupied = (anomaly_rate_map != hp.UNSEEN) & np.isfinite(anomaly_rate_map)
    if occupied.sum() < 10:
        return {"status": "insufficient_overlap", "dust_file": dust_file}

    rate_vals = anomaly_rate_map[occupied]
    dust_vals = dust_map[occupied]
    valid = np.isfinite(dust_vals) & (dust_vals != hp.UNSEEN)

    if valid.sum() < 10:
        return {"status": "insufficient_valid_dust_pixels", "dust_file": dust_file}

    r, p = stats.pearsonr(rate_vals[valid], dust_vals[valid])
    return {
        "status": "computed",
        "dust_file": os.path.basename(dust_file),
        "pearson_r": round(float(r), 6),
        "pearson_p": float(f"{p:.4e}"),
        "n_pixels": int(valid.sum()),
        "interpretation": (
            "UNCORRELATED with dust — anomalies not driven by Galactic foreground"
            if abs(r) < 0.15 else
            "CORRELATED with dust — possible foreground contamination"
        ),
    }


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    t0 = time.time()
    ckpt = load_checkpoint()
    print("=" * 65)
    print("FULL-SKY ANOMALY DENSITY MAP — MULTI-SURVEY")
    print("=" * 65)

    survey_stats = {}
    combined_total   = np.zeros(NPIX, dtype=np.float64) if HAS_HEALPY else None
    combined_anomaly = np.zeros(NPIX, dtype=np.float64) if HAS_HEALPY else None

    # ── SDSS (plate/mjd/fiberid only — no spatial mapping) ───────────────
    print("\n[1/3] Loading SDSS DR18...")
    _, _, sdss_scores, sdss_n, sdss_anom = load_parquet_batch(
        SDSS_GLOB, "SDSS",
        ra_cols=["ra", "RA", "plug_ra"],
        dec_cols=["dec", "DEC", "plug_dec"],
    )
    survey_stats["SDSS"] = {
        "total": sdss_n, "anomalies": sdss_anom,
        "rate": round(sdss_anom / max(sdss_n, 1), 6),
        "has_spatial": False,
        "note": "plate/mjd/fiberid only — aggregate stats computed",
    }
    if sdss_scores is not None and len(sdss_scores) > 0:
        survey_stats["SDSS"]["score_median"] = round(float(np.median(sdss_scores)), 4)
        survey_stats["SDSS"]["score_p99"] = round(float(np.percentile(sdss_scores, 99)), 4)
    ckpt["done_surveys"].append("SDSS")
    save_checkpoint(ckpt)

    # ── LAMOST (has RA/DEC from FITS headers) ────────────────────────────
    print("\n[2/3] Loading LAMOST DR10...")
    lam_ra, lam_dec, lam_scores, lam_n, lam_anom = load_parquet_batch(
        LAMOST_GLOB, "LAMOST",
        ra_cols=["ra", "RA", "ra_obs", "obsra"],
        dec_cols=["dec", "DEC", "dec_obs", "obsdec"],
    )
    has_lamost_coords = lam_ra is not None
    survey_stats["LAMOST"] = {
        "total": lam_n, "anomalies": lam_anom,
        "rate": round(lam_anom / max(lam_n, 1), 6),
        "has_spatial": has_lamost_coords,
    }
    if has_lamost_coords and HAS_HEALPY:
        lam_total, lam_anomaly = build_healpix_maps(lam_ra, lam_dec, lam_scores)
        combined_total   += lam_total
        combined_anomaly += lam_anomaly
        survey_stats["LAMOST"]["n_healpix_occupied"] = int(np.sum(lam_total > 0))
    ckpt["done_surveys"].append("LAMOST")
    save_checkpoint(ckpt)

    # ── eROSITA (has RA/DEC) ─────────────────────────────────────────────
    print("\n[3/3] Loading eROSITA DR1...")
    ero_ra, ero_dec, ero_scores, ero_n, ero_anom = load_single_parquet(
        EROSITA_FILE, "eROSITA",
        ra_cols=["ra", "RA", "RA_CORR"],
        dec_cols=["dec", "DEC", "DEC_CORR"],
    )
    has_ero_coords = ero_ra is not None
    survey_stats["eROSITA"] = {
        "total": ero_n, "anomalies": ero_anom,
        "rate": round(ero_anom / max(ero_n, 1), 6),
        "has_spatial": has_ero_coords,
    }
    if has_ero_coords and HAS_HEALPY:
        ero_total, ero_anomaly = build_healpix_maps(ero_ra, ero_dec, ero_scores)
        combined_total   += ero_total
        combined_anomaly += ero_anomaly
        survey_stats["eROSITA"]["n_healpix_occupied"] = int(np.sum(ero_total > 0))
    ckpt["done_surveys"].append("eROSITA")
    save_checkpoint(ckpt)

    # ── Combined HEALPix analysis ────────────────────────────────────────
    spatial_results = {}
    if HAS_HEALPY and combined_total is not None and np.sum(combined_total) > 0:
        occupied = combined_total > 0
        n_occupied = int(occupied.sum())
        sky_frac = n_occupied / NPIX

        rate_map = np.full(NPIX, hp.UNSEEN)
        stable = combined_total >= MIN_OBJECTS_PER_PIXEL
        rate_map[stable] = combined_anomaly[stable] / combined_total[stable]

        # Uniformity test: chi-squared on rate per pixel
        if stable.sum() > 10:
            rates = combined_anomaly[stable] / combined_total[stable]
            global_rate = np.sum(combined_anomaly) / np.sum(combined_total)
            expected = combined_total[stable] * global_rate
            observed = combined_anomaly[stable]
            # Poisson chi2
            nonzero = expected > 0
            chi2 = np.sum((observed[nonzero] - expected[nonzero])**2 / expected[nonzero])
            dof = int(nonzero.sum()) - 1
            chi2_pval = float(stats.chi2.sf(chi2, dof)) if dof > 0 else 1.0

            spatial_results["uniformity_test"] = {
                "chi2": round(float(chi2), 2),
                "dof": dof,
                "p_value": float(f"{chi2_pval:.4e}"),
                "reduced_chi2": round(float(chi2 / max(dof, 1)), 4),
                "interpretation": (
                    "UNIFORM: anomaly rate consistent with spatial isotropy (p > 0.01)"
                    if chi2_pval > 0.01 else
                    "NON-UNIFORM: anomaly rate varies across sky (p < 0.01)"
                ),
            }

        # Galactic latitude test
        print("\nTesting galactic latitude dependence...")
        spatial_results["galactic_latitude"] = galactic_latitude_test(
            combined_total, combined_anomaly
        )

        # Planck dust cross-correlation
        print("Cross-correlating with Planck dust...")
        spatial_results["planck_dust"] = planck_dust_correlation(rate_map)

        spatial_results["healpix"] = {
            "nside": NSIDE,
            "npix": NPIX,
            "n_occupied": n_occupied,
            "sky_coverage_fraction": round(sky_frac, 4),
            "sky_coverage_deg2": round(n_occupied * hp.nside2pixarea(NSIDE, degrees=True), 1),
            "global_anomaly_rate": round(float(np.sum(combined_anomaly) / np.sum(combined_total)), 6),
        }

        # Save FITS map
        fits_path = os.path.join(OUT_DIR, "anomaly_density_healpix.fits")
        hp.write_map(fits_path, rate_map, overwrite=True, dtype=np.float32)
        print(f"Saved HEALPix FITS: {fits_path}")
    else:
        spatial_results["status"] = "no_spatial_data_available"
        print("No spatial data available for HEALPix mapping.")

    # ── Summary JSON ─────────────────────────────────────────────────────
    elapsed = time.time() - t0
    summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_seconds": round(elapsed, 1),
        "anomaly_threshold": ANOMALY_THRESHOLD,
        "surveys": survey_stats,
        "total_sources_all_surveys": sum(s["total"] for s in survey_stats.values()),
        "total_anomalies_all_surveys": sum(s["anomalies"] for s in survey_stats.values()),
        "spatial_analysis": spatial_results,
    }

    summary_path = os.path.join(OUT_DIR, "density_map_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary: {summary_path}")

    ckpt["status"] = "COMPLETE"
    save_checkpoint(ckpt)

    # ── Report ───────────────────────────────────────────────────────────
    print("\n" + "=" * 65)
    print("FULL-SKY ANOMALY DENSITY MAP — RESULTS")
    print("=" * 65)
    for name, st in survey_stats.items():
        spatial_tag = "spatial" if st["has_spatial"] else "aggregate"
        print(f"  {name:10s}: {st['total']:>12,} sources, {st['anomalies']:>8,} anomalies "
              f"({st['rate']*100:.3f}%)  [{spatial_tag}]")
    print(f"  {'COMBINED':10s}: {summary['total_sources_all_surveys']:>12,} sources, "
          f"{summary['total_anomalies_all_surveys']:>8,} anomalies")
    if "uniformity_test" in spatial_results:
        ut = spatial_results["uniformity_test"]
        print(f"\n  Uniformity: chi2/dof = {ut['reduced_chi2']:.3f}, p = {ut['p_value']}")
        print(f"  -> {ut['interpretation']}")
    if "galactic_latitude" in spatial_results:
        gl = spatial_results["galactic_latitude"]
        if "pearson_r" in gl:
            print(f"  Gal. lat:  r = {gl['pearson_r']:.4f}, p = {gl['pearson_p']}")
            print(f"  -> {gl['interpretation']}")
    if "planck_dust" in spatial_results:
        pd_res = spatial_results["planck_dust"]
        if pd_res.get("status") == "computed":
            print(f"  Planck dust: r = {pd_res['pearson_r']:.4f}, p = {pd_res['pearson_p']}")
            print(f"  -> {pd_res['interpretation']}")
        else:
            print(f"  Planck dust: {pd_res.get('status', 'unavailable')}")
    print(f"\n  Runtime: {elapsed:.1f}s")
    print("=" * 65)


if __name__ == "__main__":
    main()
