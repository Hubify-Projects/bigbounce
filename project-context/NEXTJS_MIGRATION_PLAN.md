# BigBounce Next.js Migration Plan

**Author:** Houston Golden · **Date opened:** 2026-04-30 · **Status:** in flight (existing `site/` scaffold to be extended).

**Reference inputs read:** `CLAUDE.md` WEBSITE SYNC PROTOCOL + PAPER STATUS, `project-context/SSOT/README.md`, `project-context/SSOT/index.md`, root `*.html` listing, `style.css`, `vercel.json`, `package.json`, `server.js`, `index.html`, `data-explorer.html`, `activity.html`, `articles/` listing, existing `site/` scaffold.

**Critical pre-finding.** A Next.js 16 + Tailwind v4 + React 19 scaffold already exists at `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/` with ~12 partial routes, design-token globals.css ported from `style.css`, three card components, one feed component, and three typed data files (`papers.ts`, `predictions.ts`, `surveys.ts`). The scaffold has `output: "export"` (static export), no shadcn yet, and is NOT yet wired to the live domain. This plan **extends that scaffold** rather than creating a new one.

---

## 1. Architecture decisions

| Decision | Choice | Why |
|---|---|---|
| Next.js version | **Next 16 App Router** (already pinned in `site/package.json`) | App Router is the only path forward; the scaffold already uses it. `site/AGENTS.md` warns "this is NOT the Next.js you know" — read `node_modules/next/dist/docs/` before each new pattern. |
| Render mode | **Static export (`output: "export"`)** for all pages, with build-time data ingestion. ISR off, SSR off. | Site is read-mostly research collateral that updates on git push (matches WEBSITE SYNC PROTOCOL). Static export keeps Vercel cost ~$0 and lets the LaTeX/research repo continue to drive content via commits. SSR adds a runtime that buys nothing here. |
| Data origin | **Build-time from in-repo files.** Markdown (SSOT, articles, glossary), CSV/TXT (MCMC chains, convergence summaries), JSON (papers/predictions/surveys typed data files), PNG (figures). | Already how the static site works; matches Houston's "minimum churn on the research workflow" constraint. SSOT stays the source of truth — the site reads it, never writes it. |
| MCMC chain handling | **Pre-process at build time** via `scripts/prep_chains.ts` into per-dataset JSON shards under `site/public/chains/<dataset>/<chain>.json` (downsampled to ~1k rows for table view) plus `summary.json` with full statistics from `chain_means_latest.csv` + `convergence_latest.csv`. Full chains stay in `reproducibility/cosmology/...` for the paper-side pipeline. | Raw chain `.txt` files are 50k–200k rows × 47 cols. Embedding all 15 datasets verbatim ships >100MB. Pre-processed shards keep payload ≤5MB. |
| Tailwind | **v4** (already installed via `@tailwindcss/postcss`). Use the `@import "tailwindcss"` entry. | v4 is the breaking-change generation; mixing with v3.4 docs is a footgun. The scaffold already ports `--bg`, `--text`, etc. as plain CSS vars under `:root` — this remains the design-token strategy. Tailwind utility classes layer on top. |
| shadcn/ui | **Yes, install on top of Tailwind v4 with `npx shadcn@latest init`**, only the components in §5. New York style, neutral base color. | Houston explicitly asked for shadcn. Without it the existing scaffold is a hand-rolled component library that won't scale to 30 pages of consistent UI. |
| Dossier (`research/project_master_dossier/index.html`) | **Render at `/dossier` from the 12 source markdown files** (`00_master_index.md` … `11_*.md`) using `next-mdx-remote`. The legacy `index.html` becomes a redirect. | The dossier markdown is the canonical source; the HTML is a one-time export. Reading the markdown means it stays in sync with the rest of the SSOT/dossier without a separate publish step. |
| Convex | **Defer to v2.** The existing `convex/` directory has 8 functions but the live site only loads `convex@1.34.0` from CDN as a script tag and does not call Convex from any page render path. | v1 ships from the static repo with no live data; nothing breaks. The autonomous loop already pushes commits per fire, so Vercel auto-deploys on each SSOT update. Revisit only if Houston wants a sub-minute live pod monitor that survives between commits. |

