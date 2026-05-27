# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P4_v1_0_138
**Wall time**: 174.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=106917, completion=15827, reasoning=15018, total=122744

---

No BLOCKER-grade findings were identified. The manuscript is theoretically rigorous in its symmetry classifications and scope boundaries, but contains two MAJOR theoretical physics errors regarding the physical interpretation of chiral tensor backgrounds and EFT dimension counting, plus one MAJOR statistical error regarding binary variance.

## PAPER-GEM-M1
**Severity:** MAJOR
**Section:** VI.H, paragraph "(i) Chiral gravitational-wave power asymmetry $\Pi$"
**Concrete Issue:** The text claims an isotropic stochastic background of chiral tensors produces an "observable chirality dipole". This is theoretically impossible: an isotropic tensor background preserves isotropy and cannot source a dipole (which requires a preferred direction). The cited Yu et al. (2020) [28] paper shows it sources parity-odd 2-point correlations, not a dipole.
**Fix:** Correct the text to state that an isotropic chiral tensor background produces parity-odd spin-spin correlations, and explicitly note that the dipole observable does not constrain this isotropic channel because a dipole requires an isotropy-breaking background.

## PAPER-GEM-M2
**Severity:** MAJOR
**Section:** VI.H, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Concrete Issue:** The text attributes "dimension-7 operators in the EFT of Inflation" to Cabass, Ivanov & Philcox (2023) [18]. This is a factual error in EFT counting; the cited paper explicitly derives that the leading parity-odd operators for the scalar trispectrum in the EFT of Inflation appear at mass dimension 8.
**Fix:** Change "dimension-7 operators" to "dimension-8 operators" to match the EFT counting derived in the cited reference.

## PAPER-GEM-M3
**Severity:** MAJOR
**Section:** III.E, paragraph "Hard-label variance widening from the 21.4% argmax-flip rate"
**Concrete Issue:** The derivation of the variance widening factor $\sqrt{1 + p_{flip}(1-p_{flip})/[p(1-p)]}$ violates the law of total variance. For a binary variable $x_{obs} \in \{0,1\}$, the marginal variance $Var(x_{obs}) = p_{obs}(1-p_{obs})$ can never exceed 0.25; the flip noise shrinks the variance of the conditional expectation by exactly the amount it adds in conditional variance, leaving the total binomial variance unchanged at $\approx 0.25/N$.
**Fix:** Remove the $1.21\times$ to $1.29\times$ variance inflation factors for hard labels; the standard error of a binary fraction $p_{obs}$ is strictly $\sqrt{p_{obs}(1-p_{obs})/N}$, which already fully captures the flip noise.

## PAPER-GEM-m4
**Severity:** minor
**Section:** Abstract
**Concrete Issue:** The abstract claims that "the parity-odd analog requires 3D spin-vector or polarization-rotation cross-correlation observables", which contradicts Section VI.H where the author correctly identifies that the 2D chirality monopole ($\ell=0$) is itself a parity-odd observable.
**Fix:** Update the abstract to acknowledge that the 2D chirality monopole is a parity-odd observable, rather than claiming parity-odd tests strictly require 3D or cross-correlation observables.

## PAPER-GEM-n5
**Severity:** nit
**Section:** VI.H, paragraph "Symmetry classification..."
**Concrete Issue:** The text states that an axial vector dipole "would require a background vector or tensor source". A pure background tensor $T_{ij}$ sources a quadrupole and cannot source a dipole (vector) unless contracted with another background vector.
**Fix:** Change "background vector or tensor source" to "background vector source" for strict rotational-symmetry consistency.
