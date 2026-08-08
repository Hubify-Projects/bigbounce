# Compute Architecture Decision — Hubify Labs

**Date:** 2026-04-07
**Status:** Draft for review
**Author:** Claude (synthesized from Houston's feedback and provider docs)

---

## TL;DR

- **Move GPU experiments from RunPod to Modal.com.** Modal's pay-per-second billing plus Modal Volumes eliminates the "credits expire mid-run, pod dies, state lost" failure mode that has been the #1 pain point on RunPod. At $0.001261/sec for H200 ($4.54/hr), Modal is ~26% more expensive per hour than RunPod's $3.59/hr — but you stop paying the moment a job finishes, which for bursty research workloads is typically a net savings.
- **Adopt a 4-provider split, one role each.** Modal for GPU experiments, Fly.io for the persistent agent orchestrator and always-on services, Vercel (Fluid Compute + static) for the Hubify Labs web surface and lab APIs, Vercel Sandbox for ephemeral "vibe-coding" user code execution. Daytona and e2b remain parked.
- **Do NOT adopt Vercel Workflows yet.** Our custom agent-based orchestrator already handles long-running multi-step experiments with memory, retries, and human-in-the-loop. Workflows would be a lock-in rewrite to a Vercel-proprietary `'use workflow'` TypeScript DSL. Revisit only if we need durable state across months of sleeps.

---

## The Problem

Hubify Labs is scaling from a single-lab codebase (bigbounce) to a multi-lab platform. The current compute stack has three pain points that block that scaling:

### 1. Pods die mid-experiment when credits expire

Current setup: H200 pod `o76k3jfzbfh25e` is billed hourly against a prepaid credit balance. When the balance hits zero, the pod is killed — not paused, killed. Any in-memory state, running jobs, tmux sessions, and non-persisted output is lost. We have been bitten by this during Phase 2 and Phase 3 experiment runs, and we routinely carve work into sub-runs that can checkpoint to `/workspace` before the credits run out.

This is fundamentally a **reservation vs. consumption mismatch**: we're paying for a reserved GPU 24/7, but actually using it maybe 30% of the time. The other 70% we're either coding, analyzing results on the laptop, or asleep — and the pod is burning credits the whole time.

### 2. Persistent services are scattered across providers

The current stack spans at least 4 providers with no single control plane:

- **RunPod** — H200 pod (research compute)
- **Netlify** — static site deploy for `bigbounce.hubify.app`
- **Vercel** — DNS and custom subdomains (historical)
- **Fly.io** — Hubify control plane machines (historical, still billed)

Each has different auth, different dashboards, different billing cycles. Onboarding a second lab to this setup would 4x the surface area.

### 3. The lab surface is growing three frontends

Hubify Labs needs to support a web dashboard, a TUI for pod/experiment management, and a macOS desktop app. All three have to hit the same backend API regardless of which compute provider is running the underlying experiment. That means we need a clean API layer that abstracts provider-specific details (Modal function calls, Fly machine lifecycle, Vercel Sandbox creation) behind a stable Hubify Labs contract.

---

## Use-Case Decomposition

Before matching providers to roles, let's break down what workloads Hubify Labs actually runs. They are not interchangeable.

| Workload | Typical duration | GPU? | Persistence needed? | Concurrency | Who triggers |
|----------|------------------|------|---------------------|-------------|--------------|
| **Long-running GPU training / MCMC / anomaly sweep** | 1–48 hours | Yes (H200, H100) | Yes — chains, checkpoints, model weights survive restart | 1–10 jobs in flight | Researcher (Houston) or scheduled |
| **Parallel experiment fan-out** | Minutes to hours each | Yes | Yes — per-experiment artifact | 10–100 at once | Orchestrator agent |
| **Persistent orchestrator / agent loop** | 24/7 | No | Yes — task queue, job state | 1 | Always on |
| **Lab API backend (`api.hubify.com`)** | Per-request, ms–seconds | No | Shared DB, stateless compute | 100s req/sec | Web, TUI, desktop clients |
| **Static lab site (`{lab}.hubify.com`)** | N/A | No | N/A (CDN) | Unlimited | End users |
| **Vibe-coding sandbox** (run user / LLM-generated code) | Seconds to minutes | No | No — ephemeral per session | 10–1000 per hour | Lab users |
| **Scheduled tasks** (daily paper recompile, weekly retro, data backups) | Minutes | Sometimes | Yes — output archive | 1–5 daily | Cron |
| **Real-time collaboration / streaming** (dashboard live updates) | Continuous | No | Stateless | 100s connections | Dashboard |

Three key observations:

1. **GPU training and agent orchestration have opposite cost profiles.** GPU is expensive per hour but idle 70% of the time — we want pay-per-second. Orchestrator is cheap per hour but needs 24/7 uptime — we want flat monthly pricing.
2. **Vibe-coding sandbox is a fundamentally different security model** from research GPU work. User-provided or LLM-generated code needs network-isolated microVMs; research code is trusted.
3. **The lab API backend can be I/O-bound and bursty** — exactly the fit for fluid / serverless compute with warm reuse.

---

## Provider Evaluation

### Modal.com

**Source:** https://modal.com/pricing, https://modal.com/docs/guide/timeouts, https://modal.com/docs/guide/volumes, https://modal.com/docs/guide/sandbox, https://modal.com/docs/guide/cold-start

#### Pricing (from the Modal pricing page)

GPU pricing (per-second, then per-hour equivalent):

| GPU | Per-second | Per-hour equivalent |
|-----|-----------:|--------------------:|
| Nvidia B200 | $0.001736 | $6.25 |
| **Nvidia H200** | **$0.001261** | **$4.54** |
| Nvidia H100 | $0.001097 | $3.95 |
| Nvidia A100 (80GB) | $0.000694 | $2.50 |
| Nvidia A100 (40GB) | $0.000583 | $2.10 |
| Nvidia L4 | $0.000222 | $0.80 |
| Nvidia T4 | $0.000164 | $0.59 |

CPU/memory (for the non-GPU parts of a function):

- CPU: $0.0000131 / core / sec (physical core = 2 vCPU equivalent, min 0.125 cores per container)
- Memory: $0.00000222 / GiB / sec

Modal Sandboxes + Notebooks pricing (different tier for the sandbox product):

- CPU: $0.00003942 / core / sec
- Memory: $0.00000672 / GiB / sec

Free tier:

- Starter plan: **$30/month free credits**
- Team plan: **$100/month free credits**

#### Billing model — this is the key point

From Modal's pricing page: *"you always pay for what you use and nothing more. You never pay for idle resources — just actual compute time"*.

Modal bills per **second of actual function execution**, not per reserved hour. A function that runs for 7 minutes costs 420 seconds × $0.001261 = **$0.53** on an H200, not $4.54. When the function returns, billing stops. There is no "pod" to keep alive.

#### Does this solve the "credits expire mid-run" pain point?

**Yes, but in a fundamentally different way than RunPod.**

On RunPod, you prepay a credit balance, the pod runs until the balance hits zero, and then it's killed. A 36-hour MCMC run needs 36 × $3.59 = $129 sitting in your credit balance *before you start*, or the job will die partway through.

On Modal, there is no "pod" — a function is invoked, it runs, it returns. Billing happens after the fact. As long as your payment method is valid and you're not past a hard spending cap, a 36-hour job just... runs. The equivalent cost on an H200 is 36 × $4.54 = **$163.44** — about 27% more expensive per hour than RunPod, but spread across actual usage only, not reserved capacity.

The real question is: **when does Modal kill a running job?** Modal's timeout docs state functions can be configured *"between 1 second and 24 hours"*, with a default of 300 seconds. The 24-hour hard cap is real — longer-than-24hr training jobs cannot run as a single Modal function, they would need to be broken into chained functions or run via Modal Sandbox (which has the same 24-hour lifetime cap per the sandbox guide: *"Sandboxes have a default maximum lifetime of 5 minutes"* with `timeout` configurable *"of up to 24 hours"*).

**The credits-expire problem is replaced by a 24-hour-per-job problem.** For BigBounce workloads, this is actually fine — most phase experiments are 1-8 hours, MCMC chains are routinely checkpointed, and the handful of multi-day runs can be sharded.

#### Modal Volumes — the RunPod `/workspace` replacement

From https://modal.com/docs/guide/volumes:

> *"a high-performance distributed file system for your Modal applications... write-once, read-many I/O workloads, like creating machine learning model weights and distributing them for inference."*

Volumes v2 (beta) specs:
- No file count limit (v1 capped at 500,000 inodes)
- Max individual file size: "less than 1 TiB"
- Max files per directory: 262,144
- Bandwidth: "up to 2.5 GB/s"
- Persistence: auto-commits every few seconds during function execution, final commit on shutdown
- Mount point: `/mnt`, attached via `Volume.from_name()`

**Pricing for Volumes is not published on the public pricing page we fetched.** This is a gap — before committing, we need to confirm volume storage costs. Competitors are in the range of $0.10–0.23/GB-month. A 500GB volume for all research artifacts at $0.15/GB-month would be ~$75/month, less than 2 days of H200 time.

**Recommendation: Volumes replace pod-local `/workspace` for all persistent research artifacts** — chain files, MCMC posteriors, anomaly catalogs, model weights. Functions mount the volume, read inputs, write outputs, exit. State survives across any number of function invocations and any pause in activity.

#### Cold start latency

From https://modal.com/docs/guide/cold-start: *"Containers boot in about one second."* No GPU-specific number is published. In practice, for our workloads (training runs that take minutes to hours), a 5–30 second GPU container cold start is a rounding error. For a hypothetical real-time inference use case, we would use `min_containers` to keep warm instances.

Warming controls:
- `scaledown_window`: idle time before shutdown (default 60s, range 2–1200s)
- `min_containers`: baseline warm count
- `buffer_containers`: extras during active traffic

#### Pros

- **Pay-per-second billing** eliminates the pod-idle-cost problem. A researcher experimenting 3 hrs/day pays for 3 hrs, not 24.
- **No credit balance mid-run death.** Pay monthly in arrears like a normal cloud service.
- **Modal Volumes** provide durable state that outlives any single function invocation.
- **Python-first SDK** — functions are just Python decorators. Fits our existing workflow.
- **Sandbox product** exists for untrusted code execution (but more expensive than function compute, see the $0.00003942/sec CPU tier).
- **No infrastructure to babysit** — no pods to spin up, no ssh to manage, no tmux sessions to resume.
- **Cold start is fast enough** (~1s containers, GPU likely 10–30s) for research workloads.

#### Cons

- **~27% higher per-hour cost** than RunPod for H200 ($4.54 vs $3.59). If we actually utilized 24/7 we would lose money vs. RunPod — but we don't.
- **24-hour hard cap per function/sandbox invocation.** Multi-day jobs need sharding or chaining.
- **Cold start on GPU is not zero.** Probably fine for us, but worth measuring before committing.
- **Python ecosystem lock-in.** Porting off Modal means rewriting function decorators, volume mounts, and image definitions.
- **Volume pricing not on public page** — unknown until we ask sales or read the deeper docs.
- **ssh/interactive debugging story is weaker** than having a persistent RunPod pod. Modal Shells exist but are less flexible than `ssh -p <port> root@<pod-ip>`.

#### Fit

**Perfect fit for:** parallel experiment fan-out, MCMC chains, anomaly sweeps, model training, one-shot GPU inference, cron-driven data pipelines.

**Poor fit for:** interactive GPU debugging sessions (keep a smaller RunPod pod for this if needed), multi-day continuous training (would need sharding).

---

### Vercel Sandbox

**Source:** https://vercel.com/docs/vercel-sandbox/sdk-reference, https://vercel.com/docs/vercel-sandbox/cli-reference, https://vercel.com/docs/vercel-sandbox/pricing

#### What it is

From the SDK docs: *"The Vercel Sandbox Software Development Kit (SDK) lets you create ephemeral Linux microVMs on demand. Use it to evaluate user-generated code, run AI agent output safely, test services without touching production resources, or run reproducible integration tests that need a full Linux environment with sudo access."*

This is explicitly a **sandbox for untrusted code**, not a compute platform. Firecracker-style microVMs with full Linux + sudo, network firewall (`allow-all` / `deny-all` / custom SNI-based allowlist), snapshot/restore, and a Docker-like CLI (`sandbox create`, `sandbox exec`, `sandbox copy`, `sandbox connect`, `sandbox stop`, `sandbox run`).

Runtimes offered: `node24`, `node22`, `python3.13`. Base image: Amazon Linux 2023.

#### Pricing (Vercel Sandbox pricing page)

|  | Hobby (included) | Pro (per month) | Enterprise (per month) |
|---|---|---|---|
| Sandbox Active CPU | 5 hours/month | $0.128/hour | $0.128/hour |
| Sandbox Provisioned Memory | 420 GB-hours/month | $0.0212/GB-hour | $0.0212/GB-hour |
| Sandbox Creations | 5,000/month | $0.60/1M | $0.60/1M |
| Sandbox Data Transfer | 20 GB/month | $0.15/GB | $0.15/GB |
| Sandbox Storage | 15 GB lifetime | $0.08/GB-month | $0.08/GB-month |
| Concurrent Sandboxes | 10 | 2,000 | 2,000 |
| Max Runtime Duration | 45 minutes | 5 hours | 5 hours |
| vCPU Allocation Rate | 40/10 min | 200/min | 400/min |

Resource limits per plan:
- Hobby: max 4 vCPUs, 8 GB memory, 15 open ports
- Pro: max 8 vCPUs, 16 GB memory, 15 open ports
- Enterprise: max 32 vCPUs, 64 GB memory, 15 open ports

Key billing behavior: **Active CPU is only billed when code is running** — I/O waits are free. A sandbox that pulls `npm install` for 30s (most of which is network wait) charges much less than the wall-clock time suggests.

Pro plan comes with **$20/month included credit** against the usage rates above.

#### Example cost (from the pricing page)

| Scenario | Duration | vCPUs | Memory | Total |
|---|---|---|---|---|
| Quick test | 2 min | 1 | 2 GB | ~$0.01 |
| AI code validation | 5 min | 2 | 4 GB | ~$0.03 |
| Build and test | 30 min | 4 | 8 GB | ~$0.34 |
| Long-running task | 2 hr | 8 | 16 GB | ~$2.73 |

#### Startup time

Vercel does not publish a specific cold-start number on the pricing or SDK pages we fetched. Industry reporting on Firecracker-based sandboxes suggests 100–500ms for typical image launches. The SDK has `Sandbox.get()` and `Sandbox.list()` for reconnecting to existing sandboxes and `snapshot()` for pre-warming.

#### GPU support

**None.** Vercel Sandbox is CPU-only. No GPU runtimes listed in the SDK.

#### Isolation model

The docs use the phrase *"ephemeral Linux microVMs"* — this is Firecracker-level isolation, not container-level. Good enough to run LLM-generated code from untrusted users.

Network firewall is first-class with per-sandbox control:
```ts
Sandbox.create({ networkPolicy: 'deny-all' })
// Or custom allowlist by SNI
sandbox.updateNetworkPolicy({ allow: ["google.com", "ai-gateway.vercel.sh"] })
```

Pro/Enterprise can do **credential brokering** — the sandbox makes API calls and Vercel injects headers (API keys) at the proxy layer so the sandboxed code never sees the secret. This is important for building a "let AI run shell in your lab account" product.

#### Regions

Currently `iad1` (US East) only. This is a real limitation if we need EU data residency for any labs.

#### Pros

- **Purpose-built for the "run untrusted code" use case.** Firecracker microVMs, network firewall, snapshots, credential brokering.
- **Cheap for bursty workloads.** $0.128/CPU-hour is half the cost of a continuously-running Fly machine.
- **Docker-like ergonomics.** `sandbox run -- node script.js` is as simple as it gets.
- **Snapshots for fast cold-start.** Pre-warm a snapshot with dependencies installed, create sandbox from snapshot in sub-second.
- **Clean TS SDK** (`@vercel/sandbox`) matches our Next.js + Vercel-hosted Hubify Labs frontend.

#### Cons

- **No GPUs.** This is a CPU sandbox only.
- **Max 5 hours runtime on Pro.** Fine for ephemeral user code, not for training.
- **Single region (iad1).** No EU residency yet.
- **Filesystem is ephemeral.** Artifacts must be exported to S3 or similar; snapshots help but are rate-limited and expire.
- **10 concurrent sandboxes on Hobby** is tight if multiple users are vibe-coding simultaneously. Pro bumps to 2,000 which is plenty.

#### Fit

**Perfect fit for:** the "vibe-coding sandbox" inside Hubify Labs — letting a researcher (or their AI copilot) run arbitrary Python/Node scripts against a lab dataset in an isolated environment without touching the real pod. Also ideal for running integration tests, validating AI-generated analysis scripts, and spinning up one-off debug shells from the web UI.

**Poor fit for:** any GPU work, any multi-hour continuous job, research that needs 50GB of durable state.

---

### Vercel Workflows

**Source:** https://vercel.com/docs/workflow

#### What it is

From the docs: *"Vercel Workflow is a fully managed platform built on top of the open-source Workflow SDK, a TypeScript framework for building apps and AI agents that can pause, resume, and maintain state."*

The programming model uses two TypeScript directives:

```typescript
export async function aiContentWorkflow(topic: string) {
  'use workflow';
  const draft = await generateDraft(topic);
  const summary = await summarizeDraft(draft);
  return { draft, summary };
}

async function generateDraft(topic: string) {
  'use step';
  return await aiGenerate({ prompt: `Write a blog post about ${topic}` });
}
```

Under the hood: workflows compile into routes backed by Vercel Queues and managed persistence, with deterministic replay on crash/deploy. Steps are individually retried. `sleep('7 days')` pauses with zero resource consumption. Hooks (`defineHook`) let workflows wait for external events (webhooks, human approvals).

#### Abstraction

This is the "durable functions / step functions" pattern, like AWS Step Functions or Temporal, but with a code-first TypeScript DSL instead of YAML or JSON state machines. The docs emphasize: *"Write async/await JavaScript with two directives. No YAML or state machines."*

Underlying SDK is open source (https://useworkflow.dev), but the managed persistence, queues, and observability are Vercel-specific.

#### Pricing

From the docs:

| Resource | Hobby included | On-demand |
|---|---|---|
| Workflow Steps | First 50,000 steps | $2.50 per 100,000 steps |
| Workflow Storage | First 720 GB-hours | $0.00069 per GB-hour |

The docs note: *"Functions invoked by Workflows continue to be charged at the existing compute rates. We encourage you to use Fluid compute with Workflow."*

So total cost = Workflow Steps + Workflow Storage + underlying Fluid Compute cost for the function bodies.

For a BigBounce-sized research program: if we ran 500 experiments/month each with 10 steps, that's 5,000 steps — comfortably inside the free tier. At 50,000+ steps/month (imagine each anomaly is its own workflow), we cross into paid territory at $2.50/100k. Very cheap.

#### Lock-in analysis

**Moderate lock-in risk.**

Pros for portability:
- The SDK is open source at `useworkflow.dev`.
- The programming model (async/await + directives) is idiomatic TypeScript, not a proprietary DSL.
- Workflows compile down to standard function routes.

Cons for portability:
- Managed persistence, event log, queues, and dashboard observability are Vercel-proprietary.
- `defineHook`, `sleep`, and the durable replay semantics require Vercel's runtime behind the scenes.
- Migrating off means implementing your own durable execution layer (Temporal, Inngest, Trigger.dev, or rolling your own).

#### Does it fit Hubify Labs?

**No, not yet.** Here's why:

1. **We already have a working orchestrator.** The existing agent loop handles multi-step experiments, retries, and human-in-the-loop. Switching to Vercel Workflows would be a rewrite from Python → TypeScript plus an architectural change (our orchestrator runs on a single Fly machine, Vercel Workflows runs on Vercel's distributed functions).

2. **Our "steps" are GPU-heavy.** Vercel Functions (what Workflow steps compile to) are CPU-only. A "step" that needs to trigger a Modal H200 training run would have to call out to Modal's API, wait, then return — which works, but Workflow's main value is the durable state + sleep, not the execution runtime. We can get durable state cheaper with Postgres.

3. **Sleep semantics don't match our workflow.** `await sleep('7 days')` is amazing for "send follow-up email in a week" but not for "this MCMC chain needs 4 hours of wall-clock GPU time." The latter is a Modal function with a 4-hour timeout, not a sleeping workflow.

4. **Lock-in cost > current pain.** Our agent orchestrator is known quantity; switching to a Vercel-proprietary durable runtime is a large rewrite with unclear ROI.

**Revisit when:** we need a workflow that genuinely spans days/weeks with human approval gates (e.g., "generate paper → wait for peer review → resume editing → submit to arxiv"), OR when the agent loop becomes the bottleneck.

#### Fit

**Parked.** Not recommended for initial Hubify Labs architecture. Custom agent orchestrator stays.

---

### Vercel Fluid Compute

**Source:** https://vercel.com/docs/fluid-compute, https://vercel.com/docs/functions/usage-and-pricing

#### What it is

Fluid Compute is Vercel's "next-gen serverless" model that landed as the default for new projects on April 23, 2025. Key differences from old-style Vercel Functions:

- **Optimized concurrency**: one function *instance* handles multiple concurrent invocations instead of one request per microVM. Dramatic cost win for I/O-bound workloads.
- **Bytecode caching** on Node.js 20+ cuts cold starts.
- **Cross-region and AZ failover** built in.
- **`waitUntil` background processing**: respond to the user, keep doing work in the background.
- **Error isolation**: one crashed request doesn't kill other in-flight requests on the same instance.

Supported runtimes: Node.js, Python, Edge, Bun, Rust.

#### Pricing (Hobby → Pro)

| Resource | Hobby included | Pro on-demand |
|---|---|---|
| Active CPU | 4 hours included | Varies by region |
| Provisioned Memory | 360 GB-hours included | Varies by region |
| Invocations | 1 million included | — |

Regional pricing (selected):

| Region | Active CPU $/hr | Provisioned Memory $/GB-hr |
|---|---:|---:|
| Washington D.C. (iad1) | $0.128 | $0.0106 |
| Cleveland (cle1) | $0.128 | $0.0106 |
| Portland (pdx1) | $0.128 | $0.0106 |
| San Francisco (sfo1) | $0.177 | $0.0147 |
| London (lhr1) | $0.177 | $0.0146 |
| Frankfurt (fra1) | $0.184 | $0.0152 |
| Singapore (sin1) | $0.160 | $0.0133 |
| Tokyo (hnd1) | $0.202 | $0.0167 |

Pro plan comes with $20/month included credit.

#### The key insight: active CPU vs provisioned memory

Vercel bills Active CPU only while code is running — I/O waits are free. Provisioned memory is billed for the entire instance lifetime (even during I/O). This is *the exact opposite* pricing model from a traditional pod: you pay almost nothing during the 90% of a request that's waiting on a DB query or LLM API, and you pay the full memory cost the entire time.

For a lab API backend that's mostly gluing together calls to Postgres, Modal, and an LLM, **Active CPU billing can be 5–10x cheaper than equivalent reserved compute**.

#### Max duration

From the default settings table:

| Plan | Default | Max |
|---|---|---|
| Hobby | 300s (5 min) | 300s (5 min) |
| Pro | 300s (5 min) | 800s (13 min) |
| Enterprise | 300s (5 min) | 800s (13 min) |

13 minutes is hard-capped even on Enterprise. That's fine for the lab API (requests finish in sub-second typically) but a hard no for research compute.

#### Pros

- **Built-in warm reuse** means cold starts are rare for an active lab API.
- **Cheap for I/O-bound APIs.** Our typical lab API request: validate auth → query Postgres → call Modal to trigger a job → return. Most of that is I/O — CPU billing is seconds.
- **Zero infra to manage.** Just ship the Next.js API routes, Vercel handles everything.
- **Cross-region failover** with no config.
- **`waitUntil` for background tasks** like logging events to the activity feed without blocking the response.

#### Cons

- **13-minute max duration** rules out any real compute. This is strictly for API routes.
- **Python runtime is available** but Node is the better-supported path.
- **Region billing varies** — iad1/cle1/pdx1 at $0.128/CPU-hr is cheapest; São Paulo is 73% more expensive at $0.221.

#### Fit

**Perfect fit for:** the Hubify Labs backend API — dashboard endpoints, pod/experiment status, lab management CRUD, webhook receivers. Stateless glue code that mostly calls other services.

**Poor fit for:** any GPU work, long-running jobs, persistent services (use Fly).

---

### Daytona.io

**Source:** https://www.daytona.io, https://www.daytona.io/pricing

#### What it is

Positioned as: *"Secure Infrastructure for Running AI-Generated Code"* with *"Sub 90ms sandbox creation from code to execution."*

This puts Daytona directly head-to-head with Vercel Sandbox in the "run untrusted code" category. The differentiator is Daytona's claimed 90ms create-to-execute time (Vercel doesn't publish a number for comparison).

#### Pricing

From the pricing page:

- Free trial: $200 in compute credits, no credit card
- Pay-as-you-go:
  - Compute: **$0.0504/hour** (~$0.000014/sec)
  - Memory: **$0.0162/GiB-hour**
  - Storage: **$0.000108/GiB-hour** (after 5 free GiB)
- Startup program: up to $50k in credits
- Enterprise: custom, on-premise setup available

GPU mentions: the page references *"8-core, 12GB GDDR6, 16-core, 32-core"* options but no specific per-hour GPU pricing was extracted.

#### Comparison to Vercel Sandbox

On paper, Daytona compute is **significantly cheaper** than Vercel Sandbox:

- Daytona: $0.0504/CPU-hour + $0.0162/GiB-hour
- Vercel: $0.128/CPU-hour + $0.0212/GB-hour

At 2 vCPU × 4 GB for 1 hour:
- Daytona: $0.1008 + $0.0648 = **$0.166/hr**
- Vercel: $0.256 + $0.0848 = **$0.341/hr**

Daytona is ~51% cheaper at that shape. Plus Daytona claims sub-90ms startup (Vercel unclear).

#### Pros

- **Cheaper than Vercel Sandbox** by ~half at comparable resource shapes.
- **Sub-90ms startup** claim is industry-leading if accurate.
- **Both cloud and on-prem** options.
- **$200 free trial + $50k startup credits** — easy to experiment.
- **GPU-capable** (sizes mentioned, though exact pricing not surfaced).

#### Cons

- **Less mature ecosystem** than Vercel. No clean Next.js integration story.
- **Website documentation thin** — the main page and pricing page were mostly CSS/chrome; we couldn't extract deep feature info without digging further.
- **No obvious "credential brokering"** equivalent to Vercel's header injection feature.
- **Unknown regions** — the docs we fetched didn't specify.
- **We would still need a second sandbox provider** for the case where lab code needs to hit Vercel-proprietary services or OIDC tokens.

#### Fit

**Plausible alternative to Vercel Sandbox** if we prioritize cost over Vercel ecosystem integration. But because our Hubify Labs web surface is Vercel-hosted, Vercel Sandbox's OIDC auth + deploy integration + credential brokering is a real ergonomic advantage. Daytona is a **strong Plan B** for the sandbox role, not the starting choice.

**Action item:** run a spike comparing Daytona vs Vercel Sandbox on the actual "execute user code against a lab dataset" workflow before Hubify Labs v1 ships. If Daytona is 50% cheaper and startup is actually 90ms, the economics become hard to ignore for heavy sandbox usage.

---

### Fly.io

**Source:** https://fly.io/docs/about/pricing/

#### What it is

Already in use for the Hubify control plane. Fly.io runs Firecracker microVMs (they call them "Fly Machines") in regions around the world. You define a `fly.toml`, run `fly deploy`, and you get a running containerized service. Machines can be started/stopped/scaled manually or via Fly's auto-scaling.

#### Pricing

Machine pricing (started machines, per second → monthly equivalent):

| Machine | Memory | Per second | ~Monthly |
|---|---|---:|---:|
| shared-cpu-1x | 256MB | $0.00000078 | $2.02 |
| shared-cpu-2x | 512MB | $0.00000156 | $4.04 |
| performance-1x | 2GB | $0.00001242 | $32.19 |
| performance-2x | 4GB | $0.00002484 | $64.39 |

Additional RAM: ~$5 per 30 days per GB.

Regional multiplier: 1.0x–1.6x depending on region.

Storage:
- Volumes: **$0.15/GB/month**
- Snapshots: **$0.08/GB/month** (first 10GB free)
- Stopped machine rootfs: **$0.15/GB for 30 days**

Bandwidth (granular rates, orgs created after July 18, 2024):
- NA/EU egress: $0.02/GB
- APAC/Oceania/SA: $0.04/GB
- Africa/India: $0.12/GB
- Static egress IPs: $0.005/hr (~$3.60/month)

#### GPU status — important

From the pricing page: *"GPUs are deprecated and will be unavailable after August 1."*

Old GPU prices (for reference only):
- A10: $0.75/hr
- L40S: $0.70/hr
- A100 40G PCIe: $1.25/hr
- A100 80G SXM: $1.50/hr

**Fly.io is out of the GPU game.** Whatever GPU work used to run on Fly is now gone. This makes the decision easy: use Modal for GPU, use Fly for non-GPU persistent services.

#### Pros

- **Very cheap small persistent machines.** $2–4/month for an always-on orchestrator is essentially free.
- **Fly Machines API is clean** — can start/stop/scale individual machines programmatically from our orchestrator.
- **Volumes are persistent** and cheap ($0.15/GB-month).
- **Global region presence** (30+ regions).
- **Already deployed.** We have existing Fly infrastructure and credentials.
- **Can auto-stop** to zero (per the docs, stopped machines pay only rootfs storage).

#### Cons

- **No GPUs after August 1.** Dead for research compute.
- **Manual deploy model** (`fly deploy`) vs the "just invoke a function" Modal ergonomics.
- **Config-heavy** (`fly.toml`, launch configs, secrets management).
- **Occasional reliability concerns** reported in community (though improving).

#### Fit

**Perfect fit for:** the Hubify Labs persistent orchestrator / agent loop, `api.hubify.com` if we want a long-running websocket server, daemon services, scheduled cron jobs running on a small always-on machine.

**Poor fit for:** anything GPU, anything bursty where pay-per-second would be cheaper (use Modal or Vercel Fluid for those).

---

### e2b.dev (parked)

**Source:** not fetched — Houston has used it and didn't love it. Mentioned only for completeness.

e2b is another "run untrusted code in a sandbox" provider, competing with Vercel Sandbox and Daytona. Houston's prior experience was unfavorable — no concrete complaint was captured but the directive is clear: **not a candidate for Hubify Labs v1**.

**Revisit only if** both Vercel Sandbox and Daytona fail the spike evaluation.

---

## Recommended Architecture

The core insight is that **there is no one compute provider** that wins at everything. The right answer is a **4-provider split** with one clear role per provider, unified behind a single Hubify Labs API gateway.

| Role | Provider | Why |
|------|----------|-----|
| **GPU experiments** (training, MCMC, anomaly sweeps) | **Modal.com** | Pay-per-second H200 billing, Modal Volumes for durable state, no mid-run credit death, 24-hour per-job cap is fine for our workload shapes |
| **Persistent orchestrator** (agent loop, task queue, cron) | **Fly.io** | $2–32/month for always-on, Fly Machines API is clean, already deployed, auto-stop to zero for dev environments |
| **Vibe-coding sandbox** (run user/AI code) | **Vercel Sandbox** | Firecracker microVMs, network firewall, snapshots, credential brokering, clean TS SDK matching our frontend. Daytona is a strong Plan B. |
| **Static lab subdomains** (`{lab}.hubify.com`) | **Vercel** | Already using it for DNS + static deploys, zero-config, Git integration |
| **Lab API backend** (`api.hubify.com`) | **Vercel Fluid Compute** | Active-CPU billing is perfect for I/O-bound API, warm reuse eliminates cold starts, 13-minute cap is fine for API routes |
| **Workflow engine** | **Custom agent-based (unchanged)** | We already have it, Vercel Workflows is lock-in, our "steps" are GPU jobs not TS functions |
| **GPU interactive debugging** (optional) | **RunPod** (keep 1 small pod) | When we need ssh into a live GPU for real-time debugging, Modal's sandbox product is not as ergonomic. A single small H100 pod on RunPod for interactive work is a reasonable hedge. |

### Unified API layer

**Critical point:** the three Hubify Labs frontends (web dashboard, TUI, macOS desktop app) all hit the **same backend API at `api.hubify.com`**, regardless of which compute provider is running the underlying work.

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Web (Next)  │  │     TUI      │  │ macOS Native │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └────────┬────────┴────────┬────────┘
                │                 │
                ▼                 ▼
       ┌────────────────────────────────┐
       │   api.hubify.com               │
       │   (Vercel Fluid Compute)       │
       │   - Auth                       │
       │   - Experiment CRUD            │
       │   - Provider router            │
       └────────┬───────────────────────┘
                │
       ┌────────┼────────┬────────────┬──────────────┐
       │        │        │            │              │
       ▼        ▼        ▼            ▼              ▼
   ┌─────┐  ┌─────┐  ┌────────┐  ┌────────┐   ┌─────────┐
   │Modal│  │Fly  │  │ Vercel │  │Postgres│   │ Modal   │
   │ GPU │  │agent│  │Sandbox │  │  DB    │   │ Volumes │
   └─────┘  └─────┘  └────────┘  └────────┘   └─────────┘
```

This means:
- The TUI can submit a training job without knowing it runs on Modal.
- The web dashboard can show sandbox output without knowing it's Vercel Sandbox under the hood.
- The macOS app can tail logs without knowing they come from Fly's log stream.
- If we ever swap Modal for Daytona GPUs, only the API router changes — clients stay the same.

### Cost estimate for a typical month

Assume moderate usage (Phase 4 shape: 5 experiments running 3 hrs/day each on H200, persistent orchestrator, light API traffic):

| Line item | Estimate |
|---|---:|
| Modal GPU (5 × 3 hrs × 30 days × $4.54) | $2,043 |
| Modal Volumes (500 GB × $0.15 assumed) | $75 |
| Fly.io orchestrator (performance-1x, 24/7) | $32 |
| Fly.io volumes (50 GB × $0.15) | $8 |
| Vercel Sandbox (1,000 5-min sessions × 2 vCPU × 4 GB) | ~$30 |
| Vercel Fluid Compute (lab API, ~1M req, mostly I/O) | ~$5 (inside Pro credit) |
| Vercel static + DNS | $20 (Pro plan base) |
| **Total** | **~$2,213/month** |

Compare to current RunPod H200 24/7: $3.59 × 24 × 30 = **$2,585/month** for a single pod at 100% reservation (but ~70% idle time).

**Projected savings: ~$370/month** by moving to pay-per-second AND we get Fly, Vercel Sandbox, and Fluid Compute *included*. This is before the real win, which is that we stop losing experiments to mid-run credit death.

### Volume consolidation: one source of truth for research artifacts

**Recommendation:** Modal Volumes becomes the **canonical store** for all research artifacts that currently live in `/workspace` on the RunPod pod. Structure:

```
modal://bigbounce-artifacts/
├── chains/
│   ├── full_tension/
│   ├── dneff/
│   └── ...
├── anomaly_catalogs/
│   ├── desi_dr1/
│   ├── sdss_dr18/
│   └── ...
├── model_weights/
├── figures/
└── checkpoints/
```

Every Modal function mounts this volume read-write. The orchestrator (Fly) can read from it via Modal's Python SDK to publish results to the website. The web UI can stream logs and previews through the `api.hubify.com` layer.

Laptop syncs: we can periodically `modal volume get` to a local mirror for offline work, just like we currently `scp` from the RunPod pod.

---

## Migration Plan

A phased migration minimizes risk. Each phase is independently valuable and can be paused or rolled back.

### Phase 0 — Baseline (1 day)

- Document current RunPod pod state: installed packages, CUDA version, Python env, contents of `/workspace`
- Snapshot current `/workspace` to S3 or similar
- List all running experiments and their expected completion dates

**Exit criterion:** we can recreate the RunPod state from scratch if needed.

### Phase 1 — Modal proof-of-concept (2–3 days)

- Sign up for Modal (use the Team plan $100 free credits)
- Port one simple GPU workload: the **f_NL Fisher forecast recompute** is a good candidate (CPU-bound numpy, short runtime, well-defined output)
- Measure: cold start time, per-function cost, volume write speed, ergonomic comparison
- Port one medium workload: **a single MCMC chain extension** on H200 (3–4 hours)
- Validate: job completes, volume persists outputs, cost matches prediction
- Measure: total cost and compare against equivalent RunPod time

**Exit criterion:** a real research result produced on Modal, stored in a Modal Volume, retrievable from the laptop. Cost within 30% of RunPod equivalent.

### Phase 2 — Modal as primary GPU (1 week)

- Port the remaining Phase 4 experiments from tmux sessions on RunPod to Modal functions
- Build a thin Python wrapper (`hubify.compute.submit_job(func, gpu='H200', timeout='4h')`) that abstracts Modal and RunPod so the agent orchestrator doesn't care which provider runs the job
- Keep the RunPod pod alive in parallel as a hedge for interactive debugging
- Sync Modal Volume back to RunPod periodically for redundancy

**Exit criterion:** all new experiments run on Modal by default. RunPod is only used for interactive ssh debugging.

### Phase 3 — Hubify Labs API backend on Vercel Fluid Compute (1 week)

- Scaffold `api.hubify.com` on Vercel (Next.js API routes + Fluid Compute enabled)
- Implement first endpoints: auth, list experiments, submit experiment, get experiment logs
- Point the existing BigBounce frontend to the new API for one or two features as a canary
- Measure: p50/p95 latency, cost per request, warm reuse effectiveness

**Exit criterion:** a real feature on `bigbounce.hubify.app` fetches data through `api.hubify.com` instead of embedding it.

### Phase 4 — Fly.io orchestrator consolidation (3–5 days)

- Audit the current agent orchestrator (wherever it runs — laptop? RunPod? Fly?)
- Deploy to a Fly performance-1x machine with a 50GB volume for task state
- Connect it to Modal via the Python SDK for GPU job submission
- Connect it to `api.hubify.com` for status reporting
- Set up cron jobs on the Fly machine for scheduled tasks (daily paper recompile, nightly data backup)

**Exit criterion:** the orchestrator runs unattended for 1 week on Fly without intervention.

### Phase 5 — Vercel Sandbox for user code (1 week, after Hubify Labs v1 launches)

- Build the "vibe-coding" feature in Hubify Labs: a code editor that runs Python/Node against a lab dataset
- Use Vercel Sandbox for execution with `deny-all` network policy by default
- Implement credential brokering for cases where the sandbox needs to hit Modal/Postgres
- Spike Daytona in parallel on the same workload, compare cost and latency
- Choose the winner

**Exit criterion:** a lab user can write a Python script in the Hubify Labs web UI, click Run, see output within 5 seconds, and the script cannot exfiltrate credentials.

### Phase 6 — RunPod sunset (contingent)

- After 30 days of stable Modal operation with zero experiments lost to provider issues, we can shrink the RunPod pod to a single A100-40GB "debug shell" that only runs during interactive sessions
- Eventually, retire RunPod entirely if Modal's Shell/interactive story matures

**Exit criterion:** RunPod monthly spend is under $200 or zero.

---

## Open Questions

These need to be answered with a real spike before fully committing:

### 1. Modal Volume pricing (blocking)

Modal's public pricing page does not list Volume storage cost per GB-month. We need to confirm this either in the logged-in dashboard or with Modal support. If it's >$0.30/GB-month, the cost picture shifts materially for our 500GB+ artifact needs. **Estimate:** likely $0.10–0.20/GB-month based on competitor pricing, but this is not confirmed.

### 2. Modal H200 cold start on a real workload

How long does a real GPU container take to boot on Modal vs just running on a hot RunPod pod? We need to measure with a workload that loads ~40GB of model weights. If cold start is consistently >60 seconds, we need to use `min_containers=1` for frequently-invoked functions, which partly re-introduces the "pay for idle" problem. **Estimate:** 10–30s for typical images with cached models, but worth measuring.

### 3. Modal 24-hour cap for long MCMC runs

Some Cobaya MCMC runs legitimately need 36+ hours to converge. Can we reliably checkpoint + chain Modal functions to run a single logical experiment across multiple 24-hour function invocations without losing correlation between chain samples? **Estimate:** yes via Cobaya's native resume, but we need to test it.

### 4. Vercel Sandbox vs Daytona spike

Build the same "run user Python against a dataset" feature twice, once on Vercel Sandbox and once on Daytona. Compare:
- Actual cold-start time (claimed: Vercel ~100s of ms, Daytona 90ms)
- Cost at 1000 sessions/day
- Ergonomic fit with our Next.js frontend
- Credential brokering / secret management story

**Estimate:** ~1 week of engineering to decide definitively.

### 5. Will Fly.io's future service quality meet the orchestrator uptime needs?

Fly had reliability issues in 2023–2024 that are reportedly resolved. For a critical 24/7 orchestrator, we need to validate sub-0.5% downtime over a month. If Fly can't deliver that, alternatives are: Modal's Function with `min_containers=1` (expensive for CPU-only work), or a small EC2/DO droplet (cheaper still but manual ops).

### 6. Hubify Labs API domain + auth strategy

We haven't decided whether `api.hubify.com` shares auth tokens with `bigbounce.hubify.app` or uses a separate OAuth layer. This blocks Phase 3 of the migration. **Recommendation:** single JWT-based auth with scopes per lab; delegate to Clerk or Auth0 if we don't want to roll our own.

### 7. macOS desktop app compute surface

Is the macOS app a native Swift shell that calls `api.hubify.com`, or does it embed a local Node/Python runtime for offline work? If offline, we need to think about local-first sync with Modal Volumes. **Recommendation:** thin native shell that hits the API, matches the web/TUI stance.

---

## Decision summary

**Adopted:**
- Modal.com for all GPU experiments (replaces RunPod primary)
- Modal Volumes for persistent research artifacts (replaces pod-local `/workspace`)
- Fly.io for the persistent agent orchestrator and long-running services
- Vercel (static + Fluid Compute) for the Hubify Labs frontend and API
- Vercel Sandbox for user/AI-generated code execution
- Custom agent-based orchestrator (unchanged)

**Parked (not now):**
- Vercel Workflows — too much lock-in rewrite for not enough gain, our GPU steps don't fit the TS function model
- Daytona.io — strong Plan B for sandbox role, spike against Vercel Sandbox before committing
- e2b.dev — prior experience negative, not a candidate for v1

**Sunset (phased):**
- RunPod reduced to a single small debug pod or retired entirely after 30 days of stable Modal operation

**Critical win on the original pain point:** Modal's pay-per-second billing + Modal Volumes **fully eliminates the "credits expire mid-run, pod dies, state lost" failure mode**. A Modal function that runs for 4 hours is billed for 14,400 seconds of compute when it finishes, not reserved 24/7. A Modal Volume that holds 500GB of chain files survives indefinitely as long as the monthly storage bill is paid. There is no equivalent of "the pod died, the chain is gone" on Modal.

---

## References

All URLs fetched on 2026-04-07 while researching this document:

- Modal pricing — https://modal.com/pricing
- Modal Volumes guide — https://modal.com/docs/guide/volumes
- Modal timeouts — https://modal.com/docs/guide/timeouts
- Modal cold start — https://modal.com/docs/guide/cold-start
- Modal sandbox — https://modal.com/docs/guide/sandbox
- Vercel Sandbox SDK reference — https://vercel.com/docs/vercel-sandbox/sdk-reference
- Vercel Sandbox CLI reference — https://vercel.com/docs/vercel-sandbox/cli-reference
- Vercel Sandbox pricing — https://vercel.com/docs/vercel-sandbox/pricing
- Vercel Workflows — https://vercel.com/docs/workflow
- Vercel Fluid Compute — https://vercel.com/docs/fluid-compute
- Vercel Fluid Compute pricing — https://vercel.com/docs/functions/usage-and-pricing
- Daytona.io homepage — https://www.daytona.io
- Daytona.io pricing — https://www.daytona.io/pricing
- Fly.io pricing — https://fly.io/docs/about/pricing/

Related internal documents in `/Users/houstongolden/Desktop/CODE_2025/bigbounce/project-context/`:

- `active_pods_and_pipelines.md` — current RunPod state
- `INFRASTRUCTURE_MAP.md` — existing provider topology
- `hubify-labs-platform-plan.md` — Hubify Labs platform plan
- `HUBIFY_LABS_PRD.md` — Hubify Labs product requirements
- `hubify_lab_vision.md` — Hubify lab vision
- `gpu-inference-playbook.md` — GPU inference performance playbook (the 32x DataLoader speedup story)
