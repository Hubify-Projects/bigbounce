"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

interface SidebarLink {
  href: string;
  label: string;
  external?: boolean;
}

interface SidebarSection {
  label?: string;
  links: SidebarLink[];
}

const sections: SidebarSection[] = [
  {
    links: [
      { href: "/", label: "overview" },
      { href: "/explained", label: "explainer" },
    ],
  },
  {
    label: "research",
    links: [
      { href: "/surveys", label: "surveys (8)" },
      { href: "/predictions", label: "predictions (4)" },
      { href: "/paper", label: "papers (4)" },
    ],
  },
  {
    label: "explore",
    links: [
      { href: "/data-explorer", label: "data explorer" },
      { href: "/figures", label: "figures" },
      { href: "/glossary", label: "glossary" },
      { href: "/timeline", label: "timeline" },
    ],
  },
  {
    label: "articles",
    links: [
      { href: "/articles", label: "all articles" },
      { href: "/speculations", label: "speculations" },
    ],
  },
];

const tail: SidebarLink[] = [
  { href: "/activity", label: "activity" },
  { href: "/status", label: "status" },
];

function isActive(pathname: string, href: string): boolean {
  if (href === "/") return pathname === "/";
  return pathname === href || pathname.startsWith(`${href}/`);
}

function NavLink({
  link,
  pathname,
}: {
  link: SidebarLink;
  pathname: string;
}) {
  const active = isActive(pathname, link.href);
  const className = cn(
    "sidebar-link",
    active && "is-active",
  );
  if (link.external) {
    return (
      <a href={link.href} className={className}>
        {link.label}
      </a>
    );
  }
  return (
    <Link
      href={link.href}
      className={className}
      aria-current={active ? "page" : undefined}
    >
      {link.label}
    </Link>
  );
}

export function Sidebar() {
  const pathname = usePathname() ?? "/";
  return (
    <aside className="sidebar">
      <Link href="/" className="sidebar-brand">
        BigBounce
      </Link>
      <nav className="sidebar-nav">
        {sections.map((section, i) => (
          <div key={section.label ?? `section-${i}`} className="sidebar-section">
            {section.label && (
              <div className="sidebar-section-label">{section.label}</div>
            )}
            {section.links.map((link) => (
              <NavLink key={link.href} link={link} pathname={pathname} />
            ))}
          </div>
        ))}
        <div className="sidebar-separator" />
        <div className="sidebar-section">
          {tail.map((link) => (
            <NavLink key={link.href} link={link} pathname={pathname} />
          ))}
        </div>
      </nav>
      <div className="sidebar-footer">
        <div className="sidebar-footer-name">Houston Golden</div>
        <div className="sidebar-footer-role">Independent Researcher</div>
        <a
          href="https://github.com/Hubify-Projects/bigbounce"
          className="sidebar-footer-link"
          target="_blank"
          rel="noopener"
        >
          GitHub
        </a>
      </div>
    </aside>
  );
}
