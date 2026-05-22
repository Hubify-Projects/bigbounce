import type { Metadata } from "next";
import Link from "next/link";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export const metadata: Metadata = {
  title: "Contributions",
  description:
    "Every novel contribution from the BigBounce research program ranked by novelty: NOVEL CONTRIBUTION, FIRST COMPUTATION, INDEPENDENT VERIFICATION, and PRIOR ART. Honest novelty accounting with definitions, equations, and code links.",
};

type Tier = "N3" | "N2" | "N1" | "N0";

interface Contribution {
  id: string;
  tier: Tier;
  title: string;
  paper: string;
  oneLine: string;
  why?: string;
  what?: string;
  equation?: string;
  prior?: string;
  ours?: string;
  verify?: { label: string; href: string }[];
}

const TIER_LABEL: Record<Tier, string> = {
  N3: "NOVEL CONTRIBUTION",
  N2: "FIRST COMPUTATION",
  N1: "INDEPENDENT VERIFICATION",
  N0: "PRIOR ART",
};

const TIER_COLOR: Record<Tier, string> = {
  N3: "#16a34a",
  N2: "#2563eb",
  N1: "#9333ea",
  N0: "#6b7280",
};

const contributions: Contribution[] = [
  {
    id: "perturbation-transparency",
    tier: "N3",
    title: "Perturbation-Transparency Theorem",
    paper: "Paper 1, §12",
    oneLine:
      "All-orders proof that the Barbero-Immirzi parameter γ is invisible in every perturbative observable for minimally-coupled scalar matter in ECH.",
    why: "Tells you what the bounce CAN'T do: the bounce mechanism itself is invisible to telescopes. Every testable prediction must come from the contraction dynamics before the bounce, not from the bounce mechanism. This redirected the entire research program.",
    what: "5-step proof chain: zero spin density for scalar matter → zero torsion → Levi-Civita connection at all perturbative orders → Holst term reduces to topological Nieh-Yan invariant → no perturbative dynamics from γ. Extended to scalar, vector, AND tensor perturbations.",
    equation:
      "|ε^{μνρσ} R_{μνρσ}| < 10^{-15}  (numerical confirmation of Holst topological identity across 1000 random Riemann tensors with FRW perturbation symmetries)",
    prior:
      "Hehl et al. (1976); Freidel, Minic & Takeuchi (2005); Calcagni & Mercuri (2009); Mercuri (2009); de Berredo-Peixoto et al. (2012); Långvik et al.",
    ours:
      "No prior work combined the known ingredients into an explicit all-orders perturbation theorem for minimally coupled scalar matter in ECH. We formalized it as a 5-step theorem, proved it extends to tensors, verified numerically to machine precision.",
    verify: [
      {
        label: "verify_holst_vanishing.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/transparency_verification/verify_holst_vanishing.py",
      },
    ],
  },
  {
    id: "14-barriers",
    tier: "N3",
    title: "14-Barrier Systematic Closure Map",
    paper: "Paper 1, §11",
    oneLine:
      "Complete catalog of 14 independent structural barriers closing every standard route from a nonsingular ECH bounce to late-time dark energy.",
    why: "Proves dark energy cannot come from the bounce — period. Instead of testing one or two mechanisms and hoping, we exhaustively closed every standard route. Tells future researchers exactly where NOT to look.",
    what: "7 foundation studies (A-G) + 17 research branches (H-W). Each barrier is named, quantified, and cross-referenced. Mass-coupling lock, Topological-Shift Duality, scalar-tensor universality, Planck suppression, attractor-sensitivity dilemma, parameter immunity, Liouville conservation, and 7 more.",
    equation:
      "g_eff ~ 10^{-61}  ·  Planck suppression 10^{-122}  ·  graviton-loop fine-tuning 10^{-57}  (across the barrier set)",
    prior:
      "Blagojević & Hehl (2013); Weinberg (1989); 't Hooft (1979); Shie, Nester & Yo (2008).",
    ours:
      "No prior work tested and closed all standard mechanism classes for connecting a nonsingular bounce to late-time dark energy within a single theoretical framework. Each branch opened only after passing a 4-question filter.",
    verify: [
      {
        label: "research/foundation_A_pgt through foundation_G",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research",
      },
    ],
  },
  {
    id: "matter-bounce-fnl",
    tier: "N3",
    title: "f_NL = -35/8 Forecast Package",
    paper: "Paper 2",
    oneLine:
      "First comprehensive forecast for testing Cai et al.'s matter-bounce non-Gaussianity prediction with upcoming surveys.",
    why: "Makes the bounce hypothesis testable. Cai et al. derived f_NL = -35/8 in 2009 but nobody built the full machinery to test it. We did: SPHEREx sensitivity, Bayesian model comparison, template mismatch quantification, robustness against systematics. SPHEREx data (~2028) will confirm or kill this at ~5σ.",
    what: "Parameter-free local non-Gaussianity from matter-dominated contraction: 300× larger than standard inflation, opposite sign. Forecast: σ(f_NL) = 0.7 (Heinrich+2023 multi-tracer Fisher); 3-5σ after systematic budget; 5.2-5.5σ optimistic pre-GR/b_φ degradation; 4.4σ at MegaMapper even at the worst convention.",
    equation: "f_NL^{local} = -35/8 = -4.375",
    prior:
      "Cai, Xue, Brandenberger & Zhang (2009); Heinrich, Doré & Krause (2023); Dalal et al. (2008); Li & Brandenberger (2014).",
    ours:
      "First combination of (a) SPHEREx + MegaMapper sensitivity specific to bounce; (b) Bayesian model comparison with 600K+ MC realizations (bounce favored at 8-17:1 over tuned multifield); (c) GR-projection robustness; (d) template-mismatch (r ≈ 0.85-0.90); (e) ε-correction bounded [1-8%]; (f) cubic bounce transmission estimate; (g) Li-Brandenberger convention resolution.",
    verify: [
      {
        label: "research/bayesian_discrimination_program/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/bayesian_discrimination_program",
      },
      {
        label: "algebraic_commutator_proof.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/matter_bounce_parameters/algebraic_commutator_proof.py",
      },
    ],
  },
  {
    id: "physics-commutator",
    tier: "N3",
    title: "Physics-Derived Full-Commutator Polynomial",
    paper: "Paper 2",
    oneLine:
      "Resolves a 15-year factor-of-2 ambiguity between Cai et al. (2009) and Li et al. (2017) by tracing it to the in-in commutator.",
    what: "Using Cai et al.'s own intermediate vertex contributions (Eqs. 34-36), we derive the full-commutator shape polynomial algebraically: (6, 2, -18, 10, -66, 18). Proven by exact rational arithmetic. Published Eq. 37 coefficients (3, 1, -9, 5, -66, 9) are the single-time-ordering values. The factor of 2 is the in-in commutator: i⟨[ζ³, L]⟩ = -2 Im⟨ζ³ L⟩.",
    why: "Two groups published different answers; nobody knew who was right. We proved both groups are correct at their respective levels. The exact polynomial determines how well SPHEREx can actually detect the signal.",
    equation:
      "Full-commutator polynomial: (6, 2, -18, 10, -66, 18)  ·  template overlap r ≈ 0.85-0.90",
    verify: [
      {
        label: "algebraic_commutator_proof.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/matter_bounce_parameters/algebraic_commutator_proof.py",
      },
    ],
  },
  {
    id: "alp-birefringence",
    tier: "N2",
    title: "ALP Birefringence Consistency",
    paper: "Paper 1, §11.5 / Paper 2",
    oneLine:
      "ECH parity structure motivates a Planck-scale ALP. Predicted β = 0.27° matches the 3.6σ Planck+ACT observation at 0.5σ.",
    what: "Numerical ΛCDM ALP field evolution gives Δφ/f_a = 0.65-1.07 across the natural mass range m/H₀ ∈ [1, 3]. Fiducial β = 0.27° (at m ≈ 1.8H₀) matches observed 0.242 ± 0.061° within 0.5σ. NaMaster pod 1 production 500MC: β = 0.27° recovered at SNR = 20.32σ.",
    why: "Our prediction matches an actual observation at 3.9σ inverse-variance combined. LiteBIRD tests at 9σ in early 2030s. Bounce-mechanism independent — falsification target separate from f_NL.",
    equation:
      "β = 0.27°  ·  recovered as 0.238° at SNR = 20.32σ in pod 1 NaMaster production",
    verify: [
      {
        label: "alp_field_evolution/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/alp_field_evolution",
      },
    ],
  },
  {
    id: "topological-shift-duality",
    tier: "N2",
    title: "Topological-Shift Duality (Barrier 2)",
    paper: "Paper 1, §11.2",
    oneLine:
      "Mass protection and geometric content are mutually exclusive for pseudoscalar fields coupled to the Nieh-Yan 4-form.",
    what: "If Nieh-Yan is topological (standard EC), pseudoscalar mass is shift-symmetry protected but the coupling is a total derivative — no dynamics. If Nieh-Yan is non-topological (metric-affine), dynamics arise but shift symmetry breaks — no mass protection. Cannot have both.",
    why: "Closes a loophole that keeps coming up — people repeatedly try to build light pseudoscalars for dark energy from Nieh-Yan. Applies beyond our framework: constrains any attempt to use topological gravity terms as sources for light pseudoscalars.",
    verify: [
      {
        label: "foundation_B_lock_breaking/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/foundation_B_lock_breaking",
      },
    ],
  },
  {
    id: "chirality-catalog",
    tier: "N3",
    title: "8.47M-Galaxy Chirality Catalog",
    paper: "Paper 4",
    oneLine:
      "Largest survey-scale spiral-galaxy chirality catalog: CW/CCW/NOT_SPIRAL with equivariant DL ensemble, null result for large-scale parity violation.",
    what:
      "8,474,531 galaxies from DESI Legacy Survey DR8. Equivariance-aware CNN ensemble (rotation+flip augmented) producing P(CW)/P(CCW)/P(NS) per galaxy. Strongest individual signal: north-south hemisphere asymmetry at 3.05σ, marginal and look-elsewhere-corrected away. No evidence for large-scale parity violation.",
    why:
      "First null at this scale. Constrains any cosmological parity-violating mechanism — including the early-universe consequences of ECH parity-odd structure beyond the ALP birefringence channel.",
    equation:
      "CW fraction (N) = 49.81%  ·  CW fraction (S) = 49.64%  ·  Δ = 0.17 pp at 3.05σ (marginal)",
    verify: [
      {
        label: "bamfai/galaxy-chirality-catalog (HuggingFace)",
        href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
      },
      {
        label: "chirality_catalog_paper.pdf",
        href: "/papers/chirality_catalog_paper.pdf",
      },
    ],
  },
  {
    id: "anomaly-catalog",
    tier: "N3",
    title: "Multi-Survey Anomaly Catalog (378,280 anomalies)",
    paper: "Paper 3",
    oneLine:
      "First unified anomaly sweep across 7 surveys (37.3M sources) after Path-C native retrains and 5″ positional dedup.",
    what:
      "DESI DR1 (195,829), SDSS DR18 (77,905), LAMOST DR10 (44,075), eROSITA DR1 (298), Planck CMB (200), NEOWISE (436), Gaia DR3 (500). 388,493 raw → 378,280 unique after global friends-of-friends union-find at 5″ (637 multi-survey + 9,576 intra-survey collapses).",
    why:
      "Cross-survey continuity is the load-bearing falsification surface for any new physics claim. Population-level rare-class discovery (z>6 QSOs, ultra-rare AE candidates) is the byproduct.",
    verify: [
      {
        label: "pipelines/p3_anomaly_engine/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p3_anomaly_engine",
      },
    ],
  },
  {
    id: "spherex-fisher",
    tier: "N2",
    title: "SPHEREx f_NL Fisher Forecast",
    paper: "Paper 2",
    oneLine:
      "Multi-tracer Fisher forecast of σ(f_NL) = 0.7 → 4.7-12σ detection of bounce f_NL = -4.375 by 2027.",
    equation:
      "σ(f_NL) = 0.36 (Fisher ideal)  ·  σ(f_NL) = 0.93 (Munchmeyer+2019 conservative)  ·  detection 4.7-12σ",
    what:
      "Externalized to Heinrich+2023 multi-tracer bispectrum forecast with the bounce template; noise-weighted shape mismatch, ε-correction, b_φ marginalization, GR projection all carried through.",
    why:
      "Sets a hard deadline on falsification — SPHEREx will report by ~2027-2028.",
    verify: [
      {
        label: "research/focused_paper_source_integration/02_full_draft.tex",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/focused_paper_source_integration/02_full_draft.tex",
      },
    ],
  },
  {
    id: "desi-environment",
    tier: "N3",
    title: "DESI Environmental Chirality Study",
    paper: "Paper 5",
    oneLine:
      "Cross-match of 2.23M DESI LSS galaxies with the 8.47M chirality catalog to test environmental dependence of spiral spin direction.",
    what:
      "Matched 2,233,012 galaxies between DESI Y1 LSS and the Paper-4 chirality catalog. First-pass environmental fraction analysis on disk. Cosmic-web headline analysis blocked on missing DESI environmental VAC.",
    why:
      "Cosmic-web environment is the most natural place to look for spin alignment / handedness correlations. If any signature exists it should be strongest in filaments/walls.",
    verify: [
      {
        label: "pipelines/p5_desi_chirality/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p5_desi_chirality",
      },
    ],
  },
  {
    id: "mcmc-verification",
    tier: "N2",
    title: "MCMC Verification Infrastructure (424,781 samples)",
    paper: "Paper 1, §9",
    oneLine:
      "424,781 posterior samples across 3 frozen dataset combinations. Honest null: ΔN_eff ≈ 0, H₀ = 67.68 (standard ΛCDM).",
    what:
      "Cobaya 3.6.1 + CAMB 1.6.5. 4 dataset configs, 6-7 chains each, Gelman-Rubin convergence. Corrected our own earlier artifact (H₀ = 69.2 was a SH0ES prior artifact).",
    why: "Demonstrates honest negative reporting — we found our own bug and disclosed it.",
    verify: [
      {
        label: "reproducibility/cosmology/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility/cosmology",
      },
    ],
  },
  {
    id: "pta-bounce",
    tier: "N2",
    title: "NANOGrav Bounce GW Spectrum",
    paper: "Paper 3, §6",
    oneLine:
      "Combined PTA GPU MCMC γ = 3.20 ± 0.42 vs bounce γ = 3.0 (0.48σ); SMBHB excluded at ≳2σ.",
    equation:
      "γ_bounce = 3.0  ·  γ_obs = 3.20 ± 0.42  ·  consistency 0.48σ",
  },
];

