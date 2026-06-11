"use client";

import { useMemo, useState, useEffect, type ReactNode } from "react";
import Link from "next/link";
import {
  BookOpen,
  ChevronRight,
  Copy,
  Database,
  ExternalLink,
  FileJson,
  GitBranch,
  KeyRound,
  Layers3,
  Network,
  Search,
  Server,
  ShieldCheck,
  Sparkles,
  Terminal,
  Workflow,
  Check,
  type LucideIcon,
} from "lucide-react";

type HttpMethod = "GET" | "POST" | "PATCH" | "DELETE" | "QUERY" | "MUTATION";

const METHOD_COLOR: Record<HttpMethod, string> = {
  GET: "#16a34a",
  POST: "#2563eb",
  PATCH: "#d97706",
  DELETE: "#dc2626",
  QUERY: "#16a34a",
  MUTATION: "#2563eb",
};

interface DocField {
  name: string;
  type: string;
  required?: boolean;
  description: string;
}

interface Endpoint {
  method: HttpMethod;
  name: string;
  description: string;
  input?: DocField[];
  returns: string;
  example?: string;
}

interface DocSection {
  id: string;
  group: string;
  title: string;
  icon: LucideIcon;
  status?: "stable" | "beta" | "internal";
  blurb: string;
  body?: ReactNode;
  endpoints?: Endpoint[];
}

interface NavGroup {
  label: string;
  icon: LucideIcon;
  sections: string[];
}

const TABLES = [
  { name: "papers", purpose: "Canonical per-paper metadata. Readiness is COMPUTED, never hand-set.", keys: "slug · title · novelty (N1–N3) · readinessComputed · sitePdfPath" },
  { name: "paper_versions", purpose: "Append-only .tex version history.", keys: "paperSlug · version · texCommit · pdfMd5 · pages · changelog" },
  { name: "papers_notables", purpose: "Notable-contribution bullets shown on /papers/[slug].", keys: "paperSlug · ordinal · bullet · citationKey?" },
  { name: "papers_externalReviews", purpose: "External / journal / colleague review pass log.", keys: "paperSlug · source enum · reviewerLabel · severity counts · recommendation" },
  { name: "r_rounds", purpose: "Cross-vendor peer-review round dispatches.", keys: "paperSlug · roundN · source (openrouter/direct/subagent/houston-external) · vendor" },
  { name: "findings", purpose: "Individual reviewer findings.", keys: "rRoundId · severity · truthAuditVerdict · closureStatus · closureCommit?" },
  { name: "pathc_caveats", purpose: "Paper-internal §pathc_caveats deferral list. Guards against caveat-as-closure.", keys: "paperSlug · label · closureMethod enum" },
  { name: "pods", purpose: "RunPod lifecycle + cost accounting.", keys: "podId · status · gpu · costAccrued · artifactsBackedUp · backupLocations" },
  { name: "tasks", purpose: "Open work queue.", keys: "priority · owner · blockedBy · paperSlug?" },
];

const MCP_TOOLS = [
  { name: "bigbounce_list_papers", summary: "Cross-paper dashboard with computed-readiness state.", input: null as Record<string, string> | null, returns: "Array<PaperState>" },
  { name: "bigbounce_get_paper", summary: "Full state for one paper by slug.", input: { slug: "p1a | p1b | p2 | p3 | p4 | p5" }, returns: "PaperState" },
  { name: "bigbounce_list_open_findings", summary: "R-round work queue (closureStatus = open | in-progress).", input: { paperSlug: "optional filter" }, returns: "Array<Finding>" },
  { name: "bigbounce_truth_audit_finding", summary: "Apply truth-audit verdict (REQUIRED before close).", input: { findingId: "Id", verdict: "VERIFIED | STALE | FALSIFIED | OPINION | LOW-RIGOR", evidence: "file:line citations" }, returns: "void" },
  { name: "bigbounce_close_finding", summary: "Atomic finding closure. Enforces closureStatus enum + truth-audit-first ordering.", input: { findingId: "Id", closureStatus: "closed-via-fix | closed-via-falsification | closed-via-out-of-scope", closureCommit: "git SHA" }, returns: "void" },
  { name: "bigbounce_bump_paper_version", summary: "Atomic .tex version bump → site re-renders within seconds.", input: { paperSlug: "slug", version: "vX.Y.Z", changelog: "what changed" }, returns: "Id<paper_versions>" },
  { name: "bigbounce_list_pathc_caveats", summary: "Per-paper §pathc_caveats deferral list.", input: { paperSlug: "slug" }, returns: "Array<PathcCaveat>" },
  { name: "bigbounce_close_pathc_caveat", summary: "Close caveat with explicit closureMethod enum (⚠️ flags caveat-as-closure).", input: { paperSlug: "slug", label: "caveat label", closureMethod: "real-computation | artifact-verification | truth-audit-falsification | text-only-no-real-action" }, returns: "void" },
  { name: "bigbounce_list_pods", summary: "RunPod state synced from Convex.", input: { statusFilter: "optional" }, returns: "Array<Pod>" },
  { name: "bigbounce_get_external_review_prompt", summary: "Dynamic copy/paste external-review prompt — replaces hardcoded focusAreas.", input: { slug: "paper slug" }, returns: "{ paperSlug, paperVersion, pdfPath, prompt }" },
  { name: "bigbounce_list_tasks", summary: "Cross-paper + per-paper open task queue.", input: { status: "optional", owner: "optional", paperSlug: "optional" }, returns: "Array<Task>" },
  { name: "bigbounce_add_notable", summary: "Insert/update a notable-contribution bullet.", input: { paperSlug: "slug", ordinal: "number", bullet: "text" }, returns: "void" },
  { name: "bigbounce_add_external_review", summary: "Log an external review pass (journal / arxiv / colleague-private / internal-stage3).", input: { paperSlug: "slug", source: "enum", reviewerLabel: "label", severity: "counts" }, returns: "Id" },
];

