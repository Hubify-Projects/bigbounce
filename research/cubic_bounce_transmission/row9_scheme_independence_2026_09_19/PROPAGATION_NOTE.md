# PROPAGATION NOTE — row 9 / D-A3-9 result → A3M

**From:** lane `LS4-ledger9-scheme` · **To:** the A3M lane (owner of `research/track_a3_multichannel/paper/main.tex`)
**Date:** 2026-09-19 · **Evidence:** `ROW9_SCHEME_INDEPENDENCE_2026-09-19.md`, commit `8d7ede35`,
pre-registration `117051bd`, manifest `a3-row9-scheme-independence`.

**This lane did NOT edit `main.tex`, SSOT, the site or Convex.** Below are exact printable sentences; accept,
reject or re-word them as the paper's owner. Nothing here should be propagated without the A3M lane's own
verification against the committed logs — and note that the change is **mixed in direction** (§4), which is
part of why it should not be applied silently.

---

## 0. One-line summary of what changed

D-A3-9's residual — *"a scheme-independent variable choice through H = 0"* — is **closed**. The variable exists
(the Bardeen potential Φ), it selects **scheme S2**, and the two-scheme band is therefore **not** a physical
ambiguity. `f_NL^after` on the Quintin-type background becomes a single number, **−1.25**, not `[−1.25, −0.50]`.

## 1. Replacement for the §"Scheme S2" closing sentences (currently: "S1 and S2 are therefore genuinely physically inequivalent continuations through H = 0 … reported as the two-scheme band")

> S1 and S2 are not two regularizations of one answer, but neither are they two equally admissible
> continuations: the ambiguity is resolvable. The Bardeen potential $\Phi$ obeys
> $\Phi''+2(\mathcal H-\phi''/\phi')\Phi'+(k^2+2\mathcal H'-2\mathcal H\phi''/\phi')\Phi=0$, which contains
> neither a choice of $z$ nor any explicit $1/H$; it is regular at the bounce ($H=0$, where it reduces to
> $\Phi''+(k^2+2a^2\Upsilon)\Phi=0$) and equally regular at the NEC crossing $\rho+p=0$, where $z^2_{\rm S2}$
> vanishes and $\zeta$ is logarithmically divergent. Written as the first-order system
> $\Phi'=-\dot H\,\Xi-\mathcal H\Phi$, $\Xi'=(a^2-\mu k^2)\Phi+\mathcal H\Xi$ with
> $\Xi\equiv\mu(\Phi'+\mathcal H\Phi)$ and $\mu=a^2/(\mathcal H^2-\mathcal H')=-1/\dot H$, it is free of
> $\delta$-functions, so $\Phi$ and $\Xi$ are continuous across the NEC boundaries and no junction prescription
> need be imposed -- the continuity it enforces is identically S2's $[\zeta]=0$, $[z^2\zeta']=0$. Propagating
> this system across the Quintin-type bounce gives $|\lambda_\zeta|=0.9699$ at
> $k\eta_B=10^{-3}$--$10^{-2}$, agreeing with scheme S2 to $7\times10^{-8}$ and differing from S1's $6.06$ by
> $84\%$. Scheme S1's $z=a$ is exact if and only if $\epsilon=-\dot H/H^2$ is constant -- true throughout the
> matter contraction, where the two schemes coincide and both give $\fnl^{\rm before}=-35/16$, and false in the
> bounce window, which is precisely where they part company. The transmitted amplitude on this background is
> therefore the single value $\fnl^{\rm after}=-1.25$, not a band.

## 2. Table `tab:s1_after` — recommended change

The S1 rows describe a variable choice that does not solve the Einstein equations on these backgrounds. Options,
in decreasing order of this lane's preference:

* **(a) preferred** — keep all four rows but relabel: the S1 rows become *"scheme S1 ($z=a$), superseded for the
  Quintin-type background by Sec. [ref]; retained for comparison"*, and the S2 row becomes the quoted result.
  The caption sentence *"the S2 row … is not directly comparable to the S1 rows above it"* must be **deleted or
  reversed** — it is now the S1 rows that are not the comoving-curvature transfer.
* **(b)** report only `f_NL^after = −1.25` (Quintin-type) and move the S1 column to an appendix.

**Not yet available:** S2 numbers for the LQC and poly backgrounds at cubic order (lane 9b-2 (A1): those
backgrounds have $\dot H=0$ crossings). Until they exist, the honest statement is *"−1.25 on the Quintin-type
background; the LQC and poly rows remain S1-only and are flagged as such"* — **do not** quote `[−0.65, −0.50]`
as an S2-validated range, and do not quietly rescale the LQC/poly rows by 2.5.

## 3. Sentences to DELETE or qualify wherever they appear

* `"the transmitted amplitude is not scheme-independent"` → now false as stated for the linear transfer.
* `"the transmitted amplitude is reported as the two-scheme band $\fnl^{\rm after}\in[-1.25,-0.50]$"` → replace
  per §1.
* `"every use of $\fnl^{\rm after}$ in this paper carries its scheme qualifier"` → the qualifier on the
  **linear transfer** can be dropped on the Quintin-type background; a qualifier is still owed for the
  **cubic-action** form (raw-ADM vs Maldacena-form) and for the LQC/poly rows.
* Abstract line 40 `"Transmission is scheme-qualified"` → needs rewording consistent with the above.
* §"this bound is specific to scheme S1 -- S2's raw-ADM continuation lies outside assumption (A4)": since S2 is
  now the selected scheme, the $0\le T_{\fnl}<1/2$ bound is a statement about a superseded variable and should
  not be presented as the paper's transfer bound.

