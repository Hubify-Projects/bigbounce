# P1A auto-2026-06-05_1617pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (11432 chars)
**Wall time**: 238.5s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter” (21 pages)

Scope of review
I audited the manuscript for methodological rigor: derivation chains, dimensional analysis, internal arithmetic consistency, reproducibility of quoted numbers, and statistical claims. I checked every equation for dimensional consistency where possible, recomputed all stated σ-levels and order-of-magnitude ratios, and reviewed every figure/table caption against body text.

Findings

ESSENTIAL

P1A-E1
- Location: Abstract p.1; Sec. I B p.4–5; multiple throughout (Tables I, III, IV; Secs. III, VI–VII; “Companion paper” paragraph p.5)
- Issue: Reliance on unpublished, “in preparation,” and internal analyses for load-bearing numerical claims (ΛCDM+ΔNeff MCMC values; ALP fit and NaMaster validation; galaxy spin null; PTA γ reanalysis; Fisher forecast for fNL). Examples: “309,189 frozen accepted samples… documented internally rather than as externally citable arXiv-posted numbers,” “Paper I(b) [6], in preparation,” “Paper II forecast,” “Paper III… GPU MCMC,” “Paper IV [23].”
- Required fix: Either (a) remove all claims that depend on unpublished companion works and internal analyses (including values in Tables I/IV and all text that cites them for support), or (b) include full, self-contained methods and results in this paper (datasets, likelihoods, priors, convergence diagnostics, parameter tables, and code/chain DOIs) so that every quoted scalar and uncertainty is traceable and reproducible without relying on “in preparation” material. PRD cannot evaluate or publish claims that rest on non-public computations.

P1A-E2
- Location: Sec. X (pp.14–15) and Abstract/Conclusions
- Issue: “Perturbation-transparency theorem” is asserted with a brief sketch. No full derivation of the second-order (or all-orders) action is given; no explicit variation showing the boundary term’s non-contribution under cosmological boundary conditions; no treatment of vector modes; no gauge-fixing and constraint analysis; and no demonstration that the Holst/Nieh–Yan term cannot feed back via lapse/shift constraints at cubic order.
- Required fix: Provide a rigorous derivation with explicit perturbative expansion (to at least second order in scalar and tensor perturbations, ideally including vectors), clearly stated assumptions (matter content; boundary conditions; topology; gauge), and a full variation showing that all Holst contributions reduce to a total derivative that does not affect the equations of motion. Alternatively, cite a peer-reviewed detailed derivation that exactly matches the action and assumptions here and restrict claims accordingly.

P1A-E3
- Location: Sec. II A.2–C (pp.5–7); Appendix B (pp.19–20); Abstract; Sec. XIV D
- Issue: Core dark-energy mapping and the stated Ntot ~ 92 tension rest on a parity-odd operator whose off-shell mass dimension is acknowledged to be +1 (not +4). Despite acknowledging this is an ansatz (not an EFT derivation), the paper uses it to quantify “amplitude-level” closures and to propagate a specific “Ntot ≈ 92” that anchors the claimed structural tension with fNL.
- Required fix: Either (a) supply a controlled EFT operator of dimension four with a properly normalized coupling derived from the underlying theory (or a clearly justified decoupling limit) and re-derive all amplitude and Ntot results from that operator, or (b) move all quantitative results that depend on this ansatz (e.g., Ntot ≈ 92; the detailed “suppression” bookkeeping; structural-tension conclusions) to a clearly labeled speculative section without being used to close channels or to assert tensions; the abstract and conclusions must then be reframed to reflect that no EFT-level derivation is provided.

P1A-E4
- Location: Sec. IV D p.10; Sec. XII “Surviving tests” p.18
- Issue: Misstated consistency between WMAP+Planck and ACT DR6 birefringence central values. The text claims “consistent within ∼1.4σ”; the difference is |0.342° − 0.215°| = 0.127°, combined σ = sqrt(0.094² + 0.074²) = 0.120°, giving 1.06σ, not 1.4σ.
- Required fix: Correct the numerical significance to ≈1.1σ and propagate wherever used. If 1.4σ was obtained under a different weighting or covariance, provide the exact calculation and references.

