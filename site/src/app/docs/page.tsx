import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Docs — API, MCP, Skills",
  description:
    "Internal docs for the BigBounce research-orchestration data layer: Convex schema, bigbounce-mcp tools, skill-stack commands. Read-only — no API keys or external interactions exposed.",
};

const MCP_TOOLS = [
  { name: "bigbounce_list_papers", summary: "Cross-paper dashboard with computed-readiness state.", input: "(none)", returns: "Array<PaperState>" },
  { name: "bigbounce_get_paper", summary: "Full state for one paper by slug.", input: "{ slug }", returns: "PaperState" },
  { name: "bigbounce_list_open_findings", summary: "R-round work queue. Open findings (closureStatus = open | in-progress).", input: "{ paperSlug? }", returns: "Array<Finding>" },
  { name: "bigbounce_truth_audit_finding", summary: "Apply truth-audit verdict (REQUIRED before close).", input: "{ findingId, verdict, evidence }", returns: "void" },
  { name: "bigbounce_close_finding", summary: "Atomic finding closure. Enforces closureStatus enum + truth-audit-first ordering.", input: "{ findingId, closureStatus, closureCommit?, closureArtifact?, closureNote? }", returns: "void" },
  { name: "bigbounce_bump_paper_version", summary: "Atomic .tex version bump → site re-renders within seconds.", input: "{ paperSlug, version, datestamp, texCommit, pdfMd5, pdfPages, pdfSizeBytes, changelog, arxivTarballPath?, arxivTarballSizeBytes? }", returns: "Id<paper_versions>" },
  { name: "bigbounce_list_pathc_caveats", summary: "Per-paper §pathc_caveats deferral list.", input: "{ paperSlug }", returns: "Array<PathcCaveat>" },
  { name: "bigbounce_close_pathc_caveat", summary: "Close caveat with explicit closureMethod enum (⚠️ flags caveat-as-closure).", input: "{ paperSlug, label, closureMethod, closureArtifact?, closureCommit?, closureNote? }", returns: "void" },
  { name: "bigbounce_list_pods", summary: "RunPod state synced from Convex.", input: "{ statusFilter? }", returns: "Array<Pod>" },
  { name: "bigbounce_get_external_review_prompt", summary: "Dynamic copy/paste external-review prompt — replaces hardcoded focusAreas.", input: "{ slug }", returns: "{ paperSlug, paperVersion, pdfPath, prompt }" },
  { name: "bigbounce_list_tasks", summary: "Cross-paper + per-paper open task queue.", input: "{ status?, owner?, paperSlug? }", returns: "Array<Task>" },
];

const SKILLS = [
  { cmd: "/bigbounce-status", desc: "Print live paper-state dashboard (calls list_papers)." },
  { cmd: "/bigbounce-r-round <paper-slug>", desc: "Fire direct-vendor R-round (4 vendors parallel), write findings to Convex." },
  { cmd: "/bigbounce-truth-audit <findingId> <verdict> <evidence>", desc: "Apply verdict per feedback_peer_review_truth_audit_protocol. REQUIRED before close." },
  { cmd: "/bigbounce-close <findingId|caveat-ref> <method>", desc: "Atomic finding/caveat closure with closureStatus enum." },
  { cmd: "/bigbounce-bump <paper-slug> <version> [--changelog]", desc: "Atomic .tex version bump; site re-renders." },
];

const TABLES = [
  { name: "papers", purpose: "Canonical per-paper metadata (readiness is COMPUTED, never hand-set)." },
  { name: "paper_versions", purpose: "Append-only .tex version history; pdfMd5/pages/size/changelog per row." },
  { name: "r_rounds", purpose: "Cross-vendor peer-review round dispatches (source ∈ openrouter/direct/subagent/houston-external)." },
  { name: "findings", purpose: "Individual reviewer findings with truthAuditVerdict + closureStatus first-class." },
  { name: "pathc_caveats", purpose: "Paper-internal §pathc_caveats deferral list. closureMethod enum guards against caveat-as-closure." },
  { name: "pods", purpose: "RunPod lifecycle + cost accounting (artifactsBackedUp, backupLocations)." },
  { name: "tasks", purpose: "Open work queue. Priority + owner + blockedBy." },
];

