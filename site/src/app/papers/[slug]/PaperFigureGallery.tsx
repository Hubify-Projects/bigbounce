"use client";

import { useState } from "react";
import type { PaperFigure } from "@/lib/livePapers";
import { FigureBlock } from "@/components/primitives";
import { Dialog, DialogContent, DialogTitle, DialogDescription } from "@/components/ui/dialog";

interface PaperFigureGalleryProps {
  inPaper: PaperFigure[];
  candidates: PaperFigure[];
  paperNumber: string;
}

/**
 * Full-width figure list for a paper detail page (REDESIGN_SPEC.md §3.4
 * item 5, §5.1 #10). No card grid — one FigureBlock per figure, full
 * content width, click to open the full-size lightbox. Candidates are
 * grouped separately and labeled, never mixed silently into "in paper".
 */
export function PaperFigureGallery({ inPaper, candidates, paperNumber }: PaperFigureGalleryProps) {
  const [active, setActive] = useState<PaperFigure | null>(null);

  return (
    <div className="paper-figure-gallery">
      {inPaper.map((fig) => (
        <FigureBlock
          key={`${fig.paperSlug}-${fig.ordinal}`}
          src={fig.src}
          alt={fig.alt}
          caption={`Figure ${fig.ordinal} — ${fig.title}`}
          credit={`Paper ${paperNumber} · ${fig.paperVersion}`}
          full
          onClick={() => setActive(fig)}
        />
      ))}

      {candidates.length > 0 && (
        <>
          <p className="row-purpose" style={{ marginTop: 24 }}>
            Candidate figures — validated analysis outputs not yet included in the draft.
          </p>
          {candidates.map((fig) => (
            <FigureBlock
              key={`${fig.paperSlug}-${fig.ordinal}`}
              src={fig.src}
              alt={fig.alt}
              caption={`Candidate — ${fig.title}`}
              credit="not yet in paper"
              full
              onClick={() => setActive(fig)}
            />
          ))}
        </>
      )}

      <Dialog open={active !== null} onOpenChange={(open) => !open && setActive(null)}>
        <DialogContent className="max-w-6xl">
          {active && (
            <>
              <DialogTitle className="text-base">{active.title}</DialogTitle>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={active.src}
                alt={active.alt}
                style={{ maxHeight: "70vh", width: "auto", margin: "0 auto", objectFit: "contain" }}
              />
              <DialogDescription className="text-xs leading-relaxed">
                {active.desc}
              </DialogDescription>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
