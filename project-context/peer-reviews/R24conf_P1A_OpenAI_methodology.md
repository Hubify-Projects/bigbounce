# P1A R24conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.51.pdf` md5=2ab29d5b pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7177 chars)
**Wall time**: 362.0s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter” (24 pp.)

Scope of this review
- Journal standards: Physical Review D, methodology rigor. I assessed statistical and theoretical derivation chains, dimensional analysis, internal arithmetic consistency, figure/table integrity, and whether abstract/conclusions are supported by derivations in the main text.
- I read every page, equation, table, figure caption, and footnote visible in the submitted PDF. All findings refer to text that appears in the PDF.

Global assessment
The manuscript makes a primarily theoretical claim: a “channel-level closure” of four specific dark-energy routes in minimal Einstein–Cartan–Holst (ECH) gravity, and a “perturbation-transparency” theorem for canonical scalar matter. While the core transparency observation (vanishing of the Holst dual on a torsion-free connection via the algebraic Bianchi identity) is sound and important to state clearly, a large fraction of the manuscript’s quantitative content relies on (i) phenomenological ansätze that the authors explicitly acknowledge are not controlled EFT-level operators; (ii) amplitude comparisons built on ad hoc one-loop-inspired operators without a firm derivation; and (iii) load-bearing results deferred to multiple “companion papers in preparation / posted concurrently,” which are not available for peer verification at submission. There is also version-history language embedded in the body text, which is not acceptable in a PRD submission.

Below I list all concrete issues, with classification and required fixes.

ESSENTIAL issues (must be resolved before the paper can be considered for publication)

P1A-E1 (Page 2, footnote a; Page 16, Section X D/E footnotes)
Problem: Version-history and self-correction language appears inside the scientific narrative. Examples include:
- “Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion…”
- “An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density.”
PRD does not permit version-log prose in the main text.

Required fix: Remove all version-history comments from the main body and footnotes. If the authors wish to transparently document a corrected misidentification, add a brief “Note added” at the end with a neutral statement and a precise correction, or simply present the correct derivations without historical commentary.

P1A-E2 (Multiple pages: 5, 11–12, 18–21)
Problem: The manuscript relies substantively on unpublished “companion papers in preparation/posted concurrently” for core methodological claims and numerical values:
- ΛCDM+ΔNeff MCMC verification, NaMaster EB pipeline validation, and ALP parameter fitting (Paper I(b) [6]) support several quoted numbers (e.g., H0 = 67.68 ± 1.06, ΔNeff ≈ 0; β forecasts).
- SPHEREx fNL forecast and survey-level significance claims (Paper II [2]).
- Real-KDE PTA spectral-slope result (Paper III [46]).
- Galaxy chirality classifier methodology and null result (Paper IV [23]).
PRD requires that all load-bearing results be available for peer scrutiny, either within the present manuscript or in publicly accessible, citable sources (published or at least posted on arXiv with stable identifiers).

Required fix: Either (a) remove all claims and numbers that depend on unpublished companion work; or (b) supply the full methods and results in this manuscript; or (c) replace with citations to already posted arXiv versions containing the full methods and results. In particular, do not quote MCMC-derived cosmological parameters, EB pipeline validations, PTA reanalyses, or galaxy-spin significance numbers unless the underlying analysis is available and reproducible at submission.

P1A-E3 (Pages 6–7 Eq. (10); Pages 7, 21–22; Appendix B)
Problem: Inconsistent conventions and dimensional bookkeeping between Λ and ρΛ. The text alternates between Λeff = Ξ MPl^2 (dimension two) and ρΛ = Ξ MPl^4 (dimension four) using the same symbol Ξ. The relation ρΛ = Λ M̄Pl^2 (in units with c = ħ = 1) depends on whether one uses the reduced Planck mass M̄Pl = (8πG)−1/2 or the unreduced MPl = G−1/2.

Required fix: State explicit unit conventions at the outset (c = ħ = 1) and fix which Planck mass is used (reduced or unreduced). Provide the precise relation ρΛ = Λ M̄Pl^2 and ensure all appearances of Ξ are consistent with these definitions. Audit Eqs. (10), (24), Appendix B (B2), Table IV, and the associated prose so that every occurrence of Λ and ρΛ is dimensionally consistent.

