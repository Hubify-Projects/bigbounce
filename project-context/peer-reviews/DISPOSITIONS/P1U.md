# Canonical dispositions — P1U (as of v1U.0.12, 2026-07-11; W2-EXT adjudication appended)

One numbered entry per DISTINCT finding-class. Duplicates across reviewers/rounds are
merged. Source: `EXT_real/H17_2026-07-10/P1U_truth_audit.md` (body + INT re-test,
EXT re-test, and INT retest2 addenda). Reviewers cited: EXT ChatGPT, EXT Grok,
INT OpenAI/gpt-5.5, INT Grok/grok-4.3, INT Claude-subagent. Load-bearing tex line
numbers spot-checked against current `arxiv/paper1_unified.tex` v1U.0.11 and updated.

### DP1U-01: Check D / torsion-current normalization (S·S sign + factor-16)
- **class:** CLOSED-BY-EDIT (v1U.0.11)
- ChatGPT: footnote below Eq.(torsion) gives `S_abc S^abc = -3/8 J5²` but Check D / O4–O5 reduction printed `6 J5²` — sign error + factor-of-16 discrepancy.
- Real internal inconsistency, VERIFIED. The footnote's carefully-derived `S^abc=¼ε^abcd J5_d ⟹ S_abc S^abc = -3/8 (J5·J5)` (Lorentzian `ε_abcd ε^abce = -3! δ`, L1810-1811) was propagated to both restatements (O4/O5 reduction L1958; Check D L4883). Structural conclusion unchanged (O4→κ²(J5·J5), O5→κ(J5·J5), same M_Pl⁻² power). No fabrication — only propagates the paper's own footnote value.
- **fingerprint:** Check D, S·S, torsion-current normalization, -3/8, factor-16, sign error, J5², epsilon contraction, eps-eps=3!delta, verified symbolically, dim4_parityodd_enumeration.py, Lorentzian sign, collapse coefficient

### DP1U-02: κ / M_Pl convention (M_Pl=G^{-1/2} vs 8πG=M_Pl^{-2}, κ vs κ²)
- **class:** CLOSED-BY-EDIT (v1U.0.11)
- ChatGPT #19, OpenAI-grok minor, Claude, OpenAI retest2 MIN #14: `κ ≡ 8πG = M_Pl⁻²` with unreduced `M_Pl=G^{-1/2}` is mathematically wrong (8πG=8π M_Pl⁻²≠M_Pl⁻²).
- Confirmed error, fixed. Convention block now states `κ ≡ 8πG = 8π M_Pl⁻² = M̄_Pl⁻²` with `M̄_Pl=(8πG)^{-1/2}=M_Pl/√(8π)` reduced (L2103-2109); the compact `κ=M_Pl⁻²` shorthand flagged as reduced-mass sense (8π factor immaterial to OOM budgets). κ² usage (=16πG, Shapiro–Teixeira) already correctly attributed.
- **fingerprint:** kappa convention, reduced Planck mass, M_Pl, 8πG, kappa vs kappa-squared, unreduced

### DP1U-03: Eq.(1) variational hybrid (¼T·T displayed but not varied)
- **class:** RE-FLAG-DISCLOSED (clarity edit v1U.0.10)
- ChatGPT #2, OpenAI-grok #1, OpenAI retest MIN #15/#3, ChatGPT retest: ¼T·T shown on-shell but "not an independent kinetic term"; claim Eqs.(3)–(4) not derived from written action.
- Already disclosed (footnote; body): Eq.(1) is first-order Palatini–EC varied over {e,ω,ψ} with ¼T·T "not varied," appearing only after on-shell torsion elimination; Eqs.(3)–(4) derived from connection variation. Clarity: two-step off-shell→effective reading added inline after Eq.(1) (v1U.0.10, L1683+). No physics change.
- **fingerprint:** Eq(1), variational hybrid, T·T not varied, on-shell shorthand, Palatini, Cartan, two-step reading, foundational action inconsistent, torsion-squared inside action, off-shell first-order action, four-fermion derivation, Holst-induced four-fermion, Fierz does not cure, V-A partner nonminimal

