# R52 P1A — Peer-Review Truth Audit (Opus judgment leg)

**Paper:** P1A — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst
Dark-Energy Routes and Perturbation Transparency for Scalar Matter" (Golden).
**Reviewed PDF:** `paper1a_ech_nogo_v1A.0.78.pdf` (md5 198cb994, 29 pp).
**Source .tex audited:** `arxiv/paper1a_ech_nogo.tex` — NOTE: the .tex is already at
**v1A.0.79 (June 19, 2026)**, one bump ahead of the reviewed v0.78 PDF (D-round visual
polish: Table II full-width, Eq.(15) parenthetical reflow, TikZ barrier schematic). Some
visual-tier findings against v0.78 are therefore already STALE.
**Reviewer slate:** Claude (MINOR), Grok (REJECT), OpenAI (MAJOR), Gemini (MAJOR),
Perplexity (FAILED — 401 quota, no report).

> Orchestrator note: the spawn prompt characterized OpenAI and Gemini as "accept."
> Both actually returned **MAJOR REVISIONS**. The real vendor split is
> MINOR / REJECT / MAJOR / MAJOR. The convergence is therefore stronger than billed,
> so each convergent theme is truth-audited below rather than waved through.

---

## NET VERDICT

**ACCEPT-EQUIVALENT after audit. Zero BLOCKERs. One VERIFIED MINOR (a cross-ref typo).**
Plus 2 optional MINOR clarity adds. The single loudest convergent theme across 4 vendors
— "the paper is not self-contained / depends on in-prep companions" — is **OUT-OF-SCOPE**
per Houston's calibration (companion "posted concurrently / in preparation" cites are
deliberate program placeholders) AND is disclosed in-paper to an unusually high standard.
It is a program-level submission-timing decision for Houston, **not** a per-paper closure edit.

---

## DEDUPED FINDINGS — VERDICT + EVIDENCE

