# Session handoff — 2026-09-03 23:30Z → 2026-09-04 (orchestrator: Fable 5.1, medium; research account)

Supersedes `SESSION_HANDOFF_2026-09-02.md` for state; that file remains the record of
the 09-02/03 work. Canonical truth stays in `SSOT/`, `VISION.md`,
`NEXT_SCIENCE_LEDGER.md`, `PAPER_LINEAGE_2026-08-05.md`.

**State at close:** working tree clean; origin and upstream at `541a5eb5`; 71 commits this
session; pod `8ofv5d4ynu7hku` EXITED (balance $140.56 at stop); no cron/launchd review loop
active (the You.md `com.you.context-sync` agent still auto-commits in this repo — see
Blockers). Live site deployed and verified (v3M.0.10 PDF served, md5 `d3981d8b…`).

## What the session did (science first, per directive R)

| # | Item | Result | Receipts |
|---|---|---|---|
| Phase 3 v2 | Landed, three-way verified (local/B2/HF), recovery benchmark run, pod stopped | 569/1,244 SIMBAD/NED matched (45.7%); 8 families over 675 unmatched; no reference class clears the confirmed-class bar (1 BAL match, 4.2×) | `PHASE3_V2_LANDING_2026-09-03.md`, 38e57851 |
| Ledger #8 | **ANSWERED — DATA RELEASE**, not a paper (pre-declared criterion unmet) | Q1 release document drafted; lineage entry; explorers restated to science-target counts | cfb2f527, 0e9e5b41, 6522fe58 |
| Ledger #7 | **CLOSED — NEGATIVE.** Minimal ECH + Dirac/Weyssenhoff has no parity-odd O(h²) operator; Δ_h structurally k-odd, ≤6e−13 at LISA | March's "single best next theory" reversed with reason | `research/chiral_gw_gate/`, 198f084c…ea5b13eb |
| Ledger #2 second half | **CLOSED AS SCOPED.** Bounce's own cubic term Δf_NL^bounce = −(5/24)ρ_B (S1); f_NL^after ∈ [−0.65, −0.50] across three backgrounds; S2 divergent; Quintin+2015 not contradicted, Agullo+2017 not comparable (scheme-limited, stated) | lanes a/b/c | `research/cubic_bounce_transmission/lane_{a,b,c}_*`, 97ad2ca2, 45658a9f, 1e680272, 521e1d96 |
| A3-2 + monopole adjudication | Bianchi-I separate universe: shear traceless, no monopole; **Fable adjudication: in-in −15/8 correct**, δN computes δN_c = (1−ε/3)ζ, shift class [X] carries the quadrupole and +5/4 monopole; factor-2 quadrupole = re-threading boundary term | ledger #1 amended, method-independent check closed | `research/theory_audit/fnl_{bianchi_separate_universe,monopole_adjudication}_2026_09_03.*`, 866cf342, f3516042 |
| A3-1b | In-lab Δ²_ζ: PBH channel a clean null (7.0 dex short, f_PBH = 0); FIRAS excludes the broadband SMBH-seed amplitude ~1.8e3×; ledger #6 early-SMBH discriminator answered as a null | ratio widened to 1.7–1.9 | `research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.*`, ac530afd |
| Ledger #4 | DESI DR1 PNG reproduction plan (Chaussidon+ 2024 target, ≈64 GB, $0 local, ~1 week); step 1 executed: 0.86 GB QSO v1.5 products, count reproduced to 0.14% | OPEN — execution is a next session's lane | `research/desi_png_reproduction/`, dc19f247, 7594b5bd |
| A3-3 | **CLOSED — VERDICT A.** Lab spectrum at nHz through the validated Kohri–Terada kernel: γ_pred = 5.07, Ω_GW h²(f_yr) = 1.45e−23, 14.3 dex below NANOGrav → PTA channel is a null; γ=3 attribution withdrawn | decision D-A3-3 in lineage | `research/track_a3_multichannel/SIGW_NHZ_NOTE_2026-09-04.md`, a68ac1ec…a638a02c, ab947b2c |
| A3M paper | v3M.0.7 → **v3M.0.10** (13 pp): science-gate results integrated (v3M.0.8); R3 board → truth-audit 19 genuinely-new → closure C1–C10 with **decision C1 = propagate the transmitted amplitude** (v3M.0.9); R4 verification board → 15 real → editorial closure + D-A3-3 (v3M.0.10). Readiness 75. **Rounds STOPPED (R2).** | Track A now: three honest nulls (PTA, PBH, PNG high-z) + one reachable-but-unseparable channel (LSS at f_NL^after; SPHEREx 0.7–0.9σ) | `SSOT/paper-a3m/status.md`, boards/audits under `peer-reviews/INT_v3/`, 742f85e7 |
| Site | Explorers restated; `convex/publicationStatus.ts` canonical list fixed (STALE banner root cause); A3M readiness cap 75 in Convex; skills autolog + 4 skill-improvement entries; freshness PASS; headed QA twice | — | 6522fe58, 597efeb2, b8460550, be4b5bef |