### DP1U-04: Eq.(16) V·A parity-odd partner provenance (FMT: minimal coupling → no V·A)
- **class:** CLOSED-BY-EDIT (v1U.0.10)
- ChatGPT, OpenAI-grok #2, ChatGPT retest (F2 finite-γ contorsion): V·A `J·J⁵` term presented as arising at finite Barbero–Immirzi from minimal torsion elimination — contradicts Freidel–Minic–Takeuchi (minimal coupling → axial–axial only; V·A only under non-minimal).
- Real citation/internal inconsistency, closed by claiming less. V·A partner relabeled a *non-minimal* operator everywhere (abstract L1225-1234; §r1_parityodd_partner; completeness lemma; Fierz appendix), with explicit FMT citation + "non-minimal coupling only" tag. Strengthens the no-go (one fewer minimal operator; partner still κ=M_Pl⁻² suppressed). Pure reclassification, no fabrication.
- **fingerprint:** V·A partner, Freidel-Minic-Takeuchi, FMT, non-minimal coupling, parity-odd, finite Immirzi, J·J5

### DP1U-05: Route 1 NJL closure — ⟨J5⟩=0 ⇏ ⟨J5 J5⟩=0 / vacuum condensate
- **class:** CLOSED-BY-COMPUTE (directive-L, v1U.0.14) — was RE-FLAG-DISCLOSED
- ChatGPT, OpenAI-grok #5, OpenAI retest #10, ChatGPT retest: mean-vanishing doesn't exclude variance; no regulated gap-equation / effective-potential NJL vacuum-condensate exclusion.
- **CLOSED v1U.0.14 (directive-L):** the finite-density mean-field concession is upgraded to a *derived* exclusion. New Appendix `app:njl_gap` (leg iii of §r1_njl) presents the regulated NJL gap equation on the paper's own operator −(3/16)κ(J5·J5): (A) Fierz-projecting to the scalar (SS) condensate channel via eq:AAdecomp gives G_scalar=−(3/64)κ<0 → **repulsive** → M=0 is the only effective-potential minimum at ANY coupling/cutoff (no condensate forms); (B) even |G_eff| is far sub-critical vs the derived G_crit=π²/(N_f N_c Λ²) — |G_eff|/G_crit=(3/64)N_f N_c/π²≈4.3e-2 (Nf Nc=9) at Λ=M_Pl, worst case 0.156 scanned, Holst ~30× smaller. **Truth-audit note:** every number verified against `arxiv/scripts/njl_gap_equation_route1.py` + `_results.json` (script self-checks PASS: G_crit symbolic match=True, sign repulsive, worst-case ratio 0.156, subcritical all cases). Nothing fabricated — coefficients are the paper's own (eq:NJL_torsion, eq:AAdecomp), G_crit derived symbolically. Framework assumption (standard mean-field NJL) stated explicitly in-paper. Residual strong-coupling-beyond-mean-field / non-minimal completion stays out-of-scope (unchanged).
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
- **fingerprint:** dim+1, +1-vs-+4, dimensional promotion, N_tot 92, Eq(6), Bianchi, illustrative heuristic, bookkeeping, single-scale NDA, no-go, wrong mass dimension, on-shell curvature dressing, EFT matching, non-adopted benchmark figures, Fig 3-7 illustrative

### DP1U-09: Route 2 one-loop parity-odd (ansatz vs derivation, ∂ϑ bookkeeping)
- **class:** RE-FLAG-DISCLOSED
- OpenAI-grok #6, Grok-EXT, OpenAI #4, OpenAI retest #5, ChatGPT retest: R2 Eq.(17) phenomenological; ∂ϑ dimension / field-excursion vs instantaneous-rate; birefringence anomaly-chain not justified.
- Dimensions explicitly correct (∂ϑ dim +2, operator dim +4); ∂ϑ∼H substitution + alternative-ordering loose bound disclosed. Route labeled "exploratory framing, not load-bearing" (L2919/L3381-adjacent). One-loop-grounded via Shapiro–Teixeira coefficients (v1A.0.108→109), absolute normalization honestly pending the ST Riccati flow.
- **fingerprint:** Route 2, one-loop, parity-odd, ∂ϑ dimension, Shapiro-Teixeira, exploratory framing, birefringence, ansatz, literature attribution overstated, related work, Holst/Nieh-Yan papers, one-loop papers, imply stronger support, anomaly-chain, Eq(17) phenomenological

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
- **fingerprint:** 13 barriers, 14 catalog, independence, logical consequence, separately decisive, B8 subsumed by B14, sec:barriers, heterogeneous constraints, cumulative barrier catalog, mechanism-class, Sec X B logical slip, total derivative contributes nothing, Holst contraction vanishes pointwise, 13/14-barrier phrasing

