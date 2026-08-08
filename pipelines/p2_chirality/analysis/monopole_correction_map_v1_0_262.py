#!/usr/bin/env python3
"""
monopole_correction_map_v1_0_262.py
===================================

Delivered per-region CW-fraction monopole correction map for Catalog C
(P4, chirality catalog paper, v1.0.262).

WHY THIS EXISTS
---------------
The paper (Sec. "Global CW Fraction", Table `tab:cw_frac`) documents a
catalog-wide equivariant Catalog-C monopole:

    f_CW = 0.49735314698421823  (N_CW=1,592,107 ; N_CCW=1,609,053 ;
                                 N_spiral=3,201,160)
    excess = f_CW - 0.5 = -0.265%  ==>  -9.47 sigma (binomial)

and states a *prose recipe* for l=0 parity users: "the released catalog labels
must be locally monopole-renormalized (per-region CW-fraction subtraction)
before any global parity-odd statistic is formed."

The R-round truth audit (INT_v3 ROUND 2026-07-16-P4-v1.0.261, finding C4,
GENUINELY-NEW-REAL / product-completeness) asked that this prose recipe be
converted into a *delivered* pre-computed product: a per-region CW-fraction
monopole map with per-region binomial uncertainty. This script produces it.

WHAT IT COMPUTES
----------------
For each sky region r on the released Catalog-C spiral labels:
    N_spiral(r), N_CW(r)
    f_CW(r)                     = N_CW(r) / N_spiral(r)
    monopole_correction(r)      = f_CW(r) - 0.5   [the local excess to subtract]
    sigma_binomial(r)           = sqrt(f_CW(r)(1-f_CW(r)) / N_spiral(r))
    z_vs_half(r)                = monopole_correction(r) / sigma_binomial(r)

A downstream l=0 parity user renormalizes each region to local parity by
subtracting monopole_correction(r) from the region's CW fraction (equivalently,
by working with f_CW(r) - f_CW(r) = 0 per region) before forming any global
parity-odd statistic. This is a convenience product only: it changes NO science
number in the paper and does NOT affect the primary real-space dipole, which
absorbs any *constant* monopole into its fitted monopole term (proven
generatively, paper Sec. "Global CW Fraction").

REGION SCHEMES
--------------
Two HEALPix schemes are delivered (RING ordering, lonlat=True from ra_deg/dec_deg):
  * NSIDE=64  -- the *native pixelization used for the dipole fit* in the paper
                 (49,152 pixels). This is the map resolution at which a user
                 forms the A_p field; per-pixel binomial sigma is large
                 (~few percent) because ~130 spirals/pixel.
  * NSIDE=8   -- coarse, stable regions (768 pixels, ~7,000 spirals/region),
                 the recommended scale for a stable local-monopole subtraction.

INPUTS (all committed / hashed)
-------------------------------
Released public Catalog C, committed in-repo at:
  apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet
Catalog-C spiral sample := rows with is_spiral == True (class_eq in {CW, CCW}),
which exactly reproduces the canonical Table-4 monopole (asserted below). The
correction map is defined on the *released* Catalog-C label field as-is (it
therefore includes the raw_flip_qc_unsafe rows, matching the Table-4 monopole
definition, which is the label field a downstream l=0 user actually consumes).

Every input file is sha256-hashed into the output JSON header.

INTEGRITY
---------
Per /never-fabricate-derivation: every number written here is computed from the
committed parquet at run time. The script asserts the reproduced catalog-wide
monopole equals the canonical value in
outputs/canonical_provenance/global_cw_fraction.json to machine precision before
writing anything.
"""

import datetime as _dt
import hashlib
import json
import os
import sys

import numpy as np

try:
    import healpy as hp
except ImportError:  # pragma: no cover
    sys.exit("healpy required")
import pyarrow.parquet as pq

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_P4 = os.path.dirname(HERE)  # pipelines/p2_chirality

