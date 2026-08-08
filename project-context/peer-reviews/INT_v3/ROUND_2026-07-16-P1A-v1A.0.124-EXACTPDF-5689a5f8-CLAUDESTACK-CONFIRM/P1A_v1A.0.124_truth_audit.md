# P1A v1A.0.124 — Truth Audit (fresh skeptical Claude leg, CONFIRM round)

- **Paper:** P1A v1A.0.124 — "Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches" (CQG Note, 7 pp)
- **PDF SHA-256:** `5689a5f8b4c6488b9fa1c4d2225d3c0211b830b028b0284299c00f912d0977aa`  — exactness gate **PASS** (on-disk == mandated hash; matches Grok+Gemini receipts)
- **Source:** `arxiv/paper1a_ech_nogo.tex` (v1A.0.124; paper commit `23b4afb8a454a16b72ed78c1c11a9c04df4b45a7`). Rendered ranges are the gaps between `\begin{comment}…\end{comment}` blocks: L1–1195, L1317–1371, L1709–1830, L2601–2701, L3798–4020, L4709–4848, L5039–5042. All line citations below are v1A.0.124 line numbers (shifted from v1A.0.123).
- **Board audited:** `API_P1A_claude.md` — claude-opus-4-8 subagent, **MAJOR REVISIONS (3 MAJOR / 4 MINOR)**; `API_P1A_grok.md` — grok-4.3 **MINOR (3)**; `API_P1A_gemini.md` — gemini-3.1-pro-preview **MINOR (3)**.
- **Auditor stance:** fresh, skeptical, source-cited. Never dismiss without citation; when in doubt → GENUINELY-NEW-REAL.
- **Prior audit:** `ROUND_2026-07-16-P1A-v1A.0.123-EXACTPDF-4c450a67-CLAUDESTACK/P1A_v1A.0.123_truth_audit.md`. Its 3 genuinely-new items (m4 torsion-lemma coefficients; §III.B "diagnostic" relabel + softening; consolidated relation-to-prior-work sentence) were **CLOSED in v1A.0.124** — verified below.

---

## Headline

The Claude referee re-verified every derivation and numeric he could check and found **ZERO correctness errors** (his §(1): "The arithmetic I could check reproduces exactly … Q_γ inverse … κn_ψ² … R_S/R_A … γ→∞ coefficient"). All 13 findings across all three legs are significance / interpretation / self-containment / cross-reference asks — **no correctness defect, no science change indicated**. On source-check every finding is either (a) a re-flag of content already disclosed verbatim in the exact place the referee points to, (b) a tracked SSOT venue/robustness gate, or (c) a scope/venue opinion. The three v1A.0.123 genuinely-new items are closed. **Genuinely-new-real editable items this round: 0.**

**Arithmetic spot-recheck (independent):** Q_γ Q_γ⁻¹ = γ²/(1+γ²)(1+γ⁻²) = 1 ✓ (on ⋆²=−1); −3κ/16 = −3(8πG)/16 = −(3/2)πG ✓ (L1808–1809); R_S = 3N_fN_c/(4π)|_{Λ=M_Pl} = 0.239/0.716/2.148 ✓ (Table I L4824–4826); R_A = R_S/2 = 0.119/0.358/1.07 ✓. Clean, consistent with referee and prior board.

---

## Verdict matrix

