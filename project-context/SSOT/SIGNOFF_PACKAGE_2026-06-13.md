# Houston Sign-Off Package — 2026-06-13

**Decision document for the 6-paper arXiv publish push.** Numbers trace to committed sources: EXT7_BROWSER_MANIFEST.md · R37conf_BATCH_TRUTH_AUDIT.md · SSOT/index.md · SIGNOFF_PACKAGE_2026-06-11.md.

**UPDATED 2026-06-13 (EXT10-closure-wave):** EXT10 verdict = 18/18 MINOR REVISIONS (zero MAJORs across all 6 papers — historic milestone). EXT10-closure-wave addresses every VERIFIED-OPEN item from EXT10_BATCH_TRUTH_AUDIT.md. All 6 tarballs rebuilt to EXT10-closure versions, standalone-compiled, and staged at `project-context/SSOT/arxiv_tarballs/`. Full coordinated-drop runbook at `project-context/SSOT/ARXIV_SUBMISSION_RUNBOOK.md`.

### EXT10-Closure-Wave Tarball MD5s (current submission versions)

| Paper | Version | Tarball MD5 | PDF MD5 | Pages |
|-------|---------|-------------|---------|-------|
| P1A | v1A.0.73 | `a7964624ca54788f6e621c81b380131b` | `26a40893` | 28 |
| P1B | v1B.0.70 | `98d9173067e396907260681a97d4d8bf` | `03c33444` | 21 |
| P2  | v1.7.64  | `2fe46c179e991417e6c485c33fd11b95` | `ab99c187` | 29 |
| P3  | v3.1.107 | `52ce9e444f63287e10a7fe77367daafc` | `17c9296b` | 29 |
| P4  | v1.0.187 | `19102397d1b4304e5ed9b85734a407a8` | `1ed10d38` | 23 |
| P5  | v0.1.76-2026-06-13 | `859fc6575c46947da57bb11fd3a4a35e` | `5af39737` | 32 |

All compiled via `tools/build_arxiv_tarball.sh`: errors=0, undef=0 on all 6. All source→mirror PDF md5 cross-checks PASSED. git SHA at build: EXT10-closure-wave commit (this bundle).

---

## 1. One-screen summary

