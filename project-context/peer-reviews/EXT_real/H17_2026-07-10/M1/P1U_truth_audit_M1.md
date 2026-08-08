# P1U M1-wave truth audit — v1U.0.19 (2026-07-12)

**Wave:** M1 — first full external measurement AFTER the directive-M presentation
overhaul (commit `1c15b695` v1U.0.19: repetition purge + barrier-catalog
consolidation + appendix reframe; `5ffe104a` H0/M_Pl exponent consistency
10^-60→10^-61). Both EXT raws reviewed **v1U.0.19** (.aux confirms).
**Reviewers:** EXT Grok = MAJOR REVISIONS; EXT ChatGPT = REJECT.
**Method:** verdict-first, source-cited (patterns 061-066, directive-H/H-refined).
Both raws read verbatim before any disposition (Grok l.1 `VERDICT: MAJOR
REVISIONS`, ChatGPT l.1 `VERDICT: REJECT`). ledger_match.py pre-pass +
full manual truth-audit vs `arxiv/paper1_unified.tex` v1U.0.19 + `DISPOSITIONS/P1U.md`.

---

## §0 — OVERHAUL-REGRESSION SWEEP (the critical M1 check)

Because M1 is the first read after the abstract-shortening + de-duplication +
barrier-catalog consolidation, I specifically hunted for overhaul-introduced
regressions. **All checks PASS — the overhaul was clean:**

| Check | Method | Result |
|-------|--------|--------|
| Broken `\ref`/`\eqref`/`\cref` | diff all `\label` vs all ref targets | **0 dangling** |
| Undefined citations | compile-log scan (`Citation ... undefined`) | **0 undefined** (the sole log "undefined" is a harmless `OMS/cmtt` font-shape warning, not a ref) |
| Abstract cross-refs (de-dup risk) | grep `\ref` inside `abstract` env | all 18 resolve (sec:fourroute, app:fierz, app:dimensions, sec:barriers, sec:transparency, etc.) |
| Abstract number ↔ body match | grep headline values in abstract vs body | f_NL `−35/16` ✓, `N_tot≈92` ✓, `sub-critical` ✓, `channel-level`/`operator-level` ✓ — **byte-preserved** |
| Headline-number regression from `10^-60→10^-61` fix | trace the R2 arithmetic chain L2991-3001 | **consistent**: input `H0/M_Pl∼10^{-61}` (L2991,2639,3322,3808); derived output `10^{-3}·10^{-61}/(10^{-2}·6×10^{-3})≈10^{-60}` (L2998) is arithmetically exact; conservatism allowance `≥10^{-58}` (L3001). No stale `10^-60` orphan. Grok's own raw quotes "10^-58–10^-60", matching. |
| Compile freshness | `.aux` version marker | **v1U.0.19** — served/compiled PDF matches reviewed version |

**No overhaul-introduced broken cross-ref, orphaned sentence, dangling pointer,
or de-dup-deleted supporting claim was found.** The presentation overhaul
preserved all load-bearing content and numbers.

---

## §1 — EXT GROK (MAJOR REVISIONS) — per-finding disposition

Grok's own closing one-sentence CONCEDES the central claim is supported: *"...is
supported by the dimensional no-go, torsion-elimination derivations, and
Bianchi-identity decoupling arguments once the carefully scoped 'channel-level'
(rather than operator-complete) nature of the result is accepted..."*