| # | Leg | Sev | Finding (compressed) | Verdict | Source citation |
|---|-----|-----|----------------------|---------|-----------------|
| M1 | Claude | MAJOR | Novelty/significance threshold for a CQG Note; make significance case or broaden scope | **SCOPE-VENUE-OPINION** + **ALREADY-TRACKED-GATE** (human CQG review); provenance sub-ask **DISCLOSED-RE-FLAG** (closed v124) | provenance L1344–1352; significance = SSOT human-CQG gate |
| M2 | Claude | MAJOR | NJL "no-condensate" convention-fragile + supercritical; demonstrate no Fierz-flip or withdraw | **DISCLOSED-RE-FLAG** + **ALREADY-TRACKED-GATE** (alt-regulator/Fierz-complete) | scoped L1170–1174, L2680–2683, L2695–2700; supercrit disclosed Table I L4826 + L2686–2687, L3984–3985, L4831–4834; sign labeled convention-bound L4766 |
| M3 | Claude | MAJOR | Scalar-transparency: boundary/surface-term vanishing asserted, not shown; "every order" load-bearing | **DISCLOSED-RE-FLAG** (referee premise rebutted; load-bearing steps demonstrated; boundary scoped) | L3813–3815, L3829–3832, L3859–3861, L3865–3867, L3873–3874, L3903–3905 |
| m4 | Claude | MINOR | "Two branches of same equation" framing overstates | **SCOPE-VENUE-OPINION** (defensible framing) | J≠0 vs J=0 branches of Eq (cartan_source) L1767–1772 |
| m5 | Claude | MINOR | Reduction (3)→(5)/(7) compressed; add explicit intermediate | **DISCLOSED-RE-FLAG** (normalization bridge shown) + optional | Eq (fmt_normalization_bridge) L1807–1810 |
| m6 | Claude | MINOR | Table I interpretation risk; state table gives no magnitude bound | **DISCLOSED-RE-FLAG** | L2684–2687, L3983–3985, L4831–4836 |
| m7 | Claude | MINOR | Purpose of dimensional benchmark; add diagnostic-use sentence | **DISCLOSED-RE-FLAG** | abstract L1162–1170, intro L1366–1370, discussion L3961–3963 |
| G1 | Grok | MINOR | Benchmark not explicitly flagged illustrative/non-constraining | **DISCLOSED-RE-FLAG** | L1162–1163, L1168–1170, L2652–2653, L2660–2664 |
| G2 | Grok | MINOR | Text doesn't note Fierz identity rearranges into unexamined channels | **DISCLOSED-RE-FLAG** | L4762–4767, L2698–2700, L4842–4846 |
| G3 | Grok | MINOR | Cross-ref helicity-solution statement to E_R=E_L operators (Eq 12) | **DISCLOSED-RE-FLAG** | L3820–3822, L3896, L3898–3899, L3948–3950 |
| Ge1 | Gemini | MINOR | n_ψ=100 cm⁻³ — anchor to CνB or other density | **DISCLOSED-RE-FLAG** (deliberately unanchored) | L2652–2653 |
| Ge2 | Gemini | MINOR | Cite specific ECH-dark-energy/bounce phenomenology targets | **SCOPE-VENUE-OPINION** (critiqued running class already cited) | L1366–1370, L3799–3805, L4000–4003 |
| Ge3 | Gemini | MINOR | R_H(Γ̊) in Eq (13) used without prior definition | **DISCLOSED-RE-FLAG** / falsified-as-stated (defined via ≡ at first use) | L3909–3910, L3913–3914 |

**Counts:** 13 findings · 0 correctness errors (referee-confirmed + independently spot-checked) · 0 BLOCKER · 3 MAJOR (all Claude) → 1 SCOPE-VENUE-OPINION+tracked-gate, 1 DISCLOSED-RE-FLAG+tracked-gate, 1 DISCLOSED-RE-FLAG · 10 MINOR → 8 DISCLOSED-RE-FLAG, 2 SCOPE-VENUE-OPINION. **Genuinely-new-real: 0.**

---

## MAJOR findings

### M1 — Novelty/significance threshold → SCOPE-VENUE-OPINION + ALREADY-TRACKED-GATE (provenance sub-ask DISCLOSED-RE-FLAG)

The referee's M1 has two components. **(a) Per-claim provenance** ("a reader cannot separate original from re-derived") — this was the *optional* nicety flagged in the v123 audit and is now **CLOSED in v124**: the dedicated consolidated sentence at **L1344–1352** delineates each element to its source — "the finite-γ bivector inverse and axial contact coefficient follow Freidel, Minic, and Takeuchi (their Eqs. 6, 17, 23 [Freidel2005]), the Einstein–Cartan axial–axial contact is the Hehl–Datta result [Hehl1976,HehlDattaNJL1971], and the vanishing of the Holst density on the torsion-free scalar branch is the first (algebraic) Bianchi identity; the element assembled here is their convention-audited consolidation." The abstract (L1190–1193) restates the "contribution = consolidation, no new prediction" boundary. This sub-ask is fully answered → **DISCLOSED-RE-FLAG**.

**(b) The significance/yield judgment** — "what open confusion does the audit resolve, and for whom, or broaden the scope" — is a **venue call**, not an editable defect. The paper already states its diagnostic purpose (retiring the exploratory Holst-running→dark-energy mapping, L1366–1370; making the claim boundary explicit, L3961–3963). Whether that yield clears the bar for a CQG Note is precisely the **tracked "human CQG/editorial review" gate** on the SSOT ledger (status.md banner: readiness cap 62 HOLDS pending "human CQG review"). A maximally-harsh LLM referee's structural-floor MAJOR on significance is the documented pattern-066 behavior (H-directive). **Verdict: SCOPE-VENUE-OPINION + ALREADY-TRACKED-GATE.** Nothing editable.

