import type { Metadata } from "next";
import { PageHeader } from "@/components/primitives";
import { GLOSSARY_TERMS } from "@/lib/glossaryLinks";

export const metadata: Metadata = {
  title: "Glossary",
  description:
    "Plain-English glosses for every jargon term, parameter, and equation used across the BigBounce research program.",
};

interface Entry {
  term: string;
  pronunciation: string;
  definition: string;
  slug: string;
}

// Display text + pronunciation kept alongside the shared gloss in
// glossaryLinks.ts (single source of truth for the term -> slug map and the
// one-line gloss). This list supplies the fuller definition shown here.
const entries: Entry[] = [
  { term: "Big Bounce", pronunciation: "big bowns", slug: GLOSSARY_TERMS["big-bounce"].slug, definition: "A cosmological model where the universe transitioned from a contraction phase to expansion through a bounce at finite density, avoiding the Big Bang singularity." },
  { term: "f_NL", pronunciation: "eff-en-ell", slug: GLOSSARY_TERMS["f_nl"].slug, definition: "The amplitude of local primordial non-Gaussianity. P2 derives f_NL = -35/16 = -2.1875 for its stated matter-contraction assumptions. A future SPHEREx measurement may test that conditional prediction; it is not a current bounce detection." },
  { term: "Birefringence", pronunciation: "by-ree-FRIN-jens", slug: GLOSSARY_TERMS.birefringence.slug, definition: "The rotation of CMB polarization angle β as photons travel through space. Predicted β = 0.27° from ALP field evolution. Current measurement: 0.342° ± 0.094° (3.6σ)." },
  { term: "Quintom", pronunciation: "KWIN-tom", slug: GLOSSARY_TERMS.quintom.slug, definition: "A dark energy model with both quintessence (w > -1) and phantom (w < -1) fields, allowing the equation of state to cross w = -1. Treated theoretically in our program. External DESI DR2 (Adame et al.) reports 2.8-4.2σ for w-crossing." },
  { term: "ECH", pronunciation: "ee-see-aitch", slug: GLOSSARY_TERMS.ech.slug, definition: "Einstein-Cartan-Holst theory. Extends general relativity with torsion (antisymmetric part of the spacetime connection). A 14-constraint catalog closes the four enumerated minimal-ECH dark-energy routes at the channel level, under stated assumptions." },
  { term: "Torsion", pronunciation: "TOR-shun", slug: GLOSSARY_TERMS.torsion.slug, definition: "The antisymmetric part of the spacetime connection. In ECH theory, torsion couples to fermion spin and can prevent gravitational singularities by providing a repulsive force at extreme densities." },
  { term: "MCMC", pronunciation: "em-see-em-see", slug: GLOSSARY_TERMS.mcmc.slug, definition: "Markov Chain Monte Carlo. A statistical sampling method used to explore parameter spaces. Historic posterior records are research context, not P1B's publication role: P1B is namaster-proof research software." },
  { term: "SPHEREx", pronunciation: "SFEER-ex", slug: GLOSSARY_TERMS.spherex.slug, definition: "Spectro-Photometer for the History of the Universe, Epoch of Reionization, and Ices Explorer. NASA mission launching ~2028 that will measure f_NL to σ ≈ 0.7-1.0." },
  { term: "σ(f_NL)", pronunciation: "sigma of eff-en-ell", slug: GLOSSARY_TERMS["sigma-f-nl"].slug, definition: "The uncertainty on the f_NL measurement. Current external constraints do not establish P2's conditional matter-contraction prediction; the SPHEREx target is prospective." },
  { term: "PBH", pronunciation: "pee-bee-aitch", slug: GLOSSARY_TERMS.pbh.slug, definition: "Primordial Black Holes. A hypothetical dark-matter candidate. Track A's PBH channel is a measured null — the predicted abundance is 7.0 dex short of a detectable signal." },
  { term: "NANOGrav", pronunciation: "NAN-oh-grav", slug: GLOSSARY_TERMS.nanograv.slug, definition: "North American Nanohertz Observatory for Gravitational Waves. The validated Kohri-Terada kernel prediction sits 14.3 dex below the NANOGrav background — the PTA channel is closed as a null, not a detection." },
  { term: "Autoencoder", pronunciation: "AW-toh-en-KOH-der", slug: GLOSSARY_TERMS.autoencoder.slug, definition: "A neural network trained to reconstruct its input. Objects it cannot reconstruct well may be flagged as candidates, not discoveries. P3 recovers 181 public DESI DR1 TARGETIDs from one frozen historical list, not a detection claim." },
  { term: "Barbero-Immirzi parameter", pronunciation: "bar-BAIR-oh im-EER-zee", slug: GLOSSARY_TERMS["barbero-immirzi"].slug, definition: "Parameter γ_BI = 0.2375 in loop quantum gravity that sets the minimum area quantum. Appears in the ECH action and controls the strength of parity-odd quantum corrections." },
  { term: "Holst term", pronunciation: "holst", slug: GLOSSARY_TERMS["holst-term"].slug, definition: "The parity-odd topological term in the gravitational action, proportional to 1/γ_BI. It produces no classical equations of motion but generates quantum effects including birefringence." },
  { term: "Path-C", pronunciation: "path see", slug: GLOSSARY_TERMS.path_c.slug, definition: "A historic native-retrain quality-gate concept for exploratory anomaly pipelines. These pipeline records are legacy/superseded methodology and do not contribute a current anomaly-catalog headline or evidence for a bounce." },
  { term: "LQC", pronunciation: "el-kyoo-see", slug: GLOSSARY_TERMS.lqc.slug, definition: "Loop Quantum Cosmology. A quantization of cosmological spacetimes where discrete structure at the Planck scale replaces the Big Bang singularity with a quantum bounce — distinct from the ECH/torsion mechanism." },
  { term: "Matter Bounce", pronunciation: "MAT-er bowns", slug: GLOSSARY_TERMS["matter-bounce"].slug, definition: "A bounce cosmology scenario where the contracting phase is dominated by matter-like sources (w ≈ 0). P2 studies a conditional f_NL = -35/16 = -2.1875 prediction; observations have not established that a matter bounce occurred." },
  { term: "PTA", pronunciation: "pee-tee-ay", slug: GLOSSARY_TERMS.pta.slug, definition: "Pulsar Timing Array. A nanohertz gravitational-wave probe (e.g. NANOGrav). Through the validated Kohri-Terada kernel, the program's predicted spectrum is 14.3 dex below the NANOGrav background — the PTA channel is closed as a null." },
  { term: "SIGW", pronunciation: "sig-double-you", slug: GLOSSARY_TERMS.sigw.slug, definition: "Scalar-Induced Gravitational Waves — a gravitational-wave background sourced by second-order scalar perturbations re-entering the horizon. The framework used to compute the PTA-channel null prediction." },
  { term: "kη_B", pronunciation: "kay-eta-bee", slug: GLOSSARY_TERMS["k-eta-b"].slug, definition: "The dimensionless product of wavenumber and bounce-epoch conformal time. It sets the horizon scale at the bounce; bounce-scale enhancement near kη_B ≈ 1 is the one remaining non-null route being investigated for Track A's PTA/PBH channels." },
  { term: "S1 / S2 schemes", pronunciation: "ess-one ess-two", slug: GLOSSARY_TERMS["s1-s2-schemes"].slug, definition: "The two computational schemes tried for the bounce's own cubic transmission term. S1 (series-regular) gives a finite result, Δf_NL^bounce = -(5/24)ρ_B; S2 diverges and is not used." },
  { term: "δN formalism", pronunciation: "delta-en", slug: GLOSSARY_TERMS["delta-n"].slug, definition: "The separate-universe delta-N formalism, used to compute the curvature perturbation from differences in local e-folds across patches — one of the independent methods used to adjudicate the program's f_NL sign and monopole terms." },
  { term: "namaster", pronunciation: "nah-MAS-ter", slug: GLOSSARY_TERMS.namaster.slug, definition: "NaMaster, the pseudo-Cl power-spectrum estimation code. P1B is namaster-proof research software validating the pipeline underlying the program's birefringence measurement, not an MCMC results paper." },
  { term: "Readiness", pronunciation: "red-ee-ness", slug: GLOSSARY_TERMS.readiness.slug, definition: "The Convex-sourced publication-readiness percentage per work: science closure, evidence and reproducibility, automated review convergence, and packaging, plus Houston's final sign-off for the last 5%. Venue, endorsement, and submission are tracked separately and never subtract from this number." },
];

export default function GlossaryPage() {
  return (
    <>
      <PageHeader
        eyebrow="Reference"
        title="Glossary"
        lead={`${entries.length} terms, parameters, and concepts from the BigBounce research program — plain-English first, technical detail second.`}
      />

      <section aria-label="Terms" className="mt-2">
        <dl className="grid grid-cols-1 gap-x-10 gap-y-0 md:grid-cols-2">
          {entries.map((entry) => (
            <div
              key={entry.slug}
              id={`term-${entry.slug}`}
              className="scroll-mt-24 border-t py-4"
              style={{ borderColor: "var(--rule, var(--border))" }}
            >
              <dt className="flex items-baseline gap-2">
                <span
                  className="text-base font-semibold"
                  style={{ fontFamily: "var(--font-mono-stack)" }}
                >
                  {entry.term}
                </span>
                <span className="font-mono text-xs text-muted-foreground">
                  /{entry.pronunciation}/
                </span>
              </dt>
              <dd className="mt-1.5 text-sm leading-relaxed text-muted-foreground">
                {entry.definition}
              </dd>
            </div>
          ))}
        </dl>
      </section>
    </>
  );
}
