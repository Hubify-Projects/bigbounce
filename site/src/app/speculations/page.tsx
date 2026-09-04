import type { Metadata } from "next";
import { Band, PageHeader } from "@/components/primitives";
import type { ReactNode } from "react";

export const metadata: Metadata = {
  title: "Speculations",
  description:
    "Future research directions spanning dark energy, black holes, SETI, and particle physics — clearly labeled as speculation, not results.",
};

interface SpecItemProps {
  title: string;
  children: ReactNode;
  tag: string;
}

function SpecItem({ title, children, tag }: SpecItemProps) {
  return (
    <div className="py-4">
      <p
        className="mb-1 text-sm font-semibold"
        style={{ fontFamily: "var(--font-mono-stack)" }}
      >
        {title}
      </p>
      <p className="mb-2 text-sm leading-relaxed text-muted-foreground">
        {children}
      </p>
      <span className="mono text-[10px] uppercase tracking-wider text-muted-foreground opacity-70">
        {tag}
      </span>
    </div>
  );
}

const sections: Array<{ heading: string; cards: SpecItemProps[] }> = [
  {
    heading: "Cosmology & dark energy",
    cards: [
      {
        title: "What is dark energy?",
        tag: "actionable · w0-wa MCMC · DESI DR2 · quintom",
        children:
          "The quintom branch of bounce cosmology is a theoretical possibility that predicts w-crossing. External DESI analyses are not a BigBounce result, and our program has not run a free-w0-wa analysis. P1B is namaster-proof research software, not an MCMC paper. The actionable next step would be a separately scoped in-house analysis.",
      },
      {
        title: "f_NL = -35/16: a conditional future test",
        tag: "actionable (forecast) · SPHEREx ~2028 · scoped assumptions",
        children:
          "P2 derives a conditional matter-contraction prediction f_NL = -2.1875. SPHEREx may provide a future test, but no present measurement proves a bounce or resolves the model landscape by itself.",
      },
      {
        title: "What is dark matter?",
        tag: "future · LISA ~2035 · PBH dark matter",
        children:
          "Some bounce scenarios motivate asteroid-mass primordial black holes as dark-matter candidates. This remains a theoretical research direction, not a conclusion from the program's surveys or current artifacts.",
      },
    ],
  },
  {
    heading: "Black holes & extreme gravity",
    cards: [
      {
        title: "GW echoes from black hole mergers",
        tag: "actionable · LIGO O4 data · Cai & Zhu 2026",
        children:
          "If black hole interiors contain baby universes, mergers might produce gravitational wave echoes. LIGO/Virgo/KAGRA could detect these in existing data.",
      },
      {
        title: "Supermassive black hole formation",
        tag: "actionable · JWST data · cross-match with anomaly catalog",
        children:
          "Early massive black holes motivate several formation hypotheses, including speculative primordial seeds. The legacy anomaly archive is not a discovery catalog and should not be treated as evidence for any such mechanism.",
      },
    ],
  },
  {
    heading: "Astrophysics & discovery",
    cards: [
      {
        title: "Exploratory anomaly candidates",
        tag: "speculative · autoencoder pipeline candidates",
        children:
          "Historic exploratory autoencoder runs flagged archival candidates for possible follow-up. They are not confirmed detections and are now legacy/superseded pipeline records. P3 is the integrated Supporting Data Release recovering 181 DESI DR1 TARGETIDs from a frozen historical list, not a standalone discovery claim.",
      },
      {
        title: "Galaxy morphology: what shapes don't fit?",
        tag: "actionable · Legacy Survey cutouts · image autoencoder",
        children:
          "An autoencoder on galaxy images could find unusual morphologies: double nuclei, tidal tails, ring galaxies, or entirely novel structures.",
      },
      {
        title: "Time-domain: what changed?",
        tag: "actionable · NEOWISE/unTimely · ZTF · $200-400",
        children:
          "A future cross-match could identify candidates that are unusual in more than one modality. Such candidates would still require independent validation and would not by themselves support a bounce claim.",
      },
    ],
  },
  {
    heading: "Search for extraterrestrial intelligence",
    cards: [
      {
        title: "Dyson spheres at scale",
        tag: "actionable · Gaia DR3 + AllWISE · IR excess detection",
        children:
          "A Dyson sphere would create anomalous IR excess. Prior searches found 7 candidates from 5M stars. We could search 100x more with our pipeline.",
      },
      {
        title: "FRB anomaly detection",
        tag: "future · CHIME/FRB catalog · time-series autoencoder",
        children:
          "Fast radio bursts from cosmological distances — our anomaly detection approach on FRB properties could identify subpopulations that current classification misses.",
      },
    ],
  },
  {
    heading: "Particle physics",
    cards: [
      {
        title: "LHC anomaly detection",
        tag: "future · LHC Run 3 · CMS/ATLAS open data",
        children:
          "An unsupervised autoencoder on collision events could find signatures that don't match any Standard Model prediction — new particles hiding in plain sight.",
      },
      {
        title: "Spacetime fabric: discrete or continuous?",
        tag: "testable · Fermi-LAT · CTA ~2027",
        children:
          "LQG predicts discrete spacetime producing energy-dependent photon speeds. Our birefringence prediction is another test of spacetime microstructure.",
      },
    ],
  },
  {
    heading: "Frontier & cross-domain",
    cards: [
      {
        title: "Multi-messenger astronomy",
        tag: "actionable · cross-survey architecture exists",
        children:
          "Combining heterogeneous data could prioritize future follow-up candidates. Agreement across pipelines is not a discovery confirmation or evidence for a bounce without independent validation.",
      },
      {
        title: "The Hubify lab scaling vision",
        tag: "actionable · this is the plan",
        children:
          "Build reproducible discovery infrastructure around explicit parent-catalog, model, score, and selection lineage. Any future outputs should be scoped as question-first programs rather than a paper-count target.",
      },
    ],
  },
];

export default function SpeculationsPage() {
  return (
    <>
      <PageHeader
        eyebrow="Living document · updated June 2026"
        title="Speculations"
        lead="Future research paths and wild ideas we want to build. This page is not results — every entry below is a direction to investigate, not a finding, and none of it changes the readiness or evidence grade of any published work."
      />

      <Band tone="deep" width="content" className="my-6">
        <p className="py-3 text-sm font-medium">
          Not yet formal work. Nothing on this page is a claim, a measurement,
          or a result — see /research and /papers for those. This is the
          program's open idea backlog.
        </p>
      </Band>

      {sections.map((section) => (
        <section key={section.heading} className="section">
          <h2>{section.heading}</h2>
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
