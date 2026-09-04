import type { Metadata } from "next";
import Link from "next/link";
import {
  getLivePapers,
  getRunningPods,
  displayVersion,
  type LivePaperState,
} from "@/lib/livePapers";
import { getPaperBySlug } from "@/data/papers";
import { readinessBreakdown, readinessBreakdownNote, publishingPhase } from "@/data/readinessBreakdown";
import { SurveyQcTable } from "@/components/Cards/SurveyQcTable";
import {
  Band,
  PageHeader,
  StatRow,
  DataTable,
  ReadinessBar,
  EvidenceChip,
} from "@/components/primitives";

export const metadata: Metadata = {
  title: "Research Status",
  description: "Current research-program, artifact, and editorial status for BigBounce.",
};

export const dynamic = "force-static";

const BUILD_NOW = Date.now();
const STALE_DAYS = 30;

function taglineFor(slug: string, rolePrefix?: string): string {
  const plainTitle = getPaperBySlug(slug)?.plainTitle ?? "";
  return rolePrefix ? `${rolePrefix} · ${plainTitle}` : plainTitle;
}

const PAPER_DISPLAY: Record<string, { number: string; tagline: string }> = {
  "paper-1a": { number: "P1A", tagline: taglineFor("paper-1a") },
  "paper-1b": { number: "P1B", tagline: taglineFor("paper-1b") },
  "paper-2": { number: "P2", tagline: taglineFor("paper-2") },
  "paper-3": { number: "P3", tagline: taglineFor("paper-3", "Integrated Supporting Data Release") },
  "paper-4": { number: "P4", tagline: taglineFor("paper-4") },
  "paper-5": { number: "P5", tagline: taglineFor("paper-5", "Standalone AJ companion") },
};

function findingsLabel(p: LivePaperState): string {
  if (p.openBlockers > 0) return `${p.openBlockers} blocker${p.openBlockers === 1 ? "" : "s"}`;
  if (p.openMajors > 0) return `${p.openMajors} major${p.openMajors === 1 ? "" : "s"}`;
  if (p.openMinors > 0) return `${p.openMinors} minor${p.openMinors === 1 ? "" : "s"}`;
  return "none recorded open";
}

function daysAgo(iso: string | null): number | null {
  if (!iso) return null;
  const d = new Date(iso).getTime();
  if (Number.isNaN(d)) return null;
  return Math.floor((BUILD_NOW - d) / 86_400_000);
}

