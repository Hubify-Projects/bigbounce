"use client";

/**
 * VerdictTrajectoryChart — the honest verdict-trajectory chart (Houston 2026-07-10).
 *
 * X = review waves in chronological order (INT + EXT).
 * Y = verdict scale 0..3  (REJECT=0 · MAJOR=1 · MINOR=2 · ACCEPT=3) — HIGHER IS BETTER,
 *     so the average line should visibly climb REJECT/MAJOR → MINOR/ACCEPT over time.
 * Series: bold per-paper average (toggleable) + a bold program-average line.
 * FAILED legs are rendered as GAPS (line breaks), never zeros.
 * Rigor events are vertical annotation markers with labels (each cites a source).
 *
 * Two honest trend numbers (Houston 2026-07-10): the all-history delta spans the
 * Jul-4 verified-review reset where the pre-reset "high" scores were fabricated-era
 * reviews, so it can read negative and misleadingly. We therefore show:
 *   • "since last rigor event" (PRIMARY) — the honest, comparable window.
 *   • "all history (spans rigor resets)" (SECONDARY) — with a tooltip explaining
 *     why it can be negative.
 *
 * Inline view is DECLUTTERED: capped to the last INLINE_CAP waves, thinned x-labels,
 * prominent program-average line, and a note pointing at the full-page Expand view.
 * The expanded view (via ChartShell) shows every wave, every label, a larger plot,
 * horizontal scroll, working paper toggles, and full rigor-event labels.
 *
 * Dependency-free inline SVG, styled with the existing CSS vars (dark/light safe).
 * No verdict is invented — every point comes from a real recorded verdict row.
 */
import { useMemo, useState } from "react";
import type { WaveRow, RigorEvent } from "@/lib/liveReadiness";
import { ChartShell } from "./ChartShell";

const MONO = "var(--font-mono-stack)";
const AXIS = "var(--text-muted)";
const GRID = "var(--border)";

// How many most-recent waves the INLINE (non-expanded) view shows.
const INLINE_CAP = 15;

// Verdict → numeric scale (HIGHER = BETTER). "failed" → null (gap).
const SCORE: Record<string, number | null> = {
  reject: 0,
  "major-revisions": 1,
  "minor-revisions": 2,
  accept: 3,
  failed: null,
};
const Y_LABELS = ["REJECT", "MAJOR", "MINOR", "ACCEPT"];

const PAPER_ORDER = ["P1A", "P1B", "P2", "P3", "P4", "P5"];
const PAPER_COLOR: Record<string, string> = {
  P1A: "var(--model-chatgpt, #7c9cff)",
  P1B: "var(--model-grok, #ff8a5c)",
  P2: "var(--model-gemini, #8be0c0)",
  P3: "color-mix(in srgb, var(--warn) 60%, var(--accent))",
  P4: "var(--accent, #b28cff)",
  P5: "color-mix(in srgb, var(--success) 55%, var(--accent))",
};

type Wave = {
  label: string;
  dateISO: string;
  seq: number;
  paperMean: Record<string, number | null>;
  programMean: number | null;
};

function buildWaves(rows: WaveRow[]): Wave[] {
  const byWave = new Map<string, WaveRow[]>();
  for (const r of rows) {
    const arr = byWave.get(r.waveLabel) ?? [];
    arr.push(r);
    byWave.set(r.waveLabel, arr);
  }
  const waves: Wave[] = [];
  for (const [label, group] of byWave) {
    const paperMean: Record<string, number | null> = {};
    let progSum = 0;
    let progN = 0;
    for (const row of group) {
      const scores = row.verdicts
        .map((v) => SCORE[v.verdict])
        .filter((s): s is number => s !== null && s !== undefined);
      if (scores.length === 0) {
        paperMean[row.paperId] = null;
      } else {
        const m = scores.reduce((a, b) => a + b, 0) / scores.length;
        paperMean[row.paperId] = m;
        progSum += scores.reduce((a, b) => a + b, 0);
        progN += scores.length;
      }
    }
    waves.push({
      label,
      dateISO: group[0].dateISO,
      seq: Math.min(...group.map((g) => g.seq)),
      paperMean,
      programMean: progN === 0 ? null : progSum / progN,
    });
  }
  return waves.sort((a, b) => a.seq - b.seq);
}