const SKILLS = [
  // astrostack — the full bigbounce-specific namespace (18 skills)
  { cmd: "/bigbounce-status", desc: "Print live paper-state dashboard (calls list_papers).", origin: "astrostack" },
  { cmd: "/bigbounce-r-round", desc: "Fire direct-vendor R-round (4 vendors parallel), write findings to Convex.", origin: "astrostack" },
  { cmd: "/bigbounce-truth-audit", desc: "Apply verdict per peer-review-truth-audit protocol. REQUIRED before close.", origin: "astrostack" },
  { cmd: "/bigbounce-close", desc: "Atomic finding/caveat closure with closureStatus enum.", origin: "astrostack" },
  { cmd: "/bigbounce-bump", desc: "Atomic .tex version bump; site re-renders.", origin: "astrostack" },
  { cmd: "/bigbounce-version-bump", desc: "Paper version bump driver (pairs with /bigbounce-paper-pdf-mirror).", origin: "astrostack" },
  { cmd: "/bigbounce-post-bump-sync", desc: "Mandatory full-surface sync after every bump (papers.ts, live-status.ts, SSOT, Convex, mirror PDFs, commit, push, curl-verify).", origin: "astrostack" },
  { cmd: "/bigbounce-site-sync", desc: "Same-commit dual sync of public site surfaces with SSOT.", origin: "astrostack" },
  { cmd: "/bigbounce-paper-pdf-mirror", desc: "Mirror versioned PDFs into site/public/papers/ with metadata refresh.", origin: "astrostack" },
  { cmd: "/bigbounce-claims-table-sync", desc: "Replace a quantitative claim at every site simultaneously (claims table).", origin: "astrostack" },
  { cmd: "/bigbounce-revision-tracker", desc: "Maintain REVISION_TRACKER.md across review rounds.", origin: "astrostack" },
  { cmd: "/drive-to-100-fire", desc: "One atomic step of the drive-to-100 cron loop.", origin: "astrostack" },
  { cmd: "/external-review-browser-loop", desc: "Automated browser-tier external review submission to logged-in frontier web apps.", origin: "astrostack" },
  { cmd: "/houston-method-v2", desc: "Mandatory experiment completion protocol (QC → analyze → expand → backup).", origin: "astrostack" },
  { cmd: "/gpu-dataloader-pattern", desc: "DataLoader num_workers=16 pin_memory=True GPU inference pattern.", origin: "astrostack" },
  { cmd: "/runpod-lifecycle", desc: "RunPod provision / monitor / teardown lifecycle.", origin: "astrostack" },
  { cmd: "/idle-gpu-rescue", desc: "Auto-assign work when a pod sits idle.", origin: "astrostack" },
  { cmd: "/pod-backup-before-stop", desc: "3+ location backup gate before any pod stop.", origin: "astrostack" },
  // hubstack — cross-paper learning-loop + publishing namespaces
  { cmd: "/cross-vendor-r-round", desc: "Cascaded multi-vendor reviews with GPT-5→GPT-4o fallback detection and LOW-RIGOR tagging.", origin: "hubstack/learning-loop" },
  { cmd: "/peer-review-truth-audit", desc: "Per-finding VERIFIED/STALE/FALSIFIED/OPINION/LOW-RIGOR verdict before closures.", origin: "hubstack/learning-loop" },
  { cmd: "/cascaded-r-rounds", desc: "Drive R-rounds until 3 consecutive convergent-silence rounds.", origin: "hubstack/learning-loop" },
  { cmd: "/paper-pre-review-check", desc: "8-gate pre-review including /never-fabricate-derivation + /never-claim-n4 hard gates.", origin: "hubstack/learning-loop" },
  { cmd: "/never-fabricate-derivation", desc: "Pattern-036 prevention: scan closure diffs for math claims lacking citation/derivation.", origin: "hubstack/learning-loop" },
  { cmd: "/r-round-finding-archive", desc: "Archive every round's findings into the findings-archive JSON store.", origin: "hubstack/learning-loop" },
  { cmd: "/r-round-pattern-mine", desc: "Mine closed rounds for new review patterns (catalog growth).", origin: "hubstack/learning-loop" },
  { cmd: "/never-claim-n4", desc: "Mechanical novelty-tier audit. Demotes any N4 self-claim to N3.", origin: "hubstack/infra" },
  { cmd: "/paper-compile-revtex", desc: "4-pass revtex4-2 compile + log audit.", origin: "hubstack/publishing" },
  { cmd: "/latex-audit", desc: "7-step overflow / URL / artifact / date audit on every compile.", origin: "hubstack/publishing" },
  { cmd: "/artifact-link-verify", desc: "Verify every cited artifact path / URL resolves before a round closes.", origin: "hubstack/publishing" },
  { cmd: "/pdf-restamp-bundle", desc: "Bundled version+date restamp, recompile, mirror, SSOT update in one commit.", origin: "hubstack/publishing" },
  { cmd: "/ssot-update", desc: "Update project-context/SSOT/ canonical paper status.", origin: "hubstack/publishing" },
];

