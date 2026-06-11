/**
 * Server-side fetcher for the unified Convex activity feed.
 *
 * Used by /activity to render a time-sorted list of every paper-orchestration
 * event (version bumps, R-rounds, finding closures, caveat closures, pod
 * lifecycle). Read-only.
 */
export type ActivityEvent = {
  id: string;
  kind: string;
  paperSlug: string | null;
  headline: string;
  detail: string;
  timestamp: number;
  colorHint: string;
};

export type ActivitySummary = {
  paperVersions: number;
  rRounds: number;
  findings: { total: number; closed: number; open: number };
  caveats: { total: number; closed: number; open: number };
  pods: { total: number; running: number };
};

const CONVEX_URL =
  process.env.NEXT_PUBLIC_CONVEX_URL || process.env.CONVEX_URL || "";

export async function getRecentActivity(limit = 200): Promise<{
  events: ActivityEvent[];
  summary: ActivitySummary | null;
  source: "convex" | "static-fallback";
  /** Epoch ms when the feed was fetched — used to clamp future-skewed event rows. */
  fetchedAt: number;
}> {
  const fetchedAt = Date.now();
  if (!CONVEX_URL) {
    return { events: [], summary: null, source: "static-fallback", fetchedAt };
  }
  try {
    const { ConvexHttpClient } = await import("convex/browser");
    const client = new ConvexHttpClient(CONVEX_URL);
    const events = (await client.query(
      "activityRollup:recent" as unknown as Parameters<typeof client.query>[0],
      { limit }
    )) as ActivityEvent[];
    const summary = (await client.query(
      "activityRollup:summary" as unknown as Parameters<typeof client.query>[0],
      {}
    )) as ActivitySummary;
    return { events, summary, source: "convex", fetchedAt };
  } catch (err) {
    console.warn("[liveActivity] Convex fetch failed:", err);
    return { events: [], summary: null, source: "static-fallback", fetchedAt };
  }
}
