# P1U Truth Audit — Round H17 (2026-07-10)

Paper: `arxiv/paper1_unified.tex` v1U.0.9 → v1U.0.10 (this round)
Reviewers audited: EXT ChatGPT (REJECT, 12 MAJOR + 2 MINOR), EXT Grok (MAJOR, 4 MAJOR + 2 MINOR),
INT Claude-subagent (MINOR), INT OpenAI/gpt-5.5 (REJECT), INT Grok/grok-4.3 (REJECT).

Verdict codes: REAL-NEW (genuinely-new, editable, closed this round) / RE-FLAG (source-cited
re-flag of already-disclosed content) / SCOPE (real but fundamental scope; honest open item) /
FALSIFIED (contradicted by source).

Never fabricated math. Every disposition below cites a source line/reference.

---

## PRIORITY 1

### (a) Eq.(1) variational hybrid (T·T displayed but "on-shell shorthand not varied") — ChatGPT #2, OpenAI-grok #1
**Verdict: RE-FLAG (already disclosed) + CLARITY CLOSE.**
The paper already states the variational principle unambiguously: Eq.(1) is a first-order
Palatini–EC action varied w.r.t. {e,ω,ψ}; the ¼T·T is explicitly "not an independent kinetic term
and is not varied," appearing only after on-shell torsion elimination (footnote L1685–1722; body
L1713–1722). ChatGPT's claim that Eqs.(3)–(4) "are not derived from the written action" is a
re-read of already-disclosed structure — they ARE derived from the connection variation, not from
varying T·T. **Action taken (honest clarity, not physics change):** added an inline two-step reading
directly after Eq.(1) (L1683+): step-1 off-shell ECHD+Dirac action varied over {e,ω,ψ} with the
¼T·T *absent*; step-2 solve Cartan Eq.(3), back-substitute, yielding effective Eq.(4). Makes the
off-shell→effective separation airtight at the display, not only in the footnote.

