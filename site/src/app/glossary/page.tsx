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
"The amplitude of local primordial non-Gaussianity. The matter bounce predicts f_NL = -35/8 = -4.375, parameter-free. Inflation predicts |f_NL| < 1. SPHEREx will measure this.",
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
"A dark energy model with both quintessence (w > -1) and phantom (w < -1) fields, allowing the equation of state to cross w = -1. Treated theoretically in our program — Paper 1 §VII.H is explicit that there are zero free-w0–wa samples in our 309,789-sample posterior. External DESI DR2 (Adame et al.) reports 2.8–4.2σ for w-crossing.",
  },
  {
    term:"ECH",
    pronunciation:"ee-see-aitch",
    definition:
"Einstein-Cartan-Holst theory. Extends general relativity with torsion (antisymmetric part of the spacetime connection). 14 structural barriers close ECH-specific routes to dark energy.",
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
"Markov Chain Monte Carlo. A statistical sampling method used to explore parameter spaces. We have 424,781+ frozen posterior samples across 3 dataset combinations (176,840 + 132,949 + 114,992).",
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
"The uncertainty on the f_NL measurement. Current combined: σ ≈ 4.1. Our multi-tracer improvement: 6.1%. SPHEREx target: σ ≈ 0.7-1.0.",
  },
  {
    term:"PBH",
    pronunciation:"pee-bee-aitch",
    definition:
"Primordial Black Holes. Formed from density fluctuations in the early universe. The matter bounce f_NL = -35/8 naturally regulates PBH abundance, preventing overproduction.",
  },
  {
    term:"NANOGrav",
    pronunciation:"NAN-oh-grav",
    definition:
"North American Nanohertz Observatory for Gravitational Waves. Detected a gravitational wave background with spectral index γ = 3.2 ± 0.6. Bounce predicts γ = 3.0 (0.48σ consistent against the v2b Fisher recompute).",
  },
  {
    term:"Autoencoder",
    pronunciation:"AW-toh-en-KOH-der",
    definition:
"A neural network trained to reconstruct its input. Objects it can't reconstruct well are anomalous. Used to find 319,443 anomalies across 37,292,042 sources in 8 surveys (Paper 3 Table 1 canonical totals after eROSITA top-cut).",
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
