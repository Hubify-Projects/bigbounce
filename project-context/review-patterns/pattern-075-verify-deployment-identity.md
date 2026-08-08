# Pattern 075 — Verify deployment identity before every deploy (two real hijacks)

**Class:** ops-reliability
**First observed:** 2026-07-21/23 (Vercel junk-project relink; Convex prod-vs-dev split)

## Observation
Two distinct deploy-target drifts in one week: (a) the Vercel CLI silently
re-linked the deploy dir to a junk project ("out") so prod deploys went
nowhere; (b) `npx convex deploy` pushed a function fix to the PROD deployment
while the live site reads the DEV deployment (brilliant-panther-471) — the fix
was invisible until re-pushed with `npx convex dev --once`.

## Rule
Before any deploy, assert the target identity from the config on disk
(.vercel/project.json projectId; CONVEX_DEPLOYMENT in .env.local) and verify
the effect ON THE SERVING ENDPOINT afterward (curl the live domain / query the
live Convex URL). "Deploy succeeded" is not "the live surface changed."