## 2. Directory layout

LaTeX papers, research scripts, MCMC chains, and the dossier markdown all stay where they are. Only the rendering layer moves. The existing `site/` directory becomes the home of the Next.js app.

```
bigbounce/                                # repo root (unchanged)
├── arxiv/, research/, reproducibility/   # research artifacts — UNCHANGED
├── pipelines/, projects/, public/        # data + figures — UNCHANGED
├── project-context/SSOT/                 # canonical paper status — UNCHANGED, READ-ONLY from site
├── articles/, *.html, style.css          # legacy static site — frozen, deleted at end of stage 5
├── site/                                 # Next.js app (EXTEND, do not recreate)
│   ├── package.json                      # next 16, react 19, tailwind 4 — already pinned
│   ├── next.config.ts                    # output:"export", images.unoptimized:true — keep
│   ├── postcss.config.mjs, tsconfig.json # already configured
│   ├── components.json                   # NEW — shadcn config
│   ├── public/
│   │   ├── images/      → symlink ../public/images   # build step
│   │   ├── papers/      → symlink ../public/papers
│   │   ├── chains/      # NEW — built JSON shards, gitignored
│   │   └── og/          # NEW — generated OG images
│   ├── scripts/
│   │   ├── prep_chains.ts        # NEW — read reproducibility/cosmology/.../*.txt → JSON
│   │   ├── prep_articles.ts      # NEW — copy/parse articles/*.html → MDX
│   │   ├── prep_dossier.ts       # NEW — read research/project_master_dossier/*.md
│   │   └── prep_ssot.ts          # NEW — read project-context/SSOT/*.md → typed JSON
│   └── src/
│       ├── app/
│       │   ├── layout.tsx, page.tsx, globals.css   # extend existing
│       │   ├── papers/[slug]/page.tsx              # exists — flesh out
│       │   ├── paper/page.tsx                      # exists — papers index
│       │   ├── explained/, glossary/, timeline/    # exist — extend
│       │   ├── activity/, status/, speculations/   # exist
│       │   ├── predictions/, surveys/              # exist (with [slug])
│       │   ├── data-explorer/page.tsx              # NEW — port data-explorer.html
│       │   ├── figures/page.tsx                    # NEW — port figures.html
│       │   ├── articles/page.tsx                   # NEW — index of /articles/[slug]
│       │   ├── articles/[slug]/page.tsx            # NEW — article pages
│       │   ├── dossier/page.tsx                    # NEW — render dossier markdown
│       │   ├── visualize/page.tsx                  # NEW — port visualize.html
│       │   └── datasets/, methodology/, contributions/, sources/, team/, sitemap/
│       ├── components/
│       │   ├── ui/                # NEW — shadcn drop-zone (button, card, table, badge, dialog, …)
│       │   ├── Cards/             # exists (StatCard, Badge, DiscoveryCard) — port to shadcn primitives
│       │   ├── Feed/              # exists (FeedItem)
│       │   ├── Layout/            # NEW — Sidebar, Topbar, MobileNav extracted from layout.tsx
│       │   ├── DataExplorer/      # NEW — DatasetSidebar, ChainTable, StatsPanel, FormulaCard, NodeTree
│       │   ├── Figures/           # NEW — FigureGrid, Lightbox
│       │   └── Math/              # NEW — Equation (KaTeX server-rendered)
│       ├── data/                  # exists (papers.ts, predictions.ts, surveys.ts) — extend with glossary.ts, articles.ts, ssot.ts (generated)
│       ├── lib/                   # NEW — utils, math helpers, route map
│       └── content/               # NEW — MDX articles (or .md sourced via prep step)
└── vercel.json                            # UPDATED — see §7
```

