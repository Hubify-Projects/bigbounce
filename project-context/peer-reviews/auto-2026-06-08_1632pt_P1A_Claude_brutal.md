# P1A auto-2026-06-08_1632pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14802 chars)
**Wall time**: 435.8s

---

# Referee Report — Paper P1A
## "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

---

## Overall Assessment

This is a 21-page manuscript that, by its own admission, (i) does not derive a new physical result, (ii) closes a framework the author proposed elsewhere by hand-waving four "routes" while explicitly leaving operator-basis closure to a follow-up, (iii) bases its "central theorem" on a trivial corollary of the algebraic Bianchi identity that was previously misidentified in earlier drafts, and (iv) relies on **five** companion papers by the same author marked "in preparation" or "available upon request" for its observational numbers, MCMC posteriors, NaMaster pipeline validation, and birefringence parameter fitting. The paper is effectively unreviewable in standalone form, contains substantial internal version-history language in the body, and its two "surviving predictions" are admitted by the author *not* to be predictions of ECH.

The acceptance bar at PRD is high. This paper does not meet it. The recommendation will be REJECT.

---

## ESSENTIAL findings (must be addressed before any further consideration)

### P1A-E1 (Throughout): Paper is unreviewable due to dependence on unsubmitted companion works
References [2], [6], [23], [46] are all "in preparation" by the same author, and [47] is "companion technical note, available upon request from the author." Critical numerical claims depend on these:
- "H0 = 67.68 ± 1.06, ∆Neff ≈ 0" (Table I, Table IV) — sourced to Paper I(b) [6]
- "γ = 2.567 ± 0.382 from real-KDE re-analysis" (Sec. X G, Table IV) — sourced to Paper III [46]
- "fNL Fisher 3–5σ" (Abstract, Table I, Sec. VII, Sec. XIII) — sourced to Paper II [2]
- Galaxy spin null at p_LEE < 10⁻⁴ (Table IV) — sourced to Paper IV [23]
- ALP MCMC parameter fitting "(9,720 accepted samples, R̂−1 < 0.01)" (Sec. XII B) — sourced to Paper I(b)

The author's own text explicitly states: *"should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted"* (Sec. I B). This is an admission that the paper cannot be refereed against the standard PRD criteria. **Fix:** Either inline the verification machinery from Paper I(b)/II/III/IV as appendices with full data products, or post all companion papers as arXiv preprints prior to PRD submission. As written, the manuscript fails the reproducibility threshold.

### P1A-E2 (Sec. X, p. 14, and footnote a, p. 1; footnote 2, p. 15): "Central result" is a corrected trivial corollary of the algebraic Bianchi identity
The "perturbation-transparency theorem" reduces to: scalar matter has zero spin → torsion vanishes algebraically → Holst dual contraction $\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma} = 0$ by $R_{\mu[\nu\rho\sigma]}=0$. This is a textbook identity (Cartan, Hehl–Datta 1971; the Holst-on-torsion-free-connection identity is essentially in Holst 1996 [25]). The author's own footnote (a) on p. 1 and footnote 2 on p. 15 admit that **earlier versions of this paper misidentified the Holst dual contraction with the Pontryagin density** and that the present version is a correction. A "central theorem" that was wrong in earlier drafts of the same submission, and whose correct form is a one-line identity, does not constitute a PRD-grade theorem. **Fix:** Demote to a Remark or Appendix; remove "central result" framing throughout (Abstract, Sec. I A, Sec. XV).

### P1A-E3 (Body, multiple locations): Internal version-history / audit-log prose embedded in the paper text
The published body contains explicit "earlier draft" / "superseded" language that has no place in a finalized manuscript:
- p. 1, footnote a: *"Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion..."*
- p. 15, footnote 2: *"An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction (Bianchi-vanishing rather than Pontryagin-total-derivative) preserves the headline..."*
- p. 15, Sec. X G: *"This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts; the migration is documented in Paper III §6."*
- p. 19 Appendix B: *"not the ∼ 35 misstated in earlier drafts"*

Each instance must be **removed**; PRD does not publish review-log prose.

### P1A-E4 (Abstract; Sec. XV Conclusions, p. 18): σ-values from different null hypotheses juxtaposed without per-instance comparability flag
The Abstract presents WMAP+Planck "∼3.6σ from β=0" alongside ACT DR6 "∼2.9σ" as if directly comparable; the Conclusions then mix a "∼9σ" LiteBIRD sensitivity against β=0 with a "0.73σ" model-discrimination test against β_obs without consistent labeling at every juxtaposition. The Conclusions paragraph eventually flags the asymmetry, but the Abstract and Sec. XII B do not. Per the reviewer instructions, this requires explicit "not directly comparable" qualifiers at every juxtaposition. **Fix:** Annotate every σ-pair with its null hypothesis.