### M2 — NJL "no-condensate" convention-fragile + supercritical → DISCLOSED-RE-FLAG + ALREADY-TRACKED-GATE

The referee demands the Note either **demonstrate that no legitimate Fierz/exchange-basis choice flips G_scalar > 0**, or **withdraw** the "no nonzero solution" statement rather than state it even conditionally. On careful source-check against the exact question posed (does the paper claim a flip-exclusion, or scope to the stated convention?):

- **The paper claims NO flip-exclusion.** It explicitly disclaims one: App Fierz L4762–4764 "an operator-order-specific Dirac-algebra identity, **not an assertion that one mean-field factorization is basis-independent**"; App NJL L4844–4846 "**not presented as a regulator- or basis-independent exclusion of every condensate mechanism**." The referee's demand ("demonstrate no legitimate Fierz-flip") is a request for a **stronger** result than the paper asserts.
- **Every instance of the conclusion is scoped to the single declared convention** — the v124 softening the prompt cites is present: abstract L1170–1174 "In the declared direct-channel, hard-four-momentum-cutoff, standard mean-field NJL convention … has no nonzero solution. This conditional sign result does not exclude other truncations…"; §III.B L2681–2683 "admits **no nonzero scalar gap solution in this single mean-field convention**"; L2695–2698 "we make **no claim beyond this convention**"; Conclusions L3980–3982 "in the declared direct-channel … gap equation." No unscoped statement of the conclusion exists.
- **The R_S = 2.15 supercriticality is fully disclosed** — Table I L4826 (N_fN_c=9 → R_S=2.15); §III.B L2686–2687 "run from 0.239 to 2.15 and therefore are **not uniformly subcritical**"; Conclusions L3984–3985 "the N_fN_c=9 coefficient magnitude is **supercritical**"; App NJL L4831–4834 "supercritical only in the N_fN_c=9 … row … The old blanket magnitude-subcritical statement is **false**."
- **The sign is affirmatively labeled convention-bound to the reader** — L4766 "its sign is convention-bound" — so the referee's residual worry ("a reader cannot tell whether the sign is physical or a convention artifact") is answered by the paper telling the reader it is convention-dependent, and that the condensate conclusion rests on the sign, not the magnitude (L4834–4836).

The paper's claim is therefore **already exactly as narrow as the referee's "state it conditionally with full disclosure" option**, and strictly narrower than the flip-exclusion he alternatively demands (which the paper explicitly declines to claim). The "demonstrate no Fierz-flip" strengthen-path maps directly onto the **tracked alternate-regulator / Fierz-complete robustness gate** (SSOT banner OPEN gate "alternate-regulator robustness"). No residual overclaim survives. **Verdict: DISCLOSED-RE-FLAG + ALREADY-TRACKED-GATE.**

### M3 — Scalar-transparency boundary/surface-term step → DISCLOSED-RE-FLAG (referee premise rebutted; steps demonstrated; boundary scoped)

The referee asserts the "GR-equal observables at every perturbative order" claim rests on an **asserted-but-unshown** first-order variational surface-term vanishing and an order-by-order E_R=E_L equality. On source-check, the manuscript's argument **explicitly repudiates that premise** and does not rely on the step he flags:

