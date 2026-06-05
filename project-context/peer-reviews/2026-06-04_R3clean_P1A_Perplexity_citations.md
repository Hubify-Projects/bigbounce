# P1A 2026-06-04_R3clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 22.8s

---

I cannot complete the requested referee report to the standard you asked for because the paper’s citation claims need live arXiv/ADS verification and I do not actually have browsing access in this session beyond the single supplied search block. I can still give you a **partial forensic audit** of the text you provided, but it will be incomplete and should not be treated as a final PRD referee report.

## Partial citation-forensics findings

**P1A-M1 — Section I / p. 3–4 — “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9, 10]”**  
Problem: This is presented as a settled motivating fact, but the paper later treats DESI-driven \(w_0w_a\) evidence as merely compatible with quintom scenarios and not used in any calculation. The claim also conflates BAO-only constraints with full dynamical-DE inference without specifying the exact dataset combination.  
Required fix: State precisely which DESI analysis is meant, what parameterization was fit, and which significance belongs to which dataset. If the paper is not using the result quantitatively, downgrade the statement to a contextual remark.

**P1A-M2 — Section I / p. 4 — “Companion paper, this volume” / multiple “in preparation” references [2], [6], , , **  
Problem: The paper repeatedly relies on unpublished companion works for core numerical claims, MCMC outputs, SPHEREx forecasts, galaxy-spin catalogs, and reproducibility. In a PRD submission, this is not acceptable as support for central results unless those works are publicly accessible and citable.  
Required fix: Replace internal/in-preparation citations with public arXiv/ADS references or remove the dependent claims from the present manuscript.

**P1A-E1 — Abstract / p. 1–2 — “We assess four enumerated minimal-Einstein-Cartan-Holst (ECH) spin-torsion channels … and find that each fails at the amplitude level”**  
Problem: The abstract claims “closure” of the four routes, but the body repeatedly concedes that Route 4 is not amplitude-closed and is only rejected by a naturalness/explanatory-deficit argument. That is not the same as an amplitude-level no-go.  
Required fix: Revise the abstract to match the actual proof status: Route 4 is not amplitude-excluded; it is constrained by a model-building/naturalness argument under additional assumptions.

**P1A-E2 — Abstract / p. 1–2 — “the four enumerated routes (NJL, one-loop EA, Immirzi running, parity-CMB) are not proven to be a complete diffeomorphism-invariant operator basis”**  
Problem: The paper explicitly admits missing operators, but still uses language like “channel-level closure” and “no-go” in a way that can be mistaken for a theorem about the full operator basis.  
Required fix: Make the scope limitation prominent in the abstract and conclusion: this is a closure of four hand-picked channels, not a theorem about the full ECH EFT.

**P1A-M3 — Abstract / p. 1–2 — “the Holst dual contraction … reduces on the Levi-Civita connection to the Pontryagin density ∝ RR̃”**  
Problem: This is broadly true, but the paper’s later notation is internally inconsistent, alternating among \(RR̃\), \(\partial_\mu K^\mu\), and “total derivative” language without a clean derivation.  
Required fix: Standardize notation and give the exact identity once, with the precise conditions under which it holds.

**P1A-M4 — Abstract / p. 1–2 — “for canonical scalar matter, torsion vanishes at all perturbation orders”**  
Problem: The statement is too broad. The body later restricts the result to canonical scalar matter and explicitly excludes fermions, non-minimal couplings, dynamical torsion, and boundary/topological sectors.  
Required fix: Add the exclusions directly into the abstract sentence.

**P1A-M5 — Section II A 1 / p. 5 — Eq. (1), “T abc Tabc” in the action**  
Problem: The text describes \(T^{abc}T_{abc}\) as a shorthand for the four-fermion contact interaction after integrating out torsion, but in the displayed action it is written as if it were part of the fundamental action. That is conceptually misleading.  
Required fix: Separate the fundamental ECH action from the effective four-fermion term after torsion elimination.

**P1A-M6 — Section II A 1 / p. 5 — “The Holst term contributes non-trivially when fermions are present”**  
Problem: This is too vague and risks overstatement. In minimal coupling, the Holst term affects the torsion sector algebraically, but the paper later claims perturbation transparency for canonical scalar matter.  
Required fix: Clarify that the Holst term affects fermionic torsion elimination and parity-odd effective operators, not scalar perturbations in the stated canonical setup.

**P1A-M7 — Section II A 2 / p. 5–6 — Eq. (5)–(7), mass-dimension claims**  
Problem: The paper repeatedly says the parity-odd operator has off-shell mass dimension \(+1\) and then uses an on-shell scaling ansatz to map it to \(\rho_\Lambda\). This is not a derivation and is presented too confidently in several places.  
Required fix: Label all \(\rho_\Lambda\) mappings as phenomenological ansätze everywhere, not as derived relations.