### P1A-E5 (Sec. IV B, Eq. 15, p. 9): Dimensional reduction of Route-2 amplitude is internally inconsistent
The text claims H₀/M_Pl ∼ 10⁻⁶¹ (correct: H₀≈1.5×10⁻³³ eV, M_Pl≈1.22×10²⁸ eV gives ≈1.2×10⁻⁶¹), but Sec. IV preamble (p. 8) refers to *"Planck suppression by H₀/M_Pl ∼ 10⁻⁶⁰ in the dimensionful form."* These are inconsistent by an order of magnitude in the same section. The author then quotes the final ratio as "∼10⁻⁵⁸ to 10⁻⁶⁰" with a "factor-of-∼100 ambiguity" that conveniently absorbs the discrepancy. Additionally, the text admits *"an alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼10⁻³³ ratio"* — a 25-order-of-magnitude ambiguity in the "no-go" amplitude budget. A no-go closure with this much dimensional ambiguity is not a no-go. **Fix:** Resolve the ordering and present a single defensible amplitude; or downgrade Route 2 closure status accordingly.

### P1A-E6 (Sec. IV D, p. 10–11): Route 4 is explicitly admitted *not* to be closed
The text states: *"R4 is therefore not closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling... requires an ultralight-mass tuning... a naturalness objection rather than an amplitude exclusion."* and *"the channel is closed at the level of an explanatory deficit, not an amplitude no-go at the operator level."* This directly contradicts the Abstract claim of "channel-level amplitude closure" of all four routes. The paper's headline claim is therefore false as stated: one of the four routes is not amplitude-closed by the author's own admission. **Fix:** Rewrite Abstract, Sec. I, Sec. IV E "Closure summary," and Sec. XV to reflect that 3 of 4 routes are amplitude-closed and the 4th is a naturalness reframing of the standard CC problem.

### P1A-E7 (Abstract; Sec. XIII; Sec. XV): Both "surviving predictions" are admitted *not* to be ECH predictions
- f_NL = −35/8 is *"a property of the matter-bounce class [1]... with no ECH input"* (Abstract); *"not a distinctive ECH prediction in any case"* (Sec. XIII).
- β ≈ 0.27° is *"a benchmark consistency point, not an ECH prediction... arises in any GR+ALP setup with the same parameters and is not derived from the ECH action"* (Abstract); *"not a distinctive ECH prediction"* (Sec. XII B).

A paper whose stated framework predicts nothing distinctive cannot motivate a PRD publication as a positive result. The framing throughout — "surviving testable predictions" (Sec. VII, Sec. XIII, Sec. XV) — overclaims relevance to the ECH theory the paper is about. **Fix:** Either (a) provide a genuine ECH-specific prediction or (b) reframe the paper as a negative-result note and shorten it accordingly (see P1A-M1).

### P1A-E8 (Abstract; Sec. I A; Sec. IX): "13 logically-independent" vs "14 historical catalog entries" inconsistency
The Abstract claims "13 logically-independent mechanism-class constraints" and "14 historical catalog entries, of which B8 is subsumed by B14." Then Sec. IX classifies Barriers 5, 6, 7, 9 as "Known results" (i.e., not original) and Barrier 13 as "Structural/philosophical observation" — 5 of 14 are not novel. So the actual original-content count is at most 13 − 5 = 8 (after subsumption), not the headline 14. The paper systematically inflates its barrier count. **Fix:** State the original-contribution count honestly.

### P1A-E9 (Appendix B, Eq. B2, p. 19): Admitted dimensional ansatz, not derivation
*"[α/M] = −1, [ε... eeF]=+2 ⟹ [L_odd]=+1"* — three units short of the +4 required for a Lagrangian density. The Abstract acknowledges this, but the body of the paper — Sec. II C Eq. 10, Sec. XII A Eq. 24 — uses the ansatz as if it were a derivation, computing fine-tuning hierarchies and N_tot ≈ 92 from it. The author explicitly writes *"we treat this scaling explicitly as an ansatz, not a derivation"* and then derives quantitative numerical claims from it (N_tot ≈ 92 ± 2, residual 10⁵ fine-tuning). Numerical quantities derived from an explicitly admitted ad-hoc dimensional ansatz cannot be presented in tables or conclusions as quantitative results.

### P1A-E10 (Table III, footnote ‡, p. 16): Live MCMC chain status reported in body
*"a new DESI DR2 + Planck NPIPE + ... cobaya chain... is running on a dedicated MPI pod (16 chains, OMP threads tuned to suppress BLAS oversubscription)... At the time of this writing the chain has accumulated ∼3.8×10⁴ accepted samples... and reports R̂ − 1 ≈ 3×10⁻²... we deliberately do not commit to a specific calendar date for convergence in this footnote."*

This is a live cluster-job status report inside a Physical Review D submission. It must be removed entirely. Either the chain has converged and the result is reported, or it has not, in which case the row is omitted.

---

## MAJOR findings

### P1A-M1 Length is grossly disproportionate to content
21 pages for: (i) a trivial Bianchi-identity observation, (ii) four amplitude estimates closing channels of the author's own framework, (iii) a catalog of 14 barriers with 5 admitted "known results," (iv) two "surviving predictions" admitted not to be ECH predictions. The paper would be a 4–6 page PRD note at most after honest pruning. Recommended maximum length: **6 pages** in PRD format.

### P1A-M2 (Sec. IV "Scope" paragraphs, p. 8 and p. 11): The four-route enumeration is admitted incomplete
The paper explicitly omits the Jackiw–Pi gravitational Chern–Simons operator $R\wedge\tilde R$ and the parity-odd four-fermion partner of R1 with $\gamma_{\rm BI}/(\gamma_{\rm BI}^2+1)\cdot 8\pi G$ coefficient. These are precisely the operators that would source the parity-odd phenomenology the paper claims to close. "Channel-level closure with the dominant parity-odd operators omitted" is not closure; it is a partial audit of selected channels. The Abstract should not use the word "closure" without this qualifier next to it on first appearance.