P1A-E4 (Pages 16–17, Sec. X)
Problem: The central “perturbation-transparency result” is stated in a sketch form. While the Bianchi-identity argument that the Holst dual ϵμνρσ Rμνρσ(Γ̊) vanishes for torsion-free Γ̊ is correct, a PRD-level theorem requires a careful statement of assumptions and an explicit demonstration that the Holst sector gives zero contribution to (i) the background FRW equations, (ii) the quadratic action for scalar and tensor perturbations, and (iii) the cubic action relevant for the bispectrum, including boundary terms and gauge conditions.

Required fix: Provide a compact but explicit derivation (preferably as an appendix) showing the variation of the Holst term with respect to the tetrad/connection in the torsionless, canonical-scalar case and demonstrating the vanishing of contributions to second and third order in perturbations. Clearly list all assumptions (matter content, boundary terms, topology, absence of non-minimal couplings). Cite a standard reference when possible and isolate the novel part of the argument.

P1A-E5 (Page 5, Eq. (1) and surrounding text)
Problem: The action includes an explicit + (1/4) Tabc Tabc term and then later states that “The Tabc Tabc term in Eq. (1) is a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term.” Writing down Tabc Tabc at the starting point and also integrating out torsion risks double counting unless the logical order is made precise.

Required fix: Start from the standard Palatini-Holst action with minimally coupled fermions, derive the Cartan equation, then integrate out torsion to obtain the four-fermion interaction with its γ-dependent coefficient (as you already do in Eqs. (3)–(4)). Remove the bare Tabc Tabc term from the “fundamental” starting action unless you explicitly define the starting theory as Einstein–Cartan with a specific torsion-squared term and demonstrate that it exactly matches the integrated-out four-fermion form (including numerical coefficients). As currently written, this is ambiguous.

P1A-E6 (Pages 9–10, Sec. IV B, Eq. (14) and Eq. (15))
Problem: The Route-2 one-loop “parity-odd effective action” operator and amplitude estimate are introduced as an ansatz “not literally derived.” Yet the channel-level closure relies on its normalization and scaling. As written, Γone-loop ∝ (αem/4π) (H0/MPl) after various identifications; the dependence on the Nieh–Yan pseudoscalar and on J5μ is asserted rather than derived.

Required fix: Either (a) provide a derivation or a published citation that yields an operator of the form you use, with its normalization; or (b) convert the closure to a robust upper bound independent of the precise form, e.g., “any one-loop parity-odd coupling linear in ∂μ of a pseudoscalar and suppressed by one power of MPl is bounded by … leading to Δθ_one-loop/Δθ_obs ≲ 10−58.” Present a clean dimensional analysis with explicit steps, using defined conventions, so that the bound and its dependence on α/M and βobs can be independently checked.

P1A-E7 (Pages 8, 12, 19–20; Sec. III B, V, VI)
Problem: The paper presents a “confirmed null” for galaxy spin asymmetry and claims to refute a 3% signal. However, all classifier methodology, bias audits, and significance calculations are deferred to Paper IV “in preparation.” This is load-bearing if one of the observational “branches” used to close channels rests on this null.

Required fix: Either remove the galaxy spin result from the present paper, or include a concise but complete methods section (data selection, classifier architecture, calibration, bias tests, null estimators, counting statistics, sky coverage, look-elsewhere accounting) and the resulting numbers and uncertainties. At minimum, table the dipole amplitude with uncertainties and the test details. Without this, the result cannot be evaluated by the reader.

MAJOR issues (significant revision required)

P1A-M1 (Pages 6–7, Eq. (5)–(7); Appendix B)
Problem: The central parity-odd operator Seff ∝ (α/M) ε e e F has off-shell mass dimension +1. The authors acknowledge it is not a controlled dimension-4 EFT operator and treat all mappings to ρΛ as a phenomenological ansatz. Nonetheless, this operator permeates the paper (e.g., in defining Ξ and the Dinf bookkeeping).

Required fix: Move all use of the non-EFT operator and its derived scalings (including Dinf, Ntot ≈ 92, and “fine-tuning reduction”) to a clearly marked appendix, and remove them from the main logical chain used to “close” channels. In the main text, do not draw quantitative conclusions that rest on this operator beyond explicitly labeled heuristics.

P1A-M2 (Pages 6–7, Eq. (10) and surrounding text; Table IV)
Problem: Unit and mass-scale conventions are not consistently applied (MPl vs. M̄Pl). See also P1A-E3. This affects Eq. (10) (Λeff vs. ρΛ), Eq. (24), and the parameter table.

