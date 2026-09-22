# Pre-registration — LS12: the pointwise perturbativity diagnostic on the 144-point PBH headline grid

**Lane:** `LS12-pbh-perturbativity` · **Date written:** 2026-09-22 · **Status at writing: NO NUMBER HAS BEEN COMPUTED.**

This file is committed BEFORE the computation, alone, in its own commit. Nothing below is adjusted
afterwards; the outcome is recorded against these criteria verbatim, including every branch that goes
against the paper.

## 0. The open item, restated verbatim (not re-scoped)

`project-context/peer-reviews/DISPOSITIONS/A3M.md`, `DA3M-R12-06` [ESSENTIAL, PARTIAL], CONFIRMED real
and pre-existing:

> Channel II's headline $1.84\pm0.03$ is measured entirely inside the region Table V's own caption calls
> the non-perturbative branch, and the stated mechanism (large positive $\gamma_{\rm cr}=0.766$–$0.968$)
> does not apply to the headline window ($\gamma_{\rm cr}=0.267$–$0.630$).

R12 closed it by **honest disclosure only**. A3M `main.tex` currently says, in Sec. "Regime of validity":

> "$1.2|\fnl|\sigma_r\approx0.54$--$1.01$ at $-35/16$ and $\approx1.09$--$2.02$ at $-35/8$ on the displayed
> $27$-point grid … This diagnostic has not been separately evaluated point-by-point on the headline
> $144$-point in-coverage set … that the ratio's own $\gamma_{\rm cr}$-slope is measured continuous and
> consistent between the two grids is evidence the same qualitative regime applies, not a substitute for
> the pointwise diagnostic, which is left for future work."

and Table V's caption calls the $\gamma_{\rm cr}\lesssim0.8$ rows the *non-perturbative branch*, with
"$1.2|\fnl|\sigma_r\approx0.5$–$2$". The entire 144-point headline population has
$\gamma_{\rm cr}\in[0.267,0.630]$, i.e. lies **below** that threshold.

This lane runs the pointwise diagnostic. It is permitted to conclude against the paper.

## 1. The diagnostic, defined before it is computed

**Definition.** For a grid point $p$ and a value $\fnl$,

$$\varepsilon_p(\fnl) \;\equiv\; 1.2\,|\fnl|\,\sigma_r(p,\fnl),$$

where $\sigma_r$ is **the compaction script's own variance integral**, Choudhury et al. 2025 Eq. (53) as
implemented verbatim in `research/track_a3_multichannel/pbh_compaction_fnl.py::covariances` (and its
wide-$k$ twin `row11_pbh_residuals/row11_gammacr_extension.py::_cov_wide`, already validated there to
$5.7\times10^{-16}$ against the committed integrator):

$$\sigma_r^2 \;=\; \int \frac{dk}{k}\; W_s^2(kr_p)\, T^2(k,r_p)\, \Delta^2_\zeta(k;A),$$

with $W_s=\mathrm{sinc}$, $T$ the radiation transfer of Eq. (48), and $\Delta^2_\zeta$ the point's own
spectrum family:
* family **L**: lognormal of width $\Delta$, peak $k_p$, evaluated at $r_pk_p$;
* family **P**: power law $A(k/k_p)^{n_s-1}$ with IR cutoff $k_{\min}/k_p$.

Every one of $(\Delta\ \text{or}\ n_s,k_{\min}/k_p)$, $r_pk_p$, $C_{\rm th}$ is stored per point in
`row11_pbh_residuals/results/row11_gammacr_extension.json`. **Nothing is estimated, interpolated, or
scaled from an adjacent point.** The integral is re-run per point.

**Which amplitude $A$ enters.** This is the choice that decides what the diagnostic means, so it is fixed
here:

* **PRIMARY — the headline's own amplitudes.** The headline quantity is
  $A(-35/16)/A(-35/8)$ at fixed target $f_{\rm PBH}=10^{-3}$. Each leg of that ratio is a curvature
  amplitude *solved for at that $\fnl$*, and both are already stored per point as `A_-35/16` and
  `A_-35/8`. The diagnostic that decides whether the ratio is a controlled quantity is therefore
  $\varepsilon_p(-35/16)$ evaluated at $A=$ `A_-35/16`, and $\varepsilon_p(-35/8)$ evaluated at
  $A=$ `A_-35/8`. This is the primary result.
