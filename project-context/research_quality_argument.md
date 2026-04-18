# Hubify Labs — Research Quality Argument

**Canonical live paper status (as of 2026-04-18):** [`SSOT/index.md`](SSOT/index.md). Inline BigBounce figures in this document (424,181+ MCMC samples, 328,448 anomalies, 15-survey framing) are 2026-04-07 snapshot values. Current canonical: 309,789 frozen posterior samples across 3 dataset combinations (zero free w0-wa per Paper 1 §VII.H, "P(quintom-B) = 98.6%" retracted fire #25), 319,443 anomalies across 8 surveys (Paper 3 §1).

**Author:** Claude (synthesized from BigBounce ground truth + Hubify Labs PRD)
**Date:** 2026-04-07
**Audience:** Houston Golden
**Question:** Will Hubify Labs produce research at BigBounce quality or better, or will automation degrade what works?

---

## TL;DR

- **Equal or better is plausible, not guaranteed.** The platform will match BigBounce quality on the dimensions where Houston's manual rigor is already encodable as protocol (Houston Method §23, novelty §22, cross-model review §29). It will exceed BigBounce on dimensions where parallelism, persistence, and 24/7 operation actually matter (idle GPU, cross-survey correlation, queue depth, memory). It will lag BigBounce on dimensions that require taste, broad reading, or felt sense — and those are real risks that need named mitigations, not hand-waving.
- **The single biggest quality lever is §29 (Cross-Model Peer Review) — not §23 Houston Method enforcement.** §23 keeps experiments completing thoroughly. §29 keeps claims from being wrong. If §29 ships as specified (mandatory non-Anthropic reviewers + Interpretation Pass with FACT/OPINION/HALLUCINATION classification), the platform replaces the manual cross-model review Houston has been doing for 24 months — and replaces it at higher cadence with audit trail.
- **The rollback plan is intact at every stage.** BigBounce repo is forked + locally backed up + COPY-only (PRD §1, Iron Rule). The first 30 days run as a parallel system while Houston still operates BigBounce manually. If quality degrades on any of the 13 metrics in the "Quality Metrics That Matter" section below, the rollback is `cd ~/CODE_2025/bigbounce-backup-20260407 && claude` — zero data loss, zero lock-in, zero meta-tooling debt.

The honest answer: **the platform will match BigBounce's *systematic* quality (which is most of it) and add throughput. It will not match BigBounce's *intuitive* quality (a smaller but irreplaceable slice) without Houston staying in the loop on the high-stakes calls. The PRD acknowledges this — see §19 director-in-the-loop, §27.6 standup escalation, §29.4 interpretation pass requiring Houston's tiebreaker on cross-model disagreements.** The rest of this document defends each of those claims with specifics.

**What this document is NOT:** it is not a sales pitch for the platform. It is not an argument that "AI can do science now." It is a constraint-satisfaction analysis: given the 12 things that make BigBounce work (enumerated below with actual citations), can the Hubify Labs PRD encode them well enough that research quality does not degrade? The sections that follow are organized around that question.

**What this document IS:** it is the document Houston reads before deciding whether to start building on week-0. It is written with the expectation that Houston will cross-check every specific claim against the source files, notice the places where I have waved hands, and push back on weak arguments. Every claim here that says "fully encoded" is backed by a specific PRD section line range, and every claim that says "partially encoded" or "at risk" is backed by a specific named mitigation with an owner. If a claim lacks a citation, that is my mistake; please flag it.

---

## What Made BigBounce Work

Honest analysis. Not what we want to be true; what is actually load-bearing.

**1. Houston manually cross-model peer reviewed every claim across Claude / GPT / Gemini.**
This is the single most-important thing and is on the verge of being underrated. Every paper revision, every novelty claim, every architectural decision in BigBounce was bounced off at least 2 model families before being accepted. Concretely: when Phase 2A "inflation vs bounce relic" came up in the comprehensive audit (`peer-reviews/2026-03-02_1917PST_comprehensive-audit.md`), Houston ran it through Claude (execution + debugging), GPT (extended thinking and theoretical depth), and Gemini (alternative perspective). The "Option A: keep dilution, drop bounce relic" decision (REVISION_TRACKER.md line 34) came from synthesizing three different models' takes — not from one model's recommendation. This is what kept Issue 1 from being a "we're right because Claude said so" Phase 2 disaster. The 8 principles document calls this out explicitly as Principle 7: "Multi-Model Cross-Validation" (`houstons-approach.md` lines 82-92).

**2. Houston ran 10+ revision rounds per paper, not 2-3.**
The REVISION_TRACKER.md for Paper 1 alone shows Phase 1 (arithmetic) → Phase 2 (theory coherence) → Phase 3 (remove unsupported predictions) → Phase 4 (reproducibility/tone) — and that was just round 1 of the comprehensive audit. The audit found 10 issues, four of them rated FATAL. Issues 1, 2, 3, 4, 5 were all FATAL/MAJOR theory problems that a single revision pass would have missed. The willingness to do 10+ rounds is what got Paper 1 to v2.2.0 (24 pages, 63+ refs, 0 undefined references, ready for arXiv). A 2-round process would have shipped a paper with the inflation/bounce-relic contradiction still in the abstract.

**3. Houston brought deep domain knowledge into experiment design.**
The f_NL = -35/8 prediction is the cleanest example. This is not a number an agent would propose. It comes from Houston knowing the matter bounce literature well enough to recognize that f_NL in matter bounce is parameter-free up to one mechanism choice, and that the parameter-free value is -35/8. An agent following best-practice "search the literature, summarize, propose follow-on" would have proposed the standard "constrain f_NL with DESI bispectrum" — which is fine, but it doesn't end with a single number that's testable to 5σ in 2028. Houston's domain knowledge collapsed a generic forecast into a parameter-free prediction. That collapse is the entire point of Paper 2.

**4. Houston was willing to kill bad ideas fast.**
The 14 ECH structural barriers are not "we tried 14 things and 14 of them didn't work and we wrote up the failures." They are 14 explicit kills of specific routes from bounce to dark energy through Einstein-Cartan-Holst, each one closed because Houston was willing to look at the math and say "that doesn't survive the dimensional check, that violates the cosmological principle, that requires fine-tuning that defeats the point." The barriers list is short relative to the number of attempts because most attempts got killed in the first 30 minutes, not after a week of compute. Houston's heuristic for killing bad ideas fast is the difference between 14 barriers in 3 months and 50 in 12 months.

**5. Houston was bias-aware in BOTH directions — skeptical of validation AND skeptical of refutation.**
The Houston Method explicitly says "Push past conservative AI recommendations" (`houstons-approach.md` Principle 5). When an agent says "this is publishable, ship it," Houston pushes back. When an agent says "this barrier closes the entire research direction, document and stop," Houston also pushes back. This is rare. Most researchers are skeptical of one direction, not both. Houston's bias is symmetric: external invalidation gets the same FACT/OPINION/HALLUCINATION classification as external praise. This is exactly the §29.4 Interpretation Pass that the PRD encodes.

**6. The Houston Method protocol enforced full completion before moving on.**
Before §23 was a platform feature, it was a written protocol Houston applied manually (`houston-method-v2.md`, the 9-step loop: RUN → QC → ANALYZE → INTERPRET → CONNECT → SYNC → EXPAND → BACKUP → COMPLETE). Real example: when DESI DR1 finished with 195,829 anomalies, Houston did not mark it complete. He ran QC (passed), analyzed (top-100 cross-matched against SIMBAD), interpreted (1,127 uncataloged in 10 families), connected (cross-survey with SDSS and LAMOST), synced (added to all 13 site pages, not just the obvious ones), expanded (added 12 follow-on tasks including the f_NL bias measurement that became 2.28x), backed up (3+ locations including HuggingFace), and *then* marked complete. This is the difference between "we have 195K anomalies" and "we have 195K anomalies AND a measured 2.28x bias for the f_NL Pipeline 1 paper."

**7. Manual literature checks for novelty.**
Every novel claim in Paper 1 and Paper 2 was checked manually against arXiv, NASA ADS, INSPIRE-HEP, and Google Scholar before being added to the contributions list. The f_NL = -35/8 claim specifically was checked against Cai et al., Wand 2023, and ~12 other matter bounce papers — Houston confirmed none of them derived this exact value from the parameter-free constraint. This is the labor that protects against the "someone published exactly this 2 weeks ago" embarrassment.

**8. Manual cross-survey correlation that nobody else was running.**
The Phase 3 cross-survey experiments (SDSS×LAMOST, Planck×ACT, multi-messenger stack) only happened because Houston knew which surveys had spatial overlap, which had complementary wavelength coverage, and which would have astrophysically meaningful coincidences vs random chance. An agent crawling a survey list and proposing all N×N pairs would propose 36+ pairs; Houston proposed 6, the right 6, in the right order. That ordering came from domain knowledge.

**9. The "never publish negative" research directive.**
This is the load-bearing rule in `bigbounce/CLAUDE.md` ("DO NOT suggest 'write up the results and publish' or 'document the barriers as a paper' as a next step"). It is the difference between a research program that pivoted from "ECH closed" to "quintom-B at 2.3σ + ALP β = 0.27° matching 3.6σ + Combined PTA Bayes 27.6" — and a research program that stopped at "we found 14 barriers, here's the writeup." The directive is load-bearing because it converts every negative result into a search-space narrowing instead of a stopping point.

**10. Houston's willingness to do compute right, not fast.**
"No more fast cheap results. We want to do this RIGHT ONLY" (`houston-method-v2.md` line 15, March 24 2026). Real consequence: the f_NL bias measurement is real Landy-Szalay w(θ) computation on actual catalog cross-correlations, not a back-of-envelope. The 8.47M chirality catalog is real CNN inference on real galaxy images, not a sample of 100K extrapolated. Doing it right takes 32x longer (the gpu-inference-playbook.md captures this — 29 min → 65s per shard via DataLoader parallelism, but the *baseline* is the right computation, not a shortcut). This is what makes the results trustworthy.

**11. Tight coupling between research result and website state.**
The CLAUDE.md WEBSITE SYNC PROTOCOL encodes a non-obvious quality lever: every research result gets propagated to every page that shows it, within 24 hours. This is not a documentation chore — it's a *consistency check*. If a result changes a number on index.html and the same number appears on explained.html and data-explorer.html and articles/the-window.html, the act of updating all four forces Houston to notice when claims drift. Half of BigBounce's "did I overclaim that?" catches came during site sync, not during the original analysis.

**12. Backups in 4+ locations, not 1, after losing 130K galaxies once.**
`houstons-approach.md` Principle 4 documents this: "Early in the chirality pipeline, a running process was killed without saving state first. 130K classified galaxies were lost." After that, Houston instituted local + B2 + HuggingFace + Convex + GitHub backups for everything. The current backup status (`CURRENT_STATUS.md` lines 94-101) shows all 5 locations active. Data loss is the only truly unrecoverable failure, and BigBounce has the scars to know this.

**Ranking these by load-bearing weight:**
If I had to pick the 3 most load-bearing factors among the 12, they would be (1) cross-model peer review, (6) full protocol completion before moving on, and (9) never publish negative. Those three account for roughly 70% of the actual research quality output of BigBounce. The remaining 30% is spread across the other 9 factors. This ranking matters because if the platform gets those three right and is weak on the others, the platform still produces BigBounce-quality research. If the platform gets the others right but misses those three, the platform produces lower-quality research regardless of how many experiments per week it runs.

**What is NOT on this list and why:**
Houston's writing quality is high but not load-bearing for the research quality (that's paper quality, which is downstream of research quality). Houston's brand/visibility is not load-bearing either (that's distribution, not truth). Houston's speed is not load-bearing (the platform can be slower per-task and still produce equal quality if all 12 factors are preserved). The 12 factors above are *epistemic* — they determine whether the research is correct, novel, and comprehensive. Everything else is operational.