Review rounds this session: A3M R3 (v3M.0.8) and R4 (v3M.0.9), each preceded by a
science decision (science-gate closure; C1). Both allowed under R2; further rounds require
a new science decision (ledger row 9).

## Ledger state (end of session)
1 CLOSED (amended: monopole adjudication) · 2 CLOSED AS SCOPED · 3 first pass + A3-1b/A3-2/A3-3
closed, open A3-4 (r) and A3-1e → row 9 · 4 OPEN, plan + step 1 done · 5 DONE · 6 first test
done, SMBH discriminator null · 7 CLOSED NEGATIVE · 8 ANSWERED (data release) ·
**9 OPEN (new): bounce-scale enhancement at kη_B ~ 1 — the only remaining non-null route for
Track A's PTA/PBH channels.**

## Blockers / notes
- `com.you.context-sync` (launchd) commits in this repo on its own (`context-sync: Mac-1287 …`,
  0b934028, f95aa2be); it swept a review receipt and raws mid-write. Not unloaded (Houston's
  infra). Click-list: decide whether it should skip `bigbounce`.
- Sub-agent stalls: six lanes died on the 600 s watchdog; the anti-stall rules (first commit
  ≤10 tool calls, commit per item, ≤80-line edits, no nested delegation, no Monitor inside
  lanes) are now standing in memory and in the review-timeline skill entries.
- The Sonnet safety classifier timed out twice near the end; the last packaging bundle was
  executed in the orchestrator session step by step (all receipts in `SSOT/paper-a3m/status.md`).
- Phase-3 v2 packed tar (42 MB) was committed to git by a concurrent sweep (v1 precedent
  excluded it); content correct; not reverted.

## Houston's ordered click-list (unchanged items from 09-02 first)
1. Sign-off reads (95 → 100): P4′ v4P.0.5 and ECH Note v1N.0.5 — paste sign-off quotes into `SSOT/paper-4p/status.md`, `SSOT/paper-1n/status.md`.
2. Zenodo new-version DOIs (irreversible): records 21481838 / 21461899 per `SSOT/PORTAL_KITS_2026-09-02.md`; **plus** a Zenodo record for the anomaly-catalogue v2 data release (`pipelines/p3_anomaly_engine/release/ANOMALY_CATALOGUE_RELEASE_v2_2026-09-03.md`, HF `phase3_v2/2026-09-03/`).
3. Endorsement emails (gr-qc → Popławski; astro-ph.GA → Desmond) per `SSOT/ENDORSER_OUTREACH_2026-09-02.md`.
4. Headed-browser reads of PRD/JCAP length limits into the portal kit.
5. arXiv submissions after endorsement; journal portals (CQG Paper; ApJS).
6. Secrets/infra: `HUBIFY_TOKEN` (vault passphrase or `hubify auth login`); confirm retirement of the Codex launchd agents; decide on `com.you.context-sync` for this repo.
7. **New — A3M scope read:** the Track-A paper now headlines a transmission-corrected f_NL^after and three nulls. Read `SSOT/paper-a3m/status.md` v3M.0.10 and the two lineage entries of 2026-09-04 and confirm the framing before any A3M submission step (readiness stays 75 until a science decision on row 9 and a final verification board).

---

## Evening state (2026-09-04, ~19:30 PT)

361 commits since 06:00 today. Science table (rows closed/answered this
session, one line + receipt each):

