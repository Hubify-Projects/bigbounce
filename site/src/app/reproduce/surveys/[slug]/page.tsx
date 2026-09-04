import { surveys, getSurveyBySlug } from "@/data/surveys";
import { MathText } from "@/components/MathText";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  Band,
  PageHeader,
  StatRow,
  EvidenceChip,
  RowList,
  DataTable,
  type DataTableColumn,
} from "@/components/primitives";

export function generateStaticParams() {
  return surveys.map((s) => ({ slug: s.slug }));
}

type PageParams = Promise<{ slug: string }>;

export async function generateMetadata({ params }: { params: PageParams }): Promise<Metadata> {
  const { slug } = await params;
  const survey = getSurveyBySlug(slug);
  if (!survey) return { title: "Not found" };
  return {
    title: survey.name,
    description: `${survey.name}: ${survey.sources} scanned. ${survey.qcNote}`,
  };
}

interface AnomalyRow {
  rank: number;
  ra: number;
  dec: number;
  score: number;
  type?: string;
}

const anomalyColumns: DataTableColumn<AnomalyRow>[] = [
  { key: "rank", header: "Rank", mono: true, accessor: (a) => `#${a.rank}` },
  { key: "ra", header: "RA", mono: true, accessor: (a) => `${a.ra.toFixed(1)}°` },
  { key: "dec", header: "Dec", mono: true, accessor: (a) => `${a.dec.toFixed(1)}°` },
  { key: "score", header: "Score", mono: true, accessor: (a) => a.score.toFixed(2) },
  { key: "type", header: "Type", accessor: (a) => a.type ?? "—" },
];

export default async function SurveyDetailPage({ params }: { params: PageParams }) {
  const { slug } = await params;
  const survey = getSurveyBySlug(slug);
  if (!survey) notFound();

  const related = survey.connections.filter((c) => c.href.startsWith("/surveys/"));
  const external = survey.connections.filter((c) => !c.href.startsWith("/surveys/"));

  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow={`Survey data & QC → ${survey.shortName}`}
          title={survey.name}
          lead={<MathText>{survey.description}</MathText>}
          meta={[
            { label: "sources", value: survey.sources, mono: true },
            { label: "band", value: survey.wavelength.split(" ")[0] },
          ]}
          actions={[{ label: "All surveys", href: "/reproduce/surveys" }]}
        />
        <EvidenceChip grade={survey.qcStatus === "pass" ? "measured" : "null"} label={survey.qcNote} />
      </Band>

      <Band width="content">
        <StatRow
          items={[
            { value: survey.sources, label: "Sources" },
            { value: survey.anomalies.toLocaleString(), label: "Pre-dedup candidates" },
            { value: survey.anomalyRate, label: "Rate" },
            { value: survey.cost, label: "Est. cost" },
            { value: survey.runtime, label: "Wall-clock" },
          ]}
        />
      </Band>

      <Band tone="alt" width="content">
        <h2 className="page-header-title" style={{ fontSize: 20 }}>
          Key findings
        </h2>
        <div>
          {survey.keyFindings.map((finding, i) => (
            <p
              key={i}
              className="mono"
              style={{
                fontSize: 14,
                color: "var(--ink-2)",
                padding: "10px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--rule)",
              }}
            >
              <span style={{ color: "var(--ink-3)" }}>{String(i + 1).padStart(2, "0")}</span>{" "}
              <MathText>{finding}</MathText>
            </p>
          ))}
        </div>
      </Band>

      <Band width="content">
        <h2 className="page-header-title" style={{ fontSize: 20 }}>
          Pipeline
        </h2>
        <DataTable
          columns={[
            { key: "k", header: "Field", accessor: (r: [string, string]) => r[0] },
            { key: "v", header: "Value", mono: true, accessor: (r: [string, string]) => r[1] },
          ]}
          rows={[
            ["Model", survey.pipeline],
            ["Wavelength", survey.wavelength],
            ["Cost", survey.cost],
            ["Runtime", survey.runtime],
          ]}
          rowKey={(r) => r[0]}
        />
      </Band>

      {survey.topAnomalies.length > 0 && (
        <Band tone="alt" width="content">
          <h2 className="page-header-title" style={{ fontSize: 20 }}>
            Top candidates
          </h2>
          <DataTable columns={anomalyColumns} rows={survey.topAnomalies} rowKey={(a) => a.rank} />
        </Band>
      )}

      <Band width="content">
        <h2 className="page-header-title" style={{ fontSize: 20 }}>
          Follow-up queue
        </h2>
        <div>
          {survey.followUpTasks.map((task, i) => (
            <p
              key={i}
              style={{
                fontSize: 14,
                color: "var(--ink-2)",
                padding: "10px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--rule)",
              }}
            >
              <MathText>{task}</MathText>
            </p>
          ))}
        </div>
      </Band>

      <Band tone="alt" width="content">
        <h2 className="page-header-title" style={{ fontSize: 20 }}>
          Links
        </h2>
        <RowList
          items={[
            ...survey.paperRefs.map((ref) => ({ title: ref, href: "/papers" })),
            ...related.map((c) => ({ title: c.label, href: c.href })),
            ...external.map((c) => ({ title: c.label, href: c.href })),
          ]}
        />
        <p style={{ marginTop: 16 }}>
          <Link href="/reproduce/surveys">&larr; All surveys</Link>
        </p>
      </Band>
    </>
  );
}
