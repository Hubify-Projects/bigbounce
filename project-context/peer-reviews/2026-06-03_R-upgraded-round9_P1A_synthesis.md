# P1A R-upgraded-round9 synthesis — truth-audit triage

**Paper**: `arxiv/paper1a_ech_nogo.tex` v1A.0.44
**Round**: 2026-06-03_R-upgraded-round9
**Cascaded counter (pre-round)**: 1 of 3
**Cascaded counter (post-round)**: **2 of 3** — convergent silence held (0 VERIFIED bump-grade findings)
**Pattern-008 (Pontryagin propagation) check**: CLEAN — no reviewer caught a regression in the abstract/§X/conclusions "non-zero pointwise but a total derivative" phrasing.

---

## Per-vendor finding count

| Vendor | Model | BLOCKER | MAJOR | minor | nit | Total |
|--------|-------|---------|-------|-------|-----|-------|
| Gemini-2.5-Pro (cosmology) | gemini-2.5-pro direct | 0 | 3 | 1 | 0 | 4 |
| GPT-5 (methodology) | gpt-4o FALLBACK | 4 ("B"-tagged) | 2 ("M"-tagged) | 0 | 0 | 6 |
| Grok-4 (brutal) | grok-4 direct | 1 | 2 | 1 | 1 | 5 |
| Perplexity Sonar-Pro (citations) | sonar-pro direct | 1 | 3 | 1 | 1 | 6 |
| **TOTAL** | — | **6** | **10** | **3** | **2** | **21** |

GPT used `gpt-4o` fallback (pattern-009 low-rigor); Gemini ran clean on billing (no pattern-015 skip).

---

## Per-vendor truth-audit table

### Gemini-2.5-Pro
| ID | Raw | Verdict | Pattern-IDs | Evidence |
|----|-----|---------|-------------|----------|
| GEM-M1 | MAJOR | **STALE** | 5, 22, 30 | §XII.A L1615-1628 already labels D_inf "parameterization-of-fine-tuning diagnostic, not viable dynamical channel"; §XIV.D header L1789 is verbatim "robustness check, not co-equal closure" |
| GEM-M2 | MAJOR | **STALE** | 5, 16 | Abstract L348-349 cites Cai:2009fn (matter-bounce class); detailed scope "scalar-only $w=0$" carried in §XIII L1694-1707 and Table I footnote L469. Reviewer wants the hedge re-stated earlier — already present in body |
| GEM-M3 | MAJOR | **STALE** | 5, 16, 20 | Abstract L317-320 already verbatim: "phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4 ... we treat this scaling explicitly as an ansatz, not a derivation" |
| GEM-m1 | minor | **OPINION** | 5 | §XV.B L1859 leads with 9σ then immediately ties to model-discrimination 0.73σ with explicit null-hypothesis distinction; reviewer requests reorder = stylistic preference |

### GPT-5 (gpt-4o fallback)
| ID | Raw | Verdict | Pattern-IDs | Evidence |
|----|-----|---------|-------------|----------|
| GPT-B1 | BLOCKER | **STALE** | 5, 9 | Abstract sentence 3 + Appendix B already name the +1 vs +4 mismatch; reviewer paraphrases existing text as "issue" |
| GPT-B2 | BLOCKER | **FALSIFIED** | 9 | Paper does NOT claim Holst dual "vanishes identically"; abstract L329-335 and §X.A explicitly state "non-zero pointwise but a total derivative ... contributes only a boundary term"; reviewer mis-reads (pattern-008 inverse-confab) |
| GPT-B3 | BLOCKER | **OPINION** | 9 | Error-propagation lives in companion Paper I(b)/II per scope split; not a P1A gap |
| GPT-B4 | BLOCKER | **OPINION** | 9 | Bayes-factor framing not used as primary closure in P1A; Paper I(b) carries marginalization |
| GPT-M1 | MAJOR | **STALE** | 9 | One-loop suppression factor application is consistent across abstract/§II.C.1/§XII.A; reviewer asserts inconsistency without citing two lines |
| GPT-M2 | MAJOR | **STALE** | 5, 9 | §XIV.D header is literally "robustness check, not co-equal closure"; abstract L340 + §IV explicit |

