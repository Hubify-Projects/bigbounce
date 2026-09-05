"""The honest run and its named shortcut variants, each emitting a trace.

Every variant returns (bandpowers, trace).  The trace is *measured* by the
harness (hashes of the actual intermediates, the instrumented 3j counter, wall
clock) except in S5, which deliberately forges an honest-looking trace over a
shortcut computation — the design note's in-principle-undetectable class.
"""

from __future__ import annotations

import hashlib
import platform
import time
from pathlib import Path

import numpy as np

import pcl
import wigner

VARIANTS = ("honest", "S1_skip_operator", "S2_truncate_operator",
            "S3_grid_interpolate", "S4_cache_substitute", "S5_metadata_forgery")


def h_array(a: np.ndarray) -> str:
    return hashlib.sha256(np.ascontiguousarray(a, dtype=np.float64).tobytes()).hexdigest()


def code_sha256() -> str:
    d = hashlib.sha256()
    for name in ("pcl.py", "wigner.py"):
        d.update(Path(__file__).with_name(name).read_bytes())
    return d.hexdigest()


def _env() -> dict:
    import healpy

    return {"numpy": np.__version__, "healpy": healpy.__version__,
            "python": platform.python_version(), "platform": platform.system()}


def run_variant(variant: str, nside: int, lmax: int, map_seed: int,
                cache: dict | None = None) -> tuple[np.ndarray, dict]:
    t0 = time.time()
    mask = pcl.make_mask(nside)
    sky = pcl.make_map(nside, lmax, map_seed)
    w_l = pcl.mask_power(mask, lmax)
    p_l = pcl.pseudo_cl(sky, mask, lmax)
    full_grid = list(range(lmax + 1))
    wigner.reset_counter()
    m = None
    grid = full_grid

    if variant in ("S1_skip_operator", "S5_metadata_forgery"):
        out = p_l / float(mask.mean())
    elif variant == "S2_truncate_operator":
        m = pcl.coupling_matrix(w_l, lmax, bandwidth=4)
        out = pcl.decouple(m, p_l)
    elif variant == "S3_grid_interpolate":
        grid = list(range(0, lmax + 1, 4))
        m = pcl.coupling_matrix(w_l, lmax, rows=np.array(grid))
        sub = m[np.ix_(grid[1:], grid[1:])] * 4.0
        coarse = np.linalg.solve(sub, p_l[grid[1:]])
        out = np.zeros(lmax + 1)
        out[2:] = np.interp(full_grid[2:], grid[1:], coarse)
    elif variant == "S4_cache_substitute":
        assert cache is not None, "S4 needs a prior honest run to substitute"
        m, out = cache["m"], cache["out"]
    else:
        m = pcl.coupling_matrix(w_l, lmax)
        out = pcl.decouple(m, p_l)

    trace = {
        "inputs": {"map_sha256": h_array(sky), "mask_sha256": h_array(mask),
                   "nside": nside, "lmax": lmax},
        "code": {"sha256": code_sha256()},
        "env": _env(),
        "intermediates": {
            "coupling_sha256": None if m is None else h_array(m),
            "coupling_shape": None if m is None else list(m.shape),
            "coupling_support": None if m is None else int(np.count_nonzero(m)),
            "ell_grid": grid,
            "n_wigner3j": wigner.counter(),
        },
        "wall_s": round(time.time() - t0, 4),
    }
    return out, trace