CATALOG_REL = "apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"
GLOBAL_CW_REL = "outputs/canonical_provenance/global_cw_fraction.json"

OUT_JSON = os.path.join(HERE, "monopole_correction_map_v1_0_262.json")
OUT_NPZ = os.path.join(HERE, "monopole_correction_map_v1_0_262_nside64.npz")

VERSION = "v1.0.262"
AUDIT_ROUND = (
    "project-context/peer-reviews/INT_v3/"
    "ROUND_2026-07-16-P4-v1.0.261-EXACTPDF-60d96cde-CLAUDESTACK-CONFIRM/"
    "P4_v1.0.261_truth_audit.md  (finding C4)"
)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def region_table(pix, is_cw, nside):
    """Aggregate per-region counts and binomial correction stats."""
    npix = hp.nside2npix(nside)
    n_spiral = np.bincount(pix, minlength=npix).astype(np.int64)
    n_cw = np.bincount(pix, weights=is_cw, minlength=npix).astype(np.int64)
    occ = n_spiral > 0
    f_cw = np.full(npix, np.nan)
    f_cw[occ] = n_cw[occ] / n_spiral[occ]
    correction = f_cw - 0.5  # local excess to subtract to renormalize to parity
    sigma = np.full(npix, np.nan)
    sigma[occ] = np.sqrt(f_cw[occ] * (1.0 - f_cw[occ]) / n_spiral[occ])
    z = np.full(npix, np.nan)
    nz = occ & (sigma > 0)
    z[nz] = correction[nz] / sigma[nz]
    return n_spiral, n_cw, f_cw, correction, sigma, z, occ


