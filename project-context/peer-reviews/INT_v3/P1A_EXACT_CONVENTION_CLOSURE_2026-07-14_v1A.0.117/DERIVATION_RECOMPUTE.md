# P1A derivation and recomputation record

## 1. Planck convention

The paper declares the unreduced Planck mass

\[
M_{\rm Pl}=G_N^{-1/2}=1.22089\times10^{19}\ {\rm GeV}.
\]

It must therefore use

\[
\kappa=8\pi G_N=\frac{8\pi}{M_{\rm Pl}^2}
=\frac{1}{\bar M_{\rm Pl}^2},
\qquad
\bar M_{\rm Pl}=(8\pi G_N)^{-1/2}.
\]

All active P1A formulas and numerical evaluations now use this convention.

## 2. Hard four-dimensional cutoff gap equation

For the declared interaction

\[
\mathcal L_{\rm int}=G_s(\bar\psi\psi)^2,
\]

the direct scalar mean-field relation is

\[
M=-2G_s\langle\bar\psi\psi\rangle.
\]

With a hard Euclidean four-ball cutoff, the radial integral is

\[
I_4(M,\Lambda)=\int_{p_E^2\leq\Lambda^2}
\frac{d^4p_E}{(2\pi)^4}\frac{1}{p_E^2+M^2}
=\frac{\Lambda^2-M^2\ln(1+\Lambda^2/M^2)}{16\pi^2}.
\]

The Dirac trace and the `N_f N_c` degeneracy then give

\[
\langle\bar\psi\psi\rangle
=-\frac{N_fN_cM}{4\pi^2}
\left[\Lambda^2-M^2\ln\left(1+\frac{\Lambda^2}{M^2}\right)\right],
\]

and hence

\[
M=\frac{G_sN_fN_cM}{2\pi^2}
\left[\Lambda^2-M^2\ln\left(1+\frac{\Lambda^2}{M^2}\right)\right].
\]

Linearizing at `M -> 0` yields

\[
G_{\rm crit}=\frac{2\pi^2}{N_fN_c\Lambda^2}.
\]

This is the threshold for this exact interaction normalization and this exact
hard four-dimensional regulator. It is not a regulator-independent statement.

## 3. Sign result and magnitude diagnostic

The declared Fierz convention gives

\[
G_{\rm scalar}=-\frac{3\kappa}{64},
\qquad
G_A=+\frac{3\kappa}{32}=2|G_{\rm scalar}|.
\]

For nonzero real `M`, the bracket in the scalar gap equation is positive. The
right-hand side therefore cannot equal the positive left-hand normalization
when `G_s < 0`. The repulsive scalar coefficient admits no nonzero real
homogeneous scalar-mass solution in this declared direct-channel mean-field
model. This does not establish a Fierz-independent, axial, global-potential, or
beyond-mean-field no-condensate theorem.

Using the corrected Planck convention, the separate scalar magnitude ratio is

\[
\frac{|G_{\rm scalar}|}{G_{\rm crit}}
=\frac{3N_fN_c}{16\pi}\frac{\Lambda^2}{M_{\rm Pl}^2}.
\]

| `N_f N_c` | `Lambda/M_Pl` | scalar ratio | axial coefficient / scalar threshold |
|---:|---:|---:|---:|
| 1 | 1 | 0.05968310 | 0.11936621 |
| 1 | `1/sqrt(0.274)` | 0.21782155 | 0.43564309 |
| 3 | 1 | 0.17904931 | 0.35809862 |
| 3 | `1/sqrt(0.274)` | 0.65346464 | 1.30692928 |
| 9 | 1 | 0.53714793 | 1.07429587 |
| 9 | `1/sqrt(0.274)` | 1.96039392 | 3.92078783 |

The blanket magnitude-subcritical claim is false. The last scalar benchmark is
formally supercritical in magnitude. The axial column is exactly twice the
scalar column but is only a coefficient benchmark against the scalar threshold;
it is not a derived axial criticality test. `N_fN_c=9` is the three-flavor,
three-color benchmark, not a single-species case.

## 4. Density bound

Using

\[
\hbar c=1.973269804\times10^{-5}\ {\rm eV\,cm},
\qquad n=100\ {\rm cm}^{-3},
\]

gives

\[
n=7.68350556945\times10^{-13}\ {\rm eV}^3,
\quad
\kappa=1.68611342609\times10^{-55}\ {\rm eV}^{-2}.
\]

Thus the conservative coefficient-one bound is

\[
\kappa n^2=9.95418269628\times10^{-80}\ {\rm eV}^4
=3.55708516489\times10^{-69}\rho_\Lambda,
\]

or `68.4489057367` orders below
`rho_Lambda=(2.3 meV)^4=2.79841e-11 eV^4`. Including the actual `3/16`
contact coefficient gives `1.86640925555e-80 eV^4`, or
`6.66953468417e-70 rho_Lambda` (`69.1759044646` orders below).

## 5. Equation-of-state boundary

No value of `w` is inferred from `\langle J^5\rangle=0`. A one-point current
does not determine the state-dependent composite expectation
`\langle J^5J^5\rangle` or its stress tensor. The finite-density amplitude
bound alone excludes the contact term as the observed late-time acceleration
for the specified state.

The executable recomputation and all full-precision values are frozen in
`proof/njl_gap_equation_route1.v1A.0.117.py` and
`proof/njl_gap_equation_route1_results.v1A.0.117.json`.