export default async function StatusPage() {
  const [livePapers, runningPods] = await Promise.all([getLivePapers(), getRunningPods()]);
  const isLive = livePapers.length > 0 && livePapers[0].source === "convex";

  const totalOpenBlockers = livePapers.reduce((s, p) => s + p.openBlockers, 0);
  const totalOpenMajors = livePapers.reduce((s, p) => s + p.openMajors, 0);
  const noMajorCount = livePapers.filter((p) => p.openBlockers === 0 && p.openMajors === 0).length;
  const avgReadiness =
    livePapers.length > 0
      ? Math.round(livePapers.reduce((s, p) => s + p.readinessComputed, 0) / livePapers.length)
      : 0;

  return (
    <>
      <Band>
        <PageHeader
          eyebrow={isLive ? "Live portfolio status" : "Static fallback"}
          title="Research program status"
          lead="One honest picture of where every work stands. Dates below are real last-update dates — a two-month-old date is a backlog signal, not a display bug."
          actions={[
            { label: "Review evidence →", href: "/reviews" },
            { label: "Activity feed →", href: "/activity" },
            { label: "Publishing phase →", href: "/publish" },
          ]}
        />
        <StatRow
          items={[
            { value: `${noMajorCount}/${livePapers.length}`, label: "no open blocker/major" },
            { value: `${avgReadiness}%`, label: "avg readiness" },
            { value: totalOpenBlockers, label: "open blockers" },
            { value: totalOpenMajors, label: "open majors" },
          ]}
        />
      </Band>

      <Band tone="alt" width="full" id="table">
        <div style={{ maxWidth: "var(--content-width)", margin: "0 auto", padding: "0 24px" }}>
          <DataTable
            rows={livePapers}
            rowKey={(p) => p.slug}
            columns={[
              {
                key: "work",
                header: "Work",
                render: (p) => {
                  const meta = PAPER_DISPLAY[p.slug] ?? { number: p.number, tagline: p.shortTitle };
                  return (
                    <>
                      <Link href={`/papers/${p.slug}`}>{meta.number}</Link>{" "}
                      <span className="row-purpose">{meta.tagline}</span>
                    </>
                  );
                },
              },
              { key: "version", header: "Version", mono: true, render: (p) => displayVersion(p.currentVersion) },
              {
                key: "readiness",
                header: "Readiness",
                render: (p) => <ReadinessBar value={p.readinessComputed} />,
              },
              { key: "findings", header: "Open findings", mono: true, render: (p) => findingsLabel(p) },
              {
                key: "updated",
                header: "Last update",
                mono: true,
                render: (p) => {
                  const age = daysAgo(p.lastUpdated);
                  return (
                    <>
                      {p.lastUpdated ?? "—"}
                      {age !== null && age > STALE_DAYS && (
                        <span className="stale-note">stale · no change {age}d</span>
                      )}
                    </>
                  );
                },
              },
              {
                key: "publishing",
                header: "Publishing",
                render: (p) => (
                  <EvidenceChip grade={p.houstonSignOff ? "measured" : "open"} label={p.houstonSignOff ? "signed off" : "in progress"} />
                ),
              },
            ]}
          />
          <p className="row-purpose" style={{ marginTop: 12 }}>
            Readiness follows directive P (2026-07-23): the headline % is package and review
            evidence, not a scientific endorsement, standalone-submission decision, or journal
            acceptance. P3 is an integrated Supporting Data Release; P5 is the standalone AJ
            companion. Readiness is Convex-sourced only — never hand-edited here.
          </p>
        </div>
      </Band>

      <Band id="signoff">
        <PageHeader
          eyebrow="Final review · directive P"
          title="What &ldquo;ready&rdquo; means — five gates per work"
          lead={readinessBreakdownNote}
        />
        {readinessBreakdown.map((p) => {
          const paper = getPaperBySlug(
            Object.keys(PAPER_DISPLAY).find((slug) => PAPER_DISPLAY[slug].number === p.code) ?? "",
          );
          const pdf = paper?.artifacts.find((a) => a.kind === "primary" && a.href.endsWith(".pdf"));
          return (
            <div key={p.code} className="widget-row">
              <div style={{ display: "flex", alignItems: "baseline", gap: 12, flexWrap: "wrap" }}>
                <span className="row-title mono">{p.code}</span>
                <ReadinessBar value={p.publicationReadiness} />
                {pdf && (
                  <a className="page-header-action" href={pdf.href} target="_blank" rel="noreferrer">
                    Open exact PDF ↗
                  </a>
                )}
              </div>
              <div className="readiness-bar-segments mono" style={{ marginTop: 8 }}>
                {p.gates.map((g) => (
                  <span key={g.dimension} className="readiness-bar-segment" title={g.status}>
                    {g.dimension} {g.score}% (×{g.weight}) — {g.owner === "done" ? "complete" : g.owner}
                  </span>
                ))}
              </div>
            </div>
          );
        })}
        <p className="row-purpose" style={{ marginTop: 16 }}>
          Publishing-phase next steps (endorsement, Zenodo, submission) are tracked separately at{" "}
          <Link href="/publish">/publish</Link> and never subtract from the readiness score above.
        </p>
        <div className="readiness-bar-segments mono" style={{ marginTop: 10 }}>
          {publishingPhase.map((s) => (
            <span key={s.step} className="readiness-bar-segment" title={s.status}>
              {s.step} — {s.owner}
            </span>
          ))}
        </div>
      </Band>

      <Band tone="alt">
        <PageHeader eyebrow="Compute" title="Active compute" />
        {runningPods.length === 0 ? (
          <p className="row-purpose">0 pods running · $0/hr. All compute jobs idle.</p>
        ) : (
          <StatRow
            items={runningPods.map((pod) => ({
              value: `$${pod.hourlyCostUsd.toFixed(2)}/hr`,
              label: `${pod.name} · ${pod.gpu}`,
            }))}
          />
        )}
      </Band>

      <Band id="surveys">
        <PageHeader
          eyebrow="Legacy survey-pipeline records"
          title="Survey QC"
          lead="Preserved methodology and archive records. Historic candidate counts are superseded by the current portfolio; no survey result here proves a bounce."
        />
        <SurveyQcTable />
      </Band>
    </>
  );
}
