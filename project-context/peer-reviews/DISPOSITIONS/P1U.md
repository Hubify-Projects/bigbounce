# Canonical dispositions — P1U (as of v1U.0.11, 2026-07-10; H17G ledger-audit appended)

One numbered entry per DISTINCT finding-class. Duplicates across reviewers/rounds are
merged. Source: `EXT_real/H17_2026-07-10/P1U_truth_audit.md` (body + INT re-test,
EXT re-test, and INT retest2 addenda). Reviewers cited: EXT ChatGPT, EXT Grok,
INT OpenAI/gpt-5.5, INT Grok/grok-4.3, INT Claude-subagent. Load-bearing tex line
numbers spot-checked against current `arxiv/paper1_unified.tex` v1U.0.11 and updated.

### DP1U-01: Check D / torsion-current normalization (S·S sign + factor-16)
- **class:** CLOSED-BY-EDIT (v1U.0.11)
- ChatGPT: footnote below Eq.(torsion) gives `S_abc S^abc = -3/8 J5²` but Check D / O4–O5 reduction printed `6 J5²` — sign error + factor-of-16 discrepancy.
- Real internal inconsistency, VERIFIED. The footnote's carefully-derived `S^abc=¼ε^abcd J5_d ⟹ S_abc S^abc = -3/8 (J5·J5)` (Lorentzian `ε_abcd ε^abce = -3! δ`, L1810-1811) was propagated to both restatements (O4/O5 reduction L1958; Check D L4883). Structural conclusion unchanged (O4→κ²(J5·J5), O5→κ(J5·J5), same M_Pl⁻² power). No fabrication — only propagates the paper's own footnote value.
- **fingerprint:** Check D, S·S, torsion-current normalization, -3/8, factor-16, sign error, J5², epsilon contraction

### DP1U-02: κ / M_Pl convention (M_Pl=G^{-1/2} vs 8πG=M_Pl^{-2}, κ vs κ²)
- **class:** CLOSED-BY-EDIT (v1U.0.11)
- ChatGPT #19, OpenAI-grok minor, Claude, OpenAI retest2 MIN #14: `κ ≡ 8πG = M_Pl⁻²` with unreduced `M_Pl=G^{-1/2}` is mathematically wrong (8πG=8π M_Pl⁻²≠M_Pl⁻²).
- Confirmed error, fixed. Convention block now states `κ ≡ 8πG = 8π M_Pl⁻² = M̄_Pl⁻²` with `M̄_Pl=(8πG)^{-1/2}=M_Pl/√(8π)` reduced (L2103-2109); the compact `κ=M_Pl⁻²` shorthand flagged as reduced-mass sense (8π factor immaterial to OOM budgets). κ² usage (=16πG, Shapiro–Teixeira) already correctly attributed.
- **fingerprint:** kappa convention, reduced Planck mass, M_Pl, 8πG, kappa vs kappa-squared, unreduced

### DP1U-03: Eq.(1) variational hybrid (¼T·T displayed but not varied)
- **class:** RE-FLAG-DISCLOSED (clarity edit v1U.0.10)
- ChatGPT #2, OpenAI-grok #1, OpenAI retest MIN #15/#3, ChatGPT retest: ¼T·T shown on-shell but "not an independent kinetic term"; claim Eqs.(3)–(4) not derived from written action.
- Already disclosed (footnote; body): Eq.(1) is first-order Palatini–EC varied over {e,ω,ψ} with ¼T·T "not varied," appearing only after on-shell torsion elimination; Eqs.(3)–(4) derived from connection variation. Clarity: two-step off-shell→effective reading added inline after Eq.(1) (v1U.0.10, L1683+). No physics change.
- **fingerprint:** Eq(1), variational hybrid, T·T not varied, on-shell shorthand, Palatini, Cartan, two-step reading