### P1A-M3 (Sec. II C, p. 7, "Reheating thermal-reset barrier"): Hand-waving thermodynamic argument inserted ad hoc
A 30-line paragraph inserts a "fluctuation–dissipation r.m.s. residual scales as ∼√n_ψ/T_reh^(1/2)" claim with no derivation, then concludes torsion is "instantaneously" thermally reset. This is dimensional sketching, not a calculation. If this is load-bearing for Barrier 14, it requires a proper derivation; if it isn't, omit.

### P1A-M4 (Sec. II C 1, p. 7): The $(T_{\rm reh}/M_{\rm GUT})^{3/2}$ factor is explicitly admitted to be aesthetic
*"a fully rigorous first-principles derivation of the half-integer power requires the parity-odd density-of-states phase-space integral, which is dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function"*

The factor enters the N_tot = 92 calculation. An "aesthetic" half-integer power is not a derivation. The matching paragraph then says *"this is bookkeeping, not progress... the framework has not solved the cosmological constant problem; it has only relocated the fine-tuning into inflationary initial conditions."* The author is right; the question is why this is in PRD.

### P1A-M5 (Sec. III A, Eq. 12, p. 8): The CMB EB prediction is admitted to lack a derivation
*"Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here."* So Eq. 12 in this paper does no work. Why is it in the paper?

### P1A-M6 (Sec. V "Data Methods"): Methods section delegates entirely to a companion in preparation
The full data-methods section is two sentences pointing to Paper IV [23]. PRD requires self-contained methods.

### P1A-M7 (Eq. 16, Sec. IV C, p. 10): Adopted Immirzi β-function is acknowledged not to be from the cited literature
*"we use Eq. (16) only as an upper-bound EFT ansatz for the Route-3 amplitude budget and do not claim it is taken verbatim from [26]. The actual fermion-induced perturbative running of the Immirzi parameter is computed by Benedetti & Speziale [27]..."*

So the "Route 3 closure" uses an EFT ansatz rather than the actual published RG result. The closure rests on the upper-bound being saturating. This needs to be checked against the actual Benedetti–Speziale β-function or the closure does not stand.

### P1A-M8 (Eq. 14, Sec. IV B, p. 9): Phenomenological one-loop operator with no derivation
*"no published calculation currently derives this exact coefficient structure from the Mercuri construction, and the present analysis uses it strictly as an upper-bound EFT ansatz."* The Route 2 amplitude budget thus rests on an ansatz coefficient. Combined with P1A-E5, Route 2 closure is far weaker than the Abstract suggests.

### P1A-M9 (Sec. XII A and Appendix B): N_tot = 92 vs N_tot = 94 inconsistency
The structural-tension argument and Sec. XIV D use N_tot ≈ 92. Appendix B derives N_tot ≈ 94 from the genuine M_Pl⁴/ρ_Λ hierarchy and labels it "consistent at the ∼2% level." A 2% offset on N_tot maps to e^(6) ≈ 400× shift in the e-fold density factor, which is not "consistent" in any physical sense. The "e^32" SPHEREx scale-erasure argument (Abstract, Sec. XIV D) is therefore sensitive to the N_tot ansatz choice in ways the paper does not acknowledge.

### P1A-M10 Reference [47] is non-citable
*"H. Golden, Systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity (2026), companion technical note, available upon request from the author."*

PRD does not accept "available upon request" citations. Either post to arXiv or remove.

### P1A-M11 (Acknowledgments, p. 19): AI-assistance disclosure is incompletely scoped
*"The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation."*

PRD policy on generative-AI authorship/assistance requires specifying what the AI did and did not do. "Perturbation-gate verification" by AI is concerning given that the earlier draft had a Bianchi/Pontryagin misidentification (P1A-E2/E3). Was that misidentification AI-introduced? The author should clarify.

### P1A-M12 (Table III, p. 16): Table mixes "consistent at model level" with "not tested" and a "✓"-symbol that has different meanings per row
The Quintom-B row carries "consistent†" while other rows carry "not tested‡" — the table is mostly empty. The matter-bounce row "✓" for w₀w_a is contradicted by the same footnote ‡. As presented, Table III conveys nothing other than that the w₀w_a chain is running. Drop the table.

### P1A-M13 Figure 1 (p. 4) is a stylized cartoon of unclear evidentiary value
The figure plots six bounce mechanisms with arrows to five observable channels. There is no quantitative content. The legend distinguishes "produces ECH; permitted" from "structurally closed (this paper)" but the figure is essentially a slide. PRD figures should carry data.

### P1A-M14 Figure 2 (p. 5) plots the phenomenological ansatz the paper admits is not derived
*"This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action."* A figure illustrating an admitted ad-hoc ansatz as a "hierarchy" is misleading.

---

## MINOR findings

### P1A-N1 (Abstract): Abstract is a single 90+ line paragraph
The Abstract is structurally a wall of parenthetical hedges with embedded footnote text (footnote a appears *inside* the Abstract on p. 1). PRD abstracts are typically 200 words. This one is approximately 1000+ words. Cut to one paragraph stating result, method, key constraint.

