import { getPaperBySlug, researchPrograms } from "@/data/papers";
import { liveStatus } from "@/data/live-status";
import { Button } from "@/components/ui/button";
import { getLivePapers, displayVersion } from "@/lib/livePapers";
import {
  ArrowRight,
  Database,
  ExternalLink,
  FileText,
  FlaskConical,
} from "lucide-react";
import Link from "next/link";

// ──────────────────────────────────────────────────────────────────────
// First-time-visitor homepage. The science questions lead; candidate packages,
// review evidence, and readiness remain available as supporting material.
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
    tier: "N2",
    paper: "P1A",
    title: "Minimal-ECH Boundary Note",
    line: "A convention-audited result for a narrow minimal Einstein–Cartan–Holst branch, without claiming a universal no-go theorem or dark-energy model.",
  },
  {
    id: "physics-commutator",
    tier: "N2",
    paper: "P2",
    title: "Exact Ordered Four-Vertex Polynomial",
    line: "The exact contraction-phase re-summation gives coefficients (3, 1, −9, 5, −33, 9) and f_NL = −35/16 under the stated action and conventions.",
  },
  {
    id: "matter-bounce-fnl",
    tier: "N2",
    paper: "P2",
    title: "Matter-Contraction Non-Gaussianity",
    line: "The primary result is an exact algebraic amplitude; survey sensitivity is explicitly conditional on bounce transmission, covariance, and nuisance assumptions.",
  },
  {
    id: "anomaly-catalog",
    tier: "N2",
    paper: "P3",
    title: "Public-ID Anomaly-List Recovery",
    line: "181 public DESI DR1 TARGETIDs recovered from a frozen historical anomaly list — a reproducible archive/provenance product, not a detection or novelty claim.",
  },
  {
    id: "chirality-catalog",
    tier: "N2",
    paper: "P4",
    title: "8.47M-Galaxy Chirality Catalog",
    line: "8,474,531 observed labels; the quality-controlled 890,069-row primary result is null-consistent (z_mom=+0.635, rank p=0.23768), not a physical-parity bound.",
  },
  {
    id: "desi-environment",
    tier: "N2",
    paper: "P5",
    title: "DESI Chirality × Environment Null",
    line: "An exploratory void/non-void classifier-label contrast is consistent with zero; it is not a physical environment-independence result.",
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
    links: [{ label: "Browse papers & artifacts", href: "/paper", internal: true }],
  },
  {
    label: "Datasets on HuggingFace",
    blurb: "Public catalog roots: the anomaly catalog is historical provenance pending a clean rebuild; the chirality catalog supports P4 and P5.",
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
    blurb: "Released checkpoint roots: BigAE is historical provenance; the chirality model supports observed-label reproducibility within declared limits.",
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
  const avgReadiness = Math.round(
    livePapers.reduce((acc, p) => acc + p.readinessComputed, 0) /
      Math.max(1, livePapers.length),
  );

  return (
    <>
      {/* 1 — Science story */}
      <section className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Bounce cosmology · live research program
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 650 }}>
          Was there a bounce before the Big Bang?
        </h1>
        <p className="subtitle">
          This is an open research program testing what a nonsingular
          <strong> Big Bounce</strong> cosmology can actually predict and what
          archival survey data can independently establish. The theory,
          spectral-anomaly, and galaxy-chirality programs share tools and
          motivation, but the survey catalogs are not presented as detections of
          a bounce.
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
          Three research programs connect theory, discovery, and observation.
          Their lead results, candidate packages, data, and review evidence are
          public — but a finished package is not automatically a flagship paper.
        </p>
        <div className="mt-5 flex flex-wrap gap-2">
          <Button asChild>
            <Link href="/explained">
              Start with the explainer <ArrowRight size={15} />
            </Link>
          </Button>
          <Button asChild variant="outline">
            <Link href="/paper">Browse papers &amp; artifacts</Link>
          </Button>
          <Button asChild variant="outline">
            <Link href="/publish">See the publication plan</Link>
          </Button>
        </div>
      </section>

      {/* 2 — Research programs */}
      <section className="section" style={{ marginTop: 8 }}>
        <p style={sectionLabel}>Research programs</p>
        <h2 style={{ marginTop: 0 }}>Three questions, three lead results</h2>
        <p style={{ marginTop: 4, fontSize: 14, lineHeight: 1.7, maxWidth: "66ch" }}>
          The portfolio is organized around scientific questions, not a fixed
          paper count. Supporting notes, software, and exploratory companions
          remain available with their evidence, but do not displace the lead result.
        </p>
        <div style={{ display: "grid", gap: 0, marginTop: 16, maxWidth: "76ch" }}>
          {researchPrograms.map((program, i) => {
            const lead = program.leadSlug ? getPaperBySlug(program.leadSlug) : null;
            const supports = program.supportSlugs
              .flatMap((slug) => {
                const paper = getPaperBySlug(slug);
                return paper ? [paper] : [];
              });
            return (
            <div
              key={program.id}
              style={{
                padding: "18px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--border)",
              }}
            >
              <p style={sectionLabel}>{program.status}</p>
              <h3 style={{ margin: 0, fontFamily: "var(--font-mono-stack)", fontSize: 17 }}>{program.title}</h3>
              <p style={{ marginTop: 6, fontSize: 14, lineHeight: 1.65 }}><strong>Question:</strong> {program.question}</p>
              <p style={{ marginTop: 4, fontSize: 13.5, lineHeight: 1.6, color: "var(--text-secondary)" }}><strong>Current result:</strong> {program.result}</p>
              <p style={{ marginTop: 4, fontSize: 13, lineHeight: 1.6, color: "var(--text-tertiary)" }}><strong>Boundary:</strong> {program.limitation}</p>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 12, marginTop: 9, fontSize: 13 }}>
                {lead && <Link href={`/papers/${lead.slug}`} style={{ color: "var(--accent)" }}>Lead: {lead.number} · {lead.title} &rarr;</Link>}
                {supports.map((paper) => <Link key={paper.slug} href={`/papers/${paper.slug}`} style={{ color: "var(--text-secondary)" }}>Support: {paper.number} &middot; {paper.title}</Link>)}
              </div>
            </div>
            );
          })}
        </div>
      </section>

      {/* 3 — Candidate packages, scannable (readiness from getLivePapers) */}
      <section className="section">
        <p style={sectionLabel}>Evidence library</p>
        <h2 style={{ marginTop: 0 }}>Papers, software, and technical records</h2>
        <p style={{ marginTop: 4, fontSize: 13.5, lineHeight: 1.6, color: "var(--text-secondary)", maxWidth: "70ch" }}>
          These candidate packages preserve their PDFs, artifacts, and version-specific review evidence. Their readiness is evidence status, not a claim that every package is science-complete or awaiting endorsement alone.
        </p>
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
          Evidence and review state remain useful, but publication follows the
          scientific architecture: P2 and P4 are lead results; P1A and P1B are
          specialist outputs; P5 is a standalone companion; P3 is an integrated
          supporting data release; and the anomaly flagship is a parallel rebuild.
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
