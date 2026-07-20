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
import { papers } from "@/data/papers";

const VERDICT_COLOR: Record<Verdict, string> = {
  REJECT: "var(--crit)",
  MAJOR: "var(--warn)",
  MINOR: "color-mix(in srgb, var(--warn) 35%, var(--success))",
  ACCEPT: "var(--success)",
  NO_VERDICT: "var(--text-muted)",
};

const VERDICT_SHORT: Record<Verdict, string> = {
  REJECT: "R",
  MAJOR: "M",
  MINOR: "m",
  ACCEPT: "A",
  NO_VERDICT: "—",
};

const MONO = "var(--font-mono-stack)";
const AXIS = "var(--text-muted)";
const GRID = "var(--border)";

/* ── (a) Verdict-trajectory strip: papers × rounds × reviewers ───────── */

/**
 * Latest genuinely-tested verdict per paper × reviewer.
 * Walks rounds newest→oldest (externalVerdictRounds is oldest→newest) and takes
 * the first non-NO_VERDICT cell, remembering the round it came from. NO_VERDICT
 * ("—") means "not re-swept that round" — this carries the verdict forward from
 * the latest round that actually tested that paper/reviewer. Computed from the
 * existing data — no new verdict is invented.
 */
function computeCurrent(): Record<PaperId, { verdict: Verdict; roundId: string }[]> {
  const out = {} as Record<PaperId, { verdict: Verdict; roundId: string }[]>;
  for (const p of PAPER_IDS) {
    out[p] = REVIEWERS.map((_rv, ri) => {
      for (let i = externalVerdictRounds.length - 1; i >= 0; i--) {
        const v = externalVerdictRounds[i].verdicts[p][ri];
        if (v !== "NO_VERDICT") return { verdict: v, roundId: externalVerdictRounds[i].roundId };
      }
      return { verdict: "NO_VERDICT" as Verdict, roundId: "—" };
    });
  }
  return out;
}

/**
 * Historical automated-verdict diagnostic: counts ACCEPT cells in the CURRENT
 * column over papers × reviewer legs. NO_VERDICT / FAILED / gap legs are not
 * ACCEPT. These labels are not journal decisions or a publication gate.
 */
export function AllAMeter() {
  const current = computeCurrent();
  let accept = 0;
  let total = 0;
  for (const p of PAPER_IDS) {
    for (const c of current[p]) {
      total += 1;
      if (c.verdict === "ACCEPT") accept += 1;
    }
  }
  const pct = total === 0 ? 0 : Math.round((accept / total) * 100);
  const done = accept === total && total > 0;
  return (
    <div className="alla-meter" role="group" aria-label="Automated review ACCEPT-label diagnostic">
      <div className="alla-meter-row">
        <span className="alla-meter-count">
          {accept} / {total} cells ACCEPT
        </span>
        <span className="alla-meter-pct" style={{ color: done ? "var(--success)" : "var(--text-secondary)" }}>
          {pct}%
        </span>
      </div>
      <div className="alla-meter-track" aria-hidden>
        <div className="alla-meter-fill" style={{ width: `${pct}%` }} />
      </div>
      <p className="alla-meter-goal">
        <strong>Automated-review diagnostic only.</strong> Counted from the CURRENT column
        (papers × reviewer legs); FAILED / not-yet-swept legs count as not-ACCEPT. An ACCEPT
        here is not journal acceptance, and 100% is not required to submit a paper.
      </p>
    </div>
  );
}

