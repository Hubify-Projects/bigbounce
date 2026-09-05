"""Row 16 (iv) tests (a) environment-density and (c) redshift. Pre-registered."""
import numpy as np, time, pyarrow.parquet as pq
from sklearn.neighbors import BallTree
from chirality_structure_common import (load_chirality, pix_of, PixelShuffler,
                                        zscore, save, P5, CAT)

NNULL = 1000
K = 20


def knn_density(ra_field, dec_field, ra_q, dec_q, k=K):
    tree = BallTree(np.radians(np.column_stack([dec_field, ra_field])), metric="haversine")
    d, _ = tree.query(np.radians(np.column_stack([dec_q, ra_q])), k=k + 1)
    theta = d[:, -1]                       # radians to k-th neighbour
    area = 2 * np.pi * (1 - np.cos(theta))  # steradians
    return k / np.maximum(area, 1e-30)


def binned_means(delta, ibin, nbin):
    ssum = np.bincount(ibin, weights=delta, minlength=nbin)
    cnt = np.bincount(ibin, minlength=nbin)
    return ssum / np.maximum(cnt, 1), cnt


def chi2_and_slope(delta, ibin, nbin, xcen):
    m, cnt = binned_means(delta, ibin, nbin)
    var = np.maximum(1.0 - m ** 2, 1e-12) / np.maximum(cnt, 1)
    chi2 = float(np.sum((m - np.average(m, weights=cnt)) ** 2 / var))
    w = cnt / var * 0 + cnt
    xb = np.average(xcen, weights=w)
    slope = float(np.sum(w * (xcen - xb) * m) / np.sum(w * (xcen - xb) ** 2))
    return chi2, slope, m, cnt


def run_binned(name, delta, ibin, nbin, xcen, pixs, seed):
    rng = np.random.default_rng(seed)
    sh = PixelShuffler(pixs, rng)
    c0, s0, m0, cnt = chi2_and_slope(delta, ibin, nbin, xcen)
    cn, sn = [], []
    t = time.time()
    for i in range(NNULL):
        d = sh.shuffle(delta)
        c, s, _, _ = chi2_and_slope(d, ibin, nbin, xcen)
        cn.append(c); sn.append(s)
    return {"test": name, "bin_means": m0.tolist(), "bin_counts": cnt.tolist(),
            "bin_centers": np.asarray(xcen).tolist(),
            "chi2": zscore(c0, cn), "slope": zscore(s0, sn),
            "seconds": time.time() - t}


def main():
    res = {}
    ra, dec, s = load_chirality(True)
    delta = s - s.mean()
    pixs = pix_of(ra, dec)
    print("HC parity sample", ra.size, "mean s", s.mean())

    # ---- (a) environment via parity-blind kNN surface density of the full spiral parent
    t = pq.read_table(CAT, columns=["ra_deg", "dec_deg", "is_spiral"])
    fs = t["is_spiral"].to_numpy(zero_copy_only=False).astype(bool)
    raf = t["ra_deg"].to_numpy()[fs]; decf = t["dec_deg"].to_numpy()[fs]
    print("density field N =", raf.size, flush=True)
    t0 = time.time(); sig = knn_density(raf, decf, ra, dec); print("knn", time.time() - t0, flush=True)
    q = np.quantile(sig, [0.25, 0.5, 0.75])
    ib = np.digitize(sig, q)
    xcen = [float(np.median(np.log10(sig[ib == j]))) for j in range(4)]
    res["a_environment_density_quartiles"] = run_binned(
        "a", delta, ib, 4, xcen, pixs, 16041)
    res["a_density_field_N"] = int(raf.size)

    # ---- (c) redshift via the DESI spec-z matched chirality catalogue
    p5 = pq.read_table(P5, columns=["desi_z", "desi_zwarn", "match_class_eq",
                                    "match_ra", "match_dec", "matched_primary_deduped",
                                    "match_confidence_eq"])
    mp = p5["matched_primary_deduped"].to_numpy(zero_copy_only=False).astype(bool)
    cls = np.asarray(p5["match_class_eq"].to_pylist())
    z = p5["desi_z"].to_numpy(); zw = p5["desi_zwarn"].to_numpy()
    conf = p5["match_confidence_eq"].to_numpy()
    m = mp & np.isin(cls, ["CW", "CCW"]) & (zw == 0) & np.isfinite(z) & (z > 0) & (z < 0.6) & (conf > 0.6)
    zs = z[m]; ss = np.where(cls[m] == "CW", 1.0, -1.0)
    rz = p5["match_ra"].to_numpy()[m]; dz = p5["match_dec"].to_numpy()[m]
    print("z sample", zs.size, flush=True)
    edges = np.quantile(zs, np.linspace(0, 1, 6)); edges[0] -= 1e-9; edges[-1] += 1e-9
    ibz = np.clip(np.digitize(zs, edges[1:-1]), 0, 4)
    zc = [float(np.median(zs[ibz == j])) for j in range(5)]
    res["c_redshift_bins"] = run_binned("c", ss - ss.mean(), ibz, 5, zc,
                                        pix_of(rz, dz), 16042)
    res["c_z_sample_N"] = int(zs.size)
    save("chirality_structure_env_z.json", res)


if __name__ == "__main__":
    main()
