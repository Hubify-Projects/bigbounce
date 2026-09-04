import type { Metadata } from "next";
import Link from "next/link";
import { papers } from "@/data/papers";
import {
  Band,
  PageHeader,
  DataTable,
  type DataTableColumn,
} from "@/components/primitives";

// Readiness caps sourced from papers.ts (canonical static mirror of Convex) so
// this board can never drift out of sync with the paper pages.
const capBySlug = new Map(papers.map((p) => [p.slug, p.readiness]));
const capOf = (slug: string) => capBySlug.get(slug) ?? 0;
const avgCap = Math.round(
  papers.reduce((acc, p) => acc + p.readiness, 0) / Math.max(1, papers.length),
);

export const metadata: Metadata = {
  title: "Architecture — API & MCP",
  description:
    "BigBounce data model, Convex API, and MCP tool catalog — the discoverable interface for any agent (Claude Code, Codex, Cursor) contributing to the project.",
};

interface McpTool {
  name: string;
  summary: string;
  input: string;
  returns: string;
}

const MCP_TOOLS: McpTool[] = [
  {
    name: "bigbounce_list_papers",
    summary:
      "Cross-paper dashboard with computed-readiness state. Read-only. The canonical 'where are we?' query.",
    input: "(none)",
    returns:
      "Array<{ slug, number, shortTitle, status, currentVersion, lastUpdated, readinessComputed, openBlockers, openMajors, openMinors, openCaveats, houstonSignOff }>",
  },
  {
    name: "bigbounce_get_paper",
    summary:
      "Full state for one paper by slug. Includes version history + R-round count + caveat counts + computed readiness.",
    input: "{ slug: string }",
    returns: "Paper state object (full)",
  },
  {
    name: "bigbounce_list_open_findings",
    summary:
      "R-round work queue. Open findings (closureStatus = open | in-progress), optionally filtered by paper.",
    input: "{ paperSlug?: string }",
    returns: "Array<Finding>",
  },
  {
    name: "bigbounce_truth_audit_finding",
    summary:
      "Apply truth-audit verdict to a finding (required before close, per the review truth-audit protocol).",
    input: "{ findingId: string, verdict: VERIFIED|FALSIFIED|STALE|OUT-OF-SCOPE|OPINION, evidence: string }",
    returns: "void (mutation)",
  },
  {
    name: "bigbounce_close_finding",
    summary: "Atomic finding closure. Enforces the closureStatus enum + truth-audit-first ordering.",
    input: "{ findingId: string, closureStatus: enum, closureCommit?: string, closureArtifact?: string, closureNote?: string }",
    returns: "void (mutation)",
  },
  {
    name: "bigbounce_bump_paper_version",
    summary:
      "Atomic .tex version bump. Site re-renders on Convex subscription — eliminates a 5-file hand-edit.",
    input: "{ paperSlug, version, datestamp, texCommit, pdfMd5, pdfPages, pdfSizeBytes, changelog, arxivTarballPath?, arxivTarballSizeBytes? }",
    returns: "Id<paper_versions>",
  },
  {
    name: "bigbounce_list_pathc_caveats",
    summary: "Per-paper §pathc_caveats deferral list. Each item has a closureMethod enum.",
    input: "{ paperSlug: string }",
    returns: "Array<PathcCaveat>",
  },
  {
    name: "bigbounce_close_pathc_caveat",
    summary: "Close a §pathc_caveats item. closureMethod enum includes an explicit text-only-no-real-action flag.",
    input: "{ paperSlug, label, closureMethod: enum, closureArtifact?, closureCommit?, closureNote? }",
    returns: "void (mutation)",
  },
  {
    name: "bigbounce_list_pods",
    summary: "RunPod state synced from Convex. Includes cost accounting + backup-location tracking.",
    input: "{ statusFilter?: 'running'|'exited'|'terminated' }",
    returns: "Array<Pod>",
  },
  {
    name: "bigbounce_get_external_review_prompt",
    summary: "Dynamic copy/paste external-review prompt for a paper's live PDF.",
    input: "{ slug: string }",
    returns: "{ paperSlug, paperVersion, pdfPath, prompt }",
  },
  {
    name: "bigbounce_list_tasks",
    summary: "Cross-paper + per-paper open task queue.",
    input: "{ status?, owner?, paperSlug? }",
    returns: "Array<Task>",
  },
];

