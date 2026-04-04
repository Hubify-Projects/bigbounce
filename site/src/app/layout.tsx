import type { Metadata } from "next";
import { Inter, IBM_Plex_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const ibmPlexMono = IBM_Plex_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
  weight: ["400", "500", "600"],
});

export const metadata: Metadata = {
  title: {
    default: "BigBounce — Spin-Torsion Cosmology",
    template: "%s — BigBounce",
  },
  description:
    "A comprehensive spin-torsion cosmology research program exploring bounce cosmology as an alternative to inflation.",
  metadataBase: new URL("https://bigbounce.hubify.app"),
  openGraph: {
    siteName: "BigBounce — Spin-Torsion Cosmology",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${ibmPlexMono.variable}`}
      suppressHydrationWarning
    >
      <body>
        <div className="shell">
          <aside className="sidebar">
            <a href="/" className="sidebar-brand">BigBounce</a>
            <nav className="sidebar-nav">
              <div className="sidebar-section">
                <a href="/" className="sidebar-link" data-page="index">research/</a>
                <a href="/paper" className="sidebar-link" data-page="paper">papers</a>
                <a href="/explained" className="sidebar-link" data-page="explained">explainer</a>
              </div>
              <div className="sidebar-section">
                <div className="sidebar-section-label">data &amp; explore</div>
                <a href="/data-explorer" className="sidebar-link" data-page="data-explorer">data explorer</a>
                <a href="/anomaly-explorer" className="sidebar-link" data-page="anomaly-explorer">anomaly explorer</a>
                <a href="/galaxy-explorer" className="sidebar-link" data-page="galaxy-explorer">galaxy explorer</a>
                <a href="/figures" className="sidebar-link" data-page="figures">figures</a>
                <a href="/datasets" className="sidebar-link" data-page="datasets">datasets</a>
              </div>
              <div className="sidebar-section">
                <div className="sidebar-section-label">reference</div>
                <a href="/glossary" className="sidebar-link" data-page="glossary">glossary</a>
                <a href="/articles" className="sidebar-link" data-page="articles">articles</a>
                <a href="/contributions" className="sidebar-link" data-page="contributions">contributions</a>
                <a href="/methodology" className="sidebar-link" data-page="methodology">methodology</a>
                <a href="/sources" className="sidebar-link" data-page="sources">sources</a>
              </div>
              <div className="sidebar-section">
                <div className="sidebar-section-label">visualize</div>
                <a href="/timeline" className="sidebar-link" data-page="timeline">timeline</a>
                <a href="/visualize" className="sidebar-link" data-page="visualize">visualize</a>
                <a href="/animations" className="sidebar-link" data-page="animations">animations</a>
              </div>
              <div className="sidebar-separator" />
              <div className="sidebar-section">
                <a href="/speculations" className="sidebar-link" data-page="speculations">speculations</a>
                <a href="/infrastructure" className="sidebar-link" data-page="infrastructure">infrastructure</a>
                <a href="/activity" className="sidebar-link" data-page="activity">activity</a>
                <a href="/status" className="sidebar-link" data-page="status">status</a>
                <a href="/sitemap" className="sidebar-link" data-page="sitemap">sitemap</a>
              </div>
            </nav>
            <div className="sidebar-footer">
              <div className="sidebar-footer-name">Houston Golden</div>
              <div className="sidebar-footer-role">Independent Researcher</div>
              <a href="https://github.com/Hubify-Projects/bigbounce" className="sidebar-footer-link" target="_blank" rel="noopener">GitHub</a>
            </div>
          </aside>

          <header className="topbar">
            <span>Spin-Torsion Cosmology Research Program</span>
            <div className="topbar-right">
              <span>Houston Golden</span>
              <button className="theme-toggle" aria-label="Toggle theme">
                <span className="theme-icon">◑</span>
              </button>
            </div>
          </header>

          <main className="content">
            <div className="container">
              {children}
            </div>
          </main>
        </div>
      </body>
    </html>
  );
}
