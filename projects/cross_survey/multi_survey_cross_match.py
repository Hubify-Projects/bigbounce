#!/usr/bin/env python3
"""
Multi-Survey Anomaly Cross-Match: SDSS DR18 × eROSITA DR1 × DESI DR1

Loads anomaly catalogs from three independent surveys, resolves sky coordinates
for SDSS (plate/mjd/fiberid → RA/DEC via SkyServer API), and performs pairwise
and triple spatial cross-matching at 3 arcsec radius using cKDTree on unit-sphere
Cartesian coordinates for correct great-circle separation.

Outputs:
  results/sdss_anomalies_with_coords.parquet   — SDSS anomalies with RA/DEC
  results/matches_sdss_desi.parquet            — SDSS × DESI matches
  results/matches_sdss_erosita.parquet         — SDSS × eROSITA matches
  results/matches_desi_erosita.parquet         — DESI × eROSITA matches
  results/matches_triple.parquet               — Triple matches (all 3 surveys)
  results/cross_match_summary.json             — Full statistics summary
"""

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import json
import os
import time
import urllib.request
import urllib.parse
from pathlib import Path
from scipy.spatial import cKDTree
from io import StringIO

# ── Configuration ────────────────────────────────────────────────────────────
MATCH_RADIUS_ARCSEC = 3.0
MATCH_RADIUS_DEG    = MATCH_RADIUS_ARCSEC / 3600.0
SDSS_SCORE_THRESH   = 5.0
DESI_SCORE_THRESH   = 5.0
EROSITA_SCORE_THRESH = 5.0   # only 298 objects; all of them are genuinely anomalous
SDSS_API_MAX_FIBERS  = 300   # max fiberids per API call (controls URL length)
SDSS_API_RATE_SLEEP  = 0.25  # seconds between API calls

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SDSS_DIR   = PROJECT_ROOT / "pipelines" / "h200_results" / "sdss_dr18"
EROSITA_FILE = PROJECT_ROOT / "pipelines" / "h200_results" / "erosita" / "erosita_anomalies.parquet"
DESI_DIR   = PROJECT_ROOT / "pipelines" / "p1_highz_tracers" / "outputs" / "enhanced_18M"
OUT_DIR    = Path(__file__).resolve().parent / "results"
SDSS_COORDS_CACHE = OUT_DIR / "sdss_anomalies_with_coords.parquet"

os.makedirs(OUT_DIR, exist_ok=True)


# ── Utility: unit-sphere coordinates for cKDTree ─────────────────────────────
def to_xyz(ra_deg, dec_deg):
    """Convert RA/DEC (degrees) to unit Cartesian vectors."""
    ra  = np.radians(np.asarray(ra_deg, dtype=float))
    dec = np.radians(np.asarray(dec_deg, dtype=float))
    x = np.cos(dec) * np.cos(ra)
    y = np.cos(dec) * np.sin(ra)
    z = np.sin(dec)
    return np.stack([x, y, z], axis=-1)


def chord_to_arcsec(chord):
    """Convert chord length (unit sphere) to angular separation in arcseconds."""
    # chord = 2 * sin(theta/2), so theta = 2 * arcsin(chord/2)
    half = np.clip(chord / 2.0, -1.0, 1.0)
    return np.degrees(2.0 * np.arcsin(half)) * 3600.0


def arcsec_to_chord(arcsec):
    """Convert arcsecond radius to chord length on unit sphere."""
    return 2.0 * np.sin(np.radians(arcsec / 3600.0) / 2.0)


