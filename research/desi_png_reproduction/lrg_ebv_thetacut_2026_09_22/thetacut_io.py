"""Lane LS14: streaming reader for the OFFICIAL DESI DR1 LRG products in
BOTH conventions -- untreated and `_thetacut0.05`.

This is ../lrg_channel_2026_09_22/lrg_official_io.py with one added
argument (`variant`) and cap-resolved spectra. The fetch/sha256/BytesIO
mechanics are byte-for-byte that module's: each file is pulled once by HTTP
range reads into memory, sha256'd, and opened with h5py from a BytesIO, so
the sha256 recorded in the manifest is the sha256 of the exact bytes the fit
used and nothing is written to disk.
"""
import hashlib
import io
import sys

import h5py
import numpy as np

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction"
sys.path.insert(0, f"{HERE}/lrg_channel_2026_09_22")
import http_stream as hs  # noqa: E402

VAC = ("https://data.desi.lbl.gov/public/dr1/vac/dr1/"
       "full-shape-bao-clustering/v1.0/data")
ZBIN = "0.8-1.1"
UNTREATED, THETACUT = "", "_thetacut0.05"
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


def load_window(variant, zbin=ZBIN, cap="GCcomb"):
    f = _h5(f"{VAC}/spectrum/window_spectrum-poles_LRG_{cap}_z{zbin}{variant}.h5")
    value = f["value"][()]
    theory_k = {ell: f[f"theory/{ell}/k"][()] for ell in (0, 2, 4)}
    obs_k = {ell: f[f"observable/{ell}/k"][()] for ell in (0, 2, 4)}
    obs_kedges = {ell: f[f"observable/{ell}/k_edges"][()] for ell in (0, 2, 4)}
    f.close()
    return value, theory_k, obs_k, obs_kedges


def load_measured(variant, zbin=ZBIN, cap="GCcomb"):
    f = _h5(f"{VAC}/spectrum/spectrum-poles_LRG_{cap}_z{zbin}{variant}.h5")
    zeff = float(f.attrs["zeff"])
    out = {}
    for ell in (0, 2, 4):
        out[ell] = dict(k=f[f"{ell}/k"][()], value=np.real(f[f"{ell}/value"][()]),
                        nmodes=f[f"{ell}/nmodes"][()],
                        num_shotnoise=f[f"{ell}/num_shotnoise"][()])
    f.close()
    out["zeff"] = zeff
    return out


def load_covariance(variant, zbin=ZBIN):
    f = _h5(f"{VAC}/covariance/EZmock/"
            f"covariance_spectrum-poles_LRG_GCcomb_z{zbin}{variant}.h5")
    cov = f["value"][()]
    kedges = {ell: f[f"observable/{ell}/k_edges"][()] for ell in (0, 2, 4)}
    kc = {ell: f[f"observable/{ell}/k"][()] for ell in (0, 2, 4)}
    f.close()
    return cov, kedges, kc
