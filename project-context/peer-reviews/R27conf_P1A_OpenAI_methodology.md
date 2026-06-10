# P1A R27conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.55.pdf` md5=5dc099dc pages=25
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7522 chars)
**Wall time**: 324.4s

---

Referee report for PRD (methodology review)
Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes …”
Pages: 25

Scope of review
I audited the full text (equations, figures, tables, captions, footnotes, and references) for methodological rigor: dimensional consistency, derivation chains, numerical arithmetic, uncertainty claims, comparability of significances, and reliance on external/non-public analyses. Below are all issues found, each tagged with severity and a concrete required fix.

Findings

ESSENTIAL

P1A-E1 (Abstract, p.1; Sec. I B “Companion paper”, p.5; Table I, p.4; Secs. III–VII, IX, XIII–XV; multiple locations)
Problem: The manuscript repeatedly relies on quantitative claims and parameter values from “companion work in preparation” [6] (ΛCDM+ΔNeff MCMC posteriors, NaMaster validation, ALP parameter fits, chain lengths, convergence status), and even includes specific values (e.g., H0 = 67.68 ± 1.06, ΔNeff ≈ 0, number of accepted samples), while explicitly stating these are not yet publicly citable.
Required fix: Either (a) remove all quantitative results that depend on [6] and any claims that cannot be supported within this paper alone, or (b) replace [6] with a publicly available, arXiv-posted companion containing full methods and results, and summarize the necessary methods here (likelihoods, priors, sampler settings, convergence diagnostics). Do not include “internal” or “frozen” unpublished results.

P1A-E2 (Page 2 footnote under Contents; Sec. X footnote p.18; multiple)
Problem: Version-history language appears inside the paper: “Earlier versions of this manuscript erroneously…”, “An earlier version of this manuscript misidentified…”.
Required fix: Remove all version-history/revision-log statements from the body/footnotes. Replace with neutral, timeless statements and a proper citation or a short erratum-style clarification if genuinely needed.

P1A-E3 (Table I, p.4; Fig. 4 caption p.13; Sec. VII p.13; Sec. XIII p.20)
Problem: The paper juxtaposes multiple σ-significance claims from different null hypotheses and methodologies (SPHEREx fNL 3–5σ forecast; LiteBIRD β ≈ 9σ against β = 0) without explicitly stating that these significances are not directly comparable. The text also mixes forecasted σ values (from external Fisher forecasts) with measured σ values (WMAP+Planck/ACT) in the same contexts.
Required fix: At every place where different-significance numbers are shown side-by-side, add an explicit “not directly comparable” qualifier that the hypotheses, estimators, data, and pipelines differ. For SPHEREx, either provide the full in-paper forecast methodology or relegate the numbers to a properly cited, public companion and state clearly that no new forecast is performed here.

P1A-E4 (Sec. IV.B, Eq. (15), pp.10–11)
Problem: In the one-loop Route-2 closure, the dimensionless birefringence ratio ∆θone-loop/∆θobs is given with an “alternative ordering” note producing a numerically different estimate (~10−33 vs ~10−60). This signals an unresolved dimensional accounting/insertion of MPl factors.
Required fix: Present a single, unambiguous, dimensionally consistent derivation of ∆θone-loop/∆θobs with all steps shown. Remove the “alternative ordering” remark. State the mass dimension for ϑNY and J5 explicitly, justify the MPl placement, and show the numerical evaluation unambiguously to the stated order of magnitude.

P1A-E5 (Sec. IV.B, Eq. (14), p.10)
Problem: The operator Γone-loop ∝ (1/MPl) ∫ √−g ∂μϑNY J5μ is introduced without stating the mass dimension of ϑNY. Dimensional consistency is therefore unclear.
Required fix: Specify the field dimension of ϑNY and verify in-text that the Lagrangian density has mass-dimension +4. If ϑNY is dimension-1 (axion-like), then (∂ϑNY) has dim 2 and (1/MPl) ensures a dim-4 operator; state this explicitly and add a supporting reference or short derivation.

