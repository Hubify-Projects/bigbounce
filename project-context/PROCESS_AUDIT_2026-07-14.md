# Process Audit — bigbounce review loop (2026-07-14)

Successor to `ACCELERATION_LOG_2026-07-10.md` (tooling round 1+2) and
`REPEATED_ASKS_AUDIT_2026-07-11.md` (repeated-human-reminder class map). Those
two audits are **not duplicated here** — this doc cross-references them and
covers the *new* failure surface that emerged across the M20→M36 wave block of
2026-07-13/14, plus a current honest read of where the program actually stands.

Sources mined: `git log` M20→M36 (commits `f8339c16`…`3d8f3b6d`); the canonical
scistack `bigbounce-r-round/SKILL.md` dated lessons (2026-07-13/14 block, L603–734);
`EXT_real/H17_2026-07-10/manifest.jsonl` (280 rows); the M30–M34 truth-audits.

---

## 1. Executive summary — where the program actually is

**Content is converged.** Across the M-wave block (~M9 → M36, roughly 15+
adjudicated waves) every reviewer finding on every paper has truth-audited to
either a source-cited standing disposition (`DISPOSITIONS/<P>.md`), an
OPEN-COMPUTE item, or an honestly-disclosed scope limitation. Genuinely-new
*real* defects now surface at roughly **1 per ~10 waves** — the P2 orbit-count
narrative sign/stale-BF cluster and P5's DP5-26 artifact-ID descriptor were the
last two, both **closed with real edits and verified held** on re-test
(P2 v1.7.112; P5 v0.1.127, streak recrossed the two-clean-waves bar at M31/M34).
No new real defect has appeared in the M33/M34/M35 legs.

**The residual gap is not a content gap — it is the pattern-066 verdict-word
floor on LLM referees.** The same byte-identical PDF draws ACCEPT→MINOR→MAJOR→MINOR
from Grok and REJECT↔MAJOR from ChatGPT across consecutive waves with zero
content change (§3 below). More text waves do not move the verdict word — this is
measured, not asserted.

**Honest levers left** (all Houston-gated or thin):
1. **Venue / human-referee routing** — the only lever that has *measurably*
   moved verdict words (P3 ApJS flip is proven; P4 Grok-EXT ACCEPT at M21/W1).
2. **A thin open-compute tail** — P4 image-level classifier injection +
   per-pixel confusion + generative null; P2 channel-native Fisher + Zenodo DOI;
   P3 held-out re-inference; P5 Zel'dovich RSD reconstruction; P1U regulated NJL
   gap equation. Each is a real computation, not a text edit.

Directives K (two-clean-waves checkpoint) and M (all-A grid terminal criterion)
both hold: the checkpoint is proven repeatedly; the terminal criterion is gated
on the two levers above, which only Houston can pull. The loop's job now is to
**keep measuring** (never to farm verdicts) and to ship the open-compute tail.

---

## 2. Failure-class catalog — every recurring blocker of the M20→M36 block

Each class: symptom → root cause → occurrences → the mechanical kill now in
place (sha-cited) → residual risk. Classes (a)–(e), (g), (h) are **root-fixed in
committed tooling**; (f) is adjudicator-layer only with harvest-layer hardening
in progress this same cycle; (i)–(l) are operating realities managed by
protocol, not fully killable in code.

### (a) ChatGPT URL-capture race — stale-URL captured as the leg's chat
- **Symptom:** M25 recorded P5+P2 ChatGPT rows both pointing at the P4 M24 chat
  URL — the manifest attributed two legs to the wrong (prior) conversation.
- **Root cause:** when fresh-chat navigation silently fails the tab still sits on
  the *previous* leg's `/c/` URL; the `/c/`-polling loop accepts it instantly.
- **Occurrences:** M25 (P5, P2). Also the earlier 2026-07-11 project-page race.
- **Kill:** `3fb1ffd9` — `ext_submit.sh` captures `PRE_URL` before send and only
  accepts a `/c/` URL that **differs** from `PRE_URL`; if none appears in the
  window and `PRE_URL` was a chat, it dies `FAILED-badurl` instead of recording.
- **Residual risk:** low; interacts with (c) redirect latency — the die window
  had to be widened (see (c)).