const CONVEX_TABLES = [
  { name: "papers", purpose: "Canonical per-paper state (NOT readiness — that's computed)." },
  { name: "paper_versions", purpose: "Append-only .tex version history." },
  { name: "r_rounds", purpose: "Cross-vendor peer-review rounds." },
  { name: "findings", purpose: "Individual R-round findings with a truth-audit lifecycle." },
  { name: "pathc_caveats", purpose: "Paper-internal §pathc_caveats deferrals." },
  { name: "pods", purpose: "RunPod lifecycle + cost accounting." },
  { name: "tasks", purpose: "Open work queue (cross-paper + infrastructure)." },
];

const tableColumns: DataTableColumn<(typeof CONVEX_TABLES)[number]>[] = [
  { key: "name", header: "Table", mono: true, accessor: (t) => t.name },
  { key: "purpose", header: "Purpose", accessor: (t) => t.purpose },
];

const toolColumns: DataTableColumn<McpTool>[] = [
  { key: "name", header: "Tool", mono: true, accessor: (t) => t.name },
  {
    key: "summary",
    header: "Summary",
    render: (t) => <span style={{ whiteSpace: "normal", maxWidth: "40ch", display: "inline-block" }}>{t.summary}</span>,
  },
  {
    key: "input",
    header: "Input",
    mono: true,
    render: (t) => <span style={{ whiteSpace: "normal", maxWidth: "28ch", display: "inline-block" }}>{t.input}</span>,
  },
  {
    key: "returns",
    header: "Returns",
    mono: true,
    render: (t) => <span style={{ whiteSpace: "normal", maxWidth: "32ch", display: "inline-block" }}>{t.returns}</span>,
  },
];

const SKILLS = [
  { cmd: "/bigbounce-status", desc: "dashboard" },
  { cmd: "/bigbounce-r-round <paper-slug>", desc: "fire direct-vendor R-round, write findings to Convex" },
  { cmd: "/bigbounce-truth-audit <findingId> <verdict> <evidence>", desc: "required before close" },
  { cmd: "/bigbounce-close", desc: "atomic finding/caveat closure" },
  { cmd: "/bigbounce-bump <paper-slug> <version>", desc: "atomic version bump, site re-renders" },
];

const GUARDS = [
  {
    title: "No caveat-as-closure.",
    body: "closeFinding + closePathcCaveat require an explicit closureMethod enum. The value text-only-no-real-action is permitted but raises a flag (“simply disclosing deferred items and caveats is not real science”).",
  },
  {
    title: "Truth-audit before close.",
    body: "Findings must have truthAuditVerdict set before close succeeds, per the review truth-audit protocol.",
  },
  {
    title: "Provider routes are explicit and auditable.",
    body: "OpenAI-family review uses subscription-backed Codex/ChatGPT CLI sessions, never the OpenAI API. Direct Gemini and Grok API legs retain sanitized raw receipts. Anthropic is not part of the active review route. Provider failures remain failures rather than being silently replaced or relabeled.",
  },
  {
    title: "No hand-set readiness.",
    body: "readinessComputed is derived from open findings + caveats. It cannot be patched directly via mutation.",
  },
];

