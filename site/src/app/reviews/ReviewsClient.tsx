"use client";

/**
 * Client filter controller for the /reviews feed. The feed entries themselves
 * are SERVER-rendered by page.tsx (full content in the static HTML); this
 * component only reads ?papers=&kinds= URL state, renders the filter chips,
 * and toggles visibility of the server-rendered entries via their
 * data-papers / data-kind attributes. No round content lives here.
 */
import { useCallback, useEffect, useMemo, useState } from "react";
import { useSearchParams } from "next/navigation";
import { PAPER_IDS, type PaperId } from "@/data/reviewTimeline";
import { KIND_GROUPS, type KindGroup } from "./ReviewEntry";

function parseList<T extends string>(raw: string | null, valid: readonly T[]): T[] {
  if (!raw) return [];
  const set = new Set(valid);
  return raw
    .split(",")
    .map((s) => s.trim().toUpperCase() as T)
    .filter((s) => set.has(s));
}

export default function ReviewsClient({ totalRounds }: { totalRounds: number }) {
  const searchParams = useSearchParams();
  const [visibleCount, setVisibleCount] = useState(totalRounds);

  const selectedPapers = useMemo(
    () => parseList<PaperId>(searchParams.get("papers"), PAPER_IDS),
    [searchParams],
  );
  const selectedKinds = useMemo(
    () => parseList<KindGroup>(searchParams.get("kinds"), KIND_GROUPS),
    [searchParams],
  );

  const setParams = useCallback(
    (papers: PaperId[], kinds: KindGroup[]) => {
      const params = new URLSearchParams(window.location.search);
      if (papers.length > 0) params.set("papers", papers.join(","));
      else params.delete("papers");
      if (kinds.length > 0) params.set("kinds", kinds.join(","));
      else params.delete("kinds");
      const qs = params.toString();
      window.history.replaceState(null, "", qs ? `?${qs}` : window.location.pathname);
    },
    [],
  );

  const togglePaper = (p: PaperId) => {
    const next = selectedPapers.includes(p)
      ? selectedPapers.filter((x) => x !== p)
      : [...selectedPapers, p];
    setParams(next, selectedKinds);
  };

  const toggleKind = (k: KindGroup) => {
    const next = selectedKinds.includes(k)
      ? selectedKinds.filter((x) => x !== k)
      : [...selectedKinds, k];
    setParams(selectedPapers, next);
  };

  // Overlay the filter state onto the server-rendered feed.
  useEffect(() => {
    const feed = document.getElementById("review-feed");
    if (!feed) return;
    const entries = Array.from(feed.querySelectorAll<HTMLElement>(".review-entry"));
    let visible = 0;
    for (const el of entries) {
      const papers = (el.dataset.papers ?? "").split(" ");
      const kind = (el.dataset.kind ?? "") as KindGroup;
      const show =
        (selectedPapers.length === 0 ||
          papers.some((p) => selectedPapers.includes(p as PaperId))) &&
        (selectedKinds.length === 0 || selectedKinds.includes(kind));
      el.hidden = !show;
      if (show) visible++;
    }
    const empty = feed.querySelector<HTMLElement>("[data-feed-empty]");
    if (empty) empty.hidden = visible > 0;
    setVisibleCount(visible);
  }, [selectedPapers, selectedKinds]);

  const hasFilter = selectedPapers.length > 0 || selectedKinds.length > 0;

  return (
    <div className="review-filters" role="group" aria-label="Filter the review feed">
      <div className="review-filter-row">
        <span className="review-filter-label">papers</span>
        {PAPER_IDS.map((p) => (
          <button
            key={p}
            type="button"
            className={selectedPapers.includes(p) ? "filter-chip is-active" : "filter-chip"}
            aria-pressed={selectedPapers.includes(p)}
            onClick={() => togglePaper(p)}
          >
            {p}
          </button>
        ))}
      </div>
      <div className="review-filter-row">
        <span className="review-filter-label">kind</span>
        {KIND_GROUPS.map((k) => (
          <button
            key={k}
            type="button"
            className={selectedKinds.includes(k) ? "filter-chip is-active" : "filter-chip"}
            aria-pressed={selectedKinds.includes(k)}
            onClick={() => toggleKind(k)}
          >
            {k}
          </button>
        ))}
        {hasFilter && (
          <button type="button" className="filter-chip filter-clear" onClick={() => setParams([], [])}>
            clear
          </button>
        )}
      </div>
      <div className="review-filter-count">
        {visibleCount} of {totalRounds} rounds
      </div>
    </div>
  );
}
