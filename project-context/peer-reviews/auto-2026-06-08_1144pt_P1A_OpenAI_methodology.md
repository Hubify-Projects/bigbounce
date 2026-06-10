# P1A auto-2026-06-08_1144pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9940 chars)
**Wall time**: 235.9s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
I evaluated the full manuscript for methodological rigor, statistical validity, derivation chains, dimensional consistency, internal arithmetic, and traceability of every numerical claim in the abstract and conclusions. I also audited every table/figure for internal consistency and usefulness.

High-level assessment
The manuscript aims to close four commonly-invoked routes by which a minimal Einstein–Cartan–Holst (ECH) sector might source late-time dark energy, and to state a “perturbation-transparency” result for scalar/tensor cosmological perturbations. Much of the paper is qualitative. Where it becomes quantitative, a large fraction of the results and even basic numbers depend on unpublished “companion” works [2, 6, 23, 46] that are not available to the referee or readers. Several key derivations are only sketched; multiple load-bearing operators are admitted to be phenomenological or dimensionally inconsistent off-shell; and some amplitude estimates are internally inconsistent by tens of orders of magnitude depending on how missing mass dimensions are “re-associated.”

PRD requires self-contained methodology and rigor. As written, the paper does not meet PRD standards. Below I itemize specific findings.

Findings

ESSENTIAL

P1A-E1
- Location: Abstract, p. 1; Sec. I (Introduction), p. 3; throughout
- Problem: Core numerical claims are drawn from unpublished “companion works” and internal analyses. Examples: “ΛCDM+ΔNeff MCMC verification, NaMaster pipeline validation, and ALP parameter fitting are documented separately in companion work in preparation [6]”; “H0 = 67.68 ± 1.06, ΔNeff ≈ 0… are drawn from the companion internal MCMC analysis… should be read as internal-analysis inputs… rather than… peer-reviewable values until Paper I(b) is publicly posted.”
- Required fix: Remove all numerical claims not derived within this manuscript or from publicly available, citable sources. If MCMC results are needed, include full methods (likelihoods, priors, sampler settings, convergence metrics) and posteriors in this paper. Eliminate reliance on in-preparation works for any load-bearing conclusion or quoted value.

P1A-E2
- Location: Sec. II.A.2 (Derivation of the Parity-Odd Term), Eq. (6), pp. 5–6; Appendix B, p. 19
- Problem: The central operator Seff ∝ (α/M) ε e e F is admitted to have off-shell mass dimension +1 (not +4), and the mapping to ρΛ requires an “on-shell scaling ansatz.” Nonetheless, this ansatz underpins key quantitative claims (e.g., Ntot ≈ 92). Using an uncontrolled, dimensionally inconsistent operator to extract numbers presented as constraints is methodologically invalid.
- Required fix: Either (a) replace Eq. (6) with a controlled, gauge- and diffeomorphism-invariant local operator of dimension four with a fully specified coefficient, and re-derive all downstream quantities; or (b) remove all quantitative results that depend on Eq. (6), including the Ntot ≈ 92/94 discussion, Dinf e-fold scaling, and any “amplitude budget” conclusions that rely on the ansatz.

P1A-E3
- Location: Sec. IV.B (Route 2), Eq. (14)–(15), p. 9
- Problem: The one-loop “parity-odd effective action” Γone-loop ∝ (1/16π^2) β(γ)/MPl ∫ √−g ∂μθ J5μ is introduced without derivation and is dimensionally inconsistent as written if θ is dimensionless (∂θ has dimension 1, J5 has 3 → product 4; dividing by MPl introduces mass−1, lowering the Lagrangian density to mass^3). The subsequent amplitude estimate Eq. (15) mixes dimensional factors ad hoc and acknowledges giving answers differing by ∼27 orders of magnitude (“∼10−58 to 10−60” vs an “alternative ordering… ∼10−33”). This is not acceptable.
- Required fix: Present a correct, fully dimensionally consistent one-loop operator with its derivation or a precise literature citation demonstrating the operator and its coefficient; perform a clean, unit-consistent estimate of its observational impact. Remove the “alternative ordering” caveat and provide a single, reproducible amplitude bound with clear assumptions.

