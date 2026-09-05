# Ledger row 11 — PBH channel residuals (items a, b)

Date: 2026-09-04 · Track A3 multichannel · status: IN PROGRESS

## Scope
- (a) Locate the Choudhury et al. 2025 sign disagreement on the compaction-function
  f_NL response operator-by-operator; settle whether negative local f_NL suppresses
  or enhances PBH abundance at fixed Gaussian amplitude; name the responsible term.
- (b) Extend the compaction γ_cr scan to [0.2, 1.0] and report
  A(-35/16)/A(-35/8) inside the in-lab shape's coverage γ_cr ∈ [0.267, 0.630];
  state whether "1.7-1.9" survives, changes, or is dropped.
- (c) second-order δN threading identity — NOT in this session's scope.

## Method
Small-f_NL analytic expansion of the compaction threshold + numerical check in
`row11_choudhury_sign.py`; independent γ_cr grid rerun in
`row11_gammacr_extension.py` (new outputs, committed outputs untouched).
No tuning: the amplitude solver targets a fixed reference abundance only.

## Verdicts
(filled in below as the work lands)

---

# Item (a) — the Choudhury *et al.* 2025 sign disagreement, located

**Script:** `row11_choudhury_sign.py` · **Output:** `results/row11_choudhury_sign.json`
**Verdict: NOT a disagreement of formulae.** Every operator in the chain is
identical in the two calculations. The sign is decided by a single coefficient,
and that coefficient is a property of the **spectrum shape**, not of the
non-Gaussianity.

## 1. The operator chain, side by side

| # | operator | this lab (`pbh_compaction_fnl.py`) | Choudhury *et al.* 2025 (arXiv:2409.18983) | agree? |
|---|---|---|---|---|
| O1 | NG map | ζ = ζ_G + (3/5) f_NL (ζ_G² − ⟨ζ_G²⟩) | their Eq. (35), same | ✔ |
| O2 | Jacobian | J = dζ/dζ_G = 1 + (6/5) f_NL ζ_G | same | ✔ |
| O3 | compaction | C = −f(w) rζ′[2 + rζ′], f(w) = 2/3; C = C_lin − C_lin²/(4f), C_lin = C_G J, C_G = −2f rζ_G′ | their Eqs. (30), (40) | ✔ |
| O4 | threshold | C ≥ C_th ⇔ C_lin ≥ C_lin,− = 2f[1 − √(1 − C_th/f)] (type I) | their Eqs. (61), (63)–(65) | ✔ |
| O5 | joint PDF | bivariate normal in (C_G, ζ_G), correlation γ_cr = σ_cr²/(σ_c σ_r) | their Eqs. (49)–(50), (52)–(54) | ✔ |
| O6 | abundance | β = ∫_D K(C − C_th)^0.36 P_G dC_G dζ_G | their Eq. (60) | ✔ |

Choudhury *et al.*'s claim (full text, §PBH abundance): *"f_NL<0 is considered
more favourable to suppress the PBH abundance"*, with a **sharply peaked USR/RRR**
Δ²_ζ. The lab's `PBH_COMPACTION_NOTE_2026-09-02.md` §4.3 found the opposite —
enhancement — for γ_cr ≲ 0.85. Both used the table above. So the difference is
in the *evaluation regime*, and it can be exhibited in closed form.

## 2. The small-f_NL expansion that settles it

Reduce O5+O6 to its exponent on the threshold surface C_lin = C_lin,−, using
C_G = C_lin/J. With

    x = ζ_G/σ_r,   ν = C_lin,−/σ_c,   ε = (6/5) f_NL σ_r,   g ≡ γ_cr,

    S(x) = x²/2 + ( ν/(1 + εx) − g x )² / (2(1 − g²)).

Minimising over x (envelope theorem; x₀ = gν at ε = 0, x₁ = ν²(1 − 2g²)) gives

    **S_min(ε) = ν²/2 − g ν³ ε + ½ ν⁴ (6g² − 1) ε² + O(ε³)**,   ln β ≃ −S_min.

Verified numerically in `row11_choudhury_sign.py` part (A) against direct
minimisation of S over ν ∈ {3,4,5} × g ∈ {0.10 … 0.968}: all three coefficients
reproduced (max relative error 4.9×10⁻², attained only at g = 1/√6 where the
quadratic coefficient passes through zero and the *absolute* error is ~2×10⁻²).

Two terms, two different behaviours:

* **O(ε):** `+ g ν³ ε` in ln β. For f_NL < 0 (ε < 0) and γ_cr > 0 this is
  **negative — suppression — always**, with strength ∝ γ_cr.
* **O(ε²):** `− ½ ν⁴ (6γ_cr² − 1) ε²` in ln β. This **changes sign at
  γ_cr = 1/√6 = 0.4082**; below it the term is positive, i.e. *enhancing*.

**This is the responsible term.** The lab's enhancement branch is the O(ε²)
saddle term with coefficient (6γ_cr² − 1) < 0. Nothing else in the chain
carries a sign ambiguity.

## 3. Which sign is right for negative f_NL — settled

`row11_choudhury_sign.py` part (B) runs the *full* Eq. (60) integral (no
expansion) at nine spectrum shapes spanning γ_cr ∈ [0.305, 0.968], with A solved
at each point so the **Gaussian** case gives f_PBH = 1 (fixed-Gaussian-amplitude
comparison, nothing tuned):