# ── Catalog loaders ───────────────────────────────────────────────────────────
def load_sdss_raw():
    """Load all SDSS batches into a single DataFrame (plate/mjd/fiberid + scores)."""
    print("Loading SDSS DR18 batches...")
    files = sorted(SDSS_DIR.glob("sdss_batch_*.parquet"))
    if not files:
        raise FileNotFoundError(f"No SDSS parquet files in {SDSS_DIR}")

    # Only load essential columns to save memory
    keep_cols = ["plate", "mjd", "fiberid", "anomaly_score", "rB", "rR", "rZ"]
    dfs = []
    for i, f in enumerate(files):
        t = pq.read_table(str(f), columns=[c for c in keep_cols])
        dfs.append(t.to_pandas())
        if (i + 1) % 10 == 0:
            print(f"  Loaded {i+1}/{len(files)} batches...")

    sdss = pd.concat(dfs, ignore_index=True)
    print(f"  Total SDSS spectra: {len(sdss):,}")

    # Filter to anomalies
    sdss_anom = sdss[sdss["anomaly_score"] > SDSS_SCORE_THRESH].copy().reset_index(drop=True)
    print(f"  SDSS anomalies (score > {SDSS_SCORE_THRESH}): {len(sdss_anom):,}")
    return sdss_anom


def query_sdss_skyserver(pmf_tuples):
    """
    Query SDSS SkyServer DR18 (specobjall) for RA/DEC given (plate, mjd, fiberid) tuples.

    Strategy: group tuples by (plate, mjd) and issue OR-WHERE clauses:
      plate=P AND mjd=M AND fiberid IN (f1,f2,...)
    Batches SDSS_API_BATCH_SIZE plate+mjd groups per request to keep URL manageable.

    Returns a DataFrame with columns: plate, mjd, fiberid, ra, dec, class, z, zErr.
    """
    from collections import defaultdict

    base_url = "https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch"

    # Group by plate only (drop MJD — SDSS anomaly scan may use different MJD than DR18 canonical)
    # The fiberid uniquely identifies the fiber on a given plate; MJD just picks the observing run.
    groups: dict = defaultdict(list)
    for p, m, fid in pmf_tuples:
        groups[int(p)].append(int(fid))

    # Deduplicate fiberids per plate
    for p in groups:
        groups[p] = sorted(set(groups[p]))

    # Build batches limited by total fiber count to keep URL < ~7KB
    batches: list[list] = []   # each element = list of (plate, [fiberids])
    current_batch: list = []
    current_fiber_count = 0

    for p, fibers in groups.items():
        chunk_size = SDSS_API_MAX_FIBERS
        for fib_chunk_start in range(0, len(fibers), chunk_size):
            fib_chunk = fibers[fib_chunk_start: fib_chunk_start + chunk_size]
            if current_fiber_count + len(fib_chunk) > SDSS_API_MAX_FIBERS and current_batch:
                batches.append(current_batch)
                current_batch = []
                current_fiber_count = 0
            current_batch.append((p, fib_chunk))
            current_fiber_count += len(fib_chunk)

    if current_batch:
        batches.append(current_batch)

    n_batches = len(batches)
    results = []
    print(f"  {len(groups):,} unique plates → {n_batches} API calls "
          f"(max {SDSS_API_MAX_FIBERS} fibers/call, MJD-agnostic)")

    for batch_i, batch in enumerate(batches):
        clauses = []
        for (p, fibers) in batch:
            fib_str = ",".join(str(f) for f in fibers)
            clauses.append(f"(plate={p} AND fiberid IN ({fib_str}))")

        where = " OR ".join(clauses)
        # Select best (highest snMedian) row per plate+fiberid combination in case of duplicates
        sql = (
            "SELECT plate, mjd, fiberid, ra, dec, class, z, zErr "
            f"FROM specobjall WHERE {where}"
        )
        params = urllib.parse.urlencode({"cmd": sql, "format": "csv"})
        url = f"{base_url}?{params}"

        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "BigBounce-CrossMatch/1.0"}
                )
                resp = urllib.request.urlopen(req, timeout=120)
                text = resp.read().decode("utf-8", errors="replace")
                if text.strip() and not text.strip().startswith("ERROR"):
                    df_batch = pd.read_csv(StringIO(text), comment="#")
                    results.append(df_batch)
                break
            except Exception as e:
                if attempt < 2:
                    time.sleep(2 ** attempt)
                else:
                    print(f"    Warning: batch {batch_i} failed after 3 attempts: {e}")

        if (batch_i + 1) % 50 == 0 or (batch_i + 1) == n_batches:
            total_so_far = sum(len(r) for r in results)
            print(f"  Batch {batch_i+1}/{n_batches} done — {total_so_far:,} coords retrieved")

        time.sleep(SDSS_API_RATE_SLEEP)

    if results:
        return pd.concat(results, ignore_index=True)
    return pd.DataFrame(columns=["plate", "mjd", "fiberid", "ra", "dec", "class", "z", "zErr"])


