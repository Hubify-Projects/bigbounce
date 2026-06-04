"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Activity,
  BarChart3,
  BookOpen,
  Code2,
  Database,
  FileText,
  Gauge,
  Globe,
  Home,
  Image,
  Library,
  Lightbulb,
  Map,
  MessageSquare,
  Orbit,
  Search,
  Sparkle,
  Telescope,
} from "lucide-react";
import { cn } from "@/lib/utils";

interface SidebarLink {
  href: string;
  label: string;
  icon: React.ComponentType<{ className?: string }>;
  external?: boolean;
}

interface SidebarSection {
  label?: string;
  links: SidebarLink[];
}

const sections: SidebarSection[] = [
  {
    links: [
      { href: "/search", label: "search", icon: Search },
      { href: "/", label: "overview", icon: Home },
      { href: "/explained", label: "explainer", icon: BookOpen },
    ],
  },
  {
    label: "research",
    links: [
      { href: "/surveys", label: "surveys", icon: Database },
      { href: "/predictions", label: "predictions", icon: Orbit },
      { href: "/paper", label: "papers", icon: FileText },
      { href: "/contributions", label: "contributions", icon: Sparkle },
    ],
  },
  {
    label: "explore",
    links: [
      { href: "/data-explorer", label: "data explorer", icon: BarChart3 },
      { href: "/galaxy-explorer", label: "galaxy explorer", icon: Globe },
      { href: "/anomaly-explorer", label: "anomaly explorer", icon: Telescope },
      { href: "/visualize", label: "visualize", icon: Orbit },
      { href: "/figures", label: "figures", icon: Image },
      { href: "/glossary", label: "glossary", icon: Library },
      { href: "/timeline", label: "timeline", icon: Map },
    ],
  },
  {
    label: "articles",
    links: [
      { href: "/articles", label: "articles", icon: BookOpen },
      { href: "/speculations", label: "speculations", icon: Lightbulb },
    ],
  },
  {
    label: "chat",
    links: [
      { href: "/chat", label: "astro chat", icon: MessageSquare },
    ],
  },
];

const tail: SidebarLink[] = [
  { href: "/activity", label: "activity", icon: Activity },
  { href: "/status", label: "status", icon: Gauge },
  { href: "/docs", label: "docs", icon: Code2 },
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
  const Icon = link.icon;
  const className = cn(
    "sidebar-link",
    active && "is-active",
  );
  if (link.external) {
    return (
      <a href={link.href} className={className}>
        <Icon />
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
      <Icon />
      {link.label}
    </Link>
  );
}

export function Sidebar() {
  const pathname = usePathname() ?? "/";
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <Link href="/" className="sidebar-brand-home" aria-label="BigBounce — home">
          <svg
            className="sidebar-brand-mark"
            viewBox="0 0 64 64"
            fill="none"
            aria-hidden="true"
          >
            <circle cx="20" cy="32" r="10" fill="none" stroke="currentColor" strokeWidth="3" />
            <circle cx="20" cy="32" r="3" fill="currentColor" />
            <g fill="currentColor">
              <circle cx="34" cy="32" r="1.8" />
              <circle cx="38" cy="28" r="1.5" />
              <circle cx="38" cy="36" r="1.5" />
              <circle cx="42" cy="24" r="1.3" />
              <circle cx="42" cy="32" r="1.3" />
              <circle cx="42" cy="40" r="1.3" />
              <circle cx="46" cy="20" r="1.1" />
              <circle cx="46" cy="28" r="1.1" />
              <circle cx="46" cy="36" r="1.1" />
              <circle cx="46" cy="44" r="1.1" />
              <circle cx="50" cy="24" r="0.9" />
              <circle cx="50" cy="32" r="0.9" />
              <circle cx="50" cy="40" r="0.9" />
              <circle cx="54" cy="28" r="0.7" />
              <circle cx="54" cy="36" r="0.7" />
              <circle cx="58" cy="32" r="0.6" />
            </g>
          </svg>
          <span className="sidebar-brand-name">BigBounce</span>
        </Link>
        <a
          href="https://hubify.com"
          target="_blank"
          rel="noopener noreferrer"
          className="sidebar-brand-kicker"
        >
          Hubify research lab
        </a>
      </div>
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
        <div className="mb-2">
          <span className="sidebar-footer-kicker">
            live dossier
          </span>
        </div>
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
