# Cai–Li factor-of-2 certification scripts (f_NL = −35/16)

The sympy scripts that certify the corrected matter-bounce squeezed-limit
f_NL^local = −35/16 (App. A of the paper): vertex extraction from Cai et al.
2009 (arXiv:0903.0631) LaTeX source, exact vertex sum + squeezed/equilateral
limits, the spurious +(99/128)Σk³ discrepancy in the printed A_T, and the
Li et al. 2017 (arXiv:1612.02036) c_s=1 cross-check.

Inputs: the two papers' arXiv source tarballs (not redistributed here) —
fetch with `curl -L https://arxiv.org/e-print/0903.0631 -o 0903.0631.tar.gz`
(same for 1612.02036) and extract alongside these scripts.

Run: python3 cai_vertices.py && python3 cai_shape.py && python3 cai_conv.py && python3 cai_reconcile.py
Expected: vertex-sum squeezed limit = −35/16; equilateral −255/128; printed-A_T
discrepancy +(99/128)Σk³; Li Eq.(5.1) at c_s=1 = −35/16 exactly.
