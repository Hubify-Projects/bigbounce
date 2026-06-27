# P1A R55 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R55_P1A/paper1a_ech_nogo.pdf` md5=304331a0 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8731 chars)
**Wall time**: 593.2s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
- Focus: methodology rigor; internal arithmetic, dimensional analysis, estimator definitions, statistical claims, figure/table consistency, and stand‑alone reproducibility as per PRD standards.
- I read the full 29-page manuscript, including all figures, tables, equations, captions, appendices, and the abstract, and recomputed every stated ratio/significance/percentage that is numerically checkable from in-text numbers.

Overall assessment
The manuscript advances a “channel‑level closure” program for four minimal ECH routes and presents a clean perturbation‑transparency statement. However, the paper relies extensively on “companion papers (in preparation)” for multiple load‑bearing statements (MCMC posteriors, galaxy‑spin null, SPHEREx Fisher forecast, PTA reanalysis, NaMaster validation, ALP parameter fits). The Data/Code Availability section promises a future Zenodo DOI but provides only a mutable GitHub link. Several of the named “barriers” (especially B1–B2) are asserted without derivations or with scaling ansätze that are insufficiently justified for a closure claim. One four‑fermion coefficient appears inconsistent with the canonical literature. A number of figures (e.g., Fig. 5) present quantitative “scores” without a traceable computation.

Below I list specific findings.

Findings

ESSENTIAL

P1A-E1 (Data availability; p. 26, “Data and Code Availability”)
- Problem: “a Zenodo-archived release will pin all artifacts to the submitted-version snapshot.” Only a GitHub link is provided; no fixed DOI, no tagged commit hash, no release version stated in the paper.
- Required fix: Provide a permanent, versioned archival DOI (Zenodo or equivalent) of the exact code/data used to produce the figures, tables, and any quoted numbers. List the specific commit hash/tag corresponding to the manuscript. Include a manifest enumerating which scripts reproduce which figures/tables, with dependency versions.

P1A-E2 (Standalone-reader requirement; multiple places: Abstract p. 1–2; Sec. I, pp. 3–4; Sec. III B p. 10; captions Fig. 4 p. 16 and Fig. 7 p. 23; Sec. XIII p. 23; Appendix references)
- Problem: Numerous load-bearing claims are deferred to “companion papers (in preparation)” or internal analyses that are not accessible to a reader: ΛCDM+ΔNeff MCMC values (H0, σ8), NaMaster validation, ALP parameter fitting and LiteBIRD forecast, SPHEREx fNL Fisher forecast, PTA real-KDE reanalysis, and the galaxy-spin null. The paper states the numbers are “not used in the closure proof,” but they are presented as part of the results narrative (Table I, Figs. 4, 7; Secs. III B, XIII).
- Required fix: Either (a) remove all results that depend on in-preparation or internal analyses and restrict the paper to the self-contained ECH closure and perturbation-transparency arguments; or (b) include, in this manuscript or its Supplemental Material, the full methods and results for each used analysis (dataset specs, priors, likelihoods, convergence diagnostics, estimator definitions, masks, systematics), with reproducible artifacts (see E1). PRD cannot accept “in preparation” as load-bearing evidence.

P1A-E3 (Executive-summary table uses internal, non-reproducible posteriors; Table I, p. 4)
- Problem: “H0 = 67.68 ± 1.06, ΔNeff ≈ 0; Recovers ΛCDM” are taken from an internal MCMC (Paper I(b), in preparation). These quantitative claims are not reproducible from the paper and are not ancillary; they are presented as verification.
- Required fix: Remove these posterior numbers or replace with published Planck/BAO/SN values (with proper citations) and state explicitly that this paper does not contribute new MCMC constraints. Alternatively, provide full MCMC details and chains within this manuscript’s SI (see E1/E2).

P1A-E4 (Four-fermion contact coefficient; Sec. II A 2 Eq. (4), p. 7; Sec. IV A p. 11)
- Problem: The displayed coefficient for the axial–axial contact Lint = −(3πGN/2) × [γ^2/(γ^2+1)] J5·J5 conflicts with the canonical minimal-coupling Einstein–Cartan–Holst result in several references, where the γ-dependence for the axial–axial channel appears as 1/(1+γ^2) (and γ-dependence can drop out under Mercuri’s non-minimal scheme reconstructing Nieh–Yan). The manuscript cites [15,16,20] but does not derive Eq. (4).
- Required fix: Provide a transparent derivation (with conventions fixed) or a definitive citation that matches Eq. (4) exactly. Clarify the coupling choice (minimal vs non-minimal) and whether the γ^2 in the numerator is correct. If the coefficient is altered by convention, show the mapping. The amplitude‑closure conclusion likely survives, but PRD requires coefficient-level correctness.