### (b) Eq.(16) provenance (Freidel–Minic–Takeuchi): V·A vanishes at minimal coupling — ChatGPT #b/#… , OpenAI-grok #2
**Verdict: REAL-NEW (editable, closed by claiming less). Confirmed against source.**
Web-verified FMT (PRD 72, 104002 / hep-th/0507253): **minimal coupling → NO parity violation,
effective Lagrangian contains ONLY the axial–axial interaction**; the vector–axial (V·A) parity-odd
cross term appears **only under non-minimal coupling**. The paper's `eq:4fermi_partner` (L2631)
presented the V·A `J·J⁵` term as arising "at finite Barbero–Immirzi parameter" from the *minimal*
torsion-elimination step — contradicting the cited FMT result AND the paper's own structural fact F2
(L2452: minimal coupling → totally-antisymmetric axial spin current). This was a genuine
internal + citation inconsistency. **Action taken:** relabeled the V·A partner as a *non-minimal*
operator everywhere it appears — §r1_parityodd_partner (L2625+, explicit FMT citation + "non-minimal
coupling only" tag on the equation + "included for completeness / even-if-adjoined" framing),
completeness lemma (L2459), Fierz appendix (L4863), and abstract (L1209). Does NOT weaken the no-go
(it strengthens it: one fewer *minimal* operator; the partner still shares the κ=M_Pl⁻² suppression
so is closed even if adjoined non-minimally). No fabrication — pure reclassification to match FMT.

### (c) Route 1 NJL closure: ⟨J5⟩=0 ⇏ ⟨J5 J5⟩=0 — ChatGPT, OpenAI-grok #5
**Verdict: RE-FLAG (already disclosed) + SCOPE-TIGHTEN.**
The paper ALREADY concedes exactly this (L2599–2604 pre-edit): "The vanishing of the mean does not
imply that the variance ⟨J⁵J⁵⟩ ... is zero — an incoherent thermal contribution ... is permitted —
but ... does not carry a coherent w=−1 equation of state and is in any case bounded above by leg (i)."
The Route-1 claim is already scoped to (i) finite-density mean-field bound + (ii) no coherent w=−1.
OpenAI-grok's escalation ("requires a regulated gap equation / effective potential") is a
scope-demand beyond what the paper claims. **Action taken (honest scope):** added an explicit
sentence (L2599+) stating the paper does NOT claim to exclude a fully regulated NJL vacuum
condensate via gap equation/effective potential — that is an out-of-scope open item — and that what
IS established is the Planck-suppressed finite-density bound + no coherent w=−1. Claim reframed to
exactly what is established.

### (d) M_Pl convention (M_Pl=G^{-1/2} vs 8πG=M_Pl^{-2}) and κ vs κ² — ChatGPT #19, OpenAI-grok #minor, Claude
**Verdict: REAL-NEW (cheap, editable). Confirmed error.**
The paper wrote `κ ≡ 8πG = M_Pl⁻²` with `M_Pl = G^{-1/2}` (unreduced). Mathematically wrong:
`8πG = 8π M_Pl⁻² ≠ M_Pl⁻²`; the identity `κ=M_Pl⁻²` holds only for the *reduced* mass
`M̄_Pl=(8πG)^{-1/2}`. **Action taken:** fixed the convention block (L2073+) to state
`κ ≡ 8πG = 8π M_Pl⁻² = M̄_Pl⁻²`, and flag that the compact `κ=M_Pl⁻²` shorthand used in
order-of-magnitude budgets is understood in the reduced-mass sense (the 8π≈25 factor immaterial to
those budgets). Footnote updated to match. κ vs κ² usage (κ²=16πG one-loop, Shapiro–Teixeira) is
already correctly attributed (L2076) and unchanged.

---

## PRIORITY 2 (dispositions — all RE-FLAG unless noted)

- **dim-+1 promotion / N_tot 92-vs-94 sensitivity** (OpenAI #3, Grok-EXT M2, Claude): RE-FLAG.
  The +1→+4 dressing is explicitly labeled "dispensable illustrative heuristic, not load-bearing"
  (L1877–1892, L4851); the genuine dim-4 O1–O6 basis is the primary foundation. N_tot spread is
  disclosed bookkeeping (L1757). No over-claim.
- **O1/O6 Nieh–Yan redundancy / basis completeness** (OpenAI #4, OpenAI-grok #4, ChatGPT): RE-FLAG.
  Basis completeness is argued *analytically* (F1+F2+NDA monotonicity, L2448–2467) with the two
  tensor identities symbolically checked; the abstract "symbolic verification" wording was softened
  this round (L1226, Claude MINOR) to say the SCRIPT verifies the two identities, not completeness.
- **Route 2 ∂ϑ dimension bookkeeping + field-excursion vs instantaneous-rate** (OpenAI-grok #6, Grok-EXT):
  RE-FLAG. Dimensions explicitly correct (L2830: ∂ϑ dim +2, operator dim +4). The ∂ϑ∼H substitution
  + alternative-ordering loose bound are disclosed (L2865–2868); route labeled "exploratory framing,
  not load-bearing" (L2872).
- **Route 3 Δγ→dark-energy link** (OpenAI #8, OpenAI-grok #7): RE-FLAG/SCOPE. Route 3 is the one
  cleanly-integrated β-function result (|Δγ/γ|≈1.4e-6); the H0/M_Pl mapping is amplitude-budget
  framing, already flagged conditional. Honestly disclosed.
- **Route 4 naturalness-vs-exclusion** (OpenAI #9/#10, OpenAI-grok #8, Grok-EXT): RE-FLAG. The
  abstract (L1194–1204) explicitly states R4 is "NOT closed by amplitude mismatch but by an
  explanatory-deficit / CC fine-tuning objection ... relocating the CC problem rather than solving
  it." Exactly the reviewers' point, already headlined honestly. Not over-claimed as exclusion.
- **D_inf non-derivation + a^{-6} scaling** (OpenAI #14, OpenAI-grok #9): RE-FLAG. D_inf is
  explicitly "mathematical scaffolding" after reheating resets the axial mean (disclosed);
  the a^{-6} vs a^{-3} point concerns the erased channel the paper already concedes is not a
  dynamical prediction (L… §gdp). Honest.
- **13-barrier catalog independence** (ChatGPT #13, OpenAI #13, OpenAI-grok #10, Grok-EXT minor2):
  RE-FLAG. Exemplary disclosure at sec:barriers head (L3530–3554): "no barrier is a logical
  consequence of another ... they do NOT assert ... each is an independent rigorous no-go theorem
  ... not a claim that thirteen separately decisive theorems each independently exclude." B8
  subsumed by B14, B9 heuristic, B5/6/7/10/13 general — all flagged. No edit needed.
- **transparency-triviality** (OpenAI #11, OpenAI-grok #11, Claude "no new content"): RE-FLAG.
  The paper labels it the "standard on-shell equivalence" and its "solid positive core" narrowly for
  canonical scalar matter, explicitly excluding fermions/torsion/dynamical-γ (Claude verified-correct).
  Not over-claimed as novel-broad.
- **multi-model patchwork** (OpenAI-grok #12): SCOPE/OPINION. The paper is a channel-level survey of
  minimal-ECH routes, not a single unified cosmological solution; this is disclosed as its stated
  scope. Referee-preference (venue-shaped), not an editable error.
- **appendices E–G evidentiary value** (OpenAI #15, OpenAI-grok #13): RE-FLAG. Each observational
  appendix is explicitly labeled a stock-CAMB proxy / synthetic-sky validation / companion import,
  "not an ECH test" (Claude verified-correct: MCMC labeled "stock-CAMB proxy, not an ECH test").
  Honestly bounded.
- **−35/16 self-containedness** (OpenAI-grok minor, Claude verified): RE-FLAG. Value used
  consistently; the historical Cai −35/8 is a deliberately-cited comparison (Claude verified
  the six −35/8 hits are comments + one historical citation). Self-containedness is a companion-paper
  dependency disclosed in the Self-containment paragraph.

## MINORS (cheap reframes — closed)
- Claude MINOR "every admissible" verdict (L4827): softened to "within the enumerated set at the
  stated power-counting order," explicitly excluding the Fierz-caveat non-enumerated classes.
- Claude MINOR "symbolic verification" abstract wording (L1226): reworded to "two load-bearing tensor
  identities verified symbolically ... not a completeness proof, which is argued analytically."
- Claude MAJOR O4 table dim ambiguity (tab:dim4_parityodd): the Fate column shows the *bare-invariant*
  reduction (O4→κ²(J⁵·J⁵) at dim+2 is correct for the bare invariant); added an explicit note that the
  *genuine* O4^[4]=M_Pl²·κ²(J⁵·J⁵)=κ(J⁵·J⁵) matches O5^[4] at dim+4, resolving the "+4 throughout"
  apparent conflict. Physics unchanged (Check D unchanged).
- Grok-EXT minor1 (scope-qualifier vs titular language): RE-FLAG — title already reads "Under Stated
  Assumptions," abstract L1200–1208 disambiguates "amplitude closure" and states "not an
  operator-level theorem." No edit needed.

---

## SUMMARY
- **Priority items:** (a) RE-FLAG + clarity close; (b) REAL-NEW closed (FMT-verified reclassification);
  (c) RE-FLAG + scope-tighten; (d) REAL-NEW closed (convention fix).
- **Closed this round:** 6 edits — (a) two-step action label, (b) V·A→non-minimal relabel ×4 sites,
  (c) Route-1 gap-equation scope sentence, (d) κ/M_Pl convention fix, + O4 table note, "every
  admissible" softening, "symbolic verification" softening, abstract V·A tag.
- **Dispositioned (RE-FLAG/SCOPE, source-cited):** ~13 Priority-2 items + 2 EXT minors.
- **Genuine open items (honest scope, not editable):** regulated NJL vacuum-condensate gap-equation
  exclusion (out of scope); operator-level (vs channel-level) completeness across the full
  diffeomorphism-invariant basis; single unified cosmological model. All disclosed in-paper.
- **No fabricated math.** The (b) fix and (d) fix are the only genuinely-new REAL findings; both
  closed by claiming less / fixing a convention, per the paper's honest-scope survival mode.

---

## Addendum — INT re-test v1U.0.10 (2026-07-10 ~07:34 UTC)

Fresh INT API re-test on v1U.0.10 raws: `INT_v3/ROUND_2026-07-09/API_P1U_openai.md`
(gpt-5.5, REJECT, 14 MAJOR + 6 MINOR) and `API_P1U_grok.md` (grok-4.3, REJECT,
3 MAJOR + 2 MINOR). Claude-subagent = MINOR (from H17 body). Every [MAJOR]/[MINOR]
audited against v1U.0.10 source below. **Result: 0 genuinely-new real+editable
findings on either vendor — every item is a source-cited RE-FLAG of already-disclosed
content or a SCOPE item the paper honestly discloses. No edit; no version bump.**

### OpenAI gpt-5.5 (REJECT) — per-finding

| # | Sev | Finding (paraphrase) | Verdict | Source cite |
|---|-----|----------------------|---------|-------------|
| 1 | MAJ | "four-route closure not a well-defined theorem / channel-vs-operator-level inconsistent" | RE-FLAG | abstract "channel-level assessment, not an operator-level theorem" (L1200-1208, L1390); title "Under Stated Assumptions". H17(a)-adjacent disclosure. |
| 2 | MAJ | ρ_Λ mapping not derived; Eq.(6) dimensionally incomplete; NDA no-go = naturalness | RE-FLAG | +1-vs-+4 named as property of on-shell reduction (L1223,1362,1402); single-scale NDA framing (v106 comment L235); "single-scale residual KEPT" honest. Matches prior audit (a)/(d)/P2. |
| 3 | MAJ | O1–O6 not complete basis; omits derivative/multi-flavor/curvature-torsion/non-minimal etc. | RE-FLAG | completeness argued analytically via F1+F2+NDA monotonicity (L2448-2467); non-minimal irreps explicitly OUT-OF-SCOPE (F2, L234 comment); Fierz caveat disclosed. Prior audit P2 O1/O6 item. |
| 4 | MAJ | R2 Eq.(17) phenomenological, birefringence anomaly-chain not justified | RE-FLAG | Route 2 labeled "exploratory framing, not load-bearing" (L2919, L3381). Prior audit Route-2 item. |
| 5 | MAJ | R3 Δγ/γ→(H0/M_Pl) is ansatz not derived | RE-FLAG/SCOPE | H0/M_Pl mapping flagged conditional amplitude-budget framing; Route 3 the one clean β-function result. Prior audit Route-3 item. |
| 6 | MAJ | R4 ALP φFF̃ imported, m~H0 is generic quintessence naturalness not ECH-specific | RE-FLAG | R4 explicitly "NOT closed by amplitude mismatch but by explanatory-deficit/CC relocation" (L1195-1198); spectator-ALP benchmark disclosed as imported (L580,811,819). Prior audit Route-4 item. |
| 7 | MAJ | Tier-III/ansatz status vs closure headline = overstatement | RE-FLAG | evidentiary tiers explicit (tab:evidentiary_status, L1390); abstract headlines R4 non-amplitude. Same as #1/#6. |
| 8 | MAJ | 13 barriers not independent/comparable status | RE-FLAG | sec:barriers head disclosure "no barrier is a logical consequence of another … not thirteen separately decisive theorems" (L3551, L528 comment). Prior audit barrier item. |
| 9 | MAJ | transparency = standard scalar-zero-spin-density, not novel enough | RE-FLAG/OPINION | labeled narrow "canonical scalar matter" result (L1248,1370,3333); novelty is referee-preference, not editable error. Prior audit transparency item. |
| 10 | MAJ | Fierz lemma asserted; no controlled vacuum-condensate/NJL exclusion | RE-FLAG/SCOPE | regulated NJL vacuum condensate explicitly NOT claimed excluded (L2632-2633, H17(c)); Fierz projection deferred as disclosed follow-up. Prior audit (c). |
| 11 | MAJ | D_inf, (T_reh/M_GUT)^{3/2}, N_tot≈92 phenomenological, not derived | RE-FLAG | D_inf labeled "mathematical scaffolding"; N_tot spread disclosed bookkeeping (L1757). Prior audit D_inf item. |
| 12 | MAJ | Appendices E–H don't test ECH (stock-CAMB/synthetic/ALP) | RE-FLAG | each labeled "does not directly test the ECH spin-torsion" / stock-CAMB proxy (L5537). Prior audit appendices item. |
| 13 | MAJ | depends on companions/repo artifacts/future-dated refs; not self-contained | RE-FLAG | Self-containment paragraph: no theorem depends on companion numerics; artifacts reproducible-now (L1413, L232/L512 comments). Prior audit self-containment item. |
| 14 | MAJ | Figs illustrative presented as evidentiary; Fig.3 H0 benchmark | RE-FLAG | Fig-3 H0 closed v1A.0.85; figure captions carry illustrative/exploratory tags (L3381). Prior audit figures item. |
| 15 | MIN | Eq.(1) hybrid on-shell T² shorthand risks double-counting | RE-FLAG | two-step off-shell/effective reading added this round (L1690-1700, H17(a)); ¼T·T "not varied". |
| 16 | MIN | ρ_crit 0.27–0.41 ρ_Pl mixes LQC area-gap / BH-entropy conventions | RE-FLAG | both values attributed to canonical LQC γ-choices; disclosed (L1441,1472; L1062 comment). |
| 17 | MIN | birefringence mixes WMAP+Planck/NPIPE/ACT DR6/Gaussian fits | RE-FLAG | dataset provenance disclosed; kept separate from model prediction (App G). Same class as #4/#12. |
| 18 | MIN | NaMaster synthetic skies simplified; appendix too long | RE-FLAG/OPINION | labeled synthetic-sky validation "not an ECH test"; length is style-preference. |
| 19 | MIN | manuscript too long/repetitive/self-referential | OPINION | venue-shaped style preference (Grok minor echoes); not an editable error. |
| 20 | MIN | refs to unpublished/future-dated companions lack stable IDs | RE-FLAG | TODO-SUBMISSION arXiv-ID markers + BigBounceRepro archive ref; reproducible-now (L232 comment). Same as #13. |

### Grok grok-4.3 (REJECT) — per-finding

| # | Sev | Finding | Verdict | Source cite |
|---|-----|---------|---------|-------------|
| 1 | MAJ | four-route "channel-level closure" qualified as not-operator-level / non-minimal loopholes open ⇒ interpretive survey | RE-FLAG | abstract/title "channel-level, not an operator-level theorem" + non-minimal residual disclosed (L1200-1221,1390). = OpenAI #1. |
| 2 | MAJ | single-scale NDA no-go + Fierz lemma = heuristic power counting; +1-vs-+4 an artifact of Eq.(6) shorthand | RE-FLAG | +1→+4 framed as property of on-shell reduction, not ill-defined; single-scale residual kept honest (L1223,1362; L90/L235 comments). = OpenAI #2. |
| 3 | MAJ | R4 "explanatory-deficit" vs amplitude-mismatch is subjective; same coupling reparameterized, relocates CC | RE-FLAG | this IS the paper's own stated framing verbatim ("relocating the CC problem rather than solving it", L1198). = OpenAI #6/#7. |
| 4 | MIN | transparency/B8 subsumption asserted w/o order-by-order perturbed-Holst verification | RE-FLAG/SCOPE | B8-subsumption disclosed at sec:barriers head; transparency scoped to canonical scalars (L1248,3333). = OpenAI #9. |
| 5 | MIN | excessive hedging + 14-barrier catalog inflate length; would be clearer as a Letter | OPINION | style/venue preference. = OpenAI #19. |

### Addendum summary
- **Genuinely-new real+editable:** OpenAI 0/14 MAJOR + 0/6 MINOR; Grok 0/3 MAJOR + 0/2 MINOR.
- **Re-flag of already-disclosed / prior-audit-dispositioned:** OpenAI 14 MAJ + 5 MIN; Grok 3 MAJ + 2 MIN (1 OpenAI MIN #19 + Grok MIN #5 = pure length/style OPINION).
- Every RE-FLAG cites a live v1U.0.10 source line or a prior-audit entry. The four this-round
  fixes (a two-step reading L1690; b FMT non-minimal relabel L1212; c NJL gap-equation scope L2632;
  d κ/M_Pl convention L2090) are all confirmed present in source and pre-empt findings #15/#2/#10/#2.
- **No new edit made → no v1U.0.11 bump, no directive-G, no Convex write.** v1U.0.10 stands.
- **No fabricated math.** All dispositions source-cited.