/** Break a series into contiguous non-null segments so FAILED = gap, not a drop-to-zero. */
function segments(pts: (number | null)[]): { i: number; v: number }[][] {
  const segs: { i: number; v: number }[][] = [];
  let cur: { i: number; v: number }[] = [];
  pts.forEach((v, i) => {
    if (v === null) {
      if (cur.length) segs.push(cur);
      cur = [];
    } else {
      cur.push({ i, v });
    }
  });
  if (cur.length) segs.push(cur);
  return segs;
}

/**
 * Two honest trend windows over the program-average series.
 *   sinceRigor: delta from the first non-null program mean AT/AFTER the last rigor
 *     event to the latest — the comparable, un-reset window (PRIMARY).
 *   allHistory: delta from the first ever to the latest — spans resets (SECONDARY).
 */
function computeTrends(
  waves: Wave[],
  rigorEvents: RigorEvent[],
): {
  sinceRigor: { delta: number; ok: boolean; fromLabel?: string };
  allHistory: { delta: number; ok: boolean };
} {
  const idxVals = waves
    .map((w, i) => ({ i, v: w.programMean }))
    .filter((p): p is { i: number; v: number } => p.v !== null);

  const allHistory =
    idxVals.length >= 2
      ? { delta: idxVals[idxVals.length - 1].v - idxVals[0].v, ok: true }
      : { delta: 0, ok: false };

  // Most-recent rigor event by date.
  const lastRigorDate = rigorEvents
    .map((e) => e.dateISO)
    .sort()
    .at(-1);

  let sinceRigor: { delta: number; ok: boolean; fromLabel?: string } = {
    delta: 0,
    ok: false,
  };
  if (lastRigorDate) {
    const windowVals = idxVals.filter((p) => waves[p.i].dateISO >= lastRigorDate);
    if (windowVals.length >= 2) {
      sinceRigor = {
        delta: windowVals[windowVals.length - 1].v - windowVals[0].v,
        ok: true,
        fromLabel: waves[windowVals[0].i].label,
      };
    }
  }
  // Fallback: if no rigor window has ≥2 points, use the last few waves.
  if (!sinceRigor.ok && idxVals.length >= 2) {
    const recent = idxVals.slice(-3);
    sinceRigor = {
      delta: recent[recent.length - 1].v - recent[0].v,
      ok: true,
      fromLabel: waves[recent[0].i].label,
    };
  }
  return { sinceRigor, allHistory };
}

function arrow(d: number) {
  return d > 0.05 ? "↑" : d < -0.05 ? "↓" : "→";
}
function trendColor(d: number) {
  return d > 0.05 ? "var(--success)" : d < -0.05 ? "var(--crit)" : AXIS;
}

/* ── The SVG plot (shared by inline + expanded) ──────────────────────── */