P1A-E5 (Barrier statements used as “closures” without derivations; Sec. IX, pp. 16–20)
- Problem: Several barriers are asserted, not derived. In particular:
  - B1 (“Mass-Coupling Lock”; Eq. 18): geff ~ 1/(MPl sqrt|t3|) ~ H0/MPl is presented as a scaling ansatz without a derivation from a specified PGT Lagrangian (signs, normalization, mode content).
  - B2 (“Topological-Shift Duality”): “Mass protection ⇔ No geometric fingerprint” is a strong claim stated without proof.
  - B9 (“Liouville Conservation”): closure argument is heuristic and assumption-laden.
  - B12 (GW ceiling): ΩGW|bounce ≲ (ρcrit/ρPl)^2 quoted as a “ceiling ansatz” without derivation.
- Required fix: For each barrier used to close a route, either (i) supply a derivation/proof (or bound) with precise assumptions and equations, or (ii) clearly demote it to a conjecture/heuristic that does not participate in any route closure. As written, these barriers cannot be cited as methodologically rigorous closures in PRD.

P1A-E6 (Route-2 closure: missing explicit derivation of photon coupling chain; Sec. IV B pp. 12–13)
- Problem: The one-loop operator (14) couples ∂μϑNY J5μ. The subsequent birefringence amplitude estimate for CMB photons relies on the anomaly chain ∂μJ5μ ⊃ (αem/4π) FF̃ and an implicit mapping to a net line-of-sight polarization rotation. This is used to conclude “~10^−60 suppression.” The derivation is described as an “amplitude‑budget bound,” not a controlled calculation.
- Required fix: Provide an explicit, self-contained derivation of the induced birefringence from Eq. (14), with all steps (anomaly insertion, Green’s function/response, late-time projection) and dimensional scalings, or replace the present estimate with a fully rigorous inequality (with clear assumptions). If this step remains heuristic, the claim that R2 is “closed by amplitude suppression” is not rigorous enough for PRD.

P1A-E7 (Use of non-EFT operator as load-bearing construct; Eq. (6) and Appendix B, pp. 7, 26)
- Problem: The key parity-odd operator (6) is acknowledged to have mass dimension +1 off-shell; mapping to an energy density uses an on-shell scaling ansatz (Appendix B). Nevertheless, Eq. (10) and Fig. 3 use this parameterization to discuss Λeff and H(z).
- Required fix: Either (a) recast all sections that use Eq. (6) strictly as illustrative parameterizations, removing any closure arguments that rely on it, or (b) promote a proper dimension‑4 EFT operator with an explicit coupling (as acknowledged in App. B: α MPl^3/M), and propagate the consequences consistently throughout. PRD requires operator-level consistency for any load‑bearing derivation.

MAJOR

P1A-M1 (Fig. 5 “fine-tuning score” and RG-running panel; p. 18)
- Problem: The lower panel shows “fine-tuning scores” 10^5 (this work), 10^40 (f(R)), 10^60 (quintessence), 10^120 (ΛCDM) but no explicit definition, estimator, or calculation path is given; the text calls it a “reparameterization,” not a solution. The upper panel shows an RG “running of α/M” but there is no specified β-function or computation.
- Required fix: For each bar, define the metric (what is “fine-tuning score,” how is it computed, and from which parameters?), with a worked calculation or detailed reference. For the RG plot, specify the RG equation and inputs used to produce the curve.

P1A-M2 (Fig. 3 H(z) deviation; p. 8)
- Problem: The ECH curve and its “2–3%” deviation are based on Ξ chosen to match ρΛ via the non-EFT ansatz of Eq. (6)/(10). This can be misconstrued as a predictive curve.
- Required fix: Add “illustrative only; not derived from a controlled EFT” on the panel or in the caption and in the main text next to Fig. 3, or remove Fig. 3.

