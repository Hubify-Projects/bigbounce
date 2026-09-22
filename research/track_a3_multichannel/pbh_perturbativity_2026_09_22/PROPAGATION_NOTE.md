# PROPAGATION NOTE — LS12 → the A3M lane

**From** `LS12-pbh-perturbativity` (2026-09-22) · **Closes** `DA3M-R12-06` [ESSENTIAL, PARTIAL] **by
computation**, replacing R12's honest disclosure.
**Evidence** `research/track_a3_multichannel/pbh_perturbativity_2026_09_22/`
(`PREREGISTRATION.md` committed alone at `b289aa0f`; `pbh_perturbativity.py`, `results.json`,
`threshold_sensitivity.json`, `pbh_perturbativity.png`, `PBH_PERTURBATIVITY_2026-09-22.md`);
manifest `reproducibility/manifests/experiments/a3-pbh-perturbativity-pointwise.json`.

**This lane touched no `.tex`, no SSOT file and no site datum.** Everything below is for the A3M lane to
apply under directive-G hygiene in its own bundle.

---

## 0. The one-line consequence

The headline moves: **`1.84 ± 0.03` (n = 144) → `1.81 ± 0.02` (n = 62)** when the paper's own
perturbativity criterion is enforced pointwise. It is **re-scoped, not withdrawn**. The shift (0.025) is
inside the currently quoted std (0.031), so no scientific conclusion of Channel II changes — but the
printed three-significant-figure value does, in the abstract and in three body locations, and the sentence
saying the diagnostic "has not been separately evaluated point-by-point … left for future work" is now
false and must go.

## 1. Numbers, verified, for the A3M lane to use

| quantity | value |
|---|---|
| headline window H (what is printed now) | n = 144, ratio 1.8374, std 0.0312, range [1.7594, 1.8915] |
| perturbative subset P (`eps <= 1` at both legs) | **n = 62, ratio 1.8121, std 0.0241, range [1.7594, 1.8511]** |
| non-perturbative complement | n = 82, ratio 1.8565, std 0.0205, range [1.7972, 1.8915] |
| `eps(-35/16)` over H | [0.543, 1.048], median 0.703 |
| `eps(-35/8)` over H | [0.817, 1.534], median 1.035 |
| points failing per leg | `-35/8`: 82; `-35/16`: 1 |
| by threshold | `C_th=0.4`: 47 of 48 perturbative · `C_th=0.5`: 15 of 48 · `C_th=0.6`: **0 of 48** |
| `gamma_cr` span of P vs of H\P | identical, [0.2679, 0.6298] — `gamma_cr` does not discriminate |
| ratio vs `eps` inside H | Pearson `+0.829`, OLS slope `+0.161` per unit `eps` |
| points with `eps <= 0.5` | **0 of 144** |
| 27-point window at its own ratio amplitudes | `eps(-35/16)` [0.635, 2.220]; `eps(-35/8)` [0.965, 3.217] |

## 2. Exact printable sentences

### 2.1 REPLACE the "Regime of validity" passage (`main.tex`, the sentences beginning "\emph{Regime of validity.} The result lives on the anti-correlated…" through "…which is left for future work.")

> \emph{Regime of validity.} The result lives on the anti-correlated ($\gamma_{\rm cr}>0$, $J>1$) branch
> identified above, and the perturbativity of the quadratic local map has now been evaluated
> \emph{pointwise} across the full $144$-point in-coverage set, each point at its own required amplitude:
> $1.2|\fnl|\sigma_r$ runs $0.54$--$1.05$ at $-35/16$ and $0.82$--$1.53$ at $-35/8$, so the criterion
> $1.2|\fnl|\sigma_r\lesssim1$ is satisfied at both candidate values at $62$ of the $144$ points and
> violated at the remaining $82$ (all $48$ points at $C_{\rm th}=0.6$, $33$ of $48$ at $C_{\rm th}=0.5$,
> $1$ of $48$ at $C_{\rm th}=0.4$; the $-35/8$ leg is the binding one, the $-35/16$ leg failing at a
> single point). Restricted to the $62$ points that satisfy it, the required-amplitude ratio is
> $1.81~[1.76,\,1.85]$, ${\rm std}=0.02$ --- the value quoted in Eq.~\eqref{eq:pbh_ratio} and in the
> abstract. Two facts are recorded against it rather than around it: no point of the in-coverage set
> reaches $1.2|\fnl|\sigma_r\le0.5$, so the population is marginal throughout; and the ratio is
> correlated with the diagnostic itself (Pearson $+0.83$, slope $+0.16$ per unit $1.2|\fnl|\sigma_r$
> across the window), so the subset mean slides with the threshold, from $1.798$ at a cut of $0.9$ to the
> full-window $1.837$ at $1.4$. The ratio is therefore a result within a stated and
> threshold-conditional regime, not a claim of general validity, and a cut-independent Channel~II
> observable would require the resummed (non-quadratic) map left open above. This is the same class of
> limitation Choudhury \textit{et al.} report as their own $|\fnl|\lesssim60$ perturbativity bound, and a
> limitation of the shared quadratic ansatz rather than of either calculation specifically.