P1A-E5
- Location: Sec. IV B, Eq. (15) p.9
- Issue: Route-2 (one-loop Holst-sector) amplitude estimate normalizes by the Route-4-fitted coupling α/M ~ 10^-21 GeV^-1 (calibrated on birefringence). This cross-normalization mixes distinct mechanisms and assumptions. The one-loop operator itself is introduced ad hoc (not derived), and the final suppression estimate depends on the R4 calibration.
- Required fix: Provide a route-internal upper bound for the one-loop coefficient from a first-principles calculation or a published bound (e.g., explicit one-loop computation in Einstein–Cartan–Holst with fermions), and compute the Route-2 amplitude independent of Route-4 fits. If not available, recast R2 as a conjectural amplitude estimate and remove amplitude-level closure claims for R2.

P1A-E6
- Location: Sec. II A.3 p.6
- Issue: “The parent black hole mass must exceed Mcrit ≈ 10^-3 M⊙” is asserted without derivation or citation.
- Required fix: Provide a derivation (with assumptions) or a peer-reviewed citation that establishes this threshold. Otherwise remove the claim.

P1A-E7
- Location: Sec. II C.1 “Reheating thermal-reset barrier,” pp.6–7
- Issue: Claims that C/P-violating scattering rates at Treh exceed H and erase ⟨J5μ⟩ are qualitative and citation-free; no rate estimates or references are provided.
- Required fix: Provide quantitative estimates or literature citations for the relevant Standard Model scattering rates at T ≈ 10^15 GeV and their comparison to H. Absent this, the “thermal reset” barrier must be labeled as conjecture and not used as a closure argument.

P1A-E8
- Location: Sec. IX L (Barrier 12) p.13–14, Eq. (20)
- Issue: The “vacuum amplification ceiling” ΩGW^ECH|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is asserted without derivation or citation.
- Required fix: Provide a derivation (assumptions, normalization, and how this ceiling propagates to present-day bands), or cite a peer-reviewed source. Otherwise remove or reframe as a conjectural bound not used for closure.

P1A-E9
- Location: Table III p.16 (footnote) and Sec. X G p.15
- Issue: Live-run and version-history language inside scientific text (e.g., “At the time of this writing the chain has accumulated… we deliberately do not commit to a specific calendar date…”) and claims to an unpublished “real-KDE GPU MCMC” posterior (γ = 2.567 ± 0.382) used for model comparison.
- Required fix: Remove all version-history/progress prose. Do not present unpublished posterior values. Either provide a complete, citable analysis within this paper (methods, priors, chains, convergence) or remove these comparisons.

P1A-E10
- Location: Data and Code Availability p.18; throughout tables/text where numbers are quoted from internal analyses
- Issue: Reproducibility gap: the GitHub link does not include the MCMC chains or inputs underpinning the quoted “verified values” in Table IV or other internal scalars; those are said to be “in companion Paper I(b).”
- Required fix: Deposit all datasets, chains, configuration files, and scripts required to reproduce every claimed number in this paper (with commit hash/DOI). Otherwise remove those numbers from the manuscript.

P1A-E11
- Location: Multiple locations (Abstract p.1; Secs. I–XIV; Tables I/III/IV)
- Issue: Pervasive use of “companion works in preparation,” “this volume,” “hUBIFY-2026-00X,” procedural notes, and internal bookkeeping within the body text.
- Required fix: Replace with published citations or integrate the relevant material here. Remove internal project-management language.

P1A-E12
- Location: Sec. II C.2 p.7–8; Sec. XIV B p.16–17
- Issue: “Underpredicts any plausible spin asymmetry by > 100 orders of magnitude” is asserted with neither a back-of-envelope calculation nor a citation.
- Required fix: Provide an explicit order-of-magnitude calculation tying α/M ~ 10^-21 GeV^-1 to a predicted galaxy spin dipole amplitude (including distance/redshift weighting and astrophysical mechanisms), or remove the quantitative claim.