P1A-M3 (Executive-summary density of claims; Table I, p. 4)
- Problem: The table mixes illustrative projections (SPHEREx/LiteBIRD), internal MCMC, and theoretical closures in a single “result” grid, which can suggest achievements that are not actually accomplished in this paper.
- Required fix: Split into (i) results proven in this paper (with page references), and (ii) external/forecast items (clearly marked as “not computed here”), or remove the table.

P1A-M4 (Repeated dependence on galaxy-spin companion; Sec. III B p. 10; Sec. VI p. 15; Sec. XIV B p. 24; Fig. 4 p. 16; Fig. 7 p. 23)
- Problem: The claimed “confirmed null” (pLEE < 10^−4) and sample stats come from Paper IV (in preparation). No minimal in-paper description of selection, classifier performance, bias tests, or sky coverage is provided.
- Required fix: Either remove these claims or provide a concise, self-contained methods and results subsection sufficient for a reader to evaluate the statistical validity (classifier accuracy, calibration, null tests, masks, LEE correction).

P1A-M5 (PTA annotation; Fig. 1 caption p. 5; Sec. X G p. 21)
- Problem: The cited result γPTA = 2.567 ± 0.382 from “real-KDE GPU MCMC” is not documented here. While not central, it is featured in Fig. 1 and interpreted (+1.13σ).
- Required fix: Remove this annotation or supply enough method detail and a stable artifact so that a reader can check the number.

P1A-M6 (Route-3 running of γ; Sec. IV C p. 13)
- Problem: The displayed running dγ/d ln μ = (NLF − NRF)/(12π^2) γ + O(γ^2) is introduced as an “upper-bound EFT ansatz” and not taken from [26] or [27]. The subsequent amplitude closure depends on combining this ansatz with mass-dimension arguments.
- Required fix: Either use the published β-function from Benedetti & Speziale (with the induced four-fermion terms) and propagate it to a quantitative bound, or present a rigorous inequality that closes R3 without an ad hoc β-function.

P1A-M7 (Ambiguous Holst+T^2 starting action; Eq. (1), pp. 5–6)
- Problem: The action includes + (1/4) Tabc Tabc within the 1/(16π G) bracket, then a footnote explains this is a “Hehl–Datta shorthand” and is not varied. Including it in the fundamental action but then stating it is not an independent term is confusing and risks double counting for readers.
- Required fix: Present the actual varied action cleanly (Einstein–Cartan–Holst + Dirac), derive the Cartan equation, then show the effective on-shell Lint separately. Remove T^2 from the displayed fundamental action or partition the terms explicitly as “on-shell effective.”

P1A-M8 (Barrier nomenclature vs logical independence; Table II p. 17; Fig. 6 p. 19)
- Problem: The paper states “13 logically independent barriers” but B8 is observationally subsumed by B14. Several other barriers overlap conceptually with the perturbation-transparency result (e.g., B3, B4). The claim of logical independence requires care.
- Required fix: Provide a dependency graph with precise statements of which barriers derive from which assumptions/results, and adjust the “logically independent” count accordingly, or soften the claim.

P1A-M9 (Overuse of “in preparation” across abstract and text; Abstract pp. 1–2; Sec. I pp. 3–5; Sec. XIII p. 23; Acknowledgments p. 26)
- Problem: Prominent reliance on “in preparation” references throughout the narrative reduces verifiability.
- Required fix: Remove or replace with published sources, or confine to a brief Outlook paragraph that does not support any core claim.

P1A-M10 (Statistical comparability guardrails need to be repeated whenever joint plots appear; Figs. 4 and 7)
- Problem: While you do include comparability caveats in the abstract and some captions, each instance where multiple σ values appear together (CMB EB, galaxy spins, joint curves) should carry a clear reminder that null procedures differ.
- Required fix: Add explicit “not directly comparable” caveats in every multi-σ juxtaposition (e.g., Fig. 4 legend/caption, Fig. 7 caption already almost does; make it unambiguous).

MINOR

P1A-m1 (Arithmetic check: ACT vs Planck birefringence difference; Sec. IV D p. 14)
- Check: |0.342 − 0.215| / sqrt(0.094^2 + 0.074^2) = 1.06σ as stated. Correct.