| γ_cr | 0.968 | 0.930 | 0.888 | 0.808 | 0.766 | 0.630 | 0.557 | 0.412 | 0.305 |
|---|---|---|---|---|---|---|---|---|---|
| β/β_G at f_NL = −0.02 | 5.9e−2 | 2.4e−2 | 2.4e−2 | 2.2e−2 | 1.4e−2 | 1.2e−2 | 1.7e−2 | 2.6e−2 | 5.5e−2 |
| β/β_G at f_NL = −0.05 | 2.2e−4 | 8.2e−6 | 8.5e−6 | 8.1e−6 | 2.3e−6 | 5.2e−6 | 3.3e−5 | 1.1e−3 | 4.9e−2 |
| β/β_G at f_NL = −35/16 | 5e−107 | 3e−32 | 4e−14 | 3.4e−1 | 3.5e+3 | 1.0e+9 | 1.9e+10 | 1.8e+12 | 1.9e+13 |

**At small |f_NL| the ratio is < 1 at *every* γ_cr, including γ_cr = 0.305.**
That is the O(ε) term, and it is the perturbative — i.e. the controlled —
statement. Enhancement appears only once |ε| is large enough for the O(ε²) term
to overtake the linear one, which requires *both* large |f_NL| *and*
γ_cr < 1/√6-ish. It is a **non-perturbative branch**, and the lab has already
flagged (open item A3-1c) that 1.2|f_NL|σ_r ≈ 0.5–2 there, so the quadratic
truncation of O1 is itself outside its domain of validity on exactly that branch.

## 4. The decisive check: the enhancement is IR-divergent, the suppression is not

Part (C) recomputes the three covariance integrals for the lab's own
near-scale-invariant shape while scanning the IR cutoff k_min/k_p:

| k_min/k_p | 1e−5 | 1e−4 | 1e−3 | 1e−2 | 3e−2 | 1e−1 | 3e−1 |
|---|---|---|---|---|---|---|---|
| γ_cr (n_s = 0.9649) | 0.2668 | 0.3043 | 0.3581 | 0.4458 | 0.5135 | 0.6298 | 0.8030 |
| σ_r | 1.196 | 1.049 | 0.891 | 0.716 | 0.621 | 0.503 | 0.371 |
| σ_c | 0.0928 | 0.0928 | 0.0928 | 0.0928 | 0.0928 | 0.0928 | 0.0926 |
| **σ_cr²/σ_c** | **0.31921** | **0.31921** | **0.31921** | **0.31918** | **0.31896** | **0.31658** | 0.29770 |

σ_c and σ_cr² carry (k r_p)⁴ and (k r_p)² weights and are IR-safe; σ_r, with the
spherical window W_s → 1, is not. Therefore:

* the **suppressing** coefficient is `g ν³ ε ∝ (γ_cr σ_r) = σ_cr²/σ_c` —
  **IR-finite**, stable to 5 significant figures over four decades of cutoff;
* the **enhancing** coefficient is `½ ν⁴(6γ_cr² − 1) ε² ∝ σ_r²` with
  (6γ_cr² − 1) → −1 as γ_cr → 0 — **IR-divergent** for n_s ≤ 1: it grows without
  bound as k_min → 0.

An answer that diverges with an arbitrary superhorizon cutoff is not a
prediction. The enhancement is bought entirely from ζ_G excursions on scales far
outside the PBH-forming configuration (the ζ_G < 0 quadrant, where J > 1 for
f_NL < 0), whose physical role is to *modulate* the local abundance — a
large-scale bias / PBH-isocurvature effect — not to raise the ensemble mean at a
fixed local amplitude. Choudhury *et al.*'s peaked USR spectrum has no IR wing,
so σ_r is set by the peak, γ_cr ≈ 0.9, and both terms suppress.

## 5. Verdict (item a)

> **Negative local f_NL SUPPRESSES the compaction-function PBH abundance at
> fixed Gaussian amplitude.** Choudhury *et al.* 2025 are right and the lab's
> "enhancement for γ_cr ≲ 0.85" is an artefact, not a disagreement of formalism.
> The responsible term is the **second-order saddle-point coefficient
> ½ν⁴(6γ_cr² − 1)ε², ε = (6/5)f_NL σ_r**, which turns positive below
> γ_cr = 1/√6 = 0.408; its size scales as σ_r², which is IR-divergent for a
> near-scale-invariant Δ²_ζ, whereas the first-order suppressing coefficient
> γ_cr σ_r = σ_cr²/σ_c is IR-finite. The lab's low γ_cr is itself produced by the
> IR cutoff (γ_cr = 0.267 at k_min/k_p = 10⁻⁵ rising to 0.803 at 3×10⁻¹), so the
> enhancement branch is cutoff-dependent throughout.

**Paper-ready sentences (evidential strength: derived + numerically verified here):**

> Expanding the compaction-threshold saddle point in ε = (6/5) f_NL σ_r gives
> ln β ≃ −ν²/2 + γ_cr ν³ ε − ½ν⁴(6γ_cr² − 1)ε², ν = C_lin,−/σ_c. The
> first-order response is suppressing for f_NL < 0 at every γ_cr, with an
> IR-finite coefficient γ_cr σ_r = σ_cr²/σ_c; the second-order response changes
> sign at γ_cr = 1/√6 and scales as σ_r², which for a near-scale-invariant
> spectrum is IR-divergent. The enhancement we previously reported at
> γ_cr ≲ 0.85 is therefore a cutoff-dependent, non-perturbative branch rather
> than a discrepancy with Choudhury *et al.* (2025), whose peaked spectrum sits
> at γ_cr ≈ 0.9 where both orders suppress. We adopt suppression.