### DP1U-04: Eq.(16) V·A parity-odd partner provenance (FMT: minimal coupling → no V·A)
- **class:** CLOSED-BY-EDIT (v1U.0.10)
- ChatGPT, OpenAI-grok #2, ChatGPT retest (F2 finite-γ contorsion): V·A `J·J⁵` term presented as arising at finite Barbero–Immirzi from minimal torsion elimination — contradicts Freidel–Minic–Takeuchi (minimal coupling → axial–axial only; V·A only under non-minimal).
- Real citation/internal inconsistency, closed by claiming less. V·A partner relabeled a *non-minimal* operator everywhere (abstract L1225-1234; §r1_parityodd_partner; completeness lemma; Fierz appendix), with explicit FMT citation + "non-minimal coupling only" tag. Strengthens the no-go (one fewer minimal operator; partner still κ=M_Pl⁻² suppressed). Pure reclassification, no fabrication.
- **fingerprint:** V·A partner, Freidel-Minic-Takeuchi, FMT, non-minimal coupling, parity-odd, finite Immirzi, J·J5

### DP1U-05: Route 1 NJL closure — ⟨J5⟩=0 ⇏ ⟨J5 J5⟩=0 / vacuum condensate
- **class:** RE-FLAG-DISCLOSED (scope sentence added v1U.0.10)
- ChatGPT, OpenAI-grok #5, OpenAI retest #10, ChatGPT retest: mean-vanishing doesn't exclude variance; no regulated gap-equation / effective-potential NJL vacuum-condensate exclusion.
- Already conceded in-paper: variance ⟨J⁵J⁵⟩ permitted as incoherent thermal contribution, no coherent w=−1, bounded by leg (i). Route-1 claim scoped to finite-density mean-field bound + no coherent w=−1 (§r1_njl, L2589+). Explicit sentence added that a fully regulated NJL vacuum condensate via gap-equation/effective-potential is NOT claimed excluded — honest out-of-scope open item (see DP1U-19).
- **fingerprint:** Route 1, NJL, gap equation, effective potential, vacuum condensate, J5 variance, w=-1, finite-density

### DP1U-06: Four-route closure = channel-level, not operator-level theorem
- **class:** RE-FLAG-DISCLOSED
- OpenAI #1/#7/#12, OpenAI-grok, Grok #1, OpenAI retest #1, Grok retest #1: "four-route closure not a well-defined theorem / channel-vs-operator-level inconsistent / interpretive survey."
- Abstract + title already headline this: title "Under Stated Assumptions" (L1190); "channel-level assessment, not an operator-level theorem" (L1219, L1389-1390); evidentiary-tier table explicit. Exactly the reviewers' point, disclosed — not an editable error.
- **fingerprint:** channel-level, operator-level theorem, four-route, well-defined theorem, under stated assumptions, interpretive survey

### DP1U-07: O1–O6 basis completeness / Nieh–Yan redundancy / not complete diffeo basis
- **class:** RE-FLAG-DISCLOSED
- OpenAI #3/#4, OpenAI-grok #4, ChatGPT, Grok, OpenAI retest #1, Grok retest #1: basis not complete/independent; omits derivative/multi-flavor/curvature-torsion/non-minimal irreps; Nieh–Yan redundancy.
- Completeness argued *analytically* via F1 (torsion algebraic/non-propagating) + F2 (minimal coupling → axial current) + NDA monotonicity (L2448-2467), with the two tensor identities symbolically checked; abstract wording softened to say the SCRIPT verifies the two identities, not completeness (L1226-adjacent). Non-minimal/derivative/multi-species irreps explicitly OUT-OF-SCOPE. Not over-claimed.
- **fingerprint:** O1-O6, basis completeness, Nieh-Yan, diffeomorphism-invariant basis, F1, F2, NDA monotonicity, non-minimal irreps

### DP1U-08: dim +1 → +4 promotion / N_tot 92-vs-94 sensitivity / Eq.(6) dimensional
- **class:** RE-FLAG-DISCLOSED
- OpenAI #2/#3, Grok-EXT M2, Claude, OpenAI retest #2, ChatGPT retest (Eq.6 dim-1 / Bianchi): +1→+4 dressing artifact; Eq.(6) dimensionally incomplete; N_tot spread.
- The +1→+4 dressing is labeled "dispensable illustrative heuristic, not load-bearing" (L1877-1892-adjacent comments; the +1→+4 named a property of the on-shell reduction, L1223); genuine dim-4 O1–O6 basis is primary. N_tot spread is disclosed bookkeeping (L1757-adjacent). No over-claim.
- **fingerprint:** dim+1, +1-vs-+4, dimensional promotion, N_tot 92, Eq(6), Bianchi, illustrative heuristic, bookkeeping

