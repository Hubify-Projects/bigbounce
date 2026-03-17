# 01: Literature Search — Matter Bounce, Torsion Bounce, and Perturbation Spectra

**Created:** 2026-03-17
**Purpose:** Identify all prior work close to Branch V (dust contraction → ECH bounce → radiation expansion, scalar spectrum + f_NL)

---

## A. Foundational Matter Bounce Papers

### A1. Wands (1999)
- **Citation:** D. Wands, "Duality Invariance of Cosmological Perturbation Spectra," Phys. Rev. D 60, 023507 (1999). arXiv: gr-qc/9809062
- **Background:** Generic collapsing FRW universe
- **Perturbation variables:** Curvature perturbation (linear)
- **Key result:** Showed that a collapsing universe can produce a scale-invariant spectrum via duality
- **f_NL:** Not computed
- **Torsion/ECH:** No
- **Closeness to Branch V:** Conceptual precursor only

### A2. Finelli & Brandenberger (2002)
- **Citation:** F. Finelli, R. Brandenberger, "On the Generation of a Scale-Invariant Spectrum of Adiabatic Fluctuations in Cosmological Models with a Contracting Phase," Phys. Rev. D 65, 103522 (2002). arXiv: hep-th/0112249
- **Background:** Single canonical scalar field, dust-like (w = 0) contraction, assumed nonsingular bounce (unspecified mechanism)
- **Perturbation variables:** Curvature perturbation ζ, Bardeen potential Φ (linear order)
- **Key result:** Scale-invariant spectrum (n_s = 1) for both scalar and tensor modes from vacuum fluctuations during matter-dominated contraction
- **f_NL:** Not computed (linear order only)
- **Torsion/ECH:** No — bounce mechanism left unspecified
- **Closeness to Branch V:** HIGH for the contraction-phase result. They establish n_s = 1 from dust contraction without specifying the bounce. Our Phase 1a reproduces exactly this result.

### A3. Cai, Xue, Brandenberger & Zhang (2009)
- **Citation:** Y.-F. Cai, W. Xue, R. Brandenberger, X. Zhang, "Non-Gaussianity in a Matter Bounce," JCAP 05, 011 (2009). arXiv: 0903.0631
- **Background:** Single scalar field with matter-dominated contraction, nonsingular bounce via ghost condensate / Lee-Wick type NEC violation
- **Perturbation variables:** Curvature perturbation ζ to second order (bispectrum)
- **Key result:** f_NL^local = −35/8 ≈ −4.375 for canonical scalar field (c_s = 1)
- **f_NL = 5/12?** NO. The matter bounce result is f_NL = −35/8, NOT 5/12.
- **Torsion/ECH:** No
- **Closeness to Branch V:** HIGH for non-Gaussianity. This is the standard matter-bounce f_NL paper. **Our Phase 1a f_NL = 5/12 estimate appears to be WRONG — the literature value is −35/8.**

### A4. Quintin, Sherkatghanad, Cai & Brandenberger (2015)
- **Citation:** J. Quintin, Z. Sherkatghanad, Y.-F. Cai, R. Brandenberger, "Evolution of cosmological perturbations and the production of non-Gaussianities through a nonsingular bounce," Phys. Rev. D 92, 063532 (2015). arXiv: 1508.04141
- **Background:** Generic single scalar field, matter contraction + nonsingular bounce
- **Perturbation variables:** ζ to second order through the bounce
- **Key result:** NO-GO THEOREM — in single-field matter bounce, suppressing r to observational levels requires curvature perturbation growth at the bounce, which simultaneously enhances f_NL to unacceptable levels. Tension between small r and small f_NL.
- **f_NL:** Order unity before bounce, enhanced during bounce if r is suppressed
- **Torsion/ECH:** No (general scalar field bounce)
- **Closeness to Branch V:** VERY HIGH. This no-go theorem may apply to our scenario. Critical question: does the ECH bounce evade this no-go?

