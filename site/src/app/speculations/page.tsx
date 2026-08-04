import { Badge } from"@/components/ui/badge";
import { Separator } from"@/components/ui/separator";
import type { Metadata } from"next";

export const metadata: Metadata = {
  title: "Speculations",
  description:
    "Future research directions spanning dark energy, black holes, SETI, and particle physics.",
};

interface SpecItemProps {
  title: string;
  children: React.ReactNode;
  tag: string;
}

function SpecItem({ title, children, tag }: SpecItemProps) {
  return (
    <div className="py-4">
      <p
        className="font-semibold text-sm mb-1"
        style={{ fontFamily: "var(--font-mono-stack)" }}
      >
        {title}
      </p>
      <p className="text-sm leading-relaxed text-muted-foreground mb-2">
        {children}
      </p>
      <span className="font-mono text-[10px] uppercase tracking-wider text-muted-foreground opacity-70">
        {tag}
      </span>
    </div>
  );
}

const sections: Array<{
  heading: string;
  badge: string;
  cards: SpecItemProps[];
}> = [
  {
    heading:"Cosmology & Dark Energy",
    badge:"Cosmology",
    cards: [
      {
        title:"What Is Dark Energy?",
        tag:"ACTIONABLE · w0-wa MCMC · DESI DR2 · Quintom",
        children:
"The quintom branch of bounce cosmology is a theoretical possibility that predicts w-crossing. External DESI analyses are not a BigBounce result, and our program has not run a free-w0–wa analysis. P1B is namaster-proof research software, not an MCMC paper. The actionable next step would be a separately scoped in-house analysis.",
      },
      {
        title:"fNL = −35/16: The Decisive Test",
        tag:"ACTIONABLE (forecast) · SPHEREx ~2028 · Parameter-free",
        children:
"P2 derives a conditional matter-contraction prediction fNL = −2.1875. SPHEREx may provide a future test, but no present measurement proves a bounce or resolves the model landscape by itself.",
      },
      {
        title:"What Is Dark Matter?",
        tag:"Future · LISA ~2035 · PBH dark matter",
        children:
"Some bounce scenarios motivate asteroid-mass primordial black holes as dark-matter candidates. This remains a theoretical research direction, not a conclusion from the program's surveys or current artifacts.",
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
"Early massive black holes motivate several formation hypotheses, including speculative primordial seeds. The legacy anomaly archive is not a discovery catalog and should not be treated as evidence for any such mechanism.",
      },
    ],
  },
  {
    heading:"Astrophysics & Discovery",
    badge:"Astrophysics",
    cards: [
      {
        title:"Exploratory anomaly candidates",
        tag:"SPECULATIVE · autoencoder pipeline candidates",
        children:
"Historic exploratory autoencoder runs flagged archival candidates for possible follow-up. They are not confirmed detections and are now legacy/superseded pipeline records. P3 is the integrated Supporting Data Release recovering 181 DESI DR1 TARGETIDs from a frozen historical list, not a standalone discovery claim.",
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
"A future cross-match could identify candidates that are unusual in more than one modality. Such candidates would still require independent validation and would not by themselves support a bounce claim.",
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
"Combining heterogeneous data could prioritize future follow-up candidates. Agreement across pipelines is not a discovery confirmation or evidence for a bounce without independent validation.",
      },
      {
        title:"The Hubify Lab Scaling Vision",
        tag:"ACTIONABLE · This is the plan",
        children:
"Build reproducible discovery infrastructure around explicit parent-catalog, model, score, and selection lineage. Any future outputs should be scoped as question-first programs rather than a paper-count target.",
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
          <div className="flat-item-list">
            {section.cards.map((card) => (
              <SpecItem key={card.title} title={card.title} tag={card.tag}>
                {card.children}
              </SpecItem>
            ))}
          </div>
        </section>
      ))}
    </>
  );
}
