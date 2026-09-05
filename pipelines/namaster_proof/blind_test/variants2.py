"""Batch-2 variant table: batch-1's S1-S5 plus the referee-requested S6.

S6_effective_multipole is the shortcut the paper's own Statement of Need calls
"a common shortcut": instead of applying the full window/coupling operator, the
analyst evaluates the coupling at one *effective multipole* per band and divides
through by that scalar transfer factor.  It is deliberately a *hard* class for
this verifier: the full mode-coupling matrix is genuinely built (so the l-grid,
the Wigner-3j count, the operator shape and support in the trace are all real and
all match the contract) and the shortcut is taken downstream, in the band
evaluation step, which the execution trace does not instrument.  Whether R1-R6
catch it is the open question of batch 2; no expected outcome is pre-declared.

Batch-1 objects (`variants.VARIANTS`, `variants.run_variant`) are untouched so
batch 1 still reproduces exactly.
"""

from __future__ import annotations

import time

import numpy as np

import pcl
import variants
import wigner

VARIANTS_V2 = variants.VARIANTS + ("S6_effective_multipole",)
BAND_WIDTH = 8
LMIN = 2


def _effective_multipole(m: np.ndarray, p_l: np.ndarray, lmax: int) -> np.ndarray:
    """Divide each band by the coupling evaluated at the band's effective l."""
    out = np.zeros(lmax + 1)
    for start in range(LMIN, lmax + 1, BAND_WIDTH):
        stop = min(start + BAND_WIDTH, lmax + 1)
        l_eff = int(round(0.5 * (start + stop - 1)))
        transfer = float(m[l_eff, LMIN:].sum())
        out[start:stop] = p_l[start:stop] / transfer
    return out


def run_variant(variant: str, nside: int, lmax: int, map_seed: int,
                cache: dict | None = None) -> tuple[np.ndarray, dict]:
    if variant != "S6_effective_multipole":
        return variants.run_variant(variant, nside, lmax, map_seed, cache=cache)

    t0 = time.time()
    mask = pcl.make_mask(nside)
    sky = pcl.make_map(nside, lmax, map_seed)
    w_l = pcl.mask_power(mask, lmax)
    p_l = pcl.pseudo_cl(sky, mask, lmax)
    wigner.reset_counter()
    m = pcl.coupling_matrix(w_l, lmax)          # full operator, genuinely built
    out = _effective_multipole(m, p_l, lmax)    # shortcut is downstream of it

    trace = {
        "inputs": {"map_sha256": variants.h_array(sky),
                   "mask_sha256": variants.h_array(mask),
                   "nside": nside, "lmax": lmax},
        "code": {"sha256": variants.code_sha256()},
        "env": variants._env(),
        "intermediates": {
            "coupling_sha256": variants.h_array(m),
            "coupling_shape": list(m.shape),
            "coupling_support": int(np.count_nonzero(m)),
            "ell_grid": list(range(lmax + 1)),
            "n_wigner3j": wigner.counter(),
        },
        "wall_s": round(time.time() - t0, 4),
    }
    return out, trace