function TrajectoryPlot({
  waves,
  rigorEvents,
  active,
  expanded,
}: {
  waves: Wave[];
  rigorEvents: RigorEvent[];
  active: Record<string, boolean>;
  expanded: boolean;
}) {
  const n = waves.length;

  // Wider per-wave spacing when expanded so labels + points breathe.
  const perWave = expanded ? 46 : 30;
  const width = Math.max(expanded ? 900 : 640, 120 + n * perWave);
  const padL = 56;
  const padR = 28;
  const padT = expanded ? 52 : 40;
  // more label room when expanded (full labels, not truncated)
  const padB = expanded ? 150 : 104;
  const plotW = width - padL - padR;
  const plotH = expanded ? 360 : 220;
  const height = padT + plotH + padB;

  const x = (i: number) => padL + (n === 1 ? plotW / 2 : (i / (n - 1)) * plotW);
  const y = (v: number) => padT + (1 - v / 3) * plotH;
  const xAxisY = padT + plotH;

  const linePath = (segs: { i: number; v: number }[][]) =>
    segs
      .map((seg) => seg.map((p, k) => `${k === 0 ? "M" : "L"}${x(p.i)},${y(p.v)}`).join(" "))
      .join(" ");

  const programSegs = segments(waves.map((w) => w.programMean));

  // Label thinning: inline shows every Nth label; expanded shows all.
  // Aim for ≤ ~22 labels inline so they don't collide.
  const labelStep = expanded ? 1 : Math.max(1, Math.ceil(n / 22));

  const rigorMarks = rigorEvents
    .map((e) => {
      let idx = waves.findIndex((w) => w.dateISO >= e.dateISO);
      if (idx < 0) idx = waves.length - 1;
      return { ...e, idx };
    })
    .filter((m) => m.idx >= 0 && m.idx < waves.length);

  const labelFS = expanded ? 8.5 : 6.8;
  const rigorFS = expanded ? 8.5 : 7;

  return (
    <svg
      viewBox={`0 0 ${width} ${height}`}
      role="img"
      aria-label="Verdict trajectory: per-paper and program-average verdict score across review waves (higher is better)"
      className="progress-svg"
      style={{ maxWidth: "none" }}
    >
      {/* y grid + labels (REJECT bottom → ACCEPT top) */}
      {[0, 1, 2, 3].map((v) => (
        <g key={v}>
          <line
            x1={padL}
            y1={y(v)}
            x2={width - padR}
            y2={y(v)}
            stroke={GRID}
            strokeWidth={0.75}
            strokeDasharray="2 4"
          />
          <text
            x={padL - 7}
            y={y(v) + 3}
            textAnchor="end"
            fontFamily={MONO}
            fontSize={expanded ? 9.5 : 8}
            fill={AXIS}
          >
            {Y_LABELS[v]}
          </text>
        </g>
      ))}

      {/* rigor-event vertical annotation markers */}
      {rigorMarks.map((m, k) => (
        <g key={`rigor-${m.label}-${k}`}>
          <line
            x1={x(m.idx)}
            y1={padT}
            x2={x(m.idx)}
            y2={xAxisY}
            stroke="var(--warn)"
            strokeWidth={0.9}
            strokeDasharray="3 3"
            opacity={0.6}
          />
          <text
            x={x(m.idx) + 3}
            y={padT + 9 + (k % 3) * (expanded ? 13 : 11)}
            fontFamily={MONO}
            fontSize={rigorFS}
            fill="var(--warn)"
            opacity={0.95}
          >
            ⚑ {expanded ? m.label : m.label.length > 18 ? m.label.slice(0, 17) + "…" : m.label}
            <title>{`${m.label} (${m.dateISO}) — ${m.description}\nsource: ${m.source}`}</title>
          </text>
        </g>
      ))}

      {/* per-paper average series (toggleable, light) */}
      {PAPER_ORDER.map((p) => {
        if (!active[p]) return null;
        const segs = segments(waves.map((w) => w.paperMean[p] ?? null));
        if (segs.length === 0) return null;
        return (
          <g key={`series-${p}`}>
            <path
              d={linePath(segs)}
              fill="none"
              stroke={PAPER_COLOR[p]}
              strokeWidth={1.4}
              strokeLinejoin="round"
              opacity={0.85}
            />
            {segs.flatMap((seg) =>
              seg.map((pt) => (
                <circle
                  key={`${p}-${pt.i}`}
                  cx={x(pt.i)}
                  cy={y(pt.v)}
                  r={expanded ? 2.6 : 2}
                  fill={PAPER_COLOR[p]}
                  stroke="var(--bg)"
                  strokeWidth={0.8}
                >
                  <title>{`${p} · ${waves[pt.i].label} (${waves[pt.i].dateISO}): mean ${pt.v.toFixed(2)} / 3`}</title>
                </circle>
              )),
            )}
          </g>
        );
      })}

      {/* program-average line (bold) */}
      <path
        d={linePath(programSegs)}
        fill="none"
        stroke="var(--text-primary)"
        strokeWidth={expanded ? 2.8 : 2.4}
        strokeLinejoin="round"
      />
      {programSegs.flatMap((seg) =>
        seg.map((pt) => (
          <circle
            key={`prog-${pt.i}`}
            cx={x(pt.i)}
            cy={y(pt.v)}
            r={expanded ? 3.4 : 2.8}
            fill="var(--text-primary)"
            stroke="var(--bg)"
            strokeWidth={1.2}
          >
            <title>{`Program average · ${waves[pt.i].label} (${waves[pt.i].dateISO}): ${pt.v.toFixed(2)} / 3`}</title>
          </circle>
        )),
      )}

      {/* x-axis ticks + rotated labels (thinned inline, full when expanded) */}
      {waves.map((w, i) => {
        const cx = x(i);
        const labelY = xAxisY + 5;
        const showLabel = i % labelStep === 0 || i === n - 1;
        return (
          <g key={`xl-${w.label}-${i}`}>
            <line x1={cx} y1={xAxisY} x2={cx} y2={xAxisY + 3} stroke={AXIS} strokeWidth={0.6} />
            {showLabel ? (
              <text
                x={cx}
                y={labelY}
                textAnchor="end"
                fontFamily={MONO}
                fontSize={labelFS}
                fill={AXIS}
                transform={`rotate(-55, ${cx}, ${labelY})`}
              >
                {expanded ? w.label : w.label.length > 16 ? w.label.slice(0, 15) + "…" : w.label}
                <tspan fill={AXIS} opacity={0.6}> {w.dateISO.slice(5)}</tspan>
                <title>{`${w.label} (${w.dateISO})${
                  w.programMean !== null ? ` — program mean ${w.programMean.toFixed(2)} / 3` : ""
                }`}</title>
              </text>
            ) : null}
          </g>
        );
      })}

      {/* program-average legend */}
      <g>
        <line
          x1={padL}
          y1={expanded ? 20 : 16}
          x2={padL + 18}
          y2={expanded ? 20 : 16}
          stroke="var(--text-primary)"
          strokeWidth={2.4}
        />
        <text
          x={padL + 22}
          y={expanded ? 23 : 19}
          fontFamily={MONO}
          fontSize={expanded ? 9 : 8}
          fill="var(--text-secondary)"
        >
          program average (bold) · thin lines = per-paper average · gaps = FAILED legs
        </text>
      </g>
    </svg>
  );
}

