"use client";

import { useState } from"react";
import type { Figure, FigureSection } from"@/data/figures";
import { Card } from"@/components/ui/card";
import { Badge } from"@/components/ui/badge";
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogDescription,
} from"@/components/ui/dialog";

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
                fontFamily:"var(--font-mono-stack)",
                fontSize:"1rem",
                fontWeight: 600,
                color:"var(--text)",
                textTransform:"none",
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
                className="figure-card group overflow-hidden p-0 transition-colors hover:border-[var(--border-bright)]"
              >
                <button
                  type="button"
                  onClick={() => setActive(fig)}
                  className="block h-full w-full text-left"
                >
                  <div className="figure-stage flex aspect-[16/10] w-full items-center justify-center overflow-hidden border-b">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={fig.src}
                      alt={fig.alt}
                      loading="lazy"
                      className="h-full w-full object-contain p-3 transition-transform duration-200 group-hover:scale-[1.015]"
                    />
                  </div>
                  <div className="p-4">
                    <div className="flex items-center justify-between gap-3">
                      <div className="font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
                        {fig.number}
                      </div>
                      {fig.source && (
                        <Badge variant="secondary" className="max-w-[48%] truncate font-mono text-[10px]">
                          {fig.source}
                        </Badge>
                      )}
                    </div>
                    <div
                      className="mt-2 text-sm font-semibold leading-snug"
                      style={{ fontFamily:"var(--font-mono-stack)" }}
                    >
                      {fig.title}
                    </div>
                    <p className="mt-2 text-xs leading-relaxed text-muted-foreground">
                      {fig.desc}
                    </p>
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
