import type { NextConfig } from "next";

const nextConfig: NextConfig = {
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
