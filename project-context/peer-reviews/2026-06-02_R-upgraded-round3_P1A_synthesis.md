# P1A R-upgraded-round3 4-Vendor Direct R-Round — Truth Audit + Closure Synthesis

**Round label:** `2026-06-02_R-upgraded-round3`
**Paper:** P1A — Channel-Level Closure of Four Minimal ECH Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Reviewed version:** v1A.0.42
**Closure version:** v1A.0.42 (NO BUMP — zero VERIFIED closures)
**Reviewer set:** Grok-4 (brutal) / GPT-4o-fallback-from-GPT-5 (methodology) / Perplexity Sonar-Pro (citations) / Gemini-2.5-Pro (cosmology)
**Pattern catalog:** 34 patterns (`project-context/review-patterns/INDEX.md`)
**Consecutive-clean counter:** **2/3 toward post-bump exit** at v1A.0.42

---

## Per-finding truth audit table

Verdict legend: **VERIFIED** · **STALE** (already closed; reviewer reading prior artifact or content already present) · **STALE_OPINION** (already-closed framing complaint) · **FALSIFIED** (on-disk evidence contradicts) · **OPINION** (framing preference, not factual claim) · **STALE_OUT_OF_SCOPE** (request belongs to companion paper).

### Reviewer 1 — Grok-4 (brutal-honesty, 6 findings)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GRO-B1 | BLOCKER | Replace "closure"/"no-go"/"theorem" with "amplitude estimates under phenomenological ansatz"; remove "theorem" from title | STALE_OPINION | 5, 19 | No action. Title already "Channel-Level Closure ..." (no "no-go"); abstract sentence 2 already "channel-level assessment, *not* an operator-level theorem"; missing operators (Jackiw-Pi, parity-odd four-fermion) enumerated by name. Reviewer asking for second retitle of already-softened title. |
| GRO-B2 | BLOCKER | Hundreds of lines of review-round logs / pattern-IDs / vendor names leak into abstract and body | FALSIFIED | 3, 14 | No action. Verified by reading abstract L282-378: ZERO review-round language in the rendered body. The `% v1A.0.42 …` changelog block (L40-260) is LaTeX `%`-comments only — invisible in compiled PDF. Grok read raw .tex source, not PDF. Identical to GRO-m1 from prior round. |
| GRO-M1 | MAJOR | Route 4 declared "closed by naturalness" while text shows free α/M ALP reproduces both β_obs AND ρ_Λ | STALE | 5 | No action. §IV.D heading L1058 already "naturalness objection rather than amplitude no-go"; L1132 explicit "a free-coupling spectator-ALP fit reproduces both β_obs and ρ_Λ". Reviewer asks for content already present (verbatim). |
| GRO-M2 | MAJOR | "Perturbation-transparency theorem" reduces to textbook canonical-scalar→Holst-topological | STALE_OPINION | 5, 19 | No action. §X explicitly restricted to canonical-scalar matter (L1442); §X.E lists fermion / propagating-torsion / non-minimal as breaking conditions; the contribution flagged is the generalization of Hehl 1976 to the Holst sector + all perturbation orders. "Demote to remark" is a structural counter-proposal not a fact-claim. |
| GRO-m1 | minor | Abstract presents 0.342° as joint Planck/ACT in one clause then corrects in next | FALSIFIED | 1, 28 | No action. Verified abstract L329-336: "first reported by Minami & Komatsu and refined by Eskilt & Komatsu" (WMAP+Planck) — THEN — "comparable to the independent ACT DR6 follow-up β = 0.215° ± 0.074° (Diego-Palazuelos & Komatsu)". The two measurements are correctly separated, not conflated. Reviewer misread structure. |
| GRO-n1 | nit | Repeated "dimensional-analysis aesthetic" statements for (T_reh/M_GUT)^{3/2} | OPINION | — | No action. Cross-referencing the load-bearing disclaimer in abstract+§II.C.1+Appendix B is intentional per pattern-020 (avoid burial). Reviewer's preference is editorial. |