### DP1U-09: Route 2 one-loop parity-odd (ansatz vs derivation, ∂ϑ bookkeeping)
- **class:** RE-FLAG-DISCLOSED
- OpenAI-grok #6, Grok-EXT, OpenAI #4, OpenAI retest #5, ChatGPT retest: R2 Eq.(17) phenomenological; ∂ϑ dimension / field-excursion vs instantaneous-rate; birefringence anomaly-chain not justified.
- Dimensions explicitly correct (∂ϑ dim +2, operator dim +4); ∂ϑ∼H substitution + alternative-ordering loose bound disclosed. Route labeled "exploratory framing, not load-bearing" (L2919/L3381-adjacent). One-loop-grounded via Shapiro–Teixeira coefficients (v1A.0.108→109), absolute normalization honestly pending the ST Riccati flow.
- **fingerprint:** Route 2, one-loop, parity-odd, ∂ϑ dimension, Shapiro-Teixeira, exploratory framing, birefringence, ansatz

### DP1U-10: Route 3 Δγ → dark-energy / (H0/M_Pl) mapping is ansatz
- **class:** RE-FLAG-DISCLOSED (SCOPE)
- OpenAI #8, OpenAI-grok #7, OpenAI retest #6: R3 Δγ/γ→(H0/M_Pl) mapping asserted not derived.
- R3 is the one cleanly-integrated β-function result (|Δγ/γ|≈1.4e-6); the H0/M_Pl amplitude-budget mapping is flagged conditional. Honestly disclosed as amplitude-budget framing.
- **fingerprint:** Route 3, Delta gamma, beta-function, H0/M_Pl, amplitude budget, Immirzi running, conditional

### DP1U-11: Route 4 naturalness-vs-exclusion (ALP, m~H0, CC relocation)
- **class:** RE-FLAG-DISCLOSED
- OpenAI #9/#10, OpenAI-grok #8, Grok-EXT, Grok #3, OpenAI retest #7, ChatGPT retest, Grok retest: R4 not closed by amplitude mismatch; ALP φFF̃ imported; m~H0 generic quintessence naturalness; "relocates CC problem."
- Abstract explicitly states R4 is "NOT closed by amplitude mismatch but by an explanatory-deficit / CC fine-tuning objection ... relocating the CC problem rather than solving it" (L1195-1198). Spectator-ALP benchmark disclosed as imported. This IS the paper's verbatim framing — exactly the reviewers' point, not over-claimed.
- **fingerprint:** Route 4, ALP, φFF-tilde, naturalness, CC relocation, explanatory-deficit, quintessence, m~H0

### DP1U-12: transparency / B8-subsumption (standard scalar equivalence, novelty)
- **class:** RE-FLAG-DISCLOSED (OPINION on novelty)
- OpenAI #11, OpenAI-grok #11, Claude, Grok #4, OpenAI retest #8, Grok retest #2, Grok-EXT: transparency = standard on-shell scalar-zero-spin-density equivalence, not novel; B8-subsumption asserted without order-by-order perturbed-Holst verification.
- Labeled the "standard on-shell equivalence," narrow "solid positive core" for canonical scalar matter, explicitly excluding fermions/torsion/dynamical-γ (Claude verified-correct, L1248/L3333-adjacent). B8-subsumption disclosed at sec:barriers head. Novelty is referee-preference, not an editable error.
- **fingerprint:** transparency, perturbation transparency, B8 subsumption, canonical scalar, on-shell equivalence, novelty, perturbed-Holst

