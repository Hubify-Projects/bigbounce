# P1A R-multi-round5 — Truth-Audit Synthesis (no version bump; stands at v1A.0.39)

**Round**: `2026-06-01_R-multi-round5`
**Paper**: P1A — Structural Closure of Einstein–Cartan–Holst Dark Energy
**Source**: `arxiv/paper1a_ech_nogo.tex`
**Pre-round version**: v1A.0.39
**Post-closure version**: **v1A.0.39 (unchanged; 0 VERIFIED findings)**
**Reviewers**:
- Grok-4 (direct vendor; brutal-honesty persona) — 2 BLOCKER + 2 MAJOR + 2 nit (all STALE/OPINION)
- GPT-4o (FALLBACK from gpt-5; methodology rigor persona) — 1 BLOCKER + 5 MAJOR (all restatements)
- Perplexity Sonar Pro (direct vendor; citation forensics) — 1 BLOCKER + 3 MAJOR + 2 minor (all attribution polish on cites already verified)
- Gemini-2.5-pro: skipped per Houston standing protocol (vendor billing failure; 3-of-4 acceptable)

Standing protocol applied: `memory/feedback_peer_review_truth_audit_protocol.md`.

Prior syntheses:
- `2026-06-01_R-multi-true95_P1A_synthesis.md` (v1A.0.36 → v1A.0.37, 2 closures)
- `2026-06-01_R-multi-round2_P1A_synthesis.md` (v1A.0.37 → v1A.0.38, 5 closures)
- `2026-06-01_R-multi-round3_P1A_synthesis.md` (v1A.0.38 → v1A.0.39, 1 closure)
- `2026-06-01_R-multi-round4_P1A_synthesis.md` (v1A.0.39 unchanged, 0 closures, clean-count 1/3)

---

## Truth-audit table

