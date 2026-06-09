# P1A auto-2026-06-09_1042pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12776 chars)
**Wall time**: 639.8s

---

# Referee Report — Physical Review D submission

**Manuscript:** "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"
**Author:** H. Golden (Independent Researcher)

---

## Overall assessment

This is a 23-page manuscript whose central technical content reduces to: (a) the elementary observation that the Holst dual contraction ε^μνρσ R_μνρσ vanishes identically on a torsion-free connection by the algebraic Bianchi identity (a textbook fact, known since Holst 1996), and (b) a heavily hedged "channel-level" amplitude survey of four routes by which ECH might source dark energy, all four of which the author admits rest on a *phenomenological scaling ansatz* of off-shell mass dimension +1 rather than +4 (Appendix B). The paper itself states, repeatedly and in the abstract, that the dark-energy mapping is "not a derivation," that the four routes are "not proven to be a complete operator basis," that two key parity-odd operators (Jackiw–Pi gravitational Chern–Simons R∧R̃, parity-odd four-fermion partner) are explicitly **excluded** from the enumeration, that the "surviving predictions" are **not** predictions of ECH, and that the load-bearing companion MCMC, Fisher forecasts, ALP fits, NANOGrav reanalysis, and galaxy-chirality results are all in five separate "in preparation" companion papers ([2], [6], [23], [46], [47]) that the referee cannot examine.

Stripped of these hedges, the paper closes nothing definitively, derives nothing, and predicts nothing that is unique to ECH. The prose is buried in self-citation, internal-bookkeeping language ("13 logically-independent, 14 catalog entries, B8 subsumed by B14"), and corrections of "earlier-version" errors that should not be visible in a submitted manuscript. This is not at the level expected for PRD.

---

## ESSENTIAL findings

### P1A-E1 — Central "theorem" is trivial and not new (§X, p. 15–16)
The "perturbation-transparency theorem" is: if matter has zero spin density, then T=0, the connection is Levi–Civita, and the Holst dual contraction vanishes by the algebraic Bianchi identity R_μ[νρσ]=0. This is a textbook one-line observation, known since at least Holst (1996) and explicit in every review of Einstein–Cartan with bosonic matter. The footnote on p. 16 even admits "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density" — i.e. the author corrected a basic confusion mid-draft. The result is not novel and does not warrant being the headline central result.
**Required fix:** Demote from "central result" to a one-paragraph remark with proper attribution, or withdraw the novelty claim.

### P1A-E2 — Five load-bearing companion papers are "in preparation" (refs [2], [6], [23], [46], [47])
The abstract, conclusions, and Table IV depend on numerical results that are *not in this manuscript*: H0 = 67.68 ± 1.06, ∆Neff = −0.020 ± 0.169, σ8 = 0.803 ± 0.008, 309,189 MCMC samples, fNL Fisher forecasts of 3–5σ, NANOGrav γ = 2.567 ± 0.382 from "real-KDE GPU MCMC", galaxy chirality at 8.47M galaxies with p_LEE < 10⁻⁴, ALP MCMC with 9,720 accepted samples. None of these are verifiable from what is submitted.
**Required fix:** Either (i) include the load-bearing analyses as appendices in this manuscript, or (ii) remove every numerical claim that depends on them and rewrite the paper as a pure theoretical no-go. The current form is unreviewable.

### P1A-E3 — Dark-energy mapping is admitted to be a phenomenological ansatz, not a derivation (Appendix B, p. 21)
Equation (B2): "ρ_Λ^bounce ∼ (α/M) M_Pl^5 ∼ 10⁻² M_Pl^4 ... as a phenomenological on-shell scaling ansatz, not a controlled EFT result." The leading operator of Eq. (6) has off-shell mass dimension +1, *three units short of what a local Lagrangian density requires*. The entire Ξ ∼ 10⁻¹²³ → Ntot ≈ 92 chain rests on this dimensional patch. The abstract still presents the "closure" as if it constrains a derived framework.
**Required fix:** State in the abstract — not buried in Appendix B — that no derivation of ρ_Λ from the ECH action exists, and that the no-go applies to a phenomenological ansatz the author himself supplies.

### P1A-E4 — Four-route enumeration is admitted to be incomplete (§IV "Scope", p. 8–9; abstract)
The author explicitly excludes the Jackiw–Pi gravitational Chern–Simons term R∧R̃ and the parity-odd four-fermion partner of R1 (carrying γ_BI/(γ²_BI+1)·8πG). The paper then markets itself as "channel-level closure of the four enumerated minimal-ECH dark-energy routes". For a no-go result this is fatal: a no-go that **a priori** excludes two of the most important parity-odd operators in the ECH action is not a no-go. R∧R̃ is, in fact, the canonical parity-odd gravitational operator in any discussion of cosmic birefringence.
**Required fix:** Either close R∧R̃ and the parity-odd four-fermion partner, or recast the paper as "amplitude bounds on a partial subset of channels". Title and abstract must reflect the incompleteness.

