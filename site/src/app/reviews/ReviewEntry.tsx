/**
 * Server-rendered review-feed entry. NO "use client" — these entries must
 * land fully in the static HTML (SEO / no-JS / curl readers). The client
 * filter controller (ReviewsClient) only toggles visibility via the
 * data-papers / data-kind attributes rendered here.
 */
import Link from "next/link";
import type { ReviewRound, ReviewRoundKind } from "@/data/reviewTimeline";

export const KIND_LABEL: Record<ReviewRoundKind, string> = {
  "external-browser": "EXTERNAL",
  "internal-api": "INTERNAL",
  "internal-cc": "INTERNAL",
  "skill-improvement": "SKILL-UPGRADE",
  "closure-wave": "CLOSURES",
  "ext-closure": "CLOSURES",
  restructure: "DECISION",
};

/** Filterable kind groups (internal-api + internal-cc collapse into INTERNAL). */
export const KIND_GROUPS = ["EXTERNAL", "INTERNAL", "SKILL-UPGRADE", "CLOSURES", "DECISION"] as const;
export type KindGroup = (typeof KIND_GROUPS)[number];

export function kindGroupOf(kind: ReviewRoundKind): KindGroup {
  return KIND_LABEL[kind] as KindGroup;
}

function KindBadge({ kind }: { kind: ReviewRoundKind }) {
  const external = kind === "external-browser";
  return (
    <span className={external ? "review-kind-badge is-external" : "review-kind-badge"}>
      {KIND_LABEL[kind]}
    </span>
  );
}

function GapLine({ round }: { round: ReviewRound }) {
  const gap = round.gapMetric;
  if (!gap) return null;
  const line =
    gap.externalOnlyFindings > 0
      ? `internal missed ${gap.externalOnlyFindings} finding${gap.externalOnlyFindings === 1 ? "" : "s"} external caught — ${gap.note}`
      : `internal/external gap: ${gap.note}`;
  return <p className="review-gap">{line}</p>;
}

export function ReviewEntry({ round }: { round: ReviewRound }) {
  return (
    <article
      className="review-entry"
      aria-label={round.id}
      data-papers={round.papers.join(" ")}
      data-kind={kindGroupOf(round.kind)}
    >
      <div className="review-entry-meta">
        <span className="review-timestamp">
          {round.dateISO}
          {round.timePT ? ` · ${round.timePT}` : ""}
        </span>
        <KindBadge kind={round.kind} />
        <span className="review-timestamp">{round.id}</span>
      </div>
      <h2 className="review-entry-title">{round.title}</h2>
      <div className="review-paper-chips">
        {round.papers.map((p) => (
          <span key={p} className="review-paper-chip">
            {p}
          </span>
        ))}
      </div>
      <p className="review-summary">{round.summary}</p>
      {round.keyTakeaways.length > 0 && (
        <details className="review-takeaways">
          <summary>key takeaways ({round.keyTakeaways.length})</summary>
          <ul>
            {round.keyTakeaways.map((t) => (
              <li key={t}>{t}</li>
            ))}
          </ul>
        </details>
      )}
      <GapLine round={round} />
      {round.links.length > 0 && (
        <div className="review-links">
          {round.links.map((l) => (
            <a key={`${l.label}-${l.href}`} href={l.href} target="_blank" rel="noopener noreferrer">
              {l.label} ↗
            </a>
          ))}
        </div>
      )}
      {round.reportSlug && (
        <Link href={`/reviews/${round.reportSlug}`} className="review-report-link">
          Full report →
        </Link>
      )}
    </article>
  );
}