P1A-m2 (Arithmetic check: “∼ 6 ρΛ” at mθ = H0; Sec. IV D p. 14)
- Check: ρΛ ≈ (2.3 meV)^4 ≈ 2.8 × 10^−11 eV^4; ρθ ≈ 1.6 × 10^−10 eV^4 → ratio ≈ 5.7. Statement “≈ 6” is consistent.

P1A-m3 (Arithmetic check: (Treh/MGUT)^(3/2); Sec. II C 1 p. 8)
- Check: (10^15/10^16)^(3/2) = 0.1^1.5 ≈ 0.0316 ≈ 0.03. Correct.

P1A-m4 (Arithmetic check: Ntot for dilution 10^−122; App. B p. 26)
- Check: N = (ln 10) × 122 / 3 ≈ 93.8; body text’s “~94” is consistent; the “~92” used for tension is acknowledged as ansatz-dependent. Fine.

P1A-m5 (Arithmetic check: H0/MPl; Sec. IV B p. 12)
- Check: ∼ 10^−61 is correct.

P1A-m6 (Minor typographical consistency)
- Instances: spacing and hyphenation (e.g., “Pop lawski” vs “Popławski”), occasional duplicated hyphenation (“channel‑level,” “programme”). Clean these to PRD style.

P1A-m7 (Notational clarity)
- Problem: Early and frequent use of γ for Barbero–Immirzi and γPTA for PTA spectral index. Although you do note the distinction, consider a different symbol for the PTA index throughout figures/captions to avoid reader confusion.
- Required fix: Rename γPTA to nPTA or αPTA in all figures/captions and the text.

NIT

P1A-n1 (Aesthetic)
- The acknowledgment of AI assistance is acceptable but consider moving details to a footnote if journal policy prefers brevity in Acknowledgments.

P1A-n2 (Reference formatting)
- Ensure journal names, years, and arXiv IDs are consistently formatted (e.g., [9], [10] list “DESI 2024 VI” vs “DESI DR2 Results II” inconsistently).

Verification/consistency checks passed
- EB small-angle formula (Eq. 12) is standard.
- Bianchi-identity argument for RH(Γ̊) ≡ (1/2) ε R = 0 at T = 0 is correct and the distinction from Pontryagin is clearly made.
- Unit conversions in the R1 amplitude estimate are correct.
- One-loop coefficient order-of-magnitude [(α/M) MPl] ≈ 3 × 10^−3 from Eq. (7) checks out with the stated inputs.
- ρcrit(γSU(2)) ≃ 0.27 ρPl computed from the quoted γ values is consistent.

Length and focus
- The manuscript is long (29 pages) relative to the core proven content (perturbation-transparency result and enumerated closures). Consider reducing to 18–20 pages by:
  - Removing forecasts and internal/companion results (Figs. 4, 7; Table I).
  - Condensing Section IX to those barriers with full derivations in this paper.
  - Moving long convention footnotes and the H(z) illustration (Fig. 3) to SI.

Abstract-last drift sweep
- The abstract contains several caveats that are honored later (“not operator-basis complete,” “ansatz,” “not an ECH prediction,” “not directly comparable”). However, it still cites companion-paper forecasts (SPHEREx) and internal pipelines as if integral to the paper’s contributions.
- Required adjustment: Remove all references to in-prep results from the abstract. Restrict the abstract to results actually proved here (perturbation-transparency, channel-level closures with stated assumptions).

## Summary recommendation
MAJOR REVISIONS

The core perturbation-transparency statement is sound and interesting, and several numerical checks are correct. However, the paper as submitted does not meet PRD methodological standards due to (i) lack of a permanent, reproducible artifact archive; (ii) heavy dependence on in-preparation companion papers for multiple load-bearing statistical claims and figures; (iii) insufficient derivations for several “barriers” used to close routes; and (iv) at least one likely incorrect four-fermion coefficient. If the authors confine the manuscript to what is rigorously derived here, provide proofs (or downgrade unproven barriers), correct the EC/Holst contact coefficient with a derivation, and supply a permanent reproducibility package, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second‑pass audit)

Note: I do not repeat items already listed in my first report. New issues are labeled continuing the same scheme.

ESSENTIAL

