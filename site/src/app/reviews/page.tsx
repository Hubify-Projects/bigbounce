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
        Every paper cycled through internal multi-vendor review rounds, then external
        browser-tier rounds against frontier web models, then a per-finding truth-audit,
        same-day fixes, and process upgrades mined from whatever only the external tier
        caught. Through mid-2026 the program ran 20+ rounds, including a de-biased external
        validation (severity-steering struck from referee prompts) and a final 3-round
        INT+EXT grind (Rounds A/B/C, Jun 28–30 2026). 23 real findings were closed across
        those three rounds; a neutral gate-discipline truth-audit found 0 new genuine items.
        External verdicts are now MINOR-dominant with occasional ACCEPTs — not uniformly
        all-ACCEPT. Residual MAJORs reflect disclosed caveats, submission-time blockers
        (Zenodo DOI / arXiv IDs mintable only at submission), and frontier-LLM run-to-run
        variance — not unaddressed quality issues. The papers are internally verified honest
        and publishable-strong. This feed is a permanent record of the program.
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
              Six papers × 20+ browser-tier rounds × three frontier referees (ChatGPT, Grok,
              Gemini) through a de-biased external validation and a final 3-round INT+EXT
              grind (Rounds A/B/C, Jun 28–30 2026). Current profile: MINOR-dominant with
              occasional ACCEPTs — e.g. P5 Gemini at ACCEPT, others at MINOR or isolated
              MAJOR. Residual MAJORs are disclosed caveats, submission-gated blockers (arXiv
              IDs / Zenodo DOIs mintable only at submission), and LLM run-to-run noise — not
              unaddressed science issues. All-3-ACCEPT-zero-MINOR is an asymptote against
              noisy frontier referees; the papers are internally verified publishable-strong.
            </p>
            <div className="verdict-carousel">
              <VerdictTrajectory />
            </div>
            <VerdictLegend />
          </div>
          <div className="progress-charts">
            <div className="progress-block">
              <h3 className="progress-block-title">Internal/external gap — findings only the external tier caught</h3>
              <p className="progress-block-sub">
                Substantive externally-caught findings that survived every internal round. The gap
                closed to zero by EXT20; the 2026-06-28 de-biased referee prompt then surfaced 2 genuine
                self-favoring items (since fixed), and the final 3-round grind (A/B/C) closed with 0 genuinely-new findings.
              </p>
              <GapClosureChart />
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
                An independent audit of the review loop verified convergence GENUINE on substance (HIGH ~90%); identified a mild self-favoring bias
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
              <SkillsGrowthChart />
            </div>
          </div>
        </div>
      </details>

      {/* ── Campaign observations ─────────────────────────────────────── */}
      <div className="campaign-obs-panel">
        <h2 className="campaign-obs-heading">Campaign observations</h2>
        <p className="campaign-obs-lede">
          The program ran 20+ internal + external rounds, then a de-biased external validation (2026-06-28, severity-steering struck from the referee prompt) and a final 3-round INT+EXT grind (Round A/B/C, Jun 28–30 2026). 23 real items were closed across the 3 rounds; a neutral gate-discipline truth-audit found 0 genuinely-new real findings. External verdicts are MINOR-dominant with occasional ACCEPTs — not uniformly all-ACCEPT.
        </p>
        <ul className="campaign-obs-list">
          <li>
            <strong>Run-to-run variance is the headline:</strong> the <em>same</em> papers swung MINOR-dominant (Round B EXT) → MAJOR-dominant (Round C EXT) while getting slightly <em>better</em>, not worse — frontier fast-tier referees carry large run-to-run noise, so any single sweep's verdict tally is not a stable quality signal.
          </li>
          <li>
            <strong>Grok — harsh outlier (pattern-064):</strong> its REJECT/MAJOR verdicts truth-audit as false positives (future-date FPs, companion-reliance, disclosed-caveat-as-defect); it softened to MINOR on several papers after the round fixes landed.
          </li>
          <li>
            <strong>Gemini — most ACCEPTs:</strong> returned real ACCEPTs (P1A at Round A, P5 at Round C) but also swings to MAJOR run-to-run — high variance rather than a fixed bias.
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
                <td className="eta-td eta-td-label">Internal review (INT, multi-vendor API) — 3 rigorous rounds A/B/C</td>
                <td className="eta-td">✓ Complete (Jun 28–30 2026). 23 real items closed program-wide; final neutral truth-audit found 0 genuinely-new real findings.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">External review (de-biased browser, 3 sweeps + validation)</td>
                <td className="eta-td">MINOR-dominant verdicts with occasional ACCEPTs (e.g. P5 Gemini). Residual MAJORs = disclosed caveats + submission-time DOI/arXiv blockers + frontier-LLM run-to-run variance — not unaddressed quality. Verified internally honest.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Readiness</td>
                <td className="eta-td">96 (R-converged ceiling; final 1% = Houston sign-off, hard cap — never written here without it).</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Awaiting: Houston external-review sign-off → coordinated arXiv submission</td>
                <td className="eta-td">Pending Houston action. Submission mints the Zenodo DOIs / arXiv IDs that mechanically clear the last structural reviewer blocker.</td>
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
