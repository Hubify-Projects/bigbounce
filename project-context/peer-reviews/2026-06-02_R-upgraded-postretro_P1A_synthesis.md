# P1A R-upgraded-postretro 4-Vendor Direct R-Round — Truth Audit + Closure Synthesis

**Round label:** `2026-06-02_R-upgraded-postretro`
**Paper:** P1A — Channel-Level Closure of Four Minimal ECH Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Reviewed version:** v1A.0.41
**Closure version:** v1A.0.42
**Reviewer set:** Grok-4 (brutal) / GPT-4o-fallback-from-GPT-5 (methodology) / Perplexity Sonar-Pro (citations) / **Gemini-2.5-Pro (cosmology) — FIRST direct-vendor Gemini response in the campaign**
**Pattern catalog:** 34 patterns (`project-context/review-patterns/INDEX.md`)

---

## Per-finding truth audit table

Verdict legend: **VERIFIED** · **STALE** (previously closed; reviewer reading old artifact or framing already in text) · **FALSIFIED** (on-disk evidence contradicts) · **OPINION** (framing preference, not factual claim).

### Reviewer 1 — Grok-4 (brutal)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GRO-B1 | BLOCKER | Retitle to "Amplitude-Level Constraints ... Under a Phenomenological Ansatz"; move "not operator-level theorem" to abstract first paragraph | STALE / OPINION | 5, 19 | No action. Current title already removed "structural closure" → "Channel-Level Closure"; abstract sentence 2 already reads "This is a channel-level assessment, *not* an operator-level theorem"; missing operators enumerated by name in the abstract. Reviewer is asking for a second retitle of an already-softened title — counter-proposal, not a fact-claim. |
| GRO-B2 | BLOCKER | Headline numbers (N_tot≈92, β≈0.27°, ΔN_eff, fnl) sourced exclusively to "(in preparation)" companions; non-reproducible | STALE | 6, 20, 27 | No action. Companions are bibitem-registered with "(in preparation)" labels; abstract+§I+Table~I+§XII+§XIII+§XIV+conclusions all hedge with "in preparation / companion work" wording (sweep landed v1A.0.40, GPT-B10 closure). The β≈0.27°/fnl=-35/8/0.342° numbers are derived in this paper (Eqs.~16, 17, §IV.D, §VII); ΔN_eff and MCMC posteriors are correctly attributed to P1B in-prep. |
| GRO-M1 | MAJOR | "closure" / "13 logically-independent barriers" inflated vs literature | STALE / OPINION | 5 | No action. Already softened to "channel-level closure under stated assumptions" throughout (v1A.0.40); abstract explicitly says "13 logically-independent mechanism-class constraints" not "13 novel barriers". Literature-comparison table is a polish refactor, recorded as future-pattern. |
| GRO-M2 | MAJOR | Perturbation-transparency narrower than headline (canonical scalar only) | STALE | 5 | No action. Theorem §X already explicitly states "for canonical scalar field matter" in title, statement, and 5-step proof (L1417–1454); §X.E "What Would Break the Transparency" lists fermion / propagating-torsion / non-minimal exclusions; abstract sentence 4 says "for canonical scalar matter". Reviewer asks to retitle §X to a variant already 95% present. |
| GRO-m1 | minor | Preamble version-history comment block + future-dated metadata in source | STALE | 14 | No action. The `% v1A.0.42 …` block is in LaTeX `%` comments only — does NOT appear in compiled PDF body (verified L40–250 are all comment lines). Reviewer received raw .tex, not the PDF; this is the same misreading pattern as pattern-014 (text-comment not stripped). "Future-dated metadata" refers to today's date which is correct. |
| GRO-n1 | nit | Route 4 "naturalness objection rather than amplitude no-go" inconsistent with α/M-floated viability paragraph | STALE | — | No action. Section heading L1058 already reads "Route 4 ... naturalness objection rather than amplitude" and L1132 explicitly says "Route-4 status: a naturalness objection ... a free-coupling spectator-ALP fit reproduces both β_obs and ρ_Λ". Reviewer asks for clarifying sentence already present. |

