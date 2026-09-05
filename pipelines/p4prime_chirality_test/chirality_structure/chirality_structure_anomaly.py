"""Row 16 (iv) test (b): anomaly x parity angular cross-correlation + NN parity excess."""
import numpy as np, time, pyarrow.parquet as pq
from scipy.spatial import cKDTree
from chirality_structure_common import (load_chirality, pix_of, PixelShuffler,
                                        zscore, save, unit_vec, ANOM)

NNULL = 1000
NROT = 1000
EDGES = np.logspace(np.log10(0.02), np.log10(5.0), 9)   # 8 bins, degrees


def chord(deg):
    return 2 * np.sin(np.radians(deg) / 2)


def pair_bins(tree, gv, av, edges):
    """Return (galaxy index array, bin index array) for all anomaly-galaxy pairs."""
    idx = tree.query_ball_point(av, chord(edges[-1]), workers=-1)
    gi, bi = [], []
    ce = chord(edges)
    for k, lst in enumerate(idx):
        if not lst:
            continue
        j = np.asarray(lst)
        d = np.linalg.norm(gv[j] - av[k], axis=1)
        b = np.digitize(d, ce) - 1
        ok = (b >= 0) & (b < len(edges) - 1)
        gi.append(j[ok]); bi.append(b[ok])
    return np.concatenate(gi), np.concatenate(bi)


def binstat(delta, gi, bi, nbin):
    return (np.bincount(bi, weights=delta[gi], minlength=nbin) /
            np.maximum(np.bincount(bi, minlength=nbin), 1))


def main():
    ra, dec, s = load_chirality(True)
    delta = s - s.mean()
    gv = unit_vec(ra, dec)
    tree = cKDTree(gv)
    t = pq.read_table(ANOM, columns=["target_ra", "target_dec"])
    ara = t["target_ra"].to_numpy(); adec = t["target_dec"].to_numpy()
    ok = np.isfinite(ara) & np.isfinite(adec)
    av = unit_vec(ara[ok], adec[ok])
    print("anomalies", av.shape[0], flush=True)

    t0 = time.time(); gi, bi = pair_bins(tree, gv, av, EDGES)
    print("pairs", gi.size, time.time() - t0, flush=True)
    nb = len(EDGES) - 1
    w_obs = binstat(delta, gi, bi, nb)
    cnt = np.bincount(bi, minlength=nb)

    # nearest-neighbour parity excess
    dnn, inn = tree.query(av, k=1, workers=-1)
    nn_obs = float(delta[inn].mean())

    # ---- null 1: within-pixel label shuffle
    sh = PixelShuffler(pix_of(ra, dec), np.random.default_rng(16043))
    wn, nn_n = [], []
    t0 = time.time()
    for _ in range(NNULL):
        d = sh.shuffle(delta)
        wn.append(binstat(d, gi, bi, nb)); nn_n.append(d[inn].mean())
    wn = np.asarray(wn); print("shuffle null", time.time() - t0, flush=True)

    # ---- null 2: rigid random rotation of the anomaly positions
    rng = np.random.default_rng(16045)
    wr, nn_r = [], []
    t0 = time.time()
    for i in range(NROT):
        M = np.linalg.qr(rng.normal(size=(3, 3)))[0]
        if np.linalg.det(M) < 0:
            M[:, 0] *= -1
        avr = av @ M
        g2, b2 = pair_bins(tree, gv, avr, EDGES)
        wr.append(binstat(delta, g2, b2, nb))
        _, i2 = tree.query(avr, k=1, workers=-1)
        nn_r.append(delta[i2].mean())
        if i == 4:
            print("rot null per-iter", (time.time() - t0) / 5, flush=True)
    wr = np.asarray(wr); print("rot null", time.time() - t0, flush=True)

    res = {"edges_deg": EDGES.tolist(), "pair_counts": cnt.tolist(),
           "n_anomalies": int(av.shape[0]), "n_galaxies": int(ra.size),
           "w_theta_obs": w_obs.tolist(),
           "w_theta_vs_shuffle": [zscore(w_obs[j], wn[:, j]) for j in range(nb)],
           "w_theta_vs_rotation": [zscore(w_obs[j], wr[:, j]) for j in range(nb)],
           "nn_parity_excess": {"obs": nn_obs,
                                "vs_shuffle": zscore(nn_obs, nn_n),
                                "vs_rotation": zscore(nn_obs, nn_r),
                                "median_nn_sep_deg": float(np.degrees(2 * np.arcsin(np.median(dnn) / 2)))}}
    save("chirality_structure_anomaly.json", res)


if __name__ == "__main__":
    main()
