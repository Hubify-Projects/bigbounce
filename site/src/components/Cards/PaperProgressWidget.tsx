import Link from "next/link";
import { getLivePapers } from "@/lib/livePapers";

function readinessColor(pct: number): string {
  if (pct === 100) return "#10b981";
  if (pct >= 90) return "#22c55e";
  if (pct >= 80) return "#84cc16";
  if (pct >= 60) return "#eab308";
  if (pct >= 30) return "#f97316";
  return "#ef4444";
}

function statusDot(status: string): { color: string; label: string } {
  switch (status) {
    case "active-drive-to-100":
      return { color: "#2563eb", label: "active" };
    case "paused-houston-external":
      return { color: "#d97706", label: "paused" };
    case "submitted-arxiv":
      return { color: "#16a34a", label: "submitted" };
    case "in-revision":
      return { color: "#7c3aed", label: "revision" };
    case "accepted":
      return { color: "#10b981", label: "accepted" };
    default:
      return { color: "#6b7280", label: "—" };
  }
}

export async function PaperProgressWidget() {
  const papers = await getLivePapers();
  return (
    <section
      className="section"
      style={{
        border: "1px solid var(--border)",
        borderRadius: 10,
        padding: "14px 18px",
        marginBottom: 18,
      }}
      aria-label="Paper progress snapshot"
    >
      <div
        style={{
          display: "flex",
          alignItems: "baseline",
          justifyContent: "space-between",
          marginBottom: 10,
        }}
      >
        <h3
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.78rem",
            letterSpacing: "0.08em",
            textTransform: "uppercase",
            color: "var(--text-muted)",
            margin: 0,
          }}
        >
          Paper Progress
        </h3>
        <Link
          href="/paper"
          style={{
            fontSize: "0.72rem",
            color: "var(--text-muted)",
            textDecoration: "none",
          }}
        >
          full list →
        </Link>
      </div>
      <ul
        style={{
          listStyle: "none",
          padding: 0,
          margin: 0,
          display: "grid",
          gap: 6,
        }}
      >
        {papers.map((p) => {
          const dot = statusDot(p.status);
          return (
            <li key={p.slug}>
              <Link
                href={`/papers/${p.slug}`}
                style={{
                  display: "grid",
                  gridTemplateColumns: "48px 1fr 92px 44px",
                  alignItems: "center",
                  gap: 10,
                  padding: "6px 4px",
                  borderRadius: 6,
                  color: "var(--text)",
                  textDecoration: "none",
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: "0.8rem",
                  transition: "background 120ms",
                }}
                className="paper-progress-row"
              >
                <span style={{ fontWeight: 600, color: "var(--text-muted)" }}>
                  P{p.number}
                </span>
                <span
                  style={{
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    whiteSpace: "nowrap",
                    fontSize: "0.78rem",
                    color: "var(--text-muted)",
                  }}
                  title={p.currentVersion ?? ""}
                >
                  {p.currentVersion ?? "—"}
                </span>
                <div
                  style={{
                    position: "relative",
                    height: 6,
                    borderRadius: 3,
                    background: "var(--border)",
                    overflow: "hidden",
                  }}
                  aria-label={`${p.readinessComputed}% ready`}
                >
                  <div
                    style={{
                      width: `${p.readinessComputed}%`,
                      height: "100%",
                      background: readinessColor(p.readinessComputed),
                      transition: "width 240ms",
                    }}
                  />
                </div>
                <span
                  style={{
                    fontSize: "0.74rem",
                    textAlign: "right",
                    color: "var(--text-muted)",
                  }}
                >
                  <span
                    aria-hidden="true"
                    title={dot.label}
                    style={{
                      display: "inline-block",
                      width: 7,
                      height: 7,
                      borderRadius: "50%",
                      background: dot.color,
                      marginRight: 4,
                      verticalAlign: "middle",
                    }}
                  />
                  {p.readinessComputed}%
                </span>
              </Link>
            </li>
          );
        })}
      </ul>
    </section>
  );
}
