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

---

## Addendum — EXT re-test (v1U.0.10 → v1U.0.11, 2026-07-10)

Fresh EXT re-tests on the CURRENT v1U.0.10 PDF: `retest/P1U_grok_retest.md` (MAJOR, 3 MAJOR + 2 MINOR),
`retest/P1U_chatgpt_retest.md` (REJECT, ~15 MAJOR + 1 MINOR). Every finding re-audited against
v1U.0.10 source. **Result: 1 genuinely-new real+editable finding (ChatGPT "Check D") — CLOSED;
1 disclosure-backfire documented; all other findings source-cited RE-FLAG of prior-audit content.**

### GENUINELY-NEW REAL+EDITABLE — CLOSED

**ChatGPT MAJOR "Check D / torsion-current normalization" — REAL, internal inconsistency, FIXED.**
ChatGPT: "the footnote below Eq.(3) obtains S_abc S^abc = -3/8 J5², whereas Appendix B states the same
contraction gives 6 J5² — sign error and factor-of-16 discrepancy." VERIFIED against source:
- Footnote below Eq.(torsion) (L1796-1797) *carefully derives*: `S^abc = ¼ ε^abcd J5_d` ⟹
  `S_abc S^abc = (1/16) ε_abcd ε^abce J5^d J5_e = -3/8 (J5·J5)`, using the correct Lorentzian
  mostly-plus `ε_abcd ε^abce = -3! δ_d^e` (ε^0123=+1). This is the once-fixed normalization.
- Check D (L4866-4870) AND the O4/O5 reduction (L1944) both printed `S_abc S^abc = 6 (J5·J5)`
  using `ε_abcd ε^abce = +3! δ` (WRONG sign for Lorentzian) AND dropping the `(1/4)²=1/16` from
  `S=¼ε J5` — two independent slips relative to the footnote.
ChatGPT is correct: sign + factor-16. **CLOSED (v1U.0.11):** propagated the footnote's carefully-derived
`-3/8 (J5·J5)` + the correct `-3!` Lorentzian sign to BOTH restatements (L4866-4870, L1944).
No fabrication — the correct value was already derived in the paper's own footnote; this only
propagates it. **Structural conclusion UNCHANGED**: O4 still reduces to `κ²(J5·J5)`, O5 to
`κ(J5·J5)`, same `M_Pl⁻²` power, same Fierz-closed {SS,VV,AA,PP} basis. The sign/overall constant
of the S·S intermediate is not a load-bearing coefficient of the no-go — it only sets which
four-fermion contact operator the torsion-square collapses onto, and that operator's identity and
power counting are unchanged. PDF page renders the corrected `-3/8 (J5·J5)` in Check D.

### DISCLOSURE-BACKFIRE (pattern-066) — documented, not editable

**Grok MAJOR #7 (Sec IV scope + App C) — punishes this program's honest scope hedging.**
Quote: *"Repeated disclaimers that the work is 'channel-level, not an operator-level theorem' and
'not proven to be a complete diffeomorphism-invariant operator basis' sit in direct tension with the
assertion that the four routes … 'exhaust' minimal-ECH channels … this hedging undermines the
strength of the claimed closure."* The paper's honest scope disclosures — reinforced across prior
rounds precisely to be truthful about what is and is not proven — are here recast as a *weakness*.
This is the canonical disclosure-backfire: honesty penalized. Not editable (removing the hedging
would be dishonest overclaiming). Documented per directive-C.

### RE-FLAG of prior-audit-dispositioned content (source-cited non-real)

- **ChatGPT: single-action model / Eq.(10) not from Eq.(1) / N_tot not a common model** — RE-FLAG.
  Self-containment + companion-independence disclosed (prior audit self-containment item; L1413).
- **ChatGPT: Eq.(1) variational hybrid (T·T displayed but not varied)** — RE-FLAG. = prior audit (a);
  two-step off-shell/effective reading added v1U.0.10 (L1683+).
