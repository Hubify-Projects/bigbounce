import { cn } from "@/lib/utils";

export type GridVerdict = "REJECT" | "MAJOR" | "MINOR" | "ACCEPT" | "NO_VERDICT";

export interface VerdictGridRound {
  roundId: string;
  dateISO: string;
  /** One verdict per leg, in `legLabels` order. */
  verdicts: GridVerdict[];
}

export interface VerdictGridRow {
  work: string;
  rounds: VerdictGridRound[];
}

export interface VerdictGridProps {
  /** Leg labels in verdict-array order, e.g. ["ChatGPT", "Grok", "Gemini"]. */
  legLabels: string[];
  /** Indices into legLabels counted toward the all-A meter. */
  activeLegIndices: number[];
  /** Indices into legLabels displayed greyed with a "frozen" note. */
  frozenLegIndices: number[];
  rows: VerdictGridRow[];
  /** Cap on rounds shown, newest-left. */
  maxRounds?: number;
  className?: string;
}

const VERDICT_LETTER: Record<GridVerdict, string> = {
  REJECT: "R",
  MAJOR: "M",
  MINOR: "m",
  ACCEPT: "A",
  NO_VERDICT: "—",
};

/**
 * Newest-round-left verdict grid (REDESIGN_SPEC.md §3.6, §5.1 #8). Rows are
 * works, columns are rounds; each cell packs one letter per active leg plus
 * a greyed letter per frozen leg. Never deletes a frozen leg's history —
 * shown dimmed with a footnote, per directive M-AMENDED.
 */
export function VerdictGrid({
  legLabels,
  activeLegIndices,
  frozenLegIndices,
  rows,
  maxRounds = 10,
  className,
}: VerdictGridProps) {
  return (
    <div className={cn("verdict-grid-wrap", className)}>
      <div className="data-table-wrap">
        <table className="data-table verdict-grid">
          <thead>
            <tr>
              <th>Work</th>
              {rows[0]?.rounds.slice(0, maxRounds).map((r) => (
                <th key={r.roundId} className="mono align-right" title={r.dateISO}>
                  {r.roundId}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.work}>
                <td className="mono">{row.work}</td>
                {row.rounds.slice(0, maxRounds).map((r) => (
                  <td key={r.roundId} className="align-right mono verdict-grid-cell">
                    {r.verdicts.map((v, i) => {
                      const isFrozen = frozenLegIndices.includes(i);
                      const isActive = activeLegIndices.includes(i);
                      return (
                        <span
                          key={i}
                          className={cn(
                            "verdict-grid-letter",
                            `verdict-grid-${v.toLowerCase()}`,
                            isFrozen && "verdict-grid-frozen",
                            !isActive && !isFrozen && "verdict-grid-inactive",
                          )}
                          title={`${legLabels[i]}: ${v}`}
                        >
                          {VERDICT_LETTER[v]}
                        </span>
                      );
                    })}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {frozenLegIndices.length > 0 && (
        <p className="verdict-grid-note">
          {frozenLegIndices.map((i) => legLabels[i]).join(", ")} column
          {frozenLegIndices.length === 1 ? " is" : "s are"} frozen, not counted — paused
          under standing directive N; history is preserved, never deleted or faked.
        </p>
      )}
    </div>
  );
}
