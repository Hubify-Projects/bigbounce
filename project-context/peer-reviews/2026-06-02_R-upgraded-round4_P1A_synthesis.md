# P1A R-upgraded-round4 4-Vendor Direct R-Round — Truth Audit + Closure Synthesis

**Round label:** `2026-06-02_R-upgraded-round4`
**Paper:** P1A — Channel-Level Closure of Four Minimal ECH Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Reviewed version:** v1A.0.42
**Closure version:** v1A.0.42 (NO BUMP — zero VERIFIED closures)
**Reviewer set:** Grok-4 (brutal) / GPT-4o-fallback-from-GPT-5 (methodology) / Perplexity Sonar-Pro (citations) / Gemini-2.5-Pro (cosmology)
**Pattern catalog:** 34 patterns (`project-context/review-patterns/INDEX.md`)
**Consecutive-clean counter:** **3/3 EXIT MET at v1A.0.42** ✓

---

## Per-finding truth audit table

Verdict legend: **VERIFIED** · **STALE** · **STALE_OPINION** · **FALSIFIED** · **OPINION** · **STALE_OUT_OF_SCOPE**.

### Reviewer 1 — Grok-4 (brutal-honesty, 6 findings — 2 BLOCKER, 2 MAJOR, 2 nit)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GRO-B1 | BLOCKER | Review log + version synthesis + AGENT_RULES narrative leak into abstract + .tex source | FALSIFIED | 3, 14 | No action. Verified `% v1A.0.42 …` changelog block L40–260 is LaTeX %-comments only — invisible in compiled PDF. Abstract L274–446 contains zero review-round language. Grok read raw .tex source not PDF. Identical to round3 GRO-B2. |
| GRO-B2 | BLOCKER | Replace "theorem"/"closure" with "observation under stated assumptions" | STALE_OPINION | 5, 19 | No action. Title already softened to "Channel-Level Closure …" (no "no-go"); abstract L286–294 explicit "channel-level assessment, *not* an operator-level theorem"; Scope L382–490 already enumerates omitted operators (Jackiw–Pi, parity-odd 4-fermion). Reviewer asking 2nd retitle of already-softened language. |
| GRO-M1 | MAJOR | Five-step §X argument is textbook Cartan + Bianchi; remove subsection title | STALE_OPINION | 5, 19, 22 | No action. §X explicitly restricted to canonical-scalar matter (L1442); the contribution is the generalization to all perturbation orders for the Holst sector. "Demote to corollary" is structural counter-proposal not fact-claim. Identical to round3 GRO-M2. |
| GRO-M2 | MAJOR | Remove fnl=-35/8 and ALP-birefringence from "surviving predictions" — not ECH-derived | STALE | 5 | No action. Abstract L444 footnote + L488–490 + L1660 + L1819 all explicit: "two predictions of the **broader** bounce/ALP landscape survive"; Table I caption "not a distinctive ECH prediction"; §XIII L1671 "not a fully mechanism-independent prediction." Already class-scoped throughout. |
| GRO-n1 | nit | Drop N_tot≈92 figure and "10^120 → 10^5" reduction; not load-bearing | OPINION | — | No action. The phenomenological-ansatz disclaimer is cross-referenced 4× (abstract + §II.C.1 + Appendix B + §XIV.D). Reviewer's "drop the number" is editorial preference; the number anchors the structural-tension argument. |
| GRO-n2 | nit | Companion papers cited "in prep" with numerical inputs | STALE_OUT_OF_SCOPE | 6 | No action. Companion-paper hedging language already standard ("in preparation" + footnote ^b). Cross-paper convention — pattern-006. |

