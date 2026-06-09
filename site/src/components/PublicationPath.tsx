import type { Paper, PublicationStage, StageState } from "@/data/papers";
import { pathSummary } from "@/data/papers";

const STATE_COLOR: Record<StageState, string> = {
  done: "#16a34a",
  active: "#0369a1",
  blocked: "#d97706",
  pending: "var(--border)",
};

const STATE_LABEL: Record<StageState, string> = {
  done: "done",
  active: "in progress",
  blocked: "waiting on Houston",
  pending: "queued",
};

/** Vertical 6-stage path-to-publication tracker for paper detail pages. */
export function PublicationPath({ stages }: { stages: PublicationStage[] }) {
  return (
    <ol style={{ listStyle: "none", margin: 0, padding: 0 }}>
      {stages.map((stage, i) => {
        const color = STATE_COLOR[stage.state];
        const isLast = i === stages.length - 1;
        return (
          <li
            key={stage.label}
            style={{
              display: "grid",
              gridTemplateColumns: "18px minmax(0,1fr)",
              gap: 12,
            }}
          >
            <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
              <span
                aria-hidden="true"
                style={{
                  width: 12,
                  height: 12,
                  marginTop: 4,
                  borderRadius: "50%",
                  flexShrink: 0,
                  background: stage.state === "pending" ? "transparent" : color,
                  border: `2px solid ${stage.state === "pending" ? "var(--border)" : color}`,
                  boxShadow:
                    stage.state === "active" ? "0 0 0 3px rgba(3,105,161,0.18)" : undefined,
                }}
              />
              {!isLast && (
                <span
                  aria-hidden="true"
                  style={{
                    width: 2,
                    flex: 1,
                    minHeight: 14,
                    background:
                      stage.state === "done" ? "rgba(22,163,74,0.35)" : "var(--border)",
                  }}
                />
              )}
            </div>
            <div style={{ paddingBottom: isLast ? 0 : 14 }}>
              <div
                style={{
                  display: "flex",
                  flexWrap: "wrap",
                  alignItems: "baseline",
                  gap: 8,
                }}
              >
                <span
                  style={{
                    fontSize: "0.88rem",
                    fontWeight: stage.state === "active" || stage.state === "blocked" ? 600 : 500,
                    color: stage.state === "pending" ? "var(--text-muted)" : "var(--text)",
                  }}
                >
                  {stage.label}
                </span>
                <span
                  style={{
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: "0.66rem",
                    letterSpacing: "0.05em",
                    textTransform: "uppercase",
                    color: stage.state === "pending" ? "var(--text-muted)" : color,
                  }}
                >
                  {STATE_LABEL[stage.state]}
                </span>
              </div>
              {stage.note && (
                <p
                  style={{
                    margin: "2px 0 0 0",
                    fontSize: "0.76rem",
                    lineHeight: 1.45,
                    color: "var(--text-muted)",
                  }}
                >
                  {stage.note}
                </p>
              )}
            </div>
          </li>
        );
      })}
    </ol>
  );
}

/** One-line segmented strip + current gate, for list rows and cards. */
export function PublicationPathCompact({ paper }: { paper: Paper }) {
  const { done, total, current } = pathSummary(paper);
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        flexWrap: "wrap",
        gap: 8,
      }}
    >
      <span
        aria-label={`${done} of ${total} publication stages complete`}
        style={{ display: "inline-flex", gap: 3 }}
      >
        {paper.path.map((stage) => (
          <span
            key={stage.label}
            title={`${stage.label} — ${STATE_LABEL[stage.state]}`}
            style={{
              width: 16,
              height: 5,
              borderRadius: 2,
              background:
                stage.state === "pending" ? "var(--border)" : STATE_COLOR[stage.state],
              opacity: stage.state === "done" ? 0.85 : 1,
            }}
          />
        ))}
      </span>
      <span
        style={{
          fontFamily: "var(--font-mono-stack)",
          fontSize: "0.7rem",
          color: "var(--text-muted)",
          whiteSpace: "nowrap",
        }}
      >
        {done}/{total}
        {current ? ` · next: ${current.label.toLowerCase()}` : " · complete"}
      </span>
    </div>
  );
}
