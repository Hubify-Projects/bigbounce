import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  // ── Review System ──
  reviews: defineTable({
    pipelineId: v.string(),
    objectId: v.string(),
    label: v.string(),
    aiLabel: v.string(),
    aiReason: v.string(),
    humanNotes: v.string(),
    reviewerName: v.string(),
    reviewedAt: v.number(),
    metadata: v.any(),
  })
    .index("by_pipeline", ["pipelineId"])
    .index("by_pipeline_object", ["pipelineId", "objectId"]),

  checklistItems: defineTable({
    pipelineId: v.string(),
    category: v.string(),
    text: v.string(),
    status: v.string(),
    updatedAt: v.number(),
  }).index("by_pipeline", ["pipelineId"]),

  pipelineState: defineTable({
    pipelineId: v.string(),
    name: v.string(),
    status: v.string(),
    gatesPassed: v.number(),
    totalGates: v.number(),
    lastUpdated: v.number(),
    summary: v.string(),
  }).index("by_pipeline", ["pipelineId"]),

  models: defineTable({
    pipelineId: v.string(),
    modelName: v.string(),
    version: v.string(),
    huggingfaceUrl: v.string(),
    trainingSamples: v.number(),
    metrics: v.any(),
    createdAt: v.number(),
  }).index("by_pipeline", ["pipelineId"]),

  // ── Chat Logging ──
  chatMessages: defineTable({
    sessionId: v.string(),
    role: v.string(),
    content: v.string(),
    pageContext: v.optional(v.object({
      title: v.optional(v.string()),
      path: v.optional(v.string()),
    })),
    ipHash: v.optional(v.string()),
    timestamp: v.number(),
  })
    .index("by_session", ["sessionId", "timestamp"])
    .index("by_timestamp", ["timestamp"]),

  // ── Activity Feed ──
  activityFeed: defineTable({
    type: v.string(),
    date: v.string(),
    title: v.string(),
    body: v.string(),
    tags: v.array(v.object({
      label: v.string(),
      kind: v.string(),
    })),
    createdAt: v.number(),
  }).index("by_date", ["createdAt"]),

  // ── MCMC Convergence Status ──
  mcmcStatus: defineTable({
    dataset: v.string(),
    rhat: v.any(),
    ess: v.any(),
    drift: v.any(),
    parameterMeans: v.any(),
    converged: v.boolean(),
    timestamp: v.number(),
  })
    .index("by_dataset", ["dataset", "timestamp"]),

  // ── Spectral Pipeline Results ──
  spectralResults: defineTable({
    pipelineId: v.string(),
    targetId: v.string(),
    ra: v.number(),
    dec: v.number(),
    anomalyScore: v.number(),
    anomalyType: v.string(),
    worstRegion: v.string(),
    regionB: v.number(),
    regionR: v.number(),
    regionZ: v.number(),
    simbadStatus: v.string(),
    batchId: v.string(),
    processedAt: v.number(),
  })
    .index("by_pipeline", ["pipelineId"])
    .index("by_score", ["pipelineId", "anomalyScore"])
    .index("by_batch", ["batchId"]),

  // ── Page Analytics ──
  pageViews: defineTable({
    path: v.string(),
    referrer: v.optional(v.string()),
    sessionHash: v.optional(v.string()),
    timestamp: v.number(),
  }).index("by_path", ["path", "timestamp"])
    .index("by_timestamp", ["timestamp"]),

  // ── Galaxy Chirality Catalog (8.47M galaxies) ──
  galaxies: defineTable({
    dr8_id: v.string(),
    p_cw: v.float64(),
    p_ccw: v.float64(),
    p_ns: v.float64(),
    classification: v.string(),  // "CW" | "CCW" | "NOT_SPIRAL"
    confidence: v.float64(),
  })
    .index("by_classification", ["classification"])
    .index("by_confidence", ["confidence"])
    .index("by_dr8_id", ["dr8_id"]),

  // ──────────────────────────────────────────────────────────────────────
  // Paper-level orchestration (added 2026-05-29 per DATA_MODEL_ARCHITECTURE.md)
  // ──────────────────────────────────────────────────────────────────────

  // Canonical per-paper state. Readiness is COMPUTED from open findings (see
  // convex/papers.ts query getPaperState), NEVER hand-set. This is the
  // structural fix for the "I forgot to bump readiness after 5 closures" drift.
  papers: defineTable({
    slug: v.string(),                  // "paper-1a"
    number: v.string(),                // "1A"
    title: v.string(),
    shortTitle: v.string(),
    targetJournal: v.union(
      v.literal("PRD"),
      v.literal("MNRAS"),
      v.literal("JCAP"),
      v.literal("ApJ"),
      v.literal("other")
    ),
    status: v.union(
      v.literal("active-drive-to-100"),       // P1B, P2, P3, P5 right now
      v.literal("paused-houston-external"),   // P1A, P4 right now
      v.literal("submitted-arxiv"),
      v.literal("in-revision"),
      v.literal("accepted")
    ),
    // Path to .tex source relative to repo root, e.g.
    // "arxiv/paper1a_ech_nogo.tex" or "pipelines/p3_anomaly_engine/paper3_draft.tex"
    texPath: v.string(),
    // Path to the rendered PDF in site/public/papers/ that the site links to.
    sitePdfPath: v.string(),
    // Focus areas for the external-review prompt generator. Replaces the
    // hardcoded focusAreas array in site/src/app/papers/[slug]/page.tsx.
    focusAreas: v.array(v.string()),
    // Houston-only sign-off (final 1% per feedback_99_pct_readiness_cap).
    houstonSignOff: v.optional(v.string()),  // ISO date
    houstonSignOffNote: v.optional(v.string()),
    // Novelty tier per /never-claim-n4 standing directive. Self-claim ceiling is
    // N3; N4 is reserved for paradigm-shifting work awarded by the field over
    // time and cannot be set on a paper by the authors. The enum here enforces
    // that ceiling at the schema layer — Convex will reject any write of "N4".
    // See project-context/SSOT/novelty-tiers.md for tier definitions.
    novelty: v.optional(v.union(
      v.literal("N1"),
      v.literal("N2"),
      v.literal("N3")
    )),
  })
    .index("by_slug", ["slug"])
    .index("by_status", ["status"]),

  // Append-only version history per paper. Each .tex bump writes a new row.
  // The Paper's "current version" is the most recent row by datestamp.
  paper_versions: defineTable({
    paperSlug: v.string(),             // FK to papers.slug
    version: v.string(),               // "v1A.0.36"
    datestamp: v.string(),             // ISO date "2026-05-28"
    texCommit: v.string(),             // git SHA of the .tex file at this version
    pdfMd5: v.string(),
    pdfPages: v.number(),
    pdfSizeBytes: v.number(),
    changelog: v.string(),             // single-paragraph human summary
    arxivTarballPath: v.optional(v.string()),
    arxivTarballSizeBytes: v.optional(v.number()),
    createdAt: v.number(),
  })
    .index("by_paper", ["paperSlug", "datestamp"]),

  // Cross-vendor adversarial peer-review rounds. Each fire of
  // tools/cross_vendor_review_direct.py creates one row here.
  r_rounds: defineTable({
    paperSlug: v.string(),             // FK to papers.slug
    paperVersionReviewed: v.string(),  // e.g. "v3.1.68"
    roundLabel: v.string(),            // "2026-05-29_R-direct-v1b"
    source: v.union(
      v.literal("openrouter"),          // legacy
      v.literal("direct"),              // direct vendor SDKs (preferred)
      v.literal("subagent"),            // Claude subagent simulation
      v.literal("houston-external")     // Houston copy/paste into ChatGPT/Gemini/etc
    ),
    vendors: v.array(v.string()),       // ["gpt-4o", "gemini-2.5-pro", "grok-4", "sonar-pro"]
    dispatchedAt: v.number(),
    completedAt: v.optional(v.number()),
    promptText: v.optional(v.string()), // archive of the prompt sent (for reproducibility)
  })
    .index("by_paper", ["paperSlug", "dispatchedAt"])
    .index("by_label", ["roundLabel"]),

  // Individual findings from R-rounds. The truth-audit verdict and the
  // closure method are first-class fields — no more "closed by caveat-as-closure"
  // anti-pattern without an explicit flag.
  findings: defineTable({
    roundId: v.id("r_rounds"),
    paperSlug: v.string(),             // denormalized for fast paper-level queries
    reviewerName: v.string(),          // "GPT5_methodology" | "Gemini25Pro_cosmology" | ...
    findingId: v.string(),             // "PAPER-GRO-M2"
    classification: v.union(
      v.literal("BLOCKER"),
      v.literal("MAJOR"),
      v.literal("MINOR"),
      v.literal("NIT")
    ),
    location: v.string(),              // "§sec:fnl L310" | "abstract" | "Table I caption"
    claim: v.string(),                 // what the reviewer said is wrong
    proposedFix: v.string(),
    // Truth-audit per feedback_peer_review_truth_audit_protocol — every finding
    // MUST be audited before closure work. The audit verdict + evidence ARE the
    // first-class closure path; "closed-by-truth-audit-falsification" is just as
    // valid an outcome as "closed-by-real-action".
    truthAuditVerdict: v.optional(v.union(
      v.literal("VERIFIED"),            // claim accurate → real-action closure needed
      v.literal("FALSIFIED"),           // claim wrong → audit-only closure
      v.literal("STALE"),               // was true earlier, already closed in prior version
      v.literal("OUT-OF-SCOPE"),
      v.literal("OPINION")              // stylistic / preference, not a defect
    )),
    truthAuditEvidence: v.optional(v.string()),  // citation to .tex line / artifact / paper section
    closureStatus: v.union(
      v.literal("open"),
      v.literal("in-progress"),
      v.literal("closed-by-real-action"),
      v.literal("closed-by-truth-audit-falsification"),
      v.literal("closed-by-artifact-verification"),
      v.literal("deferred-genuine")     // VERY rare; needs explicit Houston OK
    ),
    closureCommit: v.optional(v.string()),       // git SHA
    closureArtifact: v.optional(v.string()),     // path to script/JSON that proves closure
    closureNote: v.optional(v.string()),
    closedAt: v.optional(v.number()),
  })
    .index("by_round", ["roundId"])
    .index("by_paper", ["paperSlug", "closureStatus"])
    .index("by_status", ["closureStatus"]),

  // Paper-internal §pathc_caveats deferral list. Distinct from r_rounds
  // findings because these are author-tracked items (e.g. P3's items a-j)
  // rather than external-reviewer-surfaced items.
  pathc_caveats: defineTable({
    paperSlug: v.string(),
    label: v.string(),                  // "a" | "b" | "c" | ... | "j"
    description: v.string(),
    status: v.union(
      v.literal("open"),
      v.literal("deferred"),
      v.literal("closed")
    ),
    // Critical anti-pattern guard per Houston's 2026-05-29 pushback
    // "simply disclosing deferred items and caveats IS NOT REAL SCIENCE":
    closureMethod: v.optional(v.union(
      v.literal("real-computation"),     // actually ran the analysis
      v.literal("artifact-verification"), // verified existing on-disk artifact already proves it
      v.literal("truth-audit-falsification"), // R-round flagged it, audit showed claim was wrong
      v.literal("text-only-no-real-action") // ⚠️ FLAG — this is the caveat-as-closure smell
    )),
    closureArtifact: v.optional(v.string()),
    closureCommit: v.optional(v.string()),
    closureNote: v.optional(v.string()),
    closedAt: v.optional(v.number()),
  })
    .index("by_paper", ["paperSlug", "status"]),

  // RunPod lifecycle + cost accounting. Replaces the ad-hoc pod_runs/*.log
  // files. Closes the "1 RUNNING pod, what's on it?" mystery.
  pods: defineTable({
    podId: v.string(),                  // RunPod ID, e.g. "ijzftpy3klystt"
    name: v.string(),                   // "cobaya-r43-v2"
    status: v.union(
      v.literal("running"),
      v.literal("exited"),
      v.literal("terminated")
    ),
    gpu: v.string(),                    // "RTX A5000" | "H200 SXM" | ...
    volumeGb: v.number(),               // persistent volume size
    containerGb: v.number(),
    hourlyCostUsd: v.number(),
    startedAt: v.number(),
    stoppedAt: v.optional(v.number()),
    totalCostUsd: v.number(),
    purpose: v.string(),                // human description: "iter2 Cobaya chain for P1A/P1B"
    artifactsBackedUp: v.boolean(),
    backupLocations: v.array(v.string()), // ["HF:bamfai/bigbounce-mcmc/iter2_converged_2026-05-18/", "local:reproducibility/cosmology/iter2_..."]
    lastSyncedAt: v.number(),           // when we last polled RunPod GraphQL for this pod
    // 2026-06-09: per-job tracking so the site shows WHAT runs on the pod,
    // not just that a pod exists. One row per tmux job (C1/C2/C3/C5 etc).
    jobs: v.optional(
      v.array(
        v.object({
          name: v.string(),          // "C1 P1B NaMaster fsky sweep"
          paper: v.string(),         // "paper-1b"
          tmuxSession: v.string(),   // "c1"
          status: v.union(
            v.literal("queued"),
            v.literal("running"),
            v.literal("done"),
            v.literal("failed")
          ),
          etaNote: v.string(),       // "~4h, ETA 2026-06-09 16:00 PT"
          outputPath: v.optional(v.string()),
        })
      )
    ),
  })
    .index("by_pod_id", ["podId"])
    .index("by_status", ["status"]),

  // ──────────────────────────────────────────────────────────────────────
  // Gap #1 (closed 2026-06-03) — notable contributions + external reviews.
  //
  // papers_notables = per-paper "novelty highlights" bullets for the
  //   detail page; distinct from focusAreas (which targets reviewers).
  //   Reader-facing 2-4 bullets that capture what's notable about the
  //   paper.
  //
  // papers_externalReviews = referee-report metadata (one row per report).
  //   Distinct from r_rounds (which is the direct-vendor adversarial
  //   review pipeline). Stores Houston-paste, journal referees, arxiv
  //   endorser comments, and internal-stage3 multi-vendor synthesis
  //   rollups.
  // ──────────────────────────────────────────────────────────────────────
  papers_notables: defineTable({
    paperSlug: v.string(),
    ordinal: v.number(),                 // display order (1 = top)
    bullet: v.string(),                  // short rendered string, supports MathText
    citationKey: v.optional(v.string()), // FK to a future citations table
    createdAt: v.number(),
  }).index("by_paper", ["paperSlug", "ordinal"]),

  // ──────────────────────────────────────────────────────────────────
  // paper_figures — per-paper canonical figure list, sourced from each
  // paper's current .tex \includegraphics + \caption block via
  // tools/seed_paper_figures.mjs. Drives /figures so the page stays in
  // sync with the live .tex (no manual figures.ts maintenance).
  // ──────────────────────────────────────────────────────────────────
  paper_figures: defineTable({
    paperSlug: v.string(),               // p1a | p1b | p2 | p3 | p4 | p5
    ordinal: v.number(),                 // appearance order; in-paper: 1..N, candidates: 100..N
    src: v.string(),                     // public path e.g. /images/foo.png
    alt: v.string(),                     // accessibility alt text
    title: v.string(),                   // short label "Figure 3"-style heading
    desc: v.string(),                    // caption (truncated)
    paperVersion: v.string(),            // version this figure was seeded from
    citationLabel: v.optional(v.string()),
    // 2026-06-09: status distinguishes figures currently \includegraphics-ed
    // in the .tex (in-paper) from valid candidate figures that exist on disk
    // but are NOT yet in the paper (candidate). Houston uses this on the
    // paper detail page to pick which candidates to re-add to the .tex.
    // Retracted figures (bad science / corrected) are flagged "retracted"
    // and excluded from default gallery views.
    status: v.optional(
      v.union(
        v.literal("in-paper"),
        v.literal("candidate"),
        v.literal("retracted"),
      ),
    ),
    addedAt: v.number(),
  })
    .index("by_paper", ["paperSlug"])
    .index("by_paper_ordinal", ["paperSlug", "ordinal"])
    .index("by_paper_status", ["paperSlug", "status"]),

  papers_externalReviews: defineTable({
    paperSlug: v.string(),
    source: v.union(
      v.literal("journal"),
      v.literal("arxiv"),
      v.literal("houston-paste"),
      v.literal("colleague-private"),
      v.literal("internal-stage3")
    ),
    reviewerLabel: v.string(),           // "MNRAS referee 1" | "Gemini-2.5-Pro" | ...
    receivedAt: v.string(),              // ISO date
    blockerCount: v.number(),            // post-truth-audit VERIFIED counts
    majorCount: v.number(),
    minorCount: v.number(),
    recommendation: v.union(
      v.literal("accept"),
      v.literal("minor-revisions"),
      v.literal("major-revisions"),
      v.literal("reject"),
      v.literal("pending")
    ),
    rRoundId: v.optional(v.id("r_rounds")),
    pdfUrl: v.optional(v.string()),      // GitHub/Drive link to full report
    notes: v.optional(v.string()),
  })
    .index("by_paper", ["paperSlug", "receivedAt"])
    .index("by_source", ["source", "receivedAt"]),

  // Task tracker: cross-paper + per-paper open work items. The "should
  // I do this now?" queue for any agent that wants to contribute.
  tasks: defineTable({
    paperSlug: v.optional(v.string()),  // null for cross-paper / infrastructure tasks
    title: v.string(),
    description: v.string(),
    priority: v.union(
      v.literal("P0"),
      v.literal("P1"),
      v.literal("P2")
    ),
    owner: v.union(
      v.literal("agent"),
      v.literal("houston")
    ),
    status: v.union(
      v.literal("pending"),
      v.literal("in-progress"),
      v.literal("blocked"),
      v.literal("done")
    ),
    blockedBy: v.optional(v.array(v.id("tasks"))),
    createdAt: v.number(),
    closedAt: v.optional(v.number()),
    closureCommit: v.optional(v.string()),
  })
    .index("by_status", ["status", "priority"])
    .index("by_paper", ["paperSlug", "status"])
    .index("by_owner", ["owner", "status"]),
});