### P1A-N2 (Abstract, p. 1): Footnote inside the abstract
Footnote `a` is attached to the Abstract. PRD style does not permit footnotes in abstracts.

### P1A-N3 (Sec. I A, p. 3): Phrase "channel-level closure" appears repeatedly
By informal count the phrase appears ~30 times in the manuscript. Several appearances are within single paragraphs (Sec. IV "Scope," Sec. IV E, Sec. XV). Pick one usage per section.

### P1A-N4 (Sec. II A 2, Eq. 7, p. 6): Order-of-magnitude estimate "∼ 10⁻²" for [(α/M)M_Pl] is presented without showing the input numbers
The reader has to backwork: g²/(32π²) × γ × ln(Λ²/μ²)... for what gauge coupling g? Specify.

### P1A-N5 (Sec. III B, p. 8): Section claims a galaxy-spin null but defers the entire quantitative result to a companion
Same issue as P1A-M6.

### P1A-N6 (Sec. IV B, Eq. 15, p. 9): "10⁻⁵⁸ to 10⁻⁶⁰" is presented as a range, but the section text says "ε-correction perturbative-order scaling alone"
A 2-order-of-magnitude range is not "ε-correction"; that would be O(1). Either justify or pick a single value.

### P1A-N7 (Sec. VII, footnote 1, p. 11): SPHEREx forecast σ(f_NL) ≈ 0.7 → ratio = 4.375/0.7 ≈ 6.25σ "degraded to 5–5.5σ optimistic"
The arithmetic 4.375/0.7 = 6.25 is correct, but the degradation factors are stated without source. *"Template-overlap correction r ≈ 0.84"* — cite. *"GR-projection and b_φ uncertainty"* — quantified at what level individually? Sec. VI gives 20% and σ(b_φ)/b_φ ≈ 0.2 — the propagation to "3–5σ realistic" should be shown.

### P1A-N8 (Sec. VIII Related Work, p. 12): Cai & Zhu citation [44]
arXiv:2603.13924 in [44] — year 2026 in a Phys. Rev. D submission dated June 8, 2026. The "2603" in arXiv ID corresponds to March 2026 — sanity check that this number is real. (Also Liu et al. [41] arXiv:2507.04265 is dated July 2025, and Legner et al. [42] arXiv:2507.09228 — these dates need to be verified against publication.)

### P1A-N9 (Sec. XIV C, p. 18): "LSST Era (2025–2035): 10⁹ spiral galaxies to z ∼ 1"
LSST does not target 10⁹ *spiral* galaxies specifically; total galaxy count to z ∼ 1 in usable photo-z bins is ∼10⁹ but the spiral fraction is much lower. Correct or qualify.

### P1A-N10 (Eq. 20, Sec. IX L, p. 13): Ω_GW|_bounce ≲ (ρ_crit/ρ_Pl)² ≃ 0.07–0.17
The square of (0.27–0.41) gives (0.073–0.168). Arithmetic checks. But comparing this "energy-density fraction at the bounce" to NANOGrav Ω_GW(f_nHz) ∼ 10⁻⁹ without redshift dilution and transfer function — the author admits this, but if the comparison can't be done, why include Eq. 20 as a "Barrier 12"?

### P1A-N11 (Table I "H₀ = 67.68 ± 1.06"): Posterior values not externally verifiable
Sec. I B labels these "internal-analysis inputs... not... independently peer-reviewable values until Paper I(b) is publicly posted." Tables presenting numbers should either cite external published values or move to the companion paper.

### P1A-N12 (Table IV, "Verified Value" column for γ): "0.274 (scheme range ∼0.020)"
"Verified" is the wrong word for a scheme-dependent choice. Use "Adopted" or "Selected."

### P1A-N13 (References [9] and [10]): DESI 2024/2025 σ-range
The Abstract states "3.1–4.2σ (dataset-dependent)." Verify against DESI DR2 paper [10]. DR2 reports preference for dynamical DE varying from ∼2.8σ to ∼4.2σ depending on SN sample. The 3.1 lower bound is dataset-specific; cite the specific combination.

### P1A-N14 (Table II caption, p. 13): "B14 is the first-principles theorem that subsumes B8"
The "theorem" is the Bianchi-identity corollary discussed in P1A-E2. Calling a one-line tensorial identity a "first-principles theorem" overstates its content.

### P1A-N15 (Sec. XII A): The "10¹²⁰ to 10⁵" fine-tuning reduction is admitted to be cosmetic
*"The framework has not solved the cosmological constant problem; it has only relocated the fine-tuning into inflationary initial conditions."* If admitted, do not advertise the "10¹²² → 10⁵" reduction in earlier sections (Sec. II C 1) without simultaneously stating it is bookkeeping.

### P1A-N16 (Figure 1 footer): "structurally closed (this paper)" legend annotation
PRD figures should not contain self-referential authorial commentary in legends.

### P1A-N17 (Sec. XV, p. 18): "(a 0.27°/0.03° overall sensitivity number)"
This is the author noting an arithmetic fact about the relevant ratio, but is presented in the conclusions as if it were a model statement. Clean up the prose.

