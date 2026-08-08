"use client";

/**
 * ChartShell — a reusable chart frame with an "Expand ⤢" affordance that opens
 * a full-viewport modal for exploring a cramped chart at readable size.
 *
 * Houston 2026-07-10: "these charts need to be able to be viewed in an expanded
 * more full page view … there is too much data crammed here and it looks too
 * small and unreadable to the human eye."
 *
 * Usage: wrap any chart in <ChartShell title="…">{<Chart/>}</ChartShell>.
 * The children render inline (compact). When expanded, the modal renders either
 * the same children OR an optional `expandedContent` node — used by the verdict
 * trajectory chart to swap in a full-history, all-labels rendering.
 *
 * Clean Vercel-like: one outer boundary (no nested boxes), generous spacing,
 * full-viewport modal that uses the whole width/height.
 */
import { useEffect, useState, type ReactNode } from "react";
import { createPortal } from "react-dom";

const MONO = "var(--font-mono-stack)";

export function ChartShell({
  title,
  children,
  expandedContent,
  hint,
}: {
  title: string;
  children: ReactNode;
  /** Optional richer node shown only in the expanded modal (defaults to children). */
  expandedContent?: ReactNode;
  /** Optional short hint shown by the expand control inline (e.g. "last 15 of 52"). */
  hint?: ReactNode;
}) {
  const [open, setOpen] = useState(false);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    const timer = window.setTimeout(() => setMounted(true), 0);
    return () => window.clearTimeout(timer);
  }, []);

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    document.addEventListener("keydown", onKey);
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = prev;
    };
  }, [open]);

  return (
    <div className="chart-shell">
      <div className="chart-shell-head">
        {hint ? <span className="chart-shell-hint">{hint}</span> : <span />}
        <button
          type="button"
          className="chart-expand-btn"
          onClick={() => setOpen(true)}
          aria-label={`Expand ${title} to full-page view`}
          title="Expand to full-page view"
        >
          Expand <span aria-hidden>⤢</span>
        </button>
      </div>
      <div className="chart-shell-body">{children}</div>

      {mounted && open
        ? createPortal(
            <div
              className="chart-modal-overlay"
              role="dialog"
              aria-modal="true"
              aria-label={`${title} — full-page view`}
              onClick={(e) => {
                if (e.target === e.currentTarget) setOpen(false);
              }}
            >
              <div className="chart-modal">
                <div className="chart-modal-head">
                  <h2 className="chart-modal-title">{title}</h2>
                  <button
                    type="button"
                    className="chart-modal-close"
                    onClick={() => setOpen(false)}
                    aria-label="Close full-page view"
                  >
                    Close <span aria-hidden>✕</span>
                  </button>
                </div>
                <div className="chart-modal-body">{expandedContent ?? children}</div>
                <p className="chart-modal-foot" style={{ fontFamily: MONO }}>
                  Esc or click outside to close · scroll horizontally to explore the full history
                </p>
              </div>
            </div>,
            document.body,
          )
        : null}
    </div>
  );
}
