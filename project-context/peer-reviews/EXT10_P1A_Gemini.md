# EXT10 Harvest — P1A — Gemini
- Provider: Gemini
- Model/Effort: 3.5 Thinking (Solves complex problems)
- Chat URL: https://gemini.google.com/u/0/app/c522ddc10dbdff0b
- PDF md5: ea008466
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report

**Journal:** Physical Review D / JCAP
**Paper Title:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden
**PDF Date:** June 13, 2026
**Version:** v1A.0.71

---

**1. Recommendation: MINOR REVISIONS**

This is an exceptionally well-scoped, rigorous, and clear-headed phenomenological audit of minimal Einstein-Cartan-Holst (ECH) gravity. The paper systematically deconstructs the pathways by which spin-torsion configurations could map onto late-time dark energy, establishing a robust channel-level "no-go" for four standard minimal routes. The mathematical arguments are sound, and the author is highly commendable for explicitly distinguishing between true derivations, loop-quantum-cosmology prescriptions, and phenomenological scaling ansätze.

Because the load-bearing claims are structurally solid and the methodology is highly transparent, the paper is fundamentally fit for publication. The recommended minor revisions are solely intended to address submission-epoch synchronization with companion works and minor technical definitions.

---

**2. Blockers (Must Fix Before Publication)**

None. The paper presents no structural failures, unsupported foundational claims, or missing controls that invalidate its central conclusions.

---

**3. Majors (Should Fix)**

None. The scoping limits (such as treating the off-shell mass dimension mapping as a phenomenological ansatz and leaving the full operator-basis space to future work) are explicitly stated and justified. There are no major scientific gaps requiring deep rework.

---

**4. Minors (Polish)**

- **Companion Paper Placeholders (Sec. I & References):** The text frequently references companion papers "in preparation" (specifically Papers II, Ib, and IV). While understood to be part of a coordinated submission sequence, the author should ensure that actual arXiv identifiers or finalized cross-references are updated during the proofing stage once the concurrent manuscripts are posted.

- **Repository and Data Pinning (Sec. XIV):** The text links to a live GitHub repository for the reproducibility pipeline. Prior to final production, the author should substitute or append a permanent Zenodo DOI or similar immutable repository snapshot to secure the frozen MCMC chains and configuration artifacts long-term.

---

**5. Strengths**

- **Exemplary Structural Transparency:** The author avoids the common pitfall of obfuscating scaling assumptions, explicitly labeling the dimension +1 off-shell operator's transition to a dimension +4 local vacuum density as a phenomenological ansatz rather than an EFT derivation.

- **Definitive Proof of Perturbation Transparency:** The application of the first (algebraic) Bianchi identity (Rμ[νρσ]=0) to demonstrate the clean pointwise vanishing and decoupling of the Holst sector from all classical scalar/tensor perturbation equations of motion on the torsion-free branch is elegant and physically definitive.

- **Rigorous Reheating Thermodynamics:** The treatment of the thermal-reset barrier avoids lazy assumptions about total particle densities, correctly identifying that the algebraic torsion tracks the axial current expectation value (⟨Jμ5⟩), which is driven to zero in a thermal bath.

- **Honest Multi-Survey Forecasting:** The discussion of the structural tension between dark energy dilution (Ntot≈92) and the preservation of the matter-bounce non-Gaussianity signature (fNL=−35/8) provides a vital reality check for joint observational pipelines.

---

**6. Specific Scrutiny**

**A. Four-Route Channel-Level Closure**
The systematic closing of the four minimal channels is executed with excellent granularity. Routes 1–3 are cleanly dismissed via amplitude-budget constraints:

- Route 1 (NJL contact): Correctly identified as parity-even under the Lorentz contraction of two axial-vector pseudovectors, with a mean-field amplitude suppressed by roughly 69 orders of magnitude relative to the observed dark energy density.
- Routes 2 & 3 (One-loop corrections & Immirzi running): Thoroughly constrained by Planck suppression and mass-dimension locks, demonstrating that quantum adjustments fall short of the observed birefringence signature by at least 58 to 60 orders of magnitude.
- Route 4 (Parity-CMB coupling): The author rightly notes that this channel is not mathematically closed by an amplitude deficit, but rather by an explanatory deficit. Demanding that the spectator field yield both the observed dark energy density (ρΛ) and the birefringence angle (βobs) forces an ultralight-mass tuning (mθ∼H0). This cleanly demonstrates that Route 4 merely relocates the cosmological constant problem into an inflationary initial condition rather than solving it.

**B. Perturbation-Transparency Result for Canonical Scalar Matter**
The theorem in Section X successfully generalizes historical Einstein-Cartan assumptions to the Holst sector across all perturbation orders. Because a canonical scalar field yields zero spin density (S=0), classical torsion vanishes identically (T=0). The author's explicit correction of an earlier draft's misidentification (clarifying that the single-curvature Holst dual contraction vanishes pointwise via the first algebraic Bianchi identity, distinguishing it from the two-curvature Pontryagin density total derivative) adds immense value and technical accuracy to the manuscript. The conclusion that the scalar bispectrum maps identically to standard General Relativity is watertight.

**C. Reheating Thermal Reset**
The thermodynamic erasure analysis in Section II C 1 is a standout feature of the paper. Because minimal ECH torsion lacks a kinetic term, it is non-propagating and slave to the instantaneous local axial current. The author correctly outlines that even if the total fermion number density (nψ) is massive at reheating, an unpolarized plasma in C/P-equilibrium forces ⟨Jμ5⟩→0. The explicit hierarchy of chirality-flipping rates—correctly identifying the Standard Model top-Yukawa interaction (Γt/H≫1) as the primary, dominant thermalizing channel at 10^15 GeV before electroweak-sphalerons complete the erasure later—proves a robust thermodynamic barrier that bypasses simple kinematic scale bookkeeping.

**D. Spectator-ALP Birefringence as a Class Test**
The treatment of the uniform cosmic birefringence benchmark (β≈0.27°) is phenomenologically mature. Rather than parading this value as a triumph or unique prediction of ECH, the author explicitly categorizes it as an ECH-independent consistency check shared entirely with a standard GR+ALP framework using identical parameters. The WKB phase analysis in Appendix C is technically sound; recomputing the spatial-gradient scales to verify the ∼10^−35 eV background rate against a 6×10^−4 eV CMB photon establishes a safe WKB compliance margin of over 30 orders of magnitude. Furthermore, the statistical warning in Section XV regarding LiteBIRD's actual model-discrimination threshold (properly accounting for current Planck uncertainty quadrature to show a real tension of ∼0.73σ instead of a naive 2.4σ) reflects excellent data literacy.

---

**Final Verdict**

The manuscript is exceptionally comprehensive and introduces an important foundational barrier catalog for alternative cosmologies. Once the author coordinates the companion placeholders upon arXiv publication, this paper will be fully ready to anchor its place in the literature.
