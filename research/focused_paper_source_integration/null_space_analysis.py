#!/usr/bin/env python3
"""Retired compatibility entry point.

The former benchmark-fit null-space scan treated three displayed benchmark
values as the only constraints on a polynomial that is, in fact, fixed by the
exact four-vertex derivation.  Its sampled uncertainty was artificial and must
not be regenerated or propagated.
"""

raise RuntimeError(
    "RETIRED: artificial benchmark-fit null-space uncertainty. "
    "Run scripts/exact_shape_analysis.py instead."
)
