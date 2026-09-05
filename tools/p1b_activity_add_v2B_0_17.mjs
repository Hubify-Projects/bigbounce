import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.activityFeed.add, {
  type: "skill-improvement",
  date: "2026-09-04",
  title: "P1B v2B.0.17 — namaster-proof reframed as verification primitive; blind shortcut-detection test",
  body: "Novelty lift #3 integrated: namaster-proof's content-bound execution receipts reframed and tested against a pre-declared, sealed blind protocol (18 runs). Verifier detected all 4 shortcut classes it can see (operator-skip, operator-truncate, grid-interpolate, cache-substitute) 12/12 with 0/3 false positives on honest runs; a 5th, pre-declared metadata-forgery class escaped 3/3 as predicted by the threat model. New paper section, receipt-binding table, limitations, and reproducibility manifest p1b-blind-shortcut-detection added. Claim framed exactly at its evidential strength: a shortcut detector, not a fraud detector. No prior science number changed. 4-pass recompile clean (0 undef refs, 8pp), mirrored to all served paths (md5 7bc21cbe), tarball rebuilt + standalone-verified.",
  tags: [
    { label: "P1B", kind: "paper" },
    { label: "v2B.0.17", kind: "version" },
    { label: "namaster-proof", kind: "software" },
  ],
});
console.log("Inserted:", result);
