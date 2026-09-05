"""Row 16 (iv) common loaders + null machinery. Pre-registered 2026-09-04."""
import numpy as np, pyarrow.parquet as pq, healpy as hp, json, os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CAT = os.path.join(REPO, "pipelines/p2_chirality/apjs_release_v1.0.244/"
                         "p4_catalog_primary_safe_v1.0.244.parquet")
ANOM = os.path.join(REPO, "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/"
                          "phase3_v2/flagship_sample_v2_enriched.parquet")
P5 = os.path.join(REPO, "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet")
NSIDE_SHUF = 64
OUT = os.path.dirname(os.path.abspath(__file__))


def load_chirality(hc_only=True):
    t = pq.read_table(CAT, columns=["ra_deg", "dec_deg", "class_eq", "primary_hc"])
    ra = t["ra_deg"].to_numpy(); dec = t["dec_deg"].to_numpy()
    cls = np.asarray(t["class_eq"].to_pylist()); hc = t["primary_hc"].to_numpy(zero_copy_only=False)
    m = np.isin(cls, ["CW", "CCW"])
    if hc_only:
        m &= hc.astype(bool)
    s = np.where(cls[m] == "CW", 1.0, -1.0)
    return ra[m].astype(np.float64), dec[m].astype(np.float64), s


def pix_of(ra, dec, nside=NSIDE_SHUF):
    return hp.ang2pix(nside, ra, dec, lonlat=True)


class PixelShuffler:
    """Permute labels within HEALPix pixels: preserves footprint + per-pixel selection."""

    def __init__(self, pix, rng):
        self.order = np.argsort(pix, kind="stable")
        self.pix_sorted = pix[self.order]
        self.rng = rng
        self.n = pix.size

    def shuffle(self, vals):
        """Return vals permuted within pixel groups (vals in original row order)."""
        keys = self.rng.random(self.n)
        perm = np.lexsort((keys, self.pix_sorted))
        out = np.empty_like(vals)
        out[self.order] = vals[self.order][perm]
        return out


def zscore(obs, null):
    null = np.asarray(null, dtype=float)
    mu, sd = null.mean(), null.std(ddof=1)
    z = (obs - mu) / sd if sd > 0 else np.nan
    p = (np.sum(np.abs(null - mu) >= abs(obs - mu)) + 1) / (null.size + 1)
    return dict(obs=float(obs), null_mean=float(mu), null_std=float(sd),
                z=float(z), p_two_sided=float(p), n_null=int(null.size))


def unit_vec(ra, dec):
    r, d = np.radians(ra), np.radians(dec)
    return np.column_stack([np.cos(d) * np.cos(r), np.cos(d) * np.sin(r), np.sin(d)])


def gal_to_vec(l, b):
    v = hp.ang2vec(l, b, lonlat=True)
    rot = hp.Rotator(coord=["G", "C"])
    return rot(v)


def save(name, obj):
    p = os.path.join(OUT, name)
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, default=float)
    print("wrote", p)