### A5. Li, Brandenberger & Cai (2016)
- **Citation:** Y. Li, R. Brandenberger, Y.-F. Cai, "Matter bounce cosmology with a generalized single field: non-Gaussianity and an extended no-go theorem," arXiv: 1612.02036
- **Background:** Generalized k-essence with arbitrary c_s
- **Key result:** Extended no-go — small c_s suppresses r but produces large f_NL. Tension persists across all single-field realizations.
- **Closeness to Branch V:** HIGH. Extends the no-go to the general case.

---

## B. Review Papers

### B1. Brandenberger (2012)
- **Citation:** R. Brandenberger, "The Matter Bounce Alternative to Inflationary Cosmology," arXiv: 1206.4196
- **Content:** Focused review of matter bounce: perturbation generation, realizations, observational signatures. Establishes n_s = 1, discusses f_NL, BKL problem.

### B2. Brandenberger & Peter (2017)
- **Citation:** R. Brandenberger, P. Peter, "Bouncing Cosmologies: Progress and Problems," Found. Phys. 47, 797 (2017). arXiv: 1603.05834
- **Content:** Comprehensive review of all bouncing cosmology approaches. Covers perturbation matching, instabilities, observational constraints.

### B3. Novello & Bergliaffa (2008)
- **Citation:** M. Novello, S.E.P. Bergliaffa, "Bouncing Cosmologies," Phys. Rep. 463, 127 (2008). arXiv: 0802.1634
- **Content:** Early review of nonsingular bounce mechanisms and perturbation behavior.

---

## C. LQC Matter Bounce Papers (CRITICAL — same Friedmann equation as ECH)

### C1. Wilson-Ewing (2013)
- **Citation:** E. Wilson-Ewing, "The Matter Bounce Scenario in Loop Quantum Cosmology," JCAP 03, 026 (2013). arXiv: 1211.6269
- **Background:** Dust contraction → LQC bounce → expansion. Modified Friedmann: H² = (8πG/3)ρ(1 − ρ/ρ_c)
- **Perturbation variables:** Mukhanov-Sasaki for scalar and tensor modes, with LQC quantum-geometry corrections to the effective mass term
- **Key results:**
  - n_s ≈ 1 (scale-invariant, small red tilt from quantum corrections)
  - **r ≈ 9 × 10⁻⁴** — drastically suppressed from classical value (r ~ 16) by quantum geometry corrections to the perturbation equation
  - Amplitude requires ρ_c ~ 10⁻⁹ ρ_Pl
- **f_NL:** Not computed
- **Torsion/ECH:** No — LQC holonomy corrections
- **Closeness to Branch V:** EXTREMELY HIGH. Same background equation. Same scenario. The perturbation equations differ only if the LQC "dressed metric" corrections differ from ECH perturbation corrections.

### C2. Cai & Wilson-Ewing (2014)
- **Citation:** Y.-F. Cai, E. Wilson-Ewing, "A ΛCDM Bounce Scenario," JCAP 03, 006 (2015). arXiv: 1412.2914
- **Background:** CDM + radiation + Λ, LQC bounce
- **Key results:** Nearly scale-invariant spectrum with slight red tilt from Λ, positive running of n_s (distinguishing prediction vs inflation)
- **f_NL:** Not primary focus
- **Closeness to Branch V:** HIGH. More realistic matter content than pure dust.

### C3. Agullo, Ashtekar, Nelson (2012–2013)
- **Citation:** I. Agullo, A. Ashtekar, W. Nelson, "Perturbations in Loop Quantum Cosmology," arXiv: 1204.1288; "A Quantum Gravity Extension of the Inflationary Scenario," PRL 109, 251301 (2012), arXiv: 1209.1609; "Extension of the Quantum Theory of Cosmological Perturbations to the Planck Era," PRD 87, 043507 (2013), arXiv: 1211.1354
- **Background:** LQC bounce followed by inflation (not matter bounce)
- **Key results:** Rigorous dressed-metric perturbation theory through the LQC bounce. QFT on quantum-dressed background.
- **f_NL:** Not in these papers
- **Closeness to Branch V:** MODERATE. Different scenario (inflation after bounce) but establishes the perturbation framework.