**P1A-M8 — Section II B / p. 6 — “Ashtekar & Singh  quote the canonical LQC value ρcrit ≃ 0.41 ρPl at the standard LQC area-gap choice γ = 0.2375”**  
Problem: The paper imports a scheme-dependent value and then extrapolates it across counting prescriptions to \(0.27\,\rho_{\rm Pl}\). That extrapolation is internal, not directly quoted from the cited review.  
Required fix: Distinguish cited values from author extrapolations and do not present the extrapolation as a published LQC result.

**P1A-M9 — Section II C 1 / p. 6–7 — “Reheating thermal-reset barrier”**  
Problem: This entire mechanism is an author-constructed thermodynamic argument, but it is written as if it were an established closure theorem. It is not supported by any cited source in the paper text shown.  
Required fix: Mark this as the authors’ heuristic argument and do not cite it as established literature.

**P1A-M10 — Section III A / p. 7 — “Connecting to a quantitative rotation angle β … requires an explicit photon-torsion coupling that has not been derived here.”**  
Problem: The paper later uses the observed birefringence value numerically as though it were available to constrain the coupling in Routes 2–4. This is a modeling choice, not a derived prediction from ECH.  
Required fix: Explicitly separate the observational fit from the ECH derivation and avoid implying ECH predicts \(β\).

**P1A-M11 — Section IV B / p. 9 — “The one-loop induced β is suppressed by ∼ 58–60 orders of magnitude relative to the observed signal”**  
Problem: The paper itself notes an alternative ordering yielding a numerically distinct \(\sim10^{-33}\) ratio. Presenting both as compatible is a red flag for unstable dimensional bookkeeping.  
Required fix: Choose one consistent dimensional convention and eliminate the alternate orderings, or clearly state that the estimate is not robust enough for a quantitative no-go.

**P1A-E3 — Section IV D / p. 10 — Route 4 is “closed by a naturalness objection rather than amplitude no-go”**  
Problem: This directly violates the paper’s own recurring claim that all four routes are closed “at the amplitude level.” Route 4 is not amplitude-closed in the manuscript’s own text.  
Required fix: Downgrade the global closure claim throughout the paper, or provide an actual amplitude exclusion independent of the naturalness argument.

**P1A-M12 — Section IV D / p. 10 — “the overshoot conclusion is conditional on the one-loop matching assumption”**  
Problem: A conditional argument is being used as a definitive channel closure. If \(\alpha/M\) is allowed to float, the paper says both \(β\) and \(\rho_\Lambda\) can be matched.  
Required fix: State explicitly that the “no-go” only applies under the rigid one-loop matching prior; otherwise the route survives as a phenomenological fit.

**P1A-M13 — Section IV D / p. 10 — “mθ ∼ H0 … is precisely the cosmological constant problem in disguise”**  
Problem: This is an interpretive statement, not a no-go theorem. The paper should not present it as a proof of failure.  
Required fix: Recast as a model-building criticism, not as a mathematical exclusion.

**P1A-M14 — Section IV E / p. 11 — “the condensate mechanism investigated in earlier internal versions”**  
Problem: Internal version history leaks into the body prose. This is exactly the kind of review-log artifact that should not appear in a submission.  
Required fix: Remove all references to earlier internal versions from the body.

**P1A-M15 — Section VI / p. 11 — “The CMB birefringence channel provides the surviving parity-violation evidence from the published WMAP+Planck Eskilt & Komatsu measurement”**  
Problem: The paper treats a single birefringence measurement as “surviving parity-violation evidence,” but the evidence is statistically modest and literature-dependent. The manuscript also conflates central value, prior, and follow-up constraints in different places.  
Required fix: Present the birefringence result as a tentative observational hint, not as established evidence.

**P1A-M16 — Section IX / p. 12–13 — “14 mechanism-class constraints” vs “13 logically-independent barriers”**  
Problem: The manuscript uses two different counting systems and then says one barrier is subsumed by another. The logic is fragile and the presentation is opaque.  
Required fix: Provide one unambiguous barrier count and one mapping table; do not alternate between 13 and 14 as though both are equivalent.

**P1A-M17 — Section X / p. 14 — “For canonical scalar field matter, torsion vanishes at all perturbation orders”**  
Problem: This is the core theorem of the paper, but the proof only establishes it for a restricted matter content and under minimal-coupling assumptions. The claim is over-broadened in the statement of the theorem.  
Required fix: Restate the theorem with all assumptions inline, including the exclusions listed later in the manuscript.

**P1A-M18 — Section X B / p. 14 — “The bispectrum is therefore identical to the standard GR result.”**  
Problem: This is only true under the paper’s restricted setup. The manuscript later discusses non-minimal couplings and fermions as exceptions, so the unconditional language is too strong.  
Required fix: Qualify the statement by the assumptions under which it holds.

