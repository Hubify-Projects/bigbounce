# Adjudication: the L×S second-order lapse monopole A₂(ε) on the uniform-density slice (2026-09-07)

**Status:** DONE 2026-09-07 — **VERDICT: A₂ = ε(3−ε)²/3 (S9's constraint solve is right) AND f^ρ = 5(ε−7)/8 = −55/16 (S9c's number is right, same variable); the S9 map's error is not in A₂ but in the composition step f^{in-in}/λ′ (§4).** Script + json alongside (9.6 s, all asserts pass). Independent adjudicator; reads only S9 (`psu_gates_S9_S10_2026_09_05.md`) and S9c (`psu_gate_S9c_evolution_residual_2026_09_05.md`).

## Dispute
- S9: from the exact comoving-gauge density surface ρ = φ̇²/(2N²)+V with lapse N = 1+α₁+α₂, α₂ = A₂ ζ_L ζ_S, the constraint solve gives the squeezed super-Hubble monopole A₂ = ε(3−ε)²/3 (= 9/8 at dust) and hence f^ρ = 5(2ε−15)/24 = −5/2 at dust.
- S9c: an exact separate-universe solution (closed form + DOP853) gives f^ρ = 5(ε−7)/8 = −55/16 on the uniform-density slice (all ε), −5 comoving, and shows the whole gap 5(6−ε)/24 sits in A₂: it requires A₂ = 2(3−ε)² = 2α_Lα_S/(ζ_Lζ_S) (= 9/2 at dust).

## Plan (one commit per step, explicit paths, no paper .tex edits)
1. Set up the ADM constraints in comoving gauge (δφ=0) for a constant-ε background, second order in ζ, long×short product, super-Hubble (gradient-free) limit; solve the Hamiltonian constraint for N₂ exactly (it is algebraic in the separate-universe limit).
2. Identify the L×S monopole; obtain A₂(ε) in closed form; compare with ε(3−ε)²/3 and 2(3−ε)².
3. Feed A₂ into S9's (S9.4) chain → f^ρ; compare with −5/2 and −55/16 at dust.
4. Validations: attractor ε→0; USR (ε→0 with growing mode m=3/ε−1 → the Namjoo 5/2 check through the same lapse formula); comoving-slice analogue → −5.
5. VERDICT + printable sentences; script `a2_lapse_monopole_adjudication_2026_09_07.py` + json; manifest; ledger rows 1 + 17.

## 1. Direct constraint solve (script Part A; the decisive computation for A₂)

Exact ADM objects in Maldacena's comoving gauge, $\delta\phi=0$, $h_{ij}=a^2e^{2\zeta}\delta_{ij}$, $N=1+\alpha$, $N_i=\partial_i\psi$:
$E_{ij}=\tfrac12(\dot h_{ij}-D_iN_j-D_jN_i)$ with $D_iN_j=\partial_i\partial_j\psi-\partial_i\zeta\partial_j\psi-\partial_j\zeta\partial_i\psi+\delta_{ij}\partial\zeta\!\cdot\!\partial\psi$,
$R^{(3)}=-a^{-2}e^{-2\zeta}[4\partial^2\zeta+2(\partial\zeta)^2]$, $\rho=\dot\phi^2/(2N^2)+V$;
Hamiltonian $R^{(3)}+N^{-2}(E^2-E_{ij}E^{ij})=2\rho$, momentum $D_j[N^{-1}(E^j{}_i-\delta^j_iE)]=0$ (exact: $J_i\propto\partial_i\phi=0$).
Two plane waves $\zeta=\zeta_L+\zeta_S+\zeta_{LS}$ ($k_L\hat z$, $k_S$ at angle $\mu$), constant-$\epsilon$ contraction $a=(-t)^{1/\epsilon}$,
$H=1/(\epsilon t)$, growing mode $\zeta\propto a^{-(3-\epsilon)}$; the $L\times S$ coefficient is extracted exactly ($\partial_l\partial_s$ at $l=s=0$).
Linear order is reproduced from the same code path: $N_1=\dot\zeta/H$ (momentum), $\psi=-\zeta/H+\chi$, $\partial^2\chi=a^2\epsilon\dot\zeta$ (Hamiltonian).
Gradient-free limit $k\to\delta k$, leading order (the projected momentum constraint is $O(\delta^2)$; $\psi_{LS}\sim\delta^{-2}$); then squeezed $k_L/k_S\to0$:
$$
N_{LS}=\frac{\dot\zeta_{LS}}{H}+A_2\,\zeta_L\zeta_S,\qquad
A_2=\underbrace{\epsilon(3-\epsilon)\,\mu\,\frac{k_S}{k_L}}_{\text{odd in }\mu\ (\text{translation})}
+\frac{\epsilon(3-\epsilon)}{2}\Big[(4-\epsilon)-(6-\epsilon)\mu^2\Big]+O(k_L/k_S),
$$
$$
\boxed{\ \langle A_2\rangle_{\mu}=\frac{\epsilon(3-\epsilon)^2}{3}\ =\ \frac98\ \text{at }\epsilon=\tfrac32\ }\qquad(\text{json }\texttt{A2\_monopole}).
$$
The pole coefficient $\epsilon(3-\epsilon)$ and the monopole are exactly S9's (`S9.A2_superhubble_growing`, $\mu^2\to\tfrac13$). Not $2(3-\epsilon)^2$.

