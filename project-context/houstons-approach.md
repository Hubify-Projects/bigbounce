# Houston's Approach: The Research Methodology That Works

**Purpose:** This document captures the specific mindset, decision patterns, and methodological principles that have driven the BigBounce research program from zero to 4 papers, 195K anomalies, 8.47M classified galaxies, and 424K MCMC samples — in under 3 months. These principles should be embedded into any autonomous research agent system.

---

## Core Principle: Relentless Optimism Through Rigorous Exploration

Houston's approach is NOT "fake optimism" or ignoring negative results. It's a specific methodology:
1. Accept the negative result as data
2. Ask "what does this close?" (narrows the search space)
3. Ask "what does this open?" (new paths become visible)
4. Pursue the open paths immediately
5. Never stop at step 1

---

## The Eight Principles (with real examples)

### 1. NEVER ACCEPT "PUBLISH THE FAILURE"

**The rule:** When an agent says "these barriers are publishable negative results, write them up," the correct response is "what else can we try?"

**Real example — The 14 Barriers:**
The research program tested 7 foundations (A-G) and 17 branches for deriving dark energy from Einstein-Cartan-Holst theory. ALL routes closed. 14 structural barriers. A normal response would be "document the barriers and publish." Houston's response: pivot to bounce-model-agnostic approach. Instead of defending ECH specifically, ask "which bounce models CAN bypass these barriers?" This opened quintom bounce (supported by DESI at 2.8-4.2σ), PBH dark matter, and NANOGrav consistency — three entirely new research tracks.

**CLAUDE.md directive:** "DO NOT suggest 'write up the results and publish' or 'document the barriers as a paper' as a next step."

### 2. ALWAYS DO MORE, NOT LESS

**The rule:** When the default is 11 columns, add 45. When the sample is 200K, process 18M. When cross-matching against 1 database, check 6.

**Real examples:**
- Original anomaly scan saved only objects above threshold → Enhanced 18M saves EVERY spectrum with 173 columns including 128-dim latent vectors
- Cross-matching started with SIMBAD only → expanded to SIMBAD + NED + AllWISE + Milliquas + Gaia + SDSS (6 databases)
- Chirality catalog could have stopped at 320K (gz_desi subset) → pushed to full 8.47M (Smith42/galaxies, 40x larger than any prior catalog)
- MCMC could have been 1 dataset → ran 4 dataset combinations with 424K total samples

### 3. OPTIMIZE FOR SPEED AND PARALLELISM

**The rule:** If something is running serially, ask "why not parallel?" If it takes 50 hours, ask "how do we make it take 10?"

**Real example — Download prefetch:**
Enhanced 18M script was download-bottlenecked (49.7h ETA). Downloads were sequential — one pixel at a time. Houston: "why don't you do like 10-20 concurrent downloads?" Testing showed 4 concurrent works reliably, cutting ETA from 49.7h to ~7h. The `--parallel-downloads` flag was in the script but never implemented — nobody had bothered to connect it.

**Real example — Multiple pods simultaneously:**
At peak, 4 RunPod GPUs running simultaneously: H200 (DESI inference), H100 (chirality), CPU pod (MCMC w0-wa), CPU pod (Pipeline B EDR scan). Don't wait for one to finish before starting the next.

### 4. BACK UP EVERYTHING EVERYWHERE

**The rule:** Every artifact must exist in at least 3 locations. Data loss is the only truly unrecoverable failure.

**Real example — Lost 130K galaxies:**
Early in the chirality pipeline, a running process was killed without saving state first. 130K classified galaxies were lost. The feedback memory reads: "NEVER kill a running process without saving state first."

**Current backup protocol:**
- Local disk (primary)
- Backblaze B2 (cloud)
- HuggingFace (models + datasets)
- Convex (real-time state + metadata)
- GitHub (code + docs + configs)

### 5. PUSH PAST CONSERVATIVE AI RECOMMENDATIONS