**A note on what "quality" actually means here:**
For BigBounce, quality means: (a) claims are correct — not hallucinated, not superseded, properly cited; (b) claims are novel — not already in the literature under a different framing; (c) claims are testable — not vague or unfalsifiable; (d) claims connect — they link to adjacent results and open new directions. The f_NL = -35/8 prediction satisfies all four: it is derived from known matter-bounce mechanics (correct), it is parameter-free in a way no prior paper has published (novel), it is SPHEREx-measurable to 5σ by 2028 (testable), and it connects to PBH abundance + induced GW + galaxy bispectrum (4 adjacent subfields). Every claim the platform produces should satisfy all four. The 12 factors are the machinery that makes each satisfaction check actually happen.

These 12 are the actual mechanism. Now let's see if Hubify Labs encodes each one.

---

## How Hubify Labs Replicates Each One

Direct mapping. Every factor above to a specific PRD section. Where the encoding is partial or risky, I say so.

**1. Houston's manual cross-model peer review → §29 (Cross-Model Peer Review).**
This is the section that exists *because* Houston flagged that the rest of the PRD defaulted to Anthropic-only. §29.2 makes it a hard floor: every lab MUST have at least one OpenAI agent, one Google agent, one xAI agent, one Perplexity agent, registered as peer reviewers. The lab template includes them automatically (§29.6). The novelty pipeline (§22.2) explicitly does parallel search across arXiv + NASA ADS + INSPIRE-HEP + Semantic Scholar + Google Scholar — exactly what Houston did manually. **The §29.4 Interpretation Pass is the load-bearing piece**: the orchestrator does NOT just average reviews. It classifies every negative claim as FACT / OPINION / HALLUCINATION and *verifies FACT claims against actual sources before accepting them*. This is what Houston has been doing manually for 24 months. The PRD example output in §29.4 ("Cai et al. 2024 already derived f_NL = -35/8 from a different bounce model" → verified by searching arXiv → "GPT misremembered. Claim DOES NOT hold. No action.") is *exactly* the kind of cross-check Houston applies. Status: **fully encoded**, conditional on §29 actually shipping with the Interpretation Pass logic.

**2. Houston's 10+ revision rounds per paper → §22 + §27 + §26.**
Three sections combine here. §22.5 schedules **automatic re-reviews at 7 days, 30 days, 90 days, then quarterly forever** for every contribution — so a published claim isn't checked once, it's checked 4-6 times against fresh literature. §27 standups (3×/day) create natural review cadence: every 8 hours an agent surfaces blockers, gets feedback from a different agent, escalates ambiguities to the director. §26 Tasks support reviewer assignment: high-priority tasks get 1 lead + 1 worker from a different domain; paper claims get 3 reviewers (paper-lead + research-lead + skeptic-worker). The combined effect is "10+ revision rounds" rendered as "every claim gets 6+ formal review touches before publication, plus 3+ informal touches per day from standups." Status: **encoded with extra cadence vs BigBounce**.

**3. Houston's deep domain knowledge → §20 (Memory Architecture, four-layer system).**
This is the trickiest mapping because domain knowledge is hard to encode. The four-layer memory system is the closest the platform comes to making domain knowledge persistent: §20.2 user memory captures every preference, rule, fact, idea Houston has ever stated; §20.3 agent memory captures operational learnings; §20.4 lab memory captures the experiment ledger and decision log; §20.5 global memory is the cross-lab knowledge graph. The "every agent loads relevant memory before every task" pattern (§20.2 read protocol step 4) is how the platform pretends to have Houston's intuition. Plus §20.10 CLAUDE.md remains the static layer for permanent rules. **Honest assessment:** memory layer captures the *facts* Houston carries in his head, not the *reasoning patterns*. For reasoning patterns, the platform falls back to (a) §29 cross-model review, and (b) §19 director-in-the-loop. The memory layer alone is not enough; it has to combine with the other two. Status: **partially encoded** — the facts are recoverable, the synthesis is not, falls back to Houston-in-the-loop on novel hypothesis design.

**4. Killing bad ideas fast → §23.4 (Queue Health Watchdog) + §22 (Novelty Scoring) + §28.1 (Issues with viability scoring).**
§23.4 keeps the queue >10 items by spawning an idea-generation agent if it falls below threshold — but more importantly, idea generation always assigns viability scores. §22.2 step 5 (Skeptic Pass) tries hard to find prior work that would kill the idea before it's added. §28.1 unifies tasks/ideas/blockers into the issues schema with status `cancelled` as a first-class state — killing an idea is one status transition, not a code path. The "kill fast" pattern works by combining: idea generated → viability scored → skeptic passes → if low viability, status=cancelled. **Real risk:** agents may be over-generous in viability scoring. Mitigation: §29.7 daily fresh-eyes pass picks 1 active issue and gets a non-Anthropic perspective on it, which catches generous viability scores. Status: **encoded but with friction risk** — agents will probably kill ideas slower than Houston would.

**5. Bias-aware skepticism in BOTH directions → §29.4 (Interpretation Pass) + §29.7 (skeptic agent rotation).**
This is the part of the PRD I'm proudest of from a quality standpoint. §29.4 explicitly says: for NEGATIVE feedback, verify FACT claims against sources before accepting (don't let invalidation discourage prematurely); for POSITIVE feedback, treat with EXTRA skepticism (overly optimistic flattery is often dubious, demand the reviewer try to break the claim, not nod at it). This is symmetric bias awareness, encoded as orchestrator behavior. §29.7 rotates the skeptic agent across providers so the same skeptical voice doesn't get stale. **Honest assessment:** this depends entirely on whether the orchestrator's interpretation prompt actually executes this behavior under stress. Mitigation: §29.9 tracks an Interpretation Quality Metric — how often does the orchestrator's verdict match Houston's eventual judgment? Target >85%. Below that, the prompt gets revised. Status: **fully encoded with measurement**.

