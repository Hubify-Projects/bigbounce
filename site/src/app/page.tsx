import { papers, getPaperBySlug } from "@/data/papers";
import { liveStatus } from "@/data/live-status";
import { sortedReviewRounds } from "@/data/reviewTimeline";
import { Button } from "@/components/ui/button";
import { LiveStatus } from "@/components/Shell/LiveStatus";
import { getLivePapers, displayVersion } from "@/lib/livePapers";
import { getPublishEta } from "@/lib/liveReadiness";
import { PublishEtaWidget } from "@/components/PublishEtaWidget";
import {
  ArrowRight,
  Database,
  ExternalLink,
  FileText,
  FlaskConical,
} from "lucide-react";
import Link from "next/link";

// ──────────────────────────────────────────────────────────────────────
// First-time-visitor homepage. Opens with the science story, then the
// two-halves program arc (mirrors /contributions #program-arc), the six
// papers (readiness sourced ONLY from getLivePapers — the single Convex
// source, NOT static papers.ts.readiness), a concise contributions list,
// the open-science artifacts (PDFs + HuggingFace datasets + models), a
// deep-dive nav, and finally a compact live-status strip.
// ──────────────────────────────────────────────────────────────────────

function readinessColor(readiness: number): string {
  if (readiness >= 95) return "var(--success)";
  if (readiness >= 85) return "var(--text-secondary)";
  if (readiness >= 70) return "var(--warn)";
  return "var(--crit)";
}

// Short, public-friendly titles (curated in live-status.ts) keyed by slug.
const shortTitleBySlug = new Map(
  liveStatus.papers.map((p) => [p.slug, p.shortTitle]),
);

// The two-halves arc — verbatim from /contributions #program-arc so the
// homepage and the deep-dive page tell the same story.
const arcRoles: Array<{ n: string; role: string }> = [
  { n: "P1A", role: "ECH theory + no-go: a perturbation-transparency theorem and a 14-constraint channel-level closure of the four minimal bounce→dark-energy routes." },
  { n: "P1B", role: "MCMC + pipeline companion: frozen ΛCDM+ΔN_eff chains (honest null), NaMaster recovery, and an ALP-birefringence consistency check." },
  { n: "P2", role: "f_NL = −35/16 forecast: the surviving falsifiable handle — matter-bounce non-Gaussianity, ~300× inflation and opposite sign, testable by SPHEREx at 3–5σ." },
  { n: "P3", role: "Public-ID archive recovery: 181 DESI DR1 TARGETIDs recovered from a frozen historical anomaly list (170 high-coordinate-consistency core + 11 lower-confidence) — a reproducible provenance product, explicitly not a purity, novelty, or detection claim." },
  { n: "P4", role: "Galaxy chirality null: 8.47M classified galaxies, a null +0.41σ real-space dipole, refuting the claimed ~3% parity signal at scale." },
  { n: "P5", role: "DESI chirality × environment null: spiral handedness is independent of cosmic-web environment, constraining environment-coupled parity models." },
];

