import { Card, CardContent } from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import type { Metadata } from"next";
import type { CSSProperties } from"react";

export const metadata: Metadata = {
  title:"Cosmic Timeline",
  description:
"Visual timeline from the parent universe through the bounce to SPHEREx 2028.",
};

const events: Array<{
  time: string;
  label: string;
  desc: string;
  color: string;
}> = [
  {
    time:"∞ — ?",
    label:"Parent Universe",
    desc:"A previous universe contracts under gravity. Density increases toward Planck scale (~10⁹³ g/cm³).",
    color:"var(--text-tertiary)",
  },
  {
    time:"t → 0⁻",
    label:"Contraction Phase",
    desc:"Matter-dominated contraction. Perturbations grow, imprinting f_NL = -35/16 on the bispectrum. PBH seeds form.",
    color:"#8d806b",
  },
  {
    time:"t = 0",
    label:"THE BOUNCE",
    desc:"Torsion (or quantum gravity) prevents singularity. Density reaches maximum but stays finite. Expansion begins.",
    color:"var(--crit)",
  },
  {
    time:"10⁻³⁶ s",
    label:"Post-Bounce Expansion",
    desc:"Universe expands rapidly. No inflation needed — the contraction phase already solved the horizon and flatness problems.",
    color:"#8f6a2f",
  },
  {
    time:"3 min",
    label:"Nucleosynthesis",
    desc:"Light elements form (H, He, Li). Identical to standard cosmology. ΔNeff ≈ 0 confirmed by our MCMC.",
    color:"var(--accent)",
  },
  {
    time:"380,000 yr",
    label:"CMB Release",
    desc:"Universe becomes transparent. CMB carries bounce imprint: f_NL, birefringence β = 0.27°, spectral index.",
    color:"var(--accent)",
  },
  {
    time:"~1 Gyr",
    label:"First Galaxies",
    desc:"Galaxies form from bounce-era perturbations. Our 195K DESI anomalies trace structure at z > 2.",
    color:"#9c927e",
  },
  {
    time:"9.8 Gyr",
    label:"Dark Energy Onset",
    desc:"Dark energy begins dominating expansion. Whether w(z) crosses -1 (quintom-B behavior) is treated theoretically in our program; external DESI DR2 (Adame et al.) reports 2.8–4.2σ for w-crossing depending on dataset combination. Our own DESI DR2 w0wa chain (Paper 1B) gives w_pivot = −0.952 ± 0.019, +2.5σ from −1.",
    color:"#9c927e",
  },
  {
    time:"13.8 Gyr",
    label:"NOW (2026)",
    desc:"BigBounce research program: 6 papers, 8 surveys, 37.3M sources, 378,280 anomalies, 309,189 frozen MCMC samples, 8.47M-galaxy chirality catalog. 20+ review rounds complete (latest INT-M2, 2026-06-30) — MINOR-dominant with occasional ACCEPTs, 0 unaddressed genuine findings; readiness 96; awaiting author sign-off → coordinated arXiv drop.",
    color:"var(--text-secondary)",
  },
  {
    time:"2028",
    label:"SPHEREx Launch",
    desc:"NASA's SPHEREx will measure f_NL to σ ≈ 0.7–1.0. If f_NL ≈ -2.1875: bounce confirmed at >4σ.",
    color:"var(--text-secondary)",
  },
  {
    time:"~2032",
    label:"LiteBIRD",
    desc:"JAXA's LiteBIRD will measure birefringence to ~0.03°. Tests β = 0.27° prediction at ~9σ.",
    color:"var(--text-tertiary)",
  },
  {
    time:"~2035",
    label:"LISA",
    desc:"ESA's LISA will detect induced gravitational waves from PBH formation. Tests bounce GW spectrum directly.",
    color:"var(--text-tertiary)",
  },
];

export default function TimelinePage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Visual Timeline
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Cosmic Timeline
        </h1>
        <p className="subtitle">
          From the parent universe through the bounce to SPHEREx 2028 and
          beyond.
        </p>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>The Story of the Universe</h2>
        <div className="relative pl-12">
          <div className="absolute left-[21px] top-3 bottom-3 w-px bg-border" />
          <div className="flex flex-col gap-4">
            {events.map((event, i) => (
              <div key={i} className="relative">
                <span
                  className="timeline-dot absolute -left-[33px] top-4 h-3 w-3 rounded-full border-2"
                  style={{
                    "--timeline-tone": event.color,
                    borderColor:"var(--bg)",
                  } as CSSProperties}
                />
                <Card>
                  <CardContent className="space-y-1.5 p-4">
                    <div className="font-mono text-xs uppercase tracking-wider text-muted-foreground">
                      {event.time}
                    </div>
                    <div
                      className="text-base font-semibold"
                      style={{ fontFamily:"var(--font-mono-stack)" }}
                    >
                      {event.label}
                    </div>
                    <p className="text-sm leading-relaxed text-muted-foreground">
                      {event.desc}
                    </p>
                  </CardContent>
                </Card>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