### DP1U-14: D_inf non-derivation, a^{-6} scaling, N_tot ansatz, matter-bounce erasure
- **class:** RE-FLAG-DISCLOSED
- OpenAI #14, OpenAI-grok #9, OpenAI retest #11, ChatGPT retest, Grok retest #5: D_inf phenomenological not derived; a^{-6} vs a^{-3}; N_tot≈92 ansatz; erasure claimed "definitively."
- D_inf explicitly "mathematical scaffolding" after reheating resets the axial mean (disclosed); a^{-6} concerns the erased channel already conceded not a dynamical prediction; N_tot spread disclosed bookkeeping (L1757-adjacent). Honest.
- **fingerprint:** D_inf, mathematical scaffolding, a^-6 scaling, N_tot 92, matter-bounce erasure, reheating reset

### DP1U-15: Appendices E–H don't test ECH (stock-CAMB / synthetic-sky / imported)
- **class:** RE-FLAG-DISCLOSED
- OpenAI #15, OpenAI-grok #13, ChatGPT, OpenAI retest #12/#18, ChatGPT retest: observational appendices provide no ECH test (stock-CAMB proxy / synthetic-sky / ALP import).
- Each appendix explicitly labeled a stock-CAMB proxy / synthetic-sky validation / companion import, "not an ECH test" (Claude verified; L5537-adjacent). Honestly bounded.
- **fingerprint:** appendices E-H, stock-CAMB proxy, synthetic sky, NaMaster, not an ECH test, MCMC, evidentiary value, negative Delta N_eff, one-sided positive bounds, proxy MCMC statistical device, App E convoluted

### DP1U-16: Companion-reliance / self-containedness / future-dated refs
- **class:** RE-FLAG-DISCLOSED
- OpenAI #13, ChatGPT (single-action / Eq.(10) not from Eq.(1) / N_tot), OpenAI retest #13/#16/#20, ChatGPT retest: depends on companions/repo artifacts/future-dated refs; not self-contained.
- Self-containment paragraph: no theorem depends on companion numerics; artifacts reproducible-now via `\cite{BigBounceRepro}` archive + explicit paths (frozen Cobaya chains, NaMaster MC, catalogs); TODO-SUBMISSION arXiv-ID markers pending same-day insertion (L1413-adjacent). Reproducible-now, not "cannot be refereed until posted."
- **fingerprint:** self-containment, companion reliance, in-preparation, BigBounceRepro, future-dated refs, arXiv-ID, reproducible-now, repository artifacts, unpublished forecasts, provenance, external unpublished material, CORRECTED.json present in repro tree

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

### DP1U-19: Regulated NJL vacuum-condensate exclusion
- **class:** CLOSED-BY-COMPUTE (directive-L, v1U.0.14) — was OPEN-VENUE
- OpenAI-grok #5 escalation, OpenAI retest #10: paper does not exclude a fully regulated NJL vacuum condensate via gap-equation / effective-potential.
- **CLOSED v1U.0.14:** the exact object these reviewers asked for is now delivered — a regulated NJL gap equation + effective-potential analysis (App. `app:njl_gap`; script `arxiv/scripts/njl_gap_equation_route1.py`). Two independent exclusions: repulsive scalar channel (no condensate at any coupling) + sub-critical coupling. See DP1U-05 for the full truth-audit note. The exclusion is stated within the standard mean-field NJL framework (assumption disclosed in-paper); strong-coupling-beyond-mean-field remains out-of-scope.
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
- **fingerprint:** length, 60 pages, repetitive, self-referential, Letter, 14-barrier overhead, style preference, abstract too long, response-to-referees document, overburdened with disclaimers, tier labels, scope statements, notation gamma confusing