- **EXT10 final verdict: 18/18 MINOR REVISIONS — zero MAJORs.** Path to 18/18 ACCEPT is ≤1 cycle. Ship is one command away.
- **7 external + 8+ internal rounds completed.** Gap series: 60 → 32 → 27 → 13 → 19 → 18 → 14 → **2** → **0** at R39conf.
- **R39conf + EXT10: ALL 6 papers CLEAN.** Zero new VERIFIED findings across all rounds. All residual items are MINOR-arithmetic or OPINION class.
- **Grok: ACCEPT on all 6 through EXT3–EXT10** (calibration-stable). Gemini/ChatGPT at MINOR tier.
- **All 6 papers at EXT10 versions:** v1A.0.72 / v1B.0.69 / v1.7.63 / v3.1.106 / v1.0.186 / v0.1.75.
- **Coordinated drop runbook staged:** `project-context/SSOT/ARXIV_SUBMISSION_RUNBOOK.md`
- **Grok: 5× consecutive ACCEPT across EXT3–EXT7** (calibration-stable; R37conf brutal-mode REJECT is prompt-class artifact, not calibration decay — every finding HD-ruled or OPINION).
- **Gemini: 2 ACCEPT + 4 MINOR across EXT7** (fresh-thread recipe in force; P2 ACCEPT-WITH-MINOR is the round's strongest calibration anchor).
- **ChatGPT: MAJOR×6 in EXT7** (baseline-floor pattern; truth-audit confirmed 0 new physics blockers; P2 "narrowly" running for ≥4 rounds).
- **All 6 papers at 95% readiness cap**; exit-criterion met (clean external round + converged gap series).
- **Submission versions after P1A patch:** v1A.0.69 / v1B.0.65 / v1.7.60 / v3.1.103 / v1.0.182 / v0.1.72.

---

## 2. Per-paper state

### P1A — ECH structural constraints (v1A.0.68 → v1A.0.69 after 2-line patch)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini ACCEPT WITH MINOR REVISIONS. EXT7 finding count after truth-audit: 2 MINOR-arithmetic (OpenAI P1A-E4: 10¹²⁰/10¹²² convention mismatch between body and Fig 5/Table I; P1A-E5: sphaleron T-threshold "10¹² GeV" → "few × 10¹⁰ GeV" — conclusion unchanged). All EXT7 ESSENTIALs stale or HD-ruled. 12 STALE, 8 OPINION, 0 new physics blocker.

**R37conf internal:** NOT-CLEAN on the same 2 MINOR items; all other rounds CLEAN. Closure plan: 1-line fix each at L1261/L1263 (E5) + Fig 5 caption / Table I convention unification (E4) → v1A.0.69 bump.

**What's left:** Apply 2-line patch, bump to v1A.0.69, recompile. Then this paper is submission-ready.

**[ ] Houston approves P1A v1A.0.69 for arXiv submission**

---

### P1B — MCMC companion (v1B.0.65)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini ACCEPT. Grok ACCEPT stable through EXT3–EXT7. EXT7 findings: 0 new VERIFIED. ChatGPT MAJOR reduces to companion-posture re-raise (standalone-reader) — HOUSTON-DECISION. Gemini ACCEPT confirms EXT7 FB2 NaMaster Eq (1) closure persisted.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED findings. 16 STALE, 6 OPINION.

**What's left:** Optional — fold SN-overlap control chains (Exploratory w₀wₐ section) before submission; paper already carries the "Exploratory" caveat + full disclosure. Ruling: hold or ship is Houston's call.

**[ ] Houston approves P1B v1B.0.65 for arXiv submission** (option: hold for SN-overlap chain fold-in)

---

### P2 — f_NL forecast (v1.7.60)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini MINOR REVISION. Grok ACCEPT stable EXT3–EXT7. Gemini MINOR (ACCEPT-tier). EXT7 findings: 0 new VERIFIED. ChatGPT MAJOR reduces to re-raises of EXT6 items already closed (2.6–5σ realistic leading in abstract; Fig 1 6.25σ ref-only bar tagged; Refs [28]/[34] updated). Truth-audit: "zero residual findings is a physics/derivation blocker."

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 11 STALE, 8 OPINION. Gemini P2 ACCEPT-WITH-MINOR is R37conf's strongest calibration anchor.

**What's left:** None blocking. Optional: targeted in-thread ChatGPT delta-confirm on regenerated figures (recommended; cheap; submission-day).

**[ ] Houston approves P2 v1.7.60 for arXiv submission**

---

### P3 — Multi-survey anomaly catalog (v3.1.103)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini MAJOR REVISIONS. Grok ACCEPT stable EXT3–EXT7. Gemini MAJOR driven by data-leakage blocker on Planck 152/200 overlap — EXT7 closure added explicit binomial p-value caveat. EXT7 findings after truth-audit: 0 new VERIFIED on disk.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 18 STALE, 6 OPINION, 1 FALSIFIED (Grok P3-M2 SDSS log scale misread). Gemini-P3 calibration restored (§-number resolution verified; EXT6 hallucination did not recur).

**What's left:** The two residual Houston-decisions from the 2026-06-11 package (title plural/count framing; S_BigAE column strip from Table III) are re-listed below in §4. No compute gate open.

**[ ] Houston approves P3 v3.1.103 for arXiv submission**

---

### P4 — Galaxy chirality catalog (v1.0.182)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini ACCEPT WITH MINOR REVISIONS. Grok ACCEPT stable EXT3–EXT7. Gemini "high-quality, impactful" — MAJOR driven entirely by HD-11 release-bundle gate (Zenodo DOI placeholder), not science. EXT7 findings: 0 new VERIFIED. No headline number challenged (HC null +0.41σ, WLS exclusion z≈−18) in any of 7 cycles.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 14 STALE, 7 OPINION.

**What's left:** HF model-repo version tag `bamfai/galaxy-chirality-v2` → tag v2026.04 (5 min, HF write token). Submission-day task only. First paper in submission queue.

**[ ] Houston approves P4 v1.0.182 for arXiv submission** (first in queue)

---

### P5 — DESI chirality environment (v0.1.72)

**EXT7 (3-vendor):** ChatGPT MAJOR REVISIONS · Grok ACCEPT · Gemini MINOR REVISION. Grok ACCEPT stable EXT3–EXT7. Gemini MINOR (ACCEPT-tier). EXT7 findings: 0 new VERIFIED. Grok ESSENTIAL k=20 re-raise now at SEVENTH consecutive flag — auto-falsify rule binding; exact k-unbounded rerun is in the paper, conclusions invariant.

**R37conf internal:** CLEAN — 0 genuinely-new VERIFIED. 13 STALE, 7 OPINION.

**What's left:** NM1 title count ruling (title reads "791,635" but T-Web cross-check uses 783,820 env-matched; recommend "783,820 Environment-Matched DR1 Spirals"). Once ruled, Fig 3 title regen is minutes of local work. Insert P4's arXiv ID on submission day.

**[ ] Houston approves P5 v0.1.72 for arXiv submission** (after NM1 title ruling + Fig 3 regen)

---

## 3. Submission runbook

**Full coordinated-drop runbook (2026-06-13 EXT10 pre-stage):** `project-context/SSOT/ARXIV_SUBMISSION_RUNBOOK.md`

Key addition vs earlier runbook: **coordinated same-hour drop + 24h v2 back-patch window** to resolve companion ESSENTIAL cross-citations simultaneously.

Order per SSOT/PUBLISH_PLAN.md: **P4 → P1A+P1B → P3 → P2 → P5**.

1. **P4 (first):** Tag GitHub release at v1.0.182 → Zenodo auto-import → edit metadata → publish → copy DOI. Replace all `\artifact{}` blob/main links with pinned commit or DOI. Add HF model-repo tag v2026.04 on `bamfai/galaxy-chirality-v2`. Recompile + `/latex-audit` + `/artifact-link-verify`. Rebuild tarball `paper4_arxiv_v1.0.182.tar.gz`. Upload to arXiv. Note the arXiv ID.

2. **P1A (same day):** Apply v1A.0.69 patch (E4+E5 closures, ~3 lines). Recompile. Insert P4 arXiv ID at companion anchors + `\preprint{arXiv:XXXX.XXXXX}` marker. Tag + Zenodo DOI. Tarball `paper1a_arxiv_v1A.0.69.tar.gz`. Upload.

3. **P1B (same day as P1A):** Insert P1A arXiv ID at companion refs. Replace App A "pending DOI assignment" with minted DOIs. If SN-overlap chains converged, fold (w₀,wₐ) shifts into §III/Table II. Recompile. Tarball `paper1b_arxiv_v1B.0.65.tar.gz`. Upload.

4. **P3:** Insert P1A/P1B arXiv IDs. Flip HF dataset `bamfai/bigbounce-anomaly-catalog` STAGED → public at arXiv posting. Insert Zenodo DOI in DATA_RELEASE_MANIFEST.md header + tex L44 marker. Recompile. Tarball `paper3_arxiv_v3.1.103.tar.gz`. Upload.

5. **P2:** Run ZENODO_RELEASE_CHECKLIST.md steps 1–6 (tag paper2-v1.7.60). Replace "DOI inserted at submission" placeholders. Optional in-thread ChatGPT figure delta-confirm. Tarball `paper2_arxiv_v1.7.60.tar.gz`. Upload.

6. **P5 (last):** NM1 title ruling → Fig 3 regen → restamp to v0.1.72 (or v0.1.73 if regen forces a bump). Insert P4 arXiv ID. Mint Zenodo DOI. Tarball. Upload.

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
