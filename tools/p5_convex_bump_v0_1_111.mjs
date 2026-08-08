import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p5",
  version: "v0.1.111",
  datestamp: "July 9, 2026",
  texCommit: "ca08043d",
  pdfMd5: "5c21304d883b2ebcca7392c48e16463a",
  pdfPages: 42,
  pdfSizeBytes: 1400649,
  changelog:
    "CV-round EXT closure (2026-07-09; ChatGPT MAJOR-revisions reopened off CA ACCEPT, Grok/Gemini MINOR). " +
    "Framing/relocation only; every verified number unchanged EXCEPT the stated systematic envelope, which was WIDENED (never tightened). " +
    "B1: headline recast everywhere as a bound on the classifier-labelled CW fraction (not physical spiral chirality), with 69.91%/kappa=0.40 attenuation caveat (abstract, App A, XII-B, Conclusions). " +
    "B2: in-footprint-restricted DESIVAST contrast (n_nonvoid=253,276, dfCW=+0.0018) promoted to PRIMARY; all-z<=0.24-outside-hole (n=621,964, dfCW=+0.0007) demoted to sensitivity check. " +
    "B3: consolidated systematic-error table; geometry (0.60pp) now co-dominant (not sub-dominant); honest quadrature envelope widened 0.5-0.6pp -> ~0.9pp everywhere (max single excursion 0.60pp). " +
    "B4: 'primary' -> 'designated primary for reporting / exploratory'; removed 'look-elsewhere can only weaken a null' (wrong for upper bounds). " +
    "B5: immutable-artifact framing kept honest future-tense (no DOI claimed). " +
    "M1 matched-control/IPW pointer (adjustment via program-split + global systematics; full IPW disclosed future item); M2 sphere-PIS labeled author-constructed approximation vs catalog-native GALZONE; M3 title now 'Redshift-Space...'; M4 T-Web section relabeled secondary diagnostic; M5 0/6 concordance softened; M6 toy-EFT supplementary-tier; M7 bright/dark 0.81pp leakage into DESIVAST = ~0.001pp; M8 statistics-glossary table. " +
    "Recompile 0 undef, 0 overfull (42 pp). Standalone tarball verified.",
  sitePdfPath: "/papers/p5_desi_chirality_v0.1.111-2026-07-09.pdf",
  arxivTarballPath: "submissions/P5/arxiv_p5_v0.1.111.tar.gz",
});
console.log("P5 v0.1.111 inserted:", result);
