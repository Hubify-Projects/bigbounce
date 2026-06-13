# EXT10 Harvest — P1A — ChatGPT
- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc597-d61c-83e8-ac93-8f3bf7f139fb
- PDF md5: ea008466
- Harvested: 2026-06-13 15:16 PDT

---

## Referee report on Paper 1A v1A.0.71

**Manuscript:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

---

**Recommendation: MINOR REVISIONS**

I read the full 28-page PDF end-to-end. The manuscript is unusually self-auditing and now scopes its central claims much more carefully than the title alone might suggest: it argues for channel-level closure of four enumerated minimal-ECH dark-energy routes, not for a complete operator-basis no-go theorem. The strongest result is the perturbation-transparency theorem for canonical scalar matter, which I find essentially correct under the stated assumptions. The remaining required changes are local consistency and wording fixes, not substantial scientific rework.

---

**BLOCKERS — must fix before publication**

**B1. Dimensional bookkeeping inconsistency between Sec. IV and Appendix B**
Location: Sec. IV scope paragraph, p. 11; Appendix B, p. 25, Eq. (B2).
Issue: Sec. IV says the dimensional reconstruction requires consistency between (α/M)M_Pl^3 and [(α/M)M_Pl]M_Pl^4, and then says the choice of M_Pl^5 versus M_Pl^3 controls N_tot. This is not a clean statement of the Appendix B convention. Appendix B uses ρ_Λ^bounce ~ (α/M)M_Pl^5 ~ 10^{-2}M_Pl^4, while the promoted local operator coefficient is described as αM_Pl^3/M. Those are different objects: one is the on-shell density ansatz; the other is a possible local operator promotion.
Proposed fix: Replace the Sec. IV sentence with something like: "The dimensional reconstruction used in Appendix B distinguishes the local operator promotion αM_Pl^3 ϵeeF/M from the on-shell density ansatz ρ_Λ^bounce ~ (α/M)M_Pl^5 = [(α/M)M_Pl]M_Pl^4. The quoted N_tot bookkeeping follows from the latter ansatz."

**B2. Reheating washout: residual sphaleron-rate contradiction**
Location: Sec. II.C.1, p. 9, reheating thermal-reset paragraph.
Issue: The paper correctly states that electroweak sphalerons do not exceed H at T_reh ~ 10^15 GeV, becoming relevant only after the plasma cools. But a few lines later it says the washout expectation follows from both α_W^5 M_Pl/T ≫ 1 and y_t^2 M_Pl/T ≫ 1 "at the GUT scale." The first inequality is inconsistent with the preceding sentence. The "top-Yukawa-first" ordering is the correct one; the sphaleron channel is later/lower-temperature support.
Proposed fix: Change the final condition to: "At T_reh ~ 10^15 GeV, the top-Yukawa channel gives the dominant rapid chirality-equilibration estimate, y_t^2 M_Pl/T ≫ 1. Electroweak sphalerons do not themselves exceed H at this temperature, but can complete the erasure once the plasma cools into the regime where α_W^5 M_Pl/T ≳ 1, while still above the electroweak transition."

**B3. Route 2 needs one unambiguous dimensional chain**
Location: Sec. IV.B, p. 12, Eq. (15) and following paragraph.
Issue: The Route-2 closure is likely correct in sign and conclusion — far too small to explain observed birefringence — but the current text leaves two different amplitude orderings in play: a canonical ~10^{-60} ratio and an "alternative ordering" giving ~10^{-33}. Both close the route, but a 27-order discrepancy inside a quantitative no-go section should not remain as an unresolved alternative.
Proposed fix: Add a compact derivation from the operator in Eq. (14) to the dimensionless rotation-angle ratio, including the line-of-sight integral and the anomaly-chain normalization if used. Then either remove the ~10^{-33} ordering or state explicitly that it is a deliberately loose upper bound not used in the closure.

---

**MAJORS — should fix**

**M1. Do not call Eq. (1) the "fundamental action" while it contains an on-shell torsion shorthand** (Sec. II.A.1, p. 5–6): Split the presentation into two equations: the genuine first-order ECH+Dirac action, followed by the post-elimination effective contact term.

**M2. Route 3 should avoid "relative to dark-energy density" unless an actual density ratio is shown** (Sec. IV.C, p. 12–13): Either compute the induced energy-density contribution and compare to ρ_Λ, or rephrase as "relative to the dimensionless parity-rotation/dynamical amplitude budget."