## 3. Page-to-route mapping

Group A — **Homepage / overview** (1)
- `index.html` → `/`

Group B — **Paper-facing static** (8)
- `paper.html` → `/paper`
- `explained.html` → `/explained`
- `methodology.html` → `/methodology`
- `methodology-anomaly.html` → `/methodology/anomaly`
- `mathematics.html` → `/mathematics`
- `findings.html` → `/findings`
- `speculations.html` → `/speculations`
- `arxiv-preview.html` → `/arxiv-preview`

Group C — **Per-paper pages** (4)
- `/papers/paper-1`, `/papers/paper-2`, `/papers/paper-3`, `/papers/paper-4` (already routed as `papers/[slug]/page.tsx`)

Group D — **Data-driven** (8)
- `data-explorer.html` → `/data-explorer`
- `figures.html` → `/figures`
- `glossary.html` → `/glossary`
- `activity.html` → `/activity`
- `ssot.html` → `/ssot`
- `status.html` → `/status`
- `datasets.html` → `/datasets`
- `versions.html` → `/versions`

Group E — **Explorers** (5)
- `anomaly-explorer.html` → `/explorers/anomaly`
- `galaxy-explorer.html` → `/explorers/galaxy`
- `galaxy-zoo.html` → `/explorers/galaxy-zoo`
- `interactive-data.html` → `/explorers/interactive`
- `data-comparison.html` → `/explorers/data-comparison`

Group F — **Visual / narrative** (4)
- `visualize.html` → `/visualize`
- `timeline.html` → `/timeline`
- `animations.html` → `/animations`
- `infrastructure.html` → `/infrastructure`

Group G — **Articles** (8)
- `articles.html` → `/articles`
- `articles/*.html` → `/articles/[slug]`

Group H — **Project meta** (7)
- `projects.html`, `team.html`, `sources.html`, `contributions.html`, `review.html`, `sitemap.html`, `bigbounce-md.html`

Group I — **Dossier** (1)
- `research/project_master_dossier/index.html` → `/dossier`

Group J — **Excluded** (auth-gated, do not migrate)
- `admin.html`, `chat.html`, `gate.js`, `view-pdf.html`, `404.html`

## 4. Data layer

| Page | Current source | Next.js source | Prep step |
|---|---|---|---|
| `/data-explorer` | 15 datasets inlined as `<script>` literals; chain `.txt` files in `reproducibility/cosmology/.../chains/dneff/` | `site/public/chains/<dataset>.json` + `site/src/data/chains.ts` | `prep_chains.ts` — reads each chain `.txt`, applies the `+1 column offset` rule from `CLAUDE.md`, downsamples to 1k rows, emits `{header, rows, stats}`. Reads `chain_means_latest.csv`, `convergence_latest.csv`, `dataset_chain_map.csv`. |
| `/activity` | Inlined timeline | `site/src/data/activity.ts` (generated) | `prep_ssot.ts` — reads `project-context/SSOT/index.md`, `peer-reviews/REVISION_TRACKER.md`, recent `git log`. |
| `/ssot` | Mirrors `project-context/SSOT/*.md` | Server-render via MDX | `prep_ssot.ts` symlinks MD into `site/src/content/ssot/`. |
| `/figures` | Hand-listed `<img>` tags | `site/src/data/figures.ts` (generated) | `prep_figures.ts` — globs `public/images/*.png`, joins to `data/figures/*/meta.yml`. |
| `/glossary` | 28 entries + 13 equations inline | `site/src/data/glossary.ts` (typed) | One-time hand-extract; KaTeX for equations. |
| `/paper` and `/papers/[slug]` | `paper.html` plus PDF links | Existing `papers.ts` extended to wire to `project-context/SSOT/paper-N/status.md` | `prep_ssot.ts` extracts version, page count, KB size from each `paper-N/status.md`. |
| `/dossier` | Static HTML | MDX from 12 markdown files | `prep_dossier.ts` — copy MD into `site/src/content/dossier/`. |
| `/articles/*` | Hand-written HTML pages | MDX | `prep_articles.ts` — convert article HTML to MDX once. |
| `/explorers/*` | Inline data + JS | `site/public/data/<explorer>.json` | `prep_explorers.ts` — read `pipelines/.../r42_results/*.json`. |

