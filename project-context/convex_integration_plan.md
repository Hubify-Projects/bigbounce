# Convex Integration Plan for BigBounce

**Purpose:** Hand this file to a separate Claude Code session to set up Convex as the persistence layer for the BigBounce research site.

---

## What Exists Now

- Static site deployed on Vercel from `main` branch
- Review page at `review/pipeline-b-desi-spectral.html` uses **localStorage** for saving labels, comments, and checklist state
- No backend database currently
- Site is vanilla HTML/CSS/JS (no React, no framework)

## Convex Details

```
Dev: impressive-quail-879
  URL: https://impressive-quail-879.convex.cloud
  Deploy key in .env.local as CONVEX_DEV_DEPLOY_KEY

Prod: scintillating-cow-269
  URL: https://scintillating-cow-269.convex.cloud
  Deploy key in .env.local as CONVEX_PROD_DEPLOY_KEY
```

## What Convex Should Store

### Table: `reviews`
```
{
  pipelineId: string,        // "pipeline-b", "pipeline-a", etc.
  objectId: string,          // DESI TARGETID or equivalent
  label: string,             // "INTERESTING" | "ARTIFACT" | "KNOWN_TYPE" | "NEEDS_SPECTRUM" | "CONFIRMED"
  aiLabel: string,           // original AI-assigned label
  aiReason: string,          // AI reasoning text
  humanNotes: string,        // reviewer's free-text comments
  reviewerName: string,      // "Houston" or whoever
  reviewedAt: number,        // timestamp
  metadata: object,          // ra, dec, z, type, score, fluxes — whatever the pipeline provides
}
```

### Table: `checklistItems`
```
{
  pipelineId: string,
  category: string,          // "leakage", "astrophysical", "instrument", "falsification"
  text: string,              // the risk description
  status: string,            // "not_started" | "in_progress" | "addressed" | "accepted_risk"
  updatedAt: number,
}
```

### Table: `pipelineState`
```
{
  pipelineId: string,
  name: string,
  status: string,            // "IDEA" | "PROTOTYPE" | ... | "PAPER_READY"
  gatesPassed: number,
  totalGates: number,
  lastUpdated: number,
  summary: string,
}
```

### Table: `models`
```
{
  pipelineId: string,
  modelName: string,
  version: string,
  huggingfaceUrl: string,
  trainingSamples: number,
  metrics: object,           // { train_loss, val_loss, gate3_status, etc. }
  createdAt: number,
}
```

## Integration Points

### 1. Review Page (`review/pipeline-b-desi-spectral.html`)

Currently uses localStorage. Replace with Convex client:

```html
<script src="https://unpkg.com/convex/dist/browser/convex.js"></script>
<script>
  const client = new ConvexHttpClient("https://impressive-quail-879.convex.cloud");

  // Save a review
  async function saveReview(objectId, label, notes) {
    await client.mutation("reviews:save", { pipelineId: "pipeline-b", objectId, label, humanNotes: notes, reviewedAt: Date.now() });
  }

  // Load reviews
  async function loadReviews() {
    return await client.query("reviews:byPipeline", { pipelineId: "pipeline-b" });
  }
</script>
```

### 2. Review Hub (`review/index.html`)

Query `pipelineState` to show live status cards for each pipeline.

### 3. Activity Feed (`activity.html`)

Optionally query recent reviews to show "Houston reviewed 5 objects in Pipeline B" type entries.

## What NOT To Change

- Do NOT convert the site to React/Next.js — keep it vanilla HTML
- Do NOT move the science data (spectra, MCMC chains) into Convex — those stay as files
- Do NOT add authentication — Houston is the only reviewer for now
- Keep localStorage as a fallback if Convex is unreachable

## Implementation Steps

1. `npm install convex` in the project root
2. Create `convex/schema.ts` with the tables above
3. Create `convex/reviews.ts` with mutations (save, update) and queries (byPipeline, byObject)
4. Create `convex/checklist.ts` with mutations and queries
5. Create `convex/pipelineState.ts` with mutations and queries
6. Deploy to dev: `npx convex dev --once`
7. Update `review/pipeline-b-desi-spectral.html` to use Convex client instead of localStorage
8. Test locally
9. Deploy to prod: `npx convex deploy`

## Prompt for the Other Session

```
You are working in the BigBounce research repo at /Users/houstongolden/Desktop/CODE_2026/bigbounce.

Read project-context/convex_integration_plan.md for the full plan.

Task: Set up Convex as the persistence backend for the review system.

The site is vanilla HTML/CSS/JS on Vercel (no React). The review page at
review/pipeline-b-desi-spectral.html currently uses localStorage.

Convex details are in .env.local (CONVEX_DEV_URL, CONVEX_DEV_DEPLOY_KEY).

Steps:
1. Install convex, create schema, write mutations/queries
2. Deploy to dev
3. Update the review page to use ConvexHttpClient
4. Keep localStorage as fallback
5. Test that saving/loading reviews works

Do NOT touch any science code, research files, or pipeline scripts.
Do NOT convert the site to React. Keep it vanilla JS.
```