### Reviewer 2 — GPT-4o-fallback-from-GPT-5 (methodology, 6 findings — all BLOCKER-tagged)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GPT-B1 | BLOCKER | Channel-level closure not operator-level; abstract should emphasize | STALE | 5, 9 | No action. Abstract L286-294 already explicit: "channel-level assessment, *not* an operator-level theorem"; Jackiw-Pi + parity-odd four-fermion enumerated by name. Identical to GRO-B1. |
| GPT-B2 | BLOCKER | §2.4 Eq (9) parity-odd action lacks dimensional justification | STALE | 9, 22 | No action. Abstract sentence 3 + Appendix B explicitly label scaling phenomenological with +1 off-shell vs +4 required; cross-referenced in §I Scope + §XIV.D. GPT-4o fallback re-flagging closed item. |
| GPT-B3 | BLOCKER | §4.2 Route 2 one-loop graviton lacks higher-loop discussion | STALE | 9 | No action. §IV.B Route 2 closure rests on 30+ orders-of-magnitude margin against ρ_Λ — robust to one-loop vs two-loop ambiguity. Already addressed v1A.0.40. |
| GPT-B4 | BLOCKER | §6 systematic analysis doesn't propagate CMB birefringence errors explicitly | STALE_OUT_OF_SCOPE | 9, 22 | No action. Quantitative birefringence systematic budget lives in companion P1B \cite{Golden2026P1b} (NaMaster + MCMC). P1A is channel-level closure paper, not CMB-pipeline paper. Standard cross-paper convention. |
| GPT-B5 | BLOCKER | Appendix B dimensional analysis inconsistent with main text | STALE | 9, 22 | No action. Appendix B explicitly states phenomenological ansatz; main text §IV invokes same +1-vs-+4 framing. No on-disk inconsistency. GPT-4o fallback hallucination. |
| GPT-B6 | BLOCKER | §10 transparency lacks observational-tests implications | STALE_OPINION | 9 | No action. §X.E + §X "Implications" + §XIII "Surviving Tests" subsections already present. GPT fallback editorial counter-proposal. |

### Reviewer 3 — Perplexity Sonar-Pro (citation forensics, 6 findings)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| **PER-B1** | **BLOCKER** | **arXiv:1402.4854 is Shapiro & Takata, not Shapiro & Teixeira** | **FALSIFIED** | **1, 13** | **No action.** Verified via direct WebFetch to `arxiv.org/abs/1402.4854`: authors are exactly "Ilya L. Shapiro, Poliane M. Teixeira" (NOT Takata). Perplexity hallucinated "Takata" — there is no such author on that arXiv ID. Bib entry `ShapiroTeixeira2014` in references.bib L84-92 is correct. Pattern-001 + pattern-013 textbook miss; SAME FALSIFIED verdict as prior PER round attempts where Perplexity flagged this from different angles. |
| PER-M1 | MAJOR | γ-running formula not in DKS or Benedetti-Speziale literally | STALE | 1, 12 | No action. L1019 cites DKS only for qualitative topology statement; L1033 already explicitly disclaims "EFT toy ansatz, not the β-function computed in either DKS or Benedetti-Speziale". Identical to round-2 PER-M1. |
| PER-M2 | MAJOR | Lue-Wang-Kamionkowski normalization blurring | STALE | 1 | No action. L1066+L1074 already explicit: "LWK provides early cosmological-birefringence framework" and "−¼(α/M)θFF̃ normalization standard in the ALP literature; we adopt this normalization". Body explicitly does NOT attribute coefficient to LWK. |
| PER-m1 | minor | Ashtekar-Singh 0.27 value not in their paper | STALE | 1, 28 | No action. L635-642 already explicit: "Ashtekar & Singh quote canonical LQC value ρ_crit ≈ 0.41 ρ_Pl"; 0.27 labeled "internal extrapolation across counting schemes (not Ref. [Ashtekar2011])". Already closed round-2 PER-m1. |
| PER-m2 | minor | fnl=-35/8 not universal across matter-bounce class; specific to Cai 2009 | STALE | 1, 28 | No action. Abstract L322-326 already says "$\fnl=-35/8$ is a property of the matter-bounce class \cite{Cai:2009fn}, derived from contraction-phase cubic action with no ECH input"; §XIII L1663-1675 explicit "scalar-only w=0 matter-bounce class"; Table V footnote ^c "Class-level: scalar-only w=0 matter-bounce under Assumption (f)". Already class-scoped throughout. |
| PER-n1 | nit | Minami 2020 Planck-only vs Eskilt 2022 WMAP+Planck — current text occasionally compresses | STALE | 1, 28 | No action. Abstract L331 explicitly: "first reported by Minami & Komatsu and refined by Eskilt & Komatsu". Citation order encodes the Planck-only → WMAP+Planck refinement. Already corrected v1A.0.42 (PER-m1 from postretro round). |

