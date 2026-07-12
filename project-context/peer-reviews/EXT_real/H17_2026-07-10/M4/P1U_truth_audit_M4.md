# P1U M4-EXT truth-audit — v1U.0.19 (2026-07-12) — STRICT ledger-first

**Raws audited (read verbatim, in full):**
- `EXT_real/H17_2026-07-10/M4/P1U_grok_M4.md` — VERDICT: **MAJOR REVISIONS** (3 MAJOR + 2 MINOR)
- `EXT_real/H17_2026-07-10/M4/P1U_chatgpt_M4.md` — VERDICT: **REJECT** (16 MAJOR + 2 MINOR)

**Cross-check:** prior M4-INT truth-audit (`INT_api/H17_2026-07-10/M4_INT_truth_audit.md`) already found
**0 genuinely-new** on the SAME byte-unchanged v1U.0.19; it diagnosed the Claude MIN→MAJ slip as
pattern-066 referee oscillation (severity re-grade on unchanged content, zero fresh items). Paper source
`arxiv/paper1_unified.tex` confirmed `\paperVersion = v1U.0.19` (L54), byte-unchanged since the NJ/M-era waves.

UNMATCHED-by-fingerprint findings (Grok mass-dim MINOR + presentation MINOR; ChatGPT #2/#7/#12/#14/#15/#17)
were each independently source-verified against the live `.tex` (grep evidence cited inline below), not assumed.

The Grok raw line `REVISIONS ISSUES:` region and the ChatGPT header line are parse artifacts, not findings.

---

## RAW 1 — EXT Grok (MAJOR REVISIONS)

| # | sev | verdict | D-id / .tex evidence | reason |
|---|-----|---------|----------------------|--------|
| 1 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-06** (+DP1U-21) | "abstract/Table I frame as 'channel-level closure' that 'exhausts the fourth channel'... completeness lemma should be elevated to a numbered subsection." The paper's title already says "Under Stated Assumptions" and the abstract states verbatim "channel-level assessment, not an operator-level theorem" (L1219, L1389-90; grep confirms channel-vs-operator caveat throughout). "Elevate to numbered subsection" = presentation preference; the lemma is in §IV b + App C. Disclosure-backfire (DP1U-21). Not editable. |
| 2 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-11** | "R4 is a naturalness/explanatory-deficit objection, not on the same footing as R1–R3 amplitude suppression; re-label 'naturalness objection' not 'closure'." This is verbatim the paper's own framing: abstract states R4 is "NOT closed by amplitude mismatch but by an explanatory-deficit / CC fine-tuning objection ... relocating the CC problem rather than solving it" (L1195-1198); evidentiary-tier table makes the R1–R3-vs-R4 asymmetry explicit. Exactly the reviewer's point, disclosed. Not editable. |
| 3 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-12** | "§X transparency proof high-level; term-by-term perturbed-tetrad expansion promised in §X E not shown; write out Bianchi step + Cartan slaving with explicit linearized eqs." Standard on-shell scalar-zero-spin-density equivalence, labeled the narrow "solid positive core" for canonical scalar matter (DP1U-12, L1248/L3333-adj). "Show more explicit lines" = presentation/rigor-preference on a disclosed narrow result; NJ4-Grok raised the identical "term-by-term not displayed" item → DP1U-12. Not a reader-visible defect. |
| 4 | MINOR | RE-FLAG-DISCLOSED | **DP1U-08** (mass-dim bookkeeping) | "on-shell (+1→+4) vs local-operator-promotion readings presented with different compensating M_Pl powers; consolidate side-by-side table showing identical numerical outcome." The +1→+4 dressing is labeled an "illustrative heuristic, subordinate to the operator basis" (L1974-1976) and the closure "survives at dimension 4 without the heuristic on-shell dressing" (L1303); the genuine dim-4 O1–O6 basis is primary (O4/O5 already at dim 4, L1990). The two readings agreeing at OOM for N_tot≈92 is disclosed bookkeeping. "Add a consolidated table" = presentation nicety. Not editable defect. |
| 5 | MINOR | RE-FLAG-DISCLOSED | **DP1U-22** (+DP1U-16) | "63 pages, footnote-dense, self-referential; observational appendices reduce standalone readability; condense; move scripts to Supplementary." Pure length/venue/style OPINION (DP1U-22, standing) + companion-reliance (DP1U-16, self-containment paragraph + reproducible-now artifacts). Referee variance, Houston-gated venue class. Not editable defect. |

**Grok closing one-sentence:** "the central claim ... is supported within the explicitly delimited scope."
→ Grok itself affirms the science holds; the MAJOR verdict is severity-on-presentation, pattern-066.

---

## RAW 2 — EXT ChatGPT (REJECT)

| # | sev | verdict | D-id / .tex evidence | reason |
|---|-----|---------|----------------------|--------|
| 1 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-03** | "Eq.(1) contains ¼T·T declared not-varied — action can't be both fundamental and on-shell shorthand; Eq.(3) not finite-γ Holst solution." Eq.(1) disclosed first-order Palatini–EC varied over {e,ω,ψ}, ¼T·T "not varied" appearing only after on-shell torsion elimination; two-step off-shell→effective reading added v1U.0.10. Verbatim DP1U-03. |
| 2 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-14** (+DP1U-16) | "no single dynamical model; LQC bounce eq doesn't follow from Eq.(1); no transition eqs contraction→bounce→inflation→reheating." Fingerprint UNMATCHED (best DP1U-14 @0.29) — VERIFIED re-flag: "no coherent single-action model / bounce-to-inflation matching conditions" is exactly the DP1U-14 fingerprint; D_inf disclosed "mathematical scaffolding," companion/self-containment disclosed (DP1U-16). Standing, disclosed as scope. Not new. |
| 3 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-07** (+DP1U-04) | "torsion decomposition incorrect for finite γ; totally-antisym Dirac current doesn't imply purely axial torsion; trace-torsion-only-under-nonminimal is false." The paper derives the minimal-coupling Dirac current totally-antisymmetric S^abc=¼ε J5 → trace/vector parts vanish; finite-γ vector components arise ONLY under non-minimal coupling, scoped out (DP1U-04, FMT). Same as NJ3b UNMATCHED#1. Re-flag. |
| 4 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-08** | "Eq.(6) dim +1 not +4; Bianchi can't strip a curvature factor / change engineering dimension; single-scale NDA is a naturalness estimate not a dimensional impossibility theorem." Verbatim DP1U-08: +1→+4 named a property of the on-shell reduction, labeled dispensable illustrative heuristic (L1974-76); dim-4 O1–O6 basis primary. Standing. |
| 5 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-07** (+DP1U-20) | "O1–O6 double-count / Fierz only rearranges indices / not a diffeo-invariant EFT completeness / EFT tower uncontrolled at E~M_Pl." Completeness argued analytically via F1+F2+NDA-monotonicity; non-minimal/derivative/higher-curvature irreps explicitly OUT-OF-SCOPE (DP1U-07); full operator-level theorem out-of-scope (DP1U-20). Disclosed. |
| 6 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-05** (+DP1U-19/-26/-NJ4-01) | "NJL: ⟨J5⟩=0⇏⟨J5·J5⟩=0; ISM density irrelevant to vacuum condensate; Popławski QCD-condensate; Fierz ambiguity." CLOSED-BY-COMPUTE v1U.0.14: regulated NJL gap eq + effective potential (App njl_gap): repulsive scalar channel (leg A, convention-independent sign) + sub-critical coupling (leg B). Standing. |
| 7 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-09** | "Route 2 10⁻⁶⁰ not derived; [ϑ_NY]=1 so [∂ϑ]=2 but ∂ϑ~H0 (dim 1); birefringence depends on endpoint Δϑ/M_Pl not bare H0/M_Pl." Fingerprint UNMATCHED (best DP1U-09 @0.29) — VERIFIED re-flag against source: paper states ϑ_NY dim +1 (L2888), ∂ϑ_NY dim +2 explicitly (L2976-77), discloses the ∂ϑ~H substitution "division by M_Pl" (L2976), gives the Δφ=f_a Δθ line-of-sight/endpoint form (L5181), and labels Route 2 "exploratory framing, not load-bearing" (L677/L3018). Verbatim DP1U-09. Not new. |
| 8 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-10** | "Route 3: Benedetti–Speziale flow convention/truncation-dependent; Euclidean (γ²−1) vs Lorentzian (γ²+1); never derives ρ_Λ operator ∝ (Δγ/γ)(H0/M_Pl); running a dimensionless coupling ≠ generating Λ." Verbatim DP1U-10: β-function result honest, H0/M_Pl amplitude-budget mapping flagged conditional. Standing. |
| 9 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-11** | "Route 4 naturalness mislabeled as closure; free-coupling ALP fits both β_obs and ρ_Λ = lack of predictivity not exclusion; α/M phenomenological; describe as external non-minimal model." Verbatim DP1U-11 = the paper's own abstract framing (L1195-98). Standing. Same class as Grok #2. |
| 10 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-12** | "§X transparency result narrower than claimed; doesn't constrain R1 (fermions)/R2-R3 (loop)/R4 (pseudoscalar); labeling B14 a constraint on R1–R4 conflates domains." DP1U-12 (+DP1U-13 B8/B14 subsumption): §X labeled the standard on-shell equivalence for canonical scalar matter, explicitly excluding fermions/torsion/dynamical-γ. Disclosed. |
| 11 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-14** | "inflationary dilution law ad hoc; derived interaction quadratic ⇒ J²∝a⁻⁶ not a⁻³; (T_reh/M_GUT)^{3/2} admitted phase-space ansatz; thermal-reset contradicts surviving diluted memory; N_tot≈92/ΔN≈4/10⁵ tuning not physical." Verbatim DP1U-14: D_inf "mathematical scaffolding," a⁻⁶ the erased channel already conceded not a prediction, N_tot spread disclosed bookkeeping. Standing. |
| 12 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-14** (§XIV.D erasure) | "§XIV.D erasure not demonstrated; multiplying k by e^{N_tot−N_exit} is scale bookkeeping not Bogoliubov coeffs; no transfer matrix / N_coh; 'definitively erased' → conjecture." Fingerprint UNMATCHED (best DP1U-17 @low) — VERIFIED re-flag: source shows "definitively erase(s)" IS the e^{N_tot−N_exit}~e^{32} physical-scale argument (L1343-44/L1559-60), disclosed as the class-level scale-erasure claim with the transfer-function Fisher forecast deferred to the P2 companion (L1550-52). This is the standing DP1U-14 matter-bounce-erasure item ("erasure claimed definitively") — the deferred detailed calc is disclosed, not hidden. Not new. |
| 13 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-17** | "f_NL=−35/16 attributed to Cai but Cai reports −35/8; general-c_s gives −35/16 at c_s=1; companion title still −35/8; derivation must appear here." Verbatim DP1U-17: value used consistently; P2 companion v1.7.95 resolves the Cai-Li factor-of-2 (spurious +(99/128)Σk³) → −35/16, quadruple-certified; self-containedness disclosed as companion dependency. Standing. |
| 14 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-13** | "13/14-barrier catalog: counting heterogeneous observations ≠ closure proof; B9 heuristic, B12 ansatz, B13 philosophical; barriers not independent; can't be cited in abstract/conclusion as collective closure." Fingerprint UNMATCHED (best DP1U-13 @low) — VERIFIED re-flag: sec:barriers head discloses verbatim "no barrier is a logical consequence of another ... not a claim that thirteen separately decisive theorems each independently exclude"; B8 subsumed by B14, B9 heuristic, B12 ceiling ansatz (L3882), B13 philosophical — all flagged in-paper. Exactly the reviewer's point, disclosed. Not new. |
| 15 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-15** | "App F stock-CAMB ΛCDM+ΔN_eff doesn't test/bound/validate ECH; torsion ∝a⁻⁶ vs constant ΔN_eff∝a⁻⁴; bespoke solver 'would return same null' is inference not calculation." Fingerprint UNMATCHED (best DP1U-15 @low) — VERIFIED re-flag: App F explicitly labeled a stock-CAMB ΔN_eff proxy / "not a proxy for an unknown ECH prediction," with the proxy validity established quantitatively (L2127/L2446/L4476-4488/L4631/L5288); disclosed "not an ECH test." Standing DP1U-15. Not new. |
| 16 | MINOR | RE-FLAG-DISCLOSED | **DP1U-24** (+DP1U-15) | "App G / Figs 4,7,10 not publication-ready; NaMaster ~12% multiplicative bias foreground-free synthetic; Figs 4/7 combine unrelated fNL/β with arbitrary correlation w/o joint likelihood; remove unless full model provided." DP1U-24: the ρ curves are labeled the *assumed* cross-correlation in-caption (L3483-87); NaMaster disclosed synthetic-pipeline validation (DP1U-15). Disclosed-in-caption. |
| 17 | MINOR | RE-FLAG-DISCLOSED | **DP1U-22** (+DP1U-06/-21) | "throughout: claims require radical narrowing; alternates 'illustrative/basis-complete/Tier-III/derived/naturalness closure/hard no-go'; ~half of 63pp non-load-bearing; publishable replacement = one action + one modest claim (torsion-free scalar decoupling), remove DE closure/barriers/observational synthesis." Fingerprint UNMATCHED ("radical narrowing") — VERIFIED re-flag: the multi-tier vocabulary IS the paper's own disclosed evidentiary-tier framing (channel-level not operator-level, DP1U-06); "radical narrowing / should be a shorter paper" = venue/scope OPINION (DP1U-22) + disclosure-backfire on the honest tier labels (DP1U-21). Not editable. |

**ChatGPT closing:** "supports only the narrow classical statement that a constant-Holst torsion-free scalar sector
reduces to GR; does not support the broader central claim." = the standing ChatGPT structural harsh-referee
REJECT floor (directive-H), identical structure to H17G / W1 / W2b / NJ3b / NJ4 / NJ5 / NJ6 ChatGPT REJECTs.

---

## Summary

**P1U M4-EXT genuinely-new: 0**

- **Grok (MAJOR REVISIONS):** 3 MAJOR + 2 MINOR, all source-cited re-flags → DP1U-06/-21, -11, -12, -08, -22/-16. Grok's own one-sentence affirms the science holds within scope; MAJOR = severity-on-presentation (pattern-066).
- **ChatGPT (REJECT):** 16 MAJOR + 2 MINOR, all source-cited re-flags → DP1U-03, -14/-16, -07/-04, -08, -07/-20, -05/-19/-26/-NJ4-01, -09, -10, -11, -12, -14, -14, -17, -13, -15, -24, -22/-21. Standing ChatGPT harsh-referee structural floor.
- **UNMATCHED-by-fingerprint resolved (all VERIFIED against live `arxiv/paper1_unified.tex`):**
  - Grok mass-dim MINOR → **DP1U-08** (L1303/L1974-76/L1990).
  - Grok presentation MINOR → **DP1U-22** (+DP1U-16).
  - ChatGPT #2 (no single dynamical model) → **DP1U-14** (+DP1U-16).
  - ChatGPT #7 (Route-2 10⁻⁶⁰ not derived) → **DP1U-09** (L2888/L2976-77/L5181; ∂ϑ dim +2 stated, exploratory-framing L677/L3018).
  - ChatGPT #12 (§XIV.D bispectrum erasure) → **DP1U-14** (L1343-44/L1559-60; e^{N_tot−N_exit} scale argument disclosed, detailed transfer deferred to P2 companion).
  - ChatGPT #14 (13/14-barrier catalog) → **DP1U-13** (sec:barriers head discloses non-independence; L3882).
  - ChatGPT #15 (App-F stock-CAMB) → **DP1U-15** (L2127/L2446/L4476-88/L5288).
  - ChatGPT #17 (throughout radical narrowing) → **DP1U-22** (+DP1U-06/-21).
- **Header artifact:** the raw header line region is a parse artifact, not a finding — noted, not dispositioned.

**Cross-check consistency:** the M4-INT truth-audit found 0 genuinely-new on the same v1U.0.19 and diagnosed
the INT-Claude MIN→MAJ as pattern-066 oscillation on byte-unchanged content. This M4-EXT audit independently
lands the same: 0 genuinely-new; every EXT MAJOR/MINOR is a source-cited re-flag of a standing D-id.

## Integrity statement

Both EXT raws read verbatim, in full, before any disposition (Grok l.1 `VERDICT: MAJOR REVISIONS`;
ChatGPT l.1 `VERDICT: REJECT`). No ACCEPT faked. No finding dismissed without a source-cited verdict —
every disposition cites a D-id and/or a specific `arxiv/paper1_unified.tex` line verified this session.
No math fabricated. No hedging removed. Every UNMATCHED-by-fingerprint finding was source-verified against
the live `.tex`, not assumed. The Grok-MAJOR / ChatGPT-REJECT verdict words are the documented LLM
harsh-referee structural floor on honestly-scoped, disclosed channel-level content — not editable defects.

**No bump; v1U.0.19 stands. `directive_g.sh` NOT run (no edit).**