## 4. The change that goes AGAINST the paper — must be propagated in the same pass

Row 18a established that the **tensor** transfer is scheme-independent and that $\lambda_T=\lambda_\zeta^{\rm S1}$
identically. With the scalar transfer now fixed at $\lambda_\zeta=0.970$:

> $r_{\rm after}=24(\lambda_T/\lambda_\zeta)^2$ takes row 18a's S2 value $\approx9.4\times10^2$, not the S1
> value $24.0$. Against BK18+Planck $r<0.036$ that is $2.6\times10^4\times$ rather than $6.7\times10^2\times$.

The tensor no-go is **strengthened**, and the conservative number the paper currently quotes (§VII--VIII,
"A3M quotes the conservative S1 number with a scheme label") is no longer the applicable one. Suggested wording:

> With the scalar transfer fixed by the Bardeen continuation at $\lambda_\zeta=0.970$ and the scheme-independent
> $\lambda_T=6.06$, the post-bounce tensor-to-scalar ratio is $r_{\rm after}=9.4\times10^2$, exceeding the
> BICEP/Keck--Planck bound by $2.6\times10^4$; the no-go of Sec. [ref] is unchanged in direction and strengthened.

**Do not apply §1--§3 without §4.** Taken alone, §1--§3 make $|\fnl|$ larger (better survey reach) while §4 makes
the tensor channel worse; propagating only the favourable half would be exactly the self-favouring pattern the
integrity audit (directive F) exists to catch.

## 5. What is NOT claimed (carry these limits into the paper, do not soften them)

1. This adjudicates the **linear** MS-variable choice. The cubic-order choice (raw-ADM vs Maldacena-form action)
   is settled only indirectly, by the raw form being the one finite on the now-selected S2 modes
   (lane 9b-2 §2, unchanged).
2. Computed on the **Quintin-type background only**.
3. No claim is made to have refuted an LQC **dressed-metric** calculation. If S1 is meant as a different theory
   rather than a continuation of this classical background, the correct statement is *"S1 does not apply here"*,
   not *"S1 is wrong"*. Worth noting in-paper: the dressed-metric framework's own published gauge dictionary is
   $\mathcal R=-(a/z)\delta\phi$ with $z=a\dot\phi/H$ — the S2 $z$ — per the source-cited transcription in
   `../lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md` §1.2 (their Eq. 25). This lane did not re-derive
   those equations.
4. $c_s=1$, single scalar, no anisotropic stress — and note that the bounce window requires a **kinetic-sign
   flip** ($P=\sigma X-V$, $\sigma:+1\to-1$): a canonical scalar cannot give $\dot H>0$. This is the same
   NEC-violating idealisation the rest of the A3M transmission calculation already assumes (lane 9b-2's (A5)),
   but it should be named in-paper rather than left implicit.
5. At $\rho+p=0$ no metric-only variable is complete: $\Phi$ stays finite and its equation regular, but the
   $0i$ constraint degenerates, so the full content there needs $(\Psi,\delta\phi,\dot{\delta\phi})$. This is
   the same degeneracy that makes $\zeta$ log-divergent there.
6. **Not closed by this lane:** the dependence on the choice of matching surface, and the thin-shell
   idealisation of the kinetic-sign flip. Carry both as stated caveats; do not claim they are resolved.

**Independent blind adjudication: CONFIRMS.** A separate Fable-tier referee, told neither this lane's
conclusion nor its method and forbidden to read its directory, derived the same verdict by a different route
(the $(\Psi, D)$ system with $D=-\delta\phi/\dot\phi$, junctions fixed by Israel matching rather than by the
$\delta$-free-system argument): **S2, $\lambda_\zeta=0.970$, confidence $\approx90\%$**, independently
reproducing the exact $\zeta'$ identity, the "S1 is exact iff $\epsilon'=0$" condition, the invalidity of the
naive expanded-form junction, and the logarithmic divergence of $\zeta$ at a smooth NEC crossing. Details and
its own strongest counter-argument: findings note \S6.

**One number to keep straight.** The adjudicator's "S1 overestimates $\lambda_\zeta$ by 6.25" is correct for
the LINEAR transfer only. Because $\fnl^{\rm after}=T\,\fnl^{\rm before}+\Delta\fnl^{\rm bounce}$ also carries
the bounce's own cubic term, the change in the quoted value is $-0.50\to-1.25$, a factor **2.5, not 6.25**.
Do not propagate 6.25 into the manuscript.

## 6. Directive-G / process reminders for the A3M lane

* Any edit acting on this note is a paper change: bump `\paperVersion` + `\date`, 4-pass recompile with
  0 undef-refs, `/latex-audit`, re-mirror byte-identical to every served path, Convex `paperVersions:bump` with
  the real md5/pages, three-way md5 check — all in the same bundle.
* **Directive I6 applies**: `f_NL^after` and `r_after` appear inside figure images. A text grep cannot see a
  value baked into a PNG. Inventory every `\includegraphics` and regenerate any figure carrying `−0.50`,
  `[−0.65,−0.50]`, `[−1.25,−0.50]`, `r_after = 24`, or `λ_ζ = 6.06`, then verify by rendering the figure page.
* A3M is under a **directive-R2 rounds-stop** (R9+R10 budget spent). This note is a *science decision*, which is
  exactly the intervening event R2 requires before another board — but the decision to run one is the
  director's, not this lane's.