### DP1U-23: LQC ρ_crit range / dataset-provenance minors
- **class:** RE-FLAG-DISCLOSED
- OpenAI retest MIN #16/#13, #17: ρ_crit 0.27–0.41 ρ_Pl mixes LQC area-gap / BH-entropy conventions; birefringence mixes WMAP+Planck/NPIPE/ACT DR6/Gaussian fits.
- Both ρ_crit values attributed to canonical LQC γ-choices, disclosed (L1441/L1472-adjacent; ρcrit block L2024). Birefringence dataset provenance disclosed and kept separate from the model prediction (App G).
- **fingerprint:** rho_crit, LQC, area-gap, BH-entropy, Immirzi choice, birefringence datasets, NPIPE, ACT DR6, provenance

## OPEN ITEMS
| ID | Class | Item | Gate |
|----|-------|------|------|
| DP1U-19 | ~~OPEN-VENUE~~ **CLOSED-BY-COMPUTE (v1U.0.14)** | Regulated NJL vacuum-condensate exclusion via gap-equation/effective-potential | **CLOSED (directive-L):** derived exclusion added — App. `app:njl_gap` + `arxiv/scripts/njl_gap_equation_route1.py` (repulsive scalar channel + sub-critical coupling; mean-field NJL framework). See DP1U-05/-19 truth-audit note. |
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

### DP1U-25: Check D artifact/abstract not synced to v1U.0.11 body fix (directive-I6)
- **class:** CLOSED-BY-EDIT (v1U.0.12)
- Claude INT MAJOR (W1, 2026-07-11): the v1U.0.11 Check D correction (`S_abc S^abc = -3/8 (J5.J5)`, Lorentzian `εε=-3!δ` + `(1/4)²` norm) was propagated ONLY through the .tex body (footnote L1810, O4/O5 L1957, Check D L4883-4884). The cited verification script `arxiv/scripts/dim4_parityodd_enumeration.py:141-169` still asserted `expected = 6*sp.eye(d)` and printed `εε=3!δ ⇒ S_abc S^abc = 6 (J5.J5)` (pre-fix, unsigned, no 1/16, docstring called the sign "immaterial"); the abstract L1243 still listed `εε=3!δ` (positive). A referee re-running the cited artifact got output contradicting the body Eq.
- **GENUINELY-NEW, REAL, EDITABLE** — verified against files: script L163 `6*sp.eye`, abstract L1243 `3!δ`, body L1810/1957/4883 `-3/8`/`-3!δ`. Not a science error (body already correct since v1U.0.11); a directive-I6/artifact-sync completeness gap introduced by incomplete propagation of the last fix. Under directive-K this RESET P1U's clean-wave streak to 0.
- **CLOSED v1U.0.12:** `check_D()` rewritten to apply the Lorentzian sign (`result = -result_euclid`, `expected = -6*I`) and carry the `(1/16)` normalization, so it now computes+asserts+prints `S_abc S^abc = -3/8 (J5.J5)` (script run confirms PASS); docstring corrected ("Lorentzian sign is NOT immaterial"). Abstract L1243 → `Lorentzian εε=-3!δ`. Recompiled 0 undef-refs, mirrored 6 paths, Convex bumped (row k572qqqjnwa8pcs1xe1v4xgk118aaaq1).
- Claude MINOR #3 (repro tree not resolvable): FALSIFIED — `parameter_summary_CORRECTED.json` files DO exist in `reproducibility/cosmology/frozen/*/diagnostics/`; reviewer's checkout was the `arxiv/` submission dir, but the abstract cites `\cite{BigBounceRepro}` = the public repro tree which contains them → DP1U-16 re-flag, not editable.
- **fingerprint:** Check D script sync, dim4_parityodd_enumeration.py, verified symbolically contradicts, abstract 3!delta vs body -3!delta, artifact propagation, directive-I6, expected 6 eye, 1/16 normalization, immaterial sign