P1A-E4
- Location: Sec. X (Perturbation-Transparency Result), pp. 14–15; Abstract p. 1
- Problem: The “perturbation-transparency theorem” is asserted with a five-step sketch. There is no explicit variational derivation for the action at quadratic and cubic order in cosmological perturbations, no explicit check of boundary conditions/topological sectors in FRW, and no demonstration that the Holst term’s boundary contribution does not affect the constraint structure or canonical variables in the perturbation theory. Stating it for “all orders” requires more than a paragraph-level sketch.
- Required fix: Provide a rigorous derivation (in an appendix) of the decoupling at the level of the second- and third-order actions for scalar and tensor perturbations, including an explicit demonstration that the Holst term reduces to a total derivative that does not contribute to the Euler–Lagrange equations under the assumed boundary conditions. Clarify the scope: background topology, boundary terms, and any assumptions about compact support or falloff. If relying entirely on published theorems, cite them precisely and adapt notations to show one-to-one correspondence.

P1A-E5
- Location: Sec. IX.L (Barrier 12), Eq. (20), p. 13
- Problem: ΩGW^ECH|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is asserted with no derivation, no definition of ΩGW at the bounce, and no statement of how gravitational-wave energy density is bounded by ρcrit in the ECH framework. Squaring a density ratio to produce an “energy-density-fraction ceiling” is dimensionally opaque absent a definition.
- Required fix: Provide a derivation from the ECH/LQC dynamics linking the GW energy density to ρcrit/ρPl, or remove this barrier. If this is an order-of-magnitude heuristic, label it explicitly as such and do not use it as a barrier in Table II.

P1A-E6
- Location: Table III and associated footnote, p. 16
- Problem: The table includes live status of a running MCMC chain (“At the time of this writing the chain has accumulated ∼3.8×10^4 accepted samples… R̂−1 ≈ 3×10−2… we deliberately do not commit to a specific calendar date for convergence…”) and “this volume/companion paper” language. PRD does not allow in-progress/run-log content as part of scientific claims.
- Required fix: Remove all in-progress chain status and version-history prose. If w0wa analyses are needed, present completed, reproducible analyses within this paper or move all such discussion to a separate, published and citable paper and remove it here.

P1A-E7
- Location: Sec. V–VI and III.B (Galaxy spin), pp. 11–12, 8
- Problem: The “confirmed null” relies entirely on “Paper IV [23] (in preparation).” No sample description, classifier accuracy/confusion, bias tests, dipole estimator, or sky mask is provided here. As used, this is a load-bearing observational claim tied to a “barrier.”
- Required fix: Either remove the galaxy spin channel from the set of “tested” barriers or include a self-contained methods section with data description, classification metrics, test suite, null-test catalog, error propagation, and significance calculation for the dipole/hemisphere asymmetries.

P1A-E8
- Location: Throughout; e.g., Abstract p. 1; Sec. I p. 3; Sec. VII p. 11; Table I p. 4; Sec. XIII p. 16
- Problem: Repeated reliance on “companion works in preparation” [2, 6, 23, 46] for forecasts (SPHEREx σ(fNL)), MCMC validations, birefringence pipelines, and anomaly catalogs. PRD requires that load-bearing methods and results be available to referees and readers.
- Required fix: Remove all forward references for load-bearing results, or incorporate the necessary methods and results into this manuscript.

P1A-E9
- Location: Sec. II.C.1 (Inflationary suppression), pp. 6–7
- Problem: The factor (Treh/MGUT)3/2 is introduced as a “phase-space ansatz,” explicitly not derived from a thermal calculation but then used to fix Ntot at the level of a few e-folds. The “reheating thermal-reset barrier” is asserted without any quantitative rates (no Γ/H comparison, no cross sections).
- Required fix: Either provide a quantitative derivation (thermal integral for the parity-odd density-of-states factor and a Γ/H estimate showing rapid washout of J5) or demote these to qualitative remarks and remove any numerical dependence on them (e.g., Ntot values).

P1A-E10
- Location: Sec. IV.D (Route 4), Eq. (17), p. 10
- Problem: The birefringence mapping β ≈ (α/M) √(2ρθ)/mθ2 (note the manuscript’s numerator/denominator) is inconsistent with the usual axion-photon birefringence relation for L ⊃ (g/4) φ F F̃ (β ∼ g Δφ/2, with ρ = m^2 φ0^2/2 giving β ∼ g√(2ρ)/ (2 m)). The manuscript’s Eq. (17) drops numerical factors and conflates θ vs φ conventions without specifying kinetic normalization. It also uses g ≡ α/M but does not show how that identification follows from their θ-normalization.
- Required fix: Specify the scalar normalization (dimension-1 field vs dimensionless angle), the kinetic term, the photon coupling convention, and re-derive β(ρθ, mθ, g) with correct constants and units. Then recompute the inverted ρθ in the mθ ∼ H0 case and the stated “22–36 orders of magnitude overshoot” across the mass band with the corrected formula.

