# PROPAGATION NOTE — row 9b (Bardeen route on LQC/poly + the evaluation window) → A3M

**From:** lane `LS9-bardeen-lqc` · **To:** the A3M lane (owner of `research/track_a3_multichannel/paper/main.tex`)
**Date:** 2026-09-22 · **Evidence:** `ROW9B_BARDEEN_LQC_2026-09-22.md`, pre-registration `d079d7bd`,
computation `9ee1d478`, manifest `a3-row9b-bardeen-lqc-poly`.

**This lane did NOT edit `main.tex`, SSOT, the site or Convex.** Below are exact printable sentences; accept,
reject or re-word them as the paper's owner. Nothing here should be propagated without the A3M lane's own
verification against the committed logs. As with row 9, **the change is mixed in direction** (§3), and §1–§2
must not be applied without §3.

---

## 0. One-line summary

A3M's own Next-steps item (i) is **closed**. The Bardeen route extends to the LQC and poly backgrounds, where
`rho + p = 0` is crossed **smoothly**: `Phi` and `Phi'` stay continuous, the divergence is a **logarithm** in
the momentum sector with a closed-form amplitude, and the continuation is the principal value. The transmitted
linear amplitude differs from scheme S1 on **all three** backgrounds — so the selection is background-
independent in direction — but by **6.25x (Quintin), 2.00x (LQC), 2.67x (poly)**, so the magnitude is
background-specific and row 9's "factor 6.25" must NOT be carried to the LQC/poly rows.

**Read §2c before quoting any of this.** At the smooth crossing the Mukhanov-Sasaki operator is **not
essentially self-adjoint**, so the continuation carries a free parameter per surface and the numbers above are
the **time-symmetric (principal-value)** member of that family. On LQC there is a second, prescription-free
anchor giving the same `1/2`; **on poly there is not**, and `3/8` is conventional. Separately, the R11
ESSENTIAL evaluation-window item now closes by computation, not disclosure.

## 1. Table `tab:s1_after` — recommended replacement

The LQC and poly rows are no longer "this paper's only computed value on those backgrounds in the S1 scheme,
retained because nothing better exists". A Bardeen-continuation linear transfer now exists on both. Recommended
form (values from `results.json`, `consequences`):

| background | `T_fNL` | `Delta f_NL^bounce` | `f_NL^after` |
|---|---|---|---|
| Quintin-type (S1, superseded) | 0.165 | -0.140 | -0.501 |
| LQC effective dust (S1, superseded) | 0.250 | -0.104 | -0.651 |
| poly (S1, superseded) | 0.196 | -0.127 | -0.555 |
| Quintin-type (Bardeen continuation / S2 raw-ADM) | 1.031 | +1.007 | **-1.25** |
| LQC effective dust (Bardeen continuation, PV; second anchor agrees) | **0.500** | *not computed* | linear part **-1.094** |
| poly (Bardeen continuation, **PV-only**) | **0.521** | *not computed* | linear part **-1.140** |

**The two new `f_NL^after` entries are LINEAR-TRANSFER-ONLY and the caption must say so.** The cubic term
`Delta` on LQC/poly is not computed by anyone in this program (it needs the raw-ADM in-in integral on those
backgrounds, whose integrand carries the same `Q = 0` logarithm at cubic order). If a full `f_NL^after` must be
shown for those rows it can only be a **labelled bracket** between the two cubic endpoints that have actually
been computed anywhere — LQC `[-1.198, -0.087]`, poly `[-1.267, -0.133]` — and **never a single value**.

## 2. Replacement / addition for the Sec. III A "Bardeen continuation" discussion