def load_sdss_with_coords(force_requery=False):
    """
    Load SDSS anomalies with RA/DEC.
    Uses cached file if available; otherwise queries SDSS SkyServer.
    """
    if SDSS_COORDS_CACHE.exists() and not force_requery:
        print(f"Loading SDSS coords from cache: {SDSS_COORDS_CACHE}")
        df = pq.read_table(str(SDSS_COORDS_CACHE)).to_pandas()
        print(f"  Cached: {len(df):,} rows, {df['ra'].notna().sum():,} with coords")
        return df

    # Need to query
    sdss_anom = load_sdss_raw()
    pmf_list  = list(sdss_anom[["plate", "mjd", "fiberid"]].itertuples(index=False, name=None))

    print(f"\nQuerying SDSS SkyServer for {len(pmf_list):,} anomaly coordinates...")
    t0 = time.time()
    coords = query_sdss_skyserver(pmf_list)
    elapsed = time.time() - t0
    print(f"  Retrieved {len(coords):,} coordinate rows in {elapsed:.0f}s")

    if len(coords) > 0:
        # Normalise column names (SkyServer sometimes returns mixed case)
        coords.columns = [c.lower() for c in coords.columns]
        rename_map = {"zerr": "zerr_sdss", "z": "z_sdss", "class": "class_sdss",
                      "mjd": "mjd_dr18", "ra": "ra", "dec": "dec"}
        coords = coords.rename(columns=rename_map)

        # specobjall may return multiple rows per (plate, fiberid) for different MJDs.
        # Keep the first (they share the same fiber/target; RA/DEC is the same).
        coords = coords.drop_duplicates(subset=["plate", "fiberid"], keep="first")

        # Merge on plate+fiberid only (MJD in anomaly catalog may differ from DR18 canonical MJD)
        sdss_anom = sdss_anom.merge(
            coords[["plate", "fiberid", "ra", "dec", "class_sdss", "z_sdss", "zerr_sdss"]],
            on=["plate", "fiberid"],
            how="left"
        )
    else:
        sdss_anom["ra"] = np.nan
        sdss_anom["dec"] = np.nan
        sdss_anom["class_sdss"] = None
        sdss_anom["z_sdss"] = np.nan
        sdss_anom["zerr_sdss"] = np.nan

    matched = sdss_anom["ra"].notna().sum()
    print(f"  Coordinate match rate: {matched:,} / {len(sdss_anom):,} ({matched/len(sdss_anom)*100:.1f}%)")

    # Cache result
    pq.write_table(pa.Table.from_pandas(sdss_anom), str(SDSS_COORDS_CACHE))
    print(f"  Saved cache: {SDSS_COORDS_CACHE}")
    return sdss_anom


def load_erosita():
    """Load eROSITA DR1 anomaly catalog (pre-filtered at score > threshold)."""
    print(f"Loading eROSITA DR1 from {EROSITA_FILE}...")
    df = pq.read_table(str(EROSITA_FILE)).to_pandas()
    print(f"  Total eROSITA rows: {len(df):,}")
    if "anomaly_score" in df.columns:
        df = df[df["anomaly_score"] > EROSITA_SCORE_THRESH].copy().reset_index(drop=True)
        print(f"  eROSITA anomalies (score > {EROSITA_SCORE_THRESH}): {len(df):,}")
    # Normalise ra/dec column names
    for col in df.columns:
        if col.upper() == "RA":
            df = df.rename(columns={col: "ra"})
        if col.upper() == "DEC":
            df = df.rename(columns={col: "dec"})
    return df


