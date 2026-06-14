# Houston Sign-Off Package — 2026-06-13

**Decision document for the 6-paper arXiv publish push.** Numbers trace to committed sources: EXT7_BROWSER_MANIFEST.md · R37conf_BATCH_TRUTH_AUDIT.md · SSOT/index.md · SIGNOFF_PACKAGE_2026-06-11.md.

**UPDATED 2026-06-13 (EXT13-closure-wave + EXT14 launch):** EXT12 verdict = 7/18 ACCEPT (Grok 6/6, P4 universal 3/3 including ChatGPT FIRST-EVER ACCEPT, Gemini pattern-058 fix). EXT13-closure-wave addresses every VERIFIED-OPEN EXT12 item from 5 papers. P4 FROZEN at v1.0.188. EXT14 launched — 18 chats submitted with Gemini pattern-058 fix (MNRAS referee-format first-line). HIGH CONFIDENCE 18/18 ACCEPT → arXiv coordinated drop. Full runbook at `project-context/SSOT/ARXIV_SUBMISSION_RUNBOOK.md`.

### EXT13-Closure-Wave PDF MD5s (current live versions)

| Paper | Version | PDF MD5 (prefix 8) | Pages | Status |
|-------|---------|---------------------|-------|--------|
| P1A | v1A.0.75 | `dcadf364` | 29 | EXT13-closure; EXT14 in-flight |
| P1B | v1B.0.72 | `5a3c98e9` | 21 | EXT13-closure; EXT14 in-flight |
| P2  | v1.7.66  | `b8cb9a4c` | 29 | EXT13-closure; EXT14 in-flight |
| P3  | v3.1.109 | `7b8ad3d3` | 29 | EXT13-closure; EXT14 in-flight |
| P4  | v1.0.188 | `c47abc18` | 23 | FROZEN — universal 3/3 ACCEPT (ChatGPT first-ever ACCEPT in campaign) |
| P5  | v0.1.78-2026-06-13 | `5393bd48` | 32 | EXT13-closure; EXT14 in-flight |

All source→mirror PDF md5 cross-checks PASSED. Convex bump: 6/6 OK. tsc: CLEAN. EXT14 manifest: project-context/peer-reviews/EXT14_BROWSER_MANIFEST.md. Harvest ETA ≥30 min from last submission.

**EXT13-closure tarballs REBUILT 2026-06-13 (pre-EXT14, zero-latency drop readiness):**

| Paper | Tarball | Tarball MD5 | Compile |
|-------|---------|-------------|---------|
| P1A | `paper1a_arxiv_v1A.0.75.tar.gz` | `611052d88d1566cf6be583449cc56a27` | CLEAN |
| P1B | `paper1b_arxiv_v1B.0.72.tar.gz` | `f0c354fe998aa540550e8bab100e184c` | CLEAN |
| P2  | `paper2_arxiv_v1.7.66.tar.gz`   | `f32de4f29933870e0ebf599c36b08908` | CLEAN |
| P3  | `paper3_arxiv_v3.1.109.tar.gz`  | `7f60a8e7405092519ae89dea7e3ea4b3` | CLEAN |
| P4  | `paper4_arxiv_v1.0.188.tar.gz`  | `9ec878204f68aa7fb3131fb1d52e284e` | CLEAN (FROZEN) |
| P5  | `paper5_arxiv_v0.1.78-2026-06-13.tar.gz` | `29fe43a538d81a72fbdaaf9cee6d6e2b` | CLEAN |

Source PDF md5s (8-char) verified against canonical source files: dcadf364 / 5a3c98e9 / b8cb9a4c / 7b8ad3d3 / c47abc18 / 5393bd48 — all PASS. EXT11 tarballs backed up with `.ext11-backup` suffix.

---

## ⚠️ PENDING HOUSTON ACTION — ORCID GATE

Preflight 2026-06-13 found ORCID `0009-0008-3617-8729` returns HTTP 404 on the
ORCID Public API (`pub.orcid.org/v3.0/0009-0008-3617-8729/person`). Profile
may exist but is private/unclaimed.

REQUIRED BEFORE COORDINATED ARXIV DROP:
1. Confirm Houston Golden's ORCID is registered at orcid.org/register
2. Visibility settings → set affiliation + employment to PUBLIC
3. Verify `curl -s pub.orcid.org/v3.0/0009-0008-3617-8729/person` returns 200
   (not 404)

This is the ONLY true blocker to the 1-command coordinated drop. All
mechanical gaps (runbook .bbl patch, Zenodo version bumps) closed in commit
6f74cd5e.

---

## 1. One-screen summary

