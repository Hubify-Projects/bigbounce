# LQC Perturbation Formalism Landscape

**Created:** 2026-03-19
**Status:** REFERENCE DOCUMENT
**Purpose:** Map the four LQC perturbation formalisms and their known differences.

---

## Dressed-Metric Approach (Agullo, Ashtekar, Nelson)

**What it quantizes:** Full background geometry is quantized; perturbations propagate on the quantum-corrected effective metric. The metric that perturbation modes "see" is dressed by quantum fluctuations of the background.

**Key modification:** Effective Mukhanov-Sasaki equation with quantum-corrected potential z''/z that differs from the classical expression near the bounce. The corrections arise from the quantum-geometry-corrected expressions for background quantities (a, H, epsilon).

**Known effects:**
- Modifies power spectrum at k ~ k_LQC (bounce scale). Suppresses tensor-to-scalar ratio (r ~ 10^{-4}).
- Can produce oscillatory features in P(k) at k near k_LQC.
- n_s receives negligible corrections at observable k (quantum corrections confined to k ~ k_LQC).

**Reliability:** Well-established for power spectrum. Third-order (bispectrum) NOT YET COMPUTED in this formalism.

**Key literature:**
- Agullo, Ashtekar, Nelson, PRL 109 (2012) 251301
- Agullo, Ashtekar, Nelson, CQG 30 (2013) 085014
- Wilson-Ewing, CQG 29 (2012) 215013; CQG 30 (2013) 035011

**Relevance to our lane:** This is the formalism our Wilson-Ewing model implicitly uses. The r ~ 10^{-4} prediction and the n_s robustness come from this formalism.

---

## Hybrid Approach (Fernandez-Mendez, Mena Marugan, Olmedo)

**What it quantizes:** Homogeneous background with LQC (polymer quantization), perturbations with standard Fock space quantum field theory. Born-Oppenheimer-like separation between the two sectors.

**Key modification:** Different effective Mukhanov-Sasaki potential from dressed-metric. The perturbation Hamiltonian is derived from the full Hamiltonian constraint after the homogeneous-inhomogeneous split. Differences arise in the regularization of inverse-volume terms (1/a^n corrections).

**Known effects:**
- Agrees with dressed-metric in UV (k >> k_LQC): quantum corrections vanish at short wavelengths.
- Agrees with dressed-metric in deep IR (k << k_LQC) for the power spectrum: superhorizon modes unaffected.
- Can differ at intermediate k (near the bounce scale k_LQC).
- Different vacuum prescription at the bounce.

**Reliability:** Also well-established for power spectrum. Bispectrum: NOT COMPUTED.

**Key literature:**
- Fernandez-Mendez, Mena Marugan, Olmedo, PRD 86 (2012) 024003; PRD 89 (2014) 044041
- Castello Gomar, Mena Marugan, Martin de Blas, PRD 93 (2016) 104025

**Relevance:** Alternative formalism. If predictions differ from dressed-metric at observable scales, formalism choice becomes empirically relevant.

---

## Deformed Algebra (Bojowald, Paily)

**What it modifies:** The constraint algebra itself. The Dirac algebra of constraints receives quantum corrections: {H[N], H[M]} = D[...] with modified structure functions. The modified algebra generates effective equations that differ from dressed-metric and hybrid.

**Known issues:**
- Compatibility with general covariance questioned (Bojowald, Paily, PRD 86 (2012) 104018).
- Some results appear incompatible with dressed-metric and hybrid in the UV.
- The modified algebra may not close consistently in some regimes.
- Technical controversies make it less reliable for phenomenology.

**Reliability:** CONTROVERSIAL. Some community members question its consistency.

**Relevance:** LOW. Too controversial to base predictions on. Mentioned for completeness only. Do not invest time unless forced by results from dressed-metric and hybrid.

---

## Separate Universe Approach

**What it does:** Treats superhorizon patches as independent FRW universes. Perturbations encoded as differences in local expansion history. delta-N formalism relates perturbations to differences in e-fold number.

**Validity:** Only for superhorizon modes (k << aH). Requires spatial gradients to be negligible.

**Known limitation for bouncing cosmologies:** The standard delta-N formalism assumes zeta is conserved on superhorizon scales. In matter contraction, zeta GROWS on superhorizon scales (the growing mode). The growing mode invalidates standard delta-N and requires the extended Salopek-Bond gradient expansion.

**Relevance:** Our CMB/LSS modes ARE deeply superhorizon during the bounce (k/k_bounce ~ 10^{-56}). At this level, separate universe approximately equals any formalism. Not a distinct approach for our scales -- it is the common limit that all formalisms approach for k << k_LQC.

---

## The 2024 Comparison Paper (arXiv:2405.12296)

**Paper:** Agullo, Ashtekar, Gupt (2024), comparison of dressed-metric and hybrid perturbation formalisms in LQC.

### What it shows:
- Both formalisms give the SAME background evolution (same effective Friedmann equation, same bounce).
- Both AGREE in the UV (k >> k_LQC).
- Both AGREE in the deep IR (k << k_LQC) for the power spectrum.
- Both give the same qualitative picture: tensor suppression, scalar near-invariance.

### Where they differ:
- Initial-state prescriptions: different vacuum definitions at the bounce.
- Infrared behavior of quantum corrections: intermediate-k regime (k ~ k_LQC) receives different corrections.
- Regularization near the bounce: dressed-metric uses quantum-geometry-corrected background; hybrid uses standard expressions on the effective trajectory.

### Critical gap:
**The paper compares POWER SPECTRUM only. No bispectrum comparison exists in the literature.**

### Key implication for our modes:
Observable modes (k ~ 0.002 - 0.2 Mpc^{-1}) are superhorizon during the bounce by k/k_bounce ~ 10^{-56}. The differences between formalisms are confined to k ~ k_LQC, which is ~56 orders of magnitude above observable k. This is the foundation of the structural insensitivity argument.