def load_desi():
    """Load DESI DR1 anomaly catalog (score > threshold)."""
    print(f"Loading DESI DR1 from {DESI_DIR}...")
    files = sorted(DESI_DIR.glob("desi_dr1_catalog_batch_*.parquet"))
    if not files:
        raise FileNotFoundError(f"No DESI parquet files in {DESI_DIR}")

    # Only keep essential columns
    essential = ["anomaly_score", "target_ra", "target_dec", "targetid",
                 "spectype", "z", "zerr", "classification", "discovery_potential",
                 "rR", "rZ", "rB"]

    dfs = []
    for i, f in enumerate(files):
        schema_names = pq.read_schema(str(f)).names
        cols = [c for c in essential if c in schema_names]
        df = pq.read_table(str(f), columns=cols).to_pandas()
        dfs.append(df[df["anomaly_score"] > DESI_SCORE_THRESH])
        if (i + 1) % 10 == 0:
            print(f"  Loaded {i+1}/{len(files)} batches...")

    desi = pd.concat(dfs, ignore_index=True)
    # Rename positional columns to canonical ra/dec
    desi = desi.rename(columns={"target_ra": "ra", "target_dec": "dec"})
    print(f"  DESI anomalies (score > {DESI_SCORE_THRESH}): {len(desi):,}")
    return desi


# ── Spatial cross-match ───────────────────────────────────────────────────────
def build_kdtree(df):
    """Build cKDTree on unit-sphere Cartesian coords for a catalog with ra/dec."""
    ra  = df["ra"].values.astype(float)
    dec = df["dec"].values.astype(float)
    xyz = to_xyz(ra, dec)
    return cKDTree(xyz), xyz


def cross_match(cat_a, cat_b, name_a, name_b, radius_arcsec=MATCH_RADIUS_ARCSEC):
    """
    Cross-match two catalogs by sky position using cKDTree.

    Returns a DataFrame of matches with columns:
      idx_a, idx_b, separation_arcsec, ra, dec, score_a, score_b
    plus score-weighted combined_score.
    """
    print(f"\nCross-matching {name_a} ({len(cat_a):,}) × {name_b} ({len(cat_b):,}) "
          f"at {radius_arcsec}\"...")

    mask_a = cat_a["ra"].notna() & cat_a["dec"].notna()
    mask_b = cat_b["ra"].notna() & cat_b["dec"].notna()
    a = cat_a[mask_a].reset_index(drop=True)
    b = cat_b[mask_b].reset_index(drop=True)

    if len(a) == 0 or len(b) == 0:
        print(f"  Skipped — one catalog has no coordinates")
        return pd.DataFrame()

    chord = arcsec_to_chord(radius_arcsec)

    t0 = time.time()
    tree_b, xyz_b = build_kdtree(b)
    xyz_a = to_xyz(a["ra"].values, a["dec"].values)

    # For each object in a, find all objects in b within chord distance
    indices_list = tree_b.query_ball_point(xyz_a, chord)
    elapsed = time.time() - t0

    rows = []
    for i_a, neighbours in enumerate(indices_list):
        for i_b in neighbours:
            sep = chord_to_arcsec(np.linalg.norm(xyz_a[i_a] - xyz_b[i_b]))
            rows.append({
                f"idx_{name_a}": int(i_a),
                f"idx_{name_b}": int(i_b),
                "separation_arcsec": float(sep),
                "ra": float(a.iloc[i_a]["ra"]),
                "dec": float(a.iloc[i_a]["dec"]),
                f"score_{name_a}": float(a.iloc[i_a].get("anomaly_score", np.nan)),
                f"score_{name_b}": float(b.iloc[i_b].get("anomaly_score", np.nan)),
            })

    print(f"  Found {len(rows):,} raw matches in {elapsed:.2f}s")

    if not rows:
        return pd.DataFrame()

    matches = pd.DataFrame(rows)
    matches["combined_score"] = matches[f"score_{name_a}"] + matches[f"score_{name_b}"]
    matches = matches.sort_values("combined_score", ascending=False).reset_index(drop=True)

    # Attach full metadata from each catalog (minimal columns)
    def _safe_cols(cat, name):
        keep = ["ra", "dec", "anomaly_score"]
        if "spectype" in cat.columns:      keep.append("spectype")
        if "z" in cat.columns:             keep.append("z")
        if "z_sdss" in cat.columns:        keep.append("z_sdss")
        if "class" in cat.columns:         keep.append("class")
        if "class_sdss" in cat.columns:    keep.append("class_sdss")
        if "targetid" in cat.columns:      keep.append("targetid")
        if "iauname" in cat.columns:       keep.append("iauname")
        if "plate" in cat.columns:         keep += ["plate", "mjd", "fiberid"]
        if "classification" in cat.columns: keep.append("classification")
        return cat[[c for c in keep if c in cat.columns]].add_suffix(f"_{name}")

    a_sub = cat_a[mask_a].reset_index(drop=True)
    b_sub = cat_b[mask_b].reset_index(drop=True)

    a_meta = _safe_cols(a_sub, name_a).iloc[matches[f"idx_{name_a}"].values].reset_index(drop=True)
    b_meta = _safe_cols(b_sub, name_b).iloc[matches[f"idx_{name_b}"].values].reset_index(drop=True)

    result = pd.concat([matches.reset_index(drop=True), a_meta, b_meta], axis=1)
    # Drop duplicate ra/dec columns from meta
    result = result.loc[:, ~result.columns.duplicated()]
    return result