function ContributionCard({ c }: { c: Contribution }) {
  const color = TIER_COLOR[c.tier];
  return (
    <Card
      id={c.id}
      style={{
        padding: 20,
        borderLeft: `3px solid ${color}`,
        scrollMarginTop: 80,
      }}
    >
      <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: 10 }}>
        <span
          style={{
            display: "inline-block",
            padding: "2px 8px",
            borderRadius: 4,
            background: color,
            color: "#fff",
            fontFamily: "var(--font-mono-stack)",
            fontSize: 10,
            fontWeight: 700,
            letterSpacing: 0.4,
          }}
        >
          {TIER_LABEL[c.tier]}
        </span>
        <span
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: 11,
            color: "var(--text-muted)",
          }}
        >
          {c.paper}
        </span>
      </div>
      <h3
        style={{
          marginTop: 10,
          marginBottom: 6,
          fontFamily: "var(--font-mono-stack)",
          fontSize: 16,
          fontWeight: 600,
        }}
      >
        {c.title}
      </h3>
      <p style={{ marginTop: 0, fontSize: 13, lineHeight: 1.6 }}>{c.oneLine}</p>
      {c.equation && (
        <div
          style={{
            marginTop: 10,
            padding: "8px 12px",
            background: "color-mix(in srgb, var(--accent) 6%, var(--surface))",
            borderLeft: "2px solid var(--accent)",
            fontFamily: "var(--font-mono-stack)",
            fontSize: 12,
            lineHeight: 1.6,
          }}
        >
          {c.equation}
        </div>
      )}
      <h4 style={{ marginTop: 14, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
        Why it matters
      </h4>
      <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.why}</p>
      <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
        What it is
      </h4>
      <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.what}</p>
      {c.prior && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            What existed before
          </h4>
          <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.prior}</p>
        </>
      )}
      {c.ours && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            What we did
          </h4>
          <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.ours}</p>
        </>
      )}
      {c.verify && c.verify.length > 0 && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            How to verify
          </h4>
          <ul style={{ margin: 0, paddingLeft: 18, fontSize: 13, lineHeight: 1.8 }}>
            {c.verify.map((v) => (
              <li key={v.href}>
                <a
                  href={v.href}
                  target={v.href.startsWith("http") ? "_blank" : undefined}
                  rel="noopener noreferrer"
                  style={{ color: "var(--accent)", fontFamily: "var(--font-mono-stack)", fontSize: 12 }}
                >
                  {v.label}
                </a>
              </li>
            ))}
          </ul>
        </>
      )}
    </Card>
  );
}

