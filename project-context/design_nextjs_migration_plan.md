# Next.js Migration Plan — bigbounce.hubify.app

**Author:** Houston Golden / Hubify Labs
**Status:** PLANNED — do NOT execute until all 4 papers are arXiv-submitted and locked
**Target stack:** Next.js 15 (app router) + React 19 + Tailwind CSS 4 + shadcn/ui + KaTeX
**Current stack:** Static HTML (38 root `.html` files + 9 `articles/*.html`), shared `style.css`, `nav.js` JS-injected sidebar+topbar+inline nav, MathJax 3 via CDN, Vercel auto-deploy from `main`
**Trigger condition:** Houston gives explicit "go" after Paper 1, 2, 3, 4 all hit arXiv with submitted version IDs. Until then, this doc sleeps.

---

## 0. Executive summary

The current site is 38 hand-rolled HTML files sharing one `style.css` (terminal-aesthetic, monochrome, mono-typography sidebar with editorial right-pane content) and one `nav.js` that injects a sidebar + topbar + inline nav at runtime. It works, but: (a) `nav.js` runtime injection means a flash-of-no-nav before hydration, (b) every page reimplements its own `<head>` and SEO tags, (c) `data-explorer.html` is 2,942 lines of inline data + DOM-manipulating JS that should be a real component tree, (d) MathJax loads from CDN on every page and re-runs MathJax.typeset() on each, (e) the lightbox in `figures.html` is hand-rolled, (f) the visualize page uses a custom canvas simulation, (g) all the chrome (favicon, theme toggle, search) is JS-injected at runtime instead of server-rendered. Migrating to Next.js 15 + Tailwind 4 + shadcn/ui will give server-rendered HTML for SEO, real component reuse, type-safe data, and a proper home for the data-explorer interactivity. The migration is sized at 3-5 days solo, ~1-2 days with parallel sub-agents, and should ship in the order: scaffold → nav/layout/theme → home → papers → explainer → figures → glossary → activity → articles → data-explorer (last, hardest) → cutover.

This doc covers: routing tree (A), shadcn component map (B), Tailwind 4 theme matching the current monochrome academic aesthetic via CSS-variable bridge so existing styles keep working during the migration (C), MathJax→KaTeX swap with explicit fallbacks for `align` + macros (D), data-layer decision matrix (E), Vercel deploy mechanics (F), an 11-step incremental migration sequence with no big-bang cutover (G), and a risk register that pins down PDF deep-links, SEO, and design-quality benchmarking against k-dense.ai / feynman.is (H).

---

## A. Routing structure (Next.js 15 app router)

Next.js 15 app router maps `app/<segment>/page.tsx` → `/<segment>`. Below is the canonical mapping from the current 38-file static surface to the target route tree. Pages are ordered by visit volume / value, not alphabetically.

```
app/
├── layout.tsx                          # Root shell: <html>, <body>, fonts, ThemeProvider, Sidebar, Topbar, InlineNav
├── page.tsx                            # /                          ← index.html (homepage)
├── not-found.tsx                       # /404                       ← 404.html
├── globals.css                         # Tailwind 4 + CSS-var bridge (see §C)
│
├── papers/
│   ├── page.tsx                        # /papers                    ← paper.html (4-paper listing)
│   └── [slug]/
│       └── page.tsx                    # /papers/paper1 … paper4    ← per-paper landing (NEW — split paper.html anchors into pages)
│
├── explained/
│   └── page.tsx                        # /explained                 ← explained.html
│
├── data/
│   └── page.tsx                        # /data                      ← data-explorer.html
│       (split into client subcomponents under app/data/_components/)
│
├── figures/
│   └── page.tsx                        # /figures                   ← figures.html
│
├── glossary/
│   └── page.tsx                        # /glossary                  ← glossary.html (search + 13 equations + 28 entries)
│
├── activity/
│   └── page.tsx                        # /activity                  ← activity.html (status banner + queue + timeline)
│
├── timeline/
│   └── page.tsx                        # /timeline                  ← timeline.html (cosmic timeline visual)
│
├── visualize/
│   └── page.tsx                        # /visualize                 ← visualize.html (dark-mode canvas simulation)
│
├── datasets/
│   └── page.tsx                        # /datasets                  ← datasets.html
│
├── articles/
│   ├── page.tsx                        # /articles                  ← articles.html (index)
│   └── [slug]/
│       └── page.tsx                    # /articles/<slug>           ← articles/*.html (9 articles)
│       (slugs: ech-bounce-phenomenology, evolution-of-rigor, look-up,
│               matter-bounce-blueprint, program-visual-guide,
│               publication-roadmap, students-guide-big-bounce,
│               technical-evaluation, the-window)
│
├── galaxy-explorer/
│   └── page.tsx                        # /galaxy-explorer           ← galaxy-explorer.html (Paper 4 explorer)
│
├── anomaly-explorer/
│   └── page.tsx                        # /anomaly-explorer          ← anomaly-explorer.html (Paper 3 explorer)
│
├── methodology/
│   └── page.tsx                        # /methodology               ← methodology.html
├── methodology-anomaly/
│   └── page.tsx                        # /methodology-anomaly       ← methodology-anomaly.html
├── mathematics/
│   └── page.tsx                        # /mathematics               ← mathematics.html
├── sources/
│   └── page.tsx                        # /sources                   ← sources.html
├── findings/
│   └── page.tsx                        # /findings                  ← findings.html
├── contributions/
│   └── page.tsx                        # /contributions             ← contributions.html (key findings)
├── projects/
│   └── page.tsx                        # /projects                  ← projects.html
├── speculations/
│   └── page.tsx                        # /speculations              ← speculations.html
├── infrastructure/
│   └── page.tsx                        # /infrastructure            ← infrastructure.html
├── versions/
│   └── page.tsx                        # /versions                  ← versions.html
├── status/
│   └── page.tsx                        # /status                    ← status.html
├── ssot/
│   └── page.tsx                        # /ssot                      ← ssot.html
├── animations/
│   └── page.tsx                        # /animations                ← animations.html
├── interactive-data/
│   └── page.tsx                        # /interactive-data          ← interactive-data.html
├── data-comparison/
│   └── page.tsx                        # /data-comparison           ← data-comparison.html
├── galaxy-zoo/
│   └── page.tsx                        # /galaxy-zoo                ← galaxy-zoo.html
├── review/
│   └── page.tsx                        # /review                    ← review.html
├── team/
│   └── page.tsx                        # /team                      ← team.html
├── arxiv-preview/
│   └── page.tsx                        # /arxiv-preview             ← arxiv-preview.html
├── bigbounce-md/
│   └── page.tsx                        # /bigbounce-md              ← bigbounce-md.html
├── view-pdf/
│   └── page.tsx                        # /view-pdf                  ← view-pdf.html (PDF viewer wrapper)
├── sitemap/
│   └── page.tsx                        # /sitemap                   ← sitemap.html (HTML sitemap; in addition to Next's auto sitemap.xml)
│
├── research/
│   └── dossier/
│       └── page.tsx                    # /research/dossier          ← research/project_master_dossier/index.html
│       (the 12 markdown files in research/project_master_dossier/ become a sub-tree
│        of MDX pages under app/research/dossier/[slug]/page.mdx if we want them browsable;
│        otherwise import + render at the dossier index)
│
├── admin/
│   ├── page.tsx                        # /admin                     ← admin.html (gated; investigate keep vs drop)
│   └── chat/
│       └── page.tsx                    # /admin/chat                ← chat.html (currently top-level; move under /admin since it's gated)
│
├── api/
│   ├── chains/[name]/route.ts          # /api/chains/dneff_baseline … (see §E for data layer)
│   └── search/route.ts                 # /api/search                ← replaces nav.js search.js (server-side fuzzy)
│
├── sitemap.ts                          # Next 15 auto-sitemap.xml generator
├── robots.ts                           # Next 15 robots.txt generator
└── opengraph-image.tsx                 # Default OG image generator
```