### Reviewer 2 — GPT-4o-fallback-from-GPT-5 (methodology, 6 findings — all BLOCKER-tagged)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GPT-B1 | BLOCKER | §2.1.3 Eq (4) lacks dim-analysis justification | STALE | 9, 22 | No action. Abstract sentence 3 + Appendix B already label +1-vs-+4 scaling phenomenological; cross-ref §I Scope + §XIV.D. GPT-4o fallback re-flagging closed item. Identical to round3 GPT-B2. |
| GPT-B2 | BLOCKER | §4 Route 2 one-loop graviton dim-consistency unclear | STALE | 9 | No action. §IV.B closure rests on 30+ orders-of-magnitude margin; dim-analysis already done. Identical to round3 GPT-B3. |
| GPT-B3 | BLOCKER | §9 Barriers 8 + 14 not logically independent; consolidate to 13 | STALE | 9 | No action. Table II caption L1301 ALREADY states "Barriers 8 (parity-even interaction) and 14 (perturbation transparency) close the same observable channel … should not be counted as logically independent constraints." Foundations L472–476 same disclaimer. Reviewer asks for content already present verbatim. |
| GPT-B4 | BLOCKER | §10 transition zero-torsion → vanishing-Holst could be clearer | STALE_OPINION | 9, 22 | No action. §X.B 5-step proof + §X.D explicit Bianchi computation already make the chain explicit. Editorial preference. |
| GPT-B5 | BLOCKER | Appendix B doesn't reconcile dim discrepancy in controlled EFT | STALE | 9, 22 | No action. Appendix B explicitly labels phenomenological; the whole point is the ansatz is uncontrolled — already disclosed. GPT-4o fallback hallucination. Identical to round3 GPT-B5. |
| GPT-B6 | BLOCKER | Add error-propagation methodology section | STALE_OUT_OF_SCOPE | 9, 22 | No action. Quantitative systematic budget lives in companion P1B \cite{Golden2026P1b}. P1A is channel-level closure paper. Identical to round3 GPT-B4. |