P1A-E8 (Route‑2 ratio in Eq. 15: dimensional/algebraic clarity)
- Problem: The dimensionless ratio Δθone‑loop/Δθobs in Eq. (15) is constructed as (αem/4π) (H0/MPl) / [MPl (α/M) βobs]. This mixes “restored” MPl factors in an ad hoc way; the path from the operator in Eq. (14) to a line‑of‑sight rotation angle never appears, and Eq. (15) does not transparently track how a response kernel and anomaly insertion reduce to this exact product. Even granting “amplitude‑budget bound” status, the displayed ratio is not a cleanly derived inequality and could hide order‑unity–to–orders‑of‑magnitude factors.
- Required fix: Replace Eq. (15) by a self‑contained derivation from Eq. (14) (or a rigorous upper bound) that shows: (i) how ∂μϑNY J5μ sources the EM helicity dispersion explicitly via the anomaly, (ii) what Green’s function/causal response is used, (iii) why exactly one power of MPl appears in the denominator, and (iv) that the final expression is dimensionless without inserting compensating powers by hand. If the result is only order‑of‑magnitude, state it as such and bound all omitted constants.

P1A-E9 (Appendix C–to–Sec. IV D consistency: conformal vs cosmic time factors)
- Problem: The WKB condition in App. C compares k to (α/M) ϕ′ with ϕ′ ≡ dϕ/dη ≈ fa a H0 (for mθ ≲ H0). In Sec. IV D, the overshoot and β mapping implicitly use cosmic‑time excursions. The switch between conformal and cosmic time is handled heuristically; the factor of a(η) on the line of sight is never shown or bounded.
- Required fix: Show the full line‑of‑sight integral with the a(η) factors, or bound their effect (e.g., prove that the integral of (α/M) ϕ′/k is ≤ 10−30 across recombination→today). This removes a silent assumption about scale‑factor normalization.

P1A-E10 (Perturbation‑transparency claim for the cubic action)
- Problem: Sec. X states “the cubic action for ζ receives zero contribution from the Holst term,” but no explicit ζ action is presented and no reference is cited that carries this to cubic order. The Bianchi‑identity argument proves the vanishing of e∧e∧R(Γ̊) pointwise; it does not, by itself, demonstrate that all possible third‑order metric–scalar combinations vanish in the perturbed action before using equations of motion (total derivatives vs. identically zero).
- Required fix: Provide an explicit third‑order expansion (or a tight reference) showing that the ζ cubic vertex receives no Holst‑sector contribution when T = 0, or rephrase this line as a corollary of the stronger pointwise identity with a short proof sketch.

P1A-E11 (Equation (6) notation collision and operator identity)
- Problem: Eq. (6) uses FIJρσ for the curvature two‑form in components, but later Fμν denotes the EM field strength. Although you note “calligraphic F” earlier, Eq. (6) itself is not calligraphic and can be confused with the EM Fμν used in Sec. IV D.
- Required fix: Use a distinct symbol (e.g., RIJρσ or calligraphic script everywhere) in Eq. (6) and in the caption/body where Eq. (6) is invoked, and reaffirm that this is the gravitational curvature. This is easy to fix but prevents misreading when Eq. (6) and the ALP–photon section are viewed side‑by‑side.

MAJOR

P1A-M11 (Inconsistent spectator‑ALP benchmark value)
- Problem: The manuscript alternates between β ≈ 0.27° and “0.27°–0.30°” as the benchmark spectator‑ALP rotation. The figures appear to use 0.27°, while some body text mentions 0.27°–0.30°.
- Required fix: Choose one benchmark (0.27°) and use it consistently in text, figures, and tables, or present both and explain why two values are relevant. This matters for quoted σ‑level statements against future sensitivities.

P1A-M12 (Table III “Quintom‑B consistent” entry without support)
- Problem: Table III marks “Quintom‑B … consistent†” with a footnote that no MCMC was done in this paper. As written, this suggests an evidence‑based conclusion that is not performed here.
- Required fix: Either remove the “consistent” marker or replace it by “model‑level accommodation; no statistical test in this paper,” with a citation to a published study that demonstrates this, if available.

P1A-M13 (Prior specification for α/M in Table IV)
- Problem: Table IV lists “α/M: Log‑flat ∼ 10−21 GeV−1; One‑loop motivated” but does not define the prior bounds or base of the log, and later sections treat α/M as effectively fixed by βobs. This leaves ambiguity about whether α/M is free (with a prior) or pegged.
- Required fix: Specify the prior precisely (range, base, role in any fits shown) or state clearly that α/M is not sampled anywhere in this paper and is only used as a fixed illustrative value.