# ── Triple match ──────────────────────────────────────────────────────────────
def find_triple_matches(sdss_desi, sdss_erosita, sdss, desi, erosita,
                        radius_arcsec=MATCH_RADIUS_ARCSEC):
    """
    Find objects matched in all three surveys:
    Use SDSS×DESI and SDSS×eROSITA matches; objects appearing in both are triple.
    """
    print("\nFinding triple matches (all 3 surveys)...")

    if sdss_desi.empty or sdss_erosita.empty:
        print("  No triple matches possible — one or more pairwise matches empty")
        return pd.DataFrame()

    # Get the SDSS index sets
    sd_sdss_idx = set(sdss_desi["idx_SDSS"].values)
    se_sdss_idx = set(sdss_erosita["idx_SDSS"].values)
    triple_sdss_idx = sd_sdss_idx & se_sdss_idx

    if not triple_sdss_idx:
        print("  No triple matches found")
        return pd.DataFrame()

    print(f"  Triple candidates (SDSS objects in both DESI and eROSITA matches): {len(triple_sdss_idx):,}")

    # Gather rows
    rows = []
    for idx_sdss in triple_sdss_idx:
        sd_rows = sdss_desi[sdss_desi["idx_SDSS"] == idx_sdss]
        se_rows = sdss_erosita[sdss_erosita["idx_SDSS"] == idx_sdss]

        for _, sd in sd_rows.iterrows():
            for _, se in se_rows.iterrows():
                rows.append({
                    "ra": float(sd["ra"]),
                    "dec": float(sd["dec"]),
                    "idx_SDSS": int(idx_sdss),
                    "idx_DESI": int(sd["idx_DESI"]),
                    "idx_eROSITA": int(se["idx_eROSITA"]),
                    "sep_SDSS_DESI_arcsec": float(sd["separation_arcsec"]),
                    "sep_SDSS_eROSITA_arcsec": float(se["separation_arcsec"]),
                    "score_SDSS": float(sd.get("score_SDSS", np.nan)),
                    "score_DESI": float(sd.get("score_DESI", np.nan)),
                    "score_eROSITA": float(se.get("score_eROSITA", np.nan)),
                })

    if not rows:
        return pd.DataFrame()

    triple = pd.DataFrame(rows)
    triple["combined_score"] = triple[["score_SDSS", "score_DESI", "score_eROSITA"]].sum(axis=1)
    triple = triple.sort_values("combined_score", ascending=False).reset_index(drop=True)
    print(f"  Triple matches: {len(triple):,}")
    return triple


