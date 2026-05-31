import { getLivePapers, isLive, type LivePaperState } from "@/lib/livePapers";
import Link from "next/link";

function readinessColor(readiness: number) {
  if (readiness >= 95) return "#16a34a"; // green
  if (readiness >= 85) return "#0369a1"; // blue
  if (readiness >= 70) return "#d97706"; // amber
  return "#dc2626"; // red
}

function statusLabel(status: string): string {
  switch (status) {
    case "active-drive-to-100":
      return "active";
    case "paused-houston-external":
      return "paused (houston review)";
    case "submitted-arxiv":
      return "arXiv submitted";
    case "in-revision":
      return "in revision";
    case "accepted":
      return "accepted";
    default:
      return status;
  }
}

/**
 * Server-component dashboard rendering live paper state from Convex
 * (or static fallback if Convex isn't deployed yet). Replaces the
 * hand-maintained papers.ts + live-status.ts duplication on the
 * homepage. Phase 4 of the rebuild.
 */
export async function LivePapersDashboard() {
  const papers = await getLivePapers();
  const live = isLive(papers);

  return (
    <section
      aria-label="Paper state"
      style={{
        border: "1px solid var(--border)",
        borderRadius: 10,
        padding: 16,
        background: live ? "rgba(22,163,74,0.03)" : "rgba(217,119,6,0.03)",
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "baseline",
          marginBottom: 12,
        }}
      >
        <h2
          style={{
            margin: 0,
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.85rem",
            letterSpacing: "0.06em",
            textTransform: "uppercase",
            color: "var(--text-muted)",
          }}
        >
          Paper state — {live ? "live from Convex" : "static fallback"}
        </h2>
        <span
          style={{
            fontSize: "0.7rem",
            color: live ? "#16a34a" : "#d97706",
            fontFamily: "var(--font-mono-stack)",
          }}
          title={
            live
              ? "Reading from Convex — site re-renders on every R-round closure."
              : "Reading from static papers.ts + live-status.ts. Run npx convex dev + seed script to flip live (see DATA_MODEL_ARCHITECTURE.md Phase 1.5)."
          }
        >
          ● {live ? "LIVE" : "STATIC"}
        </span>
      </div>

      <table
        style={{
          width: "100%",
          fontSize: "0.85rem",
          fontFamily: "var(--font-mono-stack)",
          borderCollapse: "collapse",
        }}
      >
        <thead>
          <tr style={{ borderBottom: "1px solid var(--border)", textAlign: "left" }}>
            <th style={{ padding: "6px 4px" }}>Paper</th>
            <th style={{ padding: "6px 4px" }}>Version</th>
            <th style={{ padding: "6px 4px" }}>Readiness</th>
            <th style={{ padding: "6px 4px" }}>Status</th>
            <th style={{ padding: "6px 4px" }}>Updated</th>
            <th style={{ padding: "6px 4px", textAlign: "right" }}>Open (B/M/m/C)</th>
          </tr>
        </thead>
        <tbody>
          {papers.map((p: LivePaperState) => {
            const color = readinessColor(p.readinessComputed);
            return (
              <tr
                key={p.slug}
                style={{ borderBottom: "1px solid var(--border)" }}
              >
                <td style={{ padding: "6px 4px" }}>
                  <Link
                    href={`/papers/${p.slug}`}
                    style={{ color: "var(--text)", textDecoration: "none" }}
                  >
                    {p.number}
                  </Link>
                </td>
                <td style={{ padding: "6px 4px", color: "var(--text-muted)" }}>
                  {p.currentVersion ?? "—"}
                </td>
                <td style={{ padding: "6px 4px" }}>
                  <span style={{ color, fontWeight: 600 }}>
                    {p.readinessComputed}%
                  </span>
                </td>
                <td style={{ padding: "6px 4px", color: "var(--text-muted)" }}>
                  {statusLabel(p.status)}
                </td>
                <td style={{ padding: "6px 4px", color: "var(--text-muted)" }}>
                  {p.lastUpdated ?? "—"}
                </td>
                <td
                  style={{
                    padding: "6px 4px",
                    textAlign: "right",
                    color: "var(--text-muted)",
                  }}
                >
                  {p.openBlockers}B {p.openMajors}M {p.openMinors}m {p.openCaveats}C
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>

      {!live && (
        <p
          style={{
            fontSize: "0.72rem",
            color: "var(--text-muted)",
            marginTop: 10,
            marginBottom: 0,
          }}
        >
          ⚠️ Showing static fallback data. Set <code>NEXT_PUBLIC_CONVEX_URL</code>{" "}
          and run the Phase 1.5 seed migration to flip this to live.
        </p>
      )}
    </section>
  );
}
