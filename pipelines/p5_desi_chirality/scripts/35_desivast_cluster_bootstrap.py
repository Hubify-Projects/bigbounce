#!/usr/bin/env python3
"""DP5-10: cluster-aware uncertainty for the primary DESIVAST contrast.

The manuscript's primary estimand is

    Delta f_CW = f_CW(non-void, footprint restricted) - f_CW(void)

on the exact k-unbounded union-of-holes membership.  The published counting
interval treats galaxies as independent.  This script instead resamples whole
DESIVAST maximal-void neighbourhoods, so galaxies sharing a large-scale void
region move together.

The original 1.2 GB matched-row parquet is not materialized on this machine.
The script therefore rebuilds the exact low-z parent from the raw DESI zall
FITS and P4 parquet.  Crucially, it applies the original scripts/03 global
nearest-match de-duplication over *all* quality-cut redshifts before selecting
z <= 0.24.  A low-z-only de-duplication is not equivalent.  The rebuild must
match every published primary integer count or the script aborts.

Resampling unit
---------------
Each primary-sample galaxy is assigned to its nearest published DESIVAST
VoidFinder MAXIMALS centre (NGC/SGC VOID ids are namespaced).  These 3-D
nearest-maximal regions form a deterministic void-centred Voronoi partition of
the same footprint for both arms.  A pairs cluster bootstrap samples these
maximal-void neighbourhoods with replacement and recomputes the pooled
two-arm contrast.  A delete-one-cluster jackknife is also reported as a check.

Run:
  nice -n 5 python3 pipelines/p5_desi_chirality/scripts/35_desivast_cluster_bootstrap.py

The JSON intentionally omits wall-clock timestamps and measured runtime so a
fixed-seed rerun is byte deterministic.  Runtime is printed and recorded in
the accompanying compute report.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


P5 = Path(__file__).resolve().parents[1]
REPO = P5.parents[1]
DESI_FITS = P5 / "data/desi_zall.fits"
P4_PARQUET = P5 / "data/p4_chirality.parquet"
DESIVAST = P5 / "data/desivast"
CACHE = P5 / "outputs/35_exact_primary_rows_cache.parquet"
STABLE_CACHE = P5 / "outputs/35_stable_tiebreak_primary_rows_cache.parquet"
DEFAULT_OUT = P5 / "outputs/35_desivast_cluster_bootstrap.json"

H0 = 67.66
OM0 = 0.315
LITTLE_H = 0.6766
Z_MAX_MATCH = 4.0
Z_MAX_PRIMARY = 0.24
MATCH_RADIUS_ARCSEC = 1.0
NSIDE = 64
DEFAULT_SEED = 20260714
DEFAULT_N_RESAMPLES = 20_000
CHUNK_ROWS = 750_000

EXPECTED = {
    "desi_quality_rows": 16_361_731,
    "matched_within_1arcsec": 2_349_908,
    "matched_global_deduped": 2_232_212,
    "primary_lowz_cwccw": 678_945,
    "holes": 101_863,
    "maximal_voids": 3_765,
    "footprint_pixels": 5_075,
    "void_n": 57_081,
    "void_cw": 28_339,
    "nonvoid_footprint_n": 253_276,
    "nonvoid_footprint_cw": 126_202,
}


def log(t0: float, message: str) -> None:
    print(f"[{time.perf_counter() - t0:8.1f}s] {message}", flush=True)


def sha256_file(path: Path, chunk_bytes: int = 16 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(chunk_bytes):
            digest.update(block)
    return digest.hexdigest()


def assert_equal(label: str, observed: int, expected: int) -> None:
    if int(observed) != int(expected):
        raise RuntimeError(
            f"validation failed for {label}: observed {observed:,}, "
            f"expected {expected:,}; refusing to compute DP5-10"
        )


def canonical_sample_hash(frame: pd.DataFrame) -> str:
    """Hash scientific row content, independent of parquet metadata."""
    ordered = frame.sort_values(
        ["desi_targetid", "match_dr8_id", "sep_arcsec"], kind="mergesort"
    )
    digest = hashlib.sha256()
    for column, dtype in [
        ("desi_targetid", "<i8"),
        ("desi_ra", "<f8"),
        ("desi_dec", "<f8"),
        ("desi_z", "<f8"),
        ("sep_arcsec", "<f8"),
    ]:
        values = np.ascontiguousarray(ordered[column].to_numpy().astype(dtype))
        digest.update(column.encode("ascii"))
        digest.update(values.view(np.uint8))
    digest.update(b"match_dr8_id:utf8-length-prefixed")
    for value in ordered["match_dr8_id"].astype(str):
        encoded = value.encode("utf-8")
        digest.update(len(encoded).to_bytes(4, "little"))
        digest.update(encoded)
    labels = np.ascontiguousarray((ordered["match_class_eq"] == "CW").to_numpy(np.uint8))
    digest.update(b"match_class_eq:CW=1")
    digest.update(labels.view(np.uint8))
    return digest.hexdigest()


def rebuild_exact_primary(
    t0: float, force: bool = False
) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Reproduce scripts/03 global de-duplication, then select z<=0.24 CW/CCW."""
    required = {
        "desi_targetid", "desi_ra", "desi_dec", "desi_z",
        "match_class_eq", "match_dr8_id", "sep_arcsec",
    }
    if CACHE.exists() and STABLE_CACHE.exists() and not force:
        frame = pd.read_parquet(CACHE)
        stable_frame = pd.read_parquet(STABLE_CACHE)
        missing = required.difference(frame.columns)
        if missing:
            raise RuntimeError(f"cache missing columns: {sorted(missing)}")
        stable_missing = required.difference(stable_frame.columns)
        if stable_missing:
            raise RuntimeError(f"stable cache missing columns: {sorted(stable_missing)}")
        assert_equal("cached primary rows", len(frame), EXPECTED["primary_lowz_cwccw"])
        log(
            t0,
            f"loaded exact-parent caches: historical {len(frame):,}; "
            f"stable-first {len(stable_frame):,}",
        )
        return frame, stable_frame, {
            "source": "raw rebuild using scripts/03 global-deduplication semantics",
            "desi_quality_rows": EXPECTED["desi_quality_rows"],
            "matched_within_1arcsec": EXPECTED["matched_within_1arcsec"],
            "matched_global_deduped": EXPECTED["matched_global_deduped"],
        }

    from astropy.coordinates import SkyCoord
    from astropy.io import fits
    import astropy.units as u

    log(t0, "loading P4 coordinates/classes")
    p4 = pd.read_parquet(P4_PARQUET, columns=["dr8_id", "ra", "dec", "class_eq"])
    if p4["dr8_id"].nunique() != len(p4):
        raise RuntimeError("P4 dr8_id is not unique; row-index de-duplication is invalid")
    p4_coord = SkyCoord(
        ra=p4["ra"].to_numpy(np.float64) * u.deg,
        dec=p4["dec"].to_numpy(np.float64) * u.deg,
    )
    # Preserve every accepted row in original FITS order.  scripts/03 performs
    # pandas' default (quicksort) sort_values on all accepted rows before
    # drop_duplicates.  Repeat coadds can have bit-identical sky coordinates
    # and therefore tied separations; a streaming "first minimum" reduction is
    # not equivalent to that historical tie behaviour and changes 22 low-z
    # winners on this catalog.  Retaining the 2.35M accepted rows is modest and
    # reproduces the released parent exactly.
    accepted_parts: dict[str, list[np.ndarray]] = {
        key: [] for key in [
            "p4_index", "sep_arcsec", "desi_targetid", "desi_ra",
            "desi_dec", "desi_z",
        ]
    }
    n_quality = 0
    n_matched = 0

    log(t0, "streaming full DESI catalog for global nearest-match de-duplication")
    with fits.open(DESI_FITS, memmap=True) as hdul:
        data = hdul["ZCATALOG"].data
        n_raw = len(data)
        for start in range(0, n_raw, CHUNK_ROWS):
            stop = min(start + CHUNK_ROWS, n_raw)
            block = data[start:stop]
            z = np.asarray(block["Z"], dtype=np.float64)
            zwarn = np.asarray(block["ZWARN"])
            spectype = np.char.strip(np.asarray(block["SPECTYPE"]).astype("U"))
            keep = (
                (zwarn == 0)
                & (z >= 0.0)
                & (z <= Z_MAX_MATCH)
                & np.isin(spectype, ["GALAXY", "QSO"])
            )
            local = np.flatnonzero(keep)
            n_quality += len(local)
            if not len(local):
                continue
            coord = SkyCoord(
                ra=np.asarray(block["TARGET_RA"])[local].astype(np.float64) * u.deg,
                dec=np.asarray(block["TARGET_DEC"])[local].astype(np.float64) * u.deg,
            )
            p4_index, sep, _ = coord.match_to_catalog_sky(p4_coord)
            sep_arcsec = sep.arcsec
            accepted = sep_arcsec <= MATCH_RADIUS_ARCSEC
            n_matched += int(accepted.sum())
            if accepted.any():
                candidate_p4 = np.asarray(p4_index[accepted], dtype=np.int64)
                candidate_sep = np.asarray(sep_arcsec[accepted], dtype=np.float64)
                selected_local = local[accepted]
                accepted_parts["p4_index"].append(candidate_p4)
                accepted_parts["sep_arcsec"].append(candidate_sep)
                accepted_parts["desi_targetid"].append(
                    np.asarray(block["TARGETID"])[selected_local].astype(np.int64)
                )
                accepted_parts["desi_ra"].append(
                    np.asarray(block["TARGET_RA"])[selected_local].astype(np.float64)
                )
                accepted_parts["desi_dec"].append(
                    np.asarray(block["TARGET_DEC"])[selected_local].astype(np.float64)
                )
                accepted_parts["desi_z"].append(z[selected_local])
            if stop == n_raw or (stop // CHUNK_ROWS) % 5 == 0:
                log(
                    t0,
                    f"DESI rows {stop:,}/{n_raw:,}; quality {n_quality:,}; "
                    f"1-arcsec matches {n_matched:,}",
                )

        assert_equal("DESI quality rows", n_quality, EXPECTED["desi_quality_rows"])
        assert_equal("matches within 1 arcsec", n_matched, EXPECTED["matched_within_1arcsec"])
        accepted_frame = pd.DataFrame({
            key: np.concatenate(parts) for key, parts in accepted_parts.items()
        })
        assert_equal("retained accepted rows", len(accepted_frame), n_matched)
        # This deliberately uses pandas' default quicksort, matching scripts/03.
        winners = accepted_frame.sort_values("sep_arcsec", ascending=True).drop_duplicates(
            subset=["p4_index"], keep="first"
        )
        assert_equal("global deduped matches", len(winners), EXPECTED["matched_global_deduped"])
        stable_winners = accepted_frame.sort_values(
            "sep_arcsec", ascending=True, kind="mergesort"
        ).drop_duplicates(subset=["p4_index"], keep="first")
        assert_equal(
            "stable global deduped matches",
            len(stable_winners),
            EXPECTED["matched_global_deduped"],
        )

        def materialize_primary(winner_rows: pd.DataFrame) -> pd.DataFrame:
            winner_rows = winner_rows.copy()
            winner_p4 = winner_rows["p4_index"].to_numpy(np.int64)
            winner_rows["match_class_eq"] = (
                p4["class_eq"].to_numpy()[winner_p4].astype(str)
            )
            winner_rows["match_dr8_id"] = (
                p4["dr8_id"].to_numpy()[winner_p4].astype(str)
            )
            return winner_rows[
                (winner_rows["desi_z"] <= Z_MAX_PRIMARY)
                & winner_rows["match_class_eq"].isin(["CW", "CCW"])
            ][[
                "desi_targetid", "desi_ra", "desi_dec", "desi_z",
                "match_class_eq", "match_dr8_id", "sep_arcsec",
            ]].copy()

        frame = materialize_primary(winners)
        stable_frame = materialize_primary(stable_winners)
        assert_equal("low-z CW/CCW parent", len(frame), EXPECTED["primary_lowz_cwccw"])

    # dr8_id is a source identifier, not a number (some ids contain an
    # underscore, e.g. ``371623_1242``); preserve its exact UTF-8 spelling.
    frame["match_dr8_id"] = frame["match_dr8_id"].astype(str)
    stable_frame["match_dr8_id"] = stable_frame["match_dr8_id"].astype(str)
    frame = frame.sort_values(
        ["desi_targetid", "match_dr8_id", "sep_arcsec"], kind="mergesort"
    ).reset_index(drop=True)
    stable_frame = stable_frame.sort_values(
        ["desi_targetid", "match_dr8_id", "sep_arcsec"], kind="mergesort"
    ).reset_index(drop=True)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    frame.to_parquet(CACHE, index=False)
    stable_frame.to_parquet(STABLE_CACHE, index=False)
    log(t0, f"wrote derived exact-parent cache: {CACHE.name}")
    log(t0, f"wrote stable-tiebreak sensitivity cache: {STABLE_CACHE.name}")
    return frame, stable_frame, {
        "source": "raw rebuild using scripts/03 global-deduplication semantics",
        "desi_quality_rows": n_quality,
        "matched_within_1arcsec": n_matched,
        "matched_global_deduped": len(winners),
    }


def load_void_geometry() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return holes, maximals, and namespaced cluster ids."""
    from astropy.io import fits

    holes_parts: list[np.ndarray] = []
    maximal_parts: list[np.ndarray] = []
    maximal_ids: list[np.ndarray] = []
    offset = 0
    for cap in ["NGC", "SGC"]:
        path = DESIVAST / f"DESIVAST_BGS_VOLLIM_VoidFinder_{cap}.fits"
        with fits.open(path, memmap=True) as hdul:
            holes = hdul["HOLES"].data
            maximals = hdul["MAXIMALS"].data
            holes_parts.append(np.column_stack([
                holes["X"], holes["Y"], holes["Z"], holes["RADIUS"],
            ]).astype(np.float64))
            maximal_parts.append(np.column_stack([
                maximals["X"], maximals["Y"], maximals["Z"], maximals["R_EFF"],
            ]).astype(np.float64))
            void_id = np.asarray(maximals["VOID"], dtype=np.int64)
            expected_ids = np.arange(len(maximals), dtype=np.int64)
            if not np.array_equal(void_id, expected_ids):
                raise RuntimeError(f"{cap} MAXIMALS VOID ids are not contiguous")
            maximal_ids.append(void_id + offset)
            offset += len(maximals)
    return np.vstack(holes_parts), np.vstack(maximal_parts), np.concatenate(maximal_ids)


def galaxy_xyz(frame: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    from astropy.cosmology import FlatLambdaCDM

    cosmo = FlatLambdaCDM(H0=H0, Om0=OM0)
    chi = cosmo.comoving_distance(frame["desi_z"].to_numpy(np.float64)).value * LITTLE_H
    ra = np.deg2rad(frame["desi_ra"].to_numpy(np.float64))
    dec = np.deg2rad(frame["desi_dec"].to_numpy(np.float64))
    xyz = np.column_stack([
        chi * np.cos(dec) * np.cos(ra),
        chi * np.cos(dec) * np.sin(ra),
        chi * np.sin(dec),
    ])
    return xyz, chi


def exact_union_membership(gal_xyz: np.ndarray, holes: np.ndarray) -> np.ndarray:
    """Exact k-unbounded point-in-any-hole membership."""
    from scipy.spatial import cKDTree

    tree = cKDTree(gal_xyz)
    member = np.zeros(len(gal_xyz), dtype=bool)
    for indices in tree.query_ball_point(holes[:, :3], r=holes[:, 3]):
        member[indices] = True
    return member


def footprint_mask(frame: pd.DataFrame, chi: np.ndarray, holes: np.ndarray) -> tuple[np.ndarray, dict]:
    """Reproduce artifact 29's NSIDE=64 angular-disc union + radial span."""
    import healpy as hp

    radius_from_origin = np.linalg.norm(holes[:, :3], axis=1)
    direction = holes[:, :3] / radius_from_origin[:, None]
    angular_radius = np.arcsin(np.clip(holes[:, 3] / radius_from_origin, 0.0, 1.0))
    pixels = np.zeros(hp.nside2npix(NSIDE), dtype=bool)
    for vector, radius in zip(direction, angular_radius):
        pixels[hp.query_disc(NSIDE, vector, radius, inclusive=True)] = True
    assert_equal("footprint pixel count", pixels.sum(), EXPECTED["footprint_pixels"])
    theta = np.deg2rad(90.0 - frame["desi_dec"].to_numpy(np.float64))
    phi = np.deg2rad(np.mod(frame["desi_ra"].to_numpy(np.float64), 360.0))
    galaxy_pixel = hp.ang2pix(NSIDE, theta, phi)
    radial_min = float(np.min(radius_from_origin - holes[:, 3]))
    radial_max = float(np.max(radius_from_origin + holes[:, 3]))
    inside = pixels[galaxy_pixel] & (chi >= radial_min) & (chi <= radial_max)
    return inside, {
        "nside": NSIDE,
        "pixels": int(pixels.sum()),
        "f_sky": float(pixels.mean()),
        "radial_span_mpc_h": [radial_min, radial_max],
    }


def cluster_aggregates(
    xyz: np.ndarray,
    maximals: np.ndarray,
    cluster_ids: np.ndarray,
    void: np.ndarray,
    footprint: np.ndarray,
    cw: np.ndarray,
) -> tuple[pd.DataFrame, np.ndarray]:
    """Aggregate both arms over nearest-maximal-void Voronoi regions."""
    from scipy.spatial import cKDTree

    primary = void | ((~void) & footprint)
    _, nearest = cKDTree(maximals[:, :3]).query(xyz[primary], k=1)
    assignment = cluster_ids[nearest]
    selected_void = void[primary]
    selected_cw = cw[primary]
    table = pd.DataFrame({
        "cluster": assignment,
        "void_n": selected_void.astype(np.int64),
        "void_cw": (selected_void & selected_cw).astype(np.int64),
        "nonvoid_n": (~selected_void).astype(np.int64),
        "nonvoid_cw": ((~selected_void) & selected_cw).astype(np.int64),
    }).groupby("cluster", sort=True, as_index=False).sum()
    return table, primary


def contrast(kn: np.ndarray | float, nn: np.ndarray | float,
             kv: np.ndarray | float, nv: np.ndarray | float) -> np.ndarray | float:
    return kn / nn - kv / nv


def cluster_bootstrap(
    table: pd.DataFrame, n_resamples: int, seed: int
) -> tuple[np.ndarray, dict]:
    rng = np.random.default_rng(seed)
    cols = ["void_n", "void_cw", "nonvoid_n", "nonvoid_cw"]
    counts = table[cols].to_numpy(np.int64)
    n_clusters = len(counts)
    draws = np.empty(n_resamples, dtype=np.float64)
    batch = 256
    for start in range(0, n_resamples, batch):
        stop = min(start + batch, n_resamples)
        sampled = rng.integers(0, n_clusters, size=(stop - start, n_clusters))
        total = counts[sampled].sum(axis=1)
        draws[start:stop] = contrast(total[:, 3], total[:, 2], total[:, 1], total[:, 0])
    observed_total = counts.sum(axis=0)
    observed = float(contrast(observed_total[3], observed_total[2],
                              observed_total[1], observed_total[0]))
    return draws, {
        "observed": observed,
        "se": float(draws.std(ddof=1)),
        "mean": float(draws.mean()),
        "bias": float(draws.mean() - observed),
        "ci95_percentile": [float(x) for x in np.quantile(draws, [0.025, 0.975])],
        "probability_delta_le_zero": float(np.mean(draws <= 0.0)),
    }


def jackknife(table: pd.DataFrame) -> dict:
    counts = table[["void_n", "void_cw", "nonvoid_n", "nonvoid_cw"]].to_numpy(np.float64)
    total = counts.sum(axis=0)
    loo = total[None, :] - counts
    theta = contrast(loo[:, 3], loo[:, 2], loo[:, 1], loo[:, 0])
    mean = float(theta.mean())
    g = len(theta)
    se = float(np.sqrt((g - 1.0) / g * np.sum((theta - mean) ** 2)))
    observed = float(contrast(total[3], total[2], total[1], total[0]))
    return {
        "n_delete_one_clusters": g,
        "observed": observed,
        "se": se,
        "normal_ci95": [observed - 1.959963984540054 * se,
                        observed + 1.959963984540054 * se],
    }


def binomial_comparison(nv: int, kv: int, nn: int, kn: int) -> dict:
    pv = kv / nv
    pn = kn / nn
    delta = pn - pv
    se = math.sqrt(pv * (1.0 - pv) / nv + pn * (1.0 - pn) / nn)
    pooled = (kv + kn) / (nv + nn)
    se_pooled = math.sqrt(pooled * (1.0 - pooled) * (1.0 / nv + 1.0 / nn))
    z = delta / se_pooled
    return {
        "assumption": "independent Bernoulli galaxies (counting statistics only)",
        "delta": delta,
        "se_unpooled": se,
        "normal_ci95": [delta - 1.959963984540054 * se,
                        delta + 1.959963984540054 * se],
        "pooled_two_proportion_z": z,
        "p_two_sided": float(2.0 * stats.norm.sf(abs(z))),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--n-resamples", type=int, default=DEFAULT_N_RESAMPLES)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--force-rebuild", action="store_true")
    args = parser.parse_args()
    if args.n_resamples < 1_000:
        raise ValueError("use at least 1,000 resamples for the reported percentile CI")
    t0 = time.perf_counter()

    for path in [DESI_FITS, P4_PARQUET]:
        if not path.exists():
            raise FileNotFoundError(path)
    frame, stable_frame, rebuild = rebuild_exact_primary(t0, force=args.force_rebuild)
    sample_hash = canonical_sample_hash(frame)
    stable_sample_hash = canonical_sample_hash(stable_frame)
    holes, maximals, cluster_ids = load_void_geometry()
    assert_equal("hole count", len(holes), EXPECTED["holes"])
    assert_equal("maximal void count", len(maximals), EXPECTED["maximal_voids"])
    xyz, chi = galaxy_xyz(frame)
    cw = (frame["match_class_eq"] == "CW").to_numpy()
    log(t0, "computing exact k-unbounded union-of-holes membership")
    void = exact_union_membership(xyz, holes)
    in_footprint, footprint_meta = footprint_mask(frame, chi, holes)
    nonvoid = (~void) & in_footprint

    nv, kv = int(void.sum()), int(cw[void].sum())
    nn, kn = int(nonvoid.sum()), int(cw[nonvoid].sum())
    assert_equal("exact void N", nv, EXPECTED["void_n"])
    assert_equal("exact void CW", kv, EXPECTED["void_cw"])
    assert_equal("footprint nonvoid N", nn, EXPECTED["nonvoid_footprint_n"])
    assert_equal("footprint nonvoid CW", kn, EXPECTED["nonvoid_footprint_cw"])
    log(t0, f"validated primary integers: void {kv:,}/{nv:,}; nonvoid {kn:,}/{nn:,}")

    table, primary = cluster_aggregates(xyz, maximals, cluster_ids, void, in_footprint, cw)
    assert_equal("cluster-table selected N", int(primary.sum()), nv + nn)
    draws, bootstrap = cluster_bootstrap(table, args.n_resamples, args.seed)
    jack = jackknife(table)
    binom = binomial_comparison(nv, kv, nn, kn)
    cluster_sizes = (table["void_n"] + table["nonvoid_n"]).to_numpy()
    bootstrap["se_ratio_to_binomial"] = bootstrap["se"] / binom["se_unpooled"]
    bootstrap["variance_design_effect_vs_binomial"] = (
        bootstrap["se"] / binom["se_unpooled"]
    ) ** 2

    # Historical tie-order sensitivity.  This is deliberately not substituted
    # for the released parent: it quantifies the consequence of replacing
    # pandas' unstable default quicksort with a deterministic stable-first rule.
    stable_xyz, stable_chi = galaxy_xyz(stable_frame)
    stable_cw = (stable_frame["match_class_eq"] == "CW").to_numpy()
    stable_void = exact_union_membership(stable_xyz, holes)
    stable_footprint, stable_footprint_meta = footprint_mask(
        stable_frame, stable_chi, holes
    )
    stable_nonvoid = (~stable_void) & stable_footprint
    stable_nv = int(stable_void.sum())
    stable_kv = int(stable_cw[stable_void].sum())
    stable_nn = int(stable_nonvoid.sum())
    stable_kn = int(stable_cw[stable_nonvoid].sum())
    stable_table, stable_primary = cluster_aggregates(
        stable_xyz, maximals, cluster_ids, stable_void, stable_footprint, stable_cw
    )
    assert_equal(
        "stable cluster-table selected N",
        int(stable_primary.sum()),
        stable_nv + stable_nn,
    )
    _, stable_bootstrap = cluster_bootstrap(
        stable_table, args.n_resamples, args.seed
    )
    stable_jack = jackknife(stable_table)
    stable_binom = binomial_comparison(
        stable_nv, stable_kv, stable_nn, stable_kn
    )
    historical_ids = set(frame["match_dr8_id"].astype(str))
    stable_ids = set(stable_frame["match_dr8_id"].astype(str))
    stable_bootstrap["se_ratio_to_binomial"] = (
        stable_bootstrap["se"] / stable_binom["se_unpooled"]
    )

    log(t0, "hashing material raw inputs")
    input_paths = [
        DESI_FITS,
        P4_PARQUET,
        DESIVAST / "DESIVAST_BGS_VOLLIM_VoidFinder_NGC.fits",
        DESIVAST / "DESIVAST_BGS_VOLLIM_VoidFinder_SGC.fits",
    ]
    input_hashes = {
        str(path.relative_to(REPO)): sha256_file(path) for path in input_paths
    }

    result = {
        "schema": "p5.dp5-10.desivast-cluster-bootstrap.v1",
        "script": "pipelines/p5_desi_chirality/scripts/35_desivast_cluster_bootstrap.py",
        "disposition": "DP5-10",
        "estimand": {
            "name": "primary DESIVAST footprint-restricted chirality contrast",
            "definition": "f_CW(non-void, footprint restricted) - f_CW(void)",
            "sign_convention": "positive means higher CW fraction outside voids",
            "membership": "exact k-unbounded point-in-union of all 101,863 hole spheres",
            "control": "non-void within NSIDE=64 union-of-hole angular discs and hole radial span",
        },
        "reconstruction_validation": {
            **rebuild,
            "z_match_max": Z_MAX_MATCH,
            "z_primary_max": Z_MAX_PRIMARY,
            "match_radius_arcsec": MATCH_RADIUS_ARCSEC,
            "deduplication": "global nearest separation per unique P4 dr8_id before low-z selection",
            "primary_row_count": len(frame),
            "canonical_primary_row_sha256": sample_hash,
        },
        "primary_counts": {
            "void": {"n": nv, "n_cw": kv, "f_cw": kv / nv},
            "nonvoid_footprint_restricted": {"n": nn, "n_cw": kn, "f_cw": kn / nn},
            "delta_f_cw_nonvoid_minus_void": kn / nn - kv / nv,
        },
        "cluster_unit": {
            "definition": (
                "nearest published DESIVAST VoidFinder MAXIMALS centre in 3-D comoving "
                "Mpc/h; NGC/SGC VOID ids namespaced; both arms share the same "
                "maximal-void-centred Voronoi partition"
            ),
            "available_maximal_voids": len(maximals),
            "nonempty_primary_sample_clusters": len(table),
            "cluster_size_primary_rows": {
                "min": int(cluster_sizes.min()),
                "median": float(np.median(cluster_sizes)),
                "mean": float(cluster_sizes.mean()),
                "p95": float(np.quantile(cluster_sizes, 0.95)),
                "max": int(cluster_sizes.max()),
            },
        },
        "cluster_pairs_bootstrap": {
            "seed": args.seed,
            "n_resamples": args.n_resamples,
            "resampling": "sample nonempty maximal-void clusters with replacement; recompute pooled two-arm fractions",
            **bootstrap,
        },
        "delete_one_cluster_jackknife": jack,
        "independent_binomial_comparison": binom,
        "tie_break_sensitivity": {
            "reason": (
                "repeat DESI coadds can have exactly tied angular separations. "
                "The released parent inherits pandas default quicksort tie order; "
                "a stable-first sort is deterministic but is a different parent."
            ),
            "historical_rule": "pandas sort_values(sep_arcsec) default quicksort, then first duplicate",
            "sensitivity_rule": "pandas stable mergesort by sep_arcsec, then first duplicate in FITS order",
            "recommendation": (
                "Future releases should specify a total deterministic ordering, "
                "for example (sep_arcsec, TARGETID, original_row_index), version it, "
                "and regenerate every dependent artifact together."
            ),
            "historical_primary_rows": len(frame),
            "stable_primary_rows": len(stable_frame),
            "delta_rows_stable_minus_historical": len(stable_frame) - len(frame),
            "p4_ids_only_historical": len(historical_ids - stable_ids),
            "p4_ids_only_stable": len(stable_ids - historical_ids),
            "stable_primary_row_sha256": stable_sample_hash,
            "stable_counts": {
                "void": {"n": stable_nv, "n_cw": stable_kv, "f_cw": stable_kv / stable_nv},
                "nonvoid_footprint_restricted": {
                    "n": stable_nn, "n_cw": stable_kn, "f_cw": stable_kn / stable_nn,
                },
                "delta_f_cw_nonvoid_minus_void": stable_kn / stable_nn - stable_kv / stable_nv,
            },
            "count_deltas_stable_minus_historical": {
                "void_n": stable_nv - nv,
                "void_cw": stable_kv - kv,
                "nonvoid_n": stable_nn - nn,
                "nonvoid_cw": stable_kn - kn,
            },
            "cluster_pairs_bootstrap": {
                "seed": args.seed,
                "n_resamples": args.n_resamples,
                **stable_bootstrap,
            },
            "delete_one_cluster_jackknife": stable_jack,
            "independent_binomial_comparison": stable_binom,
            "footprint": stable_footprint_meta,
            "delta_cluster_bootstrap_se_stable_minus_historical": (
                stable_bootstrap["se"] - bootstrap["se"]
            ),
            "delta_point_estimate_stable_minus_historical": (
                stable_bootstrap["observed"] - bootstrap["observed"]
            ),
        },
        "footprint": footprint_meta,
        "input_sha256": input_hashes,
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scipy": stats.__version__ if hasattr(stats, "__version__") else __import__("scipy").__version__,
        },
        "determinism": (
            "JSON contains no timestamp/runtime; fixed seed, sorted cluster ids, "
            "canonical row hash, and input hashes permit byte-identical reruns"
        ),
        "honest_scope": (
            "This quantifies sampling covariance among galaxies sharing published "
            "maximal-void neighbourhoods. It does not model classifier bias, DESI "
            "selection-function error, uncertainty in the published void catalog, "
            "or correlations extending across multiple maximal-void regions."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    log(t0, f"wrote {args.output}")
    log(
        t0,
        f"cluster bootstrap SE={bootstrap['se']:.6f}, "
        f"95% CI={bootstrap['ci95_percentile']}; "
        f"binomial SE={binom['se_unpooled']:.6f}",
    )
    print(f"RUNTIME_SECONDS={time.perf_counter() - t0:.3f}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
