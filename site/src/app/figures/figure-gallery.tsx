"use client";

import { useCallback, useEffect, useMemo, useState } from"react";
import Link from"next/link";
import type { Figure, FigureSection } from"@/data/figures";
import { Card } from"@/components/ui/card";
import { Badge } from"@/components/ui/badge";
import { Button } from"@/components/ui/button";
import { ChevronLeft, ChevronRight, Search, SlidersHorizontal } from"lucide-react";
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogDescription,
} from"@/components/ui/dialog";

interface FigureGalleryProps {
  sections: FigureSection[];
}

type FigurePaper = "P1A" | "P1B" | "P2" | "P3" | "P4" | "P5" | "X";
type FigureSort = "paper" | "number" | "title" | "source";
type FigureView = "grid" | "list";

interface EnrichedFigure extends Figure {
  sectionTitle: string;
  paper: FigurePaper;
  figureIndex: number;
  sourceGroup: string;
}

// Extract paper key from a section title like "Paper 1A — …" / "Paper 5 — …".
// Returns "P1A", "P1B", "P2", "P3", "P4", "P5", or "X" (cross-cutting).
function paperKey(title: string): FigurePaper {
  const m = title.match(/Paper\s+(1A|1B|[2-5])/i);
  if (m) return `P${m[1].toUpperCase()}` as FigurePaper;
  return "X";
}

function paperLabel(key: FigurePaper) {
  if (key === "X") return "Cross-cutting";
  return `Paper ${key.replace("P", "")}`;
}

/** Route slug for a paper key — null for cross-cutting figures. */
function paperSlug(key: FigurePaper): string | null {
  if (key === "X") return null;
  return `paper-${key.replace("P", "").toLowerCase()}`;
}

function figureNumberValue(number: string) {
  const match = number.match(/\d+/);
  return match ? Number(match[0]) : 9999;
}

function sourceGroup(source: string) {
  const normalized = source.toLowerCase();
  if (normalized.includes("paper 1a")) return "Paper 1A";
  if (normalized.includes("paper 1b") || normalized.includes("namaster")) return "P1B / namaster-proof software";
  if (normalized.includes("paper 2") || normalized.includes("forecast") || normalized.includes("fnl")) return "Paper 2 / Forecast";
  if (normalized.includes("paper 3") || normalized.includes("catalog")) return "P3 / Supporting Data Release";
  if (normalized.includes("paper 4") || normalized.includes("chirality")) return "Paper 4 / Chirality";
  if (normalized.includes("paper 5")) return "P5 / AJ companion";
  if (normalized.includes("analysis")) return "Analysis";
  if (normalized.includes("program")) return "Program";
  return "Other";
}

// Stable artifact display order: P1A → P1B → P2 → P3 data release → P4 → P5 → cross-cutting
const ORDER: Record<FigurePaper, number> = {
  P1A: 1,
  P1B: 2,
  P2: 3,
  P3: 4,
  P4: 5,
  P5: 6,
  X: 7,
};

const FILTERS: Array<{
  key: "all" | FigurePaper;
  label: string;
}> = [
  { key: "all", label: "All artifacts" },
  { key: "P1A", label: "Paper 1A (ECH routes)" },
  { key: "P1B", label: "P1B (namaster-proof software)" },
  { key: "P2", label: "Paper 2 (f_NL)" },
  { key: "P3", label: "P3 (Supporting Data Release)" },
  { key: "P4", label: "Paper 4 (chirality)" },
  { key: "P5", label: "P5 (AJ companion)" },
  { key: "X", label: "Cross-cutting" },
];

