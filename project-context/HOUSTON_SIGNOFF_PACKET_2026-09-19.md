# Houston sign-off packet — 2026-09-19

**Prepared by:** campaign lane `bb-L6-signoff-packets` (Sonnet), campaign
`project-context/campaigns/CAMPAIGN_2026-09-18_publication_push.md`, criterion A9.
**Readiness semantics (directive P, `CLAUDE.md`):** 95 = every agent gate done
(science 25 + evidence/reproducibility 25 + automated review convergence 25 +
packaging/PDF hygiene 20); **100 only via Houston's literal per-paper sign-off**,
recorded as a quoted `APPROVE` in that paper's SSOT status file. There is no 96.
Venue/submission clicks, arXiv endorsement, and Houston's own independent
scientific read are a separate "publishing phase," never subtracted from the
95 score.

All hashes below were computed fresh in this session (`md5`, `pdfinfo`) against
the files actually on disk and cross-checked live against Convex
(`paperVersions:current`, `papers:listAllPaperStates`) via the public HTTP API —
not copied from any prior report.

---

## 0. Lineage reconciliation — READ THIS FIRST (Houston's call)

Five papers currently carry SSOT readiness 95 and are the historical "sign-off
five": **P1A, P1B, P2, P4, P5**. Since `PAPER_LINEAGE_2026-08-05.md`'s
2026-09-02 portfolio restructure (directive R3), **two of the five have been
superseded by newer, differently-scoped papers that also exist and are also at
95** (`P1N`, `P4P`). Nothing was deleted — this is a live choice about which
manuscript is the actual submission target. Stated plainly, both options:

| Original (still on disk, still 95, still has its own submission kit) | Superseding paper (also 95, actively being finished by this campaign) | What superseding means |
|---|---|---|
| **P1A** — `arxiv/paper1a_ech_nogo.tex` v1A.0.127, CQG Note, standalone algebraic no-go | **P1N** — `arxiv/paper1bc_ech_note/main.tex` v1N.0.6, `arxiv/paper1bc_ech_note/`, merges P1A + the frozen P1C no-go survey into one ≤12pp CQG/gr-qc Note | If you submit P1N, P1A itself is not separately submitted — its content lives inside P1N. If you'd rather ship the original narrower P1A Note on its own, that's still possible; the CQG kit for it (`SSOT/CQG_SUBMISSION_KIT_P1A_2026-07-24.md`) still exists. |
| **P4** — `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.274, ApJS, 8.47M-galaxy catalog + observed-label dipole null | **P4P** — `pipelines/p4prime_chirality_test/paper/main.tex` v4P.0.7, `pipelines/p4prime_chirality_test/paper/`, folds P4 + P5 into one ≤15pp Poplawski spin-axis-exclusion test | Same choice: P4P absorbs both P4's catalog paper and P5's environment paper into one reframed test. Submitting P4P means P4 and P5 are not separately submitted as standalone manuscripts. |
| **P5** — `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.147-2026-08-03, AJ, DESIVAST void/non-void chirality null | *(same P4P as above)* | — |
| **P1B** — `arxiv/paper1b_namaster_proof.tex` v2B.0.23, JORS, namaster-proof software metapaper | *(no superseding paper — P1B stands alone)* | Not affected by the lineage decision. |
| **P2** — `research/focused_paper_source_integration/02_full_draft.tex` v1.7.130, PRD, f_NL = −35/16 derivation | *(folded as a theory section into A3M, per the 2026-09-02 evening decision — but P2 itself was NOT retired; it remains the PRD submission target for the derivation on its own)* | Not affected by the lineage decision for sign-off purposes; A3M is a separate flagship paper still at readiness 75 (rounds stopped, not part of this packet). |

