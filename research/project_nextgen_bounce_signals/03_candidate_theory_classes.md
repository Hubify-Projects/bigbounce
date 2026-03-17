# 03: Candidate Next-Generation Theory Classes

**Created:** 2026-03-17
**Status:** COMPLETE

---

## A. Bounce + Entropy/Curvaton Conversion Sector

**Core mechanism:** A spectator field acquires perturbations during contraction. At or after the bounce, its isocurvature perturbations convert to curvature perturbations, imprinting a new spectrum with tilt.

**How it transmits information:** The conversion transfers spectator-field statistics (spectrum, non-Gaussianity) into the curvature sector. The conversion efficiency can be k-dependent if it happens near the bounce scale.

**Likely observable:** Red-tilted scalar spectrum (n_s ≈ 0.965), possibly distinctive f_NL shape.

**Distance from old ECH core:** Medium — requires a new field but uses the same bounce background.

**Biggest theoretical risk:** The conversion mechanism is generic curvaton physics. Already done by Cai & Brandenberger (2011) and Alexander et al. (2014). Our version would differ only in the curvaton identity, which the novelty audit showed is insufficient.

**Biggest novelty risk:** HIGH — this is standard curvaton cosmology transplanted into a bounce context. Likely already saturated.

---

## B. Bounce + Sourced Parity/Chiral GW Sector

**Core mechanism:** The bounce involves a parity-violating interaction (e.g., gravitational Chern-Simons coupling, Nieh-Yan term, or axion-gauge coupling) that sources chiral gravitational waves. The bounce is the unique moment when curvature is Planckian and parity violation is maximal, producing a net circular polarization in the tensor spectrum.

**How it transmits information:** The parity-violating coupling converts the bounce-scale curvature into a chirally asymmetric GW spectrum. This is a fundamentally nonlinear process: the GW polarization asymmetry depends on the bounce dynamics, not just the contraction phase.

**Likely observable:** Circular polarization (V-mode Stokes parameter) of the stochastic GW background. Frequency-dependent chirality that peaks near the bounce scale. Potentially detectable by LISA or next-gen detectors via cross-correlation techniques.

**Distance from old ECH core:** CLOSE — the Holst term is a parity-odd gravitational term, and the Barbero-Immirzi pseudoscalar naturally couples as a Chern-Simons-like interaction. The torsion at the bounce is the parity-violation source.

**Biggest theoretical risk:** The chiral signal may be confined to the bounce scale (k ~ k_b ~ GHz), far above any detector band.

**Biggest novelty risk:** LOW — Zhu & Cai (2023, arXiv:2301.13502) showed parity enhancement is possible at the bounce but did NOT compute a quantitative circular polarization spectrum. Jiang et al. (2024, arXiv:2406.16549) used Nieh-Yan in an inflationary context. Nobody has computed the chiral GW spectrum from a torsion bounce. This is a genuine gap.

---

## C. Bounce + Time-Asymmetric / Dissipative Phase

**Core mechanism:** The bounce is not time-symmetric. Particle production, dissipation, or entropy generation during the bounce phase creates a preferred direction of time. The asymmetry imprints on perturbations: modes that enter the bounce are processed differently from modes that exit.

**How it transmits information:** Dissipation during the bounce damps some modes and amplifies others. The transfer function T(k) acquires a non-trivial k-dependent imaginary part (phase shift) or amplitude modification. This breaks the "T = 1 for super-Hubble modes" conclusion of the symmetric bounce.

**Likely observable:** Spectral features (oscillations, damping, phase shifts) in the scalar or tensor power spectrum. Potentially a running of the spectral index that encodes the bounce timescale.

**Distance from old ECH core:** Medium — requires adding dissipation (thermal bath, particle production) to the bounce, which goes beyond the perfect-fluid ECH framework.

**Biggest theoretical risk:** The dissipation scale may be at the bounce energy (Planckian), making all effects unobservable at CMB scales.

**Biggest novelty risk:** MODERATE — "warm bounce" (analogous to warm inflation) is essentially unstudied. Nobody has computed perturbation spectra from a dissipative bounce. But the concept of particle production at the bounce exists (Quintin et al. 2014, Cai et al. 2011). The novelty is in the systematic perturbation-level treatment.

---

## D. Bounce + Localized Feature Generation / PBH Window

**Core mechanism:** The bounce or near-bounce dynamics (e.g., a phase transition, resonance, or equation-of-state change) produces a localized enhancement in the scalar power spectrum at a specific scale. This enhanced power generates PBHs when the enhanced modes re-enter the horizon during expansion.

**How it transmits information:** The bounce-scale physics (curvature peak, EOS transition, resonance) creates a bump in P_ζ(k) at k ~ k_feature. PBHs form from the overdense regions.

**Likely observable:** PBH abundance in a specific mass window. Induced SGWB from the enhanced scalar modes. Potentially correlated with PTA signal.

**Distance from old ECH core:** Medium — requires identifying a specific feature-generation mechanism (EOS transition, parametric resonance, etc.) near the bounce.

**Biggest theoretical risk:** Papanikolaou et al. (2024) already computed PBH + SIGW from the matter bounce. Ye et al. (2026) found vanishingly small PBH fractions in a dust-radiation bounce (negative result).

**Biggest novelty risk:** MODERATE-HIGH — the PBH+bounce space is actively occupied. Novelty only if the feature mechanism is specific and distinct from the generic small-scale growth.

---

## E. Bounce + Induced GW from Sourced Scalar Features