## W1-INT adjudication wave (2026-07-11, vs v1U.0.11→v1U.0.12)
- **Inputs:** Claude INT MINOR (`INT_api/H17_2026-07-10/intwave_P1U_claude_1931.md`), OpenAI/gpt-5.5 INT REJECT (`INT_v3/ROUND_2026-07-09/API_P1U_openai.md`, 21 findings), Grok/grok-4.3 INT MAJOR (`.../API_P1U_grok.md`, 7 findings incl. 2 header-parse artifacts).
- **1 genuinely-new real+editable finding: DP1U-25** (Claude MAJOR — Check D script+abstract not synced to v1U.0.11 body fix). CLOSED in v1U.0.12 this bundle.
- **All other findings = source-cited re-flags** of ledgered D-ids (fingerprints enriched this wave): OpenAI 21 → DP1U-06,-08,-20,-09,-10,-11,-03/-04,-12,-13,-14,-15,-16,-18,-22; Grok 5 real → DP1U-06,-12,-11,-13. Claude MINOR #3 → DP1U-16 (FALSIFIED, CORRECTED.json present).
- **Clean-wave streak RESET to 0** (directive-K: the genuinely-new DP1U-25 was surfaced against a "no changes" re-test). v1U.0.12 re-tests fresh next wave.
- verdicts: OpenAI INT=reject, Grok INT=major-revisions, Claude INT=minor-revisions.

## H17G ledger-audit wave (2026-07-10, vs v1U.0.11)
- **ChatGPT EXT = REJECT** (raw `H17_2026-07-10/final/P1U_chatgpt_final.md`, on v1U.0.11) — 16 MAJOR + 2 MINOR. Fingerprint-match: 4-route/no-go=DP1U-06; Eq(1)-(4) variational=DP1U-03; Eq(5)-(8) dim+1/+1→+4=DP1U-08; App-B1 basis/O1=O6/Nieh-Yan=DP1U-07; NDA CC-naturalness restatement=DP1U-07/-11; Route-1 NJL ⟨J5⟩⇏⟨J5J5⟩=DP1U-05/-19; Route-2 ϑNY ansatz=DP1U-09; Route-3 Δγ inserted=DP1U-10; Route-4 ALP fixed-vs-floated=DP1U-11; App-C Fierz V⊗A=DP1U-04; quantum-consistency/counterterms=DP1U-07; Sec-X transparency novelty=DP1U-12; Eq(13)/N_tot≃92 dilution=DP1U-14; matter-bounce erasure + −35/8→−35/16=DP1U-14/-17; 13-barrier=DP1U-13; App-E-G don't test ECH=DP1U-15; MINOR figs=DP1U-24; MINOR length/organization=DP1U-22.
- **0 genuinely-new editable findings.** Every MAJOR is a source-cited re-flag of already-disclosed channel-level scope / honest out-of-scope items; both MINORs are disclosed-in-caption / OPINION. Consistent with the ChatGPT structural harsh-referee floor. No bump; v1U.0.11 stands.