**Houston's decision needed:** for the P1A/P1N pair and the P4+P5/P4P triple,
pick ONE track per row to actually submit. The agent-side recommendation
(not a substitute for your call): submit the merged/folded versions (**P1N**,
**P4P**) — that is what the 2026-09-02 portfolio restructure (directive R3,
`PORTFOLIO_DECISION_2026-09-02.md`) already decided editorially, and it is why
this campaign is actively finishing P1N's D/P-round and P4P's confirmation
board in parallel lanes right now. Submitting the older P1A/P4/P5 kits instead
remains fully possible — their tarballs, portal kits, and DOIs already exist —
this is not a technical blocker either way, only your editorial choice. **This
packet covers all five of the 95-readiness papers (P1A, P1B, P2, P4, P5) as
literally asked**, and flags P1N/P4P inline where they change the picture.

---

## 1. P1A — ECH algebraic Note (spin contact + zero-spin scalar branch)

- **Canonical source:** `arxiv/paper1a_ech_nogo.tex`, `\paperVersion` = **v1A.0.127** (July 24, 2026, 18:35 PDT)
- **Served PDF md5 (source + both mirrors, verified identical):** `0bc1ee72836c867114118521cf86e1c2` at `arxiv/paper1a_ech_nogo.pdf`, `public/papers/paper1a_ech_nogo.pdf`, `public/papers/paper1a_ech_nogo_v1A.0.127.pdf`, `site/public/papers/paper1a_ech_nogo.pdf`, `site/public/papers/paper1a_ech_nogo_v1A.0.127.pdf` — **all 5 paths match, no mismatch.**
- **Convex `paperVersions:current` (slug `paper-1a`):** version `v1A.0.127`, md5 `0bc1ee72836c867114118521cf86e1c2`, 8 pages, datestamp "July 24, 2026" — **matches served files exactly.**
- **Page count:** 8 pp (this is the merged/trimmed CQG Note length; not the ~20pp figure quoted in the superseded May-2026 `HOUSTON_SIGN_OFF_BRIEF.md` — that document is stale, see §5).
- **Convex `listAllPaperStates`:** readinessComputed **95**, houstonSignOff **null**, openBlockers/Majors/Minors/Caveats **0/0/0/0**.
- **arXiv tarball:** `project-context/SSOT/arxiv_tarballs/paper1a_arxiv_v1A.0.127.tar.gz` present; also `arxiv/paper1a_arxiv_v1A.0.127.tar.gz` + `.proof.json` (standalone-compile-verified per its own proof record).
- **DISPOSITIONS/P1A.md:** 0 open items in the current ledger (all DP1A-01..07 CLOSED-BY-EDIT/SCOPE/SPLIT, or explicitly moved to "REMOVED FROM CLAIM SET; OPEN RESEARCH" — i.e. disclosed as out of scope, not hidden). **DEFECT:** the file's own header still says "Current paper-local version: v1A.0.116 (2026-07-14 split revival)" — stale by 11 patch versions; harmless (the disposition rows themselves are current per SSOT cross-reference) but worth a housekeeping refresh.
- **Last confirmed exact-version INT board:** v1A.0.124 (2026-07-16, round `ROUND_2026-07-16-P1A-v1A.0.124-EXACTPDF-5689a5f8-CLAUDESTACK-CONFIRM`) — Claude Opus subagent **MAJOR REVISIONS** (3M/4m, but headline: "ZERO correctness errors," all 13 findings were significance/self-containment asks), Grok **MINOR** (3), Gemini **MINOR** (3); truth-audit: 0 genuinely-new-real. A later CQG-Note confirmation at v1A.0.123 (2026-07-14) got a ChatGPT-subscription Codex CLI **ACCEPT** (0/0).
  - **DEFECT (real, plainly stated):** the exact CURRENT bytes (v1A.0.127) have **not** had their own dedicated INT/EXT confirmation board — the last verified board ran on v1A.0.124, three patch versions behind. The three intervening bumps (v1A.0.125 DOI embed, v1A.0.126 confirmation-wave closures, v1A.0.127 GATE-0/word-count close per the CQG kit) are text/metadata-only per their own commit notes, not science changes, but this is still an un-reconfirmed-on-exact-bytes gap, consistent with every other paper in this packet (see §6).
