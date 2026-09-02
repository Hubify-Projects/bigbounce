#!/usr/bin/env python3
"""Known-object recovery benchmark for the AUG-011 anomaly flagship catalogue
(NEXT_SCIENCE_LEDGER.md item #8).

Answers the ledger question directly: does the sealed S>5 catalogue (and the
S>8 deep sample) *recover* published classes of genuinely unusual objects at
a rate meaningfully above the base rate an untargeted cut would give? A
positional cross-match of published "unusual object" reference lists against
the flagship catalogue's TARGETIDs, restricted to the exact DESI footprint
this generation actually scanned (`sealed_2026-08-05/locator_inventory.jsonl`
converted to a HEALPix pixel set — the same nside/nested convention DESI's
own healpix coadd directory layout uses), with a binomial (Wilson score)
confidence interval on each class's recovery fraction and its enrichment
over the catalogue's own base rate (catalogue_rows / parent_unique_targetids
at that threshold). Per ledger #8's exit rule: >=1 class with recovery
enrichment > 10x and >=5 matches is a "confirmed class" signal worth writing
up; otherwise the catalogue stands as a data release.

Three independently gated stages, run in order (each fails closed rather
than silently degrading):

  1. `--fetch-references` — pull the reference "unusual object" catalogues
     from VizieR via `astroquery.vizier.Vizier` (REFERENCE_CLASSES below;
     each entry cites its source paper + best-known VizieR catalogue ID).
     Whatever cannot be fetched (no network, ID not found, service error)
     is recorded as `status: "unavailable"` with the raw exception message
     — NEVER silently dropped, NEVER a fabricated row count. Cached to
     `--reference-cache-dir` (kept OUTSIDE the repo, like every other
     phase-3 intermediate) as VOTable + a JSON checksum manifest.

  2. `--crossmatch` — positional cross-match (astropy SkyCoord, configurable
     radius, default 1.5 arcsec) of every successfully-fetched reference
     class against one or more normalized parent catalogues (a JSON
     `--catalogs-config`, one entry per catalogue: path, column names,
     detection threshold, and the DOCUMENTED parent/threshold counts this
     script itself never computes — see `catalogs_config_example.json`).
     Reference objects are first restricted to the exact scanned footprint
     (HEALPix pixel membership against the sealed locator inventory);
     recovery = (matched AND in-footprint) / (in-footprint). When both
     sides carry a redshift, a redshift-agreement flag is also computed
     (`|z_ref - z_cat| / (1 + z_ref) <= --z-tol`) but does NOT gate the
     positional match — it is reported as supporting evidence only, since
     most reference catalogues and the enrichment sample's redrock columns
     are frequently null (no redrock file downloaded in this generation).

  3. Output: `<out-dir>/recovery_benchmark.json` (full per-class, per-catalogue
     table with CIs, enrichment, and closed-loop candidate flags) and
     `<out-dir>/recovery_benchmark.md` (the same as a markdown table).

Everything downstream of `--crossmatch` is pure/offline and covered by
`pipelines/p1_highz_tracers/tests/test_recovery_benchmark.py` against
synthetic fixtures — no network, no VizieR, no live catalogues needed to
verify the matching, footprint-restriction, CI, and enrichment arithmetic
are correct.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
import traceback
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derive_locator_inventory import (  # noqa: E402
    read_json,
    require_sha,
    sha256_file,
    write_json_atomic,
)

DEFAULT_RADIUS_ARCSEC = 1.5
DEFAULT_Z_TOL = 0.05
DEFAULT_HEALPIX_NSIDE = 64  # DESI's own healpix coadd directory convention
DEFAULT_HEALPIX_NEST = True
CLOSED_LOOP_ENRICHMENT_MIN = 10.0
CLOSED_LOOP_MATCHES_MIN = 5


class BenchmarkError(RuntimeError):
    """Raised when a required input cannot be trusted or is missing."""


# ---------------------------------------------------------------------------
# 1. Reference class registry
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ReferenceClass:
    class_id: str
    name: str
    citation: str
    vizier_id: Optional[str]
    ra_col_candidates: tuple[str, ...]
    dec_col_candidates: tuple[str, ...]
    z_col_candidates: tuple[str, ...]
    notes: str


# Best-known VizieR catalogue IDs for each class, with the source paper cited
# so a human can re-verify the ID against the live VizieR catalogue-of-
# catalogues search before a real (networked) run. This environment's outbound
# access to vizier.cds.unistra.fr is TCP-reachable but the TAP/VO query layer
# returned a mid-query connection reset on every attempt made while building
# this tool (2026-09-02) -- see `--fetch-references`'s per-class `status` and
# `error` fields for the exact honest outcome of each attempt, never a
# fabricated row count. IDs marked "unverified" have not been confirmed to
# resolve from any host during this build; run --fetch-references again on a
# host with working VizieR access before trusting a "fetched" status.
REFERENCE_CLASSES: tuple[ReferenceClass, ...] = (
    ReferenceClass(
        class_id="baron_poznanski_weird",
        name="Baron & Poznanski (2017) 'weirdest' SDSS galaxies",
        citation="Baron & Poznanski 2017, MNRAS 465, 4530; arXiv:1611.07526",
        vizier_id="J/MNRAS/465/4530",
        ra_col_candidates=("RAJ2000", "RA_ICRS", "_RA.icrs"),
        dec_col_candidates=("DEJ2000", "DE_ICRS", "_DE.icrs"),
        z_col_candidates=("z", "zsp", "Z"),
        notes="Unsupervised outlier-detection list; direct methodological analog to the AUG-011 anomaly score.",
    ),
    ReferenceClass(
        class_id="bal_quasars",
        name="Broad absorption line (BAL) quasars",
        citation="Gibson et al. 2009, ApJ 692, 758 (SDSS DR5 BALQSO catalog)",
        vizier_id="J/ApJ/692/758",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=("z", "zBAL", "Z"),
        notes="Unverified VizieR ID -- confirm at query time; BAL troughs are a known non-artifact spectral anomaly source.",
    ),
    ReferenceClass(
        class_id="roma_bzcat_blazars",
        name="Roma-BZCAT blazars (5th edition)",
        citation="Massaro et al. 2015, Ap&SS 357, 75 (Roma-BZCAT 5th ed.)",
        vizier_id="VII/274",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=("z", "Z"),
        notes="All-sky blazar catalogue; featureless/highly-variable continua are a plausible high-anomaly-score class.",
    ),
    ReferenceClass(
        class_id="cv_white_dwarf_binaries",
        name="Cataclysmic variables / white-dwarf binaries",
        citation="Ritter & Kolb 2003 (7th ed. catalog of CVs)",
        vizier_id="B/cb/cb",
        ra_col_candidates=("RA1950", "RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DE1950", "DEJ2000", "DE_ICRS"),
        z_col_candidates=(),
        notes="Galactic; expected to be a LOW-recovery class relative to DESI's extragalactic-dominated footprint (sanity-check class).",
    ),
    ReferenceClass(
        class_id="carbon_stars",
        name="Carbon stars",
        citation="Downes et al. 2004, AJ 128, 3;",
        vizier_id="J/AJ/128/3",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=(),
        notes="Unverified VizieR ID -- confirm at query time. Galactic; sanity-check class like CVs.",
    ),
    ReferenceClass(
        class_id="lyman_alpha_emitters",
        name="Lyman-alpha emitters (LAEs)",
        citation="Ouchi et al. 2008, ApJS 176, 301",
        vizier_id="J/ApJS/176/301",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=("z", "zLya", "Z"),
        notes="High-z narrowband-selected LAE list; overlaps DESI's Lya forest / high-z QSO redshift range only partially (z~3-6 narrowband fields).",
    ),
    ReferenceClass(
        class_id="extreme_emission_line_galaxies",
        name="Extreme emission-line galaxies (EELGs)",
        citation="Amorin et al. 2015, A&A 578, A48",
        vizier_id="J/A+A/578/A48",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=("z", "Z"),
        notes="Extreme [OIII]/Hbeta EW galaxies; plausible high-anomaly-score class from strong emission-line residuals.",
    ),
    ReferenceClass(
        class_id="changing_look_quasars",
        name="Changing-look quasars",
        citation="MacLeod et al. 2016, ApJ 826, 188",
        vizier_id="J/ApJ/826/188",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=("z", "Z"),
        notes="Spectral-state-transition quasars; only a single-epoch spectrum overlaps DESI, so recovery is expected to be low/noisy.",
    ),
    ReferenceClass(
        class_id="superluminous_sn_hosts",
        name="Superluminous supernova (SLSN) host galaxies",
        citation="Perley et al. 2016, ApJ 830, 13",
        vizier_id="J/ApJ/830/13",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=("z", "Z"),
        notes="SLSN hosts are frequently extreme low-metallicity dwarfs -- another plausible high-residual class.",
    ),
    ReferenceClass(
        class_id="grb_hosts",
        name="Gamma-ray burst (GRB) host galaxies",
        citation="Kruhler et al. 2015, A&A 581, A125",
        vizier_id="J/A+A/581/A125",
        ra_col_candidates=("RAJ2000", "RA_ICRS"),
        dec_col_candidates=("DEJ2000", "DE_ICRS"),
        z_col_candidates=("z", "Z"),
        notes="Same low-metallicity/extreme-emission-line family as SLSN hosts.",
    ),
    ReferenceClass(
        class_id="little_red_dots",
        name="'Little red dots' (LRDs) / compact high-z red AGN candidates",
        citation="Matthee et al. 2024, ApJ 963, 129; Kokorev et al. 2024, ApJL 968, L38",
        vizier_id=None,
        ra_col_candidates=(),
        dec_col_candidates=(),
        z_col_candidates=(),
        notes="No VizieR-catalogued positional table identified as of this build (2026-09-02) -- JWST-selected, mostly outside DESI's optical spectroscopic reach. Recorded status is always 'no_catalog_id_known', never fetched.",
    ),
)


@dataclass
class FetchResult:
    class_id: str
    status: str  # "fetched" | "unavailable" | "no_catalog_id_known"
    n_rows: int
    vizier_id: Optional[str]
    cache_path: Optional[str]
    cache_sha256: Optional[str]
    ra_col: Optional[str]
    dec_col: Optional[str]
    z_col: Optional[str]
    error: Optional[str]
    fetched_at: str

    def to_json(self) -> dict[str, Any]:
        return {
            "class_id": self.class_id,
            "status": self.status,
            "n_rows": self.n_rows,
            "vizier_id": self.vizier_id,
            "cache_path": self.cache_path,
            "cache_sha256": self.cache_sha256,
            "ra_col": self.ra_col,
            "dec_col": self.dec_col,
            "z_col": self.z_col,
            "error": self.error,
            "fetched_at": self.fetched_at,
        }


def _pick_column(colnames: list[str], candidates: tuple[str, ...]) -> Optional[str]:
    lower = {c.lower(): c for c in colnames}
    for candidate in candidates:
        if candidate.lower() in lower:
            return lower[candidate.lower()]
    return None


def fetch_reference_class(
    ref: ReferenceClass, cache_dir: Path, row_limit: int, timeout_sec: float
) -> FetchResult:
    now = datetime.now(timezone.utc).isoformat()
    cache_dir.mkdir(parents=True, exist_ok=True)
    if ref.vizier_id is None:
        return FetchResult(
            class_id=ref.class_id,
            status="no_catalog_id_known",
            n_rows=0,
            vizier_id=None,
            cache_path=None,
            cache_sha256=None,
            ra_col=None,
            dec_col=None,
            z_col=None,
            error="no VizieR catalogue ID identified for this class -- see REFERENCE_CLASSES notes",
            fetched_at=now,
        )
    try:
        from astroquery.vizier import Vizier  # local import: optional dep
    except ImportError as exc:  # pragma: no cover - environment guard
        return FetchResult(
            class_id=ref.class_id,
            status="unavailable",
            n_rows=0,
            vizier_id=ref.vizier_id,
            cache_path=None,
            cache_sha256=None,
            ra_col=None,
            dec_col=None,
            z_col=None,
            error=f"astroquery not importable: {exc}",
            fetched_at=now,
        )

    vizier = Vizier(row_limit=row_limit, timeout=timeout_sec)
    try:
        catalogs = vizier.get_catalogs(ref.vizier_id)
        if not catalogs:
            raise BenchmarkError(f"VizieR returned zero tables for {ref.vizier_id}")
        table = catalogs[0]
        for candidate in catalogs[1:]:
            if len(candidate) > len(table):
                table = candidate
    except Exception as exc:  # noqa: BLE001 - record every failure mode honestly
        return FetchResult(
            class_id=ref.class_id,
            status="unavailable",
            n_rows=0,
            vizier_id=ref.vizier_id,
            cache_path=None,
            cache_sha256=None,
            ra_col=None,
            dec_col=None,
            z_col=None,
            error=f"{type(exc).__name__}: {exc}",
            fetched_at=now,
        )

    colnames = list(table.colnames)
    ra_col = _pick_column(colnames, ref.ra_col_candidates)
    dec_col = _pick_column(colnames, ref.dec_col_candidates)
    z_col = _pick_column(colnames, ref.z_col_candidates)
    if ra_col is None or dec_col is None:
        return FetchResult(
            class_id=ref.class_id,
            status="unavailable",
            n_rows=len(table),
            vizier_id=ref.vizier_id,
            cache_path=None,
            cache_sha256=None,
            ra_col=ra_col,
            dec_col=dec_col,
            z_col=z_col,
            error=f"fetched {len(table)} rows but could not identify RA/Dec columns among {colnames}",
            fetched_at=now,
        )

    cache_path = cache_dir / f"{ref.class_id}.ecsv"
    table.write(cache_path, format="ascii.ecsv", overwrite=True)
    cache_sha = sha256_file(cache_path)
    return FetchResult(
        class_id=ref.class_id,
        status="fetched",
        n_rows=len(table),
        vizier_id=ref.vizier_id,
        cache_path=str(cache_path),
        cache_sha256=cache_sha,
        ra_col=ra_col,
        dec_col=dec_col,
        z_col=z_col,
        error=None,
        fetched_at=now,
    )


def fetch_all_reference_classes(
    cache_dir: Path, row_limit: int, timeout_sec: float
) -> list[FetchResult]:
    results = []
    for ref in REFERENCE_CLASSES:
        try:
            results.append(fetch_reference_class(ref, cache_dir, row_limit, timeout_sec))
        except Exception as exc:  # noqa: BLE001 - a class failing must never abort the sweep
            results.append(
                FetchResult(
                    class_id=ref.class_id,
                    status="unavailable",
                    n_rows=0,
                    vizier_id=ref.vizier_id,
                    cache_path=None,
                    cache_sha256=None,
                    ra_col=None,
                    dec_col=None,
                    z_col=None,
                    error=f"unexpected {type(exc).__name__}: {exc}\n{traceback.format_exc(limit=2)}",
                    fetched_at=datetime.now(timezone.utc).isoformat(),
                )
            )
    return results


def write_reference_manifest(results: list[FetchResult], out_path: Path) -> None:
    payload = {
        "manifest_version": "bigbounce-recovery-benchmark-references/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "classes": [r.to_json() for r in results],
        "summary": {
            "n_classes": len(results),
            "n_fetched": sum(1 for r in results if r.status == "fetched"),
            "n_unavailable": sum(1 for r in results if r.status == "unavailable"),
            "n_no_catalog_id_known": sum(1 for r in results if r.status == "no_catalog_id_known"),
        },
    }
    write_json_atomic(out_path, payload)


# ---------------------------------------------------------------------------
# 2. Footprint restriction (HEALPix membership against the sealed locator
#    inventory -- the exact set of pixels this generation actually scanned)
# ---------------------------------------------------------------------------


def load_footprint_pixel_set(
    locator_inventory_path: Path, nside: int = DEFAULT_HEALPIX_NSIDE
) -> set[int]:
    """Read the sealed per-group locator inventory's `healpix` column.

    The inventory's `healpix` field IS already the DESI healpix pixel index
    at the survey's own nside (64, nested) -- see `derive_locator_inventory.py`
    and `coadd_relative_path()`, which builds paths directly from this same
    field. No re-derivation from ra/dec is needed for the CATALOGUE side;
    this function just collects the pixel set. `nside` is accepted for
    documentation/consistency with `restrict_to_footprint` below (both must
    agree) but is not itself used to recompute anything here.
    """
    if not locator_inventory_path.is_file():
        raise BenchmarkError(f"locator inventory is absent: {locator_inventory_path}")
    pixels: set[int] = set()
    with locator_inventory_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            pixels.add(int(row["healpix"]))
    if not pixels:
        raise BenchmarkError(f"locator inventory contained zero healpix pixels: {locator_inventory_path}")
    return pixels


def restrict_to_footprint(
    ra_deg: np.ndarray,
    dec_deg: np.ndarray,
    footprint_pixels: set[int],
    nside: int = DEFAULT_HEALPIX_NSIDE,
    nest: bool = DEFAULT_HEALPIX_NEST,
) -> np.ndarray:
    """Return a boolean mask: True where (ra, dec) falls in a scanned pixel."""
    import healpy as hp

    theta = np.radians(90.0 - np.asarray(dec_deg, dtype=float))
    phi = np.radians(np.asarray(ra_deg, dtype=float))
    pix = hp.ang2pix(nside, theta, phi, nest=nest)
    footprint_arr = np.fromiter(footprint_pixels, dtype=np.int64, count=len(footprint_pixels))
    return np.isin(pix, footprint_arr)


# ---------------------------------------------------------------------------
# 3. Parent catalogue loading + cross-match
# ---------------------------------------------------------------------------


@dataclass
class CatalogSpec:
    name: str
    path: str
    id_col: str
    ra_col: str
    dec_col: str
    score_col: str
    z_col: Optional[str]
    threshold: float
    parent_total: int
    catalog_total_at_threshold: int
    catalog_total_note: str
    is_partial_preview: bool = False

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "CatalogSpec":
        required = [
            "name",
            "path",
            "id_col",
            "ra_col",
            "dec_col",
            "score_col",
            "threshold",
            "parent_total",
            "catalog_total_at_threshold",
            "catalog_total_note",
        ]
        missing = [k for k in required if k not in payload]
        if missing:
            raise BenchmarkError(f"catalogs-config entry missing keys {missing}: {payload}")
        return CatalogSpec(
            name=payload["name"],
            path=payload["path"],
            id_col=payload["id_col"],
            ra_col=payload["ra_col"],
            dec_col=payload["dec_col"],
            score_col=payload["score_col"],
            z_col=payload.get("z_col"),
            threshold=float(payload["threshold"]),
            parent_total=int(payload["parent_total"]),
            catalog_total_at_threshold=int(payload["catalog_total_at_threshold"]),
            catalog_total_note=payload["catalog_total_note"],
            is_partial_preview=bool(payload.get("is_partial_preview", False)),
        )


def load_catalog(spec: CatalogSpec) -> pd.DataFrame:
    path = Path(spec.path)
    if not path.is_file():
        raise BenchmarkError(f"catalogue '{spec.name}' path is absent: {path}")
    if path.suffix == ".parquet":
        df = pd.read_parquet(path)
    elif path.suffix == ".csv":
        df = pd.read_csv(path)
    else:
        raise BenchmarkError(f"unsupported catalogue file type: {path}")
    for col in (spec.id_col, spec.ra_col, spec.dec_col, spec.score_col):
        if col not in df.columns:
            raise BenchmarkError(f"catalogue '{spec.name}' is missing required column '{col}' (has {list(df.columns)})")
    out = pd.DataFrame(
        {
            "targetid": df[spec.id_col],
            "ra": df[spec.ra_col].astype(float),
            "dec": df[spec.dec_col].astype(float),
            "score": df[spec.score_col].astype(float),
        }
    )
    if spec.z_col and spec.z_col in df.columns:
        out["z"] = df[spec.z_col].astype(float)
    else:
        out["z"] = np.nan
    return out


def crossmatch_positional(
    ref_ra: np.ndarray,
    ref_dec: np.ndarray,
    cat_ra: np.ndarray,
    cat_dec: np.ndarray,
    radius_arcsec: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Nearest-neighbor match of ref onto cat. Returns (matched, sep_arcsec, cat_idx)."""
    from astropy import units as u
    from astropy.coordinates import SkyCoord

    if len(cat_ra) == 0 or len(ref_ra) == 0:
        n = len(ref_ra)
        return np.zeros(n, dtype=bool), np.full(n, np.nan), np.full(n, -1, dtype=int)

    ref_coord = SkyCoord(ra=ref_ra * u.deg, dec=ref_dec * u.deg)
    cat_coord = SkyCoord(ra=cat_ra * u.deg, dec=cat_dec * u.deg)
    idx, sep2d, _ = ref_coord.match_to_catalog_sky(cat_coord)
    sep_arcsec = sep2d.arcsec
    matched = sep_arcsec <= radius_arcsec
    return matched, sep_arcsec, idx