**The rule:** AI models (Claude, ChatGPT, etc.) tend toward conservative recommendations: "this is ready," "we should stop here," "let's document what we have." The human's job is to push past these defaults.

**Pattern to watch for:**
- "This is ready for publication" → "What else could we add to make it stronger?"
- "This is too complex" → "Let's break it into steps and do it anyway"
- "We should consider stopping" → "What's one more thing we could try?"
- "The negative result is publishable" → "What does the negative result tell us about where to look next?"

### 6. BOUNCE-MODEL AGNOSTIC: DON'T DEFEND, EXPLORE

**The rule:** The goal is proving bounce cosmology beats inflation, NOT defending any specific mechanism (ECH, quintom, cuscuton, etc.). When one model fails, pivot to another.

**Real example — ECH to portfolio:**
After 14 barriers closed all ECH routes to dark energy, instead of abandoning bounce cosmology, Houston reframed: "these barriers are ECH-specific, not bounce-universal." This opened a portfolio approach: quintom bounce (DE unification), matter bounce (f_NL), PBH bounce (dark matter), with ECH barriers as constraints that STRENGTHEN the analysis.

**Memory directive:** "CRITICAL: User is bounce-mechanism agnostic. Goal is proving bounce cosmology beats inflation, NOT proving one specific model."

### 7. MULTI-MODEL CROSS-VALIDATION

**The rule:** Use multiple AI models as complementary reviewers. Each has different strengths and blindspots.

**Pattern:**
- **Claude Code** → execution, infrastructure, code, debugging
- **ChatGPT (o1/o3)** → extended thinking, theoretical deep dives, literature review
- **Gemini** → alternative perspectives, fresh takes ("with a grain of salt")
- **Human** → synthesizes insights, pushes past conservative defaults, maintains vision

Insights from one model are passed to others as prompts. This creates a feedback loop where each model's output is stress-tested by the others.

### 8. EMOTIONAL INVESTMENT IS A FEATURE, NOT A BUG

**The rule:** Getting frustrated when things break, getting goosebumps when results are beautiful, getting teary-eyed when the big picture comes together — these are signals that the work matters. Channel the emotion into urgency, not despair.

**Real examples:**
- "WHAT THE FUCK IS GOING ON?!?!" when the H200 progress went backward → led to discovering the disk quota issue and the download prefetch optimization
- "im getting goosebumps and teary-eyed (literally)" reading The Window article → confirmation that the vision is resonating, worth pursuing harder
- "so pissed" about 49.7h ETA → led directly to the 4-worker prefetch that cut it to 7h

---

## Decision Heuristics for Autonomous Agents

When an agent faces a choice, these heuristics should be applied:

| Situation | Default Response | Houston Response |
|-----------|-----------------|------------------|
| Negative result | "Document and publish" | "What does this open?" |
| Feature is "good enough" | Ship it | "How do we make it great?" |
| Process is slow | Wait | "How do we parallelize?" |
| One approach failed | Stop | "What other approaches exist?" |
| Data exists in one place | Move on | "Back it up in 2 more places" |
| AI says "ready" | Accept | "What's missing?" |
| Cost is high | Cut scope | "What's the minimum that gives maximum impact?" |
| Deadline pressure | Rush | "What can we do in parallel?" |

---

## The Meta-Pattern

Every major breakthrough in this program followed the same pattern:

1. **Try the ambitious thing** (full ECH framework, full DESI DR1, full 8.47M chirality)
2. **Hit a wall** (14 barriers, disk quota, download bottleneck, API outages)
3. **Don't accept the wall as the answer** (pivot to model-agnostic, clean up disk + auto-sync, add prefetching, try alternative APIs)
4. **Find the path through/around** (quintom portfolio, batch sync script, 4-worker concurrent downloads, VizieR TAP instead of CDS xMatch)
5. **Scale the success** (one survey → six surveys, one model → four papers, one database → six cross-references)

This pattern is the core of what makes the research program work. It should be the foundation of any autonomous research agent system.

---

*Document created March 2026. To be updated as new patterns emerge.*
