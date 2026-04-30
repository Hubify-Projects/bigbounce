import type { Metadata } from "next";
import { Inter, IBM_Plex_Mono, Newsreader } from "next/font/google";
import { Sidebar } from "@/components/Shell/Sidebar";
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

const newsreader = Newsreader({
  variable: "--font-serif",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  style: ["normal", "italic"],
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
      className={`${inter.variable} ${ibmPlexMono.variable} ${newsreader.variable}`}
      suppressHydrationWarning
    >
      <body>
        <div className="shell">
          <Sidebar />

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
