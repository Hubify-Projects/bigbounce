# When does the isotropic separate universe fail? A criterion for the $O(1)$ breakdown of $\delta N$ in non-attractor phases

**BigBounce theory-audit lane · 2026-09-04 · novelty lift #2 (`project-context/NOVELTY_AUDIT_2026-09-04.md` C2) · proposed NEXT_SCIENCE_LEDGER row 16**

## Plan (written first, anti-stall)

Input (frozen, not re-derived here): the exact threading identity
$\delta N_c(x_f)=\zeta(t_f,x_f)-\tfrac13\int\partial_iN^i\,dt$ along the fluid worldline, and the constant-$\epsilon$
second-order map $f_{\delta N}=f^{\rm in\text{-}in}/\lambda+f_{\rm map}$, $\lambda=1-\epsilon/3$,
$f_{\rm map}=-\tfrac{5\epsilon}{4}+\tfrac{5\epsilon}{4}\mu^2$
(`threading_map_second_order_2026_09_04.{md,py,json}`; in-in inputs from `fnl_monopole_adjudication_2026_09_03.md`).

Steps, each committed by explicit path as it lands:
1. Linear order for a **general** history $\epsilon(t)$, $\zeta_L(t)$: derive $\lambda$ as a functional of the
   history; identify the dimensionless control parameter and show where $\lambda\ne1$ comes from.
2. Second order at constant $\epsilon$: $f_{\rm map}(\epsilon,\mu)$, its general-$w$ form, and the $\epsilon\to0$
   (USR-type) and $\dot\zeta\to0$ (attractor) limits; state precisely why $\delta N$ with $N(\phi,\pi)$ works in
   USR although the shift is $O(1/k_L)$ there too.
3. Validations: dust contraction ($\epsilon=3/2$), USR inflation, attractor slow-roll, ekpyrotic contraction
   ($\epsilon\gg3$, both $\zeta$ modes). Script + JSON (exact sympy, closed forms; no new constraint solve).
4. The criterion in one line; literature placement (Namjoo–Firouzjahi–Sasaki 1210.3692; Chen–Firouzjahi–Namjoo–Sasaki
   1301.5699; Pajer–Schmidt–Zaldarriaga 1305.0824; Dai–Pajer–Schmidt 1504.00351; Cai et al. 1712.09998;
   Bravo–Mooij–Palma–Pradenas 1711.02680 / 1711.05290; Passaglia–Hu–Motohashi 1812.08243; Artigas–Grain–Vennin
   2110.11720; Jackson et al. 2311.03281); what is new relative to each; the sentences a short note could claim.
5. VERDICT; manifest; ledger row-16 proposal line (not added to the ledger by this lane).

Conventions as in the inputs: $B_{\rm sq}=\tfrac{12}{5}f\,P_LP_S$, $\mu=\hat k_L\!\cdot\!\hat k_S$, $\epsilon=-\dot H/H^2$
(positive in contraction), $\delta N_c$ = e-folds of the fluid (zero-shift) congruence = the variable the isotropic
separate universe computes.

(Derivation, validations, criterion and verdict follow as they are completed.)

---