MAJOR

P1A-M1
- Location: Sec. II.A.2, Eq. (7), p. 6
- Problem: The one-loop estimate α/M ∼ (g^2/32π^2)(γ/M) ln(ΛUV^2/μ^2) + δNY is presented without defining g or δNY, and with no numerical inputs. The text then states “motivating [(α/M) MPl] ∼ 10−2.” This is not justified.
- Required fix: Define all symbols, cite a derivation or perform one, and show numerically how [(α/M) MPl] ∼ 10−2 follows (or adopt a benchmark value but clearly label it and disconnect any “conclusions” that depend on it).

P1A-M2
- Location: Sec. IV.C (Route 3), Eq. (16), p. 10
- Problem: The RG running ansatz dγ/d ln μ = (1/12π^2)(NLF − NRF) γ + O(γ^2) is given without derivation or a clear literature link, and the step to Δγ/γ ∼ 10−2 from GUT-to-IR is asserted without numbers. The conclusion that the effect is then suppressed by (Δγ/γ)(H/MPl) ∼ 10−63 relies on these unsupported inputs.
- Required fix: Either cite a derivation and plug in the Standard Model chiral content explicitly to show the integrated running, or remove the numerical bound and state only the qualitative mass-dimension argument.

P1A-M3
- Location: Sec. IX (Table II and barrier text), pp. 12–14
- Problem: Several “barriers” are qualitative statements (e.g., “Scale separation,” “Attractor-sensitivity dilemma,” “Gravitational democracy”) without formal statements, proofs, or quantitative bounds. They are presented as part of a “13 logically-independent” closure.
- Required fix: For each barrier used as part of a “closure,” either provide a precise theorem/proposition with assumptions and proof or reclassify them as qualitative observations and remove them from any count of “logically-independent constraints.” The paper’s title and abstract should reflect the (qualitative vs theorem-level) status.

P1A-M4
- Location: Sec. III.A, p. 7; Sec. XII (Spectator-ALP birefringence), p. 16
- Problem: The paper repeatedly quotes a “WMAP+Planck” βobs = 0.342° ± 0.094° and an “independent ACT DR6 follow-up β = 0.215° ± 0.074°,” and asserts consistency. There is no direct computation here of the joint constraint or a model comparison; the internal estimate of “LiteBIRD will not by itself separate 0.27° from 0.342°” is correct in spirit but requires explicit treatment of the posterior combination. Moreover, the mapping g ≈ 10−21 GeV−1 from β is not derived here.
- Required fix: If you retain any quantitative ALP coupling inference from β, include the explicit estimator definition and mapping, and show the posterior on g under your convention, or remove the numeric mapping and refer to literature constraints only.

P1A-M5
- Location: Sec. II.C.2 (Galaxy Spin Alignment Mechanism), p. 7–8
- Problem: “Underpredicts any plausible spin asymmetry by > 100 orders of magnitude” is asserted without a derivation or even a scaling argument, and is then used to justify a “confirmed null.”
- Required fix: Provide a back-of-envelope quantitative estimate with clear scaling to show the claimed ≥100 OOM suppression, or remove the claim.

P1A-M6
- Location: Multiple sections (e.g., Abstract p. 1; Sec. IV Scope note p. 8; Sec. XV Conclusions p. 18)
- Problem: The manuscript repeatedly asserts “channel-level closure” while explicitly acknowledging omission of important operators (e.g., Jackiw–Pi gravitational Chern–Simons, parity-odd four-fermion partner). Without an operator-basis closure or rigorous bounds on omitted terms, the “closure” language is overstrong.
- Required fix: Soften all claims of “closure” to “we find no viable route within the four enumerated channels under stated assumptions,” and move the operator-basis closure claim to future work. Alternatively, include an operator-basis enumeration with bounds.

MINOR

P1A-m1
- Location: Sec. II.B, Eq. (9), p. 6
- Problem: ρcrit formula is used with γ from BH entropy counting to quote 0.27 ρPl. While numerically consistent, this “internal extrapolation across counting schemes” should be clearly flagged as a choice, not a published LQC number (you partly do). A short, explicit derivation connecting Δ to ρcrit would improve clarity.
- Required fix: Add a short derivation or a footnote showing the Δ substitution and the resulting numerical factors.

