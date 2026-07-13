# P1U M13-EXT truth-audit (2026-07-12) — STRICT, ledger-first — GROK MINOR→MAJOR SLIP DIAGNOSED

**Raws (verbatim, read before any disposition):**
- `M13/P1U_grok_M13.md` = **MAJOR REVISIONS** (4 MAJOR + 2 MINOR) — l.1 `VERDICT: MAJOR REVISIONS`
- `M13/P1U_chatgpt_M13.md` = **REJECT** (13 MAJOR + 3 MINOR) — l.1 `VERDICT: REJECT`

Both on byte-unchanged **v1U.0.20** (`\paperVersion{v1U.0.20}`, `\paperTimestamp{July 12, 2026}`).
Pre-triage: `tools/ledger_match.py` (Grok 6/7, ChatGPT 9/16 MATCHED); every UNMATCHED +
every low-score MATCHED given a full §3 source-cited disposition below.

## GROK MINOR→MAJOR SLIP DIAGNOSIS (pattern-066)

**Prior P1U-EXT read (M11-EXT, SAME byte-unchanged v1U.0.20) = Grok MINOR** (5 minors,
closing "the central claim … is supported"). **M13 = Grok MAJOR on the IDENTICAL file.**
The M13 item set is the SAME content class as M11's — the delta is the top-line verdict word only:

| M13 Grok item | M11 Grok analogue | D-id |
|---|---|---|
| MAJOR "four-route uniform phrasing conflates deductive/interpretive/ansatz; tiered taxonomy" | M11 #1 (scope-prominence) | DP1U-11 / DP1U-06 |
| MAJOR "completeness lemma O1–O6 + Fierz doesn't rule out other dim-6 ops; close the gap in-text" | M11 #4 (NJL two-line) + #1 | DP1U-07 / DP1U-20 |
| MAJOR "§X perturbation-transparency only sketches; full linearized ECH eqns must appear" | M11 #3 (§X perturbed-tetrad) | DP1U-12 |
| MAJOR "R4 naturalness closure not amplitude-level; re-label" | (new emphasis; same class) | DP1U-11 |
| MINOR "N_tot≈92 from two inconsistent routes; state the convention" | — | DP1U-08 |
| MINOR "repetitive scope caveats; consolidate into one box" | M11 #5 (length) | DP1U-06 / DP1U-22 |

Every M13 Grok item maps to a STANDING disclosed D-id (no `directive_g.sh`-gated content).
`ledger_match.py` auto-MATCHED 5/6 (only the line-1 verdict header UNMATCHED, a non-finding).
Grok's M13 one-sentence STILL SUPPORTS the central claim ("supported within its explicitly
delimited scope by the dimensional/power-counting arguments, Fierz projection lemma, integrated
one-loop running, and decoupling analysis"). **This is canonical pattern-066 verdict-word
oscillation on unchanged content — NOT a content regression, NOT a genuinely-new finding.**
The ledger already documents Grok MINOR↔MAJOR oscillation in BOTH directions on this paper
(W1-EXT MINOR → W2-EXT MAJOR, NJ-series MAJOR, M11-EXT MINOR).

## VERDICT: 0 genuinely-new reader-visible editable findings