// Concise contributions — a short, scannable subset of /contributions.
// Every line is copied from the canonical contributions data (no new claims).
const TIER_COLOR: Record<"N3" | "N2", string> = {
  N3: "var(--tier-n3)",
  N2: "var(--tier-n2)",
};
const topContributions: Array<{
  id: string;
  tier: "N3" | "N2";
  paper: string;
  title: string;
  line: string;
}> = [
  {
    id: "perturbation-transparency",
    tier: "N3",
    paper: "P1A",
    title: "Perturbation-Transparency Theorem",
    line: "The bounce mechanism itself is invisible to telescopes — every testable prediction must come from the pre-bounce contraction.",
  },
  {
    id: "14-barriers",
    tier: "N3",
    paper: "P1A",
    title: "14-Constraint Channel-Level Closure Map",
    line: "Closes every enumerated minimal route from a nonsingular ECH bounce to late-time dark energy, under stated assumptions.",
  },
  {
    id: "matter-bounce-fnl",
    tier: "N3",
    paper: "P2",
    title: "f_NL = −35/16 Forecast Package",
    line: "The surviving falsifiable handle: SPHEREx (~2028) will confirm or kill the matter-bounce non-Gaussianity at multi-σ.",
  },
  {
    id: "anomaly-catalog",
    tier: "N3",
    paper: "P3",
    title: "Public-ID Anomaly-List Recovery",
    line: "181 public DESI DR1 TARGETIDs recovered from a frozen historical anomaly list — a reproducible archive/provenance product, not a detection or novelty claim.",
  },
  {
    id: "chirality-catalog",
    tier: "N3",
    paper: "P4",
    title: "8.47M-Galaxy Chirality Catalog",
    line: "Largest chirality-labeled catalog to date; a null +0.41σ real-space dipole refutes a claimed ~3% parity signal.",
  },
  {
    id: "desi-environment",
    tier: "N3",
    paper: "P5",
    title: "DESI Chirality × Environment Null",
    line: "Galaxy handedness is statistically independent of large-scale-structure environment.",
  },
  {
    id: "alp-birefringence",
    tier: "N2",
    paper: "P1A / P2",
    title: "ALP Birefringence Consistency",
    line: "A predicted β = 0.27° sits within 0.5σ of the 3.6σ Planck+ACT cosmic-birefringence observation.",
  },
];

const artifactGroups: Array<{
  label: string;
  blurb: string;
  links: Array<{ label: string; href: string; internal?: boolean }>;
}> = [
  {
    label: "Paper PDFs",
    blurb: "Every paper compiles to a versioned PDF, served from the papers index.",
    links: [{ label: "Browse all six papers", href: "/paper", internal: true }],
  },
  {
    label: "Datasets on HuggingFace",
    blurb: "The two public survey catalogs behind the data-arm papers.",
    links: [
      {
        label: "bigbounce-anomaly-catalog",
        href: "https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog",
      },
      {
        label: "galaxy-chirality-catalog",
        href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
      },
    ],
  },
  {
    label: "Models on HuggingFace",
    blurb: "The trained detectors that produced the catalogs.",
    links: [
      {
        label: "desi-spectral-anomaly-detector",
        href: "https://huggingface.co/bamfai/desi-spectral-anomaly-detector",
      },
      {
        label: "galaxy-chirality-v2",
        href: "https://huggingface.co/bamfai/galaxy-chirality-v2",
      },
    ],
  },
  {
    label: "Source & code",
    blurb: "Every headline number is reproducible from committed scripts.",
    links: [
      {
        label: "github.com/Hubify-Projects/bigbounce",
        href: "https://github.com/Hubify-Projects/bigbounce",
      },
    ],
  },
];

const deepDives: Array<{ href: string; title: string; blurb: string }> = [
  { href: "/explained", title: "Plain-English explainer", blurb: "What a Big Bounce is and why it can be tested with real telescopes." },
  { href: "/contributions", title: "Contributions", blurb: "Every novel result, ranked on the N1–N4 novelty scale." },
  { href: "/reviews", title: "The review program", blurb: "How each paper was adversarially stress-tested before sign-off." },
  { href: "/predictions", title: "Predictions", blurb: "The falsifiable signatures and the experiments that will settle them." },
  { href: "/surveys", title: "Surveys", blurb: "The seven archival surveys mined, with per-survey QC status." },
  { href: "/data-explorer", title: "Data explorer", blurb: "Browse the catalogs and survey data interactively." },
  { href: "/anomaly-explorer", title: "Anomaly explorer", blurb: "Explore the DESI DR1 autoencoder anomaly-detection pipeline and its candidate list." },
  { href: "/galaxy-explorer", title: "Galaxy explorer", blurb: "Explore the 8.47M-galaxy chirality catalog." },
];

const sectionLabel: React.CSSProperties = {
  fontFamily: "var(--font-mono-stack)",
  fontSize: 11,
  textTransform: "uppercase",
  letterSpacing: "0.06em",
  color: "var(--text-tertiary)",
  marginBottom: 8,
};