| Finding | Class | Reviewer claim (paraphrase) | On-disk verification (v1A.0.39) | Verdict |
|---------|-------|-----------------------------|---------------------------------|---------|
| GRO-B1 | BLOCKER | "Perturbation-transparency theorem" is the standard vanishing-spin-density consequence; retitle to "decoupling observation" | L252 already labels it "perturbation-transparency theorem"; the 5-step proof of B14 is the on-disk content (canonical scalar → vanishing spin density → vanishing torsion → Holst term inert → no birefringence/no parity-odd density at perturbation level). Round 4 GRO-M1 raised the same retitle preference; STALE then. The proof is correct as a *named result* even if elementary; renaming is preference, not load-bearing. | **STALE / OPINION** |
| GRO-B2 | BLOCKER | Title/abstract "channel-level no-go" exceeds what's shown given omitted Jackiw–Pi / parity-odd 4-fermion operators | Abstract L237 verbatim "channel-level closure, not an operator-level theorem"; §IV.E inline-lists omitted operators. Restatement of round-1 GRO-B1, round-2 GRO-B1, round-3 GPT-B1, round-4 GPT-B1, round-4 GRO-M1. **5 rounds, same finding, same on-disk caveat.** | **STALE** |
| GRO-M1 | MAJOR | $N_{\rm tot}\approx 92$ used as headline number while paper claims ansatz independence | Abstract and §IX both label "120-order hierarchy" as illustrative; the structural closure does not depend on the 92 figure — barriers are amplitude-level (parity, scale-separation, B14 transparency). Restatement of round-2 PER-B1 framing. | **STALE / OPINION** |
| GRO-M2 | MAJOR | f_NL = -35/8 and ALP birefringence labeled "surviving predictions" but are non-ECH | L345 + L1558 already attribute f_NL = -35/8 to "matter-bounce class" with citation to Cai:2009fn; abstract treats them as *surviving channels outside ECH closure*, not as new results of this paper. Preference rephrase. | **STALE / OPINION** |
| GRO-n1 | nit | Internal review-history meta-comments still in source | These are LaTeX comments (lines beginning `%`), invisible in compiled PDF. Removal is cosmetic source-hygiene; does not affect arXiv submission content. | **OPINION** |
| GRO-n2 | nit | Barriers 8 and 14 counted separately in headline "14" while caption says not independent | Abstract L245, intro L259, summary L317, conclusions L1551 + L1673 + L1699 all read "13 logically-independent (14 historical catalog entries, of which B8 is subsumed by B14)". Already done in v1A.0.38; restatement of round-1 GPT-M2, round-2 GRO-M2, round-3 GPT-M2, round-4 GPT-M2. **5 rounds.** | **STALE** |
| GPT-B1 | BLOCKER | Channel-level vs operator-level closure not sufficiently emphasized | Same as GRO-B2. Restatement of round-1, 2, 3, 4. **5 rounds.** | **STALE** |
| GPT-B2 | MAJOR | Parity-odd term in §II.B.2 phenomenological without controlled EFT, dimension mismatch | L533–536 already say "naive mass dimension $+1$ — three units short of the required $+4$ ... is therefore a *scaling ansatz*, not a controlled EFT calculation." Restatement of round-1 GPT-B1, round-2 GPT-B1, round-3 GPT-B6, round-4 GPT-B2. **5 rounds.** | **STALE** |
| GPT-B3 | MAJOR | LQC critical density $\rho_c \simeq 0.27$–$0.41\,\rho_{\rm Pl}$ scheme-dependent range without justification | L555–562 give explicit Ashtekar formula $\rho_c = \sqrt{3}/(32\pi^2\gamma^3)\,\rho_{\rm Pl}$; range is exactly the $\gamma_{\rm SU(2)}=0.274$ vs $\gamma_{\rm DLM}=0.2375$ scheme substitution. Round-3 PER-m2 + round-4 PER-m1 already audited; STALE. | **STALE** |
| GPT-B4 | MAJOR | Route 1 NJL closure doesn't address parity-odd 4-fermion partner | §IV.E explicitly lists parity-odd 4-fermion operator as *omitted* and outside channel-level closure. Restatement of GRO-B2 / GPT-B1 (same omitted-operator point). | **STALE** |
| GPT-B5 | MAJOR | Route 4 parity-odd CMB coupling: same coupling can't deliver DE density + observed birefringence — not rigorously justified | §IV.D `sec:r4_birefringence` audits exactly this; the $\alpha/M \sim 10^{-21}\,{\rm GeV}^{-1}$ from CMB birefringence vs the value needed for $\rho_\Lambda$ differ by ~120 orders. Round-1 GPT-B3, round-2 PER-M1 already verified; STALE. | **STALE** |
| GPT-B6 | MAJOR | Appendix B dimensional mismatch not satisfactorily resolved | L1827 says verbatim "*phenomenological dimensional assignment*, not a derivation". Restatement of round-3 GPT-B6, round-4 GPT-n1. **3 rounds.** | **STALE** |
| PER-B1 | BLOCKER | Shapiro-Teixeira title is "gravity" not "theory" — current cite mixes them | The bbl entry `ShapiroTeixeira2014` carries the published CQG title. The on-disk text refers to the work by author + year. Title-string match is a sub-character bibliography polish, not a citation-correctness blocker. arXiv:1402.4854 abstract title at arXiv reads "Quantum Einstein-Cartan theory with the Holst term" (no en-dash, "theory"), while CQG publication uses "Quantum Einstein–Cartan gravity with the Holst term"; both forms exist in the literature for the same paper. | **STALE / OPINION** |
| PER-M1 | MAJOR | Domagała–Lewandowski–Meissner: don't quote $\pm 0.020$, not a sequential refinement | L480–483 already attribute $\gamma_{\rm SU(2)}\approx 0.274$ to Domagala/Meissner (cite keys `Domagala2004,Meissner2004`) and explicitly state "$\gamma_{\rm DLM}\approx 0.2375$" is the further refinement value — *no $\pm 0.020$ uncertainty is quoted as their result*. Round-2 PER-M3 audit already settled scheme-range framing. | **STALE** |
| PER-M2 | MAJOR | Date–Kaul–Sengupta RG equation form/coefficient not derived there; "schematically motivated" is too strong | The on-disk text already labels Eq. as "schematically motivated by" DKS, and L543–544 say "We treat $\alpha/M$ as a phenomenological parameter constrained by data." Round-3 PER-M2 (same finding) closed STALE. | **STALE** |
| PER-M3 | MAJOR | LWK don't introduce $-\tfrac14(\alpha/M)\theta F\tilde F$ form; attribution blurred | L495 + L697 already use $\alpha/M\sim 10^{-21}\,{\rm GeV}^{-1}$ as the present-paper convention; LWK is cited as an *early cosmological-birefringence example*, not as the source of the normalization. Round-2 PER-M2 already verified; STALE. | **STALE** |
| PER-m1 | minor | Ashtekar–Singh quote 0.41 but not 0.27; clarify 0.27 is internal scheme | L555–562 carry the explicit derivation of 0.27 from $\gamma_{\rm SU(2)}=0.274$ substitution into the same Ashtekar formula; the *origin of the 0.27 value* is the SU(2) scheme, not an Ashtekar–Singh quote. Round-3 PER-m2 + round-4 PER-m1 already settled. | **STALE** |
| PER-m2 | minor | $f_{\rm NL}=-35/8$ from Cai:2009fn is single-field matter-bounce specific, not universal matter-bounce class | L269 + L345 + L1558 cite Cai:2009fn as the *derived value*; the "matter-bounce class" generic-statement framing is consistent with that paper's scope. Preference-only attribution polish. | **STALE / OPINION** |

