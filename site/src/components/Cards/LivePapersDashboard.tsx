import { getLivePapers, isLive, displayVersion, type LivePaperState } from "@/lib/livePapers";
import Link from "next/link";

function readinessColor(readiness: number) {
  if (readiness >= 95) return "var(--success)";
  if (readiness >= 85) return "var(--text-secondary)";
  if (readiness >= 70) return "var(--warn)";
  return "var(--crit)";
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
    <section aria-label="Paper state" className="live-papers-dashboard">
      <div className="live-papers-dashboard-head">
        <h2>Paper state — {live ? "live from Convex" : "static fallback"}</h2>
        <span
          className={live ? "tone-success" : "tone-caution"}
          style={{ fontSize: "0.7rem", fontFamily: "var(--font-mono-stack)" }}
          title={
            live
              ? "Reading from Convex — site re-renders on every R-round closure."
              : "Reading from static papers.ts + live-status.ts. Run npx convex dev + seed script to flip live (see DATA_MODEL_ARCHITECTURE.md Phase 1.5)."
          }
        >
          ● {live ? "LIVE" : "STATIC"}
        </span>
      </div>

      <div className="table-scroll">
        <table>
          <thead>
            <tr>
              <th>Paper</th>
              <th>Version</th>
              <th>Readiness</th>
              <th>Status</th>
              <th>Updated</th>
              <th style={{ textAlign: "right" }}>Open (B/M/m/C)</th>
              <th style={{ textAlign: "right" }}>PDF</th>
            </tr>
          </thead>
          <tbody>
            {papers.map((p: LivePaperState) => {
              const color = readinessColor(p.readinessComputed);
              return (
                <tr key={p.slug}>
                  <td>
                    <Link
                      href={`/papers/${p.slug}`}
                      style={{
                        color: "var(--text)",
                        fontWeight: 600,
                        textDecoration: "none",
                      }}
                    >
                      {p.number}
                    </Link>
                  </td>
                  <td style={{ color: "var(--text-tertiary)" }}>
                    {displayVersion(p.currentVersion)}
                  </td>
                  <td>
                    <span
                      className="live-papers-readiness"
                      style={{ color, fontWeight: 600 }}
                    >
                      {p.readinessComputed}%
                    </span>
                    <span className="live-papers-bar" aria-hidden="true">
                      <span
                        style={{
                          width: `${p.readinessComputed}%`,
                          background: color,
                        }}
                      />
                    </span>
                  </td>
                  <td style={{ color: "var(--text-tertiary)" }}>
                    {statusLabel(p.status)}
                  </td>
                  <td style={{ color: "var(--text-tertiary)" }}>
                    {p.lastUpdated ?? "—"}
                  </td>
                  <td
                    style={{ textAlign: "right", color: "var(--text-tertiary)" }}
                  >
                    {p.openBlockers}B {p.openMajors}M {p.openMinors}m{" "}
                    {p.openCaveats}C
                  </td>
                  <td style={{ textAlign: "right" }}>
                    {p.sitePdfPath ? (
                      <a
                        href={p.sitePdfPath}
                        target="_blank"
                        rel="noopener noreferrer"
                        style={{
                          color: "var(--text-secondary)",
                          textDecoration: "underline",
                          textUnderlineOffset: 2,
                          textDecorationColor: "var(--border-strong)",
                        }}
                      >
                        PDF
                      </a>
                    ) : (
                      <span style={{ color: "var(--text-muted)" }}>—</span>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {!live && (
        <p
          style={{
            fontSize: "0.72rem",
            color: "var(--text-tertiary)",
            marginTop: 10,
            marginBottom: 0,
          }}
        >
          Showing static fallback data. Set <code>NEXT_PUBLIC_CONVEX_URL</code>{" "}
          and run the Phase 1.5 seed migration to flip this to live.
        </p>
      )}
    </section>
  );
}
