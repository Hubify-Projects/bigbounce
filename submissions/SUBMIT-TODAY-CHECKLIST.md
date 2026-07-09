# SUBMIT-TODAY CHECKLIST — all 6 papers (2026-07-05)

All six papers passed a fresh full-source publication audit today (fix-verified, packets
standalone-compile-tested, three-way md5 compile==served==Convex). Every reviewer finding
is closed by real science, artifact-cited, or resolved by this coordinated plan. Houston's
clicks are the only remaining step.

## WAVE 1 — submit now, in this order (no dependencies)

| # | Paper | Bundle | Ver | pp | Notes |
|---|-------|--------|-----|----|-------|
| 1 | **P4** chirality catalog | `submissions/P4/arxiv_p4_v1.0.221.tar.gz` | v1.0.221 | 31 | astro-ph.CO, x-list GA. Metadata in `ARXIV_METADATA.txt`. v1.0.221 venue-compliance disclosure edit: AI-methods now names models (Anthropic Claude Opus 4 2026 + OpenAI GPT-5/o3 + xAI Grok-4 + Google Gemini 2.5); presentation-only, no science number changed; recompile 0 undef, mirrored byte-identical, bundle rebuilt+standalone-verified. **Submit FIRST — P5 needs its ID.** |
| 2 | **P1B** MCMC/NaMaster/ALP companion | `submissions/P1B/arxiv_p1b_v1B.0.103.tar.gz` | v1B.0.103 | 22 | P1A cross-ref placeholder inside; reciprocal ID insert per `SUBMISSION_NOTE.md`. v1B.0.103 D-round final polish: presentation + disclosure only, no science number changed; tarball rebuilt + standalone-verified (0 undef-refs, 22pp), stale v1B.0.101 removed. |
| 3 | **P3** anomaly catalog | `submissions/P3/arxiv_p3_v3.1.142.tar.gz` | v3.1.142 | 33 | Title: "A Multi-Survey Autoencoder Anomaly Catalog: 268,519 Validated Sources from a Native-Trained Scan of 37.3 Million Spectra and Map Patches". v3.1.142 venue-compliance disclosure edit (Edit A): added explicit author-responsibility + not-an-author clause AND model naming per AAS/IOP — closes the P3 responsibility-clause gap; no science number changed; tarball rebuilt + standalone-verified (0 undef-refs). Flip HF dataset visibility public (manual); Zenodo DOI mints at submit. DESI score-vs-z DATA-UNLOCK closed (honest MIXED result: DESI composition transfers, score-vs-z scoped to SDSS). |
| 4 | **P2** f_NL forecast + Cai/Li resolution | `submissions/P2/arxiv_p2_v1.7.99.tar.gz` (md5 b081ce65) | v1.7.99 | 34 | Positioned as honest forecast + the −35/16 literature resolution. v1.7.99 venue-compliance disclosure edit: AI-methods now names models (Anthropic Claude Opus 4 2026 + OpenAI GPT-5/o3 + xAI Grok-4 + Google Gemini 2.5) per IOP/JCAP. No science number changed. Recompile 0 undef, mirrored byte-identical, bundle rebuilt+standalone-verified. Zenodo DOI at submit. |

arXiv assigns each ID immediately on submission (announcement later; the ID is usable at once).

## WAVE 2 — same day, after wave-1 IDs exist

| # | Paper | Bundle | Ver | pp | Pre-submit step (~2 min each) |
|---|-------|--------|-----|----|------------------------------|
| 5 | **P5** DESI environmental chirality | `submissions/P5/arxiv_p5_v0.1.105.tar.gz` | v0.1.105 | 37 | v0.1.105 venue-compliance disclosure edit (Edit B): added explicit author-responsibility + not-an-author clause AND model naming per MNRAS/APS — closes the P5 responsibility-clause gap; presentation-only, zero numbers changed; tarball rebuilt + standalone-verified. Set `\paperIVarxiv` to P4's real ID (see `SUBMISSION_NOTE.txt`) → recompile → submit. |
| 6 | **P1A** ECH no-go | `submissions/P1A/arxiv_p1a_v1A.0.113.tar.gz` | v1A.0.113 | 37 | v1A.0.113 venue-compliance disclosure edit (Edit C, VENUE_POLICY_COMPLIANCE.md): AI-methods disclosure now names models used (Anthropic Claude Opus 4 family 2026, with OpenAI GPT-5/o3, xAI Grok-4, Google Gemini 2.5 as cross-check/internal-review) per IOP/JCAP model+version requirement. No science number changed. Recompile 0 undef-refs, mirrored byte-identical to all served paths, bundle rebuilt+standalone-verified (37pp). Fill `TODO-SUBMISSION` markers in references.bib with wave-1 IDs (see `SUBMISSION_NOTE`) → recompile → rebuild tarball → submit. Then insert P1A's ID back into P1B v2 (reciprocal note). |

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
- **P2**: v1.7.99 venue-compliance disclosure (AI-methods names models per IOP/JCAP); built on v1.7.98 D-round polish. −35/16 3-way certified; Grok MINOR.
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

