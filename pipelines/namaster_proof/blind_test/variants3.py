"""Batch-3 variant table: batch-2's arms plus `S4b_cache_crossrun`, and the new
`pseudo_cl` instrumented intermediate that rule R7 reads.

Batch-1 and batch-2 objects (`variants.VARIANTS`, `variants2.VARIANTS_V2` and
their `run_variant`s) are untouched, so both earlier batches still reproduce.

`S4b_cache_crossrun` models the cache substitution R6's *second* disjunct was
written for and batch 2 never exercised: the run genuinely builds its own
operator and declares its own input map, but publishes the bandpowers of an
earlier run **in this same batch** rather than the published reference run.
"""

from __future__ import annotations

import numpy as np

import pcl
import variants
import variants2

VARIANTS_V3 = (variants2.VARIANTS_V2[:5] + ("S4b_cache_crossrun",)
               + variants2.VARIANTS_V2[5:])


def pseudo_spectrum(nside: int, lmax: int, map_seed: int) -> list[float]:
    """The run's own pseudo-C_l: measured, not declared by the variant."""
    mask = pcl.make_mask(nside)
    sky = pcl.make_map(nside, lmax, map_seed)
    return [float(x) for x in pcl.pseudo_cl(sky, mask, lmax)]


def run_variant(variant: str, nside: int, lmax: int, map_seed: int,
                cache: dict | None = None) -> tuple[np.ndarray, dict]:
    if variant == "S4b_cache_crossrun":
        assert cache is not None and cache.get("prior_out") is not None
        _own, trace = variants2.run_variant("honest", nside, lmax, map_seed, cache=cache)
        out = np.asarray(cache["prior_out"], dtype=float)
    else:
        out, trace = variants2.run_variant(variant, nside, lmax, map_seed, cache=cache)
    trace["intermediates"]["pseudo_cl"] = pseudo_spectrum(nside, lmax, map_seed)
    return out, trace
