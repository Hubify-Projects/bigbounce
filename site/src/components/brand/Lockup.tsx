import Link from "next/link";
import type { CSSProperties, ReactNode } from "react";
import { LabMark } from "./LabMark";

interface LockupProps {
  size?: "sm" | "lg";
  href?: string;
  className?: string;
}

const SIZES = {
  sm: { mark: 20, tenant: 15, platform: 13 },
  lg: { mark: 32, tenant: 22, platform: 15 },
} as const;

/**
 * Property lockup per hubify BRAND_SYSTEM.md §7: "[Mark] BigBounce Lab | Hubify".
 * The tenant leads in --ink; a 1px --rule divider separates it from "Hubify",
 * set subordinate in --ink-3 at the `small` type step. No co-branded glyph.
 */
export function Lockup({ size = "sm", href = "/", className }: LockupProps) {
  const s = SIZES[size];
  const content = (
    <span
      className={className}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 8,
        color: "var(--ink)",
        textDecoration: "none",
        lineHeight: 1,
      }}
    >
      <LabMark size={s.mark} title="BigBounce Lab" />
      <span
        style={{
          fontFamily: "var(--font-sans)",
          fontWeight: 500,
          fontSize: s.tenant,
          letterSpacing: "-0.02em",
          color: "var(--ink)",
          whiteSpace: "nowrap",
        }}
      >
        BigBounce Lab
      </span>
      <span aria-hidden="true" style={{ width: 1, height: "1.15em", background: "var(--rule)" }} />
      <span
        style={{
          fontFamily: "var(--font-sans)",
          fontWeight: 400,
          fontSize: s.platform,
          color: "var(--ink-3)",
          whiteSpace: "nowrap",
        }}
      >
        Hubify
      </span>
    </span>
  );

  return wrap(content, href);
}

function wrap(content: ReactNode, href?: string) {
  const style: CSSProperties = { display: "inline-flex" };
  if (!href) return <span style={style}>{content}</span>;
  return (
    <Link href={href} style={style} aria-label="BigBounce Lab, a Hubify research lab">
      {content}
    </Link>
  );
}
