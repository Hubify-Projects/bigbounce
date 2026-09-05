"""Batch-4 variant table: batch-3's arms minus `S4b` (its R6 cross-run disjunct
is already exercised and reported), plus the two adversaries the R3 referee's
MAJOR 1 and MAJOR 2 describe.

`S7_r7_aware_effective` is MAJOR 1 made concrete.  It runs `S6` exactly -- the
full mode-coupling operator is genuinely built, the shortcut is downstream -- and
then computes R7's spot rows with the verifier's own `verify3.spot_rows`, from
the same mask hash and the same published-bandpower hash the verifier will use,
and overwrites the declared pseudo-spectrum on exactly those six rows with the
consistent value `(M C)`.  Every other entry stays at the honestly measured
value.  Cost: six entries of a matrix the run already holds.

`S8_omit_pseudo_cl` is MAJOR 2 made concrete: an `S6` run whose receipt simply
does not carry `intermediates.pseudo_cl`.

Batch-1/2/3 objects are untouched, so all three earlier batches still reproduce.
"""

from __future__ import annotations

import numpy as np

import pcl
import variants
import variants2
import variants3
import verify3

VARIANTS_V4 = (("honest", "S1_skip_operator", "S2_truncate_operator",
                "S3_grid_interpolate", "S4_cache_substitute",
                "S5_metadata_forgery", "S6_effective_multipole")
               + ("S7_r7_aware_effective", "S8_omit_pseudo_cl"))
LMIN = 2


def _full_operator(nside: int, lmax: int, cache: dict | None) -> np.ndarray:
    """The mask is fixed for the batch, so M is too; reuse it when offered."""
    if cache is not None and cache.get("m_full") is not None:
        return cache["m_full"]
    return pcl.coupling_matrix(pcl.mask_power(pcl.make_mask(nside), lmax), lmax)


def run_variant(variant: str, nside: int, lmax: int, map_seed: int,
                cache: dict | None = None) -> tuple[np.ndarray, dict]:
    if variant not in ("S7_r7_aware_effective", "S8_omit_pseudo_cl"):
        return variants3.run_variant(variant, nside, lmax, map_seed, cache=cache)

    out, trace = variants3.run_variant("S6_effective_multipole", nside, lmax,
                                       map_seed, cache=cache)
    if variant == "S8_omit_pseudo_cl":
        trace["intermediates"].pop("pseudo_cl", None)
        return out, trace

    published = [float(x) for x in out]
    rows = verify3.spot_rows(trace["inputs"]["mask_sha256"],
                             verify3.band_hash(published), lmax)
    m = _full_operator(nside, lmax, cache)
    c = np.asarray(published, dtype=float)
    p = np.asarray(trace["intermediates"]["pseudo_cl"], dtype=float)
    # no marker of any kind is written into the receipt: the published artifact
    # must be indistinguishable from S6 except in the six forged entries.
    for l1 in rows:
        p[l1] = float(m[l1, LMIN:] @ c[LMIN:])
    trace["intermediates"]["pseudo_cl"] = [float(x) for x in p]
    return out, trace
