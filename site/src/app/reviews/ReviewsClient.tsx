"use client";

import Link from "next/link";
import { useCallback, useMemo } from "react";
import { useSearchParams } from "next/navigation";
import {
  sortedReviewRounds,
  PAPER_IDS,
  type PaperId,
  type ReviewRound,
  type ReviewRoundKind,
} from "@/data/reviewTimeline";
import {
  VerdictTrajectory,
  VerdictLegend,
  GapClosureChart,
  GapPerPaperDeltas,
  SkillsGrowthChart,
  ReadinessStrip,
} from "./ProgressViz";

const KIND_LABEL: Record<ReviewRoundKind, string> = {
  "external-browser": "EXTERNAL",
  "internal-api": "INTERNAL",
  "internal-cc": "INTERNAL",
  "skill-improvement": "SKILL-UPGRADE",
  "closure-wave": "CLOSURES",
};

/** Filterable kind groups (internal-api + internal-cc collapse into INTERNAL). */
const KIND_GROUPS = ["EXTERNAL", "INTERNAL", "SKILL-UPGRADE", "CLOSURES"] as const;
type KindGroup = (typeof KIND_GROUPS)[number];

function kindGroupOf(kind: ReviewRoundKind): KindGroup {
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

function parseList<T extends string>(raw: string | null, valid: readonly T[]): T[] {
  if (!raw) return [];
  const set = new Set(valid);
  return raw
    .split(",")
    .map((s) => s.trim().toUpperCase() as T)
    .filter((s) => set.has(s));
}

export default function ReviewsClient() {
  const searchParams = useSearchParams();
  const selectedPapers = useMemo(
    () => parseList<PaperId>(searchParams.get("papers"), PAPER_IDS),
    [searchParams],
  );
  const selectedKinds = useMemo(
    () => parseList<KindGroup>(searchParams.get("kinds"), KIND_GROUPS),
    [searchParams],
  );

  const setParams = useCallback(
    (papers: PaperId[], kinds: KindGroup[]) => {
      const params = new URLSearchParams(window.location.search);
      if (papers.length > 0) params.set("papers", papers.join(","));
      else params.delete("papers");
      if (kinds.length > 0) params.set("kinds", kinds.join(","));
      else params.delete("kinds");
      const qs = params.toString();
      window.history.replaceState(null, "", qs ? `?${qs}` : window.location.pathname);
    },
    [],
  );

  const togglePaper = (p: PaperId) => {
    const next = selectedPapers.includes(p)
      ? selectedPapers.filter((x) => x !== p)
      : [...selectedPapers, p];
    setParams(next, selectedKinds);
  };

  const toggleKind = (k: KindGroup) => {
    const next = selectedKinds.includes(k)
      ? selectedKinds.filter((x) => x !== k)
      : [...selectedKinds, k];
    setParams(selectedPapers, next);
  };

  const rounds = useMemo(() => sortedReviewRounds(), []);
  const filtered = rounds.filter((r) => {
    if (selectedPapers.length > 0 && !r.papers.some((p) => selectedPapers.includes(p))) return false;
    if (selectedKinds.length > 0 && !selectedKinds.includes(kindGroupOf(r.kind))) return false;
    return true;
  });

  const hasFilter = selectedPapers.length > 0 || selectedKinds.length > 0;

  return (
    <>
      {/* ── Progress section ─────────────────────────────────────────── */}
      <details className="progress-panel" open>
        <summary className="progress-summary">Progress</summary>
        <div className="progress-body">
          <ReadinessStrip />
          <div className="progress-block">
            <h3 className="progress-block-title">External referee verdicts — convergence toward ACCEPT</h3>
            <p className="progress-block-sub">
              Six papers × two browser-tier rounds × three frontier referees (same chat threads,
              delta-prompts between rounds). 10 of 18 verdicts improved EXT1 → EXT2.
            </p>
            <VerdictTrajectory />
            <VerdictLegend />
          </div>
          <div className="progress-charts">
            <div className="progress-block">
              <h3 className="progress-block-title">Internal/external gap — findings only the external tier caught</h3>
              <p className="progress-block-sub">
                Substantive externally-caught findings that survived every internal round. The loop
                exits at zero.
              </p>
              <GapClosureChart />
              <GapPerPaperDeltas />
            </div>
            <div className="progress-block">
              <h3 className="progress-block-title">Skills stack — the review machinery self-improving</h3>
              <p className="progress-block-sub">
                Every external miss is mined into the pattern catalog and the reviewer prompts, then
                validated against the pre-closure snapshot before it counts.
              </p>
              <SkillsGrowthChart />
            </div>
          </div>
        </div>
      </details>

      {/* ── Filters ──────────────────────────────────────────────────── */}
      <div className="review-filters" role="group" aria-label="Filter the review feed">
        <div className="review-filter-row">
          <span className="review-filter-label">papers</span>
          {PAPER_IDS.map((p) => (
            <button
              key={p}
              type="button"
              className={selectedPapers.includes(p) ? "filter-chip is-active" : "filter-chip"}
              aria-pressed={selectedPapers.includes(p)}
              onClick={() => togglePaper(p)}
            >
              {p}
            </button>
          ))}
        </div>
        <div className="review-filter-row">
          <span className="review-filter-label">kind</span>
          {KIND_GROUPS.map((k) => (
            <button
              key={k}
              type="button"
              className={selectedKinds.includes(k) ? "filter-chip is-active" : "filter-chip"}
              aria-pressed={selectedKinds.includes(k)}
              onClick={() => toggleKind(k)}
            >
              {k}
            </button>
          ))}
          {hasFilter && (
            <button type="button" className="filter-chip filter-clear" onClick={() => setParams([], [])}>
              clear
            </button>
          )}
        </div>
        <div className="review-filter-count">
          {filtered.length} of {rounds.length} rounds
        </div>
      </div>

      {/* ── Feed ─────────────────────────────────────────────────────── */}
      <div className="review-feed">
        {filtered.map((r) => (
          <Entry key={r.id} round={r} />
        ))}
        {filtered.length === 0 && (
          <p className="review-feed-empty">No rounds match the current filters.</p>
        )}
      </div>
    </>
  );
}