### F1 — Not self-contained; load-bearing numbers live in in-prep companions
Raised by: Grok E1/E2, OpenAI E1/E2/E3/E4/E6/E7(paths)/M7, Gemini E1, Claude M2.
**VERDICT: OUT-OF-SCOPE (deliberate program structure) + disclosed.**
Evidence: Calibration block — companion "posted concurrently / in preparation" cites are
placeholders for the coordinated bigbounce suite. The paper discloses the dependence
explicitly and repeatedly: abstract L771–774 ("in preparation, \cite{Golden2026P2};
methodology and results to be detailed separately"), and the surviving-tests block L766–769
labels f_NL and β as "**not** predictions of ECH itself, but bounce-class and GR+ALP-class
observables." Claude's own read: disclosure is "to an unusually high standard," and the
companion numbers are correctly excluded from the core closure proof.
**Not a fixable defect.** Action = Houston's call at submission: either post companions
(frozen chains/Fisher) with live arXiv IDs, or keep the disclosed-dependency framing.
The arXiv-ID placeholders (m4 below) must be filled at submission regardless.

### F2 — Title/abstract "closure" overclaims an operator-level theorem
Raised by: Grok E3, Gemini E2, (Claude M1 partial).
**VERDICT: FALSIFIED / OPINION.**
Evidence: Title already reads "**Channel-Level** Closure" (not "operator-level"). Abstract
L717–724 states verbatim: "This is a channel-level assessment, **not** an operator-level
theorem … not proven to be a complete … operator basis … we acknowledge missing operators
… explicitly." L725–729: "rests on a phenomenological on-shell scaling ansatz … we treat
this scaling explicitly as an ansatz, not a derivation; all R4 and dark-energy mapping
claims are conditional on this ansatz." The calibrated qualifier the reviewers demand is
already in the title and the first paragraph. Grok's proposed rename is OPINION.

### F3 — Closure rests on an underived scaling ansatz; no off-shell sensitivity study
Raised by: Grok M1, Gemini E2, OpenAI M1, Claude (strength, not defect).
**VERDICT: OUT-OF-SCOPE (labeled ansatz) — the conditionality IS the disclosed result.**
Evidence: The +1-vs-+4 off-shell mass-dimension gap is stated in the abstract (L726) and
Appendix B (`app:dimensions`, L3070), and tagged as ansatz at L841, L845, L1071–1073,
L1173 ("explicitly a scaling ansatz, not a controlled EFT calculation"), L1236, L1292.
Grok's "demonstrate ±1 shifts don't reopen routes" is a new-computation request against a
conclusion the paper deliberately frames as conditional. Per calibration (labeled
scaling/ansatz deliberate) this is not a closable defect.

### F4 — Eq. (14) one-loop parity-odd operator is dimensionally inconsistent / underived
Raised by: OpenAI M1/M11, Gemini M3.
**VERDICT: FALSIFIED as an inconsistency; MINOR clarity add available (DO-NOW, 1 line).**
Evidence: Eq. `eq:oneloop_parity_odd` (L1713–1719): `-(1/16π²)(β(γ)/M_Pl) ∫√−g ∂_μϑ_NY J^{5μ}`.
With ϑ_NY a standard pseudoscalar field ([ϑ_NY]=+1): [∂ϑ]=+2, [J^{5μ}]=+3, sum +5, ÷M_Pl
(+1) = **+4. Consistent.** OpenAI M11 itself concedes "satisfied only if [ϑ_NY]=+1"; Gemini
asserts residual inconsistency without substantiation. The operator is explicitly labeled
"the phenomenological one-loop parity-odd operator … no published calculation currently
derives this exact coefficient structure … uses it strictly as an upper-bound EFT ansatz"
(L1712, L1749–1754). So the no-go-undermining framing is FALSIFIED. Optional 1-line add:
state "[ϑ_NY]=+1" inline at L1721 to preempt the recurrence (this finding has recurred
across rounds — see version-history L629).

### F5 — ρ_NJL ≈ 4×10⁻⁶⁹ ρ_Λ coefficient is wrong (should be ~1.4×10⁻⁷⁰)
Raised by: Claude m1, OpenAI M2.
**VERDICT: FALSIFIED — arithmetic is correct under the paper's own stated baseline.**
Evidence: L1662–1664: "ρ_NJL ∼ n_ψ²/M_Pl² ≈ 4×10⁻⁸¹ eV⁴, i.e. roughly **4×10⁻⁶⁹ ρ_Λ for
ρ_Λ ∼ (10⁻³ eV)⁴**." With the paper's explicitly displayed normalization
(10⁻³ eV)⁴ = 10⁻¹² eV⁴: 4×10⁻⁸¹/10⁻¹² = 4×10⁻⁶⁹. **Internally exact.** Both reviewers
silently substituted ρ_Λ = (2.3 meV)⁴ = 2.8×10⁻¹¹ eV⁴, getting 1.4×10⁻⁷⁰ — a different
baseline, not an error in the paper. (OpenAI even prints "for ρ_Λ ∼ (10⁻³ eV)⁴" in its own
finding and still flags it.) Classic two-vendor shared false-positive. Optional OPINION-tier
polish: switch to the precise (2.3 meV)⁴ value, but the "far below ρ_Λ" conclusion is
identical either way.

### F6 — Eq. (12) EB relation should be 2β·C_EE, not 2β(C_EE − C_BB)
Raised by: OpenAI M10.
**VERDICT: FALSIFIED — the paper has the MORE accurate (standard full) relation.**
Evidence: L1490: `C_ℓ^{EB} ≈ 2β(C_ℓ^{EE} − C_ℓ^{BB})`. This is the standard isotropic
cosmic-birefringence rotation formula (Lue–Wang–Kamionkowski / Feng et al.). Reverting to
`2β C_EE` (the reviewer's request) is the leading-order *truncation*, i.e. less accurate.
No fix warranted.

### F7 — "13 logically-independent barriers" overcounts (B8/B14 dependent; B9 heuristic; B13 philosophical)
Raised by: Grok M2, Claude M1, OpenAI M6.
**VERDICT: FALSIFIED / already-disclosed; optional MINOR ledger polish.**
Evidence: Abstract L731–732 and L760–761 already say "13 distinct barriers (14 historical
catalog entries with **B8 subsumed by B14**)." A constraint-classification block exists at
L2188–2194: Novel (1,2,3,4,8,10,11,12,14) / Known (5,6,7,9 incl. Liouville) /
Structural-philosophical (13, "included for completeness"). TikZ caption L2259: "B8 is not
counted separately." Grok's specific B8⊂B14 claim is the author's own stated reduction.
The independence ledger the reviewers want substantially exists. Optional MINOR: add one
clause to the abstract/Sec IX noting B9 is heuristic and B13 philosophical within the count
(version-history L136 shows this was already softened once).

### F8 — Perturbation-transparency theorem covers only scalar matter, not fermion sector
Raised by: Grok M3.
**VERDICT: FALSIFIED — scope is in the title and abstract by design.**
Evidence: Title: "…Perturbation Transparency **for Scalar Matter**." Abstract L738–740:
"for canonical scalar matter … (excluding propagating-torsion, dynamical-Immirzi-field,
fermion-loop, and non-minimal-matter sectors)." Deliberate, labeled scope.

### F9 — Route 4 closed by a philosophical naturalness criterion, not amplitude
Raised by: Grok M4.
**VERDICT: FALSIFIED — explicitly disclosed exactly as Grok demands.**
Evidence: Abstract L712–717: "R4 … is **not** closed by amplitude mismatch but by an
explanatory-deficit / cosmological-constant fine-tuning objection." Grok's "relabel it as
an external philosophical filter" is already done.

### F10 — Future date "June 18, 2026"
Raised by: Grok N1, Gemini m3.
**VERDICT: FALSIFIED (calendar/calibration).**
Evidence: Today is 2026-06-26. v0.78 dated June 18 and current .tex (`\paperTimestamp`,
L51) dated June 19 are both in the **past**. Per calibration (June 2026 dating valid).