### P1A-N18 (Throughout): Excessive parenthetical hedging
Sentences regularly contain 3–5 levels of nested parentheses with mid-sentence definitions (e.g., Abstract: "(the relative e-fold differential between bounce and CMB horizon-exit; comoving wavenumbers k are constant by definition and only physical scales scale with a⁻¹ ∝ e⁻ᴺ)"). Readability collapses.

### P1A-N19 (Sec. IX C "Scalar-Tensor Universality"): The constraint is essentially the perturbation-transparency result
Barrier 3 and Barrier 14 say the same thing for the scalar sector. The "13 logically-independent" count should be re-audited; B3 and B14 are not independent.

---

## NITs

### P1A-NIT1 Numerous typographic and arithmetic micro-issues
- p. 6 Eq. 2: "γ_SU(2) ≈ 0.274" — Domagała–Lewandowski gives γ_DLM ≈ 0.2375, and Meissner ≈ 0.237. The "0.020 scheme spread" is approximately correct but inflated.
- p. 7: "[(α/M) M_Pl] ∼ 10⁻²" — order-of-magnitude, no derivation.
- p. 11, footnote 1: "(α_em ≈ 1/137)" parenthetical is a small touch but unnecessary mid-equation.
- p. 19 Appendix B "the small offset reflects" — reword to avoid editorial tone.

### P1A-NIT2 Author affiliation
"Independent Researcher, Los Angeles, California, USA" — fine for arXiv but PRD typically expects an institutional affiliation. Not blocking.

---

## Specific arithmetic recomputations
- f_NL/σ = 4.375/0.7 = 6.25σ → matches paper's "Fisher-ideal" claim ✓
- e^32 from N_tot=92 − N_exit=60 → matches ✓
- α_em/(4π) = 0.0073/12.57 = 5.8×10⁻⁴ → paper's "more precisely ≈ 5.8×10⁻⁴" ✓ but earlier "5×10⁻⁴" is rounded
- H₀/M_Pl = 1.5×10⁻³³ eV / 1.22×10²⁸ eV = 1.2×10⁻⁶¹ → paper alternates between 10⁻⁶⁰ and 10⁻⁶¹ ✗ (P1A-E5)
- ρ_θ at m_θ = H₀: my computation gives ≈4×10⁻¹¹ eV⁴; paper says 2.8×10⁻¹¹ eV⁴ — within factor 1.5; OK
- |0.342 − 0.27|/√(0.03² + 0.094²) = 0.072/0.0987 = 0.729 ≈ 0.73σ ✓
- (ρ_crit/ρ_Pl)² with ρ_crit/ρ_Pl ∈ [0.27, 0.41] gives [0.073, 0.168]; paper says 0.07–0.17 ✓

---

## Summary recommendation

**REJECT**

The paper does not meet the PRD bar on multiple independent axes: (i) the headline "channel-level closure" is openly admitted to be incomplete (omitted Jackiw–Pi and parity-odd four-fermion operators), (ii) one of the four routes (R4) is admitted *not* to be amplitude-closed, (iii) the "central theorem" is a one-line Bianchi-identity corollary that earlier drafts of the same submission got wrong, (iv) all load-bearing numerical results (H₀ posterior, γ_PTA, f_NL forecast, galaxy-spin null, ALP MCMC) are deferred to five companion papers either in preparation or "available upon request," (v) the body contains version-history language ("supersedes," "earlier drafts," "misstated") that has no place in a published paper, (vi) both "surviving predictions" are explicitly stated by the author *not* to be predictions of the framework the paper is about, (vii) the dimensional ansatz underlying the N_tot ≈ 92 fine-tuning calculation is admitted to be aesthetic rather than derived, and (viii) the paper at 21 pages is at least 3× too long for its actual content. The author should either fold the genuinely original observations (≈ Barriers 1, 2, 10, 12 and the inflation/bounce tension argument) into a short PRD note (≤ 6 pages) after companion papers I(b), II, III, IV are posted to arXiv, or resubmit as a Comment/Brief Report once Paper I(b) provides the externally-verifiable numerics. As written, the manuscript is not refereeable in standalone form and should not be published.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Fresh-Eyes Pass

After re-examining the manuscript against the specified failure modes, I find substantial additional issues, particularly in (A) arithmetic, (B) figure/body consistency, (C) equation dimensions, and (E/H) null-hypothesis comparability. The initial review missed several.

---

## New ESSENTIAL Findings

### P1A-E11 (Sec. IV D, p. 10; Sec. XII B, p. 16): Quoted ACT-vs-Planck consistency is arithmetically wrong
The paper states ACT DR6 (β = 0.215° ± 0.074°) is *"consistent within ∼1.4σ"* with WMAP+Planck (β = 0.342° ± 0.094°). The standard frequentist consistency between two independent measurements is

$$Z = \frac{|0.342 - 0.215|}{\sqrt{0.094^2 + 0.074^2}} = \frac{0.127}{0.1196} \approx 1.06\sigma$$

**not 1.4σ.** The 1.4σ figure would only arise from dividing by the WMAP+Planck error alone (0.127/0.094 = 1.35), which is not the standard convention for between-measurement consistency. This is repeated in both Sec. IV D and Sec. XII B. **Fix:** Replace with 1.1σ throughout, or specify the non-standard convention being used.

