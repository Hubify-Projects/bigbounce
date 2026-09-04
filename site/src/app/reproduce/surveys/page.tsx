import type { Metadata } from "next";
import Link from "next/link";
import { surveys, type Survey } from "@/data/surveys";
import {
  Band,
  PageHeader,
  StatRow,
  EvidenceChip,
  DataTable,
  type DataTableColumn,
} from "@/components/primitives";

export const metadata: Metadata = {
  title: "Survey data & QC",
  description:
    "Every astronomical survey the anomaly-detection pipeline has touched, and its current QC status — including why zero of them currently clear the survey-hard publication bar.",
};

function sourceCountValue(sources: string) {
  const n = parseFloat(sources.replace(/[^\d.]/g, ""));
  const mult = sources.includes("M") ? 1e6 : sources.includes("K") ? 1e3 : 1;
  return n * mult;
}

const columns: DataTableColumn<Survey>[] = [
  {
    key: "survey",
    header: "Survey",
    render: (s) => (
      <Link href={`/reproduce/surveys/${s.slug}`}>
        <span>{s.name}</span>
        <span className="row-purpose" style={{ display: "block", fontSize: 12.5 }}>
          {s.wavelength.split(" ")[0]}
        </span>
      </Link>
    ),
  },
  { key: "sources", header: "Sources", mono: true, accessor: (s) => s.sources },
  {
    key: "candidates",
    header: "Pre-dedup candidates",
    mono: true,
    accessor: (s) => (s.anomalies > 0 ? s.anomalies.toLocaleString() : "suppressed (superseded)"),
  },
  {
    key: "qc",
    header: "Survey-hard bar",
    render: (s) => (
      <EvidenceChip grade={s.qcStatus === "pass" ? "measured" : "null"} label={s.qcStatus === "pass" ? "clears" : "does not clear"} />
    ),
  },
  {
    key: "note",
    header: "Why",
    render: (s) => (
      <span style={{ whiteSpace: "normal", maxWidth: "40ch", display: "inline-block", color: "var(--ink-3)" }}>
        {s.qcNote}
      </span>
    ),
  },
];

export default function SurveysHubPage() {
  const totalSources = surveys.reduce((sum, s) => sum + sourceCountValue(s.sources), 0);
  const passCount = surveys.filter((s) => s.qcStatus === "pass").length;
  const sorted = [...surveys].sort((a, b) => sourceCountValue(b.sources) - sourceCountValue(a.sources));

  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow="Reproducibility &middot; surveys"
          title="Survey data & QC"
          lead="Every astronomical survey the anomaly-detection program has processed, organized by whether it clears the survey-hard publication bar — a strict standard, not a pass/fail on the survey's real astronomical data."
          actions={[{ label: "Reproduce this lab", href: "/reproduce" }]}
        />
      </Band>

      <Band width="content">
        <StatRow
          items={[
            { value: `${(totalSources / 1e6).toFixed(1)}M`, label: "Sources scanned" },
            { value: surveys.length, label: "Surveys touched" },
            { value: `${passCount} of ${surveys.length}`, label: "Clear the survey-hard bar" },
          ]}
        />
        <p style={{ maxWidth: "72ch", color: "var(--ink-2)", marginTop: 16, fontSize: 14 }}>
          <strong style={{ color: "var(--ink)" }}>
            {passCount} of {surveys.length} surveys currently clear the survey-hard bar
          </strong>{" "}
          — this is a disclosed null, not a pipeline failure. Every row below is a historical,
          unreconciled exploratory-pipeline record: candidate counts are legacy artifacts of an
          earlier autoencoder scan, superseded by the current DESI DR1 anomaly-discovery flagship
          (the 1,244-object v2 catalogue on{" "}
          <Link href="/reproduce#releases">/reproduce#releases</Link>). None of these legacy runs
          is asserted as a current, publication-grade catalog, and none provides evidence for a
          bounce on its own — that is exactly why the bar reads zero, and it is stated here rather
          than left unexplained.
        </p>
      </Band>

      <Band width="content">
        <DataTable columns={columns} rows={sorted} rowKey={(s) => s.slug} />
      </Band>
    </>
  );
}
