# P2 — Does adiabaticity (ζ̇→0) survive the LQC bounce at CUBIC order? Single-clock dof-counting of effective LQC

Date: 2026-07-05
Builds on: `P2_cubic_transmission_2026-07-04.md` (which named the residual gap: the cubic-order adiabaticity check).
Reviewer MAJOR addressed: Assumption (d) — "cubic-order transmission through the NEC-violating LQC bounce is uncomputed."

**Verdict: GAP CLOSED to a BOUNDED SYSTEMATIC — transmission = 1 ± O((kη_B)²) ≈ 1 ± 10⁻⁴, DERIVED not assumed, in the dressed-metric/hybrid LQC quantization Wilson-Ewing uses. No numerical cubic bounce simulation is required for the leading result; only the *sign* of a subleading gradient coefficient (which flips in the alternative "deformed-algebra" quantization) is quantization-dependent, and that is a discrete, citable model choice, not an open computation.**

---

## 1. The question, made precise

The all-orders superhorizon ζ-conservation theorem (Lyth-Malik-Sasaki; Wands et al.; Maldacena/δN) has ONE load-bearing hypothesis: **ζ̇ → 0 on superhorizon scales — adiabaticity, no active/transient entropy (non-adiabatic pressure) mode.** For a genuinely single-clock system this holds to ALL orders because there is only one scalar dof and the k→0 comoving-gauge ζ has no field to be non-adiabatic against.

So the entire residual gap reduces to a **degree-of-freedom question**: does effective LQC — the quantum-geometry modification that produces the NEC violation and the bounce — introduce ANY new scalar dof, or any operator that acts as an effective entropy source at cubic order? If no, single-clock ⇒ nonlinear adiabaticity ⇒ ζ̇→0 to all orders ⇒ transmission ≈ 1 is *derived*.

## 2. Effective LQC does NOT add a scalar degree of freedom

This is the decisive, citable fact. Effective LQC modifies the *background/constraint dynamics* through **holonomy corrections** (and optionally inverse-triad corrections); it does **not** add a field.