### Reviewer 2 — GPT-4o-fallback-from-GPT-5 (methodology)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GPT-B1 | BLOCKER | Perturbation-transparency theorem overclaim; depends on canonical scalar matter assumption | STALE | 5, 9 | No action. Identical to GRO-M2 above. §X explicitly conditional; §X.E lists exclusions; abstract says "for canonical scalar matter". GPT-4o is the GPT-5 fallback (pattern-009 reduced-rigor framing). |
| GPT-B2 | MAJOR | Parity-odd term dimensional analysis inconsistent (off-shell +1 vs on-shell ansatz) | STALE | 5, 9 | No action. Abstract sentence 3 already reads "off-shell mass dimension is +1 rather than +4 (Appendix B); we treat this scaling explicitly as an ansatz, not a derivation". Appendix B labels the scaling phenomenological. Reviewer asks for content already present. |
| GPT-B3 | MAJOR | One-loop graviton 10^-58–10^-60 suppression mixes dimensionful and dimensionless | STALE / OPINION | 9 | No action. Route 2 (§IV.B) was rewritten in v1A.0.40 to adopt the canonical 10^-58 ordering with the 10^-33 alternative footnoted. Step-by-step derivation already in §IV.B + Appendix. GPT fallback re-flagging a previously-closed item. |
| GPT-B4 | MAJOR | Reheating thermal-reset relies on qualitative reasoning | STALE | 9, 22 | No action. §II.C.1 was rewritten in v1A.0.40 (Gem-3.1 + GPT-B9 closure) to source torsion from ⟨J^5_μ⟩ with explicit C/P-violating thermalization argument; Cartan equation propagates ⟨J^5_μ⟩→0 to mean-zero torsion. Quantitative simulation request is out-of-scope (no controlled simulation exists in the literature). |
| GPT-B5 | MAJOR | Route 4 closure summary mixes amplitude exclusion with naturalness objection | STALE | 9 | No action. Identical to GRO-n1. §IV.D heading already explicitly labels Route 4 "naturalness objection rather than amplitude no-go". Closure-summary §IV.E carries the distinction. |
| GPT-B6 | minor | Limitations section doesn't connect each limitation to main conclusions | OPINION | 9 | No action. Polish-tier framing, not a fact-claim. Limitations are already cross-referenced (§I Scope, §XIV.D, §XV). |

### Reviewer 3 — Perplexity Sonar-Pro (citations)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| PER-B1 | (calls itself BLOCKER) | Shapiro–Teixeira arXiv:1402.4854 fused metadata | FALSIFIED | 1, 3 | No action. The "PER-B1 round 3 Shapiro-Teixeira fictional" line is in the LaTeX `%`-comment changelog block (line 108), already FALSIFIED on disk (L108-110 record the truth-audit verdict). The bibitem `ShapiroTeixeira2014` in references.bib + .bbl is the real Quantum Einstein–Cartan with Holst paper. Perplexity is reading the changelog comment, not the bibliography — pattern-001 + pattern-003 textbook miss. |
| PER-M1 | MAJOR | Date–Kaul–Sengupta β-function over-attribution | STALE | 1, 12 | No action. L1019 cites DKS only for the "topologically invariant in the chiral-matter setting" qualitative statement; L1033 explicitly disclaims: "Eq.~\eqref{eq:gamma_running} only as an upper-bound EFT ansatz [...] not appearing verbatim from DKS"; L1037 attributes the actual fermion-induced running to Benedetti & Speziale [2011]. Already closed v1A.0.40 (GPT-B6) + v1A.0.38 round-2 PER-M1. |
| PER-M2 | MAJOR | Lue–Wang–Kamionkowski normalization blurring | STALE | 1 | No action. L1066 + L1074 already say "Lue, Wang & Kamionkowski [LWK1999]" provides "an early cosmological-birefringence framework", with the −¼(α/M)θFF̃ "normalization standard in the ALP literature; we adopt this normalization". The body explicitly does NOT attribute the coefficient to LWK. Already closed v1A.0.38 round-2 PER-M2. |
| **PER-m1** | **minor** | **Eskilt 2022 sole-source of 0.342°; Minami 2020 should be co-credited** | **VERIFIED** | **1, 28** | **CLOSED in v1A.0.42.** Abstract L317-318 only cited Eskilt~\cite{Eskilt2022} for the 0.342° number; Minami~\&~Komatsu~2020 is the originator. Body L1255 already attributes correctly; abstract was the only surface still implicit. Patched: "first reported by Minami~\&~Komatsu~\cite{Minami2020} and refined by Eskilt~\&~Komatsu~\cite{Eskilt2022}". |
| PER-m2 | minor | Ashtekar–Singh 0.27 value not in their paper | STALE | — | No action. L635-642 already say "Ashtekar & Singh quote the canonical LQC value ρ_crit ≈ 0.41 ρ_Pl at the standard LQC area-gap choice"; the 0.27 value is labeled "an internal [extrapolation] across counting schemes (not Ref.~\cite{Ashtekar2011})". Already closed v1A.0.38 round-2 PER-m1. |
| PER-n1 | nit | CQG 31:185002 (2014) Shapiro–Teixeira title traceability | OPINION | 1, 13 | No action. Duplicate of PER-B1. Bibitem is correct on disk. Perplexity counter-proposal lacks fact-claim; web-search confabulation pattern (pattern-013). |