### Notes on routing decisions

- **Per-paper landing pages** (`/papers/paper1`-`paper4`): the current `paper.html` uses `#paper1`/`#paper2`/etc anchors to scroll to inline sections of one giant page. In Next we split each paper into its own route. The shell `paper.html` remains as `/papers` (the listing). This makes per-paper sharing, OG metadata, and arXiv inbound links cleaner.
- **`view-pdf.html` as `/view-pdf`**: keep as a route that takes `?pdf=…` and renders an iframe. The 4 PDFs in `public/papers/*.pdf` stay at the same URLs, so existing arXiv inbound deep links don't break (see §H).
- **`/admin/chat`**: `chat.html` and `admin.html` exist at root today; move chat under admin since it's the only consumer and is gated. If `chat.html` has external inbound links, add a redirect (see §H).
- **`research/project_master_dossier/index.html`**: currently a separate site nested under `research/`. Migrate it to `app/research/dossier/page.tsx` and lift its 12 markdown supporting files into MDX so they're browsable; OR simply pre-render the existing dossier dashboard as a single page (decide at scaffold time based on whether the 12 markdown files have unique inbound links).
- **API routes**: only added where a current static page uses inline JS to fake an API (data-explorer, search). Everything else stays SSG/RSC.

---

## B. Component map (shadcn/ui)

shadcn/ui is the only third-party UI library we install — and we install it via the shadcn CLI which copies components into `components/ui/`, so we own the source. Each row below names the current pattern, its current implementation in `style.css`, and the shadcn primitive that replaces it.

| Current pattern                                         | Where in current site                                    | shadcn/ui replacement                                            | Notes                                                                                                          |
| ------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Stat cards** (homepage Key Discoveries grid)          | `index.html` `.stat`, `.stat-value`, `.stat-label`       | `Card` + `Badge` (compose; no built-in `Stat`)                   | Wrap `Card` with `text-center`. Keep mono font for value via Tailwind class.                                   |
| **Paper cards** (4 papers on home + on `/papers`)       | `index.html` `.card[style="border-left: 4px solid …"]`   | `Card` with custom `border-l-4` Tailwind utility                 | The colored left-border per paper (`#1e40af`, `#16a34a`, `#f97316`, `#a855f7`) becomes a per-paper accent var. |
| **Version history timeline** (`/papers`)                | `paper.html` `.timeline`, `.timeline-item`               | **Custom Timeline component** (no shadcn primitive)              | Build under `components/timeline.tsx`. Use Tailwind for the dot + line. Keep the existing CSS DNA.             |
| **Sidebar (left, dark, CLI-tree)**                      | `style.css` `.sidebar`, `.sidebar-section`               | Custom `Sidebar` component, optionally on top of shadcn `Sidebar` (newer shadcn ships one) | The current sidebar has bespoke `~/` and `>` glyphs. Keep that aesthetic; don't accept shadcn defaults.        |
| **Topbar** (thin metadata strip)                        | `style.css` `.topbar`                                    | Plain server component                                           | No interactivity. Render in `layout.tsx`.                                                                      |
| **Inline nav (mobile-hamburger)**                       | `nav.js` `.nav-toggle` + `.nav-links`                    | `Sheet` (off-canvas drawer)                                      | Replaces hand-rolled mobile menu. `Sheet` uses Radix Dialog + accessible focus trap.                           |
| **Mobile sidebar drawer**                               | `style.css` `.sidebar.open` (transform-based)            | `Sheet` with `side="left"`                                       | Same component as above; just two Sheet instances (one for sidebar, one for inline nav) on mobile.             |
| **Search palette**                                      | `nav.js` loads `search.js` at runtime                    | `Command` (cmdk wrapper) + `Dialog`                              | Trigger via Cmd+K. Index built at build time from MDX frontmatter + page metadata.                             |
| **MCMC table** (`/data`)                                | `data-explorer.html` raw `<table>` + custom JS sort      | `Table` + Tanstack Table (`@tanstack/react-table`)               | shadcn ships a DataTable recipe wrapping Tanstack. Get sortable headers, virtualization for long chains.       |
| **Claims table** (sortable on home + papers)            | `index.html` plain `<table>`                             | `Table` + Tanstack Table                                         | Same recipe, smaller dataset.                                                                                  |
| **Lightbox** (`/figures`)                               | `figures.html` `#lightbox` div + custom JS               | `Dialog` from shadcn + `yet-another-react-lightbox`              | shadcn `Dialog` for the shell; YARL for the keyboard nav + zoom. Don't reinvent.                               |
| **Searchable glossary** (`/glossary`)                   | `glossary.html` `<input>` + custom filter JS             | `Command` (full-screen search) + `Accordion` for entries         | 28 glossary entries + 13 equations. Command palette gives keyboard-first access; accordion for full term page. |
| **Equation calculators** (6, on `/data`)                | `data-explorer.html` inline `<input>` + JS              | `Form` + `Input` + `react-hook-form` + `zod`                     | Standard shadcn form pattern. KaTeX for the rendered output.                                                   |
| **Activity status banner** (`/activity`)                | `activity.html` colored banner + pill                    | `Alert` + `Badge`                                                | Status banner is 1-line; map cleanly.                                                                          |
| **Activity timeline feed**                              | `activity.html` timeline list                            | Reuse custom `Timeline` component from §B row 3                  | Same component, different data.                                                                                |
| **Priority queue** (`/activity`)                        | `activity.html` ordered list of cards                    | `Card` + `Badge` for status pill                                 | No new primitive needed.                                                                                       |
| **Cosmic timeline** (`/timeline`)                       | `timeline.html` SVG/HTML hand-rolled                     | Keep custom; no shadcn primitive                                 | Visual one-off. Convert SVG to a component but don't try to shadcn-ify.                                        |
| **Cosmic simulation** (`/visualize`)                    | `visualize.html` `<canvas>` + 1,743 lines of vanilla JS  | Keep canvas; wrap in client component (`"use client"`)           | Keep the canvas logic verbatim; only the wrapper changes. Hydration-safe via `useEffect`.                      |
| **Theme toggle**                                        | `nav.js` `.theme-toggle`                                 | `next-themes` library + custom toggle button                     | `next-themes` handles SSR + flash-of-wrong-theme. Use `useTheme()` in the toggle.                               |
| **Math rendering**                                      | MathJax 3 via CDN, `<script async>` per page             | `react-katex` + KaTeX CSS imported once in `layout.tsx`          | See §D.                                                                                                        |
| **Code blocks** (rare; in articles)                     | Plain `<pre><code>`                                      | `shiki` (build-time syntax highlight, RSC-safe) or plain `<pre>` | Tiny usage — start with plain `<pre>` and add shiki only if articles need it.                                  |
| **MDX articles**                                        | 9 hand-coded `articles/*.html`                           | `next-mdx-remote` or `@next/mdx`                                 | Authoring future articles in MDX is the win; existing 9 articles get migrated to MDX once.                     |
| **PDF viewer** (`/view-pdf`)                            | `view-pdf.html` `<iframe>`                               | Plain iframe in a server component                               | No JS needed; route param drives the `src`.                                                                    |
| **Buttons**                                             | `style.css` `.btn`, `.btn-primary`, `.btn-secondary`     | `Button` with `variant="default"` / `variant="outline"`          | Map: `.btn-primary` → `default`, `.btn-secondary` → `outline`. Keep mono font globally.                        |

