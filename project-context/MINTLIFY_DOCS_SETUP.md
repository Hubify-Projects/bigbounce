# K8 — Mintlify Docs Port: Exact Hubify Subpath Setup

**Status:** Spec complete (K8 BUILD_READINESS loop, 2026-04-09)
**Author:** Claude (BUILD_READINESS loop) — extracted from `/Users/houstongolden/Desktop/CODE_2025/hubify/`
**Purpose:** Preserve the exact Mintlify subpath setup so it doesn't need to be re-discovered. Houston: "it was annoyingly complex (issue prone) to get it right on the hubify.com/docs subpath vs subdomain so don't wanna go through that nightmare again."

---

## 0. The Core Insight

Mintlify defaults to deploying as a **subdomain** (`docs.yourdomain.com`). Getting it to serve at a **subpath** (`yourdomain.com/docs`) requires a **Next.js rewrite proxy** pattern. The Mintlify site is still deployed to its own Mintlify subdomain (`bamf.mintlify.dev` in the hubify case), but Next.js rewrites all `/docs/*` traffic to that Mintlify URL transparently — so users see `hubify.com/docs/...` in their browser.

**Key:** Do NOT set `basePath` in `docs.json`. The rewrite handles this. Setting `basePath` will break internal links.

---

## 1. What Exists in the hubify Repo

Reference path: `/Users/houstongolden/Desktop/CODE_2025/hubify/`

| File | Purpose |
|------|---------|
| `docs/` | Mintlify docs source directory — all `.mdx` pages, `docs.json` config, `favicon.svg`, `logo/` |
| `docs/docs.json` | Mintlify configuration (no `basePath` — handled by Next.js rewrites) |
| `apps/web/next.config.ts` | Contains the rewrite rules that proxy `/docs/*` to Mintlify |

---

## 2. The Next.js Rewrite Rules (exact copy)

In `apps/web/next.config.ts` (or equivalent `next.config.js`), inside the `rewrites()` function:

```typescript
// Proxy /docs/* to Mintlify
async rewrites() {
  return {
    beforeFiles: [
      {
        source: "/docs",
        destination: "https://bamf.mintlify.dev/docs",
      },
      {
        source: "/docs/:path*",
        destination: "https://bamf.mintlify.dev/docs/:path*",
      },
    ],
  };
},
```

**Why `beforeFiles` (not `afterFiles`)?** `beforeFiles` runs before Next.js checks for pages/api routes. This means `/docs` won't accidentally match a static file or page in the Next.js app. If you put this in `afterFiles`, it won't fire for routes that exist in Next.js.

**For Hubify Labs:** Replace `bamf` with whatever Mintlify deployment slug is assigned. The slug is chosen during the Mintlify dashboard setup (below).

---

## 3. Mintlify Dashboard Setup

### 3.1 Create a new Mintlify project

