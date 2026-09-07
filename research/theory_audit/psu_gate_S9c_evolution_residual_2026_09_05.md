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

---

## 1. Where the shift can and cannot enter (exact, before any computation)

Write the exact worldline identity of `threading_map_second_order_2026_09_04.md` eq. (1) once more,
$NK=\tfrac{d}{dt}\ln\sqrt h\,|_{\rm worldline}-\partial_iN^i$, with $K=\nabla_\mu n^\mu$ the expansion of the
normal (= fluid, $\delta\phi=0$) congruence. Two different objects are called "$\zeta$" in the two lanes:

* the **metric variable** $\zeta_{\rm Mald}=\tfrac13\delta\ln\sqrt h$ (Maldacena, in-in), and
* the **e-fold variable** $\delta N_c=\int\tfrac13NK\,dt-\bar N$ of the fluid congruence (separate universe).

The shift divergence is *exactly* their difference, eq. (2) of that note: $\delta N_c=\zeta_{\rm Mald}-\tfrac13\int\partial_iN^i\,dt$.
The $\delta N$ lane never forms $\ln\sqrt h$: its output is the e-fold count of a local FRW patch, $N_{\rm loc}=\int H_{\rm loc}\,d\tau$,
and $H_{\rm loc}$ is obtained from the local Friedmann + Klein–Gordon equations, i.e. from the equations of the **$n$-frame
quantities** $(K,\ d\phi/d\tau,\ \rho)$. In the 3+1 equations projected on $n^\mu$ the shift never appears explicitly — it is a
threading choice — and the $O(k^0)$ super-Hubble equations of the normal congruence are (units $8\pi G=1$)
$$
\tfrac23K^2-\sigma_{ij}\sigma^{ij}+R^{(3)}=2\rho,\qquad
\dot K=-\tfrac13K^2-\sigma^2-\tfrac12(\rho+3p)+D_ia^i,\qquad
\ddot\phi+K\dot\phi=-V'(\phi)\ (\text{dots}=d/d\tau,\ D_i\phi=0),
$$
with $R^{(3)}=O(k^2/a^2)$ and $D_ia^i=\partial^2\alpha/a^2=O(k^2)$. The isotropic separate universe is these equations with
$\sigma=0$. Hence the **only** $O(k^0)$ term the lane drops is $\sigma^2$; and in comoving gauge the shear *is* the traceless
part of the shift gradient, $\sigma_{ij}=-a^{-2}(\partial_i\partial_j\psi-\tfrac13\delta_{ij}\partial^2\psi)=-\epsilon\dot\zeta\,(\hat k_i\hat k_j-\tfrac13\delta_{ij})$
on the growing mode (the $\partial_iN^i$ trace part is what eq. (2) already accounts for). Its long–short cross term is
$2\sigma_L{:}\sigma_S\propto\dot\zeta_L\dot\zeta_S\,(\mu^2-\tfrac13)$, a **pure quadrupole**: it cannot move an isotropic number
(this is the Bianchi-I finding of `fnl_bianchi_separate_universe_2026_09_03.*`, "traceless, zero monopole", seen from the constraint side).

**Consequence for the plan.** The candidate named in the plan — "the lane drops $\partial_iN^i$ in the evolution" — is not a
dynamical omission: $\partial_iN^i$ enters only the *definition* of the variable, and S9 (`psu_gates_S9_S10_2026_09_05.md`) already keeps it
exactly when it continues $\zeta_{\rm Mald}\to\delta N_{c,\rho}$. If the separate-universe dynamics is exact for the monopole,
the lane's $\delta N$ on the $\rho$-slice and S9's $\delta N_{c,\rho}$ are the **same variable** and must agree in the monopole;
an isotropic residual $5(6-\epsilon)/24$ then cannot be an evolution term and must be a bookkeeping error in one of the two
computations. §2 tests this with an independent, exact separate-universe integration (both final slices, general $\epsilon$),
which decides which side carries the error before any further term is hunted.
