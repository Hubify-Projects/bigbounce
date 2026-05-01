"use client";

import { useEffect } from "react";
import { liveStatus } from "@/data/live-status";

const REFRESH_MS = 15 * 60 * 1000;

export function LiveStatus() {
  const { lastUpdatedDisplay, headline, summary, papers, blockerTally, cronStatus, etaToCompletion, pods } =
    liveStatus;
  const avgReadiness = Math.round(
    papers.reduce((acc, p) => acc + p.readiness, 0) / papers.length,
  );

  useEffect(() => {
    const id = setInterval(() => {
      window.location.reload();
    }, REFRESH_MS);
    return () => clearInterval(id);
  }, []);

  return (
    <aside className="live-status" aria-label="Live build status">
      <div className="live-status-row live-status-row-primary">
        <span className="live-status-pulse" aria-hidden="true" />
        <span className="live-status-stamp">last update {lastUpdatedDisplay}</span>
        <span className="live-status-sep" aria-hidden="true">·</span>
        <span className="live-status-headline">{headline}</span>
      </div>
      <p className="live-status-summary">{summary}</p>
      <div className="live-status-grid">
        <ol className="live-status-papers" aria-label="Paper readiness">
          {papers.map((p) => (
            <li key={p.slug} className="live-status-paper">
              <span className="live-status-paper-id">P{p.number}</span>
              <span className="live-status-paper-title">{p.shortTitle}</span>
              <span className="live-status-paper-version">{p.version}</span>
              <span className="live-status-paper-bar" aria-hidden="true">
                <span
                  className="live-status-paper-fill"
                  style={{ width: `${p.readiness}%` }}
                />
              </span>
              <span className="live-status-paper-pct">{p.readiness}%</span>
            </li>
          ))}
        </ol>
        <dl className="live-status-stats">
          <div>
            <dt>avg readiness</dt>
            <dd>{avgReadiness}%</dd>
          </div>
          <div>
            <dt>BLOCKERs closed / open</dt>
            <dd>
              {blockerTally.closed} / {blockerTally.openBlockers}
            </dd>
          </div>
          <div>
            <dt>open MAJOR / MINOR</dt>
            <dd>
              {blockerTally.openMajors} / {blockerTally.openMinors}
            </dd>
          </div>
          <div>
            <dt>cron</dt>
            <dd>{cronStatus}</dd>
          </div>
        </dl>
      </div>
      {pods.length > 0 && (
        <ul className="live-status-pods" aria-label="Pod status">
          {pods.map((pod) => (
            <li key={pod.name} data-state={pod.state}>
              <span className="live-status-pod-dot" aria-hidden="true" />
              <span className="live-status-pod-name">{pod.name}</span>
              <span className="live-status-pod-note">{pod.note}</span>
            </li>
          ))}
        </ul>
      )}
      <p className="live-status-eta">{etaToCompletion}</p>
    </aside>
  );
}