**Convex assessment.** Skipped for v1.

## 5. Component library

Install via `npx shadcn@latest init` then `npx shadcn@latest add` only:

`button`, `card`, `badge`, `separator`, `tabs`, `accordion`, `dialog`, `sheet`, `table`, `tooltip`, `scroll-area`, `command`, `input`, `select`, `toggle`, `breadcrumb`, `navigation-menu`, `skeleton`, `alert`, `popover`.

That's 19 components.

**Charting:** `recharts`.
**Math:** `katex` server-side via `<Equation>`.
**Lightbox:** shadcn `dialog`.

**Design tokens.** Keep CSS variables identical to `style.css`. The existing `site/src/app/globals.css` already does this — extend, don't rewrite.

**Typography.** `next/font` with **Newsreader**, **Inter**, **JetBrains Mono**. Newsreader is the academic-feel anchor and `CLAUDE.md` calls it out.

## 6. Migration strategy

**Staged. 5 stages over ~5–7 nights.** Live `bigbounce.hubify.app` keeps serving the static HTML until the last cutover.

- **Stage 0 — Tonight (§8).** Wire shadcn into the existing scaffold; verify dev server; deploy `site/` as a Vercel preview project.
- **Stage 1 — Static foundation.** Group A + Group B + Group H (16 pages).
- **Stage 2 — Per-paper + articles.** Group C + Group G.
- **Stage 3 — Data-driven.** Group D — heaviest stage (`/data-explorer` alone is ~1500 lines).
- **Stage 4 — Explorers + visual + dossier.** Groups E, F, I.
- **Stage 5 — Cutover.** Switch Vercel project root to `/site/`, add `vercel.json` rewrites, move legacy HTML to `site/public/legacy/` for one release, delete next commit.

**No-break rule.** Production keeps serving static HTML until Stage 5.

## 7. Deploy plan

**Vercel project config (post-cutover).**

```jsonc
{
  "buildCommand": "cd site && npm install && npm run prep && npm run build",
  "outputDirectory": "site/out",
  "framework": "nextjs",
  "rewrites": [
    { "source": "/index.html", "destination": "/" },
    { "source": "/paper.html", "destination": "/paper" },
    { "source": "/explained.html", "destination": "/explained" },
    { "source": "/data-explorer.html", "destination": "/data-explorer" },
    { "source": "/figures.html", "destination": "/figures" },
    { "source": "/glossary.html", "destination": "/glossary" },
    { "source": "/activity.html", "destination": "/activity" },
    { "source": "/articles.html", "destination": "/articles" },
    { "source": "/articles/(.*).html", "destination": "/articles/$1" },
    { "source": "/timeline.html", "destination": "/timeline" },
    { "source": "/visualize.html", "destination": "/visualize" },
    { "source": "/ssot.html", "destination": "/ssot" },
    { "source": "/status.html", "destination": "/status" },
    { "source": "/datasets.html", "destination": "/datasets" },
    { "source": "/methodology.html", "destination": "/methodology" },
    { "source": "/methodology-anomaly.html", "destination": "/methodology/anomaly" },
    { "source": "/findings.html", "destination": "/findings" },
    { "source": "/galaxy-explorer.html", "destination": "/explorers/galaxy" },
    { "source": "/anomaly-explorer.html", "destination": "/explorers/anomaly" },
    { "source": "/galaxy-zoo.html", "destination": "/explorers/galaxy-zoo" },
    { "source": "/data-comparison.html", "destination": "/explorers/data-comparison" },
    { "source": "/interactive-data.html", "destination": "/explorers/interactive" },
    { "source": "/animations.html", "destination": "/animations" },
    { "source": "/infrastructure.html", "destination": "/infrastructure" },
    { "source": "/sitemap.html", "destination": "/sitemap" },
    { "source": "/team.html", "destination": "/team" },
    { "source": "/sources.html", "destination": "/sources" },
    { "source": "/contributions.html", "destination": "/contributions" },
    { "source": "/review.html", "destination": "/review" },
    { "source": "/projects.html", "destination": "/projects" },
    { "source": "/research/project_master_dossier(/.*)?", "destination": "/dossier" }
  ]
}
```

