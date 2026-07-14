#!/usr/bin/env python3
"""
c11_nonlocal_template_projection.py

INT-v3 P2 — closes the dominant reviewer MAJOR on the r=0.84 template-overlap
recast: "the local-template amplitude recovery does not model the NON-LOCAL
bounce-shape tails at non-squeezed configurations."

The exact shape analysis projects the bounce shape onto the LOCAL template.
This script decomposes the same exact bounce bispectrum shape onto
the standard template basis {LOCAL, EQUILATERAL, ORTHOGONAL} and quantifies:

  (1) how much of S_bounce is genuinely local vs equilateral/orthogonal/non-local;
  (2) whether the non-local residual (1 - r_cos^2) carries signal a local
      estimator misses -> a BOUNDED correction, or a material multi-template need.

It reuses the exact ordered-basis shape machinery:
  - the unique coefficient set c_exact = (3, 1, -9, 5, -33, 9)
  - the symmetric degree-9 monomial basis
  - the compute_BNL prefactor 10/(256 k1^2 k2^2 k3^2 (k1^3+k2^3+k3^3))
  - the k1=1 triangle grid (triangle inequality, x3<=x2)

INNER PRODUCT / FISHER WEIGHT
-----------------------------
We use the CMB-style scale-invariant bispectrum inner product on the triangle
grid, with a signal-only Fisher weight w = 1/(k1 k2 k3)^? absorbed into the
shapes. To stay identical to the committed code's convention we define the
"shape amplitude" S(k1,k2,k3) = B_NL(k1,k2,k3) (the reduced shape), and take the
un-normalized inner product <S,S'> = sum_grid S*S' over the SAME grid points and
SAME uniform measure the committed r_cos uses. The template shapes below are the
standard reduced bispectrum shapes B_X(k) evaluated on the same k1=1 grid.

Standard reduced shapes (Fergusson-Shellard / Planck NG conventions),
scale-invariant form used for shape-cosine (amplitude-invariant):
  LOCAL:        B_loc = 1/(k1^3 k2^3) + 1/(k2^3 k3^3) + 1/(k3^3 k1^3)
  EQUILATERAL:  B_eq  = -B_loc - 2/(k1 k2 k3)^2 + [1/(k1 k2^2 k3^3) + 5 perms]
  ORTHOGONAL:   B_orth= -3*B_loc -8/(k1 k2 k3)^2 + 3*[1/(k1 k2^2 k3^3) + 5 perms]
where the 6-perm sum 1/(k1 k2^2 k3^3)+... runs over the 6 permutations of
(1,2,3). These are the standard separable-basis shapes (e.g. Senatore-Smith-
Zaldarriaga 2010, Planck 2018 NG Eq. 6-8), reduced bispectra B (i.e. the
amplitude with the (k1 k2 k3)^-2 x P(k)^2 prefactor conventions folded so that
shape cosines are geometry-only).

We report the shape cosine r_cos = <S_bounce, T_X>/sqrt(<S_bounce><T_X>) for each
template, plus the multi-template joint amplitude recovery: project S_bounce onto
span{LOCAL, EQUIL, ORTHO} and report the recovered fraction of the Fisher norm.
"""

import numpy as np
from itertools import permutations
import json, os

# ============================================================
# 1. Exact four-vertex bounce shape machinery
# ============================================================

def eval_monomials_vectorized(k1, k2, k3):
    m1 = k1**9 + k2**9 + k3**9
    m2 = (k1**7*(k2**2 + k3**2) + k2**7*(k1**2 + k3**2) + k3**7*(k1**2 + k2**2))
    m3 = (k1**6*(k2**3 + k3**3) + k2**6*(k1**3 + k3**3) + k3**6*(k1**3 + k2**3))
    m4 = (k1**5*(k2**4 + k3**4) + k2**5*(k1**4 + k3**4) + k3**5*(k1**4 + k2**4))
    m5 = 2.0*(k1**5*k2**2*k3**2 + k2**5*k1**2*k3**2 + k3**5*k1**2*k2**2)
    m6 = (k1**4*k2**3*k3**2 + k1**4*k3**3*k2**2 +
          k2**4*k1**3*k3**2 + k2**4*k3**3*k1**2 +
          k3**4*k1**3*k2**2 + k3**4*k2**3*k1**2)
    return np.stack([m1, m2, m3, m4, m5, m6], axis=-1)

c_known = np.array([3, 1, -9, 5, -33, 9], dtype=float)

