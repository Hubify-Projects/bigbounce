import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p1b",
  version: "v1B.0.99",
  datestamp: "July 4, 2026",
  texCommit: "3b7904ceab30e175b429e525e2c8d89c42e9897e",
  pdfMd5: "4a69075a1d001465fd504e1f4594c591",
  pdfPages: 22,
  pdfSizeBytes: 1171065,
  changelog: "RS25 Grok MINOR closure (no physics changed): §III.A added explicit thermal-average intermediate step <(psibar g5 g^mu psi)^2>_T ~ n_f^2 ~ (g_* T^3)^2 for the dim-6 four-fermion contact operator, cite Kapusta & Gale (2006); Table IV caveat that posterior-mass fractions are conditional on the Gaussian summary-likelihood approx and omit EB-specific band-power covariance/calibration; §IV Fig.3 explicit real-sky clause (no systematic floor; galactic foregrounds break beta-alpha degeneracy). DeltaN_eff^(ECH) UNCHANGED.",
  sitePdfPath: "/papers/paper1b_mcmc_companion_v1B.0.99.pdf",
});
console.log("Inserted:", result);