> The selection made by the Bardeen continuation is not specific to the piecewise background on which it was
> established. On backgrounds that cross $\rho+p=0$ smoothly rather than jumping across it -- the
> loop-quantum-cosmology effective-dust background and the analytic non-LQC background used elsewhere in this
> section -- the quantity $Q\equiv\mathcal H^2-\mathcal H'=-a^2\dot H$ has a simple zero, at which the
> $\Phi$ equation is a regular singular point with indicial exponents $\{0,2\}$. Every solution therefore has
> $\Phi$ and $\Phi'$ continuous, with $\Phi'(\eta_c)=-\mathcal H(\eta_c)\Phi(\eta_c)$ -- the degeneration of
> the momentum constraint at $\rho+p=0$, obtained here as the equation's own first recursion rather than
> assumed. The resonance between the two exponents gives the $r=0$ branch a $t^2\log t$ term of amplitude
> $-\Phi(\eta_c)k^2/2$, so $\zeta$ and $\Xi$ diverge only logarithmically, with amplitude
> $c_{\log}=-k^2\mathcal H(\eta_c)\Phi(\eta_c)/Q'(\eta_c)$; a logarithm is integrable, and the continuation
> through the surface is its unique symmetric finite part. Propagating the regular system across both
> backgrounds, and comparing at fixed incoming adiabatic vacuum, the transmitted constant-$\zeta$ amplitude is
> a fraction $R=1/2$ (LQC) and $R=3/8$ (poly) of scheme S1's, against $R=0.160$ on the Quintin-type
> background. Both rational values are exact: at leading order in the gradient expansion
> $R=3\,I_\epsilon/I_{\rm S1}$ with $I_s=\int d\eta/z_s^2$ and $I_\epsilon$ a principal value, giving
> $3(\pi/6\sqrt3)/(\pi/\sqrt3)$ and $3(\pi/32)/(\pi/4)$ respectively. Because
> $f_{\rm NL}\propto\zeta^{-1}$ under a common linear rescaling, the transmitted amplitude scales as $1/R$:
> scheme S1 transmits more curvature perturbation than the regular continuation does on every background
> tested, and therefore *understates* $|\fnl^{\rm after}|$ -- by a factor $6.25$ on the Quintin-type
> background, but only $2.00$ and $2.67$ on the other two. The factor is background-specific and should not be
> quoted as universal.

**A sentence the paper should add, because it is a real property of the paper's own construction:**

> On the Quintin-type background the handoff surface $|t|=t_m$ is the end of the exact dust contraction, so
> $\zeta$ there is unambiguous and $\fnl^{\rm before}=-35/16$ is evaluated where it is defined. On the LQC and
> poly backgrounds the corresponding surface is the point at which $\dot H$ vanishes, which lies inside the
> bounce region rather than in the dust phase, and at which $\zeta$ is logarithmically divergent in the
> selected continuation; the ratio $R$ quoted above is used precisely because it refers to no handoff surface
> at all.

## 2b. The handoff convention — read this before quoting `T_fNL = 0.500 / 0.521`

Those two numbers use a handoff in the **dust contraction**, where the Bardeen and S1 `zeta` are the same
function (verified to `7.7e-10` and `1.3e-8`). They are **not** `zeta_Bardeen(-eta_B)/zeta_C(+infty)`. Both
conventions were computed:

| background | `T_fNL[S1]` | dust handoff (**adopted**) | at `-eta_B` | ratio | `epsilon` at `-eta_B` |
|---|---|---|---|---|---|
| Quintin-type | 0.1650 | 1.0310 | 1.0310 | **1.000** | 1.500 |
| LQC | 0.2500 | **0.5000** | 0.3465 | 0.693 | **0.000** |
| poly | 0.1955 | **0.5213** | 0.0975 | 0.187 | **0.000** |

On the Quintin-type background the two agree to `4.4e-6`, because `-t_m` there really is the end of the exact
dust phase. On LQC and poly they do not, and the `-eta_B` column is the wrong one: that surface is *defined*
by `Q = 0`, so `epsilon = Q/\mathcal H^2 = 0` there **exactly**, and the matter-contraction
`\fnl^{\rm before} = -35/16` is an `epsilon = 3/2` result that cannot be evaluated on it. The same surface is
where `zeta` is logarithmically divergent, and the discrepancy tracks the log amplitude exactly (`0.693` vs
`c_log/zeta_fp = 0.46`; `0.187` vs `2.83`).

