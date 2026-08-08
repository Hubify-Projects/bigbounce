"use client";

import { useEffect, useState } from "react";
import { Menu, Moon, Sun } from "lucide-react";

type Theme = "light" | "dark";

const THEME_KEY = "bigbounce-theme";
const SIDEBAR_KEY = "bigbounce-sidebar";

function readInitialTheme(): Theme | null {
  if (typeof window === "undefined") return null;
  const saved = window.localStorage.getItem(THEME_KEY);
  if (saved === "light" || saved === "dark") return saved;
  return null;
}

function getBrowserTheme(): Theme {
  const saved = readInitialTheme();
  if (saved) return saved;
  return window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
}

function applyTheme(theme: Theme) {
  document.documentElement.setAttribute("data-theme", theme);
}

function setMobileOpen(open: boolean) {
  const root = document.documentElement;
  if (open) root.setAttribute("data-sidebar", "open");
  else root.removeAttribute("data-sidebar");
}

function toggleSidebar() {
  const root = document.documentElement;
  const isMobile = window.matchMedia("(max-width: 900px)").matches;
  if (isMobile) {
    const open = root.getAttribute("data-sidebar") === "open";
    setMobileOpen(!open);
    return;
  }
  const collapsed = root.hasAttribute("data-sidebar-collapsed");
  if (collapsed) {
    root.removeAttribute("data-sidebar-collapsed");
    window.localStorage.setItem(SIDEBAR_KEY, "expanded");
  } else {
    root.setAttribute("data-sidebar-collapsed", "");
    window.localStorage.setItem(SIDEBAR_KEY, "collapsed");
  }
}

export function Topbar() {
  // Keep the server and the first client render identical. Browser preferences
  // are applied only after hydration; the inline boot script prevents a flash.
  const [theme, setTheme] = useState<Theme>("light");

  useEffect(() => {
    const next = getBrowserTheme();
    applyTheme(next);
    queueMicrotask(() => setTheme(next));
  }, []);

  function toggleTheme() {
    const next: Theme = theme === "dark" ? "light" : "dark";
    setTheme(next);
    applyTheme(next);
    window.localStorage.setItem(THEME_KEY, next);
  }

  const themeLabel = theme === "dark" ? "Switch to light theme" : "Switch to dark theme";

  return (
    <>
      <header className="topbar">
        <span className="topbar-left">
          <button
            className="nav-toggle"
            onClick={toggleSidebar}
            aria-label="Toggle navigation"
            title="Toggle navigation"
          >
            <Menu size={16} />
          </button>
          <span className="breadcrumb">
            <span>bigbounce</span>
            <span>/</span>
            <span className="breadcrumb-current">
              spin-torsion cosmology research program
            </span>
          </span>
        </span>
        <div className="topbar-right">
          <span className="status-dot" aria-hidden="true" />
          <span>research live</span>
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
        </div>
      </header>
      <div
        className="sidebar-backdrop"
        onClick={() => setMobileOpen(false)}
        aria-hidden="true"
      />
    </>
  );
}
