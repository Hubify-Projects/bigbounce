#!/usr/bin/env python3
"""Row 16 (iv-b): chirality parity vs DESI DR1 BGS_BRIGHT-21.5 environment.

Pre-registered in ROW16IVB_BGS_ENVIRONMENT_2026-09-05.md before any data run.
Environment = k-NN density contrast of the chirality galaxies against the BGS
tracer field, normalised by the same estimator on the BGS randoms (selection
function).  Bins: void-like (lowest quintile), wall/filament (middle three),
node-like (top quintile).  NOT a void finder; a density-based proxy.
"""
import glob, json, os, time
import numpy as np, pyarrow.parquet as pq
from scipy.spatial import cKDTree
from chirality_structure_common import (load_chirality, pix_of, PixelShuffler,
                                        zscore, save, unit_vec, P5)

BGS = os.path.expanduser("~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/bgs")
K = 10
NNULL_SHUF = 1000
NNULL_ROT = int(os.environ.get("NNULL_ROT", 1000))
RAN_CAP = 3_000_000          # per cap, uniform seeded subsample of the randoms
OM, H0 = 0.315, 67.4
RESID_MONOPOLE = -0.26       # % injection-calibrated residual (P4')


def comoving(z):
    """Flat LCDM comoving distance [Mpc], trapezoid on a fine grid."""
    zg = np.linspace(0, 1.0, 20001)
    E = np.sqrt(OM * (1 + zg) ** 3 + (1 - OM))
    chi = np.concatenate([[0.0], np.cumsum(np.diff(zg) * 0.5 * (1 / E[1:] + 1 / E[:-1]))])
    return np.interp(z, zg, chi) * (299792.458 / H0)


def load_bgs(kind, nran, seed=1604):
    ra, dec, z = [], [], []
    for cap in ("NGC", "SGC"):
        if kind == "dat":
            files = [f"{BGS}/BGS_BRIGHT-21.5_{cap}_clustering.dat.parquet"]
        else:
            files = [f"{BGS}/BGS_BRIGHT-21.5_{cap}_{i}_clustering.ran.parquet"
                     for i in range(nran)]
            files = [f for f in files if os.path.exists(f)]
        rr, dd, zz = [], [], []
        for f in files:
            t = pq.read_table(f, columns=["RA", "DEC", "Z"])
            rr.append(t["RA"].to_numpy()); dd.append(t["DEC"].to_numpy())
            zz.append(t["Z"].to_numpy())
        rr, dd, zz = np.concatenate(rr), np.concatenate(dd), np.concatenate(zz)
        if kind != "dat" and rr.size > RAN_CAP:
            idx = np.random.default_rng(seed).choice(rr.size, RAN_CAP, replace=False)
            rr, dd, zz = rr[idx], dd[idx], zz[idx]
        ra.append(rr); dec.append(dd); z.append(zz)
    return np.concatenate(ra), np.concatenate(dec), np.concatenate(z)


def xyz3d(ra, dec, z):
    return unit_vec(ra, dec) * comoving(z)[:, None]


def knn_rho(tree, q, k=K, dim=3):
    d, _ = tree.query(q, k=k, workers=-1)
    r = np.maximum(d[:, -1], 1e-12)
    return k / r ** dim


def env_bins(rho_d, rho_r, nd, nr):
    """Density contrast, then quintile bins -> 0 void-like, 1 wall, 2 node-like."""
    dl = (rho_d / nd) / np.maximum(rho_r / nr, 1e-30)
    q = np.quantile(dl, [0.2, 0.8])
    return np.digitize(dl, q), dl


def fcw(s):
    return 0.5 * (1.0 + s.mean())


def bin_stats(s, ib, nb=3):
    """f_CW per bin and chi2 of the trend across bins (on f_CW)."""
    cnt = np.bincount(ib, minlength=nb).astype(float)
    ssum = np.bincount(ib, weights=s, minlength=nb)
    f = 0.5 * (1.0 + ssum / np.maximum(cnt, 1))
    fbar = 0.5 * (1.0 + s.mean())
    var = np.maximum(fbar * (1 - fbar), 1e-12) / np.maximum(cnt, 1)
    chi2 = float(np.sum((f - fbar) ** 2 / var))
    return f, cnt, chi2


def dipole(delta, nhat):
    """Free best-fit dipole: a = (N N^T)^-1 sum delta*n ; amplitude |a|."""
    M = nhat.T @ nhat
    b = nhat.T @ delta
    a = np.linalg.solve(M, b)
    return float(np.linalg.norm(a)), a / np.linalg.norm(a)