### P1A-E5 — R4 closure is by naturalness, not amplitude — and the prior amplitude claim is silently corrected (§IV D, p. 10–11)
The paper states: "R4 is therefore *not* closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H0 to also produce ρ_Λ". I.e., with α/M floated as a free phenomenological parameter, the spectator-ALP class **does** reproduce both β_obs and ρ_Λ. The paper itself concludes: "R4 therefore relocates the cosmological-constant problem rather than solving it. The inequality is rigid only under the one-loop matching assumption; with α/M floated, the spectator-ALP class is recovered as a viable parity-odd source". This is not a closure — it is an admission that route R4 is viable and that the no-go fails on its only observationally-relevant channel.
**Required fix:** Honestly state that R4 is not closed, that the no-go is therefore at most 3-route, and rewrite the abstract.

### P1A-E6 — "Surviving predictions" are explicitly not ECH predictions (abstract; §XIII, p. 18–19)
The abstract markets fNL = −35/8 and β ≈ 0.27° as testable signatures, then immediately states: "The two predictions discussed below as 'surviving' are accordingly *not* predictions of ECH itself, but bounce-class and GR+ALP-class observables." This is intellectually incoherent: the paper trumpets observables that it admits don't come from the theory under discussion. Either they are predictions of ECH (in which case the no-go is incomplete) or they are not (in which case they have no place in an ECH paper's headline list).
**Required fix:** Remove fNL and β from any list of ECH predictions. Confine them to a "context" paragraph.

### P1A-E7 — Inconsistent σ-significance claims for the LiteBIRD test (§XV, p. 20)
The conclusions claim LiteBIRD will detect non-zero β at "∼ 9σ (a 0.27°/0.03° overall sensitivity number)" *and* will distinguish spectator-ALP from current data at "≈ 0.73σ". These are two different null hypotheses presented side-by-side without the kind of explicit qualification PRD requires. Per reviewer instruction (rule 7), this juxtaposition is ESSENTIAL.
**Required fix:** Either remove the 9σ figure entirely (it is a sensitivity number against the wrong null) or label every juxtaposition with "not directly comparable: different null hypotheses".

### P1A-E8 — Structural-tension argument is internally circular (§I.A item 2; §XIV D, p. 20)
The paper claims a "structural tension" between Ntot ≈ 92 e-folds required for dark-energy suppression and the fNL = −35/8 erasure threshold Ntot ≳ 60. But (a) Ntot ≈ 92 is *fitted* (Table IV, "fitted"), not predicted; (b) the dark-energy mapping that requires Ntot ≈ 92 is admitted to be a phenomenological ansatz (E3); (c) the fNL prediction is admitted not to be from ECH (E6). The "structural tension" is therefore between a tunable parameter in an admitted ansatz and an observable from a different theory class. This is not a tension; it is a tautology.
**Required fix:** Withdraw the "structural tension" claim or recast it as a parameter-choice incompatibility within a phenomenological model.

### P1A-E9 — R2 amplitude estimate has an unaddressed factor-of-10²⁵ ambiguity (§IV B, p. 9–10)
The paper computes two estimates of the R2 induced birefringence differing by 25 orders of magnitude: "10⁻⁵⁸ to 10⁻⁶⁰" in one ordering, "10⁻³³" in another, depending on how H₀ is contracted with M_Pl. The author asserts "the qualitative closure statement... is robust to this choice". A 10²⁵ ambiguity is not robust — it indicates the dimensional reduction is not actually controlled. The "factor-of-∼100 ambiguity reflects ε-correction perturbative-order scaling alone" phrase is empty.
**Required fix:** Do the dimensional reduction correctly once. State the unique answer. Stop labelling 10²⁵ discrepancies as "robust".

### P1A-E10 — Half-integer power in Eq. (11) is admitted to be "dimensional-analysis aesthetic" (§II C 1, p. 7)
The (T_reh/M_GUT)^(3/2) factor that load-bears the fine-tuning-reduction claim is explicitly described as "dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function," and "treated as a phenomenological phase-space ansatz, not as derivable from the one-loop anomaly coefficient." The headline "fine-tuning reduction from 10¹²² to 10⁵" therefore rests on an undefined exponent.
**Required fix:** Either derive the 3/2 from the parity-odd phase-space integral, or remove the "fine-tuning reduction" headline.

---

## MAJOR findings

