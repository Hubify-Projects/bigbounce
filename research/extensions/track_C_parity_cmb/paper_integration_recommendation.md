# Track C Paper Integration Recommendation

**Date:** 2026-03-13
**Auditor:** Claude (automated audit)
**Program:** Extension Program — Track C (Parity/CMB Birefringence)

---

## Recommendation

**Include Track C as a 2-3 paragraph addition to the Discussion section**, with 1 figure (consistency window plot). Frame as a phenomenological consistency check, not as a constraint or inference result.

---

## What to Include

1. **The consistency check result:** The framework's parity-odd coupling α/M ≈ 10⁻²¹ GeV⁻¹ requires f_photon ≈ 1.7 to match observed cosmic birefringence — an O(1) vertex factor requiring no fine-tuning.

2. **The combined birefringence measurement:** β = 0.24° ± 0.06° from Planck (Eskilt 2022) and ACT DR6 (Diego-Palazuelos & Komatsu 2025), cited as published results.

3. **The consistency window figure:** f_photon vs β plot showing the observational bands and the O(1) region.

## What NOT to Include

- Do not call this a "constraint on f_photon" — no likelihood was evaluated
- Do not say "we find 3.9σ evidence" — Eskilt and Diego-Palazuelos found the evidence; we combine their published numbers
- Do not include the EB shape plot as a "fit" — no fitting was performed
- Do not use language like "posterior," "credible interval," or "Bayesian" — none of these apply

---

## Draft Paragraphs

### Conservative version (RECOMMENDED):

> The parity-odd operator in Eq.~(XX) predicts cosmic birefringence — a uniform rotation of CMB linear polarization. Recent analyses of Planck PR4 data report $\beta = 0.30^\circ \pm 0.11^\circ$ \cite{Eskilt2022}, while an independent analysis of ACT DR6 data finds $\beta = 0.215^\circ \pm 0.074^\circ$ \cite{DiegoPalazuelos2025}. Combining these independent measurements yields $\beta = 0.24^\circ \pm 0.06^\circ$.
>
> In this framework, the birefringence angle is $\beta = f_\text{photon} \times [\alpha/M] \times M_\text{Pl} \times C_0$, where $f_\text{photon}$ parameterizes the photon-torsion vertex strength. Matching the combined observational value requires $f_\text{photon} \approx 1.7$, an $\mathcal{O}(1)$ factor consistent with a perturbative one-loop origin. This consistency check does not constitute independent evidence for the framework — the birefringence data do not uniquely select spin-torsion cosmology — but it establishes that the framework's coupling scale is compatible with the observed signal without fine-tuning.

### Slightly stronger version (acceptable but less conservative):

> The parity-odd operator in Eq.~(XX) predicts cosmic birefringence with an amplitude set by the same coupling $\alpha/M \approx 10^{-21}~\text{GeV}^{-1}$ that enters the dark energy mechanism. Recent CMB polarization analyses from Planck \cite{Eskilt2022} and ACT DR6 \cite{DiegoPalazuelos2025} independently detect nonzero birefringence at a combined significance of $3.9\sigma$: $\beta = 0.24^\circ \pm 0.06^\circ$. Matching this value within the framework requires a photon-torsion vertex factor $f_\text{photon} = 1.7 \pm 0.4$. The $\mathcal{O}(1)$ magnitude of $f_\text{photon}$ is a non-trivial consistency check: if the coupling scale were orders of magnitude wrong, $f_\text{photon}$ would need to compensate, signaling fine-tuning. Instead, the framework's parity-odd scale naturally accommodates the observed birefringence.

---

## Language Guide

| Safe language | Unsafe language |
|---------------|-----------------|
| "consistency check" | "constraint" |
| "compatible with" | "predicts" |
| "requires f_photon ≈ 1.7" | "we measure f_photon = 1.7" |
| "combining published measurements" | "our analysis finds" |
| "O(1) vertex factor" | "natural prediction" |
| "does not uniquely select" | "supports the framework" |

---

## Figures

### Include:
- **Consistency window plot** (`consistency_window.pdf`): Shows f_photon vs β with observational bands. Clear, informative, and accurately represents the analysis.

### Do not include:
- `eb_shape_comparison.pdf` — Shows a forward model without data comparison. Would suggest a fit was performed.
- `eb_ratio_diagnostic.pdf` — Diagnostic plot with no data overlay. Not informative for the reader.
- `beta_posterior.pdf` — Labeled "posterior" but is just Gaussian curves from published means/sigmas. Misleading label.
- `geff_posterior.pdf` — Same issue. If included, must be relabeled as "parameter translation" not "posterior."

### If a second figure is desired:
Relabel `beta_posterior.pdf` as "Published birefringence measurements and their inverse-variance weighted combination" (not "posterior"). This accurately describes the content.

---

## Integration Timing

Include with the planck_only results update (~March 19-20), as part of a version bump (v1.6.0). This allows:
1. All MCMC results to be finalized first
2. Track C results to be added in context
3. A single comprehensive revision rather than piecemeal updates
