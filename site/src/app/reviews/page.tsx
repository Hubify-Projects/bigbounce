import Link from "next/link";
import { Suspense } from "react";
import type { Metadata } from "next";
import { sortedReviewRounds } from "@/data/reviewTimeline";
import ReviewsClient from "./ReviewsClient";
import { ReviewEntry } from "./ReviewEntry";
import {
  VerdictTrajectory,
  AllAMeter,
  VerdictLegend,
  GapClosureChart,
  GapPerPaperDeltas,
  SkillsGrowthChart,
  ReadinessStrip,
  VerdictSeverityTrend,
} from "./ProgressViz";
import { VerdictTrajectoryChart } from "./VerdictTrajectoryChart";
import { ChartShell } from "./ChartShell";
import { PublishEtaWidget } from "@/components/PublishEtaWidget";
import { getReadinessWaves, getRigorEvents, getPublishEta } from "@/lib/liveReadiness";
import "./reviews.css";

// Live data updates on every commit/push (Vercel rebuild) + Convex subscription.
export const revalidate = 60;

export const metadata: Metadata = {
  title: "Review Activity",
  description:
    "Filterable timeline of the internal/external paper-review loop — verdict trajectories, gap-closure and skills-growth visualizations, every round, truth-audit, closure wave, and skill upgrade, in the open.",
};