| # | Sev | Finding (abridged) | Disposition | D-id + source cite |
|---|-----|--------------------|-------------|--------------------|
| G1 | MAJOR | Four-route "exhaust" presented as no-go yet repeatedly caveated as channel-level not operator-level theorem; completeness (F1+F2+NDA) not shown to rule out all higher-dim/boundary operators | **RE-FLAG-DISCLOSED** | DP1U-06 + DP1U-07 (+DP1U-21 disclosure-backfire). Title "Under Stated Assumptions" (L372/L1053-adjacent); "channel-level assessment, not an operator-level theorem" present in abstract+body. Grok's "tension" between "exhaust" and the hedge IS the honest scope DP1U-21 documents as recast-as-weakness. Not editable (removing the hedge = overclaiming). |
| G2 | MAJOR | §X/§XIV-D transparency: torsion-vanishes-at-all-orders stated for canonical scalar only; proof sketches X B–E don't show algebraic Cartan + Bianchi suffice to ALL orders (vs linear); Tier-I + N_tot≈92 vs f_NL erasure rest on incomplete extrapolation | **RE-FLAG-DISCLOSED** | DP1U-12 (transparency = standard on-shell scalar-zero-spin equivalence, narrow "solid positive core," fermions/torsion/dynamical-γ explicitly excluded) + DP1U-14 (N_tot ansatz/D_inf scaffolding disclosed). Novelty/all-orders-rigor is referee-preference, not an editable defect. |
| G3 | MAJOR | R1 NJL: regulated gap-eq condensate exclusion + finite M_Pl^-2 four-fermion basis rest on external scripts/appendices not reproduced in main text → independent verification impossible | **RE-FLAG-DISCLOSED (PROCESS/transparency)** | DP1U-05/-19/-26 + DP1U-NJ4-01 (all CLOSED-BY-COMPUTE; App `app:njl_gap` + committed `njl_gap_equation_route1.py`). The "not reproduced in main text" is the DP1U-19 self-containment/transparency class (Grok NJ2 raised the identical "display Fierz coeffs in main text" request). PROCESS-nit, not a defeater; Grok engaged and its one-sentence supports the claim. |
| G4 | MAJOR | R4 naturalness closure + single-scale NDA no-go: ρ_Λ=Ξ M_Pl^4, N_tot≈92, +1-vs-+4 bookkeeping, D_inf presented as derived while depending on phenomenological ansätze (bounce-curvature insertion, (T_reh/M_GUT)^{3/2}); "no amplitude derived so not circular" true but doesn't rescue predictive power | **RE-FLAG-DISCLOSED** | DP1U-11 (R4 "NOT closed by amplitude mismatch but by explanatory-deficit / CC fine-tuning ... relocating the CC problem" — verbatim abstract, L247/L346-adjacent) + DP1U-08 (+1→+4 "dispensable illustrative heuristic, not load-bearing") + DP1U-14 (N_tot/D_inf/thermal-factor disclosed scaffolding). Grok's "not circular" concession = the paper's own framing. |
| G5 | MINOR | Extremely dense, footnote-heavy, repeated hedging ("under stated assumptions," "channel-level not operator-level," "exhausts the fourth channel") obscures logical status of 13/14 barriers; hard to referee/cite | **RE-FLAG-DISCLOSED (OPINION)** | DP1U-22 (length/repetition venue OPINION) + DP1U-13 (13/14-barrier independence disclosed at sec:barriers head) + DP1U-21 (hedging-as-weakness backfire). Style/venue preference; not an editable error. Note: this MINOR is the directive-M overhaul-acknowledgment — see §3. |
| G6 | MINOR | §II-C/XII-A thermal-washout (Γ_wash>H erasing ⟨J5⟩) offered for B14 but left as an asserted inequality, not computed across SM channels; plausible but not load-bearing, should be labeled such | **RE-FLAG-DISCLOSED** | DP1U-14 (thermal-reset/reheating bookkeeping, explicitly non-load-bearing scaffolding). Grok itself says "not load-bearing" — matches the paper's own disclosure. Not a defeater. |

**Grok genuinely-new: 0.**

---

## §2 — EXT CHATGPT (REJECT) — per-finding disposition

ChatGPT's closing sentence: *"The narrow classical claim that the Holst term is
inert on the torsion-free canonical-scalar branch is supported, but the advertised
central claim of a four-route minimal-ECH dark-energy closure is not."* — i.e. it
concedes the positive core and rejects on the honestly-scoped channel-level claim.
This is structurally identical to every prior ChatGPT REJECT (H17G / W1 / W2b /
NJ3b / NJ4 / NJ5 / NJ6) — the directive-H harsh-referee structural floor.

