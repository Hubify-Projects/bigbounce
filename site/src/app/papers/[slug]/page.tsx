import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { papers, getPaperBySlug } from "@/data/papers";
import { getLivePapers, getFiguresForPaper, displayVersion } from "@/lib/livePapers";
import { sortedReviewRounds, type PaperId } from "@/data/reviewTimeline";
import { reproExperiments } from "@/data/repro";
import { paperSlugForCode } from "@/lib/reproLab";
import { MathText } from "@/components/MathText";
import { Band, PageHeader, EvidenceChip, type EvidenceGrade } from "@/components/primitives";
import { contributions } from "@/data/tracks";
import { CONTRIBUTION_TYPE_LABEL, CONTRIBUTION_TYPE_HINT } from "@/lib/contributionTypes";
import { ExternalReviewPanel } from "@/components/ExternalReviewPanel";
import { PaperFigureGallery } from "./PaperFigureGallery";

export function generateStaticParams() {
  return papers.map((p) => ({ slug: p.slug }));
}

type PageParams = Promise<{ slug: string }>;

export async function generateMetadata({ params }: { params: PageParams }): Promise<Metadata> {
  const { slug } = await params;
  const paper = getPaperBySlug(slug);
  if (!paper) return { title: "Not found" };
  return { title: paper.plainTitle, description: paper.plainTitle };
}

const SLUG_TO_PAPER_ID: Record<string, PaperId> = {
  "paper-1a": "P1A",
  "paper-1b": "P1B",
  "paper-2": "P2",
  "paper-3": "P3",
  "paper-4": "P4",
  "paper-5": "P5",
};

/** Pulls "md5 <hex>" out of a paper's pdfMeta artifact line for the header meta row. */
function extractMd5(pdfMeta: string): string | null {
  const m = pdfMeta.match(/md5 ([0-9a-f]{6,32})/i);
  return m ? m[1].slice(0, 12) : null;
}

function stateLabel(status: string | null, staticVariant: string): string {
  switch (status) {
    case "active-drive-to-100":
      return "active";
    case "paused-houston-external":
      return "paused — author review";
    case "submitted-arxiv":
      return "submitted to arXiv";
    case "in-revision":
      return "in revision";
    case "accepted":
      return "accepted";
    default:
      return staticVariant === "green" ? "ready" : staticVariant === "blue" ? "active" : "draft";
  }
}

/** Heuristic evidence grade for a one-line result claim — used only until a
 * per-result grade field exists on Paper. Nulls stay "null" (never red). */
function claimGrade(text: string): EvidenceGrade {
  const t = text.toLowerCase();
  if (t.includes("null") || t.includes("no dipole") || t.includes("excludes") || t.includes("rules out")) return "null";
  if (t.includes("derive") || t.includes("exact") || t.includes("amplitude")) return "derived";
  if (t.includes("confirm") || t.includes("measure")) return "measured";
  return "open";
}

