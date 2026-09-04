import { createElement, Fragment, type ReactNode } from "react";
import Link from "next/link";
import { cn } from "@/lib/utils";

// NOTE: this file is intentionally `.ts` (not `.tsx`) per the Lane 6 spec —
// `Term` is built with `createElement` rather than JSX so it stays parseable
// as plain TypeScript while still exporting a component other lanes can use.

/**
 * Shared jargon -> glossary anchor map (REDESIGN_SPEC.md §3.8, §6 Lane 6).
 * Every key's slug MUST match an `id="term-<slug>"` on /glossary. Other
 * lanes may import { GLOSSARY_TERMS, Term } from this file to wrap the same
 * jargon strings on their own pages without duplicating the map.
 */
export interface GlossaryTermMeta {
  slug: string;
  /** One-line plain-English gloss, stated at evidential strength. */
  gloss: string;
}

export const GLOSSARY_TERMS: Record<string, GlossaryTermMeta> = {
  "big-bounce": {
    slug: "big-bounce",
    gloss: "the universe transitioned from contraction to expansion at finite density, avoiding the Big Bang singularity",
  },
  "f_nl": {
    slug: "f-nl",
    gloss: "the amplitude of local primordial non-Gaussianity; P2 derives f_NL = -35/16 for its stated matter-contraction assumptions",
  },
  birefringence: {
    slug: "birefringence",
    gloss: "rotation of the CMB polarization angle as photons travel through space",
  },
  quintom: {
    slug: "quintom",
    gloss: "a dark-energy model allowing the equation of state to cross w = -1; treated theoretically in this program",
  },
  ech: {
    slug: "ech",
    gloss: "Einstein-Cartan-Holst theory — general relativity extended with spacetime torsion",
  },
  torsion: {
    slug: "torsion",
    gloss: "the antisymmetric part of the spacetime connection; can prevent singularities at extreme density",
  },
  mcmc: {
    slug: "mcmc",
    gloss: "Markov Chain Monte Carlo — the sampling method used to explore cosmological parameter posteriors",
  },
  spherex: {
    slug: "spherex",
    gloss: "NASA's SPHEREx mission (~2028), which will measure f_NL to roughly ±0.7-1.0",
  },
  "sigma-f-nl": {
    slug: "sigma-f-nl",
    gloss: "the measurement uncertainty on f_NL — current data do not yet reach the program's conditional prediction",
  },
  pbh: {
    slug: "pbh",
    gloss: "primordial black holes — a hypothetical dark-matter candidate; the program's PBH channel is a measured null (7.0 dex short)",
  },
  nanograv: {
    slug: "nanograv",
    gloss: "a pulsar-timing gravitational-wave background measurement used as a PTA-channel comparison point",
  },
  autoencoder: {
    slug: "autoencoder",
    gloss: "a neural network trained to reconstruct its input; poor reconstructions flag anomaly candidates, not discoveries",
  },
  "barbero-immirzi": {
    slug: "barbero-immirzi",
    gloss: "a loop-quantum-gravity parameter that sets the minimum quantum of area, appearing in the ECH action",
  },
  "holst-term": {
    slug: "holst-term",
    gloss: "the parity-odd topological term in the gravitational action that generates quantum birefringence effects",
  },
  lqc: {
    slug: "lqc",
    gloss: "Loop Quantum Cosmology — a quantum-geometric bounce mechanism, distinct from the ECH/torsion route",
  },
  "matter-bounce": {
    slug: "matter-bounce",
    gloss: "a bounce scenario with a matter-like (w ~ 0) contracting phase; the source of the conditional f_NL = -35/16 prediction",
  },
  pta: {
    slug: "pta",
    gloss: "Pulsar Timing Array — a nanohertz gravitational-wave probe; the program's PTA channel is closed as a null, 14.3 dex below NANOGrav",
  },
  sigw: {
    slug: "sigw",
    gloss: "Scalar-Induced Gravitational Waves — a gravitational-wave background sourced by second-order scalar perturbations at horizon re-entry",
  },
  "k-eta-b": {
    slug: "k-eta-b",
    gloss: "the dimensionless product of wavenumber and bounce-epoch conformal time, kη_B — sets the horizon scale at the bounce; bounce-scale enhancement near kη_B ~ 1 is the one remaining non-null route for Track A's PTA/PBH channels",
  },
  "s1-s2-schemes": {
    slug: "s1-s2-schemes",
    gloss: "the two computational schemes tried for the bounce's own cubic transmission term — S1 gives a regular finite result, S2 diverges",
  },
  "delta-n": {
    slug: "delta-n",
    gloss: "the separate-universe delta-N formalism used to compute the curvature perturbation from differences in e-folds across patches",
  },
  namaster: {
    slug: "namaster",
    gloss: "NaMaster, the pseudo-Cl power-spectrum code whose validated pipeline underwrites the program's birefringence measurement (P1B is namaster-proof research software)",
  },
  readiness: {
    slug: "readiness",
    gloss: "the Convex-sourced publication-readiness percentage per work — science, evidence, review convergence, and packaging, plus Houston's final sign-off; never a venue or submission decision",
  },
  path_c: {
    slug: "path-c",
    gloss: "a historic native-retrain quality-gate concept for exploratory anomaly pipelines; legacy/superseded methodology, not a current catalog claim",
  },
};

export type GlossaryTermKey = keyof typeof GLOSSARY_TERMS;

export interface TermProps {
  /** Key into GLOSSARY_TERMS, e.g. "f_nl", "pta", "k-eta-b". */
  term: GlossaryTermKey;
  children: ReactNode;
  className?: string;
}

/**
 * Wraps a jargon string with a link into its /glossary#term-<slug> anchor.
 * The link carries the gloss as a native title tooltip so the plain-English
 * meaning is one hover away without leaving the page. Styling relies on
 * existing global `a`/`.container a` rules (globals.css is Lane-1-owned and
 * out of scope here) plus a dotted underline so a glossary link reads as
 * distinct from a plain navigation link.
 */
export function Term({ term, children, className }: TermProps) {
  const meta = GLOSSARY_TERMS[term];
  if (!meta) return createElement(Fragment, null, children);
  return createElement(
    Link,
    {
      href: `/glossary#term-${meta.slug}`,
      className: cn("underline decoration-dotted underline-offset-2", className),
      title: meta.gloss,
    },
    children,
  );
}
