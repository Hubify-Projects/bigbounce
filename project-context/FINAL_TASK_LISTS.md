# Final task lists for all 5 papers — post R23 wave

Generated 2026-05-21 after the R23 5-vendor cross-vendor wave fired in parallel on P1A v1A.0.33, P1B v1B.0.20, P2 v1.7.30, P3 v3.1.56, P4 v1.0.122.

**Aggregate R23 verdict: 24 of 25 reviewers returned 0 BLOCKER / 0 MAJOR.** The lone non-clean reviewer (Gemini-3.1-Pro on P1A) was audit-falsified on its BLOCKER (prompt-meta error, not paper content) and its MAJOR + minor + nit were closed text-level in v1A.0.34 in the same wave.

Houston standing rule for this list: **eat the frog, do the hard thing, no deferrals** — items appear here only because they are genuinely the next step, not because they are convenient.

---

## P1A — ECH Structural Closure (no-go theorem) — v1A.0.34

**Status: 90% / 99% cap · external-review-ready · cascaded-loop exit holds.**

R-round history: R15 + R16 + R23 all 0/0 across all 5 vendors on paper content (R23 Gemini BLOCKER was prompt-meta-error, falsified; M1+m1+n1 closed in v1A.0.34). 10th-consecutive Gemini-cosmology effective 0-BLOCKER on content. AGENT_RULES §4.4.1 satisfied.

| # | Task | Owner | Blocker? |
|---|------|-------|---|
| 1 | **Houston sign-off on v1A.0.34** | Houston | ✅ ONLY remaining gate |
| 2 | Build arXiv tarball (paper1a_ech_nogo.tex + references.bib + figures/ + main.bbl) | agent | autonomous |
| 3 | arXiv tarball clean-revtex smoke test (`pdflatex+bibtex+pdflatex+pdflatex` from tarball alone) | agent | autonomous |
| 4 | arXiv submission (astro-ph.CO + astro-ph.IM) | Houston | needs Houston's arXiv endorsement |

**Nothing else is open.** All prior R-rounds + truth-audits closed; PDF is 20 pp / 813 KB / 0 overfull >20pt / 0 undef refs / 0 undef cites. 4 mirrors byte-identical.

---

## P1B — MCMC Companion paper — v1B.0.20

**Status: ≈67% (SSOT lag) / 99% cap · external-review-ready per R16+R23 convergence.**

R-round history: R16 had 4-of-5 reviewers 0/0; Grok-only B1+B2 BLOCKERs FALSIFIED via stale-comment audit. R23 returned **5-of-5 reviewers 0/0** (fully clean — no findings of any class). The 67% SSOT readiness number is stale; live state is functionally equivalent to P1A's loop-exit position pending the next SSOT refresh.

| # | Task | Owner | Blocker? |
|---|------|-------|---|
| 1 | **Bump readiness number in SSOT/paper-2/status.md (P1B section) + papers.ts to reflect R23 5/5 clean** | agent | autonomous (queued this tick) |
| 2 | **Houston sign-off on v1B.0.20** | Houston | gate |
| 3 | Build arXiv tarball | agent | autonomous |
| 4 | arXiv submission | Houston | endorsement |

---

## P2 — f_NL Forecast (SPHEREx) — v1.7.30

**Status: 82% (SSOT) → likely revise upward after R23 clean · external-review-ready candidate.**

R-round history: R23 returned **5-of-5 reviewers 0/0** (DeepSeek + Gemini + GPT-5 + Grok + Perplexity all clean). This is the first all-5-clean round on P2 in the campaign. Heinrich+2023 σ(f_NL)=0.7 externalization is reviewer-accepted.

| # | Task | Owner | Blocker? |
|---|------|-------|---|
| 1 | **Bump readiness in SSOT + papers.ts to reflect R23 5/5 clean (82 → 95+ proposed)** | agent | autonomous |
| 2 | Compile a fresh PDF on the latest .tex (verify date stamp + cross-references current) | agent | autonomous |
| 3 | Site-sync paper2_fnl_forecast.pdf to all mirrors (currently 614 KB v1.7.0 on disk; .tex is at v1.7.30) | agent | autonomous |
| 4 | **Houston sign-off on v1.7.30** | Houston | gate |
| 5 | arXiv submission (astro-ph.CO) | Houston | endorsement |

---

## P3 — Multi-Survey Anomaly Catalog — v3.1.56

**Status: 86% (SSOT) → likely revise upward after R23 clean · external-review-ready candidate.**

R-round history: R16 had 4-of-5 reviewers 0/0; Grok-only BLOCKERs truth-audited (abstract states qualifier 3× at <1σ). R23 returned **5-of-5 reviewers 0/0**. v3.1.56 closed the multi-round 9,576 dedup-shortfall via union-find.