* **SECONDARY — the amplitude the paper's own printed numbers use.** The committed
  `outputs/pbh_compaction_fnl.json` stores $\sigma_r$ only in
  `calibrated_amplitude_comparison`, i.e. at the Gaussian-calibrated $A_*$ where $f_{\rm PBH}(\fnl{=}0)=1$,
  at the single shape $(\Delta,r_pk_p)=(0.5,1.0)$, for $C_{\rm th}=0.4/0.5/0.6$. Those three rows are
  reproduced as a validation gate (G3) and reported separately, because they are where the paper's printed
  "$0.54$–$1.01$" and "$1.09$–$2.02$" actually come from. If the paper's attribution of those numbers to
  "the displayed 27-point grid" does not survive this check, that is recorded as a finding, not smoothed over.

## 2. The threshold, fixed before it is computed

The paper's own criterion, Sec. V B and `r9_perturbativity/r9_perturbativity.py` (`PERT_COEFF = 1.2`,
"1.2 |f_NL| sigma <~ 1"):

$$\textbf{perturbative} \iff \varepsilon \le 1 .$$

A point $p$ of the headline population is **perturbative** iff **both** legs satisfy it:
$\varepsilon_p(-35/16)\le1$ **and** $\varepsilon_p(-35/8)\le1$. Rationale fixed in advance: the headline is
a *ratio of the two legs*; if either leg's quadratic map is uncontrolled, the ratio is not a controlled
quantity, regardless of the other leg.

Reported alongside, as pre-registered sensitivity only (never as the gate): the counts at
$\varepsilon\le0.5$ (comfortably perturbative) and $\varepsilon\le1.5$ (a 50 %-loose reading). The gate is
$\varepsilon\le1$.

## 3. Validation gates — all four must PASS before any of the other 117 points is trusted

