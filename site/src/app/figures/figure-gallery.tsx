"use client";

import { useState } from "react";
import type { Figure, FigureSection } from "@/data/figures";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";

interface FigureGalleryProps {
  sections: FigureSection[];
}

export function FigureGallery({ sections }: FigureGalleryProps) {
  const [active, setActive] = useState<Figure | null>(null);

  return (
    <>
      {sections.map((section) => (
        <section key={section.title} className="section">
          <div className="mb-3 flex items-baseline justify-between gap-3">
            <h2
              className="!m-0 !border-b-0 !p-0"
              style={{
                fontFamily: "var(--font-serif)",
                fontSize: "1.25rem",
                fontWeight: 600,
                color: "var(--text)",
                textTransform: "none",
                letterSpacing: 0,
              }}
            >
              {section.title}
            </h2>
            <Badge variant="outline" className="font-mono text-xs">
              {section.count}
            </Badge>
          </div>

          <div className="grid gap-3 md:grid-cols-2">
            {section.items.map((fig) => (
              <Card
                key={`${section.title}-${fig.number}`}
                className="overflow-hidden p-0 transition-colors hover:border-foreground/40"
              >
                <button
                  type="button"
                  onClick={() => setActive(fig)}
                  className="block w-full text-left"
                >
                  <div className="aspect-[4/3] w-full overflow-hidden bg-muted">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={fig.src}
                      alt={fig.alt}
                      loading="lazy"
                      className="h-full w-full object-contain p-2"
                    />
                  </div>
                  <div className="border-t p-4">
                    <div className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
                      {fig.number}
                    </div>
                    <div
                      className="mt-1 text-sm font-semibold leading-snug"
                      style={{ fontFamily: "var(--font-serif)" }}
                    >
                      {fig.title}
                    </div>
                    <p className="mt-2 text-xs leading-relaxed text-muted-foreground">
                      {fig.desc}
                    </p>
                    {fig.source && (
                      <div className="mt-3">
                        <Badge variant="secondary" className="font-mono text-[10px]">
                          {fig.source}
                        </Badge>
                      </div>
                    )}
                  </div>
                </button>
              </Card>
            ))}
          </div>
        </section>
      ))}

      <Dialog
        open={active !== null}
        onOpenChange={(open) => !open && setActive(null)}
      >
        <DialogContent className="max-w-6xl">
          {active && (
            <>
              <DialogTitle
                style={{ fontFamily: "var(--font-serif)" }}
                className="text-base"
              >
                {active.number} — {active.title}
              </DialogTitle>
              <div className="flex max-h-[70vh] items-center justify-center overflow-auto bg-muted">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={active.src}
                  alt={active.alt}
                  className="max-h-[70vh] w-auto object-contain"
                />
              </div>
              <DialogDescription className="text-xs leading-relaxed">
                {active.desc}
                {active.source && (
                  <span className="mt-2 block font-mono text-[10px] uppercase tracking-wider">
                    Source: {active.source}
                  </span>
                )}
              </DialogDescription>
            </>
          )}
        </DialogContent>
      </Dialog>
    </>
  );
}
