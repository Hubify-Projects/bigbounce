"""Row 16 (iv) test (d): parity dipole along fixed axes + free best-fit direction.

NOTE (deviation, see .md S4): the pre-registered within-pixel label shuffle is
DEGENERATE for pixel-level dipole statistics (it preserves every pixel mean
exactly, giving zero null variance).  The nulls used here are therefore
(i) random-axis rotation (pre-registered for (d)) and (ii) permutation of the
per-pixel parity means among occupied pixels, which preserves the footprint and
the distribution of pixel means while destroying the parity-position link.
"""
import numpy as np, healpy as hp, time
from chirality_structure_common import load_chirality, zscore, save

NSIDE = 64
NNULL = 1000
AXES = {"cmb_dipole_l264_b48": (264.0, 48.0),
        "cmb_quad_oct_l250_b60": (250.0, 60.0)}


def pixel_map(ra, dec, s):
    pix = hp.ang2pix(NSIDE, ra, dec, lonlat=True)
    npix = hp.nside2npix(NSIDE)
    cnt = np.bincount(pix, minlength=npix)
    tot = np.bincount(pix, weights=s, minlength=npix)
    occ = np.where(cnt > 0)[0]
    m = tot[occ] / cnt[occ]
    return occ, m - m.mean(), cnt[occ]


def amp(mvals, cosang):
    return float(np.sum(mvals * cosang) / np.sum(cosang ** 2))


def main():
    ra, dec, s = load_chirality(True)
    occ, m, cnt = pixel_map(ra, dec, s)
    vecs = np.asarray(hp.pix2vec(NSIDE, occ)).T
    print("occupied pixels", occ.size, "galaxies", ra.size, flush=True)
    rot = hp.Rotator(coord=["G", "C"])
    rng = np.random.default_rng(16044)
    res = {"n_pixels": int(occ.size), "n_galaxies": int(ra.size),
           "nside": NSIDE, "shamir_axis": "UNAVAILABLE - no explicit RA/Dec "
           "quoted for Shamir's axis in the P4-prime paper; not fabricated"}

    def null_dists(axis_vec=None):
        rot_null, perm_null = [], []
        for _ in range(NNULL):
            if axis_vec is not None:
                v = rng.normal(size=3); v /= np.linalg.norm(v)
                rot_null.append(abs(amp(m, vecs @ v)))
            perm_null.append(abs(amp(rng.permutation(m), vecs @ (axis_vec if axis_vec is
                                                                 not None else np.array([0, 0, 1.0])))))
        return rot_null, perm_null

    for name, (l, b) in AXES.items():
        v = np.asarray(rot(hp.ang2vec(l, b, lonlat=True)))
        v = v / np.linalg.norm(v)
        cosang = vecs @ v
        a0 = amp(m, cosang)
        rot_null, perm_null = null_dists(v)
        res[name] = {"axis_galactic_l_b": [l, b],
                     "amplitude_frac": a0,
                     "vs_random_axis_null": zscore(abs(a0), rot_null),
                     "vs_pixel_permutation_null": zscore(abs(a0), perm_null)}
        print(name, a0, res[name]["vs_pixel_permutation_null"]["z"], flush=True)

    # free best-fit dipole (uniform pixel weight least squares), max-null LEE
    A = vecs
    coef, *_ = np.linalg.lstsq(A, m, rcond=None)
    amp_free = float(np.linalg.norm(coef))
    nhat = coef / amp_free
    cg = np.asarray(hp.Rotator(coord=["C", "G"])(nhat))
    l_f, b_f = hp.vec2ang(cg / np.linalg.norm(cg), lonlat=True)
    maxnull = []
    t = time.time()
    for _ in range(NNULL):
        c, *_ = np.linalg.lstsq(A, rng.permutation(m), rcond=None)
        maxnull.append(float(np.linalg.norm(c)))
    res["free_best_fit_dipole"] = {
        "amplitude_frac": amp_free,
        "direction_galactic_l_b": [float(l_f[0]), float(b_f[0])],
        "direction_equatorial_ra_dec": [float(hp.vec2ang(nhat, lonlat=True)[0][0]),
                                        float(hp.vec2ang(nhat, lonlat=True)[1][0])],
        "vs_pixel_permutation_max_null": zscore(amp_free, maxnull),
        "seconds": time.time() - t}
    print(res["free_best_fit_dipole"], flush=True)
    save("chirality_structure_axes.json", res)


if __name__ == "__main__":
    main()