* **G1** `_cov_wide` reproduces the committed narrow-grid `covariances` on the committed lognormal family
  to $<10^{-6}$ relative (the row-11 script's own `_validate_wide`, re-run here, not quoted from its log).
* **G2** The $\gamma_{\rm cr}$ recomputed from each stored point's own shape parameters reproduces that
  point's stored `gamma_cr` to $<10^{-10}$ relative, for **all 255** stored points. This is the gate that
  proves the JSON's stored shape parameters fully determine the integrand, and therefore that $\sigma_r$
  is reconstructible rather than guessed.
* **G3** $\sigma_r$ recomputed at $(\Delta,r_pk_p)=(0.5,1.0)$ and $A=A_*$ reproduces the three committed
  `calibrated_amplitude_comparison` values $0.20699892\ldots$, $0.28147149\ldots$, $0.38522840\ldots$ and
  their `perturbativity_1.2_absfNL_sigma_r` entries, to $<10^{-10}$ relative — i.e. reproduces the paper's
  printed $0.54$–$1.01$ / $1.09$–$2.02$ from scratch.
* **G4** $\gamma_{\rm cr}$ recomputed with the **narrow** integrator reproduces all 27 stored
  `robust_amplitude_requirement_grid` $\gamma_{\rm cr}$ values to $<10^{-10}$ relative. (The committed
  27-point grid used the narrow integrator; the 144-point grid used the wide one. They are checked
  against their own.)

If any gate fails, the lane reports **OUTCOME (c)** naming the failing gate and the exact missing or
inconsistent input, and stops. It does not proceed on a partially validated integrator.

## 4. The decision rule, including what would INVALIDATE the headline

Let $H$ be the headline population: the stored points with a finite ratio and
$\gamma_{\rm cr}\in[0.267,0.630]$ — reproduced from the JSON by the row-11 script's own selection, and
required to come out at $|H| = 144$ with mean $1.8374$, std $0.0312$, range $[1.759,1.891]$ (gate G5; a
mismatch here is also OUTCOME (c)). Let $P\subseteq H$ be the perturbative subset of §2.

* **OUTCOME (a) — HEADLINE STANDS.** $|P| = 144$. Every point of the headline population is perturbative
  by the paper's own criterion. The disclosure paragraph is replaced by the computation, quoting
  $\max_H\varepsilon$ at both legs.
* **OUTCOME (b) — HEADLINE MOVES.** $|P| < 144$. Then:
  * **(b0) WITHDRAW** if $|P| = 0$: no point of the headline population is in the controlled regime. The
    $1.84\pm0.03$ may not be quoted as a result; it becomes a diagnostic of an uncontrolled regime, and
    Channel II's robust output must be re-stated or dropped.
  * **(b1) WITHDRAW-FOR-THINNESS** if $0<|P|<20$, or if $P$ fails shape diversity — fewer than two
    spectrum families, or fewer than two distinct $C_{\rm th}$, or fewer than two distinct shape
    parameters. A "scan result" cannot rest on a population thinner than the 27-point grid the paper
    itself already declines to call universal.
  * **(b2) RE-SCOPE — CENTRAL VALUE CHANGES** if $|\mathrm{mean}(P) - 1.8374| > 0.0312$ (one quoted std),
    or $\mathrm{mean}(P)$ does not round to $1.84$ at 3 s.f. The printed central value must become
    $\mathrm{mean}(P)$ and the abstract changes.
  * **(b3) RE-SCOPE — SPREAD OR RANGE CHANGES** if $\mathrm{std}(P)$ does not round to $0.03$, or
    $[\min P,\max P]$ is not contained in $[1.755,1.895]$ (the printed $[1.76,1.89]$ at its own rounding).
  * **(b4) RE-SCOPE-LIGHT** otherwise: the central value, spread and range survive on $P$, but every
    statement of "$n=144$" must be re-stated as "$|P|$ perturbative of 144", and the
    still-non-perturbative points must be named in the paper, not summarised away.
* **OUTCOME (c) — NOT COMPUTABLE.** A gate fails, or a stored point lacks a parameter the integrand needs.
  The exact missing input is named and the lane stops. **No value is estimated from an adjacent point** —
  that prohibition is the reason this item exists (`/never-fabricate-derivation`).

Additional pre-registered report items, to be stated whichever branch fires:

* the $\varepsilon$ range over $H$ at each leg, and over the 27-point grid at its own ratio amplitudes;
* whether the paper's attribution of "$0.54$–$1.01$ / $1.09$–$2.02$" to "the displayed 27-point grid"
  is accurate (they are reproduced here from three $A_*$ calibration rows at one shape);
* whether $\varepsilon$ correlates with $\gamma_{\rm cr}$ in the direction the paper's continuity argument
  assumes, and whether the caption's "$\gamma_{\rm cr}\lesssim0.8$ = non-perturbative branch" equivalence
  survives pointwise;
* if OUTCOME (b) fires, the explicit list of non-perturbative points (family, shape, $r_pk_p$,
  $C_{\rm th}$, $\gamma_{\rm cr}$, both $\varepsilon$).

## 5. What this lane does NOT claim, fixed in advance

* It does not re-derive the compaction formalism, re-solve any $A(f_{\rm PBH})$, or change any number in
  `row11_gammacr_extension.json`. It reads that file's stored amplitudes and re-runs only the variance
  integral.
* $\varepsilon\le1$ is a *necessary* control diagnostic for the quadratic local map, not a proof of
  convergence of the truncated expansion. A population that passes is reported as "passes the paper's own
  criterion", never as "the expansion is proved convergent".
* The PBH channel's standing result — that the in-lab spectrum is 7.0 dex short and the channel is a NULL
  (ledger row 11 / A3-1b) — is untouched by this lane either way. What is at stake is only the
  *required-amplitude ratio* $1.84\pm0.03$ and its stated regime.
* No paper `.tex`, SSOT file or site datum is edited by this lane. Printable sentences go to
  `PROPAGATION_NOTE.md` for the A3M lane.
