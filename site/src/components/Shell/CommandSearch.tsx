"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { Search } from "lucide-react";
import { papers } from "@/data/papers";

interface SearchEntry {
  title: string;
  blurb: string;
  href: string;
  kind: string;
}

const ROUTE_ENTRIES: SearchEntry[] = [
  { kind: "Page", title: "Overview", blurb: "The ten-second answer: the claim, the tracks, the nulls.", href: "/" },
  { kind: "Page", title: "Research", blurb: "The three research tracks, as questions.", href: "/research" },
  { kind: "Page", title: "All works", blurb: "Flat, complete index of every paper, note, and release.", href: "/papers" },
  { kind: "Page", title: "Explore", blurb: "Galaxy, anomaly and data explorers, figures, visualize.", href: "/explore" },
  { kind: "Page", title: "Reproduce", blurb: "Experiment manifests, data sources, releases & DOIs.", href: "/reproduce" },
  { kind: "Page", title: "Status", blurb: "Live per-work publication-readiness dashboard.", href: "/status" },
  { kind: "Page", title: "Reviews", blurb: "Internal multi-model review convergence — a gate, not a product.", href: "/reviews" },
  { kind: "Page", title: "Learn", blurb: "The plain-English explainer, glossary, timeline, articles.", href: "/learn" },
  { kind: "Page", title: "Explained", blurb: "Non-technical explanation of the research program.", href: "/explained" },
  { kind: "Page", title: "Glossary", blurb: "Definitions for every jargon term used on the site.", href: "/glossary" },
  { kind: "Page", title: "Activity", blurb: "Chronological research + review log.", href: "/activity" },
  { kind: "Page", title: "Publishing", blurb: "Venue, endorsement, and submission state — not readiness.", href: "/publish" },
  { kind: "Page", title: "Docs", blurb: "API and MCP reference.", href: "/docs" },
];

function buildIndex(): SearchEntry[] {
  const paperEntries: SearchEntry[] = papers.map((p) => ({
    kind: "Work",
    title: p.title,
    blurb: p.plainTitle,
    href: `/papers/${p.slug}`,
  }));
  return [...ROUTE_ENTRIES, ...paperEntries];
}

/** ⌘K / Ctrl+K command search over the static site + papers index. */
export function CommandSearch() {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);
  const index = useMemo(buildIndex, []);

  useEffect(() => {
    function onKeydown(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setOpen((v) => !v);
      } else if (e.key === "Escape") {
        setOpen(false);
      }
    }
    function onOpenEvent() {
      setOpen(true);
    }
    window.addEventListener("keydown", onKeydown);
    window.addEventListener("bigbounce:open-search", onOpenEvent);
    return () => {
      window.removeEventListener("keydown", onKeydown);
      window.removeEventListener("bigbounce:open-search", onOpenEvent);
    };
  }, []);

  useEffect(() => {
    if (open) {
      setQuery("");
      queueMicrotask(() => inputRef.current?.focus());
    }
  }, [open]);

  const results = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return index.slice(0, 8);
    return index
      .filter(
        (e) =>
          e.title.toLowerCase().includes(q) ||
          e.blurb.toLowerCase().includes(q) ||
          e.kind.toLowerCase().includes(q),
      )
      .slice(0, 20);
  }, [query, index]);

  if (!open) return null;

  return (
    <div className="command-search-overlay" onClick={() => setOpen(false)}>
      <div
        className="command-search-panel"
        role="dialog"
        aria-modal="true"
        aria-label="Search"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="command-search-input-wrap">
          <Search size={15} aria-hidden="true" />
          <input
            ref={inputRef}
            className="command-search-input"
            placeholder="Search works, tracks, pages…"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-label="Search"
          />
          <kbd className="command-search-esc">esc</kbd>
        </div>
        <ul className="command-search-results">
          {results.length === 0 && (
            <li className="command-search-empty">No matches.</li>
          )}
          {results.map((r) => (
            <li key={r.href}>
              <Link href={r.href} className="command-search-result" onClick={() => setOpen(false)}>
                <span className="command-search-result-kind mono">{r.kind}</span>
                <span className="command-search-result-body">
                  <span className="command-search-result-title">{r.title}</span>
                  <span className="command-search-result-blurb">{r.blurb}</span>
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
