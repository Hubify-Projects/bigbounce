# INT Referee Report — P2 (independent Claude-stack leg)

- **Model:** claude-opus-4-8 (subagent, independent referee leg)
- **Date:** 2026-07-16 (PT)
- **Paper:** P2 — "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping"
- **Version:** v1.7.122
- **pdf_sha256:** 4097bac5a9930df7fa73e4a4567a7c60156f6cadb4321e51146dd237e13225c9
- **PDF path:** research/focused_paper_source_integration/02_full_draft.pdf
- **Venue / profile:** Physical Review D — PRD-RESEARCH
- **Scope reviewed:** entire manuscript, all 10 pages (main text §§I–X + Appendices A, B)

**PARSED VERDICT: MAJOR REVISIONS**

---

## (1) VERDICT

**MAJOR REVISIONS.**

The manuscript is technically careful and unusually honest about its own limits.
The internal algebra I could check by hand is self-consistent (Table V per-vertex
sums reproduce −35/16 squeezed and −255/128 equilateral; Eq. (B2)'s −(99/128)Σkᵢ³
shift maps the exact vertex sum −35/16 to the printed polynomial's actual reduction
−305/64; the Li et al. c_s=1 arithmetic −165/16 + 65/8 = −35/16 checks). The central
algebraic value therefore appears supported and independently corroborated. It falls
short of ACCEPT / MINOR for two substantive reasons: (i) the novel scientific content
for a PRD *Research Article* is thin — the headline number −35/16 already follows from
Li et al. (2016)'s published general-c_s formula at c_s=1, which the paper itself uses
as a cross-check, so the genuinely new material is an *incomplete* reconciliation of a
transcription discrepancy the paper cannot fully close; and (ii) the observational
section builds a multi-significant-figure apparatus (Table III ladder, RSD multipole
recovery ratios, orientation-grid convergence) on an in-house surrogate covariance that
explicitly does not reproduce the unavailable true SPHEREx per-triangle covariance,
making those quantitative outputs un-validatable. Both are fixable with substantial
revision, hence MAJOR rather than REJECT.

---

## (2) ISSUES

### [MAJOR] 1 — Novelty / significance for a PRD Research Article (Abstract; §II B; §IX Discussion; App. B)
The paper's stated primary contribution is "the exact contraction-phase amplitude
derivation" giving f_NL^local = −35/16. But the paper's own cross-check (App. B, and
§II B "−35/16 agrees independently with Li et al. [8] at c_s=1") shows that Li et al.
(2016), Eq. (5.1), f_NL = −165/16 + 65/(8c_s²), already yields −35/16 at c_s=1. The
number is therefore *not new*: it is present in the published literature. The genuinely
novel content reduces to a vertex-by-vertex re-summation reconciling why Cai et al.'s
*printed* polynomial differs — which, per Issue 2, the paper cannot fully close. As
written, the manuscript's framing ("corrects the unreproduced printed −35/8 literature
value," abstract) overstates the novelty relative to a value Li et al. already published.
The authors should (a) reframe the headline as *confirming/adjudicating between* Li et al.
(−35/16) and Cai et al.'s printed −35/8, and (b) make an explicit case that the vertex-level
reconciliation clears the significance bar for a Research Article rather than a Comment or
short note. This bears directly on the accept decision at PRD.

### [MAJOR] 2 — The central "correction" narrative is incomplete: −35/8 is never reconstructed, and the printed polynomial actually reduces to −305/64 (§II B; App. B, Eqs. (B2), (B8))
The paper establishes three *distinct* numbers: the exact vertex sum −35/16 (−2.1875);
Cai et al.'s *separately stated* −35/8 (−4.4375); and — crucially — the value Cai et al.'s
*transcribed printed polynomial* (their Eq. 37) actually squeezed-reduces to, which the
paper computes as −305/64 (−4.766), NOT −35/8. The manuscript honestly discloses (p. 7)
that it "do[es] not claim to have reconstructed how the separately stated −35/8 arose."
The result is that the paper's own decisive object (the printed polynomial) does not match
either the exact sum *or* the stated literature value, and one of the three numbers (−35/8)
is left entirely unexplained. This weakens the "replaces −35/8" claim to the weak sense of
"our sum disagrees with a value we cannot reproduce." For a PRD paper whose headline is a
literature correction, the authors should either (a) fully account for the origin of −35/8
(convention/symmetry-factor/typo trace), or (b) explicitly restructure the claim around the
robust triangulation (vertex sum = Cai ε-grouped intermediates = Li et al. formula = −35/16),
demoting −35/8 to a flagged unreconciled discrepancy. Note the factor-of-two flavor
(−35/8 = 2×(−35/16)) is exactly the kind of ambiguity that lives in the in-in "2 Im⟨ζ³H⟩"
commutator / six-Wick symmetry factors the paper itself discusses (Eqs. B6–B9); a referee
will want the −35/8 origin pinned, not just the −35/16 asserted.

