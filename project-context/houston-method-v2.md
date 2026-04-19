# Houston Method v2: Research Completion Protocol

**Purpose:** This document defines the mandatory completion loop for every experiment, analysis, and pipeline in the BigBounce research program. Nothing is "done" after running a script. The Houston Method v2 enforces a 9-step loop that pushes every research path as far as it can possibly go before marking anything complete.

**Supersedes:** `houstons-approach.md` Principles 1-8 remain. This adds Principle 9 (The Completion Loop) and the Quality Gate system.

---

## Houston's Directives (Verbatim)

These are the exact words that motivated this protocol. They are non-negotiable.

> "There must be more experiments. Do not accept 'complete' easily for any experiments and ensure there are a long list of checks after anything marked complete like all potential follow-on work from each research — backups, site updates on all pages, additional runs based on findings from initial research, additional runs on the additional runs, anything new we should run based on insights from the runs, more full runs if datasets are available, more advanced simulations via MCMC or other datasets, new paper drafts on all findings, new site updates on all that, search for new public datasets for new or old cosmological datasets that we could leverage the H200 for big and small that we have not done yet — add all this to the queue logic and cron run." — Apr 3, 2026

> "Do this right. No more fast cheap results. We want to do this RIGHT ONLY." — Mar 24, 2026

> "We need to prioritize genuine new science over premature packaging." — Mar 20, 2026

> "Run all and add all remaining to the QUEUE to ensure they continue running via the cron ideally cloud/server-side so even if my computer dies they all keep running." — Apr 2, 2026

### The 5 Core Themes (distilled from all directives):

1. **Never mark anything "COMPLETE" without exhaustive follow-up** — QC, interpret, cross-match, site updates, paper updates, additional runs, runs-on-runs, new datasets
2. **Queue should be deep** — always generate more work from findings, search for new public datasets, run more advanced simulations
3. **Do it RIGHT, not fast** — real end-to-end pipelines, not recasts from published summaries. If it seems too easy, something is probably wrong.
4. **Site/papers/docs must stay synced** — every result change must propagate to every relevant page, figure, equation, data table, narrative, and claim
5. **Keep running even when computer is off** — cloud-based cron/queue so research continues autonomously

---

## The Completion Loop

Every experiment/analysis follows this mandatory sequence. Skipping steps is not allowed.

```
RUN → QC → ANALYZE → INTERPRET → CONNECT → SYNC → EXPAND → BACKUP → COMPLETE
  ↑                                                    |
  └────────────────────────────────────────────────────┘
  (new tasks from EXPAND feed back into RUN)
```

---

## Step 1: RUN

Execute the computation. Save raw outputs.

**Outputs:** Raw result files (parquet, JSON, FITS, CSV, figures)

---

## Step 2: QC GATE (Automated)

Automated quality checks run immediately after the experiment finishes. If ANY check fails, the experiment is marked `needs-rerun` and the queue continues to the next item.

### Mandatory QC Checks

| Check | Failure Condition | Failure Mode |
|-------|------------------|--------------|
| **Null coordinates** | >5% of top anomalies have RA=0.0, Dec=0.0 | Coordinate propagation bug |
| **Training quality** | val_loss > 1,000 or no convergence | Undertrained model |
| **Cluster degeneracy** | >80% of objects in a single cluster | Meaningless clustering |
| **Score explosion** | max(anomaly_score) > 10^6 | Model confusion / domain shift |
| **Spatial concentration** | All top 20 anomalies within 5° radius | Survey systematic, not real signal |
| **Empty output** | 0 anomalies found or empty output file | Pipeline error |
| **NaN/Inf values** | Any NaN or Inf in scores or coordinates | Numerical instability |

### QC Output

```json
{
  "experiment_id": "planck-cmb-masked-v2",
  "qc_status": "PASS" | "FAIL",
  "checks": {
    "null_coordinates": {"passed": true, "null_fraction": 0.0},
    "training_quality": {"passed": true, "val_loss": 0.42, "epochs": 87},
    "cluster_degeneracy": {"passed": true, "max_cluster_fraction": 0.34},
    "score_range": {"passed": true, "max_score": 4.2, "min_score": 0.01},
    "spatial_concentration": {"passed": true, "max_pair_separation_deg": 142.3},
    "output_nonempty": {"passed": true, "n_anomalies": 187},
    "no_nan_inf": {"passed": true}
  },
  "failure_modes": [],
  "recommendation": "PROCEED" | "RE-RUN with [specific fix]"
}
```

**If QC fails:** Log the failure mode, add a re-run task to the queue with the specific fix, continue to the next experiment. Do NOT proceed to Step 3.

