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
                <a href="/" className="sidebar-link">overview</a>
                <a href="/explained" className="sidebar-link">explainer</a>
              </div>
              <div className="sidebar-section">
                <div className="sidebar-section-label">research</div>
                <a href="/surveys" className="sidebar-link">surveys (8)</a>
                <a href="/predictions" className="sidebar-link">predictions (4)</a>
                <a href="/paper" className="sidebar-link">papers (4)</a>
              </div>
              <div className="sidebar-section">
                <div className="sidebar-section-label">explore</div>
                <a href="/data-explorer" className="sidebar-link">data explorer</a>
                <a href="/figures" className="sidebar-link">figures</a>
                <a href="/glossary" className="sidebar-link">glossary</a>
                <a href="/timeline" className="sidebar-link">timeline</a>
              </div>
              <div className="sidebar-section">
                <div className="sidebar-section-label">articles</div>
                <a href="/articles" className="sidebar-link">all articles</a>
                <a href="/speculations" className="sidebar-link">speculations</a>
              </div>
              <div className="sidebar-separator" />
              <div className="sidebar-section">
                <a href="/activity" className="sidebar-link">activity</a>
                <a href="/status" className="sidebar-link">status</a>
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