def run_subset(tag, ra, dec, s, ib, res, seed):
    nhat = unit_vec(ra, dec)
    pixs = pix_of(ra, dec)
    rng = np.random.default_rng(seed)
    sh = PixelShuffler(pixs, rng)
    f0, cnt, chi20 = bin_stats(s, ib)
    dip0 = [dipole(s[ib == j] - s[ib == j].mean(), nhat[ib == j])[0] for j in range(3)]
    dir0 = [dipole(s[ib == j] - s[ib == j].mean(), nhat[ib == j])[1].tolist() for j in range(3)]
    fn, cn, dn = [], [], []
    t0 = time.time()
    for _ in range(NNULL_SHUF):
        sp = sh.shuffle(s)
        f, _, c = bin_stats(sp, ib)
        fn.append(f); cn.append(c)
        dn.append([dipole(sp[ib == j] - sp[ib == j].mean(), nhat[ib == j])[0]
                   for j in range(3)])
    fn, dn = np.array(fn), np.array(dn)
    names = ["void_like", "wall_filament", "node_like"]
    res[tag] = {
        "N": int(s.size), "bin_counts": cnt.tolist(),
        "f_CW": {names[j]: {"value": float(f0[j]),
                            "binomial_sigma": float(np.sqrt(0.25 / max(cnt[j], 1))),
                            **zscore(f0[j], fn[:, j])} for j in range(3)},
        "chi2_trend_2dof": zscore(chi20, cn),
        "dipole": {names[j]: {"direction_xyz": dir0[j], **zscore(dip0[j], dn[:, j])}
                   for j in range(3)},
        "residual_monopole_percent": RESID_MONOPOLE,
        "null_seconds": time.time() - t0,
    }
    print(tag, "f_CW", f0, "chi2", chi20, flush=True)


def rand_rot(rng):
    A = rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(A)
    return Q * np.sign(np.diag(R))


def rotation_null(tag, s, ib0, X, td, tr, nd, nr, dim, res, seed, nrot):
    """Rigidly rotate the tracer field (equivalently the query set), re-bin, re-stat."""
    rng = np.random.default_rng(seed)
    _, _, chi20 = bin_stats(s, ib0)
    cn = []
    t0 = time.time()
    for _ in range(nrot):
        Xr = X @ rand_rot(rng).T
        ib, _ = env_bins(knn_rho(td, Xr, dim=dim), knn_rho(tr, Xr, dim=dim), nd, nr)
        cn.append(bin_stats(s, ib)[2])
    res[tag]["chi2_trend_rotation_null"] = zscore(chi20, cn)
    res[tag]["rotation_null_realisations"] = int(nrot)
    res[tag]["rotation_seconds"] = time.time() - t0
    print(tag, "rotation null done", time.time() - t0, flush=True)


def main():
    nran = len(glob.glob(f"{BGS}/BGS_BRIGHT-21.5_NGC_*_clustering.ran.parquet"))
    res = {"k": K, "n_randoms_per_cap": nran, "random_subsample_cap": RAN_CAP,
           "tracer": "DESI DR1 BGS_BRIGHT-21.5 (0.1<z<0.4)"}
    dra, ddec, dz = load_bgs("dat", nran)
    rra, rdec, rz = load_bgs("ran", nran)
    res["bgs_data_N"], res["bgs_random_N"] = int(dra.size), int(rra.size)
    print("BGS data", dra.size, "randoms", rra.size, flush=True)

    # ---------- (1) spec-z subset: 3D comoving environment ----------
    p5 = pq.read_table(P5, columns=["desi_z", "desi_zwarn", "match_class_eq", "match_ra",
                                    "match_dec", "matched_primary_deduped",
                                    "match_confidence_eq"])
    mp = p5["matched_primary_deduped"].to_numpy(zero_copy_only=False).astype(bool)
    cls = np.asarray(p5["match_class_eq"].to_pylist())
    z = p5["desi_z"].to_numpy(); zw = p5["desi_zwarn"].to_numpy()
    conf = p5["match_confidence_eq"].to_numpy()
    m = (mp & np.isin(cls, ["CW", "CCW"]) & (zw == 0) & np.isfinite(z)
         & (z > 0.1) & (z < 0.4) & (conf > 0.6))
    sz = np.where(cls[m] == "CW", 1.0, -1.0)
    raz, decz = p5["match_ra"].to_numpy()[m], p5["match_dec"].to_numpy()[m]
    Xq = xyz3d(raz, decz, z[m])
    td = cKDTree(xyz3d(dra, ddec, dz)); tr = cKDTree(xyz3d(rra, rdec, rz))
    ib3, dl3 = env_bins(knn_rho(td, Xq), knn_rho(tr, Xq), dra.size, rra.size)
    print("spec-z subset", sz.size, flush=True)
    run_subset("specz_3d", raz, decz, sz, ib3, res, 16050)
    rotation_null("specz_3d", sz, ib3, Xq, td, tr, dra.size, rra.size, 3, res, 16051, NNULL_ROT)

    # ---------- (2) photo-z / no-z subset: projected environment ----------
    ra, dec, s = load_chirality(True)
    nd2 = unit_vec(dra, ddec); nr2 = unit_vec(rra, rdec)
    td2 = cKDTree(nd2); tr2 = cKDTree(nr2)
    Q = unit_vec(ra, dec)
    ib2, dl2 = env_bins(knn_rho(td2, Q, dim=2), knn_rho(tr2, Q, dim=2), dra.size, rra.size)
    run_subset("photoz_projected", ra, dec, s, ib2, res, 16052)
    rotation_null("photoz_projected", s, ib2, Q, td2, tr2, dra.size, rra.size, 2, res, 16053,
                  max(NNULL_ROT // 5, 200))
    res["median_density_contrast"] = {
        "specz_3d": [float(np.median(dl3[ib3 == j])) for j in range(3)],
        "photoz_projected": [float(np.median(dl2[ib2 == j])) for j in range(3)]}
    save("row16ivb_bgs_environment.json", res)
    print("ROW16IVB_DONE", flush=True)


if __name__ == "__main__":
    main()
