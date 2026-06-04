#!/usr/bin/env node
/**
 * Seed `papers_notables` bullets for the 6 bigbounce papers.
 * Each paper gets 2-4 short reader-facing "notable contributions"
 * extracted from its abstract + intro headline. Distinct from
 * focusAreas (which targets reviewers).
 *
 * Idempotent — uses notables:upsertByOrdinal so re-runs replace bullet
 * text at the same ordinal slot rather than appending duplicates.
 */
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient(
  process.env.CONVEX_URL || "https://brilliant-panther-471.convex.cloud"
);

const NOTABLES = {
  "paper-1a": [
    "First channel-level no-go assessment of the four enumerated minimal-Einstein-Cartan-Holst (ECH) spin-torsion routes to late-time dark energy",
    "Perturbation-transparency theorem: for canonical scalar matter the Holst sector decouples from all scalar/tensor perturbation EOMs",
    "13 logically-independent mechanism-class constraints across 7 foundation studies and 6 observational branches",
    "Explicit scope disclosure: parity-odd ansatz has off-shell dimension +1 vs +4, treated as ansatz not derivation",
  ],
  "paper-1b": [
    "309,189 frozen Cobaya MCMC samples across two converged dataset combinations as a null-consistency test of $\\Delta N_{\\rm eff}$",
    "Both combinations find $\\Delta N_{\\rm eff}$ consistent with zero and $H_0$ consistent with $\\Lambda$CDM",
    "NaMaster pseudo-$C_\\ell$ pipeline validation on Planck Commander: $\\hat\\beta=0.238^\\circ$ recovery of $\\beta=0.27^\\circ$ injection",
    "Eskilt+Komatsu PR3-vs-PR4 disambiguation supplied verbatim to preempt recurring reviewer reflag",
  ],
  "paper-2": [
    "First template-mismatch quantification between matter-bounce and local $f_{\\rm NL}$ templates: local estimator recovers $84\\% \\pm 2\\%$ of bounce signal",
    "Bispectrum-only SPHEREx forecast $\\sigma(f_{\\rm NL}^{\\rm local}) \\approx 0.7$ gives template-corrected $3$–$5\\sigma$ after full systematic budget",
    "Bayesian model comparison: BF$\\sim 10$–$17$ favoring bounce over tuned multifield competitors at the broad-prior envelope",
    "Bounce-vs-inflation contrast: $|f_{\\rm NL}^{\\rm bounce}|/|f_{\\rm NL}^{\\rm inf}| \\approx 290$ in absolute value",
  ],
  "paper-3": [
    "Largest-scale autoencoder anomaly catalog to date: 378,280 unique anomalies across 7 archives (37.3M sources)",
    "$141\\times$ scale of the largest prior single-survey spectroscopic anomaly catalog (Liang et al.\\ 2023)",
    "Path-C rebuild protocol addresses cross-transfer artifacts: $21.5\\times$ anomaly-rate reduction after LAMOST native retraining",
    "Empirical multi-tracer $\\alpha=0.19 \\pm 0.65$ measured from QSO-candidate angular correlation; $\\sigma(f_{\\rm NL}) \\in [3.92, 8.98]$",
  ],
  "paper-4": [
    "Largest spiral chirality catalog: 3.2M DESI Legacy spirals (471,049 high-confidence at $p_{\\rm CW}^{\\rm eq} > 0.9$)",
    "Headline null $\\ell=1$ chirality-dipole observable: subsample-mask pseudo-$C_1$ at $-0.12\\sigma$, consistent with no dipole",
    "Four-null systematic battery + direct cross-spectrum disfavors clean-dipole interpretation: $\\ell=2$ broadband, no quartile scaling, $\\sigma=-2.89$ depth cross-spectrum at $\\ell=2$",
    "Falsification criterion: $>5\\sigma$ detection at $\\gtrsim 0.75\\%$ amplitude in future $\\geq 10^7$-galaxy systematics-modeled survey",
  ],
  "paper-5": [
    "First end-to-end environmental-dependence test of spiral chirality on 791,635 matched DESI DR1 $\\times$ Paper IV spirals",
    "V-Web tidal classification on 14.6M DR1 spectroscopic galaxies links every matched spiral to a cosmic-web class",
    "DESIVAST three-algorithm void catalog (VoidFinder, V2-REVOLVER, V2-VIDE) supplies the void anchor",
    "Tests whether spiral handedness is statistically independent of large-scale structure environment",
  ],
};

let totalInserted = 0;
for (const [slug, bullets] of Object.entries(NOTABLES)) {
  for (let i = 0; i < bullets.length; i++) {
    await client.mutation(api.notables.upsertByOrdinal, {
      paperSlug: slug,
      ordinal: i + 1,
      bullet: bullets[i],
    });
    totalInserted++;
  }
  console.log(`✔ ${slug}: ${bullets.length} bullets seeded`);
}

console.log(`\n✔ ${totalInserted} total notables across ${Object.keys(NOTABLES).length} papers`);

// Verify
const grouped = await client.query(api.notables.listAll);
console.log("\nPost-seed:");
for (const slug of Object.keys(NOTABLES)) {
  const rows = grouped[slug] ?? [];
  console.log(`  ${slug.padEnd(12)} ${rows.length} bullets`);
}
