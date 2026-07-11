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
 * Trend: program-average delta over the last 3 waves with ↑ / → / ↓.
 *
 * Dependency-free inline SVG, styled with the existing CSS vars (dark/light safe),
 * matching ProgressViz.tsx. No verdict is invented — every point comes from a real
 * recorded verdict row.
 */
import { useMemo, useState } from "react";
import type { WaveRow, RigorEvent } from "@/lib/liveReadiness";

const MONO = "var(--font-mono-stack)";
const AXIS = "var(--text-muted)";
const GRID = "var(--border)";

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
  // paperId -> mean verdict score across that paper's non-failed reviewer legs
  paperMean: Record<string, number | null>;
  // program mean across all non-failed legs this wave
  programMean: number | null;
};

function buildWaves(rows: WaveRow[]): Wave[] {
  // Group rows by wave label (rows are per-paper per-wave).
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

  if (waves.length === 0) {
    return (
      <p style={{ fontFamily: MONO, fontSize: "0.72rem", color: AXIS }}>
        No verdict-trajectory data yet — the loop records a row per review wave.
      </p>
    );
  }

  // Layout
  const width = Math.max(680, 120 + waves.length * 26);
  const padL = 52;
  const padR = 24;
  const padT = 40;
  const padB = 96; // rotated x labels + rigor markers
  const plotW = width - padL - padR;
  const plotH = 220;
  const height = padT + plotH + padB;
  const n = waves.length;

  const x = (i: number) => padL + (n === 1 ? plotW / 2 : (i / (n - 1)) * plotW);
  const y = (v: number) => padT + (1 - v / 3) * plotH;
  const xAxisY = padT + plotH;

  const linePath = (segs: { i: number; v: number }[][]) =>
    segs
      .map((seg) => seg.map((p, k) => `${k === 0 ? "M" : "L"}${x(p.i)},${y(p.v)}`).join(" "))
      .join(" ");

  const programSegs = segments(waves.map((w) => w.programMean));

  // Trend: program-avg delta over the last 3 non-null program means.
  const progVals = waves.map((w) => w.programMean).filter((v): v is number => v !== null);
  const recent = progVals.slice(-3);
  const trendDelta = recent.length >= 2 ? recent[recent.length - 1] - recent[0] : 0;
  const trendArrow = trendDelta > 0.05 ? "↑" : trendDelta < -0.05 ? "↓" : "→";
  const trendColor =
    trendDelta > 0.05 ? "var(--success)" : trendDelta < -0.05 ? "var(--crit)" : AXIS;

  // Map rigor events to the nearest wave index by date (for x placement).
  const rigorMarks = rigorEvents
    .map((e) => {
      // place at the first wave with dateISO >= event date, else last wave
      let idx = waves.findIndex((w) => w.dateISO >= e.dateISO);
      if (idx < 0) idx = waves.length - 1;
      return { ...e, idx };
    })
    .filter((m) => m.idx >= 0);

  return (
    <div>
      {/* Toggle chips */}
      <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 10 }}>
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
        <span
          style={{
            fontFamily: MONO,
            fontSize: "0.64rem",
            marginLeft: "auto",
            color: trendColor,
            alignSelf: "center",
          }}
          title="Program-average verdict-score change over the last 3 waves (higher = better)"
        >
          trend {trendArrow} {trendDelta >= 0 ? "+" : ""}
          {trendDelta.toFixed(2)}
        </span>
      </div>

      <div className="verdict-carousel">
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
              <text x={padL - 7} y={y(v) + 3} textAnchor="end" fontFamily={MONO} fontSize={8} fill={AXIS}>
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
                y={padT + 9 + (k % 3) * 11}
                fontFamily={MONO}
                fontSize={7}
                fill="var(--warn)"
                opacity={0.95}
              >
                ⚑ {m.label}
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
                      r={2}
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
            strokeWidth={2.4}
            strokeLinejoin="round"
          />
          {programSegs.flatMap((seg) =>
            seg.map((pt) => (
              <circle
                key={`prog-${pt.i}`}
                cx={x(pt.i)}
                cy={y(pt.v)}
                r={2.8}
                fill="var(--text-primary)"
                stroke="var(--bg)"
                strokeWidth={1.2}
              >
                <title>{`Program average · ${waves[pt.i].label} (${waves[pt.i].dateISO}): ${pt.v.toFixed(2)} / 3`}</title>
              </circle>
            )),
          )}

          {/* x-axis ticks + rotated labels */}
          {waves.map((w, i) => {
            const cx = x(i);
            const labelY = xAxisY + 5;
            return (
              <g key={`xl-${w.label}-${i}`}>
                <line x1={cx} y1={xAxisY} x2={cx} y2={xAxisY + 3} stroke={AXIS} strokeWidth={0.6} />
                <text
                  x={cx}
                  y={labelY}
                  textAnchor="end"
                  fontFamily={MONO}
                  fontSize={6.8}
                  fill={AXIS}
                  transform={`rotate(-55, ${cx}, ${labelY})`}
                >
                  {w.label.length > 16 ? w.label.slice(0, 15) + "…" : w.label}
                  <tspan fill={AXIS} opacity={0.6}> {w.dateISO.slice(5)}</tspan>
                </text>
              </g>
            );
          })}

          {/* program-average legend */}
          <g>
            <line x1={padL} y1={16} x2={padL + 18} y2={16} stroke="var(--text-primary)" strokeWidth={2.4} />
            <text x={padL + 22} y={19} fontFamily={MONO} fontSize={8} fill="var(--text-secondary)">
              program average (bold) · thin lines = per-paper average · gaps = FAILED legs
            </text>
          </g>
        </svg>
      </div>
    </div>
  );
}