**Consequence for the paper, stated plainly:** A3M's existing LQC and poly rows already pair a handoff
amplitude taken at `epsilon = 0` with an `epsilon = 3/2` bispectrum. That is a *pre-existing* convention
mismatch, not one introduced by this note, and it does not arise on the Quintin-type row. The A3M lane should
either state the handoff explicitly in the caption or move it into the dust phase for all three rows.

## 2c. The prescription dependence — a hard caveat, quantified, that must travel with §1–§2

At a simple sign-changing zero of `z^2 = 2a^2\epsilon` (which every smooth NEC-violating bounce has, and which
the Quintin-type parametrization avoids only by jumping `\dot H`), writing `u = \eta-\eta_B` and
`z^2 = \alpha u(1+O(u))` gives `z''/z = -1/(4u^2)` — the **critical** attractive inverse-square potential. The
operator is **not essentially self-adjoint**: it admits a one-parameter family of self-adjoint extensions per
surface, and continuity of `\Phi` and `\Phi'` does not select one (every solution obeys
`\Phi'(\eta_c) = -\mathcal H_c\Phi(\eta_c)`, so the two-dimensional solution space maps onto a one-dimensional
set of data there). Measured, in this lane's own code and independently by the blind adjudication:

| background | `R` (principal value) | complex-contour extension | extension parameter giving `R = 1` |
|---|---|---|---|
| LQC | 0.500 | 0.7070 ( `= \|1+i\| x 1/2` ) | `\nu = \pi` |
| poly | 0.375 | 0.7496 ( `= \|1+i\sqrt3\| x 3/8` ) | `\nu = 3.02` |

`R(\nu)` is linear, so the family sweeps the positive line. **An extension one analytic-continuation unit away
from the principal value returns `R` to 1 and erases the entire effect.**

**Why LQC survives this and poly does not.** On the LQC background the zero of `2a^2\epsilon` sits at
`1-2x = 0`, where the *quantum-geometry* factor vanishes — not where the matter kinetic term does, since the
source is dust and `\rho+p = x` never vanishes. The matter-built weight
`z_K^2 = a^2(\rho+p)/(c_s^2H^2) = 3a^2/(1-x)` is therefore **strictly positive with no zero at all**, its
continuation is unambiguous, and its mixing integral `\pi/(6\sqrt3)` is *identical* to the principal value of
the geometric one — giving `R = 1/2` with **no prescription**. poly specifies no matter sector, so no such
anchor exists there.

**Recommended in-paper sentence:**

> Because $z^2=2a^2\epsilon$ has a simple sign-changing zero wherever the null energy condition is violated
> smoothly, the Mukhanov-Sasaki operator there is the critical inverse-square case and is not essentially
> self-adjoint; the transmitted amplitude carries a one-parameter continuation ambiguity per surface, and we
> quote the time-symmetric member. On the loop-quantum-cosmology background this choice is not required: the
> zero lies where the quantum-geometry factor vanishes rather than where the matter kinetic term does, the
> matter-built weight $a^2(\rho+p)/c_s^2H^2$ has no zero, and it returns the same value independently. On the
> analytic non-LQC background no such anchor exists and the quoted value is convention-dependent at
> $\mathcal O(1)$.

**The assumption the LQC anchor rests on, which must be stated:** that the effective theory producing
`H^2=(\rho/3)(1-\rho/\rho_c)` leaves the scalar kinetic weight proportional to `a^2(\rho+p)/H^2`. If its
constraint algebra instead rescales that weight by the same `(1-2x)` factor — plausible, since in
holonomy-corrected effective dynamics that factor also multiplies `k^2` and signals **signature change**
rather than ordinary evolution — the anchor disappears and LQC becomes as convention-dependent as poly.
Neither this lane nor the adjudication derived which weight that theory produces.