### P1A-M1 — Internal-bookkeeping prose in the body and abstract
Throughout the manuscript: "13 logically-independent constraints / 14 historical catalog entries / of which B8 is subsumed by B14 per the perturbation-transparency result / retained for historical mechanism-class completeness". This appears in the abstract, §I.A, §IX, Table II caption, and §XV. This is internal review/version-history language. A reader does not need to know that B8 "is retained in the catalog for historical mechanism-class completeness" — they need to know the count of logically-independent barriers, once.
**Required fix:** State the actual count (13 or 14) and remove all "historical / superseded / earlier version / retained for completeness" prose.

### P1A-M2 — Multiple footnote acknowledgements of "earlier-version" errors visible in the submitted manuscript
Page 1 footnote: "Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion..." Page 16 footnote 3: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density." Appendix B: "the ∼ 35 misstated in earlier drafts." These do not belong in a submitted paper.
**Required fix:** Remove all version-history acknowledgements.

### P1A-M3 — Figure 5 caption / panel mismatch (p. 13)
Figure 5 has two panels: (top) "Renormalization Group Running of α/M", (bottom) "Dark Energy Fine-Tuning Comparison" bar chart (ΛCDM 10¹²⁰ / Quintessence 10⁶⁰ / f(R) 10⁴⁰ / Spin-Torsion 10⁵). The caption labels the figure "Naturalness landscape for the four minimal-ECH dark-energy routes (R1 NJL, R2 one-loop effective action, R3 Immirzi running, R4 parity-CMB spectator-ALP)" and describes a (mass × coupling) plane with naturalness window — *which neither panel shows*. Caption and figure are unrelated.
**Required fix:** Either replace the figure to match the caption or rewrite the caption to describe what is actually plotted.

### P1A-M4 — Figure 3 caption discusses cosmic rotation but plot shows Hubble parameter evolution (p. 6)
The figure shows H(z) for ΛCDM vs spin-torsion (essentially indistinguishable, with a ~10⁻²² contribution annotated). The text caption begins "Cosmic rotation ω vs Hubble expansion H" but the figure is an H(z) plot with a residual axis. The caption then admits "negligible at all redshifts" — so the figure shows nothing.
**Required fix:** Either remove the figure (it conveys no information) or align caption with content.

### P1A-M5 — α/M to canonical g_aγ conversion has 10× discrepancy (footnote 1, p. 10)
The author admits the paper's α/M = 10⁻²¹ GeV⁻¹ does not match the canonical ALP–photon coupling g_aγ at the natural identification (off by ~10×), and resolves this by "either a sub-Planckian decay constant f_a ∼ M_Pl/10 or an amplified photon-coupling coefficient c_γ ∼ O(10); both are non-trivial UV-completion assumptions not derived in this paper." The R4 closure depends on the matching of these two couplings.
**Required fix:** State this dependence in the body, not in a long footnote, and acknowledge that R4 is sensitive to the unspecified UV completion.

### P1A-M6 — Barbero–Immirzi "scheme range ~0.020" is not a statistical uncertainty (Table IV; §II A 1)
The paper repeatedly reports γ = 0.274 with an apparent ±0.020. Section II A 1 admits this is "scheme dependence rather than a statistical or theoretical error," that DLM does not quote ±0.020, and that "the ~0.020 figure is the spread between counting prescriptions, retained as an effective range only." This is then carried into Table IV's "Verified Value" column where it reads as an uncertainty. The Table footer does not flag the distinction.
**Required fix:** Remove the ±0.020 from the Verified Value column, or explicitly label as "scheme range" inline.

### P1A-M7 — DESI 3.1–4.2σ claim is loose (§I, p. 3; §XIV D, p. 20)
"DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9, 10]." The DESI DR1 (2024) and DR2 (2025) papers report specific dataset combinations with explicit σ values; the "3.1–4.2σ" range is presented without specifying which datasets. DESI DR2 reports up to 4.2σ for specific combinations including DES-SN5YR, ~2.8σ for others. The range as stated is not precisely traceable.
**Required fix:** Either cite specific dataset combinations with their actual σ values, or remove the range and quote a single representative figure.

### P1A-M8 — Equation (18) dimensional inconsistency (§IX A, p. 14)
Equation 18: g_eff ∼ 1/(M_Pl √|t_3|) ∼ H_0/M_Pl. If t_3 is the dimensionless PGT coupling, then 1/(M_Pl √|t_3|) has dimension −1, but g_eff is dimensionless. To recover H_0/M_Pl on the right, t_3 would need to be dimensionful or H_0 must appear explicitly. As written the chain doesn't work.
**Required fix:** Show the derivation; identify t_3; restore dimensional consistency.