### Reviewer 4 — Gemini-2.5-Pro (cosmology) [FIRST DIRECT GEMINI RESPONSE]

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GEM-B1 | BLOCKER | N_tot≈92 + structural tension rests on dim-inconsistent operator + on-shell scaling ansatz; not a controlled EFT | STALE | 5, 20, 22 | No action. Abstract sentence 3 + §I "Scope and Limitations" + Appendix B all flag the +1-vs-+4 dim mismatch and label the scaling phenomenological. §XIV.D "Structural Tension" is explicitly labeled "robustness check, not co-equal closure". The argument IS already reframed as schematic; reviewer asks to remove it entirely, which is a counter-proposal not a fact-claim. |
| GEM-B2 | BLOCKER | MCMC / SPHEREx Fisher / PTA results from "(in preparation)" companions are unverifiable | STALE | 6, 20, 27 | No action. Identical to GRO-B2. The companion hedge sweep landed v1A.0.40 (GPT-B10). The numbers Gemini lists (MCMC posteriors, SPHEREx, PTA spectral index) are ALL correctly attributed to P1B / P2 / P3 in-prep companions inline in abstract + §I + §XII + §XIII. The convention is standard for cross-paper bundled programmes. |
| GEM-M1 | MAJOR | Route 2 ambiguity 10^-58 vs 10^-33 (25 orders of magnitude); declaring "robust" by fiat | STALE | 22 | No action. §IV.B in v1A.0.40 explicitly adopts the 10^-58 canonical-ordering estimate with the 10^-33 alternative footnoted; closure is stated as "robust to the ordering choice because both bracketing estimates exceed the dark-energy budget by ≥30 orders of magnitude". This is GPT-B5 / Gem-4.1 closure from v1A.0.40 — Gemini is re-flagging a previously-closed item. |
| GEM-M2 | MAJOR | Perturbation-transparency violated by all known fermions; framing overstates applicability | STALE | 5 | No action. Identical to GRO-M2 / GPT-B1. §X explicitly restricted to "canonical scalar field matter"; §X.E lists fermion exclusion as breaking condition (1); abstract sentence 4 + §X.E + §X "Implications" all say the same. Reframing "as a baseline for a toy model" is a re-wording counter-proposal of content already present. |
| GEM-m1 | minor | Structural tension prominent in abstract but buried in §XIV.D ("robustness check, not co-equal") | OPINION | 5 | No action. The label "robustness check, not co-equal closure" was added at Houston's direction (v1A.0.38) to avoid overclaim. Promoting it to a standalone section is a structural choice already deliberately made the other way; reviewer's preference, not fact-claim. |
| GEM-m2 | minor | §II.C.1 conflates robust thermal-reset argument with weaker D_inf ∝ e^{-3N_tot} scaling | STALE | — | No action. §II.C.1 + §XII.A reminder block in v1A.0.40 (Gem-3.1 closure) already explicitly separate the two: thermal-reset is presented as primary (⟨J^5_μ⟩→0); D_inf exponential is explicitly framed as "mathematical scaffolding for a hypothetical un-reset channel, not a physically operative dilution". |

---

## Pattern catalog hits (incident counts this round)

| Pattern | Hits | Notes |
|---|---|---|
| 001 (perplexity-citation-confab) | 4 | PER-B1, PER-M1, PER-M2, PER-n1 |
| 003 (stale-comment-misread) | 2 | PER-B1, GRO-m1 |
| 005 (overclaim-language) | 7 | GRO-B1, GRO-M1, GRO-M2, GPT-B1, GEM-B1, GEM-M2, GEM-m1 |
| 006 (companion-paper-hedge) | 2 | GRO-B2, GEM-B2 |
| 009 (gpt-fallback-low-rigor) | 6 | All 6 GPT findings (model fell back to gpt-4o) |
| 012 (perplexity-web-search-miss) | 1 | PER-M1 |
| 013 (perplexity-counter-proposal-may-be-wrong) | 1 | PER-n1 |
| 014 (text-comment-not-stripped) | 1 | GRO-m1 |
| 019 (title-overclaim-vs-body) | 1 | GRO-B1 |
| 020 (load-bearing-disclosure-buried) | 3 | GRO-B2, GEM-B1, GEM-B2 |
| 022 (closure-narrative-instead-of-derivation) | 3 | GPT-B4, GEM-B1, GEM-M1 |
| 027 (headline-claim-without-on-disk-artifact) | 2 | GRO-B2, GEM-B2 |
| 028 (arithmetic-vs-cited-literature) | 1 | PER-m1 |

**No new-pattern candidates this round.** All 22 findings map cleanly to existing 34-pattern catalog. The catalog absorbed the failure modes as designed.

---

## Cumulative closure count