### P1A-E12 (Figure 1, p. 4): Figure contains stale numerical value already corrected in the body
Figure 1 displays the PTA panel as *"PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)"*. The body (Sec. X G, p. 15; Table IV) explicitly states this value has been **superseded**: *"This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts."* The current real-KDE value is 2.567 ± 0.382. The figure was not updated when the body number was migrated. The figure is therefore actively misleading and contradicts the body of the same paper. **Fix:** Regenerate Figure 1 with γ = 2.567 ± 0.382, or remove the panel.

### P1A-E13 (Eq. 14, Sec. IV B, p. 9): Equation 14 is dimensionally inconsistent as written
$$\Gamma^{\rm parity-odd}_{\rm one-loop} = -\frac{1}{16\pi^2}\frac{\beta(\gamma)}{M_{\rm Pl}}\int d^4x\,\sqrt{-g}\,\partial_\mu\theta(x)\,J^{5\mu}$$

Dimensional accounting: $\beta(\gamma)$ is called *"a slowly varying function of γ"* and γ is dimensionless, so $\beta(\gamma)$ should be dimensionless. Then $[1/M_{\rm Pl}] = -1$, $[d^4x] = -4$, $[\partial_\mu\theta] = [\theta]+1$, $[J^{5\mu}] = +3$. For the action to be dimensionless: $-1 - 4 + [\theta] + 1 + 3 = [\theta] - 1 = 0$, requiring $[\theta] = +1$. But $\theta$ is described as *"the Nieh–Yan pseudoscalar"* which in standard conventions is dimensionless (the NY 4-form integrated to a pseudoscalar phase). With $[\theta]=0$, the action carries dimension $-1$ — inconsistent. Either the $1/M_{\rm Pl}$ should be absent, or $\beta(\gamma)$ must carry hidden mass dimension, in which case the entire Route 2 amplitude estimate downstream (Eq. 15) is dimensionally undefined. The paper explicitly admits Eq. 14 is *"strictly an upper-bound EFT ansatz"* — but an ansatz that is not dimensionally well-formed is not an upper bound at all.

### P1A-E14 (Sec. IV D, p. 10, "ρ_θ ≈ 2.8 × 10⁻¹¹ eV⁴"): Quoted value is the target ρ_Λ, not the formula output
The text inverts $\beta = (\alpha/M)\sqrt{2\rho_\theta/m_\theta^2}$ to $\rho_\theta = m_\theta^2 \beta^2/[2(\alpha/M)^2]$ and plugs in $\alpha/M = 10^{-21}$ GeV⁻¹, $\beta = \beta_{\rm obs} \approx 6\times 10^{-3}$ rad, $m_\theta = H_0 \approx 1.5\times 10^{-33}$ eV. The actual formula evaluation gives:

$$\rho_\theta = \frac{(1.5\times 10^{-33})^2 \cdot (5.97\times 10^{-3})^2}{2 \cdot (10^{-30})^2}\,{\rm eV}^4 \approx 4.0\times 10^{-11}\,{\rm eV}^4$$

The paper quotes $\rho_\theta \approx 2.8\times 10^{-11}$ eV⁴, which is *exactly* $\rho_\Lambda = (2.3\,{\rm meV})^4$ — the **target** value, not the formula output. The author is reporting the desired answer as if it were the calculation. The actual output 4×10⁻¹¹ eV⁴ does land within a factor of ~1.5 of $\rho_\Lambda$, so the qualitative conclusion ("matches within a factor of unity") survives, but the *quoted number is not the calculation*. **Fix:** Quote the formula output 4×10⁻¹¹ eV⁴ and then compare to ρ_Λ ≈ 2.8×10⁻¹¹ eV⁴, stating the agreement factor explicitly.

---

## New MAJOR Findings

### P1A-M15 (Sec. IV B, Eq. 15, p. 9): Direct recomputation does not yield "10⁻⁵⁸ to 10⁻⁶⁰"; only the lower end is reproducible
Plugging in: $\alpha_{\rm em}/(4\pi) = 5\times 10^{-4}$, $H_0/M_{\rm Pl} = 10^{-61}$, $M_{\rm Pl}(\alpha/M) = 10^{-2}$, $\beta_{\rm obs} = 6\times 10^{-3}$:

$$\frac{\Delta\theta_{\rm one-loop}}{\Delta\theta_{\rm obs}} = \frac{5\times 10^{-4}\cdot 10^{-61}}{10^{-2}\cdot 6\times 10^{-3}} \approx 8\times 10^{-61}$$

The "10⁻⁶⁰" end of the range matches; **the "10⁻⁵⁸" end is two orders of magnitude away from any reproducible value** of the displayed formula. The paper attributes the 2-OOM spread to *"ε-correction perturbative-order scaling alone"* — but a perturbative ε correction is by definition O(1), not O(100). The "factor-of-~100 ambiguity" claim is unsupported.

### P1A-M16 (Table I, p. 4 + Sec. III B, p. 8): "Recovers ΛCDM" obscures a 3.6σ Hubble tension with SH0ES
Table I reports H₀ = 67.68 ± 1.06 km/s/Mpc and claims this *"Recovers ΛCDM"* under the row "H₀/σ₈ tension resolution?" SH0ES gives H₀ = 73.04 ± 1.04. The internal MCMC posterior is in $3.6\sigma$ tension with SH0ES:

