"use client";

import { useCallback, useEffect, useState } from "react";
import type { PaperFigure } from "@/lib/livePapers";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { ChevronLeft, ChevronRight } from "lucide-react";
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";

type Mode = "all" | "in-paper" | "candidate";

interface PaperFigureGalleryProps {
  inPaper: PaperFigure[];
  candidates: PaperFigure[];
  paperNumber: string;
}

export function PaperFigureGallery({
  inPaper,
  candidates,
  paperNumber,
}: PaperFigureGalleryProps) {
  const [mode, setMode] = useState<Mode>("all");
  const [activeIndex, setActiveIndex] = useState<number | null>(null);

  const visible =
    mode === "in-paper"
      ? inPaper
      : mode === "candidate"
        ? candidates
        : [...inPaper, ...candidates];

  const counts = {
    all: inPaper.length + candidates.length,
    "in-paper": inPaper.length,
    candidate: candidates.length,
  };

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

  return (
    <div className="paper-figure-gallery">
      <div
        className="paper-figure-toolbar"
        style={{
          display: "flex",
          flexWrap: "wrap",
          alignItems: "center",
          gap: 12,
          marginBottom: 18,
          paddingBottom: 14,
          borderBottom: "1px solid var(--border)",
        }}
      >
        <div
          style={{
            display: "flex",
            gap: 6,
            padding: 4,
            border: "1px solid var(--border)",
            borderRadius: 8,
            background: "var(--surface)",
          }}
          role="tablist"
          aria-label="Figure status filter"
        >
          {(
            [
              { key: "all", label: "All" },
              { key: "in-paper", label: "In paper" },
              { key: "candidate", label: "Candidates" },
            ] as Array<{ key: Mode; label: string }>
          ).map(({ key, label }) => {
            const isActive = mode === key;
            return (
              <button
                key={key}
                type="button"
                role="tab"
                aria-selected={isActive}
                onClick={() => {
                  setMode(key);
                  setActiveIndex(null);
                }}
                style={{
                  padding: "5px 12px",
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: "0.7rem",
                  letterSpacing: "0.04em",
                  textTransform: "uppercase",
                  borderRadius: 5,
                  border: "none",
                  cursor: "pointer",
                  background: isActive ? "var(--text)" : "transparent",
                  color: isActive ? "var(--bg)" : "var(--text-muted)",
                  transition: "background-color 120ms, color 120ms",
                }}
              >
                {label}
                <span
                  style={{
                    marginLeft: 6,
                    fontSize: "0.62rem",
                    opacity: 0.65,
                  }}
                >
                  {counts[key]}
                </span>
              </button>
            );
          })}
        </div>
        <div
          style={{
            marginLeft: "auto",
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.7rem",
            color: "var(--text-muted)",
          }}
        >
          Paper {paperNumber} · {visible.length}{" "}
          {visible.length === 1 ? "figure" : "figures"}
        </div>
      </div>

      {visible.length === 0 ? (
        <Card style={{ padding: 24, textAlign: "center" }}>
          <p
            style={{
              margin: 0,
              fontSize: "0.85rem",
              color: "var(--text-muted)",
            }}
          >
            {mode === "candidate"
              ? "No candidate figures awaiting review for this paper."
              : mode === "in-paper"
                ? "No figures currently in the .tex."
                : "No figures registered for this paper."}
          </p>
        </Card>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(260px, 1fr))",
            gap: 14,
          }}
        >
          {visible.map((fig, i) => {
            const isCandidate = fig.status === "candidate";
            return (
              <Card
                key={`${fig.paperSlug}-${fig.ordinal}-${fig.title}`}
                className="paper-figure-card"
                style={{
                  overflow: "hidden",
                  padding: 0,
                  border: "1px solid var(--border)",
                  background: "var(--surface)",
                  transition: "border-color 120ms",
                }}
              >
                <button
                  type="button"
                  onClick={() => setActiveIndex(i)}
                  style={{
                    display: "block",
                    width: "100%",
                    background: "none",
                    border: "none",
                    padding: 0,
                    cursor: "pointer",
                    textAlign: "left",
                    color: "inherit",
                  }}
                  aria-label={`Open ${fig.title}`}
                >
                  <div
                    style={{
                      aspectRatio: "16 / 10",
                      width: "100%",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      borderBottom: "1px solid var(--border)",
                      background: "var(--background)",
                      overflow: "hidden",
                    }}
                  >
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={fig.src}
                      alt={fig.alt}
                      loading="lazy"
                      decoding="async"
                      style={{
                        width: "100%",
                        height: "100%",
                        objectFit: "contain",
                        padding: 10,
                      }}
                    />
                  </div>
                  <div style={{ padding: "12px 14px" }}>
                    <div
                      style={{
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "space-between",
                        gap: 8,
                        marginBottom: 6,
                      }}
                    >
                      <span
                        style={{
                          fontFamily: "var(--font-mono-stack)",
                          fontSize: "0.62rem",
                          letterSpacing: "0.06em",
                          textTransform: "uppercase",
                          color: "var(--text-muted)",
                        }}
                      >
                        {isCandidate
                          ? `Candidate #${fig.ordinal - 100}`
                          : `Fig. ${fig.ordinal}`}
                      </span>
                      <Badge
                        variant={isCandidate ? "outline" : "secondary"}
                        className="font-mono"
                        style={{ fontSize: "0.6rem" }}
                      >
                        {isCandidate ? "candidate" : "in paper"}
                      </Badge>
                    </div>
                    <div
                      style={{
                        fontFamily: "var(--font-mono-stack)",
                        fontSize: "0.82rem",
                        fontWeight: 600,
                        lineHeight: 1.35,
                        color: "var(--text)",
                      }}
                    >
                      {fig.title}
                    </div>
                    <p
                      style={{
                        margin: "6px 0 0",
                        fontSize: "0.72rem",
                        lineHeight: 1.5,
                        color: "var(--text-muted)",
                        display: "-webkit-box",
                        WebkitLineClamp: 3,
                        WebkitBoxOrient: "vertical",
                        overflow: "hidden",
                      }}
                    >
                      {fig.desc}
                    </p>
                  </div>
                </button>
              </Card>
            );
          })}
        </div>
      )}

      <Dialog
        open={active !== null}
        onOpenChange={(open) => !open && setActiveIndex(null)}
      >
        <DialogContent className="max-w-6xl">
          {active && (
            <>
              <DialogTitle
                style={{ fontFamily: "var(--font-mono-stack)" }}
                className="text-base"
              >
                {active.status === "candidate"
                  ? `Candidate · ${active.title}`
                  : `Figure ${active.ordinal} · ${active.title}`}
              </DialogTitle>
              <div
                style={{
                  maxHeight: "70vh",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  background: "var(--background)",
                  borderRadius: 6,
                  overflow: "auto",
                }}
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={active.src}
                  alt={active.alt}
                  style={{
                    maxHeight: "70vh",
                    width: "auto",
                    objectFit: "contain",
                  }}
                />
              </div>
              {visible.length > 1 && (
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    gap: 12,
                  }}
                >
                  <button
                    type="button"
                    onClick={() => step(-1)}
                    aria-label="Previous figure (left arrow)"
                    className="figure-nav-btn"
                  >
                    <ChevronLeft size={15} />
                  </button>
                  <span
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: "0.7rem",
                      color: "var(--text-muted)",
                      fontVariantNumeric: "tabular-nums",
                    }}
                  >
                    {(activeIndex ?? 0) + 1} / {visible.length}
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
                <span
                  style={{
                    display: "block",
                    marginTop: 8,
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: "0.62rem",
                    letterSpacing: "0.06em",
                    textTransform: "uppercase",
                    color: "var(--text-muted)",
                  }}
                >
                  {active.src} · {active.paperVersion}
                  {active.status === "candidate" && (
                    <>
                      {" · "}
                      <span style={{ color: "var(--warn)" }}>
                        not yet in paper — tell Houston to add
                      </span>
                    </>
                  )}
                </span>
              </DialogDescription>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
