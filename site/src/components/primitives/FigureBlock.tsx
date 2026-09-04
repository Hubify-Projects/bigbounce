import { cn } from "@/lib/utils";

export interface FigureBlockProps {
  src: string;
  alt: string;
  caption: string;
  credit?: string;
  full?: boolean;
  onClick?: () => void;
  className?: string;
}

/**
 * Full-content-width figure on a tonal band (REDESIGN_SPEC.md §4.4, §5.1
 * #10). Caption sits below, left-aligned, no frame. Used by
 * /explore/figures and /papers/[slug]. Not a bordered surface — the image
 * itself is the only visual boundary.
 */
export function FigureBlock({
  src,
  alt,
  caption,
  credit,
  full,
  onClick,
  className,
}: FigureBlockProps) {
  return (
    <figure className={cn("figure-block", full && "figure-block-full", className)}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={src}
        alt={alt}
        className="figure-block-img"
        onClick={onClick}
        role={onClick ? "button" : undefined}
        tabIndex={onClick ? 0 : undefined}
      />
      <figcaption className="figure-block-caption">
        {caption}
        {credit && <span className="figure-block-credit"> &middot; {credit}</span>}
      </figcaption>
    </figure>
  );
}
