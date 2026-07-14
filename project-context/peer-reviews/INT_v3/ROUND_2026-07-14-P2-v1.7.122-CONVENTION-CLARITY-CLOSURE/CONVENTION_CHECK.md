# P2 primordial-to-LSS convention check

The manuscript defines the local curvature convention

`B_zeta^loc = (6/5) f_NL [P_zeta P_zeta + cyc.]`.

During matter domination, `Phi=(3/5)zeta`, so

- `B_Phi=(3/5)^3 B_zeta`, and
- `P_Phi=(3/5)^2 P_zeta`.

Therefore the coefficient in the potential basis is exactly

`(3/5)^3 (6/5) / (3/5)^4 = 2`,

giving

`B_Phi^loc = 2 f_NL [P_Phi P_Phi + cyc.]`.

This matches `outputs/c13_independent_bounce_fisher.json`. The LSS response then uses the same dimensionless `f_NL` in `Delta b=f_NL b_phi/M`; the C8 convention specializes `b_phi=2 delta_c(b-p)` with `p=1`. No additional factor of `3/5` is introduced.