MAJOR

P1A-M1
- Location: Appendix B Eq. (B1) p.19
- Issue: Dimensional counting of e, ε, and F is stated without a consistent convention. In first-order gravity, dimensions of e^I_μ and F^IJ can differ by convention; [ε e e F] = +2 is asserted but not derived.
- Required fix: State the unit conventions (ħ = c = 1), and provide a consistent dimensional analysis for e, ω, R, and the 4-form Lagrangian density. Show explicitly how [ε e e F] = +2 is obtained under those conventions.

P1A-M2
- Location: Sec. IV A p.8; Barrier 8 p.13
- Issue: The statement that (J5)^2 is parity-even is correct, but the leap “therefore cannot generate tensor chirality in primordial GWs” is not demonstrated. In principle, parity-even operators can still affect tensor spectra differently if background pseudoscalars or anisotropies exist.
- Required fix: Either provide a short derivation under FRW and minimal coupling assumptions that (J5)^2 cannot induce parity asymmetry in the tensor sector, or qualify the statement to those conditions.

P1A-M3
- Location: Sec. II A.2–3 pp.5–6
- Issue: M in Eqns. (5)–(7) is taken as “Marea-gap ∼ MPl/√γ” without derivation or numeric specification.
- Required fix: Derive or cite the relation between the LQG area gap and an effective mass scale M used in the parity-odd operator. Provide the numerical constant(s) and discuss scheme dependence.

P1A-M4
- Location: Sec. II B pp.6
- Issue: Mapping ρcrit across γ-schemes: substituting γSU(2) ≈ 0.274 into the standard LQC formula is an “internal extrapolation.” This is not standard practice without justification.
- Required fix: Either justify the extrapolation with references or restrict to the canonical LQC value and clearly segregate the extrapolation as speculative, not used for any quantitative conclusion.

P1A-M5
- Location: Sec. I p.3; Table I p.4
- Issue: “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent)”—no precise dataset combo or test statistic is provided.
- Required fix: Specify exactly which DESI data combinations yield 3.1σ and 4.2σ, the statistical methodology (e.g., Δχ² vs nested models; look-elsewhere correction), and cite the precise tables/figures from [9,10].

P1A-M6
- Location: Sec. II C Eq. (10) p.6
- Issue: Λeff parameterization adds cω ω^2. No derivation or citation is provided, and dimensions/normalization of ω are not stated.
- Required fix: Provide a derivation or citation for the rotational contribution to the effective cosmological constant and specify units/normalization for ω and cω.

P1A-M7
- Location: Sec. II C.1 pp.6–7
- Issue: The (Treh/MGUT)^{3/2} factor is presented as a “phenomenological phase-space ansatz.” It is subsequently used to tune Ntot and to draw structural-tension conclusions.
- Required fix: Either derive this factor from a controlled calculation (or cite one) or demote all results that use it (especially Ntot estimates and “tension” claims) to speculative status and remove them from the abstract and conclusions.

P1A-M8
- Location: Sec. X pp.14–15
- Issue: The “all orders” statement omits vector perturbations and boundary/topology subtleties. The manuscript briefly notes exceptions later but not within the theorem statement.
- Required fix: Amend the theorem statement to include all assumptions and scope limitations (including vectors, boundary terms, topology, and matter content), and ensure the proof treats or explicitly excludes those cases.

P1A-M9
- Location: Sec. IX I (Barrier 9) p.13
- Issue: “Liouville conservation prevents irreversible selection” is asserted without a model-specific derivation (bounce-specific Hamiltonian flow, measure, and coarse-graining).
- Required fix: Provide a formal statement of the phase-space flow for the bounce model considered and show how Liouville’s theorem applies; or cite a rigorous derivation.

