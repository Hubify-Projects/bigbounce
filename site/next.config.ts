import type { NextConfig } from "next";
import { dirname } from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = dirname(fileURLToPath(import.meta.url));

const nextConfig: NextConfig = {
  turbopack: {
    root: siteRoot,
  },

  // Static export for Netlify/Vercel static hosting (same as current site)
  output: "export",

  // Images are all in public/ — no need for image optimization server
  images: {
    unoptimized: true,
  },

  // Trailing slashes to match current URL structure
  trailingSlash: false,
};

export default nextConfig;
