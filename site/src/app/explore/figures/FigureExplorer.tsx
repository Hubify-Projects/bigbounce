"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import Link from "next/link";
import type { Figure, FigureSection } from "@/data/figures";
import { Search } from "lucide-react";
import { Dialog, DialogContent, DialogTitle, DialogDescription } from "@/components/ui/dialog";

interface FigureExplorerProps {
  sections: FigureSection[];
}

type FigureTrack = "P1A" | "P1B" | "P2" | "P3" | "P4" | "P5" | "X";

interface EnrichedFigure extends Figure {
  sectionTitle: string;
  track: FigureTrack;
  figureIndex: number;
}

function trackKey(title: string): FigureTrack {
  const m = title.match(/Paper\s+(1A|1B|[2-5])/i);
  if (m) return `P${m[1].toUpperCase()}` as FigureTrack;
  return "X";
}

function trackSlug(key: FigureTrack): string | null {
  if (key === "X") return null;
  return `paper-${key.replace("P", "").toLowerCase()}`;
}

function figureNumberValue(number: string) {
  const match = number.match(/\d+/);
  return match ? Number(match[0]) : 9999;
}

const FILTERS: Array<{ key: "all" | FigureTrack; label: string }> = [
  { key: "all", label: "All" },
  { key: "P1A", label: "Paper 1A" },
  { key: "P1B", label: "P1B" },
  { key: "P2", label: "Paper 2" },
  { key: "P3", label: "P3" },
  { key: "P4", label: "Paper 4" },
  { key: "P5", label: "P5" },
  { key: "X", label: "Cross-cutting" },
];

/**
 * Filterable figure gallery (REDESIGN_SPEC.md §3.8, §2.4 "/figures ->
 * /explore/figures"). Filter row is text toggles, not bordered chips
 * (§3.2); the grid itself has no per-figure card border — a hairline
 * separates rows, the lightbox (Dialog) is the one legitimate bordered
 * surface here.
 */
export function FigureExplorer({ sections }: FigureExplorerProps) {
  const [activeIndex, setActiveIndex] = useState<number | null>(null);
  const [filter, setFilter] = useState<typeof FILTERS[number]["key"]>("all");
  const [query, setQuery] = useState("");

  const allFigures = useMemo<EnrichedFigure[]>(
    () =>
      sections.flatMap((section) =>
        section.items.map((fig) => ({
          ...fig,
          sectionTitle: section.title,
          track: trackKey(section.title),
          figureIndex: figureNumberValue(fig.number),
        })),
      ),
    [sections],
  );

  const visible = useMemo(() => {
    const q = query.trim().toLowerCase();
    return allFigures
      .filter((fig) => filter === "all" || fig.track === filter)
      .filter((fig) => {
        if (!q) return true;
        return [fig.title, fig.desc, fig.number, fig.source]
          .join(" ")
          .toLowerCase()
          .includes(q);
      })
      .sort((a, b) => a.figureIndex - b.figureIndex);
  }, [allFigures, filter, query]);

  const active = activeIndex === null ? null : (visible[activeIndex] ?? null);

  const step = useCallback(
    (delta: number) => {
      setActiveIndex((prev) => {
        if (prev === null || visible.length === 0) return prev;
        return (prev + delta + visible.length) % visible.length;
      });
    },
    [visible.length],
  );

  useEffect(() => {
    if (activeIndex === null) return;
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "ArrowRight") step(1);
      else if (e.key === "ArrowLeft") step(-1);
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [activeIndex, step]);

  return (
    <div className="figure-explorer">
      <div className="figure-explorer-toolbar">
        <div className="figure-explorer-filters">
          {FILTERS.map((f) => (
            <button
              key={f.key}
              type="button"
              onClick={() => setFilter(f.key)}
              className={`figure-explorer-filter${filter === f.key ? " is-active" : ""}`}
            >
              {f.label}
            </button>
          ))}
        </div>
        <div className="figure-explorer-search">
          <Search size={14} aria-hidden="true" />
          <input
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search figures"
            aria-label="Search figures"
          />
        </div>
        <span className="row-purpose mono">{visible.length} of {allFigures.length}</span>
      </div>

      {visible.length === 0 ? (
        <p className="row-purpose" style={{ padding: "24px 0" }}>No figures match this filter.</p>
      ) : (
        <div className="figure-explorer-grid">
          {visible.map((fig, i) => (
            <button
              key={`${fig.sectionTitle}-${fig.number}`}
              type="button"
              className="figure-explorer-item"
              onClick={() => setActiveIndex(i)}
            >
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={fig.src} alt={fig.alt} loading="lazy" className="figure-explorer-thumb" />
              <span className="figure-explorer-item-body">
                <span className="figure-explorer-item-number mono">{fig.number}</span>
                <span className="figure-explorer-item-title">{fig.title}</span>
                <span className="figure-explorer-item-desc">{fig.desc}</span>
              </span>
            </button>
          ))}
        </div>
      )}

      <Dialog open={active !== null} onOpenChange={(open) => !open && setActiveIndex(null)}>
        <DialogContent className="max-w-6xl">
          {active && (
            <>
              <DialogTitle className="text-base">{active.number} — {active.title}</DialogTitle>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={active.src}
                alt={active.alt}
                style={{ maxHeight: "70vh", width: "auto", margin: "0 auto", objectFit: "contain" }}
              />
              <DialogDescription className="text-xs leading-relaxed">
                {active.desc}
                {trackSlug(active.track) && (
                  <>
                    {" · "}
                    <Link href={`/papers/${trackSlug(active.track)}`}>Open paper &rarr;</Link>
                  </>
                )}
              </DialogDescription>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