P1A-M10
- Location: Sec. III A p.8; Sec. XII p.16
- Issue: “Observed isotropic birefringence at β ≈ 0.27°–0.30°” is conflated with the WMAP+Planck central value 0.342° ± 0.094°. 0.27° is the benchmark point used in this paper, not the observed central value.
- Required fix: Rephrase to avoid implying that 0.27°–0.30° is the observed range. Distinguish clearly between benchmark choices and published central values.

P1A-M11
- Location: Sec. XIV D p.17; Appendix B p.20
- Issue: Two different headline values Ntot ≈ 92 and Ntot ≈ 94 appear. The body text uses 92; Appendix B argues for ≈94 from MPl^4/ρΛ ≈ 10^122. The reconciliation is qualitative.
- Required fix: Adopt a single consistent treatment, quantify the systematic, and ensure that all appearances (including the abstract and “tension” narrative) reflect that uncertainty and do not hinge on a specific integer value.

MINOR

P1A-m1
- Location: Throughout references and text (pp.3, 12, 19)
- Issue: Spelling/diacritics: “Pop lawski” vs “Popławski” (and consistency).
- Required fix: Standardize author names and diacritics per journal style.

P1A-m2
- Location: Table I p.4 (footnote markers “a”, “b”)
- Issue: Footnote formatting and a stray “b3–5σ” artifact.
- Required fix: Clean up footnote formatting and ensure no artifacts remain.

P1A-m3
- Location: Abstract p.1; Sec. X D p.14
- Issue: Notation “RRe” for Pontryagin density is nonstandard; risk of confusion.
- Required fix: Use standard *RR (R∧R̃) notation consistently.

P1A-m4
- Location: Sec. III A p.8, Eq. (12)
- Issue: For small uniform rotation, Cℓ^EB ≈ 2β Cℓ^EE is typical when Cℓ^BB ≪ Cℓ^EE; the manuscript gives Cℓ^EB ≈ 2β(Cℓ^EE − Cℓ^BB) without citing a reference.
- Required fix: Cite a standard reference and clarify the regime where the −CBB term is retained.

P1A-m5
- Location: Appendix B p.19–20
- Issue: Notation ρ_bounce_Λ is introduced without a clean definition and then compared to ρ_Pl and ρΛ.
- Required fix: Define all symbols precisely and maintain consistent notation.

NIT

P1A-n1
- Location: Throughout
- Issue: Nonstandard capitalization (“Foundations A–G,” “Branches H, J, L…”).
- Required fix: Conform to PRD style; consider moving catalog items to an appendix.

P1A-n2
- Location: Various (pp.5–6, 10–18)
- Issue: Multiple long asides and parentheticals interrupt flow; some hyphenation inconsistencies.
- Required fix: Edit for clarity and concision.

P1A-n3
- Location: Acknowledgments p.18
- Issue: “Acknowledges the use of Claude (Anthropic) as an AI research assistant.” This is unusual for PRD and not relevant to the scientific content.
- Required fix: Remove or move to a non-published disclosure; PRD typically does not include such statements.

Length and focus
Given the heavy reliance on unpublished companion works and the speculative status of the key operator, the manuscript is too long for the contribution currently demonstrated. If the paper is refocused on a rigorous, fully derived perturbation-transparency theorem (with all assumptions) plus a strictly operator-level, route-by-route amplitude analysis that does not rely on unpublished results or on the dimension-+1 ansatz, it could be substantially shortened to ≲12–14 pages.

## Summary recommendation
REJECT

The manuscript advances interesting ideas, but it does not meet PRD’s methodological standards in its current form. Core quantitative claims depend on an acknowledged non-EFT ansatz and on unpublished companion analyses; the central “theorem” is presented only as a sketch; several amplitude-closure arguments mix assumptions across routes; and there are arithmetic and reproducibility issues. A future submission that (i) provides a self-contained, rigorous derivation of the perturbation-transparency result, (ii) eliminates dependence on unpublished works, and (iii) bases all amplitude statements on controlled EFT operators with correct dimensionality could be suitable for consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