- **Submission target:** CQG Note (gr-qc). Kit: `project-context/SSOT/CQG_SUBMISSION_KIT_P1A_2026-07-24.md`. Zenodo DOI PUBLISHED: `10.5281/zenodo.21481838` (concept `21481837`).
- **Superseded-by-lineage note:** see §0 — P1N (`arxiv/paper1bc_ech_note/`) is the merged successor and is what this campaign is actively finishing (D-round/P-round, lane L3, now at v1N.0.6, Convex readinessComputed **99**).

## 2. P1B — namaster-proof (reproducible spin-2 software metapaper)

- **Canonical source:** `arxiv/paper1b_namaster_proof.tex`, `\paperVersion` = **v2B.0.23** (2026-09-05 12:00 PT)
- **Served PDF md5 (source + both mirrors + arXiv-alias, verified identical):** `60d1a18ab3ea499398106d6a92bc8a35` at `arxiv/paper1b_namaster_proof.pdf`, `public/papers/paper1b_namaster_proof.pdf`, `public/papers/paper1b_namaster_proof_v2B.0.23.pdf`, `public/papers/paper1b_namaster_proof_arxiv_v2B.0.23.pdf`, `site/public/papers/paper1b_namaster_proof.pdf`, `site/public/papers/paper1b_namaster_proof_v2B.0.23.pdf`, `site/public/papers/paper1b_namaster_proof_arxiv_v2B.0.23.pdf` — **all 7 paths match.**
- **Convex `paperVersions:current` (slug `paper-1b`):** version `v2B.0.23`, md5 `60d1a18ab3ea499398106d6a92bc8a35`, 16 pages, datestamp "2026-09-05" — **matches.**
- **Convex `listAllPaperStates`:** readinessComputed **95**, houstonSignOff **null**, 0/0/0/0 open.
- **arXiv tarball:** `public/papers/paper1b_namaster_proof_arxiv_v2B.0.23.pdf` present as an arXiv-alias PDF; the source tarball referenced by SSOT is `paper1b_namaster_proof_arxiv_v2B.0.23.tar.gz` (standalone-smoke PASS per the v2B.0.23 status note: tarball sha256 `495c4bde...`).
- **DISPOSITIONS/P1B.md:** legacy v1B rows (DP1B-01..05) CLOSED; the current v2B (batch-3/R7/R8 blind-shortcut-detection) science closure is tracked directly in `SSOT/paper-1/status.md`, not re-listed in the DISPOSITIONS file — **DEFECT:** DISPOSITIONS/P1B.md's header is stale at "v2B.0.8," 15 patch versions behind current v2B.0.23; the real closure trail lives in SSOT instead. Worth consolidating so DISPOSITIONS stays the single ledger per its own stated purpose.
- **Last confirmed exact-version INT board:** v2B.0.20 (2026-09-05, round `ROUND_2026-09-05-P1B-v2B.0.20-EXACTPDF-cf57f485-R3VERIFY`) closed 27 of 33 canonical findings as genuinely-new-real via real science (batch-4 R7/R8 post-commitment verifier test). SSOT explicitly records **"ROUNDS STOPPED (R2) — next: venue decision + ASCL/Zenodo kit (Houston)"** after that closure — i.e. P1B's review rounds are deliberately paused per directive R2 (convergence budget), awaiting your venue call, not stalled by accident. v2B.0.21–v2B.0.23 closed three remaining **text-only** deferred items (audit-trail sentence, frozen-rule digest quoting, a table trust-category) with no new science and, per the campaign's own convention, do not require a fresh board.
- **Submission target:** JORS. Per-paper queue: "JORS account, five reviewer names with real emails, fee/waiver decision, final sign-off, and upload." Software archive DOI PUBLISHED: `10.5281/zenodo.21481753` (namaster-proof 0.1.7).
- **Not affected by lineage §0** — stands alone, no superseding paper.

## 3. P2 — f_NL forecast (exact matter-contraction −35/16)