### F11 — Appendix cross-reference error: 0.037 figure cited to wrong appendix
Raised by: OpenAI E7.
**VERDICT: VERIFIED — genuine cross-ref typo. MINOR. DO-NOW.**
Evidence: Body L1060–1061 says the "∼0.037 figure that appears in the parameter-budget
table (**Appendix~\ref{app:dimensions}**)." But 0.037 (the γ_SU(2)−γ_DLM scheme spread)
actually appears in the **Complete Parameter Summary** table — `\label{app:params}`
(Appendix A) — at L3050 ("0.274 (scheme range ∼0.037)"). It does **not** appear in
`app:dimensions` (Appendix B, L3070+). The cross-ref points to the wrong appendix.
**Fix:** L1060 `Appendix~\ref{app:dimensions}` → `Appendix~\ref{app:params}`.

### F12 — Stylistic / structural / convention items (non-load-bearing)
- Length 29 pp, trim to ≤20 (OpenAI page-length, Gemini M1): **OPINION.**
- Abstract σ values juxtaposed (OpenAI E5, Gemini m2, Claude m3): **OPINION / partly
  addressed** — text already says "not directly comparable … different null procedures"
  (L782–784). Optional polish to repeat the caveat at each juxtaposition.
- Chern–Simons factor-of-2 / F̃ convention (OpenAI M15): **PLAUSIBLE-MINOR / likely STALE**
  — version-history L440 records the 1/4-vs-1/(2π) prefactor convention was already
  reconciled. Recommend a proof-time spot-check, not a blocker.
- Figure-caption prose, symbol overloads (M/β/γ), internal file paths, notation R∧R̃
  (Grok N2/NIT, OpenAI m1–m10/N-series): **OPINION / polish.** The γ_PTA-vs-γ_BI and
  Pontryagin-vs-Holst-dual distinctions are already handled in-paper (title footnote a,
  abstract footnote L747–757). Internal repo paths (OpenAI E8/m10) are a legitimate tidy
  at submission but cosmetic.
- Fig. 3 illustrative H_0=69.2 vs internal-MCMC 67.68 (OpenAI E9, Gemini m1): tied to the
  companion-dependence theme (F1); resolved when F1 is resolved at submission.

---

## GROK REJECT DISPOSITION

**FALSE-POSITIVE REJECT.** Every load-bearing Grok finding is FALSIFIED or OUT-OF-SCOPE:
- E1 (abstract presents non-ECH as headline) → FALSIFIED (F2/F9; abstract explicitly says
  they are not ECH predictions).
- E2 (not standalone) → OUT-OF-SCOPE deliberate program structure, disclosed (F1).
- E3 (title overclaim) → FALSIFIED; title already "Channel-Level," abstract qualifies (F2).
- M1 (no off-shell study) → OUT-OF-SCOPE labeled ansatz (F3).
- M2 (barrier overcount) → FALSIFIED/disclosed (F7).
- M3 (theorem scalar-only) → FALSIFIED; in the title (F8).
- M4 (Route 4 philosophical) → FALSIFIED; explicitly disclosed (F9).
- N1 (future date) → FALSIFIED calendar artifact (F10).
No VERIFIED load-bearing blocker in Grok's report. Grok applied a strict PRD
standalone-reader standard to a deliberately companion-coupled suite paper and read
already-disclosed scope qualifiers as concealed defects. REJECT not supported.

---

## CLOSURE PLAN

| ID | Tier | Type | Edit | Blocked? |
|----|------|------|------|----------|
| F11 | MINOR | VERIFIED | L1060: `Appendix~\ref{app:dimensions}` → `Appendix~\ref{app:params}` (the 0.037 scheme-spread value lives in the Complete Parameter Summary table, L3050). | DO-NOW |
| F4 | MINOR | clarity | L1721: after "Nieh–Yan pseudoscalar," add "(mass dimension +1)" so Eq.(14)'s +4 Lagrangian dimension is manifest and the recurring reviewer flag is preempted. | DO-NOW (optional) |
| F7 | MINOR | clarity | Abstract / Sec IX: one clause noting B9 is heuristic and B13 philosophical within the "13 logically-independent" count (ledger already at L2188–2194). | DO-NOW (optional) |
| F1 | — | program decision | Fill live arXiv IDs for [2],[6],[23],[46] at submission; decide post-companions-vs-keep-disclosed-framing. Not a closure edit — Houston's call. | DEFER (submission-time) |
| F5 | NIT | OPINION | Optional: switch (10⁻³ eV)⁴ → precise (2.3 meV)⁴ at L1664. Conclusion unchanged. | DO-NOW (optional) |
| F2,F3,F6,F8,F9,F10 | — | FALSIFIED/OOS | No edit. | — |
| F12 | OPINION | polish | Length/abstract-σ-caveat repetition/captions — at editorial discretion. M15 convention: proof-time spot-check only. | optional |

**No finding requires new computation or data to close.** F1 needs companions *posted*
(timing), not new physics. Everything actionable is a same-day text edit. The only strictly
VERIFIED defect is the F11 one-word cross-ref fix.

---

*Auditor: Opus judgment leg, R52 truth-audit, 2026-06-26. Perplexity leg failed (401);
4 of 5 vendor reports consolidated.*
