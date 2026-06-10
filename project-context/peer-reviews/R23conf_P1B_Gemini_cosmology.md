# P1B R23conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.51.pdf` md5=856fbad2 pages=13
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 164.8s

---

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..." by Houston Golden

This paper presents technical verification material for a larger research program on Einstein-Cartan-Holst (ECH) cosmology. It documents three distinct numerical analyses: (1) a Markov Chain Monte Carlo (MCMC) analysis of the ΛCDM+ΔNeff model using stock CAMB as a null test, (2) a validation of a NaMaster-based pseudo-Cℓ pipeline for cosmic birefringence on synthetic skies, and (3) a consistency check of the observed cosmic birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-written, rigorous, and transparent. The scope of each analysis is clearly and repeatedly defined, with crucial distinctions made between pipeline validation and sky detection, and between generic phenomenological tests and specific theoretical predictions. The level of detail provided for reproducibility, including code repositories, likelihood configurations, and MCMC chain diagnostics, is exemplary and meets the highest standards of the field. The numerical results are presented with appropriate statistical caveats, and all calculations appear to be correct. The paper serves its stated purpose as a technical companion document effectively.

While the paper is in excellent condition and ready for publication, I have a few minor suggestions for improvement.

---

### Detailed Findings

#### MINOR

**P1B-M1: Section VI, Page 9, Birefringence Formula Convention**
The paper uses the formula `β ≈ (α_EM / 4π) * C_αγ * (Δφ/fa)`. While the numerical calculation based on this is correct, the prefactor for the photon-axion coupling-induced birefringence angle can be convention-dependent (e.g., `α_EM / 2π` is also common, depending on the Lagrangian definition).
**Required fix:** For clarity and to aid readers, please briefly state the Lagrangian convention for the photon-ALP coupling `g_aγγ a Fμν F̃μν` that leads to this prefactor, or cite a standard reference that uses this specific `1/4π` convention.

**P1B-M2: Section IV, Page 6, Mode-Coupling Matrix Notation**
The text states, "The Mee' matrix is computed...". The notation `Mee'` is slightly ambiguous. It likely refers to the EE block of the full mode-coupling matrix that maps harmonic-space Cℓ to pseudo-Cℓ, but the prime could be misinterpreted.
**Required fix:** Please clarify the notation. For example, specify that this refers to the EE block of the mode-coupling matrix, `M_{bb'}^{EE}`, which couples different bandpowers.

#### NIT (Cosmetic)

**P1B-N1: Section III, Page 3, Informal Phrasing**
The text reads: "here 'minimal' = the single-scalar w = 0 matter-dominated contraction phase". The use of an equals sign is slightly informal for a publication in PRD.
**Required fix:** Please rephrase for more formal language, e.g., "(where 'minimal' refers to the single-scalar...)" or "(in this context, 'minimal' denotes...)".

**P1B-N2: Section VI, Page 9, Informal Phrasing**
The text states: "All three within 1σ."
**Required fix:** Please consider a more formal phrasing, such as "All three values are consistent within their respective 1σ uncertainties."

**P1B-N3: Figure 3 Caption, Page 7, Color Descriptor**
The caption refers to "outer (light) error bars". In a printed or grayscale version, "light" may not be an effective descriptor.
**Required fix:** Please consider using a more robust descriptor, such as "outer (faint) error bars" or simply "outer error bars".

---

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is a high-quality methods paper that exemplifies scientific rigor and transparency. The authors have meticulously documented their analyses, clearly delineated the scope and limitations of their work, and provided extensive materials for reproducibility. The paper is a valuable contribution as a technical companion to its associated research program. The required corrections are minor and intended to further improve the clarity of an already excellent manuscript. Once these minor points are addressed, the paper is suitable for publication in Physical Review D.