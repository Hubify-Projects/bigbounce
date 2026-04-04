import { StatCard } from "@/components/Cards/StatCard";
import { Badge } from "@/components/Cards/Badge";
import { DiscoveryCard } from "@/components/Cards/DiscoveryCard";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Research Status",
  description:
    "Master status page: papers, pipelines, MCMC chains, compute pods, and discoveries.",
};

export default function StatusPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Last Updated: April 4, 2026
        </p>
        <h1>Research Program Status</h1>
        <p className="subtitle">
          Comprehensive source of truth for the entire BigBounce spin-torsion
          cosmology research program.
        </p>
      </div>

      <hr />

      {/* Top-level stats */}
      <div className="grid grid-4" style={{ margin: "20px 0" }}>
        <StatCard value="4" label="Papers" color="green" />
        <StatCard value="475K+" label="MCMC Samples" color="green" />
        <StatCard value="33.5M+" label="Sources Scored (8 Surveys)" color="green" />
        <StatCard value="328K+" label="Anomalies Found" color="green" />
        <StatCard value="6" label="AI Pipelines" color="blue" />
        <StatCard value="14" label="Computation Scripts" color="blue" />
        <StatCard value="6" label="Bounce Channels" color="amber" />
      </div>

      <hr />

      <section className="section">
        <h2>1. Research Papers</h2>
        <table>
          <thead>
            <tr>
              <th>Paper</th>
              <th>Title</th>
              <th>Status</th>
              <th>Pages</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Paper 1</strong></td>
              <td>Spin-Torsion Framework: 14 Barriers, Falsifiable Predictions</td>
              <td><Badge variant="green">99% Ready</Badge></td>
              <td>~24</td>
            </tr>
            <tr>
              <td><strong>Paper 2</strong></td>
              <td>
                f<sub>NL</sub> = -35/8 Forecast: SPHEREx Discrimination
              </td>
              <td><Badge variant="green">Submission-Ready</Badge></td>
              <td>~12</td>
            </tr>
            <tr>
              <td><strong>Paper 3</strong></td>
              <td>Multi-Survey Anomaly Catalog: 328K from 33.5M Sources</td>
              <td><Badge variant="blue">Draft (~95%)</Badge></td>
              <td>~18</td>
            </tr>
            <tr>
              <td><strong>Paper 4</strong></td>
              <td>Galaxy Chirality at Scale: 8.47M Galaxies</td>
              <td><Badge variant="blue">Draft (~85%)</Badge></td>
              <td>~11</td>
            </tr>
          </tbody>
        </table>
      </section>

      <section className="section">
        <h2>2. Bounce Cosmology Portfolio</h2>
        <table>
          <thead>
            <tr>
              <th>Channel</th>
              <th>Best Model</th>
              <th>Prediction</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <strong>
                  Galaxy bispectrum f<sub>NL</sub>
                </strong>
              </td>
              <td>Matter bounce</td>
              <td>
                f<sub>NL</sub> = -35/8 (parameter-free)
              </td>
              <td><Badge variant="purple">FLAGSHIP</Badge></td>
            </tr>
            <tr>
              <td><strong>Quintom bounce-DE</strong></td>
              <td>Quintom bounce</td>
              <td>w(z) crosses -1</td>
              <td><Badge variant="green">2.3&sigma; confirmed</Badge></td>
            </tr>
            <tr>
              <td><strong>NANOGrav GW</strong></td>
              <td>Matter bounce</td>
              <td>&gamma; = 3.0 vs 3.2 &plusmn; 0.6</td>
              <td><Badge variant="green">1&sigma; consistent</Badge></td>
            </tr>
            <tr>
              <td><strong>PBH dark matter</strong></td>
              <td>Asymmetric matter bounce</td>
              <td>Asteroid-mass PBHs</td>
              <td><Badge variant="amber">Viable</Badge></td>
            </tr>
          </tbody>
        </table>
      </section>

      <section className="section">
        <h2>3. Completed Surveys (8 total)</h2>
        <table>
          <thead>
            <tr>
              <th>Survey</th>
              <th>Sources</th>
              <th>Anomalies</th>
              <th>QC Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>DESI DR1</strong></td>
              <td>22.5M spectra</td>
              <td>195,829 (0.87%)</td>
              <td><Badge variant="green">PASS</Badge></td>
            </tr>
            <tr>
              <td><strong>SDSS DR18</strong></td>
              <td>2.3M spectra</td>
              <td>77,905 (3.4%)</td>
              <td>
                <Badge variant="amber">Caution: domain shift</Badge>
              </td>
            </tr>
            <tr>
              <td><strong>LAMOST DR10</strong></td>
              <td>11.4M spectra</td>
              <td>44,075 (0.39%)</td>
              <td>
                <Badge variant="amber">Caution: blue-excess bias</Badge>
              </td>
            </tr>
            <tr>
              <td><strong>eROSITA DR1</strong></td>
              <td>930K X-ray</td>
              <td>9,303 (1%)</td>
              <td><Badge variant="green">PASS</Badge></td>
            </tr>
            <tr>
              <td><strong>Planck CMB</strong></td>
              <td>20K patches</td>
              <td>200</td>
              <td>
                <Badge variant="red">QC FAIL: galactic contamination</Badge>
              </td>
            </tr>
            <tr>
              <td><strong>ACT DR6</strong></td>
              <td>20K patches</td>
              <td>200</td>
              <td>
                <Badge variant="red">QC FAIL: undertrained</Badge>
              </td>
            </tr>
            <tr>
              <td><strong>NEOWISE</strong></td>
              <td>43.5K sources</td>
              <td>436</td>
              <td>
                <Badge variant="red">QC FAIL: ecliptic systematic</Badge>
              </td>
            </tr>
            <tr>
              <td><strong>Gaia DR3</strong></td>
              <td>50K variables</td>
              <td>500</td>
              <td>
                <Badge variant="amber">Needs 10x expansion</Badge>
              </td>
            </tr>
          </tbody>
        </table>
      </section>

      <section className="section">
        <h2>4. Key Discoveries</h2>

        <DiscoveryCard
          title="f_NL = -35/8 Mechanism Independence"
          borderColor="#22c55e"
          tag="Paper 2 · quintom_fnl_verification.py"
        >
          Verified across 3 bounce models: f_NL = -4.375 is parameter-free and
          mechanism-independent. SPHEREx (~2028) will measure to &sigma; ~ 0.7-2.
        </DiscoveryCard>

        <DiscoveryCard
          title="Quintom-B w-Crossing at 98.6%"
          borderColor="#3b82f6"
          tag="cobaya_w0wa_quintom_test.yaml · 50.9K samples"
        >
          w₀ = -0.871 &plusmn; 0.060, wₐ = -0.542 &plusmn; 0.245. Independently
          confirms DESI DR2 signal at 2.3&sigma;.
        </DiscoveryCard>

        <DiscoveryCard
          title="NANOGrav Consistency"
          borderColor="#3b82f6"
          tag="nanograv_model_comparison.py"
        >
          Matter bounce &gamma; = 3.0 vs NANOGrav 3.2 &plusmn; 0.6 (0.33&sigma;).
          Bayesian: bounce preferred 5.6:1 over SMBH.
        </DiscoveryCard>

        <DiscoveryCard
          title="328K Anomalies Across 8 Surveys"
          borderColor="#22c55e"
          tag="Pipeline B · 33.5M sources"
        >
          First multi-survey AI anomaly sweep. 6.1% f_NL improvement via
          latent-space multi-tracer. SPHEREx 4.38&sigma; forecast.
        </DiscoveryCard>
      </section>
    </>
  );
}