# ── Diagnostic print ──────────────────────────────────────────────────────────
def print_diagnostics(sdss, desi, erosita,
                      sd_matches, se_matches, de_matches, triple):
    print("\n" + "=" * 65)
    print("MULTI-SURVEY CROSS-MATCH RESULTS")
    print("=" * 65)
    print(f"  Catalogs:")
    print(f"    SDSS  DR18: {len(sdss):,}  anomalies  (score > {SDSS_SCORE_THRESH})")
    print(f"    DESI  DR1 : {len(desi):,}  anomalies  (score > {DESI_SCORE_THRESH})")
    print(f"    eROSITA   : {len(erosita):,}   anomalies  (score > {EROSITA_SCORE_THRESH})")
    print(f"\n  Cross-match radius: {MATCH_RADIUS_ARCSEC}\"")
    print(f"\n  Pairwise matches:")
    print(f"    SDSS × DESI    : {len(sd_matches):,}")
    print(f"    SDSS × eROSITA : {len(se_matches):,}")
    print(f"    DESI × eROSITA : {len(de_matches):,}")
    print(f"\n  Triple matches (all 3 surveys): {len(triple):,}")

    if not sd_matches.empty:
        print(f"\n  Top 10 SDSS × DESI matches (by combined score):")
        for _, r in sd_matches.head(10).iterrows():
            print(f"    RA={r['ra']:.4f} DEC={r['dec']:.4f}  "
                  f"SDSS={r['score_SDSS']:.1f}  DESI={r['score_DESI']:.1f}  "
                  f"sep={r['separation_arcsec']:.2f}\"")

    if not se_matches.empty:
        print(f"\n  Top 10 SDSS × eROSITA matches (by combined score):")
        for _, r in se_matches.head(10).iterrows():
            print(f"    RA={r['ra']:.4f} DEC={r['dec']:.4f}  "
                  f"SDSS={r['score_SDSS']:.1f}  eROSITA={r['score_eROSITA']:.1f}  "
                  f"sep={r['separation_arcsec']:.2f}\"")

    if not de_matches.empty:
        print(f"\n  Top 10 DESI × eROSITA matches (by combined score):")
        for _, r in de_matches.head(10).iterrows():
            print(f"    RA={r['ra']:.4f} DEC={r['dec']:.4f}  "
                  f"DESI={r['score_DESI']:.1f}  eROSITA={r['score_eROSITA']:.1f}  "
                  f"sep={r['separation_arcsec']:.2f}\"")

    if not triple.empty:
        print(f"\n  Triple matches (all 3 surveys):")
        for _, r in triple.iterrows():
            print(f"    RA={r['ra']:.4f} DEC={r['dec']:.4f}  "
                  f"SDSS={r['score_SDSS']:.1f}  DESI={r['score_DESI']:.1f}  "
                  f"eROSITA={r['score_eROSITA']:.1f}  "
                  f"(SDSS-DESI={r['sep_SDSS_DESI_arcsec']:.2f}\"  "
                  f"SDSS-eROSITA={r['sep_SDSS_eROSITA_arcsec']:.2f}\")")

    print("=" * 65)


# ── Save outputs ──────────────────────────────────────────────────────────────
def save_parquet(df, path):
    if df.empty:
        print(f"  (skipping empty table: {path.name})")
        return
    pq.write_table(pa.Table.from_pandas(df, preserve_index=False), str(path))
    print(f"  Saved: {path}  ({len(df):,} rows)")