P1A-M14 (Fig. 4 and Fig. 7 “ρ” correlation parameter)
- Problem: Both figures include a “combined (ρ = …)” curve but do not define how ρ is obtained (cross‑covariance of estimators? common‑mode systematics?). No formula is provided for the combined significance as a function of ρ.
- Required fix: Add a short methods box or caption line with the combination formula (e.g., S2 = S2
1 + S2
2 + 2ρ S1 S2 under Gaussian assumptions), how ρ is estimated, and a statement that this is an illustrative combination (not computed from data here).

MINOR

P1A-m8 (Caption/body mismatch: LiteBIRD σ(β) vs plotted timeline)
- Observation: The text uses σ(β) ≈ 0.03° and a “∼ 9σ” detectability for β = 0.27°, while Fig. 4’s top panel timeline appears to top out at ≲ 6–7σ. The caption does not explain why the timeline crest differs from the naive 9σ bar.
- Suggestion: Add a sentence in the Fig. 4 caption noting that the timeline tracks a staged combination with current uncertainties (hence < 9σ), while the 9σ figure refers to a single‑experiment end‑state sensitivity.

P1A-m9 (Holst‑term identity wording)
- Observation: Sec. X D claims “pointwise vanishing” via e ∧ e ∧ R = −NY + T ∧ T. This identity involves the full torsionful connection. The wording could be read as “topological in vacuum” (which e ∧ e ∧ R is not). You do clarify later, but the sentence can confuse non‑specialists.
- Suggestion: Add “for the Levi‑Civita connection (T = 0), both terms vanish and thus e ∧ e ∧ R(Γ̊) = 0 pointwise; this is distinct from the Pontryagin density, which remains a total derivative even at T = 0.”

P1A-m10 (Stated H(z) deviation range vs inputs in Fig. 3)
- Observation: The caption quotes “2–3% across z = 0–3”. With H0 = 69.2 vs 67.36 km/s/Mpc (Δ ≈ 2.7%), the z = 0 end is consistent. At z ≳ 2, for fixed Ωm, the relative difference can fall below 2% depending on radiation terms. The panel is illustrative, but the caption reads as a quantitative statement.
- Suggestion: Qualify as “∼2–3% at z ≲ 3 for this illustrative parameter set.”

P1A-m11 (Cross‑reference precision)
- Observation: Several places point to “Sec. X G” for the PTA annotation; others to “Paper III §6.” Ensure every in‑paper pointer (e.g., Sec. X G) actually contains the quoted number and caveat, to minimize reader hunting.
- Suggestion: Add a one‑line restatement of the value in Sec. X G so the reader does not have to rely on the figure caption.

P1A-m12 (Notation for γPTA)
- Observation: You already warn that γPTA is distinct from the Barbero–Immirzi γ. A more orthogonal symbol (nPTA) in the figures would avoid split‑second misreads.
- Suggestion: Rename in the figure labels/legends if possible.

NOISE/COSMETIC

P1A-n3 (Equation (6) symbol choice)
- Minor clarity gain if RIJμν is used throughout for the gravitational curvature to avoid any overlap with the EM Fμν later.

P1A-n4 (Consistent use of reduced/unreduced Planck mass)
- You note that you use unreduced MPl throughout, but Eq. (1) and several GR‑normalization sentences are most familiar in reduced units. Consider appending “unreduced MPl is used everywhere; numerical factors of 8π do not affect any OOM bound shown.”

Rationale for additional pass
- The second pass focused on tightening operator‑to‑observable mappings (E8–E10), consistency between appendices and body text (E9/E10), resolving notation/benchmark consistency (M11–M13), and clarifying combined‑significance plots (M14/m8). These items were not fully covered in my first review and materially improve reproducibility and clarity without repeating earlier points.

Summary
- The new essential items (E8–E11) require explicit fixes to meet PRD’s standards for rigor in operator mapping, time‑variable handling, and perturbative claims. Major items (M11–M14) are presentation/consistency issues that could mislead readers and should be addressed. Minor items (m8–m12) are clarifications that will reduce confusion.