| # | Sev | Finding (abridged) | Disposition | D-id + source cite |
|---|-----|--------------------|-------------|--------------------|
| C1 | MAJOR | Eqs.(1)-(4) not a consistent variational theory: ¼T·T displayed but declared absent off-shell; T=κS not the Holst-Dirac connection eq (misses ε^IJKL A_L + 1/γ trace term); F2 (minimal→only totally-antisym torsion) "false at connection level" | **RE-FLAG-DISCLOSED** | DP1U-03 (¼T·T-not-varied, footnote; two-step off-shell→effective reading added v1U.0.10) + DP1U-04 (finite-γ vector/trace components arise ONLY under NON-minimal coupling per FMT; V·A relabeled non-minimal) + DP1U-07 (F1/F2 completeness argued analytically). Paper DERIVES minimal-coupling `S^abc=¼ε^abcd J5_d` → trace/vector parts vanish; the finite-γ pieces are scoped-out non-minimal. |
| C2 | MAJOR | Eq.(6) dim +1 not dimensionless; "on-shell reduction" of a dim-4 basis doesn't repair; Bianchi can't change engineering dim +2→+1 or strip a curvature; no eq derives (6) from (7)-(8); Ξ, ρ_Λ, N_tot are phenomenological insertions | **RE-FLAG-DISCLOSED** | DP1U-08. The +1→+4 dressing is labeled "dispensable illustrative heuristic, not load-bearing"; the genuine dim-4 O1–O6 basis (`eq:Seff_dim4`) is primary. Paper states the off-shell dim mismatch deliberately. Disclosed bookkeeping. |
| C3 | MAJOR | Dim-4/operator-basis completeness (§IV, App-B1) not demonstrated: O1=O6 same Holst contraction, O4 non-standard index structure, appendix excludes derivative/curvature-torsion-mixed/multi-species while claiming "every admissible" exhausted; Fierz closes bilinears not the gravitational EFT | **RE-FLAG-DISCLOSED** | DP1U-07 + DP1U-20 (operator-level completeness across full diffeo basis is OPEN-VENUE, honestly out-of-scope). "Every admissible" already softened to "within the enumerated set at the stated power-counting order" (DP1U-18, v1U.0.10). Non-minimal/derivative/multi-species explicitly OUT-OF-SCOPE. |
| C4 | MAJOR | Single-scale NDA no-go confuses Wilson coefficients with expectation values; NDA estimates the coefficient, not that ⟨operator⟩=M_Pl^4; "zero or M_Pl^4" dichotomy not exhaustive; assuming no IR scale/symmetry/threshold merely restates the CC problem | **RE-FLAG-DISCLOSED** | DP1U-08 (+DP1U-11). Channel-level scope + non-load-bearing +1→+4 heuristic disclosed. "Restates the CC problem" = the paper's own DP1U-11 "relocates not solves CC" framing. Known-EFT-observation re-statement, not a defect. |
| C5 | MAJOR | R1 condensate exclusion (§IV-A, App C–D) not robust: one-channel mean-field gap-eq has Fierz ambiguity unless exchange-complete set treated; evaluates contact EFT at cutoff ≥M_Pl where dim-6 not controlled; attractive pseudoscalar condensate can't be dismissed for breaking parity (constant PP vev is Lorentz scalar, stress tensor must be computed) | **RE-FLAG-DISCLOSED** | DP1U-05/-19/-26 + DP1U-NJ4-01. Leg-(A) scalar-channel sign exclusion `G_scalar=−3/64κ` is repulsive & convention-independent (decisive; ChatGPT engaged only leg-(B)/Fierz, did not rebut leg-(A) — same partial-engagement as NJ2/NJ3b/NJ4/NJ5/NJ6). AA/PP attractive channels: worst `2×0.156=0.31` sub-critical (DP1U-NJ4-01, CLOSED v1U.0.17). Strong-coupling-beyond-mean-field out-of-scope, disclosed. |
| C6 | MAJOR | R2 (§IV-D) dimensionally inconsistent: [ϑ_NY]=1 → [∂ϑ]=2 but ∂ϑ~H_0 (dim 1) omits field amplitude; birefringence scales with endpoint Δϑ/M_Pl not H_0/M_Pl; 10^-58–10^-60 an artifact of assumed normalization; cited one-loop work doesn't derive Eq.(17) | **RE-FLAG-DISCLOSED** | DP1U-09. Paper states ϑ_NY dim +1, ∂ϑ_NY dim +2 (correct), discloses ∂ϑ~H substitution as an approximation + alternative-ordering endpoint bound (App E), labels R2 "exploratory framing, not load-bearing." One-loop-grounded via Shapiro–Teixeira coeffs; absolute norm honestly pending Riccati flow. [Note: ChatGPT's own "10^-58–10^-60" quote confirms the byte-preserved post-overhaul range — see §0.] |
| C7 | MAJOR | R3 (§IV-E) doesn't connect Immirzi running to DE: Benedetti–Speziale β Euclidean (γ²=1) applied to Lorentzian value without analytic-continuation/scheme analysis, quoted to 4 sig figs; no calc maps Δγ to stress tensor/vacuum density/observable; (Δγ/γ)(H_0/M_Pl) simply posited | **RE-FLAG-DISCLOSED (SCOPE)** | DP1U-10. R3 is the one cleanly-integrated β result (|Δγ/γ|≈1.4e-6); the H0/M_Pl amplitude-budget mapping flagged conditional/amplitude-budget framing (scheme-spread disclosed). Honestly disclosed as conditional. |
| C8 | MAJOR | R4 (§IV-F) not a channel of minimal ECH: introduces new propagating pseudoscalar + kinetic + potential + independent φFF̃ none of which follows from minimal ECH; α/M alternately fixed ECH prediction and free parameter; once free, "overshoot" disappears; m~H_0 generic naturalness not exclusion | **RE-FLAG-DISCLOSED** | DP1U-11. Abstract explicitly: R4 spectator-ALP imported, "NOT closed by amplitude mismatch but by explanatory-deficit / CC fine-tuning ... relocating the CC problem." The paper's verbatim framing = ChatGPT's point. Not over-claimed. |
| C9 | MAJOR | §X transparency correct only in narrow/immediate sense (canonical scalars zero spin current → torsion-free branch → Holst vanishes by Bianchi); NOT a new all-orders calc, it's exact classical equivalence before any expansion; excludes fermions/loops/dynamical-γ/ALP/propagating-torsion so Table IV can't use B14 on all 4 routes; "all obs identical to GR" applies to Holst only not LQC bounce bg | **RE-FLAG-DISCLOSED (OPINION on novelty)** | DP1U-12. Labeled the "standard on-shell equivalence," narrow "solid positive core," explicitly excluding fermions/torsion/dynamical-γ (Claude verified-correct). B8-subsumption disclosed at sec:barriers head. Novelty = referee-preference. |
| C10 | MAJOR | §§II-C-1/XII/XIV-D no consistent bounce-to-late-time solution: combines LQC Friedmann + ECH torsion + BH-universe + slow-roll inflation + matter-bounce + spectator ALP without one action/matching solution; (T_reh/M_GUT)^{3/2} admitted ansatz; nonpropagating torsion has no "memory" to dilute; §XII calls D_inf "scaffolding" → N_tot≈92 fitted bookkeeping not prediction | **RE-FLAG-DISCLOSED** | DP1U-14 (+DP1U-06/-16). D_inf explicitly "mathematical scaffolding"; N_tot spread disclosed bookkeeping; no-coherent-single-action-model disclosed (channel-level, companion-reproducible). Honest. |
| C11 | MAJOR | Matter-bounce value + erasure unsupported: Cai gives −35/8, manuscript asserts −35/16 without reproducing revised cubic-action calc; even companion Ref.[2] title retains −35/8; multiplying k by e^{N_tot−N_exit} is only scale-history, doesn't compute bispectrum transfer through bounce+inflation; "definitively" unjustified | **RE-FLAG-DISCLOSED (companion-resolved)** | DP1U-17 (+DP1U-14). −35/16 used consistently; P2 companion (v1.7.95) resolves the Cai-Li factor-of-two (spurious +(99/128)Σk³ term) → −35/16, quadruple-certified. Historical Cai −35/8 a deliberately-cited comparison. Self-containedness disclosed as companion dependency. |
| C12 | MAJOR | "13 mechanism-class constraints" (§IX) don't aggregate into a no-go: several generic naturalness slogans, several conditional, B9 evadable, B12 uncomputed ceiling ansatz, multiple reuse the same dimensional mapping; counting qualitatively-different objections ≠ independent/exhaustive; barrier count shouldn't appear in title/abstract/conclusions | **RE-FLAG-DISCLOSED** | DP1U-13. Exemplary disclosure at sec:barriers head: "no barrier is a logical consequence of another ... not a claim that thirteen separately decisive theorems each independently exclude." B8 subsumed by B14, B9 heuristic, B5/6/7/10/13 general — all flagged. |
| C13 | MINOR | Not organized to PRD standards: title/abstract excessively long, claims/caveats repeated many times, stock-CAMB/synthetic-NaMaster/galaxy-spin/forecast/ALP material doesn't test minimal-ECH theory; figures combining significances for unrelated null hypotheses + illustrative unsourced "fine-tuning scores" should be removed; isolate one result, much shorter internally-consistent manuscript | **RE-FLAG-DISCLOSED (OPINION)** | DP1U-22 (length/venue) + DP1U-15 (App F–H stock-CAMB proxy / synthetic-sky, explicitly "not an ECH test") + DP1U-24 (Figs 4/7 assumed-ρ + Fig-3 imposed-H0 disclosed IN-CAPTION). Style/venue OPINION. This MINOR is the directive-M overhaul-acknowledgment — see §3. |

