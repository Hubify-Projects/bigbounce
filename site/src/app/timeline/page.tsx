import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Cosmic Timeline",
  description: "Visual timeline from the parent universe through the bounce to SPHEREx 2028.",
};

const events = [
  { time: "∞ — ?", label: "Parent Universe", desc: "A previous universe contracts under gravity. Density increases toward Planck scale (~10⁹³ g/cm³).", color: "#7c3aed" },
  { time: "t → 0⁻", label: "Contraction Phase", desc: "Matter-dominated contraction. Perturbations grow, imprinting f_NL = -35/8 on the bispectrum. PBH seeds form.", color: "#6366f1" },
  { time: "t = 0", label: "THE BOUNCE", desc: "Torsion (or quantum gravity) prevents singularity. Density reaches maximum but stays finite. Expansion begins.", color: "#ef4444" },
  { time: "10⁻³⁶ s", label: "Post-Bounce Expansion", desc: "Universe expands rapidly. No inflation needed — the contraction phase already solved the horizon and flatness problems.", color: "#f59e0b" },
  { time: "3 min", label: "Nucleosynthesis", desc: "Light elements form (H, He, Li). Identical to standard cosmology. ΔNeff ≈ 0 confirmed by our MCMC.", color: "#22c55e" },
  { time: "380,000 yr", label: "CMB Release", desc: "Universe becomes transparent. CMB carries bounce imprint: f_NL, birefringence β = 0.27°, spectral index.", color: "#22c55e" },
  { time: "~1 Gyr", label: "First Galaxies", desc: "Galaxies form from bounce-era perturbations. Our 195K DESI anomalies trace structure at z > 2.", color: "#3b82f6" },
  { time: "9.8 Gyr", label: "Dark Energy Onset", desc: "Quintom dark energy begins dominating. w(z) crosses -1 (P = 98.6% from our MCMC). Expansion accelerates.", color: "#3b82f6" },
  { time: "13.8 Gyr", label: "NOW (2026)", desc: "BigBounce research program: 4 papers, 8 surveys, 33.5M sources, 328K anomalies, 475K MCMC samples.", color: "#0ea5e9" },
  { time: "2028", label: "SPHEREx Launch", desc: "NASA's SPHEREx will measure f_NL to σ ≈ 0.7–1.0. If f_NL ≈ -4.375: bounce confirmed at >4σ.", color: "#0ea5e9" },
  { time: "~2032", label: "LiteBIRD", desc: "JAXA's LiteBIRD will measure birefringence to ~0.03°. Tests β = 0.27° prediction at ~9σ.", color: "#94a3b8" },
  { time: "~2035", label: "LISA", desc: "ESA's LISA will detect induced gravitational waves from PBH formation. Tests bounce GW spectrum directly.", color: "#94a3b8" },
];

export default function TimelinePage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>Visual Timeline</p>
        <h1>Cosmic Timeline</h1>
        <p className="subtitle">
          From the parent universe through the bounce to SPHEREx 2028 and beyond.
        </p>
      </div>

      <hr />

      <section className="section">
        <h2>The Story of the Universe</h2>
        <div style={{ position: "relative", paddingLeft: 28, marginTop: 8 }}>
          <div style={{ position: "absolute", left: 7, top: 12, bottom: 12, width: 1, background: "var(--border)" }} />
          {events.map((event, i) => (
            <div key={i} style={{ position: "relative", marginBottom: 24, paddingLeft: 20 }}>
              <div
                style={{
                  position: "absolute",
                  left: -25,
                  top: 6,
                  width: 12,
                  height: 12,
                  borderRadius: "50%",
                  background: event.color,
                  border: "2px solid var(--bg)",
                  boxShadow: `0 0 0 2px ${event.color}40`,
                }}
              />
              <div style={{ fontSize: 11, fontFamily: "var(--font-mono-stack)", color: "var(--text-muted)", marginBottom: 2 }}>
                {event.time}
              </div>
              <div style={{ fontSize: 15, fontWeight: 600, color: "var(--text)", marginBottom: 4 }}>
                {event.label}
              </div>
              <p style={{ fontSize: 13, color: "var(--text-secondary)", margin: 0, lineHeight: 1.6 }}>
                {event.desc}
              </p>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