### P1A-M9 — ρ_crit window 0.27–0.41 ρ_Pl is not a published LQC range (§II B, p. 6)
The paper acknowledges: "this lower value is an internal extrapolation across counting schemes (not a value quoted in Ref. [11])". Yet 0.27–0.41 ρ_Pl is presented throughout the paper (Table I, Sec II B, Eq. 20) as if it were a standard LQC range.
**Required fix:** Use only the published Ashtekar–Singh ρ_crit ≃ 0.41 ρ_Pl as the canonical value; mark the 0.27 extrapolation as the author's scheme choice.

### P1A-M10 — Eq. (14) one-loop operator is undecidably "motivated" (§IV B, p. 9)
"Motivated by (but *not literally derived in*) the Holst+non-minimal-fermion construction of Mercuri and Mercuri & Capozziello — those works establish the classical structure of the Holst term coupled to fermions and the Nieh–Yan invariant, not this exact one-loop operator — we adopt the phenomenological one-loop parity-odd operator". The Route-2 amplitude bound is based on this operator. If the operator is not derived, the bound is not a bound on the actual one-loop physics.
**Required fix:** Either cite a published derivation of this specific operator or label R2 as an EFT-ansatz amplitude estimate rather than a closure.

### P1A-M11 — Eq. (16) Immirzi running is an EFT ansatz, contradicting Benedetti–Speziale (§IV C, p. 10)
The paper writes a chiral-loop ansatz dγ/d ln μ = (N_F^L − N_F^R)γ/(12π²), then admits the actual perturbative calculation by Benedetti & Speziale [27] gives a β-function with a different sign-and-magnitude structure. The R3 closure is based on the ansatz, not on the actual published result.
**Required fix:** Use the Benedetti–Speziale result directly, or label the bound as a chiral-count EFT estimate and reconcile.

### P1A-M12 — Length disproportion (entire manuscript)
The actual technical content (Holst Bianchi-vanishing + four amplitude estimates, all of which are admitted to be EFT ansätze) does not justify 23 pages. The structural arguments could be presented in ~10–12 pages with the MCMC and observational claims moved to the companion paper that already exists.
**Required fix:** Compress to ≤ 12 pages. Remove all sections that depend on companion-paper numerics until those papers are public.

### P1A-M13 — Table III footnotes admit no-test rows masquerading as a comparison table (p. 17)
Three of five rows in the w0wa DESI column are "not tested" with a long footnote explaining that the relevant MCMC chain has accumulated only ∼3.8 × 10⁴ samples and reports R̂−1 ≈ 3 × 10⁻² (not converged). The table presents these alongside a Quintom-B "consistent" row with the footnote disclaimer that this is "consistent at the model level rather than a posterior-preference ✓." This is not a comparison; it is a placeholder.
**Required fix:** Remove the w0wa DESI column until the chain converges, or remove the table entirely.

### P1A-M14 — Numerical claim ρ_θ ≈ 2.8 × 10⁻¹¹ eV⁴ "to within a factor of unity" of ρ_Λ — author admits R4 reproduces ρ_Λ (§IV D, p. 11)
The arithmetic checks: at α/M = 10⁻²¹ GeV⁻¹, β = 6 × 10⁻³ rad, m_θ = H_0 ≈ 1.5 × 10⁻³³ eV, the predicted ρ_θ matches ρ_Λ. This is the *failure* of R4 as a no-go, dressed as a closure. See E5.

### P1A-M15 — Footnote 2 (p. 12) Fisher-σ arithmetic is internally inconsistent
"σ(f_NL) ≈ 0.7 Fisher-ideal (raw ratio |f_NL|/σ = 4.375/0.7 ≈ 6.25σ, degraded to ∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84 between the matter-bounce shape and the local/equilateral basis, before further GR-projection and b_ϕ degradation)". A 0.84 template-overlap correction takes 6.25σ to 6.25 × 0.84 ≈ 5.25σ — consistent. But this then goes to "3–5σ realistic" with no quantitative budget. The path from 5.25σ → 3–5σ is unjustified.
**Required fix:** Provide the explicit systematic budget or remove the 3–5σ claim.

---

## MINOR findings

### P1A-N1 — Duplicate / inflated phrasing
- Abstract: "channel-level closure" appears 4× in the abstract alone.
- §IV: "channel-level enumeration, not an operator-level basis" appears in §IV scope paragraph and again in §IV E "Closure summary".
- "logically-independent" appears 6× in the abstract.
- "phenomenological ansatz" / "phenomenological scaling ansatz" appears 12+ times.

### P1A-N2 — Acknowledgements declare extensive AI assistance
"The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation." Transparent, but combined with the volume of repetitive prose, internal-bookkeeping language, and disposable footnotes (P1A-M1, P1A-M2, P1A-N1), suggests heavy LLM authorship that the editorial process should weigh.