### 2.2 REPLACE Eq. `eq:pbh_ratio` and its lead-in

> reaching the floor of the Choudhury \textit{et al.} band, $\fpbh = 10^{-3}$, requires
> \begin{equation}
>   \frac{A(-35/16)}{A(-35/8)} = 1.81~[1.76,\,1.85],\quad {\rm std}=0.02,\ n=62,
>   \label{eq:pbh_ratio}
> \end{equation}
> over the points of the $\gamma_{\rm cr}\in[0.267,0.630]$ in-coverage set --- the interval this model's
> own near-scale-invariant spectrum shape occupies --- that satisfy the paper's own perturbativity
> criterion at both candidate values ($62$ of $144$; see \emph{Regime of validity} below). Without that
> restriction the same $144$ points give $1.84~[1.76,\,1.89]$, ${\rm std}=0.03$; on the narrower,
> original $27$-point fiducial grid ($\gamma_{\rm cr}\in[0.766,0.968]$, whose own pointwise diagnostic is
> \emph{worse}, $1.2|\fnl|\sigma_r$ up to $2.2$ and $3.2$ at the two candidate values) the ratio is
> $1.732~[1.610,\,1.809]$, ${\rm std}=0.050$, and must not be quoted as universal.

### 2.3 ABSTRACT — replace "PBHs (ratio $1.84\pm0.03$ within this model's own $\gamma_{\rm cr}$ coverage, …"

> PBHs (ratio $1.81\pm0.02$ over the perturbatively controlled points of this model's own
> $\gamma_{\rm cr}$ coverage, $6.7$--$7.0$ decades short, $\fpbh=0$)

### 2.4 DISCUSSION — replace "Primordial black holes yield a reproducible amplitude ratio ($1.84\pm0.03$ within this model's own $\gamma_{\rm cr}$ coverage)"

> Primordial black holes yield a reproducible amplitude ratio ($1.81\pm0.02$ over the perturbatively
> controlled points of this model's own $\gamma_{\rm cr}$ coverage; $1.84\pm0.03$ if the uncontrolled
> points are retained)

### 2.5 Sec. `sec:pbh_inlab` — replace "inside the model's own $\gamma_{\rm cr}\in[0.267,0.630]$ coverage the required-amplitude ratio is $1.84\pm0.03$ across a threshold scan $C_{\rm th}\in\{0.4,0.5,0.6\}$"

> inside the model's own $\gamma_{\rm cr}\in[0.267,0.630]$ coverage the required-amplitude ratio is
> $1.81\pm0.02$ over the perturbatively controlled points of a threshold scan
> $C_{\rm th}\in\{0.4,0.5,0.6\}$ --- the whole of $C_{\rm th}=0.6$ being excluded by that criterion, and
> $1.84\pm0.03$ if the uncontrolled points are retained

### 2.6 TABLE V CAPTION — two required corrections

(i) Replace the headline sentence "the headline $1.84\pm0.03$ below comes from the $144$-point
in-coverage subset of the extended scan" with:

> the headline $1.81\pm0.02$ below comes from the $62$ perturbatively controlled points of the
> $144$-point in-coverage subset of the extended scan

and correspondingly "$\mathbf{1.84\pm0.03}$ ($144$ points, range $[1.76,1.89]$; …)" with
"$\mathbf{1.81\pm0.02}$ ($62$ of $144$ points, range $[1.76,1.85]$; the full $144$ give
$1.84\pm0.03$, range $[1.76,1.89]$)". **The $78$-lognormal/$66$-power-law split refers to the full
$144$; the controlled subset is $34$ lognormal and $28$ power-law.**

(ii) **The "non-perturbative branch" label attached to the $\gamma_{\rm cr}\lesssim0.8$ rows is
inverted and must be corrected.** Measured pointwise at each point's own required amplitude,
$1.2|\fnl|\sigma_r$ \emph{rises} with $\gamma_{\rm cr}$ (Pearson $+0.32$ over the $255$-point scan), and
the $\gamma_{\rm cr}\in[0.766,0.968]$ window is the \emph{less} controlled of the two ($[0.64,2.22]$ and
$[0.97,3.22]$ versus $[0.54,1.05]$ and $[0.82,1.53]$ in the headline window). Replace the parenthetical
"(\emph{non-perturbative branch}; $1.2|\fnl|\sigma_r\approx0.5$--$2$, …)" with:

