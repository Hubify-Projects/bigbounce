# Threading map at second order: Maldacena's comoving $\zeta$ vs the zero-shift $\delta N_c$ in a non-attractor contraction

**BigBounce theory-audit lane · 2026-09-04 · NEXT_SCIENCE_LEDGER row 11(c)**

## Plan (written first, anti-stall)

Goal: derive the mechanism behind the identity recorded in
`fnl_monopole_adjudication_2026_09_03.md` §4:
$[L]-\delta N_c = 5\epsilon/4 = (5/12)(3\epsilon)$, i.e. the second-order part of the
threading map from Maldacena's comoving gauge ($N_i=\partial_i\psi$, $\psi\supset a^2\epsilon\,\partial^{-2}\dot\zeta$,
$O(1/k_L)$) to the zero-shift threading in which the isotropic separate universe computes
$\delta N_c=(1-\epsilon/3)\zeta$.

Steps (each committed by explicit path as it lands):
1. Set up the coordinate transformation $x^i\to \tilde x^i = x^i+\xi^i(t,x)$ that removes the long
   mode's shift; compute $\xi^i$ on the growing mode; show $\xi$ is $O(1/k_L)\times\zeta_L$ so $k_L\xi=O(1)$.
2. Transform the short-mode curvature perturbation to second order: the argument shift
   $\zeta_S(x)\to\zeta_S(x+\xi)$ (pure translation) plus the Jacobian/dilation piece
   $\partial_i\xi^i$ and the time re-threading of the slicing. Identify which pieces survive at
   $O(k_L^0)$ in the squeezed limit.
3. Compute the induced squeezed bispectrum contribution of each piece in the adjudication's
   conventions ($B_{\rm sq}=(12/5)f\,P_LP_S$, $\mu=\hat k_L\cdot\hat k_S$), general constant $\epsilon$.
4. Validate in sympy: $\epsilon=3/2$ gives $5/4$; general $\epsilon$ gives $5\epsilon/4$; attractor
   $\epsilon\to0$ (constant $\zeta$, $\dot\zeta_L\to0$) gives 0 with the Maldacena consistency
   relation untouched; USR if tractable.
5. Verdict + Appendix-A paragraph; script + json; manifest; ledger row 11(c) line.

(Derivation, validation and verdict follow below as they are completed.)
