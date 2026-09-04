import type { Metadata } from "next";
import { PageHeader } from "@/components/primitives";
import { Term } from "@/lib/glossaryLinks";
import type { ReactNode } from "react";

export const metadata: Metadata = {
  title: "Cosmic Timeline",
  description:
    "A single typographic timeline from the parent universe through the bounce to SPHEREx 2028.",
};

const events: Array<{ time: string; label: string; desc: ReactNode }> = [
  {
    time: "∞ — ?",
    label: "Parent universe",
    desc: "A previous universe contracts under gravity. Density increases toward Planck scale (~10⁹³ g/cm³).",
  },
  {
    time: "t → 0⁻",
    label: "Contraction phase",
    desc: (
      <>
        Matter-dominated contraction. Perturbations grow, imprinting{" "}
        <Term term="f_nl">f_NL</Term> = -35/16 on the bispectrum.{" "}
        <Term term="pbh">PBH</Term> seeds form.
      </>
    ),
  },
  {
    time: "t = 0",
    label: "The bounce",
    desc: (
      <>
        <Term term="torsion">Torsion</Term> (or quantum gravity) prevents a
        singularity. Density reaches maximum but stays finite. Expansion
        begins.
      </>
    ),
  },
  {
    time: "10⁻³⁶ s",
    label: "Post-bounce expansion",
    desc: "Universe expands rapidly. No inflation needed — the contraction phase already solved the horizon and flatness problems.",
  },
  {
    time: "3 min",
    label: "Nucleosynthesis",
    desc: "Light elements form (H, He, Li). Identical to standard cosmology. ΔNeff ≈ 0 confirmed by our MCMC.",
  },
  {
    time: "380,000 yr",
    label: "CMB release",
    desc: (
      <>
        Universe becomes transparent. CMB carries bounce imprint: f_NL,{" "}
        <Term term="birefringence">birefringence</Term> β = 0.27°, spectral
        index.
      </>
    ),
  },
  {
    time: "~1 Gyr",
    label: "First galaxies",
    desc: "Galaxies form from primordial perturbations. BigBounce's historical DESI pipeline records are unreconciled and do not establish a high-redshift population or a bounce connection; the anomaly flagship is being rebuilt.",
  },
  {
    time: "9.8 Gyr",
    label: "Dark energy onset",
    desc: (
      <>
        Dark energy begins dominating expansion. Whether w(z) crosses -1 (
        <Term term="quintom">quintom</Term>-B behavior) is treated
        theoretically in our program; external DESI DR2 (Adame et al.) reports
        2.8-4.2σ for w-crossing depending on dataset combination. Our own
        DESI DR2 w0wa chain (Paper 1B) gives w_pivot = -0.952 ± 0.019, +2.5σ
        from -1.
      </>
    ),
  },
  {
    time: "13.8 Gyr",
    label: "Now (2026)",
    desc: (
      <>
        BigBounce is organized around three research tracks (A: bounce vs.
        inflation flagship, B: the <Term term="ech">ECH</Term> Note closed
        line, C: DESI data products). Track A now reports three honest nulls (
        <Term term="pta">PTA</Term>, <Term term="pbh">PBH</Term>, high-z PNG)
        plus one reachable-but-unseparable LSS channel; final author review
        remains separate from endorsement, submission, and independent peer
        review. <Term term="readiness">Readiness</Term> is tracked live on{" "}
        /status.
      </>
    ),
  },
  {
    time: "2028",
    label: "SPHEREx launch",
    desc: (
      <>
        <Term term="spherex">SPHEREx</Term> is a relevant future probe of
        primordial non-Gaussianity. Whether the paper&apos;s conditional f_NL
        = -35/16 result maps to a survey-level test depends on the stated
        bounce-transmission and covariance assumptions; it would not by
        itself prove a unique bounce origin.
      </>
    ),
  },
  {
    time: "~2032",
    label: "LiteBIRD",
    desc: "JAXA's LiteBIRD will measure birefringence to ~0.03°. Tests β = 0.27° prediction at ~9σ.",
  },
  {
    time: "~2035",
    label: "LISA",
    desc: "ESA's LISA will detect induced gravitational waves from PBH formation. Tests the bounce GW spectrum directly.",
  },
];

export default function TimelinePage() {
  return (
    <>
      <PageHeader
        eyebrow="Visual timeline"
        title="Cosmic timeline"
        lead="From the parent universe through the bounce to SPHEREx 2028 and beyond — one typographic line, no cards."
      />

      <section aria-label="The story of the universe" className="mt-2">
        <ol className="flex flex-col">
          {events.map((event, i) => (
            <li
              key={i}
              className="grid grid-cols-[minmax(84px,auto)_1fr] gap-x-5 gap-y-1 border-t py-4 md:grid-cols-[140px_1fr]"
              style={{ borderColor: "var(--rule, var(--border))" }}
            >
              <span className="mono self-baseline text-xs uppercase tracking-wider text-muted-foreground">
                {event.time}
              </span>
              <div>
                <p
                  className="text-base font-semibold"
                  style={{ fontFamily: "var(--font-mono-stack)" }}
                >
                  {event.label}
                </p>
                <p className="mt-1 text-sm leading-relaxed text-muted-foreground">
                  {event.desc}
                </p>
              </div>
            </li>
          ))}
        </ol>
      </section>
    </>
  );
}