- **Canonical source:** `research/focused_paper_source_integration/02_full_draft.tex`, `\paperVersion` = **v1.7.130** (July 24, 2026, 18:35 PDT)
- **Served PDF md5 (source + both mirrors, verified identical):** `f7116fe3e2541d6f649876f2ec7789ee` at `research/focused_paper_source_integration/02_full_draft.pdf`, `public/papers/02_full_draft.pdf`, `public/papers/02_full_draft_v1.7.130.pdf`, `site/public/papers/02_full_draft.pdf`, `site/public/papers/02_full_draft_v1.7.130.pdf` — **all 5 paths match.**
- **Convex `paperVersions:current` (slug `paper-2`):** version `v1.7.130`, md5 `f7116fe3e2541d6f649876f2ec7789ee`, 12 pages, datestamp "July 24, 2026" — **matches.**
- **Convex `listAllPaperStates`:** readinessComputed **95**, houstonSignOff **null**, 0/0/0/0 open.
- **arXiv tarball:** `research/focused_paper_source_integration/paper2_arxiv_v1.7.130.tar.gz`, receipt `FINAL_PACKAGE_RECEIPT_v1.7.130_2026-08-03.md` (source bundle sha256 `74124142...`).
- **DISPOSITIONS/P2.md:** most-recent canonical entry is the v1.7.118 editorial/reproducibility closure (all 6 named items closed); the file's own header is stale relative to the current v1.7.130 (12 patch versions of subsequent DOI-embed, dressed-metric, and torsion-bound closures live in `SSOT/paper-2/status.md`'s inline HTML-comment history instead — same pattern as P1B, **DEFECT** of the same shape).
- **Last confirmed exact-version INT board:** v1.7.122 (2026-07-14, round `ROUND_2026-07-14-P2-v1.7.122-EXACTPDF-4097bac5-PRD-NONANTHROPIC-CONFIRM`) — ChatGPT-subscription Codex CLI **ACCEPT**, Gemini **ACCEPT**, Grok **ACCEPT**, 0 hidden MAJOR/MINOR either leg; truth-audit confirmed all seven prior clarity findings closed and the exact four-vertex coefficients.
  - **DEFECT:** current v1.7.130 is 8 patch versions past that confirmed board (v1.7.123 torsion-bound compute closure, v1.7.124 framing/citation fixes, v1.7.125 dressed-metric transmission closure, plus subsequent DOI-embed and confirmation-wave text closures) — no fresh exact-byte confirmation board has run since. Each intervening bump has its own closure note citing real science or real truth-audited edits, but the ALL-ACCEPT board itself is stale by 8 versions.
- **Submission target:** PRD. Per-paper queue: "APS account/ORCID/DAS checks, final sign-off, PRD upload." Zenodo DOI PUBLISHED: `10.5281/zenodo.21461881` (archives the reviewed v1.7.125 bytes exactly; the v1.7.126 DOI-embed sentence is the only subsequent edit, no science number changed).
- **Not affected by lineage §0 for sign-off purposes** — P2 remains its own PRD target even though its theory content is now also echoed inside A3M (readiness 75, rounds stopped, not part of this packet).

## 4. P4 — Observed-label chirality-dipole null + 8.5M-galaxy catalog