### P1A-N3 — Reference [44] arXiv:2603.13924 (Cai & Zhu, "Smoking-gun signatures of bounce cosmology...", 2026)
The arXiv ID 2603.xxxxx corresponds to March 2026, which is plausible relative to the June 2026 paper date. The reference should be verifiable; flagging only because it cannot be cross-checked in the present review.

### P1A-N4 — Table I "PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)" in Figure 1 is inconsistent with §X G
Figure 1 quotes "3.20 ± 0.42" while §X G states the value has been migrated to "γ = 2.567 ± 0.382 from real-KDE re-analysis" and that the 3.20 ± 0.42 figure is "superseded". Figure 1 should be updated.

### P1A-N5 — Figure 4 axis labels not legible; lacks units and explicit σ definition
The "Detection Significance Forecast" axis is unlabelled with respect to which σ procedure is used.

### P1A-N6 — Reference [31] annotation in bibliography
"canonical quintom-cosmology review (two-field DE with w crossing -1). Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism..." — this is internal notes prose, not a bibliography entry.

### P1A-N7 — Eq. (20) compares bounce-epoch Ω_GW to present-day Ω_GW(f_nHz) — author admits non-comparison
The author notes this directly: "is not directly comparable to the present-day PTA spectral-density measurement... A quantitative comparison... is deferred to a forthcoming bounce-GW dedicated paper". Barrier 12 therefore does not bind against NANOGrav as the paper implies.

### P1A-N8 — Eq. (22) phrasing "∆v = 0 (identically)"
Trivial restatement: if T = 0 then GR follows, so of course GW polarizations are identical. Does not warrant a numbered equation.

### P1A-N9 — Conclusions: arithmetic check
"|0.342 − 0.27|/√(0.03² + 0.094²) ≈ 0.072°/0.0987° ≈ 0.73σ" — checks out. But the comparison is between a *consistency benchmark* (0.27°, not predicted) and an *observed value* (0.342°), so the 0.73σ has no model-discrimination interpretation.

---

## Summary recommendation

**REJECT**

The manuscript's headline result is a textbook identity (Holst dual vanishes on a torsion-free connection by Bianchi) that the author himself admits to having confused with the Pontryagin density in an earlier draft. Its "four-route no-go" explicitly excludes the two most relevant parity-odd operators (R∧R̃, parity-odd four-fermion), and its fourth route (R4 spectator-ALP) is admitted in the body to actually *reproduce* both β_obs and ρ_Λ at the fitted coupling — i.e., R4 is not closed. The dark-energy mapping that underwrites the entire "Ntot ≈ 92" structural-tension argument is admitted in Appendix B to be a phenomenological ansatz of the wrong mass dimension, patched on shell. The "surviving predictions" (fNL = −35/8 and β ≈ 0.27°) are explicitly stated to **not** be ECH predictions. All load-bearing numerical claims (MCMC, Fisher, NANOGrav, galaxy chirality, ALP fits) are deferred to five companion papers "in preparation" that the referee cannot examine. The manuscript is 23 pages of repetitive prose, internal-bookkeeping ("13 logically-independent / 14 historical catalog entries / B8 subsumed by B14"), version-history footnotes that should not appear in a submitted paper, and a figure (Fig. 5) whose caption is unrelated to its panels. Even granting every hedge in the abstract, the paper does not establish a no-go, does not predict anything unique to ECH, and does not derive its own central scaling relation. This is not at the threshold for PRD and would require a complete rewrite — including, at minimum, closing R∧R̃, honestly handling R4, deriving (or removing) the dimensional ansatz of Appendix B, and excising the companion-paper dependencies — before resubmission could be considered. Recommended maximum length on resubmission: 12 pages.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Second Pass (Fresh Eyes)

I performed the requested systematic re-examination focused on arithmetic, figure/text concordance, dimensional consistency, cross-references, null-procedure mixing, abstract faithfulness, novelty support, hedging, appendix/main-text alignment, and stale numbers. I found a number of additional issues that escaped the first pass. The new findings, none of which duplicate items already in the initial report, are below.

---

## ADDITIONAL ESSENTIAL findings

### P1A-E11 — Arithmetic error: Eskilt vs ACT-DR6 tension is 1.06σ, not "∼1.4σ" (§IV D, p. 10; §XII B, p. 18)
The paper twice describes the WMAP+Planck vs ACT DR6 comparison "β = 0.342° ± 0.094° ... comparable to ... β = 0.215° ± 0.074° at ∼2.9σ, consistent within ∼1.4σ". Recomputing with the standard combined error:

|0.342 − 0.215|/√(0.094² + 0.074²) = 0.127°/√(0.008836 + 0.005476) = 0.127°/0.1197° = **1.06σ**