- **The all-orders content is NOT an order-by-order / surface-cancellation argument.** L3829–3831: "Its all-orders content **does not come from an order-by-order calculation**: the Cartan constraint is algebraic, and the Bianchi identity used below is pointwise." L3832: "The displayed linear tensor equation and second-order Holst expression are **checks** of those identities, **not their foundation**."
- **The surface term is explicitly scoped as a hypothesis (matched boundary data), not a derived step** — option (c) in the audit rubric. L3813–3815: "on a local patch with matched background, initial, and boundary data. Here standard boundary data means the usual falloff conditions **with the boundary contribution to the first-order variation set to zero**." The abstract's "so the first-order variational surface contribution vanishes" (L1183–1184) is this same scoping assumption, consistently defined in the body.
- **The referee's load-bearing premise is directly denied.** L3873–3874: "**No total-derivative argument is a load-bearing step in this proof.** The operative statement is the pointwise algebraic Bianchi identity in Step 4." The Nieh–Yan boundary decomposition is retained "only to distinguish related densities" (L3875–3877, L3919–3921).
- **The two genuinely load-bearing steps ARE demonstrated in-manuscript:** (i) T=0 via the invertible-tetrad dual-frame contraction (§Theory L1774–1784, referenced at proof Step 2 L3844–3846 "the explicit dual-frame contraction … proves that its invertible-tetrad kernel is trivial"); (ii) the Holst dual vanishes **pointwise** on Levi-Civita by the first Bianchi identity, shown by the one-line cyclic-sum contraction with ε at L3859–3861 — "identically zero on the Levi-Civita connection **(not merely a boundary term)**, so it contributes nothing to the action at any order" (L3865–3867). With the reduced Lagrangian pointwise identical to Einstein–scalar, equality of the EOM at every order is a consequence of identical actions, not of an order-by-order surface cancellation.
- **E_R=E_L is explicitly demoted to an illustration, not the foundation.** L3881–3882 "As an illustrative source-free linear specialization"; L3903–3905 "The all-order statement is **not** the displayed linear equation: it is equality of the classical action and equations of motion to their GR forms … before any perturbative expansion."

The paper anticipated and closed exactly this objection: the strong claim is demonstrated via the pointwise-algebraic-identity route, and the boundary term is a stated hypothesis explicitly declared non-load-bearing. **Verdict: DISCLOSED-RE-FLAG.** (Optional, non-required clarity nicety noted below — not a genuine gap.)

---

## MINOR dispositions

- **m4 (branches framing) — SCOPE-VENUE-OPINION.** The spin-sourced (J⁵≠0) and zero-spin (J^IJ=0) cases are literally the source-nonzero and source-zero branches of the *same* algebraic connection equation Q_γ(e^[I∧T^J])=J^IJ (Eq (cartan_source) L1767–1768; zero-source reduction L1771–1773). The "two consequences of the same algebraic Cartan equation" framing (abstract L1158–1160) is defensible, arguably precise. Softening is a stylistic preference, not a defect.
- **m5 (reduction compressed) — DISCLOSED-RE-FLAG + optional.** The key normalization bridge is shown explicitly: Eq (fmt_normalization_bridge) L1807–1810 (4πG=κ/2, −(3/2)πG=−3κ/16), between the FMT contorsion Eq (fmt_contorsion) L1796–1800 and the resulting Eq (4fermi) L1813–1815. The remaining FMT back-substitution (their Eq 23) is a legitimately cited standard result, not omitted reconstructable arithmetic. No stated-without-showing step (unlike v123-m4). Further intermediate is optional self-containment enrichment.
- **m6 (Table I magnitude) — DISCLOSED-RE-FLAG.** The paper states, in three places, that the conclusion rests on the sign not the magnitude and that the magnitude is supercritical: §III.B L2684–2687, Conclusions L3983–3985, App NJL L4831–4836. Caption L4818–4819 disclaims stress-tensor/EoS reading. Exactly what m6 requests, verbatim.
- **m7 (benchmark purpose) — DISCLOSED-RE-FLAG.** Diagnostic purpose stated: abstract L1162–1170 ("illustrates only its scale"; does not fix composite/stress-tensor/EoS), intro L1366–1370 (retiring the running→dark-energy mapping), discussion L3961–3963 ("its utility is to make the dimensional benchmark and claim boundary explicit"). One-sentence sharpening optional; no gap.
- **G1 (illustrative disclaimer) — DISCLOSED-RE-FLAG.** L1162–1163 "illustrates only its scale," L1168–1170 (not an EoS/VEV/stress-tensor), L2652–2653 "deliberately elevated for illustration; neither a cosmological-density estimate nor a preferred state," L2660–2664. Disclosed verbatim.
- **G2 (other Fierz channels unexamined) — DISCLOSED-RE-FLAG.** L4762–4767 (operator-order-specific, not basis-independent; report axial only through |G_A|), L2698–2700, L4842–4846 ("A different Fierz-complete truncation, exchange treatment, multi-species model, or nonperturbative completion can change the mean-field organization"). Grok's exact concern is stated.
- **G3 (cross-ref helicity to E_R=E_L) — DISCLOSED-RE-FLAG.** Operator-identity vs solution-identity distinction is made at three sites including at Eq (12) itself: L3820–3822, L3898–3899 ("v_R=v_L follows only when the initial data are also parity symmetric"), L3948–3950. Explicit cross-reference is optional cosmetic.
- **Ge1 (anchor n_ψ) — DISCLOSED-RE-FLAG.** The paper *deliberately* declines to anchor the normalization to a physical density (L2652–2653) to avoid implying physical significance; Gemini's suggested CνB anchor would work against the paper's honest scoping. Disclosed choice, not a defect.
- **Ge2 (cite ECH-dark-energy targets) — SCOPE-VENUE-OPINION.** The critiqued running/RG class IS cited — ShapiroTeixeira2014, BenedettiSpeziale2011run (intro L1366–1370; §V "Running literature" L3799–3805; Benedetti2011), and the conclusions reference "proposed running-based extensions" (L4000–4003). Adding further specific phenomenology cites is optional enrichment; the paper states no factual error and cites the class it corrects. (Any added citation must be a real, verified reference — integrity rule; not performed here as it is non-required.)
- **Ge3 (R_H undefined) — DISCLOSED-RE-FLAG / falsified-as-stated.** R_H(Γ̊) is defined at its first appearance via the identity sign: L3913–3914 "R_H(Γ̊) ≡ ½ε^μνρσ R_μνρσ(Γ̊) = 0," with the preceding prose L3909–3910 stating "the Holst dual evaluates on the Levi-Civita connection (T=0) as." There is no undefined prior use. Trivial cosmetic wording tweak at most.

