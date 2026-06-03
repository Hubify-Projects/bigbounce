import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p5",
  version: "v0.1.44",
  datestamp: "2026-06-03",
  texCommit: "f1d312483f38a1a64dea1d19716bdc81bd8309a3",
  pdfMd5: "d1692724a5d83198e325f8e3f4bebc2a",
  pdfPages: 21,
  pdfSizeBytes: 965918,
  changelog: "R-upgraded-round9 closure bundle (7 do-now fixes): GRO-B1 title retitle to lead with DESIVAST primary path; GRO-B2 'strongest' wording softened; GEM-M1+GPT-M3+GRO-M1 3-way RSD anisotropic-eigenvalue reframing; PER-M1 abstract DESIVAST scope tightened; GEM-m1 'any future model' scoped to bounce-chirality coupling class @ 25 Mpc/h; GEM-n1 §XI.B retitled 'Implications for bounce and inflation models'; GRO-n1 380-line preamble changelog stripped (archived to CHANGELOG_pre-v0.1.44.txt). Toy EFT appendix retained with v0.1.41 caveat per Houston decision.",
});
console.log("Inserted:", result);