/* ── Trend badges + paper toggle chips (shared header controls) ──────── */

function ChartControls({
  active,
  setActive,
  trends,
}: {
  active: Record<string, boolean>;
  setActive: React.Dispatch<React.SetStateAction<Record<string, boolean>>>;
  trends: ReturnType<typeof computeTrends>;
}) {
  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 10, alignItems: "center" }}>
      {PAPER_ORDER.map((p) => (
        <button
          key={p}
          type="button"
          onClick={() => setActive((s) => ({ ...s, [p]: !s[p] }))}
          style={{
            fontFamily: MONO,
            fontSize: "0.64rem",
            letterSpacing: "0.05em",
            padding: "2px 9px",
            borderRadius: 4,
            cursor: "pointer",
            border: `1px solid ${active[p] ? PAPER_COLOR[p] : "var(--border)"}`,
            background: active[p]
              ? `color-mix(in srgb, ${PAPER_COLOR[p]} 16%, transparent)`
              : "transparent",
            color: active[p] ? "var(--text-secondary)" : "var(--text-tertiary)",
            opacity: active[p] ? 1 : 0.6,
          }}
          aria-pressed={active[p]}
        >
          <span
            style={{
              display: "inline-block",
              width: 8,
              height: 8,
              borderRadius: 2,
              background: PAPER_COLOR[p],
              marginRight: 6,
              verticalAlign: "middle",
              opacity: active[p] ? 1 : 0.4,
            }}
          />
          {p}
        </button>
      ))}

      {/* Two honest trend numbers */}
      <span style={{ display: "inline-flex", gap: 12, marginLeft: "auto", alignItems: "center" }}>
        {trends.sinceRigor.ok ? (
          <span
            style={{ fontFamily: MONO, fontSize: "0.64rem", color: trendColor(trends.sinceRigor.delta) }}
            title={`Program-average verdict-score change since the last documented rigor event${
              trends.sinceRigor.fromLabel ? ` (${trends.sinceRigor.fromLabel})` : ""
            } — the honest, comparable window (higher = better).`}
          >
            since rigor event {arrow(trends.sinceRigor.delta)}{" "}
            {trends.sinceRigor.delta >= 0 ? "+" : ""}
            {trends.sinceRigor.delta.toFixed(2)}
          </span>
        ) : null}
        {trends.allHistory.ok ? (
          <span
            style={{ fontFamily: MONO, fontSize: "0.6rem", color: AXIS, opacity: 0.85 }}
            title="Program-average change across ALL recorded history. This spans documented rigor resets — most importantly the 2026-07-04 verified-review reset, where the earlier, higher scores were fabricated-era (unverified) reviews. So this figure can read negative even while quality improves; use the 'since rigor event' number for an honest comparison."
          >
            all history (spans rigor resets) {arrow(trends.allHistory.delta)}{" "}
            {trends.allHistory.delta >= 0 ? "+" : ""}
            {trends.allHistory.delta.toFixed(2)}
          </span>
        ) : null}
      </span>
    </div>
  );
}