> (\emph{uncapped-abundance rows}; these are the rows whose Gaussian-calibrated $\fpbh$ exceeds unity,
> an amplitude-calibration statement and not a perturbativity one --- the pointwise diagnostic
> $1.2|\fnl|\sigma_r$ in fact \emph{increases} with $\gamma_{\rm cr}$, reaching $2.2$ and $3.2$ at the
> two candidate values on this grid's own required amplitudes, against $1.05$ and $1.53$ on the
> headline in-coverage set)

### 2.7 One accuracy correction the A3M lane must make wherever it appears

The printed "$1.2|\fnl|\sigma_r\approx0.54$--$1.01$ at $-35/16$ and $\approx1.09$--$2.02$ at $-35/8$ on
the displayed $27$-point grid" is **reproduced exactly** by this lane — but from the three
Gaussian-calibration rows of `outputs/pbh_compaction_fnl.json` at the single shape
$(\Delta, r_pk_p) = (0.5, 1.0)$, $C_{\rm th} = 0.4/0.5/0.6$, evaluated at $A_*$ (where
$\fpbh(\fnl{=}0)=1$), which is **not** the amplitude the ratio is defined at. The attribution "on the
displayed 27-point grid" is inaccurate; either say "at the Gaussian-calibrated amplitude $A_*$ of the
representative shape $(\Delta,r_pk_p)=(0.5,1.0)$" or replace the numbers with the 27-point window's own
ratio-amplitude values $[0.64, 2.22]$ / $[0.97, 3.22]$.

### 2.8 Reproducibility statement — add

> The pointwise perturbativity diagnostic of Sec.~\ref{sec:pbh_compaction} is
> \artifact{research/track\_a3\_multichannel/pbh\_perturbativity\_2026\_09\_22/}
> (\texttt{pbh\_perturbativity.py}, \texttt{results.json},
> \texttt{threshold\_sensitivity.json}; pre-registration committed before the computation), manifest
> \texttt{reproducibility/manifests/}\allowbreak\texttt{experiments/}\allowbreak\texttt{a3-pbh-perturbativity-pointwise.json}.
> It re-runs the committed variance integral at each scan point's own required amplitude and reproduces
> the committed $\gamma_{\rm cr}$ and $\sigma_r$ values exactly.

### 2.9 Directive-I6 figure sweep — REQUIRED

`1.84` and `1.732` appear inside committed figure images. Before this closure lands, inventory every
`\includegraphics` in `main.tex` and check each rendered figure for the superseded value:
**`row11_pbh_residuals/results/row11_gammacr_extension.png` bakes the "quoted 1.7-1.9" band and the
in-lab/committed shading into the image**, and any figure reproducing the headline number must be
regenerated (preferably by re-running the committed generator with the new subset overlay) and re-mirrored
byte-identically. A text grep cannot see these. `pbh_perturbativity.png` in this lane's directory is
available as a drop-in panel if the A3M lane wants the diagnostic shown.

## 3. Is this the next directive-R2 intervening science decision?

**Yes — this lane's result is a directive-R2 intervening science decision, and it lifts A3M's "no further
board without another intervening science or scope decision" stop.** Grounds:

1. It is **new computation**, not a re-reading: 255 variance integrals at the points' own required
   amplitudes, gated against the committed artifacts (three gates exact to machine zero), pre-registered
   before any number existed.
2. It **changes a printed headline value** in the abstract and four body locations, changes `n` from 144
   to 62, changes a table caption's physical label, and deletes a stated limitation — i.e. it is exactly
   the "science or scope decision" R2 requires, not another presentation pass.
3. It **closes the one ESSENTIAL item R12 could only disclose**, which `DISPOSITIONS/A3M.md` names as
   A3M's "next unlock".

The decision to record (suggested id **D-A3-15**): *Channel II's required-amplitude ratio is quoted on
the perturbatively controlled subset of its own in-coverage grid, `1.81 ± 0.02` (n = 62 of 144), with the
threshold-dependence and the `eps ~ O(1)` marginality of the whole population stated rather than
suppressed; the `gamma_cr <~ 0.8` "non-perturbative branch" label is corrected to an
uncapped-abundance label.*

**Ordering for the A3M lane:** apply §2.1–2.9 in one directive-G bundle (version bump, 4-pass recompile,
`/latex-audit`, byte-identical mirrors, the I6 figure sweep) **first**; only then is the confirmation
board R2 now permits worth spending, since it would otherwise review superseded numbers.

## 4. What this does NOT license

* It does not license quoting `1.81 ± 0.02` as a cut-independent number. §2.1's correlation sentence is
  not optional trimming — without it the new value is a worse misstatement than the old one.
* It does not change Channel II's scientific conclusion. The in-lab spectrum is still 7.0 dex short and
  the PBH channel is still a NULL (`f_PBH = 0`). Ledger row 11 / A3-1b stand.
* It does not resolve open item A3-1c (the resummed, non-quadratic NG map), which is the only route to a
  Channel II ratio that does not depend on where the perturbativity cut is placed.
