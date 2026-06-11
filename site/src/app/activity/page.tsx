import type { Metadata } from "next";
import Link from "next/link";
import { getRecentActivity, type ActivityEvent } from "@/lib/liveActivity";

export const metadata: Metadata = {
  title: "Activity",
  description:
    "Time-stamped activity feed for the BigBounce research program — version bumps, R-rounds, finding closures, and pod lifecycle events from the Convex live source-of-truth.",
};

function relativeTime(ms: number, now: number): string {
  const diff = now - ms;
  const min = Math.floor(diff / 60000);
  if (min < 1) return "just now";
  if (min < 60) return `${min} min ago`;
  const hr = Math.floor(min / 60);
  if (hr < 24) return `${hr} hr ago`;
  const day = Math.floor(hr / 24);
  if (day < 30) return `${day}d ago`;
  const mo = Math.floor(day / 30);
  return `${mo}mo ago`;
}

/* Render in PT (matching the home-page header), not UTC. Some event writers
   stored PDT-naive datetimes as UTC (+7h) and one pod writer ran ~36h fast,
   so raw stamps used to render up to 2 days in the future. */
const ptFormat = new Intl.DateTimeFormat("en-CA", {
  timeZone: "America/Los_Angeles",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
  hour12: false,
});

function ptLine(ms: number): string {
  return ptFormat.format(new Date(ms)).replace(",", "") + " PT";
}

/* Defensive clamp: a research log can never contain future events. If a
   Convex row carries a timestamp ahead of render time (bad writer clock /
   PDT-naive double conversion), display it clamped to render time and keep
   the raw stored stamp in the tooltip for forensics. */
function clampTimestamp(
  ms: number,
  now: number,
): { ms: number; skewed: boolean } {
  return ms > now + 60_000 ? { ms: now, skewed: true } : { ms, skewed: false };
}

function kindLabel(kind: string): string {
  switch (kind) {
    case "version_bump": return "VERSION";
    case "r_round": return "R-ROUND";
    case "r_round_done": return "R-ROUND ✓";
    case "finding_real_close": return "FINDING ✓";
    case "finding_audit_close": return "FINDING (audit)";
    case "caveat_close": return "CAVEAT ✓";
    case "pod_start": return "POD START";
    case "pod_stop": return "POD STOP";
    default: return kind.toUpperCase();
  }
}