Required fix: Define M̄Pl unambiguously at the start, carry consistent powers in all formulas, and clean up the text so that relations like ρΛ = Ξ M̄Pl^4 are not mixed with Λeff = Ξ MPl^2 without clearly mapping between the two.

P1A-M3 (Pages 13–16, Sec. IX and Table II)
Problem: “13 logically-independent barriers” are presented. Several are qualitative or heuristic without proofs or citations sufficient for PRD-level claims of generality (e.g., Barrier 1 Mass-Coupling Lock Eq. (18), Barrier 5 Scale Separation, Barrier 6 Attractor-Sensitivity Dilemma, Barrier 9 Liouville Conservation, Barrier 10 UV→IR Specificity Dilemma, Barrier 11 Decoupling Universality).

Required fix: For each barrier that is used to close a mechanism class, either provide a precise statement and derivation/proof within stated assumptions, or downgrade the language from “barrier”/“closure” to “heuristic argument”/“concern,” and remove any claims of logical independence unless demonstrated. Include at least one worked example or counterexample to clarify scope.

P1A-M4 (Pages 10–11, Sec. IV D, Eq. (17))
Problem: The ALP birefringence rotation angle β formula and normalization are given with a −1/4 (α/M) θ F F̃ convention that is not gaγ and include a factor 1/2 “standard small-rotation result.” The overshoot conclusions (ρθ ≈ 6 ρΛ at mθ = H0) hinge on this normalization.

Required fix: Derive Eq. (17) explicitly from the Maxwell–Chern–Simons Lagrangian used here, showing the linearized E-mode to B-mode rotation relation and the factor 1/2. Provide a brief appendix with the equation of motion and the small-angle approximation. Clearly specify the conversion between your α/M and the canonical gaγ normalization. Re-check the overshoot numbers with this self-contained derivation.

P1A-M5 (Page 15, Sec. IX L, Eq. (20))
Problem: The “Vacuum Amplification Ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 is asserted without derivation. As written, it is not clear why the GW energy-density fraction scales as the square of the LQC critical-density ratio.

Required fix: Provide a derivation or a literature citation for this bound, with definitions of ΩGW and assumptions (e.g., fraction of energy in GWs at the bounce, transfer to today). Clarify that this is a bound on the total GW energy fraction at the bounce, not directly comparable to PTA-band spectral densities (you already note this, but the bound itself still needs justification).

P1A-M6 (Pages 12, 18–19; Sec. VII and XIII)
Problem: SPHEREx fNL forecast significance (3–5σ) is quoted repeatedly but deferred to a companion paper. Heinrich et al. (2024) is cited for σ(fNL) ≈ 0.7 in Fisher-ideal conditions, but the degradation chain to “3–5σ realistic” depends on choices and systematics.

Required fix: Either (a) remove the numerical 3–5σ claim here and cite Heinrich et al. alone, or (b) include a concise, self-contained forecast sufficient for peer evaluation (assumed survey specs, tracer populations, bias and shot-noise models, GR corrections, photo-z, template-overlap factors, and the resulting σ(fNL)). If left as a qualitative point, avoid quoting a numerical detection significance not supported within the paper.

P1A-M7 (Pages 6–7, Eq. (9) and text)
Problem: The paper extrapolates ρcrit from γSU(2) ≈ 0.274 to give ρcrit ≈ 0.27 ρPl, while acknowledging the canonical LQC value 0.41 ρPl is quoted at γ ≈ 0.2375. This is fine as an illustrative “scheme dependence” argument, but presently it reads as an internal extrapolation without citation for the explicit functional dependence on γ.

Required fix: Cite a standard LQC reference deriving ρcrit = 3/(8πG γ^2 Δ) with Δ = 4√3 π γ ℓP^2 and explicitly show how Eq. (9) follows, so the γ-dependence used to produce 0.27–0.41 ρPl is traceable.

P1A-M8 (Bibliography, multiple entries)
Problem: Several references appear to be placeholders for 2025–2026 preprints (e.g., [5], [41]–[45]) with no journal info, some with future arXiv IDs (e.g., “arXiv:2603.13924”). PRD requires that all citations be accurate at the time of submission.

Required fix: Verify that all cited works exist and have correct arXiv identifiers and metadata. If a work is not yet public, remove the citation and any dependent claim.

