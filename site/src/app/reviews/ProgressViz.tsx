/**
 * Dependency-free inline-SVG progress visualizations for /reviews.
 * Styled exclusively with existing CSS vars (dark/light safe). No animation
 * beyond subtle CSS transitions defined in reviews.css.
 */
import {
  externalVerdictRounds,
  gapSeries,
  readinessCheckpoints,
  skillsSeries,
  PAPER_IDS,
  REVIEWERS,
  type PaperId,
  type Verdict,
} from "@/data/reviewTimeline";

const VERDICT_COLOR: Record<Verdict, string> = {
  REJECT: "var(--crit)",
  MAJOR: "var(--warn)",
  MINOR: "color-mix(in srgb, var(--warn) 35%, var(--success))",
  ACCEPT: "var(--success)",
};

const VERDICT_SHORT: Record<Verdict, string> = {
  REJECT: "R",
  MAJOR: "M",
  MINOR: "m",
  ACCEPT: "A",
};

const MONO = "var(--font-mono-stack)";
const AXIS = "var(--text-muted)";
const GRID = "var(--border)";

/* ── (a) Verdict-trajectory strip: papers × rounds × reviewers ───────── */

export function VerdictTrajectory() {
  const rounds = externalVerdictRounds;
  const cellW = 30;
  const cellH = 20;
  const cellGap = 4;
  const groupGap = 34;
  const labelW = 42;
  const headerH = 36;
  const rowGap = 6;
  const groupW = REVIEWERS.length * cellW + (REVIEWERS.length - 1) * cellGap;
  const width = labelW + rounds.length * groupW + (rounds.length - 1) * groupGap + 8;
  const height = headerH + PAPER_IDS.length * (cellH + rowGap);

  const groupX = (gi: number) => labelW + gi * (groupW + groupGap);

  return (
    <svg
      viewBox={`0 0 ${width} ${height}`}
      role="img"
      aria-label="External referee verdicts per paper per round"
      className="progress-svg"
      style={{ maxWidth: width }}
    >
      {/* round + reviewer headers */}
      {rounds.map((round, gi) => (
        <g key={round.roundId}>
          <text x={groupX(gi) + groupW / 2} y={11} textAnchor="middle" fontFamily={MONO} fontSize={9.5} letterSpacing={1} fill="var(--text-tertiary)">
            {round.roundId}
          </text>
          {REVIEWERS.map((rv, ri) => (
            <text key={rv} x={groupX(gi) + ri * (cellW + cellGap) + cellW / 2} y={26} textAnchor="middle" fontFamily={MONO} fontSize={7.5} fill={AXIS}>
              {rv === "ChatGPT" ? "GPT" : rv === "Grok" ? "GRK" : "GEM"}
            </text>
          ))}
        </g>
      ))}
      {/* arrows between round groups */}
      {rounds.slice(0, -1).map((_, gi) => (
        <text key={gi} x={groupX(gi) + groupW + groupGap / 2} y={headerH + (PAPER_IDS.length * (cellH + rowGap)) / 2} textAnchor="middle" fontFamily={MONO} fontSize={11} fill={AXIS}>
          →
        </text>
      ))}
      {/* rows */}
      {PAPER_IDS.map((p, pi) => {
        const y = headerH + pi * (cellH + rowGap);
        return (
          <g key={p}>
            <text x={0} y={y + cellH / 2 + 3.5} fontFamily={MONO} fontSize={9.5} fill="var(--text-secondary)">
              {p}
            </text>
            {rounds.map((round, gi) =>
              round.verdicts[p as PaperId].map((v, ri) => (
                <g key={`${round.roundId}-${ri}`}>
                  <rect
                    x={groupX(gi) + ri * (cellW + cellGap)}
                    y={y}
                    width={cellW}
                    height={cellH}
                    rx={3}
                    fill={VERDICT_COLOR[v]}
                    fillOpacity={v === "ACCEPT" ? 0.92 : 0.78}
                    className="verdict-cell"
                  >
                    <title>{`${p} · ${round.roundId} · ${REVIEWERS[ri]}: ${v}`}</title>
                  </rect>
                  <text
                    x={groupX(gi) + ri * (cellW + cellGap) + cellW / 2}
                    y={y + cellH / 2 + 3.5}
                    textAnchor="middle"
                    fontFamily={MONO}
                    fontSize={9}
                    fontWeight={600}
                    fill="var(--bg)"
                    pointerEvents="none"
                  >
                    {VERDICT_SHORT[v]}
                  </text>
                </g>
              )),
            )}
          </g>
        );
      })}
    </svg>
  );
}