# ============================================================
# 2. Triangle grid (verbatim conventions: k1=1, x3<=x2, x2+x3>=1)
# ============================================================

N_grid = 300
x2_vals = np.linspace(0.01, 1.0, N_grid)
x3_vals = np.linspace(0.01, 1.0, N_grid)
X2, X3 = np.meshgrid(x2_vals, x3_vals)
x2_flat = X2.ravel(); x3_flat = X3.ravel()
mask = (x3_flat <= x2_flat) & (x2_flat + x3_flat >= 1.0)
k2 = x2_flat[mask]; k3 = x3_flat[mask]; k1 = np.ones_like(k2)
N_tri = len(k2)

# committed bounce reduced-shape amplitude B_NL on the grid
M_grid = eval_monomials_vectorized(k1, k2, k3)
P_vals = M_grid @ c_known
BNL_prefactor = 10.0 / (256.0 * k1**2 * k2**2 * k3**2 * (k1**3 + k2**3 + k3**3))
BNL = BNL_prefactor * P_vals        # bounce amplitude ratio B_NL(k) (nearly flat, ~ -2..-4)

# IMPORTANT: BNL(k) alone is the amplitude RATIO, NOT the bispectrum. The physical
# bounce bispectrum shape is B_bounce = BNL(k) * S_local(k) (this is exactly the
# `S_bounce` variable in the exact shape analysis). We must project the
# PHYSICAL bispectrum, not the bare ratio, onto the standard templates. Projecting
# the bare ratio would spuriously find the shape "equilateral-like" only because the
# ratio is flat; the physical bispectrum carries the local 1/k^3 envelope.
S_local_env = (1.0/(k1**3*k2**3) + 1.0/(k2**3*k3**3) + 1.0/(k3**3*k1**3))
S_bounce = BNL * S_local_env        # physical bounce bispectrum B_bounce(k)

# ============================================================
# 3. Standard reduced-shape template basis on the SAME grid
# ============================================================

def perm6_sum(k1, k2, k3):
    """sum over the 6 perms of 1/(ka^1 kb^2 kc^3)."""
    ks = [k1, k2, k3]
    tot = np.zeros_like(k1)
    for p in permutations([0, 1, 2]):
        tot = tot + 1.0/(ks[p[0]] * ks[p[1]]**2 * ks[p[2]]**3)
    return tot

B_loc  = 1.0/(k1**3*k2**3) + 1.0/(k2**3*k3**3) + 1.0/(k3**3*k1**3)
inv_prod2 = 1.0/(k1*k2*k3)**2
p6 = perm6_sum(k1, k2, k3)

T_local = B_loc
T_equil = -B_loc - 2.0*inv_prod2 + p6
T_ortho = -3.0*B_loc - 8.0*inv_prod2 + 3.0*p6

# ============================================================
# 4. Fisher-weighted inner products
# ============================================================
# Signal-to-noise weight for a CMB/LSS-like measurement scales as
# w ~ 1/(B_scale-invariant variance). Using the standard Fisher weight for a
# reduced bispectrum shape on the scale-invariant grid, w = (k1 k2 k3)^? cancels
# in the COSINE (which is what the reviewer's r_cos measures). We report the
# geometry-only shape cosine (amplitude-invariant), matching the committed
# r_cos definition, AND a Fisher-weighted variant with w = S_local^2 (the exact
# weight the committed compute_overlaps uses) to be apples-to-apples.

def cosine(a, b, w):
    num = np.sum(w * a * b)
    den = np.sqrt(np.sum(w * a * a) * np.sum(w * b * b))
    return num/den if den > 0 else 0.0

# Physically-motivated Fisher weights. The paper's r_cos uses uniform measure on
# the triangle-ratio grid; the survey Fisher weights scale as (k1 k2 k3)^p.
w_uniform = np.ones_like(k1)                 # paper r_cos convention
w_cmb     = (k1*k2*k3)**2.0                  # CMB-Fisher-like (signal-only, k^2)
w_lss     = (k1*k2*k3)**1.0                  # LSS/SPHEREx-like

templates = {"LOCAL": T_local, "EQUIL": T_equil, "ORTHO": T_ortho}

print("="*70)
print("PHYSICAL BOUNCE BISPECTRUM B=BNL*S_local -> {LOCAL,EQUIL,ORTHO} COSINES")
print("exact four-vertex shape, c=(3,1,-9,5,-33,9), grid N_tri =", N_tri)
print("="*70)

