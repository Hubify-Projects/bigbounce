# SUBMIT-TODAY CHECKLIST — all 6 papers (2026-07-05)

All six papers passed a fresh full-source publication audit today (fix-verified, packets
standalone-compile-tested, three-way md5 compile==served==Convex). Every reviewer finding
is closed by real science, artifact-cited, or resolved by this coordinated plan. Houston's
clicks are the only remaining step.

## WAVE 1 — submit now, in this order (no dependencies)

| # | Paper | Bundle | Ver | pp | Notes |
|---|-------|--------|-----|----|-------|
| 1 | **P4** chirality catalog | `submissions/P4/arxiv_p4_v1.0.220.tar.gz` (25MB, tarball md5 c8748642) | v1.0.220 | 31 | astro-ph.CO, x-list GA. Metadata in `ARXIV_METADATA.txt`. v1.0.220 D-round final polish: condensed title + reader-first abstract + expanded AI-methods disclosure; presentation-only, no science number changed. **Submit FIRST — P5 needs its ID.** |
| 2 | **P1B** MCMC/NaMaster/ALP companion | `submissions/P1B/arxiv_p1b_v1B.0.102.tar.gz` | v1B.0.102 | 22 | P1A cross-ref placeholder inside; reciprocal ID insert per `SUBMISSION_NOTE.md`. v1B.0.102 D-round final polish: presentation + disclosure only, no science number changed; tarball rebuilt + standalone-verified (0 undef-refs, 22pp), stale v1B.0.101 removed. |
| 3 | **P3** anomaly catalog | `submissions/P3/arxiv_p3_v3.1.140.tar.gz` (4.07MB, tarball md5 f4404748) | v3.1.140 | 33 | Packaging-kit refreshed to the new 20-word title ("A Multi-Survey Autoencoder Anomaly Catalog: 268,519 Validated Sources from a Native-Trained Scan of 37.3 Million Spectra and Map Patches") + v3.1.140 across ARXIV_METADATA / DATA_RELEASE_MANIFEST / cover; tarball rebuilt + standalone-verified (0 undef-refs), stale v3.1.139 removed. Flip HF dataset visibility public (manual); Zenodo DOI mints at submit. DESI score-vs-z DATA-UNLOCK closed (honest MIXED result: DESI composition transfers, score-vs-z scoped to SDSS). |
| 4 | **P2** f_NL forecast + Cai/Li resolution | `submissions/P2/arxiv_p2_v1.7.98.tar.gz` (md5 894fd8bb) | v1.7.98 | 34 | Positioned as honest forecast + the −35/16 literature resolution. v1.7.98 D-round final polish: abstract restructured to lead with the −35/16 Cai-Li resolution then the forecast then the load-bearing caveat (was caveat-dense); colorblind-safe palette + consistent fonts across all figures; finished −35/8 → −35/16 label-sync in fig2/fig3/fig5 (which still showed the retracted value, contradicting their own corrected captions); AI-methods disclosure expanded; raw file-path column-overflow fixed. Presentation + disclosure only, no science number changed. pdf md5 7af1d09f. Zenodo DOI at submit. |

arXiv assigns each ID immediately on submission (announcement later; the ID is usable at once).

## WAVE 2 — same day, after wave-1 IDs exist

| # | Paper | Bundle | Ver | pp | Pre-submit step (~2 min each) |
|---|-------|--------|-----|----|------------------------------|
| 5 | **P5** DESI environmental chirality | `submissions/P5/arxiv_p5_v0.1.104.tar.gz` (md5 fc8c5eaf) | v0.1.104 | 37 | v0.1.104 POST-POLISH INT fix: 3 D-round-regenerated 300-dpi serif figures now embedded (were served stale at 150 dpi; no `\graphicspath`); presentation-only, zero numbers changed. Set `\paperIVarxiv` to P4's real ID (see `SUBMISSION_NOTE.txt`) → recompile → submit. |
| 6 | **P1A** ECH no-go | `submissions/P1A/arxiv_p1a_v1A.0.112.tar.gz` | v1A.0.112 | 37 | v1A.0.112 POSTPOLISH figure-image correction: `fig_theory_map.png` still rendered the superseded matter-bounce `f_NL=-35/8` in its prediction box while the body was uniformly `-35/16` (value baked into the PNG, invisible to text grep) — regenerated `arxiv/scripts/fig_theory_map.py` with `-35/16`, re-mirrored byte-identical to all served paths; no science number changed vs body. Tarball rebuilt from v111 file set + new tex + corrected PNG + standalone-verified (0 undef-refs, 37pp). Fill `TODO-SUBMISSION` markers in references.bib with wave-1 IDs (see `SUBMISSION_NOTE`) → recompile → rebuild tarball → submit. Then insert P1A's ID back into P1B v2 (reciprocal note). |

## Post-submit (agent-executable — say the word)
- Insert real IDs, recompile wave-2, rebuild bundles (I do this the moment you give me the IDs)
- Update P1B replacement (v2) with P1A's ID
- Site/Convex/SSOT sync with arXiv IDs + announcement links; reviewTimeline "published" entries
- Strengthening computes from the DATA agent (P3-DESI, P4-morphology, P2-CovB) fold into v2
  replacements if they land — none are blocking

## Verified state per paper (today's audit round)
- **P4**: v1.0.220 D-round polish (condensed title + reader-first abstract); Grok+Gemini MINOR, null "robustly supported"; INT ACCEPT; every number reproduces.
- **P1B**: INT MINOR/error-clean; standalone ΔN_eff contribution surfaced; false cover claims fixed.
- **P3**: INT ACCEPT (byte-identical reproduction); anomalies proven real high-z QSOs (p~1e-103).
- **P2**: v1.7.98 D-round polish — abstract leads with −35/16 Cai-Li resolution; colorblind figures + fig2/3/5 label-sync (−35/8→−35/16); AI-methods expanded; path-overflow fixed. −35/16 3-way certified; Grok MINOR.
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
