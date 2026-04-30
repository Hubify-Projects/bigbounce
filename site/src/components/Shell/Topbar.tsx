"use client";

import { useEffect, useState } from "react";

type Theme = "light" | "dark";

const STORAGE_KEY = "bigbounce-theme";

function readInitialTheme(): Theme | null {
  if (typeof window === "undefined") return null;
  const saved = window.localStorage.getItem(STORAGE_KEY);
  if (saved === "light" || saved === "dark") return saved;
  return null;
}

function applyTheme(theme: Theme) {
  document.documentElement.setAttribute("data-theme", theme);
}

export function Topbar() {
  const [theme, setTheme] = useState<Theme | null>(null);

  useEffect(() => {
    const saved = readInitialTheme();
    if (saved) {
      setTheme(saved);
      applyTheme(saved);
      return;
    }
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const initial: Theme = prefersDark ? "dark" : "light";
    setTheme(initial);
    applyTheme(initial);
  }, []);

  function toggle() {
    const next: Theme = theme === "dark" ? "light" : "dark";
    setTheme(next);
    applyTheme(next);
    window.localStorage.setItem(STORAGE_KEY, next);
  }

  const icon = theme === "dark" ? "☀" : "☾";
  const label = theme === "dark" ? "Switch to light theme" : "Switch to dark theme";

  return (
    <header className="topbar">
      <span>Spin-Torsion Cosmology Research Program</span>
      <div className="topbar-right">
        <span>Houston Golden</span>
        <button
          className="theme-toggle"
          onClick={toggle}
          aria-label={label}
          title={label}
          suppressHydrationWarning
        >
          <span className="theme-icon" suppressHydrationWarning>
            {theme ? icon : "◑"}
          </span>
        </button>
      </div>
    </header>
  );
}