export function VerdictTrajectory() {
  // Order: CURRENT pinned far-LEFT, then rounds newest → oldest flowing right.
  const rounds = [...externalVerdictRounds].reverse();
  const current = computeCurrent();
  const cellW = 30;
  const cellH = 20;
  const cellGap = 4;
  const groupGap = 34;
  const labelW = 42;
  const headerH = 46;
  const rowGap = 6;
  const groupW = REVIEWERS.length * cellW + (REVIEWERS.length - 1) * cellGap;
  const currentGap = 40; // wider gap + divider after the CURRENT column
  // CURRENT sits first (far left), after the row-label gutter.
  const currentX0 = labelW;
  const roundsX0 = currentX0 + groupW + currentGap;
  const width = roundsX0 + rounds.length * groupW + (rounds.length - 1) * groupGap + 8;
  const height = headerH + PAPER_IDS.length * (cellH + rowGap);

  const groupX = (gi: number) => roundsX0 + gi * (groupW + groupGap);

  return (
    <svg
      viewBox={`0 0 ${width} ${height}`}
      width={width}
      role="img"
      aria-label="External referee verdicts per paper — CURRENT column first, then rounds newest to oldest"
      className="progress-svg"
      style={{ maxWidth: "none" }}
    >
      {/* ── CURRENT column (far left): latest tested verdict per paper × reviewer ── */}
      <text x={currentX0 + groupW / 2} y={11} textAnchor="middle" fontFamily={MONO} fontSize={9.5} letterSpacing={1} fill="var(--text-primary)" fontWeight={700}>
        CURRENT
      </text>
      <text x={currentX0 + groupW / 2} y={23} textAnchor="middle" fontFamily={MONO} fontSize={8} fill="var(--text-tertiary)">
        latest per paper
      </text>
      {REVIEWERS.map((rv, ri) => (
        <text key={`cur-hdr-${rv}`} x={currentX0 + ri * (cellW + cellGap) + cellW / 2} y={36} textAnchor="middle" fontFamily={MONO} fontSize={7.5} fill={AXIS}>
          {rv === "ChatGPT" ? "GPT" : rv === "Grok" ? "GRK" : "GEM"}
        </text>
      ))}
      {/* row labels (paper ids) — drawn once, in the left gutter */}
      {PAPER_IDS.map((p, pi) => {
        const y = headerH + pi * (cellH + rowGap);
        return (
          <text key={`lbl-${p}`} x={0} y={y + cellH / 2 + 3.5} fontFamily={MONO} fontSize={9.5} fill="var(--text-secondary)">
            {p}
          </text>
        );
      })}
      {PAPER_IDS.map((p, pi) => {
        const y = headerH + pi * (cellH + rowGap);
        return (
          <g key={`cur-${p}`}>
            {current[p].map((c, ri) => (
              <g key={`cur-${p}-${ri}`}>
                <rect
                  x={currentX0 + ri * (cellW + cellGap)}
                  y={y}
                  width={cellW}
                  height={cellH}
                  rx={3}
                  fill={VERDICT_COLOR[c.verdict]}
                  fillOpacity={c.verdict === "ACCEPT" ? 0.92 : 0.78}
                  stroke="var(--text-primary)"
                  strokeOpacity={0.28}
                  strokeWidth={1}
                  className="verdict-cell"
                >
                  <title>{`${p} · ${REVIEWERS[ri]}: ${c.verdict} — latest tested in ${c.roundId}`}</title>
                </rect>
                <text
                  x={currentX0 + ri * (cellW + cellGap) + cellW / 2}
                  y={y + cellH / 2 + 3.5}
                  textAnchor="middle"
                  fontFamily={MONO}
                  fontSize={9}
                  fontWeight={600}
                  fill="var(--bg)"
                  pointerEvents="none"
                >
                  {VERDICT_SHORT[c.verdict]}
                </text>
              </g>
            ))}
          </g>
        );
      })}
      {/* divider between CURRENT and the round history */}
      <line
        x1={roundsX0 - currentGap / 2}
        y1={4}
        x2={roundsX0 - currentGap / 2}
        y2={height - 4}
        stroke={GRID}
        strokeWidth={1}
        strokeDasharray="2 3"
      />
      {/* round + reviewer headers (newest → oldest, left → right) */}
      {rounds.map((round, gi) => (
        <g key={round.roundId}>
          <text x={groupX(gi) + groupW / 2} y={11} textAnchor="middle" fontFamily={MONO} fontSize={9.5} letterSpacing={1} fill="var(--text-tertiary)">
            {round.roundId}
          </text>
          {round.windowPT ? (
            <text x={groupX(gi) + groupW / 2} y={23} textAnchor="middle" fontFamily={MONO} fontSize={8} fill={AXIS}>
              {round.windowPT.split("·")[0].trim()}
              <title>{round.windowPT}</title>
            </text>
          ) : null}
          {REVIEWERS.map((rv, ri) => (
            <text key={rv} x={groupX(gi) + ri * (cellW + cellGap) + cellW / 2} y={36} textAnchor="middle" fontFamily={MONO} fontSize={7.5} fill={AXIS}>
              {rv === "ChatGPT" ? "GPT" : rv === "Grok" ? "GRK" : "GEM"}
            </text>
          ))}
        </g>
      ))}
      {/* arrows between round groups — point LEFT toward more-recent rounds (time flows right→left into CURRENT) */}
      {rounds.slice(0, -1).map((_, gi) => (
        <text key={gi} x={groupX(gi) + groupW + groupGap / 2} y={headerH + (PAPER_IDS.length * (cellH + rowGap)) / 2} textAnchor="middle" fontFamily={MONO} fontSize={11} fill={AXIS}>
          ←
        </text>
      ))}
      {/* round rows */}
      {PAPER_IDS.map((p, pi) => {
        const y = headerH + pi * (cellH + rowGap);
        return (
          <g key={p}>
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
    <>
      <div className="verdict-legend">
        {order.map((v) => (
          <span key={v} className="verdict-legend-item">
            <span className="verdict-legend-swatch" style={{ background: VERDICT_COLOR[v] }} />
            {v}
          </span>
        ))}
      </div>
      <p className="verdict-legend-note">
        <strong>—</strong> = not re-swept that round (verdict carries from the latest tested
        round, shown in the <strong>CURRENT</strong> column at right).
      </p>
    </>
  );
}

/* ── (b) Gap-closure chart: external-only findings per round → zero ──── */

/** Chronological order regardless of authoring order: dateISO, then round sequence (EXT1 < EXT2 < EXT3). */
function chronologicalGapSeries() {
  return [...gapSeries].sort((a, b) => a.dateISO.localeCompare(b.dateISO) || a.roundId.localeCompare(b.roundId));
}

export function GapClosureChart() {
  const pts = chronologicalGapSeries();
  const width = 640;
  const height = 272;
  const padL = 42;
  const padR = 72;
  const padT = 32;
  const padB = 60;
  const plotW = width - padL - padR;
  const plotH = height - padT - padB;
  const maxY = 70;
  const x = (i: number) => padL + (pts.length === 1 ? plotW / 2 : (i / (pts.length - 1)) * plotW);
  const y = (v: number) => padT + (1 - v / maxY) * plotH;
  // y-coordinate of the x-axis baseline
  const xAxisY = padT + plotH;

  const linePath = pts.map((p, i) => `${i === 0 ? "M" : "L"}${x(i)},${y(p.total)}`).join(" ");
  const areaPath = `${linePath} L${x(pts.length - 1)},${y(0)} L${x(0)},${y(0)} Z`;

  return (
    <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Internal/external gap: externally-caught findings per round, target zero" className="progress-svg">
      {/* y grid + ticks */}
      {[0, 35, 70].map((v) => (
        <g key={v}>
          <line x1={padL} y1={y(v)} x2={width - padR} y2={y(v)} stroke={GRID} strokeWidth={v === 0 ? 0 : 1} strokeDasharray={v === 0 ? undefined : "2 4"} />
          <text x={padL - 7} y={y(v) + 3} textAnchor="end" fontFamily={MONO} fontSize={10} fill={AXIS}>
            {v}
          </text>
        </g>
      ))}
      {/* target-zero baseline */}
      <line x1={padL} y1={y(0)} x2={width - padR} y2={y(0)} stroke="var(--success)" strokeWidth={1.25} strokeDasharray="5 4" opacity={0.7} />
      <text x={width - padR + 6} y={y(0) + 3} fontFamily={MONO} fontSize={10} fill="var(--success)">
        target 0
      </text>
      {/* area + line */}
      <path d={areaPath} fill="var(--warn)" opacity={0.1} />
      <path d={linePath} fill="none" stroke="var(--warn)" strokeWidth={1.75} />
      {/* milestone vertical guides — rendered before data points so lines sit behind dots */}
      {pts.map((p, i) =>
        p.milestone ? (
          <g key={`ms-${p.roundId}`}>
            <line
              x1={x(i)} y1={padT}
              x2={x(i)} y2={xAxisY}
              stroke="var(--success)"
              strokeWidth={0.8}
              strokeDasharray="2 3"
              opacity={0.45}
            />
            <text
              x={x(i)}
              y={padT - 4}
              textAnchor="middle"
              fontFamily={MONO}
              fontSize={11}
              fill="var(--success)"
              opacity={0.95}
              style={{ cursor: "default" }}
            >
              ⚑
              <title>{`${p.roundId} — ${p.milestone}`}</title>
            </text>
          </g>
        ) : null
      )}
      {/* points + rotated x labels */}
      {pts.map((p, i) => {
        const cx = x(i);
        const cy = y(p.total);
        // Anchor point for rotated label — just below the x-axis tick
        const labelY = xAxisY + 5;
        const isMilestone = Boolean(p.milestone);
        return (
          <g key={p.roundId}>
            <circle
              cx={cx}
              cy={cy}
              r={isMilestone ? 4.5 : 3.5}
              fill={isMilestone ? "var(--success)" : "var(--warn)"}
              stroke="var(--bg)"
              strokeWidth={1.5}
            >
              <title>{`${p.roundId}: ${p.total} — ${p.note}${isMilestone ? ` ★ ${p.milestone}` : ""}`}</title>
            </circle>
            <text x={cx} y={cy - 9} textAnchor="middle" fontFamily={MONO} fontSize={10} fontWeight={600} fill={isMilestone ? "var(--success)" : "var(--text)"}>
              {p.total}
            </text>
            {/* tick mark */}
            <line x1={cx} y1={xAxisY} x2={cx} y2={xAxisY + 3} stroke={AXIS} strokeWidth={0.75} />
            {/* rotated round label + date stamp — reads left-to-right when tilted 45° */}
            <text
              x={cx}
              y={labelY}
              textAnchor="end"
              fontFamily={MONO}
              fontSize={8}
              fill={isMilestone ? "var(--success)" : AXIS}
              transform={`rotate(-45, ${cx}, ${labelY})`}
            >
              {p.roundId}
              <tspan fill={AXIS} opacity={0.7}> · {p.dateISO.slice(5)}</tspan>
            </text>
          </g>
        );
      })}
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
  const width = 640;
  const height = 278;
  const padL = 42;
  const padR = 20;
  // padT large enough to hold a 2-row stacked legend above the plot
  const padT = 50;
  // padB enlarged to accommodate -45° rotated x-axis labels
  const padB = 80;
  const plotW = width - padL - padR;
  const plotH = height - padT - padB;
  // maxY raised to 75 so the highest data value (patterns=64) sits comfortably inside bounds
  const maxY = 75;
  const x = (i: number) => padL + (i / (pts.length - 1)) * plotW;
  const y = (v: number) => padT + (1 - v / maxY) * plotH;
  const xAxisY = padT + plotH;

  const step = (vals: number[]) =>
    vals
      .map((v, i) => {
        if (i === 0) return `M${x(0)},${y(v)}`;
        return `L${x(i)},${y(vals[i - 1])} L${x(i)},${y(v)}`;
      })
      .join(" ");

  const patternPath = step(pts.map((p) => p.patterns));
  const rulesPath = step(pts.map((p) => p.promptRules));
  // tooling is optional (undefined on legacy points before the counter existed).
  // Build a stepped path only over the contiguous tail where it is defined, so
  // undefined renders as a gap — never a zero.
  const toolingIdx = pts.map((p, i) => (p.tooling != null ? i : -1)).filter((i) => i >= 0);
  const toolingStart = toolingIdx.length ? toolingIdx[0] : -1;
  const toolingPath =
    toolingStart >= 0
      ? pts
          .slice(toolingStart)
          .map((p, k) => {
            const i = toolingStart + k;
            const v = p.tooling as number;
            if (k === 0) return `M${x(i)},${y(v)}`;
            const prev = pts[i - 1].tooling as number;
            return `L${x(i)},${y(prev)} L${x(i)},${y(v)}`;
          })
          .join(" ")
      : "";

  // Shorten long id strings for the x-axis label: take the part before "·"/"(",
  // strip date suffixes + verbose tags, cap length so rotated labels don't clip.
  const shortId = (id: string) => {
    const base = id
      .split(/[·(]/)[0]
      .trim()
      .replace("-gapmine", "")
      .replace("-mine", "")
      .replace("-learning-loop", "")
      .replace(/-?2026-\d\d-\d\d/g, "")
      .replace(/-+$/, "");
    return base.length > 15 ? base.slice(0, 14) + "…" : base;
  };

  return (
    <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Skills-stack growth: review patterns, reviewer-prompt rules, and process/tooling assets per round" className="progress-svg">
      {/* y grid + ticks — updated to match new maxY */}
      {[0, 25, 50, 75].map((v) => (
        <g key={v}>
          <line x1={padL} y1={y(v)} x2={width - padR} y2={y(v)} stroke={GRID} strokeWidth={1} strokeDasharray="2 4" />
          <text x={padL - 7} y={y(v) + 3} textAnchor="end" fontFamily={MONO} fontSize={10} fill={AXIS}>
            {v}
          </text>
        </g>
      ))}
      {/* process/tooling (tertiary) — dotted, only over the tail where defined */}
      {toolingPath && (
        <path d={toolingPath} fill="none" stroke="var(--model-grok, #c084fc)" strokeWidth={1.25} strokeDasharray="1.5 3" />
      )}
      {/* prompt rules (secondary) */}
      <path d={rulesPath} fill="none" stroke="var(--text-muted)" strokeWidth={1.25} strokeDasharray="4 3" />
      {/* patterns (primary) */}
      <path d={patternPath} fill="none" stroke="var(--accent)" strokeWidth={1.75} />
      {pts.map((p, i) => (
        <g key={p.id}>
          <circle cx={x(i)} cy={y(p.patterns)} r={3} fill="var(--accent)" stroke="var(--bg)" strokeWidth={1.5}>
            <title>{`${p.id}: ${p.patterns} patterns · ${p.promptRules} prompt rules${p.tooling != null ? ` · ${p.tooling} process/tooling` : ""} — ${p.note}`}</title>
          </circle>
          <text x={x(i)} y={y(p.patterns) - 8} textAnchor="middle" fontFamily={MONO} fontSize={9.5} fontWeight={600} fill="var(--text)">
            {p.patterns}
          </text>
          <circle cx={x(i)} cy={y(p.promptRules)} r={2.25} fill="var(--text-muted)" stroke="var(--bg)" strokeWidth={1.25}>
            <title>{`${p.id}: ${p.promptRules} reviewer-prompt rules`}</title>
          </circle>
          {p.tooling != null && (
            <circle cx={x(i)} cy={y(p.tooling)} r={2.25} fill="var(--model-grok, #c084fc)" stroke="var(--bg)" strokeWidth={1.25}>
              <title>{`${p.id}: ${p.tooling} process/tooling assets (cumulative, sha-cited)`}</title>
            </circle>
          )}
          {/* x-axis tick */}
          <line x1={x(i)} y1={xAxisY} x2={x(i)} y2={xAxisY + 3} stroke={AXIS} strokeWidth={0.75} />
          {/* single rotated x-axis label — -45° prevents overlap on dense series */}
          <text
            x={x(i)}
            y={xAxisY + 6}
            textAnchor="end"
            fontFamily={MONO}
            fontSize={7.5}
            fill={AXIS}
            transform={`rotate(-45, ${x(i)}, ${xAxisY + 6})`}
          >
            {shortId(p.id)} ({p.dateISO.slice(5)})
          </text>
        </g>
      ))}
      {/* stacked legend — sits in padT zone, above the plot, well clear of data.
          Three inline columns so a third series fits without pushing into data. */}
      <g fontFamily={MONO} fontSize={8}>
        {/* col 1: review patterns */}
        <line x1={padL + 2} y1={padT - 22} x2={padL + 18} y2={padT - 22} stroke="var(--accent)" strokeWidth={1.75} />
        <text x={padL + 22} y={padT - 19} fill="var(--text-secondary)">
          review patterns
        </text>
        {/* col 2: reviewer-prompt rules */}
        <line x1={padL + 118} y1={padT - 22} x2={padL + 134} y2={padT - 22} stroke="var(--text-muted)" strokeWidth={1.25} strokeDasharray="4 3" />
        <text x={padL + 138} y={padT - 19} fill="var(--text-secondary)">
          reviewer-prompt rules
        </text>
        {/* col 3: process/tooling (dotted) */}
        <line x1={padL + 258} y1={padT - 22} x2={padL + 274} y2={padT - 22} stroke="var(--model-grok, #c084fc)" strokeWidth={1.25} strokeDasharray="1.5 3" />
        <text x={padL + 278} y={padT - 19} fill="var(--text-secondary)">
          process/tooling (sha-cited)
        </text>
      </g>
    </svg>
  );
}

/* ── (d) Verdict Severity Trend: stacked bars + per-model mean severity ── */

const SEVERITY: Record<Verdict, number> = {
  ACCEPT: 0,
  MINOR: 1,
  MAJOR: 2,
  REJECT: 3,
  NO_VERDICT: -1, // excluded
};

const MODEL_COLORS = {
  ChatGPT: "var(--model-chatgpt)",
  Grok: "var(--model-grok)",
  Gemini: "var(--model-gemini)",
};

/** Sort externalVerdictRounds chronologically by dateISO then roundId. */
function chronologicalVerdictRounds() {
  return [...externalVerdictRounds].sort(
    (a, b) => a.dateISO.localeCompare(b.dateISO) || a.roundId.localeCompare(b.roundId),
  );
}

export function VerdictSeverityTrend() {
  const rounds = chronologicalVerdictRounds();

  // Layout constants
  const padL = 44;
  const padR = 18;
  const padTop = 54; // title + subtitle space
  const barH = 200; // View 1: stacked bar chart
  const gapBetween = 28; // gap between view 1 and view 2
  const lineH = 120; // View 2: per-model severity lines
  const padBot = 72; // room for rotated x-axis labels
  const legendH = 20; // legend row at very bottom of padBot space

  const width = 700;
  const totalH = padTop + barH + gapBetween + lineH + padBot;

  const plotW = width - padL - padR;
  const n = rounds.length;
  const barW = Math.max(8, Math.floor(plotW / n) - 2);
  const barSpacing = plotW / n;

  const xCenter = (i: number) => padL + i * barSpacing + barSpacing / 2;

  // View 1 top/bottom
  const v1Top = padTop;
  const v1Bot = padTop + barH;
  // View 2 top/bottom
  const v2Top = v1Bot + gapBetween;
  const v2Bot = v2Top + lineH;

  const maxCount = 18; // 6 papers × 3 reviewers

  // Y for view 1 (count, 0=bottom)
  const yBar = (count: number) => v1Bot - (count / maxCount) * barH;

  // Y for view 2 (severity 0=ACCEPT at bottom, 3=REJECT at top inverted)
  const maxSev = 3;
  const yLine = (sev: number) => v2Bot - (sev / maxSev) * lineH;

  // Integrity gate date
  const GATE_DATE = "2026-06-26";

  // Find first round at or after gate date
  const gateIdx = rounds.findIndex((r) => r.dateISO >= GATE_DATE);

  // Per-round aggregated data
  const roundData = rounds.map((r) => {
    const counts: Record<Verdict, number> = {
      REJECT: 0, MAJOR: 0, MINOR: 0, ACCEPT: 0, NO_VERDICT: 0,
    };
    const modelSev: Record<string, number[]> = { ChatGPT: [], Grok: [], Gemini: [] };

    for (const paperId of PAPER_IDS) {
      const triple = r.verdicts[paperId as PaperId];
      triple.forEach((v, ri) => {
        counts[v]++;
        if (v !== "NO_VERDICT") {
          const reviewer = REVIEWERS[ri];
          modelSev[reviewer].push(SEVERITY[v]);
        }
      });
    }

    const meanSev = (arr: number[]) =>
      arr.length === 0 ? null : arr.reduce((s, v) => s + v, 0) / arr.length;

    return {
      counts,
      chatgptSev: meanSev(modelSev.ChatGPT),
      grokSev: meanSev(modelSev.Grok),
      geminiSev: meanSev(modelSev.Gemini),
    };
  });

  // Build polyline points for each model
  const modelLine = (key: "chatgptSev" | "grokSev" | "geminiSev") => {
    const pts: string[] = [];
    roundData.forEach((d, i) => {
      const sev = d[key];
      if (sev !== null) {
        pts.push(`${xCenter(i)},${yLine(sev)}`);
      }
    });
    return pts.join(" ");
  };

  // Verdict stacking order bottom → top: ACCEPT, MINOR, MAJOR, REJECT
  const STACK_ORDER: Verdict[] = ["ACCEPT", "MINOR", "MAJOR", "REJECT"];

  const xAxisY = v2Bot;

  return (
    <svg
      viewBox={`0 0 ${width} ${totalH}`}
      role="img"
      aria-label="Verdict severity trend across external rounds"
      className="progress-svg"
    >
      {/* ── Title + subtitle ── */}
      <text
        x={padL}
        y={16}
        fontFamily={MONO}
        fontSize={11.5}
        fontWeight={700}
        fill="var(--text)"
        letterSpacing={0.3}
      >
        Verdict Severity Over Time
      </text>
      <text x={padL} y={32} fontFamily={MONO} fontSize={8} fill={AXIS}>
        Tracks ACCEPT/minor/MAJOR/REJECT across all 6 papers × 3 referees per external round.
      </text>
      <text x={padL} y={44} fontFamily={MONO} fontSize={8} fill={AXIS}>
        Rising MAJOR share after the 06-26 integrity gate = stricter de-biased prompt, not degrading papers.
      </text>

      {/* ── View 1: Stacked bar chart ── */}
      {/* Y grid lines for View 1 */}
      {[0, 6, 12, 18].map((v) => (
        <g key={`v1g-${v}`}>
          <line
            x1={padL} y1={yBar(v)}
            x2={width - padR} y2={yBar(v)}
            stroke={GRID}
            strokeWidth={v === 0 ? 1 : 0.75}
            strokeDasharray={v === 0 ? undefined : "2 4"}
          />
          <text x={padL - 6} y={yBar(v) + 3.5} textAnchor="end" fontFamily={MONO} fontSize={9} fill={AXIS}>
            {v}
          </text>
        </g>
      ))}

      {/* Stacked bars */}
      {rounds.map((_, i) => {
        const d = roundData[i];
        let bottom = 0;
          const segments: { verdict: Verdict; y: number; h: number; count: number }[] = [];
        for (const verdict of STACK_ORDER) {
          const count = d.counts[verdict];
          if (count === 0) { bottom += count; continue; }
          const barHeight = (count / maxCount) * barH;
          segments.push({ verdict, y: yBar(bottom + count), h: barHeight, count });
          bottom += count;
        }
        return (
          <g key={rounds[i].roundId}>
            {segments.map((s) => (
              <rect
                key={s.verdict}
                x={xCenter(i) - barW / 2}
                y={s.y}
                width={barW}
                height={s.h}
                fill={VERDICT_COLOR[s.verdict]}
                fillOpacity={0.85}
              >
                <title>{`${rounds[i].roundId} · ${s.verdict}: ${s.count}`}</title>
              </rect>
            ))}
          </g>
        );
      })}

      {/* View 1 legend (inline, top-right) */}
      {STACK_ORDER.slice().reverse().map((v, i) => (
        <g key={`leg1-${v}`}>
          <rect
            x={width - padR - 100 + i * 25}
            y={v1Top + 4}
            width={10}
            height={10}
            rx={2}
            fill={VERDICT_COLOR[v]}
            fillOpacity={0.85}
          />
          <text
            x={width - padR - 100 + i * 25 + 12}
            y={v1Top + 13}
            fontFamily={MONO}
            fontSize={7}
            fill={AXIS}
          >
            {v === "NO_VERDICT" ? "N/A" : v}
          </text>
        </g>
      ))}

      {/* ── View 2 label ── */}
      <text
        x={padL - 6}
        y={v2Top - 6}
        textAnchor="start"
        fontFamily={MONO}
        fontSize={8.5}
        fill={AXIS}
        letterSpacing={0.4}
      >
        mean severity / model
      </text>

      {/* ── View 2: Per-model severity lines ── */}
      {/* Y grid lines for View 2 */}
      {[0, 1, 2, 3].map((v) => (
        <g key={`v2g-${v}`}>
          <line
            x1={padL} y1={yLine(v)}
            x2={width - padR} y2={yLine(v)}
            stroke={GRID}
            strokeWidth={0.75}
            strokeDasharray="2 4"
          />
          <text x={padL - 6} y={yLine(v) + 3.5} textAnchor="end" fontFamily={MONO} fontSize={8} fill={AXIS}>
            {["A", "m", "M", "R"][v]}
          </text>
        </g>
      ))}

      {/* Model lines */}
      {(["ChatGPT", "Grok", "Gemini"] as const).map((model) => {
        const key = model === "ChatGPT" ? "chatgptSev" : model === "Grok" ? "grokSev" : "geminiSev";
        const pts = modelLine(key);
        if (!pts) return null;
        return (
          <polyline
            key={model}
            points={pts}
            fill="none"
            stroke={MODEL_COLORS[model]}
            strokeWidth={1.5}
            strokeLinejoin="round"
            opacity={0.9}
          />
        );
      })}

      {/* Model dots */}
      {(["ChatGPT", "Grok", "Gemini"] as const).map((model) => {
        const key = model === "ChatGPT" ? "chatgptSev" : model === "Grok" ? "grokSev" : "geminiSev";
        return roundData.map((d, i) => {
          const sev = d[key];
          if (sev === null) return null;
          return (
            <circle
              key={`${model}-${i}`}
              cx={xCenter(i)}
              cy={yLine(sev)}
              r={2.5}
              fill={MODEL_COLORS[model]}
              stroke="var(--bg)"
              strokeWidth={1}
            >
              <title>{`${rounds[i].roundId} · ${model}: ${sev.toFixed(2)}`}</title>
            </circle>
          );
        });
      })}

      {/* View 2 legend */}
      {(["ChatGPT", "Grok", "Gemini"] as const).map((model, i) => (
        <g key={`leg2-${model}`}>
          <line
            x1={padL + i * 80}
            y1={v2Top + 8}
            x2={padL + i * 80 + 16}
            y2={v2Top + 8}
            stroke={MODEL_COLORS[model]}
            strokeWidth={1.5}
          />
          <text
            x={padL + i * 80 + 20}
            y={v2Top + 12}
            fontFamily={MONO}
            fontSize={8}
            fill={AXIS}
          >
            {model}
          </text>
        </g>
      ))}

      {/* ── Integrity gate vertical dashed line ── */}
      {gateIdx >= 0 && (
        <g>
          {/* Gate line in View 1 */}
          <line
            x1={xCenter(gateIdx)}
            y1={v1Top}
            x2={xCenter(gateIdx)}
            y2={v1Bot}
            stroke="var(--warn)"
            strokeWidth={1}
            strokeDasharray="3 3"
            opacity={0.75}
          />
          {/* Gate line in View 2 */}
          <line
            x1={xCenter(gateIdx)}
            y1={v2Top}
            x2={xCenter(gateIdx)}
            y2={v2Bot}
            stroke="var(--warn)"
            strokeWidth={1}
            strokeDasharray="3 3"
            opacity={0.75}
          />
          {/* Gate label between views */}
          <text
            x={xCenter(gateIdx) + 4}
            y={v1Bot + gapBetween / 2 + 3}
            fontFamily={MONO}
            fontSize={7.5}
            fill="var(--warn)"
            opacity={0.9}
          >
            Integrity gate 06-26
          </text>
        </g>
      )}

      {/* ── X-axis ticks + rotated labels (shared) ── */}
      {rounds.map((r, i) => {
        const cx = xCenter(i);
        const labelY = xAxisY + 5;
        return (
          <g key={`xlabel-${r.roundId}`}>
            <line x1={cx} y1={xAxisY} x2={cx} y2={xAxisY + 3} stroke={AXIS} strokeWidth={0.75} />
            <text
              x={cx}
              y={labelY}
              textAnchor="end"
              fontFamily={MONO}
              fontSize={7.5}
              fill={AXIS}
              transform={`rotate(-50, ${cx}, ${labelY})`}
            >
              {r.roundId}
              <tspan fill={AXIS} opacity={0.65}> {r.dateISO.slice(5)}</tspan>
            </text>
          </g>
        );
      })}
    </svg>
  );
}

/* ── Readiness strip: sparse per-paper checkpoints (95-cap rule) ──────── */

// Per-paper readiness — sourced directly from papers.ts (the canonical static
// mirror of Convex readinessComputed) so this strip can never drift the way the
// old hardcoded 2026-07-15 snapshot did. All six papers remain IN REVISION;
// automated verdict labels inform the record but are not journal acceptance.
const READINESS_BY_SLUG: Record<PaperId, string> = {
  P1A: "paper-1a",
  P1B: "paper-1b",
  P2: "paper-2",
  P3: "paper-3",
  P4: "paper-4",
  P5: "paper-5",
};
const PER_PAPER_READINESS: Record<PaperId, number> = PAPER_IDS.reduce(
  (acc, p) => {
    const slug = READINESS_BY_SLUG[p as PaperId];
    acc[p as PaperId] = papers.find((pp) => pp.slug === slug)?.readiness ?? 0;
    return acc;
  },
  {} as Record<PaperId, number>,
);

export function ReadinessStrip() {
  const cps = readinessCheckpoints;
  const last = cps[cps.length - 1];
  const avg = Math.round(
    (Object.values(PER_PAPER_READINESS) as number[]).reduce((a, b) => a + b, 0) /
      Object.keys(PER_PAPER_READINESS).length,
  );
  return (
    <div className="readiness-strip" title="Canonical evidence-capped readiness, sourced from papers.ts. All papers remain IN REVISION; automated verdict labels are not journal acceptance.">
      <span className="readiness-strip-label">Program readiness · evidence-capped, avg {avg}% · all papers IN REVISION</span>
      {PAPER_IDS.map((p) => {
        const r = PER_PAPER_READINESS[p as PaperId];
        const trail = cps
          .filter((c) => typeof c.values[p as PaperId] === "number")
          .map((c) => `${c.id} ${c.values[p as PaperId]}%`)
          .join(" → ");
        void last;
        return (
          <span key={p} className="readiness-chip" title={`${p}: ${trail} → ${r}% (canonical evidence cap, sourced from papers.ts; IN REVISION)`}>
            <span className="gap-delta-paper">{p}</span> {r}%
          </span>
        );
      })}
    </div>
  );
}