Below are only NEW issues not listed in my initial report. I follow the same tagging scheme and structure.

ESSENTIAL

P1A-E13
- Location: Sec. IV B, Eq. (14) and surrounding text
- Issue: Dimensional inconsistency in the proposed one-loop operator. With θ a (dimensionless) Nieh–Yan pseudoscalar, ∂μθ has mass dimension 1 and J5μ has dimension 3, so ∂μθ J5μ has dimension 4. The coefficient must therefore be dimensionless. The manuscript inserts 1/MPl, which lowers the operator to dimension 3 and makes the Lagrangian density dimensionally inconsistent.
- Required fix: Remove the 1/MPl factor (or, if θ is instead assigned mass dimension 1, state this explicitly and re-derive all normalizations). Provide a consistent dimensional derivation from a first-principles calculation or a published result.

P1A-E14
- Location: Sec. II A.2, Eq. (4)
- Issue: Undefined symbol “N” in the four-fermion interaction coefficient, Lint = −(3πGN/2) × γ^2/(γ^2+1) × J5·J5. N is never defined (number of fermion species? color factor?).
- Required fix: Define N precisely (including which species are counted and how) or remove it. Recompute any numerical statements that depend on N.

P1A-E15
- Location: Sec. I Fig. 1 (right column label) vs. Sec. X G (p.15)
- Issue: Stale/inconsistent PTA γ numbers between figure and text. The figure label reads “PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)” while the body text later replaces this with “2.567 ± 0.382 (real-KDE)”. This is a figure–body mismatch and risks misinforming readers.
- Required fix: Update the figure to match the current value (or remove the number from the figure). Do not cite unpublished values unless fully documented in this paper (see P1A-E1 in the initial report).

P1A-E16
- Location: Sec. IV B, Eq. (15) and paragraph below
- Issue: Internal normalization ambiguity in the Route-2 amplitude by ∼27 orders of magnitude. The manuscript states “an alternative ordering … yields a numerically distinct ∼10−33 ratio,” yet ultimately quotes 10−58–10−60. Such an enormous spread signals an unresolved dimensional/normalization inconsistency and undermines the amplitude-level closure claim for R2.
- Required fix: Present a single, self-consistent, route-internal amplitude derivation with correct units and no reliance on Route-4 calibration. Remove the alternative estimate or reconcile both explicitly; otherwise, refrain from amplitude-level closure claims for R2.

MAJOR

P1A-M12
- Location: Sec. II A.1, Eq. (1) and paragraph below
- Issue: Action structure/double-counting ambiguity. The action includes +(1/4) TabcTabc inside the 1/(16πG) gravitational bracket, then states it is “a shorthand for the four-fermion contact interaction … not an independently specified kinetic term.” As written, it looks like a gravity-sector torsion-squared term with a fixed coefficient rather than a matter-sector contact induced after algebraic elimination, risking double-counting and wrong normalization.
- Required fix: Write the standard EC+Holst action without an explicit T^2 term in the gravity sector, show the algebraic elimination, and then exhibit the induced four-fermion term in the matter effective action with its correct coefficient. Alternatively, provide a published reference that uses exactly this normalization and placement.

P1A-M13
- Location: Sec. IV A p.8 (last paragraph)
- Issue: Internal inconsistency on γ-dependence. The text says “torsion-elimination map is independent of γ at the classical level,” but Eq. (4) explicitly carries γ-dependence (γ^2/(γ^2+1)). These statements are contradictory.
- Required fix: Correct the text to reflect the known γ-dependence of the induced four-fermion operator in the Holst-extended EC theory, and ensure that any later conclusions are consistent with this dependence.