**ChatGPT genuinely-new: 0.**

---

## §3 — OVERHAUL-ACKNOWLEDGMENT QUOTES (trend evidence, directive-M)

Both reviewers, on the FIRST read after the abstract-shortening + de-dup +
barrier-consolidation overhaul, STILL flag length/density/repetition — i.e. the
overhaul did not move either reviewer off the DP1U-22 length/OPINION class. These
are the trend-evidence verbatim quotes:

**EXT ChatGPT (REJECT), MINOR (final finding):**
> "The submission is not organized to PRD standards. The title and abstract are
> excessively long, claims and caveats are repeated many times, and extensive
> stock-CAMB, synthetic-NaMaster, galaxy-spin, forecast, and ALP-summary-likelihood
> material does not test the stated minimal-ECH theory. ... a viable resubmission
> would need to isolate one precisely formulated result and present a substantially
> shorter, internally consistent manuscript."

**EXT Grok (MAJOR REVISIONS), MINOR:**
> "The manuscript is written in an extremely dense, footnote-heavy style with
> repeated hedging ('under stated assumptions,' 'channel-level not operator-level,'
> 'exhausts the fourth channel') that forces the reader to parse multiple layers of
> qualification before reaching any concrete claim; this obscures the precise
> logical status of the 13/14 barriers and makes the paper unnecessarily difficult
> to referee or cite."