P1A-m2
- Location: Sec. IV.A, p. 8–9
- Problem: Parity classification of (J5)^2 is correct; add a short sentence reminding readers why “pseudovector × pseudovector → scalar” is parity-even to forestall confusion (you partially do).
- Required fix: Expand by one sentence to make this airtight.

P1A-m3
- Location: Sec. X.D, Eq. (23), p. 14
- Problem: Notation alternates between R∧R̃, RR̃, and “Re(Γ)”. Standardize notation to avoid confusion; define Pontryagin density once and use a single symbol thereafter.
- Required fix: Harmonize notation and add a one-line definition in Sec. II or X.

P1A-m4
- Location: Fig. 2, p. 5
- Problem: Axis lacks units/labels (the y-axis is “energy density hierarchy”). As a conceptual figure, that is acceptable, but PRD usually expects either axes with units or explicit “schematic; not to scale.”
- Required fix: Add “schematic; not to scale” and a y-axis label “log energy density” (schematic).

P1A-m5
- Location: Acknowledgments, p. 18
- Problem: “Acknowledges the use of Claude… as an AI research assistant.” PRD policy may require a precise statement that the authors are responsible for all content and that no AI-generated text is unreviewed. You do say claims were independently verified, but please check journal policy.
- Required fix: Ensure compliance with APS policy on AI use; adjust acknowledgement language if required.

NITS

P1A-n1
- Location: Typographical: multiple places
- Problem: Spacing in names (e.g., “Pop lawski,” “Domaga la,” “G¨odel” mixing diacritics). These should be normalized.
- Required fix: Copy-edit names and diacritics consistently.

P1A-n2
- Location: Reference [22] line, p. 20
- Problem: Journal abbreviation “Annalen Phys.” is nonstandard; APS style uses “Ann. Phys. (Berlin).”
- Required fix: Update to standard journal abbreviations across the bibliography.

P1A-n3
- Location: Table I and text
- Problem: Footnote symbols and references (a, b, c) are dense and refer to in-prep materials.
- Required fix: After removing in-prep reliance (per E1/E8), simplify footnotes to keep only self-contained material.

Paper length
For the claimed contribution (primarily qualitative channel-by-channel arguments with one core “theorem”), 21 pages is excessive. If the essential issues are addressed, the paper could be condensed to ~10–12 pages by:
- Removing companion-paper logistics and internal run logs
- Consolidating qualitative “barriers” into a succinct section
- Providing a single rigorous derivation for the perturbation-transparency result, and
- Eliminating the galaxy-spin and PTA detours unless fully executed within this paper

## Summary recommendation
REJECT

The manuscript relies heavily on in-preparation companion works for core numerical claims and methods, presents key operators that are dimensionally inconsistent off-shell, contains an internally inconsistent one-loop amplitude estimate, and asserts a “theorem” without a rigorous derivation commensurate with PRD standards. The repeated inclusion of run-status prose and “this volume” references is unacceptable. While parts of the perturbation-transparency statement are likely correct in spirit, the present paper does not meet the methodological rigor and self-contained standards required for PRD. A substantially rewritten, self-contained manuscript with complete derivations and without reliance on unpublished companions would be required before reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS

P1A-E11
- Location: Sec. II.C, Eq. (10); Appendix B; multiple places using ρΛ and Λ interchangeably
- Problem: In Eq. (10) the quantity defined is Λeff = Ξ MPl^2 + cω ω^2 (units of mass^2), while elsewhere the manuscript repeatedly treats ρΛ = Ξ MPl^4 (units of mass^4) without ever specifying the conversion convention (e.g., ρ = Λ MPl^2/8π in chosen units). This Λ↔ρ slippage underpins several numeric statements (Ξ bookkeeping, Ntot), but the paper never fixes a single normalization to relate Λ and ρ.
- Required fix: Choose and state a single convention relating Λ and ρ (e.g., reduced MPl units with ρ = Λ MPl^2/2). Then audit every instance where Ξ multiplies MPl^2 vs MPl^4 and correct all downstream formulas and numbers to be mutually consistent.

P1A-E12
- Location: Sec. II.A.2, Eq. (4); Sec. IV.A, Eq. (13)
- Problem: Two inequivalent normalizations for the torsion-induced four-fermion contact appear. Eq. (4) contains “−(3π GN/2) × (γ^2/(γ^2+1)) J5·J5” (with an undefined N) while Eq. (13) gives the standard “−(3/16) κ (J5·J5).” The symbol N is never defined; the two coefficients cannot both be correct simultaneously.
- Required fix: Remove or define N, provide a single derivation (or precise citation) of the four-fermion coefficient with Holst dependence, and ensure the same coefficient is used consistently throughout. If different conventions are being used, state the mapping explicitly.