def main():
    cat_path = os.path.join(REPO_P4, CATALOG_REL)
    gcw_path = os.path.join(REPO_P4, GLOBAL_CW_REL)

    cat_sha = sha256_file(cat_path)
    cat_bytes = os.path.getsize(cat_path)

    tbl = pq.read_table(
        cat_path, columns=["ra_deg", "dec_deg", "class_eq", "is_spiral"]
    )
    ra = tbl["ra_deg"].to_numpy()
    dec = tbl["dec_deg"].to_numpy()
    cls = tbl["class_eq"].to_numpy(zero_copy_only=False)
    is_spiral = tbl["is_spiral"].to_numpy(zero_copy_only=False).astype(bool)

    # Catalog-C spiral sample (CW+CCW); reproduce canonical Table-4 monopole.
    ra = ra[is_spiral]
    dec = dec[is_spiral]
    cls = cls[is_spiral]
    is_cw = (cls == "CW").astype(np.float64)

    n_spiral_total = int(is_spiral.sum())
    n_cw_total = int(is_cw.sum())
    n_ccw_total = n_spiral_total - n_cw_total
    p_cw_total = n_cw_total / n_spiral_total
    sigma_total = float(np.sqrt(p_cw_total * (1 - p_cw_total) / n_spiral_total))
    dev_sigma_total = (0.5 - p_cw_total) / sigma_total  # +ve == CW-deficit

    # ---- provenance guard: must match canonical global monopole ----
    with open(gcw_path) as fh:
        gcw = json.load(fh)
    assert n_cw_total == gcw["N_CW"], (n_cw_total, gcw["N_CW"])
    assert n_ccw_total == gcw["N_CCW"], (n_ccw_total, gcw["N_CCW"])
    assert n_spiral_total == gcw["N_spiral"], (n_spiral_total, gcw["N_spiral"])
    assert abs(p_cw_total - gcw["p_CW"]) < 1e-15, (p_cw_total, gcw["p_CW"])
    assert abs(dev_sigma_total - gcw["deviation_from_parity_sigma"]) < 1e-9

    schemes = {}
    nside64_arrays = {}
    for nside in (8, 64):
        pix = hp.ang2pix(nside, ra, dec, lonlat=True)
        n_sp, n_cw, f_cw, corr, sig, z, occ = region_table(pix, is_cw, nside)
        occ_idx = np.where(occ)[0]

        # Well-sampled subset: excludes near-empty edge regions whose +/-tens-%
        # corrections are pure small-N noise (huge binomial sigma). Threshold
        # matches the paper's N_spiral>=10 support convention, scaled up for the
        # coarse NSIDE=8 regions.
        thr = 10 if nside == 64 else 100
        ws = occ & (n_sp >= thr)

        scheme = {
            "nside": nside,
            "ordering": "RING",
            "npix_total": int(hp.nside2npix(nside)),
            "npix_occupied": int(occ.sum()),
            "approx_pix_area_deg2": float(hp.nside2pixarea(nside, degrees=True)),
            "n_spiral_min": int(n_sp[occ].min()),
            "n_spiral_median": float(np.median(n_sp[occ])),
            "n_spiral_max": int(n_sp[occ].max()),
            "correction_min_pct": float(np.nanmin(corr) * 100),
            "correction_max_pct": float(np.nanmax(corr) * 100),
            "sigma_binomial_median": float(np.nanmedian(sig)),
            "abs_z_max": float(np.nanmax(np.abs(z))),
            "well_sampled": {
                "n_spiral_threshold": thr,
                "npix": int(ws.sum()),
                "correction_min_pct": float(np.nanmin(corr[ws]) * 100),
                "correction_max_pct": float(np.nanmax(corr[ws]) * 100),
                "abs_z_max": float(np.nanmax(np.abs(z[ws]))),
                "note": (
                    "Correction range and max |z| over regions with "
                    "N_spiral >= threshold; the full-region extremes above are "
                    "dominated by near-empty edge regions (small-N noise)."
                ),
            },
        }

        if nside == 8:
            # Full per-region table inline (441 occupied regions).
            regions = []
            for p in occ_idx:
                th, ph = hp.pix2ang(nside, int(p), lonlat=True)
                regions.append(
                    {
                        "healpix_ring": int(p),
                        "center_ra_deg": float(th),
                        "center_dec_deg": float(ph),
                        "n_spiral": int(n_sp[p]),
                        "n_cw": int(n_cw[p]),
                        "f_cw": float(f_cw[p]),
                        "monopole_correction": float(corr[p]),
                        "monopole_correction_pct": float(corr[p] * 100),
                        "sigma_binomial": float(sig[p]),
                        "z_vs_half": float(z[p]),
                    }
                )
            scheme["regions"] = regions
            scheme["note"] = (
                "Full per-region table inline. Recommended stable scale for "
                "local monopole subtraction (~7k spirals/region)."
            )
        else:
            # NSIDE=64: native dipole-fit resolution; full-sky arrays -> npz.
            scheme["arrays_file"] = os.path.basename(OUT_NPZ)
            scheme["arrays_note"] = (
                "Full-sky length-49152 RING arrays saved to the .npz. Empty "
                "pixels are hp.UNSEEN in float arrays and 0 in count arrays. "
                "This is the native pixelization used for the paper's dipole "
                "fit; per-pixel binomial sigma is large (~few %) at ~130 "
                "spirals/pixel -- use NSIDE=8 for a stable subtraction."
            )
            f_cw_s = np.where(occ, f_cw, hp.UNSEEN)
            corr_s = np.where(occ, corr, hp.UNSEEN)
            sig_s = np.where(occ, sig, hp.UNSEEN)
            z_s = np.where(occ, z, hp.UNSEEN)
            nside64_arrays = dict(
                n_spiral=n_sp.astype(np.int32),
                n_cw=n_cw.astype(np.int32),
                f_cw=f_cw_s,
                monopole_correction=corr_s,
                sigma_binomial=sig_s,
                z_vs_half=z_s,
            )
        schemes[f"nside{nside}"] = scheme

    np.savez_compressed(
        OUT_NPZ,
        nside=64,
        ordering=np.string_("RING"),
        **nside64_arrays,
    )
    npz_sha = sha256_file(OUT_NPZ)

    now_pt = _dt.datetime.now(_dt.timezone(_dt.timedelta(hours=-7)))
    header = {
        "product": "Catalog-C per-region CW-fraction monopole correction map",
        "paper_version": VERSION,
        "generated_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "generated_pt": now_pt.isoformat(),
        "generator": "pipelines/p2_chirality/analysis/monopole_correction_map_v1_0_262.py",
        "closes_finding": AUDIT_ROUND,
        "purpose": (
            "Delivered pre-computed per-region CW-fraction monopole correction "
            "(the 'locally monopole-renormalize / per-region CW-fraction "
            "subtraction' recipe stated in the paper's Global CW Fraction "
            "section) with per-region binomial uncertainty. Convenience product "
            "for l=0 parity-odd users; changes NO science number and does not "
            "affect the primary real-space dipole (constant-monopole absorption "
            "proven generatively in the paper)."
        ),
        "definition": {
            "sample": "Catalog C spiral sample (is_spiral True; class_eq in {CW,CCW})",
            "includes_raw_flip_qc_unsafe": True,
            "includes_unsafe_note": (
                "The map is defined on the released Catalog-C label field as-is, "
                "matching the Table-4 catalog-wide monopole definition; this is "
                "the label field a downstream l=0 parity user consumes."
            ),
            "f_cw": "N_CW(region) / N_spiral(region)",
            "monopole_correction": "f_cw(region) - 0.5  (local excess to subtract)",
            "sigma_binomial": "sqrt(f_cw(1-f_cw)/N_spiral) per region",
            "z_vs_half": "(f_cw-0.5)/sigma_binomial per region",
            "usage": (
                "Subtract monopole_correction(region) from each region's CW "
                "fraction before forming any global parity-odd (l=0) statistic."
            ),
        },
        "inputs": [
            {
                "role": "released Catalog C (public, committed in-repo)",
                "path": CATALOG_REL,
                "sha256": cat_sha,
                "bytes": cat_bytes,
                "rows_total": int(tbl.num_rows),
            },
            {
                "role": "canonical global monopole (provenance guard)",
                "path": GLOBAL_CW_REL,
                "sha256": sha256_file(gcw_path),
            },
        ],
        "catalog_wide_monopole_reproduced": {
            "N_CW": n_cw_total,
            "N_CCW": n_ccw_total,
            "N_spiral": n_spiral_total,
            "p_CW": p_cw_total,
            "sigma_binomial": sigma_total,
            "deviation_from_parity_sigma": dev_sigma_total,
            "excess_pct": (p_cw_total - 0.5) * 100,
            "matches_global_cw_fraction_json": True,
        },
        "outputs": {
            "json": os.path.basename(OUT_JSON),
            "npz_nside64": {
                "file": os.path.basename(OUT_NPZ),
                "sha256": npz_sha,
            },
        },
        "region_schemes": schemes,
    }

    with open(OUT_JSON, "w") as fh:
        json.dump(header, fh, indent=2)

    print("wrote", OUT_JSON)
    print("wrote", OUT_NPZ, "sha256", npz_sha)
    print(
        "catalog-wide monopole reproduced: f_CW=%.17f  dev=%.6f sigma"
        % (p_cw_total, dev_sigma_total)
    )
    for k, s in schemes.items():
        ws = s["well_sampled"]
        print(
            "  %-8s occ=%4d  ws(N>=%d) n=%d corr%%=[%+.3f,%+.3f] |z|max=%.2f"
            % (
                k,
                s["npix_occupied"],
                ws["n_spiral_threshold"],
                ws["npix"],
                ws["correction_min_pct"],
                ws["correction_max_pct"],
                ws["abs_z_max"],
            )
        )


if __name__ == "__main__":
    main()
