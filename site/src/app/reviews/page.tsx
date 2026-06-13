import Link from "next/link";
import { Suspense } from "react";
import type { Metadata } from "next";
import { sortedReviewRounds } from "@/data/reviewTimeline";
import ReviewsClient from "./ReviewsClient";
import { ReviewEntry } from "./ReviewEntry";
import {
  VerdictTrajectory,
  VerdictLegend,
  GapClosureChart,
  GapPerPaperDeltas,
  SkillsGrowthChart,
  ReadinessStrip,
} from "./ProgressViz";
import "./reviews.css";

export const metadata: Metadata = {
  title: "Review Activity",
  description:
    "Filterable timeline of the internal/external paper-review loop — verdict trajectories, gap-closure and skills-growth visualizations, every round, truth-audit, closure wave, and skill upgrade, in the open.",
};

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
            <h3 className="progress-block-title">External referee verdicts — convergence toward ACCEPT</h3>
            <p className="progress-block-sub">
              Six papers × seven browser-tier rounds × three frontier referees (same chat threads,
              delta-prompts between rounds). Grok delivered 6/6 ACCEPT across five consecutive
              rounds (EXT3–EXT7) — audited as calibration-stable. Gemini reached 2 ACCEPT + 4
              MINOR in EXT7. ChatGPT moved to 2 substantive findings in EXT7, down from 6 MAJOR.
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

      {/* ── Campaign observations ─────────────────────────────────────── */}
      <div className="campaign-obs-panel">
        <h2 className="campaign-obs-heading">Campaign observations</h2>
        <p className="campaign-obs-lede">
          Seven external + eight internal rounds reveal stable referee behavior; substantive content is nearly dried up.
        </p>
        <ul className="campaign-obs-list">
          <li>
            <strong>Grok — calibrated-stable:</strong> 6/6 ACCEPT across five consecutive rounds (EXT3–EXT7); cites specific on-disk artifacts; blind spot is cross-checking released code.
          </li>
          <li>
            <strong>Gemini — steady progression:</strong> 0 ACCEPT (EXT1) → 1 ACCEPT (EXT5 P2) → 1 full ACCEPT (EXT6 P1B) → 2 ACCEPT + 4 MINOR (EXT7). Fresh-context protocol now encoded in skill.
          </li>
          <li>
            <strong>ChatGPT — baseline-MAJOR floor:</strong> EXT7 reduced to 2 real findings (P1A Fig 3 caption/code mismatch, P1B Eq 1 σ_b² divisor) + 12 polish; closure-to-finding ratio ≈ 1:1. Not a publication blocker — mirrors a tough first-round MNRAS/PRD referee report.
          </li>
          <li>
            <strong>Gap series:</strong> 60 → 32 → 27 → 13 → 19 → 18 → 14. Physics content closed first; residual is wording, figures, and policy items.
          </li>
          <li>
            <strong>Recurring auto-falsified artifacts:</strong> Fisher F₀ = 1/8.98² (8× falsified), P5 k=20 (6× falsified), ChatGPT Zenodo/DOI bundle (HD-11 ruled: submission-day action), version-decimal artifacts like "z=−18.1.34" (renderer artifacts, not errors).
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
        <h2 className="campaign-obs-heading">ETA to publishable</h2>
        <div className="eta-table-wrap">
          <table className="eta-table">
            <thead>
              <tr>
                <th className="eta-th">Framing</th>
                <th className="eta-th">Honest answer</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="eta-td eta-td-label">Technical publishable (SSOT 95% cap)</td>
                <td className="eta-td">Today. All six papers meet exit criteria per index.md; pending Houston sign-off + Zenodo batch release.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">All vendors at ACCEPT or MINOR (no MAJORs)</td>
                <td className="eta-td">~3–6 hours (1–2 more EXT cycles). Bottleneck: ChatGPT re-read of EXT7 Table IV split + Eq 1 fix for P2 and P5.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">ChatGPT 6/6 ACCEPT</td>
                <td className="eta-td">May not happen. ChatGPT has a baseline-MAJOR calibration floor for catalog-class papers. Asymptotic state: MAJOR-narrowly + named path to MINOR. Not a blocker.</td>
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