### [MAJOR] 3 — The observational forecast rests on an un-validatable in-house surrogate covariance (§IV; §VII; Table III)
The paper states the external SPHEREx per-triangle covariance from Heinrich et al. is
"unavailable" and that its channel-native covariance is an in-house leading-order Gaussian
multi-tracer surrogate that "does not replace the unpublished external per-triangle
covariance." Consequently the entire Table III significance ladder (3.47σ → 3.14σ → 2.32σ →
0.42σ), the redshift-space recovery ratios (r_eff = 0.9953 / 0.9991), the primordial-only
run (0.9981), and the orientation-grid convergence (1.4×10⁻⁶ fractional) are all computed
against a covariance the authors constructed, never validated against the real survey
covariance. Yet they are presented at three-to-four significant figures, which conveys a
precision the surrogate cannot support. The only genuinely survey-anchored observational
statement is the 2.63σ arithmetic scaling of the *published scalar* σ(f_NL)=0.7 through the
recovery fraction. Recommendation: either (a) obtain/reconstruct a defensible approximation
to the true covariance and validate the surrogate against it, or (b) substantially trim
§§IV/VII to the one defensible scalar map plus a clearly-labeled *directional* sensitivity
note, and drop the high-precision digits. The current hedging language ("illustrative,"
"conditional") is honest but does not cure the precision-vs-validity mismatch.

### [MINOR] 4 — f_NL convention chain not explicitly closed for the survey map (§II A Eq. (2); §III A; §IV)
The bounce amplitude is defined with B_NL = (10/3) A_T/Σkᵢ³ (Cai/Li convention), while the
mapped survey number uses Heinrich et al.'s σ(f_NL^local). §III A does the ζ = ζ_g +
(3/5)f_NL(...) bookkeeping and states "no additional factor of 3/5," but the manuscript never
states in one place that the (10/3)-convention −35/16 is numerically identical to the local
f_NL convention in which Heinrich et al. quote σ=0.7. Since this is the load-bearing 2.63σ
number, add one explicit sentence confirming the convention identity (or the conversion
factor), so the reader need not reconstruct it.

### [MINOR] 5 — Citation inconsistency for the −35/16 attribution (§I Introduction)
The Introduction attributes "the negative local amplitude f_NL = −35/16 [7–9]," but Ref. [7]
(Cai et al.) is precisely the source of the *printed* −35/8 that the paper argues is wrong.
Citing [7] as a source *for* −35/16 contradicts the paper's own thesis. Attribute −35/16 to
Li et al. [8] (and this work), and cite Cai [7] separately as the printed −35/8 to be corrected.

### [MINOR] 6 — Proliferation of near-unity recovery/overlap ratios is confusing (Abstract; §IV B; §VII)
The manuscript carries at least six distinct near-unity quantities: r = 0.8354 (flat-grid),
r = 0.84±0.02 (adopted), r_cos = 0.9817 (shape cosine), 0.876 (signal-only endpoint),
r_eff = 0.9929/0.9986 and 0.9953/0.9991 (survey-weighted / RSD), and 0.9981 (primordial-only).
Even with the disclaimer that "the two quantities use different inner products and are not
interchangeable," this is hard to follow and risks conflation. Consolidate into a single
labeled table giving each symbol, its definition/inner product, and its value.

### [MINOR] 7 — Abstract phrasing "before the nonsingular transition" (Abstract; §II B; §II C assumption d)
The −35/16 is a *pre-bounce* amplitude; the observable f_NL depends on faithful cubic
transmission through the bounce, which the paper explicitly does NOT compute (only linear
transfer is verified, assumption (d)). The abstract does say "conditional on faithful cubic
transmission," so this is largely handled, but ensure no sentence (abstract or conclusion)
can be read as asserting −35/16 is the *observable* amplitude.

### [MINOR] 8 — Grid dependence of the flat-grid r not quantified (§IV B; Fig. 1)
r = 0.83542294 is quoted on a "23,098-triangle ratio grid" to eight significant figures, but
its sensitivity to grid/k-range choice is not reported (only the RSD *orientation* grid gets a
convergence check). Either report an r stability estimate under grid variation or quote r to a
precision the grid actually justifies.

### [MINOR] 9 — Appendix A prior-volume scans retained "only as provenance artifacts" (App. A)
If the Bayesian summary-likelihood scans are not used in any conclusion, consider removing them
to reduce reader confusion; if retained, state the competitor-width W dependence of BF ∝
W/√(σ_eff²+σ_theory²) in-line so the reader sees the scans are competitor-width driven and not
a forecast.

---

## (3) Is the central claim supported?

The **central algebraic claim** (f_NL^local = −35/16 from the exact four-vertex matter-contraction
sum) appears supported: it is internally self-consistent on every arithmetic check I could perform
by hand and is independently corroborated by Li et al. (2016) at c_s=1 — though it is largely a
*confirmation* of an already-published value rather than a new result, and the paper cannot fully
reconstruct the −35/8 it claims to correct; the **observational claims** are explicitly conditional
and, apart from the single survey-anchored 2.63σ scalar map, rest on an un-validatable in-house
surrogate covariance.