### DP1U-13: 13-barrier catalog independence
- **class:** RE-FLAG-DISCLOSED
- ChatGPT #13, OpenAI #13, OpenAI-grok #10, Grok-EXT minor2, OpenAI retest #9, Grok retest #3: 13 barriers not independent/comparable status.
- Exemplary disclosure at sec:barriers head: "no barrier is a logical consequence of another ... not a claim that thirteen separately decisive theorems each independently exclude." B8 subsumed by B14, B9 heuristic, B5/6/7/10/13 general — all flagged. No edit needed.
- **fingerprint:** 13 barriers, 14 catalog, independence, logical consequence, separately decisive, B8 subsumed by B14, sec:barriers

### DP1U-14: D_inf non-derivation, a^{-6} scaling, N_tot ansatz, matter-bounce erasure
- **class:** RE-FLAG-DISCLOSED
- OpenAI #14, OpenAI-grok #9, OpenAI retest #11, ChatGPT retest, Grok retest #5: D_inf phenomenological not derived; a^{-6} vs a^{-3}; N_tot≈92 ansatz; erasure claimed "definitively."
- D_inf explicitly "mathematical scaffolding" after reheating resets the axial mean (disclosed); a^{-6} concerns the erased channel already conceded not a dynamical prediction; N_tot spread disclosed bookkeeping (L1757-adjacent). Honest.
- **fingerprint:** D_inf, mathematical scaffolding, a^-6 scaling, N_tot 92, matter-bounce erasure, reheating reset

### DP1U-15: Appendices E–H don't test ECH (stock-CAMB / synthetic-sky / imported)
- **class:** RE-FLAG-DISCLOSED
- OpenAI #15, OpenAI-grok #13, ChatGPT, OpenAI retest #12/#18, ChatGPT retest: observational appendices provide no ECH test (stock-CAMB proxy / synthetic-sky / ALP import).
- Each appendix explicitly labeled a stock-CAMB proxy / synthetic-sky validation / companion import, "not an ECH test" (Claude verified; L5537-adjacent). Honestly bounded.
- **fingerprint:** appendices E-H, stock-CAMB proxy, synthetic sky, NaMaster, not an ECH test, MCMC, evidentiary value

### DP1U-16: Companion-reliance / self-containedness / future-dated refs
- **class:** RE-FLAG-DISCLOSED
- OpenAI #13, ChatGPT (single-action / Eq.(10) not from Eq.(1) / N_tot), OpenAI retest #13/#16/#20, ChatGPT retest: depends on companions/repo artifacts/future-dated refs; not self-contained.
- Self-containment paragraph: no theorem depends on companion numerics; artifacts reproducible-now via `\cite{BigBounceRepro}` archive + explicit paths (frozen Cobaya chains, NaMaster MC, catalogs); TODO-SUBMISSION arXiv-ID markers pending same-day insertion (L1413-adjacent). Reproducible-now, not "cannot be refereed until posted."
- **fingerprint:** self-containment, companion reliance, in-preparation, BigBounceRepro, future-dated refs, arXiv-ID, reproducible-now

### DP1U-17: f_NL = −35/16 vs Cai −35/8 self-containedness
- **class:** RE-FLAG-DISCLOSED (companion-resolved)
- OpenAI-grok minor, Claude, OpenAI retest #11, ChatGPT retest: −35/16 vs Cai's −35/8; companion title still −35/8.
- Value used consistently (L1289, L1303, L1471, L1487, L1493, L3479, L3492); historical Cai −35/8 is a deliberately-cited comparison. The P2 companion (v1.7.95) resolves the Cai-Li factor-of-two (spurious +(99/128)Σk³ term) → −35/16, quadruple-certified. Self-containedness disclosed as companion dependency.
- **fingerprint:** f_NL, -35/16, -35/8, Cai, matter-bounce signature, factor-of-two, P2 companion, SPHEREx