P1A-E6 (Sec. I B p.5; Table I p.4; Sec. XIII p.20; Table III p.19)
Problem: The manuscript presents unconverged or pipeline-external MCMC details (chain sizes, R̂, “do not commit to a specific calendar date for convergence”) and uses them to support conclusions (e.g., H0, ΔNeff) despite acknowledging these analyses are not part of the present paper.
Required fix: Remove all in-progress chain details and any use of unconverged chains. Either present a self-contained MCMC analysis here (data, likelihoods, priors, sampler, convergence, posteriors) or delete all quantitative claims derived from those runs.

P1A-E7 (Figs. 4 and 6, pp.13 and 20)
Problem: “Detection significance” time-series curves are shown without in-paper methodology or reproducible inputs; the text admits that no independent SPHEREx Fisher computation is done here.
Required fix: Either provide full forecasting methodology and inputs (survey model, redshift distributions, bias models, covariance, templates, systematics treatment) enabling reproduction, or remove these figures and replace with qualitative statements and proper citations to external works supplying such curves.

P1A-E8 (Table III footnotes and text, p.19)
Problem: The paper includes details of a non-converged “DESI DR2 w0wa (new)” chain and internal compute logistics (“OMP threads tuned…”, etc.). This is not appropriate in a journal article and is irrelevant to the present paper’s conclusions.
Required fix: Remove these operational details entirely. If DESI w0wa results are needed methodologically, present a complete, converged analysis or defer such claims to a public, fully described companion paper.

MAJOR

P1A-M1 (Sec. IV.D, pp.11–12; Sec. II A 2 pp.6–7)
Problem: The stated benchmark α/M ≈ 10−21 GeV−1 is used repeatedly but not explicitly derived in this paper from βobs; the text relies on an ALP mapping and a basis-conversion footnote without a concrete numerical extraction from data.
Required fix: Provide a clear, single-step numerical derivation showing how α/M ≈ 10−21 GeV−1 follows from βobs and the assumed Δθ (or the assumed mθ ~ H0 and energy density). Alternatively, state that α/M is fixed by external fits and provide a precise reference (with equations and inputs) enabling readers to reproduce the number.

P1A-M2 (Sec. II C 1 “Reheating thermal-reset barrier”, pp.7–8)
Problem: The claim that C/P-violating scattering rates at Treh exceed the Hubble rate (and therefore erase ⟨J5μ⟩) is asserted without any quantitative rate vs. H estimate or citation.
Required fix: Provide an order-of-magnitude computation or authoritative citation for the relevant axial-randomization processes at Treh (cross sections, densities) demonstrating ΓCP/H ≫ 1. Clarify the assumptions (species, couplings) and the robustness of the erasure argument.

P1A-M3 (Table II Barrier 12; Sec. IX.L, p.15)
Problem: The bounce-era gravitational-wave energy-density ceiling ΩGW|bounce ≲ (ρcrit/ρPl)2 ≃ 0.07–0.17 is introduced as an “ansatz” with no derivation but used as a barrier.
Required fix: Either (a) provide a supporting derivation or reference showing why the GW energy fraction should scale quadratically with ρcrit/ρPl and how it constrains present observations, or (b) remove Barrier 12 as an actionable constraint and rephrase it as a speculative ceiling with no bearing on conclusions.

P1A-M4 (Sec. IV.D, p.12 and footnote)
Problem: The discussion of the ALP coupling basis-conversion (gaγ vs α/M) acknowledges a ∼10× gap but leaves the reader uncertain about which convention is adopted in the rest of the paper and how that choice propagates to numerical statements.
Required fix: Choose a single convention, state it once (including all factors of 2, π, αem), and propagate consistently. If you retain α/M, give the explicit dictionary to the canonical gaγ and show the numerical value in both conventions for the benchmark.

P1A-M5 (Sec. V–VI, pp.13–14; Sec. III.B p.9)
Problem: The paper asserts an independent galaxy-spin null detection and refers to “Paper IV [23]” as the source of methods and significances, but this present paper still leans on those null results to motivate narrative flow.
Required fix: Either summarize the essential methodology (data selection, classifier performance, bias audits, estimator, uncertainties) sufficient to evaluate the null’s robustness, or de-emphasize the spin channel entirely here and simply cite the independent paper without importing its claims.

P1A-M6 (Sec. I.A.2; Fig. 5 bottom caption and axis labels; pp.4,16)
Problem: The “fine-tuning improvement by 115 orders of magnitude” graphic risks misleading readers despite textual caveats (it is a reparameterization). Visual emphasis conflicts with the stated caution.
Required fix: Move this comparison to an appendix, add an overplot annotation “reparameterization only; not a solution to CC problem,” and ensure the main text does not present this as an “improvement.”

