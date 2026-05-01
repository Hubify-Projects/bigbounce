"use client";

import { useEffect, useState } from "react";
import { ChevronDown, ChevronUp } from "lucide-react";
import { liveStatus } from "@/data/live-status";

const REFRESH_MS = 15 * 60 * 1000;
const STORAGE_KEY = "bigbounce-live-status-expanded";

function formatCountdown(msLeft: number): string {
  const total = Math.max(0, Math.floor(msLeft / 1000));
  const m = Math.floor(total / 60);
  const s = total % 60;
  return `${m}:${s.toString().padStart(2, "0")}`;
}

export function LiveStatus() {
  const {
    lastUpdatedDisplay,
    headline,
    summary,
    papers,
    blockerTally,
    cronStatus,
    etaToCompletion,
    pods,
  } = liveStatus;
  const avgReadiness = Math.round(
    papers.reduce((acc, p) => acc + p.readiness, 0) / papers.length,
  );

  const [expanded, setExpanded] = useState(false);
  const [msLeft, setMsLeft] = useState(REFRESH_MS);

  useEffect(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved === "true") setExpanded(true);
    } catch {}
  }, []);

  useEffect(() => {
    const mountedAt = Date.now();
    const tickId = setInterval(() => {
      const elapsed = Date.now() - mountedAt;
      setMsLeft(Math.max(0, REFRESH_MS - elapsed));
    }, 1000);
    const refreshId = setInterval(() => {
      window.location.reload();
    }, REFRESH_MS);
    return () => {
      clearInterval(tickId);
      clearInterval(refreshId);
    };
  }, []);

  function toggle() {
    setExpanded((prev) => {
      const next = !prev;
      try {
        localStorage.setItem(STORAGE_KEY, next ? "true" : "false");
      } catch {}
      return next;
    });
  }

  return (
    <aside
      className={`live-status ${expanded ? "is-expanded" : "is-compact"}`}
      aria-label="Live build status"
    >
      <button
        type="button"
        className="live-status-compact-row"
        onClick={toggle}
        aria-expanded={expanded}
        aria-controls="live-status-detail"
      >
        <span className="live-status-pulse" aria-hidden="true" />
        <span className="live-status-compact-stamp">
          {lastUpdatedDisplay}
        </span>
        <span className="live-status-compact-bar" aria-hidden="true">
          <span
            className="live-status-compact-fill"
            style={{ width: `${avgReadiness}%` }}
          />
        </span>
        <span className="live-status-compact-pct">{avgReadiness}% ready</span>
        <span className="live-status-compact-eta">
          next refresh {formatCountdown(msLeft)}
        </span>
        <span className="live-status-compact-toggle" aria-hidden="true">
          {expanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
        </span>
      </button>

      {expanded && (
        <div id="live-status-detail" className="live-status-detail">
          <p className="live-status-headline-row">{headline}</p>
          <p className="live-status-summary">{summary}</p>
          <div className="live-status-grid">
            <ol className="live-status-papers" aria-label="Paper readiness">
              {papers.map((p) => (
                <li key={p.slug} className="live-status-paper">
                  <span className="live-status-paper-id">P{p.number}</span>
                  <span className="live-status-paper-title">
                    {p.shortTitle}
                  </span>
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
        </div>
      )}
    </aside>
  );
}