- **Total findings surfaced this round:** 22 (Grok 6 / GPT 6 / Perplexity 6 / Gemini 6)
- **VERIFIED closures landed in v1A.0.42:** 1 (PER-m1 — Minami 2020 added alongside Eskilt 2022 in abstract attribution of 0.342°)
- **STALE:** 17 (re-flags of items already closed in v1A.0.40 or earlier)
- **FALSIFIED:** 1 (PER-B1 — reviewer reading the .tex changelog comment, not the bibitem)
- **OPINION:** 3 (GPT-B6, GEM-m1, PER-n1)

---

## Round-quality comparison vs prior P1A externals

| Round | Findings | VERIFIED closures | BLOCKER survived audit | MAJOR survived audit |
|---|---|---|---|---|
| 2026-06-02 (prior, v1A.0.36 Houston-shared 3-reviewer external) | ~30 | 18 + 5 partial | 0 (5 closed) | 0 (8 closed) |
| **2026-06-02 (this round, v1A.0.41, upgraded+post-retro 4-vendor)** | **22** | **1** | **0** | **0** |

**Quality of findings DROPPED hard.** Prior external surfaced 18 VERIFIED closures of substantive content (title rewrite, scope paragraph, thermal-reset rewrite, Route 2 dim ambiguity resolved, Benedetti–Speziale citation correction, body-prose review-log strip, companion-hedge sweep). This round surfaced 1 single-line abstract-citation polish. The mechanical-sweep + upgraded-skill stack absorbed every other category of issue.

**Houston's hypothesis confirmed:** The upgraded skills + the v1A.0.40 mechanical sweep + the pattern catalog ARE doing the work — reviewers are running out of substantive things to find.

---

## Gemini's unique signal

This was the **first direct-vendor Gemini response** in the campaign (prior rounds all failed billing — pattern-015 gemini-billing-skip).

**What Gemini caught that others missed:** Nothing materially new. All 6 Gemini findings were also raised by Grok or GPT in this round, or had been raised by Grok / GPT / Gemini in the v1A.0.36 external round and closed in v1A.0.40. Gemini did NOT surface anything resembling a novel signal — it converged onto the same overclaim / load-bearing-disclosure / closure-narrative axis that the other 3 vendors hit.

**Interpretation:** Either (a) the four largest LLM cosmology reviewers are all reading the same surface failure modes and the catalog absorbs them, or (b) Gemini was in convergent-silence mode this round (pattern-010-style). Given Gemini took 52s of wall-time vs Grok's 12s and surfaced 6 findings (more than Grok and GPT individually), interpretation (a) is more likely than (b). Gemini IS thinking, but the paper genuinely doesn't surface much.

**One subtle Gemini-only nuance:** GEM-m2 separated the "robust thermal-reset" from the "weaker D_inf scaling" with the framing "weakening the stronger argument by tying it to the weaker one" — Grok / GPT didn't articulate that specific coupling concern. This is a polish-tier framing observation, not a substantive finding (already STALE — closure in v1A.0.40 already does the separation).

---

## Bump decision

**v1A.0.41 → v1A.0.42** triggered by single PER-m1 VERIFIED closure (real .tex edit at abstract L317-319).

---

## Consecutive-clean-round counter

This round counts as **1/3 for the upgraded-postretro track on v1A.0.42**: 0 surviving BLOCKER + 0 surviving MAJOR after truth audit, single polish-tier MINOR closed. Following AGENT_RULES §4.4.1 cascaded-loop exit criterion (zero convergent regressions + zero novel BLOCKERs + ≤1-2 polish-tier MAJORs for 2 consecutive rounds), one more clean round at v1A.0.42+ would re-satisfy exit. The earlier v1A.0.40 exit-satisfaction was on the v1A.0.36 baseline; bumping to v1A.0.42 restarts the post-bump counter at 1/3 here for safety.

---

## Honest self-assessment

The catalog absorbed the substantive content. 21 of 22 findings were correctly identifiable as STALE / OPINION / FALSIFIED on a 30-minute audit by checking the .tex against the prior round's closure synthesis. The 1 VERIFIED finding (Minami attribution in abstract) is exactly the polish-tier residue one would expect after a clean R-round. This is what "catalog doing its job" looks like — not zero findings, but zero substantive findings that aren't already closed in the .tex.

The risk: optimism bias. If Gemini-2.5-Pro (top cosmology reviewer, first time speaking in the campaign) found nothing materially new, AND Grok-4 in brutal mode found nothing new, AND GPT (even at fallback-4o) found nothing new — that's either a real cleanliness signal or the prompts are not eliciting the deep critique. Houston should consider commissioning a true blind external review (anonymous, no prior context, no prompt hints toward catalog patterns) before declaring P1A truly converged.