`npm run prep` runs all `scripts/prep_*.ts` in dependency order: `prep_ssot` → `prep_articles` → `prep_chains` → `prep_figures` → `prep_dossier`.

## 8. First-night executable steps

Goal: by end of tonight, `/data-explorer` and `/figures` routes still 404 (those are stage 3), but the homepage at the Vercel preview URL renders with shadcn `Button` and `Card` swapped in, typography matches the legacy site.

```bash
cd /Users/houstongolden/Desktop/CODE_2025/bigbounce/site
npm install
npm run dev   # confirm homepage renders at http://localhost:3000

# Add Newsreader font in src/app/layout.tsx alongside Inter + Plex_Mono.

# Initialize shadcn (New York, neutral)
npx shadcn@latest init

# Install v1 component set
npx shadcn@latest add button card badge separator tabs accordion \
  dialog sheet table tooltip scroll-area command input select \
  toggle breadcrumb navigation-menu skeleton alert popover

# Override shadcn tokens to consume our CSS vars (in globals.css)

# Swap one component on homepage as smoke test (Card + Button)

npm run build    # must produce site/out/

# Stand up Vercel preview project (one-time)
# Import same GitHub repo as second project "bigbounce-next-preview",
# Root Directory = "site", Build = "npm run build", Output = "out".

git add site/components.json site/src site/package.json site/package-lock.json
git commit -m "feat(site): shadcn install + Newsreader font + first card swap"
git push origin main
```

**Done means:** (a) homepage shows Newsreader serif on `<h1>`, sidebar, shadcn `Button`; (b) `npm run build` succeeds; (c) Vercel preview project URL renders the same homepage; (d) production `bigbounce.hubify.app` is untouched.

## 9. Risks

1. **Data-explorer column-offset bug.** Chain `.txt` header begins with `#`, shifts every parameter's data-row index by `+1`, AND `full_tension` has 47 cols vs others' 46. Mitigation: vendor a `chains.test.ts` asserting mean(H₀) ≈ 67.68 ± 0.5 against `chain_means_latest.csv`.
2. **Dossier MD ↔ HTML drift.** The legacy `index.html` may have hand-written sections not in MD. Mitigation: diff before deleting.
3. **SEO + redirects.** ~30 legacy URLs linked from arXiv preprint, peer reviews, Twitter. Missing a single rewrite breaks an external citation.
4. **Static export limits.** No API routes, no middleware, no on-demand revalidation. The plan assumes none.
5. **Convex script-tag.** Currently a no-op; confirm before drop.
6. **Vercel Git LFS.** `public/images/` PNGs are LFS-tracked; Vercel needs LFS enabled.
7. **Existing scaffold drift.** `site/` last touched at commit `ee6ac2b`; numbers in `site/src/data/*.ts` are 1–2 weeks behind. Mitigation: regenerate via `prep_ssot.ts` in stage 1.

## 10. Open questions for Houston

1. **Cutover guard.** Keep legacy static HTML reachable at `/legacy/*.html` for 14 days post-cutover, then delete? (Default if no answer: yes, keep 14 days.)
2. **Articles authoring.** Future articles author in MDX in `site/src/content/articles/`? (Default: yes.)
3. **Convex on `/activity`.** Skipped per §4. If you want sub-deploy-cadence live pod heartbeat, say so before stage 3.