Not 1.4σ. The number 1.4 corresponds to dividing only by σ_Eskilt = 0.094° (0.127/0.094 = 1.35), i.e. ignoring the ACT uncertainty entirely — not a standard convention. Since this comparison is used to claim the two parity-odd birefringence measurements are mutually consistent, the underlying number must be correct.
**Required fix:** Replace "∼1.4σ" with the correct combined-error value (~1.06σ) wherever it appears.

### P1A-E12 — Figure 2 uses N = 55 e-folds while body text uses Ntot ≈ 92 (Fig. 2, p. 5; §II C 1; §XII A; Appendix B)
Figure 2 ("Energy density hierarchy: Planck scale → observed Λ_obs") explicitly labels the inflationary-dilution arrow with "× e^(−3N) (∼10⁻⁷²)" and "After inflationary dilution (N = 55 e-folds)". Cross-checking: e^(−3×55) = e^(−165) ≈ 10⁻⁷². But every other section of the paper requires Ntot ≈ 92, with e^(−3×92) ≈ 10⁻¹²⁰. The figure therefore illustrates a scenario that fails to bridge the M_Pl⁴ ↔ ρ_Λ hierarchy by ~50 orders of magnitude — i.e. it does not actually depict the mechanism the body claims. This is a load-bearing schematic carrying a stale e-fold count from an earlier version of the manuscript.
**Required fix:** Regenerate Figure 2 with N = 92 (and the correct ∼10⁻¹²⁰ dilution annotation), or remove it.

### P1A-E13 — The "10⁻⁵⁸ to 10⁻⁶⁰" range in Eq. (15) is not what the arithmetic gives (§IV B, p. 9–10)
The paper writes "Δθ_one-loop/Δθ_obs ∼ 10⁻³ · 10⁻⁶¹/(10⁻² · 6×10⁻³) ∼ 10⁻⁵⁸ to 10⁻⁶⁰". Recomputing:
- numerator = 10⁻³ × 10⁻⁶¹ = 10⁻⁶⁴
- denominator = 10⁻² × 6×10⁻³ = 6×10⁻⁵
- ratio = 1.7×10⁻⁶⁰ ≈ **10⁻⁶⁰**

The "10⁻⁵⁸" endpoint does not follow from the displayed arithmetic. The author then hand-waves the missing two orders of magnitude as "factor-of-∼100 ambiguity reflects ε-correction perturbative-order scaling alone", which is not a controlled estimate. Combined with the separately admitted 10²⁵ ambiguity to 10⁻³³ in a different ordering (P1A-E9), Route 2's amplitude bound contains undocumented O(100) and O(10²⁵) gaps from a single calculation.
**Required fix:** State the unique value from the stated inputs (∼10⁻⁶⁰) and remove the unjustified upper bound.

---

## ADDITIONAL MAJOR findings