- **Canonical source:** `pipelines/p2_chirality/chirality_catalog_paper.tex`, `\paperVersion` = **v1.0.274** (per SSOT top board; file header shows the running v1.0.27x closure series)
- **Served PDF md5 (source + both mirrors, verified identical):** `6c7de2b81dfa3d7af2a7414214d57cfc` at `pipelines/p2_chirality/chirality_catalog_paper.pdf`, `public/papers/chirality_catalog_paper.pdf`, `public/papers/chirality_catalog_paper_v1.0.274.pdf`, `site/public/papers/chirality_catalog_paper.pdf`, `site/public/papers/chirality_catalog_paper_v1.0.274.pdf` — **all 5 paths match.**
- **Convex `paperVersions:current` (slug `paper-4`):** version `v1.0.274`, md5 `6c7de2b81dfa3d7af2a7414214d57cfc`, 32 pages, datestamp "August 3, 2026" — **matches.**
- **Convex `listAllPaperStates`:** readinessComputed **95**, houstonSignOff **null**, 0/0/0/0 open.
- **arXiv/ApJS package:** `pipelines/p2_chirality/paper4_arxiv_v1.0.274.tar.gz` + `.proof.json`; `APJS_PORTAL_KIT_v1.0.274.md` present. Per SSOT: "The 14-member flat ApJS/arXiv package SHA-256 is `9503ddd1...be736`; isolated Tectonic compile and the full visual, overflow, artifact, and URL audits pass."
- **DISPOSITIONS/P4.md:** extremely long, active history through M44 (2026-07-14); current standing items DP4-15 (OPEN-COMPUTE: image-level end-to-end classifier injection) and DP4-17 (OPEN-COMPUTE: joint real-space × harmonic covariance) remain explicitly disclosed-open, not fabricated closed — these are exactly what ledger row 13/16 (§6) targets.
- **Last confirmed exact-version INT board:** v1.0.264 (2026-07-17, round `ROUND_2026-07-17-P4-v1.0.264-EXACTPDF-325b7ced-CLAUDESTACK-CONFIRM`) — Claude Opus **MAJOR** (7M/5m), Grok **MAJOR** (3M/2m), Gemini **MINOR** (4m); truth-audit dispositioned 21 findings to 8 tracked gates + 6 disclosed re-flags + 8 venue/style opinions + 0 falsified + **2 genuinely-new-real**, both closed same-wave in v1.0.265 with real computation (an observed-label coverage-calibrated upper limit, and a review-narration-clause fix).
  - **DEFECT, stated plainly by the paper's own status file:** "Exact v1.0.274 provider confirmation remains due." Current v1.0.274 is **10 patch versions** past the last confirmed board (v1.0.265→274 closed a real inline-provenance-density MAJOR at v1.0.272, an AASTeX source-package defect at v1.0.273, and one genuinely-new minor ECE-acronym expansion at v1.0.274 — each with its own closure evidence — but no fresh multi-vendor board has re-run on the exact current bytes since v1.0.264).
- **Submission target:** ApJS. Per-paper queue: "confirm AAS acceptance of declared HF-hosted assets, final sign-off, and ApJS upload." HF model `bamfai/galaxy-chirality-v2`. DOI PUBLISHED: `10.5281/zenodo.21461899`.
- **Superseded-by-lineage note:** see §0 — P4P folds P4 (this paper) and P5 together; P4P v4P.0.7 is currently mid-confirmation-board in lane L4, Convex readinessComputed 95, md5 `1fc6b21ae07accb0b2a3441e4a31ebc1` (13pp) — matches all served/source paths verified this session.

## 5. P5 — DESIVAST catalog-native void non-detection (galaxy chirality × cosmic web)

