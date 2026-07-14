# P1A exact-convention NJL and density recomputation

**Paper:** `arxiv/paper1a_ech_nogo.tex` v1A.0.117
**Script:** `arxiv/scripts/njl_gap_equation_route1.py`
**Generated result:** `arxiv/scripts/njl_gap_equation_route1_results.json`

This artifact fixes the conventions used by P1A and records the exact
calculation. It does not assert a regulator-independent or beyond-mean-field
condensate exclusion.

## Planck convention

P1A uses the unreduced mass

\[
M_{\rm Pl}=G_N^{-1/2}=1.22089\times10^{19}\ {\rm GeV}.
\]

Therefore

\[
\kappa=8\pi G_N=\frac{8\pi}{M_{\rm Pl}^{2}},
\]

not \(M_{\rm Pl}^{-2}\). The latter equals \(\kappa\) only when the reduced
Planck mass \(\bar M_{\rm Pl}=(8\pi G_N)^{-1/2}\) is used.

## Hard-four-dimensional-cutoff gap equation

For the exact declared interaction

\[
\mathcal L_{\rm int}=G_s(\bar\psi\psi)^2,
\]

mean field gives \(M=-2G_s\langle\bar\psi\psi\rangle\). A Euclidean
four-ball cutoff gives

\[
I_4=\frac{1}{16\pi^2}
\left[\Lambda^2-M^2\ln\left(1+\frac{\Lambda^2}{M^2}\right)\right],
\]

and the Dirac trace and \(N_fN_c\) degeneracy give

\[
\langle\bar\psi\psi\rangle
=-\frac{N_fN_cM}{4\pi^2}
\left[\Lambda^2-M^2\ln\left(1+\frac{\Lambda^2}{M^2}\right)\right].
\]

Thus

\[
M=\frac{G_sN_fN_cM}{2\pi^2}
\left[\Lambda^2-M^2\ln\left(1+\frac{\Lambda^2}{M^2}\right)\right],
\qquad
G_{\rm crit}=\frac{2\pi^2}{N_fN_c\Lambda^2}.
\]

## Sign and magnitude are separate results

The paper's Fierz convention gives

\[
G_{\rm scalar}=-\frac{3\kappa}{64}<0,
\qquad
G_A=+\frac{3\kappa}{32}=2|G_{\rm scalar}|.
\]

For the real homogeneous scalar gap equation, division by nonzero \(M\) makes
the right-hand side proportional to \(G_s\) times a positive factor. Hence the
negative scalar coupling admits no nonzero scalar-mass solution in this
declared direct-channel mean-field model. This is the surviving sign result.
It is not a global-potential, Fierz-independent, axial-condensation, or
beyond-mean-field statement.

The separate coefficient-magnitude diagnostic is

\[
\frac{|G_{\rm scalar}|}{G_{\rm crit}}
=\frac{3N_fN_c}{16\pi}\frac{\Lambda^2}{M_{\rm Pl}^2}.
\]

The axial column below is only \(G_A\) divided by the same *scalar* threshold;
it is not an independently derived axial-vector critical coupling.

| \(N_fN_c\) | \(\Lambda/M_{\rm Pl}\) | scalar ratio | axial benchmark |
|---:|---:|---:|---:|
| 1 | 1 | 0.05968310 | 0.11936621 |
| 1 | \(1/\sqrt{0.274}\) | 0.21782155 | 0.43564309 |
| 3 | 1 | 0.17904931 | 0.35809862 |
| 3 | \(1/\sqrt{0.274}\) | 0.65346464 | 1.30692928 |
| 9 | 1 | 0.53714793 | 1.07429587 |
| 9 | \(1/\sqrt{0.274}\) | 1.96039392 | 3.92078783 |

The former blanket magnitude-subcritical claim is false. The last scalar row
is formally above threshold, and three axial coefficient benchmarks exceed
unity. The \(N_fN_c=9\) row is the three-flavor, three-color benchmark; it is
not called a single-species case.

## Density bound

With \(\hbar c=1.973269804\times10^{-5}\ {\rm eV\,cm}\),

\[
100\ {\rm cm}^{-3}=7.68351\times10^{-13}\ {\rm eV}^3.
\]

Consequently,

\[
\kappa n^2=9.9542\times10^{-80}\ {\rm eV}^4
=3.5571\times10^{-69}\rho_\Lambda,
\]

which is 68.45 orders below \(\rho_\Lambda=(2.3\ {\rm meV})^4\). Including
the actual \(3/16\) contact coefficient gives
\(1.8664\times10^{-80}\ {\rm eV}^4=6.6695\times10^{-70}\rho_\Lambda\).

No equation of state is inferred from \(\langle J^5\rangle=0\). A vanishing
one-point current does not determine the state-dependent stress tensor of
\(\langle J^5J^5\rangle\). The finite-density amplitude bound alone is enough
to exclude this term as the observed late-time acceleration in the specified
state.