def redshift_agreement(
    ref_z: np.ndarray, cat_z: np.ndarray, cat_idx: np.ndarray, matched: np.ndarray, z_tol: float
) -> np.ndarray:
    """For matched rows with a redshift on both sides, flag |dz|/(1+z_ref) <= tol.

    Returns an object array: True (agrees), False (disagrees), or None
    (not applicable -- missing z on one or both sides, or unmatched).
    """
    out = np.full(len(ref_z), None, dtype=object)
    for i in range(len(ref_z)):
        if not matched[i]:
            continue
        j = cat_idx[i]
        if j < 0 or j >= len(cat_z):
            continue
        zr, zc = ref_z[i], cat_z[j]
        if not (np.isfinite(zr) and np.isfinite(zc)):
            continue
        out[i] = bool(abs(zr - zc) / (1.0 + zr) <= z_tol)
    return out


# ---------------------------------------------------------------------------
# 4. Binomial confidence interval + enrichment
# ---------------------------------------------------------------------------


def wilson_score_interval(k: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    """Wilson score 95% CI (default z for alpha=0.05) for a binomial proportion.

    Deterministic, dependency-free (no scipy needed), matches the standard
    closed-form Wilson interval used across the astro literature for small-n
    recovery-fraction reporting.
    """
    if n <= 0:
        return (float("nan"), float("nan"))
    p_hat = k / n
    denom = 1.0 + z * z / n
    center = p_hat + z * z / (2 * n)
    half_width = z * math.sqrt((p_hat * (1 - p_hat) + z * z / (4 * n)) / n)
    lo = (center - half_width) / denom
    hi = (center + half_width) / denom
    return (max(0.0, lo), min(1.0, hi))


@dataclass
class ClassRecoveryResult:
    class_id: str
    class_name: str
    citation: str
    catalog_name: str
    n_reference_total: int
    n_reference_in_footprint: int
    n_matched: int
    n_z_agree: int
    n_z_checked: int
    recovery: float
    recovery_ci_lo: float
    recovery_ci_hi: float
    base_rate: float
    enrichment: float
    is_closed_loop_candidate: bool
    radius_arcsec: float

    def to_json(self) -> dict[str, Any]:
        return {
            "class_id": self.class_id,
            "class_name": self.class_name,
            "citation": self.citation,
            "catalog_name": self.catalog_name,
            "n_reference_total": self.n_reference_total,
            "n_reference_in_footprint": self.n_reference_in_footprint,
            "n_matched": self.n_matched,
            "n_z_agree": self.n_z_agree,
            "n_z_checked": self.n_z_checked,
            "recovery": self.recovery,
            "recovery_ci_95_lo": self.recovery_ci_lo,
            "recovery_ci_95_hi": self.recovery_ci_hi,
            "base_rate": self.base_rate,
            "enrichment": self.enrichment,
            "is_closed_loop_candidate": self.is_closed_loop_candidate,
            "radius_arcsec": self.radius_arcsec,
        }


def compute_class_recovery(
    class_id: str,
    class_name: str,
    citation: str,
    ref_ra: np.ndarray,
    ref_dec: np.ndarray,
    ref_z: Optional[np.ndarray],
    catalog_df: pd.DataFrame,
    spec: CatalogSpec,
    footprint_pixels: Optional[set[int]],
    radius_arcsec: float,
    z_tol: float,
    nside: int = DEFAULT_HEALPIX_NSIDE,
    nest: bool = DEFAULT_HEALPIX_NEST,
) -> ClassRecoveryResult:
    n_total = len(ref_ra)
    if footprint_pixels is not None and n_total > 0:
        in_footprint = restrict_to_footprint(ref_ra, ref_dec, footprint_pixels, nside=nside, nest=nest)
    else:
        in_footprint = np.ones(n_total, dtype=bool)
    n_in_footprint = int(in_footprint.sum())

    ref_ra_f = ref_ra[in_footprint]
    ref_dec_f = ref_dec[in_footprint]
    matched, sep_arcsec, cat_idx = crossmatch_positional(
        ref_ra_f, ref_dec_f, catalog_df["ra"].to_numpy(), catalog_df["dec"].to_numpy(), radius_arcsec
    )
    n_matched = int(matched.sum())

    n_z_agree = 0
    n_z_checked = 0
    if ref_z is not None:
        ref_z_f = ref_z[in_footprint]
        z_flags = redshift_agreement(ref_z_f, catalog_df["z"].to_numpy(), cat_idx, matched, z_tol)
        n_z_checked = int(sum(1 for v in z_flags if v is not None))
        n_z_agree = int(sum(1 for v in z_flags if v is True))

    recovery = (n_matched / n_in_footprint) if n_in_footprint > 0 else float("nan")
    ci_lo, ci_hi = wilson_score_interval(n_matched, n_in_footprint)
    base_rate = spec.catalog_total_at_threshold / spec.parent_total if spec.parent_total > 0 else float("nan")
    enrichment = (recovery / base_rate) if (base_rate and base_rate > 0 and not math.isnan(recovery)) else float("nan")
    is_candidate = (
        not math.isnan(enrichment)
        and enrichment > CLOSED_LOOP_ENRICHMENT_MIN
        and n_matched >= CLOSED_LOOP_MATCHES_MIN
    )
    return ClassRecoveryResult(
        class_id=class_id,
        class_name=class_name,
        citation=citation,
        catalog_name=spec.name,
        n_reference_total=n_total,
        n_reference_in_footprint=n_in_footprint,
        n_matched=n_matched,
        n_z_agree=n_z_agree,
        n_z_checked=n_z_checked,
        recovery=recovery,
        recovery_ci_lo=ci_lo,
        recovery_ci_hi=ci_hi,
        base_rate=base_rate,
        enrichment=enrichment,
        is_closed_loop_candidate=is_candidate,
        radius_arcsec=radius_arcsec,
    )


# ---------------------------------------------------------------------------
# 5. Report writers
# ---------------------------------------------------------------------------


def write_markdown_report(results: list[ClassRecoveryResult], reference_summary: dict[str, Any], out_path: Path) -> None:
    lines = [
        "# Known-object recovery benchmark (NEXT_SCIENCE_LEDGER item #8)",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        f"Reference classes: {reference_summary['n_classes']} total, "
        f"{reference_summary['n_fetched']} fetched, "
        f"{reference_summary['n_unavailable']} unavailable, "
        f"{reference_summary['n_no_catalog_id_known']} no catalogue ID known.",
        "",
        "| Class | Catalog | N ref (footprint) | N matched | Recovery | 95% CI | Base rate | Enrichment | Closed-loop candidate |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        recov = "n/a" if math.isnan(r.recovery) else f"{r.recovery:.3%}"
        ci = "n/a" if math.isnan(r.recovery_ci_lo) else f"[{r.recovery_ci_lo:.3%}, {r.recovery_ci_hi:.3%}]"
        base = "n/a" if math.isnan(r.base_rate) else f"{r.base_rate:.4%}"
        enr = "n/a" if math.isnan(r.enrichment) else f"{r.enrichment:.1f}x"
        flag = "YES" if r.is_closed_loop_candidate else ""
        lines.append(
            f"| {r.class_name} | {r.catalog_name} | {r.n_reference_in_footprint} | {r.n_matched} | "
            f"{recov} | {ci} | {base} | {enr} | {flag} |"
        )
    lines.append("")
    candidates = [r for r in results if r.is_closed_loop_candidate]
    if candidates:
        lines.append("## Closed-loop candidate classes (enrichment > 10x, >=5 matches)")
        for r in candidates:
            lines.append(f"- **{r.class_name}** on `{r.catalog_name}`: {r.n_matched} matches, {r.enrichment:.1f}x enrichment ({r.citation})")
    else:
        lines.append("## Closed-loop candidate classes")
        lines.append("None at this run's thresholds/sample -- see `--catalog` inputs used for exact provenance.")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_json_report(
    results: list[ClassRecoveryResult],
    reference_manifest: dict[str, Any],
    catalogs: list[CatalogSpec],
    args_used: dict[str, Any],
    out_path: Path,
) -> None:
    payload = {
        "benchmark_version": "bigbounce-recovery-benchmark/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "ledger_item": "NEXT_SCIENCE_LEDGER.md #8 -- anomaly catalogue known-object recovery benchmark",
        "parameters": args_used,
        "reference_manifest_summary": reference_manifest.get("summary", {}),
        "catalogs": [
            {
                "name": c.name,
                "threshold": c.threshold,
                "parent_total": c.parent_total,
                "catalog_total_at_threshold": c.catalog_total_at_threshold,
                "catalog_total_note": c.catalog_total_note,
                "is_partial_preview": c.is_partial_preview,
            }
            for c in catalogs
        ],
        "results": [r.to_json() for r in results],
        "closed_loop_candidates": [r.to_json() for r in results if r.is_closed_loop_candidate],
    }
    write_json_atomic(out_path, payload)


# ---------------------------------------------------------------------------
# 6. CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fetch-references", action="store_true", help="fetch reference classes from VizieR")
    parser.add_argument("--reference-cache-dir", type=Path, default=None, help="where to cache fetched reference tables (outside the repo)")
    parser.add_argument("--reference-manifest", type=Path, default=None, help="path to write/read the reference fetch manifest JSON")
    parser.add_argument("--row-limit", type=int, default=200_000)
    parser.add_argument("--vizier-timeout", type=float, default=30.0)

    parser.add_argument("--crossmatch", action="store_true", help="run the positional cross-match + recovery computation")
    parser.add_argument("--catalogs-config", type=Path, default=None, help="JSON: list of catalogue specs (see catalogs_config_example.json)")
    parser.add_argument("--locator-inventory", type=Path, default=None, help="sealed locator_inventory.jsonl for footprint restriction; omit to skip footprint restriction")
    parser.add_argument("--healpix-nside", type=int, default=DEFAULT_HEALPIX_NSIDE)
    parser.add_argument("--no-nest", action="store_true", help="use RING instead of NESTED healpix ordering")
    parser.add_argument("--radius-arcsec", type=float, default=DEFAULT_RADIUS_ARCSEC)
    parser.add_argument("--z-tol", type=float, default=DEFAULT_Z_TOL)
    parser.add_argument("--out-dir", type=Path, default=None, help="directory to write recovery_benchmark.json/.md")
    return parser


def run_fetch_references(args: argparse.Namespace) -> dict[str, Any]:
    if args.reference_cache_dir is None:
        raise BenchmarkError("--reference-cache-dir is required with --fetch-references")
    results = fetch_all_reference_classes(args.reference_cache_dir, args.row_limit, args.vizier_timeout)
    manifest_path = args.reference_manifest or (args.reference_cache_dir / "reference_manifest.json")
    write_reference_manifest(results, manifest_path)
    print(f"wrote reference manifest: {manifest_path}")
    for r in results:
        print(f"  {r.class_id}: {r.status} ({r.n_rows} rows)" + (f" -- {r.error}" if r.error else ""))
    return read_json(manifest_path)


def run_crossmatch(args: argparse.Namespace) -> None:
    if args.catalogs_config is None:
        raise BenchmarkError("--catalogs-config is required with --crossmatch")
    if args.out_dir is None:
        raise BenchmarkError("--out-dir is required with --crossmatch")
    reference_manifest_path = args.reference_manifest
    if reference_manifest_path is None and args.reference_cache_dir is not None:
        reference_manifest_path = args.reference_cache_dir / "reference_manifest.json"
    if reference_manifest_path is None or not reference_manifest_path.is_file():
        raise BenchmarkError("--reference-manifest (or --reference-cache-dir with reference_manifest.json in it) is required with --crossmatch")

    reference_manifest = read_json(reference_manifest_path)
    catalogs_payload = json.loads(args.catalogs_config.read_text(encoding="utf-8"))
    catalogs = [CatalogSpec.from_json(c) for c in catalogs_payload]

    footprint_pixels = None
    if args.locator_inventory is not None:
        footprint_pixels = load_footprint_pixel_set(args.locator_inventory, nside=args.healpix_nside)

    nest = not args.no_nest
    results: list[ClassRecoveryResult] = []
    for spec in catalogs:
        catalog_df = load_catalog(spec)
        for class_entry in reference_manifest["classes"]:
            if class_entry["status"] != "fetched":
                continue
            ref_class = next((r for r in REFERENCE_CLASSES if r.class_id == class_entry["class_id"]), None)
            if ref_class is None:
                continue
            from astropy.table import Table

            ref_table = Table.read(class_entry["cache_path"], format="ascii.ecsv")
            ra_col = class_entry["ra_col"]
            dec_col = class_entry["dec_col"]
            z_col = class_entry.get("z_col")
            ref_ra = np.asarray(ref_table[ra_col], dtype=float)
            ref_dec = np.asarray(ref_table[dec_col], dtype=float)
            ref_z = np.asarray(ref_table[z_col], dtype=float) if z_col and z_col in ref_table.colnames else None
            result = compute_class_recovery(
                class_id=ref_class.class_id,
                class_name=ref_class.name,
                citation=ref_class.citation,
                ref_ra=ref_ra,
                ref_dec=ref_dec,
                ref_z=ref_z,
                catalog_df=catalog_df,
                spec=spec,
                footprint_pixels=footprint_pixels,
                radius_arcsec=args.radius_arcsec,
                z_tol=args.z_tol,
                nside=args.healpix_nside,
                nest=nest,
            )
            results.append(result)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args_used = {
        "radius_arcsec": args.radius_arcsec,
        "z_tol": args.z_tol,
        "healpix_nside": args.healpix_nside,
        "healpix_nest": nest,
        "footprint_restriction": footprint_pixels is not None,
        "catalogs_config": str(args.catalogs_config),
        "locator_inventory": str(args.locator_inventory) if args.locator_inventory else None,
    }
    write_json_report(results, reference_manifest, catalogs, args_used, args.out_dir / "recovery_benchmark.json")
    write_markdown_report(results, reference_manifest.get("summary", {}), args.out_dir / "recovery_benchmark.md")
    print(f"wrote {args.out_dir / 'recovery_benchmark.json'}")
    print(f"wrote {args.out_dir / 'recovery_benchmark.md'}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if not args.fetch_references and not args.crossmatch:
        parser.error("pass --fetch-references and/or --crossmatch")
    try:
        if args.fetch_references:
            run_fetch_references(args)
        if args.crossmatch:
            run_crossmatch(args)
    except BenchmarkError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
