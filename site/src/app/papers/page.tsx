import type { Metadata } from "next";
import Link from "next/link";
import { papers, researchPrograms, type Paper } from "@/data/papers";
import { getLivePapers, displayVersion } from "@/lib/livePapers";
import { MathText } from "@/components/MathText";
import { Band, PageHeader, DataTable, type DataTableColumn } from "@/components/primitives";

export const metadata: Metadata = {
  title: "All works",
  description:
    "Every BigBounce paper, note, software release, and data release in one flat, sortable list — with a plain-English purpose line for each.",
};

type PaperRole = "lead" | "specialist" | "companion" | "supporting release";

function paperRole(paper: Paper): PaperRole {
  const isLead = researchPrograms.some((program) => program.leadSlug === paper.slug);
  if (isLead) return "lead";
  const role = paper.publicationRole.toLowerCase();
  if (role.includes("companion")) return "companion";
  if (role.includes("supporting data release") || role.includes("supporting release")) {
    return "supporting release";
  }
  return "specialist";
}

function trackForSlug(slug: string) {
  return researchPrograms.find(
    (program) => program.leadSlug === slug || program.supportSlugs.includes(slug),
  );
}

const ROLE_LABEL: Record<PaperRole, string> = {
  lead: "Lead",
  specialist: "Specialist",
  companion: "Companion",
  "supporting release": "Supporting release",
};

interface WorkRow {
  paper: Paper;
  trackTitle: string;
  trackId: string;
  version: string;
  readiness: number;
  state: string;
}

const columns: DataTableColumn<WorkRow>[] = [
  {
    key: "work",
    header: "Work",
    render: (row) => (
      <Link href={`/papers/${row.paper.slug}`} className="works-table-title-link">
        <span className="works-table-title">
          <MathText>{row.paper.title}</MathText>
        </span>
        <span className="row-purpose">{row.paper.plainTitle}</span>
      </Link>
    ),
  },
  {
    key: "kind",
    header: "Kind",
    render: (row) => ROLE_LABEL[paperRole(row.paper)],
  },
  { key: "track", header: "Track", accessor: (row) => row.trackTitle },
  { key: "version", header: "Version", mono: true, accessor: (row) => row.version },
  {
    key: "readiness",
    header: "Readiness",
    mono: true,
    align: "right",
    accessor: (row) => `${row.readiness}%`,
  },
  { key: "state", header: "State", accessor: (row) => row.state },
  {
    key: "pdf",
    header: "PDF",
    render: (row) => {
      const pdf = row.paper.artifacts.find(
        (a) => a.kind === "primary" && a.href.toLowerCase().endsWith(".pdf"),
      );
      return pdf ? (
        <a href={pdf.href} target="_blank" rel="noreferrer" className="works-table-pdf-link">
          Read
        </a>
      ) : (
        <span className="row-purpose">&mdash;</span>
      );
    },
  },
];

function stateLabel(status: string | null): string {
  switch (status) {
    case "active-drive-to-100":
      return "active";
    case "paused-houston-external":
      return "paused";
    case "submitted-arxiv":
      return "submitted";
    case "in-revision":
      return "in revision";
    case "accepted":
      return "accepted";
    default:
      return "draft";
  }
}

export default async function PapersIndexPage() {
  const live = await getLivePapers();
  const liveBySlug = new Map(live.map((p) => [p.slug, p]));

  const rows: WorkRow[] = papers.map((paper) => {
    const track = trackForSlug(paper.slug);
    const livePaper = liveBySlug.get(paper.slug);
    return {
      paper,
      trackTitle: track?.title ?? "Unassigned",
      trackId: track?.id ?? "z",
      version: displayVersion(livePaper?.currentVersion ?? paper.version),
      readiness: livePaper?.readinessComputed ?? paper.readiness,
      state: stateLabel(livePaper?.status ?? null),
    };
  });
  rows.sort(
    (a, b) => a.trackId.localeCompare(b.trackId) || b.readiness - a.readiness,
  );

  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow="Works"
          title="All works"
          lead="The complete flat list of every paper, note, software release, and data release in the portfolio — sorted by track, then readiness. Prefer the question-first view? See research by track."
          actions={[{ label: "Research tracks", href: "/research" }]}
        />
      </Band>
      <Band width="content">
        <DataTable columns={columns} rows={rows} rowKey={(r) => r.paper.slug} />
      </Band>
    </>
  );
}