P1A-M7 (Inconsistent status of [6]; p.5 vs p.24)
Problem: [6] is described as “in preparation” in Sec. I B p.5 but “posted concurrently on arXiv” in the references p.24.
Required fix: Make the status of [6] consistent throughout. If it is posted, give its arXiv identifier and ensure it contains the promised analysis. If it is not posted, remove “posted concurrently” and excise all dependence on it (see ESSENTIAL items).

P1A-M8 (Sec. X, pp.17–18)
Problem: The key “perturbation transparency” claim is correct in spirit, but it would benefit from a brief explicit index proof or a standard reference that ϵμνρσRμνρσ(Γ̊) = 0 by the algebraic Bianchi identity (beyond form-language remarks).
Required fix: Add a two-line index proof or cite a standard GR text demonstrating the vanishing of the dual contraction on a torsionless connection; keep the distinction from Pontryagin as you already do.

MINOR

P1A-m1 (Throughout; e.g., Refs. [13–14], p.24)
Problem: Author name “Pop lawski” appears with a spurious space; standard spelling is “Popławski” (without space; often rendered “Poplawski” in ASCII).
Required fix: Correct the spelling throughout.

P1A-m2 (Notation; Abstract p.1; Sec. IV.E p.12; Sec. X p.17)
Problem: Mixed notation for the gravitational Chern–Simons/Pontryagin density (R ∧ R̃ vs. “R ∧ Re”).
Required fix: Use a single standard notation (e.g., R ∧ R̃ or ϵ·RR) and define it once.

P1A-m3 (Language; Figs. 3, 5 captions; multiple)
Problem: Casual phrases (“burned-in annotation”, “we deliberately do not commit to a specific calendar date…”) are not appropriate for a PRD article.
Required fix: Replace with formal scientific language or remove.

P1A-m4 (Units and constants; Sec. IV.D p.12; Sec. II C p.7)
Problem: H0 ≈ 1.5 × 10−33 eV is used correctly, but the paper would benefit from a brief unit-conversion note or citation the first time this conversion is used.
Required fix: Add a parenthetical or footnote with the Hz→eV conversion (1 Hz = 4.1357… × 10−15 eV) and H0 ≈ 67.7 km s−1 Mpc−1 ≈ 1.5 × 10−33 eV.

NIT

P1A-n1 (Typos; various)
Examples: “Domaga la–Lewandowski” → “Domagala–Lewandowski”; “Poincar´e” has stray accent in some places; occasional spacing before commas/semicolons.
Required fix: Copy-edit.

P1A-n2 (Reference formatting; multiple)
Problem: Some references lack journal identifiers or have placeholder phrasing (“arXiv preprint (2025)”). Ensure consistency and completeness.
Required fix: Standardize citations to PRD/PRL/A&A/JCAP styles with year, volume, page, arXiv id.

P1A-n3 (Equation cross-references)
Problem: A few cross-references in the prose to equations (e.g., “Eq. 14” in Sec. II C 1) are potentially ambiguous with local numbering.
Required fix: Verify all equation references point to the intended equation numbers.

Additional methodological comments
- The central “perturbation transparency” result is an interesting structural statement, and the Bianchi-identity route is clean. However, because much of the rest of the paper is a catalog of amplitude/naturalness closures, the manuscript must be fully self-contained methodologically. At present, too many key quantitative elements are deferred to non-public companions, or are shown in figures without methods.

- The Route-2 (one-loop) closure is the only place where I found real ambiguity in the dimensional reduction to a dimensionless observable. This must be rectified with one coherent chain.

- The ALP birefringence naturalness critique (Route-4) is carefully argued and the arithmetic checks out (ρθ ≈ 1.6 × 10−10 eV4 for mθ = H0 and α/M = 10−21 GeV−1 does give ~6 ρΛ). Good.

- The NJL suppression arithmetic also checks: nb ≈ 330 cm−3 ≈ 2.5 × 10−12 eV3 leads to ρNJL ~ 4 × 10−80 eV4, i.e., ~10−69 ρΛ.

