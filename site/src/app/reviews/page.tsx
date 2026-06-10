import Link from "next/link";
import type { Metadata } from "next";
import {
  sortedReviewRounds,
  type ReviewRound,
  type ReviewRoundKind,
} from "@/data/reviewTimeline";
import "./reviews.css";

export const metadata: Metadata = {
  title: "Review Activity",
  description:
    "Live timeline of the internal/external paper-review loop — every round, truth-audit, closure wave, and skill upgrade, in the open.",
};

const KIND_LABEL: Record<ReviewRoundKind, string> = {
  "external-browser": "EXTERNAL",
  "internal-api": "INTERNAL",
  "internal-cc": "INTERNAL",
  "skill-improvement": "SKILL-UPGRADE",
  "closure-wave": "CLOSURES",
};

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

function Entry({ round }: { round: ReviewRound }) {
  return (
    <article className="review-entry" aria-label={round.id}>
      <div className="review-entry-meta">
        <span className="review-timestamp">{round.dateISO}</span>
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
            <a
              key={`${l.label}-${l.href}`}
              href={l.href}
              target="_blank"
              rel="noopener noreferrer"
            >
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

export default function ReviewsPage() {
  const rounds = sortedReviewRounds();
  return (
    <>
      <p
        style={{
          fontFamily: "var(--font-mono-stack)",
          fontSize: "0.72rem",
          letterSpacing: "0.08em",
          textTransform: "uppercase",
          color: "var(--text-tertiary)",
          margin: "0 0 8px 0",
        }}
      >
        Review Activity
      </p>
      <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600, marginTop: 0 }}>
        The review loop, in the open
      </h1>
      <p
        style={{
          maxWidth: "72ch",
          fontSize: "0.9rem",
          color: "var(--text-muted)",
          lineHeight: 1.6,
          margin: "10px 0 6px 0",
        }}
      >
        Every paper cycles through internal multi-vendor review rounds, then external
        browser-tier rounds against frontier web models, then a per-finding truth-audit,
        same-day fixes, and upgrades to the internal review process mined from whatever
        only the external tier caught. The loop repeats until the internal/external gap
        hits zero — that is the publishable bar. This feed updates with every push.
      </p>
      <div
        style={{
          fontFamily: "var(--font-mono-stack)",
          fontSize: "0.72rem",
          color: "var(--text-muted)",
          margin: "0 0 28px 0",
        }}
      >
        internal rounds → external browser rounds → truth-audit → fixes →
        internal-skill upgrades → repeat
      </div>

      <div className="review-feed">
        {rounds.map((r) => (
          <Entry key={r.id} round={r} />
        ))}
      </div>
    </>
  );
}
