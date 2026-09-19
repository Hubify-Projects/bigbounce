# AF (anomaly flagship) status — current authoritative section

**Current candidate:** vAF.0.4 · `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.tex`
**Directive-P readiness:** 75 (COMPUTED, Convex `readinessCap`) — R1 INT board closed
2026-09-19 (lane LR1): all 6 BLOCKER + all 16 MAJOR findings truth-audited verdict-first;
17 closed with real edits/new computation, 3 honestly disclosed as open (not fabricated,
not hidden). Directive R2: round 1 of 2 spent. See "R1 INT board closed" below for the
full item-by-item outcome; `project-context/peer-reviews/DISPOSITIONS/AF.md` for the
canonical per-item ledger.

## R1 INT board closed (vAF.0.3 → vAF.0.4, 2026-09-19)

Campaign lane LR1. Board: Claude opus (INT, verdict-blind, exact vAF.0.2 sha8
`b972d890`) + Grok API `grok-4.3` + Gemini API `gemini-3.1-pro-preview` (both via
`tools/v3_native_pdf_review.py`, `ApJS-CATALOG` profile, exact vAF.0.3 sha8 `d85487e9`).

**Verdicts (words diagnostic only, per directive H):** Claude opus MAJOR REVISIONS (6
BLOCKER, 16 MAJOR, 16 MINOR, 9 NIT). Grok REJECT (9 ESSENTIAL across 2 passes, 3 MAJOR, 2
MINOR, 1 NIT). Gemini MAJOR REVISIONS (6 ESSENTIAL/MAJOR across 2 passes, 3 findings, 1
NIT). **All three legs independently converged on the same core defects** — the
validation-contract pass-count error (13 claimed vs. 11 actual), the abstract-vs-body
mismatch on statistical power and the blue-arm origin, and the title not carrying the
paper's own null result — a strong triangulation signal, not one reviewer's
idiosyncrasy.

**Orchestrator verification (before any closure, per the standing truth-audit rule):**
every BLOCKER and the highest-impact MAJOR findings were independently re-derived from
the committed artifacts (`validation_contract_results.json`,
`flagship_sample_v2_enriched.parquet`, `flagship_sample_v2.parquet`) — not accepted from
reviewer text alone. 10/10 spot-checks reproduced the reviewer's numbers exactly.

**The single most consequential finding (DAF-03/04):** the abstract's "supports one"
z≈4.3 quasar candidate is, on independent verification, a row inside the paper's own
disclosed 406-row photometric-join defect (empty `morphtype`, exact-zero WISE/shape
columns) whose own r/z flux ratio is physically backwards for the redshift it would need
to support. Downgraded from "Supported" to "Undecidable"; the abstract's headline
follow-up outcome is now "refutes one of four, cannot decide the other three" (was
"refutes one, supports one, cannot decide two").

**17 of 20 canonical findings closed with real edits or new, independently-verified
computation** (no science number changed without a committed computation, per directive):
validation pass count 13→11 (V1 marked partial pass); provenance-chain caption corrected
to state exactly what V2 vs. V3 each verify; title changed to
"...selection, validation, and a null known-object recovery benchmark"; abstract/§I/§XI
rewritten in all three summary locations for the monotonicity qualifier, the blue-arm
evidence, and the benchmark power caveat; **new committed script**
`blue_arm_diagnostics_2026-09-19.py` (independently written and run by the orchestrator)
adds a real variance decomposition (mean_mse on rB/rR/rZ: R²=0.777, dropping rB collapses
it to 0.006) and a rest-frame-vs-observed-frame concentration test (IQR/median 0.39 vs.
0.68) — both lean instrumental without closing the blue-arm origin question; Table VII's
BAL enrichment fixed at the generator script (not hand-edited), 4.2×→3.3× against the
correct science-target denominator; the "Supported"→"Undecidable" downgrade above;
matched/unmatched score difference reframed as confounded by brightness with the real
medians/p-values; Table IV schema gains `residual_kurtosis` and an explicit
constant-placeholder-column disclosure; the f_NL paragraph now cites a real,
already-committed derivation script (`research/anomaly_map/ledger6_png_highz_abundance.py`)
with a corrected order-of-magnitude comparison (was arithmetically wrong: 0.3 dex ≈
factor 2, not >10×); NED/VizieR/AllWISE/Redrock citations added; the 2 remaining raw
`[placeholder:]` blocks (OT-1, Zenodo DOI) rewritten to honest specified-but-not-executed
prose.

