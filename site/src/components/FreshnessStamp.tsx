"use client";

import { useEffect, useState } from "react";

/**
 * FreshnessStamp — the anti-drift primitive.
 *
 * The bug this exists to prevent: the homepage rendered an eight-day-old
 * clean-wave number as if it were current, because the number was computed at
 * build time and nothing on the page carried a timestamp the reader could check.
 *
 * A statically-rendered page cannot age-check itself: if the site is not
 * rebuilt, a server-computed "1 day ago" stays "1 day ago" forever. So the
 * server sends only the raw epoch-ms of the newest evidence and this client
 * component computes the age against the VIEWER'S clock, after mount. A build
 * frozen for eight days therefore reads "8 days ago · STALE" in the browser,
 * with no rebuild and no agent action required.
 *
 * It renders nothing on the server pass (avoiding hydration mismatch) and fills
 * in on mount. `onStale` lets the parent widget switch its own copy to the
 * stale variant.
 */
export function FreshnessStamp({
  evidenceMs,
  staleAfterDays,
  onStale,
}: {
  evidenceMs: number;
  staleAfterDays: number;
  onStale?: (stale: boolean) => void;
}) {
  const [ageText, setAgeText] = useState<string | null>(null);
  const [stale, setStale] = useState(false);

  useEffect(() => {
    function tick() {
      if (!evidenceMs) {
        setAgeText("no evidence timestamp recorded");
        setStale(true);
        onStale?.(true);
        return;
      }
      const ms = Date.now() - evidenceMs;
      const hours = ms / 3_600_000;
      const days = hours / 24;
      const text =
        hours < 1
          ? "just now"
          : hours < 24
            ? `${Math.round(hours)} h ago`
            : `${Math.round(days)} d ago`;
      const isStale = days > staleAfterDays;
      setAgeText(text);
      setStale(isStale);
      onStale?.(isStale);
    }
    tick();
    // Re-check every 10 minutes so a long-open tab also ages honestly.
    const id = setInterval(tick, 600_000);
    return () => clearInterval(id);
  }, [evidenceMs, staleAfterDays, onStale]);

  if (ageText === null) return null;

  return (
    <span
      style={{
        fontFamily: "var(--font-mono-stack)",
        fontSize: "0.64rem",
        color: stale ? "var(--warn)" : "var(--text-muted)",
      }}
    >
      {" · "}
      {ageText}
      {stale ? " · STALE" : ""}
    </span>
  );
}

/**
 * StaleBanner — shown only when the evidence is older than the threshold,
 * decided on the client for the same reason as above.
 */
export function StaleBanner({
  evidenceMs,
  staleAfterDays,
  asOf,
}: {
  evidenceMs: number;
  staleAfterDays: number;
  asOf: string;
}) {
  const [stale, setStale] = useState(false);
  const [ageDays, setAgeDays] = useState(0);

  useEffect(() => {
    function tick() {
      if (!evidenceMs) {
        setStale(true);
        setAgeDays(0);
        return;
      }
      const days = (Date.now() - evidenceMs) / 86_400_000;
      setStale(days > staleAfterDays);
      setAgeDays(Math.round(days));
    }
    tick();
    const id = setInterval(tick, 600_000);
    return () => clearInterval(id);
  }, [evidenceMs, staleAfterDays]);

  if (!stale) return null;

  return (
    <p
      style={{
        margin: "0 0 14px 0",
        padding: "8px 10px",
        borderLeft: "3px solid var(--warn)",
        fontFamily: "var(--font-mono-stack)",
        fontSize: "0.7rem",
        lineHeight: 1.5,
        color: "var(--warn)",
      }}
    >
      STALE — no version bump or review board has been recorded for{" "}
      {evidenceMs ? `${ageDays} day${ageDays === 1 ? "" : "s"}` : "an unknown period"}. Everything below is
      the state as of {asOf}, not as of today. Treat it as a snapshot until the
      loop writes again.
    </p>
  );
}
