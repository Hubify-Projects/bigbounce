import type { ReactNode } from "react";
import Link from "next/link";
import { cn } from "@/lib/utils";

export interface RowItem {
  title: ReactNode;
  purpose?: ReactNode;
  href: string;
  right?: ReactNode;
  chips?: ReactNode;
  external?: boolean;
}

/** A single hairline-separated row (used standalone or via RowList). */
export function Row({ title, purpose, href, right, chips, external }: RowItem) {
  const content = (
    <>
      <span className="row-main">
        <span className="row-title">{title}</span>
        {purpose && <span className="row-purpose">{purpose}</span>}
        {chips && <span className="row-chips">{chips}</span>}
      </span>
      {right && <span className="row-right mono">{right}</span>}
    </>
  );
  return external ? (
    <a href={href} target="_blank" rel="noreferrer" className="row">
      {content}
    </a>
  ) : (
    <Link href={href} className="row">
      {content}
    </Link>
  );
}

export interface RowListProps {
  items: RowItem[];
  className?: string;
}

/**
 * Rows separated by hairlines only — no per-item card borders
 * (REDESIGN_SPEC.md §5.1 #5). Used by tracks, works fallback, learn/explore
 * hubs, activity.
 */
export function RowList({ items, className }: RowListProps) {
  return (
    <div className={cn("row-list", className)}>
      {items.map((it, i) => (
        <Row key={`${it.href}-${i}`} {...it} />
      ))}
    </div>
  );
}
