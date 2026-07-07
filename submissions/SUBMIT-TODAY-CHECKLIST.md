# SUBMIT-TODAY CHECKLIST — all 6 papers (2026-07-05)

All six papers passed a fresh full-source publication audit today (fix-verified, packets
standalone-compile-tested, three-way md5 compile==served==Convex). Every reviewer finding
is closed by real science, artifact-cited, or resolved by this coordinated plan. Houston's
clicks are the only remaining step.

## WAVE 1 — submit now, in this order (no dependencies)

| # | Paper | Bundle | Ver | pp | Notes |
|---|-------|--------|-----|----|-------|
| 1 | **P4** chirality catalog | `submissions/P4/arxiv_p4_v1.0.218.tar.gz` (26.7MB, md5 d3039085) | v1.0.218 | 31 | astro-ph.CO, x-list GA. Metadata in `ARXIV_METADATA.txt`. v1.0.218 DATA-UNLOCK: edge-on-isolated tie-break now measured — spatially isotropic (joint p=0.49, N=295,170), closes Gemini App E. **Submit FIRST — P5 needs its ID.** |
| 2 | **P1B** MCMC/NaMaster/ALP companion | `submissions/P1B/arxiv_p1b_v1B.0.101.tar.gz` | v1B.0.101 | 22 | P1A cross-ref placeholder inside; reciprocal ID insert per `SUBMISSION_NOTE.md`. |
| 3 | **P3** anomaly catalog | `submissions/P3/arxiv_p3_v3.1.139.tar.gz` (4.07MB) | v3.1.139 | 34 | Flip HF dataset visibility public (manual); Zenodo DOI mints at submit. DESI score-vs-z DATA-UNLOCK closed (honest MIXED result: DESI composition transfers, score-vs-z scoped to SDSS). |
| 4 | **P2** f_NL forecast + Cai/Li resolution | `submissions/P2/arxiv_p2_v1.7.97.tar.gz` (md5 f244b52e) | v1.7.97 | 34 | Positioned as honest forecast + the −35/16 literature resolution. v1.7.97 FIGURE HYGIENE: regenerated fig1 (shape function) + fig4 (decision thresholds), which still rendered the stale −35/8-era labeling while every text/table headline already carried −35/16 — fig1 curve now converges to −35/16 = −2.1875 (benchmarks match tab:benchmarks), fig4 prediction line + error bars at −35/16 in the "strongly favors bounce" zone. Cosmetic label-sync, no number invented. pdf md5 ca8e376d. Zenodo DOI at submit. |

arXiv assigns each ID immediately on submission (announcement later; the ID is usable at once).

## WAVE 2 — same day, after wave-1 IDs exist

| # | Paper | Bundle | Ver | pp | Pre-submit step (~2 min each) |
|---|-------|--------|-----|----|------------------------------|
| 5 | **P5** DESI environmental chirality | `submissions/P5/arxiv_p5_v0.1.102.tar.gz` | v0.1.102 | 37 | Set `\paperIVarxiv` to P4's real ID (see `SUBMISSION_NOTE.txt`) → recompile → submit. |
| 6 | **P1A** ECH no-go | `submissions/P1A/` bundle v1A.0.110 | v1A.0.110 | 39 | Fill `TODO-SUBMISSION` markers with wave-1 IDs (see `SUBMISSION_NOTE`) → recompile → submit. Then insert P1A's ID back into P1B v2 (reciprocal note). |

## Post-submit (agent-executable — say the word)
- Insert real IDs, recompile wave-2, rebuild bundles (I do this the moment you give me the IDs)
- Update P1B replacement (v2) with P1A's ID
- Site/Convex/SSOT sync with arXiv IDs + announcement links; reviewTimeline "published" entries
- Strengthening computes from the DATA agent (P3-DESI, P4-morphology, P2-CovB) fold into v2
  replacements if they land — none are blocking

## Verified state per paper (today's audit round)
- **P4**: Grok+Gemini MINOR, null "robustly supported"; INT ACCEPT; every number reproduces.
- **P1B**: INT MINOR/error-clean; standalone ΔN_eff contribution surfaced; false cover claims fixed.
- **P3**: INT ACCEPT (byte-identical reproduction); anomalies proven real high-z QSOs (p~1e-103).
- **P2**: −35/16 3-way certified; stale −35/8-era σ swept (incl. a regenerated figure); Grok MINOR.
- **P5**: all numbers exact; Δf_CW monopole-invariant on public data; Paper-IV = citation timing.
- **P1A**: all tiers derived/grounded/NDA-bounded; f_NL −35/16 propagated (20 sites);
  companion numbers artifact-cited; 0 genuinely-new Grok/Gemini findings.

ChatGPT's blanket REJECTs are its structural harsh-referee floor (directive H) — record-only,
each remaining item truth-audited as re-flag/disclosed. The operative calibrated gate
(Grok+Gemini + INT + verified science) is satisfied to the honest convergence floor on all six.

## Journal targets after arXiv (orchestrator judgment, 2026-07-05 — see FINAL_SIGNOFF_AUDIT)

| Paper | Primary target | Positioning | Expected referee friction |
|---|---|---|---|
| P4 | PRD (or MNRAS) | Null-result + catalog, pre-specified, model-free confirmation | Low — strongest paper |
| P3 | ApJS / AJ | Catalog + methods data-release (right venue for tiered validation) | Low at the right venue |
| P2 | PRD / JCAP | LEAD with the −35/16 Cai–Li resolution; forecast as secondary | Moderate — forecast scope |
| P5 | MNRAS / PRD | Environmental null on public data (post P4 ID) | Low-moderate |
| P1A | JCAP / PRD | Channel-level no-go + NDA argument, scope explicit | Expect a real scope exchange — normal refereeing |
| P1B | arXiv companion (or pair with P1A; alt: methods venue) | Reproducibility + derived ΔN_eff bound | Venue-dependent |

ChatGPT's blanket REJECTs are dispositioned in FINAL_SIGNOFF_AUDIT_2026-07-05.md (0 genuinely-new
real findings); read them as a preview of the toughest human referee's *scope* questions, answered
in referee exchanges with the verified artifact record.
