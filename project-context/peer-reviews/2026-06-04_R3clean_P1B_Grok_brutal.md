# P1B 2026-06-04_R3clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 11.8s

---

**Referee Report: P1B (Technical Verification Companion to the ECH Spin-Torsion Program)**

**P1B-E1 (ESSENTIAL)**  
Section: Abstract (entirety) + p. 2 (Scope of this paper)  
Problem: The abstract states “We report the technical verification material for the Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program” and presents numerical results, yet the body repeatedly declares that none of the three analyses actually test the ECH framework (“Not a spin-torsion theory module”, “NOT the physical separation of the cosmic-rotation angle β”, “Not a distinctive ECH prediction”). The abstract therefore misrepresents what the manuscript proves.  
Required fix: Rewrite the abstract to state only what is actually demonstrated (stock-CAMB proxy consistency checks and a NaMaster pipeline validation on a foreground-cleaned map). Remove all ECH-specific framing.

**P1B-E2 (ESSENTIAL)**  
Section: Multiple locations (pp. 2–4, 6–8, footnotes 1, a, 4, and text in Secs. III, V, VI)  
Problem: The manuscript contains extensive internal audit tags, version-history language, and review-log artifacts, including “corrected fire #25”, “the nested-sampling ln B recompute is queued”, “stale mid-burn-in diagnostic convergence gpu 20260305 stale.csv”, “earlier draft footnote”, “arithmetic error”, “prior versions described the bias as…”, and repeated references to previous convergence states and reviewer concerns. These violate journal submission standards.  
Required fix: Remove every such phrase, footnote, and reference. The final manuscript must contain no trace of internal bookkeeping or prior-round language.

**P1B-E3 (ESSENTIAL)**  
Section: Sec. V B and Table II (pp. 4–5)  
Problem: The paper reports marginal-tail extrapolations labeled “+4.3σ” and “−3.6σ” from the LCDM point while simultaneously stating that the point is unsampled and that a Savage-Dickey ratio is invalid. These σ values are therefore not on the same statistical footing as conventional posterior constraints and are presented without adequate qualification.  
Required fix: Delete all σ-distance claims relative to the unsampled LCDM point or replace them with a clear statement that no quantitative tension metric is provided.

**P1B-M1 (MAJOR)**  
Section: Entire manuscript (11 pages)  
Problem: The paper consists almost entirely of scope disclaimers, null-consistency statements, and deferred analyses. After removal of internal artifacts (E2), the remaining substantive content is a standard ΛCDM+ΔN_eff run and a NaMaster validation on a single map—material too slender for an 11-page PRD methods paper.  
Required fix: Condense to a 4-page (maximum) technical note or withdraw. Alternatively, supply the actual ECH-modified Boltzmann module and sky-detection results promised by the title.

**P1B-M2 (MAJOR)**  
Section: Sec. VI and footnotes 3–4 (pp. 6–7)  
Problem: The spectator-ALP consistency check is presented as supporting the ECH program while the text states that the identical birefringence arises in standard GR, requires ∼25× fine-tuning of θ_i to remain a spectator, and lies outside minimal ALP benchmarks (|C_aγ|∼9–51). The section therefore functions as an extended caveat rather than a positive result.  
Required fix: Either remove the section or reframe it explicitly as a negative consistency test showing that the observed β cannot be accommodated by a minimal spectator ALP without additional model-building.

**P1B-M3 (MAJOR)**  
Section: Abstract and Sec. IV (p. 5)  
Problem: Pipeline-recovery SNRs (20.32σ, 25.71σ) are reported in the same paragraph as the published 2.4–2.9σ sky detection without a clear statement that the two numbers are on completely different statistical footings (MC signal recovery vs. actual sky measurement).  
Required fix: Delete all pipeline SNR numbers from the abstract and results summary or place them in a separate “Methods validation only” subsection with explicit non-comparability language.

**P1B-N1 (MINOR)**  
Section: Abstract (footnote a)  
Problem: Footnote marker “a” appears inside the abstract sentence with awkward phrasing (“2.4–2.9σ [2, 3];a the pipeline”).  
Required fix: Move all explanatory material on Eskilt & Komatsu to the main text or a proper endnote.

**P1B-N2 (NIT)**  
Section: Appendix B title (p. 9)  
Problem: Appendix B is labeled “Claims Classification” but contains only a one-line table header with no content.  
Required fix: Delete the empty appendix.

**P1B-N3 (NIT)**  
Section: Throughout  
Problem: Inconsistent use of “PR4/NPIPE” versus “Planck PR3+WMAP9” labels for the same β = 0.342° ± 0.094° (3.6σ) result.  
Required fix: Adopt a single, unambiguous citation for the headline birefringence value.

## Summary recommendation
REJECT

The manuscript cannot be considered for publication in its present form. It contains pervasive internal review artifacts and version-history language that are incompatible with journal submission, the abstract materially misrepresents the heavily caveated results actually demonstrated, and the scientific content—after removal of disclaimers and deferred analyses—does not constitute a substantial, self-contained methods contribution.