**3 findings honestly disclosed as open, not fabricated or hidden** (real further work,
correctly out of scope for a text-edit closure): the archived model's undocumented
training corpus/architecture (confirmed absent from every artifact in the repo by
search); the physically-arbitrary deduplication rule's unquantified near-threshold
membership effect; the taxonomy's RA-wrap artifact and missing UMAP/HDBSCAN
hyperparameters (a corrected re-clustering is real follow-up work).

**Hygiene (directive G):** `\paperVersion` vAF.0.3→vAF.0.4; `\paperTimestamp` unchanged
(September 19 — same day). 4-pass `pdflatex`, 0 errors, 0 undefined refs/cites, 0 overfull
hboxes >10pt, 17 pages (up from 15 — real new content, not padding). `pdftoppm -r 110`
full render of every page inspected — no overflow, no overlap.

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `4ae6347c1a4c48538241d3397a5653dd`, SHA-256
  `6a475b3cbc10856a2ccaf648cd0fef670d7d9101416a1eceaf4843b803f060e9`.
  Mirrored byte-identically to `site/public/papers/anomaly_flagship_vAF.0.4.pdf`,
  `site/public/papers/anomaly_flagship.pdf`, `public/papers/anomaly_flagship_vAF.0.4.pdf`,
  `public/papers/anomaly_flagship.pdf` (four-way md5 verified).
- **Convex:** `paperVersions:bump` id `k577hk30b41tj8zxk99a6pa1k58eqbea` read back
  verified; `rRounds:create` id `ks78f5h45pgfhv49ay38qrrnf58epytk`;
  `externalReviews:upsertByLabelDate` × 3 (claude-opus, Grok_brutal, Gemini_cosmology);
  `activityFeed:add` id `j57f9gkm6metczt6y1wb11asq18eqbw9`;
  `papers:setReadinessCap` → 75, read back verified via `getPaperState`.
- **Registry:** `project-context/draft_paper_registry.json` and
  `project-context/paper_registry.json` (companion_manuscripts.AF) both updated
  (version/pages/sha256/md5/served_aliases/review_paths).
- **Dispositions:** full item-by-item ledger (21 canonical items, DAF-01 through DAF-21)
  in `project-context/peer-reviews/DISPOSITIONS/AF.md`.
- **Git:** lane LR1 commits (this bundle + the earlier vAF.0.2→vAF.0.3 registration
  commit `f7e85cd3` and the mirror-integrity regex fix `5566ba9d`).

**Directive R2:** round 1 of 2 spent. An R2 board, if run, should verify these closures on
the exact vAF.0.4 PDF and assess whether the 3 disclosed-open items need their named
follow-up work before further readiness advance. No further board is authorized without
either an R2 dispatch or an intervening science/scope decision.

## Registration (lane LR1, 2026-09-19)

LA (2026-09-19 00:06–00:09 PT) assembled the first full draft, vAF.0.2: 15 pp, revtex4-2,
9 figures, 11 tables, 0 undefined refs, compiled clean, `REPRODUCIBILITY_MANIFEST.md`
complete. It was **not yet** a Convex-tracked paper, not mirrored to any served path, and
`site_slug` was `null` in `project-context/draft_paper_registry.json`.

Lane LR1 registered it:

- **Convex:** `papers:upsert` (slug `paper-af`, number `AF`, target journal `other` — ApJS
  is not one of the four literal enum values, so `other` is used with the real target
  journal named in `target`/`article_type` text) + `paperVersions:bump` for vAF.0.2 then
  vAF.0.3, both read back and verified.
- **Served mirrors:** `site/public/papers/anomaly_flagship.pdf` (canonical alias) and
  `anomaly_flagship_vAF.0.3.pdf` (versioned alias), mirrored identically to `public/papers/`.
  Four-way md5-verified (fresh compile == both served roots == Convex).