P1A-M9 (Figures 1, 3, 4, 5, 6)
Problem: The narrative quotes numbers from figures (e.g., ω/H bound; forecast significance curves) but the figures as printed need fully labeled axes (including units), legends, and, where applicable, error bars. For a methods paper, figures must be quantitatively interpretable without ambiguity.

Required fix: Ensure every figure has labeled axes with units, legends, and captions that specify data sources and assumptions. If curves are schematic, say so explicitly in the captions. Remove any “burned-in” annotations that quote numbers not derived in the text.

MINOR issues (address but not blocking)

P1A-m1 (Pages 2 and 16)
Problem: Holst-vs-Pontryagin clarification is good, but the repeated self-referential corrections distract from the main argument.

Required fix: Condense to a single, clear statement distinguishing the one-curvature Holst dual contraction (vanishing by algebraic Bianchi on Γ̊) from the two-curvature Pontryagin density. Remove all historical commentary (see P1A-E1).

P1A-m2 (Global)
Problem: Notation inconsistency: ε and ϵ used for Levi-Civita; ε also used for equation-of-state-related parameters (quasi-dust “ε-correction”).

Required fix: Use distinct symbols (e.g., ϵ for Levi-Civita tensor density, ε for slow-roll/perturbation parameter) and define them once in a notation box or at first use.

P1A-m3 (Page 8, Eq. (12))
Problem: The EB small-angle formula is quoted but not used for any calculation in this paper.

Required fix: Either remove Eq. (12) or keep it as a brief reminder with a sentence explaining that all β constraints quoted come from literature and not from any estimator developed here.

P1A-m4 (Pages 6–7, Eq. (10))
Problem: The term cω ω^2 is introduced without a defined coefficient or units.

Required fix: Either supply the expression and unit normalization of cω and show explicitly that the term is negligible given (ω/H)0 < 5×10−11 (quantify the resulting ρ contribution vs. ρΛ), or remove cω entirely to avoid clutter.

P1A-m5 (Page 21, “9σ detection” wording)
Problem: The discussion of LiteBIRD β sensitivity mixes two different null hypotheses (“β = 0” vs. “difference from current central value”). Although the authors ultimately state they are not directly comparable, the earlier “∼ 9σ” phrasing is easy to misread as a forecast of discrimination power.

Required fix: Keep only the qualified statement already present in XV (difference vs. WMAP+Planck central is ~0.73σ with σ(β)=0.03°). Remove the free-standing “∼ 9σ” language or fence it clearly as power to test β = 0 only.

NIT (cosmetic)

P1A-n1 (Global)
Problem: Occasional colloquialisms (“baby universe,” “does no work on the cosmological constant problem”).

Required fix: Replace with formal phrasing (“daughter universe,” “does not alleviate the cosmological constant problem”).

P1A-n2 (Global)
Problem: Redundant disclaimers (“not a distinctive ECH prediction”) recur many times.

Required fix: State once crisply and remove repetitive instances.

P1A-n3 (Global)
Problem: Ensure hyphenation and broken words introduced by PDF extraction are not in the typeset manuscript (e.g., “de-couples,” line breaks in words). Likely typesetting, but confirm.

Audit of quoted scalars and ratios
- DESI BAO preference for dynamical DE: cited as 3.1–4.2σ. I cannot verify within this paper; ensure the citation [9,10] supports those exact numbers.
- LQC ρcrit window: Using ρcrit/ρPl = √3/(32π^2 γ^3), γ = 0.2375 → 0.41; γ = 0.274 → 0.27. Correct.
- ω/H bound: (ω/H)0 < 5×10−11 → ω^2/H^2 < 2.5×10−21; text notes “≲10−20”: please tighten to the precise square if quoting both.
- α/M normalization: adopting 10−21 GeV−1 and MPl ≈ 10^19 GeV gives [(α/M) MPl] ≈ 10−2. Correct.
- Route-2 suppression: αem/(4π) ≈ 5.8×10−4; H0/MPl ≈ 1.5×10−33 eV / 1.22×10^28 eV ≈ 1.2×10−61; with MPl (α/M) ≈ 10−2 and βobs ≈ 6×10−3 rad, Δθ_one-loop/Δθ_obs ≈ O(10−60). Numerically consistent.
- Route-4 ρθ from β: Using α/M = 10−21 GeV−1 = 10−30 eV−1; mθ = 1.5×10−33 eV; β = 6×10−3; ρθ = 2 m^2 β^2 /(α/M)^2 ≈ 1.6×10−10 eV^4. Observed ρΛ ≈ (2.3 meV)^4 ≈ 2.8×10−11 eV^4 → ratio ~5.7. Correct.
- ΩGW ceiling: square of (0.27–0.41) equals 0.073–0.168. Arithmetic consistent; derivation missing (see MAJOR).

