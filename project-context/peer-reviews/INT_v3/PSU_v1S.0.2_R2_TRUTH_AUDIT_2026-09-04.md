# PSU v1S.0.2 R2 — skeptical truth-audit (2026-09-04)

**Auditor:** independent Opus truth-audit leg; no expected outcome supplied.
**Exact artifact:** `arxiv/paper_su_criterion/main.pdf` sha256 `812dbaf1…aca31`, md5 `fcbecd03…`, 4 pp
(byte-identical to `site/public/papers/paper_su_criterion_v1S.0.2.pdf`).
**Inputs:** Grok_brutal + Gemini_cosmology R2VERIFY raws, `INT_v3/PSU_v1S.0.2_R2_claude_fable_2026-09-04.md`,
receipt `INT_v3/ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY/preflight_receipt.json`,
`DISPOSITIONS/PSU.md`, `INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md`,
`research/theory_audit/psu_gates_S1_S2_2026_09_04.{md,py,json}`,
`research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md`.

**Classes:** (a) genuinely-new real — must close; (b) re-flag of an already-closed/dispositioned
item; (c) honestly-disclosed out-of-scope/limitation; (d) FALSIFIED (contradicted by the artifact
or by re-derivation); (e) OPINION / venue-genre preference.

## PLAN (in progress — sections appended and committed one at a time)
1. Independent re-derivation gate (Eq. (4) sign, the −5 composition, the ×2 robustness arithmetic).
2. Canonical finding list with class + citation + closure action.
3. Per-leg counts + convergence note (R1 → R2 genuinely-new).
4. CLOSURE PLAN: (i) editorial for v1S.0.3, (ii) science items.
5. R2 statement + DISPOSITIONS/PSU.md update.

---

## 1. Independent re-derivation gate (auditor's own sympy, scratchpad `psu_check.py`)

With $\lambda=1-\eps/3$, $f^{\rm in\text{-}in}=\tfrac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ and the paper's
Eqs. (3)–(4):

| check | result | bearing |
|---|---|---|
| $f^{\rm fin}_{\rm map}-f^{\rm init}_{\rm map}$ | $=-\dfrac{5\eps}{4(3-\eps)}(1-3\mu^2)$ (residual with the printed $+$ sign is $\neq0$; with $-$ it is exactly $0$) | Eq. (4) as printed has the **wrong sign** |
| in-in monopole, general $\eps$ | $-\tfrac{5}{18}(\eps-3)(\eps-6)$; $=-15/8$ at $\eps=3/2$ | matches the paper |
| $f^{\rm in\text{-}in}/\lambda+f^{\rm init}_{\rm map}$ | $\equiv-5$ **identically in $\mu$**, all $\eps$ | Grok PSU-E4 falsified |
| $\langle f^{\rm init}_{\rm map}\rangle_\mu$ | $-5\eps/6=-5/4$ at $\eps=3/2$ (the value at $\mu=0$ is $-5/8$) | Grok used $\mu=0$, not the monopole |
| doubling the from-scratch shape | monopole $-15/4$, gap to $-5$ is $-5/4$, ratio $\mathbf{4/3}$ | the paper's "$8/7$" is wrong |
| $(-35/8)/(-15/8)$ | $7/3$, **not** $2$ | $-35/8$ is Cai's *isoceles* amplitude ($2\times(-35/16)$), not a monopole |

Independent sources: `psu_gates_S1_S2_2026_09_04.md` §S1.2 Eq. (S1.1) states
$f^{\rm init}_{\rm map}-f^{\rm fin}_{\rm map}=+\tfrac{5\eps}{4(3-\eps)}(1-3\mu^2)$ — i.e. the committed gate note
itself carries the opposite sign to the paper's Eq. (4). `fnl_matter_contraction_adjudication_2026_09_02.md`
l. 22–23 gives the shape $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ (isoceles $-35/16$, **angle-averaged monopole
$-15/8$**) and l. 26/32/101 the uniform factor 2 on Cai's *amplitudes*.

## 2. Canonical findings (32 items)

Legs: G = Grok, Ge = Gemini, F = Fable. Line numbers refer to `arxiv/paper_su_criterion/main.tex` at the
commit that produced sha256 `812dbaf1…`.

### (a) GENUINELY-NEW REAL — 20 items