---

## GENUINELY-NEW-REAL (minimal honest fixes)

**None.** Zero genuinely-new-real editable items this round.

All three genuinely-new items from the v1A.0.123 audit are confirmed **closed in v1A.0.124**:
1. Torsion-vanishing lemma 4D contraction coefficients now shown (L1774–1784: ι_{E_I}e^I=4, e^I∧ι_{E_I}T^J=2T^J, ½(T^J+e^J∧t)=0, ι_{E_J}(e^J∧t)=3t, t=−3t ⇒ 4t=0 ⇒ T^I=0) — derived from the manuscript's own number identities, no fabrication.
2. §III.B relabeled "Standard mean-field NJL diagnostic" (L2673) with scope softening "in this single mean-field convention" (L2683) / "we make no claim beyond this convention" (L2697–2698).
3. Consolidated relation-to-prior-work sentence (L1344–1352).

**Optional (NOT required, NOT classified genuine) polish surfaced by M3:** the abstract clause "so the first-order variational surface contribution vanishes" (L1183–1184), read in isolation, can be misread as a derived load-bearing step; the body already states the correct framing (hypothesis + explicitly non-load-bearing, L3813–3815 / L3873). A one-clause abstract tweak matching the body would remove the misread that produced M3, but the body is already correct — this is presentation parity, not a defect, and matches how the v123 audit treated M1's "present-but-distributed" provenance (optional, later taken as the L1344–1352 sentence).

---

## State assessment

P1A v1A.0.124 is a technically correct, unusually honestly-scoped 7-page CQG Note whose two central claims — the minimal spin-sourced axial contact interaction −(3κ/16)[γ²/(1+γ²)]J₅² and classical zero-spin scalar-sector transparency to GR on the torsion-free branch — the fresh Claude referee independently re-derived with **zero correctness errors**, matching the Grok and Gemini MINOR verdicts and the prior Codex-subscription ACCEPT. This confirmation round surfaces **no genuinely-new real finding**: all three Claude MAJORs reduce to disclosed re-flags or tracked venue/robustness gates (M1 significance = human-CQG gate with provenance now closed at L1344–1352; M2 is already scoped exactly as narrowly as the referee's "state conditionally" option, with R_S=2.15 supercriticality disclosed in Table I + three text sites and the sign labeled convention-bound, the flip-exclusion he alternatively demands being the tracked alternate-regulator gate the paper explicitly declines to claim; M3's "asserted surface-term" premise is factually rebutted by the manuscript's own L3813–3815 boundary scoping, L3829–3831 pointwise-not-order-by-order statement, and L3873 "no total-derivative argument is load-bearing," with both load-bearing steps demonstrated), and all ten minors are disclosed verbatim in the exact locations flagged or are defensible scope/venue opinions. The three v123 genuinely-new items are confirmed closed. Net: the paper requires **no science change and no editable fix**; the only surfaced item is an optional, non-required abstract-vs-body parity clause on M3, and the two substantive open questions (CQG significance disposition; alternate-regulator/Fierz-complete robustness) remain Houston-gated ledger items already on the SSOT banner — consistent with a paper sitting at its verified external cap awaiting human venue disposition, with 0 genuinely-new-real findings this round.