---

## Step 3: ANALYZE

Scientific analysis of the results. Not optional.

### For anomaly catalogs:
- Cross-match top 100 anomalies against SIMBAD (2" radius)
- Cross-match against NED (5" radius)
- Cross-match against VizieR catalogs (survey-specific)
- Compute novelty fraction (% not in any catalog)
- Spatial distribution: are anomalies clustered (astrophysical) or uniform (instrumental)?
- Score distribution: log-normal (physical) or power-law with cutoff (systematic)?
- Classify anomaly types: QSO, star, galaxy, artifact, unknown

### For CMB experiments:
- Cross-match anomalous patches with known CMB features (Cold Spot, hemispheric asymmetry)
- Check correlation with galactic foreground templates
- Multipole-by-multipole analysis
- Null tests (half-mission splits, frequency splits)

### For time-domain experiments:
- Cross-match with known variable star catalogs (AAVSO, GCVS)
- Cross-match with AGN catalogs (Milliquas, Véron-Cetty)
- Check for periodicity in anomalous light curves
- Cross-match with ZTF/TESS alerts

### For cross-survey experiments:
- Compute expected random matches for significance
- Characterize multi-wavelength properties of matches
- Identify the most interesting individual objects for follow-up

**Outputs:** Analysis summary JSON, cross-match tables, classification breakdown

---

## Step 4: INTERPRET

What does this result mean for bounce cosmology? Every result connects to the science.

### Questions to answer:
1. Does this result improve our f_NL constraint? (tracer bias, sample size, purity)
2. Does this result test the birefringence prediction? (β = 0.27°)
3. Does this result constrain the NANOGrav GW spectrum? (γ = 3.0)
4. Does this result support or challenge the quintom w-crossing? (w₀ + wₐ < -1)
5. Does this result open a new observational channel for bounce cosmology?
6. Does this result close or narrow an existing research path?

### If the result is negative:
- What does the negative result TEACH us about where to look next?
- What constraints does it place on models?
- Does it close an ECH-specific route (add to barrier count) while leaving other bounce models open?

**Never stop at "null result." Always answer: "What does this open?"**

**Outputs:** Interpretation summary (1-2 paragraphs), connection to bounce predictions

---

## Step 5: CONNECT

How does this result relate to other survey results and the broader research program?

### Actions:
- Cross-reference with every other completed survey (N×N matrix)
- Update the bounce cosmology portfolio table (which channels strengthened/weakened?)
- Update the f_NL sensitivity forecast (did our σ improve?)
- Check if any speculations.html "ACTIONABLE" items are now feasible
- Check if any paper drafts need updates based on this finding

**Outputs:** Updated cross-reference matrix, portfolio table deltas

---

## Step 6: SYNC (Website + Papers)

Update ALL affected website pages within 24 hours. This is not optional.

### Mandatory page updates — check EVERY page, not just "the obvious ones":

| Page | When to Update |
|------|---------------|
| `activity.html` | **ALWAYS** — add new timeline entry for every experiment |
| `status.html` | When ANY pipeline/dataset/paper/pod status changes |
| `data-explorer.html` | When new datasets, tables, or equations are produced |
| `figures.html` | When new publication figures are generated |
| `paper.html` | When paper readiness %, version, or content changes |
| `index.html` | When stat cards, key results, claims table, or barrier count changes |
| `explained.html` | When scientific claims, numbers, or narrative changes |
| `glossary.html` | When new parameters, equations, or terms are introduced |
| `contributions.html` | When new novel contributions are made |
| `speculations.html` | When speculation items become actionable or are tested |
| `timeline.html` | When new milestones are reached |
| `datasets.html` | When new datasets or MCMC configs are created |
| `methodology.html` | When methodology changes (new QC gates, new architectures) |
| `articles/*.html` | When article-relevant findings change (especially The Window stats) |
| `research/project_master_dossier/` | When branch status or evidence tables change |

**The rule: if a number, claim, figure, or status appears on ANY page and the underlying data changes, that page MUST be updated.** Use grep to find all occurrences of changed values.

### Paper updates:
- If result is publishable → add to relevant paper draft
- If result changes ANY number cited in a paper → update the paper
- If result opens a new paper topic → create outline
- If result changes a figure → regenerate the figure and update all pages displaying it
- Check ALL 4 papers, not just the "relevant" one — results often affect multiple papers

**Outputs:** Git diff showing all page updates

---

## Step 7: EXPAND

Generate new tasks from this result. This is the self-perpetuating engine.

### Task generation rules:
1. **Cross-match tasks:** For each new survey result, add N cross-match tasks (one per other survey)
2. **Deeper analysis:** If top anomalies are interesting, add "download spectra + detailed analysis" task
3. **Runs on the runs:** Run additional analyses on the output (UMAP clustering, emission line extraction, photo-z estimation, density mapping, etc.)
4. **Runs on the runs on the runs:** If the additional analysis reveals something, run FURTHER analysis (e.g., UMAP reveals a cluster → classify that cluster → cross-match the cluster → measure its bias → update f_NL forecast)
5. **Architecture variant:** If results are promising, add "re-run with transformer/VAE/contrastive" task
6. **New dataset search:** After every experiment, actively search for NEW public datasets (cosmological or astrophysical) that could be processed with the same or similar pipeline. Check data release calendars, arxiv new submissions, survey websites.
7. **Advanced simulations:** If the result touches a theoretical prediction, add an MCMC or numerical simulation task to refine the prediction (not just recast from published numbers — do the real computation)
8. **Paper integration:** If publishable, add paper draft/update task
9. **Follow-up observation:** If discovery candidate, add "prepare target list for telescope proposal" task
10. **Model improvement:** If systematic identified, add "fix model and re-run" task
11. **Site propagation:** Add explicit tasks for every page that needs updating (not just "update site" — list each page)

**Every experiment should generate 5-15 new tasks.** If it generates fewer than 5, you haven't thought hard enough. The queue should ALWAYS be growing, not shrinking.

**Outputs:** New tasks added to queue (research_queue.json)

---

## Step 8: BACKUP

Results must exist in 3+ locations before marking complete.

### Backup protocol:
1. **After every experiment:** `scp` results to local disk
2. **After every experiment:** `git add + commit + push` (auto-deploys website)
3. **Every 5 experiments:** Backup to Backblaze B2
4. **Every 10 experiments:** Upload model artifacts to HuggingFace
5. **Checkpoint file:** Write `checkpoint.json` with full experiment metadata

### Checkpoint schema:
```json
{
  "experiment_id": "desi-erosita-crossmatch",
  "status": "complete",
  "qc_status": "PASS",
  "started": "2026-04-05T10:00:00Z",
  "completed": "2026-04-05T11:12:00Z",
  "gpu_hours": 1.2,
  "cost_usd": 4.31,
  "n_sources": 930203,
  "n_anomalies": 47,
  "novelty_fraction": 0.72,
  "key_finding": "47 optical×X-ray coincidences, 34 not in any catalog",
  "tasks_generated": ["erosita-neowise-xmatch", "erosita-top10-spectra"],
  "pages_updated": ["activity.html", "status.html", "data-explorer.html"],
  "backup_locations": ["local", "github", "b2"]
}
```

---

## Step 9: COMPLETE

Only after steps 1-8 are ALL done. Mark the experiment as COMPLETE in:
- `research_queue.json` (status: "complete")
- `checkpoint.json` (status: "complete")
- `wiki/entities/{survey}.md` (update entity page)
- `wiki/log.md` (append completion entry)
- `status.html` (update badge to green COMPLETE)

---

## The Self-Perpetuating Engine

The key insight: Step 7 (EXPAND) feeds new tasks back to Step 1 (RUN). The queue is never empty because every result generates new work. The research program advances not by running scripts, but by the cumulative effect of thousands of completion loops, each pushing one research path a little further.

```
Survey scan → anomalies found → cross-matched → classified → 
  → improves f_NL tracer → better σ(f_NL) → paper updated →
    → new survey scan with improved methodology → ...
```

This is the Houston Method: relentless forward progress through rigorous, systematic, compounding research loops.

---

## Principle 10: Future Work Is Code Smell — Do It NOW

Added 2026-04-17 after Houston flagged the pattern in Paper 1–4 drafts.

Every phrase in a paper that sounds like "left to future work," "will be presented elsewhere," "defer to a future study," "beyond the scope," "in preparation," "we plan to," "forthcoming," or "further investigation is needed" is a **red flag**, not a convenience.

### The Rule

If the paper mentions it as future work, the default answer is: **run it NOW and fold the result into the paper itself.**

Papers get stronger when every flagged "future direction" becomes a finished result in the manuscript. A referee who sees five future-work items will ding the paper. A referee who sees the same five items resolved in a new appendix will accept it.

### When Is "Future Work" Actually Acceptable?

Only one test passes:

> Does this require a specific piece of hardware or a specific dataset that physically does not exist yet and cannot be simulated, augmented with AI, or proxied with existing data?

Examples of **legitimate** future work:
- LiteBIRD (launches 2028) full-sky measurement — the detector literally does not exist
- LISA (launches 2035) GW band — no ground analogue at mHz
- CMB-S4 cosmic-variance-limited polarization — detector not built
- SKA Phase 2 radio polarization — array not built

Examples of **FAKE** future work (do it now):
- "A full two-loop calculation is left to future work" — it's just more math, do it
- "A dedicated MCMC analysis is beyond the scope" — run the chains
- "Independent derivation using another formalism is deferred" — do the second derivation
- "Cross-match against NED/VizieR will be presented elsewhere" — query the service today
- "Injection/recovery test is forthcoming" — write the 200 lines of Python
- "Further investigation of spatial clustering is planned" — angular correlation is an hour of work
- "A systematic bias audit using an alternative classifier" — retrain on H200

### The Augmentation Test (For Items That Look Blocked)

Before classifying something as truly-blocked, ask three questions:

1. **Can we simulate it?** Fisher forecasts, mock catalogs, synthetic data through the same pipeline — all count as "doing it now" for a paper.
2. **Can we AI-augment it?** Super-resolution models, synthetic label generation from generative models, proxy datasets that approximate the future survey.
3. **Can we proxy with existing data?** Many future surveys have public precursors (Euclid Flagship sim, LSST DC2, SPHEREx mocks). Build the pipeline against the proxy today, re-run when real data lands.

If any of the three pass, the item is **simulate/augment NOW**, not future work.

### Enforcement: The Future-Work Sweep

Before any paper is marked arXiv-ready:

1. `grep -i` the manuscript for the trigger phrases listed above.
2. For each hit, classify: **DO NOW** / **SIMULATE/AUGMENT NOW** / **TRULY BLOCKED (specify launch date)**.
3. Add every DO NOW and SIMULATE/AUGMENT item to `research_queue.json` with the paper it originated from, in PRIORITY-0 slots.
4. Run them. Fold results back into the paper. Re-grep. Repeat until the only remaining hits are TRULY BLOCKED.

This sweep is a mandatory QC gate. A paper with unresolved DO-NOW items in its text is **not ready for submission**, even if every other gate passes.

### Why This Matters

Papers on arXiv are permanent. The "future work" in a paper today is either a gift to a competitor who runs it first, or a 6-month delay to your own stronger v2. Houston's rule: we have H200 compute, we have the pipelines, we have the time. The "future" referred to in the paper is usually *this week*. Do the work now, ship the stronger paper.

---

## Principle 11: Default to the Hardest/Fullest/Highest-Quality Path — Never the Easy One

Added 2026-04-19 after Houston caught the pattern during the Paper 3 novelty-integrity rebuild.

> "you identified issues that were possible for us to solve even if they were hard and yet i still had to decipher your messages and push back on your suggestion that we do the easy thing when we should ALWAYS do the harder fullest highest quality option every time"

### The Rule

When a defect is surfaced (data-quality issue, contamination, missing validation, undertrained model, systematic bias, etc.) AND multiple fix paths exist ranging from easy-with-caveats to full-rebuild, **the default recommendation is the hardest/fullest/highest-quality path.** Period.

Do NOT list "Path A ship-with-caveats / Path B minimum-real-fix / Path C full-Cadillac" and leave the choice ambiguous. **Path C is the answer** unless there is a hard blocker (budget cap, timeline deadline, missing data that cannot be proxied).

### What Triggered This Principle

2026-04-19 Paper 3 novelty-integrity audit surfaced 5 major quality issues:
1. CMB autoencoder injection-recovery at 0.33% (catastrophically undertrained)
2. DESI in-sample bias (BigAE scored on its own training set)
3. LAMOST 98% blue-excess contamination
4. NEOWISE ecliptic-latitude systematic
5. Missing 8-way cross-survey positional dedup

I correctly identified the issues, then presented Path A (ship-with-caveats, 2 days, cheap) as a reasonable option and only reluctantly recommended Path B with Path C framed as an "upgrade." Houston had to explicitly push back: *"we do not have to accept this low quality"* — and then choose Path C himself. This should never have required pushback.

### How to Apply

- When a defect is surfaced AND a fix is possible (even if hard or expensive), **default recommendation = the full fix.**
- When presenting options, the ordering must be:
  1. **"Recommended: Path C — do it right"** with cost/time called out.
  2. Alternatives below, clearly labeled as weaker (not "also reasonable").
- Do NOT frame the easy option as "also reasonable." It is not. Houston's emotional investment + AI-compression-of-effort means the "full rebuild" cost is genuinely affordable relative to the scientific upgrade.
- If budget or timeline blocks the full path, say so explicitly as a blocker — do not downgrade the recommendation silently.
- Applies across all domains: data pipelines (retrain > caveat), papers (rewrite > patch), code (refactor > band-aid), site (redesign > style tweak), infrastructure (proper fix > monkey-patch).

### Relation to Other Principles

- **Stronger than Principle 2 ("Always do more, not less")**: Principle 2 is about *scope* (scan all, not a sample). Principle 11 is about *quality ceilings* (when there's a choice between known-contaminated and cleanly-retrained, always recommend the retrain).
- **Reinforces Principle 10 ("Future Work Is Code Smell")**: Deferring the hard fix to "v2 of the paper" is the same pattern as calling it "future work." Do it now, do it right.
- **Enforces "Do It RIGHT, Not Fast"** (below): this is the operational rule that prevents ever slipping back into fast-cheap mode.

### Test for Future Self

Before presenting any "Path A/B/C" menu to Houston, ask: *"Am I about to make Houston push back and tell me to pick C?"* If yes — just recommend C up front with the alternatives as footnotes.

Full memory: `~/.claude/projects/-Users-houstongolden-Desktop-CODE-2025-bigbounce/memory/feedback_default_hardest_path.md`

---

## Anti-Patterns (Things That Are NOT Completion)

| What Happened | Why It's Not Complete |
|--------------|----------------------|
| Script finished running | That's Step 1 of 9 |
| Results saved to disk | That's Step 8 of 9 (and only backup, not analysis) |
| "COMPLETE" badge added to status page | Badge without QC is a lie |
| Anomaly count reported | Count without classification is meaningless |
| Cross-match done against one catalog | Need SIMBAD + NED + VizieR minimum |
| "Null result" reported | What does the null result open? (Step 4) |
| No new tasks generated | Think harder (Step 7) |

---

## Integration with Existing Principles

This protocol builds on the existing Houston Method principles:

1. **Never accept "publish the failure"** → Step 4 forces interpretation of every result
2. **Always do more, not less** → Step 7 generates 3-10 new tasks per experiment
3. **Optimize for speed and parallelism** → Queue processes experiments in parallel
4. **Back up everything everywhere** → Step 8 enforces 3+ locations
5. **Push past conservative AI recommendations** → The loop never stops at "good enough"
6. **Bounce-model agnostic** → Step 4 connects to ALL bounce models, not just ECH
7. **Multi-model cross-validation** → Steps 3-4 use multiple analysis approaches
8. **Emotional investment is a feature** → The loop channels urgency into systematic progress
9. **THE COMPLETION LOOP** → This document. The enforcement mechanism for all of the above.
10. **Future Work Is Code Smell** → Do it NOW; the only exceptions are hardware/datasets that literally don't exist yet.
11. **Default to the hardest path** → When a defect has multiple fix paths, recommend the full-rebuild up front; never make Houston push back to pick quality.

---

---

## Do It RIGHT, Not Fast

> "No more fast cheap results. We want to do this RIGHT ONLY."

This means:
- **Real end-to-end pipelines**, not recasts from published summary statistics
- **Real GPU/CPU computation** on actual data, not back-of-envelope estimates
- **Real cross-matching** against actual catalog databases, not "we expect ~X matches"
- **Real systematics analysis** (injection/recovery, null tests, jackknife), not "systematics are expected to be small"
- **Real MCMC** with proper convergence diagnostics, not "assuming Gaussian posteriors"

If a result came too easily (< 1 hour for what should take days), ask: "Did we actually do the computation, or did we just reformat published numbers?" If it's the latter, it's not a result — it's a literature review.

---

## Cloud-Based Autonomous Execution

> "Run all and add all remaining to the QUEUE to ensure they continue running via the cron ideally cloud/server-side so even if my computer dies they all keep running."

Requirements:
- Queue runner must be **server-side** (RunPod pod, Convex cron, or similar)
- Research must continue **even if Houston's laptop is off**
- Results must be **auto-backed-up** to cloud storage after each experiment
- Queue must **auto-expand** — new tasks from Step 7 added programmatically
- Monitoring must be **async** — status visible via website dashboard, not requiring SSH
- Failures must be **auto-logged** with failure mode, not silently swallowed

Target architecture:
```
RunPod H200 (queue runner) → runs experiments sequentially
  → after each: QC gate → backup to B2/HuggingFace → git push
  → Convex mutation: update experiment status
  → Website (auto-deployed via git push): shows live progress
  → If QC fails: auto-adds re-run task to queue
  → If QC passes: auto-adds follow-up tasks to queue
```

Houston can check progress by visiting bigbounce.hubify.app/status anytime, from any device.

---

*Document created April 4, 2026. Updated with verbatim directives from Houston's prompt history. This is the mandatory protocol for all future research execution.*