Length
The manuscript is long (24 pages) relative to the core methodological contribution (the perturbation-transparency result and amplitude-level route closures). After removing version-history text and non-self-contained companion-paper dependencies, and consolidating heuristic material into an appendix, the paper could be reduced to ~16–18 pages without loss.

## Summary recommendation
MAJOR REVISIONS

The central perturbation-transparency observation is sound and could merit publication if presented with a rigorous, self-contained derivation. However, the manuscript, as submitted, relies on unpublished companion papers for multiple load-bearing results, includes version-history language in the body, uses a non-EFT operator with acknowledged dimensional mismatch in central arguments, and presents several “barriers” as general theorems without adequate proofs. Substantial restructuring is required: remove or fully include the dependent analyses, standardize conventions, provide rigorous derivations for the key claims (especially the transparency theorem and the one-loop closure bound), and eliminate all version-log prose. If these essential and major issues are addressed, a concise, rigorous PRD-level paper may be feasible.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A — ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

ESSENTIAL (new)

P1A-E8 (Pages 10–11, Sec. IV D: ACT vs WMAP+Planck consistency)
Problem: The text states the ACT DR6 birefringence β = 0.215° ± 0.074° is “consistent within ∼1.4σ” with WMAP+Planck β = 0.342° ± 0.094°. Recomputing the difference significance:
- |Δβ| = 0.127°
- σΔ = sqrt(0.094^2 + 0.074^2) = 0.120°
- |Δβ|/σΔ ≈ 1.06σ, not 1.4σ.
Required fix: Correct the quoted consistency to ≈1.06σ (or 1.1σ), or show how 1.4σ is obtained under a different, stated convention.

P1A-E9 (Pages 7, 18, 20: e-fold gap inconsistency)
Problem: The manuscript repeatedly argues that the dark-energy dilution requires Ntot ≈ 92 e-folds, while a matter-bounce signal would be erased for Ntot ≳ 60. Elsewhere it then says “the surplus required to close the gap is ∼ 14 e-folds,” which contradicts the 32 e-fold differential (92 − 60 = 32).
Required fix: Harmonize the numbers. If 32 e-folds is the correct differential, remove “∼14” everywhere and state 32 e-folds with a clear derivation. If 14 e-folds is intended under some alternative threshold, state and justify it explicitly.

P1A-E10 (Pages 6–7 and Fig. 3: rotation bound normalization)
Problem: The figure annotation and body text mix bounds on ω/H and ω^2/H^2. Saadeh et al. give (ω/H)0 < 5×10−11 → (ω^2/H^2)0 < 2.5×10−21. The figure’s burned-in “< 10−20” and the body’s “≲10−22 ρΛ level” are inconsistent and depend on an undefined coefficient cω in Λeff = cω ω^2.
Required fix: Provide the explicit expression for the rotation-induced contribution (with cω, units, and how it maps to ρ units), and correct the numerical bounds. Ensure the figure annotation matches the text.

MAJOR (new)

P1A-M10 (Pages 9–10, Eq. (14)–(15): identification ∂μϑNY ∼ H0)
Problem: The bound for the Route-2 one-loop term takes ∂μϑNY ∼ H0 without derivation. This choice sets the overall amplitude in Eq. (15).
Required fix: Justify this identification from the dynamics (e.g., show ϑNY is a slowly varying field whose time derivative is H0-scale today), or recast the closure as a bound that remains valid for any |∂μϑNY| ≤ ΛIR with stated ΛIR. Provide a reference or a short derivation.

P1A-M11 (Page 14, Fig. 5 caption and graphic: “115 orders of magnitude improvement”)
Problem: The graphic suggests a 115-order improvement in fine-tuning for the spin–torsion route, which conflicts with the main text’s repeated statement that the framework only reparameterizes fine-tuning (does not solve the CC problem).
Required fix: Remove the “115 orders” phrase or clearly relabel the panel as “reparameterized sensitivity (not a solution)” with an explicit caveat in the caption. Ensure consistency with the narrative.

