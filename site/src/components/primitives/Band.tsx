import type { ElementType, ReactNode } from "react";
import { cn } from "@/lib/utils";

export type BandTone = "base" | "alt" | "deep";
export type BandWidth = "prose" | "content" | "full";

export interface BandProps {
  tone?: BandTone;
  width?: BandWidth;
  as?: ElementType;
  className?: string;
  innerClassName?: string;
  id?: string;
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
  children,
}: BandProps) {
  return (
    <Tag id={id} className={cn("band", `band-${tone}`, className)}>
      <div className={cn("band-inner", `band-width-${width}`, innerClassName)}>
        {children}
      </div>
    </Tag>
  );
}
