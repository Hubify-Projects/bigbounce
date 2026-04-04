import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Speculations",
  description: "Future research directions spanning dark energy, black holes, SETI, and particle physics.",
};

interface SpecCardProps {
  title: string;
  children: React.ReactNode;
  tag: string;
}

function SpecCard({ title, children, tag }: SpecCardProps) {
  return (
    <div className="card" style={{ borderLeft: "4px solid #7c3aed" }}>
      <h4 style={{ margin: "0 0 8px" }}>{title}</h4>
      <p style={{ margin: "0 0 8px", fontSize: 15, lineHeight: 1.7 }}>{children}</p>
      <div style={{ fontSize: 12, color: "var(--text-tertiary)" }}>{tag}</div>
    </div>
  );
}

function DomainHeader({ children, className }: { children: React.ReactNode; className: string }) {
  return (
    <div style={{ marginTop: 40, padding: "12px 20px", borderRadius: 8, fontSize: 13, letterSpacing: 1, textTransform: "uppercase" as const, fontWeight: 600 }} className={className}>
      {children}
    </div>
  );
}

export default function SpeculationsPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>Living Document &middot; Updated April 2026</p>
        <h1>Speculations</h1>
        <p className="subtitle">
          Future research paths, wild ideas, and things we want to build.
        </p>
      </div>

      <hr />

      <section className="section">
        <h2>Cosmology &amp; Dark Energy</h2>
        <SpecCard title="What Is Dark Energy?" tag="ACTIONABLE · w0-wa MCMC · DESI DR2 · Quintom">
          73% of the universe is dark energy. Our quintom bounce CAN unify bounce + dark energy through phantom fields. Our MCMC confirms w-crossing at 98.6%.
        </SpecCard>
        <SpecCard title="f_NL = −35/8: The Decisive Test" tag="ACTIONABLE (forecast) · SPHEREx ~2028 · Parameter-free">
          SPHEREx will measure primordial non-Gaussianity to σ ≈ 1. Our prediction is −4.375, parameter-free. Inflation predicts |f_NL| &lt; 1. One measurement, one answer.
        </SpecCard>
        <SpecCard title="What Is Dark Matter?" tag="Future · LISA ~2035 · PBH dark matter">
          The asymmetric matter bounce can produce asteroid-mass primordial black holes as dark matter candidates. Our f_NL naturally regulates PBH abundance.
        </SpecCard>
      </section>

      <section className="section">
        <h2>Black Holes &amp; Extreme Gravity</h2>
        <SpecCard title="GW Echoes from Black Hole Mergers" tag="ACTIONABLE · LIGO O4 data · Cai & Zhu 2026">
          If black hole interiors contain baby universes, mergers might produce gravitational wave echoes. LIGO/Virgo/KAGRA could detect these in existing data.
        </SpecCard>
        <SpecCard title="Supermassive Black Hole Formation" tag="ACTIONABLE · JWST data · Cross-match with anomaly catalog">
          JWST found SMBHs at z &gt; 10 that are too massive too early. PBHs from a bounce-era transition could seed them. Our anomaly catalog might contain their host galaxies.
        </SpecCard>
      </section>

      <section className="section">
        <h2>Astrophysics &amp; Discovery</h2>
        <SpecCard title="195,829 Uncharacterized Objects" tag="ACTIONABLE · Enhanced 22.5M · Paper 3">
          Our AI pipeline found objects absent from every major catalog. What ARE they? Full classification underway.
        </SpecCard>
        <SpecCard title="Galaxy Morphology: What Shapes Don't Fit?" tag="ACTIONABLE · Legacy Survey cutouts · Image autoencoder">
          An autoencoder on galaxy images could find unusual morphologies: double nuclei, tidal tails, ring galaxies, or entirely novel structures.
        </SpecCard>
        <SpecCard title="Time-Domain: What Changed?" tag="ACTIONABLE · NEOWISE/unTimely · ZTF · $200-400">
          Cross-matching spectral anomalies with variability data finds objects that are BOTH spectrally AND temporally unusual — the strongest discovery candidates.
        </SpecCard>
      </section>

      <section className="section">
        <h2>Search for Extraterrestrial Intelligence</h2>
        <SpecCard title="Dyson Spheres at Scale" tag="ACTIONABLE · Gaia DR3 + AllWISE · IR excess detection">
          A Dyson sphere would create anomalous IR excess. Prior searches found 7 candidates from 5M stars. We could search 100x more with our pipeline.
        </SpecCard>
        <SpecCard title="FRB Anomaly Detection" tag="Future · CHIME/FRB catalog · Time-series autoencoder">
          Fast radio bursts from cosmological distances — our anomaly detection approach on FRB properties could identify subpopulations that current classification misses.
        </SpecCard>
      </section>

      <section className="section">
        <h2>Particle Physics</h2>
        <SpecCard title="LHC Anomaly Detection" tag="Future · LHC Run 3 · CMS/ATLAS open data">
          An unsupervised autoencoder on collision events could find signatures that don&apos;t match ANY Standard Model prediction — new particles hiding in plain sight.
        </SpecCard>
        <SpecCard title="Spacetime Fabric: Discrete or Continuous?" tag="Testable · Fermi-LAT �� CTA ~2027">
          LQG predicts discrete spacetime producing energy-dependent photon speeds. Our birefringence prediction is another test of spacetime microstructure.
        </SpecCard>
      </section>

      <section className="section">
        <h2>Frontier &amp; Cross-Domain</h2>
        <SpecCard title="Multi-Messenger Astronomy" tag="ACTIONABLE · Cross-survey architecture exists">
          Combining anomalies across electromagnetic + GW + neutrino data simultaneously. An object anomalous in 2+ surveys is the strongest discovery candidate.
        </SpecCard>
        <SpecCard title="The Hubify Lab Scaling Vision" tag="ACTIONABLE · This is the plan">
          Run anomaly detection on every major public dataset simultaneously. 5+ papers and 10+ public data releases within 12 months. See The Window article.
        </SpecCard>
      </section>
    </>
  );
}
