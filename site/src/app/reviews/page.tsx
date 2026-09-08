import Link from "next/link";
import type { Metadata } from "next";
import {
  sortedReviewRounds,
  externalVerdictRounds,
  PAPER_IDS,
  REVIEWERS,
} from "@/data/reviewTimeline";
import { papers } from "@/data/papers";
import { AllAMeter, GapClosureChart, GapPerPaperDeltas, SkillsGrowthChart } from "./ProgressViz";
import { ChartShell } from "./ChartShell";
import { PublicationStatusWidget } from "@/components/PublicationStatusWidget";
import { getPublicationStatus } from "@/lib/publicationStatus";
import { getLivePapers } from "@/lib/livePapers";
import {
  Band,
  PageHeader,
  VerdictGrid,
  TimelineList,
  type VerdictGridRow,
  type TimelineEntry,
} from "@/components/primitives";
import "./reviews.css";

export const revalidate = 60;

export const metadata: Metadata = {
  title: "Review Activity",
  description:
    "The internal/external multi-model review loop as a gate on publication readiness — verdict grid, publication status, round timeline, and skills growth.",
};

const boardBySlug = new Map(papers.map((p) => [p.slug, p]));
const cap = (slug: string) => boardBySlug.get(slug)?.readiness ?? 0;

const ROUNDS_SHOWN = 60;

function gridRows(): VerdictGridRow[] {
  const roundsDesc = [...externalVerdictRounds].reverse();
  return PAPER_IDS.map((p) => ({
    work: p,
    rounds: roundsDesc.map((r) => ({
      roundId: r.roundId,
      dateISO: r.dateISO,
      verdicts: r.verdicts[p],
    })),
  }));
}

function timelineEntries(): TimelineEntry[] {
  return sortedReviewRounds()
    .slice(0, ROUNDS_SHOWN)
    .map((r) => ({
      id: r.id,
      dateISO: r.dateISO,
      kind: r.kind.replace(/-/g, " "),
      title: r.title,
      href: r.reportSlug ? `/reviews/${r.reportSlug}` : r.links[0]?.href,
      quiet: r.kind === "skill-improvement",
    }));
}

export default async function ReviewsPage() {
  const [publicationStatus, livePapers] = await Promise.all([
    getPublicationStatus(),
    getLivePapers(),
  ]);

  return (
    <>
      <Band tone="base" width="content" open>
        <PageHeader
          eyebrow="Review activity"
          title="A gate on readiness, not a product"
          lead="Automated multi-model review is a gate on publication readiness, not a product. Rounds stop when the remaining findings are genre or venue (directives R2, P). Raw machine events (dispatches, closures) stream at /activity — this page is the curated review-loop story."
          actions={[{ label: "Raw activity feed →", href: "/activity" }]}
        />
      </Band>

      <Band tone="alt" width="wide" id="grid">
          <div className="band-head">
            <p className="eyebrow">Verdict grid &middot; newest round left</p>
            <h2 className="band-title">External referee verdicts</h2>
          </div>
          <p className="band-body" style={{ marginTop: 0 }}>
            Active legs only (directive M-AMENDED): Grok API + Gemini API, plotted against the
            historical six-paper board. The ChatGPT column is frozen while directive N&rsquo;s
            Codex/OpenAI pause stands — shown dimmed, never deleted or faked.
          </p>
          <AllAMeter />
          <VerdictGrid
            legLabels={[...REVIEWERS]}
            activeLegIndices={[1, 2]}
            frozenLegIndices={[0]}
            rows={gridRows()}
            maxRounds={10}
          />
          <p className="band-note">
            Historical board versions/caps: P1A {cap("paper-1a")}, P1B {cap("paper-1b")}, P2{" "}
            {cap("paper-2")}, P3 {cap("paper-3")}, P4 {cap("paper-4")}, P5 {cap("paper-5")}. The
            live-lineup works (A3, P4′, P1N) are not yet columns in this historical grid — their
            round-by-round evidence is in the timeline below and their readiness is on{" "}
            <Link href="/status">/status</Link>.
          </p>
      </Band>

      <Band tone="alt" width="content" id="publication-status" tight>
        <div className="band-head">
          <p className="eyebrow">Publication status</p>
          <h2 className="band-title">What&rsquo;s left before publication</h2>
        </div>
        <PublicationStatusWidget status={publicationStatus} livePapers={livePapers} />
      </Band>

      <Band tone="base" width="content">
          <div className="band-head">
            <p className="eyebrow">Gap and skills</p>
            <h2 className="band-title">The review machinery, self-improving</h2>
          </div>
          <p className="band-body" style={{ marginTop: 0 }}>
            Substantive findings only the external tier caught, and the pattern/prompt-rule
            catalog those findings get mined into.
          </p>
          <ChartShell title="Internal/external gap — externally-caught findings per round">
            <GapClosureChart />
          </ChartShell>
          <GapPerPaperDeltas />
          <ChartShell title="Skills stack — review patterns + reviewer-prompt rules">
            <SkillsGrowthChart />
          </ChartShell>
      </Band>

      <Band tone="base" width="content" id="timeline" tight close>
        <div className="band-head">
          <p className="eyebrow">{`Round timeline · newest first · showing ${ROUNDS_SHOWN}`}</p>
          <h2 className="band-title">Every round, truth-audit, closure, and skill upgrade</h2>
        </div>
        <p className="band-body" style={{ marginTop: 0, marginBottom: "var(--space-7)" }}>
          One line per event: date, kind, what changed, receipt link. Skill-improvement entries
          carry a quiet marker.
        </p>
        <TimelineList entries={timelineEntries()} />
        <p className="band-note">
          Full history (append-only, {sortedReviewRounds().length} rounds total) in{" "}
          <a href="https://github.com/Hubify-Projects/bigbounce/blob/main/site/src/data/reviewTimeline.ts">
            reviewTimeline.ts
          </a>
          .
        </p>
      </Band>
    </>
  );
}
