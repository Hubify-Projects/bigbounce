import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Architecture — API & MCP",
  description:
    "Bigbounce data model, Convex API, and MCP tool catalog. Discoverable interface for any agent (Claude Code, Codex, Cursor) contributing to the project.",
};

const MCP_TOOLS = [
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
      "Apply truth-audit verdict to a finding (REQUIRED before close per feedback_peer_review_truth_audit_protocol).",
    input:
      "{ findingId: string, verdict: VERIFIED|FALSIFIED|STALE|OUT-OF-SCOPE|OPINION, evidence: string }",
    returns: "void (mutation)",
  },
  {
    name: "bigbounce_close_finding",
    summary:
      "Atomic finding closure. Enforces closureStatus enum + truth-audit-first ordering.",
    input:
      "{ findingId: string, closureStatus: enum, closureCommit?: string, closureArtifact?: string, closureNote?: string }",
    returns: "void (mutation)",
  },
  {
    name: "bigbounce_bump_paper_version",
    summary:
      "Atomic .tex version bump. Site re-renders on Convex subscription — eliminates the 5-file hand-edit drift.",
    input:
      "{ paperSlug, version, datestamp, texCommit, pdfMd5, pdfPages, pdfSizeBytes, changelog, arxivTarballPath?, arxivTarballSizeBytes? }",
    returns: "Id<paper_versions>",
  },
  {
    name: "bigbounce_list_pathc_caveats",
    summary: "Per-paper §pathc_caveats deferral list. Each item has closureMethod enum.",
    input: "{ paperSlug: string }",
    returns: "Array<PathcCaveat>",
  },
  {
    name: "bigbounce_close_pathc_caveat",
    summary:
      "Close a §pathc_caveats item. closureMethod enum includes ⚠️ 'text-only-no-real-action' as explicit flag.",
    input:
      "{ paperSlug, label, closureMethod: enum, closureArtifact?, closureCommit?, closureNote? }",
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
    summary:
      "Dynamic copy/paste external-review prompt — replaces hardcoded focusAreas array in [slug]/page.tsx.",
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
  { name: "papers", purpose: "Canonical per-paper state (NOT readiness — that's computed)" },
  { name: "paper_versions", purpose: "Append-only .tex version history" },
  { name: "r_rounds", purpose: "Cross-vendor peer-review rounds" },
  { name: "findings", purpose: "Individual R-round findings with truth-audit lifecycle" },
  { name: "pathc_caveats", purpose: "Paper-internal §pathc_caveats deferrals" },
  { name: "pods", purpose: "RunPod lifecycle + cost accounting" },
  { name: "tasks", purpose: "Open work queue (cross-paper + infrastructure)" },
];