## 3. The change that goes AGAINST the paper — must be propagated in the same pass

Row 18a established `lambda_T = lambda_zeta^S1` identically on **every** background and that the tensor
transfer is scheme-independent, and it recorded an explicit open gap: *"No S2 `r_after` for LQC/poly (lane
9b-2 (A1): `z_S2^2 = 0` at their `Hdot = 0` crossings)"*. **That gap is now closed, and it closes against the
paper.** With `r_after = 24(lambda_T/lambda_zeta)^2 = 24/R^2`:

> With the scalar transfer fixed by the Bardeen continuation, the post-bounce tensor-to-scalar ratio is
> $r_{\rm after}=24/R^2$, i.e. $9.4\times10^2$ (Quintin-type), $96$ (LQC effective dust) and $1.7\times10^2$
> (poly), against the scheme-S1 value $24.0$ common to all three. Measured against the BICEP/Keck--Planck
> bound $r<0.036$ these exceed it by $2.6\times10^4$, $2.7\times10^3$ and $4.7\times10^3$ respectively, rather
> than by $6.7\times10^2$. The no-go of Sec.~[ref] is unchanged in direction and strengthened on every
> background.

**Do not apply §1–§2 without §3.** §1–§2 make `|f_NL|` larger (favourable to the survey-reach channel) while
§3 makes the tensor channel worse; propagating only the favourable half is exactly the self-favouring pattern
directive F exists to catch.

## 4. R11 ESSENTIAL 2 — the evaluation-window convention, now closed by computation

R11 closed the item by *disclosing* the non-uniform rule `eta_*/eta_B = min(50, 0.2/k eta_B)` (hence 50, 50, 20
at the three `k`-points, the third "a less-converged choice, disclosed as such"). It can now be closed properly.
A 12-point `eta_*` scan at all three `k` (committed kernel, unmodified) shows a **stationary region common to
all three `k`-points**, and a single uniform convention sits inside it:

> **Recommended replacement text.** "The post-bounce evaluation time is fixed uniformly at
> $\eta_*=15\,\eta_B$ at every $k$, which lies in the stationary region of $\fnl^{\rm after}$ at each of the
> three $k$-points and satisfies $k\eta_*\le0.15$ throughout. With this convention
> $\fnl^{\rm after}[{\rm S2}]=-1.249,\,-1.249,\,-1.246$ at $k\eta_B=10^{-3},3\times10^{-3},10^{-2}$, a spread
> of $0.22\%$ across $k$ and across the stationary window; we therefore quote $\fnl^{\rm after}=-1.25$ with a
> $0.3\%$ evaluation-time systematic."

Three significant figures are justified by this scan; four are not. **The headline `-1.25` is unchanged** —
R11's ESSENTIAL was a genuine disclosure gap, not a numerical error, and the paper can now say so positively
instead of disclosing a non-uniform convention.

## 5. Sentences to DELETE or qualify wherever they appear

* The `tab:s1_after` caption's *"they are retained for comparison and remain this paper's only computed value
  on the LQC and poly backgrounds"* → **no longer true for the linear transfer.** A Bardeen-continuation
  `T_fNL` now exists on both; only the *cubic* term remains S1-only there.
* Any statement that the LQC/poly S1 numbers are the **conservative** choice → they are not; they understate
  `|f_NL^after|` by 2.0x and 2.7x and understate `r_after` by 4.0x and 7.1x.
* The R11 closure text stating the LQC/poly exclusion is *"about the numerical propagation not yet being
  carried out there (not a different regularity class)"* → correct as written, and can now be **replaced by
  the positive statement**: the propagation has been carried out, and the regularity class is indeed the same
  (`{0,2}` at a simple zero of `Q`), with the divergence logarithmic and confined to the momentum sector.