$$\frac{73.04 - 67.68}{\sqrt{1.04^2 + 1.06^2}} = \frac{5.36}{1.485} \approx 3.6\sigma$$

The phrase "recovers ΛCDM" misframes this as a *resolution* of tension rather than what it actually is: the MCMC recovers Planck-only values and therefore *inherits the full Hubble tension*. Cited reference [41] (Liu et al., 2025) is invoked as *"EC torsion fits the S₈ tension"* yet the paper's own MCMC does not address this tension. **Fix:** Replace "Recovers ΛCDM" with "Recovers Planck-only ΛCDM; Hubble tension at 3.6σ with SH0ES unchanged."

### P1A-M17 (Sec. VII, footnote 1, p. 11 + Sec. XIII): "σ(fNL) ≈ 1.0 after systematics → 3–5σ realistic" — the 5σ upper end is unrecoverable
With template-overlap correction r ≈ 0.84, the corrected signal is $|f_{\rm NL}|\cdot r = 4.375\cdot 0.84 \approx 3.675$. Divided by σ(fNL) ≈ 1.0 (post-systematics), the realistic SNR is $\approx 3.7\sigma$. The "5σ" end of the "3–5σ realistic" range would require σ(fNL) ≈ 0.7 (Fisher-ideal) *together with* the template correction r = 0.84 *and* post-systematic σ — these conditions are mutually exclusive. The honest realistic number is ~3.7σ, not "3–5σ". **Fix:** Either narrow to "3.5–4σ realistic" or document which combination of inclusions gives 5σ.

### P1A-M18 (Eq. 6 vs Eq. 10 vs Figure 2): Three different presentations of the same dimensional ansatz, only Appendix B admits the inconsistency
- Eq. 6 (Sec. II A 2) presents $S_{\rm eff}$ as a local operator of mass dimension +1.
- Eq. 10 (Sec. II C) presents $\Lambda_{\rm eff} = \Xi M_{\rm Pl}^2 + c_\omega \omega^2$ as if it were the EFT prediction.
- Figure 2 (p. 5) plots a clean hierarchy $M_{\rm Pl}^4 \to \rho_{\rm vac} \sim [(\alpha/M)M_{\rm Pl}]M_{\rm Pl}^4 \to \Lambda_{\rm obs}$ as if dimensionally consistent.
- Only Appendix B admits the operator is dimension +1, not +4, and labels the relation a *"phenomenological on-shell scaling ansatz"*.

The body (Sec. II C, Sec. XII A) and Figure 2 do not flag the ansatz nature at the point of presentation. The reader is led through three dimensional presentations before being told in Appendix B that none of them are derivations. **Fix:** Add the ansatz disclaimer at Eqs. 6, 10, and in the Figure 2 caption.

### P1A-M19 (Sec. IX A, Eq. 18): Mass-coupling-lock formula derivation is asserted, not shown
$g_{\rm eff} \sim 1/(M_{\rm Pl}\sqrt{|t_3|}) \sim H_0/M_{\rm Pl} \sim 10^{-61}$ requires $\sqrt{|t_3|} = M_{\rm Pl}/H_0 \sim 10^{61}$. The PGT parameter $t_3$ is not defined in the paper. The connection between "Poincaré gauge theory ultralight torsion modes" and the specific functional form $1/(M_{\rm Pl}\sqrt{|t_3|})$ is not derived. Either cite a PGT review where this lock is established, or derive.

### P1A-M20 (Sec. III B, p. 8): The galaxy spin null is reported to *contradict* a prior published claim, but the actual significance of the contradiction is delegated to a companion
*"refutes Shamir's claimed 3% asymmetry at high significance"* — but "high significance" is not quantified in this paper. The actual p-value is *"p_LEE < 10⁻⁴"* in Table IV, which is sourced to Paper IV [23]. A formal refutation of a published claim requires showing the test statistic. As written, the refutation cannot be evaluated.

### P1A-M21 (Table III header + footnote ‡, p. 16): The whole table is logically vacuous given the current state of the w₀w_a chain
Footnote ‡ states the free-w₀w_a chain *has not converged* (Rˆ−1 ≈ 3×10⁻² vs publication target 10⁻²) and explicitly *"none of these rows carry a posterior-preference verdict against (or for) the DESI w₀w_a evidence."* The entire "w₀w_a DESI" column is therefore empty of evidential content. Combined with the inconsistent use of ✓ / × / — across rows (Quintom-B alone gets "consistent" while matter-bounce gets a ✓ that contradicts its own footnote), Table III conveys no usable model-discrimination information. **Fix:** Drop the w₀w_a column entirely until the chain converges.

---

## New minor / Notation findings

### P1A-N14 (Sec. III A, Eq. 12): The CMB EB equation has no role in the paper after its statement
Eq. 12 ($C_\ell^{EB} \approx 2\beta(C_\ell^{EE} - C_\ell^{BB})$) is the standard isotropic-birefringence formula. The text immediately concedes *"Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here."* The equation does no work. Either derive the connection or remove the equation.