**Core mechanism:** Same as D, but focused on the scalar-induced GW (SIGW) spectrum rather than PBH formation. The key insight: the standard SIGW formula (second-order perturbation theory) assumes a standard expanding FRW background. During a bounce, the NEC is violated, and the Green's function for the second-order tensor equation is modified. This changes the SIGW kernel.

**How it transmits information:** The bounce modifies the tensor Green's function at second order. Even if the first-order scalar spectrum passes through unchanged (transparent bounce), the second-order tensor production is different because the background is non-standard during the bounce.

**Likely observable:** Modified SIGW spectrum compared to the standard (inflationary) calculation. Potentially distinct spectral shape at frequencies corresponding to modes that were inside the horizon during the bounce.

**Distance from old ECH core:** Close — uses the same bounce background. The new ingredient is the second-order calculation in a non-standard background.

**Biggest theoretical risk:** The modification may be tiny for observable frequencies (all current SIGW bounce papers use the standard formula without modification, suggesting the effect is small for super-Hubble modes).

**Biggest novelty risk:** MODERATE — Papanikolaou (2025) and Li (2025) computed SIGW from bounces but used the standard kernel. Nobody has computed the modified SIGW kernel during the bounce phase. The gap is real but may produce a null result (modification negligible for observable modes).

---

## F. Bounce + Hidden-Sector Reheating or Phase Transition

**Core mechanism:** A cosmological phase transition (electroweak-like, QCD-like, or dark-sector) occurs during or immediately after the bounce, when the universe is at its hottest/densest. The phase transition dynamics (bubble nucleation, domain wall formation, first-order transitions) differ from the standard expanding-background case because the background is contracting-then-expanding.

**How it transmits information:** Bubble nucleation rates, bubble wall velocities, and collision dynamics depend on the Hubble rate and its time derivative. During a bounce, H passes through zero and Ḣ > 0, which is qualitatively different from H > 0, Ḣ < 0 in standard expansion. This modifies the GW spectrum from the phase transition.

**Likely observable:** Modified GW spectrum from the phase transition. Potentially different peak frequency, spectral shape, or amplitude compared to the standard expanding-background result.

**Distance from old ECH core:** Far — requires specifying a phase transition model (new sector) plus embedding it in the bounce background.

**Biggest theoretical risk:** The phase transition may not occur at the bounce energy scale. If it occurs much later (electroweak scale), the bounce is long past and the background is standard FRW.

**Biggest novelty risk:** LOW — nobody has studied phase transitions in a bouncing background. The question "how does bubble nucleation change when H = 0?" is completely open. But the theoretical overhead is high (need to specify the phase transition + the bounce + the coupling).

---

## G. Bounce + Nonlocal / Memory Effect

**Core mechanism:** The violent dynamics at the bounce (Planckian curvature, rapid H reversal) produce a nonlinear gravitational wave memory effect: a permanent displacement of the tensor field that persists into the expanding phase. This is the cosmological analog of the Christodoulou memory from binary mergers.

**How it transmits information:** The bounce is a transient event with large curvature. The nonlinear (Isaacson-type) backreaction of short-wavelength perturbations during the bounce sources a long-wavelength tensor mode that persists as a memory. This is a DC (zero-frequency) or very-low-frequency contribution to the tensor spectrum.

**Likely observable:** A specific very-low-frequency contribution to the SGWB. Potentially a characteristic spectral shape (flat or rising at low frequencies) that differs from the inflationary consistency relation.

**Distance from old ECH core:** Close — uses the same bounce. The new ingredient is the nonlinear second-order calculation.

**Biggest theoretical risk:** The memory signal is suppressed by (H_bounce × t_bounce)² at long wavelengths. If the bounce is too fast (t_bounce ~ t_Pl), the memory is confined to Planck frequencies and unobservable.

**Biggest novelty risk:** LOW — nobody has computed cosmological GW memory from a bounce. Bieri et al. (2024) computed primordial GW memory generically; Unal & Veske (2025) computed stochastic memory. Neither treats the bounce as a memory-generating event. The gap is genuine.

---

## H. Bounce + Prolonged / Non-Transparent Near-Bounce Phase

**Core mechanism:** The bounce is not instantaneous. If the near-bounce phase lasts for a duration Δt_bounce such that modes with k_CMB < k < k_b evolve non-trivially (undergo oscillation, amplification, or damping) during the bounce, the transfer function T(k) becomes non-trivial for these modes. A prolonged bounce with a specific EOS or potential structure creates a frequency-dependent transfer.

**How it transmits information:** Modes that spend time inside the Hubble radius during the bounce undergo WKB evolution, potentially including resonances. The transfer function becomes T(k) ≠ 1 for k in the "bounce band" — a range of wavenumbers that are sub-Hubble during the bounce.

**Likely observable:** Spectral features (oscillations, steps, resonances) in the power spectrum at frequencies corresponding to the bounce band. Zhu & Cai (2026, arXiv:2603.13924) showed that a double-peak potential during the bounce creates resonant tunneling patterns — "echoes" in the GW spectrum. A prolonged bounce could extend such features to lower frequencies.

**Distance from old ECH core:** Medium — the ECH bounce is fast (Δt ~ t_Pl). Making it prolonged requires either a different bounce mechanism or a multi-stage bounce.

**Biggest theoretical risk:** Making the bounce prolonged while maintaining regularity is non-trivial. A very slow bounce may develop instabilities (gradient or ghost).

**Biggest novelty risk:** MODERATE — Zhu & Cai (2026) just published on resonant GW echoes from a bounce (March 2026). But their treatment is for a symmetric bounce with a specific potential. A systematic exploration of non-transparent bounce bands with different EOS profiles is still open. Steinhardt's group distinguishes "fast vs slow" bounces conceptually but does not compute observables for the intermediate regime.
