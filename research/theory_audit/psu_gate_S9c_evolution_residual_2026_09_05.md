# paper-su gate S9c — the dropped shift-divergence term in the δN uniform-density lane (2026-09-05)

**Status:** IN PROGRESS (plan header committed first, anti-stall).

## Plan

Open item after S9b (`psu_gate_S9b_intrinsic_term_2026_09_05.md` §5): the δN lane's uniform-density value
$f^{\delta N}_{\rm NL}=5(\epsilon-7)/8=-55/16$ (`fnl_matter_contraction_second_method_2026_09_02.{md,py}`) differs from the
second-order uniform-density threading map's $f^\rho=5(2\epsilon-15)/24=-5/2$ (`psu_gates_S9_S10_2026_09_05.md`, S9) by
$5(6-\epsilon)/24=15/16$ at dust. S9b showed the intrinsic initial-data channels vanish as $1/W$, so the residual lives in the
super-Hubble evolution between the flat initial slice and the uniform-density final slice. Candidate: the shift-divergence term
$\partial_iN^i$ that the lane's separate-universe integration drops, i.e. the exact worldline identity
$\delta N_c=\zeta-\tfrac13\int\partial_iN^i\,dt$ (`threading_map_second_order_2026_09_04.md`, eq. 2) generalised to $\rho$-threading.

Steps (one commit each, script `psu_gate_S9c_evolution_residual_2026_09_05.py` + json):
1. Evolution with the shift kept: $\zeta_\rho$ / $\delta N_{c,\rho}$ to second order from the flat slice in a constant-$\epsilon$
   non-attractor background, versus the lane's $N^i=0$ evolution; isolate the shift-divergence contribution to $f_{\rm NL}$.
2. Test whether it equals $5(6-\epsilon)/24$ (general $\epsilon$; $15/16$ at $\epsilon=3/2$) or state the residual.
3. Validate: attractor (term vanishes), USR (NFS $5/2$ unaffected), comoving-threading cross-check ($-5$, initial label).
4. Consequence + verdict (RECONCILED / NOT / UNRESOLVED), printable sentences, manifest, ledger rows 1 + 17.