- The LQC density window and its γ-dependence were recalculated and are internally consistent.

Page-length
Given the paper’s present reliance on external, non-public companions and the inclusion of operational MCMC details not germane to this theory paper, the manuscript is longer than necessary. After implementing the essential removals and consolidating the derivations, a target length of 18–20 pages seems appropriate.

## Summary recommendation
MAJOR REVISIONS

The core theoretical contribution (perturbation transparency by Bianchi identity; systematic channel-level closures) is potentially publishable. However, the manuscript, as submitted, relies on non-public companion analyses, contains version-history language in the body, presents forecast/significance figures without in-paper methods, and shows a key one-loop closure with ambiguous dimensional reduction. These are methodological and presentation issues that must be fixed for PRD standards. Once the paper is made self-contained, all numerical chains are unambiguous, and extraneous internal-lab notes are removed, the work can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (post second-pass audit)

ESSENTIAL

P1A-E9 (Sec. IV.B Eq. (15) and surrounding text)
Problem: In the Route-2 one-loop estimate, the numerical substitution ∂μϑNY ∼ H0 implicitly assumes that ϑNY is dimensionless (so ∂ϑ has mass-dimension +1). However, the operator Γone-loop ∝ (1/MPl) ∫ √−g ∂μϑNY J5μ is only dimension-4 if ϑNY carries mass-dimension +1 (so ∂ϑ has mass-dimension +2). These two requirements are inconsistent. If ϑNY is dimensionless (as used in Eq. (15) to set ∂ϑ ∼ H0), then (1/MPl) ∂ϑ J5 has mass-dimension 3 and the action density is not dimension-4. If ϑNY has mass-dimension +1 (to fix the operator’s dimension), then ∂ϑ ∼ H0 is dimensionally wrong; one needs an additional mass scale. This is separate from, and more fundamental than, the “alternative ordering” issue noted previously.
Required fix: Resolve the mass-dimension of ϑNY unambiguously and make Eq. (14)–(15) consistent. If ϑNY is dimensionless, promote the prefactor to 1/M2 (or supply the missing mass) so that the Lagrangian has dimension +4; then recompute Eq. (15) with the correct mass dimensions. If ϑNY has mass-dimension +1, replace ∂ϑ ∼ H0 by ∂ϑ ∼ H0 × Mscale (and define Mscale), and recompute the ratio. Present one consistent chain.

P1A-E10 (Abstract, first paragraph)
Problem: The abstract states that all four enumerated routes “fail at the amplitude level under stated assumptions,” but in Sec. IV.E and multiple places the paper is explicit that Route 4 (parity-odd CMB coupling via spectator ALP/neutrino current) is not amplitude-excluded; it is closed by a naturalness/tuning objection (mθ ∼ H0), not by amplitude.
Required fix: Correct the abstract to reflect that R1–R3 fail at the amplitude level (or mass-dimension lock), whereas R4 fails by a naturalness objection rather than an amplitude no-go.

MAJOR

P1A-M9 (Fig. 2 vs. main-text numbers; pp.5–7)
Problem: Fig. 2 contains a “burned-in” illustrative waypoint N ≈ 55, e−3N ≈ 10−72, while the body repeatedly uses Ntot ≈ 92–94 as the relevant dilution to match ρΛ. This visual annotation is inconsistent with the analysis emphasis and risks confusing readers about the required e-fold count.
Required fix: Update the annotation to reflect the actual Ntot used (≈ 92–94), or clearly mark the 55 e-fold waypoint as purely illustrative and not used in any quantitative claim. Preferably, remove the conflicting number from the figure.

P1A-M10 (Appendix A Table IV; Sec. II.A.1 p.5)
Problem: The “γ scheme range ∼ 0.020” reported in the parameter summary is inconsistent with the stated values: γSU(2) ≈ 0.274 and γDLM ≈ 0.2375 differ by 0.0365, not ∼0.020. The U(1) value (≈0.127) increases the spread further. The table note also says the range is “the spread between counting prescriptions,” which numerically is ≳0.0365 between the two non-U(1) schemes quoted.
Required fix: Correct the reported scheme spread to ≈ 0.037 (SU(2)–DLM), state explicitly which prescriptions are being compared, and ensure this value is used consistently wherever a “scheme range” is quoted.

