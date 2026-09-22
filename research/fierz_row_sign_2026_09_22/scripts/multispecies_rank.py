#!/usr/bin/env python3
"""
Does the single-species operator degeneracy (rank 3 among {S,V,T,A,P})
survive when the fermion carries the colour/flavour multiplicity the paper's
own gap equation assumes (degeneracy factor N_c N_f)?

Lane bb-LS15-fierz-sign, 2026-09-22.

Construction: psi_{a,i}, a = Dirac index (4), i = species index (N).  The
channel operators are species-singlet in EACH bilinear,
  O_X = sum_idx (psibar_i Gamma^idx psi_i)(psibar_j Gamma_idx psi_j),
so the tensor carries delta_{ij} delta_{kl}.  The monomial
psibar_{ai} psi_{bj} psibar_{ck} psi_{dl} is antisymmetric under the
simultaneous exchange (ai)<->(ck) and under (bj)<->(dl), exactly as in the
N=1 case; only the index range changes.
"""
import json
import itertools
import numpy as np

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex); Z2 = np.zeros((2, 2), dtype=complex)
blk = lambda a, b, c, d: np.block([[a, b], [c, d]])

g0 = blk(I2, Z2, Z2, -I2)
gmm = [g0] + [blk(Z2, s, -s, Z2) for s in (s1, s2, s3)]
g = [1j * x for x in gmm]                      # mostly-plus
eta = np.diag([-1.0, 1.0, 1.0, 1.0])
g5 = 1j * g[0] @ g[1] @ g[2] @ g[3]
glow = [sum(eta[m, n] * g[n] for n in range(4)) for m in range(4)]
sig = lambda a, b: 0.5j * (a @ b - b @ a)
CH = ["S", "V", "T", "A", "P"]
PAIRS = {
    "S": [(np.eye(4, dtype=complex), np.eye(4, dtype=complex))],
    "V": [(g[m], glow[m]) for m in range(4)],
    "A": [(g[m] @ g5, glow[m] @ g5) for m in range(4)],
    "P": [(g5, g5)],
    "T": [(sig(g[m], g[n]), sig(glow[m], glow[n]))
          for m, n in itertools.combinations(range(4), 2)],
}

out = {}
for N in (1, 2, 3):
    D = 4 * N
    mats = {}
    for X, prs in PAIRS.items():
        T = np.zeros((D, D, D, D), dtype=complex)
        for up, dn in prs:
            U = np.kron(up, np.eye(N))          # (a,i),(b,j) = Gamma_ab delta_ij
            L = np.kron(dn, np.eye(N))
            T += np.einsum("AB,CD->ABCD", U, L)
        # project onto the operator subspace: antisym in (A,C), antisym in
        # (B,D), symmetric under swapping the pairs
        T = 0.25 * (T - np.einsum("CBAD->ABCD", T)
                    - np.einsum("ADCB->ABCD", T) + np.einsum("CDAB->ABCD", T))
        T = 0.5 * (T + np.einsum("CDAB->ABCD", T))
        mats[X] = T.reshape(-1)
    M = np.stack([mats[X] for X in CH], axis=1)
    sv = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(sv > 1e-9 * sv[0]))
    out[f"N_species={N}"] = dict(
        dirac_x_species_components=D, operator_rank=rank,
        singular_values=[float(x) for x in sv],
        five_channels_independent=bool(rank == 5),
    )

out["reading"] = (
    "rank 5 means the five species-singlet quartics are linearly independent "
    "as operators, so the Fierz decomposition — and therefore the mean-field "
    "scalar coupling G_s read off from it — is unambiguous.  rank 3 (N=1) is "
    "the single-species degeneracy that makes the word 'unique' an "
    "overstatement for a strictly one-species reading."
)
print(json.dumps(out, indent=2))
