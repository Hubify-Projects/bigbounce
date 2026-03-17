# Current Paper Bridge Integration Decision

**Date:** 2026-03-13
**Program:** Early Structure from Bounce Cosmology
**Decision:** What, if anything, enters the current paper

---

## Decision: OPTION 3 — SAVE ENTIRELY FOR SEPARATE PAPER

With one exception: a single brief paragraph in the Future Directions section.

---

## Rationale

1. The scale mismatch (10⁹ in k) between framework-predicted features and SMBH-relevant scales makes any SMBH/PBH claim unsupportable.

2. Including the window analysis would draw attention to a limitation (N_tot = 92 pushes features to irrelevant scales) without any compensating scientific gain.

3. The phenomenological window is narrow (~0.4 dex) and disconnected from the framework — including it would be presenting someone else's science with our motivational label attached.

4. The figures, while technically correct, would invite reviewers to ask "does your framework predict this?" — the answer is no.

---

## Acceptable Future-Directions Paragraph

### Conservative version (RECOMMENDED, 2 sentences):

> The bounce-to-inflation transition (Sec.~XIV) sets initial conditions for inflation that may differ from the standard Bunch-Davies vacuum, potentially imprinting features on the primordial scalar power spectrum at scales set by the number of pre-observable e-folds. Whether the spin-torsion variant produces such features, and at what amplitude, requires a full perturbation calculation through the bounce that has not yet been performed.

### Slightly fuller version (3 sentences, acceptable):

> The bounce-to-inflation transition (Sec.~XIV) sets initial conditions for inflation that may differ from the standard Bunch-Davies vacuum, potentially imprinting features on the primordial scalar power spectrum. With $N_\text{tot} = 92$, such features would appear at comoving scales $k \sim 10^{15}$~Mpc$^{-1}$, corresponding to sub-asteroid-mass PBH scales where observational constraints are weak. A full perturbation calculation through the spin-torsion bounce is needed to determine whether the framework produces such features and whether they have implications for PBH dark matter.

### Why the fuller version is better:
It honestly states the N_tot = 92 scale prediction, names the relevant mass range (asteroid-mass PBH), and identifies the correct observational target (PBH dark matter, not SMBH seeds). This is maximally honest.

---

## What NOT to Write

Do NOT include any of the following:

- "...with implications for early SMBH seed formation" — The framework does not predict features at SMBH-relevant scales.
- "...which could ease tensions with JWST observations" — This is not a framework prediction.
- Any reference to the phenomenological window analysis or the window figures.
- Any forward-model constraint plots.
- Any mention of "allowed windows" for P(k) features.

---

## Figure Inclusion

**Do NOT include any figures from this analysis in the current paper.**

The window analysis figure is technically correct but:
- Shows a phenomenological parameter space scan, not a framework result
- The dominant visual feature (purple scale mismatch arrow) highlights a limitation
- Would require extensive caveating in the caption
- Would invite reviewer criticism without strengthening the paper

**Archive the figures** in `research/extensions/early_structure_program/window_analysis/` for potential use in a future paper where the perturbation calculation exists.

---

## Caption (for archival reference only, NOT for current paper)

If the figure were ever included in a future paper:

> **Primordial power spectrum feature window analysis.** The (k_*, P_R) parameter space for a Gaussian P(k) feature is shown with three constraint layers: PBH overproduction limit (red, above), SMBH seed threshold (green, below), and FIRAS μ-distortion bound (blue dashed, k < 10⁴ Mpc⁻¹). A narrow phenomenological window (~0.4 decades in P_R) exists at SMBH-relevant scales (k ~ 10⁴–10⁶ Mpc⁻¹), but the spin-torsion bounce framework with N_tot = 92 predicts features at k ~ 10¹⁵ Mpc⁻¹ (purple dashed), in the asteroid-mass PBH window where constraints are weakest. The scale mismatch of ~10⁹ in wavenumber precludes a direct connection between the bounce framework and early SMBH seed formation.