- **Canonical source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, `\paperVersion` = **v0.1.147-2026-08-03** (August 3, 2026)
- **Served PDF md5 (source + both mirrors, verified identical):** `8b9365ff762e0baed12ad9963d9aea1d` at `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf`, `public/papers/p5_desi_chirality.pdf`, `public/papers/p5_desi_chirality_v0.1.147-2026-08-03.pdf`, `site/public/papers/p5_desi_chirality.pdf`, `site/public/papers/p5_desi_chirality_v0.1.147-2026-08-03.pdf` — **all 5 paths match.**
- **Convex `paperVersions:current` (slug `paper-5`):** version `v0.1.147-2026-08-03`, md5 `8b9365ff762e0baed12ad9963d9aea1d`, 46 pages, datestamp "August 3, 2026" — **matches.**
- **Convex `listAllPaperStates`:** readinessComputed **95**, houstonSignOff **null**, 0/0/0/0 open.
- **arXiv + AJ package:** `pipelines/p5_desi_chirality/paper/paper5_arxiv_v0.1.147-2026-08-03.tar.gz` + `.proof.json`, `paper5_aj_v0.1.147-2026-08-03.tar.gz` + `.proof.json`, `AJ_PORTAL_KIT_v0.1.147-2026-08-03.md` — both arXiv and AJ-specific packages present.
- **DISPOSITIONS/P5.md:** current through M45 (2026-07-15); the target-program-by-environment interaction is retained as an honestly-disclosed limitation (SSOT: "P5's target-program-by-environment interaction remains an honestly disclosed systematic limitation; convergence does not turn that conditional null into a physical independence claim") — this is disclosure, not an open defect.
- **Last confirmed exact-version INT board:** v0.1.140 (2026-07-16, round `ROUND_2026-07-16-P5-v0.1.140-EXACTPDF-287c6494-CLAUDESTACK-CONFIRM`) — Grok **MAJOR** (flipped from MINOR on v0.1.139), Gemini **MINOR**, Claude Opus **MAJOR**.
  - **DEFECT, stated plainly by the paper's own status file:** "A bounded final-hash confirmation remains due." Current v0.1.147 is **7 patch versions** past that board (hierarchy-sensitivity closure at v0.1.145, a prominent leakage-caveat addition at v0.1.146, an AASTeX 7.0.2 AJ-shell migration with no science change at v0.1.147) — no fresh board on the exact current bytes.
- **Submission target:** AJ. Per-paper queue: "retain the target-program caveat, obtain final sign-off, then mint the immutable tag/Zenodo snapshot, back-patch identifiers, rebuild, and complete the AJ upload." **P5's Zenodo DOI is NOT yet minted** — it is explicitly gated to come *after* your sign-off (unlike P1A/P1B/P2/P4, which already have PUBLISHED DOIs). This is the one paper in this packet where a sign-off unlocks a further irreversible agent action (the DOI mint), not just a submission click.
- **Superseded-by-lineage note:** see §0 — P4P folds P5 (this paper) and P4 together.

## 6. Cross-cutting notes

- **The "exact-version confirmation board" gap is universal across all 5 papers.** Every one of P1A/P1B/P2/P4/P5's most-recently-*confirmed* multi-vendor board ran on a version 3–10 patch bumps behind the paper's current canonical bytes. In every case the intervening bumps are individually closure-evidenced (real truth-audited findings closed, or disclosed text/metadata-only edits) rather than silent drift, and Convex's live `openFindings` counters read 0/0/0/0 for all five — but none of the five has had a review board run on its *literal current* PDF bytes. If your bar for "sign-off-ready" requires a board on the exact final artifact, that board has not run for any of the five; if your bar is "every known finding closed and disclosed, agent gates complete," all five already meet it (that is what readiness 95 encodes). Stating this so the choice is explicit rather than implied.
- **arXiv endorsement (D4) — still an open blocker as of the last recorded check (2026-07-22):** Houston's arXiv account (`houstongolden`) is not endorsed for gr-qc or astro-ph. Four endorsement codes were generated and emailed to `houston@bamf.ai`: gr-qc `HYEJ7S` (P1A/P1N), astro-ph.IM `L8TIPN` (P1B, P3), astro-ph.CO `LRZHC4` (P2), astro-ph.GA `CLVMAQ` (P4/P4P, P5). A draft arXiv submission (#7859751) is parked at Start. **This does not block journal submission** — CQG/JORS/PRD/ApJS/AJ portals do not require arXiv, and all papers with DOIs already have a citable, permanent record via Zenodo.
- **ORCID (D5):** correct iD is `0009-0008-5616-5994` (superseding an earlier typo'd `0009-0008-3617-8729` recorded on 2026-07-21 and since corrected in SSOT). Flip to PUBLIC + verify `pub.orcid.org` returns 200 remains on your list; last explicit queue mention was 2026-06-18/26 ("ORCID flip"). Not re-verified live in this session (no network fetch performed) — confirm current visibility yourself before journal submission, since APS/JORS/ApJS/AJ portals commonly require a public ORCID at account setup.
- **Gemini API billing — CORRECTION to the campaign brief's assumption.** `CLAUDE.md` directive I1 still carries a 2026-07-05 note that "all stored Gemini API keys 403/billing-blocked." That is stale: `queue.md` records the key issue **CLOSED 2026-07-11** ("GEM1-INT: 7TH REVIEWER ONLINE... the prior needs-Houston 'billed Gemini API key' ask is CLOSED — delivered"), and this campaign's own log today (2026-09-18) shows live Gemini API verdicts landing for both the A3M R9 board and the P-SU R2 board. **No Gemini billing action is needed from you right now** — this item can be dropped from your action list; if a fresh 403 reappears the agent side will re-flag it.
- **RunPod GPU program go/no-go (ledger rows 13/16, `project-context/NEXT_SCIENCE_LEDGER.md`):** this is a P4P/galaxy-chirality follow-on, not one of the five sign-off papers directly, but it's the item your brief asked to be listed. Row 16 (full 8.47M-galaxy dipole, retrained classifier, chirality×environment cross-correlations) has already been substantially executed on **local CPU/MPS at $0** — no pod was needed for the headline results, though a real systematic was found and disclosed (the full-parent dipole's z=+4.44σ signal traced to raw-flip QC/imaging-leg contamination, not cosmology). Row 13 (image-level end-to-end injection through the actual classifier, plus a first Euclid Q1 chirality-dipole test) is genuinely **OPEN, proposed to you 2026-09-04**, budgeted at ≤$30 on RunPod for the injection pilot. This is a real go/no-go: authorizing it would harden the 0.98% observed-label bound with a generative-null/image-level check and open a new independent measurement (Euclid Q1); declining it leaves the current label-level bound as the final word on those two open DISPOSITIONS items (DP4-15/DP4-17).

