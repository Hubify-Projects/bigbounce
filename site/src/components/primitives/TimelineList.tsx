import type { ReactNode } from "react";
import { cn } from "@/lib/utils";

export interface TimelineEntry {
  id: string;
  dateISO: string;
  kind: string;
  title: string;
  summary?: ReactNode;
  href?: string;
  /** Kinds rendered with the quiet skill-improvement marker. */
  quiet?: boolean;
}

export interface TimelineListProps {
  entries: TimelineEntry[];
  className?: string;
  /** Cap the number of rows rendered (server pagination point per §3.6). */
  limit?: number;
}

/**
 * Reverse-chronological one-line-per-entry timeline (REDESIGN_SPEC.md §3.6,
 * §5.1 #9). `kind:"skill-improvement"` entries render with a quiet marker
 * instead of the normal kind label. Hairline-separated rows only.
 */
export function TimelineList({ entries, className, limit }: TimelineListProps) {
  const shown = typeof limit === "number" ? entries.slice(0, limit) : entries;
  return (
    <div className={cn("timeline-list", className)}>
      {shown.map((e) => {
        const body = (
          <>
            <span className="timeline-list-date mono">{e.dateISO}</span>
            <span
              className={cn(
                "timeline-list-kind mono",
                e.quiet && "timeline-list-kind-quiet",
              )}
            >
              {e.quiet ? "· skill improvement" : e.kind}
            </span>
            <span className="timeline-list-title">{e.title}</span>
          </>
        );
        return (
          <div key={e.id} className="timeline-list-row">
            {e.href ? (
              <a href={e.href} className="timeline-list-link">
                {body}
              </a>
            ) : (
              body
            )}
            {e.summary && <p className="timeline-list-summary">{e.summary}</p>}
          </div>
        );
      })}
      {shown.length === 0 && (
        <p className="timeline-list-empty">Nothing recorded yet.</p>
      )}
    </div>
  );
}