### P1A-N15 (Sec. II C, Eq. 10, p. 6): $c_\omega \omega^2$ term is introduced and then immediately dismissed
*"CMB isotropy bounds give $(\omega/H)_0 < 5\times 10^{-11}$ [21], making rotation completely negligible."* If the rotation term is observationally negligible, why include it in the headline Λ_eff parameterization? It clutters the equation and serves no purpose beyond signaling the "rotating black hole universe" framing. Drop or absorb.

### P1A-N16 (Sec. IX A, "$\delta m_T^2/m_T^2 \sim 10^{-120}$"): Sign convention for fine-tuning ratio is non-standard
The fine-tuning hierarchy $M_{\rm Pl}^2/H_0^2 \sim 10^{122}$ is normally written as positive (i.e., the natural scale is *larger* than observed by 10¹²²). The paper writes $\sim 10^{-120}$, i.e., the inverse convention. The exponent magnitude (120 vs 122) also doesn't quite match the standard CC hierarchy of 10¹²² in ρ or 10⁶¹ in m². Either pick the standard convention or justify the variant.

### P1A-N17 (Sec. II A 2, Eq. 5 vs Eq. 6): Form vs component normalization differs without comment
Eq. 5 is written as $S_{\rm eff} = (\alpha/M)\int e^I\wedge e^J\wedge \mathcal{F}_{IJ}[K,\mathring{R}]$ (differential form). Eq. 6 is the component reduction $\int d^4x\sqrt{-g}\,(\alpha/M)\epsilon^{\mu\nu\rho\sigma}e^I_\mu e^J_\nu \mathcal{F}_{IJ\rho\sigma}$. The factor of $1/(4!)$ or similar that distinguishes the wedge-product integration measure from the explicit ε contraction is not shown. This affects the dimensionful coefficient by O(10) and propagates to Eq. 7's "$\sim 10^{-2}$" estimate.

### P1A-N18 (Sec. II C 1, "Reheating thermal-reset barrier", p. 7): The claim "r.m.s. residual scales as $\sqrt{n_\psi}/T_{\rm reh}^{1/2}$" is dimensionally suspicious
With $[n_\psi] = +3$ and $[T_{\rm reh}] = +1$, $\sqrt{n_\psi}/T_{\rm reh}^{1/2}$ has dimension $+3/2 - 1/2 = +1$, not the dimensionless ratio one would expect for a "relative residual". Either the formula is missing a normalization (e.g., divided by $n_\psi$ itself), or the dimensional sketch is inconsistent.

### P1A-N19 (Sec. IV B, p. 9): "$\alpha_{\rm em}/(4\pi) \approx 5\times 10^{-4}$" then qualified as "more precisely $\approx 5.8\times 10^{-4}$"
Both numbers used in the same sentence. The OOM closure is presented as robust to the discrepancy, but the parenthetical "more precisely" suggests the author noticed and did not commit. Pick one.

### P1A-N20 (Sec. XV, Conclusions item 2): "~9σ" LiteBIRD sensitivity quoted as "$0.27°/0.03°$"
This is sensitivity vs the **null β = 0**, not against the WMAP+Planck central. The same paragraph then correctly notes the model-discrimination test gives only 0.73σ. The juxtaposition of "~9σ" and "0.73σ" without explicit per-σ null-hypothesis labels at every appearance violates the comparability requirement (this partially overlaps P1A-E4 but here the labeling is at least *present*; the Abstract version is unlabeled).

### P1A-N21 (Reference [44], arXiv:2603.13924): arXiv identifier from March 2026
The submission date is June 8, 2026. arXiv ID 2603 corresponds to March 2026, so it is in principle possible, but should be sanity-checked against the actual posting. References [41] (2507.04265), [42] (2507.09228), [43] (2509.03508), [4] (2205.13962), [5] (2509.13654), and [10] (2503.14738) all have arXiv IDs that should be cross-verified against the actual published versions, especially given the manuscript's dependence on these for the parity-violation case.

### P1A-N22 (Figure 2 caption, p. 5): Caption labels the ansatz as "energy density hierarchy" but the figure's y-axis units / decade labels are not specified in the displayed structure
The figure shows arrows between density labels (M_Pl⁴, ρ_bounce, ρ_vac, Λ_obs) but the relative spacing is not stated. The caption admits *"This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action"* — so the figure is essentially a cartoon of an ansatz. As such it should not be labeled "Energy density hierarchy" as a quantitative statement.

---

## Summary of fresh-eyes findings

Four additional ESSENTIAL issues (P1A-E11 through P1A-E14): an arithmetically wrong σ-consistency, a figure carrying superseded numbers, a dimensionally inconsistent equation, and a quoted "calculation" that is actually the target value substituted backward.

Seven additional MAJOR issues (P1A-M15 through P1A-M21): non-reproducible upper end of Route-2 amplitude budget, Hubble-tension misframing, non-reproducible upper end of fNL forecast, missing ansatz disclaimer at three of four presentation points, asserted but underived PGT formula, unquantified refutation claim, vacuous w₀w_a table.

Nine additional minor findings on equation-dimension consistency, redundant equations, sign conventions, arXiv ID verification, and figure/caption claims.

The pattern across the fresh-eyes findings is consistent with the initial review's overall verdict: the manuscript shows signs of incomplete revision, dimensional sloppiness, and a willingness to quote target values as calculation outputs. The recommendation remains **REJECT**.