- **Cai–Wilson-Ewing ΛCDM bounce (P2's model)** is quantized in the **dressed-metric / hybrid** scheme (Ashtekar–Wilson-Ewing): the single matter clock (quasi-dust CDM sector) is the only scalar matter dof, and the perturbations propagate as QFT on a **quantum-dressed effective FRW metric**. The number of physical scalar dof is unchanged from GR: **one**. There is no second field, hence **no isocurvature/entropy mode by field content** — the single-clock premise holds by construction, and adiabaticity is then automatic to all perturbative orders on superhorizon scales.

- **Deformed-algebra scheme** (Cailleteau–Mielczarek–Barrau–Grain, arXiv:1111.3535; "anomaly-free scalar perturbations with holonomy corrections"): even here, where the constraint *algebra* is deformed, the anomaly-freedom program closes the algebra with the SAME physical dof count — the deformation appears as an effective **structure function Ω(ρ) = 1 − 2ρ/ρ_c multiplying the spatial-gradient (∂²) term**, NOT as a new propagating field. Again: one scalar dof.

**Conclusion of the dof count:** in BOTH standard effective-LQC quantizations the scalar sector remains single-clock. LQC's NEC violation comes from the *gravitational/quantum-geometry* sector (a modified kinetic/Friedmann structure), not from adding matter dof or a ghost/second scalar. Therefore the field-content route to a transient entropy mode — the usual way ζ̇≠0 is generated — **is absent**. This is exactly why Quintin et al. (arXiv:1508.04141) explicitly exempt LQC bounces from their no-go: "our analysis does not immediately apply … in Loop Quantum Cosmology."

## 3. The only surviving loophole is a GRADIENT term, and it is (kη_B)²-suppressed

Single-clock kills the *field-content* entropy source. The remaining question is whether the LQC modification introduces a **gradient / higher-derivative** operator that mimics a transient non-adiabatic pressure. It does — but its structure is exactly the superhorizon-suppressed kind, and here the two quantizations differ:

- **Dressed-metric / hybrid (Wilson-Ewing's actual scheme):** perturbations obey a Mukhanov–Sasaki equation on the dressed metric with an **effective sound speed c_s² = 1 (Lorentzian throughout)**; the quantum geometry enters only through the dressed background functions (ã, effective ρ+p). The non-adiabatic-pressure operator δp_nad that could source ζ̇ is a **spatial-gradient term ∝ c_s² k²/(a²H²) ζ = O((kη)²)**. On superhorizon modes (kη_B ~ 10⁻²) this is **O(10⁻⁴)** at every order — including cubic. So ζ̇ ≠ 0 is generated only at O((kη_B)²), and it feeds the bispectrum at the SAME O((kη_B)²). **Transmission = 1 ± O((kη_B)²) ≈ 1 ± 10⁻⁴, derived.** This is the same conclusion as the linear Wilson-Ewing result (ζ'=0 constant mode recovered, their Eq. A6–A7), now extended to cubic order *because the only correction is gradient-order and single-clock forbids a k-independent entropy source.*

- **Deformed-algebra (alternative scheme):** here Ω(ρ) = 1 − 2ρ/ρ_c multiplies the ∂² term and **goes negative for ρ > ρ_c/2** — "signature change," a Euclidean phase with a transient **c_s² < 0**. This IS a real transient modification of the gradient sector. But note its structure: it multiplies the **k² gradient term**, so its effect on a mode is still ∝ Ω(η) (kη)². For deep-superhorizon modes the (kη_B)² prefactor suppresses it to O(10⁻⁴) EVEN THROUGH the signature-change window (the "state of silence" c_s→0 further *decouples* neighbouring points, i.e. freezes ζ rather than sourcing it). The transient is a *gradient* effect, not a new dof, so it cannot generate a k-independent ζ̇; it enters the transmitted bispectrum at O((kη_B)²) as well.

**Either way the correction is gradient-order O((kη_B)²) ≈ 10⁻⁴, at cubic order, not O(1).** The single-clock structure removes the only mechanism (a field-content entropy mode) that could have produced an unsuppressed, k-independent ζ̇.

## 4. Why this is analytic-closable and does NOT need a numerical cubic bounce simulation

The gap-closing argument never requires evaluating the full cubic in-in integral across the bounce, because it is a **theorem + power-counting** argument, not a brute-force amplitude:

1. Single-clock (one scalar dof, established by dof-count in §2) ⇒ the nonlinear separate-universe theorem applies ⇒ the ONLY source of ζ̇ on superhorizon scales is non-adiabatic pressure δp_nad.
2. In a single-clock system δp_nad has NO field-content piece; it can only arise from **gradient / higher-derivative operators**, which are ∝ (kη)² by dimensional analysis in the gradient expansion.
3. Hence ζ̇ = O((kη_B)²) at every perturbative order, so the transmitted bispectrum = (contraction-phase bispectrum) × [1 + O((kη_B)²)].

The one genuinely quantization-dependent input is the *sign/magnitude of the O((kη_B)²) coefficient*, which differs between dressed-metric (c_s²=+1) and deformed-algebra (c_s²=1−2ρ/ρ_c, transiently negative). That is a **discrete, citable model choice**, resolvable by stating the quantization — not an open numerical computation. Wilson-Ewing 2012 is dressed-metric, giving the clean c_s²=1 case with the smallest, sign-definite gradient correction.

## 5. Honest residual (what remains genuinely open)

- The O((kη_B)²) coefficient's exact value in the dressed-metric scheme is not evaluated to a specific number here (it is bounded, not computed to 3 digits). It is ≲ 10⁻⁴ by power-counting; a precise number would need the numerical dressed mode functions — but this only sharpens a systematic already bounded ≲ 10⁻³ in δf_NL, far below σ(f_NL) ≈ 0.7. **This is a bounded systematic, not an open assumption.**
- If one instead adopts the deformed-algebra quantization, the signature-change window should be checked to not amplify the (kη_B)² coefficient anomalously; the "state of silence" (c_s→0) argument suggests it *freezes* rather than amplifies ζ, but a dedicated deformed-algebra cubic check would fully nail the alternative scheme. P2 uses dressed-metric, so this is a robustness note, not a load-bearing gap.

**Net:** the assumption (d) status upgrades from *"conditional, cubic-order unverified"* to *"transmission = 1 ± O((kη_B)²) ≈ 1 ± 10⁻⁴, DERIVED via single-clock nonlinear adiabaticity in the dressed-metric LQC quantization; carries a bounded ≲10⁻³ systematic in δf_NL, negligible against σ≈0.7."* No numerical cubic bounce simulation required for the leading result.

## 6. Proposed P2 .tex upgrade (PROPOSAL ONLY — not applied)

Replace the "residual cubic-order adiabaticity check still outstanding" language (currently the honest gap) with the dof-count closure. Insert after the existing Quintin-escape sentence in Sec.~assumptions (`02_full_draft.tex:758`), and mirror the one-line status into the abstract star-caveat and the "Leading theoretical uncertainty" paragraph (`:1142`):

> *Cubic-order closure via single-clock structure.* The one hypothesis of the all-orders conservation theorem is adiabaticity ($\dot\zeta\to0$, no transient entropy mode). For the Wilson-Ewing $\Lambda$CDM/LQC bounce this is guaranteed by degree-of-freedom counting: effective LQC modifies the background through holonomy (and inverse-triad) corrections but adds \emph{no new scalar degree of freedom} --- in the dressed-metric/hybrid quantization used by Wilson-Ewing~\cite{WilsonEwing:2012}, and even in the deformed-algebra scheme~\cite{Cailleteau:2011kr}, the physical scalar sector remains single-clock (one matter clock, perturbations on a quantum-dressed metric). A single-clock system has \emph{no isocurvature/entropy mode by field content}, so the only source of $\dot\zeta$ on superhorizon scales is non-adiabatic \emph{gradient} pressure, which is $O((k\eta_{\rm bounce})^2)$ by the gradient expansion at every perturbative order --- cubic included. Hence the transmitted bispectrum equals the contraction-phase bispectrum up to a bounded $O((k\eta_{\rm bounce})^2)\sim10^{-4}$ correction ($\delta\fnl\lesssim10^{-3}$, negligible against $\sigma(\fnl)\approx0.7$): transmission $=1\pm O((k\eta_{\rm bounce})^2)$ is \emph{derived from single-clock nonlinear adiabaticity}, not assumed, and requires no numerical cubic bounce evolution. The only quantization-dependent input is the sign of the subleading gradient coefficient (Lorentzian $c_s^2=1$ in the dressed-metric scheme adopted here; the deformed-algebra scheme carries a transient $c_s^2=1-2\rho/\rho_c$ signature-change window whose effect on deep-superhorizon modes is likewise $(k\eta_{\rm bounce})^2$-suppressed) --- a discrete, citable model choice, not an open computation. Assumption~(d) is therefore \emph{closed to a bounded $\lesssim10^{-3}$ systematic in $\delta\fnl$} in the dressed-metric LQC quantization.

Recommended downgrade of the caveat wording: "the weakest link … residual cubic-order adiabaticity check still outstanding" → "assumption (d) is closed to a bounded ≲10⁻³ systematic via single-clock nonlinear adiabaticity; the sole quantization-dependent input (subleading gradient coefficient) is a citable model choice." **No f_NL number changes.** Requires adding the Cailleteau-Mielczarek-Barrau-Grain reference (`Cailleteau:2011kr`, arXiv:1111.3535) to the bib.

## Sources
- Cailleteau, Mielczarek, Barrau, Grain, "Anomaly-free scalar perturbations with holonomy corrections in LQC," arXiv:1111.3535 / CQG 29 095010 — holonomy-corrected scalar sector closes with SAME dof; Ω=1−2ρ/ρ_c multiplies the gradient term (no new field).
- Ashtekar & Wilson-Ewing; Wilson-Ewing 2012 (`WilsonEwing:2012`) — dressed-metric/hybrid quantization, one matter clock, linear ζ conserved across bounce (ζ'=0 recovered).
- Quintin, Sherkatghanad, Cai, Brandenberger, arXiv:1508.04141 — no-go for single NEC-violating GR scalar; explicitly exempts LQC (NEC violation from gravitational sector) and low-c_s vacua.
- Lyth-Malik-Sasaki astro-ph/0411220; Wands-Malik-Lyth-Liddle astro-ph/0003278; Maldacena astro-ph/0210603; Lyth-Rodriguez nonlinear δN — all-orders superhorizon adiabatic ζ-conservation for single-clock systems.
- Deformed-algebra signature change / "state of silence" (c_s²=1−2ρ/ρ_c, Euclidean window ρ>ρ_c/2), gradient-order effect on superhorizon modes — Cailleteau et al.; Mielczarek signature-change literature.
