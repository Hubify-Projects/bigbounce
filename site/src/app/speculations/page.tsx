import { Badge } from"@/components/ui/badge";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import type { Metadata } from"next";

export const metadata: Metadata = {
  title:"Speculations",
  description:
"Future research directions spanning dark energy, black holes, SETI, and particle physics.",
};

interface SpecCardProps {
  title: string;
  children: React.ReactNode;
  tag: string;
}

function SpecCard({ title, children, tag }: SpecCardProps) {
  return (
    <Card className="border-l-4 border-tone-muted">
      <CardHeader className="pb-2">
        <CardTitle
          className="text-base"
          style={{ fontFamily:"var(--font-mono-stack)" }}
        >
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-sm leading-relaxed text-muted-foreground">
          {children}
        </p>
      </CardContent>
      <CardFooter className="pt-0">
        <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
          {tag}
        </span>
      </CardFooter>
    </Card>
  );
}

const sections: Array<{
  heading: string;
  badge: string;
  cards: SpecCardProps[];
}> = [
  {
    heading:"Cosmology & Dark Energy",
    badge:"Cosmology",
    cards: [
      {
        title:"What Is Dark Energy?",
        tag:"ACTIONABLE · w0-wa MCMC · DESI DR2 · Quintom",
        children:
"73% of the universe is dark energy. The quintom branch of bounce cosmology can unify bounce + dark energy through phantom fields, predicting w-crossing (quintom-B). External DESI DR2 (Adame et al.) reports 2.8–4.2σ for w-crossing. Our own program treats this theoretically — Paper 1 §VII.H is explicit that there are zero free-w0–wa samples in our 309,789-sample posterior. The actionable next step is standing up an in-house quintom MCMC.",
      },
      {
        title:"f_NL = −35/8: The Decisive Test",
        tag:"ACTIONABLE (forecast) · SPHEREx ~2028 · Parameter-free",
        children:
"SPHEREx will measure primordial non-Gaussianity to σ ≈ 1. Our prediction is −4.375, parameter-free. Inflation predicts |f_NL| < 1. One measurement, one answer.",
      },
      {
        title:"What Is Dark Matter?",
        tag:"Future · LISA ~2035 · PBH dark matter",
        children:
"The asymmetric matter bounce can produce asteroid-mass primordial black holes as dark matter candidates. Our f_NL naturally regulates PBH abundance.",
      },
    ],
  },
  {
    heading:"Black Holes & Extreme Gravity",
    badge:"Black Holes",
    cards: [
      {
        title:"GW Echoes from Black Hole Mergers",
        tag:"ACTIONABLE · LIGO O4 data · Cai & Zhu 2026",
        children:
"If black hole interiors contain baby universes, mergers might produce gravitational wave echoes. LIGO/Virgo/KAGRA could detect these in existing data.",
      },
      {
        title:"Supermassive Black Hole Formation",
        tag:"ACTIONABLE · JWST data · Cross-match with anomaly catalog",
        children:
"JWST found SMBHs at z > 10 that are too massive too early. PBHs from a bounce-era transition could seed them. Our anomaly catalog might contain their host galaxies.",
      },
    ],
  },
  {
    heading:"Astrophysics & Discovery",
    badge:"Astrophysics",
    cards: [
      {
        title:"195,829 Uncharacterized Objects",
        tag:"ACTIONABLE · Enhanced 22.5M · Paper 3",
        children:
"Our AI pipeline found objects absent from every major catalog. What ARE they? Full classification underway.",
      },
      {
        title:"Galaxy Morphology: What Shapes Don't Fit?",
        tag:"ACTIONABLE · Legacy Survey cutouts · Image autoencoder",
        children:
"An autoencoder on galaxy images could find unusual morphologies: double nuclei, tidal tails, ring galaxies, or entirely novel structures.",
      },
      {
        title:"Time-Domain: What Changed?",
        tag:"ACTIONABLE · NEOWISE/unTimely · ZTF · $200-400",
        children:
"Cross-matching spectral anomalies with variability data finds objects that are BOTH spectrally AND temporally unusual — the strongest discovery candidates.",
      },
    ],
  },
  {
    heading:"Search for Extraterrestrial Intelligence",
    badge:"SETI",
    cards: [
      {
        title:"Dyson Spheres at Scale",
        tag:"ACTIONABLE · Gaia DR3 + AllWISE · IR excess detection",
        children:
"A Dyson sphere would create anomalous IR excess. Prior searches found 7 candidates from 5M stars. We could search 100x more with our pipeline.",
      },
      {
        title:"FRB Anomaly Detection",
        tag:"Future · CHIME/FRB catalog · Time-series autoencoder",
        children:
"Fast radio bursts from cosmological distances — our anomaly detection approach on FRB properties could identify subpopulations that current classification misses.",
      },
    ],
  },
  {
    heading:"Particle Physics",
    badge:"Particle Physics",
    cards: [
      {
        title:"LHC Anomaly Detection",
        tag:"Future · LHC Run 3 · CMS/ATLAS open data",
        children:
"An unsupervised autoencoder on collision events could find signatures that don't match ANY Standard Model prediction — new particles hiding in plain sight.",
      },
      {
        title:"Spacetime Fabric: Discrete or Continuous?",
        tag:"Testable · Fermi-LAT · CTA ~2027",
        children:
"LQG predicts discrete spacetime producing energy-dependent photon speeds. Our birefringence prediction is another test of spacetime microstructure.",
      },
    ],
  },
  {
    heading:"Frontier & Cross-Domain",
    badge:"Frontier",
    cards: [
      {
        title:"Multi-Messenger Astronomy",
        tag:"ACTIONABLE · Cross-survey architecture exists",
        children:
"Combining anomalies across electromagnetic + GW + neutrino data simultaneously. An object anomalous in 2+ surveys is the strongest discovery candidate.",
      },
      {
        title:"The Hubify Lab Scaling Vision",
        tag:"ACTIONABLE · This is the plan",
        children:
"Run anomaly detection on every major public dataset simultaneously. 5+ papers and 10+ public data releases within 12 months. See The Window article.",
      },
    ],
  },
];

export default function SpeculationsPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Living Document &middot; Updated June 2026
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Speculations
        </h1>
        <p className="subtitle">
          Future research paths, wild ideas, and things we want to build.
        </p>
      </div>

      <Separator className="my-8" />

      {sections.map((section) => (
        <section key={section.heading} className="section">
          <div className="mb-4 flex items-center gap-3">
            <h2 className="m-0">{section.heading}</h2>
            <Badge variant="outline">{section.badge}</Badge>
          </div>
          <div className="grid gap-3 md:grid-cols-2">
            {section.cards.map((card) => (
              <SpecCard key={card.title} title={card.title} tag={card.tag}>
                {card.children}
              </SpecCard>
            ))}
          </div>
        </section>
      ))}
    </>
  );
}