export function VerdictTrajectoryChart({
  rows,
  rigorEvents,
}: {
  rows: WaveRow[];
  rigorEvents: RigorEvent[];
}) {
  const waves = useMemo(() => buildWaves(rows), [rows]);
  const [active, setActive] = useState<Record<string, boolean>>(
    () => Object.fromEntries(PAPER_ORDER.map((p) => [p, true])),
  );

  // Trends always computed over the FULL history (honest windows).
  const trends = useMemo(() => computeTrends(waves, rigorEvents), [waves, rigorEvents]);

  if (waves.length === 0) {
    return (
      <p style={{ fontFamily: MONO, fontSize: "0.72rem", color: AXIS }}>
        No verdict-trajectory data yet — the loop records a row per review wave.
      </p>
    );
  }

  const total = waves.length;
  const inlineWaves = total > INLINE_CAP ? waves.slice(-INLINE_CAP) : waves;
  const capped = total > INLINE_CAP;

  const inlineNode = (
    <>
      <ChartControls active={active} setActive={setActive} trends={trends} />
      <div className="verdict-carousel">
        <TrajectoryPlot
          waves={inlineWaves}
          rigorEvents={rigorEvents}
          active={active}
          expanded={false}
        />
      </div>
      {capped ? (
        <p
          style={{
            fontFamily: MONO,
            fontSize: "0.66rem",
            color: AXIS,
            margin: "6px 0 0 0",
          }}
        >
          Showing the last {INLINE_CAP} of {total} review waves. Use{" "}
          <strong style={{ color: "var(--text-secondary)" }}>Expand ⤢</strong> above for the full
          history at readable size, with all labels, per-wave verdicts on hover, and a scrollable
          timeline.
        </p>
      ) : null}
    </>
  );

  const expandedNode = (
    <>
      <ChartControls active={active} setActive={setActive} trends={trends} />
      <div className="verdict-carousel verdict-carousel--expanded">
        <TrajectoryPlot
          waves={waves}
          rigorEvents={rigorEvents}
          active={active}
          expanded
        />
      </div>
      <p
        style={{
          fontFamily: MONO,
          fontSize: "0.68rem",
          color: AXIS,
          margin: "8px 0 0 0",
          maxWidth: "80ch",
        }}
      >
        Full history — all {total} review waves. Hover any point for the exact paper, wave, date,
        and mean verdict; ⚑ markers carry the full rigor-event label + source. Toggle papers with
        the chips above; scroll horizontally to reach the earliest waves.
      </p>
    </>
  );

  return (
    <ChartShell
      title="Verdict trajectory — full history"
      hint={
        capped ? (
          <span style={{ fontFamily: MONO, fontSize: "0.64rem", color: AXIS }}>
            last {INLINE_CAP} of {total} waves
          </span>
        ) : undefined
      }
      expandedContent={expandedNode}
    >
      {inlineNode}
    </ChartShell>
  );
}
