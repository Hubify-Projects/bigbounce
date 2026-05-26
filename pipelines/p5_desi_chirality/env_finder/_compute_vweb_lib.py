"""Shared V-Web algorithm primitives (factored out from 01_compute_vweb.py
so 02_compute_vweb_recon.py can reuse them).

CIC deposit, Gaussian-FFT smoothing, tidal-tensor eigenvalues, classify,
nearest-neighbour interpolation. Algorithm unchanged from Hahn+ 2007 /
Cautun+ 2014; this is just a refactor for reuse."""
from __future__ import annotations

import time

import numpy as np
from scipy.fft import fftfreq, rfftn, irfftn

ENV_CLASSES = ["void", "wall", "filament", "cluster"]


def step(t0, msg):
    print(f"[{time.time()-t0:8.1f}s] {msg}", flush=True)


def cic_deposit(pos: np.ndarray, origin: np.ndarray, cell_size: float, N: int, t0: float) -> np.ndarray:
    step(t0, f"CIC deposit onto {N}^3 grid (cell = {cell_size:.3f} Mpc/h) ...")
    u = (pos - origin) / cell_size
    in_bounds = np.all((u >= 0.0) & (u < N - 1), axis=1)
    n_in = int(in_bounds.sum())
    n_out = len(pos) - n_in
    if n_out > 0:
        step(t0, f"  WARNING: {n_out:,} of {len(pos):,} fall outside grid (clamping)")
    u = u[in_bounds]
    grid = np.zeros((N, N, N), dtype=np.float32)
    i0 = np.floor(u).astype(np.int64)
    f = (u - i0).astype(np.float32)
    i1 = i0 + 1
    for dx in (0, 1):
        for dy in (0, 1):
            for dz in (0, 1):
                wx = (1 - f[:, 0]) if dx == 0 else f[:, 0]
                wy = (1 - f[:, 1]) if dy == 0 else f[:, 1]
                wz = (1 - f[:, 2]) if dz == 0 else f[:, 2]
                w = (wx * wy * wz).astype(np.float32)
                ix = i0[:, 0] if dx == 0 else i1[:, 0]
                iy = i0[:, 1] if dy == 0 else i1[:, 1]
                iz = i0[:, 2] if dz == 0 else i1[:, 2]
                np.add.at(grid, (ix, iy, iz), w)
    step(t0, f"  CIC done; sum(grid) = {grid.sum():,.0f} (expected ~{n_in:,})")
    return grid


def gaussian_smooth_fft(field: np.ndarray, cell_size: float, R_s: float, t0: float):
    step(t0, f"Gaussian smoothing in k-space (R_s = {R_s:.2f} Mpc/h) ...")
    N = field.shape[0]
    fhat = rfftn(field)
    kx = 2 * np.pi * fftfreq(N, d=cell_size).astype(np.float32)
    ky = kx
    kz = 2 * np.pi * np.fft.rfftfreq(N, d=cell_size).astype(np.float32)
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing="ij")
    k2 = KX * KX + KY * KY + KZ * KZ
    fhat *= np.exp(-0.5 * k2 * (R_s ** 2)).astype(np.float32)
    out = irfftn(fhat, s=field.shape).astype(np.float32)
    return out, KX, KY, KZ, k2


def tidal_eigenvalues(delta_smooth, KX, KY, KZ, k2, t0):
    step(t0, "Tidal tensor T_ij = d^2 Phi / dx_i dx_j (k-space) ...")
    N = delta_smooth.shape[0]
    delta_k = rfftn(delta_smooth)
    inv_k2 = np.where(k2 > 0, 1.0 / k2, 0.0).astype(np.float32)
    phi_k = -delta_k * inv_k2
    components = {}
    for name, A, B in [("xx", KX, KX), ("yy", KY, KY), ("zz", KZ, KZ),
                       ("xy", KX, KY), ("xz", KX, KZ), ("yz", KY, KZ)]:
        components[name] = irfftn(-A * B * phi_k, s=delta_smooth.shape).astype(np.float32)
        step(t0, f"  T_{name} done")
    T = np.empty((N, N, N, 3, 3), dtype=np.float32)
    T[..., 0, 0] = components["xx"]
    T[..., 1, 1] = components["yy"]
    T[..., 2, 2] = components["zz"]
    T[..., 0, 1] = T[..., 1, 0] = components["xy"]
    T[..., 0, 2] = T[..., 2, 0] = components["xz"]
    T[..., 1, 2] = T[..., 2, 1] = components["yz"]
    del components
    eigs = np.linalg.eigvalsh(T)
    del T
    return eigs[..., 2].astype(np.float32), eigs[..., 1].astype(np.float32), eigs[..., 0].astype(np.float32)


def classify_vweb(lambda1, lambda2, lambda3, lambda_th: float):
    return ((lambda1 > lambda_th).astype(np.uint8)
            + (lambda2 > lambda_th).astype(np.uint8)
            + (lambda3 > lambda_th).astype(np.uint8))


def interpolate_to_galaxies(pos, origin, cell_size, N, cell_class, cell_log1pd, cell_eigs):
    u = (pos - origin) / cell_size
    idx = np.clip(np.floor(u + 0.5).astype(np.int64), 0, N - 1)
    ix, iy, iz = idx[:, 0], idx[:, 1], idx[:, 2]
    return {
        "env_class_idx": cell_class[ix, iy, iz],
        "env_density": cell_log1pd[ix, iy, iz],
        "env_lambda1": cell_eigs[0][ix, iy, iz],
        "env_lambda2": cell_eigs[1][ix, iy, iz],
        "env_lambda3": cell_eigs[2][ix, iy, iz],
    }