P1A-M12 (Pages 7–8, “Reheating thermal-reset barrier” paragraph)
Problem: The r.m.s. scaling for the post-reheating axial current, ⟨J5μ⟩T,rms ∼ √nψ/T1/2reh, is dimensionally unclear (J5 has energy^3 units in natural units; √n/T1/2 has mismatched units).
Required fix: Provide a correct kinetic-theory estimate (e.g., axial susceptibility and fluctuation-dissipation relation with dimensions carried through) or cite a source. Otherwise, remove the formula and state the qualitative washout argument without dimensional claims.

P1A-M13 (Page 13, Barrier 1 Eq. (18): undefined t3 and dimensions)
Problem: geff ∼ 1/(MPl√|t3|) ∼ H0/MPl introduces t3 without definition and with suspect dimensions. The right-hand equality presumes √|t3| ∼ 1/H0.
Required fix: Define t3, state its mass dimension, and show the equality to H0/MPl. If this is a scaling ansatz, label it as such and avoid using it to close a mechanism class without a derivation.

P1A-M14 (Pages 6–7, Eq. (5)–(6): ambiguous FIJ[K, R̊])
Problem: Seff uses FIJ[K, R̊] and then drops explicit K-dependence in components. FIJ is not defined (is it the curvature of which connection?).
Required fix: Define FIJ precisely (curvature of the full connection, or a specific functional of contorsion and the Levi-Civita curvature). If K is neglected in components, explain why and under what assumption.

MINOR (new)

P1A-m6 (Page 16, Sec. X B.5 vs earlier steps)
Problem: After arguing the Holst dual vanishes identically on Γ̊ by the algebraic Bianchi identity, Step 5 says “A total derivative contributes nothing...”. This mixes two logically distinct statements (identical vanishing vs total-derivative vanishing).
Required fix: Keep one route. If using the Bianchi-identity pointwise vanishing, delete the “total derivative” sentence or clearly separate the Nieh–Yan boundary term discussion (and specify boundary conditions).

P1A-m7 (Page 6, 3. Parameter Naturalness)
Problem: “Required dilution of inherited rotation is naturally achieved through ∼50 e-folds of inflation” appears alongside a separate DE argument requiring Ntot ≈ 92. Without clarification, readers may conflate the targets.
Required fix: Add a clause: “This statement applies only to rotational dilution; it is unrelated to the separate Ntot ≈ 92 requirement from the dark-energy scaling ansatz.”

P1A-m8 (Page 8, Eq. (12) discussion)
Problem: The approximation CEBℓ ≈ 2β(CEEℓ − CBBℓ) is shown, while the text stresses that CBB is not neglected in published estimators. As printed, the equation is an approximation used only illustratively.
Required fix: Add “This is the small-angle, uniform-rotation approximation; all β values quoted here come from the literature using full estimators.”

P1A-m9 (Pages 10–11, Sec. IV D: degree–radian mixing)
Problem: β is quoted in degrees and then in radians in the same paragraph. The conversion 0.342° ≈ 5.97×10−3 rad is used but not shown.
Required fix: Standardize units in each paragraph or show the conversion once to prevent confusion.

P1A-m10 (Page 6–7, Eq. (7) and narrative)
Problem: Eq. (7) introduces g^2/(32π^2) and later the narrative substitutes αem/(4π) without defining g or the mapping.
Required fix: Define g (which coupling? electromagnetic?) and be consistent. If αem is intended, rewrite Eq. (7) accordingly and drop g.

P1A-m11 (Page 22, Table IV: “γ scheme range ∼ 0.020”)
Problem: The “range” can be misread as an error bar.
Required fix: Label the column explicitly as “scheme spread (not an uncertainty)” or move this comment to a note beneath the table.

P1A-m12 (Appendix B vs main: ρbounceΛ notation)
Problem: ρbounceΛ appears first in Appendix B without a prior definition in the main text.
Required fix: Define ρbounceΛ the first time it is used and keep a consistent symbol thereafter.

P1A-m13 (Page 16, Eq. (21): tensor-mode conventions)
Problem: The Fourier convention and normalization of hij are not stated; the cosmic-time form adds (k^2/a^2) without an explicit mapping from the conformal-time equation.
Required fix: Add a one-sentence note on Fourier conventions and the normalization of tensor modes to avoid ambiguity.

NO OTHER NEW DISCREPANCIES WERE FOUND in the remaining A–J classes beyond those already reported in my initial review. The items above represent newly identified arithmetic mismatches, figure-text inconsistencies, undefined/ambiguous quantities, and additional places where dimensional or procedural rigor should be strengthened for PRD standards.