## W1-EXT adjudication wave (2026-07-11, vs v1U.0.11; script-sign fixed in v1U.0.12)
- **Raws:** `EXT_real/H17_2026-07-10/W1/P1U_grok_W1.md` (Grok = **MINOR REVISIONS**, 6 real minors) + `.../P1U_chatgpt_W1.md` (ChatGPT = **REJECT**, 11 MAJOR + 2 MINOR). ledger_match.py + full §3 manual truth-audit against `arxiv/paper1_unified.tex` + this ledger.
- **Grok (MINOR)** — 6 minors, all source-cited re-flags of disclosed content: (1) channel-level vs "basis-complete within minimal ECH" tension → DP1U-06/-07 (disclosed L1219/L2448); (2) nψ∼O(10²) high-density bound justification → DP1U-05/-19 (finite-density bound scoped, NJL condensate out-of-scope); (3) Route-2 ∼10⁻⁶⁰ robustness note "move to main text" → DP1U-09 (presentation of a disclosed exploratory-framing item); (4) Sec.X transparency proof "too terse for a rigorous label" → DP1U-12 (standard on-shell equivalence, disclosed narrow scope); (5) 13/14-barrier summary table request → DP1U-13 (presentation of the disclosed independence-caveat catalog); (6) κ vs 8πG typographic cleanup → DP1U-02 (CLOSED-BY-EDIT v1U.0.11 convention block). No script-sign finding (DP1U-25 was an INT-Claude finding, already CLOSED v1U.0.12).
- **ChatGPT (REJECT)** — 11 MAJOR + 2 MINOR, identical structure to the H17G ChatGPT REJECT (16 MAJOR): Eq(1)-(4) variational=DP1U-03; Eq(5)-(8)/App-B dim+1→+4=DP1U-08; Sec.IV completeness/Nieh-Yan=DP1U-07/-20; Route-1 NJL ⟨J5⟩⇏⟨J5J5⟩=DP1U-05/-19; Route-2 ϑNY ansatz=DP1U-09; Route-3 Immirzi-running Euclidean-vs-Lorentzian γ²∓1 / no w=−1=DP1U-10; Route-4 ALP fixed-vs-floated=DP1U-11; Secs.II B-C/XII/XIV D no coherent model=DP1U-14; Sec.XIV D erasure "too strong"=DP1U-14; Sec.X transparency novelty=DP1U-12; Sec.XIII f_NL −35/8→−35/16 unsupported=DP1U-17 (P2 companion quadruple-certifies −35/16); MINOR App-E-G don't test ECH=DP1U-15; MINOR κ conventions=DP1U-02.
- **0 genuinely-new editable findings.** Every MAJOR is a source-cited re-flag of disclosed channel-level scope / honest out-of-scope items; both MINORs are disclosed/closed. Matches the ChatGPT structural harsh-referee floor (directive H). **No v1U.0.13 bump; v1U.0.12 stands. directive_g.sh not run (no edit).**
- **clean-wave streak → 1** (prior 0 after the DP1U-25 reset in W1-INT; this W1-EXT wave 0-genuinely-new re-increments to 1). Residual Grok-MINOR / ChatGPT-REJECT verdict words = the LLM harsh-referee structural floor on honestly-scoped channel-level content, not editable defects.

## W2-EXT adjudication wave (2026-07-11, vs v1U.0.12) — Grok MINOR→MAJOR oscillation
- **Raw:** `EXT_real/H17_2026-07-10/W2/P1U_grok_W2.md` (Grok = **MAJOR REVISIONS**, 3 MAJOR + 2 MINOR). ChatGPT not re-swept this wave (carry-forward REJECT). ledger_match.py + full §3 manual truth-audit vs `arxiv/paper1_unified.tex` v1U.0.12 + this ledger.
- **Grok verdict-word flip MINOR(W1)→MAJOR(W2) on UNCHANGED v1U.0.12 = pattern-066 referee variance, NOT a new finding.** The W2 raw is the SAME 6-item structure as the W1 MINOR raw, only the top-line verdict word changed. All 5 items are source-cited re-flags of ledgered D-ids:
  - **MAJOR#1 "R4 closed only by naturalness/explanatory-deficit while R1–R3 by amplitude suppression; equating them overstates R4"** → **RE-FLAG of DP1U-11.** The paper's OWN abstract (L1195-1198) states verbatim that R4 is "NOT closed by amplitude mismatch but by an explanatory-deficit / CC fine-tuning objection … relocating the CC problem rather than solving it," and the evidentiary-tier table makes the R1–R3-vs-R4 asymmetry explicit. Grok's "overstates" is the paper's own framing; disclosed, not editable.
  - **MAJOR#2 "single-scale NDA dimensional no-go restates the CC problem rather than deriving a channel-specific obstruction"** → **RE-FLAG of DP1U-08 (+ DP1U-11).** Disclosed: the +1→+4 NDA argument is labeled a "dispensable illustrative heuristic, not load-bearing" (L1877-1892-adjacent) and the no-go is honestly scoped channel-level (DP1U-06). Grok itself concedes "the argument is not circular only because no positive amplitude is claimed" — i.e. no defect, a known-EFT-observation re-statement.
  - **MAJOR#3 "basis-completeness 'internal tension' — 'basis-complete at M_Pl-power-counting' vs 'not proven to be a complete diffeomorphism-invariant operator basis'"** → **RE-FLAG of DP1U-07/-20 (+ DP1U-21 disclosure-backfire).** This is the exact channel-level-not-operator-level scope disclosed at L1219/L1389-1390/L2448; the "tension" is the honest hedging DP1U-21 documents as recast-as-weakness. Not editable (removing the hedge = overclaiming).
  - **MINOR#4 "Sec.X perturbation-transparency scoping so restrictive it adds limited insight"** → **RE-FLAG of DP1U-12** (standard on-shell scalar-equivalence, disclosed narrow "solid positive core" scope; novelty = referee preference).
  - **MINOR#5 "60pp excessively repetitive; many barriers overlap; PRD expects concision"** → **RE-FLAG of DP1U-06/-13/-22** (length/repetition OPINION; the barrier-overlap is the paper's OWN disclosed independence caveat at sec:barriers head).
