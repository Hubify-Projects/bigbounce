# Lane (b) — numerical in-in evaluation of Δf_NL^bounce on the A2 backgrounds

**Status:** PLAN COMMITTED (results appended by `bounce_cubic_inin.py`).
**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` item #2, second half. Lane (a) =
`../lane_a_vertex_table/` (vertex table + regularisation prescription); lane (c) = model-specific
(Horndeski / dressed-metric) vertex corrections, separate.
**Date:** 2026-09-03 · **Venue:** local CPU · **Cost:** $0.

## Plan

1. **Mode functions.** Integrate `mu'' + (k^2 - a''/a) mu = 0` from the adiabatic (matter) vacuum of
   A2 §4 across the bounce on the three A2 backgrounds (`a2_transmission_linear.bg_quintin`,
   `bg_lqc`, `bg_poly`), for a super-Hubble band `k eta_B in [1e-3, 0.3]`. S1 (geometric, z = a) so
   `zeta = mu/a`.
2. **In-in.** For EVERY vertex of lane (a)'s table (V1–V7) plus the redefinition terms R1–R4,
   evaluate, in the squeezed isoceles configuration and the lab convention
   `B = -2 Im[ u1u2u3(eta_*) int d eta c_V^conf(eta) sum_{S3} K_V prod_j T_j[u*] ]`,
   `f_NL = (5/6) B / (P1P2+P1P3+P2P3)`, over the bounce window `[eta_1, eta_2] = [-eta_B, +eta_B]`.
   The contraction value −35/16 is INPUT (ledger #1), not recomputed.
3. **Tests.** eta_*-independence (redefinition/boundary terms evaluated post-bounce), window
   independence (vary eta_1, eta_2), step-size convergence, normalisation gate (local `F zeta^2`
   ⇒ `f_NL = (5/3) F`), Wronskian gate.
4. **Comparison** with lane (a)'s closed form `Δf_NL[V2,S1] = −(5/24) rho_B`.
5. **Combined statement** `f_NL^after = T·(−35/16) + Δf_NL^bounce` per background, scheme-labelled,
   validity `k eta_B << 1`.
6. **S2** reported as a documented divergence (d_cut scaling exponent), never as a number.

Integrity: no tuning to any target; every number in §Results is emitted by the committed script.