const GUARDS = [
  { rule: "No caveat-as-closure", body: "closureMethod enum includes 'text-only-no-real-action' as explicit ⚠️ FLAG. Prefer real-computation / artifact-verification / truth-audit-falsification." },
  { rule: "Truth-audit before close", body: "Findings must have truthAuditVerdict set before close mutations succeed (per feedback_peer_review_truth_audit_protocol)." },
  { rule: "No OpenRouter excuse", body: "Direct vendor keys live in youmd/.env.local. tools/cross_vendor_review_direct.py calls them directly. OpenRouter cap is no longer a blocker (per feedback_no_openrouter_excuse)." },
  { rule: "No hand-set readiness", body: "readinessComputed = 95 − 2·blockers − 1·majors − 0.2·minors − 1·caveats, capped at 95 pre-Houston-sign-off. Cannot be patched directly." },
];

export default function DocsPage() {
  return (
    <div style={{ maxWidth: 960, margin: "0 auto", padding: "24px 0" }}>
      <header style={{ marginBottom: 32 }}>
        <p
          style={{
            fontSize: "0.72rem",
            color: "#d97706",
            fontFamily: "var(--font-mono-stack)",
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 8,
          }}
        >
          ⚠️ Internal documentation
        </p>
        <h1 style={{ margin: "0 0 12px 0" }}>BigBounce Stack — API · MCP · Skills</h1>
        <p style={{ color: "var(--text-muted)", maxWidth: 800, lineHeight: 1.55 }}>
          How the orchestration layer for the BigBounce research program works.
          This page is <strong>read-only</strong>; no API keys, no mutation
          forms, no external interactions are exposed. Only operators with
          local credentials (Houston + paired agents) can generate keys or
          dispatch mutations.
        </p>
        <p
          style={{
            marginTop: 16,
            padding: "10px 14px",
            border: "1px solid #d97706",
            borderRadius: 8,
            background: "rgba(217, 119, 6, 0.05)",
            fontSize: "0.85rem",
            lineHeight: 1.5,
            color: "var(--text)",
          }}
        >
          <strong>No public API keys or interactive controls.</strong> The MCP
          server runs locally over stdio (not exposed to the public
          internet); Convex mutations require the deployment access token
          which lives in <code>~/.convex/config.json</code> on Houston&apos;s
          machine. The bigbounce.hubify.app site reads via the public
          read-only deployment URL but exposes no write endpoint.
        </p>
      </header>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Data flow</h2>
        <pre
          style={{
            background: "var(--bg)",
            border: "1px solid var(--border)",
            borderRadius: 8,
            padding: 14,
            fontSize: "0.78rem",
            overflowX: "auto",
            lineHeight: 1.5,
            fontFamily: "var(--font-mono-stack)",
          }}
        >{`  .tex source  ──► pdflatex ──► local PDF ──► site/public/papers/
       │
       ▼
  bigbounce-mcp tool (local stdio)
       │
       ▼
  Convex mutation (e.g. paperVersions.bump / findings.close)
       │
       ▼
  Convex DB (canonical source of truth)
       │  ◄─ React useQuery (real-time subscriptions)
       ▼
  bigbounce.hubify.app
    ├── /         (homepage dashboard, paper progress)
    ├── /papers/<slug>  (per-paper detail + dynamic review prompt)
    ├── /activity  (time-sorted event feed)
    └── /docs      (this page)`}</pre>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Convex schema</h2>
        <table style={{ width: "100%", fontSize: "0.85rem" }}>
          <thead>
            <tr style={{ borderBottom: "1px solid var(--border)", textAlign: "left" }}>
              <th style={{ padding: "6px 4px" }}>Table</th>
              <th style={{ padding: "6px 4px" }}>Purpose</th>
            </tr>
          </thead>
          <tbody>
            {TABLES.map((t) => (
              <tr key={t.name} style={{ borderBottom: "1px solid var(--border)" }}>
                <td style={{ padding: "6px 4px", fontFamily: "var(--font-mono-stack)" }}>{t.name}</td>
                <td style={{ padding: "6px 4px", color: "var(--text-muted)" }}>{t.purpose}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p style={{ color: "var(--text-muted)", fontSize: "0.82rem", marginTop: 10 }}>
          Plus 9 pre-existing object-level tables (galaxies / reviews / checklistItems / pipelineState / models / chatMessages / activityFeed / mcmcStatus / spectralResults / pageViews). The load-bearing query is{" "}
          <code>papers.getPaperState(slug)</code>; readiness is computed, never hand-set.
        </p>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>MCP tool catalog (11 tools)</h2>
        <p style={{ color: "var(--text-muted)", fontSize: "0.85rem", marginBottom: 14 }}>
          Wired into Claude Code at <code>bigbounce/.claude/mcp_servers.json</code>{" "}
          with <code>CONVEX_URL</code> env var. Stdio transport — server runs locally only.
        </p>
        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          {MCP_TOOLS.map((t) => (
            <div
              key={t.name}
              style={{
                border: "1px solid var(--border)",
                borderRadius: 8,
                padding: 12,
                fontSize: "0.84rem",
              }}
            >
              <code style={{ fontWeight: 600, color: "#0369a1" }}>{t.name}</code>
              <p style={{ margin: "6px 0", color: "var(--text-muted)" }}>{t.summary}</p>
              <p style={{ margin: 0, fontFamily: "var(--font-mono-stack)", fontSize: "0.76rem" }}>
                <span style={{ color: "var(--text-muted)" }}>in:</span> {t.input}
                {" · "}
                <span style={{ color: "var(--text-muted)" }}>out:</span> {t.returns}
              </p>
            </div>
          ))}
        </div>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Skill commands (5 slash commands)</h2>
        <p style={{ color: "var(--text-muted)", fontSize: "0.85rem", marginBottom: 14 }}>
          Auto-loaded by Claude Code from <code>bigbounce/.claude/skills/</code>.
        </p>
        <ul style={{ fontSize: "0.88rem", lineHeight: 1.7, paddingLeft: 20 }}>
          {SKILLS.map((s) => (
            <li key={s.cmd} style={{ marginBottom: 8 }}>
              <code style={{ color: "#0369a1" }}>{s.cmd}</code>
              <span style={{ color: "var(--text-muted)", marginLeft: 8 }}>{s.desc}</span>
            </li>
          ))}
        </ul>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Anti-pattern guards (4 rules)</h2>
        <p style={{ color: "var(--text-muted)", fontSize: "0.85rem", marginBottom: 14 }}>
          Lessons encoded in the MCP layer so no fire can regress.
        </p>
        <ul style={{ fontSize: "0.88rem", lineHeight: 1.6, paddingLeft: 20 }}>
          {GUARDS.map((g) => (
            <li key={g.rule} style={{ marginBottom: 12 }}>
              <strong>{g.rule}.</strong>{" "}
              <span style={{ color: "var(--text-muted)" }}>{g.body}</span>
            </li>
          ))}
        </ul>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Security posture (current)</h2>
        <ul style={{ fontSize: "0.88rem", lineHeight: 1.7, paddingLeft: 20 }}>
          <li>
            <strong>No public mutation endpoints.</strong> The Convex deployment
            URL is referenced from the site for <em>read</em> queries only
            (papers, findings, caveats, activity rollup). Mutations require
            the deployment access token in <code>~/.convex/config.json</code>.
          </li>
          <li>
            <strong>API keys never exposed in build output.</strong> Vendor
            keys (Anthropic, OpenAI, Gemini, Grok, Perplexity) live in
            local <code>.env.local</code> files only — they never reach
            the static export. RunPod keys, HuggingFace tokens, Vercel OIDC
            same.
          </li>
          <li>
            <strong>MCP server is stdio-only.</strong> bigbounce-mcp runs
            as a subprocess of Claude Code or another local agent; there is
            no HTTP listener.
          </li>
          <li>
            <strong>Site is static.</strong> <code>next.config.ts</code>{" "}
            sets <code>output: &quot;export&quot;</code>. No server-side
            routes, no API handlers, no auth flow.
          </li>
          <li>
            <strong>External-review prompts are read-only.</strong> The{" "}
            <code>/papers/&lt;slug&gt;</code> page generates a copy-pasteable
            text prompt; Houston manually pastes into ChatGPT / Gemini /
            Claude. No agent invocation happens through the site.
          </li>
        </ul>
      </section>

      <p
        style={{
          marginTop: 40,
          fontSize: "0.72rem",
          color: "var(--text-muted)",
          fontFamily: "var(--font-mono-stack)",
          textAlign: "center",
        }}
      >
        Source: <code>project-context/DATA_MODEL_ARCHITECTURE.md</code> ·{" "}
        <Link href="https://github.com/Hubify-Projects/bigbounce">
          github.com/Hubify-Projects/bigbounce
        </Link>
      </p>
    </div>
  );
}