### EXT-Grok MAJOR — all re-flags (see slip table above)
DP1U-11 (R4 naturalness-not-amplitude, verbatim the paper's abstract L247/L346/L354),
DP1U-06/-07/-20/-21 (channel-vs-operator scope + completeness disclosure L1219/L1268-74/L2448 +
disclosure-backfire), DP1U-12 (§X standard on-shell scalar equivalence, narrow disclosed scope),
DP1U-08 (N_tot spread disclosed bookkeeping), DP1U-22 (length/repetition OPINION).

### EXT-ChatGPT REJECT (13 MAJOR + 3 MINOR) — all re-flags
Structurally identical to every prior ChatGPT REJECT (H17G/W1/W2b/NJ3b/NJ4/NJ5/NJ6/M4/M5/M8/M11):
- Eq.(6) dim+1 "Bianchi can't change dimension" / ρ_Λ=ΞM_Pl⁴ phenomenological → **DP1U-08** (off-shell +1 deliberate, dim-4 O1–O6 basis primary L307).
- {O1…O6} completeness not demonstrated / O1=O6 / T_IJ undefined / higher-dim not suppressed at E~M_Pl → **DP1U-07 / DP1U-20** (completeness argued analytically; non-minimal/derivative irreps OUT-OF-SCOPE).
- Eq.(1) not well-defined off-shell action / T=κS pure-EC-not-Holst / F1-F2 → **DP1U-03 / DP1U-04** (Palatini-EC T·T-not-varied shorthand disclosed L308/L336; minimal-coupling totally-antisymmetric spin current derived; finite-γ vector parts are non-minimal, FMT-scoped).
- **UNMATCHED#4 [MAJOR] Route-1 vacuum condensate exclusion addresses only self-generated NJL, not the QCD ⟨q̄q⟩ route; ⟨J5J5⟩ needn't factorize** → **DP1U-05 / DP1U-19** (regulated NJL gap-equation exclusion CLOSED-BY-COMPUTE v1U.0.14; leg-(A) convention-independent scalar sign G_scalar=−3/64κ<0 is decisive at ANY coupling; QCD-vacuum route is the broader Fock demand = the disclosed harsh-referee floor).
- App C–D Fierz doesn't justify independent Hartree couplings; pseudoscalar is still a Lorentz scalar → **DP1U-05 / DP1U-19 / DP1U-NJ4-01** (Fierz projection via eq:AAdecomp; AA/PP attractive channels bounded by leg-(B), mean-field framework disclosed).
- **UNMATCHED#6 [MAJOR] Route-2 Eq.(17) not derived; [∂ϑ_NY]=2≠H₀ dim-1; Eq.(18) doesn't follow; 10⁻⁶⁰ suppression** → **DP1U-09** (∂ϑ_NY dim +2 stated explicitly; ∂ϑ∼H substitution disclosed as approximation; Route-2 labeled "exploratory framing, not load-bearing" L677/L2994).
- Route-3 Benedetti–Speziale β not a universal Lorentzian law; (Δγ/γ)(H₀/M_Pl) asserted → **DP1U-10** (scheme-spread + amplitude-budget conditional framing disclosed).
- **UNMATCHED#8 [MAJOR] Route-4 internally inconsistent free-vs-rigid photon coupling; naturalness not a no-go** → **DP1U-11** (R4 closed by naturalness/explanatory-deficit NOT amplitude, verbatim abstract; spectator-ALP imported, disclosed).
- **UNMATCHED#9 [MAJOR] Sec-IV-C gravitational Pontryagin conflated with dynamical Chern–Simons; §X transparency doesn't make it inert** → **DP1U-12** (§X scope explicitly excludes dynamical-γ / non-minimal; total-derivative-in-topologically-trivial disclosed).
- §X / Table-III canonical-scalar zero-spin-density is standard, can't be B14 against R1–R4 → **DP1U-12 / DP1U-13** (narrow scalar-sector identity, B8-subsumption disclosed at sec:barriers head).
- Inflationary-dilution inconsistent with algebraic torsion; n²∝a⁻⁶ not e⁻³ᴺ; N_tot≃92 fitted → **DP1U-14** (D_inf explicitly "mathematical scaffolding" after reheating reset; a⁻⁶ concerns the erased channel; N_tot spread disclosed).
- "13 independent constraints" don't constitute a theorem → **DP1U-13** (sec:barriers head discloses non-independence, B8 subsumed, B9 heuristic).
- **UNMATCHED#13 [MAJOR] App F–H / Figs 3–11 don't test ECH; stock-CAMB, 12% NaMaster under-recovery, ALP single-datum** → **DP1U-15** (each appendix labeled a stock-CAMB proxy / synthetic-sky / import, "not an ECH test").
- [MINOR] ρ_crit 0.27–0.41 mixes LQC conventions → **DP1U-23** (both values attributed to canonical γ-choices, disclosed).
- **UNMATCHED#15 [MINOR] 10¹²²→10⁵ fine-tuning has no probability measure** → **DP1U-14 / DP1U-24** (e-fold sensitivity, illustrative comparison scores disclosed as un-derived).
- **UNMATCHED#16 [MINOR] companions without arXiv IDs, Zenodo pending, repo docs outdated; refocus 62pp** → **DP1U-16 / DP1U-22** (reproducible-now via BigBounceRepro; TODO-SUBMISSION arXiv-ID markers; length/venue OPINION).

Every UNMATCHED item independently source-verified against live v1U.0.20 `.tex` this session
(R4 naturalness L247/L346/L354; ∂ϑ_NY dim +2 + exploratory-framing L677; DP1U-09).
ChatGPT engaged the NJL appendix via leg-(B)/Fierz only, did NOT rebut the leg-(A)
convention-independent sign exclusion (same partial-engagement pattern as NJ2/NJ3b/NJ4/NJ5/NJ6).
ChatGPT structural harsh-referee floor (directive-H). **0 genuinely-new.**

## Streak / Cap
- **Streak 5→6.** Prior M11-EXT was 4→5; M13-EXT = 0 genuinely-new on byte-unchanged v1U.0.20 → **5→6** (directive-K).
- **Cap 68→62 (LOWERED per formula, applied honestly).** M11 had Grok EXT **MINOR** (12) → cap 68. M13 Grok slips **MINOR→MAJOR** (12→6). New cap = 50 + grok(MAJOR 6) + chatgpt(REJECT 0) + gemini(EXT MAJOR carry-forward 6) = **62**. The verdict-word slip on unchanged content is pattern-066 noise, but the readiness-cap formula reads the LATEST per-reviewer verdict — so the cap honestly reflects the current Grok MAJOR (the streak still advances because the SCIENCE is unchanged with 0 genuinely-new; cap and streak are orthogonal per directive-K/H). No headline number changed; no bump.

## Integrity
Both raws read verbatim (Grok l.1 `VERDICT: MAJOR REVISIONS`, ChatGPT l.1 `VERDICT: REJECT`)
before any disposition. Grok MINOR→MAJOR slip diagnosed pattern-066 (M13 item set = M11 item
set, each MAJOR quotes the paper's own disclosure; Grok still supports the central claim). No
ACCEPT faked. Every finding source-cited to an existing D-id + tex line. No un-sourced dismissal.
No math fabricated. No hedging removed. No version bumped. `directive_g.sh` NOT run (no edit).
Cap lowered honestly to reflect the latest Grok verdict rather than masking the slip.
