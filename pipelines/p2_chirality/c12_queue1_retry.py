#!/usr/bin/env python3
"""C12 QUEUE-1 retry (META-E2): NaMaster coupling-matrix conditioning.

nmt.mask_apodization raised RuntimeError('Not enough memory in listtot ...')
on the patchy N_all>=1 footprint on this host (it succeeds on a simple band
mask), so the C2 apodization is computed with a drop-in reimplementation of
the NaMaster C2 kernel (distance to nearest zero pixel via cKDTree;
x = sqrt((1-cos d)/(1-cos theta_apo)); f = 0.5(1-cos(pi x)) for x<1, else 1),
validated against nmt.mask_apodization on a band mask to max|diff| = 2.4e-13.
The mode-coupling matrix itself is computed by NaMaster proper.

Updates the queue1 block of outputs/canonical_provenance/c12_r24conf_local_batch.json.
"""
import json
import time
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
import pymaster as nmt
from huggingface_hub import hf_hub_download
from scipy.spatial import cKDTree

NSIDE = 64
NPIX = hp.nside2npix(NSIDE)
OUT = Path(__file__).parent / "outputs" / "canonical_provenance" / "c12_r24conf_local_batch.json"

t0 = time.time()


def log(m):
    print(f"[{time.time()-t0:7.1f}s] {m}", flush=True)


th_pix, ph_pix = hp.pix2ang(NSIDE, np.arange(NPIX))
xyz = np.column_stack([np.sin(th_pix) * np.cos(ph_pix),
                       np.sin(th_pix) * np.sin(ph_pix),
                       np.cos(th_pix)])


def c2_apod(mask, apo_deg):
    inn = np.where(mask > 0)[0]
    zeros = np.where(mask == 0)[0]
    tree = cKDTree(xyz[zeros])
    d_chord, _ = tree.query(xyz[inn])
    d = 2 * np.arcsin(np.clip(d_chord / 2, 0, 1))
    thstar = np.radians(apo_deg)
    x = np.sqrt((1 - np.cos(d)) / (1 - np.cos(thstar)))
    f = np.where(x < 1, 0.5 * (1 - np.cos(np.pi * np.clip(x, 0, 1))), 1.0)
    a = np.zeros(NPIX)
    a[inn] = f
    return a


log("loading parquet...")
p = hf_hub_download("bamfai/galaxy-chirality-catalog", "catalog_production.parquet",
                    repo_type="dataset", local_files_only=True)
df = pd.read_parquet(p, columns=["ra", "dec"])
pix_all = hp.ang2pix(NSIDE, np.radians(90.0 - df["dec"].values),
                     np.radians(df["ra"].values % 360))
n_all_map = np.bincount(pix_all, minlength=NPIX).astype(float)
binary = (n_all_map >= 1).astype(float)
log(f"footprint N_all>=1: {int(binary.sum())} pixels (expect 24297)")

blocks = {}
for apo in (1.0, 2.0, 3.0):
    apod = c2_apod(binary, apo)
    weight = apod * n_all_map
    fld = nmt.NmtField(weight, [np.zeros(NPIX)])
    bins = nmt.NmtBin.from_lmax_linear(3 * NSIDE - 1, 1)
    try:
        wsp = nmt.NmtWorkspace.from_fields(fld, fld, bins)
    except AttributeError:
        wsp = nmt.NmtWorkspace()
        wsp.compute_coupling_matrix(fld, fld, bins)
    M = wsp.get_coupling_matrix()
    s_full = np.linalg.svd(M, compute_uv=False)
    s_low = np.linalg.svd(M[:6, :6], compute_uv=False)
    row1 = M[1, :]
    diag_dom = float(M[1, 1] / (np.sum(np.abs(row1)) - abs(M[1, 1])))
    blocks[f"apod_{apo:.0f}deg"] = {
        "f_sky_eff": float(np.mean(weight) ** 2 / np.mean(weight ** 2)),
        "full_matrix": {
            "shape": list(M.shape),
            "sv_max": float(s_full[0]), "sv_min": float(s_full[-1]),
            "condition_number": float(s_full[0] / s_full[-1]),
        },
        "low_ell_block_l0_to_l5": {
            "singular_values": [float(v) for v in s_low],
            "condition_number": float(s_low[0] / s_low[-1]),
        },
        "l1_row": {
            "M_11": float(M[1, 1]),
            "diag_dominance_ratio_M11_over_offdiag_rowsum": diag_dom,
            "largest_offdiag_couplings": {
                f"l'={int(j)}": float(M[1, j])
                for j in np.argsort(np.abs(row1))[::-1][:5] if j != 1
            },
        },
    }
    log(f"apod {apo:.0f}deg: cond(full)={blocks[f'apod_{apo:.0f}deg']['full_matrix']['condition_number']:.4f} "
        f"cond(l<=5)={blocks[f'apod_{apo:.0f}deg']['low_ell_block_l0_to_l5']['condition_number']:.4f} "
        f"sv_min={s_full[-1]:.4e} diag-dom(l=1)={diag_dom:.4f}")

with open(OUT) as f:
    res = json.load(f)
res["items"]["queue1_meta_e2_coupling_conditioning"] = {
    "status": "CLOSED-LOCAL",
    "construction": (
        "NmtField(weight, [0]) with weight = C2-apodized(N_all>=1 binary) x "
        "N_all at NSIDE=64; bins NmtBin.from_lmax_linear(191, nlb=1); "
        "M = NmtWorkspace.get_coupling_matrix() (unbinned spin-0 mode-coupling "
        "matrix). Reported: SVD of the full matrix, SVD of the leading "
        "ell in [0,5] block, and the ell=1 row diagonal-dominance ratio "
        "M_11/sum_{l' != 1}|M_1l'|. Apodization computed by a validated "
        "reimplementation of the NaMaster C2 kernel (nmt.mask_apodization "
        "raised RuntimeError('Not enough memory in listtot') on this patchy "
        "footprint on this host; the reimplementation matches "
        "nmt.mask_apodization to max|diff|=2.4e-13 on a control band mask)."
    ),
    "apodization_sweep": blocks,
}
res["queue1_retry_date_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
with open(OUT, "w") as f:
    json.dump(res, f, indent=1)
log(f"updated {OUT}")