export function VerdictLegend() {
  const order: Verdict[] = ["REJECT", "MAJOR", "MINOR", "ACCEPT"];
  return (
    <div className="verdict-legend">
      {order.map((v) => (
        <span key={v} className="verdict-legend-item">
          <span className="verdict-legend-swatch" style={{ background: VERDICT_COLOR[v] }} />
          {v}
        </span>
      ))}
    </div>
  );
}

/* ── (b) Gap-closure chart: external-only findings per round → zero ──── */

/** Chronological order regardless of authoring order: dateISO, then round sequence (EXT1 < EXT2 < EXT3). */
function chronologicalGapSeries() {
  return [...gapSeries].sort((a, b) => a.dateISO.localeCompare(b.dateISO) || a.roundId.localeCompare(b.roundId));
}

export function GapClosureChart() {
  const pts = chronologicalGapSeries();
  const width = 380;
  const height = 190;
  const padL = 34;
  const padR = 56;
  const padT = 18;
  const padB = 30;
  const plotW = width - padL - padR;
  const plotH = height - padT - padB;
  const maxY = 60;
  const x = (i: number) => padL + (pts.length === 1 ? plotW / 2 : (i / (pts.length - 1)) * plotW);
  const y = (v: number) => padT + (1 - v / maxY) * plotH;

  const linePath = pts.map((p, i) => `${i === 0 ? "M" : "L"}${x(i)},${y(p.total)}`).join(" ");
  const areaPath = `${linePath} L${x(pts.length - 1)},${y(0)} L${x(0)},${y(0)} Z`;

  return (
    <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Internal/external gap: externally-caught findings per round, target zero" className="progress-svg">
      {/* y grid + ticks */}
      {[0, 30, 60].map((v) => (
        <g key={v}>
          <line x1={padL} y1={y(v)} x2={width - padR} y2={y(v)} stroke={GRID} strokeWidth={v === 0 ? 0 : 1} strokeDasharray={v === 0 ? undefined : "2 4"} />
          <text x={padL - 7} y={y(v) + 3} textAnchor="end" fontFamily={MONO} fontSize={8.5} fill={AXIS}>
            {v}
          </text>
        </g>
      ))}
      {/* target-zero baseline */}
      <line x1={padL} y1={y(0)} x2={width - padR} y2={y(0)} stroke="var(--success)" strokeWidth={1.25} strokeDasharray="5 4" opacity={0.7} />
      <text x={width - padR + 6} y={y(0) + 3} fontFamily={MONO} fontSize={8.5} fill="var(--success)">
        target 0
      </text>
      {/* area + line */}
      <path d={areaPath} fill="var(--warn)" opacity={0.1} />
      <path d={linePath} fill="none" stroke="var(--warn)" strokeWidth={1.75} />
      {/* points */}
      {pts.map((p, i) => (
        <g key={p.roundId}>
          <circle cx={x(i)} cy={y(p.total)} r={3.5} fill="var(--warn)" stroke="var(--bg)" strokeWidth={1.5}>
            <title>{`${p.roundId}: ${p.total} — ${p.note}`}</title>
          </circle>
          <text x={x(i)} y={y(p.total) - 9} textAnchor="middle" fontFamily={MONO} fontSize={10.5} fontWeight={600} fill="var(--text)">
            {p.total}
          </text>
          <text x={x(i)} y={height - 10} textAnchor="middle" fontFamily={MONO} fontSize={9} fill={AXIS}>
            {p.roundId}
          </text>
        </g>
      ))}
    </svg>
  );
}

export function GapPerPaperDeltas() {
  const pts = chronologicalGapSeries();
  const a = pts[0];
  const b = pts[pts.length - 1];
  if (!a || !b || a === b) return null;
  return (
    <div className="gap-deltas">
      {PAPER_IDS.map((p) => {
        const from = a.perPaper[p as PaperId];
        const to = b.perPaper[p as PaperId];
        const improved = to < from;
        return (
          <span key={p} className="gap-delta-chip">
            <span className="gap-delta-paper">{p}</span> {from}→{to}
            <span style={{ color: improved ? "var(--success)" : "var(--warn)" }}> {improved ? "▾" : "▴"}</span>
          </span>
        );
      })}
    </div>
  );
}

/* ── (c) Skills-growth stepped lines: patterns + reviewer-prompt rules ── */