---

## Wave-2 arXiv-ID insertion — one command (`tools/insert_arxiv_ids.sh`)

Once wave-1 IDs (P4, P1B, P3, P2) are assigned, run **one** command to do every
wave-2 ID insertion, recompile, mirror, bundle-rebuild, and Convex-command
emission with all gates enforced:

```
tools/insert_arxiv_ids.sh --p4 2507.NNNNN --p1b 2507.NNNNN --p3 2507.NNNNN --p2 2507.NNNNN [--dry-run]
```

The four IDs are the **wave-1** IDs (already assigned when this runs). What it does:

1. **P5** (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`): sets the
   single `\paperIVarxiv` macro to the real **P4** ID (per `submissions/P5/SUBMISSION_NOTE.txt`).
   Every Paper-IV reference resolves through that one macro.
2. **P1A** (`arxiv/paper1a_ech_nogo.tex` via shared `arxiv/references.bib`): fills the
   four `TODO-SUBMISSION` companion bib notes — `Golden2026P1b→P1B`, `Golden2026P2→P2`,
   `Golden2026P3→P3`, `Golden2026P4→P4` — then **regenerates the `.bbl`** (bibtex) so the
   IDs render in the PDF bibliography. P1A's own forward-ref (`Golden2026P1a`,
   `[arXiv:XXXX.XXXXX]`) is **left intact** — P1A's ID doesn't exist yet.
3. **P1B reciprocal**: writes `submissions/P1B/P1B_V2_NOTE.md` staging (NOT applying)
   the P1A-ID insertion for the P1B **v2** replacement — P1B submits before P1A's ID exists.
   P1B source is never edited by this script.
4. For each touched paper (**P5, P1A**): recompile (**0-undef gate**), bump patch
   version + timestamp/date, mirror the PDF byte-identical to all served paths
   (`public/papers/` versioned+alias, `site/public/papers/`, source dir),
   rebuild + **standalone-verify** the arXiv bundle, print the **Convex `paperVersions:bump`**
   command (real md5/pages), and stamp the checklist. **Fails loudly on any gate.**
5. **`--dry-run`**: does all of the above in a `/tmp` copy, verifies every gate, and
   **touches nothing in the repo**. Verified green with placeholder IDs 2507.00001–00004
   (P5 + P1A both recompile clean 37pp, both bundles standalone-verify, IDs render in PDF).

TeX PATH the script sets itself: `$HOME/Library/TinyTeX/bin/universal-darwin:/opt/homebrew/bin`.

**Submission-day sequence:**
1. Submit wave-1 (P4 first, then P1B, P3, P2) → collect the four assigned IDs.
2. `tools/insert_arxiv_ids.sh --p4 … --p1b … --p3 … --p2 …` (drop `--dry-run`).
3. Run the two printed Convex bump commands; submit P5 + P1A (new bundles); commit.
4. When P1A's ID is assigned, apply `submissions/P1B/P1B_V2_NOTE.md` for the P1B v2 replacement.


## ⚠ WAVE RE-PLAN (2026-07-08, post-merge — supersedes the tables above)
P1B is MERGED into the unified Paper 1 (v1U.0.1, 58pp, bundle `submissions/P1A/arxiv_p1_unified_v1U.0.1.tar.gz`) — no standalone P1B submission.
**Wave 1:** P4 v1.0.224 → P3 v3.1.145 → P2 v1.7.104. **Wave 2 (same day, wave-1 IDs inserted):** P5 v0.1.107 (P4 ID) → Paper 1 unified v1U.0.1 (P2/P3/P4/P5 IDs). `tools/insert_arxiv_ids.sh` targets the OLD two-paper layout for P1A/P1B cross-refs — for the unified paper, insert companion IDs directly in `arxiv/paper1_unified.tex` (grep `arXiv:XXXX` / TODO-SUBMISSION) and recompile.
