import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p5",
  version: "v0.1.43",
  datestamp: "2026-06-02",
  texCommit: "1fbec906061fa122ce659d81c338bc9d4deea27b",
  pdfMd5: "ef20d921c541cfe3f2b473194e5d530e",
  pdfPages: 21,
  pdfSizeBytes: 963548,
  changelog: "First compiled PDF for Houston — env-dependence test on 791,635 DESI DR1 spirals. R-upgraded-round7 close (PER-B1 author-order + PER-M1 T-Web tracer-mix).",
});
console.log("Inserted:", result);