| # | Task | Owner | Blocker? |
|---|------|-------|---|
| 1 | **Bump readiness in SSOT + papers.ts to reflect R23 5/5 clean (86 → 95+ proposed)** | agent | autonomous |
| 2 | Verify all 7-survey dedup arithmetic statements (10,213 = 637 + 9,576) propagate to abstract + Table 1 + §6 | agent | autonomous |
| 3 | Compile fresh P3 PDF (current 238 KB .tex needs a clean compile + figure verification) | agent | autonomous |
| 4 | **Houston sign-off on v3.1.56** | Houston | gate |
| 5 | arXiv submission (astro-ph.CO + astro-ph.IM) | Houston | endorsement |

---

## P4 — Galaxy Chirality Catalog (8.47M / 3.2M spirals) — v1.0.122

**Status: 95% CAP · external-review-ready · R23 verification clean.**

R-round history: R22 had 3-of-5 reviewers 0/0; GPT-5 (2 BL + 4 MAJ) + Perplexity (1 BL + 3 MAJ) closed bundled in v1.0.122. **R23 verification returned 5-of-5 reviewers 0/0** — confirms no regressions from v1.0.122 closures. First 5-of-5 clean round in P4 history.

| # | Task | Owner | Blocker? |
|---|------|-------|---|
| 1 | **Houston sign-off on v1.0.122** | Houston | ✅ ONLY remaining gate |
| 2 | Push HF model card `bamfai/galaxy-chirality-v2` from v1.0.104 → v1.0.122 (HF_TOKEN in `.env.local`) | agent | autonomous (queued) |
| 3 | Build arXiv tarball (chirality_catalog_paper.tex + bib + figures/ + bbl, 26.26 MB compressed bound) | agent | autonomous |
| 4 | arXiv submission (astro-ph.GA + astro-ph.CO) | Houston | endorsement |

---

## P5 — Environmental Dependence of Spiral Chirality (DESI LSS) — bootstrap-2026-05-15

**Status: 30% · Phase 1 V-Web env_finder DONE (104s laptop, headline result landed) · scaffold paper 9 KB.**

This is the biggest lift remaining. P5 has never had an R-round and the paper is a 9 KB LaTeX scaffold. Per Houston "do the hard thing" the path is:

| # | Task | Owner | Blocker? |
|---|------|-------|---|
| 1 | Phase 2 sensitivity sweep: vary V-Web smoothing scale (10, 25, 50 Mpc/h), grid resolution (128³, 256³, 512³), eigenvalue threshold λ_th ∈ {0.0, 0.1, 0.3} | agent | autonomous |
| 2 | RSD correction: Fingers-of-God + Kaiser squashing on the spectro-z sample (replace z-space distances with reconstructed real-space distances using known DESI LSS power spectrum) | agent | autonomous |
| 3 | Tempel+2018 cross-validation: pull the Tempel+2018 SDSS group catalog where it overlaps DESI footprint, build a parallel env classification, compare to V-Web | agent | autonomous |
| 4 | Expand paper LaTeX from 9 KB scaffold to full first-draft (introduction + methods + V-Web algorithm + Phase 1 headline + Phase 2 robustness + Phase 3 Tempel cross-validation + conclusions + bibliography) — target ~30 pp | agent | autonomous |
| 5 | First P5 PDF compile (revtex4-2, mirror to 4 sites including site/public/papers/) | agent | autonomous |
| 6 | First R-round on P5 (5-vendor cross-vendor via tools/real_cross_vendor_review.py) | agent | autonomous |
| 7 | Bundled hard-fix wave closing R-round findings (whatever they are) | agent | autonomous |
| 8 | (OPTIONAL) DESI environmental VAC if Houston has access — would replace V-Web as the canonical classifier and would require a Phase 4 re-analysis | Houston | optional, falls back to V-Web if absent |
| 9 | Houston sign-off on first publishable version | Houston | gate |
| 10 | arXiv submission (astro-ph.CO + astro-ph.GA) | Houston | endorsement |

P5 is the only paper requiring NEW agent-driven work before sign-off. The other five are in the sign-off queue.

---

## Cross-cutting open items (NOT per-paper)

- Site visual sync: NEEDS HOUSTON section now at top of homepage; verify Vercel rebuild picks it up (auto-deploy from main).
- SSOT `index.md` headline + per-paper status.md percent fields are lagging current state (P1B at 67%, P2 at 82%, P3 at 86%) — proposed revisions queued in the next SSOT freshness tick.
- BackBlaze backup of the R23 review files (`project-context/peer-reviews/2026-05-21_R23_*.md`) — autonomous via existing backup cron.

## Eat-the-frog priority order

1. **Houston sign-off on P1A v1A.0.34** (the cleanest paper, the original loop-exit milestone) — biggest impact per minute of Houston attention.
2. **Houston sign-off on P4 v1.0.122** (just-landed-clean — second-cleanest paper).
3. Agent-driven SSOT freshness sweep (bump P1B/P2/P3 percentages to reflect R23 5/5 clean).
4. Agent-driven P5 Phase 2 sensitivity sweep + paper expansion (biggest remaining content task).
5. Houston sign-off on P2 / P3 / P1B after the SSOT sweep makes their state legible.
6. P5 sign-off after first PDF compile + R-round close.
7. Houston arXiv submissions in batches as sign-offs land.