### Reviewer 4 — Gemini-2.5-Pro (cosmology, 4 findings)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| **GEM-M1** | **MAJOR** | **§X proof step 4 contradicts step 5: step 4 says "Pontryagin density vanishes by Bianchi", step 5 treats as non-vanishing total derivative** | **FALSIFIED** | **5** | **No action.** Gemini conflated two distinct objects: (a) the Holst dual ε^μνρσ R_μνρσ (linear in R), which DOES vanish by the algebraic Bianchi identity R_[μνρ]σ = 0; and (b) the Pontryagin density ε^μνρσ R_μν^αβ R_ρσαβ (quadratic in R), which does NOT vanish. The paper's step 4 (L1460-1463) treats (a) — Holst-evaluated-on-Levi-Civita — which IS identically zero by Bianchi. Step 5 ("no equations of motion") is a parallel argument applicable even if non-zero (total-derivative argument), not a contradiction. |
| GEM-M2 | MAJOR | §XIII unstated tension: fnl=-35/8 requires scalar-only (negligible fermion) which suppresses defining ECH spin-torsion coupling | STALE | 5 | No action. §XIII L1663-1675 already explicit: "scalar-only w=0 matter-bounce class; models with significant fermion sectors during the bounce give distinct predictions". Abstract L322 + §I.Scope + Table V footnote ^c all carry the qualification. The "unstated tension" is already stated. |
| GEM-M3 | MAJOR | §II.C.1 Eq (10) (T_reh/M_GUT)^{3/2} prefactor breakdown is physically weak; treat as fully phenomenological | STALE_OPINION | 22 | No action. §II.C.1 already explicit "phenomenological phase-space ansatz" and Appendix B labels scaling phenomenological. The sqrt(T_reh/M_GUT) DOS-factor framing is offered as physical intuition, not derivation — already disclaimed three times (GRO-n1). Reviewer's "drop the breakdown" is editorial preference. |
| GEM-m1 | minor | §XV item 2: "~9σ" LiteBIRD framing misleading; lead with 0.73σ discrimination | STALE | 5 | No action. §XV L1825 already presents BOTH numbers with explicit caveat: "~9σ (a 0.27°/0.03° overall sensitivity number); the relevant model-discrimination test … is … ≈ 0.73σ". The 9σ-is-naive framing is already explicit in-line, not buried. Reviewer's "remove 9σ entirely" is editorial counter-proposal. |

---

## Pattern catalog hits (incident counts this round)

| Pattern | Hits | Notes |
|---|---|---|
| 001 (perplexity-citation-confab) | 6 | PER-B1, PER-M1, PER-M2, PER-m1, PER-m2, PER-n1 (every Perplexity finding) |
| 003 (stale-comment-misread) | 1 | GRO-B2 (Grok read .tex %-comments, not PDF) |
| 005 (overclaim-language) | 7 | GRO-B1, GRO-M1, GRO-M2, GPT-B1, GEM-M1, GEM-M2, GEM-m1 |
| 009 (gpt-fallback-low-rigor) | 6 | All 6 GPT findings (model fell back to gpt-4o again) |
| 012 (perplexity-web-search-miss) | 1 | PER-M1 |
| 013 (perplexity-counter-proposal-may-be-wrong) | 2 | PER-B1, PER-n1 |
| 014 (text-comment-not-stripped) | 1 | GRO-B2 |
| 019 (title-overclaim-vs-body) | 2 | GRO-B1, GRO-M2 |
| 022 (closure-narrative-instead-of-derivation) | 4 | GPT-B2, GPT-B4, GPT-B5, GEM-M3 |
| 028 (arithmetic-vs-cited-literature) | 4 | GRO-m1, PER-m1, PER-m2, PER-n1 |

**No new-pattern candidates this round.** All 22 findings map cleanly to the existing 34-pattern catalog. The catalog absorbed every failure mode.

---

## Cumulative closure count