export default async function PaperDetailPage({ params }: { params: PageParams }) {
  const { slug } = await params;
  const paper = getPaperBySlug(slug);
  if (!paper) notFound();

  const [liveStates, figures] = await Promise.all([
    getLivePapers(),
    getFiguresForPaper(slug),
  ]);
  const live = liveStates.find((p) => p.slug === slug);
  const focusAreas = live?.focusAreas ?? [];
  const readiness = live?.readinessComputed ?? paper.readiness;
  const version = displayVersion(live?.currentVersion ?? paper.version);
  const lastUpdated = live?.lastUpdated ?? paper.lastUpdated;
  const state = stateLabel(live?.status ?? null, paper.statusVariant);
  const openSummary = live
    ? `${live.openBlockers}B / ${live.openMajors}M / ${live.openMinors}m / ${live.openCaveats}C open`
    : null;

  const inPaperFigures = figures.filter((f) => (f.status ?? "in-paper") === "in-paper");
  const candidateFigures = figures.filter((f) => f.status === "candidate");

  const paperId = SLUG_TO_PAPER_ID[slug];
  const paperRounds = paperId ? sortedReviewRounds().filter((r) => r.papers.includes(paperId)) : [];
  const recentRounds = paperRounds.slice(0, 5);

  const manifests = reproExperiments.filter((e) => paperSlugForCode(e.paper) === slug);

  const pdfArtifactRaw = paper.artifacts.find((a) => a.kind === "primary" && a.href.toLowerCase().endsWith(".pdf"));
  const pdfHref = live?.sitePdfPath ?? pdfArtifactRaw?.href ?? null;
  const texArtifact = paper.artifacts.find((a) => a.label?.toLowerCase().includes("latex"));
  const doiLink = paper.artifacts.find((a) => a.label?.toLowerCase().includes("doi") || a.label?.toLowerCase().includes("zenodo") || a.label?.toLowerCase().includes("arxiv"));

  const role = paper.publicationRole.toLowerCase();
  const kind = role.includes("software")
    ? "Software"
    : role.includes("data release")
      ? "Data release"
      : role.includes("note")
        ? "Note"
        : "Paper";

  return (
    <>
      <Band width="prose">
        <p className="row-purpose" style={{ marginBottom: 4 }}>
          <Link href="/papers">All works</Link> &rarr; {kind}
        </p>
        <PageHeader
          eyebrow={kind}
          title={<MathText>{paper.title}</MathText>}
          lead={paper.plainTitle}
          meta={[
            { label: "version", value: version, mono: true },
            { label: "date", value: lastUpdated ?? "—", mono: true },
            { label: "pages", value: paper.pages, mono: true },
            { label: "md5", value: extractMd5(paper.pdfMeta) ?? "—", mono: true },
            { label: "target", value: paper.target, mono: true },
          ]}
        />
        {contributions
          .filter((c) => c.paperSlugs?.includes(paper.slug))
          .map((c) => (
            <span
              key={c.id}
              className="evidence-chip evidence-chip-type"
              style={{ marginRight: 12 }}
              title={CONTRIBUTION_TYPE_HINT[c.contributionType]}
            >
              <span className="evidence-chip-dot" aria-hidden="true" />
              {CONTRIBUTION_TYPE_LABEL[c.contributionType]} &middot; {c.tier}
            </span>
          ))}
      </Band>

      <Band width="prose">
        <div className="page-header-actions" style={{ borderTop: "1px solid var(--rule)", borderBottom: "1px solid var(--rule)", padding: "12px 0" }}>
          {pdfHref && <a href={pdfHref} target="_blank" rel="noreferrer" className="page-header-action">Read PDF</a>}
          {doiLink && <a href={doiLink.href} target="_blank" rel="noreferrer" className="page-header-action">{doiLink.label.toLowerCase().includes("arxiv") ? "arXiv" : "DOI"}</a>}
          {texArtifact && <a href={texArtifact.href} target="_blank" rel="noreferrer" className="page-header-action">Source .tex</a>}
          {manifests.length > 0 && <a href="#reproduce" className="page-header-action">Reproduction manifest</a>}
          {(inPaperFigures.length + candidateFigures.length) > 0 && <a href="#figures" className="page-header-action">Figures</a>}
        </div>
      </Band>

      <Band width="prose">
        <h2 className="section-h2">Abstract</h2>
        <p className="prose-body"><MathText>{paper.description}</MathText></p>
      </Band>

      <Band width="prose">
        <h2 className="section-h2">Result summary</h2>
        <ul className="result-summary-list">
          {paper.keyResults.slice(0, 4).map((r, i) => (
            <li key={i}>
              <EvidenceChip grade={claimGrade(r)} />
              <span><MathText>{r}</MathText></span>
            </li>
          ))}
        </ul>
      </Band>

      {(inPaperFigures.length > 0 || candidateFigures.length > 0) && (
        <Band width="prose" id="figures">
          <h2 className="section-h2">Figures</h2>
          <PaperFigureGallery inPaper={inPaperFigures} candidates={candidateFigures} paperNumber={paper.number} />
        </Band>
      )}

      <Band width="prose">
        <h2 className="section-h2">Readiness</h2>
        <div className="readiness-line">
          <strong className="readiness-line-value mono">{readiness}%</strong>
          <div className="readiness-line-track">
            <div className="readiness-line-fill" style={{ width: `${readiness}%` }} />
          </div>
        </div>
        {openSummary && <p className="row-purpose mono">{openSummary}</p>}
        <p className="row-purpose">
          Readiness is publication readiness only — science, evidence, review convergence,
          packaging, and Houston&rsquo;s final sign-off. Venue and submission are tracked
          separately below, and never subtract from this number (directive P).
        </p>
      </Band>

      <Band width="prose">
        <h2 className="section-h2">Publishing</h2>
        <p className="row-purpose">Not part of readiness.</p>
        <div className="page-header-meta mono" style={{ marginTop: 8 }}>
          <span className="page-header-meta-item"><span className="page-header-meta-label">target venue</span> {paper.target}</span>
          <span className="page-header-meta-item"><span className="page-header-meta-label">state</span> {state}</span>
          {live?.houstonSignOff && (
            <span className="page-header-meta-item"><span className="page-header-meta-label">sign-off</span> {live.houstonSignOff}</span>
          )}
        </div>
      </Band>

      {recentRounds.length > 0 && (
        <Band width="prose">
          <details className="review-evidence-details">
            <summary className="section-h2" style={{ cursor: "pointer", display: "inline-block" }}>
              Review evidence ({paperRounds.length} rounds)
            </summary>
            <div className="row-list" style={{ marginTop: 12 }}>
              {recentRounds.map((r) => (
                <div key={r.id} className="row" style={{ cursor: "default" }}>
                  <span className="row-main">
                    <span className="row-title mono">{r.id}</span>
                    <span className="row-purpose">{r.title}</span>
                  </span>
                  <span className="row-right mono">{r.dateISO}</span>
                </div>
              ))}
            </div>
            <p className="row-purpose" style={{ marginTop: 8 }}>
              Automated review is a gate on publication readiness, not a product.{" "}
              <Link href={`/reviews?papers=${paperId}`}>Full review timeline &rarr;</Link>
            </p>
            {pdfHref && (
              <ExternalReviewPanel
                paperNumber={paper.number}
                paperTitle={paper.title}
                paperVersion={version}
                paperPath={texArtifact?.href.replace(/^https:\/\/github\.com\/[^/]+\/[^/]+\/blob\/[^/]+\//, "") ?? "(see GitHub LaTeX source artifact)"}
                pdfHref={pdfHref}
                pdfMeta={paper.pdfMeta}
                focusAreas={focusAreas}
              />
            )}
          </details>
        </Band>
      )}

      {manifests.length > 0 && (
        <Band width="prose" id="reproduce">
          <h2 className="section-h2">Reproduce this</h2>
          <div className="row-list">
            {manifests.slice(0, 6).map((m) => (
              <div key={m.id} className="row" style={{ cursor: "default" }}>
                <span className="row-main">
                  <span className="row-title">{m.title}</span>
                  <span className="row-purpose">
                    {m.environment.hardware} &middot; est. {m.reproduction.est_wall_clock} &middot;{" "}
                    ${m.reproduction.est_cost_usd.toFixed(2)}
                  </span>
                </span>
                <span className="row-right mono">{m.status}</span>
              </div>
            ))}
          </div>
          <p className="row-purpose" style={{ marginTop: 8 }}>
            <Link href="/reproduce">Full reproduction manifests &rarr;</Link>
          </p>
        </Band>
      )}

      <Band width="prose">
        <h2 className="section-h2">Lineage</h2>
        <p className="prose-body">
          {paper.archivedInto
            ? `Archived — ${paper.archivedInto.note} See the current version at `
            : `${paper.publicationRole}. `}
          {paper.archivedInto && (
            <Link href={`/papers/${paper.archivedInto.successorSlug}`}>
              paper-{paper.archivedInto.successorSlug}
            </Link>
          )}
          {!paper.archivedInto && "This work does not claim beyond its stated target and scope above."}
        </p>
      </Band>
    </>
  );
}
