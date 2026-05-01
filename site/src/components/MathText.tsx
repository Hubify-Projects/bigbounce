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

export function MathText({
  children,
  className,
}: {
  children: string;
  className?: string;
}) {
  const parts = children.split(TOKEN_RE);

  return (
    <span className={cn("math-text", className)}>
      {parts.map((part, index) => (
        isMathToken(part) ? renderToken(part, index) : part
      ))}
    </span>
  );
}
