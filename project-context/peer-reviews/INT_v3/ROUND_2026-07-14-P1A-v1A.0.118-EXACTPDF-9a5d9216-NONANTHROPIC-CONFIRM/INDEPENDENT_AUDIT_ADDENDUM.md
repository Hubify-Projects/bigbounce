# Independent audit addendum to the v1A.0.118 truth audit

This addendum records the independent post-commit audit of
`P1A_CONFIRMATION_TRUTH_AUDIT.md`.  It does not alter the raw reviewer files or
their verdicts.

The independent audit confirmed the load-bearing result in CDEX-M1:

- Eq. (A1) and the checker label rows as source classes, while `F*src` selects
  the source column.
- The scalar exchange coefficient is `+1`, so
  `G_scalar=-3*kappa/16` and every scalar ratio in v1A.0.118 is too small by a
  factor of four.
- The repulsive sign and no-real-nonzero-scalar-gap conclusion survive.

It also required a convention nuance before correction.  Literal Nieves--Pal
Eq. (2.14) is the c-number-spinor map.  In its normalized basis the axial
source row is `(-1,-1/2,0,-1/2,+1)`.  Turning that relation into an
anticommuting field-operator identity introduces an overall Grassmann minus,
giving scalar `+1` and axial `+1/2` in the declared exchange ordering.  The
original contact prefactor therefore gives a post-Fierz axial coefficient
`-3*kappa/32` in that ordering, not the `+3*kappa/32` sign stated by
v1A.0.118.  The magnitude is unchanged.

Accordingly, the correction must:

1. distinguish the c-number and anticommuting-operator maps explicitly;
2. use a coherent source-row orientation rather than merely transposing the
   old ad hoc matrix;
3. remove the checker's invalid single-species eigenspace statement; and
4. report only `|G_A|=3*kappa/32` unless an axial sign is derived and labeled
   under a specific operator-order convention.

The v1A.0.118 truth-audit status remains **MAJOR REVISION**.  Its scalar
correction and factor-four scan are unchanged by this nuance; its use of an
axial magnitude benchmark is retained, while any implied axial sign is
superseded by this addendum and the v1A.0.119 correction bundle.