- **`project-context/paper_registry.json`:** added `companion_manuscripts.AF` (like `P1C`
  and `P1B-MCMC`) so `tools/verify_pdf_mirror_integrity.py`'s reverse-direction
  PDF-mirror-integrity gate recognizes the served mirrors as canonical rather than
  orphaned. **Gotcha found and fixed this lane:** AF's `\paperVersion` tokens (`vAF.0.2`,
  `vAF.0.3`, …) use a letter-only prefix — no leading digit before the letter, unlike
  every other letter-suffixed paper in this repo (`v4P.0.9`, `v3M.0.26`, `v1S.0.11`,
  `v1N.0.6` all have digit-then-letter). `served_pdf_policy.immutable_archive_name_patterns`
  requires a leading digit, so AF's versioned aliases do **not** match it — the
  `companion_manuscripts` registration is the only path that makes them pass the gate.
  Future lanes touching AF's version macro: do not "fix" this to a digit-first token without
  checking every site reference and the registry regex first; it is a known, worked-around
  quirk, not a defect to silently rename.
- **`project-context/draft_paper_registry.json`:** `AF.site_slug` set to `paper-af`,
  `served_aliases` extended, sha256/md5/version bumped to vAF.0.3, `status` narrated.
- **Site surfaces** (`site/src/data/papers.ts`, `live-status.ts`, `publish.ts`, `tracks.ts`,
  `reviewTimeline.ts`, `SSOT/index.md` top board): reconciled by lane L7c (continuation of
  L7b, the site-sync reconciler lane), commit `4bad8124`, from Convex's
  `listAllPaperStates` ground truth — readiness 60, 0 boards closed. LR1 did not hand-edit
  these files after discovering L7c's concurrent, more detailed edit already landed the same
  block (avoided a duplicate `paper-af` entry in `papers.ts` — see lesson below).

**Lesson for future lanes:** this session briefly produced two `paper-af` blocks in
`site/src/data/papers.ts` — LR1's own (written before checking for a concurrent editor) and
L7c's (richer, written independently from the same committed vAF.0.3 artifacts). LR1 deleted
its own duplicate rather than fight the collision. Read the file immediately before editing
(as the campaign brief already instructs) and re-check with `grep -c 'slug: "<slug>"'` after
any insert into a shared array — a tool's "file modified on disk since you last read it"
notice is not decorative, it means re-read before trusting your own diff.

## vAF.0.2 → vAF.0.3 (lane LR1, 2026-09-19): 2 of LA's 4 open TODOs closed

LA's first draft carried four explicit `\TODO{}` placeholders (never hidden, all four named
in-paper). LR1 closed two, non-science, no number changed:

1. **ADS bibliography verification.** The paper's own Appendix A named exactly four
   citations not recorded in any committed benchmark artifact: Ref.~`RitterKolb2003`'s
   journal/volume/page, and the three software citations `Pedregosa2011`, `Hunter2007`,
   `Ginsburg2019`. All four verified against ADS/JMLR/publisher records (2026-09-19, web
   search, not memory): Ritter & Kolb 2003, A&A 404, 301 (ADS `2003A&A...404..301R`);
   Pedregosa et al. 2011, JMLR 12, 2825; Hunter 2007, CSE 9, 90 (ADS `2007CSE.....9...90H`);
   Ginsburg et al. 2019, AJ 157, 98 (ADS `2019AJ....157...98G`, arXiv:1901.04520). **All four
   entries already carried the correct values — no bibliography text changed.** The `\TODO`
   was replaced with a verification statement naming the ADS bibcodes.
2. **Acknowledgements.** Replaced the placeholder with: the DESI DR1 standard
   funding/land acknowledgement (verbatim match to the sister P3-ApJS paper's, which uses
   the same DESI DR1 release); SIMBAD/NED/VizieR service acknowledgements; a compute-cost
   acknowledgement (GPU scan stage ≈$1.31 on RunPod, CPU assembly stage <60 s at $0); and
   the lab's standard AI-assisted-methodology disclosure paragraph (no vendor names, to stay
   clear of the directive-G leak-gate's `ChatGPT|Gemini|Grok` pattern — matches the
   `DISCLOSURE_PAT` exemption via the phrase "cross-checking and adversarial").

**Still open (2/4), correctly left open (need Houston or new GPU compute, not something an
agent lane should silently fabricate):**

