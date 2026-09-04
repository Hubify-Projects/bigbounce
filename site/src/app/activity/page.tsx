import type { Metadata } from "next";
import Link from "next/link";
import { getRecentActivity, type ActivityEvent } from "@/lib/liveActivity";
import { Band, PageHeader, StatRow, TimelineList, type TimelineEntry } from "@/components/primitives";

export const metadata: Metadata = {
  title: "Activity",
  description:
    "Time-stamped activity feed for the BigBounce research program — version bumps, review rounds, finding closures, and compute events from the live research database.",
};

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

function clampTimestamp(ms: number, now: number): number {
  return ms > now + 60_000 ? now : ms;
}

function publicHeadline(raw: string): string {
  return raw.replace(/\s*\(subagent\)\s*$/i, "").trim();
}

function paperLabel(slug: string | null): string | undefined {
  if (!slug) return undefined;
  return slug.replace(/^paper-(\d+)([a-zA-Z]?)$/, (_, n, l) => `Paper ${n}${l.toUpperCase()}`);
}

function kindLabel(kind: string): string {
  switch (kind) {
    case "version_bump": return "version";
    case "r_round": return "review round";
    case "r_round_done": return "review round ✓";
    case "finding_real_close": return "finding ✓";
    case "finding_audit_close": return "finding (verified)";
    case "caveat_close": return "caveat ✓";
    case "pod_start": return "compute start";
    case "pod_stop": return "compute stop";
    default: return kind.replace(/_/g, " ");
  }
}

function toEntry(e: ActivityEvent, now: number): TimelineEntry {
  const ts = clampTimestamp(e.timestamp, now);
  const paper = paperLabel(e.paperSlug);
  return {
    id: e.id,
    dateISO: ptLine(ts),
    kind: kindLabel(e.kind),
    title: paper ? `${paper} · ${publicHeadline(e.headline)}` : publicHeadline(e.headline),
    summary: e.detail || undefined,
    href: e.paperSlug ? `/papers/${e.paperSlug}` : undefined,
  };
}

export default async function ActivityPage() {
  const { events, summary, source, fetchedAt } = await getRecentActivity(300);
  const live = source === "convex";

  return (
    <>
      <Band>
        <PageHeader
          eyebrow={live ? "Live research activity" : "Activity feed offline"}
          title="Activity"
          lead="Every research event from the live database — version bumps, review rounds, finding closures, caveat resolutions, compute runs — time-sorted, newest first. The curated review-loop story (verdict trajectories, gap-closure, skills growth) lives at /reviews; this is the raw machine-event stream."
          actions={[{ label: "Review activity →", href: "/reviews" }]}
        />
        {summary && (
          <StatRow
            items={[
              { value: summary.paperVersions, label: "versions" },
              { value: summary.rRounds, label: "review rounds" },
              { value: summary.findings.open, label: "findings open" },
              { value: summary.findings.closed, label: "findings closed" },
              { value: summary.caveats.open, label: "caveats open" },
              { value: summary.pods.running, label: "compute running" },
            ]}
          />
        )}
      </Band>
      <Band tone="alt">
        <TimelineList entries={events.map((e) => toEntry(e, fetchedAt))} />
        {events.length === 0 && (
          <p className="row-purpose">No activity in the feed yet.</p>
        )}
        <p className="timeline-list-empty" style={{ marginTop: 16 }}>
          Showing up to 300 events. Older history in{" "}
          <Link href="https://github.com/Hubify-Projects/bigbounce">git log</Link> and SSOT/queue.md.
        </p>
      </Band>
    </>
  );
}