### DP1U-18: "every admissible" / "symbolic verification" wording (minors)
- **class:** CLOSED-BY-EDIT (v1U.0.10)
- Claude MINORs: "every admissible" verdict over-scoped; abstract "symbolic verification" implied a completeness proof.
- "Every admissible" softened to "within the enumerated set at the stated power-counting order," excluding Fierz-caveat non-enumerated classes (L4827-adjacent). "Symbolic verification" reworded to "two load-bearing tensor identities verified symbolically ... not a completeness proof, which is argued analytically" (L1226-adjacent). O4 table dim ambiguity resolved with an explicit note (physics unchanged).
- **fingerprint:** every admissible, symbolic verification, enumerated set, power-counting order, O4 table note, Fierz caveat

### DP1U-19: Regulated NJL vacuum-condensate exclusion (out of scope)
- **class:** OPEN-VENUE (honest scope, not editable)
- OpenAI-grok #5 escalation, OpenAI retest #10: paper does not exclude a fully regulated NJL vacuum condensate via gap-equation / effective-potential.
- Explicitly disclosed as an out-of-scope open item (§r1_njl scope sentence, L2589+; DP1U-05). What IS established: Planck-suppressed finite-density bound + no coherent w=−1. A regulated gap-equation/effective-potential exclusion is genuinely beyond the paper's stated scope — not an editable error.
- **fingerprint:** regulated NJL, vacuum condensate, gap equation, effective potential, out-of-scope, open item

### DP1U-20: Operator-level (vs channel-level) completeness across full diffeo basis
- **class:** OPEN-VENUE (honest scope, not editable)
- OpenAI #1/#3, Grok #1, retests: a full operator-level theorem across the complete diffeomorphism-invariant basis is not proven.
- Honestly disclosed: the result is a channel-level assessment "not an operator-level theorem" (L1219, L1389-1390; DP1U-06/DP1U-07). Full operator-level completeness across the entire diffeo-invariant basis (incl. non-minimal/derivative/multi-species irreps) is out of scope — closing it would require new derivation, not an edit.
- **fingerprint:** operator-level completeness, diffeomorphism-invariant basis, non-minimal, full theorem, out-of-scope

### DP1U-21: Disclosure-backfire — honest scope hedging recast as weakness (pattern-066)
- **class:** BACKFIRE-PATTERN-066
- Grok MAJOR #7 (EXT retest): "repeated disclaimers ('channel-level, not an operator-level theorem', 'not proven to be a complete diffeomorphism-invariant operator basis') sit in tension with 'exhaust' ... this hedging undermines the strength of the claimed closure."
- Canonical disclosure-backfire: honest scope disclosures reinforced across prior rounds to be truthful are recast as a weakness. Not editable — removing the hedging would be dishonest overclaiming. Documented per directive-C.
- **fingerprint:** disclosure-backfire, hedging, honest scope, pattern-066, referee variance, undermines closure, not editable

### DP1U-22: Length / repetitiveness / "should be a Letter" (OPINION)
- **class:** BACKFIRE-PATTERN-066
- OpenAI retest MIN #18/#19, Grok minor / Grok retest #4: 60pp too long/repetitive/self-referential; 14-barrier catalog inflates length; clearer as a Letter.
- Pure venue/style preference, not an editable error. Multiple reviewers echo — recorded as OPINION-class referee variance.
- **fingerprint:** length, 60 pages, repetitive, self-referential, Letter, 14-barrier overhead, style preference

### DP1U-23: LQC ρ_crit range / dataset-provenance minors
- **class:** RE-FLAG-DISCLOSED
- OpenAI retest MIN #16/#13, #17: ρ_crit 0.27–0.41 ρ_Pl mixes LQC area-gap / BH-entropy conventions; birefringence mixes WMAP+Planck/NPIPE/ACT DR6/Gaussian fits.
- Both ρ_crit values attributed to canonical LQC γ-choices, disclosed (L1441/L1472-adjacent; ρcrit block L2024). Birefringence dataset provenance disclosed and kept separate from the model prediction (App G).
- **fingerprint:** rho_crit, LQC, area-gap, BH-entropy, Immirzi choice, birefringence datasets, NPIPE, ACT DR6, provenance