**P1A-M19 — Section XI / p. 15 — “We considered appending late-time dynamical dark-energy freedom (CPL w0 wa ) to the bounce model, explored across 7 disguised forms”**  
Problem: “disguised forms” is editorially loaded language, not a technical classification.  
Required fix: Replace with neutral terminology and define the seven cases explicitly as model extensions.

**P1A-M20 — Section XII / p. 15–16 — “the framework has not solved the cosmological constant problem; it has only relocated the fine-tuning into inflationary initial conditions”**  
Problem: This directly undercuts the paper’s earlier “closure” rhetoric and should be reflected in the abstract and conclusion.  
Required fix: Make the limitation central, not incidental.

**P1A-M21 — Section XIII / p. 16–17 — “SPHEREx tests the former, LiteBIRD tests a related spectator field, and the ECH dark-energy ansatz remains a phenomenological parameterization.”**  
Problem: The paper presents these as surviving tests of the program, but they are not predictions of ECH itself.  
Required fix: Recast them as tests of external companion scenarios, not of the ECH no-go result.

**P1A-M22 — Section XIV B / p. 17 — “stock CAMB with ∆Neff only”**  
Problem: The text admits the MCMC pipeline does not implement the torsion model. This means the cosmological-fit claims cannot be used as direct validation of the manuscript’s ECH mechanisms.  
Required fix: Remove any implication that the MCMC analysis tests the ECH torsion model itself.

**P1A-M23 — Section XV / p. 18 — “under the stated assumptions, the 14 mechanism-class constraints … close each of the four enumerated minimal-ECH dark-energy routes at the amplitude level.”**  
Problem: This is the manuscript’s global conclusion, but it is contradicted by the body’s own admission that Route 4 is not amplitude-closed and that the surviving ALP fit is possible if \(\alpha/M\) is floated.  
Required fix: Revise the conclusion to reflect the conditional, non-universal nature of the no-go.

**P1A-M24 — Appendix B / p. 19 — “The parity-odd operator (Eq. 6) has off-shell mass dimension +1, not the +4 required for a local Lagrangian density”**  
Problem: The appendix reveals the central operator is not a controlled EFT operator. That is a major limitation and should be reflected much earlier, not buried in an appendix.  
Required fix: Promote this limitation to the abstract and main text, and demote the main claim accordingly.

**P1A-M25 — Appendix B / p. 19 — “Earlier draft framings … attempted to ‘repair’ the dimensional gap”**  
Problem: Internal draft-history material is exposed in the submitted text.  
Required fix: Remove all draft-history references.

**P1A-M26 — References [2], [6], , ,  — unpublished internal items**  
Problem: These are not publicly citable works. The manuscript uses them to support crucial claims, including numerical results and data products.  
Required fix: Replace with public preprints or remove the claims relying on them.

**P1A-M27 — References , , , , ,  — likely recent preprints requiring metadata verification**  
Problem: These entries are presented with journal/preprint metadata in a way that may be partially fused or unstable. Without live ADS/arXiv checking, I cannot confirm whether all titles, venues, and arXiv IDs are correct.  
Required fix: Verify every citation against arXiv and ADS; correct any mismatched title/author/venue/arXiv combinations.

**P1A-M28 — Reference  — “Quantum Einstein-Cartan theory with the Holst term”**  
Problem: The cited paper is used to support the one-loop operator structure, but the present manuscript also claims to derive a specific coefficient from it that the cited work may not actually provide.  
Required fix: Verify that the cited paper really contains the stated coefficient structure; if not, remove the attribution and present it as an ansatz.

**P1A-N1 — Page 1/Abstract — duplicated phrasing around “channel-level closure” and “four enumerated minimal-ECH dark-energy routes”**  
Problem: The abstract repeats the same formulation several times in near-identical wording, suggesting editing artifacts and weakening readability.  
Required fix: Remove redundant repetitions.

**P1A-N2 — Various — inconsistent capitalization and hyphenation of “Einstein-Cartan-Holst” / “Einstein–Cartan–Holst” / “minimal-ECH”**  
Problem: Terminology is not standardized.  
Required fix: Use one canonical style throughout.

**P1A-N3 — Various — “Paper I(a), Paper I(b), Paper II, Paper III, Paper IV” cross-document labeling**  
Problem: This is internal series nomenclature, not self-contained scientific referencing.  
Required fix: Convert these to public references or remove them from the main body.

## Summary recommendation
**REJECT**

The manuscript does not currently meet PRD standards because its central no-go claim is overstated relative to what the text actually proves, one of the four routes is explicitly not amplitude-closed, and critical supporting results are outsourced to unpublished companion papers and internal analyses. In addition, the paper contains unresolved dimensional-analysis ambiguities, internal version-history artifacts, and numerous claims that require live citation verification against arXiv/ADS before the bibliography can be trusted.