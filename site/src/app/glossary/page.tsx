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
"Markov Chain Monte Carlo. A statistical sampling method used to explore parameter spaces. We have 309,189 frozen posterior samples across 2 converged dataset combinations (176,240 full-tension + 132,949 Planck+BAO+SN), with a third Planck-only combination accumulating.",
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
"The uncertainty on the f_NL measurement. Current combined: σ ≈ 4.1 (external). Our DESI multi-tracer central forecast: 9.4% improvement, consistent with none at <1σ. SPHEREx target: σ ≈ 0.7-1.0.",
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
"North American Nanohertz Observatory for Gravitational Waves. Detected a gravitational wave background; our real-KDE free-spectrum re-fit gives spectral index γ = 2.567 ± 0.382. Bounce predicts γ = 3.0 (consistent at -1.13σ); SMBHB γ = 4.33 is excluded at -4.6σ.",
  },
  {
    term:"Autoencoder",
    pronunciation:"AW-toh-en-KOH-der",
    definition:
"A neural network trained to reconstruct its input. Objects it can't reconstruct well are anomalous. Used to find 378,280 unique anomalies across 37.3M sources in 8 surveys (Paper 3 canonical Path-C totals after native retrains and 5″ dedup).",
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
"The native-retrain quality gate used in Paper 3. Each survey must pass two criteria: val_loss ≤ 0.30 on native training data AND ≥50% injection-recovery at 5σ. Surveys that fail are quarantined (e.g., ACT DR6) and contribute zero objects to the canonical anomaly catalog headline.",
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
"A bounce cosmology scenario where the contracting phase is dominated by matter-like sources (w ≈ 0). Generates a nearly scale-invariant spectrum of perturbations and the parameter-free prediction f_NL = -35/8 = -4.375, which is mechanism-independent across all matter bounce variants.",
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