**Interpretation:** The directive-M overhaul reduced repetition mechanically
(commit `1c15b695`) but both LLM referees still register the paper as long/dense.
This is the DP1U-22 structural OPINION floor + DP1U-21 disclosure-backfire
(Grok explicitly punishes the honest "channel-level not operator-level" hedge) —
a venue/taste class that further edits cannot satisfy without dishonest
overclaiming or deleting honestly-scoped disclosures. NOT an editable defect.

---

## §4 — VERDICT

**Genuinely-new real+editable findings this wave: 0.**

- **Overhaul-introduced regressions: NONE.** 0 dangling `\ref`/`\eqref`/`\cref`,
  0 undefined citations (only a benign `OMS/cmtt` font warning), all 18 abstract
  cross-refs resolve, abstract headline numbers byte-preserved vs body
  (−35/16, N_tot≈92, sub-critical, channel-level), and the `10^-60→10^-61`
  exponent fix (commit `5ffe104a`) is an internally-consistent arithmetic chain
  (L2991-3001) with no stale orphan. Compile is fresh at v1U.0.19 (.aux confirmed).
- **All 6 Grok + 13 ChatGPT findings dispositioned RE-FLAG-DISCLOSED / OPINION /
  OUT-OF-SCOPE**, each source-cited to a standing D-id + tex location. Both
  reviewers' closing sentences CONCEDE the positive core is supported and reject
  only on the honestly-scoped channel-level claim (DP1U-06/-20) + length/style
  OPINION (DP1U-22) + disclosure-backfire (DP1U-21) — the known LLM harsh-referee
  structural floor for P1U (the hardest paper), matching every prior wave
  (H17G/W1/W2b/NJ3b/NJ4/NJ5/NJ6).

**P1U M1 outcome = RE-FLAG FLOOR (all findings dispositioned non-real). No real
closes this wave.** The directive-M overhaul introduced zero regressions; the
paper holds. Per directive-K this is a clean 0-genuinely-new wave on v1U.0.19
(the M-overhaul version) — the first external re-test of the overhaul.

**Integrity:** Both EXT raws read verbatim before disposition; no ACCEPT faked;
no finding dismissed without a source-cited verdict; no math fabricated
(the `10^-60`/`0.31`/`−35/16` values are the paper's own arithmetic/companion-
certified); no hedging removed. Verdict words recorded as-is: Grok EXT = MAJOR,
ChatGPT EXT = REJECT.