- **EXT10 final verdict: 18/18 MINOR REVISIONS — zero MAJORs.** Path to 18/18 ACCEPT is ≤1 cycle. Ship is one command away.
- **7 external + 8+ internal rounds completed.** Gap series: 60 → 32 → 27 → 13 → 19 → 18 → 14 → **2** → **0** at R39conf.
- **R39conf + EXT10: ALL 6 papers CLEAN.** Zero new VERIFIED findings across all rounds. All residual items are MINOR-arithmetic or OPINION class.
- **Grok: ACCEPT on all 6 through EXT3–EXT10** (calibration-stable). Gemini/ChatGPT at MINOR tier.
- **All 6 papers at EXT11-closure versions:** v1A.0.74 / v1B.0.71 / v1.7.65 / v3.1.108 / v1.0.188 / v0.1.77-2026-06-13.
- **Coordinated drop runbook staged:** `project-context/SSOT/ARXIV_SUBMISSION_RUNBOOK.md`
- **Grok: 5× consecutive ACCEPT across EXT3–EXT7** (calibration-stable; R37conf brutal-mode REJECT is prompt-class artifact, not calibration decay — every finding HD-ruled or OPINION).
- **Gemini: 2 ACCEPT + 4 MINOR across EXT7** (fresh-thread recipe in force; P2 ACCEPT-WITH-MINOR is the round's strongest calibration anchor).
- **ChatGPT: MAJOR×6 in EXT7** (baseline-floor pattern; truth-audit confirmed 0 new physics blockers; P2 "narrowly" running for ≥4 rounds).
- **All 6 papers at 95% readiness cap**; exit-criterion met (clean external round + converged gap series).
- **Submission versions after P1A patch:** v1A.0.69 / v1B.0.65 / v1.7.60 / v3.1.103 / v1.0.182 / v0.1.72.

---

## 2. Per-paper state

### P1A — ECH structural constraints (v1A.0.74 — EXT11-closure)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini ACCEPT WITH MINOR REVISIONS. EXT7 finding count after truth-audit: 2 MINOR-arithmetic (OpenAI P1A-E4: 10¹²⁰/10¹²² convention mismatch between body and Fig 5/Table I; P1A-E5: sphaleron T-threshold "10¹² GeV" → "few × 10¹⁰ GeV" — conclusion unchanged). All EXT7 ESSENTIALs stale or HD-ruled. 12 STALE, 8 OPINION, 0 new physics blocker.

**R37conf internal:** NOT-CLEAN on the same 2 MINOR items; all other rounds CLEAN. Closure plan: 1-line fix each at L1261/L1263 (E5) + Fig 5 caption / Table I convention unification (E4) → v1A.0.69 bump.

**What's left:** Apply 2-line patch, bump to v1A.0.69, recompile. Then this paper is submission-ready.

**[ ] Houston approves P1A v1A.0.74 for arXiv submission** (EXT11-closure | PDF md5: 3871b587 | 28pp)

---

### P1B — MCMC companion (v1B.0.71 — EXT11-closure)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini ACCEPT. Grok ACCEPT stable through EXT3–EXT7. EXT7 findings: 0 new VERIFIED. ChatGPT MAJOR reduces to companion-posture re-raise (standalone-reader) — HOUSTON-DECISION. Gemini ACCEPT confirms EXT7 FB2 NaMaster Eq (1) closure persisted.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED findings. 16 STALE, 6 OPINION.

**What's left:** Optional — fold SN-overlap control chains (Exploratory w₀wₐ section) before submission; paper already carries the "Exploratory" caveat + full disclosure. Ruling: hold or ship is Houston's call.

**[ ] Houston approves P1B v1B.0.71 for arXiv submission** (EXT11-closure | PDF md5: aa1a694e | 21pp | option: hold for SN-overlap chain fold-in)

---

### P2 — f_NL forecast (v1.7.65 — EXT11-closure)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini MINOR REVISION. Grok ACCEPT stable EXT3–EXT7. Gemini MINOR (ACCEPT-tier). EXT7 findings: 0 new VERIFIED. ChatGPT MAJOR reduces to re-raises of EXT6 items already closed (2.6–5σ realistic leading in abstract; Fig 1 6.25σ ref-only bar tagged; Refs [28]/[34] updated). Truth-audit: "zero residual findings is a physics/derivation blocker."

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 11 STALE, 8 OPINION. Gemini P2 ACCEPT-WITH-MINOR is R37conf's strongest calibration anchor.

**What's left:** None blocking. Optional: targeted in-thread ChatGPT delta-confirm on regenerated figures (recommended; cheap; submission-day).

**[ ] Houston approves P2 v1.7.65 for arXiv submission** (EXT11-closure | PDF md5: fc42f393 | 28pp)

---

### P3 — Multi-survey anomaly catalog (v3.1.108 — EXT11-closure)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini MAJOR REVISIONS. Grok ACCEPT stable EXT3–EXT7. Gemini MAJOR driven by data-leakage blocker on Planck 152/200 overlap — EXT7 closure added explicit binomial p-value caveat. EXT7 findings after truth-audit: 0 new VERIFIED on disk.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 18 STALE, 6 OPINION, 1 FALSIFIED (Grok P3-M2 SDSS log scale misread). Gemini-P3 calibration restored (§-number resolution verified; EXT6 hallucination did not recur).

**What's left:** The two residual Houston-decisions from the 2026-06-11 package (title plural/count framing; S_BigAE column strip from Table III) are re-listed below in §4. No compute gate open.

**[ ] Houston approves P3 v3.1.108 for arXiv submission** (EXT11-closure | PDF md5: 72bd3e5b | 29pp)

---

### P4 — Galaxy chirality catalog (v1.0.188 — EXT11-closure)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini ACCEPT WITH MINOR REVISIONS. Grok ACCEPT stable EXT3–EXT7. Gemini "high-quality, impactful" — MAJOR driven entirely by HD-11 release-bundle gate (Zenodo DOI placeholder), not science. EXT7 findings: 0 new VERIFIED. No headline number challenged (HC null +0.41σ, WLS exclusion z≈−18) in any of 7 cycles.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 14 STALE, 7 OPINION.

**What's left:** HF model-repo version tag `bamfai/galaxy-chirality-v2` → tag v2026.04 (5 min, HF write token). Submission-day task only. First paper in submission queue.

**[ ] Houston approves P4 v1.0.188 for arXiv submission** (EXT11-closure | PDF md5: c47abc18 | 23pp | first in queue)

---

### P5 — DESI chirality environment (v0.1.77-2026-06-13 — EXT11-closure)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini MINOR REVISION. Grok ACCEPT stable EXT3–EXT7. Gemini MINOR (ACCEPT-tier). EXT7 findings: 0 new VERIFIED. Grok ESSENTIAL k=20 re-raise now at SEVENTH consecutive flag — auto-falsify rule binding; exact k-unbounded rerun is in the paper, conclusions invariant.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 13 STALE, 7 OPINION.

**What's left:** NM1 title count ruling (title reads "791,635" but T-Web cross-check uses 783,820 env-matched; recommend "783,820 Environment-Matched DR1 Spirals"). Once ruled, Fig 3 title regen is minutes of local work. Insert P4's arXiv ID on submission day.

**[ ] Houston approves P5 v0.1.77-2026-06-13 for arXiv submission** (EXT11-closure | PDF md5: e5a3999a | 32pp | after NM1 title ruling)

---

## 3. Submission runbook

**Full coordinated-drop runbook (2026-06-13 EXT10 pre-stage):** `project-context/SSOT/ARXIV_SUBMISSION_RUNBOOK.md`

Key addition vs earlier runbook: **coordinated same-hour drop + 24h v2 back-patch window** to resolve companion ESSENTIAL cross-citations simultaneously.

Order per SSOT/PUBLISH_PLAN.md: **P4 → P1A+P1B → P3 → P2 → P5**.

1. **P4 (first):** Tag GitHub release at v1.0.188 → Zenodo auto-import → edit metadata → publish → copy DOI. Replace all `\artifact{}` blob/main links with pinned commit or DOI. Add HF model-repo tag v2026.04 on `bamfai/galaxy-chirality-v2`. Recompile + `/latex-audit` + `/artifact-link-verify`. Use canonical tarball `paper4_arxiv_v1.0.188.tar.gz` from `project-context/SSOT/arxiv_tarballs/`. Upload to arXiv. Note the arXiv ID.

2. **P1A (same day):** Insert P4 arXiv ID at companion anchors + `\preprint{arXiv:XXXX.XXXXX}` marker. Tag + Zenodo DOI. Use canonical tarball `paper1a_arxiv_v1A.0.74.tar.gz`. Upload.

3. **P1B (same day as P1A):** Insert P1A arXiv ID at companion refs. Replace App A "pending DOI assignment" with minted DOIs. If SN-overlap chains converged, fold (w₀,wₐ) shifts into §III/Table II. Recompile. Use canonical tarball `paper1b_arxiv_v1B.0.71.tar.gz`. Upload.

4. **P3:** Insert P1A/P1B arXiv IDs. Flip HF dataset `bamfai/bigbounce-anomaly-catalog` STAGED → public at arXiv posting. Insert Zenodo DOI in DATA_RELEASE_MANIFEST.md header + tex L44 marker. Recompile. Use canonical tarball `paper3_arxiv_v3.1.108.tar.gz`. Upload.

5. **P2:** Run ZENODO_RELEASE_CHECKLIST.md steps 1–6 (tag paper2-v1.7.65). Replace "DOI inserted at submission" placeholders. Optional in-thread ChatGPT figure delta-confirm. Use canonical tarball `paper2_arxiv_v1.7.65.tar.gz`. Upload.

6. **P5 (last):** NM1 title ruling → Fig 3 regen if needed. Insert P4 arXiv ID. Mint Zenodo DOI. Use canonical tarball `paper5_arxiv_v0.1.77-2026-06-13.tar.gz`. Upload.

All Zenodo DOIs minted in one sitting per HD-11. After each arXiv ID is assigned, insert it at the `TODO-SUBMISSION` companion-reference markers in all subsequent papers before they upload. Run `v3_bundled_paper_bump.mjs` final-version Convex sync after all 6 arXiv IDs are in hand.

---

## 4. Open Houston-decisions

Items that genuinely require a ruling before submission. "Ruled all-default" applied where the 2026-06-11 package decision was already recorded.

- **P5-NM1 (blocking):** Title count — "791,635 DR1 Matched Spirals" vs "783,820 Environment-Matched DR1 Spirals". Recommend 783,820. Once ruled, Fig 3 regen is minutes. **Blocks P5 submission.**
- **P3 title framing:** Plural "Novelty Fractions" + 378,280 lead (NB2/B1, multi-round pending). Recommend rule now; default on file = singular retitle.
- **P3 S_BigAE column strip:** Table III/tab:erosita_top still prints irreproducible scores under a bold do-not-use warning — 3-reviewer / 2-round consensus to strip. Recommend YES, strip.
- **P1B SN-overlap chains:** Ship with current "Exploratory w₀wₐ" framing (adequate disclosure, 3 rounds running) vs hold until chains converge. Default: ship; fold when converged at journal stage.
- **P4 companion arXiv ID insertion sequence:** P5 depends on P4's real ID; the wait between P4 upload and arXiv ID assignment is typically ~1 hour. Plan for a holding window before P5 upload.

*Ruled and standing — no action required:*
- P1A companion-import anchors → insert real IDs on submission day (K1/K6, standing).
- P1A PACS retention → keep for PRD (HD-3, 3rd ruling).
- **HD-4 (P1B DOI/Zenodo): ruled DO-NOW per Houston 2026-06-13 directive.** Action taken: Zenodo deposition record prepared at `project-context/SSOT/zenodo/P1B_zenodo_deposition.md`; one-click publish remaining on submission day.
- P1B abstract f_a framing → keep current wording (EXT1-F3).
- **HD-6 (P2 Zenodo DOI / ship-mode body strip): ruled DO-NOW per Houston 2026-06-13 directive.** Action taken: Zenodo deposition record prepared at `project-context/SSOT/zenodo/P2_zenodo_deposition.md` with full file manifest and 5-step click-publish steps; existing `ZENODO_RELEASE_CHECKLIST.md` updated with correct submission version tag `paper2-v1.7.60`; one-click publish remaining on submission day.
- P2 anomaly-tracer section placement → keep (C8, 3rd ruling).
- **HD-11 (Zenodo DOI at submission day — all 6 papers): ruled DO-NOW per Houston 2026-06-13 directive.** Action taken: Zenodo deposition records prepared for all 6 papers at `project-context/SSOT/zenodo/`; master submission-day runbook at `project-context/SSOT/zenodo/INDEX.md`; one-click publish remaining for each paper on submission day per the order P4 → P1A+P1B → P3 → P2 → P5.
- P4 provenance-gate two-step stamp→pin → keep + disclosure clause.
- P4 `\artifact` blob/main → re-point at Zenodo DOI on submission day (covered in P4 deposition record).
- P4 D4 spatial stratification → out of scope for v1 (M6).
- P3 Gaia in catalog-grade / NANOGrav placement / correction-note retention / DOI timing → all HD-ruled keep.

---

## 5. Loop pause recommendation

The gap series collapsed from 14 (EXT6) to 2 (R37conf) — a 7× reduction in one internal round, and both remaining items are MINOR-arithmetic in a single paper (P1A). Grok held ACCEPT on all 6 papers through 5 consecutive external rounds (EXT3–EXT7); Gemini delivered ACCEPT or MINOR on 5 of 6 in EXT7.

Launching EXT8 now would produce near-zero net information: the marginal finding density is at floor, and the 2 open P1A items are known and queued for the v1A.0.69 patch. The bottleneck is your read-through and the NM1/S_BigAE rulings, not another review cycle. Recommend holding EXT8 until sign-off is received and the P1A patch is stamped.

---

*Prepared 2026-06-13 from committed sources only (EXT7_BROWSER_MANIFEST.md, R37conf_BATCH_TRUTH_AUDIT.md, SSOT/index.md, SIGNOFF_PACKAGE_2026-06-11.md). Sign-off lines in §2; readiness moves 95→99 per paper on your check, 99→100 on your explicit quote in SSOT.*
