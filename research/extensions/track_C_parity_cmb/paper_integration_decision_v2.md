# Phase 7: Paper Integration Decision

**Date:** 2026-03-13

---

## Decision: **Include in Paper 1 as an upgraded subsection**

The Track C v2 results strengthen the paper's phenomenological reach without overclaiming. The analysis is honest, lightweight, and adds real statistical content (Bayes factor, explicit priors, proper confidence intervals) beyond the previous algebraic consistency check.

---

## Recommended Placement

**Section 8 (Observational Signatures)**, subsection on parity-violating signatures / cosmic birefringence. Replace or upgrade the existing consistency-check text.

---

## Option A: Conservative Paragraph (Minimum Viable)

> Cosmic birefringence provides a direct observable consequence of the parity-odd operator in Eq.~(XX). The effective photon-torsion coupling $g_{\rm eff} = (\alpha/M)\,M_{\rm Pl}\,f_{\rm photon}$ rotates the CMB polarization plane by an angle $\beta = g_{\rm eff}\,C_0$, where $C_0$ encodes the integrated pseudo-scalar field excursion from recombination to today and $f_{\rm photon}$ parameterizes the (currently underived) photon-torsion vertex. Combining the two independent isotropic birefringence measurements --- $\beta = 0.30^\circ \pm 0.11^\circ$ from Planck NPIPE~\cite{Eskilt2022} and $\beta = 0.215^\circ \pm 0.074^\circ$ from ACT DR6~\cite{DiegoPalazuelos2025} --- in a Gaussian summary likelihood with a uniform prior on $\beta \in [-1^\circ, 1^\circ]$, we obtain $\beta = 0.242^\circ \pm 0.061^\circ$ ($3.9\sigma$ from zero) with a Bayes factor $\mathrm{BF}(\beta \neq 0) \approx 176$ (strong evidence on the Jeffreys scale). For $C_0 \in [0.3, 3]$, the implied coupling is $f_{\rm photon} \in [0.6, 5.8]$, confirming that the operator scale $\alpha/M \sim 10^{-21}\,\mathrm{GeV}^{-1}$ is naturally compatible with the observed signal without fine-tuning. We emphasize that this is a summary-likelihood inference using published $\beta$ values, not a map-level CMB analysis, and that $(f_{\rm photon}, C_0)$ remain individually undetermined.

---

## Option B: Fuller Paragraph (Adds Degeneracy and Shape Discussion)

> Cosmic birefringence provides a direct observable consequence of the parity-odd operator in Eq.~(XX). The effective photon-torsion coupling $g_{\rm eff} = (\alpha/M)\,M_{\rm Pl}\,f_{\rm photon}$ rotates the CMB polarization plane by an angle $\beta = g_{\rm eff}\,C_0$, where $C_0$ encodes the integrated pseudo-scalar field excursion and $f_{\rm photon}$ parameterizes the photon-torsion vertex. Combining $\beta = 0.30^\circ \pm 0.11^\circ$ (Planck NPIPE;~\cite{Eskilt2022}) and $\beta = 0.215^\circ \pm 0.074^\circ$ (ACT DR6;~\cite{DiegoPalazuelos2025}) in a Gaussian summary likelihood with uniform prior $\beta \in [-1^\circ, 1^\circ]$, we find $\beta = 0.242^\circ \pm 0.061^\circ$ ($3.9\sigma$; $\mathrm{BF} \approx 176$). The derived constraint on the product $f_{\rm photon} \times C_0 = 1.73 \pm 0.44$ demonstrates that the spin-torsion operator scale requires no fine-tuning: for any $C_0$ of order unity, $f_{\rm photon}$ is also of order unity. The $(f_{\rm photon}, C_0)$ degeneracy (Fig.~\ref{fig:trackC_degeneracy}) traces a hyperbola that cannot be broken without an independent determination of $C_0$ from the pseudo-scalar field evolution --- a calculation deferred to future work. We note that uniform birefringence of this magnitude is generic to any axion-like coupling~\cite{Carroll1998}; distinguishing the spin-torsion origin requires either a first-principles derivation of $f_{\rm photon}$ or detection of the specific scale-dependent EB signature predicted by the torsion condensate profile.

---

## Figure Caption

> **Figure XX.** Gaussian summary-likelihood inference on cosmic birefringence from the spin-torsion parity-odd operator. *Left:* Posterior on the birefringence angle $\beta$, combining Planck NPIPE~\cite{Eskilt2022} and ACT DR6~\cite{DiegoPalazuelos2025} measurements ($\beta = 0.242^\circ \pm 0.061^\circ$, $3.9\sigma$). *Right:* Derived constraint on the photon-torsion coupling $f_{\rm photon}$ as a function of the cosmological integral $C_0$. The shaded band shows the 68\% credible region; $f_{\rm photon} \sim \mathcal{O}(1)$ for $C_0 \sim \mathcal{O}(1)$, indicating natural compatibility with the operator scale $\alpha/M \sim 10^{-21}\,\mathrm{GeV}^{-1}$. This is a summary-likelihood inference using published $\beta$ values, not a map-level CMB analysis.

---

## Recommendation

Use **Option B** (fuller paragraph) if the paper has room. It honestly addresses the degeneracy and explicitly states what would be needed to distinguish this framework from generic axion-like models. Use **Option A** if space is tight.

Include the corner plot (`trackC_parity_upgrade_corner.pdf`) as the primary figure, with the degeneracy plot as an optional second panel or supplementary figure.

---

## Citations to Add

| Citation | arXiv | Already in Paper 1? |
|----------|-------|---------------------|
| Eskilt 2022 | 2205.13962 | YES |
| Diego-Palazuelos & Komatsu 2025 | 2503.14452 | CHECK — may need to add |
| Carroll 1998 (axion birefringence) | hep-ph/9904272 | YES |
| SPIDER 2025 (cite only) | 2510.25489 | CHECK — may need to add |