---

## 7. Exact Houston-only action list

Nothing below requires further agent work — every item needs your literal input, click, or decision.

1. **Lineage choice (§0):** for P1A vs P1N, and for P4+P5 vs P4P, tell the agent side which manuscript(s) you want carried to actual submission. (Recommended: P1N and P4P, per the already-adopted 2026-09-02 portfolio restructure — but your call.)
2. **Per-paper sign-off (95 → 100).** For each paper you want to move to 100, record your literal `APPROVE` (or equivalent explicit sign-off sentence) in that paper's `project-context/SSOT/paper-N/status.md` — this is the only thing directive P recognizes as the last 5 points:
   - P1A (or P1N, per your §0 choice)
   - P1B
   - P2
   - P4 (or P4P, per your §0 choice)
   - P5
3. **arXiv endorsement (D4):** forward the four endorsement-code emails (already sent to `houston@bamf.ai`) to qualified endorsers — 4+ astro-ph.* submissions in the last 3mo–5yr covers all three astro-ph codes; gr-qc needs 4+ gr-qc papers from the endorser. Only needed if you want arXiv preprints in addition to journal submission; not required for journal upload itself.
4. **ORCID (D5):** confirm `0009-0008-5616-5994` is flipped to PUBLIC visibility (check `pub.orcid.org/0009-0008-5616-5994` returns your profile); several journal portals require this at account creation.
5. **Journal portal clicks** (after step 2's sign-off), one account/upload per venue:
   - P1A/P1N → CQG (Classical and Quantum Gravity)
   - P1B → JORS (five reviewer names + real emails, fee/waiver decision needed from you)
   - P2 → PRD (APS account/ORCID/DAS checks)
   - P4/P4P → ApJS (confirm AAS acceptance of the declared HF-hosted dataset/model assets)
   - P5 → AJ (after sign-off, the agent side still needs to mint the immutable Zenodo tag/DOI and back-patch it into the paper before final AJ upload — flagging that one extra irreversible step is gated on your sign-off, not skippable)
6. **RunPod GPU program go/no-go (ledger row 13):** authorize or decline the ≤$30 image-level injection pilot + Euclid Q1 access check for the galaxy-chirality line. Not required for any of the five sign-offs above; purely a research-continuation decision.
7. **Gemini billing key:** no action needed — see §6 correction above.