* `"84%"` / `"factor 6.25"` wherever it is used as *the* size of the S1/S2 difference → it is the
  **Quintin-type** value. On LQC it is 2.00 and on poly 2.67.
* Anywhere the LQC effective-fluid `T=0.409` sits next to a Bardeen/S2 number → they must not be conflated.
  `0.409` is built on the **dust** `z^2=a^2(\rho+p)/H^2`; the Bardeen/geometric variable on that background is
  `z^2=2a^2\epsilon`, and on an LQC effective background these differ by the factor `(1-2\rho/\rho_c)` because
  `\rho+p \neq -2\dot H` there. (Their super-Hubble *mixing integrals* do coincide, both `\pi/6\sqrt3` — that
  is a separate and reportable fact, not a licence to merge the two rows.)

## 6. Limits to carry into the paper — do not soften these

1. **Linear transfer only on LQC/poly.** The cubic `Delta` there is not computed. §1's bracket is a bracket.
2. **A classical-GR continuation statement about a given `a(eta)`, not LQC dressed-metric perturbation
   theory.** No claim is made about, or against, the LQC framework's own perturbation equations.
3. **On the LQC background the source's `rho+p` is not `-2\dot H`**, so "the effective-fluid scheme" and "the
   geometric scheme" are two different variables there; this lane adjudicates the continuation of a given
   `a(eta)`, not which effective source is physical.
4. **The continuation is a PRESCRIPTION and the freedom is O(1)** — see §2c, which supersedes an earlier
   version of this note that wrongly called it unique. The quoted values are the time-symmetric member of the
   extension family; `\nu = \pi` (LQC) or `3.02` (poly) returns `R` to 1. LQC has an independent anchor,
   poly does not. The paper must **not** present the poly number as prescription-free.
5. `c_s=1`, single scalar, no anisotropic stress, and the same kinetic-sign-flip idealisation the rest of the
   A3M transmission calculation already assumes. Inherited, not new.
6. At `\rho+p=0` no metric-only variable is complete: the `0i` constraint degenerates to
   `\Phi'+\mathcal H\Phi=0` (now derived, not assumed), so the full perturbation content at that instant needs
   the unreduced triple. Row 9's caveat, refined.
7. The matching-surface and thin-shell caveats row 9 carried are **not** closed here either.

## 7. Directive-G / I6 / R2 reminders for the A3M lane

* Any edit acting on this note is a paper change: bump `\paperVersion` + `\date`, 4-pass recompile with
  0 undef-refs, `/latex-audit`, re-mirror byte-identical to every served path, three-way md5 check, all in the
  same bundle. Convex is disabled — queue the mutations to `CONVEX_BACKFILL_QUEUE_2026-09-21.md`.
* **Directive I6 — inventoried by this lane, and the answer is NO regeneration needed.** `main.tex` has exactly
  two `\includegraphics`: `sigw_nhz_from_lab_spectrum_2026_09_04.png` and `pbh_compaction_fnl.png`. Their
  committed generators (`sigw_nhz_from_lab_spectrum_2026_09_04.py`, `pbh_compaction_fnl.py`) were grepped for
  every quantity this note moves — `T_fNL`, `f_NL^after`, `r_after`, `0.250`, `0.196`, `-0.651`, `-0.555`,
  `6.25`, `lambda` — and carry **none** of them: the PBH figure's `FNL` dict contains only the *pre*-bounce
  values `0`, `-35/16` and `-35/8`, and the SIGW figure's only `24` is the `P_T/24` transfer normalisation,
  not `r_after`. **No figure regeneration is required by this note.** (The A3M lane should still re-run the
  inventory itself if it adds a number to a figure while applying §1–§4.)
* **Directive R2:** this note is a *science decision* — exactly the intervening event R2 requires before
  another board on A3M. Whether to run one is the director's call, not this lane's.