### (b) Silent-exit under `set -e` — leg orphaned with no OK/FAIL/manifest row
- **Symptom:** ChatGPT legs printed `chatgpt send: sent-testid` then the script
  exited with NO poll WARN, NO manifest row, NO OK, NO FAIL — leg orphaned.
- **Root cause:** `submit_*` signals real failure only via `die()`. The success
  arm's `[ "$SUBMIT_URL" = "$PRE_URL" ] && die` short-circuits to rc 1 on the
  *normal* (URLs-differ) path; because `case … submit_chatgpt … esac` is a
  top-level statement, that leaked non-zero status tripped `set -euo pipefail`
  and aborted the script *before* the shared manifest-append + OK/FAIL block ran.
  The `02d68a8f` poll/fallback patch made this reachable on the ordinary path.
- **Occurrences:** introduced by `02d68a8f`, hit on M30 legs.
- **Kill:** `a08dd750` — guard the dispatch (`esac || true`) so a benign trailing
  status never trips `set -e` (a real `die`/`exit` is not swallowed by `|| true`);
  `SUBMIT_URL=""` initialized before dispatch. Flow now ALWAYS terminates in
  exactly one of {OK + verified fresh `/c/` row} or {explicit FAIL + non-zero}.
- **Residual risk:** low — the general rule (isolate a `die`-only function from
  `set -e`) is documented in SKILL.md.

### (c) Redirect-latency misdiagnosed as rate limit
- **Symptom:** three consecutive ChatGPT probe "failures" attributed to a daily
  rate limit; the loop deferred legs it should have harvested.
- **Root cause:** the sends **landed server-side as completed reviews**;
  ChatGPT's project→`/c/` redirect simply became slower than the 30s poll, so the
  stale-URL guard (a) died on legs that had actually succeeded.
- **Occurrences:** M26/M27 ChatGPT deferrals (`ef9dbf62`, `b538a4db`),
  three-probe streak diagnosed at M30–M33.
- **Kill:** `02d68a8f` — poll 30s→120s + sidebar-chat fallback (detect liveness
  by *content* — a sidebar chat containing our prompt — not only tab-URL change);
  recovered orphaned legs `harvested-recovered`. Plus the standing **headed
  read-only diagnostic rule**: after ~2 repeated infra failures with an assumed
  cause, look at the actual page before accepting the hypothesis.
- **Residual risk:** low; latency itself is irreducible, now hidden by the wider
  poll + content-based liveness.

### (d) OK-with-empty-URL — leg recorded successful with no chat URL
- **Symptom:** a leg banked as OK but with an empty `SUBMIT_URL`, producing an
  unverifiable "success" row.
- **Root cause:** the post-dispatch OK path did not assert a non-empty URL.
- **Occurrences:** surfaced in the M34 re-ride hardening.
- **Kill:** `80914698` — `ext_submit dies instead of recording OK with empty URL`.
- **Residual risk:** low.

### (e) Wrong-PDF attach (×2) — a leg reviewed a different paper
- **Symptom:** M32/M34 `P3APJS chatgpt` legs attached the WRONG pdf — one raw was
  byte-identical to a P1U review, one carried a P5 signature.
- **Root cause:** both misfires were ChatGPT legs *following* other ChatGPT legs
  in a chain; the upload grabbed a **stale attachment chip** from the prior leg
  still lingering in the composer, and the chip poll only confirmed *some* chip
  existed — never that the chip's FILENAME matched this leg's staged file.
- **Occurrences:** M32 (P3-ApJS→P1U signature), M34 (P3-ApJS→P5 signature);
  the M32 leg was caught and recorded INVALID (`a32aa91a`).
- **Kill:** `854acb99` — after upload, before send, poll a **composer-scoped** DOM
  query for a chip whose visible text contains the exact round token
  `ext_${PAPER}_${ROUND}`; on mismatch/absence remove + re-upload once, re-verify;
  else `die "wrong/missing attachment"`. Applied to both chatgpt AND grok flows.
  Live-tested on the real re-ride `P3APJS chatgpt M36` (token verified, sent,
  fresh `/c/` captured).