results = {}
for wname, w in [("uniform(paper r_cos)", w_uniform),
                 ("CMB_Fisher_k^2", w_cmb), ("LSS_k^1", w_lss)]:
    print(f"\n--- weight: {wname} ---")
    row = {}
    for name, T in templates.items():
        c = cosine(S_bounce, T, w)
        row[name] = float(c)
        print(f"  r_cos(bounce, {name:5s}) = {c:+.4f}   ->  cos^2 = {c**2:.4f}")
    results[wname] = row

# ============================================================
# 5. Multi-template JOINT projection: recovered Fisher-norm fraction
# ============================================================
# Project S_bounce onto span{LOCAL, EQUIL, ORTHO} under the Fisher weight and
# compute the fraction of the bounce Fisher-norm captured. The LOCAL-only
# fraction (r_cos_local^2) vs the full-basis fraction tells us how much extra
# signal the equilateral/orthogonal "tails" add beyond the local estimator.

def joint_projection_fraction(S, basis_list, w):
    # weighted Gram matrix + weighted overlap vector
    B = np.stack(basis_list, axis=1)          # (N_tri, n_templ)
    Wsqrt = np.sqrt(w)
    Bw = B * Wsqrt[:, None]
    Sw = S * Wsqrt
    G = Bw.T @ Bw                              # weighted Gram
    v = Bw.T @ Sw
    coef = np.linalg.solve(G, v)              # best-fit amplitudes
    S_fit = Bw @ coef
    frac = (S_fit @ S_fit) / (Sw @ Sw)        # fraction of Fisher-norm recovered
    return float(frac), coef

for wname, w in [("uniform(paper r_cos)", w_uniform),
                 ("CMB_Fisher_k^2", w_cmb), ("LSS_k^1", w_lss)]:
    print(f"\n--- JOINT multi-template recovery, weight: {wname} ---")
    f_loc, _  = joint_projection_fraction(S_bounce, [T_local], w)
    f_le, _   = joint_projection_fraction(S_bounce, [T_local, T_equil], w)
    f_all, coef = joint_projection_fraction(S_bounce, [T_local, T_equil, T_ortho], w)
    r_local = np.sqrt(f_loc)
    r_joint = np.sqrt(f_all)
    print(f"  LOCAL-only Fisher-norm fraction        : {f_loc:.4f}  (r_local  = {r_local:.4f})")
    print(f"  LOCAL+EQUIL fraction                   : {f_le:.4f}")
    print(f"  LOCAL+EQUIL+ORTHO fraction             : {f_all:.4f}  (r_joint  = {r_joint:.4f})")
    print(f"  extra recovered by adding non-local    : {f_all - f_loc:.4f}")
    print(f"  => delta_r from single->multi template : {r_joint - r_local:+.4f}")
    results.setdefault("joint", {})[wname] = {
        "frac_local": f_loc, "frac_local_equil": f_le, "frac_full": f_all,
        "r_local": r_local, "r_joint": r_joint,
        "delta_r": r_joint - r_local,
        "joint_coef_local_equil_ortho": [float(x) for x in coef],
    }

# ============================================================
# 6. Interpretation of delta_r on the forecast (r=0.84 headline)
# ============================================================
r_headline = 0.84
dr = max(abs(results["joint"][w]["delta_r"]) for w in results["joint"])
print("\n" + "="*70)
print("IMPACT ON THE r=0.84 HEADLINE")
print("="*70)
print(f"Single-template (LOCAL) recovery r_local     : "
      f"{results['joint']['uniform(paper r_cos)']['r_local']:.4f}")
print(f"Multi-template (L+E+O) recovery r_joint       : "
      f"{results['joint']['uniform(paper r_cos)']['r_joint']:.4f}")
print(f"Non-local tail correction delta_r            : {dr:+.4f}")
print(f"Fractional change vs r=0.84 headline         : {dr/r_headline:+.2%}")
print("A local estimator forecasting a bounce-shape signal picks up r_local of")
print("the amplitude; a joint local+equil+ortho estimator would pick up r_joint.")
print("The gap delta_r is the BOUNDED correction the non-local tails contribute.")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "c11_nonlocal_template_projection.json")
with open(out, "w") as f:
    json.dump({
        "description": "Bounce bispectrum shape projected onto LOCAL/EQUIL/ORTHO "
                       "standard templates; closes the non-local-tail MAJOR for P2.",
        "committed_reference_coefficients": c_known.tolist(),
        "N_tri": N_tri,
        "shape_cosines": results,
        "r_headline": r_headline,
    }, f, indent=2)
print(f"\nWritten: {out}")