export default async function ActivityPage() {
  const { events, summary, source, fetchedAt } = await getRecentActivity(300);
  const live = source === "convex";
  const renderedAt = fetchedAt;

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Live Research Activity
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          Activity Feed
          <span
            style={{
              marginLeft: 12,
              fontSize: "0.7rem",
              color: live ? "#16a34a" : "#d97706",
              fontFamily: "var(--font-mono-stack)",
              verticalAlign: "middle",
            }}
            title={
              live
                ? "Reading from Convex — every R-round / closure / pod event lands here within seconds."
                : "Convex unreachable; feed empty. Set NEXT_PUBLIC_CONVEX_URL."
            }
          >
            ● {live ? "LIVE" : "OFFLINE"}
          </span>
        </h1>
        <p className="subtitle">
          Every paper-orchestration event from the Convex source-of-truth:
          version bumps, cross-vendor R-rounds, finding truth-audits, §pathc_caveats closures,
          pod lifecycle. Time-sorted descending. See{" "}
          <Link href="/docs">/docs</Link> for how the pipeline writes here.
        </p>
        <p
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.78rem",
            marginTop: 12,
            padding: "10px 14px",
            border: "1px solid var(--border)",
            borderRadius: 8,
            color: "var(--text-secondary)",
            maxWidth: "72ch",
          }}
        >
          Looking for the progress story? The curated review-loop timeline — paper/kind
          filters, verdict trajectories, gap-closure and skills-growth charts — lives at{" "}
          <Link href="/reviews" style={{ color: "var(--accent-link)", textDecoration: "underline" }}>
            /reviews
          </Link>
          . This page is the raw machine-event stream.
        </p>
      </div>

      {summary && (
        <section
          aria-label="Activity summary"
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(120px, 1fr))",
            gap: 10,
            marginTop: 20,
            marginBottom: 20,
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.82rem",
          }}
        >
          {[
            { label: "Versions", v: summary.paperVersions },
            { label: "R-Rounds", v: summary.rRounds },
            { label: "Findings (open)", v: summary.findings.open },
            { label: "Findings (closed)", v: summary.findings.closed },
            { label: "Caveats (open)", v: summary.caveats.open },
            { label: "Caveats (closed)", v: summary.caveats.closed },
            { label: "Pods (running)", v: summary.pods.running },
          ].map((s) => (
            <div
              key={s.label}
              style={{
                border: "1px solid var(--border)",
                borderRadius: 8,
                padding: "10px 12px",
                background: "rgba(0,0,0,0.02)",
              }}
            >
              <div style={{ color: "var(--text-muted)", fontSize: "0.7rem", marginBottom: 4 }}>
                {s.label}
              </div>
              <div style={{ fontSize: "1.1rem", fontWeight: 600 }}>{s.v}</div>
            </div>
          ))}
        </section>
      )}

      <section
        aria-label="Event feed"
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 6,
          marginTop: 24,
        }}
      >
        {events.length === 0 && (
          <p
            style={{
              color: "var(--text-muted)",
              padding: 16,
              border: "1px dashed var(--border)",
              borderRadius: 8,
              fontFamily: "var(--font-mono-stack)",
              fontSize: "0.85rem",
            }}
          >
            No activity in the feed yet. Run an R-round or close a finding via
            the bigbounce-mcp tools to populate this.
          </p>
        )}
        {events.map((e: ActivityEvent) => {
          const { ms: displayTs, skewed } = clampTimestamp(
            e.timestamp,
            renderedAt,
          );
          return (
          <article
            key={e.id}
            style={{
              border: "1px solid var(--border)",
              borderLeft: `4px solid ${e.colorHint}`,
              borderRadius: 6,
              padding: "10px 14px",
              fontFamily: "var(--font-mono-stack)",
            }}
          >
            <div
              style={{
                display: "flex",
                gap: 12,
                alignItems: "baseline",
                flexWrap: "wrap",
                marginBottom: 4,
              }}
            >
              <span
                style={{
                  fontSize: "0.7rem",
                  letterSpacing: "0.06em",
                  color: e.colorHint,
                  fontWeight: 600,
                  textTransform: "uppercase",
                }}
              >
                {kindLabel(e.kind)}
              </span>
              {e.paperSlug && (
                <Link
                  href={`/papers/${e.paperSlug}`}
                  style={{
                    fontSize: "0.7rem",
                    color: "var(--text-muted)",
                    textDecoration: "none",
                  }}
                >
                  {e.paperSlug}
                </Link>
              )}
              <span
                style={{
                  fontSize: "0.7rem",
                  color: "var(--text-muted)",
                  marginLeft: "auto",
                }}
                title={
                  skewed
                    ? `stored stamp ${ptLine(e.timestamp)} is in the future (writer clock skew) — clamped to feed-render time`
                    : ptLine(e.timestamp)
                }
              >
                {ptLine(displayTs)} · {relativeTime(displayTs, renderedAt)}
                {skewed && (
                  <span
                    style={{ color: "var(--warn, #d97706)", marginLeft: 6 }}
                    aria-label="timestamp clamped due to writer clock skew"
                  >
                    ⚠ clock-skew
                  </span>
                )}
              </span>
            </div>
            <div style={{ fontSize: "0.88rem", marginBottom: 4 }}>
              {e.headline}
            </div>
            {e.detail && (
              <div
                style={{
                  fontSize: "0.78rem",
                  color: "var(--text-muted)",
                  lineHeight: 1.4,
                }}
              >
                {e.detail}
              </div>
            )}
          </article>
          );
        })}
      </section>

      <p
        style={{
          marginTop: 32,
          fontSize: "0.72rem",
          color: "var(--text-muted)",
          fontFamily: "var(--font-mono-stack)",
          textAlign: "center",
        }}
      >
        Showing up to 300 events. Older history in git log
        (github.com/Hubify-Projects/bigbounce) and SSOT/queue.md.
      </p>
    </>
  );
}
