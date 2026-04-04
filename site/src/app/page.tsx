export default function HomePage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Program &middot; Updated April 2026
        </p>
        <h1>Spin-Torsion Cosmology</h1>
        <p className="subtitle">
          A comprehensive research program exploring bounce cosmology as an
          alternative to cosmic inflation.
        </p>
        <div className="meta">
          <span className="badge badge-accent">4 Papers</span>
          <span className="badge badge-accent">8 Surveys</span>
          <span className="badge badge-accent">33.5M+ Sources</span>
          <span className="badge badge-accent">328K+ Anomalies</span>
          <span className="badge badge-neutral">Houston Golden</span>
        </div>
      </div>

      <hr />

      <section className="section">
        <h2>Key Results</h2>
        <div className="grid grid-2">
          <div className="card">
            <h3>
              f<sub>NL</sub> = &minus;35/8
            </h3>
            <p>
              Parameter-free, mechanism-independent prediction from the matter
              bounce. SPHEREx (~2028) will test at &sigma; &asymp; 0.7&ndash;1.0.
            </p>
          </div>
          <div className="card">
            <h3>Quintom w-Crossing at 98.6%</h3>
            <p>
              Independent MCMC (50.9K samples) finds P(quintom-B) = 98.6%,
              confirming DESI DR2 signal at 2.3&sigma;.
            </p>
          </div>
          <div className="card">
            <h3>NANOGrav Consistency</h3>
            <p>
              Matter bounce predicts &gamma; = 3.0. NANOGrav measures
              3.2 &plusmn; 0.6 (0.33&sigma;). Bayes factor 5.6:1.
            </p>
          </div>
          <div className="card">
            <h3>328K Anomalies Across 8 Surveys</h3>
            <p>
              Multi-survey AI anomaly sweep: DESI, SDSS, LAMOST, eROSITA,
              Planck, ACT, NEOWISE, Gaia. 33.5M sources scored.
            </p>
          </div>
        </div>
      </section>

      <section className="section">
        <h2>Research Papers</h2>
        <table>
          <thead>
            <tr>
              <th>Paper</th>
              <th>Status</th>
              <th>Key Result</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <strong>Paper 1</strong> &mdash; Spin-Torsion Framework
              </td>
              <td>
                <span className="badge badge-green">99%</span>
              </td>
              <td>14 barriers, ALP birefringence, bounce landscape</td>
            </tr>
            <tr>
              <td>
                <strong>Paper 2</strong> &mdash; f<sub>NL</sub> Forecast
              </td>
              <td>
                <span className="badge badge-green">100%</span>
              </td>
              <td>
                f<sub>NL</sub> = &minus;35/8, SPHEREx testable
              </td>
            </tr>
            <tr>
              <td>
                <strong>Paper 3</strong> &mdash; Anomaly Catalog
              </td>
              <td>
                <span className="badge badge-blue">95%</span>
              </td>
              <td>328K anomalies, 8 surveys, 6.1% f<sub>NL</sub> improvement</td>
            </tr>
            <tr>
              <td>
                <strong>Paper 4</strong> &mdash; Chirality Catalog
              </td>
              <td>
                <span className="badge badge-blue">85%</span>
              </td>
              <td>8.47M galaxies, dipole 0.43&sigma; null</td>
            </tr>
          </tbody>
        </table>
      </section>
    </>
  );
}