### Components we install via shadcn CLI

```bash
npx shadcn@latest add button card badge dialog sheet table command alert accordion form input label tabs separator scroll-area sidebar
```

### Components we build by hand

- `components/timeline.tsx` (version history + activity feed)
- `components/sidebar-cli.tsx` (the CLI-tree sidebar with `~/` + `>` glyphs)
- `components/topbar.tsx`
- `components/inline-nav.tsx`
- `components/equation.tsx` (KaTeX wrapper, see §D)
- `components/data-explorer/*` (the data-explorer split into ~8 client subcomponents — see §E)
- `components/cosmic-canvas.tsx` (wraps the existing visualize canvas code)

---

## C. Tailwind 4 theme — matching the current academic aesthetic

The current site is monochrome (#0a0a0a text on #ffffff bg, no color accents except 4 paper-card border colors and the sage-green status indicator). Fonts are Inter (sans) + IBM Plex Mono (mono). Critically, the current `style.css` defines a custom-property API (`--bg`, `--text`, `--border`, etc) that the entire codebase consumes. The Next.js port preserves that API as a CSS-variable bridge so all the existing Tailwind utility classes AND any inline styles in old pages keep working through the migration.

### Strategy: bridge, don't rewrite

1. Tailwind 4 supports CSS-first config via `@theme` directive in `globals.css`.
2. Define our colors and fonts as CSS variables on `:root` and `[data-theme="dark"]`, identical names to today.
3. Use Tailwind 4's `@theme` to alias the variables into design tokens (so `bg-background`, `text-foreground`, etc just work).
4. shadcn/ui consumes `--background`, `--foreground`, `--border`, `--ring` — alias these to our existing names.

### `app/globals.css`

```css
@import "tailwindcss";
@import "katex/dist/katex.min.css";

/* ──────────────────────────────────────
   Design tokens (light)
   These names match today's style.css so
   inline styles in legacy components keep
   working during the migration.
   ────────────────────────────────────── */
:root {
  --bg: #ffffff;
  --bg-subtle: #fafafa;
  --bg-code: #f6f6f6;
  --bg-sidebar: #1a1a1a;
  --bg-raised: #ffffff;
  --border: #eaeaea;
  --border-strong: #d4d4d4;
  --text: #0a0a0a;
  --text-secondary: #444444;
  --text-tertiary: #666666;
  --text-muted: #999999;
  --accent-link: #0a0a0a;
  --accent-link-hover: #000000;
  --accent-sage: #9caf88;          /* status indicator only — be sparing */

  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'IBM Plex Mono', 'JetBrains Mono', ui-monospace, monospace;
  --font-serif: 'Newsreader', Georgia, serif;  /* used in long-form articles */

  --radius: 0px;
  --sidebar-w: 240px;
  --topbar-h: 36px;
  --transition: 100ms ease;

  /* shadcn aliases — keep shadcn happy without forking it */
  --background: var(--bg);
  --foreground: var(--text);
  --card: var(--bg);
  --card-foreground: var(--text);
  --popover: var(--bg);
  --popover-foreground: var(--text);
  --primary: var(--text);
  --primary-foreground: var(--bg);
  --secondary: var(--bg-subtle);
  --secondary-foreground: var(--text-secondary);
  --muted: var(--bg-subtle);
  --muted-foreground: var(--text-muted);
  --accent: var(--bg-subtle);
  --accent-foreground: var(--text);
  --destructive: #b91c1c;
  --destructive-foreground: #ffffff;
  --input: var(--border);
  --ring: var(--text);
}

[data-theme="dark"] {
  --bg: #0a0a0a;
  --bg-subtle: #111111;
  --bg-code: #161616;
  --bg-sidebar: #050505;
  --bg-raised: #1a1a1a;
  --border: #2a2a2a;
  --border-strong: #3a3a3a;
  --text: #e5e5e5;
  --text-secondary: #a3a3a3;
  --text-tertiary: #737373;
  --text-muted: #666666;
  --accent-link: #60a5fa;
  --accent-link-hover: #93c5fd;
}

/* ──────────────────────────────────────
   Tailwind 4 @theme — alias CSS vars into
   Tailwind's design token system so utility
   classes like bg-background / text-foreground
   resolve to our vars.
   ────────────────────────────────────── */
@theme {
  --color-background: var(--bg);
  --color-foreground: var(--text);
  --color-muted: var(--bg-subtle);
  --color-muted-foreground: var(--text-muted);
  --color-border: var(--border);
  --color-card: var(--bg);
  --color-card-foreground: var(--text);
  --color-primary: var(--text);
  --color-primary-foreground: var(--bg);
  --color-secondary: var(--bg-subtle);
  --color-secondary-foreground: var(--text-secondary);
  --color-accent: var(--accent-sage);
  --color-destructive: #b91c1c;
  --color-ring: var(--text);

  --font-sans: var(--font-sans);
  --font-mono: var(--font-mono);
  --font-serif: var(--font-serif);

  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;       /* the current site is squared corners; keep it */

  --breakpoint-sm: 480px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 900px;
  --breakpoint-xl: 1200px;
}

/* ──────────────────────────────────────
   Body defaults — match style.css line 36
   ────────────────────────────────────── */
body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ──────────────────────────────────────
   Legacy class compat shim — included
   ONLY during the migration. Once every
   page is ported, delete this block.
   These selectors copy the rules from
   style.css verbatim so a page that still
   references .card / .badge / .stat / .timeline
   renders identically. Each class also has
   a Tailwind equivalent we use in new code.
   ────────────────────────────────────── */
.card           { background: var(--bg); border: 1px solid var(--border); padding: 20px 22px; transition: border-color var(--transition); }
.card:hover     { border-color: var(--border-strong); }
.card-accent    { border-left: 2px solid var(--text); }

.badge          { display: inline-flex; align-items: center; gap: 4px; padding: 1px 6px; font-size: 11px; font-weight: 500; font-family: var(--font-mono); border: 1px solid var(--border); color: var(--text-tertiary); background: var(--bg); }
.badge-success  { color: #166534; border-color: #bbf7d0; background: #f0fdf4; }

.stat           { text-align: center; padding: 16px 12px; }
.stat-value     { font-size: 1.5rem; font-weight: 600; color: var(--text); font-family: var(--font-mono); }
.stat-label     { font-size: 10px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 6px; font-family: var(--font-mono); }

/* …timeline, hero, equation-display, etc — copy verbatim from style.css …
   When a page is ported to shadcn, drop the legacy class from its JSX. */
```

### Tailwind config (`tailwind.config.ts`)

In Tailwind 4 most config lives in `globals.css` (as above). The TS file is minimal:

```ts
import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class", "[data-theme='dark']"],
  content: [
    "./app/**/*.{ts,tsx,mdx}",
    "./components/**/*.{ts,tsx}",
    "./content/**/*.{md,mdx}",
  ],
  theme: { extend: {} },          // empty — see @theme in globals.css
  plugins: [require("@tailwindcss/typography")],
};

export default config;
```

### Migration path for color tokens

Phase 1 (during migration): keep `--bg` / `--text` / `--border` exactly as named today. Both legacy pages and new shadcn-aliased Tailwind classes resolve them.
Phase 2 (after migration): we're free to migrate to OKLCH per Tailwind 4 best practice (`oklch(0.99 0 0)` etc), since the bridge layer is the only consumer. Don't do this in the same sprint as the Next migration — separate, low-risk follow-up.

### Mobile breakpoints

Current `style.css` uses `@media (max-width: 900px)` and `@media (max-width: 480px)`. Map them to Tailwind 4 named breakpoints (set in `@theme` above): `lg: 900px` and `sm: 480px`. New code uses `lg:hidden` etc; legacy media queries in the compat shim keep working.

---

## D. Math rendering migration — MathJax 3 → KaTeX

### Why swap

| Property                                  | MathJax 3                                                | KaTeX                                                       |
| ----------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------- |
| SSR-safe?                                 | No (DOM-only, runs after parse)                          | Yes (renders to HTML string at build time or RSC)           |
| Bundle size                               | ~1.2 MB script, loaded async                             | ~280 KB (CSS + fonts), tree-shakeable subset import         |
| Render speed                              | 100-500 ms typeset per page on first paint               | <10 ms per equation, server-rendered                        |
| Coverage                                  | Full LaTeX + AMS + custom macros + auto-cite             | LaTeX subset (extensive) + AMS via `\usepackage{amsmath}`-equivalent macros        |
| `align` / `gather`                        | Yes                                                      | Yes (via `aligned`, `gathered` envs — see edge cases below) |
| Custom macros (`\newcommand`)             | Yes, full TeX engine                                     | Yes via `macros: { ... }` config                            |
| Inline auto-discovery (`\(`, `\[`)        | Yes via `tex2jax` config                                 | Yes via `rehype-katex` (in MDX) or manual `<InlineMath />`  |

KaTeX has covered every formula on this site that I sampled (the f_NL paper notation, ECH connection algebra, MCMC posteriors). The known weak spots — and our fallbacks — are below.

### Implementation

```tsx
// components/equation.tsx
"use client";
import { InlineMath, BlockMath } from "react-katex";

const MACROS = {
  // Paper-specific macros that appear across the site
  "\\fnl": "f_{\\rm NL}",
  "\\Mpl": "M_{\\rm Pl}",
  "\\Neff": "N_{\\rm eff}",
  "\\bphi": "b_\\phi",
  "\\sigfnl": "\\sigma(f_{\\rm NL})",
};

export function Eq({ children, block = false }: { children: string; block?: boolean }) {
  const Component = block ? BlockMath : InlineMath;
  return <Component math={children} settings={{ macros: MACROS, throwOnError: false, strict: "ignore" }} />;
}
```

Usage:

```tsx
<p>The decisive prediction is <Eq>{`\\fnl = -35/8 = -4.375`}</Eq>.</p>

<Eq block>{`
  \\beta = \\frac{1}{2} g_{\\phi\\gamma} \\, \\dot{\\phi}_0 \\, \\Delta t
`}</Eq>
```

Imported once in `app/layout.tsx`:

```tsx
import "katex/dist/katex.min.css";
```

### Edge cases — formulas that need attention during migration

Going page-by-page during the figure / equation port, watch for:

1. **`\begin{align}` with `\tag` for paper-style equation numbers.** KaTeX `align` lives inside `\begin{aligned}` — it does NOT auto-number. If the current site uses `\tag{1}` for visible equation labels, replace with a wrapping component:
   ```tsx
   <div className="flex items-center gap-4">
     <BlockMath math={tex} />
     <span className="font-mono text-sm text-muted-foreground">(1)</span>
   </div>
   ```
2. **`\require{cancel}` or other MathJax extensions.** Map common ones to KaTeX equivalents; for `\cancel` install `@matejmazur/react-katex-cancel` or replace with plain `\overline{\cdot}`-style notation.
3. **Custom MathJax macros defined inline** (`\newcommand` blocks at the top of a page). Lift them into `MACROS` in `components/equation.tsx`. Audit the 4 paper LaTeX sources (`arxiv/main.tex`, `pipelines/p2_chirality/chirality_catalog_paper.tex`, `pipelines/p3_anomaly_engine/paper3_draft.tex`, `research/focused_paper_source_integration/02_full_draft.tex`) for `\newcommand` and `\def` lines; copy them all into `MACROS` once.
4. **`\eqref{...}` cross-references.** KaTeX doesn't support `\eqref` for cross-doc references — but neither did MathJax meaningfully on this site. Replace with explicit hyperlinks: `[Eq. (3)](/explained#eq3)`.
5. **`mhchem` or other AMS extensions.** Currently unused on this site; flag if they ever appear.

### Glossary equation gallery (`/glossary` — 13 equations)

The current glossary lists 13 equations as static MathJax displays. In the port:

```tsx
const equations = [
  { id: "eq-fnl", label: "Non-Gaussianity (matter bounce)", tex: "\\fnl = -\\frac{35}{8}", paper: "Paper 2 §III" },
  { id: "eq-beta", label: "Birefringence rotation angle",   tex: "\\beta = \\frac{1}{2} g_{\\phi\\gamma} \\dot{\\phi}_0 \\Delta t", paper: "Paper 1 §VI" },
  // … 11 more
];

export default function Glossary() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      {equations.map((e) => (
        <Card key={e.id} id={e.id} className="border-l-2 border-l-foreground">
          <CardHeader><CardTitle>{e.label}</CardTitle></CardHeader>
          <CardContent>
            <Eq block>{e.tex}</Eq>
            <p className="text-xs text-muted-foreground mt-2 font-mono">{e.paper}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
```

### Quality gate

After every page port, run a side-by-side screenshot diff (current site vs. localhost Next.js) at three breakpoints (480, 900, 1200) for any page that contains math. Use `/qa` skill — Houston already mandates a mobile sweep post-migration.

---

## E. Data layer — 15 datasets in `data-explorer.html`

Today: `data-explorer.html` is 2,942 lines. Each MCMC chain / summary CSV / parameter JSON is embedded as inline `<script>const DATA_xyz = [...]</script>` blocks. Total uncompressed payload is ~2.3 MB; the page is slow to parse.

### Decision matrix

| Option | Hydration cost | First-load size | Update story | Interactivity | Verdict |
|---|---|---|---|---|---|
| **(1) Static `/data/*.json` + RSC fetch** | Low (server reads JSON, sends pre-computed HTML for the table; client hydrates only sort handlers) | Small (only the visible table rows ship as HTML; full JSON only loaded when user opens the dataset) | Drop a JSON in `public/data/`; SSG rebuild on next deploy | Tanstack Table client-side sort once dataset is loaded | **Recommended for the 5 large chain files** (each 3-15 MB). |
| **(2) TypeScript constants** (`const dneffBaseline = [...]`) imported into the route | Medium (Next inlines into the JS bundle; tree-shaken if route doesn't import) | Big bundle if multiple datasets live in one route | Code-controlled (great for typecheck and migration) | Same | **Recommended for the 8 small summary CSVs** (`convergence_latest.csv`, parameter JSONs <100 KB). |
| **(3) Dynamic API route** (`/api/chains/[name]`) | Lowest first paint (route ships zero data) | Tiny (data fetched on click/scroll) | Edge-cached on Vercel | Loading spinner until fetch | **Recommended for the 2 mega-chains** (full posterior 4 datasets × 6-7 chains × 309K samples = the full_tension chain). Stream subsets on demand. |

### Final layout

```
app/data/
├── page.tsx                    # /data — RSC: lists 15 datasets as cards; selecting one loads via Option 1 or 3
├── _components/
│   ├── dataset-table.tsx       # client component: Tanstack Table + sort + column stats
│   ├── chain-loader.tsx        # client component: progressive load via /api/chains/[name]
│   ├── column-stats.tsx        # client component: mean/median/std/95% CI for selected column
│   └── equation-calculator.tsx # client component: 6 equation calcs with KaTeX-rendered output
public/data/
├── convergence_latest.json     # small — Option 1
├── chain_means_latest.json     # small — Option 1
├── dataset_chain_map.json      # small — Option 1
├── full_tension_physical_parameters.json  # ~50 KB — Option 1
├── galaxy_spin_counts.json     # small — Option 1
└── chains/
    ├── dneff_baseline.json     # ~3 MB — Option 1 (lazy load on click)
    ├── dneff_full.json         # ~5 MB — Option 1 (lazy load)
    └── full_tension/           # huge — Option 3 (API streams chunks)
        ├── manifest.json
        ├── chunk_0001.json     # 10K samples per chunk
        └── …
app/api/chains/[name]/route.ts  # streams chunks; ?offset=N&limit=M
```

### Source-of-truth conversion

The existing `reproducibility/cosmology/.../spin_torsion.1.txt` files are space-delimited. A one-time `scripts/convert-chains.ts` reads them, applies the column-offset rule from CLAUDE.md (`#` shifts header indices by +1), and emits typed JSON to `public/data/chains/`. Run once, check in.

```ts
// scripts/convert-chains.ts (sketch)
import fs from "node:fs";
const txt = fs.readFileSync(src, "utf-8");
const lines = txt.split("\n");
const headerLine = lines.find((l) => l.startsWith("#"))!;
const headers = headerLine.replace(/^#\s*/, "").split(/\s+/);
const rows = lines
  .filter((l) => l && !l.startsWith("#"))
  .map((l) => l.trim().split(/\s+/).map(Number));
const json = rows.map((r) => Object.fromEntries(headers.map((h, i) => [h, r[i]])));
fs.writeFileSync(dest, JSON.stringify(json));
```

### Equation calculators (6, currently inline in `data-explorer.html`)

Convert each to a `Form` + `Input` component with `react-hook-form` + `zod` validation. Render the result with `<Eq block>...</Eq>`. Cleaner pattern, type-safe, accessible.

---

## F. Deployment

The DNS, the project, and the auto-deploy pipeline are already pointed at Vercel. The migration is invisible to DNS.

| Concern | Today | After migration |
|---|---|---|
| **Repo trigger** | Push to `main` deploys static HTML | Push to `main` deploys Next.js build (Vercel auto-detects `next.config.ts`) |
| **Build cmd** | (none — static) | `next build` (auto-set by Vercel) |
| **Output** | Static files served at root | Static + RSC + serverless functions for API routes |
| **`public/`** | Served as static assets at `/public/...` | Same: `public/papers/*.pdf`, `public/images/*.png`, `public/spreadsheets/*.xlsx` resolve identically |
| **Domain** | `bigbounce.hubify.app` | unchanged |
| **TTFB** | ~50ms (static HTML) | ~80ms (RSC) — acceptable; KaTeX SSR + smaller HTML body offsets it |
| **Edge runtime** | n/a | Use `export const runtime = "edge"` on `/api/chains/*` for low-latency dataset chunks |
| **ISR** | n/a | Useful for `/activity` (revalidate every 5 min from a JSON manifest) |
| **Sitemap** | hand-written `sitemap.html` | `app/sitemap.ts` autogenerates `sitemap.xml` |

### Cutover step (single PR)

1. Open `nextjs-site/` PR off `main`.
2. Verify a Vercel preview build at `<branch>.vercel.app`.
3. Side-by-side QA every page (use `/qa-only` skill at 480/900/1200 breakpoints).
4. Move root `index.html` → `static-archive/index.html` etc. Move every `*.html` to `static-archive/`.
5. In `next.config.ts` add `redirects()` for any URL that changed (see §H.1).
6. Merge PR — Vercel builds the Next app on push.
7. If anything breaks, `git revert` and re-deploy: takes 60 seconds since the static HTML is intact in `static-archive/`.

---

## G. Incremental migration path (no big-bang)

11 steps, ordered by shipping value. Each step ships in its own PR — no step blocks any other. The site stays on the current static HTML the entire time, with the Next app under `nextjs-site/` previewable at `nextjs-site.bigbounce.hubify.app` (Vercel branch deploys handle this automatically). Final cutover is step 11.

| # | Step | Files touched | Time (solo) | Time (parallel agents) | Blockers |
|---|---|---|---|---|---|
| 1 | **Scaffold** Next 15 + Tailwind 4 + shadcn/ui in `nextjs-site/` subdir; copy `public/` over; seed `app/layout.tsx` with empty shell. | `nextjs-site/{package.json, tsconfig.json, app/, components/, public/}` | 2 hr | 2 hr (serial) | none |
| 2 | **Port nav + topbar + sidebar + theme toggle.** Build `Sidebar`, `Topbar`, `InlineNav`, `ThemeToggle` in `components/`. Wire `next-themes`. Reproduce the CLI tree exactly. | `components/sidebar-cli.tsx`, `components/topbar.tsx`, `components/inline-nav.tsx`, `app/layout.tsx` | 4 hr | 4 hr (serial — foundational) | step 1 |
| 3 | **Port homepage** (`/`) — highest visit volume, sets the visual bar. Includes hero, 4-paper grid, story-in-60s, key discoveries stat grid, MCMC table (read-only), claims table (sortable). | `app/page.tsx`, `components/paper-card.tsx`, `components/stat-card.tsx`, `components/claims-table.tsx` | 4 hr | 2 hr | step 2 |
| 4 | **Port `/papers`** — listing + 4 sub-routes (`/papers/paper1`–`paper4`) with KaTeX equation rendering. | `app/papers/page.tsx`, `app/papers/[slug]/page.tsx`, `components/version-timeline.tsx` | 4 hr | 2 hr | step 2 (uses layout) |
| 5 | **Port `/explained`** — long-form non-technical article. Quickest port: copy text into MDX with `<Eq>` swaps for math. | `app/explained/page.tsx` (or `content/explained.mdx`) | 2 hr | 1 hr | step 2 |
| 6 | **Port `/figures`** — gallery of 22 images with shadcn `Dialog` + `yet-another-react-lightbox`. | `app/figures/page.tsx`, `components/figure-gallery.tsx` | 3 hr | 2 hr | step 2 |
| 7 | **Port `/glossary`** — 13 equation cards + 28 entries + Cmd+K search via shadcn `Command`. | `app/glossary/page.tsx`, `components/glossary-search.tsx`, `content/glossary.ts` | 3 hr | 2 hr | step 2 |
| 8 | **Port `/activity`** — status banner + queue + timeline feed. Wire ISR (revalidate=300) so the cron-driven activity log freshens without rebuild. | `app/activity/page.tsx`, `components/activity-timeline.tsx` | 3 hr | 2 hr | step 2 |
| 9 | **Port `/articles`** + 9 article subpages — convert each to MDX. | `app/articles/page.tsx`, `app/articles/[slug]/page.tsx`, `content/articles/*.mdx` | 6 hr | 3 hr (parallel agent per article) | step 2 |
| 10 | **Port `/data`** (HARDEST — leave for last). Convert 15 datasets per §E. Implement Tanstack DataTable, column stats, 6 equation calculators, dataset selector. | `app/data/page.tsx`, `app/data/_components/*`, `app/api/chains/[name]/route.ts`, `public/data/*.json`, `scripts/convert-chains.ts` | 12 hr | 6 hr | steps 2 + 7 (KaTeX) |
| 10a | **Port `/timeline`, `/visualize`, `/galaxy-explorer`, `/anomaly-explorer`** — keep canvas/SVG logic; wrap as client components. | `app/timeline/page.tsx`, `app/visualize/page.tsx`, `components/cosmic-canvas.tsx`, etc | 6 hr | 3 hr | step 2 |
| 10b | **Port secondary pages** (`/methodology`, `/sources`, `/findings`, `/datasets`, `/contributions`, `/projects`, `/speculations`, `/infrastructure`, `/versions`, `/status`, `/ssot`, `/admin`, `/team`, `/sitemap`, etc — ~15 simple content pages). | `app/<segment>/page.tsx` per route | 6 hr | 1.5 hr (parallel — 10 agents, 1 page each) | step 2 |
| 11 | **Cutover.** Move all `*.html` to `static-archive/`. Promote `nextjs-site/` to root. Add redirects per §H.1. Merge PR. | repo root | 1 hr | 1 hr | every prior step |

**Solo total:** ~56 hours = ~5 working days (with breaks).
**Parallel total:** ~28 hours = ~1.5 working days if 4 sub-agents run steps 9, 10, 10a, 10b concurrently. Houston's "parallel sub-agents for independent work" rule applies — every page port is independent once the layout is in place (step 2).

### Quality gates between steps

After steps 3, 6, 9, 10, 11: run `/qa` (mobile + desktop sweep) and `/design-review` (visual regression). After step 11: run `/cso` (security audit — the new API routes need it).

---

## H. Risks / preserve-at-all-costs

### H.1 SEO and inbound URL preservation

**The hard rule:** any URL that exists in arXiv abstracts, Google index, or backlinks MUST resolve. The 4 paper PDFs in `public/papers/` are the highest-stakes example — they're linked from arXiv submission listings and from the Hubify Labs blog.

| URL pattern | Status | Action |
|---|---|---|
| `/public/papers/spin_torsion_paper1.pdf` | Critical (arXiv backlink target) | Next preserves `public/` literally → no change. |
| `/public/papers/paper2_fnl_forecast.pdf` | Critical | same |
| `/public/papers/paper3_anomaly_catalog.pdf` | Critical | same |
| `/public/papers/chirality_catalog_paper.pdf` | Critical | same |
| `/public/images/*.png` (figures) | High | Next preserves `public/` literally → no change. |
| `/index.html` | Indexed | Add `next.config.ts` redirect: `/index.html` → `/` (308). |
| `/paper.html` | Indexed | Redirect `/paper.html` → `/papers` (308). |
| `/paper.html#paper1` | Indexed | Redirect to `/papers/paper1`. The fragment doesn't survive a 308; if traffic is non-trivial, add a route handler that reads the fragment client-side and redirects. |
| `/explained.html` | Indexed | Redirect → `/explained`. |
| `/data-explorer.html` | Indexed | Redirect → `/data`. |
| `/figures.html` | Indexed | Redirect → `/figures`. |
| `/glossary.html` | Indexed | Redirect → `/glossary`. |
| `/activity.html` | Indexed | Redirect → `/activity`. |
| `/articles/<slug>.html` | Indexed (9 articles) | Redirect each → `/articles/<slug>`. |
| `/research/project_master_dossier/index.html` | Indexed | Redirect → `/research/dossier`. |

```ts
// next.config.ts (excerpt)
async redirects() {
  const map: Array<[string, string]> = [
    ["/index.html", "/"],
    ["/paper.html", "/papers"],
    ["/explained.html", "/explained"],
    ["/data-explorer.html", "/data"],
    ["/figures.html", "/figures"],
    ["/glossary.html", "/glossary"],
    ["/activity.html", "/activity"],
    ["/timeline.html", "/timeline"],
    ["/visualize.html", "/visualize"],
    ["/datasets.html", "/datasets"],
    ["/galaxy-explorer.html", "/galaxy-explorer"],
    ["/anomaly-explorer.html", "/anomaly-explorer"],
    ["/methodology.html", "/methodology"],
    ["/methodology-anomaly.html", "/methodology-anomaly"],
    ["/mathematics.html", "/mathematics"],
    ["/sources.html", "/sources"],
    ["/articles.html", "/articles"],
    ["/contributions.html", "/contributions"],
    ["/findings.html", "/findings"],
    ["/projects.html", "/projects"],
    ["/team.html", "/team"],
    ["/research/project_master_dossier/", "/research/dossier"],
    ["/research/project_master_dossier/index.html", "/research/dossier"],
    // articles/*
    ["/articles/ech-bounce-phenomenology.html", "/articles/ech-bounce-phenomenology"],
    ["/articles/evolution-of-rigor.html", "/articles/evolution-of-rigor"],
    ["/articles/look-up.html", "/articles/look-up"],
    ["/articles/matter-bounce-blueprint.html", "/articles/matter-bounce-blueprint"],
    ["/articles/program-visual-guide.html", "/articles/program-visual-guide"],
    ["/articles/publication-roadmap.html", "/articles/publication-roadmap"],
    ["/articles/students-guide-big-bounce.html", "/articles/students-guide-big-bounce"],
    ["/articles/technical-evaluation.html", "/articles/technical-evaluation"],
    ["/articles/the-window.html", "/articles/the-window"],
  ];
  return map.map(([source, destination]) => ({ source, destination, permanent: true }));
}
```

### H.2 Math visual fidelity (KaTeX vs MathJax)

After every page with math is ported: take a side-by-side screenshot at the same viewport, eyeball the equations. Most will be byte-identical. Common diffs to watch:

- **Spacing around `=`** — KaTeX uses TeX's natural spacing; MathJax sometimes adds extra. Equality is usually fine.
- **Display equation centering** — `BlockMath` is centered by default; if the legacy site left-aligned, wrap with `text-left`.
- **Subscripts on `\rm` text** — `f_{\rm NL}` renders identically in both.
- **`\mathcal`, `\mathbb`** — both renderers ship the fonts; identical output.

If a single equation breaks, the fallback is to keep MathJax for that one page (load only on `/mathematics`, not globally). But I expect zero of these.

### H.3 Mobile responsive regression

Houston's CLAUDE.md mandates `/qa` mobile sweep post-migration. Run at 480, 768, and 900 breakpoints. The current mobile pain points (table horizontal scroll, sidebar drawer, hamburger nav) all have direct shadcn equivalents (Sheet, ScrollArea, Sheet again). No regression expected if the bridge layer in §C is honored.

### H.4 The dossier nested page

`research/project_master_dossier/index.html` was originally a separate site. It has 12 supporting markdown files in the same folder. During the migration:

1. Decision: do those 12 markdown files have unique inbound traffic? (Audit in Vercel analytics.)
2. If yes: each becomes `app/research/dossier/[slug]/page.mdx`.
3. If no: they become source content for the single `/research/dossier` index page (RSC reads them at build time).
4. Either way, redirect `/research/project_master_dossier/...` → `/research/dossier/...`.

### H.5 Design quality benchmarking — k-dense.ai and feynman.is

Memory entry: Houston compares the production polish of this site against k-dense.ai and feynman.is. The migration is the moment to push design quality toward those targets. Concretely:

- **k-dense.ai** has dense data displays with airy spacing and a cohesive monochrome palette. Match: keep our monochrome discipline, lean harder on whitespace in `/data`, raise the visual hierarchy of stat cards on `/`.
- **feynman.is** has a CLI-first / terminal-aesthetic with serif body text in long-form articles. Match: we already have that DNA. Polish the article pages (`/articles/[slug]`) with Newsreader serif body + measure-controlled column width (~680px, like the current `explained.html`).
- **Both** have proper Cmd+K command palettes. shadcn `Command` gives us this for free in step 7.

Before merging step 11 (cutover), run `/design-review` and `/design-shotgun` to compare the new site against k-dense.ai and feynman.is screenshots.

### H.6 Inline scripts that today run on legacy pages

`nav.js` injects favicon, theme, sidebar, topbar, inline nav at runtime. Several pages ALSO have inline `<script>` blocks for page-specific behavior (the lightbox, the data-explorer, the visualize canvas). During the migration the inline scripts get hoisted into `_components/` client components. Audit each `<script>` block against this list before deleting:

- `figures.html` lightbox script → `components/figure-gallery.tsx` (step 6)
- `data-explorer.html` data + sort + calc scripts → `app/data/_components/*` (step 10)
- `visualize.html` canvas simulation → `components/cosmic-canvas.tsx` (step 10a)
- `timeline.html` SVG animation → `components/cosmic-timeline.tsx` (step 10a)
- `glossary.html` filter → `components/glossary-search.tsx` (step 7, replaced by `Command`)
- `nav.js` favicon/theme/active-page → handled by `next-themes` + `app/layout.tsx` `metadata` + Next's `usePathname()` (step 2)
- `nav.js` search loader → `Command` palette + build-time index (step 7)

### H.7 The drive-to-100 cron loop

CLAUDE.md flags an autonomous cron loop ("drive-to-100") that fires `chore(drive-to-100): fire #N` commits to `main` to drive paper SSOT to 100%. **DO NOT start the migration while drive-to-100 is active.** Pause the cron during the migration window — every fire that lands on `main` while we're in `nextjs-site/` is a merge conflict in the static HTML pages we're trying to retire.

---

## Appendix 1: Example component — the CLI sidebar

Annotated reference port. Fully replaces `nav.js` lines 102-159.

```tsx
// components/sidebar-cli.tsx
"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { ChevronDown, Lock, Github } from "lucide-react";
import { cn } from "@/lib/utils";

type SidebarLink = { href: string; label: string; page: string };
type SidebarGroup = { label: string; items: SidebarLink[]; defaultCollapsed?: boolean; locked?: boolean };

const PUBLIC_TOP: SidebarLink[] = [
  { href: "/papers", label: "papers", page: "papers" },
  { href: "/explained", label: "explainer", page: "explained" },
];

const GROUPS: SidebarGroup[] = [
  { label: "data & explore", items: [
    { href: "/data", label: "data catalog", page: "data" },
    { href: "/anomaly-explorer", label: "paper 3 · anomalies", page: "anomaly-explorer" },
    { href: "/galaxy-explorer", label: "paper 4 · chirality", page: "galaxy-explorer" },
    { href: "/datasets", label: "datasets", page: "datasets" },
  ]},
  { label: "reference", items: [
    { href: "/figures", label: "figures", page: "figures" },
    { href: "/glossary", label: "glossary & equations", page: "glossary" },
    { href: "/articles", label: "articles", page: "articles" },
    { href: "/mathematics", label: "mathematics", page: "mathematics" },
  ]},
  { label: "visualize", defaultCollapsed: true, items: [
    { href: "/timeline", label: "cosmic timeline", page: "timeline" },
    { href: "/visualize", label: "simulation", page: "visualize" },
  ]},
  { label: "internal", locked: true, defaultCollapsed: true, items: [
    { href: "/ssot", label: "ssot & tasks", page: "ssot" },
    { href: "/contributions", label: "key findings", page: "contributions" },
    { href: "/activity", label: "activity", page: "activity" },
    { href: "/status", label: "status", page: "status" },
    { href: "/projects", label: "projects", page: "projects" },
    { href: "/methodology", label: "methodology", page: "methodology" },
    { href: "/sources", label: "sources", page: "sources" },
    { href: "/speculations", label: "speculations", page: "speculations" },
    { href: "/infrastructure", label: "infrastructure", page: "infrastructure" },
    { href: "/versions", label: "versions", page: "versions" },
    { href: "/sitemap", label: "sitemap", page: "sitemap" },
    { href: "/admin", label: "admin", page: "admin" },
    { href: "/research/dossier", label: "dossier", page: "dossier" },
  ]},
];

export function SidebarCli() {
  const pathname = usePathname();
  const isActive = (href: string) => pathname === href || pathname.startsWith(href + "/");

  return (
    <aside className="fixed top-0 left-0 bottom-0 w-[var(--sidebar-w)] z-[100] bg-[var(--bg-sidebar)] flex flex-col overflow-y-auto">
      <Link href="/" className="px-6 pt-5 pb-4 text-[15px] font-semibold tracking-tight text-white border-b border-[#333] font-mono">
        bigbounce
      </Link>

      <nav className="py-4 flex-1">
        <Link href="/"
              className={cn(
                "flex items-center gap-1.5 px-6 py-1.5 mb-0.5 font-mono text-[13px] font-medium",
                "before:content-['~/'] before:text-[#555] after:content-['>'] after:text-[#555]",
                isActive("/") ? "text-white" : "text-[#888] hover:text-white",
              )}>
          research
        </Link>

        {PUBLIC_TOP.map((l) => (
          <Link key={l.page} href={l.href}
                className={cn(
                  "block py-1.5 pl-9 pr-6 font-mono text-[13px]",
                  isActive(l.href) ? "text-white bg-white/10 font-medium" : "text-[#999] hover:text-white hover:bg-white/5",
                )}>
            {l.label}
          </Link>
        ))}

        {GROUPS.map((g) => <SidebarGroupComponent key={g.label} group={g} isActive={isActive} />)}
      </nav>

      <div className="p-3 px-6 border-t border-[#333] font-mono text-[10px] text-[#555] leading-snug">
        Houston Golden<br />
        Independent Researcher<br />
        houston@hubify.com
        <a href="https://github.com/Hubify-Projects/bigbounce" target="_blank" rel="noreferrer"
           className="inline-flex items-center gap-1.5 mt-2 text-[var(--text-tertiary)] no-underline text-xs">
          <Github size={14} /> GitHub
        </a>
      </div>
    </aside>
  );
}

function SidebarGroupComponent({ group, isActive }: { group: SidebarGroup; isActive: (h: string) => boolean }) {
  const [open, setOpen] = useState(!group.defaultCollapsed);
  return (
    <>
      <button onClick={() => setOpen((v) => !v)}
              className={cn(
                "w-full flex items-center justify-between px-6 py-1.5 mt-3 font-mono text-[10px] uppercase tracking-wider text-[#555] hover:text-[#888]",
                group.locked && "opacity-55",
              )}>
        <span className="flex items-center gap-1.5">
          {group.locked && <Lock size={11} className="opacity-60" />}
          {group.label}
        </span>
        <ChevronDown size={8} className={cn("transition-transform", !open && "-rotate-90")} />
      </button>
      <div className={cn("overflow-hidden transition-[max-height] duration-200", open ? "max-h-[500px]" : "max-h-0")}>
        {group.items.map((l) => (
          <Link key={l.page} href={l.href}
                className={cn(
                  "block py-1.5 pl-9 pr-6 font-mono text-[13px]",
                  isActive(l.href) ? "text-white bg-white/10 font-medium" : "text-[#999] hover:text-white hover:bg-white/5",
                )}>
            {l.label}
          </Link>
        ))}
      </div>
    </>
  );
}
```

---

## Appendix 2: Example route — `/papers/paper1` using shadcn Card + Badge

```tsx
// app/papers/[slug]/page.tsx
import { notFound } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Eq } from "@/components/equation";
import Link from "next/link";

type Paper = {
  slug: string;
  number: 1 | 2 | 3 | 4;
  title: string;
  subtitle: string;
  pages: number;
  readiness: number;       // %
  target: string;          // "revtex4-2", "ApJS", "MNRAS"
  date: string;
  pdf: string;             // /public/papers/...
  accent: string;          // tailwind border color, e.g. "border-l-blue-700"
  abstract: string;
  bullets: string[];
};

const PAPERS: Record<string, Paper> = {
  paper1: {
    slug: "paper1", number: 1,
    title: "Spin-Torsion Cosmology",
    subtitle: "The theoretical foundation. Einstein-Cartan-Holst framework with Loop Quantum Gravity.",
    pages: 27, readiness: 100, target: "revtex4-2", date: "Apr 29 2026",
    pdf: "/papers/spin_torsion_paper1.pdf",
    accent: "border-l-blue-700",
    abstract: "We test the Einstein-Cartan-Holst framework against 309,789 frozen MCMC posterior samples...",
    bullets: [
      "14 structural barriers closing all bounce → dark energy routes",
      "ALP birefringence prediction β = 0.27° matching 3.9σ inverse-variance combined signal",
      "Perturbation-transparency theorem",
      "424,181 MCMC posterior samples across 3 dataset combinations",
    ],
  },
  // paper2, paper3, paper4 …
};

export async function generateStaticParams() {
  return Object.keys(PAPERS).map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: { params: { slug: string } }) {
  const p = PAPERS[params.slug];
  if (!p) return {};
  return {
    title: `${p.title} — BigBounce`,
    description: p.subtitle,
    openGraph: { title: p.title, description: p.subtitle, images: [`/images/figure${p.number}_lqg_holst_derivation_enhanced.png`] },
  };
}

export default function PaperPage({ params }: { params: { slug: string } }) {
  const paper = PAPERS[params.slug];
  if (!paper) notFound();

  return (
    <main className="container max-w-[860px] px-12 py-8">
      <div className="mb-6">
        <Link href="/papers" className="font-mono text-xs text-muted-foreground hover:text-foreground">← all papers</Link>
      </div>

      <Card className={`${paper.accent} border-l-4`}>
        <CardHeader>
          <div className="flex items-center gap-2 mb-2">
            <Badge variant="outline" className="font-mono">Paper {paper.number}</Badge>
            <Badge variant="outline" className="font-mono">{paper.pages} pages</Badge>
            <Badge variant="outline" className="font-mono">{paper.readiness}% Ready</Badge>
            <Badge variant="outline" className="font-mono">{paper.target}</Badge>
            <Badge variant="outline" className="font-mono text-muted-foreground">{paper.date}</Badge>
          </div>
          <CardTitle className="text-2xl font-bold tracking-tight">{paper.title}</CardTitle>
          <CardDescription className="text-base leading-relaxed">{paper.subtitle}</CardDescription>
        </CardHeader>

        <CardContent>
          <div className="border border-border border-l-2 border-l-foreground p-6 my-5 text-[13.5px] leading-[1.75]">
            <h4 className="font-mono text-xs uppercase tracking-wider text-muted-foreground mb-2">Abstract</h4>
            <p className="text-secondary-foreground">{paper.abstract}</p>
          </div>

          <h3 className="font-semibold text-sm mt-6 mb-3">Key results</h3>
          <ul className="space-y-2">
            {paper.bullets.map((b, i) => <li key={i} className="text-sm text-secondary-foreground">— {b}</li>)}
          </ul>

          <div className="my-6 border border-border border-l-2 border-l-foreground p-6 text-center">
            <Eq block>{`f_{\\rm NL} = -\\frac{35}{8} = -4.375`}</Eq>
            <p className="font-mono text-[11px] text-muted-foreground mt-2">Decisive prediction — Paper 2 §III</p>
          </div>

          <div className="flex flex-wrap gap-2 mt-8">
            <Button asChild><a href={paper.pdf} target="_blank" rel="noreferrer">Download PDF</a></Button>
            <Button asChild variant="outline"><Link href="/figures">Figures</Link></Button>
            <Button asChild variant="outline"><Link href="/data">Data</Link></Button>
          </div>
        </CardContent>
      </Card>
    </main>
  );
}
```

---

## Appendix 3: Root layout

```tsx
// app/layout.tsx
import type { Metadata } from "next";
import { Inter, IBM_Plex_Mono, Newsreader } from "next/font/google";
import { ThemeProvider } from "next-themes";
import { SidebarCli } from "@/components/sidebar-cli";
import { Topbar } from "@/components/topbar";
import { InlineNav } from "@/components/inline-nav";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-sans-loaded" });
const mono = IBM_Plex_Mono({ subsets: ["latin"], weight: ["400","500","600"], variable: "--font-mono-loaded" });
const newsreader = Newsreader({ subsets: ["latin"], variable: "--font-serif-loaded" });

export const metadata: Metadata = {
  title: { default: "BigBounce — Hubify Labs Bounce Cosmology Research Program", template: "%s — BigBounce" },
  description: "Four-paper research program testing bounce cosmology: theoretical framework, f_NL forecasts, 37.3M-source AI anomaly catalog, and 8.47M galaxy chirality catalog.",
  metadataBase: new URL("https://bigbounce.hubify.app"),
  openGraph: {
    type: "website", siteName: "BigBounce — Hubify Labs Bounce Cosmology Research Program",
    images: ["/images/figure1_lqg_holst_derivation_enhanced.png"],
  },
  twitter: { card: "summary_large_image" },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning className={`${inter.variable} ${mono.variable} ${newsreader.variable}`}>
      <body className="font-sans">
        <ThemeProvider attribute="data-theme" defaultTheme="light" enableSystem>
          <SidebarCli />
          <Topbar />
          <div className="ml-[var(--sidebar-w)] pt-[var(--topbar-h)] min-h-screen transition-[margin-left] duration-200 lg:ml-0 lg:[body[data-sidebar='open']_&]:ml-[var(--sidebar-w)]">
            <InlineNav />
            {children}
          </div>
        </ThemeProvider>
      </body>
    </html>
  );
}
```

---

## Appendix 4: Pre-flight checklist (run the day before kickoff)

- [ ] All 4 papers submitted to arXiv with ID strings recorded.
- [ ] `drive-to-100` cron paused.
- [ ] No open PRs against `main` modifying `*.html`.
- [ ] `git status` clean.
- [ ] Vercel project access confirmed.
- [ ] Memory entry "Next.js migration planned" updated to "Next.js migration in progress" with kickoff date.
- [ ] `/qa` and `/design-review` skills confirmed working — they're the gates between steps.
- [ ] One screenshot per current page captured at 480/900/1200 widths in `static-archive/snapshots/` for visual diff after migration.

---

**End of plan.** Time to next review: at kickoff. If a paper slips past arXiv submission deadline, the plan still applies — just delay step 1.
