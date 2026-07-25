/**
 * publicationStatus.ts — server-side fetcher for the directive-P publication
 * surface (`convex/publicationStatus.ts`).
 *
 * Replaces `liveReadiness.getPublishEta`, which fed the retired clean-wave ETA
 * widget. See the retirement note in convex/readinessMetrics.ts for why.
 *
 * Failure behaviour is deliberately DIFFERENT from the old fetcher. The old one
 * returned null and the homepage rendered nothing — so a broken Convex link and
 * a healthy one looked identical to a reader. Here, null is passed through to
 * the widget, which renders an explicit "live status unavailable" state. The
 * surface must never silently disappear or silently age.
 */

const CONVEX_URL =
  process.env.NEXT_PUBLIC_CONVEX_URL || process.env.CONVEX_URL || "";

export type PublicationOwner = "houston" | "agent" | "done";

export type PublicationPaper = {
  paperId: string;
  paperSlug: string;
  shortTitle: string;
  sitePdfPath: string | null;
  currentVersion: string | null;
  versionDateISO: string | null;
  versionCreatedAtMs: number;
  openBlockers: number;
  openMajors: number;
  openMinors: number;
  openCaveats: number;
  houstonSignOff: string | null;
  boardDateISO: string | null;
  boardWrittenMs: number;
  boardVersions: string[];
  boardCoversCurrentVersion: boolean;
  evidenceMs: number;
  owner: PublicationOwner;
  remaining: string;
};

export type PublicationStatus = {
  generatedAtMs: number;
  newestEvidenceMs: number;
  staleAfterDays: number;
  isStaleAtQueryTime: boolean;
  papersTotal: number;
  papersSignedOff: number;
  papersAwaitingHouston: number;
  papersAwaitingAgent: number;
  perPaper: PublicationPaper[];
  composition: string;
};

export async function getPublicationStatus(): Promise<PublicationStatus | null> {
  if (!CONVEX_URL) return null;
  try {
    const { ConvexHttpClient } = await import("convex/browser");
    const client = new ConvexHttpClient(CONVEX_URL);
    return (await client.query(
      "publicationStatus:get" as unknown as Parameters<typeof client.query>[0],
    )) as PublicationStatus;
  } catch (err) {
    console.warn("[publicationStatus] fetch failed:", err);
    return null;
  }
}

/** "2026-07-23" → "Jul 23, 2026". Empty input passes through as an em dash. */
export function shortDate(iso: string | null): string {
  if (!iso) return "—";
  const d = new Date(`${iso}T12:00:00Z`);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", {
    timeZone: "UTC",
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}
