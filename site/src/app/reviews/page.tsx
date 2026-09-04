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
      <Band>
        <PageHeader
          eyebrow="Review activity"
          title="A gate on readiness, not a product"
          lead="Automated multi-model review is a gate on publication readiness, not a product. Rounds stop when the remaining findings are genre or venue (directives R2, P). Raw machine events (dispatches, closures) stream at /activity — this page is the curated review-loop story."
          actions={[{ label: "Raw activity feed →", href: "/activity" }]}
        />
      </Band>

      <Band tone="alt" width="full" id="grid">
        <div style={{ maxWidth: "var(--content-width)", margin: "0 auto", padding: "0 24px" }}>
          <PageHeader
            eyebrow="Verdict grid · newest round left"
            title="External referee verdicts"
            lead="Active legs only (directive M-AMENDED): Grok API + Gemini API, plotted against the historical six-paper board. The ChatGPT column is frozen while directive N's Codex/OpenAI pause stands — shown dimmed, never deleted or faked."
          />
          <AllAMeter />
          <VerdictGrid
            legLabels={[...REVIEWERS]}
            activeLegIndices={[1, 2]}
            frozenLegIndices={[0]}
            rows={gridRows()}
            maxRounds={10}
          />
          <p className="row-purpose" style={{ marginTop: 10 }}>
            Historical board versions/caps: P1A {cap("paper-1a")}, P1B {cap("paper-1b")}, P2{" "}
            {cap("paper-2")}, P3 {cap("paper-3")}, P4 {cap("paper-4")}, P5 {cap("paper-5")}. The
            live-lineup works (A3, P4′, P1N) are not yet columns in this historical grid — their
            round-by-round evidence is in the timeline below and their readiness is on{" "}
            <Link href="/status">/status</Link>.
          </p>
        </div>
      </Band>

      <Band id="publication-status">
        <PageHeader eyebrow="Publication status" title="What's left before publication" />
        <PublicationStatusWidget status={publicationStatus} livePapers={livePapers} />
      </Band>

      <Band tone="alt" width="full">
        <div style={{ maxWidth: "var(--content-width)", margin: "0 auto", padding: "0 24px" }}>
          <PageHeader
            eyebrow="Gap and skills"
            title="The review machinery, self-improving"
            lead="Substantive findings only the external tier caught, and the pattern/prompt-rule catalog those findings get mined into."
          />
          <ChartShell title="Internal/external gap — externally-caught findings per round">
            <GapClosureChart />
          </ChartShell>
          <GapPerPaperDeltas />
          <ChartShell title="Skills stack — review patterns + reviewer-prompt rules">
            <SkillsGrowthChart />
          </ChartShell>
        </div>
      </Band>

      <Band id="timeline">
        <PageHeader
          eyebrow={`Round timeline · newest first · showing ${ROUNDS_SHOWN}`}
          title="Every round, truth-audit, closure, and skill upgrade"
          lead="One line per event: date, kind, what changed, receipt link. Skill-improvement entries carry a quiet marker."
        />
        <TimelineList entries={timelineEntries()} />
        <p className="row-purpose" style={{ marginTop: 12 }}>
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