export default async function HomePage() {
  // Readiness comes from getLivePapers ONLY — the single Convex-first source
  // shared with the live paper-state surfaces. Never re-read papers.ts.readiness.
  const livePapers = await getLivePapers();
  const eta = await getPublishEta();

  // Review-proof band data. Only kinds that ARE reviews count as review
  // rounds; skill-improvement entries are program bookkeeping and closure
  // waves are fixes, tallied separately so the trust number stays honest.
  const timeline = sortedReviewRounds();
  const REVIEW_KINDS = new Set(["external-browser", "internal-api", "internal-cc"]);
  const reviewRoundCount = timeline.filter((r) => REVIEW_KINDS.has(r.kind)).length;
  const closureWaveCount = timeline.filter((r) => r.kind === "closure-wave" || r.kind === "ext-closure").length;
  const latestRound = timeline[0];
  const avgReadiness = Math.round(
    livePapers.reduce((acc, p) => acc + p.readinessComputed, 0) /
      Math.max(1, livePapers.length),
  );

  return (
    <>
      <LiveStatus />

      {/* 1 — Science story */}
      <section className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Bounce cosmology · live research program
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 650 }}>
          Was there a bounce before the Big Bang?
        </h1>
        <p className="subtitle">
          This is an open, falsifiable research program asking one question: can a
          nonsingular <strong>Big Bounce</strong> cosmology — a universe that
          contracted and rebounded rather than began at a singularity — beat the
          standard <strong>ΛCDM + inflation</strong> picture? We attack it from
          both ends: deriving where a bounce could leave a fingerprint, then
          mining tens of millions of archival survey sources to look for it.
        </p>
        <p
          style={{
            maxWidth: "68ch",
            fontSize: 14,
            lineHeight: 1.7,
            color: "var(--text-secondary)",
            marginTop: 4,
          }}
        >
          Six papers, honest nulls, and quantified falsification windows — with
          the decisive test (SPHEREx, ~2028) already on the calendar. Everything
          here is public: the PDFs, the datasets, the models, and the code.
        </p>
        <div className="mt-5 flex flex-wrap gap-2">
          <Button asChild>
            <Link href="/explained">
              Start with the explainer <ArrowRight size={15} />
            </Link>
          </Button>
          <Button asChild variant="outline">
            <Link href="/paper">Read the six papers</Link>
          </Button>
        </div>
      </section>

      {/* 1.5 — Adversarial review proof band (counts computed from the real
          timeline at build time; the /reviews page is the full record).
          Count ONLY actual review rounds — skill-improvement and closure
          entries are program bookkeeping, not reviews, and inflating this
          number would undercut the exact trust claim the band makes. */}
      <section style={{ marginBottom: 40 }}>
        <div className="card" style={{ borderLeft: "3px solid var(--accent)" }}>
          <p className="eyebrow" style={{ marginBottom: 6 }}>
            How every claim here gets vetted
          </p>
          <p style={{ fontSize: 14, lineHeight: 1.7, color: "var(--text-secondary)", maxWidth: "72ch", margin: 0 }}>
            Every result on this site has been through{" "}
            <strong style={{ color: "var(--text)" }}>{reviewRoundCount} adversarial review rounds</strong> — model
            families from five different labs told to refute each paper, plus independent external referees, with a
            separate integrity audit on the review process itself — and {closureWaveCount} closure waves fixing what
            those rounds found. The loop has caught real errors (an overlap-inflated significance, a mislabeled
            catalog tier) before any reader could. The complete record is public
            {latestRound ? <> — most recent: {latestRound.dateISO}</> : null}.
          </p>
          <p style={{ margin: "8px 0 0" }}>
            <Link href="/reviews" style={{ color: "var(--accent)", fontSize: 13.5 }}>
              Browse the full review timeline <ArrowRight size={13} style={{ display: "inline", verticalAlign: "-2px" }} />
            </Link>
          </p>
        </div>
      </section>

      {/* 1.6 — Honest publishability ETA (live from Convex computeEta). */}
      {eta ? (
        <section style={{ marginBottom: 40 }}>
          <PublishEtaWidget eta={eta} />
        </section>
      ) : null}

      {/* 2 — Two halves / program arc */}
      <section className="section" style={{ marginTop: 8 }}>
        <p style={sectionLabel}>How the six papers fit together</p>
        <h2 style={{ marginTop: 0 }}>One program, two halves</h2>
        <p style={{ marginTop: 4, fontSize: 14, lineHeight: 1.7, maxWidth: "66ch" }}>
          The <strong>theory arm</strong> (P1A, P1B, P2) asks where a nonsingular
          Einstein–Cartan–Holst bounce could leave a falsifiable fingerprint,
          proves the bounce mechanism itself is invisible to telescopes, closes
          the enumerated dark-energy routes, and isolates the one surviving handle
          — a parameter-free matter-bounce non-Gaussianity SPHEREx can test. The{" "}
          <strong>data arm</strong> (P3, P4, P5) mines 45M+ archival sources for
          the parity- and anomaly-level signatures any bounce would have to
          imprint, and reports honest nulls with quantified falsification windows.
          Negative theory results narrowed the search space; the surveys then went
          looking exactly where the theory said to look.
        </p>
        <div style={{ display: "grid", gap: 0, marginTop: 16, maxWidth: "76ch" }}>
          {arcRoles.map((p, i) => (
            <div
              key={p.n}
              style={{
                display: "grid",
                gridTemplateColumns: "52px 1fr",
                gap: 14,
                alignItems: "baseline",
                padding: "10px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--border)",
              }}
            >
              <span
                style={{
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: 13,
                  fontWeight: 700,
                  color: "var(--accent)",
                }}
              >
                {p.n}
              </span>
              <span style={{ fontSize: 13, lineHeight: 1.6 }}>{p.role}</span>
            </div>
          ))}
        </div>
        <p style={{ marginTop: 14, fontSize: 13 }}>
          <Link href="/contributions#program-arc" style={{ color: "var(--accent)" }}>
            Read the full program arc &rarr;
          </Link>
        </p>
      </section>

      {/* 3 — The six papers, scannable (readiness from getLivePapers) */}
      <section className="section">
        <p style={sectionLabel}>The evidence</p>
        <h2 style={{ marginTop: 0 }}>The six papers</h2>
        <div style={{ display: "grid", gap: 0, marginTop: 12 }}>
          {livePapers.map((lp, i) => {
            const stat = getPaperBySlug(lp.slug);
            const title = shortTitleBySlug.get(lp.slug) ?? lp.shortTitle;
            const pdfHref =
              lp.sitePdfPath ??
              stat?.artifacts.find((a) => a.kind === "primary")?.href ??
              null;
            const color = readinessColor(lp.readinessComputed);
            return (
              <div
                key={lp.slug}
                style={{
                  display: "grid",
                  gridTemplateColumns: "1fr",
                  gap: 8,
                  padding: "18px 0",
                  borderTop: i === 0 ? "none" : "1px solid var(--border)",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    flexWrap: "wrap",
                    alignItems: "center",
                    gap: 10,
                  }}
                >
                  <span
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 11,
                      fontWeight: 700,
                      color: "var(--accent)",
                      minWidth: 34,
                    }}
                  >
                    P{lp.number}
                  </span>
                  <span
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 15,
                      fontWeight: 600,
                      flex: 1,
                      minWidth: 220,
                    }}
                  >
                    {title}
                  </span>
                  <span
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 12,
                      fontWeight: 600,
                      color,
                    }}
                    title="Readiness — live from Convex paper state"
                  >
                    {lp.readinessComputed}% ready
                  </span>
                  {lp.currentVersion && (
                    <span
                      style={{
                        fontFamily: "var(--font-mono-stack)",
                        fontSize: 11,
                        color: "var(--text-tertiary)",
                      }}
                    >
                      {displayVersion(lp.currentVersion)}
                    </span>
                  )}
                </div>
                {stat?.tldr && (
                  <p
                    style={{
                      margin: 0,
                      fontSize: 13,
                      lineHeight: 1.6,
                      color: "var(--text-secondary)",
                      maxWidth: "78ch",
                    }}
                  >
                    {stat.tldr}
                  </p>
                )}
                <div
                  style={{
                    display: "flex",
                    flexWrap: "wrap",
                    gap: 16,
                    marginTop: 2,
                    fontSize: 12.5,
                  }}
                >
                  {pdfHref && (
                    <a
                      href={pdfHref}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{
                        display: "inline-flex",
                        alignItems: "center",
                        gap: 5,
                        color: "var(--accent)",
                        fontFamily: "var(--font-mono-stack)",
                      }}
                    >
                      <FileText size={13} /> Read PDF
                    </a>
                  )}
                  <Link
                    href={`/papers/${lp.slug}`}
                    style={{ color: "var(--text-secondary)" }}
                  >
                    Details &rarr;
                  </Link>
                  {stat?.target && (
                    <span style={{ color: "var(--text-tertiary)" }}>
                      target: {stat.target}
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 4 — Concise contributions */}
      <section className="section">
        <p style={sectionLabel}>What&rsquo;s new here</p>
        <h2 style={{ marginTop: 0 }}>Top contributions</h2>
        <p style={{ marginTop: 4, fontSize: 13, lineHeight: 1.6, color: "var(--text-secondary)", maxWidth: "66ch" }}>
          A short list of the program&apos;s most novel results. Each is scored on a
          four-tier scale; our self-claim ceiling is{" "}
          <strong>N3</strong> (first-of-kind). The full accounting — prior work,
          equations, and verification links — lives on the contributions page.
        </p>
        <div style={{ display: "grid", gap: 0, marginTop: 14, maxWidth: "80ch" }}>
          {topContributions.map((c, i) => (
            <Link
              key={c.id}
              href={`/contributions#${c.id}`}
              style={{
                display: "grid",
                gridTemplateColumns: "auto 1fr",
                gap: 12,
                alignItems: "baseline",
                padding: "12px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--border)",
                textDecoration: "none",
                color: "var(--text)",
              }}
            >
              <span
                style={{
                  display: "inline-block",
                  padding: "2px 7px",
                  borderRadius: 4,
                  background: TIER_COLOR[c.tier],
                  color: "#fff",
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: 10,
                  fontWeight: 700,
                  minWidth: 26,
                  textAlign: "center",
                }}
              >
                {c.tier}
              </span>
              <span>
                <span
                  style={{
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 14,
                    fontWeight: 600,
                  }}
                >
                  {c.title}
                </span>
                <span
                  style={{
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 11,
                    color: "var(--text-tertiary)",
                    marginLeft: 8,
                  }}
                >
                  {c.paper}
                </span>
                <span
                  style={{
                    display: "block",
                    fontSize: 13,
                    lineHeight: 1.6,
                    color: "var(--text-secondary)",
                    marginTop: 3,
                  }}
                >
                  {c.line}
                </span>
              </span>
            </Link>
          ))}
        </div>
        <p style={{ marginTop: 14, fontSize: 13 }}>
          <Link href="/contributions" style={{ color: "var(--accent)" }}>
            See all contributions &rarr;
          </Link>
        </p>
      </section>

      {/* 5 — Open science / artifacts */}
      <section className="section">
        <p style={sectionLabel}>Open science</p>
        <h2 style={{ marginTop: 0 }}>Papers, data &amp; models</h2>
        <div
          style={{
            display: "grid",
            gap: 0,
            marginTop: 12,
            maxWidth: "80ch",
          }}
        >
          {artifactGroups.map((g, i) => (
            <div
              key={g.label}
              style={{
                display: "grid",
                gridTemplateColumns: "minmax(180px, 220px) 1fr",
                gap: 18,
                padding: "14px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--border)",
                alignItems: "start",
              }}
            >
              <div>
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 7,
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 13,
                    fontWeight: 600,
                  }}
                >
                  {g.label === "Datasets on HuggingFace" ||
                  g.label === "Models on HuggingFace" ? (
                    <Database size={14} style={{ color: "var(--accent)" }} />
                  ) : (
                    <FileText size={14} style={{ color: "var(--accent)" }} />
                  )}
                  {g.label}
                </div>
                <p
                  style={{
                    margin: "4px 0 0",
                    fontSize: 12,
                    lineHeight: 1.5,
                    color: "var(--text-tertiary)",
                  }}
                >
                  {g.blurb}
                </p>
              </div>
              <ul
                style={{
                  margin: 0,
                  padding: 0,
                  listStyle: "none",
                  display: "grid",
                  gap: 6,
                }}
              >
                {g.links.map((l) =>
                  l.internal ? (
                    <li key={l.href}>
                      <Link
                        href={l.href}
                        style={{
                          color: "var(--accent)",
                          fontFamily: "var(--font-mono-stack)",
                          fontSize: 13,
                        }}
                      >
                        {l.label} &rarr;
                      </Link>
                    </li>
                  ) : (
                    <li key={l.href}>
                      <a
                        href={l.href}
                        target="_blank"
                        rel="noopener noreferrer"
                        style={{
                          display: "inline-flex",
                          alignItems: "center",
                          gap: 5,
                          color: "var(--accent)",
                          fontFamily: "var(--font-mono-stack)",
                          fontSize: 13,
                          overflowWrap: "anywhere",
                        }}
                      >
                        {l.label}
                        <ExternalLink size={12} />
                      </a>
                    </li>
                  ),
                )}
              </ul>
            </div>
          ))}
        </div>
      </section>

      {/* 6 — Deep-dive navigation */}
      <section className="section">
        <p style={sectionLabel}>Go deeper</p>
        <h2 style={{ marginTop: 0 }}>Explore the program</h2>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(240px, 1fr))",
            gap: 0,
            marginTop: 10,
            borderTop: "1px solid var(--border)",
          }}
        >
          {deepDives.map((d) => (
            <Link
              key={d.href}
              href={d.href}
              style={{
                display: "block",
                padding: "14px 16px 14px 0",
                borderBottom: "1px solid var(--border)",
                textDecoration: "none",
                color: "var(--text)",
              }}
            >
              <span
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: 6,
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: 14,
                  fontWeight: 600,
                }}
              >
                {d.title}
                <ArrowRight size={13} style={{ color: "var(--accent)" }} />
              </span>
              <span
                style={{
                  display: "block",
                  fontSize: 12.5,
                  lineHeight: 1.55,
                  color: "var(--text-secondary)",
                  marginTop: 4,
                  maxWidth: "40ch",
                }}
              >
                {d.blurb}
              </span>
            </Link>
          ))}
        </div>
      </section>

      {/* 7 — Live status (secondary, compact) */}
      <section
        className="section"
        aria-label="Program status"
        style={{
          marginTop: 8,
          paddingTop: 22,
          borderTop: "1px solid var(--border)",
        }}
      >
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            alignItems: "center",
            gap: 12,
          }}
        >
          <FlaskConical size={15} style={{ color: "var(--accent)" }} />
          <span style={sectionLabel}>Program status</span>
          <span
            style={{
              fontFamily: "var(--font-mono-stack)",
              fontSize: 12,
              fontWeight: 600,
              color: readinessColor(avgReadiness),
            }}
          >
            {avgReadiness}% average readiness
          </span>
        </div>
        <p
          style={{
            margin: "10px 0 0",
            fontSize: 13.5,
            lineHeight: 1.65,
            color: "var(--text-secondary)",
            maxWidth: "74ch",
          }}
        >
          All six papers are drafted, internally peer-reviewed across multiple
          independent models, and have passed repeated adversarial review rounds
          with their numbers reproduced from committed code. The remaining step is
          the author&apos;s final sign-off and a coordinated arXiv submission — the
          science is in place; what&apos;s left is publication logistics.
        </p>
        <div className="mt-4 flex flex-wrap gap-2">
          <Button asChild size="sm" variant="outline">
            <Link href="/status">Full research status &rarr;</Link>
          </Button>
          <Button asChild size="sm" variant="outline">
            <Link href="/activity">Activity feed &rarr;</Link>
          </Button>
          <Button asChild size="sm" variant="outline">
            <Link href="/reviews">Review program &rarr;</Link>
          </Button>
        </div>
      </section>
    </>
  );
}