- **Residual risk:** low for the token-verified path. Recovery of a landed-but-
  orphaned wrong-attach leg still requires enumerating same-era chats and matching
  on the attachment token (titles don't disambiguate same-venue papers).

### (f) Harvest trusting labels — a leg's raw not sanity-checked before verdict
- **Symptom:** legs whose raw was a prompt-echo stub, a 0-byte file, or a
  misfiled other-paper raw were provisionally label-trusted; only the
  adjudicator's directive-I4 read caught them.
- **Root cause:** the harvest layer records a manifest row from the leg *label*;
  the raw-content sanity check lives one layer up, in the Opus adjudicator.
- **Occurrences:** M30 P1U grok = prompt-echo raw → verdict:failed per I4
  (`34c1eb4e`); M32/M34 misfiled raws (see (e)); assorted 0-byte legs.
- **Kill (current):** adjudicator-layer directive-I4 — every raw + screenshot is
  READ verbatim before any verdict is recorded; a leg with no reviewer output is
  FAILED, never a verdict. **Harvest-layer hardening is in progress THIS audit
  cycle** (a raw-sanity gate: min-length + prompt-echo detection + paper-signature
  provenance check at harvest time, so the failure surfaces one layer earlier —
  see §4).
- **Residual risk:** MEDIUM until the harvest-layer gate lands — today it depends
  on the adjudicator being diligent; that's a human-in-the-loop guarantee, not a
  mechanical one.

### (g) `post_verdict` cap-recompute stale-order + `record_wave` clobber
- **Symptom:** wrong readiness caps (P5 80→74 ×2, P1U 68→62, P4 80→74) and rich
  multi-reviewer wave rows overwritten to a single verdict with streak zeroed —
  both hand-corrected by adjudicators for ~8 rounds.
- **Root cause (BUG-1):** latest-per-reviewer selection took the FIRST row in
  `externalReviews:list`, assuming datestamp-descending order; the list is not
  reliably sorted and rows share a `receivedAt` string, so the tie-break landed
  on an OLDER verdict. **(BUG-2):** `readinessMetrics.recordWave` is a full patch;
  `post_verdict`'s auto call knew only one verdict and defaulted streak/open to 0,
  clobbering an existing rich wave row.
- **Occurrences:** ~8 rounds of manual cap correction; observed live on
  P5/P1U/P4 caps and M18 P2/P1U streak clobbers.
- **Kill:** `cd02c991` — select strictly by Convex `_creationTime` DESCENDING
  (the only monotonic write-order signal); `record_wave` guard queries
  `listWaves` first and SKIPS the auto call when a non-empty-verdict row already
  exists (orchestrator's own `record_wave.sh` stays authoritative writer).
- **Residual risk:** low; validated live (P1A recomputes to the known-correct 68).

### (h) INT/EXT reviewerLabel collision — INT leg displaces the EXT cap row
- **Symptom:** the P2 EXT-derived cap silently polluted when an INT-Grok MAJOR
  displaced the EXT-Grok MINOR row.
- **Root cause:** the cap formula selects the `_creationTime`-latest row PER
  reviewerLabel; an INT API leg posted under the bare EXT label ("Grok")
  overwrote the EXT row.
- **Occurrences:** M19 P2-INT adjudication.
- **Kill:** `029cb689` + the standing convention — INT legs post as
  `<wave>-INT-<vendor>` (e.g. `M19-INT-xAI`); EXT labels stay bare.
- **Residual risk:** low, convention-enforced; depends on the poster using it.

### (i) Dead chats / rate-limit realities
- **Symptom:** FAILED-dead / DEFERRED-ratelimit legs (manifest: 15 FAILED-dead,
  4 FAILED-upload-throttle, 3 DEFERRED-ratelimit, 5 FAILED-upload, 2 FAILED-badurl,
  1 each FAILED-nourl/url-lost/collision).
- **Root cause:** reviewer-UI generation latency (10–40 min/leg for thinking
  modes), Gemini browser hard-throttle, ChatGPT Cloudflare/redirect behavior —
  all external and irreducible.
- **Occurrences:** the manifest's ~44 non-`harvested` rows across the H17 block.
- **Management:** per-leg poll cap → harvest-or-FAILED, single retry with fresh
  chats, re-ride queued next tick; a FAILED leg is a chart GAP, never a zero.
- **Residual risk:** structural; the real unlock for Gemini is a billed API key
  (Houston-gated). Never fabricate a verdict off a login-wall or dead chat.

### (j) Concurrent-driver contention
- **Symptom:** two owners (a Codex/agent driver + the cron tick) drove the same
  papers — duplicate adjudication, a stalled agent needing relaunch, competing
  ledger bundles, and unpushed bundles colliding on push.
- **Root cause:** narrow `ps` grep missed a concurrent owner committing on the
  same papers (per MEMORY: cron-tick-overlap-detection, 2026-07-12).
- **Occurrences:** the M31/M32 STATE-CHECK tick explicitly yields when a
  concurrent driver is detected; the M34 ledger de-dup (`3d8f3b6d`) removed
  stale-streak dupes that were a symptom of double-adjudication.
- **Management:** hourly tick STATE-CHECK detects a concurrent driver (recent
  commits, files changing underneath) and YIELDs (no browser drive, no competing
  commit/push); `harvest` + `post_verdict.sh` stay safe. `git pull --rebase`
  before every push.
- **Residual risk:** MEDIUM — detection is heuristic; two drivers can still race
  a browser window. Mitigation: exclusive-browser-window rule per owner.

### (k) Transient Convex gate failures blocking pushes
- **Symptom:** the pre-push freshness gate (which reads Convex) intermittently
  fails on a transient Convex network blip and blocks an otherwise-clean push.
- **Root cause:** the freshness check treats a single Convex read failure as a
  hard FAIL rather than retrying.
- **Occurrences:** observed during the M-wave pushes.
- **Kill (in progress THIS cycle):** freshness-check Convex read gains a bounded
  retry so a transient blip no longer blocks a real bundle (see §4).
- **Residual risk:** LOW once the retry lands; today a re-run of the push clears it.

### (l) Compound submit chains dying mid-way — losing already-completed legs
- **Symptom:** a multi-leg `ext_submit` chain that dies on leg N loses the OK/FAIL
  bookkeeping for legs 1…N-1 that had already succeeded.
- **Root cause:** legs share one script invocation and one `set -e` fate — a
  later leg's failure aborts before earlier legs' state is durably banked.
- **Occurrences:** the (b) silent-exit family; chained P3APJS→other-paper legs.
- **Kill (in progress THIS cycle):** `tools/wave_submit.sh` with **per-leg
  isolation** — each leg runs in its own subshell so one leg's death cannot
  orphan a sibling (see §4).
- **Residual risk:** MEDIUM until per-leg isolation lands; today mitigated by
  URL-at-submit (a died chain can't orphan an already-submitted leg's URL).

---

## 3. Verdict-floor analysis — pattern-066

The residual gap is a **referee-variance floor**, not a content defect. Evidence
from the M-wave block, all on **byte-identical** served PDFs:

| Paper | Reviewer | Verdict walk on unchanged content | Rounds |
|-------|----------|-----------------------------------|--------|
| P4    | Grok     | ACCEPT → MINOR → MAJOR → MINOR     | M21 → M24 → M30 → M33 (v1.0.239 byte-identical) |
| P4    | ChatGPT  | REJECT ↔ MAJOR (floor-crack then re-settle) | M9(REJECT) → M11/M30/M33(MAJOR) |
| P5    | ChatGPT  | REJECT ↔ MAJOR                    | M22(MAJOR→REJECT) → M31(REJECT) → M34(REJECT→MAJOR) |
| P1U   | ChatGPT  | REJECT held (structural harsh floor) | 1:1 item set across M23/M26/M30/M33/H17G |
| P2    | ChatGPT  | REJECT held, concede-inside-REJECT | M31 ("−35/16 may nevertheless be correct" inside a REJECT) |

**Concede-inside-REJECT** is the tell: P2's M31 ChatGPT REJECT literally states
its own crux claim (the orbit double-counting "fix") "may nevertheless be
correct" — and that fix was **falsified by re-running the committed
`p2_vertex_check.py` + the convention-free Li et al. closed form** (both agree
with the paper's 6-permutation −35/16, not ChatGPT's convention). The referee
oscillates on the verdict *word* while its own body text concedes the science.

**What this means for the all-A grid (directive M):** the CURRENT column will
not go all-ACCEPT by running more text waves — the same content draws different
verdict words each sweep. That's the measured pattern-066 floor; treating one
sweep's tally as signal is the exact error the pattern codifies.

**What measurably moves the word** (in observed order of effect):
1. **Real compute/science closures** — P5's env-stratified confusion matrix
   (computed, integrated v0.1.118) closed the last open-recipe MAJOR; P4/P5
   produced verified Claude INT ACCEPTs after real closures.
2. **Venue matching** — P3 ApJS flip is PROVEN (ApJS-framed reviews are
   legitimate reviews of the same science); P4 Grok-EXT hit a real ACCEPT.
3. **Presentation overhaul targeting the REJECT raw's own words** — PRD abstract
   format, de-duplication, consolidation (editorial rigor, in-scope; watering
   down science is NOT).

**What does not move it:** additional text-only re-review waves. Confirmed across
15+ waves.

---

## 4. Acceleration plan

### Shipped this cycle (M20→M36 + the parallel hardening bundle)
Committed tooling root-fixes (sha-cited):
- `3fb1ffd9` stale pre-send URL guard · `02d68a8f` 120s poll + sidebar fallback ·
  `a08dd750` OK-or-FAIL dispatch guard · `80914698` empty-URL die ·
  `854acb99` attachment-token verification · `cd02c991` cap `_creationTime`-latest
  + `record_wave` clobber guard · `029cb689` INT/EXT label convention.

In-progress in the concurrent hardening bundle (disjoint files, other workers):
- **Harvest raw-sanity + paper-signature provenance gate** — pushes class (f)
  from adjudicator-layer down to harvest-layer (min-length + prompt-echo +
  paper-signature check at harvest).
- **`tools/wave_submit.sh` per-leg isolation** — each leg in its own subshell;
  kills class (l) compound-chain leg loss.
- **freshness-check Convex read retry** — kills class (k) transient-blip push block.

### Remaining recommendations, ranked by expected time saved
1. **Harvest-layer raw-sanity gate (finish + land).** Highest leverage: closes
   the one MEDIUM-risk class that still depends on adjudicator diligence, and
   removes the ~1 re-ride/round the wrong-attach + prompt-echo legs cost.
2. **Unattended-wave autonomy level.** Define a bounded autonomous wave the cron
   can run start→harvest→adjudicate→post→push with no human touch when STATE-CHECK
   shows no concurrent driver — the biggest remaining wall-clock sink is the
   orchestration hand-offs, not the reviewer latency (which is parallelized).
3. **Gemini API leg in EXT rotation** (Houston-gated key). Converts the recurring
   3h/day throttled browser-Gemini loss into an instant parallel API leg —
   documented standing bottleneck since 2026-07-10.
4. Adjudicator prompt template as a **file, not inline** — stop re-deriving the
   directive-I4 read protocol per wave; one canonical prompt file.
5. **Manifest latest-row-wins helper** — a tiny reader that returns the newest
   valid row per (paper,reviewer,round), so re-ride/retry rows never confuse a
   harvest (complements (a)/(d)/(f)).
6. **Retire redundant probes** — the three-probe "rate-limit" pattern was a
   misdiagnosis (§(c)); a single headed diagnostic replaces repeated blind probes.

---

## 5. Houston-gated queue — the levers only Houston can pull

These are the *only* paths past the measured pattern-066 verdict-word floor
(§3). None are code-fixable; all require Houston:

1. **arXiv wave-1 submission clicks** — the submit-ready bundles (P4/P5/P1B
   family) are re-verified against final versions; submission is a human click.
2. **P3 venue word** — greenlight the ApJS variant as the P3 submission target
   (the flip is proven; the call is Houston's).
3. **Human expert referees** — route the floor papers (P1A/P1U, P2, P3) to human
   referees; LLM-referee variance is exhausted as a signal.
4. **Zenodo DOI** — mint the P2 (and companion) dataset/analysis DOI so the
   channel-native Fisher + artifact citations resolve.
5. **Cai email** — the P1U/P2 −35/16 vs Cai −35/8 companion question and any
   coordination on the shared bounce derivation.
6. **Billed Gemini API key** — unlocks the Gemini INT/EXT API leg (also §4 #3).

---

*Cross-references: `ACCELERATION_LOG_2026-07-10.md` (tooling rounds 1–2, the
`ext_submit`/`ext_harvest`/`post_verdict`/`int_wave` + `directive_g.sh` + fused
owner loops + disposition ledgers), `REPEATED_ASKS_AUDIT_2026-07-11.md` (the
loop-never-dies watchdog + site-freshness class kills), and the canonical
`~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md` dated lessons.*