### Grok-4
| ID | Raw | Verdict | Pattern-IDs | Evidence |
|----|-----|---------|-------------|----------|
| GRO-B1 | BLOCKER | **STALE** | 5, 19 | Abstract L309-311 already says "channel-level assessment, *not* an operator-level theorem" verbatim; "closure" qualified explicitly at L362-369. Reviewer asks for language already present |
| GRO-B2 | MAJOR | **STALE** | 3, 14, 17 | Lines 1-291 are LaTeX %-comment review-log (pattern-014 in review-patterns/INDEX.md); not rendered in PDF body; comment-stripping is a pre-arXiv mechanical step, not a content fix |
| GRO-B3 | MAJOR | **STALE** | 5, 22 | Abstract L317-320 + §IV Scope already state "demonstrates an explanatory deficit under a stated scaling assumption, not a derived no-go"; reviewer paraphrases existing text |
| GRO-M1 | minor | **STALE** | 16 | Paper says verbatim everywhere "13 logically-independent (14 historical catalog entries, of which B8 is subsumed by B14)" (abstract L321-326, §XV L1846-1847, Table I caption) |
| GRO-m1 | nit | **OPINION** | 5 | Pontryagin sentence shortening = pure style; current phrasing flagged CLEAN by all other reviewers for pattern-008 propagation |

### Perplexity Sonar-Pro
| ID | Raw | Verdict | Pattern-IDs | Evidence |
|----|-----|---------|-------------|----------|
| PER-B1 | BLOCKER | **FALSIFIED** | 1, 12 | All four Golden2026 P1b/P2/P3/P4 companions registered in `paper1a_ech_nogo.bbl` with "in preparation" annotations; Perplexity web-search cannot see in-prep companions (pattern-012); R-multi-true95 already audited this falsified |
| PER-M1 | MAJOR | **STALE** | 1 | Shapiro & Teixeira attribution softened in R2 closure v1A.0.38 (see %-comment L168-170); abstract + §II.C.1 already say "motivated by but not literally derived in" |
| PER-M2 | MAJOR | **STALE** | 1, 12 | Date-Kaul-Sengupta β-function attribution softened in R2 closure v1A.0.38 (%-comment L171-174); §IV Route 3 already says "schematically motivated by"; Benedetti-Speziale credited |
| PER-M3 | MAJOR | **STALE** | 1 | LWK normalization clarification landed R2 v1A.0.38 (%-comment L175-180); §IV.D L1100-1115 verbatim what PER requests |
| PER-m1 | minor | **STALE** | 1 | Ashtekar-Singh 0.41/0.27 separation landed R2 v1A.0.38 (%-comment L181-184); §II.B explicit |
| PER-n1 | nit | **FALSIFIED** | 1 | `paper1a_ech_nogo.bbl` L307-318 verified on disk: HehlDattaNJL1971 entry has correct title, authors (F.W. Hehl + B.K. Datta), year (1971), journal (J. Math. Phys. 12, 1334). "NJL" lives only in bibtex key, not title field |

---

## Summary

| Bucket | Count |
|--------|-------|
| Total findings | 21 |
| **VERIFIED (bump-grade)** | **0** |
| STALE | 16 |
| FALSIFIED | 3 |
| OPINION | 2 |
| BLOCKERs landed | 0 |
| MAJORs landed | 0 |
| minors landed | 0 |
| Closures applied this round | 0 (no edits) |
| Version bump | none — paper stands at v1A.0.44 |

## Pattern hits (review-patterns/INDEX.md)

Top patterns triggered this round:
- **pattern-001 (Perplexity citation-confab)**: 6 hits — all Perplexity findings re-litigate already-closed R2 attributions
- **pattern-005 (overclaim language)**: 11 hits — most reviewers ask for hedging already present
- **pattern-009 (GPT fallback low-rigor)**: 6 hits — gpt-4o fallback consistently paraphrases existing text as findings
- **pattern-014 (text-comment not stripped after review)**: 1 hit — Grok mis-reads %-comment block as body prose
- **pattern-016 (exit-boundary wide-net reflag)**: 3 hits — reviewers reflag known-stale items as we approach cascaded exit
- **pattern-022 (closure-narrative instead of derivation)**: 2 hits
- **pattern-012 (Perplexity web-search miss)**: 1 hit — in-prep companions invisible to web search

No new pattern candidates surfaced (already-catalogued patterns explain all 21 findings).

## Exit-criterion check (AGENT_RULES §4.4.1)

Cascaded-loop exit requires **3 consecutive rounds** of: zero convergent regressions + zero novel BLOCKERs + ≤1–2 polish-tier MAJORs.

- R8 (round 8 v1A.0.44, 2026-06-02): 1/3 — 24 findings, 0 VERIFIED
- **R9 (this round v1A.0.44, 2026-06-03): 2/3 — 21 findings, 0 VERIFIED**
- R10 (next round): 3/3 → if 0 VERIFIED again, cascaded exit MET

**Status**: P1A v1A.0.44 stands. Counter advances 1/3 → **2/3**. No edits this round. One more clean convergent-silence round closes the cascaded loop. Houston sign-off remains the only gate between 95% and 99%.