export default function ApiDocsPage() {
  return (
    <div style={{ maxWidth: 920, margin: "0 auto", padding: "24px 0" }}>
      <header style={{ marginBottom: 32 }}>
        <h1 style={{ margin: "0 0 8px 0" }}>API &amp; MCP</h1>
        <p style={{ color: "var(--text-muted)", maxWidth: 720, lineHeight: 1.55 }}>
          Bigbounce paper-orchestration state lives in Convex. The{" "}
          <code>bigbounce-mcp</code> server exposes 11 tools any MCP-aware agent
          (Claude Code, Codex, Cursor) can call to read or mutate that state —
          no more hand-editing the 10+ unsynced surfaces this project used to
          maintain. See{" "}
          <Link href="https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/DATA_MODEL_ARCHITECTURE.md">
            DATA_MODEL_ARCHITECTURE.md
          </Link>{" "}
          for the full rebuild plan.
        </p>
      </header>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.1rem", marginBottom: 12 }}>Convex schema</h2>
        <p style={{ color: "var(--text-muted)", fontSize: "0.9rem" }}>
          7 paper-orchestration tables in <code>convex/schema.ts</code> (alongside
          the existing 9 object-level tables for galaxies, MCMC, etc.):
        </p>
        <div className="table-scroll">
        <table style={{ width: "100%", fontSize: "0.85rem", marginTop: 8 }}>
          <thead>
            <tr style={{ borderBottom: "1px solid var(--border)", textAlign: "left" }}>
              <th style={{ padding: "6px 4px" }}>Table</th>
              <th style={{ padding: "6px 4px" }}>Purpose</th>
            </tr>
          </thead>
          <tbody>
            {CONVEX_TABLES.map((t) => (
              <tr key={t.name} style={{ borderBottom: "1px solid var(--border)" }}>
                <td style={{ padding: "6px 4px", fontFamily: "var(--font-mono-stack)" }}>
                  {t.name}
                </td>
                <td style={{ padding: "6px 4px", color: "var(--text-muted)" }}>
                  {t.purpose}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
        <p style={{ color: "var(--text-muted)", fontSize: "0.82rem", marginTop: 10 }}>
          The load-bearing query is{" "}
          <code>papers.getPaperState(slug)</code> — it computes readiness as{" "}
          <code>ceiling − 2·openBlockers − 1·openMajors − 0.2·openMinors − 1·openCaveats</code>.
          The ceiling is the data-driven <code>readinessCap</code>, and as of 2026-07-07 that
          cap is <strong>verdict-derived</strong>, not ladder-derived: 50 (error-clean/verified
          base) + per-EXT-reviewer points from the latest verified round (ACCEPT +16.7, MINOR
          +12, MAJOR +6, REJECT 0). No paper is reviewer-accepted yet — every one still draws a
          real ChatGPT REJECT — so the caps sit at 62–80 (avg 68), not 99. A reviewer ACCEPT is
          the bar; the system never auto-awards 100.
        </p>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.1rem", marginBottom: 12 }}>MCP tool catalog</h2>
        <p style={{ color: "var(--text-muted)", fontSize: "0.9rem", marginBottom: 16 }}>
          Wire into Claude Code via <code>bigbounce/.claude/mcp_servers.json</code>{" "}
          with <code>CONVEX_URL</code> env var. See{" "}
          <code>mcp/bigbounce-mcp/README.md</code> for install / build steps.
        </p>
        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          {MCP_TOOLS.map((t) => (
            <div
              key={t.name}
              style={{
                border: "1px solid var(--border)",
                borderRadius: 8,
                padding: 12,
                fontSize: "0.85rem",
              }}
            >
              <code style={{ fontWeight: 600, color: "#0369a1" }}>{t.name}</code>
              <p style={{ margin: "6px 0", color: "var(--text-muted)" }}>{t.summary}</p>
              <p style={{ margin: "4px 0", fontFamily: "var(--font-mono-stack)", fontSize: "0.78rem" }}>
                <span style={{ color: "var(--text-muted)" }}>input:</span> {t.input}
              </p>
              <p style={{ margin: "4px 0", fontFamily: "var(--font-mono-stack)", fontSize: "0.78rem" }}>
                <span style={{ color: "var(--text-muted)" }}>returns:</span> {t.returns}
              </p>
            </div>
          ))}
        </div>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2 style={{ fontSize: "1.1rem", marginBottom: 12 }}>Skill package</h2>
        <p style={{ color: "var(--text-muted)", fontSize: "0.9rem" }}>
          5 Convex-backed slash commands at <code>bigbounce/.claude/skills/</code>{" "}
          auto-loaded by Claude Code per-project:
        </p>
        <ul style={{ fontSize: "0.88rem", lineHeight: 1.7 }}>
          <li>
            <code>/bigbounce-status</code> — dashboard
          </li>
          <li>
            <code>/bigbounce-r-round &lt;paper-slug&gt;</code> — fire direct-vendor R-round, write findings to Convex
          </li>
          <li>
            <code>/bigbounce-truth-audit &lt;findingId&gt; &lt;verdict&gt; &lt;evidence&gt;</code> — REQUIRED before close
          </li>
          <li>
            <code>/bigbounce-close</code> — atomic finding/caveat closure
          </li>
          <li>
            <code>/bigbounce-bump &lt;paper-slug&gt; &lt;version&gt;</code> — atomic version bump, site re-renders
          </li>
        </ul>
      </section>

      <section>
        <h2 style={{ fontSize: "1.1rem", marginBottom: 12 }}>Anti-pattern guards</h2>
        <p style={{ color: "var(--text-muted)", fontSize: "0.9rem", marginBottom: 8 }}>
          Lessons learned (encoded in the MCP layer so no future fire can regress):
        </p>
        <ul style={{ fontSize: "0.88rem", lineHeight: 1.7 }}>
          <li>
            <strong>No caveat-as-closure.</strong>{" "}
            <code>closeFinding</code> + <code>closePathcCaveat</code> require an
            explicit <code>closureMethod</code> enum. The value{" "}
            <code>text-only-no-real-action</code> is permitted but raises a ⚠️ flag
            (Houston 2026-05-29: "simply disclosing deferred items and caveats IS NOT REAL SCIENCE").
          </li>
          <li>
            <strong>Truth-audit before close.</strong> Findings must have{" "}
            <code>truthAuditVerdict</code> set before <code>close</code> succeeds (per{" "}
            <code>feedback_peer_review_truth_audit_protocol</code>).
          </li>
          <li>
            <strong>No OpenRouter excuse.</strong> Direct vendor keys
            (Anthropic/OpenAI/Gemini/Grok/Perplexity) live in{" "}
            <code>youmd/.env.local</code>; <code>tools/cross_vendor_review_direct.py</code>{" "}
            calls them directly. OpenRouter weekly cap is no longer a blocker (per{" "}
            <code>feedback_no_openrouter_excuse</code>).
          </li>
          <li>
            <strong>No hand-set readiness.</strong>{" "}
            <code>readinessComputed</code> is derived from open findings + caveats.
            Cannot be patched directly via mutation.
          </li>
        </ul>
      </section>
    </div>
  );
}