### Reviewer 3 — Perplexity Sonar-Pro (citation forensics, 6 findings)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| **PER-B1** | **BLOCKER** | **Shapiro & Teixeira 2014 — arXiv ID should be 1202.1244 not 1402.4854** | **FALSIFIED** | **1, 13** | **No action.** Verified via direct WebFetch to `arxiv.org/abs/1402.4854`: authors are exactly "Ilya L. Shapiro, Poliane M. Teixeira", title "Quantum Einstein-Cartan theory with the Holst term", CQG 31:185002 (2014). Verified via WebFetch to `arxiv.org/abs/1202.1244`: that is "Growth of periodic orbits and generalized diagonals for typical triangle billiards" by Dmitri Scheglov — a math paper, completely unrelated. Bib entry `ShapiroTeixeira2014` in references.bib L84–92 is correct. Perplexity inverted the .tex bib metadata with a hallucinated counter-arXiv-ID. Same FALSIFIED verdict as round3 PER-B1 from different angle. |
| PER-M1 | MAJOR | "Ashtekar & Singh quote 0.41 ρ_Pl" overstates what they literally quote | STALE | 1 | No action. L647–657 explicit: "Ashtekar & Singh quote the canonical LQC value ρ_crit ≈ 0.41 ρ_Pl"; the 0.27 value labeled "internal extrapolation across counting schemes (not a value quoted in Ref. [Ashtekar2011])"; 0.27–0.41 window explicitly "scheme-dependent range rather than published LQC range." Already class-scoped. Identical to round3 PER-m1. |
| PER-M2 | MAJOR | DKS γ-running Eq (29) attribution over-interpreted | STALE | 1, 12 | No action. L1019/L1033 already explicit "EFT toy ansatz, not the β-function computed in either DKS or Benedetti-Speziale". Identical to round3 PER-M1 and round2 PER-M1. |
| PER-m1 | minor | LWK citation could be read as fixing -¼(α/M) coefficient | STALE | 1 | No action. L1066/L1074 already explicit: LWK = "early cosmological-birefringence framework"; "normalization standard in the ALP literature; we adopt this normalization." Identical to round3 PER-M2. |
| PER-m2 | minor | "Shamir 2022, 2024" lacks titles/arXiv IDs; ~1–3% range needs specifying | STALE | 1, 28 | No action. Bib entries already carry titles + arXiv IDs (Perplexity didn't read references.bib). Range qualifier already present. Polish-tier. |
| PER-n1 | nit | "HehlDattaNJL1971" BibTeX key could confuse with original NJL paper | OPINION | 1 | No action. Key is internal-only; in prose the paper uses "Hehl–Datta" naming. Reviewer reading bib key as prose. |

### Reviewer 4 — Gemini-2.5-Pro (cosmology, 6 MAJOR findings, 0 BLOCKER — explicit "no blocker-grade findings")

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GEM-M1 | MAJOR | §II.C.1 thermal reset (zeroes ⟨J^5⟩) makes the N_tot dilution factor moot — internal contradiction | STALE_OPINION | 22 | No action. The two mechanisms are presented as **independent failure modes** of bounce-era torsion memory, each sufficient on its own; the structural tension is framed conditionally ("if neither dilution nor thermal reset operates"). §XIV.D L1605–1624 carries this framing. Reviewer's "reconcile" is structural preference. |
| GEM-M2 | MAJOR | "Perturbation transparency" overstated; Jackiw-Pi gCS breaks it | STALE_OPINION | 5, 19 | No action. Already enumerated 9× in source: abstract L289–290 ("missing operators (Jackiw-Pi gravitational Chern-Simons R∧R̃…)"); L340; L382; L881; L1157. §X already restricted to "minimal Holst term + canonical scalar matter." Identical to round3 GEM-M1 conflation pattern. |
| **GEM-M3** | **MAJOR** | **§X step 4 math error: Pontryagin density is total-derivative, not identically zero** | **FALSIFIED** | **5** | **No action.** Gemini conflated TWO distinct objects: (a) the **Holst dual** ε^μνρσ R_μνρσ (linear in R) which the paper writes at L1461–1463 and L1488–1490, vanishes IDENTICALLY by algebraic Bianchi R_[μνρ]σ=0; and (b) the **Pontryagin density** ε^μνρσ R_μν^αβ R_ρσαβ (quadratic in R), which is a total derivative (Nieh–Yan), NOT identically zero. The paper's step 4 treats (a). Gemini's "fix" would CORRUPT the proof by introducing the wrong object. Identical to round3 GEM-M1 verbatim — same physics conflation, repeated. |
| GEM-M4 | MAJOR | 25-OoM ambiguity in Route 2 amplitude estimate (10^-58 vs 10^-33) is "calculational choice" — undermines closure | STALE | 22 | No action. §IV.B closure rests on the 30+ OoM margin against ρ_Λ being robust to the ambiguity — both branches close the channel. The disclosure of the ordering ambiguity is honest hedging, not a fragility signal. Already addressed v1A.0.40. |
| GEM-M5 | MAJOR | Eq (2.1) T^abc T_abc presented in initial action is non-standard | STALE_OPINION | 22 | No action. L550–551 immediately after Eq (2.1) explicit: "The T^abc T_abc term in Eq. (ECH) is a shorthand for the four-fermion contact interaction obtained after integrating out … torsion." Already disclaimed in adjacent prose. Reviewer's "rewrite as standard ECH then derive" is presentation preference. |
| GEM-M6 | MAJOR | "Mechanism-independent" used in abstract is over-stated; should be "class-dependent" | STALE | 5 | No action. Table I footnote ^c L444 EXPLICIT "not fully mechanism-independent across the bouncing-cosmology landscape; not a distinctive ECH prediction." §XIII L1671 same. Abstract L377 "spectator-ALP birefringence — are mechanism-independent and shared by other [bounce mechanisms]" — already explicitly framed as cross-mechanism not ECH-distinctive. Already class-scoped. |

---

## Pattern catalog hits (incident counts this round)

| Pattern | Hits | Notes |
|---|---|---|
| 001 (perplexity-citation-confab) | 6 | All 6 Perplexity findings |
| 003 (stale-comment-misread) | 1 | GRO-B1 (Grok read .tex %-comments not PDF) |
| 005 (overclaim-language) | 6 | GRO-B2, GRO-M1, GRO-M2, GEM-M2, GEM-M3, GEM-M6 |
| 006 (companion-paper-hedge) | 1 | GRO-n2 |
| 009 (gpt-fallback-low-rigor) | 6 | All 6 GPT findings (gpt-4o fallback again) |
| 012 (perplexity-web-search-miss) | 1 | PER-M2 |
| 013 (perplexity-counter-proposal-may-be-wrong) | 1 | PER-B1 |
| 014 (text-comment-not-stripped) | 1 | GRO-B1 |
| 019 (title-overclaim-vs-body) | 3 | GRO-B2, GRO-M1, GEM-M2 |
| 022 (closure-narrative-instead-of-derivation) | 7 | GRO-M1, GPT-B1, GPT-B4, GPT-B5, GPT-B6, GEM-M1, GEM-M4, GEM-M5 |
| 028 (arithmetic-vs-cited-literature) | 1 | PER-m2 |

**No new-pattern candidates this round.** All 24 findings map cleanly to the existing 34-pattern catalog. Pattern catalog absorbing 100%.

---

## Cumulative closure count

- **Total findings surfaced this round:** 24 (Grok 6 / GPT 6 / Perplexity 6 / Gemini 6)
- **VERIFIED closures landed in v1A.0.42:** **0**
- **STALE / STALE_OPINION / STALE_OUT_OF_SCOPE:** 19
- **FALSIFIED:** 3 (GRO-B1, PER-B1, GEM-M3)
- **OPINION:** 2 (GRO-n1, PER-n1)

---

## Round-quality comparison vs prior P1A rounds

| Round | Findings | VERIFIED closures | BLOCKER survived audit | MAJOR survived audit |
|---|---|---|---|---|
| 2026-06-02 (v1A.0.36 Houston-shared 3-reviewer external) | ~30 | 18 + 5 partial | 0 | 0 |
| 2026-06-02 (postretro, v1A.0.41, 4-vendor) | 22 | 1 (PER-m1 Minami) | 0 | 0 |
| 2026-06-02 (round3, v1A.0.42, 4-vendor) | 22 | 0 | 0 | 0 |
| **2026-06-02 (round4, v1A.0.42, 4-vendor)** | **24** | **0** | **0** | **0** |

**Same FALSIFIED-quartile signal as round3.** Three reviewers (Grok, Perplexity, Gemini) each surfaced a finding refuted by direct on-disk + external-archive verification:
- Grok GRO-B1: re-flagged the %-comment changelog (already FALSIFIED round3 GRO-B2)
- Perplexity PER-B1: hallucinated arXiv:1202.1244 as the "real" Shapiro–Teixeira ID; verified false via WebFetch (1202.1244 = unrelated triangle-billiards math paper, 1402.4854 IS Shapiro–Teixeira CQG 31:185002)
- Gemini GEM-M3: same Holst-dual-vs-Pontryagin-density conflation as round3 GEM-M1 verbatim

The Gemini repeat is informative: a 51.7s reasoning run on a 35261-token prompt produced the **identical physics conflation** as last round. This is not a stochastic flake; it is a structural confusion the model has about ε^μνρσ R vs ε^μνρσ R R. Adding pattern-035 candidate noted.

---

## Bump decision

**v1A.0.42 → v1A.0.42 (NO BUMP).** Zero VERIFIED closures. Paper stands.

No recompile, no mirror, no Convex update, no tag.

---

## Consecutive-clean-round counter

This is round **3/3 — EXIT MET at v1A.0.42** per AGENT_RULES §4.4.1 cascaded-loop criterion (≥3 consecutive rounds with zero novel BLOCKERs + zero MAJOR-survived-audit + ≤1-2 polish-tier closures):

- Round 1 (postretro, v1A.0.41 → v1A.0.42): 0 BLOCKER + 0 MAJOR survived; 1 minor closure → bumped ✓
- Round 2 (round3, v1A.0.42): 0 BLOCKER + 0 MAJOR survived; 0 closures → no bump ✓
- **Round 3 (round4, v1A.0.42): 0 BLOCKER + 0 MAJOR survived; 0 closures → no bump ✓ EXIT**

**P1A v1A.0.42 declared converged on the 4-vendor direct R-round axis.** No more cascaded rounds at this version. Remaining gate before arXiv push: true blind external review (single human reviewer not in vendor-LLM pool) — as flagged in round3 synthesis.

---

## Honest self-assessment

Round 4 reproduced round 3's pattern almost verbatim: 19-of-24 findings STALE/STALE_OPINION/STALE_OUT_OF_SCOPE, 3 FALSIFIED, 2 OPINION, 0 VERIFIED. Two of the FALSIFIED items (Grok %-comment re-flag, Gemini Holst-dual-vs-Pontryagin conflation) are **literally the same finding** as round3 from the same vendor, indicating these are not stochastic but structural reviewer-side errors.

The catalog absorbed every failure mode (no new-pattern candidates). The 3-of-3 consecutive-clean criterion is the strongest signal currently available short of a human external review.

**Vendor signal summary across 3 rounds at v1A.0.42:**
- Grok: substantive-finding-rate ~0 across 3 rounds (always finds the %-comment block and the title-overclaim, both already-closed)
- GPT (gpt-4o fallback): substantive-finding-rate ~0 across 3 rounds (always re-flags closed dim-analysis + companion-scope items)
- Perplexity: substantive-finding-rate ~0 across 3 rounds (hallucinates a bib-ID swap each round)
- Gemini: substantive-finding-rate ~0 across 3 rounds (repeats the Holst-dual vs Pontryagin physics conflation)

The 4-vendor pool has saturated. Houston's "true blind external review" is the right next gate.