- **Zenodo DOI** for the public deposit — not minted.
- **OT-1 selection function** (completeness/purity for this model–substrate pair) — does not
  exist; requires GPU compute. The paper is explicit that no population-level claim depends
  on it (§"What this catalogue is not").

**Hygiene (directive G):** `\paperVersion` vAF.0.2→vAF.0.3; `\paperTimestamp` unchanged
(September 19, 2026 — same day). 4-pass `pdflatex`, 0 errors, 0 undefined refs/citations, 0
overfull hboxes >10pt, 15 pages (unchanged). `pdftoppm -r 110` full render of the three
touched pages (acknowledgements, Appendix A software section, bibliography) — no overflow,
no overlap.

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `078505552a563eccee07ddd7ca81e811`, SHA-256
  `d85487e97f6856040d12ef78b78ab57ce4d74fc6420d6664013cdc9651c17b41`.
  Mirrored byte-identically to `site/public/papers/anomaly_flagship_vAF.0.3.pdf`,
  `site/public/papers/anomaly_flagship.pdf`, `public/papers/anomaly_flagship_vAF.0.3.pdf`,
  `public/papers/anomaly_flagship.pdf`.
- **Convex:** `paperVersions:bump` id `k579zbnetq62twebstgy1gq64h8epgq3` read back verified.
- **Git:** commit `f7e85cd3` (tex + pdf + mirrors + draft_paper_registry.json);
  `project-context/paper_registry.json` companion-manuscript registration and campaign-log
  lines landed inside lane L7c's `4bad8124` (shared git-index hazard — staged alongside
  L7c's own files at commit time; content verified intact post-commit, nothing lost).

## R1 INT board — dispatch notes (superseded by "R1 INT board closed" above)

Review profile: `ApJS-CATALOG` (the closest existing lab profile — a catalogue + method
paper with a large public data product; no dedicated "anomaly catalogue" profile exists
yet in `tools/v3_native_pdf_review.py`'s profile table, so `ApJS-CATALOG` was reused
as-is). Focus questions given to every leg, drawn from the draft's own honest
self-assessment: (1) does the title carry the null/no-discovery framing overtly; (2) is
the blue-spectrograph-arm result's instrumental-vs-astrophysical origin argued
convincingly; (3) is the recovery-benchmark's low statistical power stated strongly
enough in the abstract, not just the body. All three were confirmed real findings — see
DAF-07, DAF-09/10/11, and DAF-12 above.

The Claude leg reviewed the exact vAF.0.2 PDF (sha8 `b972d890`) while Grok/Gemini reviewed
the exact vAF.0.3 PDF (sha8 `d85487e9`) — the only difference between those two versions
is the acknowledgements section and one Appendix-A bibliography-verification sentence; no
science content differed, so this was not a scope mismatch for any of the three focus
questions. The Grok+Gemini dispatch was blocked twice by `tools/bigbounce_preflight.py`'s
shared-checkout clean-tree gate (other concurrent lanes' files, not AF's own — PSU and
site-data files mid-edit); retried successfully once those lanes committed. Also
discovered and fixed in the same session: `tools/verify_pdf_mirror_integrity.py`'s
`served_pdf_policy.immutable_archive_name_patterns` regex rejected AF's letter-only
version-token naming (`vAF.0.2` has no leading digit, unlike every other paper's
`v4P.0.9`/`v3M.0.26`/`v1S.0.11`/`v1N.0.6`) — widened non-breaking in
`project-context/paper_registry.json` (commit `5566ba9d`) so AF's served mirrors pass the
gate going forward.

## Open gates

- Directive R2: round 1 of 2 spent. A round 2 board is authorized only to verify these
  closures on the exact vAF.0.4 PDF, or if an intervening science/scope decision occurs.
- 3 findings genuinely open (DAF-17 dedup near-threshold sensitivity, DAF-19 taxonomy
  RA-wrap/hyperparameter re-clustering, DAF-20 archived-model training-corpus
  archaeology) — each needs real further work (data analysis, a corrected re-clustering
  run, or historical documentation search) beyond a text-edit closure pass.
- Zenodo DOI, OT-1 selection-function injection-recovery experiment: genuinely open, need
  Houston (DOI minting) or new GPU compute (OT-1).
- Houston sign-off: not sought (readiness 75, below the 95-agent-gate ceiling).