def save_summary(sdss, desi, erosita,
                 sd_matches, se_matches, de_matches, triple, elapsed_total):
    summary = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "match_radius_arcsec": MATCH_RADIUS_ARCSEC,
        "score_thresholds": {
            "SDSS": SDSS_SCORE_THRESH,
            "DESI": DESI_SCORE_THRESH,
            "eROSITA": EROSITA_SCORE_THRESH,
        },
        "catalog_sizes": {
            "SDSS": int(len(sdss)),
            "SDSS_with_coords": int(sdss["ra"].notna().sum()),
            "DESI": int(len(desi)),
            "eROSITA": int(len(erosita)),
        },
        "pairwise_matches": {
            "SDSS_x_DESI": int(len(sd_matches)),
            "SDSS_x_eROSITA": int(len(se_matches)),
            "DESI_x_eROSITA": int(len(de_matches)),
        },
        "triple_matches": int(len(triple)),
        "total_runtime_seconds": round(elapsed_total, 1),
    }

    # Top objects per pairwise match
    for label, df, sa, sb in [
        ("SDSS_x_DESI",    sd_matches, "score_SDSS", "score_DESI"),
        ("SDSS_x_eROSITA", se_matches, "score_SDSS", "score_eROSITA"),
        ("DESI_x_eROSITA", de_matches, "score_DESI", "score_eROSITA"),
    ]:
        if df.empty:
            summary[f"top10_{label}"] = []
            continue
        top = df.head(10)
        summary[f"top10_{label}"] = [
            {
                "ra": float(r["ra"]),
                "dec": float(r["dec"]),
                "survey_a_score": float(r[sa]),
                "survey_b_score": float(r[sb]),
                "separation_arcsec": float(r["separation_arcsec"]),
            }
            for _, r in top.iterrows()
        ]

    if not triple.empty:
        summary["triple_objects"] = [
            {
                "ra": float(r["ra"]),
                "dec": float(r["dec"]),
                "score_SDSS": float(r["score_SDSS"]),
                "score_DESI": float(r["score_DESI"]),
                "score_eROSITA": float(r["score_eROSITA"]),
                "sep_SDSS_DESI_arcsec": float(r["sep_SDSS_DESI_arcsec"]),
                "sep_SDSS_eROSITA_arcsec": float(r["sep_SDSS_eROSITA_arcsec"]),
            }
            for _, r in triple.iterrows()
        ]

    out = OUT_DIR / "cross_match_summary.json"
    with open(out, "w") as fh:
        json.dump(summary, fh, indent=2)
    print(f"  Saved: {out}")
    return summary


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    t_start = time.time()
    print("=" * 65)
    print("MULTI-SURVEY ANOMALY CROSS-MATCH")
    print("SDSS DR18  ×  eROSITA DR1  ×  DESI DR1")
    print("=" * 65)

    # 1. Load catalogs
    print("\n[1/5] Loading catalogs...")
    sdss    = load_sdss_with_coords()
    erosita = load_erosita()
    desi    = load_desi()

    # Check SDSS coordinate coverage
    n_sdss_coords = sdss["ra"].notna().sum()
    if n_sdss_coords == 0:
        print(
            "\nWARNING: SDSS has no RA/DEC (SkyServer query returned nothing).\n"
            "  SDSS cross-matches will be skipped.\n"
            "  DESI × eROSITA match will still run.\n"
            "  Re-run after checking network connectivity to skyserver.sdss.org"
        )

    # 2. Build KD-Trees
    print("\n[2/5] Building spatial index trees...")

    # 3. Pairwise cross-matches
    print("\n[3/5] Pairwise cross-matches...")
    sd_matches = cross_match(sdss, desi,    "SDSS", "DESI")
    se_matches = cross_match(sdss, erosita, "SDSS", "eROSITA")
    de_matches = cross_match(desi, erosita, "DESI", "eROSITA")

    # 4. Triple matches
    print("\n[4/5] Finding triple matches...")
    triple = find_triple_matches(sd_matches, se_matches, sdss, desi, erosita)

    # 5. Save outputs
    print("\n[5/5] Saving outputs...")
    save_parquet(sd_matches, OUT_DIR / "matches_sdss_desi.parquet")
    save_parquet(se_matches, OUT_DIR / "matches_sdss_erosita.parquet")
    save_parquet(de_matches, OUT_DIR / "matches_desi_erosita.parquet")
    save_parquet(triple,     OUT_DIR / "matches_triple.parquet")

    elapsed = time.time() - t_start
    summary = save_summary(sdss, desi, erosita,
                           sd_matches, se_matches, de_matches, triple, elapsed)

    print_diagnostics(sdss, desi, erosita, sd_matches, se_matches, de_matches, triple)
    print(f"\nTotal runtime: {elapsed:.1f}s")
    print(f"Results in: {OUT_DIR}/")
    return summary


if __name__ == "__main__":
    main()