- **Total findings surfaced this round:** 22 (Grok 6 / GPT 6 / Perplexity 6 / Gemini 4)
- **VERIFIED closures landed in v1A.0.42:** **0**
- **STALE / STALE_OPINION / STALE_OUT_OF_SCOPE:** 17
- **FALSIFIED:** 4 (GRO-B2, GRO-m1, PER-B1, GEM-M1)
- **OPINION:** 1 (GRO-n1)

---

## Round-quality comparison vs prior P1A rounds

| Round | Findings | VERIFIED closures | BLOCKER survived audit | MAJOR survived audit |
|---|---|---|---|---|
| 2026-06-02 (v1A.0.36 Houston-shared 3-reviewer external) | ~30 | 18 + 5 partial | 0 | 0 |
| 2026-06-02 (postretro, v1A.0.41, 4-vendor) | 22 | 1 (PER-m1 Minami attribution) | 0 | 0 |
| **2026-06-02 (round3, v1A.0.42, 4-vendor)** | **22** | **0** | **0** | **0** |

**Quality of findings dropped further.** Postretro surfaced 1 single-line abstract polish; round3 surfaced ZERO substantive items. Notably FOUR findings this round are FALSIFIED (vs 1 in postretro), all variants of "reviewer read the wrong artifact" — three different reviewers (Grok x2, Perplexity, Gemini) each misread something different on disk:
- Grok read the .tex %-comment changelog (GRO-B2)
- Grok misread the abstract sentence structure (GRO-m1)
- Perplexity hallucinated author name "Takata" for arXiv:1402.4854 (PER-B1)
- Gemini conflated Holst dual (linear) with Pontryagin density (quadratic) (GEM-M1)

This is the FALSIFIED-quartile signal: when 4-of-22 findings cite content that on-disk verification refutes, the paper has converged enough that reviewers are reaching for non-existent issues.

---

## Bump decision

**v1A.0.42 → v1A.0.42 (NO BUMP).** Zero VERIFIED closures. Paper stands.

No recompile, no mirror, no Convex update, no tag.

---

## Consecutive-clean-round counter

This is round **2/3 toward post-bump exit at v1A.0.42**:
- Round 1 (postretro, v1A.0.41 → v1A.0.42): 0 BLOCKER + 0 MAJOR survived; 1 minor closure → bumped
- **Round 2 (this round, v1A.0.42): 0 BLOCKER + 0 MAJOR survived; 0 closures → no bump** ✓
- Round 3 (next): if matches → exit cascaded-loop criteria

Per AGENT_RULES §4.4.1 cascaded-loop exit (zero convergent regressions + zero novel BLOCKERs + ≤1-2 polish-tier MAJORs for 2 consecutive rounds), round 2 satisfies the post-bump criterion at v1A.0.42. One more clean round at v1A.0.42 → declared converged.

---

## Honest self-assessment

The catalog continues to absorb the substantive content. 17-of-22 findings were correctly identifiable as STALE / STALE_OPINION / STALE_OUT_OF_SCOPE on direct .tex inspection. The 4 FALSIFIED findings each represent a different category of reviewer error:
- raw-source misread (LaTeX comments rendered as body)
- structural-misread of well-formed prose
- LLM citation hallucination (verified false via direct arXiv fetch)
- physics conflation (Holst dual vs Pontryagin density)

The 1 OPINION-only item (GRO-n1) is a polish-tier nit.

**Optimism check.** Two consecutive 4-vendor direct rounds with zero substantive surviving findings is the cleanest possible outcome short of a blind external reviewer. The remaining risk vector is exactly what Houston flagged: optimism bias from auto-prompt-tuned reviewers. The "true blind external review" recommendation from the postretro synthesis still stands as the right next gate before final arXiv push.

**Specific Perplexity-confabulation note for the round.** Perplexity at 9309B was indeed heavy on arXiv-ID confabulations as predicted in the dispatch — all 6 Perplexity findings hit pattern-001, 2 also hit pattern-013, and the headline BLOCKER (PER-B1, "Shapiro & Takata") was confirmed false via direct arxiv.org fetch in seconds. Perplexity continues to be the lowest-signal vendor in the citation-forensic role despite its specialty; web-search is helping it generate plausible-sounding hallucinations rather than catching real metadata errors.
