import { cn } from "@/lib/utils";

export interface ReadinessSegment {
  label: string;
  max: number;
  earned: number;
}

export interface ReadinessBarProps {
  value: number;
  segments?: ReadinessSegment[];
  className?: string;
}

/**
 * Readiness meter — a single hairline track, filled with the accent, plus an
 * optional segment breakdown underneath (REDESIGN_SPEC.md §5.1 #7). Value is
 * a Convex-sourced number; never hand-write a readiness literal.
 */
export function ReadinessBar({ value, segments, className }: ReadinessBarProps) {
  const clamped = Math.max(0, Math.min(100, value));
  return (
    <div className={cn("readiness-bar", className)}>
      <div className="readiness-bar-row">
        <span className="readiness-bar-track" aria-hidden="true">
          <span className="readiness-bar-fill" style={{ width: `${clamped}%` }} />
        </span>
        <span className="readiness-bar-value mono">{clamped}%</span>
      </div>
      {segments && segments.length > 0 && (
        <div className="readiness-bar-segments mono">
          {segments.map((s) => (
            <span key={s.label} className="readiness-bar-segment">
              {s.label} {s.earned}/{s.max}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}