### C4. Agullo & Ashtekar (2015)
- **Citation:** I. Agullo, A. Ashtekar, "Loop Quantum Cosmology, Non-Gaussianity, and CMB Power Asymmetry," arXiv: 1507.04703
- **Background:** LQC bounce + inflation
- **Key results:** f_NL is scale-dependent and oscillatory at long wavelengths. Enhanced by orders of magnitude for modes with wavelength comparable to bounce curvature radius. Correlations between observable and super-horizon modes induce dipole-dominated CMB modulation.
- **f_NL:** Highly scale-dependent (LQC-specific prediction)
- **Closeness to Branch V:** MODERATE. Different scenario but the f_NL methodology is relevant.

---

## D. Einstein-Cartan / Torsion Bounce Perturbation Papers

### D1. Popławski (2010)
- **Citation:** N.J. Popławski, "Cosmology with Torsion: An Alternative to Cosmic Inflation," Phys. Lett. B 694, 181 (2010). arXiv: 1007.0587
- **Background:** Einstein-Cartan with spin-fluid torsion
- **Perturbation variables:** None — background only
- **Spectrum/f_NL:** Not computed
- **Closeness to Branch V:** LOW. Background only.

### D2. Popławski (2012)
- **Citation:** N.J. Popławski, "Thermal Fluctuations in Einstein-Cartan-Sciama-Kibble-Dirac Bouncing Cosmology," arXiv: 1201.0316
- **Background:** Einstein-Cartan bounce
- **Perturbation variables:** Thermal (not vacuum) fluctuations at the bounce
- **Key result:** Scale-invariant spectrum ONLY if Dirac spin tensor form is used (not macroscopic spin-fluid average). Conditional result.
- **f_NL:** Not computed
- **Closeness to Branch V:** MODERATE. EC bounce perturbations, but thermal not vacuum, and no systematic perturbation theory.

### D3. Alexander, Bambi, Marcianò, Modesto (2014)
- **Citation:** S. Alexander, C. Bambi, A. Marcianò, L. Modesto, "Fermi-bounce Cosmology and Scale-Invariant Power Spectrum," Phys. Rev. D 90, 123510 (2014). arXiv: 1402.5880
- **Background:** GR + Holst term + Dirac fermions. Torsion is non-dynamical, integrated out → effective four-fermion interaction. Bounce from fermionic NEC violation.
- **Perturbation variables:** Mukhanov-Sasaki on the modified background
- **Key result:** Scale-invariant power spectrum for suitable fermion parameters
- **f_NL:** Not computed
- **Torsion role:** Background only — torsion integrated out at action level, does NOT appear in perturbation equations
- **Closeness to Branch V:** HIGHEST among torsion papers. Uses actual EC/Holst torsion. But torsion does not propagate into the perturbation equations — same limitation as our setup.

### D4. Alexander, Cai, Marcianò (2014)
- **Citation:** S. Alexander, Y.-F. Cai, A. Marcianò, "Fermi-bounce Cosmology and the Fermion Curvaton Mechanism," Phys. Lett. B 745, 97 (2015). arXiv: 1406.1456
- **Background:** Same Fermi-bounce, but with curvaton (second fermion species)
- **Key result:** Scale-invariant spectrum from curvaton mechanism. Potentially viable r.
- **f_NL:** Not computed explicitly (curvaton generically gives local-type)
- **Closeness to Branch V:** HIGH. Torsion bounce + curvaton is close to our ALP curvaton idea.

### D5. Addazi, Alexander, Cai, Marcianò (2016)
- **Citation:** A. Addazi, S. Alexander, Y.-F. Cai, A. Marcianò, "Dark Matter and Baryogenesis in the Fermi-bounce Curvaton Mechanism," arXiv: 1612.00632
- **Extension of D4 with dark matter and baryogenesis connections.

