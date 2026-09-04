import Link from "next/link";
import { liveStatus } from "@/data/live-status";

interface FooterLink {
  label: string;
  href: string;
  external?: boolean;
}

interface FooterColumn {
  title: string;
  links: FooterLink[];
}

const COLUMNS: FooterColumn[] = [
  {
    title: "Lab",
    links: [
      { label: "Overview", href: "/" },
      { label: "Explained", href: "/explained" },
      { label: "Timeline", href: "/timeline" },
      { label: "Contributions", href: "/research#contributions" },
    ],
  },
  {
    title: "Works",
    links: [
      { label: "All works", href: "/papers" },
      { label: "Research tracks", href: "/research" },
      { label: "Figures", href: "/explore/figures" },
      { label: "Predictions", href: "/predictions" },
    ],
  },
  {
    title: "Reproduce",
    links: [
      { label: "Manifests", href: "/reproduce" },
      { label: "Data sources", href: "/reproduce/surveys" },
      { label: "Releases & DOIs", href: "/reproduce#releases" },
      {
        label: "HuggingFace",
        href: "https://huggingface.co/Hubify-Projects",
        external: true,
      },
    ],
  },
  {
    title: "Build on it",
    links: [
      { label: "Docs", href: "/docs" },
      { label: "API & MCP architecture", href: "/docs/architecture" },
      {
        label: "GitHub",
        href: "https://github.com/Hubify-Projects/bigbounce",
        external: true,
      },
      { label: "Activity", href: "/activity" },
      { label: "Legacy archive", href: "/old" },
    ],
  },
];

/** Full-width, four-column, no-border footer (REDESIGN_SPEC.md §2.3). */
export function Footer() {
  return (
    <footer className="site-footer">
      <div className="site-footer-inner">
        <div className="site-footer-columns">
          {COLUMNS.map((col) => (
            <div key={col.title} className="site-footer-col">
              <p className="site-footer-col-title">{col.title}</p>
              <ul className="site-footer-links">
                {col.links.map((l) => (
                  <li key={l.href}>
                    {l.external ? (
                      <a href={l.href} target="_blank" rel="noreferrer">
                        {l.label}
                      </a>
                    ) : (
                      <Link href={l.href}>{l.label}</Link>
                    )}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
        <div className="site-footer-bottom mono">
          <span>Houston Golden · houston@hubify.com</span>
          <span className="site-footer-honesty">
            Nulls are published as nulls; readiness is read live from Convex.
          </span>
          <span className="site-footer-stamp">{liveStatus.lastUpdatedDisplay}</span>
        </div>
      </div>
    </footer>
  );
}
