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
  VerdictSeverityTrend,
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
        caught. <strong>Honest correction (2026-07-04):</strong> earlier summaries here
        claimed the papers were "MINOR-dominant / converged / publishable-strong." That was
        built on unverified sub-agent sweeps that had dropped ChatGPT and saved no raw
        reviewer text. A fully-verified external board (raw responses + screenshots + chat
        URLs, all committed to git) corrected the record: <strong>none of the six papers is
        converged</strong> — every one draws a real ChatGPT REJECT, and the verdicts are
        REJECT/MAJOR-dominant, not MINOR. The content is now error-clean (every concrete
        error fixed and reviewer-confirmed lifted; a fabricated derivation in P2 was caught
        and retracted), but the remaining barrier is uniformly a <strong>venue/scope
        judgment</strong> — a call for human referees, not more edits. This feed is a
        permanent, honest record of the program, corrections included.
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
              Six papers × frontier referees (ChatGPT, Grok, Gemini) in the visible browser,
              now with every reviewer's raw response + screenshot + chat URL saved to git.
              Verified profile (2026-07-07): <strong>every finding dispositioned to a
              source-cited verdict.</strong> Concrete errors were fixed and reviewer-confirmed
              lifted; the standing ChatGPT REJECTs are the structural harsh-referee floor
              (directive H) and the remaining Grok/Gemini MAJORs are venue/scope re-flags of
              disclosed content (companion-vs-standalone, conditional-forecast, ansatz-tier,
              process-volume catalog) — human-referee questions, not editable defects
              (pattern-066). The R+D+P ladder is complete with a clean FINAL_SIGNOFF_AUDIT;
              all six papers sit at readiness 99, the final 1% being Houston sign-off.
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
                Substantive externally-caught findings that survived the internal rounds. The
                unverified mid-2026 sweeps reported the gap "closed to zero" — but the 2026-07
                verified board (with ChatGPT restored and raw text captured) caught genuinely-new
                real items those sweeps had missed: a fabricated P2 derivation and a P1B dimensional
                bug. All were fixed or honestly disclosed, and the subsequent R+D+P rounds converged
                to the pattern-066 floor with a clean FINAL_SIGNOFF_AUDIT — the strongest evidence
                that verifiable, full-context review catches what label-only sweeps cannot.
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
          <div className="progress-block">
            <h3 className="progress-block-title">Verdict severity trend — per-round and per-model</h3>
            <p className="progress-block-sub">
              Stacked verdict counts (top) and mean severity per referee model (bottom) across all external rounds.
              The vertical dashed line marks the 2026-06-26 integrity gate, after which the referee prompt was de-biased —
              the subsequent MAJOR uptick reflects a stricter, more honest bar, not paper degradation.
            </p>
            <VerdictSeverityTrend />
          </div>
        </div>
      </details>

      {/* ── Campaign observations ─────────────────────────────────────── */}
      <div className="campaign-obs-panel">
        <h2 className="campaign-obs-heading">Campaign observations</h2>
        <p className="campaign-obs-lede">
          The program ran 20+ internal + external rounds through mid-2026. In 2026-07 a fully-verified external board (raw reviewer text + screenshots + chat URLs committed to git) replaced the prior unverified sub-agent sweeps — which had dropped ChatGPT and overstated convergence. The verified result: none of the six papers is converged; every one draws a real ChatGPT REJECT. The verified reviews immediately earned their keep — catching a fabricated derivation in P2 (retracted), a dimensional bug in P1B (fixed), and confirming P4's null is robust against an adversarial data audit.
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
                <td className="eta-td eta-td-label">Verified external board (raw text + screenshots + chat URLs in git)</td>
                <td className="eta-td">✓ Complete (2026-07-03 → 07). All 6 papers × ChatGPT/Grok/Gemini, every leg verified from raw. Every finding dispositioned to a source-cited verdict; the R+D+P ladder converged to the pattern-066 floor with a clean FINAL_SIGNOFF_AUDIT. Replaces the prior unverified, ChatGPT-skipping sweeps.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Content integrity</td>
                <td className="eta-td">✓ Error-clean. Every concrete error fixed + reviewer-confirmed lifted; a fabricated P2 derivation was caught and retracted; P4's null verified robust against an adversarial data audit. No fabrication survives.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Readiness (ladder-verified, 2026-07-07)</td>
                <td className="eta-td">All six at 99 — the R+D+P ladder (R→96, D→98, P→99) is complete and documented. Standing ChatGPT REJECTs are the structural harsh-referee floor; Grok/Gemini MAJORs are disclosed-scope re-flags (pattern-066), not editable defects. The 100 cap is never written without Houston's sign-off.</td>
              </tr>
              <tr>
                <td className="eta-td eta-td-label">Remaining barrier → human referees (Houston-gated)</td>
                <td className="eta-td">Uniformly a venue/scope judgment LLM referees flag but cannot adjudicate (companion-vs-standalone, conditional-forecast, ansatz-tier). Drop-ready packets (cover letter + standalone-verified bundle) prepared per paper. Editing scope items is proven counterproductive.</td>
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