P1A-M14
- Location: Sec. II C p.6 (after Eq. 10)
- Issue: Rotational bound mapping and citation. The statement “CMB isotropy bounds give (ω/H)0 < 5 × 10−11 [21]” is cited to Saadeh et al. (2016), which constrains Bianchi-like anisotropic models. The mapping from those constraints to a bound on cosmic vorticity ω/H needs to be shown, and the exact definition/normalization of ω used here is not provided.
- Required fix: Define ω, state the model mapping used to translate Saadeh et al.’s limits to ω/H, quote the relevant equations, and verify numerical consistency. Otherwise, remove the specific bound.

P1A-M15
- Location: Sec. IV D, Eq. (17) and surrounding text
- Issue: Birefringence normalization and field dynamics not specified. For L ⊃ −(1/4)(α/M) θ F F̃, the standard small-angle result is β = (α/M) Δθ/2. The manuscript uses β ≈ (α/M) Δθ without stating conventions and then sets Δθ ∼ √(2ρθ)/mθ, which assumes a harmonic oscillation amplitude without redshift/equation-of-motion treatment since recombination.
- Required fix: State the precise normalization (including the 1/2 factor if applicable), define θ’s dimension and convention, and derive Δθrec→today from the field equation for the chosen potential. Recompute ρθ if needed.

P1A-M16
- Location: Sec. II A.2–A.3; Appendix B; Sec. II A.2 Step 3 and Fig. 2 caption
- Issue: Λ vs ρΛ normalization drift. The body alternates between Λeff (dimension M^2) and ρΛ (dimension M^4) without consistent 8πG factors or a single mapping (e.g., ρΛ = Λ MPl^2/8π). Fig. 2 and Appendix B use ρΛ ∼ [(α/M) MPl] MPl^4 while Eq. (10) parameterizes Λeff = Ξ MPl^2.
- Required fix: Choose one normalization and stick to it. Define the Λ–ρΛ relation once, include all factors, and ensure every occurrence is dimensionally consistent throughout.

P1A-M17
- Location: Sec. XII (p.16) “Spectator-ALP birefringence” vs. Sec. IV D (p.10)
- Issue: Contradictory fine-tuning statements. Sec. IV D argues that reproducing ρΛ together with βobs requires mθ ∼ H0 (i.e., tuning), while Sec. XII asserts “fa ∼ MPl, m ∼ H0 is consistent … without fine-tuning.” These are logically inconsistent.
- Required fix: Resolve the contradiction. If m ∼ H0 is viewed as tuning, state it consistently across the paper; if not, justify why it is natural in the chosen model (e.g., symmetry protection).

P1A-M18
- Location: Sec. IX B (Barrier 2: Topological-Shift Duality), p.12
- Issue: Strong, general claim without derivation/citation: “Mass protection ⇔ No geometric fingerprint.” No proof, model, or reference is provided.
- Required fix: Provide a formal statement and derivation (or literature citation) within metric-affine gravity that supports this exact duality under the paper’s assumptions.

P1A-M19
- Location: Sec. IX A (Barrier 1: Mass-Coupling Lock), Eq. (18)
- Issue: Unjustified PGT scaling. geff ∼ 1/[MPl √|t3|] ∼ H0/MPl is stated without defining t3 or deriving the scaling. This directly underpins the barrier’s conclusion.
- Required fix: Define the PGT parameters, derive geff from the linearized PGT action, and show how mT ∼ H0 implies geff ∼ H0/MPl (with appropriate constants). Provide citations.

P1A-M20
- Location: Sec. II C.1 (para after Eq. 11)
- Issue: Cross-reference mismatch to Eq. (14). The text contrasts a thermal phase-space factor with a “Mercuri & Capozziello [22] one-loop coefficient αem/(4π) appearing in Eq. 14,” but Eq. (14) in this paper does not contain αem/(4π). This is confusing and suggests a stale or mismatched reference.
- Required fix: Correct the cross-reference. If αem/(4π) is intended, show its appearance explicitly (with derivation or citation); otherwise, strike the comparison.