| ID | Legs | Finding | Citation / verification | Closure action |
|---|---|---|---|---|
| C1 | F M1, Ge 1, G E3 | Abstract (l. 39–41) calls $-5$ "the in-in monopole"; $-5$ is the **separate-universe** value, the in-in monopole is $-15/8$ | body l. 229, Table I; composition verified §1 | reword abstract |
| C2 | F M2, Ge 2 | Eq. (4) second equality sign (l. 144–145) | §1 sympy; gates §S1.2 Eq. (S1.1) | flip $+\to-$ |
| C3 | Ge pass-2 E1, F min1 | l. 126 "$I=1-\lambda$ reduces to $\eps/3$" contradicts $\lambda\equiv1-I/3$ | Eq. (2) l. 118–121; Table I ($I=\eps$) | "$1-\lambda=I/3$ reduces to $\eps/3$, i.e. $I\to\eps$" |
| C4 | F M4b, Ge 6 | l. 88–90: "$8/7$" treats $-35/8$ as a monopole; a uniform $\times2$ gives monopole $-15/4$, gap $-5/4$, **ratio $4/3$**; also $(-35/8)/(-15/8)=7/3\neq2$ | §1; adjudication l. 22–26, 101 | rewrite the sentence with $4/3$; state that $-35/8$ is Cai's isoceles amplitude |
| C5 | F M4a | Li, Quintin, Wang & Cai (arXiv:1612.02036, JCAP 2017) load-bearing via the adjudication but absent from the bibliography | adjudication l. 26, 38, 90; `main.tex` bib l. 326–347 has no Li entry | cite and address |
| C6 | F M4c | l. 90 "the headline $O(1)$ statement rests on the from-scratch value" — false: $\lambda=1-\eps/3=1/2$ is bispectrum-independent | Eq. (2); only the second-order $-5$ composition uses the in-in input | separate the linear from the second-order claim |
| C7 | F M6 | Refs: [6] pairs arXiv:1504.00351 (DPS "On separate universes", JCAP 1510, 059) with JCAP 1511, 043 (that is Conformal Fermi Coordinates, arXiv:1502.02011); [11] initials (D. Artigas, J. Grain); [12] first author (J. H. P. Jackson) | `main.tex` l. 331, 336, 337 | correct all three **after** checking the arXiv listings |
| C8 | F M6 | §IV never engages DPS "On separate universes", the closest prior statement of when a long mode is a local FRW | §IV l. 248–276 | add a paragraph: which DPS assumption fails at $I=O(1)$ |
| C9 | Ge pass-2 N1 | Eq. (2)/abstract: additive $O(k_L^2/a^2H^2)$ should carry the $\zeta_L$ amplitude | l. 37, 118–121 | move inside the bracket |
| C10 | Ge 4 | §IV uses $\eps$ for both the gradient-expansion order and the slow-roll parameter in one sentence | l. 248–251 | use $\eps_{\rm grad}$ or $k/aH$ |
| C11 | F min4 | Second-order treatment assumes $\zeta_L(t_i)=0$ (pure growing mode); Eq. (2)'s "any history" is a linear-order statement | l. 122–130 | state the assumption |
| C12 | F min2 | "dust" labels a $w=0$, $c_s=1$ scalar; for true dust $c_s\to0$ and $I=\zeta^{-1}\!\int(\eps/c_s^2)\dot\zeta\,dt$ diverges | Eq. (2) | relabel row; say what the criterion predicts for genuine dust |
| C13 | F min3 | Abstract "exact, invertible change of variable" | Eq. (2) is linear order, super-Hubble | "exact at linear order on super-Hubble scales" |
| C14 | F min5 | "the two coincide only as $\eps\to0$" applies the growing-mode monopole outside its domain (attractor in-in is $\tfrac{5}{12}(1-n_s)$) | l. 165, 229 | delete or qualify |
| C15 | F min6 | Kination $\eps=3$: $m=3/\eps-1=0$ is the constant mode ($\dot\zeta_L=0$, $I=0$); $\lambda\to0$ is a formal limit of the $\eps$-formula | Fig. 1 caption, l. 165 | qualify or drop |
| C16 | F min9 | Final slice is uniform-$\phi$ ( = comoving) and differs from uniform-$\rho$ at $O(k^0)$ when $I=O(1)$ — so Lyth–Malik–Sasaki's $\delta N=\zeta_{ud}$ is not the compared object | Eq. (1); adjudication l. 34 | state explicitly (second $O(1)$ slice ambiguity) |
| C17 | F min10 | Table I ekpyrosis row: "attractor-like" is not a value | Table I | give the Creminelli–Nicolis–Zaldarriaga statement or "n/a" |
| C18 | F min11 | Abstract "USR: $I=O(\eps)$"; exact is $I=\sqrt{\eps_s\eps_f}-\eps_f$ | l. 127–129 ($\lambda_{\rm USR}$) | $O(\sqrt{\eps_s\eps_f})$ |
| C19 | F min13 | Eq. (1): $\partial_iN^i$ is the coordinate divergence of the contravariant shift; $u^\mu\!\parallel\!n^\mu$ presumes a single scalar (no vorticity) | Eq. (1) | one clarifying sentence |
| C20 | F M5 | "We validate on four backgrounds" (l. 42–44): attractor + ekpyrosis are $I=0$ by definition, the USR row is not computed here, leaving one nontrivial check | §V Limits; Table I; R1 PSU-21/27 | "one nontrivial check plus three consistency limits"; mark the USR entry as not computed here |
