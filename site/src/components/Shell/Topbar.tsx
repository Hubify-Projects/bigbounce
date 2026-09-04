"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Menu, Moon, Search, Sun, X } from "lucide-react";
import { cn } from "@/lib/utils";

type Theme = "light" | "dark";

const THEME_KEY = "bigbounce-theme";

const NAV_ITEMS = [
  { href: "/research", label: "Research" },
  { href: "/papers", label: "Works" },
  { href: "/explore", label: "Explore" },
  { href: "/reproduce", label: "Reproduce" },
  { href: "/status", label: "Status" },
  { href: "/learn", label: "Learn" },
];

function readInitialTheme(): Theme | null {
  if (typeof window === "undefined") return null;
  const saved = window.localStorage.getItem(THEME_KEY);
  if (saved === "light" || saved === "dark") return saved;
  return null;
}

function getBrowserTheme(): Theme {
  const saved = readInitialTheme();
  if (saved) return saved;
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme: Theme) {
  document.documentElement.setAttribute("data-theme", theme);
}

/** Slim sticky topbar: wordmark, six nav items, ⌘K search, theme toggle, live dot. */
export function Topbar() {
  const pathname = usePathname();
  const [theme, setTheme] = useState<Theme>("light");
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const next = getBrowserTheme();
    applyTheme(next);
    queueMicrotask(() => setTheme(next));
  }, []);

  useEffect(() => {
    setMobileOpen(false);
  }, [pathname]);

  function toggleTheme() {
    const next: Theme = theme === "dark" ? "light" : "dark";
    setTheme(next);
    applyTheme(next);
    window.localStorage.setItem(THEME_KEY, next);
  }

  function openSearch() {
    window.dispatchEvent(new CustomEvent("bigbounce:open-search"));
  }

  const themeLabel = theme === "dark" ? "Switch to light theme" : "Switch to dark theme";

  return (
    <header className="topbar topbar-slim">
      <Link href="/" className="topbar-wordmark">
        bigbounce
      </Link>
      <nav className="topbar-nav" aria-label="Primary">
        {NAV_ITEMS.map((item) => {
          const active = pathname === item.href || pathname.startsWith(`${item.href}/`);
          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn("topbar-nav-link", active && "topbar-nav-link-active")}
            >
              {item.label}
            </Link>
          );
        })}
      </nav>
      <div className="topbar-right">
        <button
          className="topbar-search"
          onClick={openSearch}
          aria-label="Search (⌘K)"
          title="Search (⌘K)"
        >
          <Search size={14} />
          <span className="topbar-search-kbd">⌘K</span>
        </button>
        <span className="status-dot" aria-hidden="true" />
        <button
          className="theme-toggle"
          onClick={toggleTheme}
          aria-label={themeLabel}
          title={themeLabel}
          suppressHydrationWarning
        >
          <span className="theme-icon" suppressHydrationWarning>
            {theme === "dark" ? <Sun size={14} /> : <Moon size={14} />}
          </span>
        </button>
        <button
          className="topbar-mobile-toggle"
          onClick={() => setMobileOpen((v) => !v)}
          aria-label={mobileOpen ? "Close menu" : "Menu"}
          aria-expanded={mobileOpen}
          aria-controls="topbar-mobile-nav"
        >
          {mobileOpen ? <X size={16} /> : <Menu size={16} />}
        </button>
      </div>
      {mobileOpen && (
        <nav id="topbar-mobile-nav" className="topbar-mobile-nav" aria-label="Primary (mobile)">
          {NAV_ITEMS.map((item) => {
            const active = pathname === item.href || pathname.startsWith(`${item.href}/`);
            return (
              <Link
                key={item.href}
                href={item.href}
                className={cn("topbar-mobile-nav-link", active && "topbar-nav-link-active")}
              >
                {item.label}
              </Link>
            );
          })}
        </nav>
      )}
    </header>
  );
}
