/**
 * PublishEtaWidget — the honest "Submission-ready ETA" widget.
 *
 * Live from Convex readinessMetrics:computeEta (server-fetched, rebuilt on every
 * commit/push). Shows:
 *   - a prominent program submission-ready ETA (the loop's own convergence clock)
 *   - per-paper chips: clean-wave streak 0/1/2 + open-items counts
 *   - the two-clock honesty note: journal ACCEPTANCE depends on human referees
 *     (months, external) — a separate clock from the loop's.
 *
 * The ETA is the loop's "papers stop surfacing genuinely-new findings" clock,
 * NOT the journal-acceptance clock. The copy states its assumption explicitly.
 *
 * No nested boxes-in-boxes: one outer shell, then spacing + typography + a thin
 * divider. Server component — receives the ETA result as a prop.
 */
import Link from "next/link";
import type { EtaResult } from "@/lib/liveReadiness";
import { formatEtaHours } from "@/lib/liveReadiness";

const MONO = "var(--font-mono-stack)";

function streakColor(streak: number, target: number): string {
  if (streak >= target) return "var(--success)";
  if (streak >= 1) return "var(--warn)";
  return "var(--text-tertiary)";
}

export function PublishEtaWidget({
  eta,
  compact = false,
}: {
  eta: EtaResult | null;
  compact?: boolean;
}) {
  if (!eta) return null;
  const target = eta.targetCleanWaves;
  const programReady = eta.programEtaHours <= 0;

  return (
    <section
      aria-label="Submission-ready ETA"
      style={{
        border: "1px solid var(--border)",
        borderRadius: 10,
        padding: compact ? "16px 18px" : "20px 22px",
        background: "color-mix(in srgb, var(--bg) 55%, transparent)",
      }}
    >
      <div
        style={{
          display: "flex",
          alignItems: "baseline",
          justifyContent: "space-between",
          gap: 16,
          flexWrap: "wrap",
        }}
      >
        <div>
          <p
            style={{
              margin: 0,
              fontFamily: MONO,
              fontSize: "0.66rem",
              letterSpacing: "0.09em",
              textTransform: "uppercase",
              color: "var(--text-tertiary)",
            }}
          >
            Submission-ready ETA
          </p>
          <p
            style={{
              margin: "4px 0 0 0",
              fontFamily: MONO,
              fontWeight: 700,
              fontSize: compact ? "1.35rem" : "1.7rem",
              color: programReady ? "var(--success)" : "var(--text-primary)",
              lineHeight: 1.1,
            }}
          >
            {programReady ? "clean-wave bar met" : formatEtaHours(eta.programEtaHours)}
          </p>
        </div>
        <div style={{ textAlign: "right" }}>
          <p
            style={{
              margin: 0,
              fontFamily: MONO,
              fontSize: "0.72rem",
              color: "var(--text-secondary)",
            }}
          >
            {eta.papersConverged}/{eta.papersTotal} papers at the {target}-clean-wave bar
          </p>
          <p
            style={{
              margin: "2px 0 0 0",
              fontFamily: MONO,
              fontSize: "0.64rem",
              color: "var(--text-muted)",
            }}
          >
            median wave cadence ≈ {eta.medianWaveHours} h
          </p>
        </div>
      </div>

      {/* per-paper chips */}
      <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginTop: 14 }}>
        {eta.perPaper.map((p) => {
          const open = p.openComputeCount + p.openVenueCount;
          return (
            <span
              key={p.paperId}
              title={`${p.paperId}: clean-wave streak ${p.cleanWaveStreak}/${target}; ${
                p.converged ? "at the clean-wave bar" : `${p.remainingWaves} clean wave(s) to go (${formatEtaHours(p.etaHours)})`
              }. Last wave ${p.lastWaveLabel} (${p.lastDateISO}), genuinely-new findings: ${p.lastWaveGenuinelyNew}.${
                open ? ` Open items: ${p.openComputeCount} compute / ${p.openVenueCount} venue.` : ""
              }`}
              style={{
                fontFamily: MONO,
                fontSize: "0.66rem",
                padding: "3px 8px",
                border: "1px solid var(--border)",
                borderRadius: 5,
                color: "var(--text-secondary)",
                display: "inline-flex",
                alignItems: "center",
                gap: 6,
              }}
            >
              <span style={{ color: "var(--text-tertiary)" }}>{p.paperId}</span>
              <span style={{ color: streakColor(p.cleanWaveStreak, target) }}>
                {"◆".repeat(Math.min(p.cleanWaveStreak, target))}
                {"◇".repeat(Math.max(0, target - p.cleanWaveStreak))}
              </span>
              {open > 0 ? (
                <span style={{ color: "var(--warn)" }}>{open} open</span>
              ) : null}
            </span>
          );
        })}
      </div>

      {/* two-clock honesty note */}
      <div
        style={{
          marginTop: 14,
          paddingTop: 12,
          borderTop: "1px solid var(--border)",
        }}
      >
        <p
          style={{
            margin: 0,
            fontSize: "0.7rem",
            lineHeight: 1.55,
            color: "var(--text-muted)",
            maxWidth: "70ch",
          }}
        >
          <strong style={{ color: "var(--text-secondary)" }}>Two clocks.</strong>{" "}
          This ETA is the <em>review-loop</em> clock — time until each paper stops surfacing
          genuinely-new findings ({target} consecutive clean review waves). It assumes 0 new
          findings from here; a single genuinely-new finding on any paper resets that paper&apos;s
          streak and pushes the ETA out. <strong style={{ color: "var(--text-secondary)" }}>Journal
          acceptance is a separate, external clock</strong> — it depends on human referees and
          takes months. This widget does not predict that.{" "}
          {!compact && (
            <Link href="/reviews" style={{ color: "var(--accent-link)" }}>
              See the verdict trajectory →
            </Link>
          )}
        </p>
      </div>
    </section>
  );
}
