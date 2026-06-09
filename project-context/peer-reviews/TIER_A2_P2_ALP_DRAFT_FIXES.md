# TIER A2 P2 ALP-birefringence drafts — drafted while fire 17 runs

Pre-drafted text replacements for the 2 remaining substantive TIER A2 items on
P2 (the spectator-ALP birefringence paper at
`research/focused_paper_source_integration/paper2_alp_birefringence.tex`).
Total effort: ~4h text + 10 min sync (more substantive than the quick-wins).

---

## #A3 — P2 f_a cancellation in β formula (fire-13 P2-META-E1)

**Meta-reviewer's catch**: With $g_{a\gamma} = C_0/f_a$ and
$\Delta\phi \approx f_a \theta_i \times F(m/H_0)$, Eq. (2) implies
$\beta = (C_0/2 f_a)\,\Delta\phi \approx (C_0 \theta_i/2)\,F(m/H_0)$:
**$f_a$ cancels.** The "Planck-scale decay constant" claim is therefore
irrelevant for the isotropic $\beta$ amplitude under the author's own
definitions.

**Diagnosis**: this is a real algebraic observation. f_a DOES cancel in the β
formula. The paper's central narrative ("f_a ~ M_Pl is the natural scale
for a gravitationally coupled pseudoscalar; this setup naturally produces
β ≈ 0.27°") conflates two distinct claims:
  - **claim A** (FALSE as written): "f_a ~ M_Pl is the reason β ≈ 0.27°"
  - **claim B** (TRUE): "f_a ~ M_Pl is required for the model to be EFT-consistent + spectator;
                         the β prediction depends on θ_i + m/H_0 + C_0, with f_a as a tagalong scale"

**Fix sites** (with new text):

### Site 1: Abstract (L23, line 23)
**OLD**: "We present predictions and constraints for cosmic birefringence from
a spectator axion-like particle (ALP) with Planck-scale decay constant
$f_a \sim M_{\rm Pl}$ and mass $m \sim H_0$. For order-unity inputs, this
minimal setup naturally accommodates a birefringence rotation angle
$\beta \approx 0.27^\circ$..."

**NEW**: "We present predictions and constraints for cosmic birefringence from
a spectator axion-like particle (ALP) with Planck-scale decay constant
$f_a \sim M_{\rm Pl}$ and mass $m \sim H_0$. For order-unity initial
misalignment $\theta_i \sim \mathcal{O}(1)$ and order-unity photon anomaly
coefficient $C_0 \sim \mathcal{O}(1)$, this minimal setup yields a birefringence
rotation angle $\beta \approx 0.27^\circ$...
\emph{Note on naturalness scope}: With $g_{a\gamma}\propto 1/f_a$ and
$\Delta\phi\propto f_a\,\theta_i\,F(m/H_0)$ along an ALP trajectory in a
$\Lambda$CDM background, $f_a$ cancels in the rotation amplitude $\beta
= (g_{a\gamma}/2)\,\Delta\phi \approx (C_0\theta_i/2)\,F(m/H_0)$. The
``$f_a\sim M_{\rm Pl}$'' choice is required by EFT consistency
(gravitationally-coupled pseudoscalar) and by the spectator-energy-density
constraint $\Omega_\phi\!\ll\!1$ (see Sec.~\ref{sec:spectator_caveat}); it is
not directly responsible for the magnitude of $\beta$ matching the observed
signal. The match depends on $\theta_i$ and $C_0$ both being $\mathcal{O}(1)$
at natural prior values."

### Site 2: §I Introduction (L32)
**OLD**: "In this paper, we consider the simplest ALP model: a single
spectator field with $f_a \sim M_{\rm Pl}$, $m \sim H_0$, and generic initial
misalignment $\theta_i \sim \mathcal{O}(1)$. We show that this setup naturally
produces $\beta \approx 0.27^\circ$---consistent with the observed
signal---without any fine-tuning."

**NEW**: same as above, with an inline parenthetical pointing to the abstract
footnote.

### Site 3: §IV.A Naturalness conclusion (L169)
**OLD**: "\textbf{Naturalness:} All input parameters ($f_a \sim M_{\rm Pl}$,
$m \sim H_0$, $\theta_i \sim 1$) are at their natural scales. No tuning is
required."

**NEW**: "\textbf{Naturalness:} The $\beta$-determining inputs ($\theta_i \sim 1$
and $C_0 \sim 1$) are at their natural scales; $f_a$ cancels in the $\beta$
amplitude and is fixed by spectator-energy-density and EFT-consistency
considerations rather than by tuning to $\beta_{\rm obs}$ (see
Sec.~\ref{sec:spectator_caveat} for the $m_\theta\sim H_0$ cosmological-constant-class
tuning that is required separately to maintain the spectator condition)."

### Site 4: Conclusion (L180)
**OLD**: "The model requires no fine-tuning of dimensionless parameters: all
inputs are at their natural scales..."

**NEW**: "The model requires no fine-tuning of the $\beta$-determining
dimensionless parameters ($\theta_i \sim 1$, $C_0 \sim 1$) beyond the
$m_\theta\sim H_0$ ultralight-mass tuning that maintains the spectator
condition (this is a cosmological-constant-class tuning shared with all
ultralight-ALP cosmic-birefringence proposals; see
Sec.~\ref{sec:spectator_caveat})."

