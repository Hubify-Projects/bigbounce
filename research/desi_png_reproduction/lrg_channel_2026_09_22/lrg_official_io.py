"""Ledger row 4 LRG channel: streaming reader for the OFFICIAL DESI DR1
full-shape-bao-clustering VAC v1.0 LRG products.

Exact remote analogue of ../official_window_io.py (which reads the same six
QSO product types off local disk). Each file is pulled once by HTTP range
reads into memory, sha256'd, and opened with h5py from a BytesIO -- so the
sha256 recorded in the manifest is the sha256 of the exact bytes the fit
used, and nothing is written to disk.
"""
import hashlib
import io

import h5py
import numpy as np

import http_stream as hs

VAC = ("https://data.desi.lbl.gov/public/dr1/vac/dr1/"
       "full-shape-bao-clustering/v1.0/data")
ZBINS = ["0.4-0.6", "0.6-0.8", "0.8-1.1"]
SHA256 = {}


def _fetch(url):
    n = hs.content_length(url)
    chunks, pos, step = [], 0, 32 << 20
    while pos < n:
        end = min(pos + step, n) - 1
        chunks.append(hs._get(url, pos, end))
        pos = end + 1
    b = b"".join(chunks)
    assert len(b) == n, (len(b), n)
    SHA256[url] = dict(sha256=hashlib.sha256(b).hexdigest(), bytes=n)
    return b


def _h5(url):
    return h5py.File(io.BytesIO(_fetch(url)), "r")


def load_window(zbin, cap="GCcomb"):
    f = _h5(f"{VAC}/spectrum/window_spectrum-poles_LRG_{cap}_z{zbin}.h5")
    value = f["value"][()]
    theory_k = {ell: f[f"theory/{ell}/k"][()] for ell in (0, 2, 4)}
    obs_k = {ell: f[f"observable/{ell}/k"][()] for ell in (0, 2, 4)}
    obs_kedges = {ell: f[f"observable/{ell}/k_edges"][()] for ell in (0, 2, 4)}
    f.close()
    return value, theory_k, obs_k, obs_kedges


def load_measured(zbin, cap="GCcomb"):
    f = _h5(f"{VAC}/spectrum/spectrum-poles_LRG_{cap}_z{zbin}.h5")
    zeff = float(f.attrs["zeff"])
    out = {}
    for ell in (0, 2, 4):
        out[ell] = dict(k=f[f"{ell}/k"][()], value=f[f"{ell}/value"][()],
                        nmodes=f[f"{ell}/nmodes"][()],
                        num_shotnoise=f[f"{ell}/num_shotnoise"][()])
    f.close()
    out["zeff"] = zeff
    return out


def load_covariance(zbin):
    f = _h5(f"{VAC}/covariance/EZmock/covariance_spectrum-poles_LRG_GCcomb_z{zbin}.h5")
    cov = f["value"][()]
    kedges = {ell: f[f"observable/{ell}/k_edges"][()] for ell in (0, 2, 4)}
    kc = {ell: f[f"observable/{ell}/k"][()] for ell in (0, 2, 4)}
    f.close()
    return cov, kedges, kc
