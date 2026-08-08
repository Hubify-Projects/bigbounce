import { Card, CardContent } from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import type { Metadata } from"next";

export const metadata: Metadata = {
  title:"Glossary",
  description:
"Key terms, parameters, and equations from the BigBounce research program.",
};

const glossaryEntries = [
  {
    term:"Big Bounce",
    pronunciation:"big bowns",
    definition:
"A cosmological model where the universe transitioned from a contraction phase to expansion through a 'bounce' at finite density, avoiding the Big Bang singularity.",
  },
  {
    term:"f_NL",
    pronunciation:"eff-en-ell",
    definition:
"The amplitude of local primordial non-Gaussianity. P2 derives f_NL = -35/16 = -2.1875 for its stated matter-contraction assumptions. A future SPHEREx measurement may test that conditional prediction; it is not a current bounce detection.",
  },
  {
    term:"Birefringence",
    pronunciation:"by-ree-FRIN-jens",
    definition:
"The rotation of CMB polarization angle β as photons travel through space. Predicted β = 0.27° from ALP field evolution. Current measurement: 0.342° ± 0.094° (3.6σ).",
  },
  {
    term:"Quintom",
    pronunciation:"KWIN-tom",
    definition:
"A dark energy model with both quintessence (w > -1) and phantom (w < -1) fields, allowing the equation of state to cross w = -1. Treated theoretically in our program — Paper 1A's model-discrimination table is explicit that there are zero free-w0–wa samples in our 309,189-sample frozen posterior. External DESI DR2 (Adame et al.) reports 2.8–4.2σ for w-crossing.",
  },
  {
    term:"ECH",
    pronunciation:"ee-see-aitch",
    definition:
"Einstein-Cartan-Holst theory. Extends general relativity with torsion (antisymmetric part of the spacetime connection). A 14-constraint catalog closes the four enumerated minimal-ECH dark-energy routes at the channel level, under stated assumptions.",
  },
  {
    term:"Torsion",
    pronunciation:"TOR-shun",
    definition:
"The antisymmetric part of the spacetime connection. In ECH theory, torsion couples to fermion spin and can prevent gravitational singularities by providing a repulsive force at extreme densities.",
  },
  {
    term:"MCMC",
    pronunciation:"em-see-em-see",
    definition:
"Markov Chain Monte Carlo. A statistical sampling method used to explore parameter spaces. Historic posterior records are research context, not P1B's publication role: P1B is namaster-proof research software.",
  },
  {
    term:"SPHEREx",
    pronunciation:"SFEER-ex",
    definition:
"Spectro-Photometer for the History of the Universe, Epoch of Reionization, and Ices Explorer. NASA mission launching ~2028 that will measure f_NL to σ ≈ 0.7-1.0.",
  },
  {
    term:"σ(f_NL)",
    pronunciation:"sigma of eff-en-ell",
    definition:
"The uncertainty on the f_NL measurement. Current external constraints do not establish P2's conditional matter-contraction prediction. Earlier DESI anomaly-tracer improvement estimates are legacy/superseded pipeline work; the SPHEREx target is prospective.",
  },
  {
    term:"PBH",
    pronunciation:"pee-bee-aitch",
    definition:
"Primordial Black Holes. Hypothetical black holes that could form from early-universe density fluctuations. Their connection to a bounce scenario remains theoretical and is not established by a survey detection.",
  },
  {
    term:"NANOGrav",
    pronunciation:"NAN-oh-grav",
    definition:
"North American Nanohertz Observatory for Gravitational Waves. A historic simplified slope comparison was compatible with a matter-bounce value under its stated model choices. It is legacy context, not a bounce detection or a current portfolio result.",
  },
  {
    term:"Autoencoder",
    pronunciation:"AW-toh-en-KOH-der",
    definition:
"A neural network trained to reconstruct its input. Objects it cannot reconstruct well may be flagged as candidates, not discoveries. BigBounce's historic exploratory pipeline produced archival candidate records; P3 is the integrated Supporting Data Release recovering 181 public DESI DR1 TARGETIDs from one frozen historical list, not a detection claim.",
  },
  {
    term:"Barbero-Immirzi parameter",
    pronunciation:"bar-BAIR-oh im-EER-zee",
    definition:
"Parameter γ_BI = 0.2375 in loop quantum gravity that sets the minimum area quantum. Appears in the ECH action and controls the strength of parity-odd quantum corrections.",
  },
  {
    term:"Holst term",
    pronunciation:"holst",
    definition:
"The parity-odd topological term in the gravitational action, proportional to 1/γ_BI. It produces no classical equations of motion but generates quantum effects including birefringence.",
  },
  {
    term:"Path-C",
    pronunciation:"path see",
    definition:
"A historic native-retrain quality-gate concept for exploratory anomaly pipelines. These pipeline records are legacy/superseded methodology and do not contribute a current anomaly-catalog headline or evidence for a bounce.",
  },
  {
    term:"LQC",
    pronunciation:"el-kyoo-see",
    definition:
"Loop Quantum Cosmology. A quantization of cosmological spacetimes using loop quantum gravity methods, where the discrete structure of space at the Planck scale replaces the Big Bang singularity with a quantum bounce. The bounce is sourced by quantum geometric repulsion, distinct from the ECH/torsion mechanism.",
  },
  {
    term:"Matter Bounce",
    pronunciation:"MAT-er bowns",
    definition:
"A bounce cosmology scenario where the contracting phase is dominated by matter-like sources (w ≈ 0). P2 studies a conditional f_NL = -35/16 = -2.1875 prediction; observations have not established that a matter bounce occurred.",
  },
];

export default function GlossaryPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Reference &middot; {glossaryEntries.length} entries
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Glossary
        </h1>
        <p className="subtitle">
          Key terms, parameters, and concepts from the BigBounce research
          program.
        </p>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>Terms</h2>
        <div className="flex flex-col gap-2">
          {glossaryEntries.map((entry) => (
            <Card key={entry.term}>
              <CardContent className="space-y-1.5 p-4">
                <div className="flex items-baseline gap-2">
                  <span
                    className="text-base font-semibold"
                    style={{ fontFamily:"var(--font-mono-stack)" }}
                  >
                    {entry.term}
                  </span>
                  <span className="font-mono text-xs text-muted-foreground">
                    /{entry.pronunciation}/
                  </span>
                </div>
                <p className="text-sm leading-relaxed text-muted-foreground">
                  {entry.definition}
                </p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>
    </>
  );
}
