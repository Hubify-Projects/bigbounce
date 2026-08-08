# P1A v1A.0.119 Fierz operator-convention correction audit

## Verdict

The v1A.0.118 Fierz row/column major is **closed by computation and edit** in
v1A.0.119.  This bundle does not claim peer-review convergence: no fresh
review dispatch was authorized for this round.  A new exact-PDF confirmation
remains required before P1A can return to `ACCEPT`/`MINOR` status.

## Frozen identity

- Source SHA-256:
  `a7a74e2d2e9b9cb3a5e159ce071c3258782473e2b7f64ce1e931babb7a6b6d87`
- PDF SHA-256:
  `dfe2a47a3221888477dfa47adb9cddf7ebbe25acc96185c3af9e58a1e7c065d0`
- PDF: 7 pages, 154,010 bytes
- Corrected checker commit: `70d4cf86`

## Convention chain

The corrected appendix and checker now keep two maps distinct.

1. In the normalized c-number-spinor convention of Nieves and Pal,
   `e_I(1234)=sum_J F_c[I,J] e_J(1432)`.  Rows are source classes; columns are
   produced classes.  The axial source is the fourth row:

   `(-1, -1/2, 0, -1/2, +1)`.

2. The normalization uses `Gamma_A^mu=i gamma^mu gamma5` and `n_A=-i`, so
   `e_A` is the physical `J5.J5` product after the phases are combined.

3. Rearranging anticommuting fields requires one Grassmann exchange:
   `F_op=-F_c`.  The axial operator row in the declared ordering is therefore

   `(+1, +1/2, 0, +1/2, -1)`.

4. Multiplying the original `-3*kappa/16` contact coefficient by the scalar
   exchange coefficient `+1` gives

   `G_scalar=-3*kappa/16`.

5. The axial entry is not used as a signed physical claim.  The paper reports
   only `|G_A|=3*kappa/32`, divided by the scalar threshold as a magnitude
   benchmark.

The independent checker `fierz_lemma_check.py` builds the exact matrix, asserts
its involution, performs an explicit gamma-trace scalar projection, applies the
Grassmann sign, and contains no single-species eigenspace argument.  It exits
with `FIERZ CONVENTION CHECK: PASS`.

## Corrected gap diagnostic

For the unchanged hard-Euclidean-four-ball scalar gap equation,

`G_crit = 2*pi^2/(N_f*N_c*Lambda^2)`.

Using the unreduced Planck convention `kappa=8*pi/M_Pl^2` now gives

`R_S = 3*N_f*N_c/(4*pi) * Lambda^2/M_Pl^2`.

| `N_f N_c` | `Lambda/M_Pl` | corrected `R_S` | `R_A=|G_A|/G_crit` |
|---:|---:|---:|---:|
| 1 | 1 | 0.23873241 | 0.11936621 |
| 1 | `1/sqrt(0.274)` | 0.87128618 | 0.43564309 |
| 3 | 1 | 0.71619724 | 0.35809862 |
| 3 | `1/sqrt(0.274)` | 2.61385855 | 1.30692928 |
| 9 | 1 | 2.14859173 | 1.07429587 |
| 9 | `1/sqrt(0.274)` | 7.84157566 | 3.92078783 |

Three scalar rows are formally magnitude-supercritical.  This does not change
the declared direct-channel sign result: the real homogeneous scalar gap
equation has a positive bracket, so its negative `G_scalar` cannot support a
nonzero real mass root.  The conclusion remains explicitly regulator-,
channel-, and mean-field-specific.

## Finding closure

- **CDEX-M1:** closed.  Matrix orientation, normalized basis, Grassmann sign,
  scalar coefficient, all six scalar ratios, abstract/body/table statements,
  checker, and JSON are synchronized.
- **CDEX-m1:** closed.  The stale pointer to a nonexistent convention footnote
  is replaced by an active inline explanation of the half- versus full-weight
  torsion definition.
- **OAI-m1:** closed.  `R_A` is now defined explicitly through `|G_A|`; no
  positive axial sign is claimed, and its one-half relation to `R_S` is stated.
- **OAI-m2:** closed.  Appendix B states that `gamma=0.274` defines only the
  formal cutoff stress point; the coupling uses the maximal Einstein--Cartan
  limit.
- **OAI-m3:** no correctness edit required.  The pointwise Bianchi result and
  nonzero-torsion scope boundary remain explicit.

## Active-claim scan

After removing percent comments and complete LaTeX `comment` environments,
the active source has zero occurrences of:

- `G_scalar=-3*kappa/64`;
- old scalar values `0.05968`, `0.21782`, `0.17905`, `0.65346`, `0.53715`, or
  `1.96039`;
- `twice the scalar ratio`;
- the old `F*src`/`F_norm` orientation or the invalid eigenspace claim; and
- a signed `+3*kappa/32` axial assertion.

The old values remain only in frozen historical review/closure evidence and in
P1U historical site timeline prose.  Those records describe prior versions
and were not rewritten.  No P1A site claim surface contains these exact old
values.

## Scope and state

Per the parent correction contract, this round does not update `version.json`,
site data, SSOT, Convex, served PDF mirrors, tags, or remotes.  `version.json`
was already modified by another live lane and was left untouched.  The version
and date are synchronized in the P1A source and verified on PDF page 1.