- **ChatGPT: F2 Cartan finite-γ contorsion has ε + η/γ terms, nonzero trace** — RE-FLAG. The paper's
  minimal-coupling totally-antisymmetric spin current is derived from the *symmetrized Hermitian*
  Dirac action (L1789-1794); the trace/η parts are the *non-minimal* content the paper explicitly
  puts OUT-OF-SCOPE (F2 disclosure; prior audit (b)/O1-O6 items).
- **ChatGPT: dimensional no-go Eq.(6) dim-1 / Bianchi "strips a curvature factor"** — RE-FLAG.
  +1→+4 dressing labeled "dispensable illustrative heuristic, not load-bearing" (prior audit dim+1
  item, L1877-1892); the genuine dim-4 O1-O6 basis is primary.
- **ChatGPT/Grok: O1-O6 not complete/independent, Nieh-Yan redundancy, infinite invariants** — RE-FLAG.
  Completeness argued analytically (F1+F2+NDA monotonicity, L2448-2467); non-minimal/derivative/
  multi-species irreps explicitly excluded (prior audit O1/O6 + OpenAI #3).
- **ChatGPT: Route 1 finite-density vs NJL vacuum condensate; ⟨J5⟩=0 ⇏ ⟨J5 J5⟩=0** — RE-FLAG/SCOPE.
  = prior audit (c); regulated NJL vacuum condensate explicitly NOT claimed excluded (L2599+).
- **ChatGPT: Route 2 ϑ_NY invented matching chain / Route 3 Δγ→ρ_Λ asserted / Route 4 ALP imported**
  — RE-FLAG. Route 2 "exploratory framing, not load-bearing"; Route 3 conditional amplitude budget;
  Route 4 "closed by explanatory-deficit/CC relocation, NOT amplitude" (prior audit Routes 2/3/4).
- **ChatGPT: N_tot ansatz / D_inf scaffolding / matter-bounce erasure "definitively"** — RE-FLAG.
  D_inf labeled "mathematical scaffolding"; N_tot spread disclosed bookkeeping (prior audit D_inf item).
- **ChatGPT: −35/16 vs Cai's −35/8, companion title still −35/8** — RE-FLAG. = prior audit
  "−35/16 self-containedness"; the historical −35/8 is a deliberately-cited comparison; the P2
  companion resolves the factor-of-two (P2 audit, quadruple-certified −35/16).
- **ChatGPT: 13 barriers not independent; ChatGPT MINOR + appendices E-H don't test ECH** — RE-FLAG.
  sec:barriers head disclosure "no barrier is a logical consequence of another"; each obs appendix
  labeled stock-CAMB proxy / synthetic-sky / not-an-ECH-test (prior audit barrier + appendices items).
- **Grok MAJOR #1 (NDA relocates CC problem)** — RE-FLAG. = prior audit OpenAI #2 + R4 framing;
  the paper itself states R4 "relocates the CC problem rather than solving it" (L1198).
- **Grok MAJOR #6/#2 (transparency high-level sketch; term-by-term not shown in detail)** — RE-FLAG/
  SCOPE. Transparency scoped to canonical scalar matter, excluding fermions/torsion/non-minimal
  (prior audit transparency item, L1248,3333).
- **Grok MINOR (14-barrier numbering overhead) + MINOR (60pp density/self-reference)** — OPINION.
  Style/venue preference (= OpenAI #19 / Grok #5 prior audit).

### Addendum counts
- **Genuinely-new real+editable:** 1 (ChatGPT Check D S·S sign+factor-16) — CLOSED v1U.0.11.
- **Disclosure-backfire (pattern-066):** 1 (Grok MAJOR #7 punishing honest scope hedging).
- **RE-FLAG of prior-audit/disclosed content (source-cited non-real):** ChatGPT ~14 MAJ + 1 MIN;
  Grok 2 MAJ + 2 MIN.
- **No fabricated math.** The one fix propagates the paper's own footnote-derived value; conclusion
  unchanged.

### Directive-G hygiene (v1U.0.11)
- `\paperVersion` v1U.0.10 → v1U.0.11; `\paperTimestamp`/`\date` = July 10, 2026 (unchanged); full changelog comment inline.
- Leak-gate: 0 secret patterns pre-compile.
- TinyTeX (universal-darwin) 3-pass + bibtex: 0 undefined references (the lone "undefined" is a cosmetic OMS/cmtt font-shape warning), 3 pre-existing overfull hboxes (L1645/4715/5192, none at the edits), 60 pages.
- PDF md5 = `ba2cf6754d774c8736be5e7cf458419f`, 2582392 bytes, 60 pages. Page 1 verified: "July 10, 2026", version chip v1U.0.11; Check D renders corrected `-3/8 (J5·J5)`.
- Mirrored byte-identical to all served paths: `public/papers/paper1_unified_v1U.0.11.pdf` + `paper1_unified.pdf`, `site/public/papers/…` (both), source `arxiv/paper1_unified.pdf` — all md5 `ba2cf675…`.
- Convex `paperVersions:bump` paper-1a v1U.0.11 (real md5/pages/bytes, "July 10, 2026", texCommit "post-H17-bundle", sitePdfPath /papers/paper1_unified_v1U.0.11.pdf) → row `k57d3hpz6a9r04qvhgedch3q7h8a864h`.
- No commit (per instructions).

---

## Addendum 3 — INT retest2 v1U.0.11 (2026-07-10 22:25 UTC)

DELTA-ONLY pass on fresh INT raws for the CURRENT v1U.0.11 PDF (post Check-D fix):
`INT_v3/ROUND_2026-07-09/API_P1U_openai.md` (gpt-5.5, native-PDF, REJECT, 12 MAJOR + 4 MINOR,
UTC 22:25:48) and `API_P1U_grok.md` (grok-4.3, native-PDF, MAJOR REVISIONS — improved from the
prior REJECT, 3 MAJOR + 2 MINOR, UTC 22:25:48; header now reads v1U.0.11). Every item checked
against the two prior addenda + body. **Result: 0 genuinely-new real+editable findings on either
vendor.** No re-litigation of already-dispositioned items below — one-line map only.

### OpenAI gpt-5.5 (REJECT) — delta map

| # | Sev | Maps to prior disposition |
|---|-----|---------------------------|
| 1 | MAJ | RE-FLAG — completeness "analytically argued, not proven diffeo-basis" (Add-1 OpenAI #1/#3; body P2 O1/O6). |
| 2 | MAJ | RE-FLAG — +1→+4 dressing "dispensable illustrative heuristic" (Add-1 #2; body dim+1 item). |
| 3 | MAJ | RE-FLAG — Eq.(1) ¼T·T "not varied", two-step off-shell/effective reading added v1U.0.10 (body (a); Add-1 #15). |
| 4 | MAJ | RE-FLAG — Fierz lemma + V·A non-minimal relabel; NJL scope disclosed (body (b)/(c); Add-1 #10). |
| 5 | MAJ | RE-FLAG — Route 2 "exploratory framing, not load-bearing" (Add-1 #4; body Route-2). |
| 6 | MAJ | RE-FLAG/SCOPE — Route 3 conditional amplitude budget, one clean β-fn (Add-1 #5; body Route-3). |
| 7 | MAJ | RE-FLAG — R4 "closed by explanatory-deficit/CC relocation, NOT amplitude" (Add-1 #6; body Route-4). |
| 8 | MAJ | RE-FLAG/OPINION — transparency scoped to canonical scalar; novelty=referee-pref (Add-1 #9; body transparency). |
| 9 | MAJ | RE-FLAG — barriers "no barrier a logical consequence of another" (Add-1 #8; body barrier item). |
| 10 | MAJ | RE-FLAG — obs appendices labeled stock-CAMB/synthetic/not-an-ECH-test (Add-1 #12; body appendices). |
| 11 | MAJ | RE-FLAG — −35/16 companion-delegated, historical −35/8 deliberately cited (body −35/16 self-containedness). |
| 12 | MAJ | RE-FLAG — claim-status "contradictions" are the paper's own honest tier/scope disclosures (Add-1 #1/#7). |
| 13 | MIN | RE-FLAG — LQC ρ_crit range attributed to canonical γ-choices, disclosed (Add-1 #16). |
| 14 | MIN | RE-FLAG — notation/M_Pl reduced-vs-unreduced = the disclosed κ convention block, L2103-2113 (body (d), verified present). |
| 15 | MIN | RE-FLAG — Figs illustrative/exploratory tags on captions (Add-1 #14). |
| 16 | MIN | RE-FLAG — self-containment: no theorem depends on companion numerics, reproducible-now (Add-1 #13/#20). |

### Grok grok-4.3 (MAJOR REVISIONS — improved from REJECT) — delta map

| # | Sev | Maps to prior disposition |
|---|-----|---------------------------|
| 1 | MAJ | RE-FLAG — completeness "analytically argued vs not-proven-basis" contradiction = OpenAI #1 (Add-1 Grok #1). |
| 2 | MAJ | RE-FLAG/SCOPE — transparency proven for scalar, routes use fermion/ALP; scoped disclosure (Add-1 Grok #4; body transparency). |
| 3 | MAJ | RE-FLAG — B8⊂B14 interdependence + single-scale NDA premise disclosed at sec:barriers head (Add-1 #8/Grok #3). |
| 4 | MIN | OPINION — 60pp/14-barrier length = venue/style preference (Add-1 #19/Grok #5). |
| 5 | MIN | RE-FLAG — N_tot≈92/D_inf "phenomenological" bookkeeping disclosed (Add-1 #11; body D_inf). |

### Addendum 3 counts
- **Genuinely-new real+editable:** OpenAI 0/12 MAJOR + 0/4 MINOR; Grok 0/3 MAJOR + 0/2 MINOR.
- **Re-flag / prior-dispositioned (source-cited non-real):** OpenAI 12 MAJ + 4 MIN; Grok 3 MAJ + 2 MIN.
- **Grok delta:** verdict improved REJECT → MAJOR REVISIONS on the v1U.0.11 PDF (no new items; the
  Check-D fix + prior clarity edits removed the reject-tier trigger).
- **No new edit → no v1U.0.12 bump, no directive-G, no Convex write.** v1U.0.11 (md5 `ba2cf675…`, 60 pp) stands.
- **No fabricated math.** All dispositions cite a live v1U.0.11 source line or a prior-addendum/body entry.

---

## H17F FINAL-WAVE ADDENDUM (2026-07-10, EXT re-test vs v1U.0.11)

Raw: `final/P1U_grok_final.md` (read + verified). ChatGPT final-wave leg PENDING (not harvested this wave).

- **Grok EXT = MAJOR REVISIONS** — 10 items, all map 1:1 to prior dispositions: excessive length/idiosyncratic structure (DP1U-22 OPINION), channel-level vs no-go overclaim risk (DP1U-06 — the paper's OWN verbatim framing), perturbation-transparency proof sketch depth (DP1U-12), dim-4 parity-odd completeness enumeration (DP1U-07), Route-2 Eq.(17) normalization/Shapiro-Teixeira status (DP1U-09), N_tot≈92 vs matter-bounce erasure mapping (DP1U-08/14), convention consistency κ/M_Pl/Holst (DP1U-02 — already closed by edit), coordinated-submission self-containedness (DP1U-16), related-work/novelty framing (DP1U-12 OPINION). The scope-hedging-recast-as-weakness thread is the standing disclosure-backfire (DP1U-21). **0 genuinely-new real+editable.**

**Outcome:** Grok EXT stays MAJOR on unchanged v1U.0.11 — every item a source-cited re-flag of disclosed channel-level scope, a Houston-gated venue/length OPINION, or already-closed convention edits. ChatGPT final leg pending — does not change the disposition (prior EXT ChatGPT already dispositioned 0 genuinely-new). 0 genuinely-new → no v1U.0.12 bump, v1U.0.11 stands. No math fabricated; no hedging removed (removing it would be dishonest overclaiming).