P1A-E13
- Location: Fig. 1 (PTA box); Sec. X.G (text); Table IV
- Problem: Fig. 1 shows “PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)”, while the body states a new “real-KDE” value 2.567 ± 0.382 and claims this supersedes the earlier synthetic value. Table IV also lists 2.567 ± 0.382. The figure and caption are stale and inconsistent with the text and table.
- Required fix: Update Fig. 1 and its caption to the current value, or remove the PTA panel entirely unless the analysis is presented here or in a citable work. State explicitly which PTA posterior is used, and ensure a single number is used consistently across figure, text, and table.

P1A-E14
- Location: Sec. IV.D (Route 4), p. 10
- Problem: The stated tension between WMAP+Planck β = 0.342° ± 0.094° and ACT DR6 β = 0.215° ± 0.074° is described as “∼ 1.4σ.” The correct difference significance is |0.342 − 0.215|/sqrt(0.094^2 + 0.074^2) = 0.127/0.120 ≈ 1.06σ, not 1.4σ.
- Required fix: Correct the quoted σ-level (≈1.1σ) or remove the statement.

P1A-E15
- Location: Sec. IV.E (Closure summary), last paragraph
- Problem: The text says “The condensate mechanism … is therefore documented in Sec. X as a quantitative closure,” but Sec. X is the perturbation-transparency section; the condensate discussion is in Sec. IV.A. This is an internal cross-reference error.
- Required fix: Correct the section reference (to Sec. IV.A) or rephrase.

P1A-E16
- Location: Sec. II.C.1 (“Reheating thermal-reset barrier” paragraph)
- Problem: The rms scaling “⟨J5μ⟩T,rms ∼ √nψ/T1/2reh” is introduced without definition or derivation and is dimensionally opaque for a current density (mass^3): √n gives mass^1.5 and dividing by T1/2 gives mass^1, not mass^3. As written, dimensions do not match the axial current. This scaling is then used qualitatively to argue washout.
- Required fix: Provide a derivation with explicit operator normalization and thermal correlators showing the correct dimensional scaling (or remove the formula and keep only the qualitative washout statement with a quantitative Γ/H estimate).

P1A-E17
- Location: Sec. II.A.1, Eq. (1)
- Problem: The gravitational action is written with a single prefactor 1/(16πG) multiplying eeR, the Holst term, and also an explicit “+ (1/4) Tabc Tabc.” The text then says this T^2 term is a shorthand for the emergent four-fermion term after integrating out torsion. Including T^2 inside the starting action with the Einstein prefactor risks double counting unless the variational procedure is precisely defined. It is also nonstandard in the Holst+fermion formulation.
- Required fix: Remove the explicit T^2 term from the starting action and derive it by integrating out torsion, or provide a clear derivation demonstrating that no double counting occurs with this ansatz and that the overall normalization reproduces the standard Hehl–Datta coefficient.

P1A-E18
- Location: Sec. IX.A (Barrier 1), Eq. (18)
- Problem: The expression geff ∼ 1/(MPl p|t3|) ∼ H0/MPl introduces “p” and “t3” without definition. The conclusion geff ∼ H0/MPl is dimensionally sensible, but the intermediate formula is not defined.
- Required fix: Define all symbols, or remove the undefined intermediate expression and present a clean dimensional argument leading to geff ∼ H0/MPl.

P1A-E19
- Location: Sec. II.A.3 (Parameter Naturalness)
- Problem: “The parent black hole mass must exceed Mcrit ≈ 10−3 M⊙” is asserted with no derivation or citation and is used to argue naturalness.
- Required fix: Provide a reference or a short derivation for the quoted threshold, or remove the claim.

P1A-E20
- Location: Sec. XII (first bullet under “Surviving tests”); Sec. III.A
- Problem: The small-rotation EB relation CEBℓ ≈ 2β (CEEℓ − CBBℓ) is used without stating the small-angle assumption and without specifying the exact convention (whether CBBℓ is negligible at the level required). As later quantitative statements hinge on O(0.1°) rotations, the linear approximation should be explicitly stated and justified.
- Required fix: Add the small-β assumption and cite the standard linear-rotation formula; state whether CBBℓ is retained or neglected in your usage.