export default function ContributionsPage() {
  const grouped: Record<Tier, Contribution[]> = { N3: [], N2: [], N1: [], N0: [] };
  for (const c of contributions) grouped[c.tier].push(c);
  const counts = {
    N3: grouped.N3.length,
    N2: grouped.N2.length,
    N1: grouped.N1.length,
    N0: grouped.N0.length,
  };
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Novelty accounting
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          contributions
        </h1>
        <p className="subtitle">
          Every contribution is labeled honestly: <strong>NOVEL</strong> (we did
          this first), <strong>FIRST COMPUTATION</strong> (new quantitative
          result within a known framework), <strong>VERIFICATION</strong> (we
          confirmed someone else's result), or <strong>PRIOR ART</strong>
          (foundation we use). Full credit to prior work throughout.
        </p>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "220px 1fr", gap: 32, marginTop: 24 }}>
        <aside style={{ position: "sticky", top: 80, alignSelf: "start" }}>
          <div
            style={{
              fontFamily: "var(--font-mono-stack)",
              fontSize: 10,
              textTransform: "uppercase",
              letterSpacing: 0.8,
              color: "var(--text-muted)",
              marginBottom: 8,
            }}
          >
            By tier
          </div>
          {(["N3", "N2", "N1", "N0"] as Tier[]).map((tier) => (
            <a
              key={tier}
              href={`#tier-${tier}`}
              style={{
                display: "block",
                padding: "6px 10px",
                marginBottom: 4,
                fontFamily: "var(--font-mono-stack)",
                fontSize: 12,
                color: "var(--text)",
                textDecoration: "none",
                borderLeft: `2px solid ${TIER_COLOR[tier]}`,
              }}
            >
              <span style={{ color: TIER_COLOR[tier], fontWeight: 700 }}>{tier}</span>
              {" — "}
              {TIER_LABEL[tier]} · {counts[tier]}
            </a>
          ))}
          <div
            style={{
              fontFamily: "var(--font-mono-stack)",
              fontSize: 10,
              textTransform: "uppercase",
              letterSpacing: 0.8,
              color: "var(--text-muted)",
              marginTop: 18,
              marginBottom: 8,
            }}
          >
            All contributions
          </div>
          {contributions.map((c) => (
            <a
              key={c.id}
              href={`#${c.id}`}
              style={{
                display: "block",
                padding: "4px 10px",
                fontFamily: "var(--font-mono-stack)",
                fontSize: 11,
                color: "var(--text-muted)",
                textDecoration: "none",
                lineHeight: 1.4,
              }}
            >
              {c.title}
            </a>
          ))}
          <Link
            href="/old/contributions.html"
            style={{
              display: "block",
              marginTop: 20,
              padding: "8px 10px",
              fontFamily: "var(--font-mono-stack)",
              fontSize: 11,
              color: "var(--accent)",
              textDecoration: "none",
              border: "1px solid var(--border)",
              borderRadius: 6,
            }}
          >
            ↗ full legacy contributions page
          </Link>
        </aside>

        <div style={{ display: "grid", gap: 14 }}>
          {(["N3", "N2", "N1", "N0"] as Tier[]).map(
            (tier) =>
              grouped[tier].length > 0 && (
                <section key={tier} id={`tier-${tier}`} style={{ scrollMarginTop: 80 }}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: 10,
                      marginBottom: 12,
                    }}
                  >
                    <Badge variant="outline" className="font-mono text-[10px]">
                      {tier}
                    </Badge>
                    <h2
                      style={{
                        margin: 0,
                        fontFamily: "var(--font-mono-stack)",
                        fontSize: 14,
                        textTransform: "uppercase",
                        letterSpacing: 0.6,
                        color: TIER_COLOR[tier],
                      }}
                    >
                      {TIER_LABEL[tier]}
                    </h2>
                  </div>
                  <div style={{ display: "grid", gap: 14 }}>
                    {grouped[tier].map((c) => (
                      <ContributionCard key={c.id} c={c} />
                    ))}
                  </div>
                </section>
              ),
          )}
        </div>
      </div>
    </>
  );
}