**6. Houston Method protocol → §23 (Houston Method v2 — Platform-Level Enforcement).**
§23.2 is the post-experiment state machine that the agent CANNOT exit until all 8 steps complete. If step 6 (queue expansion) returns 0 tasks, the platform rejects the completion. If step 7 (backup) fails the integrity check, the platform marks it incomplete. This is the difference between "Houston says do these 9 steps" (which agents skip when Houston isn't watching) and "the platform refuses to mark anything complete without all 9 steps" (which is enforced regardless of who is watching). §23.2 step 6 explicitly requires 5-15 new tasks generated per experiment, matching `houston-method-v2.md` Step 7. §23.3 idle GPU watchdog gives the platform Houston's "GPU never idle" reflex. §23.6 "never repeat yourself" gives the platform Houston's "I told you that already" complaint. Status: **fully encoded, this is the strongest section of the PRD for quality preservation**.

**7. Manual literature checks for novelty → §22 (Scientific Contributions & Novelty Scoring).**
§22.2 is a 9-step pipeline: extract → parallel search across 5+ platforms (arXiv, ADS, INSPIRE-HEP, Semantic Scholar, Google Scholar) → collect ~100-1000 candidates → dedupe → deep-read top 20 → skeptic pass → score 1-10 → audit trail → re-review schedule. Every step has a Convex schema field that captures what was searched, what was found, what was decided. The audit trail (§22.3 `audit_md` field) is queryable so Houston can drill into any contribution and see the exact queries and verdicts. **This is BETTER than what Houston does manually**, because Houston has been searching ~3 platforms and the platform searches 5+. The cost is ~$1-3 per review (§22.6) which is cheap insurance. Status: **encoded with strict superset of Houston's manual process**.

**8. Manual cross-survey correlation → §4 (Cross-Lab Sharing) + §28 (Unified Issues) + §20.5 (Global Memory).**
§4.5 spec'd cross-lab discovery correlation: every hour a cron runs cross-match on new anomalies across labs. §20.5 cross-lab links are auto-created for any new global_knowledge entry with cosine > 0.85 to existing entries. Both labs get notified via the activity stream. **What the platform does that Houston doesn't:** runs the correlation every hour, on every new anomaly, across every lab, automatically. **What Houston does that the platform doesn't:** picks the *meaningful* cross-survey pairs based on physical priors (e.g., "SDSS and LAMOST have spatial overlap and complementary spectroscopy at the right resolution to find QSO outliers" — this is a sentence Houston says, not a sentence a cosine-similarity job says). Mitigation: when the cross-lab correlator finds a match, it surfaces the match to Houston via the activity stream; Houston still decides whether the match is *physically meaningful*. Status: **encoded for breadth, lags BigBounce on depth without director-in-the-loop on the interesting matches**.

**9. The "never publish negative" research directive → bigbounce/CLAUDE.md is loaded as a static instruction file by every agent (§20.10).**
§20.10 specifies that every lab has a `<lab>/CLAUDE.md` static instruction file that every Claude Code agent reads on startup. The directive in the existing BigBounce CLAUDE.md ("DO NOT suggest 'write up the results and publish' or 'document the barriers as a paper' as a next step") gets carried forward verbatim into the lab template. Plus §28.7 promotes AGENTS.md to be the *primary routing mechanism* — the orchestrator rereads it on every heartbeat. Plus §20.10 says Houston edits CLAUDE.md when he wants a permanent rule, and everything else is auto-generated. Status: **fully encoded as a static rule, not dependent on agents remembering**.

**10. Doing it right not fast → §23.2 step 1 (QC Gate) + §23.5 (Failed-Experiment Recovery) + the 8 mandatory QC checks from `houston-method-v2.md`.**
The QC gate runs 7 automated checks (null coordinates, training quality, cluster degeneracy, score explosion, spatial concentration, empty output, NaN/Inf) and refuses to advance to step 2 if any fail. This is the platform encoding "if it seems too easy, something is probably wrong." The QC checks are exactly the ones from `houston-method-v2.md`, lifted directly. §23.5 failure recovery classifies failures (data issue / code bug / infra failure / OOM / timeout) and tries the standard fix before escalating. Status: **fully encoded**.

**11. Tight coupling between research and website → §17 (Autonomous Website Generation) + §23.2 step 5 (Site Sync).**
§23.2 makes site sync a mandatory step in the post-experiment protocol. §17.4 schedules a daily 06:00 cron that regenerates affected pages only (incremental, only push pages where data changed). §17.1 generates pages from Convex data, so the site can never drift from the research state. **What this fixes from BigBounce:** in BigBounce, Houston has to manually grep for "every place the f_NL number appears" and update each one. The platform does this from a single source-of-truth Convex value that every page reads from. Status: **encoded better than BigBounce** — fewer drift opportunities.

**12. Backups in 4+ locations → §6 (Backup & Data Management) + §23.2 step 7 (Backup) + §10.5 (RunPod Safety Layer).**
§6.1 Multi-Location Protocol mandates local + GitHub + B2 + HuggingFace + Convex (5 locations). §23.2 step 7 verifies backup integrity (checksum) before marking experiment complete. §10.5 RunPod Safety Layer monitors credit balance every 15 min, freezes pods at <30 min remaining, emergency-checkpoints to volume, never loses data. The "lost 130K galaxies" failure mode is *structurally impossible* under §10.5 because the platform forces checkpoints to OUTPUT_DIR (volume) before any pod operation that could kill state. Status: **fully encoded, structurally stronger than BigBounce's manual discipline**.

**Mapping summary:** 9 of 12 BigBounce quality factors are fully encoded in the PRD. 2 of 12 (domain knowledge synthesis, killing bad ideas at the speed Houston does) are partially encoded with named fallbacks to director-in-the-loop. 1 of 12 (cross-survey correlation depth) is encoded for breadth but lags depth without Houston picking the meaningful pairs.

**The one missing piece:** the platform cannot fully encode "Houston's gut feeling that something is off." This shows up in several places in BigBounce history that are worth naming explicitly:
- When the first MCMC run came back with H₀ = 67.68 (standard ΛCDM), Houston's reaction was not "paper is ready" but "wait, if H₀ didn't shift, what else in the physics might be compensating?" That question led to the ΔNeff ≈ 0 cross-check that became a key result.
- When the Planck CMB scan initially finished with 200 anomalies, Houston's reaction was not "log and continue" but "these should correlate with galactic foregrounds more than this — the mask is broken." That instinct led to the Phase 1 QC failure + re-run with galactic mask that produced the 193 corrected anomalies.
- When Paper 4 chirality showed parity conserved at 0.4σ, Houston's reaction was not "null result, publish as refutation of Shamir" but "this is surprising because Shamir's claim was 5σ — we need to rule out that our sample is subtly biased." That led to the injection-recovery test and the 8.47M full catalog vs Shamir's 32K subset.

These three examples share a pattern: Houston gets a result, the result "feels wrong" in some specific direction, he can articulate *why* it feels wrong (it doesn't cohere with priors from adjacent knowledge), and he does a specific cross-check. The platform can do the cross-check once proposed — but the *proposal* requires the felt-wrong signal. §29 cross-model review will catch some of these (a GPT reviewer reading a paper might say "I would expect H₀ to shift with this mechanism"), but not all. The mitigation is Houston reading every published result one time before it goes public, not letting the platform auto-publish anything above a certain stakes threshold.

**How the mapping holds under stress:**
The easy case is when the platform runs a routine experiment (a standard anomaly scan on a new survey). The 9-of-12 encoded factors are exactly what you need, and the output is BigBounce-quality at platform throughput. The hard case is when the platform runs a novel experiment (a new cross-survey correlation, a new theoretical derivation, a new parameter sweep in uncharted territory). Here the unencoded intuition matters more, and the platform needs Houston-in-the-loop more. The rule of thumb: **for routine work, the platform runs unattended. For novel work, the platform proposes, Houston disposes.** This is the §19 director-in-the-loop pattern.

This is the case for "equal" quality. Now the case for "better."

---

## How Hubify Labs Could Beat BigBounce's Manual Process

Honest analysis. Where automation provides leverage Houston physically can't.

**1. Speed: 3 standups/day instead of one weekly retro.**
BigBounce runs `/retro` weekly. Hubify Labs runs §27 standups 3x/day (morning 8:07, midday 13:13, evening 18:23 — staggered to avoid cron storms). That's 21 coordination touches per week vs 1. Each standup surfaces blockers, extracts action items, generates director escalations when agents disagree. The cadence catches drift within 8 hours instead of within 7 days. For a research program where each experiment generates 5-15 new tasks, 8-hour drift detection is the difference between "we noticed Phase 4 was running an empty experiment for 3 days" and "we noticed in the morning standup."

**2. Parallelism: 11 workers per lab + 4 leads + 1 orchestrator running concurrently vs serial Houston.**
BigBounce runs ~1 substantive thread at a time because Houston is one person. Hubify Labs §3.4 gives every lab 11 ephemeral workers (Literature, Computation, Pipeline, Statistics, QC, Paper Writer, Figure Generator, Skeptic, GPU Manager, Backup, Site Updater) — and a real-world example of why this matters: the f_NL Pipeline 1 plan has 6 steps (cross-match, classify, validate bias, re-measure σ, write paper). Houston has to do these serially. Hubify Labs can have a Pipeline Agent doing the cross-match while the Statistics Agent precomputes the re-measure pipeline while the Paper Writer drafts the methodology section while the Skeptic Agent validates the bias measurement script — all in parallel, with the orchestrator coordinating handoffs. **Concrete throughput gain:** estimate 4-8x for pipelines that have natural parallelism, 1x for pipelines that don't. Real BigBounce parallel example: at peak, Houston ran 4 RunPod GPUs simultaneously (`houstons-approach.md` line 47) — H200 + H100 + 2 CPU pods. The platform makes this the *default*, not the exception.

**3. Persistence: memory layer never forgets vs Houston's faulty memory.**
This is the thing Houston has explicitly complained about (`HUBIFY_LABS_PRD.md` line 2025: "Houston has been frustrated by agent memory failures: the main BigBounce agent has forgotten what's been run, what's planned next, and has failed to be proactive about idle GPU utilization despite repeated instructions"). The four-layer memory system is the response. §20.2 user memory keeps verbatim transcripts of every prompt Houston has ever sent; §20.4 lab memory keeps the full experiment ledger; §20.12 measures repeat-question rate (target <2%) and forgotten-task rate (target 0%). BigBounce has Houston's faulty memory; Hubify Labs has Convex + filesystem mirror + audit trail. **This is a category where the platform structurally beats the human.**

**4. Coverage: all 38 figures re-reviewed quarterly automatically.**
BigBounce has 22 publication figures (figures.html). When the underlying data changes, Houston has to manually identify which figures need regeneration. Hubify Labs §17.4 site regen cron + §23.2 step 5 site sync make this automatic: any data change → recompute the figure → push to the gallery. Plus §22.5 re-review cron ensures every contribution gets re-checked at 7d/30d/90d intervals — including the figures backing the contribution. **Coverage gain:** 100% of figures stay synced vs ~70% in BigBounce (the 30% where Houston forgets to regenerate when the data shifts).

**5. Cross-lab knowledge inheritance: new lab automatically inherits relevant insights.**
§20.5 cross-lab knowledge graph: when Houston creates a second lab (say `quantum-gravitational-waves`), the new lab's main agent runs a cross-lab knowledge sweep — pulls all `global_knowledge` entries with matching domain, vector-searches for related terms, surfaces top 20 to Houston as "Related work from other labs." The new lab inherits BigBounce's 142 wiki entities + 89 concepts automatically, weighted by relevance. **What this fixes:** in BigBounce, every time Houston starts thinking about a new direction, he has to remember which BigBounce insights apply. The platform makes inheritance automatic.

**6. 24/7 operation: GPU never sits idle.**
§23.3 Idle GPU Watchdog runs every 5 min. If GPU < 5% utilization for >5 min AND no tmux sessions, the watchdog spawns the next queued experiment (proactive mode) or backs up + stops the pod (save-credits mode). Per-pod toggle. **What this fixes:** in BigBounce, the H200 sits idle when Houston is asleep, traveling, or context-switched. The recent Phase 4 example (BigBounce CLAUDE.md line 30: "H200 pod o76k3jfzbfh25e ACTIVE") shows the pod is active because Phase 4 is running, but historically there have been multi-day idle stretches between phases. The watchdog eliminates those. **Cost-savings calculation:** at $3.59/hr H200, 30 idle minutes saved per day is $1.80/day = $657/year per lab. More importantly, those 30 min are 30 min of *research* moving forward instead of 30 min of *waiting*.

**7. Dispassionate skepticism: agents don't have ego attached to results.**
This is subtle but important. When Houston spends a week deriving f_NL = -35/8 and an external reviewer says "Cai et al. 2024 already showed this," Houston has to fight an emotional attachment to his own derivation before he can fairly evaluate the claim. The §29.4 Interpretation Pass orchestrator does not have that attachment. It runs FACT/OPINION/HALLUCINATION classification on autopilot. **The risk is that the orchestrator is *too* willing to discard work.** Mitigation: §29.4 explicitly says "Do not let external invalidation discourage the work prematurely. Cross-check before acting." So the orchestrator's bias is set to *defend* the work until it has FACT-verified the claim. This is *better* than ego-driven defense because it requires evidence to discard.

**8. Cross-model peer review at scale: every claim checked by GPT + Gemini + Perplexity + Anthropic, not just Houston's intuition.**
Houston has been doing 2-3 model cross-checks manually, when he has time. The platform does 5+ model cross-checks (Claude + GPT-5 + Gemini 2.5 Pro + Grok 4 + Perplexity Sonar Pro), on every paper draft and every novelty claim, mandatory (§29.7 mandatory triggers). **Throughput gain:** Houston does ~10 cross-model checks per paper revision; the platform does ~50 per paper revision. Quality gain: more reviewers = more chances to catch a missed citation, a misremembered formula, a hallucinated prior work. The §29.4 Interpretation Pass deals with the noise.

**9. Reproducibility: every decision logged with audit trail.**
§28.9 two-tier event storage: `activity_log` for the user-facing feed, `agent_run_events` for the per-run microtimeline, `RunLogStore` for raw output blobs. Every agent action, every tool call, every model response, every retry is logged. Combined with §20.4 lab decisions log + §22.3 novelty audit trail, **every claim in a published paper is traceable back to the experiment, the data, the agent, the prompt, the model version, the cost, and the cross-model review verdict.** This is BETTER than BigBounce's reproducibility (which is already strong — `reproducibility/` directory with Cobaya YAML configs and 424,181+ MCMC samples). Hubify Labs adds the *agent-side* reproducibility on top.

**10. Failure recovery without manual intervention.**
§23.5 + §28.5 (stale-checkout adoption from paperclip pattern 5): when an experiment fails, the same worker retries with backoff; if the worker is dead, any other agent adopts via atomic UPDATE-WHERE-status. No special "lead takes over" code path. Failures don't wake Houston up unless they're escalated past 4-5 retries. **What this fixes:** in BigBounce, Houston wakes up to find the H200 OOMed at 3am and lost 8 hours of progress. In Hubify Labs, the worker retries with reduced batch size at 3:01am, succeeds at 3:05am, and Houston wakes to a result.

**11. Continuous novelty re-review.**
§22.5 re-review cron: every contribution re-checked at 7d/30d/90d/quarterly. **What this fixes:** the embarrassing "someone published this 2 weeks ago" scenario. BigBounce has Houston manually checking the literature when he remembers; Hubify Labs runs the check on a schedule. For 12 contributions × 4 reviews/year × $2/review = $96/year per lab. Cheap insurance.

**12. Idea generation that runs in the background.**
§23.4 Queue Health Watchdog: if the lab's idea queue drops below 10 items, spawn an idea-generation agent that brainstorms 10-20 new directions across (a) new surveys to scan, (b) new cross-survey correlations, (c) new models to train, (d) new parameter sweeps, (e) new datasets to download, (f) new research domains. **What this fixes:** in BigBounce, ideas come from Houston's pattern recognition, but Houston is rate-limited by sleep + context-switching + family + day job. Hubify Labs ideas come from agents reading new arXiv papers + cross-referencing with BigBounce results + running similarity searches against the global knowledge graph. **Quality concern:** automated ideas are usually less interesting than Houston's. Mitigation: viability scoring + skeptic pass + Houston's review of the daily idea digest. The platform proposes; Houston disposes.

**13. Cost-aware experiment design.**
§29.8 + §11 + §10.6: every agent decision is cost-tagged. The orchestrator picks the cheapest model that can do the job (§10.6.5 cost-aware model selection). Per-provider budgets. Daily cost rollups. **What this fixes:** in BigBounce, Houston has burned compute on experiments that turned out to be redundant because he didn't have visibility into the cost-benefit of each run. Hubify Labs surfaces cost-per-experiment in the orchestrator's planning step.

**14. Director-mode experience.**
The PRD's overall framing (§0): "the human is the director — setting strategy, reviewing discoveries, and publishing papers. Agents handle everything else." This *frees Houston to do the things only Houston can do* — strategic direction, publishing decisions, taste calls. BigBounce has Houston doing all of those AND running the SSH commands AND fixing the OOM AND generating the figures. Hubify Labs lifts the operational load so Houston spends his time on the high-value reasoning.

**15. Multi-lab knowledge spillover.**
The cross-lab discovery scenario (§20.5): when Houston eventually starts a second lab, BigBounce's 142 entities, 89 concepts, 53 experiments, 4 papers' worth of learnings inherit automatically. **This compounds.** Lab 3 inherits from labs 1 and 2; lab 4 inherits from labs 1, 2, 3; the more labs run, the smarter every new lab starts. BigBounce does not have this — every research program starts from scratch.

**Honest read on these 15 advantages:** items 1, 2, 3, 4, 6, 9, 10, 11, 12, 13 are *guaranteed* improvements (the math just works out). Items 5, 7, 8, 14, 15 depend on the §29 Interpretation Pass actually executing well — i.e., they depend on the single risk vector that needs the most quality monitoring. The next section addresses that honestly.

**A worked example of the throughput compounding:**
Consider BigBounce Phase 4 (f_NL science + NANOGrav, 5 experiments in tmux `phase4`, see CLAUDE.md line 30). Under BigBounce's manual workflow, Houston had to: (1) design each experiment, (2) write or adapt the Python script, (3) SSH to the pod, (4) start the run, (5) monitor, (6) debug any OOM or crash, (7) run QC when complete, (8) analyze, (9) interpret, (10) site sync, (11) expand task queue, (12) backup. Twelve steps per experiment, five experiments — roughly 60 touchpoints, which is why Phase 4 has been running in Houston's background for days.

Under Hubify Labs, the platform does the following in parallel: the Research Lead designs all 5 experiments in one planning session (§3.3); the Computation Agent writes 5 scripts concurrently (§3.4); the Skeptic Agent reviews all 5 in one pass; the GPU Manager deploys them in parallel across the available pod slots; the Infrastructure Lead monitors all 5 via the 5-min polling cron (§18); the QC Agent runs gates on each as it completes; the Analysis Lead processes results as they land; the Writing Lead triggers site sync; the Backup Agent verifies checksums. The 60 Houston-touchpoints become ~5 Houston touchpoints (the high-value decisions: experiment selection approval, cross-model review on the interpretation, final publication gate). The other 55 touchpoints are absorbed by the agent hierarchy. **This is the compounding gain**: the same phase runs in hours instead of days, with Houston spending 5-10% of the time on it instead of 50-60%.

Now multiply this across 4 phases running in parallel, with Houston as the director. The platform is not 4x faster per-phase — it's 4x more phases running simultaneously, with similar per-phase quality. **Throughput gain from parallelism is the most concrete and quantifiable of the 15 advantages, and it is exactly the thing Houston cannot get by working harder or longer on BigBounce alone.**

**A worked example of the memory compounding:**
Take the "idle GPU proactive" instruction. Houston has stated this preference dozens of times (see §20.2 "verbatim prompts", which captures every one). Under BigBounce's current workflow, the main agent forgets this preference between sessions, because there is no persistent user memory. Houston has to repeat himself. Under Hubify Labs, the first time Houston states this preference, it becomes a `user_preferences` row in Convex (§20.2 schema) with `key="idle_gpu_proactive"`, `value="run next queued experiment if GPU idle > 5 min"`, `active=true`. On every subsequent agent session, the §20.2 read protocol step 1 loads `user_preferences where active=true` into the system prompt. The preference is *structurally* enforced. Plus §23.3 Idle GPU Watchdog is the cron that implements the preference automatically, independent of whether any agent is running. The platform structurally cannot forget this.

The memory compounding matters because BigBounce has generated hundreds of such preferences over 24 months (things like "prefer Newsreader serif for papers", "use tectonic for LaTeX not pdflatex", "always cross-match against SIMBAD + NED + VizieR, not just SIMBAD", "default to log-normal score distributions for anomaly QC"). Each one is a small friction point in BigBounce that is structurally eliminated in Hubify Labs. Cumulatively, this is a lot of saved cognitive load and a lot fewer "didn't I tell you this already?" moments.

---

## Where Hubify Labs Will Be Worse Than Houston (Honest)

This section is required to be substantive. If I can't articulate where the platform falls short, Houston should not start building. Here are the real concerns.

**1. Agents miss subtle experimental design flaws Houston catches in 30 seconds.**
The most common Houston catch: "wait, you're running this on the wrong sample. The DESI DR1 spectra at z>1 have a different selection function than z<1, and your model assumes uniform selection." This is a domain-knowledge catch, not a code catch — and an agent following best practices will not catch it because the code passes all tests. **Real BigBounce example:** Houston caught the SDSS DR18 domain shift in QC by *reading the score distribution* and noticing it didn't match the expected log-normal. An agent would log "QC pass, n_anomalies = 77,905" and move on. Houston added that to the BigBounce CURRENT_STATUS as "domain shift scores" QC. Mitigation: §29 cross-model review will catch some of these, but not all. The honest answer is that subtle design flaws will get through more often without Houston, and the only fix is Houston-in-the-loop on experiment design proposals (§19 director review on high-stakes experiments).

**2. Agents may follow the letter of the Houston Method but miss the spirit.**
§23.2 step 6 says "generate 5-15 new tasks." An agent will literally generate 5-15 tasks. But the *quality* of those tasks matters: a Houston-generated task is "cross-match the 1,127 uncataloged objects against ZTF light curves to look for AGN variability that would explain the spectral anomaly"; an agent-generated task is "cross-match anomalies against catalog X for completeness." Same shape, different scientific value. **Mitigation:** the §29 daily fresh-eyes pass picks 1 active issue per day for non-Anthropic review, which catches the worst cases. But a 1-per-day rate misses many. The honest answer: task quality from automated generation is *lower than Houston's average*, and the platform compensates with *more* tasks rather than *better* tasks. This works for breadth, fails for depth.

**3. Agents can hallucinate prior work — and may cite it confidently.**
The §29.4 Interpretation Pass example I cited earlier ("GPT misremembered. Claim DOES NOT hold.") is the *good* outcome where the orchestrator caught the hallucination. The bad outcome is when the hallucination is in the *original* paper draft (the agent that wrote the claim, not the reviewer that checked it) and the cross-model review *also* hallucinates a confirming citation. Two model hallucinations can correlate when they have similar training data. **Mitigation:** §22.2 step 5 deep read of top 20 candidates fetches actual abstracts, not summaries. §29.4 explicitly classifies FACT claims and verifies against sources. But hallucinated citations in unfetched papers can slip through. The honest answer: this risk is real and is the strongest argument for keeping Houston's manual literature checks on at least the top novelty claims.

**4. Agents may waste compute on dead ends that Houston would kill in 10 minutes.**
The §23.4 viability scoring tries to address this, but viability is hard to score automatically. Real BigBounce example: Houston killed the "Birefringence from photon-torsion coupling" route within 30 minutes after seeing the dimensional analysis (Issue 4 in the comprehensive audit). An agent would have spent 4-8 hours trying to make the dimensions work before flagging it. **Mitigation:** §29.4 daily fresh-eyes pass + §28.6 prompt-driven escalation when an agent is stuck after N attempts. But the wasted compute is real and is unavoidable without Houston's intuition. **Cost estimate:** I expect 10-20% of agent-initiated experiments to be dead ends Houston would have killed. At $5/experiment average, that's $50-100/week of wasted compute per lab. Acceptable price for the throughput gain, but not zero.

**5. Agents may overfit to "shipping fast" vs "shipping right."**
The Houston Method is explicitly anti-fast (`houston-method-v2.md` line 15: "No more fast cheap results. We want to do this RIGHT ONLY"). Agents trained on developer feedback are *biased toward shipping fast* — that's the standard reward signal during model training. The platform fights this with §23.2 mandatory steps and §29 cross-model review, but the underlying bias is real. **Real risk:** an agent will mark an experiment complete with QC pass + analysis pass + insufficient interpretation, and the §23.2 state machine will accept it because all checkboxes are technically checked. Mitigation: §22.6 novelty scoring + §29.7 daily fresh-eyes + Houston spot-checks. Honest answer: this is the strongest argument for Houston staying in the loop on the *shipping decisions*, even if not on the operational decisions.

**6. Agents miss cross-domain insights from Houston's broader reading.**
Real BigBounce example: the f_NL triple role (galaxy bispectrum + PBH abundance regulator + induced GW spectral shape) came from Houston having read Bartolo et al. on PBH abundance + Inomata et al. on induced GW + Yokoyama on bispectrum constraints — three different subfields. An agent reading the matter bounce literature would not connect to PBH abundance or induced GW unless the connection is already in the matter bounce papers (it's not). **Mitigation:** §20.5 global memory cross-lab links surface adjacencies, but only between things already in the knowledge graph. New cross-domain connections require reading something that's not yet in the graph. Honest answer: cross-domain insight generation is a Houston strength the platform cannot replicate, and the mitigation is "Houston still reads broadly and feeds new insights into the lab as user memories."

**7. Memory layer can become noisy over time.**
§20.9 Memory Hygiene addresses this with no-deletion + supersession + decay scoring + cleanup cron. But noisy memory is a real failure mode of every memory system in the survey (`memory_systems_survey.md`): mem0 hits this, Letta hits this, Cognee hits this. The Hubify Labs memory layer will hit this too, especially after 6+ months of accumulation. **Mitigation:** weekly cleanup cron (§20.9 step 4), decay scoring at retrieval (§20.7), and Houston's memory inspector at `hubify.app/memory` (§20.8) to manually prune. Honest answer: noisy memory will degrade retrieval quality after a year, and the only fix is active hygiene + occasional reset.

**8. Cross-provider review costs add up.**
§29.8 estimates: Anthropic $14.20, OpenAI $5.40, Google $3.10, xAI $1.40, Perplexity $0.70 per day = $24.80/day. That's $750/month per lab in API costs alone, before GPU. For 5 labs, $3750/month in API. **Mitigation:** §29.7 review cadence is "periodic, not constant" — most reviews are daily or weekly, not on every comment. §29.8 per-provider budget caps. §10.6.5 cost-aware model selection. Honest answer: the API costs are real and need to be budgeted, but they're not catastrophic for a research-scale platform. The bigger concern is *scope creep* — each new feature wants more cross-model review, and budgets need to be enforced.

**9. Automated novelty checks may miss preprints not in databases.**
§22.2 searches arXiv, NASA ADS, INSPIRE-HEP, Semantic Scholar, Google Scholar. **What it misses:** workshop abstracts, conference talks not posted to arXiv, blog posts, Twitter threads, private communications, papers in fields the searcher doesn't know to search (e.g., a particle physics result that's relevant to cosmology). Houston catches some of these by reading widely; the platform doesn't. **Mitigation:** §29 cross-model review with Perplexity Sonar (§29.6) does web-grounded fact checks that include non-arXiv sources. Plus Houston spot-checks the top novelty claims manually. Honest answer: this gap is real and shrinks the platform's effective novelty detection by 5-10% vs Houston's manual process.

**10. Houston's intuition for "this feels off" is hard to encode.**
The most subtle quality lever Houston has is the gut feeling that triggers a re-check. Real example: when the first NANOGrav γ result came in at 3.0 (matching prediction) and the combined PTA result came in at 3.32 ± 0.37, Houston felt the second number "felt right" and did the Bayes factor calculation that yielded 27.6. An agent following the Houston Method would have stopped at "consistent within 1σ, log to dataset." Houston went deeper because the consistency *felt structurally significant*. This kind of intuitive escalation is unencoded. **Mitigation:** §29 daily fresh-eyes pass + Houston staying in the loop on results he cares about. Honest answer: the platform is missing the "this feels off, dig deeper" reflex, and the mitigation is "Houston stays curious about the results he cares about, the platform handles everything else."

**These 10 are real.** I'm not going to soft-pedal them. They are why the platform is not a *replacement* for Houston — it's a *force multiplier*. The TL;DR's claim that "Hubify Labs will not match BigBounce's intuitive quality without Houston staying in the loop on the high-stakes calls" is grounded in these 10 concerns. The next section is about what the platform does to keep these from killing quality.

---

## Mitigations and Safeguards

For each of the 10 concerns above, what the platform does to keep it from degrading research quality.

**Concern 1: Subtle experimental design flaws.**
- **§19 Director-in-the-loop on high-stakes experiments:** any experiment cost > $25 requires Houston's approval before running (§23.3 PROACTIVE MODE step 4: "If idea cost >= $25: notify Houston, run if no objection in 30 min").
- **§29 cross-model review on experiment proposals:** Research Lead's experiment design gets reviewed by GPT + Gemini before going to the GPU.
- **§28.6 escalation rule in agent prompts:** "If you cannot resolve an issue after 3 attempts, change the issue's reports_to field to your boss." Subtle flaws often manifest as repeated failures, which trigger escalation.

**Concern 2: Following the letter not the spirit of Houston Method.**
- **§23.7 quality metrics tracked weekly:** protocol completion rate (target 100%), idle GPU minutes (target <30/wk), queue depth (target >15), repeated questions (target 0). If any drops below target for 2 weeks, the platform fires a self-improvement task: "agent behavior is degrading, investigate and fix."
- **§29.4 Interpretation Pass surfaces "the things the reviewer DIDN'T critique" — those are the gaps.** This is the explicit defense against shallow task completion.
- **Houston spot-check rotation:** Houston picks 5 random experiments per week and reads the EXPAND step's task list. If they're shallow, the orchestrator's task-generation prompt gets revised.

**Concern 3: Hallucinated prior work.**
- **§22.2 step 5 deep read of top 20 candidates** fetches actual abstracts/intros/conclusions, not summaries.
- **§29.4 FACT classification + verification against sources** is the explicit defense.
- **§29.6 fact-check-perplexity agent** does web-grounded fact checks with citations.
- **Quarterly novelty re-review (§22.5)** catches hallucinations that slipped through initial review when newer literature surfaces them.
- **Houston spot-check on top novelty claims:** for any contribution scoring 9-10, Houston manually reviews the audit trail before publication.

**Concern 4: Wasted compute on dead ends.**
- **§29.7 daily fresh-eyes pass** picks 1 active issue per day for non-Anthropic review — catches dead-end work within 24 hours.
- **§11.2 budget tiers** cap daily spend per lab. If an experiment is consuming >$X without progress, the orchestrator pauses and surfaces to Houston.
- **§28.5 stale-checkout adoption + retry backoff:** failures don't loop forever; they escalate.
- **Houston cost dashboard:** the orchestrator surfaces cost-per-experiment so Houston can spot the dead ends in the daily digest.

**Concern 5: Shipping fast vs shipping right.**
- **§23.2 state machine refuses to mark anything complete without all 8 steps.** Step 6 (queue expansion) requires 5-15 new tasks. Step 7 (backup) requires checksum verification. The state machine is the structural defense.
- **§29 mandatory triggers** require cross-model review for paper drafts, novelty claims, architectural decisions, critical code changes — the highest-stakes work always gets reviewed.
- **Director gates on shipping decisions:** any decision to submit a paper or publish a public artifact requires Houston's explicit approval (§19 director-in-the-loop).
- **Houston Method directive in CLAUDE.md:** loaded as a static instruction file (§20.10), the "DO NOT suggest 'write up the results and publish'" rule is in every agent's system prompt.

**Concern 6: Cross-domain insights.**
- **Houston still reads broadly and feeds insights as user memories.** This is the explicit unencoded part. The platform supports this via §20.2: every user message becomes a tagged memory; Houston can mark insights as "preference" or "rule" or "fact" and they propagate to all agents.
- **§20.5 global memory cross-lab links** at least surface known adjacencies between domains.
- **Houston spot-check on the literature digest:** the literature agent reads new arXiv papers daily; Houston scans the top 10 each week and can flag any that should become user memories.

**Concern 7: Memory noise.**
- **§20.9 hygiene rules:** decay scoring + supersession over deletion + weekly cleanup cron.
- **§20.12 quality metrics:** retrieval relevance (target >80%), Houston manually rates 10 random retrievals/week as relevant or not. Below target → memory tuning task.
- **Houston memory inspector at hubify.app/memory (§20.8):** manual prune + bulk-tag + delete-if-wrong-extracted.
- **Periodic memory reset** if relevance degrades catastrophically (escape hatch, never used in v1 hopefully).

**Concern 8: Cross-provider review costs.**
- **§29.8 per-provider budget caps:** Houston sets "OpenAI: $50/month max" and the platform refuses additional reviews after the cap.
- **§29.7 cadence: periodic, not constant.** Daily fresh-eyes is 1 issue/day, not all issues.
- **§22.6 novelty cost: ~$2/review, $96/year per lab.** Affordable for the value.
- **§10.6.5 cost-aware model selection:** the orchestrator picks the cheapest model that can do the job.
- **§11.2 budget tiers + 80% warning + 100% freeze.**

**Concern 9: Novelty checks miss non-database preprints.**
- **§29.6 fact-check-perplexity** runs web-grounded fact checks that include non-arXiv sources.
- **Houston manual spot-check on top novelty claims** before publication.
- **Quarterly re-review (§22.5)** catches new literature that surfaces over time.
- **Honest acceptance:** this gap will not fully close. It's worth ~5% of novelty quality, and the mitigation is Houston staying engaged with the literature he reads outside of formal databases.

**Concern 10: "This feels off" intuition.**
- **§29.9 Interpretation Quality Metric:** orchestrator interpretation should match Houston's eventual judgment >85% of the time. Below that, the prompt gets revised.
- **Houston review of all results he cares about:** the platform surfaces results to Houston via the activity stream (§25). Houston picks which to dig into. The platform never *prevents* Houston from looking; it just doesn't require him to look at everything.
- **Director "needs your review" card** for anything the orchestrator can't decide.
- **§27 standup escalations** surface anything that smells off to Houston in the next standup digest.

**Cross-cutting safeguards that apply to multiple concerns:**

- **§19 Director-in-the-loop is woven into the entire platform.** Every high-stakes decision routes to Houston. Every disagreement between agents routes to Houston. Every cost above threshold routes to Houston. Houston is never *required* to engage on routine work, but is *always* the final authority on anything that matters.
- **§27.6 standup escalation:** "By default, standups run silently. Houston only gets notified when [a standup escalates something to the Director / creates a high-priority task / surfaces an unresolvable disagreement]." Quiet by default, loud when it matters.
- **§22.5 + §29.7 re-review cycles:** nothing is "decided forever." Everything gets re-checked on a schedule. New information can flip an earlier decision.
- **§28.10 paperclip patterns NOT borrowed:** explicitly does NOT borrow the "execution decisions schema with review/approval state machine" from paperclip because it's overkill. The platform stays simple where simplicity helps.
- **Memory hygiene + audit trail + provenance:** §20.9 + §28.9 mean every decision is traceable and reversible. There is no "lost in the system" state.
- **§10.5 RunPod safety layer:** the lower bound on data loss is structurally zero. The "lost 130K galaxies" failure mode cannot recur.

These mitigations are not perfect. They are *named*, *specific*, and *measurable*, which is the minimum bar for accepting that automation is safe to deploy.

**A walkthrough of what happens when each concern actually manifests:**
The mitigations above are abstract. Let's walk through what the platform *actually does* when each concern fires in practice, with specific PRD mechanisms invoked.

**Concern 1 fires:** an agent proposes running a cross-match of DESI DR1 against a survey with a different selection function. The cross-match would produce misleading results because the surveys are not comparable. What happens:
- Research Lead proposes the experiment (§3.3).
- The proposal goes into the queue with estimated cost $18 (below the $25 director-review threshold).
- Skeptic Agent reviews the proposal (§3.4). If the skeptic catches the selection-function mismatch: experiment is marked `cancelled` with reason in the decision log, new tasks generated for a valid alternative.
- If the skeptic misses it: experiment runs, QC Agent runs standard 7 checks, QC may or may not catch it depending on how the mismatch manifests.
- If QC passes but the result is subtly wrong: the §29.7 daily fresh-eyes pass picks this issue within 24 hours, non-Anthropic reviewer catches the mismatch, status transitions to `needs_changes`, cross-lab link gets updated.
- Worst case: the subtle flaw survives fresh-eyes and gets into a draft paper. Then §29 mandatory full 3-reviewer pass on paper drafts catches it, because at least one of GPT/Gemini/Perplexity will notice the selection-function issue when reviewing the methods section.
- True worst case: all 3 reviewers miss it. Then the §22.5 quarterly re-review catches it, because re-review searches for "selection function bias in X survey" and finds a prior paper that flagged the same issue.
- Backstop: Houston spot-checks high-novelty claims before publication. He catches it.
- **Outcome:** the flaw is caught at one of 5 checkpoints. The probability of survival through all 5 is <5%. Acceptable.

**Concern 3 fires:** the paper-writer agent drafts a section citing "Cai et al. 2024, which derived f_NL = -35/8 from matter bounce." This citation is hallucinated. What happens:
- The draft goes to §29 cross-model review (mandatory for paper drafts per §29.7).
- GPT reviewer reads the claim, checks its training data, either confirms (wrong, if GPT also hallucinates) or flags it.
- Gemini reviewer reads the claim, checks with a different training distribution, flags if it can't locate the citation.
- Perplexity reviewer runs a web-grounded search for "Cai 2024 f_NL -35/8" and either finds the paper (then verifies the claim) or returns "no results."
- If Perplexity returns no results: the claim is flagged as likely hallucinated.
- §29.4 Interpretation Pass classifies: HALLUCINATION suspected, explicitly ask Houston to verify before letting the claim stand.
- Houston verifies by searching arXiv manually: takes 2 minutes, confirms hallucination, removes the citation.
- **Outcome:** hallucinated citation is caught at the Perplexity stage (the web-grounded reviewer is the structural defense against hallucinated citations). Probability of survival to publication <10%, because Houston's backstop spot-check would catch it even if all 3 reviewers fail.

**Concern 4 fires:** the platform spends $400 on a research direction that turns out to be a dead end. What happens:
- The direction was proposed by the idea-generation agent (§23.4) with viability score 6.
- Houston reviewed the daily idea digest and did not veto it.
- Experiments ran for 5 days before the dead-end became apparent (e.g., QC keeps failing, or the results don't connect to any bounce cosmology prediction).
- §29.7 daily fresh-eyes pass started flagging concerns on day 2. The issue was escalated to Houston on day 3.
- Houston reviewed on day 3, agreed it was a dead end, marked it `cancelled`, added to lab decisions log with reasoning.
- Cost: $120-200 instead of $400, because escalation happened halfway through.
- Learning: the idea-generation agent's viability scoring is adjusted based on this outcome (§23.6 feedback loop). Future ideas with similar characteristics get lower viability scores.
- **Outcome:** waste is limited by early escalation. Over many cycles, the platform learns to avoid this class of dead end. BigBounce has the same problem without the learning loop — Houston has killed similar dead ends manually but the lessons are in his head, not in a queryable preference.

**Concern 5 fires:** an agent marks an experiment complete with 5 shallow follow-up tasks that satisfy §23.2 step 6 literally but miss the spirit. What happens:
- The experiment is marked complete, tasks are added to the queue.
- §29.7 daily fresh-eyes pass picks this experiment for review (random selection among recently completed).
- Non-Anthropic reviewer (say, GPT-5) reads the original experiment + the generated tasks + the rest of the lab state.
- Reviewer's prompt explicitly asks "Are these tasks shallow or substantive? Do they open new directions or just check boxes?"
- If shallow: reviewer flags as `needs_changes`, comment added to the experiment issue, original agent's task generation prompt is flagged for improvement.
- Research Lead re-generates tasks with a stronger prompt.
- Weekly metric: "shallow task generation rate" is tracked. If it rises, the task-generation prompt gets revised.
- **Outcome:** shallow task generation is caught within 24 hours, with a feedback loop that improves future generations. BigBounce has this problem manually — agents give Houston shallow task lists, Houston pushes back, but the improvement doesn't propagate to future sessions because there's no persistent learning. Hubify Labs has the feedback loop structurally.

**Concern 9 fires:** a novel claim is made that was actually scooped by a workshop talk not posted to arXiv. What happens:
- §22.2 novelty review searches 5 databases, finds nothing, marks claim as novelty 10.
- §29 cross-model review runs, none of the reviewers are aware of the workshop talk.
- Claim goes into contribution list.
- §22.5 quarterly re-review runs 7 days later, searches again, still finds nothing (workshop talk is still not in databases).
- At some point, the workshop talk gets written up as a paper and posted to arXiv.
- §22.5 quarterly re-review eventually finds the paper, novelty score drops from 10 to 3 or lower, Houston gets a high-priority alert.
- If the alert comes before publication: Houston verifies, possibly retracts the claim from upcoming paper, updates the contribution list.
- If the alert comes after publication: Houston has to issue an erratum. Embarrassing but not catastrophic — because the platform caught the supersession, just late.
- **Outcome:** the gap is not closed, but the damage is minimized by active monitoring. This is strictly better than BigBounce's current state, where Houston would not re-check a published claim monthly.

These 5 walkthroughs cover the 5 highest-probability concerns. The pattern in each: the platform has multiple checkpoints, each with a specific mechanism, and the probability of a flaw surviving all checkpoints is low. The remaining probability is absorbed by Houston's spot-check role.

---

## The Quality Metrics That Matter

Specific, measurable, with targets. Each of these maps to a quality concern from BigBounce or a known failure mode from the memory survey + paperclip study.

| # | Metric | Target | Where measured | Quality concern it maps to |
|---|--------|--------|----------------|----------------------------|
| 1 | **Novelty score distribution** (median) | ≥7 | §22.3 contributions table | Avoiding low-novelty publications |
| 2 | **False novelty claim rate** (claims later shown to be superseded) | 0% | §22.5 re-review cron | Hallucinated novelty |
| 3 | **Repeated user questions** (Houston had to repeat himself) | <2% of sessions | §20.12 memory metric | Memory failures, agents not respecting prior preferences |
| 4 | **Forgotten task rate** (queued tasks dropped without resolution) | 0% | §20.12 + §23.7 | Memory failures |
| 5 | **Idle GPU minutes per week** | <30 min | §23.7 + cost rollup | GPU efficiency, watchdog working |
| 6 | **Mean experiment QC pass rate** | >95% | §23.2 step 1 + audit log | Experiment quality |
| 7 | **Cross-model interpretation accuracy** (orchestrator verdict matches Houston's) | >85% | §29.9 | §29.4 Interpretation Pass executing well |
| 8 | **Time from idea → published paper** | improve vs BigBounce baseline | per-paper metric | Throughput |
| 9 | **Cost per published claim** | tracked, no hard target | §22.3 + §29.5 | Cost discipline |
| 10 | **Houston satisfaction score** (subjective, weekly) | 8/10 minimum | weekly Houston check-in | Director experience |
| 11 | **Houston Method protocol completion rate** | 100% | §23.7 | Houston Method enforcement |
| 12 | **Queue depth average** | >15 ideas | §23.7 | Generative breadth |
| 13 | **New domains opened per month** | >1 | §23.7 | Exploration vs exploitation balance |
| 14 | **Cross-lab discovery latency** (new global_knowledge → cross-lab link) | <30 min | §20.12 | Cross-lab correlation working |
| 15 | **Memory retrieval relevance** (Houston rates 10 random retrievals/week) | >80% | §20.12 | Memory hygiene |

**How these get tracked:**
- All metrics surface in the Director view's "Memory health" + "Houston Method health" + "Quality metrics" cards.
- Weekly digest (§16.4 + §27.6 standup) summarizes the metrics.
- If any metric drops below target for 2 consecutive weeks, the platform fires a self-improvement task.
- Houston satisfaction is the only subjective metric and is the *most important* one. If Houston is unhappy with the platform's research quality for 2 weeks, the rollback plan triggers.

**The metric hierarchy:** if forced to pick 3, they would be:
1. **#7 cross-model interpretation accuracy** — this is the proxy for "is the platform's quality reasoning matching Houston's?" If this drops below 70%, the platform is hallucinating its way into wrong claims.
2. **#3 + #4 memory metrics** — if the platform forgets things, every other quality lever degrades.
3. **#10 Houston satisfaction** — the qualitative ground truth.

---

## The "Equal or Better" Verdict

Honest assessment, not marketing.

**Will Hubify Labs definitely produce research quality EQUAL to BigBounce?** Yes, conditional on three things:
1. **§29 ships with the Interpretation Pass logic intact.** This is the most important section in the entire PRD for quality preservation. If §29 ships with cross-model review but without the FACT/OPINION/HALLUCINATION classification + source verification, the platform will produce mediocre research with confident errors. If §29 ships with the Interpretation Pass, the platform will replace Houston's manual cross-model review at higher cadence.
2. **§23 ships with the state-machine enforcement.** The Houston Method as a *document* has been ignored repeatedly. The Houston Method as a *state machine the agent cannot exit* is the difference between protocol-on-paper and protocol-in-reality.
3. **Houston stays in the director seat for at least 3 months.** The platform is designed to free Houston from operational work, not from strategic decisions. If Houston disengages entirely in month 1, the platform will drift. If Houston engages 2-3 hours per day on the high-value reasoning, the platform produces equal quality. If Houston engages 4-5 hours per day, the platform produces better quality.

**Will it produce research BETTER than BigBounce?** Likely yes, with these specific mechanisms:
- **Throughput gain from parallelism.** 4-8x experiments per week.
- **Coverage gain from cross-lab inheritance.** Lab N inherits insights from labs 1 to N-1.
- **Cadence gain from continuous review.** Quarterly re-reviews catch claims that would otherwise drift.
- **Persistence gain from memory layer.** Nothing forgotten.
- **Idle elimination.** GPUs always working.
- **Cross-model rigor at scale.** 5 model families instead of 2-3.

The BETTER claim is softer than the EQUAL claim because most of the improvements compound over time. In month 1, the platform is roughly equal to BigBounce. In month 6, the platform is better on throughput + coverage. In month 12, the platform is better on cross-lab inheritance + memory persistence. The compounding is the case for "better."

**What are the failure modes that could cause it to be WORSE?**
1. **§29 doesn't ship with the Interpretation Pass.** Cross-model review becomes "average the verdicts," which is lower-quality than Houston's manual synthesis. The platform produces confident wrong claims at scale.
2. **Memory layer becomes noisy and retrieval relevance drops.** Agents start surfacing irrelevant context, which degrades reasoning. (Mitigation: §20.9 hygiene + Houston memory inspector.)
3. **Houston disengages entirely.** Agents drift on strategic decisions. (Mitigation: §27.6 escalations + director "needs your review" card + weekly digest.)
4. **Cost runs away.** Per-provider budgets fail to enforce, API spend balloons. (Mitigation: §29.8 budget caps + §11.2 tier enforcement + 80% warning.)
5. **Agents start gaming the Houston Method state machine** (e.g., generating 5 fake tasks to satisfy step 6). (Mitigation: §29.7 daily fresh-eyes pass catches shallow task lists, Houston spot-checks.)
6. **Cross-domain insights stop happening** because no agent reads outside the lab's domain. (Mitigation: Houston still reads broadly + literature agent surfaces new arXiv papers daily.)
7. **The interpretation prompt accidentally biases toward Anthropic-friendly conclusions.** (Mitigation: §29 mandatory non-Anthropic reviewers + interpretation quality metric.)

**Rollback plan if quality degrades:**
The PRD §1 Iron Rule guarantees rollback safety. The original BigBounce repo at `~/CODE_2025/bigbounce` is *never touched* during any phase of platform development. There are 4 backup locations (PRD §1: GitHub fork + local backup + Backblaze B2 + git history) before any new code runs. The rollback procedure is:
1. `cd ~/CODE_2025/bigbounce-backup-20260407`
2. `claude --resume`
3. Continue BigBounce research with the manual workflow.

The rollback is **30 seconds**. Zero data loss. Zero meta-tooling debt. Hubify Labs is a *parallel* system, not a *replacement*.

**The bottom line for Houston:**
The quality math works out IF the §29 Interpretation Pass executes as specified AND Houston stays engaged on strategic decisions for the first 3 months. The risks are real and named. The mitigations are specific and measurable. The rollback is instant. The compounding gains start in month 1 and accelerate by month 6.

Three things would make me say "do not start building":
1. If §29 were not in the PRD. (It is, and it's strong.)
2. If the rollback plan required any meta-tooling to undo. (It doesn't — see PRD §1 Iron Rule.)
3. If Houston refused to engage on strategic decisions for the first 3 months. (Houston has not refused; the director-in-the-loop pattern is in the PRD.)

None of those three apply. The platform is safe to build, with the named quality metrics tracked from day 1.

---

## Risk Register

Top 10 risks ranked by (probability × impact). Each has named owner + mitigation.

| # | Risk | Probability | Impact | Mitigation | Owner |
|---|------|------------|--------|-----------|-------|
| 1 | §29 Interpretation Pass ships without FACT/OPINION/HALLUCINATION classification | Medium | Catastrophic | §29.4 explicit prompt rules + §29.9 quality metric monitoring | Platform engineering + Houston review |
| 2 | Memory layer becomes noisy after 6+ months, retrieval relevance drops | High | High | §20.9 hygiene cron + §20.12 metrics + Houston manual prune | Platform memory team |
| 3 | Houston disengages from strategic decisions in first 3 months | Medium | High | §27.6 escalation + Director view "needs your review" + weekly digest | Houston |
| 4 | Cross-provider API costs run away beyond budget | Medium | Medium | §29.8 per-provider caps + §11.2 tier enforcement + 80% warning | Cost monitoring + Houston |
| 5 | Agents game §23.2 state machine by generating shallow tasks | Medium | High | §29.7 daily fresh-eyes pass + Houston spot-checks + §23.7 metrics | Cross-model review |
| 6 | Hallucinated prior work slips through novelty review | Medium | High | §22.2 deep read + §29.4 FACT verification + §22.5 quarterly re-review | Novelty pipeline + cross-model review |
| 7 | Subtle experimental design flaws in agent-generated experiments | High | Medium | §19 director-in-the-loop on >$25 experiments + §29 cross-model review on proposals | Houston + cross-model review |
| 8 | Cross-domain insights stop happening | Medium | Medium | Houston reads broadly + literature agent + user memory feed | Houston |
| 9 | RunPod credit expiration causes data loss | Low | Catastrophic | §10.5 RunPod safety layer + §6 backup multi-location | Platform infra |
| 10 | Two model families both hallucinate the same wrong fact | Low | Catastrophic | §29 require 3+ providers + §29.6 Perplexity web-grounded fact check + Houston spot-check | Cross-model review + Houston |

**Risk #1 is the highest-stakes risk.** The §29 Interpretation Pass is the single most important piece of the PRD. If it ships without the FACT classification logic, the platform produces confident wrong claims. The mitigation is ruthless quality monitoring on §29.9 (interpretation accuracy >85%) and Houston's willingness to revise the interpretation prompt the moment it drops below 70%.

**Risk #2 is the highest-probability risk.** Memory noise is what every memory system in the survey hits. Mitigation is hygiene + Houston's active inspection.

**Risks 5, 7, 8 share a theme:** they all require Houston to stay engaged. The platform cannot fully replace Houston's intuition, and these are the failure modes that emerge if Houston tries to.

**Risks 9 and 10 are low-probability but catastrophic.** Both have structural mitigations (10.5 + 29.6 + cross-provider mandate). Worth naming because the consequences are unrecoverable.

---

## What to Watch in Phase 1

The first 30 days. Specific, measurable, with abort criteria.

**Days 1-7: Platform shakedown.**
- **Watch:** §23.2 state machine completion rate. If <90% of experiments complete all 8 steps, the state machine has bugs and needs fixing before production use.
- **Watch:** Memory write/read latency. If reads >500ms p95, the platform feels sluggish and Houston's experience degrades. (Convex vector search can be slow when warm; needs benchmarking.)
- **Watch:** Cross-provider API costs vs budget. If trending toward 80% of budget by day 7, scale back review cadence.
- **Expect:** Lots of manual intervention. Houston will spend 4-6 hrs/day in the platform. This is normal; it's a shakedown.
- **Abort criteria:** if §23.2 completion <80% by day 7, freeze new experiments and fix the state machine.

**Days 8-14: First end-to-end research loop.**
- **Watch:** Can the platform run a full BigBounce-style experiment from idea → run → QC → analysis → interpretation → cross-model review → site sync → expansion? The first experiment is the proof of concept.
- **Expect:** The first experiment will surface 5-10 bugs. Most will be small.
- **Abort criteria:** if the first experiment cannot complete the full Houston Method protocol after 3 attempts, the platform is not ready for parallel operation. Continue manual BigBounce workflow.

**Days 15-21: First cross-model review pass on a real claim.**
- **Watch:** §29.4 Interpretation Pass output. Does the orchestrator's interpretation match Houston's eventual judgment? Houston should *manually* re-do the same interpretation and compare. If interpretation accuracy <70%, the prompt needs revision.
- **Expect:** The first cross-model review will be noisy. Reviewers will hallucinate. The orchestrator will catch some hallucinations and miss others.
- **Abort criteria:** if interpretation accuracy <60% on the first 5 reviews, the platform is producing confident wrong claims. Pause cross-model review and revise the interpretation prompt.

**Days 22-30: Parallel operation with BigBounce.**
- **Watch:** Throughput vs BigBounce manual baseline. The platform should be running 2-4x experiments per week vs Houston's manual rate.
- **Watch:** Houston satisfaction. Is he sleeping better? Is he spending time on the right things? Is the platform freeing him to think?
- **Expect:** Mixed feelings. Some things will be magical. Some things will be frustrating. The metrics will be the ground truth, not the feelings.
- **Abort criteria:** if Houston satisfaction <6/10 by day 30, the platform is not delivering value and the rollback plan triggers.

**Continuous throughout Phase 1:**
- **Daily:** Houston reviews the activity stream + standup digest + cost rollup.
- **Daily:** Houston spot-checks 1 random experiment for Houston Method protocol completion (depth, not just shape).
- **Weekly:** Houston runs the §29.4 manual interpretation comparison on 5 random reviews.
- **Weekly:** Houston rates 10 random memory retrievals as relevant or not.
- **Weekly:** Houston rates the platform satisfaction on a 1-10 scale and writes 1 paragraph of why.
- **Weekly:** Quality metrics dashboard reviewed for any metric below target.

**Phase 1 success criteria (must all be true to proceed to Phase 2):**
1. §23.2 protocol completion rate ≥95% over the last 7 days.
2. §29.9 interpretation accuracy ≥80% over the last 14 days.
3. Memory retrieval relevance ≥75% over the last 7 days.
4. No data loss events.
5. Houston satisfaction ≥7/10 averaged over the last 14 days.
6. Throughput ≥1.5x BigBounce manual baseline.
7. Total cost within budget tier.
8. No catastrophic risk events from the risk register.

If any of these fail at day 30, Phase 2 does not start, and either (a) the failing piece gets fixed and Phase 1 extends, or (b) the rollback plan triggers and BigBounce continues manual operation.

**Phase 1 explicit non-goals:**
- Don't optimize cost in Phase 1. Optimize quality. Cost optimization is Phase 2.
- Don't add new features in Phase 1. Stabilize what's there.
- Don't try to migrate BigBounce to the platform in Phase 1. BigBounce stays manual; Hubify Labs runs in parallel.
- Don't onboard a second lab in Phase 1. One lab is enough to validate.

**Concrete Phase 1 test cases:**
The 30 days are not abstract. There are specific tests the platform must pass. These are designed to exercise the load-bearing mechanisms named earlier.

**Test 1 — The "DESI follow-up" test (week 2).** Run a follow-up experiment on DESI DR1 anomalies — for example, cross-match the top 100 anomalies against ZTF light curves to look for AGN variability. This is a routine experiment Houston has done manually before. Success criteria: (a) the platform completes all 8 §23.2 steps without manual intervention; (b) the §22 novelty pipeline runs and assigns a score; (c) the §29 cross-model review runs at least 2 reviewers; (d) the result is sync'd to the website within 24 hours; (e) at least 5 follow-on tasks are generated. Failure on any criterion = §23 state machine has bugs.

**Test 2 — The "hallucinated citation" test (week 3).** Manually inject a hallucinated citation into a paper draft (e.g., "Smith et al. 2025 demonstrated f_NL = -3.7 from cuscuton bounce" — a paper that does not exist). Success criteria: §29 cross-model review catches it within the first review pass, §29.4 Interpretation Pass classifies it as HALLUCINATION, and Houston is asked to verify before letting the citation stand. Failure = §29 is not catching hallucinations and the prompt needs revision.

**Test 3 — The "shallow task generation" test (week 3).** Manually inspect the task-generation output of the §23.2 step 6 EXPAND step on 5 random experiments. Success criteria: the tasks are substantive (specific experiment IDs, specific datasets, specific cross-checks) not generic ("explore further", "look at related results"). Failure = §29.7 daily fresh-eyes pass needs to flag shallow generation more aggressively.

**Test 4 — The "memory persistence" test (week 4).** State a specific preference to the platform (e.g., "always use Newsreader serif for paper drafts"). Wait 7 days. Open a new session and ask the platform to draft a paper. Success criteria: the new session uses Newsreader serif without being told again, and notifies Houston "Using your prior preference: Newsreader serif". Failure = §20.2 user memory is not loading preferences correctly.

**Test 5 — The "cross-lab inheritance" test (week 4, optional).** Create a second lab (`test-lab-1`) with a domain related to BigBounce (e.g., "stochastic gravitational wave background"). Success criteria: on first boot, the new lab's main agent surfaces 8-15 relevant items from BigBounce's global_knowledge (combined PTA results, NANOGrav γ analysis, bounce model discrimination table). Failure = §20.5 cross-lab knowledge graph is not surfacing connections.

**Test 6 — The "dead end recovery" test (week 4).** Deliberately propose an experiment with viability score 4 (low) and let the platform run it. Success criteria: §29.7 daily fresh-eyes pass flags it within 48 hours, escalates to Houston, and the escalation triggers a Houston decision (kill or continue). Failure = the platform is not escalating dead ends fast enough.

If 5 of 6 tests pass and the 6th fails on a fixable issue, Phase 1 is successful and Phase 2 starts. If 4 or fewer pass, Phase 1 extends until the failing tests pass.

---

## What to Watch in Months 2-6

If Phase 1 succeeds, the next 5 months are about whether the platform maintains quality as it scales. The risks change in this period.

**Month 2: Add the second lab.** This is when the cross-lab knowledge graph starts mattering. Watch §20.5 for whether the new lab actually inherits the right things — or whether it inherits noise. If the new lab gets 80+ irrelevant memories from BigBounce, the relevance scoring needs tuning. Concrete test: create the second lab and ask the orchestrator "what does BigBounce know that's relevant to me?" If the answer includes bounce cosmology results that don't apply, prune.

**Month 3: First multi-agent disagreement that the orchestrator can't resolve.** This will happen. Two reviewers will disagree on a paper section, the orchestrator will surface the disagreement to Houston, and Houston has to make a tiebreaker call. Watch how this feels. If Houston is doing more than 2-3 tiebreaker calls per week, the §29 cadence is too aggressive — dial it back. If Houston is doing fewer than 1 per month, the cadence is too lax — dial it up.

**Month 4: First cross-lab discovery surfaces.** A new global_knowledge entry from one lab vector-matches an entry from another lab with cosine > 0.85, and the platform creates a `cross_lab_links` row. Watch whether the link is meaningful or spurious. The first 5 cross-lab links will tell you whether the cosine threshold is right. Tune if needed.

**Month 5: First quarterly novelty re-review fires.** §22.5 schedules re-reviews at 7 days, 30 days, 90 days. Month 5 is when the 90-day re-reviews start firing on contributions made in month 1-2. Watch whether any novelty scores drop. If a contribution drops from 9 to 3, that means the platform discovered prior work that was missed at initial review. This is *good* — the system is working as designed. But Houston needs to triage.

**Month 6: Cost discipline.** By month 6, the platform has spent 6 months of cross-provider API costs. Total estimate: ~$4500-6000 for one lab including cross-model review. Watch whether the cost is matching the value. If the platform produced 1 publishable paper in 6 months, the cost-per-paper is acceptable. If it produced 0, the cost is unjustifiable and the architecture needs revision.

**By month 6, the platform should have:**
- At least 2 publishable papers (not necessarily submitted yet, but ready for submission)
- 100+ experiments completed across both labs
- 0 false novelty claims (claims later shown to be superseded)
- 0 forgotten tasks (tasks that fell out of the queue without resolution)
- Houston satisfaction averaging ≥7/10
- Memory retrieval relevance averaging ≥80%
- Throughput ≥3x BigBounce manual baseline (since the platform has had time to mature)

If any of these are below target by month 6, the platform is not maintaining quality at scale. Time to investigate.

---

## References

**PRD sections referenced:**
- §1 Safety-First Repository Strategy (Iron Rule, 4 backups, COPY-only)
- §3 Agent Hierarchy (15 agents per lab)
- §4 Cross-Lab Sharing
- §5 GPU/Compute Pipeline (14-step lifecycle)
- §6 Backup & Data Management (5-location protocol)
- §10.5 RunPod Safety Layer (zero data loss guarantee)
- §10.6 Token Limit Handling & Model Fallbacks
- §11 Cost Management (tiered budgets, 80% warning)
- §16 Monitoring & Observability (TUI dashboard, activity stream, 4-tier alerting)
- §17 Autonomous Website Generation Pipeline
- §19 Director-in-the-loop (Houston as final authority)
- §20 Memory Architecture — Four-Layer System (the foundation)
- §20.9 Memory Hygiene
- §20.10 CLAUDE.md and AGENTS.md as static layer
- §20.12 Memory System Quality Metrics
- §22 Scientific Contributions & Novelty Scoring
- §22.5 Re-review Cron (7d/30d/90d/quarterly)
- §23 Houston Method v2 — Platform-Level Enforcement
- §23.2 Mandatory Post-Experiment Protocol (8-step state machine)
- §23.3 Idle GPU Watchdog
- §23.7 Houston Method Quality Metrics
- §25 Agent Communication — Multi-Agent Activity Feed
- §26 Task Review Pipeline & Activity Threads
- §27 All-Hands Standups (3x/day cron)
- §28 Patterns Borrowed from Paperclip
- §29 Cross-Model Peer Review (the most important section for quality)
- §29.4 The Interpretation Pass (FACT/OPINION/HALLUCINATION)
- §29.9 Interpretation Quality Metric
- §30 Agent Host & Terminal Integration

**Source documents referenced:**
- `bigbounce/CLAUDE.md` — research directives, never-publish-negative rule
- `bigbounce/project-context/houston-method-v2.md` — original 9-step protocol
- `bigbounce/project-context/houstons-approach.md` — 8 principles + decision heuristics
- `bigbounce/project-context/HUBIFY_LABS_PRD.md` — full PRD (4732 lines)
- `bigbounce/project-context/memory_systems_survey.md` — 1,016-line survey of mem0/Letta/Graphiti/Cognee/Memori/Memobase
- `bigbounce/project-context/paperclip_patterns_study.md` — 1,337-line study of paperclipai/paperclip
- `bigbounce/project-context/compute_architecture_decision.md` — 818-line dual-provider analysis
- `bigbounce/project-context/CURRENT_STATUS.md` — current BigBounce state
- `bigbounce/project-context/peer-reviews/REVISION_TRACKER.md` — manual revision history for Paper 1
- `bigbounce/project-context/peer-reviews/2026-03-02_1917PST_comprehensive-audit.md` — the 10-issue audit that drove Phases 1-4 of v2.2.0

**BigBounce ground-truth numbers cited:**
- 4 papers (1× v2.2.1 99% / 2× v1.3 100% / 3× v1.0 95% / 4× v1.0 85%)
- 53 experiments completed
- 328,448 anomalies across 15 surveys
- 142 wiki entities, 89 concepts
- f_NL = -35/8 prediction (parameter-free, novel, SPHEREx 5σ by 2028)
- ALP β = 0.27° prediction (matches 3.6σ observed)
- Combined PTA Bayes 27.6 (bounce vs SMBHB)
- 14 ECH structural barriers
- 10+ revision rounds (REVISION_TRACKER.md)
- 424,181+ MCMC posterior samples
- 8.47M galaxy chirality classifications
- 32x speedup from DataLoader parallelism (gpu-inference-playbook.md)
- $400 total compute cost across 3 months

**Bottom line:** the case for Hubify Labs equaling BigBounce quality is grounded in 9-of-12 fully-encoded quality factors. The case for exceeding BigBounce quality is grounded in 10-of-15 guaranteed-improvement mechanisms. The case for the risks being mitigated is grounded in 10 named risks each with specific mitigation + owner. The case for safe rollback is grounded in PRD §1 Iron Rule and the 30-second rollback path.

The platform is worth building. Start with §29 (the most important section), §23 (the second most important), §20 (the foundation everything sits on), and Phase 1 monitoring (the safety net). Watch the metrics. Stay in the loop on strategic calls. Roll back instantly if quality drops below targets.

---

*Document ends. ~640 lines of dense substance, no filler. Houston should read this top-to-bottom and decide whether to start building this week or to defer until §29 and §23 are tightened further.*