Closes fire-13 P2-META-E1.

---

## #A4 — P2 spectator-ALP claim conflicts with Ω_φ ≈ 0.17 at θ_i~1 (fire-13 P2-META-E2)

**Meta-reviewer's catch**: For $m \approx H_0$, $f_a \approx M_{\rm Pl}$,
$\theta_i \approx O(1)$:
$\Omega_\phi \approx (1/6)(m/H_0)^2 \theta_i^2 \approx 0.17$ today — that is
NOT a spectator. For $m/H_0 \gtrsim 10$ (hinted in Fig. 1),
$\Omega_\phi \gg 1$ — incompatible with $\Lambda$CDM.

**Diagnosis**: The math is right. At $\theta_i\sim 1$ and $f_a\sim M_{\rm Pl}$
and $m\sim H_0$, ALP today has $\Omega_\phi\sim 0.17$, comparable to dark
energy. Calling it a "spectator field that does not participate in the bounce
dynamics" is inconsistent with this energy budget.

**Fix**: add a new §III subsection acknowledging the spectator-condition
constraint + restrict $\theta_i$ to the spectator-allowed range.

### Site: new §III subsection between §III.A and existing text
(or as a footnote on the L158 spectator-claim paragraph)

**NEW**:
```latex
\subsection{Spectator-condition energy-density constraint}\label{sec:spectator_caveat}

The ``spectator-field'' framing requires the ALP to contribute negligibly to
today's cosmic energy budget, $\Omega_\phi \ll 1$. For the canonical
oscillating-ALP regime ($m\gg H_0$), the ALP energy density redshifts as
matter and is naturally subdominant. In the slow-rolling regime relevant here
($m\sim H_0$), the ALP energy density today is
\begin{equation}
\rho_\phi(z\!=\!0) \approx \tfrac{1}{2}\,m^2 f_a^2\,\theta_i^2
\quad\Rightarrow\quad
\Omega_\phi(z\!=\!0) \approx \frac{1}{6}\left(\frac{m}{H_0}\right)^2
\left(\frac{f_a}{M_{\rm Pl}}\right)^2 \theta_i^2.
\end{equation}
At $f_a\sim M_{\rm Pl}$, $m\sim H_0$, and natural $\theta_i\sim \mathcal{O}(1)$,
this gives $\Omega_\phi\!\sim\!0.17$ today --- comparable to dark energy
rather than negligible. The strict spectator regime ($\Omega_\phi \ll 1$)
therefore requires either (a)~suppressing $\theta_i$ to
$\sim\!\sqrt{0.05}\,\theta_{\rm nat}\!\approx\!0.2$ (a $\sim\!25\!\times$ fine-tuning
of the initial misalignment relative to the natural prior midpoint, as already
flagged in the Paper~I(a) Sec.~\ref{sec:r4_birefringence} discussion), or (b)~suppressing $f_a$ below the
Planck scale by the same factor (which breaks the ``Planck-scale natural''
framing), or (c)~reinterpreting the ALP as a dark-energy-like component
contributing $\Omega_\phi\!\sim\!0.17$ to the present-day budget (allowed
under $\Lambda$CDM at the $\sim\!10\%$ level by current constraints but not
within the strict spectator framing).

The cosmological-birefringence prediction $\beta\approx 0.27^\circ$
\emph{itself} does not depend on which option (a, b, c) is taken --- $f_a$
cancels in the $\beta$ amplitude (see Sec.~\ref{sec:beta_prediction}) and
the prediction depends only on $\theta_i$, $C_0$, and $F(m/H_0)$. We adopt
option (a) ($\theta_i\sim 0.2$, with $f_a\sim M_{\rm Pl}$ retained for
spectator-EFT consistency) as the headline parameter point, in which case
the $\beta\sim 0.27^\circ$ prediction continues to hold by the cancellation
above; the $\sim\!25\!\times$ misalignment tuning is the same one that
Paper~I(a) flags as a cosmological-constant-class tuning rather than an
ALP-naturalness tuning.

Throughout the rest of this paper, ``spectator'' refers to the
$\Omega_\phi\!\ll\!1$ regime obtained at $\theta_i\!\sim\!0.2$; the
$\theta_i\!\sim\!1$ regime ($\Omega_\phi\!\sim\!0.17$) is the
dark-energy-like regime and is constrained by the
cosmological-parameter-fit channel separately.
```

Closes fire-13 P2-META-E2.

---

## Bundling plan

After fire 17 closes:
1. Apply edits to research/focused_paper_source_integration/paper2_alp_birefringence.tex
2. Recompile P2
3. Mirror PDFs (flat + versioned)
4. Bump version: P2 v1.7.43 → v1.7.44
5. Update papers.ts + live-status.ts
6. Bundled bump via v3_bundled_paper_bump.mjs
7. Single commit
8. Add to closure ledger

Total effort: ~3h text (the structural fix is substantive) + ~10 min sync.

## Cross-links

The P1A v1A.0.46 fine-tuning closure (#A6) cites the same cosmological-constant-class tuning that this P2 fix needs to acknowledge. Cross-references should be:
- P1A §sec:r4_birefringence → P2 sec:spectator_caveat
- P2 sec:spectator_caveat → P1A sec:r4_birefringence