- **0 genuinely-new real+editable findings.** The MINOR→MAJOR verdict-word flip on identical content is canonical pattern-066 (the directives anticipate variance in BOTH directions). **clean-wave streak 1→2 — P1U CROSSES the directive-K two-clean-waves bar.** No v1U.0.13 bump; v1U.0.12 stands. directive_g.sh not run (no edit).
- **Integrity:** Grok MAJOR recorded as-is (post_verdict.sh, cap 62 = 50 + grok-MAJ 6 + chatgpt-REJ 0 + gemini-MAJ 6); no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.

## W2b-EXT adjudication wave (2026-07-11, vs v1U.0.12) — ChatGPT re-sweep
- **Raw:** `EXT_real/H17_2026-07-10/W2b/P1U_chatgpt_W2b.md` (ChatGPT = **REJECT**, 15 MAJOR + 2 MINOR). `ledger_match.py` → 11/16 MATCHED, 5 UNMATCHED; full §3 truth-audit of the 5 UNMATCHED vs `arxiv/paper1_unified.tex` v1U.0.12 + this ledger.
- **5 UNMATCHED all source-cited re-flags:** Eq.(6) dim+1 / "identity can't change dimension" → **DP1U-08** (paper states the off-shell mismatch deliberately L1875-1885, dim-4 O1–O6 basis is primary `eq:Seff_dim4` L1888); single-scale NDA "not a no-go theorem" / E⁶/M_Pl² / bounce E~M_Pl → **DP1U-08 (+DP1U-11)** (channel-level, +1→+4 non-load-bearing); Route-2 (∂ϑ)J5/M_Pl not derived / ST λ4=γκ²(W·J) / [ϑ_NY] dim error → **DP1U-09** (one-loop-grounded via ST coeffs L1988/2197/2787, ∂ϑ dim +2 correct, exploratory-framing L618, absolute-norm honestly pending Riccati); Route-3 Euclidean/scheme caveats / Δγ×H0/M_Pl no operator → **DP1U-10** (scheme-spread + amplitude-budget conditional framing disclosed L560/1205/1323/1387); PRD-unsuitable/60pp/"new shorter paper" → **DP1U-22** (length/venue OPINION).
- **11 MATCHED confirmed:** #1→DP1U-03, #3→DP1U-20, #5→DP1U-05, #7→DP1U-10, #9→DP1U-05/-11, #10→DP1U-20/-06, #11→DP1U-14, #12→DP1U-12, #13→DP1U-15, #14→DP1U-17, MINOR #15→DP1U-02.
- **0 genuinely-new real+editable findings.** Identical structure to the H17G / W1-EXT ChatGPT REJECTs — ChatGPT structural harsh-referee floor (directive-H) on unchanged v1U.0.12. **clean-wave streak HOLDS at 2 — P1U REMAINS across the directive-K bar.** No v1U.0.13 bump; v1U.0.12 stands. `directive_g.sh` not run (no edit).
- **Integrity:** ChatGPT REJECT recorded as-is (post_verdict.sh); no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated; no hedging removed.

