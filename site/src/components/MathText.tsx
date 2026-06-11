import type { ReactNode } from "react";

import { cn } from "@/lib/utils";

const TOKEN_RE =
  /(f_NL|Omega_k|sigma8|H_0|H0|S_8|w\(z\)|(?<![A-Za-z])w0(?![A-Za-z])|(?<![A-Za-z])wa(?![A-Za-z])|Lambda_eff|β|γ|σ|\d+(?:\.\d+)?\s?σ)/g;

function isMathToken(token: string): boolean {
  return /^(f_NL|Omega_k|sigma8|H_0|H0|S_8|w\(z\)|w0|wa|Lambda_eff|β|γ|σ|\d+(?:\.\d+)?\s?σ)$/.test(token);
}

function renderToken(token: string, key: number): ReactNode {
  switch (token) {
    case "f_NL":
      return <span key={key} className="math-inline"><i>f</i><sub>NL</sub></span>;
    case "Omega_k":
      return <span key={key} className="math-inline">Ω<sub>k</sub></span>;
    case "sigma8":
      return <span key={key} className="math-inline">σ<sub>8</sub></span>;
    case "H0":
    case "H_0":
      return <span key={key} className="math-inline"><i>H</i><sub>0</sub></span>;
    case "S_8":
      return <span key={key} className="math-inline"><i>S</i><sub>8</sub></span>;
    case "w(z)":
      return <span key={key} className="math-inline"><i>w</i>(<i>z</i>)</span>;
    case "w0":
      return <span key={key} className="math-inline"><i>w</i><sub>0</sub></span>;
    case "wa":
      return <span key={key} className="math-inline"><i>w</i><sub>a</sub></span>;
    case "Lambda_eff":
      return <span key={key} className="math-inline">Λ<sub>eff</sub></span>;
    case "β":
    case "γ":
    case "σ":
      return <span key={key} className="math-inline">{token}</span>;
    default:
      if (token.includes("σ")) {
        return <span key={key} className="math-inline">{token.replace(/\s/g, "")}</span>;
      }
      return token;
  }
}

/**
 * Defensive LaTeX → unicode normalization (QA sweep P1-8). Convex-fed strings
 * (notables / focusAreas) occasionally arrive with raw inline math like
 * `$p_{\rm CW}^{\rm eq} > 0.9$` or `$\ell=1$`. Canonical fix is unicode at the
 * source; this layer guarantees readers never see un-typeset TeX even if a
 * raw string slips through a future sync.
 */
function normalizeLatexSegment(s: string): string {
  return s
    .replace(/\\mathrm\{([^}]*)\}/g, "$1")
    .replace(/\\text\{([^}]*)\}/g, "$1")
    .replace(/\{\\rm\s+([^}]*)\}/g, "$1")
    .replace(/\\rm\s*/g, "")
    .replace(/\\ell\b/g, "ℓ")
    .replace(/\\sigma\b/g, "σ")
    .replace(/\\beta\b/g, "β")
    .replace(/\\gamma\b/g, "γ")
    .replace(/\\alpha\b/g, "α")
    .replace(/\\Delta\b/g, "Δ")
    .replace(/\\Lambda\b/g, "Λ")
    .replace(/\\chi\b/g, "χ")
    .replace(/\\mu\b/g, "μ")
    .replace(/\\tau\b/g, "τ")
    .replace(/\\times\b/g, "×")
    .replace(/\\gtrsim\b/g, "≳")
    .replace(/\\lesssim\b/g, "≲")
    .replace(/\\geq?\b/g, "≥")
    .replace(/\\leq?\b/g, "≤")
    .replace(/\\approx\b/g, "≈")
    .replace(/\\sim\b/g, "~")
    .replace(/\\pm\b/g, "±")
    .replace(/\\circ\b/g, "°")
    .replace(/\\,|\\;|\\!|\\ /g, " ")
    .replace(/[{}]/g, "");
}

function normalizeLatex(s: string): string {
  if (!s.includes("$")) return s;
  return s.replace(/\$([^$]+)\$/g, (_m, inner: string) => normalizeLatexSegment(inner));
}

export function MathText({
  children,
  className,
}: {
  children: string;
  className?: string;
}) {
  const parts = normalizeLatex(children).split(TOKEN_RE);

  return (
    <span className={cn("math-text", className)}>
      {parts.map((part, index) => (
        isMathToken(part) ? renderToken(part, index) : part
      ))}
    </span>
  );
}