### P1A-M16 — Eq. (10) writes Λ_eff = Ξ M_Pl² but Appendix B uses ρ_Λ = Ξ M_Pl⁴ with the same Ξ
In GR, Λ has mass-dimension +2 (the bare term in Einstein's equations) and ρ_Λ = Λ/(8πG) ∼ Λ M_Pl² has mass-dimension +4. The paper uses both forms interchangeably with the same dimensionless Ξ:
- §II C Eq. (10): "Λ_eff = Ξ M_Pl² + c_ω ω²"
- Appendix B Eq. (B2): "ρ_Λ^bounce ∼ (α/M) M_Pl⁵ ∼ 10⁻² M_Pl⁴" with "ρ_Λ = Ξ M_Pl⁴"

The factor of 8π and the proper Λ-vs-ρ_Λ distinction is silently dropped. For an audience comparing the model's prediction to observations, this is exactly the kind of dimensional slippage that hides a missing M_Pl² factor.
**Required fix:** Use one consistent quantity (either Λ or ρ_Λ) throughout, with the 8πG factor displayed.

### P1A-M17 — Footnote 1 (p. 10) understates the basis-conversion gap; with the displayed inputs it is ~30×, not "roughly 10×"
The footnote computes g_aγ from f_a = M_Pl, c_γ = O(1): "g_aγ ∼ 10⁻²² GeV⁻¹, roughly 10× smaller than the paper's value [10⁻²¹ GeV⁻¹]". But the paper's own Eq. (7) inputs are:
- α ∼ α_em/(4π) ≈ 5.8 × 10⁻⁴
- M = M_Pl/√γ ≈ 1.91 M_Pl ≈ 2.3 × 10¹⁹ GeV (paper's value)
- α/M ≈ 5.8×10⁻⁴/(2.3×10¹⁹ GeV) ≈ **2.5 × 10⁻²³ GeV⁻¹**

This is ~40× smaller than the paper's quoted 10⁻²¹ GeV⁻¹, not 10×. The discrepancy is then folded into "α/M as a phenomenological parameter constrained by data" — but Route R4's coupling-mass tuning argument depends sensitively on whether α/M = 10⁻²¹ is the one-loop value or already a phenomenological fit. If it is fit, the "Mercuri one-loop motivation" claim is decorative.
**Required fix:** State explicitly that α/M = 10⁻²¹ GeV⁻¹ is the data-fit value, not the one-loop estimate (which is ~10⁻²³); the conflation between the two is currently used to argue both naturalness *and* observational matching.

### P1A-M18 — Perturbation-transparency theorem's stated scope (canonical scalar matter) does not apply to the actual cosmological setting in which it is claimed to operate (§X, p. 15–16; abstract; §XV)
The theorem assumes "canonical scalar field matter". §X E correctly notes the theorem fails for "matter [that] includes fermions with nonzero spin density". But the universe at every relevant epoch — recombination, large-scale structure formation, late time — contains baryons, electrons, and neutrinos, all of which carry spin density. The abstract and §X F nevertheless declare: "Perturbation observables (C_ℓ^TT, C_ℓ^EE, P_k, bispectrum): Identical to standard GR. No ECH modifications at any order." and "No GW birefringence, no tensor chirality, no TB/EB CMB parity violation from the ECH mechanism." These conclusions do not follow from the theorem because the theorem's premise (vanishing spin density) is not satisfied in the actual cosmology being observed.
**Required fix:** Restrict the claimed consequences strictly to a scalar-only matter content (e.g. inflaton-dominated epoch), or repeat the analysis with the standard cosmological fermion content and a torsion source term proportional to ⟨J⁵_μ⟩.

### P1A-M19 — §XV "below ∼ 0.05° would be needed for LiteBIRD-vs-current-central tension to cross 1σ" — actually ∼0.065° suffices
Solving |0.342 − 0.27|/√(σ_LiteBIRD² + σ_obs²) = 1 with σ_LiteBIRD = 0.03°:
- 0.072° = √(0.0009 + σ_obs²)
- σ_obs² = 0.072² − 0.0009 = 0.00428
- σ_obs ≈ **0.065°**

The "below ∼0.05°" threshold is overly restrictive by ~30%. At σ_obs = 0.05° the tension is already ~1.23σ (computed: 0.072/√(0.0009+0.0025) = 0.072/0.0583).
**Required fix:** Correct the threshold to ~0.065° (or state the calculation explicitly).

### P1A-M20 — "Δγ/γ ∼ 10⁻²" does not follow from Eq. (16) as written (§IV C, p. 10)
Eq. (16): dγ/d ln μ = (N_F^L − N_F^R) γ/(12π²). The paper then claims: "In the Standard Model, the chiral asymmetry is generated by the SU(2)_L doublets; numerically, Δγ/γ ∼ 10⁻² over the running from the GUT scale to the IR."

With the obvious chiral-fermion count (N_F^L − N_F^R = 24 if counting SU(2)_L doublet members against R-singlets, or 0 if counting net Weyl count) and ln(M_GUT/IR) ≈ 92:
- N_F^L − N_F^R = 24: γ(IR)/γ(UV) = exp(24 × 92/(12π²)) ≈ exp(18.6) ≈ 10⁸ → Δγ/γ ≫ 1, not 10⁻²
- N_F^L − N_F^R = 0: Δγ/γ = 0

Neither case gives 10⁻². The claim is therefore not derived from the displayed equation; it is a number inserted to make the subsequent (Δγ/γ)·(H/M_Pl) ∼ 10⁻⁶³ Route-3 amplitude bound work.
**Required fix:** Either justify the 10⁻² value with an explicit calculation matching Eq. (16), or use the actual Benedetti–Speziale β-function (already cited as [27]) which the paper admits has a different sign-and-magnitude structure.

### P1A-M21 — Misattribution: the value 0.342° ± 0.094° was reported by Eskilt & Komatsu (2022), not "first reported by Minami & Komatsu" (abstract; §XII B)
The abstract attributes "β_obs = 0.342° ± 0.094° (∼3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4])". The Minami & Komatsu 2020 paper [3] reported β = 0.35° ± 0.14° from Planck 2018 polarization data, *not* 0.342° ± 0.094°. The 0.342° ± 0.094° value with reduced error bar is the Eskilt & Komatsu 2022 result [4] after improved foreground analysis. The phrasing as written attributes the specific quoted value to the wrong paper.
**Required fix:** Attribute the 0.342° ± 0.094° measurement to Eskilt & Komatsu [4], with Minami & Komatsu [3] cited as the original detection at 0.35° ± 0.14°.

---

## ADDITIONAL MINOR findings

### P1A-N6 — Citation of [17, 18] for γ_SU(2) ≈ 0.274 is non-standard
The paper attributes "the refined SU(2) full counting [17, 18] gives γ_SU(2) ≈ 0.274" to Domagała & Lewandowski [17] and Meissner [18], but those two papers gave γ_DLM ≈ 0.2375 (and the paper itself notes "the further Domagała-Lewandowski-Meissner refinement gives γ_DLM ≈ 0.2375"). The 0.274 value is from a different, less standard SU(2) counting scheme (sometimes called the "ABCK" or "literal SU(2) horizon-state" prescription). Citing the same authors for both 0.274 and 0.2375 is misleading.
**Required fix:** Cite the actual source of γ ≈ 0.274 (or note explicitly that 0.274 is the SU(2) full-counting variant *prior* to the DLM refinement).

### P1A-N7 — Branch labels skip I and K (§IX; abstract; throughout)
Branches are labelled H, J, L, M, N, O — missing I and K. This is consistent with a post-hoc renumbering after some originally-numbered branches were closed or merged. The labelling exposes the catalog's evolved-rather-than-systematic structure, which weakens the "logically-independent" framing of §IX.
**Required fix:** Relabel the surviving six branches contiguously (e.g. H1–H6) or explain why I and K are absent.

### P1A-N8 — "Quantity mode" appears to be a typo (abstract, p. 1)
"…a contracting-phase **quantity mode** with k_SPHEREx ∼ 10⁻¹ h/Mpc…" — "quantity mode" is not a term used in cosmology. Likely "quantum mode" or simply "mode".
**Required fix:** Correct the typo.

### P1A-N9 — Conceptual confusion in the e-fold tracking of k_SPHEREx (§I A item 2; §XIV D)
The formula k_bounce^phys = k_SPHEREx^phys × e^(N_tot − N_exit) implicitly treats k_SPHEREx^phys as the physical scale *at horizon exit*, not the physical scale *today* (which is the natural reading of k_SPHEREx^phys). The two differ by a^post-inflation/a_today ∼ e^60 of post-inflation expansion. The conceptual conclusion (SPHEREx modes were deep sub-horizon at the bounce) is qualitatively correct, but the displayed arithmetic is misleading: k_bounce^phys is actually e^(N_tot) × k_comoving × (a_today/a_bounce), not e^(N_tot − N_exit) × k_SPHEREx^phys.
**Required fix:** Clarify which scale-factor convention is in use, or just state the conclusion (sub-horizon at the bounce) without the misleading formula.

### P1A-N10 — Figure 6's "Galaxy Spins" curve appears in a *forecast* figure, but the body declares galaxy spin a confirmed null
Figure 6 ("Detection Significance Forecast", p. 18) plots three forecast curves over 2024–2034: CMB ε-B, Galaxy Spins, Combined (ρ = 0). The galaxy-spin curve rises monotonically to ~4σ by 2034. But §III B and §V both declare galaxy spin a *confirmed null* (Paper IV, hemisphere null at p_LEE < 10⁻⁴). A forecast curve for a confirmed null doesn't make sense.
**Required fix:** Remove the galaxy-spin curve from the forecast figure (and the "Combined" curve that depends on it), or relabel the figure to indicate galaxy spin is a null channel rather than a developing detection.

---

## Summary of new findings

- 3 additional ESSENTIAL findings (arithmetic error 1.4σ→1.06σ; Figure 2 stale e-fold count; Eq. 15 range unjustified)
- 6 additional MAJOR findings (dimensional schizophrenia Λ vs ρ_Λ; basis-conversion gap 10× understated; perturbation-transparency scope vs cosmological matter content; 0.05° threshold off by ~30%; Δγ/γ ∼ 10⁻² doesn't follow; misattribution to Minami-Komatsu)
- 5 additional MINOR findings (γ ≈ 0.274 citation; branch-label gaps; "quantity mode" typo; e-fold tracking conceptual slip; Figure 6 forecasts a confirmed null)

These additions sharpen the overall verdict from the initial review: the paper's central numerical results — the 1.4σ Eskilt-vs-ACT consistency, the 10⁻⁵⁸ to 10⁻⁶⁰ Route-2 bound, the Δγ/γ ∼ 10⁻² Route-3 bound, the 0.05° LiteBIRD threshold, and Figure 2's N = 55 schematic — each fail to follow from the inputs the paper itself displays. The dimensional sloppiness between Λ and ρ_Λ (P1A-M16) and the perturbation-transparency scope mismatch (P1A-M18) further indicate that the structural conclusions are looser than the prose suggests. Combined with the original findings, the manuscript requires substantial revision before it can be evaluated as a serious technical contribution.