## GEM1-INT wave (2026-07-11, v1U.0.12 — FIRST verified Gemini INT leg, gemini-3.1-pro-preview)
- **Gemini INT = MAJOR REVISIONS** (raw `INT_v3/ROUND_2026-07-09/API_P1U_gemini.md`; native-PDF; audit `GEM1_INT_truth_audit.md`). 5 findings, all source-cited:
  1. [MAJOR] Holst-vanishes / §X transparency "trivial, reduce to one paragraph" → **DP1U-12** (standard on-shell scalar equivalence; novelty/presentation OPINION).
  2. [MAJOR] Appendices E–H "irrelevant/bloat, remove" → **DP1U-06/-11** (author-tagged "not load-bearing"; length/scope OPINION, Houston-gated presentation class).
  3. [MAJOR] Four no-go routes "overstated novelty, standard EFT dim-analysis" → **DP1U-06/-11** (verbatim the paper's channel-level-not-operator-level + CC-relocation framing, L1195-1219).
  4. [MINOR] Verbosity/repetitive caveats → PROCESS-NIT (style; DP1U-06 OPINION).
  5. [MINOR] Reliance on unpublished companions II–V → PROCESS-NIT (style; DP1U-04-adjacent).
- **0 genuinely-new editable findings.** A fresh 7th reviewer with no round history independently landed on the same disclosed classes. **clean-wave streak HOLDS at 2 — P1U REMAINS across the directive-K bar.** No v1U.0.13 bump; v1U.0.12 stands. `directive_g.sh` not run (no edit).
- **Integrity:** Gemini MAJOR recorded as-is; no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.

## FR1 adjudication wave (2026-07-11, vs v1U.0.13 restamp)
- **INT REJ/REJ/MAJ/MIN; EXT-grok MAJOR.** All findings re-flags of DP1U ledger: single-scale NDA no-go→DP1U-08; channel-vs-operator-level completeness→DP1U-06/-20; ECH action/torsion normalization→DP1U-02; R1 mean-field/NJL→DP1U-05; R2 one-loop-Holst ansatz→DP1U-09; R3 Immirzi-running→DP1U-10; R4 free-coupling ALP not-ruled-out→DP1U-11; Sec-X perturbation-transparency→DP1U-12; f_NL -35/16 self-containedness→DP1U-17; verbosity/tone/14-constraints-nomenclature→DP1U-22 PROCESS-NIT; companion-artifact provenance→DP1U-16.
- **OSCILLATION:** Grok-INT flipped MINOR→REJECT on unchanged v1U.0.13 — same 4-item scope structure (DP1U-06/-08/-11/-12), pure pattern-066 referee variance, NOT a new finding. Gemini MAJOR = same disclosed classes.
- Claude R3 lever-arm ln(10^16)=36.8 vs "30-35" → DP1U-10 (conservative-upper-bound ansatz, ≥60 orders margin; framing already disclosed; not a headline value) — re-flag, not editable defect.
- **0 genuinely-new editable findings.** clean-wave streak 2→3 (HOLDS across directive-K bar). No bump; v1U.0.13 stands. directive_g.sh not run (no edit).
- **Integrity:** EXT ChatGPT+Gemini FAILED (rate-limit) recorded as chart GAP not verdict; no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.

## FR1b adjudication wave (2026-07-11, vs v1U.0.13 restamp) — ChatGPT retry (recovered FR1 rate-limit gap)
- **EXT ChatGPT = REJECT** (14 MAJOR + 1 MINOR). Recovers the FR1-round rate-limit GAP. All findings source-cited re-flags of DP1U ledger: variational-hybrid Eq(1)/Cartan→DP1U-03; dim+1→+4 no-go→DP1U-08; O1–O6 basis-completeness/Nieh–Yan→DP1U-07/-20; Fierz mixed V⊗A closure→DP1U-07 (Fierz sub-claim, disclosed basis scope); R1 NJL condensate ⟨J5⟩≠⟨J5 J5⟩→DP1U-05; R2 one-loop/∂ϑ bookkeeping→DP1U-09; R3 Δγ→dark-energy mapping→DP1U-10; R4 ALP free-coupling→DP1U-11/-05; dynamical-CS transparency-misapplication + Sec-X overuse→DP1U-12; D_inf/N_tot≃92/matter-bounce-erasure→DP1U-14; 13-barrier independence→DP1U-13; App E–G don't test ECH→DP1U-15; global-restructure/repetition MINOR→DP1U-22 PROCESS-NIT.
- ledger_match.py: 9/15 auto-MATCHED; 6 UNMATCHED (conservative <0.30 prose-diluted) all Opus-adjudicated to the D-ids above — 0 genuinely-new.
- **0 genuinely-new editable findings.** clean-wave streak HOLDS at 3 (no reset). No bump; v1U.0.13 stands. directive_g.sh not run (no edit).
- **Integrity:** raw verbatim REJECT verdict READ before recording; no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.