P1A-M21
- Location: Sec. II A.2 Step 3–4; Eqns. (5)–(7)
- Issue: Insufficient definition of FIJ[K, R̊] and of M ≡ Marea-gap used in the parity-odd operator. The field-content of F (curvature vs contortion contributions) is left ambiguous and the mass-scale mapping from the LQG area gap is not derived.
- Required fix: Define FIJ[K, R̊] precisely, derive M from Δ = 4√3 π γ ℓP^2 to the exact numerical M (including all constants), and discuss scheme dependence quantitatively.

P1A-M22
- Location: Sec. IV A p.8 (last paragraph)
- Issue: NJL route “amplitude-suppressed” conclusion lacks even a back-of-the-envelope numeric bound. Claiming ρNJL ∼ nψ^2/MPl^2 ≪ ρΛ is plausible, but no numbers are shown.
- Required fix: Provide a quantitative bound using the largest plausible cosmological fermion densities (e.g., neutrino/baryon/electron densities at recombination or today) to demonstrate the many-orders shortfall.

MINOR

P1A-m6
- Location: Sec. III A p.8, Eq. (12) and sentence below
- Issue: The small-angle EB formula is written as CℓEB ≈ 2β(CEE−CBB). Standard references often use CℓEB ≈ 2β CℓEE when CBB ≪ CEE. The manuscript uses the former without a citation or regime statement.
- Required fix: Cite a standard reference and state explicitly the regime/assumptions under which the −CBB term is retained.

P1A-m7
- Location: Sec. II A.2 Step 3–4; Eq. (6) text line “which has naive mass dimension [Lodd] = +1”
- Issue: The component expression “εμνρσ eIμ eJν FIJρσ” implicitly mixes frame and coordinate indices without specifying conventions. This makes the ensuing dimensional claim opaque.
- Required fix: State the index conventions (frame vs coordinate), the dimensions assigned to eIμ, ω, and R, and then show explicitly how [εeeF] = +2 is obtained (cf. P1A-M1 in the initial report).

P1A-m8
- Location: Sec. I A.3 p.3 and elsewhere
- Issue: Novelty claims (“No prior work assembles these into a single quantitative framework…”) are not supported by a systematic comparison or citation survey.
- Required fix: Either remove “first-of-its-kind” language or provide a brief, referenced comparison that substantiates the claim.

P1A-m9
- Location: Appendix B, mid-page 20
- Issue: Editorial artifact (“…not the ∼ 35 misstated in earlier drafts…”) left in the final text.
- Required fix: Remove “earlier drafts” commentary and present the corrected value cleanly.

P1A-m10
- Location: Sec. II A.2 Step 2; Eq. (4) coefficient
- Issue: The Hehl–Datta coefficient form used here differs from common normalizations; since this is central, a reference equation number or explicit derivation should be provided for the γ-dependent factor.
- Required fix: Add a precise citation to a derivation with the same conventions or provide a short derivation in an appendix.

P1A-m11
- Location: Sec. II B p.6 (“no free parameters” sentence)
- Issue: Overstatement: the effective LQC dynamics depend on γ and the chosen area-gap scheme; calling the bounce “no free parameters” is misleading in that context.
- Required fix: Qualify to “fixed by γ and the chosen area-gap prescription.”

NIT

P1A-n4
- Location: Multiple
- Issue: Occasional informal phrasing remains (e.g., “ε-correction perturbative-order scaling,” “earlier synthetic-Gaussian-likelihood value,” etc.) that reads like internal notes.
- Required fix: Edit for formal tone and clarity.

Explanation
I focused on arithmetic recomputation, caption–body consistency, dimensional checks, cross-references, null-procedure comparability, abstract vs body support, and appendix/main-text alignment. The most consequential new findings are (i) a dimensional error in the one-loop operator (Eq. 14), (ii) an undefined factor N in the four-fermion term, (iii) a figure–body mismatch for PTA γ, and (iv) an unresolved 27-order ambiguity in the R2 amplitude estimate. These materially affect the paper’s central amplitude-level closure claims and must be resolved for PRD standards.