| Row | Result | Receipt |
|---|---|---|
| 2 | Bounce cubic term closed as scoped; f_NL^after ∈ [−1.25,−0.50] two-scheme band after row 9 | `research/cubic_bounce_transmission/`, `lane9b2_s2_rawadm/` |
| 7 | No chiral GWs from minimal ECH — k-odd super-Hubble suppression, O(ε) in every band | `research/chiral_gw_gate/LEDGER7_CHIRAL_GW_GATE_2026-09-03.md` |
| 8 | Anomaly catalogue → data release (pre-declared benchmark not met) | `pipelines/p3_anomaly_engine/release/ANOMALY_CATALOGUE_RELEASE_v2_2026-09-03.md` |
| 9 | Bounce-scale enhancement at kη_B~1: velocity-dip null, S2 divergence is IBP artefact (raw-ADM finite, factor 2.5 vs S1), ABS operator absent/suppressed on exact LQC modes (2.1–4.4 dex below, PBH null unchanged) | `research/track_a3_multichannel/lane9{a,b,b2,c,c2}_*/` |
| 10 | Model's own r = 16ε = 24 (dust), ~670× above BICEP/Keck; n_s=1 exactly (0.9649 is a w-anchor); r=0.84 withdrawn | `research/track_a3_multichannel/row10_r_ns/` |
| 11 | PBH sign resolved (Choudhury+2025 correct; lab's earlier enhancement an IR-divergent artefact); in-coverage ratio 1.84±0.03; second-order threading map derived (δN_c=(1−ε/3)ζ) | `row11_pbh_residuals/`, `research/theory_audit/threading_map_second_order_2026_09_04.md` |
| 14 | Joint (r,f_NL) no-go: c_s windows disjoint 296×; confirms+strengthens Li+2016 3.8× | `row14_cs_window/` |
| 15 | Curvaton route: n_s inherited, r free, f_NL O(1) but diluted by (r/24)²≈1.5e−6 — cure removes the signal | `row15_curvaton/`, adjudication note |
| 17 | Separate-universe failure criterion spun out as standalone note (paper-su v1S.0.1) | `research/theory_audit/separate_universe_failure_criterion_2026_09_04.*` |

In progress:

| Row | State |
|---|---|
| 4 | DESI DR1 f_NL v3 done (−2.2±25.3, 0.06σ from published); RunPod for own-covariance never came up ($0 spent); wide-angle/pixweight splits open |
| 12 | Preflight + provenance design complete, RunPod balance confirmed funded; pod provisioning deferred to a dedicated pollable session (anti-stall contract disallows unattended Monitor loops here) |
| 13 | Part A at-scale (N=5000, local MPS, $0) done — consistent but underpowered; N=20k script staged; Euclid Q1 domain-adaptation named as pathfinder-only, not yet run |
| 16 | Program row opened 2026-09-04 (full 8.47M dipole, chirality×structure cross-correlations, Euclid Q1); N=20k injection scripts adapted, not yet run |

**Papers.** A3M v3M.0.15 (17 pp): readiness 75, title/abstract reframed
around the joint (r,f_NL) no-go (D-A3-10/D-A3-11); rounds stopped under R2
after v3M.0.10; D-A3-9/10/11 are science decisions, not review rounds, so
one verification board (R7) is now permitted. P4′ v4P.0.5 and ECH Note
v1N.0.5: readiness 95, unchanged, waiting only on Houston sign-off.
namaster-proof/P1B v2B.0.17 (8 pp): novelty lift #3 — reframed around a
verification primitive, blind shortcut-detection test 12/12 detected, 0%
false positives, N3-candidate claim recorded (pending an external referee
board). paper-su v1S.0.1 (4 pp, new): "When the separate universe fails,"
readiness 40, draft only — no INT/EXT board has run yet. Anomaly catalogue
v2: data release, 1,244 science-only targets, 8 taxonomic families, Zenodo
DOI still Houston's click.

**Site.** The full six-lane redesign (`project-context/site-redesign/2026-09-04/REDESIGN_SPEC.md`)
shipped: shell primitives (Band/PageHeader/StatRow/EvidenceChip/RowList/
DataTable), `/research` (tracks-as-spine) + `/papers` (flat works index),
paper template + figures + `/predictions`, `/status` as a calm readiness
dashboard + simplified `/reviews` + `/publish`, `/reproduce` hub, `/learn`
cluster + explorer wrappers, a "started from one question" positioning
band on the homepage and `/research` header, contribution-type + novelty-
tier labels per the novelty audit. `tools/site_freshness_check.sh` and
`reviewTimeline.ts` contracts preserved; explorer root `.html` files
untouched (still canonical). Live headed-browser QA of the redesign is
still owed before calling it fully verified.

**Process notes.** A provider rate-limit outage 18:04–18:41 PT killed four
concurrent Agent lanes; one orphaned RunPod pod was found and terminated
at $0.29 spend. `com.you.context-sync` (launchd) continued auto-committing
in this repo through the session — expect HEAD to move between checks.
Anti-stall rules (first commit within ~10 tool calls, commit per item,
≤80-line edits, no nested delegation, no Monitor inside a lane) held for
every lane that finished; they are standing in `NEXT_SESSION_PROMPT` and
memory.

**Updated ordered click-list for Houston (supersedes the 09-02 list above
where items overlap):**
1. Sign-off reads (95 → 100): P4′ v4P.0.5 and ECH Note v1N.0.5 — paste
   sign-off quotes into `SSOT/paper-4p/status.md`, `SSOT/paper-1n/status.md`.
2. Zenodo DOIs (irreversible): records 21481838/21461899 (P4′/ECH Note per
   `SSOT/PORTAL_KITS_2026-09-02.md`); the anomaly-catalogue v2 data release
   (`pipelines/p3_anomaly_engine/release/ANOMALY_CATALOGUE_RELEASE_v2_2026-09-03.md`);
   and namaster-proof/P1B per §5 of
   `pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md`
   (Zenodo upload, then an ASCL entry at ascl.net/code/submit once the DOI
   exists).
3. Endorsement emails (gr-qc → Popławski; astro-ph.GA → Desmond) per
   `SSOT/ENDORSER_OUTREACH_2026-09-02.md`.
4. A3M framing read: after R7 closes, re-read `SSOT/paper-a3m/status.md`
   v3M.0.15 and confirm the joint (r,f_NL) no-go framing before any A3M
   submission step.
5. `HUBIFY_TOKEN` (vault passphrase or `hubify auth login`) — still blocks
   the manifest importer / hubify parity check.
6. `com.you.context-sync` decision for this repo — it keeps auto-committing
   mid-session; decide whether to exclude `bigbounce`.
7. RunPod spend approvals: row 16 full-parent dipole run after the 20–50k
   injection lands (~$60 estimate); row 12 full 1M-spectrum DR1 pilot
   (~$50) and, if that succeeds, the full DR1 SSL pass (~$300).

---

## Late-evening state (2026-09-04, close)

**Paper table.**

| Paper | Version | Readiness | Boards | Status |
|---|---|---|---|---|
| A3M | v3M.0.19 | 75 | R3–R8 (R3 c1-10, R4 15 real, R7 16 items closed, R8 18 items closed) | ROUNDS STOPPED (R2); five consecutive verification rounds found no physics/numerical error — only row-19 general-λ was Houston-gated, now answered (no-go generalizes to all P(X) k-essence, min r=12.57, 349× BK18) |
| P1B (namaster-proof) | v2B.0.19 | 95 | R1 (23 findings, 21 genuinely-new-real, batch-2 pre-registered blind test integrated), R2 (statistics-presentation fixes) | ROUNDS STOPPED (R2) pending batch 3 / OTS confirmation / PyMaster cross-check; OTS Bitcoin-anchor pending confirmation |
| paper-su | v1S.0.3 | 65 | R1 (framing decision D-PSU-1: reframed "failure" → "computes a different variable + criterion"), R2 (E-1..E-11 closed) | ROUNDS STOPPED pending S6–S11 / venue decision |
| P4′ / ECH Note | v4P.0.5 / v1N.0.5 | 95 | — | unchanged; waiting on Houston sign-off quotes only |
| Anomaly catalogue v2 | — | — | — | data release documented; Zenodo DOI is Houston's click |

**Science ledger — rows answered today (one-line results).**
- **Row 9** (bounce-scale enhancement, A3-1e): ANSWERED — no mechanism reopens PTA/PBH; S2-scheme raw-ADM gives a finite two-scheme band (f_NL^after ≈ −1.25 S2 vs −0.50 S1, factor 2.5); exact LQC-dust modes show no enhancement.
- **Row 10** (model's own r, n_s): CLOSED — r=24 exactly (matter-bounce identity, bounce-invariant to 8e-5), ~670× above BICEP/Keck; n_s=1 exactly (0.9649 is an anchor, not a prediction); r=0.84 WITHDRAWN as a P2 bispectrum-overlap conflation.
- **Row 11** (PBH residuals): (a) RESOLVED — Choudhury+2025's negative-f_NL-suppresses sign is correct, the lab's earlier enhancement was a cutoff artefact; (b) CLOSED — 255-pt γ_cr scan, ratio 1.84±0.03 holds in-coverage only; (c) DERIVED — exact δN_c threading map.
- **Row 14** (joint r/f_NL vs c_s): CLOSED — NULL, kill condition met. r=24c_s exactly; r<0.036 needs c_s<1.5e-3 giving f_NL^after ~6e5-9e5 (~1e5σ over Planck); conversely |f_NL|≤5.1 needs c_s≥0.444 (r≥10.7) — windows disjoint by 296×. Confirms + strengthens Li+2016's no-go 3.8×.
- **Row 15** (curvaton route): CLOSED — partial pass. n_s inherited unchanged (0.9649); r is free via r_dec; f_NL is O(1) and Planck-compatible for r_dec∈[0.113,1] — but the flagship −35/16 dilutes to (r/24)²≈1.5e−6 at the tensor-viable r, below SPHEREx reach. Net with row 14: every cure for r either blows up f_NL (c_s) or dilutes it away (curvaton) — matter bounce is un-diagnosed by f_NL, not excluded by it.
- **Row 17** (separate-universe failure criterion, paper-su): OPEN → spun into standalone note; R1 board (Fable major-revisions, Grok REJECT, Gemini major-revisions) truth-audited, gates S1/S2/S3 resolved, decision D-PSU-1 reframed the claim; now at v1S.0.3, rounds stopped pending venue.
- **Row 18** (S2-scheme tensor transfer + c_s-dependent bounce cubic term): DONE both lanes — (a) tensor no-go is scheme-independent (r_after^S1=24.0, r_after^S2=9.37e2, both excluded); (b) Δf_NL^bounce(c_s) generalized, moves the no-go boundary to c_s≥0.600 (r≥14.4, 400× BK18) — strengthens, not relaxes.
- **Row 19** (general-λ k-essence no-go): DONE — no-go generalized to all P(X); λ is exactly r-independent and Δf_NL^bounce-independent in S1; scan over λ/Σ∈[−1,1] + Li/DBI lines gives min r=12.57 (DBI, c_s=0.524), 349× BK18. The v3M.0.18 "λ=s=0" qualifier is dropped.

**Rows still open.**
- **Row 4** (DESI f_NL reproduction): ledger #4 v3 — official DESI-collaboration window/P_ell/EZmock-covariance products downloaded and used directly (higher-fidelity than local reconstruction); flagship f_NL=−35/16 now 0.0007σ from the 2-parameter (b1,f_NL) official-covariance fit (n_shot fixed at 0 after a genuine 3-param degeneracy was found and reported honestly, not hidden). Residuals open: wide-angle terms, systematics splits, own-covariance if RunPod becomes reachable.
- **Row 12** (SSL spectral model, full DR1): OPEN — pipeline built and compiles clean; two pod-boot attempts (RTX 4090 COMMUNITY, RTX 3090 COMMUNITY) both failed SSH within 15 min and were terminated per contract (~$0.27 spent total, no training ran). Two consecutive COMMUNITY-pool SSH failures suggest a pool/networking issue, not a fluke — retry on SECURE-cloud GPU or different region next session.
- **Row 13** (image-level injection + Euclid Q1): OPEN — GPU program proposed to Houston, not yet run.
- **Row 16** (galaxy chirality at scale): OPEN, IN PROGRESS — 20k-sample local injection pilot running on MPS (mps device, ~1.36 img/s, at 12048/20000 done, ETA ~96 min at last check, resumable from scale20k_pairs.parquet); STAGE_SAMPLE_DONE marker present, no final DONE/FAILED marker yet. Full-parent (8.47M) dipole and chirality×environment/anomaly cross-correlations still queued behind it.

**Site.** Redesign remains live (tracks-as-spine /research, flat /papers, calm /status,
works table full-width, contribution-type + novelty-tier labels, "started from one
question" positioning band). No new site-architecture changes tonight beyond routine
readiness/version syncs for A3M/P1B/paper-su. Anomaly data-release page unchanged,
Zenodo DOI still Houston's click.

**Process notes.**
- A provider rate-limit outage (18:04–18:41 PT, carried over from earlier in the day)
  had killed four concurrent Agent lanes; recovery held for the rest of the evening —
  no repeat outage.
- Anti-stall rules (commit within ~10 tool calls, commit per item, ≤80-line edits, no
  nested delegation, no Monitor inside a lane) held for every lane that ran tonight;
  the A3M R3–R8 boards and paper-su R1/R2 all landed via this discipline without a stall.
- RunPod SSH reachability: two independent programs (row 12 SSL pilot, ledger #4's
  own-covariance pod) both hit pods that boot but never become SSH-reachable within
  15–30 min on COMMUNITY-tier GPUs; row 12 burned $0.27 across two attempts, ledger #4's
  pod burned $0 (never rsynced). This is now a standing lesson: prefer SECURE-tier pods
  or a different region before another COMMUNITY-tier attempt; always confirm SSH
  reachability before staging any data transfer.
- Disposition re-derivation gate lesson: row 11's PBH sign "disagreement" turned out to
  be a genuine physics resolution (Choudhury+2025 correct, the lab's own earlier
  enhancement was a cutoff-dependent artefact) rather than a formula mismatch — closing
  a disposition sometimes requires re-deriving the competing claim term-by-term, not
  just re-running the lab's own code.
- `com.you.context-sync` (launchd) continued auto-committing in this repo through the
  evening ("context-sync: Mac-1287 …" commits interleaved with review-lane commits);
  expect HEAD to move between checks — always re-read HEAD before trusting a receipt.

**Updated ordered click-list for Houston.**
1. Sign-off reads (95 → 100): P4′ v4P.0.5 and ECH Note v1N.0.5 — paste sign-off quotes
   into `SSOT/paper-4p/status.md`, `SSOT/paper-1n/status.md`.
2. Zenodo DOIs (irreversible): records 21481838/21461899 (P4′/ECH Note); the anomaly
   catalogue v2 data release; namaster-proof/P1B per §5 of
   `pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md` (Zenodo upload, then
   an ASCL entry at ascl.net/code/submit once the DOI exists).
3. namaster-proof/P1B ASCL/Zenodo kit finalization per the same §5 (packaging steps
   written, DOI minting is the Houston-only step).
4. Endorsement emails (gr-qc → Popławski; astro-ph.GA → Desmond) per
   `SSOT/ENDORSER_OUTREACH_2026-09-02.md`.
5. **A3M framing read (now a MUST-READ before any A3M submission step, upgraded
   tonight):** after the no-go generalized to all P(X) k-essence (row 19, v3M.0.19),
   re-read `SSOT/paper-a3m/status.md` v3M.0.15→v3M.0.19 sections in full and confirm the
   joint (r,f_NL) no-go + curvaton-dilution framing before submitting.
6. paper-su venue choice (readiness 65, rounds stopped pending S6–S11/venue).
7. `HUBIFY_TOKEN` (vault passphrase or `hubify auth login`) — still blocks the manifest
   importer / hubify parity check.
8. `com.you.context-sync` decision for this repo — it keeps auto-committing
   mid-session; decide whether to exclude `bigbounce`.
9. RunPod spend approvals, contingent on pod reachability: row 16 full-parent (8.47M)
   dipole run (~$60 estimate) once the 20k local injection pilot finishes; row 12 full
   1M-spectrum DR1 pilot (~$50) and, if that succeeds, the full DR1 SSL pass (~$300) —
   only once a pod is confirmed SSH-reachable via public IP or the ssh.runpod.io proxy.

## Wave-2 close (2026-09-05 early, PT)

HEAD at close: `35d706f5` (595 commits since 06:00 today — high auto-commit/lane volume,
`com.you.context-sync` included).

| Item | Result | Receipt |
|---|---|---|
| Row 4 (DESI PNG) | v4 confirms v3: p-marginalised f_NL=-1.648, σ~19; wide-angle + 3 imaging splits (E(B-V)/stellar/depth) all null at official-covariance fidelity (\|Δ/σ\|<0.6); WEIGHT_SYS + galactic-latitude re-test at official fidelity still OPEN | `research/desi_png_reproduction/LEDGER4_RESULT_v4_2026-09-04.md` |
| Row 12 (SSL pilot) | NOT LANDED — both COMMUNITY-tier RunPod attempts (RTX 4090, RTX 3090) failed SSH within 15 min each; terminated per contract; $0.27 spent; no staging/training ran | `pipelines/p3_anomaly_engine/ssl_pilot/ROW12_PILOT_2026-09-04.md` |
| Row 16(i) full-parent dipole | Non-null on 3.2M full parent (z=+4.44), axis-shifted 295° from strict subset | `ROW16I_FULL_PARENT_2026-09-04.md` |
| Row 16(ib) axis-shift follow-up | VERDICT: SYSTEMATIC — primary_hc cut alone drops it to z=+0.68, dropping DES leg alone to z=+0.48, axis unstable ~100° across QC cuts, mask-leakage sim leaks 0.19% alone. Closed as null; P4′ paragraph drafted | `ROW16IB_AXIS_SHIFT_2026-09-04.md` |
| Row 16(iv) chirality×structure | 15/17 pre-registered stats run, all null vs spiral density, anomaly positions, redshift, CMB axes; free-fit dipole 0.44% below its own null | `ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md` |
| Row 13 pilot Part A (N=20k) | Pixel-level calibration resolved: measured slope +0.0167±0.0089 vs naive identity ~47σ off, vs mixture-corrected identity ~2.9-3.0σ (real, not noise-floor) | `pipelines/p4prime_chirality_test/injection_pilot/ROW13_PILOT_2026-09-04.md` |
| Row 15b entropy sector | Spectator/tensor transfer identical (scheme-independent to 7e-4); F_eff≥25.82 both schemes; viability condition pre-bounce, curvaton potential itself still not derived | `research/track_a3_multichannel/row15b_entropy_sector/ROW15B_ENTROPY_SECTOR_2026-09-04.md` |
| PSU gates S6-S11 | S6 RESOLVED, S8 RESOLVED, S7 NOT (uniform-factor-2 lit check pending), S9/S10 PARTIAL (second-order kernel K_c open), S11 NOT (Zenodo upload is Houston-only) | `research/theory_audit/psu_gates_S6_S11_2026_09_04.md` |
| P4′ paper | v4P.0.6 — row-16 disclosure integrated (full-parent non-null + systematic verdict); readiness unchanged at 95 | `project-context/SSOT/paper-4p/status.md` |

**Click-list delta:** P4′ sign-off read must now use v4P.0.6 (not v4P.0.5); A3M framing
read stays v3M.0.19 (unchanged); paper-su venue decision still open; namaster-proof
ASCL/Zenodo packaging still Houston-gated; RunPod public-IP/SECURE-tier pod approval
still needed for the row-12 pilot (did not land tonight — two COMMUNITY-tier attempts
both failed SSH).

**Row 12 addendum (2026-09-05 early):** third attempt failed the same way even on SECURE cloud
with the corrected `ports`/`supportPublicIp` schema (pods created, runtime never up; ~$0.32
spent; no strays). The launch scripts are fixed and committed (68b403a6); the pilot pipeline is
ready. **Click-list addition:** create a GPU pod through the RunPod web UI (as the working
phase-3 pod was; see `pipelines/p5_desi_chirality/env_finder/LAUNCH_POD.md`) and hand the
agent its SSH coordinates; the agent then runs `launch_row12_pilot.sh` unchanged.

## Wave-3 close (2026-09-05 morning PT)

| Item | Result | Receipt |
|---|---|---|
| namaster-proof v2B.0.20, batch 3 | Attempt 1 ABORTED (invalid harness: `pcl.make_map` ignored its `seed`, so the new `pseudo_cl` instrumentation described a different random map than the run analysed) — disclosed, preserved under `public3_aborted/`, not deleted. Attempt 2, after the harness fix (`variants3.seed_rng`, committed before the new key was drawn): R7 flags S1/S2/S3/S6 6/6, S4b cross-run disjunct 4/6 + reference disjunct 2/6 (6/6 flagged), honest false-positive 0/6, S5 (informed forger) escapes 0/6 as pre-declared. PyMaster (NaMaster) cross-check: in-house MASTER estimator agrees with PyMaster to machine precision (mode-coupling matrix ≲5e-13, decoupled bandpowers ≲2e-12). OpenTimestamps: batch-1/2 stamps now `ots upgrade` to "Timestamp complete" (Bitcoin block-header attested); batch-3 stamp submitted, pending. Novelty tier set to **N3** per decision D-P1B-1. | `pipelines/namaster_proof/blind_test/BATCH3_ABORT_NOTE.md`, `pipelines/namaster_proof/blind_test/public3/scorecard.json`, `pipelines/namaster_proof/PYMASTER_CROSSCHECK_2026-09-05.md`, `pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md`, `project-context/PAPER_LINEAGE_2026-08-05.md` (D-P1B-1) |
| paper-su v1S.0.4 | S7 literature gate LOCATED and CLOSED: Cai, Xue, Brandenberger & Zhang (2009) Eq. (37) is the correct squeezed shape function (= sum of their Eqs. 27–32 = Li, Quintin, Wang & Cai (2017) Eq. 4.19 at c_s=1); their printed Eqs. (38)–(41) and Fig. 5 are uniformly 2x Eq. (37) in every configuration, so the correct isoceles amplitude is −35/16, not −35/8. Li et al.'s −35/16 is an independent general-(ε,c_s) derivation coinciding with Cai's at ε=3/2, not a reuse of Cai's rows. Literature-statement correction only, not a new review round; rounds stay STOPPED under directive R2; readiness held at 65. | `research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.md`, `project-context/SSOT/paper-su/status.md` (v1S.0.4 section) |
| A3M v3M.0.20 | Same S7 correction applied to Sec. IV.B ("The Cai et al. factor of two"): the factor-of-two slip is uniform across Cai et al. Eqs. (38)–(41) and Fig. 5, downstream of the correct Eq. (37), not narrowly Eqs. (38)–(40) as previously stated. Literature-statement correction only; ROUNDS STAY STOPPED (directive R2); none of the open (ii)-ledger items (A3-S2r, A3-cs-bounce, A3-ns, A3-dN, DESI-4) touched; readiness held at 75. | `project-context/SSOT/paper-a3m/status.md` (v3M.0.20 section) |
| Ledger #4 v5 | Full 5-row systematics table on one convention (E(B-V), stellar density, Galactic depth z-band, WEIGHT_SYS on/off, Galactic latitude), all at official-DESI-window + official-EZmock-covariance fidelity. Three imaging-property splits stay null (\|Δ/σ\|<0.6, unchanged from v4). **WEIGHT_SYS on/off confirmed a real, large, necessary effect** — −4.31σ raw / −3.05σ √2-corrected, crossing the 2σ flag even after the conservative correction; not evidence against the headline f_NL (every published DESI QSO f_NL result, including this lab's headline fit, already applies WEIGHT_SYS). Galactic latitude split is marginal (−1.78σ raw / −1.26σ corrected) — flagged as a watch item, not dispositioned as a null. Headline f_NL unchanged (p=1.6: −2.169±25.3; p=1.0: −1.127±13.1; p-marginalised: −1.648, σ~19.2). | `research/desi_png_reproduction/LEDGER4_RESULT_v5_2026-09-04.md`, `research/desi_png_reproduction/outputs/systematics_table_v5.json` |
| Row 16 (iv-b) BGS environment | NULL, at the pre-registered threshold, in both subsets. Genuine external tracer field (DESI DR1 BGS_BRIGHT-21.5, 300,043 galaxies, 4 randoms/cap) replaces item (iv)'s projected self-proxy for the spec-z subset. Spec-z 3D (N=121,417): χ² trend z=-0.06, p=0.952 (rotation null p=0.917). Projected (N=949,584): χ² trend z=-1.51, p=0.084 two-sided; largest excursion is the projected node-like f_CW, z=+2.96, p_local=0.0060, p=0.084 after the pre-registered x14 Bonferroni correction — below the 3σ post-look-elsewhere detection bar. Integrated into P4′ v4P.0.7. | `pipelines/p4prime_chirality_test/chirality_structure/ROW16IVB_BGS_ENVIRONMENT_2026-09-05.md`, `project-context/SSOT/paper-4p/status.md` (v4P.0.7 section) |
| Row 12 (SSL pilot) | Still BLOCKED. Third RunPod launch attempt (SECURE cloud, corrected `ports`/`supportPublicIp` schema) failed the same way as attempts 1–2 (COMMUNITY-tier): pods created, runtime never came up SSH-reachable within the 15-min contract window. Launch scripts fixed and committed; pipeline ready to run unchanged the moment a pod is reachable. Blocker is now explicitly a RunPod **web-UI pod creation** step (API-side pod creation is the suspect), not a script defect. | `pipelines/p3_anomaly_engine/ssl_pilot/ROW12_PILOT_2026-09-04.md`, `pipelines/p5_desi_chirality/env_finder/LAUNCH_POD.md` |
| P4′ paper | v4P.0.6 → v4P.0.7 (row-16 iv-b BGS environment result); readiness unchanged at 95 | `project-context/SSOT/paper-4p/status.md` |

**Click-list update (supersedes the wave-2 list above):**
1. **P4′ sign-off read** (95 → 100) must now use **v4P.0.7** (not v4P.0.6) — paste sign-off
   quote into `SSOT/paper-4p/status.md`.
2. **RunPod web-UI pod for row 12** — create a GPU pod through the RunPod web UI (as the
   working phase-3 pod was; see `pipelines/p5_desi_chirality/env_finder/LAUNCH_POD.md`) and
   hand the agent its SSH coordinates; the agent then runs `launch_row12_pilot.sh` unchanged.
   API-side pod creation is now the confirmed suspect across three attempts.
3. **paper-su venue** decision (readiness 65, rounds stopped; S7 now closed, S8 numerical
   USR validation fund-vs-hold decision still open).
4. **namaster-proof ASCL/Zenodo** with the N3 justification — batch-3 attempt-2 scorecard
   (R7/S6/S4b/FP all as predicted) plus the PyMaster cross-check and OTS batch-1/2
   "Timestamp complete" status are the closing evidence for the packaging kit; DOI minting
   remains the Houston-only step.
5. **A3M framing read** — v3M.0.20 (S7 correction; unchanged science, rounds stay stopped).
6. Zenodo DOIs, endorsement emails, `HUBIFY_TOKEN`, `com.you.context-sync` decision — carried
   forward unchanged from the wave-2 list above.