P1A-M11 (Sec. IV.E, paragraph beginning “The condensate mechanism yields …”)
Problem: Internal contradiction about the sign of the mismatch. Earlier (Sec. IV.A) the NJL/Hehl–Datta four-fermion contribution is shown to be many orders of magnitude too small to account for ρΛ. In Sec. IV.E, the text says “The condensate mechanism yields a vacuum energy that is parametrically too large …,” which contradicts the earlier arithmetic and context (it is too small at late times).
Required fix: Reconcile the statements. If “condensate mechanism” here refers to a different scenario than the NJL late-time contribution, define it and provide the calculation. Otherwise, correct the wording to “too small” to match Sec. IV.A’s quantitative result.

MINOR

P1A-m5 (Notation collision; multiple)
Problem: The symbol β is used both for the birefringence angle and for a renormalization-group function β(γ). Although the argument β(γ) helps, there are instances where “β” appears near both meanings, inviting confusion.
Required fix: Adopt disambiguating notation throughout (e.g., βCB for cosmic birefringence; βRG(γ) for the RG function) and edit affected passages.

P1A-m6 (Figure-label/body mismatch style; Fig. 3 caption; general)
Problem: The manuscript uses informal figure-caption language (“burned-in annotation,” “rounded up to the nearest decade”) that also pertains to numerical content. While not strictly a style violation alone, coupling casual phrasing to numerical qualifiers in captions invites confusion about what is schematic vs. used in analysis.
Required fix: Replace with formal, unambiguous phrasing (“schematic annotation,” “rounded for display only; body text provides the quantitative bound (ω/H)0 < 5 × 10−11”). Ensure any rounded values in figure labels are reconciled quantitatively in the body once.

P1A-m7 (Cross-reference precision; Sec. II.C.1, “Eq. 14” reference)
Problem: Sec. II.C.1 contrasts a thermal phase-space factor with the “one-loop coefficient αem/(4π) appearing in Eq. (14)”, but Eq. (14) as written does not explicitly contain αem/(4π). This can confuse readers about which loop coefficient is being contrasted.
Required fix: Clarify in text that αem/(4π) is the expected loop factor size for the operator class, even if not explicitly displayed in Eq. (14) as written. Alternatively, rewrite Eq. (14) to show the loop factor explicitly if that is the intended normalization.

P1A-m8 (Notation collision: γ)
Problem: The symbol γ denotes both the Barbero–Immirzi parameter and, elsewhere, the PTA spectral index γ (used in Table IV and Sec. X.G). This can cause confusion in multi-parameter passages.
Required fix: Use a distinct glyph or subscript for the PTA spectral index (e.g., γPTA) consistently in text, figures, and tables.

P1A-m9 (Abstract/body consistency on “two surviving predictions”)
Problem: Table I lists “Testable prediction? fNL = −35/8” as the surviving one, while the body (Sec. XIII) emphasizes two mechanism-independent observables (fNL and β). This is a minor presentation mismatch.
Required fix: Harmonize Table I with Sec. XIII by noting both class-level tests (matter-bounce fNL and spectator-ALP β), with the explicit caveat that neither is an ECH-unique prediction.

P1A-m10 (Appendix B dimensional line, Eq. (B1))
Problem: The counting [ε μνρσ eIμ eJν FIJρσ] = +2 is acceptable if eIμ is treated dimensionless and FIJ has dimension +2, but this convention is not stated where the counting is introduced. Readers may assume [e] carries dimension +1 in other conventions.
Required fix: Add a one-sentence convention statement (“We take tetrads dimensionless and curvature two-forms of mass-dimension +2.”) adjacent to Eq. (B1) for clarity.

Rationale for additional pass
The second-pass checks focused on hard arithmetic, figure/body agreement, and dimensional consistency surfaced several new issues that were not captured in the initial review, notably: (i) an internal inconsistency in the Route-2 one-loop treatment regarding the mass dimension of ϑNY and the numerical substitution ∂ϑ ∼ H0; (ii) an abstract/body mismatch about the nature of the Route-4 closure; (iii) inconsistent numerical reporting of the γ scheme spread; (iv) a contradictory statement about the condensate route’s amplitude direction; and (v) figure annotations at odds with the main Ntot narrative. These are material to PRD-level methodological rigor and should be addressed alongside the previously noted essential/major items.