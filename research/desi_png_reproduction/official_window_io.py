"""Ledger row 4 v3: I/O for OFFICIAL DESI DR1 full-shape-clustering VAC
products (window matrix, measured P_ell, EZmock covariance) — downloaded
from data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering/v1.0/.
Real published products, not our own homebrew reconstruction (v1/v2's
shuffled-randoms window + diagonal covariance are superseded by these for
the causes they addressed: real CatalogSmoothWindow->WindowMatrix,
full-18-randoms measurement, EZmock-based covariance).
"""
import h5py
import numpy as np

D = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/official_products"


def load_window(cap):
    f = h5py.File(f"{D}/window_spectrum-poles_QSO_{cap}_z0.8-2.1.h5", "r")
    value = f["value"][()]  # (n_obs, n_theory)
    theory_k = {ell: f[f"theory/{ell}/k"][()] for ell in (0, 2, 4)}
    obs_k = {ell: f[f"observable/{ell}/k"][()] for ell in (0, 2, 4)}
    obs_kedges = {ell: f[f"observable/{ell}/k_edges"][()] for ell in (0, 2, 4)}
    f.close()
    return value, theory_k, obs_k, obs_kedges


def load_measured(cap):
    f = h5py.File(f"{D}/spectrum-poles_QSO_{cap}_z0.8-2.1.h5", "r")
    out = {}
    for ell in (0, 2, 4):
        out[ell] = dict(
            k=f[f"{ell}/k"][()], value=f[f"{ell}/value"][()],
            nmodes=f[f"{ell}/nmodes"][()],
            num_shotnoise=f[f"{ell}/num_shotnoise"][()],
        )
    f.close()
    return out


def load_covariance():
    f = h5py.File(f"{D}/covariance_spectrum-poles_QSO_GCcomb_z0.8-2.1.h5", "r")
    cov = f["value"][()]
    kedges = {ell: f[f"observable/{ell}/k_edges"][()] for ell in (0, 2, 4)}
    kc = {ell: f[f"observable/{ell}/k"][()] for ell in (0, 2, 4)}
    f.close()
    return cov, kedges, kc


def rebin_to_coarse(fine_k, fine_val, fine_nmodes, coarse_kedges):
    """nmodes-weighted average of a fine-grid vector into coarse bins
    defined by coarse_kedges (n_coarse, 2)."""
    out = np.full(len(coarse_kedges), np.nan)
    for i, (lo, hi) in enumerate(coarse_kedges):
        m = (fine_k >= lo) & (fine_k < hi)
        if m.sum() == 0:
            continue
        w = fine_nmodes[m]
        out[i] = np.average(fine_val[m], weights=w)
    return out


def theory_vec_len(theory_k):
    return sum(len(theory_k[ell]) for ell in (0, 2, 4))


def pack_theory(p0, p2, p4):
    return np.concatenate([p0, p2, p4])