### D6. Addazi & Marcianò (2018)
- **Citation:** A. Addazi, A. Marcianò, "Quantum Ekpyrotic Mechanism in Fermi-bounce Curvaton Cosmology," Chin. Phys. C 44, 105101 (2020). arXiv: 1810.05513
- **Key result:** One-loop radiative corrections to the torsion contact interaction give effective ekpyrotic behavior → addresses BKL anisotropy problem without extra scalar.
- **Spectrum/f_NL:** Uses prior results. No new computation.

### D7. Tukhashvili & Steinhardt (2023)
- **Citation:** G. Tukhashvili, P.J. Steinhardt, "Cosmological Bounces Induced by a Fermion Condensate," PRL 131, 091001 (2023). arXiv: 2307.16098
- **Background:** Chiral condensate from EC torsion interaction → bounce
- **Spectrum/f_NL:** Background only. Perturbations flagged as future work.
- **Closeness to Branch V:** MODERATE. Uses EC torsion for the bounce, but a different physical mechanism (condensate vs spin-fluid), and no perturbation results.

### D8. Tukhashvili (2023)
- **Citation:** G. Tukhashvili, "Torsion, Gravity Induced Chiral Symmetry Breaking and Cosmological Bounce," PRD 109, 043536 (2024). arXiv: 2309.08654
- **Perturbation calculation left explicitly as future work.**

---

## E. Barbero-Immirzi / Holst Action Papers

### E1. Taveras & Yunes (2009)
- **Citation:** V. Taveras, N. Yunes, arXiv: 0903.4407, PRD 80, 104007 (2009)
- **Content:** Promotes Barbero-Immirzi parameter to dynamical pseudoscalar. Studies CMB effects. NOT a bounce calculation.

### E2. Bombacigno, Boudet, Montani et al. (2016–2024)
- Multiple papers on Immirzi field + torsion bounce dynamics. Background only. No perturbation spectra.

---

## F. PGT / Other Torsion Bounce

### F1. EC Ekpyrotic Bounce (2025)
- **Citation:** arXiv: 2512.11885
- **Content:** EC + Weyssenhoff spin fluid + ekpyrotic scalar. Dynamical systems analysis. Background only. "Perturbation treatment left for future work."

### F2. Scalar-Torsion Gravity Perturbations (Toporensky & Tretyakov 2021)
- **Citation:** arXiv: 2110.12332
- **Content:** Teleparallel f(T) gravity perturbations. Different torsion definition from EC. Not directly relevant.

---

## G. Key Finding: f_NL = 5/12 Is WRONG

The value f_NL = 5/12 that we quoted in Phase 1a (06_fNL_estimate.md) is **NOT the matter bounce result**. It is the Maldacena (2003) coefficient for single-field slow-roll inflation:

$$
f_{\rm NL}^{\rm local} = \frac{5}{12}(1 - n_s)
$$

This gives f_NL ~ 0.015 for observed n_s.

The actual matter bounce result from Cai et al. (2009) is:

$$
f_{\rm NL}^{\rm local} = -\frac{35}{8} \approx -4.375
$$

for a canonical scalar field. This is ~300× larger in magnitude and opposite in sign. Furthermore, the Quintin et al. (2015) no-go theorem shows that f_NL is enhanced during the bounce if perturbation growth is needed to suppress r.

**Our Phase 1a f_NL estimate must be corrected.**

---

## H. Summary: Literature Coverage

| Topic | Papers exist? | Gap for ECH? |
|-------|--------------|--------------|
| n_s = 1 from dust contraction | YES (Finelli & Brandenberger 2002) | No gap |
| f_NL in matter bounce | YES (Cai et al. 2009: −35/8) | No gap |
| No-go theorem (r vs f_NL) | YES (Quintin et al. 2015) | Unknown if applies to ECH |
| LQC bounce perturbations (same Friedmann eq) | YES (Wilson-Ewing 2013) | Gap: ECH ≠ LQC at perturbation level? |
| EC/torsion bounce spectrum | PARTIAL (Alexander et al. 2014) | Gap: no f_NL, no r, torsion only in background |
| ECH-specific perturbation theory | NO | Gap exists |
| Holst term in perturbation equations | NO | Gap exists |
| Transfer of ζ or Φ through ECH bounce | NO | Gap exists |
