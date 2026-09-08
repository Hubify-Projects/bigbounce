import type { ReactNode } from "react";
import Link from "next/link";
import { cn } from "@/lib/utils";

export interface MetaItem {
  label: string;
  value: ReactNode;
  mono?: boolean;
}

export interface LinkItem {
  label: string;
  href: string;
  external?: boolean;
}

export interface PageHeaderProps {
  eyebrow?: string;
  title: ReactNode;
  lead?: ReactNode;
  meta?: MetaItem[];
  actions?: LinkItem[];
  className?: string;
}

/** Page/section header — eyebrow, H1, one-line lead, mono meta row, text actions. */
export function PageHeader({
  eyebrow,
  title,
  lead,
  meta,
  actions,
  className,
}: PageHeaderProps) {
  return (
    <header className={cn("page-header", className)}>
      {eyebrow && <p className="eyebrow">{eyebrow}</p>}
      <h1 className="page-header-title">{title}</h1>
      {lead && <p className="page-header-lead">{lead}</p>}
      {meta && meta.length > 0 && (
        <div className="page-header-meta mono">
          {meta.map((m, i) => (
            <span key={i} className="page-header-meta-item">
              <span className="page-header-meta-label">{m.label}</span>
              {" "}
              {m.value}
            </span>
          ))}
        </div>
      )}
      {actions && actions.length > 0 && (
        <div className="page-header-actions">
          {actions.map((a) =>
            a.external ? (
              <a
                key={a.href}
                href={a.href}
                target="_blank"
                rel="noreferrer"
                className="page-header-action"
              >
                {a.label}
              </a>
            ) : (
              <Link key={a.href} href={a.href} className="page-header-action">
                {a.label}
              </Link>
            ),
          )}
        </div>
      )}
    </header>
  );
}