**M3. Clarify that "13 logically independent barriers" includes heterogeneous levels of proof** (Sec. IX and Table II, p. 16–17): Add one column to Table II with "status" (theorem / amplitude estimate / ansatz-level / heuristic / naturalness). Then say "13 non-identical barriers" or "13 logically distinct tests."

**M4. Companion-paper dependencies should be kept out of the core evidence chain** (Abstract, Secs. I.B, III, VII, X.G, XIII, XV): Separate the paper's reviewed results from programme context in two paragraphs.

**M5. Route 4 should always be described as an explanatory-deficit closure, not as a physical exclusion** (Sec. IV.D–E, Sec. XII.B, Sec. XV): Replace any remaining phrase of the form "R4 is closed" with "R4 is not a predictive minimal-ECH dark-energy derivation; it remains a standard GR+spectator-ALP fit with a cosmological-constant-scale mass tuning."

**M6. Reheating washout should not say "C/P-violating scattering" when the key channel is chirality equilibration** (Sec. II.C.1, p. 9): Replace "C/P-violating scattering rates that randomize axial polarization" with "chirality-flipping and depolarizing interactions that equilibrate the axial-current expectation value."

**M7. Perturbation-transparency theorem should state its technical assumptions in theorem form** (Sec. X.A–E, p. 19–20): Add a boxed "Theorem / Assumptions / Conclusion" statement at the start of Sec. X.

---

**MINORS — polish**

- Abstract length and density: Shorten to the claims, assumptions, and results (much longer than typical MNRAS/PRD/JCAP abstracts).
- PACS numbers: PACS is obsolete for most current journal styles. Remove unless targeting a journal that explicitly wants it.
- Terminology: "Confirmed null" for galaxy spins should be softened to "null in the stated pipeline."
- Figures 4–6: These are programme-roadmap figures. Consider moving at least one to an appendix or simplifying.
- Sec. X.B step 5: The "total derivative" statement is secondary; rephrase step 5 as a corollary, not a proof step.
- Use one symbol for the ALP field convention in each paragraph.
- Data availability: Zenodo DOI not yet minted. Create before proof stage.

---

**Specific scrutiny requested**

**Four-route channel-level closure (NJL / one-loop EA / Immirzi running / parity-CMB):** R1 is the cleanest closure. R2 and R3 are acceptable only as ansatz-level amplitude-budget closures; they need the dimensional cleanup above. R4 is correctly reframed as a naturalness/explanatory-deficit objection rather than an amplitude exclusion. PASS with fixes.

**Perturbation transparency for canonical scalar matter:** This is the strongest part of the paper. For canonical scalar matter, spin density vanishes, torsion vanishes algebraically, the connection reduces to Levi-Civita, and the Holst dual contraction vanishes by the algebraic Bianchi identity. The paper also correctly distinguishes this from the Pontryagin density. PASS — only cleaner theorem statement needed.

**Reheating thermal reset (axial current, not total fermion number):** Correctly identifies the torsion source as ⟨J_5^μ⟩, not the total fermion number density. That is an important correction and should remain. Residual issue is the rate-ordering language (B2 above).

**ALP birefringence β≃0.27°:** The manuscript correctly treats β≃0.27° as a benchmark consistency point of GR+spectator-ALP phenomenology, not as an ECH prediction. The ACT DR6 reference and value used are consistent with the arXiv record. PASS.

**EXT2 closures:** The Shapiro–Teixeira citation is correct in the PDF as Ref. [20], not Ref. [22]; arXiv:1402.4854 is confirmed as Quantum Einstein-Cartan theory with the Holst term. Appendix C's WKB scale now reads (α/M)φ'~10^{-35} eV, not 10^{-63} eV, and the comparison with a CMB photon scale is internally consistent. The sphaleron inequality inconsistency flagged in B2 remains.

---

**Strengths**

- The paper is unusually explicit about scope: channel-level closure, not operator-basis closure.
- The perturbation-transparency result is clean, useful, and likely publishable as a standalone theorem under the stated assumptions.
- The R4 revision is scientifically honest: the paper no longer claims an amplitude no-go where the real issue is mθ ~ H0 tuning.
- The reheating discussion correctly focuses on ⟨J_5^μ⟩, not the total fermion density.
- The manuscript distinguishes ECH predictions from broader bounce/ALP class tests, especially for f_NL = −35/8 and ALP birefringence.

---

**Overall assessment**

The problems are localized and do not require a new calculation or a major change to the paper's scientific conclusion. After the blockers are corrected and the major comments are addressed with clearer wording, the manuscript should be suitable for publication as a carefully scoped no-go/catalogue paper.