export function SkillsGrowthChart() {
  const pts = skillsSeries;
  const width = 380;
  const height = 190;
  const padL = 34;
  const padR = 14;
  const padT = 18;
  const padB = 42;
  const plotW = width - padL - padR;
  const plotH = height - padT - padB;
  const maxY = 50;
  const x = (i: number) => padL + (i / (pts.length - 1)) * plotW;
  const y = (v: number) => padT + (1 - v / maxY) * plotH;

  const step = (vals: number[]) =>
    vals
      .map((v, i) => {
        if (i === 0) return `M${x(0)},${y(v)}`;
        return `L${x(i)},${y(vals[i - 1])} L${x(i)},${y(v)}`;
      })
      .join(" ");

  const patternPath = step(pts.map((p) => p.patterns));
  const rulesPath = step(pts.map((p) => p.promptRules));

  return (
    <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Skills-stack growth: review patterns and reviewer-prompt rules per round" className="progress-svg">
      {[0, 25, 50].map((v) => (
        <g key={v}>
          <line x1={padL} y1={y(v)} x2={width - padR} y2={y(v)} stroke={GRID} strokeWidth={1} strokeDasharray="2 4" />
          <text x={padL - 7} y={y(v) + 3} textAnchor="end" fontFamily={MONO} fontSize={8.5} fill={AXIS}>
            {v}
          </text>
        </g>
      ))}
      {/* prompt rules (secondary) */}
      <path d={rulesPath} fill="none" stroke="var(--text-muted)" strokeWidth={1.25} strokeDasharray="4 3" />
      {/* patterns (primary) */}
      <path d={patternPath} fill="none" stroke="var(--accent)" strokeWidth={1.75} />
      {pts.map((p, i) => (
        <g key={p.id}>
          <circle cx={x(i)} cy={y(p.patterns)} r={3} fill="var(--accent)" stroke="var(--bg)" strokeWidth={1.5}>
            <title>{`${p.id}: ${p.patterns} patterns · ${p.promptRules} prompt rules — ${p.note}`}</title>
          </circle>
          <text x={x(i)} y={y(p.patterns) - 8} textAnchor="middle" fontFamily={MONO} fontSize={9.5} fontWeight={600} fill="var(--text)">
            {p.patterns}
          </text>
          <circle cx={x(i)} cy={y(p.promptRules)} r={2.25} fill="var(--text-muted)" stroke="var(--bg)" strokeWidth={1.25}>
            <title>{`${p.id}: ${p.promptRules} reviewer-prompt rules`}</title>
          </circle>
          <text x={x(i)} y={height - 22} textAnchor="middle" fontFamily={MONO} fontSize={7.5} fill={AXIS}>
            {p.id}
          </text>
          <text x={x(i)} y={height - 11} textAnchor="middle" fontFamily={MONO} fontSize={7.5} fill={AXIS}>
            {p.dateISO.slice(5)}
          </text>
        </g>
      ))}
      {/* inline legend */}
      <g fontFamily={MONO} fontSize={8}>
        <line x1={padL + 2} y1={padT - 6} x2={padL + 16} y2={padT - 6} stroke="var(--accent)" strokeWidth={1.75} />
        <text x={padL + 20} y={padT - 3} fill="var(--text-secondary)">
          review patterns
        </text>
        <line x1={padL + 104} y1={padT - 6} x2={padL + 118} y2={padT - 6} stroke="var(--text-muted)" strokeWidth={1.25} strokeDasharray="4 3" />
        <text x={padL + 122} y={padT - 3} fill="var(--text-secondary)">
          reviewer-prompt rules
        </text>
      </g>
    </svg>
  );
}

/* ── Readiness strip: sparse per-paper checkpoints (95-cap rule) ──────── */

export function ReadinessStrip() {
  const cps = readinessCheckpoints;
  const current = cps[cps.length - 1];
  return (
    <div className="readiness-strip" title={current.note}>
      <span className="readiness-strip-label">readiness (95-cap)</span>
      {PAPER_IDS.map((p) => {
        const v = current.values[p as PaperId];
        const trail = cps
          .filter((c) => typeof c.values[p as PaperId] === "number")
          .map((c) => `${c.id} ${c.values[p as PaperId]}%`)
          .join(" → ");
        return (
          <span key={p} className="readiness-chip" title={`${p}: ${trail}`}>
            <span className="gap-delta-paper">{p}</span> {v}%
          </span>
        );
      })}
    </div>
  );
}