**Exact limit that already excludes $2(3-\epsilon)^2$.** As $\epsilon\to0$ on the growing mode (USR-like: $\zeta\propto a^{-3}$; the same
argument covers inflationary USR) $\rho\to V=3H^2+O(\epsilon)$, the $O(k^0)$ shift divergence $\epsilon\dot\zeta$ and shear are $O(\epsilon)$, so the
Hamiltonian monopole reads $[(H+\dot\zeta)/N]^2=H^2$ exactly: $N=1+\dot\zeta/H$ with **no** quadratic term, $A_2=O(\epsilon)$.
S9's value is $O(\epsilon)$; $2(3-\epsilon)^2\to18$ is not the lapse of any background.

## 2. Exact local (monopole) system on a worldline (script Part B) — reproduces S9c's separate universe

With $u=1/N$, the Hamiltonian monopole $K^2/9=\rho/3$ gives $K=3H\sqrt{1+\epsilon(u^2-1)/3}$ and energy conservation along the normal
($n^\mu\partial_\mu\rho=-K(\rho+p)$, exact for $\delta\phi=0$) gives $\dot u=F(u)=\epsilon Hu-K+(3-\epsilon)H/u$; $F'(1)=-(3-\epsilon)H$ (growing mode),
$F''(1)/F'(1)=c=(\epsilon-6)/3$, so $u_{LS}=c\,u_Lu_S$. The fluid e-fold rate is $NK/3=K/(3u)$; integrating from the early flat limit
($W\to0$) and crossing $t=t_f$ (comoving) or $\rho=\bar\rho(t_f)$ (uniform density) gives, initial label by construction,
$$
f^{\rm loc}_\phi=-5,\qquad f^{\rm loc}_\rho=\frac{5(\epsilon-7)}{8}=-\frac{55}{16},\qquad \lambda'/\lambda=2\quad(\text{all }\epsilon;\ \text{asserted}).
$$
This is S9c's separate universe (same numbers) obtained from the ADM monopole equations directly, so the SU variable **is** $\delta N_c$ read on the
$\rho$-surface — the same variable S9's (S9.3) continues. The two lanes therefore disagree on the same quantity, and §1 says $A_2$ is not where.

## 3. Three-way consistency: the momentum-constraint lapse, the local system, and the lab's in-in monopole

Kinematics: $u=1/N=1-\dot\zeta/H-A_2\zeta_L\zeta_S+2\alpha_L\alpha_S$ at $L\times S$, with $\zeta_{LS}=c_\zeta\zeta_L\zeta_S\propto a^{-2(3-\epsilon)}$
(late-time, $O(1/W)$ initial-data pieces dropped). Equating to $u_{LS}=c\,(3-\epsilon)^2\zeta_L\zeta_S$ with the derived $A_2$:
$$
c_\zeta=-\frac{(3-\epsilon)(6-\epsilon)}{3},\qquad f^{\rm in\text{-}in}_{\rm mono}=\tfrac56c_\zeta=-\frac{5(3-\epsilon)(6-\epsilon)}{18}=-\frac{15}{8}\ \text{at dust},
$$
which is exactly the ledger-row-1 in-in monopole ($-\tfrac{35}{16}+\tfrac{15}{16}\cdot\tfrac13$) and, at general $\epsilon$, exactly the
$f^{\rm in\text{-}in}/\lambda'=5(\epsilon-6)/12$ implied by S9's own table ($f^\rho_{\rm S9}-f^{\rho,\rm init}_{\rm map}$ with $f_{\rm map}=-\tfrac58$).
With $A_2^{\rm req}=2(3-\epsilon)^2$ instead, the same identity would demand $f^{\rm in\text{-}in}_{\rm mono}=-\tfrac{15}{4}$ at dust — twice the adjudicated value.