export default async function ReviewsPage() {
  const rounds = sortedReviewRounds();
  const [waveRows, rigorEvents, eta] = await Promise.all([
    getReadinessWaves(),
    getRigorEvents(),
    getPublishEta(),
  ]);
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
        This feed preserves internal and external automated-review rounds, raw evidence,
        per-finding truth audits, and subsequent closures. It is a review history, not a
        journal decision. <strong>Current status (2026-07-15): all six papers remain IN
        REVISION.</strong> The canonical readiness caps are P1A 62, P1B 56, P2 74, P3 56,
        P4 80, and P5 74. P1B v1B.0.108 and P4 v1.0.244 include closure changes that have
        not yet been re-reviewed. Automated ACCEPT labels are retained exactly as returned,
        but they are not journal acceptance. Independent human review, immutable
        archive/DOI work, and venue-specific checks remain open gates.
      </p>
      <div
        style={{
          fontFamily: "var(--font-mono-stack)",
          fontSize: "0.72rem",
          color: "var(--text-muted)",
          margin: "0 0 8px 0",
        }}
      >
        internal rounds → external browser rounds → truth-audit → fixes →
        internal-skill upgrades → repeat
      </div>
      <p
        style={{
          fontFamily: "var(--font-mono-stack)",
          fontSize: "0.72rem",
          color: "var(--text-muted)",
          margin: "0 0 24px 0",
        }}
      >
        Raw machine events (version bumps, R-round dispatches, pod lifecycle) stream at{" "}
        <Link href="/activity" style={{ color: "var(--accent-link)" }}>
          /activity
        </Link>
        .
      </p>

      {/* ── Progress section (server-rendered) ───────────────────────── */}
      <details className="progress-panel" open>
        <summary className="progress-summary">Progress</summary>
        <div className="progress-body">
          <ReadinessStrip />
          <div className="progress-block">
            <h3 className="progress-block-title">Automated-verdict trajectory — every recorded paper × reviewer leg</h3>
            <p className="progress-block-sub">
              Each review wave (internal API + external browser) plotted on the verdict scale
              (REJECT → MAJOR → MINOR → ACCEPT; higher is better). Thin lines are per-paper
              averages (toggle by paper); the bold line is the program average. FAILED reviewer
              legs are shown as gaps, never zeros. Vertical ⚑ markers flag documented changes in
              review rigor (de-biased prompt, integrity gate, verified-review reset, directive J).
              Every point is a recorded automated verdict; none is presented as a journal decision.
            </p>
            <VerdictTrajectoryChart rows={waveRows} rigorEvents={rigorEvents} />
          </div>
          <div className="progress-block">
            <h3 className="progress-block-title">External automated-review evidence</h3>
            <p className="progress-block-sub">
              The matrices below preserve the historical automated-model labels and their raw
              provenance. They are useful diagnostics, not an acceptance scoreboard. The current
              canonical board is P1A v1A.0.123/62, P1B v1B.0.108/56, P2 v1.7.122/74,
              P3 v3.2.0-r8/56, P4 v1.0.244/80, and P5 v0.1.133-2026-07-14/74; all are IN
              REVISION. P1B v108 and P4 v244 have not been re-reviewed, so older verdict cells
              must not be read as verdicts on those PDFs.
            </p>
            <AllAMeter />
            <ChartShell title="External referee verdicts — every paper × reviewer per round">
              <div className="verdict-carousel">
                <VerdictTrajectory />
              </div>
            </ChartShell>
            <VerdictLegend />
          </div>
          <div className="progress-charts">
            <div className="progress-block">
              <h3 className="progress-block-title">Internal/external gap — findings only the external tier caught</h3>
              <p className="progress-block-sub">
                Substantive externally-caught findings that survived the internal rounds. The
                unverified mid-2026 sweeps reported the gap "closed to zero" — but the 2026-07
                verified board (with ChatGPT restored and raw text captured) caught genuinely-new
                real items those sweeps had missed: a fabricated P2 derivation and a P1B dimensional
                bug. Both were truth-audited and corrected. The lesson is procedural: full-context,
                receipt-backed review is more reliable than label-only sweeps, while any remaining
                scientific adequacy still requires independent human judgment.
              </p>
              <ChartShell title="Internal/external gap — externally-caught findings per round">
                <GapClosureChart />
              </ChartShell>
              <GapPerPaperDeltas />
              <p
                style={{
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: "0.69rem",
                  color: "var(--text-muted)",
                  marginTop: "10px",
                  maxWidth: "62ch",
                  lineHeight: 1.55,
                  borderLeft: "2px solid var(--success)",
                  paddingLeft: "10px",
                  opacity: 0.88,
                }}
              >
                <span style={{ color: "var(--success)", fontWeight: 700 }}>⚑ 2026-06-26 — integrity gate.</span>{" "}
                An independent audit of the review loop found substantial closure evidence while also identifying a mild self-favoring bias
                (5/19 sampled dismissals rated OPINION when MINOR was more accurate); closed all 5 by making the papers
                <em> more conservative</em> — zero scientific conclusions changed. External referee prompt de-biased.
                R-round skills hardened: standing integrity-audit pre-check + PDF-hygiene md5 gate (pattern-062) now mandatory
                every round. Prompt-rules 23 → 24.
              </p>
            </div>
            <div className="progress-block">
              <h3 className="progress-block-title">Skills stack — the review machinery self-improving</h3>
              <p className="progress-block-sub">
                Every external miss is mined into the pattern catalog and the reviewer prompts, then
                validated against the pre-closure snapshot before it counts.
              </p>
              <ChartShell title="Skills stack — review patterns + reviewer-prompt rules">
                <SkillsGrowthChart />
              </ChartShell>
            </div>
          </div>
          <div className="progress-block">
            <h3 className="progress-block-title">Verdict severity trend — per-round and per-model</h3>
            <p className="progress-block-sub">
              Stacked verdict counts (top) and mean severity per referee model (bottom) across all external rounds.
              The vertical dashed line marks the 2026-06-26 integrity gate, after which the referee prompt was de-biased —
              the subsequent MAJOR uptick reflects a stricter, more honest bar, not paper degradation.
            </p>
            <ChartShell title="Verdict severity trend — per-round and per-model">
              <VerdictSeverityTrend />
            </ChartShell>
          </div>
        </div>
      </details>

      {/* ── Campaign observations ─────────────────────────────────────── */}
      <div className="campaign-obs-panel">
        <h2 className="campaign-obs-heading">Campaign observations</h2>
        <p className="campaign-obs-lede">
          The program ran 20+ internal and external automated-review rounds through mid-2026.
          Receipt-backed reviews replaced earlier label-only sweeps and exposed material issues,
          including a fabricated P2 derivation (retracted) and a P1B dimensional bug (fixed).
          Historical model labels vary substantially between runs; they are evidence for triage,
          not stable quality measurements or substitutes for human referees.
        </p>
        <ul className="campaign-obs-list">
          <li>
            <strong>Run-to-run variance is the headline:</strong> the <em>same</em> papers swung MINOR-dominant (Round B EXT) → MAJOR-dominant (Round C EXT) while getting slightly <em>better</em>, not worse — frontier fast-tier referees carry large run-to-run noise, so any single sweep's verdict tally is not a stable quality signal.
          </li>
          <li>
            <strong>Grok — harsh outlier (pattern-064):</strong> its REJECT/MAJOR verdicts truth-audit as false positives (future-date FPs, companion-reliance, disclosed-caveat-as-defect); it softened to MINOR on several papers after the round fixes landed.
          </li>
          <li>
            <strong>Gemini — highest automated ACCEPT-label count:</strong> returned ACCEPT labels for P1A at Round A and P5 at Round C, but also swung to MAJOR on later runs. These are model outputs, not journal decisions.
          </li>
          <li>
            <strong>ChatGPT — caught real items + re-flags:</strong> surfaced a genuine P4 self-favoring overstatement (the abstract's "robust across the full confidence-cut sweep") which was corrected, alongside re-flags of already-disclosed caveats.
          </li>
          <li>
            <strong>Recurring auto-falsified noise:</strong> future-date false-positives (June 2026 is the current date), PDF-raster math-extraction artifacts, an OpenAI leg <em>hallucinating</em> P1B robustness numbers that do not exist in the source, and the Zenodo DOI deferred-to-submission (normal pre-submission, not a defect).
          </li>
        </ul>
        <p className="campaign-obs-patterns">
          Patterns logged:{" "}
          <a className="campaign-obs-pattern-link" href="/project-context/review-patterns/pattern-009-gpt-fallback-low-rigor.md">pattern-009</a> (rubber-stamp audit),{" "}
          <a className="campaign-obs-pattern-link" href="/project-context/review-patterns/pattern-031-self-review-severity-underclassification.md">pattern-031</a> (caption/code mismatch),{" "}
          <a className="campaign-obs-pattern-link" href="/project-context/review-patterns/pattern-051-closure-introduced-regression.md">pattern-051</a> (closure-introduced regression),{" "}
          <a className="campaign-obs-pattern-link" href="/project-context/review-patterns/pattern-052-reraise-vindication.md">pattern-052</a> (re-raise vindication test).
        </p>
      </div>

      {/* ── ETA to publishable ───────────────────────────────────────────── */}
      <div className="eta-panel">
        <h2 className="campaign-obs-heading">Publication status</h2>
        {eta ? (
          <div style={{ margin: "0 0 20px 0" }}>
            <PublishEtaWidget eta={eta} />
          </div>
        ) : null}
        <div className="eta-table-wrap">
          <table className="eta-table">
            <thead>
              <tr>
                <th className="eta-th">Gate</th>
                <th className="eta-th">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="eta-td eta-td-label">Automated-review evidence</td>
                <td className="eta-td">Historical raw responses and provider receipts are retained. Coverage is version-specific: P1B v1B.0.108 and P4 v1.0.244 have not been re-reviewed. Automated labels do not establish journal acceptance.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Content integrity</td>
                <td className="eta-td">Known material findings were truth-audited and addressed, including retraction of the fabricated P2 derivation. This is not a claim that no undiscovered error remains; independent human review is still required.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Canonical readiness (2026-07-15)</td>
                <td className="eta-td">Evidence-capped average 67%: P1A 62 · P1B 56 · P2 74 · P3 56 · P4 80 · P5 74. All six remain IN REVISION; no automated score converts into journal acceptance.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Remaining publication gates</td>
                <td className="eta-td">Independent human scientific review, venue-specific formatting and scope checks, immutable archive/DOI completion, and author submission decisions. Any paper-specific open item remains governed by its SSOT record.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* ── Filters: client overlay over the server-rendered feed ──────── */}
      <Suspense fallback={<div className="review-filters" aria-busy="true" />}>
        <ReviewsClient totalRounds={rounds.length} />
      </Suspense>

      {/* ── Feed: SERVER-rendered — full round content in the static HTML.
            ReviewsClient only toggles visibility via data-papers/data-kind. ── */}
      <div className="review-feed" id="review-feed">
        {rounds.map((r) => (
          <ReviewEntry key={r.id} round={r} />
        ))}
        <p className="review-feed-empty" data-feed-empty hidden>
          No rounds match the current filters.
        </p>
      </div>
    </>
  );
}