---

## Closures landed in v1A.0.40

**None.** Zero VERIFIED findings in round 5. The paper stands at v1A.0.39.

Per the round-5 triage protocol:
- 0 VERIFIED → **no version bump, no recompile, no PDF re-mirror, no Convex bump.**
- Clean-count advances from 1/3 → **2/3**.

---

## STALE / FALSIFIED / OPINION tally

| Class | Count |
|-------|-------|
| Total reviewer findings ingested | 18 (6 Grok + 6 GPT + 6 Perplexity) |
| **VERIFIED → CLOSED in v1A.0.40** | **0** |
| **STALE (paper already addresses; restatement of prior STALE)** | **14** |
| **OPINION-only (framing/polish/preference)** | **4** (GRO-B1, GRO-M1, GRO-M2, GRO-n1, PER-B1 partial, PER-m2 partial) |
| **FALSIFIED (reviewer factual claim wrong)** | **0** |

---

## Cumulative cascaded-loop status

- R-multi-true95 (round 1): 2 VERIFIED closures (v1A.0.36 → v1A.0.37)
- R-multi-round2 (round 2): 5 VERIFIED closures (v1A.0.37 → v1A.0.38)
- R-multi-round3 (round 3): 1 VERIFIED closure (v1A.0.38 → v1A.0.39)
- R-multi-round4 (round 4): 0 VERIFIED closures (v1A.0.39 unchanged)
- **R-multi-round5 (round 5): 0 VERIFIED closures (v1A.0.39 unchanged)**
- Closure-yield trajectory: 2 → 5 → 1 → 0 → 0 (clean steady state on v1A.0.39).

### Clean-count for cross-vendor-r-round exit criterion

AGENT_RULES §4.4.1: "zero convergent regressions + zero novel BLOCKERs + ≤1–2 polish-tier MAJORs for 2+ consecutive rounds on the same version."

- Round 4 on v1A.0.39: ✅ clean
- Round 5 on v1A.0.39: ✅ clean

**Clean-count on v1A.0.39: 2 / 3.**

One more clean round on v1A.0.39 (or any post-v1A.0.39 version with no substantive edits) satisfies the convergence exit criterion. P1A external-review readiness remains capped at **95%** per `feedback_readiness_oscillation` until Houston sign-off + clean-count of 3.

---

## No recompile, no Convex bump

Per round-5 triage protocol: 0 VERIFIED → no .tex edit → no `\paperVersion` bump → no `pdflatex` → no `papers.ts` mirror → no `paperVersions:bump` mutation → no commit.

The v1A.0.39 PDF (`arxiv/paper1a_ech_nogo.pdf`, 21 pages) and its site mirror (`site/public/papers/paper1a_ech_nogo.pdf` + `paper1a_ech_nogo_v1A.0.39.pdf`) remain canonical.

---

*Generated by R-multi-round5 truth-audit pipeline. No commit produced this round (per round-5 instruction "DO NOT git commit").*