## 4. The step in S9's map that carries the gap (script Part C) — the decisive equation

S9 assembles $f^\rho=f^{\rm in\text{-}in}/\lambda'+f^\rho_{\rm map}$ with $\lambda'=\lambda+H\delta t^{(1)}_S/\zeta_S=2\lambda$ "asserted from the same objects".
But $\delta N_c=\lambda\zeta$ is a multiplicative map for **any** time dependence (it is $\zeta-\tfrac13\!\int\!\epsilon\dot\zeta\,dt$), whereas the
$\rho$-surface shift is a **derivative operator**, $H\delta t^{(1)}=-\dot\zeta/(3H)$. On the linear growing mode $\dot\zeta=-(3-\epsilon)H\zeta$ it gives
$\lambda\zeta$ (hence $\lambda'=2\lambda$); on the second-order piece $\zeta_2\propto a^{-2(3-\epsilon)}$, which is what the late-time in-in bispectrum
consists of, $\dot\zeta_2=-2(3-\epsilon)H\zeta_2$ and it gives $2\lambda\zeta_2$. Therefore (asserted symbolically in the script)
$$
\delta N_{c,\rho}=\lambda'\zeta_1+\underbrace{3\lambda}_{\neq\,\lambda'}\zeta_2+M_\rho\,\zeta_1\zeta_1,\qquad
\boxed{\ f^\rho=\frac{3\lambda}{\lambda'}\frac{f^{\rm in\text{-}in}}{\lambda'}+f^\rho_{\rm map}=\frac32\frac{f^{\rm in\text{-}in}}{\lambda'}+f^\rho_{\rm map}\ }.
$$
With the derived $A_2$, $f^{\rm in\text{-}in}_{\rm mono}$ of §3 and the map monopole computed from the ADM objects
($f_{\rm extra}=\tfrac56M_{\rm extra}/\lambda'^2=5(\epsilon-3)/24$ plus the comoving shift-divergence kernel
$\partial_iN^i|_{LS}=-\tfrac{2\epsilon}{3}(3-\epsilon)^3H\zeta_L\zeta_S$, i.e. $f^\phi_{\rm map}=-5\epsilon/6$, $-5\epsilon/24$ in $\rho$ normalisation;
total $f^\rho_{\rm map}=-\tfrac58$ for all $\epsilon$, equal to S9's initial-label monopole and to the local system's requirement):
$$
f^{\rm in\text{-}in}/\lambda'+f^\rho_{\rm map}=\frac{5(2\epsilon-15)}{24}\ (\text{S9, reproduced}),\qquad
\tfrac32f^{\rm in\text{-}in}/\lambda'+f^\rho_{\rm map}=\frac{5(\epsilon-7)}{8}\ (\text{= the exact local system}),\qquad
\text{gap}=\tfrac12\frac{f^{\rm in\text{-}in}}{\lambda'}=\frac{5(\epsilon-6)}{24}.
$$
The gap is S9c's $5(6-\epsilon)/24$ exactly, for every $\epsilon$ — produced with S9's own $A_2$. S9c's "$A_2^{\rm req}=2(3-\epsilon)^2$" is what one
obtains by forcing the gap into the lapse while keeping the $\lambda'$-on-$\zeta_2$ assumption ("the combination in which $\zeta_2$ cancels, $\lambda'=2\lambda$");
it is not a lapse (§1, and it fails the $\epsilon\to0$ limit). Equivalently: $1/N$ does carry the second-order monopole $2\alpha_L\alpha_S-A_2\zeta_L\zeta_S$.

## 5. Validations (all asserted in the script)
- Background and linear constraints reproduced from the exact ADM expressions ($N_1=\dot\zeta/H$, $\partial^2\chi=a^2\epsilon\dot\zeta$).
- Pole $\epsilon(3-\epsilon)\mu k_S/k_L$: odd in $\mu$, zero monopole (translation, label-only) — agrees with S9's eq. (3) and the threading note.
- $\epsilon\to0$ (USR-like growing mode $a^{-3}$; inflationary USR by the same Hamiltonian argument): $A_2\to0$ — S9 passes, $2(3-\epsilon)^2$ fails.
- Attractor ($\dot\zeta_L=0$): every factor $(3-\epsilon)$ in $A_2$ is a $\dot\zeta/(H\zeta)$; the quadratic lapse vanishes with $\dot\zeta$ — not discriminating (as S9c noted).
- Comoving analogue: the local system gives the established initial-label composition $-5$ for all $\epsilon$; the same objects give $\lambda'/\lambda=2$.
- Three-way closure: momentum-constraint $A_2$ + local system ⇒ in-in monopole $-15/8$ at dust = row-1 adjudicated value; general-$\epsilon$ form matches S9's table inversion.
- $f_{\rm map}$ from the ADM objects (Hamiltonian-constraint second-order shift divergence + $M_{\rm extra}$) $=-5/8=$ the local system's requirement.

## VERDICT
**Neither framing as posed; each lane is right about its own number.** $A_2=\epsilon(3-\epsilon)^2/3$ (S9's constraint solve stands; the "named step"
`solve_cross` is correct). $f^\rho=5(\epsilon-7)/8=-55/16$ at dust (the separate-universe value stands, and it is the same variable — $\delta N_c$ on the
uniform-density surface, initial label). S9's $-5/2$ comes from applying the growing-mode factor $\lambda'=2\lambda$ to the second-order $\zeta_2$ in
$f^{\rm in\text{-}in}/\lambda'$; the correct weight is $3\lambda$. S9c localised the gap correctly to "one number" but mis-assigned it to the lapse because it
inherited the same $\lambda'$ assumption. Consequences: S9's table row "$f^\rho_{\rm NL}$ initial label $=5(2\epsilon-15)/24$" is superseded by
$5(\epsilon-7)/8$ (isotropy claim unaffected: the correction is a monopole); the residual in S9.4/S9c §5 is closed; nothing in paper-su's comoving
statements ($-5$, $\lambda=1-\epsilon/3$) changes. The ledger's "two lanes" now agree on both slices.

## Sentences paper-su and A3M may print
1. *On the uniform-density surface the fluid e-fold perturbation of the constant-$\epsilon$ growing mode has squeezed monopole $f_{\rm NL}=5(\epsilon-7)/8$ ($-55/16$ at $\epsilon=3/2$), obtained both from an exact separate-universe integration and from the comoving-gauge in-in bispectrum continued through the second-order Hamiltonian and momentum constraints (second-order lapse monopole $\epsilon(3-\epsilon)^2/3$); the two routes agree for every $\epsilon$.*
2. *The continuation is not a rescaling: the time shift to the uniform-density surface acts on the second-order curvature perturbation with weight $3\lambda$ rather than the linear-mode factor $2\lambda$, and omitting this shifts the monopole by $5(6-\epsilon)/24$.*
3. (May **not** print) any statement that the second-order lapse monopole is $2(3-\epsilon)^2$, or that the separate universe and the in-in continuation disagree on the uniform-density slice.

## Integrity note
Part A (the constraint solve) was written and run with $A_2$ unknown, and its output compared with both claimed values only after the monopole was
extracted; Part B was written from the ADM monopole equations without reading S9c's script (only its §2 result was known); the composition diagnosis
(§4) followed from the Part-B/Part-A consistency and was then verified against S9's quoted $5(2\epsilon-15)/24$ and S9c's gap, both reproduced exactly.

## Artifacts
`a2_lapse_monopole_adjudication_2026_09_07.py` (sympy 1.14, 9.6 s, all asserts) · `.json` · manifest `reproducibility/manifests/experiments/a2-lapse-monopole-adjudication.json`.
