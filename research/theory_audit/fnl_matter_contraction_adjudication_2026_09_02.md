# Adjudication: the local $f_{\rm NL}$ of a canonical matter contraction ($w=0$, $\epsilon=3/2$, $c_s=1$)

**BigBounce theory-audit lane · 2026-09-02 · Fable-tier adjudication (NEXT_SCIENCE_LEDGER #1, closure)**

Artifacts
- script: `research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py` (deterministic, exact sympy; prints every intermediate)
- result: `research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.json`
- manifest: `reproducibility/manifests/experiments/p2-fnl-adjudication-inin-from-scratch.json`
- venue: local CPU · cost \$0 · wall clock 131.6 s (8 parallel sympy workers) · script sha256 `67dd4842aaa7978310c7ead714d666bff6ab8fc523e7d0bb815844fa517264fc`

---

## VERDICT

$$
\boxed{\,f_{\rm NL}^{\rm local}\big|_{k_1\ll k_2=k_3}\;=\;-\frac{35}{16}\,}
$$

**Definition (exact).** $f_{\rm NL}^{\rm local}\equiv\lim_{k_1\to0}\tfrac{10}{3}\,\mathcal A(k_1,k,k)/(2k^3)$ where $\langle\zeta_{\mathbf k_1}\zeta_{\mathbf k_2}\zeta_{\mathbf k_3}\rangle=(2\pi)^7\delta^3(\sum\mathbf k_i)\,\mathcal P_\zeta^2\,\mathcal A/\prod k_i^3$, $\zeta$ is Maldacena's comoving-gauge curvature perturbation ($h_{ij}=a^2e^{2\zeta}\delta_{ij}$, $\delta\phi=0$), evaluated at the end of the matter contraction $\eta_B$ with $|k\eta_B|\ll1$, Bunch–Davies vacuum, canonical field, $\epsilon=3/2$, $\eta_{\rm sr}=0$. This is equivalent to $\zeta=\zeta_g+\tfrac35f_{\rm NL}\zeta_g^2$ for the local template and is the definition used by Cai *et al.* 2009 (Eqs. 20–21) and Li *et al.* 2016 (Sec. 5). The limit is end-time independent at leading order (corrections are $\mathcal O(k^2\eta_B^2)$) but **orientation dependent**: with $\mu=\hat{\mathbf k}_1\!\cdot\!\hat{\mathbf k}$,

$$
f_{\rm NL}^{\rm sq}(\mu)\;=\;-\frac{35}{16}+\frac{15}{16}\mu^2
\qquad(\text{isoceles }\mu\to0:\ -35/16;\ \text{angle-averaged monopole } -15/8;\ \text{quadrupole } 15/16).
$$

**Which published number is correct.** $-35/16$ (Li *et al.* 2016 Eq. 5.1 at $c_s=1$; BigBounce Paper 2). Cai *et al.* 2009's $-35/8$ is exactly a factor 2 too large.

**Mechanical origin of each discrepancy.**

| discrepancy | origin (computed, not inferred) |
|---|---|
| Cai 2009: $-35/8$ vs $-35/16$ | Cai's printed shape function Eq. (37) is **correct** (this work reproduces it monomial by monomial). All three amplitudes they quote from it — local $-35/8$, equilateral $-255/64$, folded $-9/4$ — are each **exactly $2\times$** the from-scratch values $-35/16$, $-255/128$, $-9/8$. The slip is a uniform factor 2 in the amplitude-parameter step (their Eqs. 38–40, effectively $f_{\rm NL}=\tfrac{20}{3}\mathcal A/\sum k^3$), not in any vertex, not in Wick/commutator bookkeeping. |
| second method 2026-09-02: $-55/16$ vs in-in | **(c) different variable.** That calculation is $\delta N$ to uniform-*density* slices. Reproduced here for general $\epsilon$: $f_\rho=5(\epsilon-7)/8$. On the same growing mode the *comoving* $\delta N$ gives $f_c=-5$ (all $\epsilon$), and already at linear order $\zeta_\rho=2\zeta_c$. In a non-attractor phase uniform-$\rho$ and comoving slices differ at $\mathcal O(1)$. |
| comoving $\delta N$ ($-5$) vs in-in ($-35/16$) | **(b′) not an $\mathcal O(k^2)$ term.** The $k\to0$ limit of a comoving-gauge growing mode is *not* an FRW patch: its trace perturbation is $\delta K=\epsilon\dot\zeta$ and it carries a traceless shear $\sigma^i{}_j=(\hat k_i\hat k_j-\tfrac13\delta_{ij})\,\epsilon\dot\zeta$ of the **same order** (Sec. 7 of the script). An isotropic separate universe keeps the trace and drops the shear; the in-in keeps both, which is why its squeezed limit carries a $\mu^2$ quadrupole. Neither the isoceles value nor the monopole of the in-in is a separate-universe quantity. |
| (d) end-time / surface terms | Excluded: the leading imaginary part is the pure $S^{-12}$ term ($S=-\eta_B$); the next is $\mathcal O(k^2S^2)$; the field-redefinition (boundary) term is evaluated exactly at $\eta_B$ and reproduces Cai's row identically. |
| (a) error in one in-in route | Excluded within in-in: the from-scratch per-vertex results equal Cai's four source-level rows and Paper 2's per-vertex table exactly. |

**Independence audit (coordinator's question).** Li *et al.* 2016 is a generalisation, not an independent check: their four $c_s=1$ rows are Cai's rows coefficient-for-coefficient and their Eq. (4.19) equals Cai's Eq. (37) (checked symbolically: difference 0). Quintin *et al.* 2015 (arXiv:1508.04141, text after their Eq. for $\mathcal L_3$) *quotes* "the authors of [Cai 2009] found $f_{\rm NL}^{\rm local}=-35/16$" — a citation with the corrected number, no computation. The present script is the only computation of this quantity that does not transcribe any per-vertex expression from those papers.

**What remains open.** One computation: a second-order *anisotropic* (Bianchi-I) separate-universe calculation of the comoving $\zeta$ response to a long mode carrying shear $(\hat k\hat k-\delta/3)\epsilon\dot\zeta$, to reproduce the in-in monopole $-15/8$ and quadrupole $15/16$ from a gradient-expansion route. Until then the in-in is the only complete route, and its result stands.

---

## 1. Set-up and conventions

Conformal time $\eta<0$, $a=c\,\eta^2$ (so $\mathcal H=a'/a=2/\eta<0$, $\epsilon=1-\mathcal H'/\mathcal H^2=3/2$), $M_{\rm Pl}=1$, $c_s=1$, end of contraction $\eta_*=-S$ with $kS\ll1$. Quadratic action $S_2=\int d\eta\,d^3x\,a^2\epsilon[\zeta'^2-(\partial\zeta)^2]$; $\zeta_{\mathbf k}=u_ka_{\mathbf k}+u_k^*a^\dagger_{-\mathbf k}$ with Bunch–Davies
$$u_k=N\,\frac{(1+ik\eta)e^{-ik\eta}}{\eta^3},\qquad |N|^2=\frac{1}{4\epsilon c^2k^3}=\frac{1}{6c^2k^3},$$
fixed by $u u^{*\prime}-u^*u'=i/(2a^2\epsilon)$ (the script verifies the EOM and solves the Wronskian; it does not assume $N$). On super-Hubble scales $u\propto\eta^{-3}\propto|H|$: this is the growing (non-attractor) mode; $\zeta'=-3\zeta/\eta$, i.e. $\dot\zeta=-\tfrac32H\zeta$ (Cai's Eq. 25).

Cubic action (Maldacena, comoving gauge, canonical field, $\eta_{\rm sr}=0$), conformal time, $\tilde\chi\equiv\partial^{-2}\zeta'$ (Maldacena's $\chi=a\epsilon\tilde\chi$):
$$
\mathcal L_3=a^2\big(\epsilon^2-\tfrac{\epsilon^3}2\big)\zeta\zeta'^2+a^2\epsilon^2\zeta(\partial\zeta)^2-2a^2\epsilon^2\zeta'\partial\zeta\!\cdot\!\partial\tilde\chi+\tfrac{a^2\epsilon^3}{2}\zeta(\partial_i\partial_j\tilde\chi)^2+f(\zeta)\frac{\delta\mathcal L_2}{\delta\zeta}\Big|_1 ,
$$
where the rewriting $\tfrac{\epsilon}{2a}(\partial\zeta)(\partial\chi)\partial^2\chi+\tfrac{\epsilon}{4a}(\partial^2\zeta)(\partial\chi)^2=-\tfrac{a^3\epsilon^3}{2}\zeta\dot\zeta^2+\tfrac{\epsilon}{2a}\zeta(\partial_i\partial_j\chi)^2+\partial_i(\cdots)$ is verified in the script at the level of symmetrised Fourier kernels (Sec. 2; identity exact). Field redefinition $\zeta=\zeta_n+f(\zeta_n)$,
$$
f=\frac{\zeta\zeta'}{\mathcal H}+\frac{\epsilon}{2\mathcal H}\Big[(\partial\zeta)(\partial\tilde\chi)-\partial^{-2}\partial_i\partial_j(\partial_i\zeta\partial_j\tilde\chi)\Big]+\frac{1}{4\mathcal H^2}\Big[-(\partial\zeta)^2+\partial^{-2}\partial_i\partial_j(\partial_i\zeta\partial_j\zeta)\Big].
$$
In-in at first order, $H_{\rm int}=-L_{\rm int}$:
$$
\langle\zeta^3(\eta_*)\rangle=-i\!\int^{\eta_*}\!\!d\eta\,\langle[\zeta^3(\eta_*),H_{\rm int}(\eta)]\rangle=-2\,{\rm Im}\!\int_{-\infty(1-i0)}^{\eta_*}\!\!d\eta\,\langle\zeta^3(\eta_*)L_{\rm int}(\eta)\rangle .
$$
Wick contractions: every vertex is an ordered monomial $\zeta^{(\alpha)}_{\mathbf p}\zeta^{(\beta)}_{\mathbf q}\zeta^{(\gamma)}_{\mathbf r}$ with a kernel $V(p,q,r)$; the three external legs are attached in all $3!$ ways, each counted once, with $\langle\zeta_{\mathbf k}(\eta_*)\zeta^{(\alpha)}_{\mathbf p}(\eta)\rangle=(2\pi)^3\delta(\mathbf k+\mathbf p)\,u_k(\eta_*)\,\partial^\alpha_\eta u_k^*(\eta)$. No symmetry factor is inserted by hand. Dot products are eliminated with $\mathbf p\!\cdot\!\mathbf q=(r^2-p^2-q^2)/2$.

Time integrals are done exactly: the integrand is $e^{iK\eta}\times$ Laurent polynomial in $\eta$ ($K=\sum k_i$); $I_n\equiv\int^{-S}\eta^{-n}e^{iK\eta}d\eta$ obeys $I_n=e^{-iKS}(-S)^{1-n}/(1-n)+\tfrac{iK}{n-1}I_{n-1}$ down to $I_1=-E_1(iKS)$ (Bunch–Davies rotation). Everything is then expanded in $S$; the log from $E_1$ is tracked as a symbol and verified absent at leading order. The leading imaginary part is $\propto S^{-12}$, exactly the order of $\mathcal P_\zeta^2\propto S^{-12}$, so $\mathcal A$ is a pure function of the $k_i$ (no $\eta_B$, no $c$).

## 2. Validation before use

| benchmark | what it tests | result |
|---|---|---|
| de Sitter, constant $\epsilon$: three $\epsilon^2$ bulk vertices vs Maldacena 2003 / Chen *et al.* 2007, $\mathcal A_\epsilon=\epsilon[-\tfrac18\sum k^3+\tfrac18\sum_{i\ne j}k_ik_j^2+\tfrac1K\sum_{i>j}k_i^2k_j^2]$ | normalisation, $-2\,{\rm Im}$, six-contraction Wick count, vertex kernels, contour, exact-integral pipeline | difference $\equiv0$ |
| ultra-slow-roll ($\epsilon\propto a^{-6}$, $\eta_{\rm sr}=-6$, $\zeta\propto a^3$): redefinition term vs Namjoo–Firouzjahi–Sasaki 2012 | sign/structure of $f\supset\tfrac{\eta_{\rm sr}}4\zeta^2+\zeta\zeta'/\mathcal H$ in a non-attractor phase | $f_{\rm NL}=5/2$ exactly |
| kernel identity for the $\epsilon^3$ rewriting | equivalence of Cai's Eq. (15) with Maldacena's cubic action | exact |

Only after these pass is the same code applied to $a=c\eta^2$.

## 3. Per-vertex results (from scratch, $\epsilon=3/2$)

$\Sigma_{i\ne j}$: six ordered pairs; $\Pi\equiv k_1^2k_2^2k_3^2$; "squeezed" = isoceles $k_1\ll k_2=k_3$; $\mu=\hat{\mathbf k}_1\!\cdot\!\hat{\mathbf k}$ in the general squeezed limit.

| vertex | $\mathcal A_v$ | $f^{\rm sq}$ | $f^{\rm eq}$ | $f^{\rm fold}$ | $f^{\rm sq}(\mu)$ | equals Cai row? |
|---|---|---|---|---|---|---|
| field redefinition, local part $\zeta\zeta'/\mathcal H$ | $-\tfrac34\sum k^3$ | $-\tfrac52$ | $-\tfrac52$ | $-\tfrac52$ | $-\tfrac52$ | — |
| field redefinition, non-local part | $-\tfrac{9}{128\Pi}(k_1{-}k_2{-}k_3)(\cdots)(\sum_{i\neq j}k_i^3k_j^2)$ | $+\tfrac{15}{16}$ | $+\tfrac{45}{32}$ | — | $\tfrac{15}{16}(1-\mu^2)$ | — |
| field redefinition, gradient part $(1/4\mathcal H^2)$ | $0$ at leading order | 0 | 0 | 0 | 0 | (dropped by Cai; correctly) |
| **field redefinition, total** | $-\tfrac{\epsilon}2\sum k^3-\tfrac{\epsilon^2}{32\Pi}\{\cdots\}$ | $-\tfrac{25}{16}$ | $-\tfrac{35}{32}$ | $-\tfrac{5}{2}$ | $-\tfrac{25}{16}-\tfrac{15}{16}\mu^2$ | **yes, identically** |
| $\zeta\zeta'^2$ (coef. $\epsilon^2-\epsilon^3/2$) | $-\tfrac{3}{64}\sum k^3$ | $-\tfrac{5}{32}$ | $-\tfrac{5}{32}$ | $-\tfrac{5}{32}$ | $-\tfrac{5}{32}$ | yes |
| $\zeta(\partial\zeta)^2$ | $0$ at leading order ($\mathcal O(k^2S^2)$) | 0 | 0 | 0 | 0 | yes ("secondary") |
| $\zeta'\partial\zeta\!\cdot\!\partial\tilde\chi$ | $\tfrac{3}{16\Pi}\{\Sigma k^7k^2-\Sigma k^5k^4-\Pi\sum k^3\}$ | $0$ | $-\tfrac58$ | $+2$ | $+\tfrac{15}{8}\mu^2$ | yes |
| $\zeta(\partial_i\partial_j\tilde\chi)^2$ | $\tfrac{9}{256\Pi}\{\sum k^9-3\Sigma k^7k^2-\cdots\}$ | $-\tfrac{15}{32}$ | $-\tfrac{15}{128}$ | $-\tfrac{15}{32}$ | $-\tfrac{15}{32}$ | yes |
| **total** | $=$ Cai Eq. (37) monomial by monomial (see §4) | $\mathbf{-\tfrac{35}{16}}$ | $\mathbf{-\tfrac{255}{128}}$ | $\mathbf{-\tfrac98}$ | $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ | |

The isoceles squeezed expansion of the total is $f=-\tfrac{35}{16}+\tfrac{35}{64}k_1^2/k^2+\mathcal O(k_1^3)$, identical to Paper 2's Eq. (vertexsum). Paper 2's Table `tab:vertexwalk` (squeezed $-25/16,-5/32,0,-15/32$; equilateral $-35/32,-5/32,-5/8,-15/128$) is reproduced exactly.

Structural remarks that follow from the table:
- The two $\epsilon^3$ pieces — the $-\epsilon^3/2$ part of $\zeta\zeta'^2$ (contributing $+15/32$) and $\zeta(\partial_i\partial_j\tilde\chi)^2$ ($-15/32$) — cancel in the isoceles squeezed limit, so that limit is the same as if the $\zeta\zeta'^2$ coefficient were $\epsilon^2$ alone ($-5/8$). This is because for the long leg on the undifferentiated $\zeta$, $(\partial_i\partial_j\tilde\chi_S)^2\to(\hat k_i\hat k_j)^2\zeta_S'^2=\zeta_S'^2$.
- The $\mu^2$ quadrupole comes only from the two terms in which the long mode enters through $\partial\tilde\chi_L\propto\hat{\mathbf k}_1\zeta_L'/k_1$ — the comoving-gauge shift, i.e. the long mode's shear: $\zeta'\partial\zeta\partial\tilde\chi$ ($+\tfrac{15}8\mu^2$) and the non-local redefinition ($-\tfrac{15}{16}\mu^2$). The would-be $1/k_1^2$ and $\mu/k_1$ singularities cancel exactly in the sum, for every $\mu$.

## 4. Cai 2009, Li 2016, Quintin 2015, Paper 2 — what each got right

- **Cai Eq. (37).** With $\sum_{i\ne j\ne k}k_i^5k_j^2k_k^2$ read as the three distinct monomials (and $\sum_{i\ne j\ne k}k_i^4k_j^3k_k^2$ as its six distinct monomials), the printed polynomial equals the from-scratch total exactly: $256\,\Pi\,\mathcal A=9\sum k^9+3\Sigma k^7k^2-27\Sigma k^6k^3+15\Sigma k^5k^4-198\,\Sigma^{\rm dist}k^5k^2k^2+27\,\Sigma k^4k^3k^2$, i.e. $3\{3,1,-9,5,-66,9\}$. Read instead with six ordered permutations of the $(5,2,2)$ orbit, it differs from the total by $-\tfrac{99}{128}\sum k^3$ — this is Paper 2's "spurious term". Cai's notation is internally inconsistent (their *rows* need the six-permutation reading to match their own second forms), but the polynomial they print is the right one under the natural reading, and it is also Li's Eq. (4.19) at $c_s=1$ (difference 0).
- **Cai Eqs. (38)–(40).** $-35/8$, $-255/64$, $-9/4$ are each exactly twice $-35/16$, $-255/128$, $-9/8$. Their stated squeezed shape $\mathcal A_T|_{\rm sq}=-\tfrac{21}{8}k^3$ is twice the true $-\tfrac{21}{16}k^3$ (Li's $\mathcal F\simeq\tfrac38(-\tfrac{33}2+13)k/k_1=-\tfrac{21}{16}k/k_1$). A uniform factor 2 in the amplitude step; no vertex, commutator, Wick, or orbit error.
- **Li 2016.** Correct at $c_s=1$; inherits Cai's structure (rows identical at $c_s=1$; "one recovers the results of [Cai]"). Not independent.
- **Quintin 2015.** Quotes $-35/16$ attributing it to Cai. Not a computation.
- **Paper 2.** Adopted value correct; per-vertex table correct. Its claim that the printed polynomial "squeezed-reduces to $-305/64$" holds only under the six-permutation reading, which is not the reading under which Eq. (37) is the vertex sum; and Cai's $-35/8$ is *not* explained by that term but by the amplitude-step factor 2. **Actionable for P2 Appendix A:** replace the "spurious $-(99/128)\sum k^3$ term" narrative by: Eq. (37) is correct (distinct-monomial reading, = Li Eq. 4.19), and Cai's three quoted amplitudes are uniformly $2\times$ their own polynomial. The $-35/16$ headline is unchanged and now rests on an independent from-scratch computation.

## 5. Separate-universe ($\delta N$) on both slicings

Exponential potential, $\lambda^2=2\epsilon$; exact patch ODE $du/dN=(\epsilon-3)u+2\sqrt{3\epsilon}\,u^2+\mathcal O(u^3)$; $u\propto W=e^{-(3-\epsilon)N}\propto|H|^{(3-\epsilon)/\epsilon}$ (grows in contraction; $=|H|$ at $\epsilon=3/2$, matching $\zeta\propto\eta^{-3}$). Second-order solution $u=u_iW+u_i^2A_2(W^2-W)$ (ODE residual verified 0). Then, in the $W\to\infty$ limit:

| final slice | $\zeta_1/W$ | $\zeta_2/W^2$ | $f_{\rm NL}(\epsilon)=\tfrac53\zeta_2/\zeta_1^2$ | at $\epsilon=3/2$ |
|---|---|---|---|---|
| uniform $\phi$ (comoving = in-in variable) | $\dfrac{\sqrt3\,u_i}{\sqrt\epsilon\,(3-\epsilon)}$ | $-\dfrac{9u_i^2}{\epsilon(3-\epsilon)^2}$ | $-5$ | $-5$ |
| uniform $|H|$ (uniform density = second-method variable) | $\dfrac{2\sqrt3\,u_i}{\sqrt\epsilon\,(3-\epsilon)}$ | $\dfrac{9u_i^2(\epsilon-7)}{2\epsilon(3-\epsilon)^2}$ | $\dfrac{5(\epsilon-7)}{8}$ | $-\dfrac{55}{16}$ |

So (i) the second method is reproduced exactly for its own variable; (ii) $\zeta_\rho=2\zeta_c$ at linear order — in a non-attractor phase $\rho=\rho(\phi,\dot\phi)$, so uniform-$\rho$ and uniform-$\phi$ slices are different slices at $\mathcal O(1)$ even at zeroth order in gradients; (iii) $f_\rho-f_c=5(\epsilon+1)/8$.

## 6. Why neither $\delta N$ equals the in-in: the long mode is not an FRW patch

ADM in comoving gauge (Maldacena): $N_i=\partial_i\psi$, $\psi=-\zeta/H+a^2\epsilon\,\partial^{-2}\dot\zeta$; at linear order $K^i{}_j=H\delta^i_j-\partial_i\partial_j\psi/a^2$. For the growing mode ($\dot\zeta=-\tfrac32H\zeta$),
$$
\delta K=\frac{k^2\psi}{a^2}\;\xrightarrow{k\to0}\;\epsilon\dot\zeta\ (\ne0),\qquad
\sigma^i{}_j=\Big(\hat k_i\hat k_j-\tfrac13\delta_{ij}\Big)\,\epsilon\dot\zeta\ (\text{same order}),
$$
whereas on an attractor ($\dot\zeta=0$) both are $\mathcal O(k^2)$ and the patch is FRW. The isotropic separate universe keeps $\delta K$ and discards $\sigma$; the in-in keeps both, and the quadrupole $\tfrac{15}{16}\mu^2$ in §3 is the direct signature. Therefore the $\delta N$–in-in gap is $\mathcal O(1)$ and angular, not an $\mathcal O(k^2)$ gradient correction (option b is excluded, option b′ is established), on top of the slicing difference (option c). Options (a) and (d) are excluded by §§2–3.

## 7. Integrity note

No number was targeted. The machinery was frozen after the two literature validations passed and then run once on the matter contraction; the per-vertex agreement with Cai's rows and Paper 2's table was observed, not imposed. The factor-2 diagnosis of Cai's amplitudes rests on three independent configurations (local, equilateral, folded) all giving ratio exactly 2. The $\delta N$ values $-5$ and $-55/16$ are reported as correct for their own variables and *not* reconciled away; the remaining gap is stated with its mechanism and the single computation that would close it.

## References checked (2026-09-02)

Cai, Xue, Brandenberger, Zhang, arXiv:0903.0631v2 (source `matterbounceng2.tex`); Li, Quintin, Wang, Cai, arXiv:1612.02036 (source); Quintin, Sherkatghanad, Cai, Brandenberger, arXiv:1508.04141 (source); Maldacena, astro-ph/0210603 (source); Namjoo, Firouzjahi, Sasaki, arXiv:1210.3692; Chen, Firouzjahi, Namjoo, Sasaki, arXiv:1301.5699; Cai, Easson, Brandenberger, arXiv:1206.2382 (review; quotes Cai 2009); lab artifacts `fnl_matter_contraction_second_method_2026_09_02.{py,md,json}` (commit d7dac953), Paper 2 Appendix A and `scripts/p2_vertex_check.py`.
