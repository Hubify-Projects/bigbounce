import type { ElementType, ReactNode } from "react";
import { cn } from "@/lib/utils";
// Artistry layer (BRAND_SYSTEM.md §2/§4/§5/§6). A global sheet so it
// composes over the primitive classes without owning globals.css.
import "./artistry.css";

export type BandTone = "base" | "alt" | "deep";
export type BandWidth = "prose" | "content" | "wide" | "full";

export interface BandProps {
  tone?: BandTone;
  width?: BandWidth;
  as?: ElementType;
  className?: string;
  innerClassName?: string;
  id?: string;
  /** Extra top space — use on the first band of a page. */
  open?: boolean;
  /** Extra bottom space — use on the last band of a page. */
  close?: boolean;
  /** Continues the idea above it: no re-establishing top space. */
  tight?: boolean;
  children: ReactNode;
}

/**
 * Full-width tonal band — the layout primitive that replaces `.card` /
 * `ui/card.tsx` (REDESIGN_SPEC.md §4.3, §5.1 #1). Never nest a Band inside
 * another bordered surface; a Band separates content with a background
 * tonal shift or whitespace, never a border.
 */
export function Band({
  tone = "base",
  width = "content",
  as: Tag = "section",
  className,
  innerClassName,
  id,
  open,
  close,
  tight,
  children,
}: BandProps) {
  return (
    <Tag id={id} className={cn(
        "band",
        `band-${tone}`,
        open && "band-open",
        close && "band-close",
        tight && "band-tight",
        className,
      )}>
      <div className={cn("band-inner", `band-width-${width}`, innerClassName)}>
        {children}
      </div>
    </Tag>
  );
}