export default function ArchitectureDocPage() {
  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow="Docs &middot; reference"
          title="Architecture — API & MCP"
          lead={
            <>
              BigBounce paper-orchestration state lives in Convex. The <code>bigbounce-mcp</code>{" "}
              server exposes 11 tools any MCP-aware agent (Claude Code, Codex, Cursor) can call to
              read or mutate that state — no hand-editing the unsynced surfaces this project used
              to maintain. See{" "}
              <a
                href="https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/DATA_MODEL_ARCHITECTURE.md"
                target="_blank"
                rel="noreferrer"
              >
                DATA_MODEL_ARCHITECTURE.md
              </a>{" "}
              for the full rebuild plan.
            </>
          }
          actions={[{ label: "Docs home", href: "/docs" }]}
        />
      </Band>

      <Band width="content">
        <h2 className="page-header-title" style={{ fontSize: 22 }}>
          Convex schema
        </h2>
        <p style={{ maxWidth: "72ch", color: "var(--ink-2)", marginTop: 8 }}>
          7 paper-orchestration tables in <code>convex/schema.ts</code>, alongside the existing 9
          object-level tables for galaxies, MCMC, and related science state:
        </p>
        <div style={{ marginTop: 12 }}>
          <DataTable columns={tableColumns} rows={CONVEX_TABLES} rowKey={(t) => t.name} />
        </div>
        <p style={{ maxWidth: "72ch", color: "var(--ink-3)", fontSize: 13.5, marginTop: 12 }}>
          The load-bearing query is <code>papers.getPaperState(slug)</code> — it computes
          readiness as{" "}
          <code>ceiling − 2·openBlockers − 1·openMajors − 0.2·openMinors − 1·openCaveats</code>.
          The ceiling is the evidence-backed <code>readinessCap</code>. Current retained records:
          P1A {capOf("paper-1a")}, P1B {capOf("paper-1b")}, P2 {capOf("paper-2")}, P3{" "}
          {capOf("paper-3")}, P4 {capOf("paper-4")}, P5 {capOf("paper-5")} (average {avgCap}%).
          These are not equal submission targets — see <Link href="/research">/research</Link> for
          the current three-track framing. Automated-model verdicts and final-hash audits are
          evidence, not journal acceptance or a substitute for role-aware author decisions and
          venue-specific checks.
        </p>
      </Band>

      <Band tone="alt" width="content">
        <h2 className="page-header-title" style={{ fontSize: 22 }}>
          MCP tool catalog
        </h2>
        <p style={{ maxWidth: "72ch", color: "var(--ink-2)", marginTop: 8 }}>
          Wire into Claude Code via <code>bigbounce/.claude/mcp_servers.json</code> with a{" "}
          <code>CONVEX_URL</code> env var. See <code>mcp/bigbounce-mcp/README.md</code> for
          install/build steps.
        </p>
        <div style={{ marginTop: 12 }}>
          <DataTable columns={toolColumns} rows={MCP_TOOLS} rowKey={(t) => t.name} />
        </div>
      </Band>

      <Band width="content">
        <h2 className="page-header-title" style={{ fontSize: 22 }}>
          Skill package
        </h2>
        <p style={{ maxWidth: "72ch", color: "var(--ink-2)", marginTop: 8 }}>
          5 Convex-backed slash commands at <code>bigbounce/.claude/skills/</code>, auto-loaded by
          Claude Code per-project:
        </p>
        <div style={{ marginTop: 4 }}>
          {SKILLS.map((s, i) => (
            <p
              key={s.cmd}
              className="mono"
              style={{
                fontSize: 13.5,
                padding: "10px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--rule)",
              }}
            >
              {s.cmd} <span style={{ color: "var(--ink-3)", fontFamily: "var(--font-sans, inherit)" }}>&mdash; {s.desc}</span>
            </p>
          ))}
        </div>
      </Band>

      <Band tone="alt" width="content">
        <h2 className="page-header-title" style={{ fontSize: 22 }}>
          Anti-pattern guards
        </h2>
        <p style={{ maxWidth: "72ch", color: "var(--ink-2)", marginTop: 8 }}>
          Lessons learned, encoded in the MCP layer so no future round can regress:
        </p>
        <div style={{ marginTop: 4 }}>
          {GUARDS.map((g, i) => (
            <p
              key={g.title}
              style={{
                fontSize: 14,
                color: "var(--ink-2)",
                padding: "12px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--rule)",
              }}
            >
              <strong style={{ color: "var(--ink)" }}>{g.title}</strong> {g.body}
            </p>
          ))}
        </div>
      </Band>
    </>
  );
}
