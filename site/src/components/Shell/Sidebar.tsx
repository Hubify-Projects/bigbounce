"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Activity,
  BarChart3,
  BookOpen,
  Database,
  FileText,
  Gauge,
  Globe,
  Home,
  Image,
  Library,
  Lightbulb,
  Map,
  Orbit,
  Search,
  Sparkles,
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
    ],
  },
  {
    label: "explore",
    links: [
      { href: "/data-explorer", label: "data explorer", icon: BarChart3 },
      { href: "/galaxy-explorer", label: "galaxy explorer", icon: Globe },
      { href: "/anomaly-explorer", label: "anomaly explorer", icon: Telescope },
      { href: "/visualize", label: "visualize", icon: Sparkle },
      { href: "/figures", label: "figures", icon: Image },
      { href: "/glossary", label: "glossary", icon: Library },
      { href: "/timeline", label: "timeline", icon: Map },
    ],
  },
  {
    label: "articles",
    links: [
      { href: "/articles", label: "articles", icon: Search },
      { href: "/speculations", label: "speculations", icon: Lightbulb },
    ],
  },
];

const tail: SidebarLink[] = [
  { href: "/activity", label: "activity", icon: Activity },
  { href: "/status", label: "status", icon: Gauge },
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
      <Link href="/" className="sidebar-brand">
        BigBounce
        <span className="sidebar-brand-kicker">
          Hubify research lab
        </span>
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
        <div className="mb-2 flex items-center gap-2">
          <Sparkles size={14} className="sidebar-footer-icon" />
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
