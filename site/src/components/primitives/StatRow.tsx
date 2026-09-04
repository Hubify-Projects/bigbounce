import type { ReactNode } from "react";
import Link from "next/link";
import { cn } from "@/lib/utils";

export interface StatItem {
  value: ReactNode;
  label: string;
  href?: string;
  mono?: boolean;
}

export interface StatRowProps {
  items: StatItem[];
  className?: string;
}

/** One row of numbers with hairline dividers, no boxes (REDESIGN_SPEC.md §5.1 #3). */
export function StatRow({ items, className }: StatRowProps) {
  return (
    <div className={cn("stat-row", className)}>
      {items.map((it, i) => {
        const body = (
          <>
            <span className={cn("stat-row-value", it.mono !== false && "mono")}>
              {it.value}
            </span>
            <span className="stat-row-label">{it.label}</span>
          </>
        );
        return it.href ? (
          <Link key={i} href={it.href} className="stat-row-item stat-row-item-link">
            {body}
          </Link>
        ) : (
          <div key={i} className="stat-row-item">
            {body}
          </div>
        );
      })}
    </div>
  );
}