1. Go to [dashboard.mintlify.com](https://dashboard.mintlify.com)
2. Click "New Project"
3. Connect the `Hubify-Projects/hubify-labs` GitHub repo
4. Set the **docs directory** to `/docs` (not root — the docs source lives in a subdirectory)
5. Choose a deployment slug (e.g., `hubify-labs`) → site will be at `hubify-labs.mintlify.dev`

### 3.2 Key dashboard settings

| Setting | Value | Notes |
|---------|-------|-------|
| Repository | `Hubify-Projects/hubify-labs` | or wherever the platform repo lives |
| Docs directory | `docs/` | relative to repo root |
| Branch | `main` | auto-deploy on push |
| Custom domain | Leave blank | NOT setting a custom domain — Next.js handles routing |
| Deployment slug | `hubify-labs` | choose something human-readable |

### 3.3 Do NOT configure a custom domain in Mintlify

The custom domain approach is `docs.hubify-labs.com` (subdomain). We do NOT want that — we want `hubify-labs.com/docs` (subpath). The Mintlify site lives at `hubify-labs.mintlify.dev` only. The Next.js rewrite makes it appear at the subpath.

---

## 4. The `docs.json` Configuration

This is the exact pattern from the working hubify setup. Key points:

```json
{
  "$schema": "https://mintlify.com/docs.json",
  "theme": "mint",
  "name": "Hubify Labs Docs",
  "colors": {
    "primary": "#3d7a5c",
    "light": "#5fb88a",
    "dark": "#3d7a5c"
  },
  "favicon": "/favicon.svg",
  "font": {
    "headings": { "family": "Inter", "weight": 600 },
    "body": { "family": "Inter" }
  },
  "logo": {
    "light": "/logo/light.svg",
    "dark": "/logo/dark.svg",
    "href": "https://hubify-labs.com"
  },
  "navbar": {
    "links": [
      { "label": "App", "href": "https://hubify-labs.com/app" }
    ],
    "primary": {
      "type": "button",
      "label": "hubify-labs.com",
      "href": "https://hubify-labs.com"
    }
  },
  "navigation": {
    "tabs": [
      {
        "tab": "Guides",
        "groups": [
          {
            "group": "Getting Started",
            "pages": ["introduction", "quickstart", "installation"]
          }
        ]
      },
      {
        "tab": "CLI Reference",
        "groups": [...]
      },
      {
        "tab": "API Reference",
        "groups": [...]
      }
    ]
  },
  "footer": {
    "socials": {
      "github": "https://github.com/Hubify-Projects/hubify-labs",
      "x": "https://twitter.com/hubifylabs"
    }
  }
}
```

**CRITICAL:** No `basePath` field. No `baseUrl` field. Mintlify picks up its own URL from the deployment automatically. The subpath behavior comes entirely from the Next.js rewrite.

---

## 5. Gotchas Houston Hit (and how we avoid them)

### Gotcha 1: Subdomain vs. subpath in Mintlify dashboard
**Problem:** Mintlify dashboard has a "Custom domain" field. If you put `hubify-labs.com` there, it tries to take over the whole domain, not just `/docs`. Mintlify expects subdomains in the custom domain field (e.g., `docs.hubify-labs.com`).
**Fix:** Leave the custom domain field blank. Use Next.js rewrites only.

### Gotcha 2: Static assets not loading
**Problem:** Mintlify generates HTML with absolute paths for its JS/CSS bundles. If the Mintlify deployment is at `hubify-labs.mintlify.dev` but the user's browser sees `hubify-labs.com/docs`, the static assets are fetched from `hubify-labs.mintlify.dev` directly — which works because they're CORS-permissive CDN assets.
**Fix:** No action needed. Mintlify's CDN assets load fine cross-origin.

### Gotcha 3: Internal links not using `/docs/` prefix
**Problem:** Mintlify links between pages as `/page-slug` not `/docs/page-slug`. If someone visits `hubify-labs.com/docs/quickstart` via the proxy, internal links like `/installation` go to `hubify-labs.com/installation` (not found), not `hubify-labs.com/docs/installation`.
**Fix:** The Mintlify proxy handles this because the rewrite passes the full `/docs/:path*` pattern. When Mintlify renders the page, all internal links on the Mintlify side are `/docs/...` because Mintlify knows its base URL. The proxy mirrors those paths exactly. This is why it's a `beforeFiles` rewrite at `/docs/:path*` — every path with `/docs/` prefix is proxied.

### Gotcha 4: `/docs` without trailing slash redirects
**Problem:** Some browsers/CDNs redirect `/docs` to `/docs/`. The rewrite for `/docs` (no path) handles the bare case; `/docs/:path*` handles everything else.
**Fix:** Both rules needed (line 83-90 in the example above).

### Gotcha 5: Algolia DocSearch configuration
**Problem:** Algolia crawls `hubify-labs.com/docs/...` (the Next.js proxy) but indexes content from Mintlify's CDN origin. If the Algolia crawler follows redirect headers, it may end up crawling the Mintlify subdomain instead.
**Fix:** Configure Algolia with `startUrls: ["https://hubify-labs.com/docs/"]` and set `pathsToMatch: ["https://hubify-labs.com/docs/**"]` to force the crawler to stay on the public-facing URL.

---

## 6. Migration Checklist for Hubify Labs

When porting to the Hubify Labs repo (`Hubify-Projects/hubify-labs`):

1. **Copy `docs/` directory** from `hubify/docs/` as starting structure
2. **Update `docs/docs.json`**: Change name, colors (`#3d7a5c` sage accent), logo paths, navbar links, footer GitHub link
3. **Update page content**: Start with 7 pages from PRD §47 outline:
   - `introduction.mdx` — What is Hubify Labs
   - `quickstart.mdx` — From zero to first experiment in 5 minutes
   - `labs.mdx` — Labs = repos concept
   - `agents.mdx` — The 21-agent hierarchy
   - `cli.mdx` — `hubify` CLI reference (auto-generated from `cli-spec.yaml`)
   - `api.mdx` — REST + GraphQL API reference (auto-generated from `API_SPEC.md`)
   - `mcp.mdx` — MCP server tool/resource/prompt reference
4. **Add Next.js rewrites** in `apps/web/next.config.ts` (or equivalent): replace `bamf.mintlify.dev` with the new Mintlify deployment slug
5. **Set up Mintlify project** in dashboard (see §3 above)
6. **Verify** by visiting `hubify-labs.com/docs` — should serve Mintlify content
7. **Set up Algolia DocSearch** (optional, Tier 4): point crawler at `hubify-labs.com/docs/`

---

## 7. Auto-generation Pipeline (PRD §47 requirement)

The codegen pipeline that auto-generates API/CLI reference from YAML specs:

```bash
# On every commit (CI or Vercel build hook):
# 1. Generate API reference from API_SPEC.md + openapi.yaml
bun run scripts/gen-api-docs.ts \
  --input project-context/API_SPEC.md \
  --output docs/api/

# 2. Generate CLI reference from cli-spec.yaml
bun run scripts/gen-cli-docs.ts \
  --input project-context/cli-spec.yaml \
  --output docs/cli/

# 3. Generate MCP reference from mcp-server-spec.yaml
bun run scripts/gen-mcp-docs.ts \
  --input project-context/mcp-server-spec.yaml \
  --output docs/mcp/
```

These scripts are rebuild-phase work (not mockup). The scripts read the existing YAML/markdown specs and emit `.mdx` files with proper Mintlify frontmatter. The human-written pages (`introduction.mdx`, `quickstart.mdx`, `labs.mdx`, `agents.mdx`) are written manually and versioned in the repo.

---

## 8. Acceptance Criteria

- [ ] Mintlify project created in dashboard, connected to `Hubify-Projects/hubify-labs` repo
- [ ] `docs/docs.json` configured with Hubify Labs branding (sage `#3d7a5c`, Inter fonts, correct nav links)
- [ ] Next.js `next.config.ts` rewrite rules added (both `/docs` and `/docs/:path*`)
- [ ] `hubify-labs.com/docs` resolves and serves Mintlify content without white-flash or redirect loops
- [ ] Internal navigation within docs works (clicking nav links stays on `hubify-labs.com/docs/...`)
- [ ] 7 starter pages present (introduction, quickstart, labs, agents, cli stub, api stub, mcp stub)
- [ ] Codegen pipeline defined (scripts exist, even if not fully implemented — just so the pattern is established)

---

## 9. What NOT to Do

- **Don't** set `"basePath": "/docs"` in `docs.json` — this breaks Mintlify's internal routing
- **Don't** configure a custom domain in the Mintlify dashboard pointing to `hubify-labs.com` — the proxy handles domain routing
- **Don't** put Mintlify docs in the same Next.js repo without the `docs/` subdirectory — the Mintlify dashboard expects a distinct docs root
- **Don't** use `afterFiles` rewrites — they lose to Next.js static file matching
- **Don't** add the Mintlify deployment URL to CSP `connect-src` or `frame-src` — docs pages load fine without it (Mintlify assets come from their own CDN with proper CORS headers)