## OPEN ITEMS
| ID | Class | Item | Gate |
|----|-------|------|------|
| DP1U-19 | OPEN-VENUE | Regulated NJL vacuum-condensate exclusion via gap-equation/effective-potential | Out of scope; disclosed in-paper (§r1_njl, L2589+). New derivation, not an edit — Houston-gated / human-referee. |
| DP1U-20 | OPEN-VENUE | Full operator-level completeness across the diffeomorphism-invariant basis (non-minimal/derivative/multi-species irreps) | Out of scope; paper is channel-level by design (L1219, L1389-1390). Human-referee / venue barrier — Houston-gated. |
| DP1U-21 | HOUSTON-GATED | Grok recasts honest scope hedging as weakness (disclosure-backfire) | Not editable (removing hedging = overclaiming). Referee variance — route to human referee, do not re-spin sweeps. |
| DP1U-22 | HOUSTON-GATED | Length/venue OPINION (60pp, "should be a Letter") | Style/venue preference, not an error. Houston-gated venue decision. |

## H17F final-wave (2026-07-10, vs v1U.0.11)
- **Grok EXT = MAJOR** — 10 items all → DP1U-02/06/07/08/09/12/14/16/21/22. Channel-level "overclaim risk" = paper's own verbatim framing (DP1U-06); hedging-as-weakness = DP1U-21 backfire. 0 genuinely-new.
- **ChatGPT EXT = PENDING** (not harvested this wave; prior EXT ChatGPT already 0 genuinely-new).
- No bump; v1U.0.11 stands.

### DP1U-24: Figure statistical presentation (Figs 4/7 assumed correlation ρ; Fig 3 different H0)
- **class:** RE-FLAG-DISCLOSED
- ChatGPT H17G (H17F) MINOR: Figs 4/7 combine significances for unrelated fNL/birefringence estimators "using an arbitrary correlation coefficient without a defined joint likelihood or common hypothesis"; Fig 3 compares models with different imposed H0.
- Already disclosed IN-CAPTION: the ρ curve families are labeled the *assumed* cross-correlation coefficient (ρ=0 uncorrelated baseline; ρ>0 track joint-significance gain) with the physical role stated explicitly (`fig:obs_timeline` caption, arxiv/paper1_unified.tex L3483-3487); the birefringence β comparison is stated as differential against β_obs=0.342°±0.094° (L3491). The raw itself concedes "portions of their captions acknowledge the problem." Figure-presentation OPINION / referee variance — the caption already carries exactly the disclosure requested. Not an editable defect.
- **fingerprint:** Fig 4, Fig 7, correlation coefficient, joint likelihood, arbitrary rho, Fig 3, imposed H0, figure presentation

## H17G ledger-audit wave (2026-07-10, vs v1U.0.11)
- **ChatGPT EXT = REJECT** (raw `H17_2026-07-10/final/P1U_chatgpt_final.md`, on v1U.0.11) — 16 MAJOR + 2 MINOR. Fingerprint-match: 4-route/no-go=DP1U-06; Eq(1)-(4) variational=DP1U-03; Eq(5)-(8) dim+1/+1→+4=DP1U-08; App-B1 basis/O1=O6/Nieh-Yan=DP1U-07; NDA CC-naturalness restatement=DP1U-07/-11; Route-1 NJL ⟨J5⟩⇏⟨J5J5⟩=DP1U-05/-19; Route-2 ϑNY ansatz=DP1U-09; Route-3 Δγ inserted=DP1U-10; Route-4 ALP fixed-vs-floated=DP1U-11; App-C Fierz V⊗A=DP1U-04; quantum-consistency/counterterms=DP1U-07; Sec-X transparency novelty=DP1U-12; Eq(13)/N_tot≃92 dilution=DP1U-14; matter-bounce erasure + −35/8→−35/16=DP1U-14/-17; 13-barrier=DP1U-13; App-E-G don't test ECH=DP1U-15; MINOR figs=DP1U-24; MINOR length/organization=DP1U-22.
- **0 genuinely-new editable findings.** Every MAJOR is a source-cited re-flag of already-disclosed channel-level scope / honest out-of-scope items; both MINORs are disclosed-in-caption / OPINION. Consistent with the ChatGPT structural harsh-referee floor. No bump; v1U.0.11 stands.
