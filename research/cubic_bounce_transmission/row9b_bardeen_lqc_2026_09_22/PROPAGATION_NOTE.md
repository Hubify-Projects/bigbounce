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
background-specific and row 9's "factor 6.25" must NOT be carried to the LQC/poly rows. Separately, the R11
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
| LQC effective dust (Bardeen continuation) | **0.500** | *not computed* | linear part **-1.094** |
| poly (Bardeen continuation) | **0.521** | *not computed* | linear part **-1.140** |

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
4. **The principal value is a prescription** — derived to be the unique symmetric finite part of an integrable
   logarithm, and two independent implementations agree to `6\times10^{-5}` (LQC) and `2\times10^{-4}` (poly),
   but an asymmetric continuation is not excluded by anything computed here.
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