export function FigureGallery({ sections }: FigureGalleryProps) {
  const [activeIndex, setActiveIndex] = useState<number | null>(null);
  const [filter, setFilter] = useState<typeof FILTERS[number]["key"]>("all");
  const [sourceFilter, setSourceFilter] = useState("all");
  const [sort, setSort] = useState<FigureSort>("paper");
  const [view, setView] = useState<FigureView>("grid");
  const [query, setQuery] = useState("");

  const allFigures = useMemo<EnrichedFigure[]>(
    () =>
      sections.flatMap((section) =>
        section.items.map((fig) => ({
          ...fig,
          sectionTitle: section.title,
          paper: paperKey(section.title),
          figureIndex: figureNumberValue(fig.number),
          sourceGroup: sourceGroup(fig.source),
        })),
      ),
    [sections],
  );

  const sourceGroups = useMemo(
    () => Array.from(new Set(allFigures.map((fig) => fig.sourceGroup))).sort(),
    [allFigures],
  );

  const visibleFigures = useMemo(() => {
    const q = query.trim().toLowerCase();
    const filtered = allFigures.filter((fig) => {
      const matchesPaper = filter === "all" || fig.paper === filter;
      const matchesSource =
        sourceFilter === "all" || fig.sourceGroup === sourceFilter;
      const matchesQuery =
        q.length === 0 ||
        [fig.title, fig.desc, fig.number, fig.source, fig.sectionTitle]
          .join(" ")
          .toLowerCase()
          .includes(q);
      return matchesPaper && matchesSource && matchesQuery;
    });

    return filtered.sort((a, b) => {
      if (sort === "number") return a.figureIndex - b.figureIndex;
      if (sort === "title") return a.title.localeCompare(b.title);
      if (sort === "source") {
        return (
          a.sourceGroup.localeCompare(b.sourceGroup) ||
          ORDER[a.paper] - ORDER[b.paper] ||
          a.figureIndex - b.figureIndex
        );
      }
      return (
        ORDER[a.paper] - ORDER[b.paper] ||
        a.figureIndex - b.figureIndex ||
        a.title.localeCompare(b.title)
      );
    });
  }, [allFigures, filter, query, sort, sourceFilter]);

  const active =
    activeIndex === null ? (null as EnrichedFigure | null) : (visibleFigures[activeIndex] ?? null);

  const step = useCallback(
    (delta: number) => {
      setActiveIndex((prev) => {
        if (prev === null || visibleFigures.length === 0) return prev;
        return (prev + delta + visibleFigures.length) % visibleFigures.length;
      });
    },
    [visibleFigures.length],
  );

  // Keyboard navigation while the zoom view is open.
  useEffect(() => {
    if (activeIndex === null) return;
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "ArrowRight") {
        e.preventDefault();
        step(1);
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        step(-1);
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [activeIndex, step]);

  const groupedFigures = useMemo(
    () =>
      visibleFigures.reduce<Record<string, EnrichedFigure[]>>((acc, fig) => {
        const key = sort === "source" ? fig.sourceGroup : fig.sectionTitle;
        acc[key] ??= [];
        acc[key].push(fig);
        return acc;
      }, {}),
    [sort, visibleFigures],
  );

  const galleryBody = (
    <>
      <div className="figures-toolbar">
        <div className="figures-search">
          <Search aria-hidden="true" />
          <input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search title, caption, source"
            aria-label="Search figures"
          />
        </div>
        <label className="figures-select">
          <span>Source</span>
          <select
            value={sourceFilter}
            onChange={(event) => setSourceFilter(event.target.value)}
          >
            <option value="all">All sources</option>
            {sourceGroups.map((group) => (
              <option key={group} value={group}>
                {group}
              </option>
            ))}
          </select>
        </label>
        <label className="figures-select">
          <span>Sort</span>
          <select
            value={sort}
            onChange={(event) => setSort(event.target.value as FigureSort)}
          >
            <option value="paper">Paper order</option>
            <option value="number">Figure number</option>
            <option value="title">Title</option>
            <option value="source">Source group</option>
          </select>
        </label>
        <div className="figures-view-toggle" aria-label="Gallery view">
          <Button
            type="button"
            size="sm"
            variant={view === "grid" ? "default" : "outline"}
            onClick={() => setView("grid")}
          >
            Grid
          </Button>
          <Button
            type="button"
            size="sm"
            variant={view === "list" ? "default" : "outline"}
            onClick={() => setView("list")}
          >
            List
          </Button>
        </div>
        <span className="figures-result-count" style={{ marginLeft: "auto" }}>
          {visibleFigures.length} of {allFigures.length} shown
        </span>
      </div>
    </>
  );

  return (
    <div className="figures-layout">
      <aside className="figures-side-nav" aria-label="Browse figures by artifact">
        <div className="figures-side-label">
          <SlidersHorizontal aria-hidden="true" size={12} />
          <span>By artifact</span>
        </div>
        {FILTERS.map((f) => {
          const isActive = filter === f.key;
          const count =
            f.key === "all"
              ? allFigures.length
              : allFigures.filter((fig) => fig.paper === f.key).length;
          return (
            <button
              key={f.key}
              type="button"
              onClick={() => setFilter(f.key)}
              className={`figures-side-link${isActive ? " is-active" : ""}`}
              aria-current={isActive ? "true" : undefined}
            >
              <span>{f.label}</span>
              <span className="figures-side-count">{count}</span>
            </button>
          );
        })}
      </aside>

      <div className="figures-main">
        {galleryBody}
        {visibleFigures.length === 0 ? (
        <Card className="figure-empty-state">
          <div className="card-kicker">No figures matched</div>
          <p className="mt-2 text-sm text-muted-foreground">
            Clear the search or change the paper/source filter.
          </p>
        </Card>
      ) : (
        Object.entries(groupedFigures).map(([group, figures]) => (
        <section key={group} className="section">
          <div className="mb-3 flex items-baseline justify-between gap-3">
            <h2
              className="!m-0 !border-b-0 !p-0"
              style={{
                fontFamily:"var(--font-mono-stack)",
                fontSize:"1rem",
                fontWeight: 600,
                color:"var(--text)",
                textTransform:"none",
                letterSpacing: 0,
              }}
            >
              {group}
            </h2>
            <Badge variant="outline" className="font-mono text-xs">
              {figures.length} figure{figures.length === 1 ? "" : "s"}
            </Badge>
          </div>

          <div className={view === "grid" ? "figure-grid" : "figure-list"}>
            {figures.map((fig) => (
              <Card
                key={`${fig.sectionTitle}-${fig.number}-${fig.title}`}
                className={`figure-card group overflow-hidden p-0 transition-colors hover:border-[var(--border-bright)] ${view === "list" ? "figure-card-list" : ""}`}
              >
                <button
                  type="button"
                  onClick={() => setActiveIndex(visibleFigures.indexOf(fig))}
                  className="block h-full w-full text-left"
                  >
                  <div className="figure-stage flex aspect-[16/10] w-full items-center justify-center overflow-hidden border-b">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={fig.src}
                      alt={fig.alt}
                      loading="lazy"
                      decoding="async"
                      className="h-full w-full object-contain p-3 transition-transform duration-200 group-hover:scale-[1.015]"
                    />
                  </div>
                  <div className="p-4">
                    <div className="flex items-center justify-between gap-3">
                      <div className="font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
                        {fig.number}
                      </div>
                      <div className="flex min-w-0 items-center gap-2">
                        <Badge variant="outline" className="font-mono text-[10px]">
                          {paperLabel(fig.paper)}
                        </Badge>
                        {fig.source &&
                          fig.sourceGroup !== paperLabel(fig.paper) && (
                          <Badge variant="secondary" className="max-w-[180px] truncate font-mono text-[10px]">
                            {fig.sourceGroup}
                          </Badge>
                        )}
                      </div>
                    </div>
                    <div
                      className="mt-2 text-sm font-semibold leading-snug"
                      style={{ fontFamily:"var(--font-mono-stack)" }}
                    >
                      {fig.number.startsWith("Candidate") && (
                        <span
                          title="Validated analysis output not yet included in the paper draft."
                          style={{
                            display: "inline-block",
                            marginRight: "6px",
                            padding: "1px 6px",
                            borderRadius: "3px",
                            background: "color-mix(in srgb, var(--warn) 12%, transparent)",
                            color: "var(--warn)",
                            border: "1px solid color-mix(in srgb, var(--warn) 30%, transparent)",
                            fontFamily: "var(--font-mono-stack)",
                            fontSize: "9px",
                            fontWeight: 600,
                            textTransform: "uppercase",
                            letterSpacing: "0.06em",
                            verticalAlign: "middle",
                          }}
                        >
                          candidate
                        </span>
                      )}
                      {fig.title}
                    </div>
                    <p className="mt-2 text-xs leading-relaxed text-muted-foreground">
                      {fig.desc}
                    </p>
                    {view === "list" && fig.source && (
                      <p className="mt-2 font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
                        {fig.source}
                      </p>
                    )}
                  </div>
                </button>
              </Card>
            ))}
          </div>
        </section>
        ))
      )}

      <Dialog
        open={active !== null}
        onOpenChange={(open) => !open && setActiveIndex(null)}
      >
        <DialogContent className="max-w-6xl">
          {active && (
            <>
              <DialogTitle
                style={{ fontFamily:"var(--font-mono-stack)" }}
                className="text-base"
              >
                {active.number} — {active.title}
              </DialogTitle>
              <div className="figure-stage flex max-h-[70vh] items-center justify-center overflow-auto">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={active.src}
                  alt={active.alt}
                  className="figure-dialog-image max-h-[70vh] w-auto object-contain"
                />
              </div>
              {visibleFigures.length > 1 && (
                <div className="flex items-center justify-center gap-3">
                  <button
                    type="button"
                    onClick={() => step(-1)}
                    aria-label="Previous figure (left arrow)"
                    className="figure-nav-btn"
                  >
                    <ChevronLeft size={15} />
                  </button>
                  <span
                    className="font-mono text-[11px]"
                    style={{ color:"var(--text-tertiary)", fontVariantNumeric:"tabular-nums" }}
                  >
                    {(activeIndex ?? 0) + 1} / {visibleFigures.length}
                  </span>
                  <button
                    type="button"
                    onClick={() => step(1)}
                    aria-label="Next figure (right arrow)"
                    className="figure-nav-btn"
                  >
                    <ChevronRight size={15} />
                  </button>
                </div>
              )}
              <DialogDescription className="text-xs leading-relaxed">
                {active.desc}
                <span className="mt-2 block font-mono text-[10px] uppercase tracking-wider">
                  {active.source && <>Source: {active.source}</>}
                  {paperSlug(active.paper) && (
                    <>
                      {active.source && " · "}
                      <Link
                        href={`/papers/${paperSlug(active.paper)}`}
                        className="underline underline-offset-2"
                        style={{ color:"var(--text-secondary)" }}
                      >
                        Open {paperLabel(active.paper)} →
                      </Link>
                    </>
                  )}
                </span>
              </DialogDescription>
            </>
          )}
        </DialogContent>
      </Dialog>
      </div>
    </div>
  );
}