P1A-M7
- Location: Sec. II.A.2, Eq. (5)–(6)
- Problem: The object FIJ[K, R˚] is introduced without definition; the paper never specifies whether this is the curvature of the torsionful connection, a mixed tensor built from contorsion K and R˚, or something else. The subsequent component expression in Eq. (6) drops the K/R˚ dependence entirely.
- Required fix: Define FIJ[K, R˚] precisely and show how Eq. (5) reduces to Eq. (6). If Eq. (6) is a different ansatz, remove the ambiguous notation and present a single, fully defined operator.

P1A-M8
- Location: Sec. II.A.2, Eq. (7) and surrounding text
- Problem: The statement “motivating [(α/M) MPl] ∼ 10−2” is circular in context: later in the paper α/M is fixed to ∼10−21 GeV−1 by fitting βobs, which itself implies MPl (α/M) ∼ 10−2. No independent one-loop input is shown here to motivate this number.
- Required fix: Either provide an independent one-loop calculation (or a literature value) that yields [(α/M) MPl] ∼ 10−2 without using βobs, or label this value as a benchmark chosen for illustration and decouple it from claims that depend on an “estimate.”

P1A-M9
- Location: Sec. XIII (PTA discussion) vs Fig. 1
- Problem: Beyond the stale number in Fig. 1 (P1A-E13), the text compares a model “γ = 3.0” with a data posterior “2.567 ± 0.382,” but the null procedures (free-spectrum real-KDE vs earlier Gaussian-likelihood results) and priors are not described. Presenting the comparison as a σ-offset without clarifying the non-comparability of the posteriors is misleading.
- Required fix: Add an explicit qualifier that σ-level offsets from different PTA likelihoods are not directly comparable unless the same likelihood and priors are used, or remove the σ comparison.

P1A-m6
- Location: Table IV (Parameter summary)
- Problem: The symbol γ is used both for the Barbero–Immirzi parameter and (in the “Observational channel parameters” block) for the PTA spectral index. Reusing γ for unrelated quantities invites confusion.
- Required fix: Use distinct symbols (e.g., γBI for Barbero–Immirzi; γPTA or nGW for PTA spectral index) consistently in the table and text.

P1A-m7
- Location: Fig. 1 caption and panel text vs Sec. X.G
- Problem: Figure text includes “PTA γ = 3.0 v.s. data 3.20 ± 0.42,” while the body emphasizes that this synthetic number has been superseded by 2.567 ± 0.382. This is a figure/body mismatch (distinct from the stale-number issue above) that directly contradicts the narrative in Sec. X.G.
- Required fix: Harmonize figure and text to the same, current value, or remove the PTA panel.

P1A-m8
- Location: Sec. II.B, Eq. (9) narrative paragraph
- Problem: While the arithmetic for ρcrit/ρPl at γ = 0.2375 and 0.274 checks out, the text labels 0.27–0.41 ρPl as a “window used elsewhere in this paper” without a single consolidated footnote giving the exact numeric mapping (√3/(32π^2 γ^3)). A compact derivation would avert confusion about the scheme dependence.
- Required fix: Add a one-line derivation immediately below Eq. (9), showing ρcrit/ρPl = √3/(32π^2 γ^3), and indicate explicitly which numeric choice is used in any later bound.

P1A-n4
- Location: Throughout
- Problem: Overloaded and inconsistent notation for the Pontryagin density: R∧R̃, RR̃, Re(Γ), and “∗R R” all appear, sometimes in the same section.
- Required fix: Choose one notation, define it once (e.g., P ≡ (1/2) εμνρσ Rμνab Rρσab = ∂μ Kμ), and use it uniformly.

P1A-n5
- Location: Multiple
- Problem: Typographic inconsistencies remain beyond those previously flagged: e.g., “Jackiw–Pi gravitational Chern–Simons R∧R˜, parity-odd four-fermion partner with γBI/(γ2BI + 1) · 8πG coefficient” mixes spaced/unspaced γBI and “R∧R˜” vs “RR˜”.
- Required fix: Normalize symbols and spacing; adopt a consistent style for tildes and subscripts.

Explanation
These additional findings focus on issues my initial pass did not scrutinize closely enough: hard numerical cross-checks (e.g., 1.1σ, not 1.4σ), Λ-versus-ρ normalization slippage that affects multiple equations and claims, figure/body mismatches and stale numbers, undefined symbols and inconsistent normalizations in key operators, and a few dimensional/notation lapses that can confuse readers. Even if the broader scientific thrust remains qualitative, PRD expects these internal consistencies to be nailed down before publication.