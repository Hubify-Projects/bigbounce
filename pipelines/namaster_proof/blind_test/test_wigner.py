"""Independent check of wigner.wigner3j_000 against sympy.physics.wigner."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wigner import counter, reset_counter, wigner3j_000  # noqa: E402

CASES = [(1, 1, 0), (2, 2, 0), (2, 2, 2), (4, 4, 2), (10, 10, 4), (37, 41, 6)]


def main() -> int:
    try:
        from sympy.physics.wigner import wigner_3j
    except ImportError:
        print("SKIP: sympy not installed")
        return 0
    reset_counter()
    worst = 0.0
    for l1, l2, l3 in CASES:
        ref = float(wigner_3j(l1, l2, l3, 0, 0, 0))
        got = wigner3j_000(l1, l2, l3)
        worst = max(worst, abs(got - ref))
    assert counter() == len(CASES), "counter did not track evaluations"
    print(f"max abs deviation vs sympy over {len(CASES)} cases: {worst:.3e}")
    assert worst < 1e-12, "3j kernel disagrees with sympy"
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
