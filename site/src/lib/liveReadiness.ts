/**
 * liveReadiness.ts — server-side fetchers for the readinessMetrics + rigorEvents
 * Convex tables that drive the /reviews verdict-trajectory chart.
 *
 * Matches the codebase pattern (livePapers.ts): ConvexHttpClient on the server,
 * graceful empty/null fallback so the build NEVER breaks when Convex is
 * unreachable. Data updates land on the live site on every commit/push (Vercel
 * rebuild re-runs these fetches) and via Convex's own subscription for any
 * client that reads it.
 *
 * HONESTY: every verdict here is a REAL recorded verdict (INT-API raws + EXT
 * browser raws). A "failed" leg is a data gap, never a zero.
 *
 * RETIRED 2026-07-24: `getPublishEta` / `EtaResult` / `formatEtaHours` lived
 * here and fed the homepage "Submission-ready ETA". They projected hours to
 * directive K's two-clean-waves bar — superseded by directives L/M/P — from
 * rows that had stopped being written on 2026-07-16. Replaced by
 * `@/lib/publicationStatus`, whose surface degrades to an explicit stale state
 * instead of aging silently. See convex/readinessMetrics.ts for the full note.
 */

const CONVEX_URL =
  process.env.NEXT_PUBLIC_CONVEX_URL || process.env.CONVEX_URL || "";

export type WaveVerdict = {
  reviewer: string; // ChatGPT | Grok | Gemini | OpenAI | Claude
  channel: "INT" | "EXT";
  verdict: "reject" | "major-revisions" | "minor-revisions" | "accept" | "failed";
};

export type WaveRow = {
  paperSlug: string;
  paperId: string;
  waveLabel: string;
  dateISO: string;
  seq: number;
  genuinelyNewCount: number;
  cleanWaveStreak: number;
  openComputeCount: number;
  openVenueCount: number;
  verdicts: WaveVerdict[];
  note?: string;
};

export type RigorEvent = {
  label: string;
  dateISO: string;
  description: string;
  source: string;
};

async function convexQuery<T>(path: string): Promise<T | null> {
  if (!CONVEX_URL) return null;
  try {
    const { ConvexHttpClient } = await import("convex/browser");
    const client = new ConvexHttpClient(CONVEX_URL);
    const result = (await client.query(
      path as unknown as Parameters<typeof client.query>[0],
    )) as T;
    return result;
  } catch (err) {
    console.warn(`[liveReadiness] ${path} fetch failed:`, err);
    return null;
  }
}

export async function getReadinessWaves(): Promise<WaveRow[]> {
  return (await convexQuery<WaveRow[]>("readinessMetrics:listWaves")) ?? [];
}

export async function getRigorEvents(): Promise<RigorEvent[]> {
  return (await convexQuery<RigorEvent[]>("readinessMetrics:listRigorEvents")) ?? [];
}
