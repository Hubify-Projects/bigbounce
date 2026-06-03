import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p1b",
  version: "v1B.0.42",
  datestamp: "2026-06-03",
  texCommit: "f1d312483f38a1a64dea1d19716bdc81bd8309a3",
  pdfMd5: "03b1e2fbf229bc333627548a6e74872c",
  pdfPages: 12,
  pdfSizeBytes: 731368,
  changelog: "delete audit-trail prose L1211-1215 (GEM-m1, pattern-014/017) + hedge natural-parameters framing 3 spots (GEM-B1, pattern-005)",
});
console.log("Inserted:", result);