const SECTIONS: DocSection[] = [
  {
    id: "overview",
    group: "Getting Started",
    title: "Overview",
    icon: BookOpen,
    status: "stable",
    blurb:
      "How the BigBounce orchestration layer is wired together — Convex as canonical truth, bigbounce-mcp as the local agent surface, the Next.js site as the read-only public view.",
    body: (
      <>
        <p>
          BigBounce is an end-to-end research orchestration stack for six
          peer-reviewed cosmology papers (P1A, P1B, P2, P3, P4, P5). It
          consists of three layers:
        </p>
        <ol>
          <li>
            <strong>Convex DB</strong> — canonical source of truth for paper
            versions, findings, R-rounds, novelty, notables, external reviews,
            pods, tasks, caveats.
          </li>
          <li>
            <strong>bigbounce-mcp</strong> — a local MCP server (stdio
            transport) that exposes typed tools for the agents (Claude Code,
            Codex, Cursor) to read and mutate Convex state with guardrails
            (truth-audit-before-close, novelty cap at N3, no caveat-as-closure).
          </li>
          <li>
            <strong>bigbounce.hubify.app</strong> — read-only static export
            that subscribes to Convex via React useQuery. No write paths, no
            API keys in the bundle.
          </li>
        </ol>
        <p>
          Everything you see at <code>bigbounce.hubify.app/papers/&lt;slug&gt;</code>{" "}
          reflects the live state of the Convex tables documented below.
          When a paper version bumps, the site re-renders within seconds.
        </p>
      </>
    ),
  },
  {
    id: "data-flow",
    group: "Getting Started",
    title: "Data flow",
    icon: Workflow,
    status: "stable",
    blurb:
      "The atomic loop: edit .tex → recompile → atomic Convex bump → site re-renders. No manual website updates anywhere.",
    body: (
      <pre className="docs-codeblock" data-lang="text">{`  .tex source  ──►  pdflatex (revtex4-2, 4 passes)  ──►  paper.pdf
       │                                                      │
       │                                                      ▼
       │                                          site/public/papers/<slug>_v<ver>.pdf
       │                                                      │
       ▼                                                      ▼
  bigbounce-mcp tool  ────►  Convex mutation  ────►  papers + paper_versions
  (e.g. paperVersions:bump)         │                         │
                                    ▼                         ▼
                            findings, notables,        React useQuery
                            externalReviews            (real-time subs)
                                    │                         │
                                    └─────────►   bigbounce.hubify.app
                                                  ├── /              (dashboard)
                                                  ├── /papers/<slug> (detail + dynamic review prompt)
                                                  ├── /contributions (N1–N4 novelty)
                                                  ├── /figures       (auto-updated per .tex)
                                                  ├── /activity      (event feed)
                                                  └── /docs          (you are here)`}</pre>
    ),
  },
  {
    id: "convex-schema",
    group: "Backend",
    title: "Convex schema",
    icon: Database,
    status: "stable",
    blurb:
      "Canonical tables. Readiness is computed, not hand-set. Novelty caps at N3 (the schema validator rejects N4).",
    body: (
      <>
        <p>
          The deployment URL is{" "}
          <code>https://brilliant-panther-471.convex.cloud</code> (public
          read-only). Mutations require the deployment access token, which
          lives in <code>~/.convex/config.json</code> on Houston&apos;s
          machine.
        </p>
        <div className="table-scroll">
        <table className="docs-table">
          <thead>
            <tr>
              <th>Table</th>
              <th>Purpose</th>
              <th>Key fields</th>
            </tr>
          </thead>
          <tbody>
            {TABLES.map((t) => (
              <tr key={t.name}>
                <td>
                  <code>{t.name}</code>
                </td>
                <td>{t.purpose}</td>
                <td>
                  <code>{t.keys}</code>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      </>
    ),
  },
  {
    id: "convex-queries",
    group: "Backend",
    title: "Convex read API",
    icon: Search,
    status: "stable",
    blurb:
      "Public read-only queries the site uses. No auth — these are safe for the static bundle.",
    endpoints: [
      {
        method: "QUERY",
        name: "papers:listPapersWithVersions",
        description:
          "Cross-paper dashboard: all 6 papers joined with their latest paper_versions row.",
        returns: "Array<PaperWithVersion>",
        example: `useQuery(api.papers.listPapersWithVersions)
// → [{ slug: "p3", title: "Multi-Survey Anomaly Catalog",
//      latestVersion: "3.1.73", readinessComputed: 95, ... }, ...]`,
      },
      {
        method: "QUERY",
        name: "papers:getPaperState",
        description:
          "Full state for one paper: latest version, novelty, all open findings, caveats, R-rounds, notables, external reviews.",
        input: [
          { name: "slug", type: "string", required: true, description: "p1a | p1b | p2 | p3 | p4 | p5" },
        ],
        returns: "PaperState",
      },
      {
        method: "QUERY",
        name: "notables:list",
        description:
          "Notable contributions for one paper (rendered on /papers/[slug] under 'Notable contributions').",
        input: [
          { name: "paperSlug", type: "string", required: true, description: "paper slug" },
        ],
        returns: "Array<{ ordinal, bullet, citationKey? }>",
      },
      {
        method: "QUERY",
        name: "externalReviews:list",
        description:
          "External review entries (journal / arxiv / colleague-private / internal-stage3) for one paper.",
        input: [
          { name: "paperSlug", type: "string", required: true, description: "paper slug" },
        ],
        returns: "Array<ExternalReview>",
      },
      {
        method: "QUERY",
        name: "findings:listOpen",
        description: "Open R-round findings (closureStatus = open | in-progress) across all papers.",
        input: [{ name: "paperSlug?", type: "string", description: "optional filter" }],
        returns: "Array<Finding>",
      },
    ],
  },
  {
    id: "convex-mutations",
    group: "Backend",
    title: "Convex mutations (local only)",
    icon: Server,
    status: "internal",
    blurb:
      "Mutation surface — locked behind the deployment access token. The static bundle does not expose these.",
    endpoints: [
      {
        method: "MUTATION",
        name: "paperVersions:bump",
        description:
          "Atomic .tex version bump. Patches papers.sitePdfPath in the same transaction so the new versioned PDF is canonical immediately.",
        input: [
          { name: "paperSlug", type: "string", required: true, description: "paper slug" },
          { name: "version", type: "string", required: true, description: "vX.Y.Z" },
          { name: "datestamp", type: "string", required: true, description: "YYYY-MM-DD" },
          { name: "texCommit", type: "string", required: true, description: "git SHA of the .tex source" },
          { name: "pdfMd5", type: "string", required: true, description: "md5 of the compiled PDF" },
          { name: "pdfPages", type: "number", required: true, description: "page count" },
          { name: "pdfSizeBytes", type: "number", required: true, description: "PDF size" },
          { name: "changelog", type: "string", required: true, description: "what changed in this bump" },
          { name: "sitePdfPath?", type: "string", description: "/papers/<slug>_v<ver>.pdf (atomic patch on bump)" },
        ],
        returns: "Id<paper_versions>",
      },
      {
        method: "MUTATION",
        name: "notables:upsertByOrdinal",
        description:
          "Insert or update a notable-contribution bullet for a paper (ordinal-stable so updates don't churn the list).",
        input: [
          { name: "paperSlug", type: "string", required: true, description: "paper slug" },
          { name: "ordinal", type: "number", required: true, description: "1-indexed display order" },
          { name: "bullet", type: "string", required: true, description: "the notable bullet text" },
          { name: "citationKey?", type: "string", description: "BibTeX key if any" },
        ],
        returns: "void",
      },
      {
        method: "MUTATION",
        name: "externalReviews:add",
        description: "Log an external review pass (journal, arxiv, colleague-private, internal-stage3, etc).",
        input: [
          { name: "paperSlug", type: "string", required: true, description: "paper slug" },
          { name: "source", type: "enum", required: true, description: "journal | arxiv | houston-paste | colleague-private | internal-stage3" },
          { name: "reviewerLabel", type: "string", required: true, description: "who/what (e.g. 'Reviewer 2')" },
          { name: "receivedAt", type: "number", required: true, description: "ms timestamp" },
          { name: "blocker", type: "number", required: true, description: "count" },
          { name: "major", type: "number", required: true, description: "count" },
          { name: "minorCount", type: "number", required: true, description: "count" },
          { name: "recommendation", type: "enum", required: true, description: "accept | minor-revision | major-revision | reject | withdraw" },
        ],
        returns: "Id<papers_externalReviews>",
      },
      {
        method: "MUTATION",
        name: "findings:applyTruthAudit",
        description:
          "REQUIRED before close. Records the truth-audit verdict (VERIFIED / STALE / FALSIFIED / OPINION / LOW-RIGOR) with evidence citations.",
        input: [
          { name: "findingId", type: "Id<findings>", required: true, description: "finding to audit" },
          { name: "verdict", type: "enum", required: true, description: "VERIFIED | STALE | FALSIFIED | OPINION | LOW-RIGOR" },
          { name: "evidence", type: "string", required: true, description: "file:line citations or commit refs" },
        ],
        returns: "void",
      },
    ],
  },
  {
    id: "mcp-tools",
    group: "MCP",
    title: "bigbounce-mcp tools",
    icon: Network,
    status: "stable",
    blurb:
      "Local MCP server (stdio transport). Wired into Claude Code via bigbounce/.claude/mcp_servers.json with CONVEX_URL + CONVEX_DEPLOYMENT_TOKEN env vars.",
    endpoints: MCP_TOOLS.map((t) => ({
      method: "POST" as HttpMethod,
      name: t.name,
      description: t.summary,
      returns: t.returns,
      input: t.input
        ? Object.entries(t.input).map(([name, description]) => ({
            name,
            type: "string",
            description,
          }))
        : undefined,
    })),
  },
  {
    id: "skills",
    group: "Agent surface",
    title: "Skill commands",
    icon: Terminal,
    status: "stable",
    blurb:
      "Slash commands the agents (Claude Code, Codex, Cursor) load. ONE stack (scistack) with two namespaces: astrostack/ (bigbounce-specific) and hubstack/ (cross-paper science IP).",
    body: (
      <>
        <p>
          Skills are markdown files with YAML frontmatter. Agents auto-load
          them on session start. There is ONE canonical science skill stack —{" "}
          <code>~/.claude/scistack/</code> — with two namespaces inside it:{" "}
          <code>astrostack/</code> (bigbounce-specific) and{" "}
          <code>hubstack/</code> (cross-paper learning-loop, publishing,
          research, infra). Entries under <code>~/.claude/skills/</code> are
          symlinks back into scistack. No project-scoped duplicates;
          &ldquo;AstroStack&rdquo; and &ldquo;HubStack&rdquo; are namespaces,
          not separate stacks.
        </p>
        <div className="table-scroll">
        <table className="docs-table">
          <thead>
            <tr>
              <th>Skill</th>
              <th>Purpose</th>
              <th>Origin</th>
            </tr>
          </thead>
          <tbody>
            {SKILLS.map((s) => (
              <tr key={s.cmd}>
                <td>
                  <code>{s.cmd}</code>
                </td>
                <td>{s.desc}</td>
                <td>
                  <span className="docs-badge-soft">{s.origin}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      </>
    ),
  },
  {
    id: "novelty-policy",
    group: "Policy",
    title: "Novelty tier policy (N1–N4)",
    icon: Sparkles,
    status: "stable",
    blurb:
      "The self-claim ceiling is N3. N4 is reserved for the field to award. Encoded at three layers: schema validator, MCP guard, /never-claim-n4 audit skill.",
    body: (
      <>
        <p>
          Every paper carries a <code>papers.novelty</code> field. The Convex
          schema validator rejects N4 at the type level:
        </p>
        <pre className="docs-codeblock" data-lang="ts">{`novelty: v.optional(v.union(
  v.literal("N1"),
  v.literal("N2"),
  v.literal("N3"),
  // N4 intentionally excluded — Houston standing directive 2026-06-03
))`}</pre>
        <p>The canonical tier definitions:</p>
        <div className="table-scroll">
        <table className="docs-table">
          <thead>
            <tr>
              <th>Tier</th>
              <th>Bar</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <span className="docs-tier" style={{ background: "#9333ea" }}>
                  N1
                </span>
              </td>
              <td>Incremental refinement / replication.</td>
            </tr>
            <tr>
              <td>
                <span className="docs-tier" style={{ background: "#2563eb" }}>
                  N2
                </span>
              </td>
              <td>Novel application or combination of existing methods.</td>
            </tr>
            <tr>
              <td>
                <span className="docs-tier" style={{ background: "#16a34a" }}>
                  N3
                </span>
              </td>
              <td>
                First-of-kind demonstration / new constraint / new direction.{" "}
                <strong>Ceiling for our self-claims.</strong>
              </td>
            </tr>
            <tr>
              <td>
                <span className="docs-tier" style={{ background: "#b91c1c" }}>
                  N4
                </span>
              </td>
              <td>
                Paradigm-shifting / Nobel-worthy.{" "}
                <strong>Never self-claimed.</strong> Awarded by the field over time.
              </td>
            </tr>
          </tbody>
        </table>
        </div>
      </>
    ),
  },
  {
    id: "review-protocol",
    group: "Policy",
    title: "Review-learning-loop protocol",
    icon: GitBranch,
    status: "stable",
    blurb:
      "Every R-round flows analyze → truth-audit → findings-archive → pattern-extract → update-review-skills. 12.5× amplification ratio measured between CCAI and cross-vendor passes.",
    body: (
      <>
        <p>
          Each paper passes through three stages on the current version before
          it can be released:
        </p>
        <ol>
          <li>
            <strong>Stage 1 — CCAI same-vendor sweep.</strong> Mechanical
            same-vendor pass. Necessary but never sufficient.
          </li>
          <li>
            <strong>Stage 2 — Cross-vendor R-round.</strong> Direct vendor
            calls to Grok-4, GPT-5, Gemini-2.5-Pro, Perplexity-Sonar-Pro.
            Anthropic excluded per the no-echo-chamber rule.{" "}
            <code>tools/cross_vendor_review_direct.py</code>.
          </li>
          <li>
            <strong>Stage 3 — External journal-style review.</strong> Houston
            pastes the dynamically generated prompt into ChatGPT / Gemini /
            Claude. Results logged via <code>externalReviews:add</code>.
          </li>
        </ol>
        <p>
          Every finding gets a truth-audit verdict before close. Falsified or
          stale findings are not treated as &quot;closed via fix&quot; — they
          are closed-via-falsification with evidence.
        </p>
        <p>
          The exit criterion for cascaded R-rounds: three consecutive
          convergent-silence rounds (zero new BLOCKERs / MAJORs).
        </p>
      </>
    ),
  },
  {
    id: "security",
    group: "Security",
    title: "Security posture",
    icon: ShieldCheck,
    status: "stable",
    blurb:
      "Static site, stdio-only MCP, no public mutation endpoints, no API keys in bundle, no auth flow. Only operators with local credentials can mutate.",
    body: (
      <ul>
        <li>
          <strong>No public mutation endpoints.</strong> The Convex deployment
          URL is referenced from the site for <em>read</em> queries only
          (papers, findings, caveats, activity rollup). Mutations require the
          deployment access token in <code>~/.convex/config.json</code>.
        </li>
        <li>
          <strong>API keys never exposed in build output.</strong> Vendor keys
          (Anthropic, OpenAI, Gemini, Grok, Perplexity) live in local{" "}
          <code>.env.local</code> files only — they never reach the static
          export. RunPod, HuggingFace, Vercel OIDC keys: same.
        </li>
        <li>
          <strong>MCP server is stdio-only.</strong> <code>bigbounce-mcp</code>{" "}
          runs as a subprocess of Claude Code or another local agent. There
          is no HTTP listener.
        </li>
        <li>
          <strong>Site is static.</strong> <code>next.config.ts</code> sets{" "}
          <code>output: &quot;export&quot;</code>. No server-side routes, no
          API handlers, no auth flow, no session.
        </li>
        <li>
          <strong>External-review prompts are read-only.</strong> The{" "}
          <code>/papers/&lt;slug&gt;</code> page generates a copy-pasteable
          text prompt. Houston manually pastes into ChatGPT / Gemini /
          Claude. No agent invocation happens through the site.
        </li>
        <li>
          <strong>Schema validator hard gates.</strong> N4 novelty is rejected
          at the Convex validator. closureMethod enum includes{" "}
          <code>text-only-no-real-action</code> as an explicit ⚠️ flag.
        </li>
      </ul>
    ),
  },
  {
    id: "agent-files",
    group: "Reference",
    title: "Agent files",
    icon: FileJson,
    status: "stable",
    blurb: "Machine-readable references for agents that consume this site.",
    body: (
      <ul>
        <li>
          <a href="https://github.com/Hubify-Projects/bigbounce" target="_blank" rel="noopener noreferrer">
            github.com/Hubify-Projects/bigbounce <ExternalLink className="inline-icon" />
          </a>{" "}
          — full source.
        </li>
        <li>
          <code>project-context/SSOT/index.md</code> — cross-paper dashboard SSOT.
        </li>
        <li>
          <code>project-context/SSOT/paper-N/status.md</code> — per-paper close-the-gap.
        </li>
        <li>
          <code>project-context/peer-reviews/findings-archive/</code> — every R-round&apos;s raw findings.
        </li>
        <li>
          <code>project-context/review-patterns/</code> — extracted pattern catalog (36 patterns and counting).
        </li>
        <li>
          <code>~/.claude/scistack/</code> — master skill stack (hubstack + astrostack + extensions).
        </li>
      </ul>
    ),
  },
];

const NAV_GROUPS: NavGroup[] = [
  { label: "Getting Started", icon: BookOpen, sections: ["overview", "data-flow"] },
  { label: "Backend", icon: Database, sections: ["convex-schema", "convex-queries", "convex-mutations"] },
  { label: "MCP", icon: Network, sections: ["mcp-tools"] },
  { label: "Agent surface", icon: Terminal, sections: ["skills"] },
  { label: "Policy", icon: ShieldCheck, sections: ["novelty-policy", "review-protocol"] },
  { label: "Security", icon: KeyRound, sections: ["security"] },
  { label: "Reference", icon: Layers3, sections: ["agent-files"] },
];

function MethodBadge({ method }: { method: HttpMethod }) {
  return (
    <span className="docs-method" style={{ background: METHOD_COLOR[method] }}>
      {method}
    </span>
  );
}

function CopyButton({ text }: { text: string }) {
  const [copied, setCopied] = useState(false);
  return (
    <button
      type="button"
      className="docs-copy"
      onClick={async () => {
        try {
          await navigator.clipboard.writeText(text);
          setCopied(true);
          setTimeout(() => setCopied(false), 1200);
        } catch {
          /* clipboard blocked */
        }
      }}
      aria-label="Copy"
    >
      {copied ? <Check className="docs-copy-icon" /> : <Copy className="docs-copy-icon" />}
    </button>
  );
}

function StatusPill({ status }: { status?: DocSection["status"] }) {
  if (!status) return null;
  return <span className={`docs-status docs-status-${status}`}>{status}</span>;
}

export default function DocsClient() {
  const [query, setQuery] = useState("");
  const [activeId, setActiveId] = useState<string>("overview");

  const filtered = useMemo(() => {
    if (!query.trim()) return SECTIONS;
    const q = query.toLowerCase();
    return SECTIONS.filter(
      (s) =>
        s.title.toLowerCase().includes(q) ||
        s.blurb.toLowerCase().includes(q) ||
        s.group.toLowerCase().includes(q) ||
        s.endpoints?.some(
          (e) =>
            e.name.toLowerCase().includes(q) ||
            e.description.toLowerCase().includes(q),
        ),
    );
  }, [query]);

  const visibleIds = useMemo(() => new Set(filtered.map((s) => s.id)), [filtered]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        }
      },
      { rootMargin: "-40% 0px -55% 0px" },
    );
    SECTIONS.forEach((s) => {
      const el = document.getElementById(s.id);
      if (el) observer.observe(el);
    });
    return () => observer.disconnect();
  }, []);

  return (
    <div className="docs-shell">
      <aside className="docs-sidebar">
        <div className="docs-sidebar-header">
          <div className="docs-sidebar-title">BigBounce Stack</div>
          <div className="docs-sidebar-subtitle">API · MCP · Skills · Policy</div>
        </div>
        <div className="docs-sidebar-search">
          <Search className="docs-sidebar-search-icon" />
          <input
            type="search"
            placeholder="Search docs..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-label="Search docs"
          />
        </div>
        <nav className="docs-sidebar-nav" aria-label="Documentation pages">
          {NAV_GROUPS.map((group) => {
            const GroupIcon = group.icon;
            const visible = group.sections.filter((id) => visibleIds.has(id));
            if (visible.length === 0) return null;
            return (
              <div key={group.label} className="docs-nav-group">
                <div className="docs-nav-group-label">
                  <GroupIcon className="docs-nav-group-icon" />
                  <span>{group.label}</span>
                </div>
                <ul>
                  {visible.map((id) => {
                    const section = SECTIONS.find((s) => s.id === id);
                    if (!section) return null;
                    const Icon = section.icon;
                    const isActive = activeId === id;
                    return (
                      <li key={id}>
                        <a
                          href={`#${id}`}
                          className={isActive ? "docs-nav-link is-active" : "docs-nav-link"}
                          onClick={() => setActiveId(id)}
                        >
                          <Icon className="docs-nav-link-icon" />
                          <span>{section.title}</span>
                          {section.endpoints && (
                            <span className="docs-nav-link-count">{section.endpoints.length}</span>
                          )}
                        </a>
                      </li>
                    );
                  })}
                </ul>
              </div>
            );
          })}
        </nav>
        <div className="docs-sidebar-footer">
          <Link href="/" className="docs-sidebar-back">
            ← back to bigbounce
          </Link>
          <a
            href="https://github.com/Hubify-Projects/bigbounce"
            target="_blank"
            rel="noopener noreferrer"
            className="docs-sidebar-link"
          >
            github <ExternalLink className="inline-icon" />
          </a>
        </div>
      </aside>

      <main className="docs-main">
        <div className="docs-banner">
          <ShieldCheck className="docs-banner-icon" />
          <div>
            <strong>Internal documentation.</strong> This page is read-only.
            No API keys, mutation forms, or external interactions are exposed.
            Only operators with local credentials (Houston + paired agents)
            can dispatch mutations.
          </div>
        </div>

        {filtered.length === 0 && (
          <div className="docs-empty">No sections match &quot;{query}&quot;.</div>
        )}

        {filtered.map((section) => {
          const Icon = section.icon;
          return (
            <article key={section.id} id={section.id} className="docs-article">
              <header className="docs-article-header">
                <div className="docs-article-breadcrumb">
                  <Icon className="docs-article-breadcrumb-icon" />
                  <span>{section.group}</span>
                  <ChevronRight className="docs-article-breadcrumb-sep" />
                  <span className="docs-article-breadcrumb-current">{section.title}</span>
                </div>
                <div className="docs-article-titlerow">
                  <h2 className="docs-article-title">{section.title}</h2>
                  <StatusPill status={section.status} />
                </div>
                <p className="docs-article-blurb">{section.blurb}</p>
              </header>

              {section.body && <div className="docs-article-body">{section.body}</div>}

              {section.endpoints && (
                <div className="docs-endpoints">
                  {section.endpoints.map((e) => (
                    <div key={e.name} className="docs-endpoint">
                      <div className="docs-endpoint-header">
                        <MethodBadge method={e.method} />
                        <code className="docs-endpoint-name">{e.name}</code>
                        <CopyButton text={e.name} />
                      </div>
                      <p className="docs-endpoint-desc">{e.description}</p>
                      {e.input && e.input.length > 0 && (
                        <div className="docs-endpoint-params">
                          <div className="docs-endpoint-params-label">Input</div>
                          <div className="table-scroll">
                          <table className="docs-table docs-table-compact">
                            <thead>
                              <tr>
                                <th>Field</th>
                                <th>Type</th>
                                <th>Description</th>
                              </tr>
                            </thead>
                            <tbody>
                              {e.input.map((f) => (
                                <tr key={f.name}>
                                  <td>
                                    <code>{f.name}</code>
                                    {f.required && <span className="docs-required">*</span>}
                                  </td>
                                  <td>
                                    <code className="docs-type">{f.type}</code>
                                  </td>
                                  <td>{f.description}</td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                          </div>
                        </div>
                      )}
                      <div className="docs-endpoint-returns">
                        <span className="docs-endpoint-returns-label">Returns</span>
                        <code className="docs-type">{e.returns}</code>
                      </div>
                      {e.example && (
                        <div className="docs-endpoint-example">
                          <div className="docs-endpoint-example-header">
                            <span>Example</span>
                            <CopyButton text={e.example} />
                          </div>
                          <pre className="docs-codeblock" data-lang="ts">
                            {e.example}
                          </pre>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </article>
          );
        })}
      </main>
    </div>
  );
}
