#!/usr/bin/env node
/**
 * Bigbounce MCP server — Phase 2 of the data-model rebuild
 * (project-context/DATA_MODEL_ARCHITECTURE.md).
 *
 * Exposes the Convex-backed paper-orchestration state as MCP tools so
 * Claude Code (and any other MCP-aware agent) can read/write live paper
 * status, R-round findings, §pathc_caveats closures, pod lifecycle, and
 * tasks without hand-editing 5+ unsynced files.
 *
 * Stdio transport. Wire into Claude Code via bigbounce/.claude/mcp_servers.json:
 *
 *   {
 *     "mcpServers": {
 *       "bigbounce": {
 *         "command": "node",
 *         "args": ["./mcp/bigbounce-mcp/dist/index.js"],
 *         "env": { "CONVEX_URL": "<your-convex-deployment-url>" }
 *       }
 *     }
 *   }
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { ConvexHttpClient } from "convex/browser";
import { z } from "zod";

const CONVEX_URL = process.env.CONVEX_URL || process.env.NEXT_PUBLIC_CONVEX_URL;
if (!CONVEX_URL) {
  console.error(
    "FATAL: CONVEX_URL (or NEXT_PUBLIC_CONVEX_URL) env var required. See bigbounce/.claude/mcp_servers.json for how to set it."
  );
  process.exit(1);
}

const convex = new ConvexHttpClient(CONVEX_URL);

// ──────────────────────────────────────────────────────────────────────
// Tool descriptors — the 10 tools per DATA_MODEL_ARCHITECTURE.md Layer 2.
// ──────────────────────────────────────────────────────────────────────

const TOOLS = [
  {
    name: "bigbounce_list_papers",
    description:
      "List all 6 (or however many) papers with their computed-readiness state. Returns each paper's number, slug, shortTitle, status (active-drive-to-100 | paused-houston-external | submitted-arxiv | ...), currentVersion, lastUpdated, readinessComputed (0-100, derived from open findings + open caveats; capped at 95 pre-Houston-sign-off), and counts of open BLOCKER/MAJOR/MINOR findings + open §pathc_caveats items. Read-only. The single canonical 'where are we?' query.",
    inputSchema: { type: "object", properties: {}, required: [] },
    handler: async () => convex.query("papers:listAllPaperStates" as any, {}),
  },
  {
    name: "bigbounce_get_paper",
    description:
      "Get full state for one paper by slug (e.g. 'paper-1a', 'paper-3'). Returns paper metadata + currentVersion + version history + R-round count + findings counts + caveat counts + computed readiness. Read-only.",
    inputSchema: {
      type: "object",
      properties: {
        slug: { type: "string", description: "Paper slug (e.g. 'paper-3')" },
      },
      required: ["slug"],
    },
    handler: async (args: { slug: string }) =>
      convex.query("papers:getPaperState" as any, { slug: args.slug }),
  },
  {
    name: "bigbounce_list_open_findings",
    description:
      "List open R-round findings (closureStatus = open | in-progress). Optional filter by paperSlug. Returns each finding's roundId, reviewerName, findingId, classification (BLOCKER/MAJOR/MINOR/NIT), location, claim, proposedFix, and truthAuditVerdict if already audited. The work-queue for the next closure.",
    inputSchema: {
      type: "object",
      properties: {
        paperSlug: { type: "string", description: "Optional paper slug filter" },
      },
      required: [],
    },
    handler: async (args: { paperSlug?: string }) => {
      if (args.paperSlug) {
        return convex.query("findings:listForPaper" as any, {
          paperSlug: args.paperSlug,
          status: "open",
        });
      }
      return convex.query("findings:listOpen" as any, {});
    },
  },
  {
    name: "bigbounce_truth_audit_finding",
    description:
      "Apply truth-audit verdict to a finding per feedback_peer_review_truth_audit_protocol. MUST run before close_finding. Verdict: VERIFIED (claim accurate → real-action closure needed) | FALSIFIED (claim wrong → close as truth-audit-falsification) | STALE (was true earlier, already closed) | OUT-OF-SCOPE | OPINION (stylistic preference, not a defect). Evidence: short citation to .tex line / artifact / paper section that justifies the verdict.",
    inputSchema: {
      type: "object",
      properties: {
        findingId: { type: "string", description: "Convex finding _id" },
        verdict: {
          type: "string",
          enum: ["VERIFIED", "FALSIFIED", "STALE", "OUT-OF-SCOPE", "OPINION"],
        },
        evidence: { type: "string" },
      },
      required: ["findingId", "verdict", "evidence"],
    },
    handler: async (args: {
      findingId: string;
      verdict: string;
      evidence: string;
    }) =>
      convex.mutation("findings:truthAudit" as any, {
        findingId: args.findingId as any,
        verdict: args.verdict as any,
        evidence: args.evidence,
      }),
  },
  {
    name: "bigbounce_close_finding",
    description:
      "Close a finding atomically. Always requires closureStatus: closed-by-real-action | closed-by-truth-audit-falsification | closed-by-artifact-verification | deferred-genuine (rare; needs explicit Houston OK). Provide closureCommit (git SHA) and closureArtifact (path to script/JSON that proves closure) where applicable. The site re-renders on Convex subscription; no manual papers.ts edit needed.",
    inputSchema: {
      type: "object",
      properties: {
        findingId: { type: "string", description: "Convex finding _id" },
        closureStatus: {
          type: "string",
          enum: [
            "closed-by-real-action",
            "closed-by-truth-audit-falsification",
            "closed-by-artifact-verification",
            "deferred-genuine",
          ],
        },
        closureCommit: { type: "string" },
        closureArtifact: { type: "string" },
        closureNote: { type: "string" },
      },
      required: ["findingId", "closureStatus"],
    },
    handler: async (args: any) =>
      convex.mutation("findings:close" as any, {
        findingId: args.findingId as any,
        closureStatus: args.closureStatus,
        closureCommit: args.closureCommit,
        closureArtifact: args.closureArtifact,
        closureNote: args.closureNote,
      }),
  },
  {
    name: "bigbounce_bump_paper_version",
    description:
      "Append a new paper_version row (atomic .tex version bump). Site re-renders on Convex subscription — eliminates the 'I forgot to update the site version after pdflatex compile' drift. Args: paperSlug, version (e.g. 'v3.1.70'), datestamp (ISO), texCommit (git SHA), pdfMd5, pdfPages, pdfSizeBytes, changelog (short human summary), arxivTarballPath/Size optional.",
    inputSchema: {
      type: "object",
      properties: {
        paperSlug: { type: "string" },
        version: { type: "string" },
        datestamp: { type: "string" },
        texCommit: { type: "string" },
        pdfMd5: { type: "string" },
        pdfPages: { type: "number" },
        pdfSizeBytes: { type: "number" },
        changelog: { type: "string" },
        arxivTarballPath: { type: "string" },
        arxivTarballSizeBytes: { type: "number" },
      },
      required: [
        "paperSlug",
        "version",
        "datestamp",
        "texCommit",
        "pdfMd5",
        "pdfPages",
        "pdfSizeBytes",
        "changelog",
      ],
    },
    handler: async (args: any) =>
      convex.mutation("paperVersions:bump" as any, args),
  },
  {
    name: "bigbounce_list_pathc_caveats",
    description:
      "List §pathc_caveats items for a paper (open + closed). Each item has label (a/b/c/...), description, status, closureMethod (real-computation | artifact-verification | truth-audit-falsification | ⚠️ text-only-no-real-action), closureArtifact, closureCommit. Read-only.",
    inputSchema: {
      type: "object",
      properties: { paperSlug: { type: "string" } },
      required: ["paperSlug"],
    },
    handler: async (args: { paperSlug: string }) =>
      convex.query("pathcCaveats:listForPaper" as any, {
        paperSlug: args.paperSlug,
      }),
  },
  {
    name: "bigbounce_close_pathc_caveat",
    description:
      "Close a §pathc_caveats item. closureMethod is REQUIRED and the 'text-only-no-real-action' value is an explicit ⚠️ FLAG against the caveat-as-closure anti-pattern (Houston 2026-05-29: 'simply disclosing deferred items and caveats IS NOT REAL SCIENCE'). Prefer real-computation or artifact-verification when possible.",
    inputSchema: {
      type: "object",
      properties: {
        paperSlug: { type: "string" },
        label: { type: "string", description: "Caveat label (a/b/c/...)" },
        closureMethod: {
          type: "string",
          enum: [
            "real-computation",
            "artifact-verification",
            "truth-audit-falsification",
            "text-only-no-real-action",
          ],
        },
        closureArtifact: { type: "string" },
        closureCommit: { type: "string" },
        closureNote: { type: "string" },
      },
      required: ["paperSlug", "label", "closureMethod"],
    },
    handler: async (args: any) =>
      convex.mutation("pathcCaveats:close" as any, args),
  },
  {
    name: "bigbounce_list_pods",
    description:
      "List RunPod state from Convex (synced periodically from RunPod GraphQL). Each row has podId, name, status (running | exited | terminated), gpu, volume/container sizes, hourlyCostUsd, totalCostUsd, purpose, artifactsBackedUp boolean, backupLocations array. Read-only.",
    inputSchema: {
      type: "object",
      properties: {
        statusFilter: {
          type: "string",
          enum: ["running", "exited", "terminated"],
        },
      },
      required: [],
    },
    handler: async (args: { statusFilter?: string }) => {
      if (args.statusFilter === "running") {
        return convex.query("pods:listRunning" as any, {});
      }
      return convex.query("pods:list" as any, {});
    },
  },
  {
    name: "bigbounce_get_external_review_prompt",
    description:
      "Get the canonical copy/paste external-review prompt for a paper. The prompt is generated from current Convex state (paper title + version + pdfMeta + focusAreas + open §pathc_caveats items) — replaces the hardcoded focusAreas array in site/src/app/papers/[slug]/page.tsx that drifted out of sync. Returns { paperSlug, paperVersion, pdfPath, prompt }.",
    inputSchema: {
      type: "object",
      properties: { slug: { type: "string" } },
      required: ["slug"],
    },
    handler: async (args: { slug: string }) =>
      convex.query("papers:getExternalReviewPrompt" as any, {
        slug: args.slug,
      }),
  },
  {
    name: "bigbounce_list_tasks",
    description:
      "List open tasks across papers + infrastructure. Optional filter by status (pending/in-progress/blocked/done), owner (agent/houston), or paperSlug. The 'what should I work on next?' query for any agent contributing to the project.",
    inputSchema: {
      type: "object",
      properties: {
        status: {
          type: "string",
          enum: ["pending", "in-progress", "blocked", "done"],
        },
        owner: { type: "string", enum: ["agent", "houston"] },
        paperSlug: { type: "string" },
      },
      required: [],
    },
    handler: async (args: any) => convex.query("tasks:list" as any, args),
  },
];

// ──────────────────────────────────────────────────────────────────────
// MCP server boilerplate
// ──────────────────────────────────────────────────────────────────────

const server = new Server(
  { name: "bigbounce", version: "0.1.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: TOOLS.map((t) => ({
    name: t.name,
    description: t.description,
    inputSchema: t.inputSchema,
  })),
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const tool = TOOLS.find((t) => t.name === request.params.name);
  if (!tool) {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
  try {
    const result = await tool.handler(request.params.arguments as any);
    return {
      content: [
        { type: "text", text: JSON.stringify(result, null, 2) },
      ],
    };
  } catch (err: any) {
    return {
      content: [
        {
          type: "text",
          text: `ERROR calling ${request.params.name}: ${err.message ?? String(err)}`,
        },
      ],
      isError: true,
    };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);

console.error(
  `bigbounce-mcp v0.1.0 ready. ${TOOLS.length} tools registered. CONVEX_URL=${CONVEX_URL}`
);
