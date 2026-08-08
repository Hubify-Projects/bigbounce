---
pattern_id: spattern-broken-image-or-link
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-broken-image-or-link — Site page has a broken image or dead internal/external link

## Defect

A page on the live site (any route) renders a broken image (`<img>` 404,
blank box with alt text, or missing placeholder) or contains a link that
returns a non-200 HTTP status. This covers internal routes (Next.js pages),
external URLs (GitHub, arXiv, Zenodo, HuggingFace), and figure/gallery images
served from `site/public/`.

## How to detect

- Walk every site route with a headless browser (`/qa` / `/browse`). Capture
  console errors (`Failed to load resource`) and network errors (image 404s).
- For external links: `curl -L -o /dev/null -w "%{http_code}" <url>` — any
  4xx / 5xx is a hit (allow 403 for gated HF resources only if expected).
- For images in `site/public/images/`: verify each filename referenced in
  source code exists on disk and has been deployed.

## Fix

- Broken internal image: add the file to `site/public/images/` or fix the path
  in the component.
- Dead internal route: fix the Next.js page or redirect; never 404 a page that
  was previously live.
- Dead external link: update the URL in `papers.ts` / the component / the paper
  `.tex` source (for `\artifact{}` links) and recompile if needed.
