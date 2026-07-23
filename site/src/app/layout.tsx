import Script from "next/script";
import type { Metadata } from "next";
import { GeistSans } from "geist/font/sans";
import { GeistMono } from "geist/font/mono";
import { Sidebar } from "@/components/Shell/Sidebar";
import { ScrollToTop } from "@/components/Shell/ScrollToTop";
import { Topbar } from "@/components/Shell/Topbar";
import "./globals.css";

const themeBootScript = `
(function(){
  try {
    var savedTheme = localStorage.getItem('bigbounce-theme');
    var theme = (savedTheme === 'light' || savedTheme === 'dark')
      ? savedTheme
      : (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
    var savedSidebar = localStorage.getItem('bigbounce-sidebar');
    if (savedSidebar === 'collapsed') {
      document.documentElement.setAttribute('data-sidebar-collapsed', '');
    }
  } catch (e) {}
})();
`;

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
      className={`${GeistSans.variable} ${GeistMono.variable}`}
      suppressHydrationWarning
    >
      <head />
      <body>
        <Script
          id="bigbounce-theme-boot"
          strategy="beforeInteractive"
          dangerouslySetInnerHTML={{ __html: themeBootScript }}
        />
        <div className="shell">
          <ScrollToTop />
          <Sidebar />
          <Topbar />
          <main className="content">
            <div className="container">
              {children}
            </div>
          </main>
        </div>
        {/* Astro chat widget REMOVED 2026-07-22 (site audit): its /api/chat
            backend does not exist on this static deployment (and no Convex
            HTTP route serves it), so the bubble and /chat mount were dead UI.
            /chat now renders an honest offline state. Restore the <Script
            src="/old/astro/chat-widget.js"> include only together with a
            working backend. */}
      </body>
    </html>
  );
}
