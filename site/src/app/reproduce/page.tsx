import type { Metadata } from "next";
import Link from "next/link";
import { reproPrograms, type ReproExperiment } from "@/data/repro";
import {
  labRollup,
  programRollup,
  programExperimentsInDagOrder,
  paperSlugForCode,
  formatCost,
  STATUS_LABEL,
} from "@/lib/reproLab";
import {
  Band,
  PageHeader,
  StatRow,
  DataTable,
  type DataTableColumn,
} from "@/components/primitives";

export const metadata: Metadata = {
  title: "Reproduce this lab",
  description:
    "Every BigBounce research program and every individual experiment carries a manifest — sealed inputs, exact entrypoints, compute venue, cost, and wall-clock — so a stranger, or Hubify, can reproduce it.",
};

interface ReleaseRow {
  work: string;
  slug: string | null;
  kind: string;
  host: string;
  link: string;
  note: string;
}

// Sourced 2026-09-04 from project-context/SSOT/PORTAL_KITS_2026-09-02.md
// (Zenodo DOI ledger), pipelines/p3_anomaly_engine/release/
// ANOMALY_CATALOGUE_RELEASE_v2_2026-09-03.md (HF/B2 mirrors), and
// project-context/SSOT/paper-a3m/status.md (NANOGrav KDE HF mirror).
const RELEASES: ReleaseRow[] = [
  {
    work: "Galaxy chirality catalog (8.47M DESI Legacy DR8 galaxies)",
    slug: "paper-4p",
    kind: "Zenodo dataset",
    host: "Zenodo",
    link: "https://doi.org/10.5281/zenodo.21461899",
    note: "concept DOI 10.5281/zenodo.21461898 · CC-BY-4.0",
  },
  {
    work: "Galaxy chirality catalog — HuggingFace mirror",
    slug: "paper-4p",
    kind: "Dataset mirror",
    host: "HuggingFace",
    link: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
    note: "bamfai/galaxy-chirality-catalog",
  },
  {
    work: "ECH Note (torsion no-go) — archival record",
    slug: "paper-1n",
    kind: "Zenodo archive",
    host: "Zenodo",
    link: "https://doi.org/10.5281/zenodo.21481838",
    note: "concept DOI 10.5281/zenodo.21481837 · CC-BY-4.0",
  },
  {
    work: "namaster-proof — paper archival record",
    slug: "paper-1b",
    kind: "Zenodo archive",
    host: "Zenodo",
    link: "https://doi.org/10.5281/zenodo.21481842",
    note: "concept DOI 10.5281/zenodo.21481841",
  },
  {
    work: "namaster-proof — software release v0.1.7",
    slug: "paper-1b",
    kind: "Software archive",
    host: "Zenodo",
    link: "https://doi.org/10.5281/zenodo.21481753",
    note: "commit-pinned source",
  },
  {
    work: "f_NL forecast — archival record",
    slug: "paper-2",
    kind: "Zenodo archive",
    host: "Zenodo",
    link: "https://doi.org/10.5281/zenodo.21461881",
    note: "concept DOI 10.5281/zenodo.21461880",
  },
  {
    work: "Multi-survey anomaly engine — archival record",
    slug: "paper-3",
    kind: "Zenodo archive",
    host: "Zenodo",
    link: "https://doi.org/10.5281/zenodo.21461888",
    note: "concept DOI 10.5281/zenodo.21461887",
  },
  {
    work: "DESI DR1 anomaly-score candidate catalogue (v2, 1,244 objects)",
    slug: null,
    kind: "Data release",
    host: "HuggingFace",
    link: "https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/tree/main/phase3_v2/2026-09-03",
    note: "bamfai/bigbounce-aug-011-clean-rerun · phase3_v2/2026-09-03/",
  },
  {
    work: "DESI DR1 anomaly-score candidate catalogue (v2) — Backblaze B2 mirror",
    slug: null,
    kind: "Data mirror",
    host: "Backblaze B2",
    link: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p3_anomaly_engine/release/ANOMALY_CATALOGUE_RELEASE_v2_2026-09-03.md",
    note: "bucket bigbounce · key prefix aug-011-clean-rerun/phase3_v2/2026-09-03/ — Zenodo DOI not yet minted, cited via pinned commit",
  },
  {
    work: "NANOGrav 15-yr HD free-spectrum KDE grids (Track A3 PTA input)",
    slug: "paper-a3m",
    kind: "External data mirror",
    host: "HuggingFace",
    link: "https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/tree/main/external/nanograv15yr_kde",
    note: "bamfai/bigbounce-aug-011-clean-rerun · external/nanograv15yr_kde/ · sourced from public Zenodo 10.5281/zenodo.8060824",
  },
  {
    work: "Repository source (every paper, pipeline, and manifest)",
    slug: null,
    kind: "Source",
    host: "GitHub",
    link: "https://github.com/Hubify-Projects/bigbounce",
    note: "Hubify-Projects/bigbounce · public, MIT-adjacent per repo license",
  },
];

function InputsCell({ inputs }: { inputs: ReproExperiment["inputs"] }) {
  if (inputs.length === 0) {
    return <span style={{ color: "var(--ink-3)" }}>internal derivation — no external input</span>;
  }
  return (
    <div style={{ whiteSpace: "normal", display: "grid", gap: 2, maxWidth: "26ch" }}>
      {inputs.map((input, i) => {
        const isUrl = typeof input.locator === "string" && /^https?:\/\//.test(input.locator);
        return (
          <div key={`${input.name}-${i}`}>
            {isUrl ? (
              <a href={input.locator!} target="_blank" rel="noreferrer">
                {input.name}
              </a>
            ) : (
              <span>{input.name}</span>
            )}
          </div>
        );
      })}
    </div>
  );
}

function ScriptsCell({ code }: { code: ReproExperiment["code"] }) {
  if (code.length === 0) {
    return <span style={{ color: "var(--ink-3)" }}>&mdash;</span>;
  }
  return (
    <div style={{ whiteSpace: "normal", display: "grid", gap: 2, maxWidth: "34ch" }} className="mono">
      {code.map((c, i) => (
        <div key={`${c.path}-${i}`}>{c.entrypoint}</div>
      ))}
    </div>
  );
}

const experimentColumns: DataTableColumn<{
  entry: { id: string; depends_on: string[] };
  experiment: ReproExperiment;
}>[] = [
  {
    key: "experiment",
    header: "Experiment",
    render: ({ entry, experiment }) => (
      <div style={{ whiteSpace: "normal", maxWidth: "30ch" }}>
        <div>{experiment.title}</div>
        <div className="mono" style={{ fontSize: 11, color: "var(--ink-3)", marginTop: 2 }}>
          {experiment.id}
          {entry.depends_on.length > 0 && <> &middot; depends on {entry.depends_on.join(", ")}</>}
        </div>
      </div>
    ),
  },
  {
    key: "inputs",
    header: "Inputs",
    render: ({ experiment }) => <InputsCell inputs={experiment.inputs} />,
  },
  {
    key: "scripts",
    header: "Scripts",
    render: ({ experiment }) => <ScriptsCell code={experiment.code} />,
  },
  {
    key: "venue",
    header: "Venue",
    accessor: ({ experiment }) => experiment.reproduction.recommended_venue,
  },
  {
    key: "cost",
    header: "Est. cost",
    mono: true,
    accessor: ({ experiment }) => formatCost(experiment.reproduction.est_cost_usd),
  },
  {
    key: "wallclock",
    header: "Wall-clock",
    mono: true,
    accessor: ({ experiment }) => experiment.reproduction.est_wall_clock,
  },
  {
    key: "state",
    header: "State",
    accessor: ({ experiment }) => STATUS_LABEL[experiment.status],
  },
];

const releaseColumns: DataTableColumn<ReleaseRow>[] = [
  {
    key: "work",
    header: "Release",
    render: (row) =>
      row.slug ? (
        <Link href={`/papers/${row.slug}`}>{row.work}</Link>
      ) : (
        <span>{row.work}</span>
      ),
  },
  { key: "kind", header: "Kind", accessor: (row) => row.kind },
  { key: "host", header: "Host", accessor: (row) => row.host },
  {
    key: "link",
    header: "Link",
    render: (row) => (
      <a href={row.link} target="_blank" rel="noreferrer" className="mono" style={{ fontSize: 12 }}>
        open &#8599;
      </a>
    ),
  },
  {
    key: "note",
    header: "Note",
    render: (row) => (
      <span style={{ whiteSpace: "normal", maxWidth: "34ch", display: "inline-block", color: "var(--ink-3)" }}>
        {row.note}
      </span>
    ),
  },
];

export default function ReproducePage() {
  const lab = labRollup();

  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow="Reproducibility &middot; manifests"
          title="Reproduce this lab"
          lead="Every experiment, simulation, derivation, training run, scan, or analysis ships a manifest with sealed inputs (external data with links, or repo-pinned internal artifacts), exact entrypoints, compute venue, an estimated cost and wall-clock, and a verification method — so a stranger, or Hubify, can reproduce it without asking us anything. The full-reproduction pass across every program is the final pre-publication test of this lab, not an afterthought."
          actions={[
            { label: "Survey data & QC", href: "/reproduce/surveys" },
            { label: "Docs", href: "/docs" },
          ]}
        />
      </Band>

      <Band width="content">
        <StatRow
          items={[
            { value: lab.totalPrograms, label: "Research programs" },
            { value: lab.totalExperiments, label: "Experiment manifests" },
            { value: lab.runnableNow, label: "Runnable now" },
            { value: formatCost(lab.totalEstCostUsd), label: "Est. total reproduction cost" },
          ]}
        />
        <p style={{ fontSize: 13.5, color: "var(--ink-3)", marginTop: 16 }} className="mono">
          {lab.needsDataRestore} experiment{lab.needsDataRestore === 1 ? "" : "s"} need a data
          restore before they can run; {lab.superseded} {lab.superseded === 1 ? "is" : "are"}{" "}
          superseded and kept for lineage only, never offered as a live reproduction target.
          Per-program cost/wall-clock totals are rollups, not literal sums of the experiment rows
          below — see each program&apos;s <code>full_reproduction.order</code> note for sequencing.
        </p>
      </Band>

      {reproPrograms.map((program, i) => {
        const rollup = programRollup(program);
        const rows = programExperimentsInDagOrder(program);

        return (
          <Band key={program.id} tone={i % 2 === 0 ? "alt" : "base"} width="content">
            <p className="eyebrow">Research program &middot; {program.id}</p>
            <h2 className="page-header-title" style={{ fontSize: 24 }}>
              {program.title}
            </h2>
            <p style={{ maxWidth: "70ch", color: "var(--ink-2)", marginTop: 8 }}>
              <strong style={{ color: "var(--ink)" }}>Question:</strong> {program.question}
            </p>
            <p className="mono" style={{ fontSize: 12.5, color: "var(--ink-3)", marginTop: 10 }}>
              {rollup.totalExperiments} experiments &middot; {rollup.runnableNow} runnable now
              &middot; full reproduction {formatCost(rollup.estCostUsd)} &middot;{" "}
              {rollup.estWallClock}
            </p>

            <h3 style={{ fontSize: 16, marginTop: 28, marginBottom: 10 }}>
              Experiments &mdash; reproduction order
            </h3>
            <DataTable columns={experimentColumns} rows={rows} rowKey={(r) => r.experiment.id} />

            <h3 style={{ fontSize: 16, marginTop: 28, marginBottom: 10 }}>
              Papers in this program
            </h3>
            <DataTable
              columns={[
                { key: "paper", header: "Work", accessor: (p) => p.title },
                { key: "code", header: "Code", mono: true, accessor: (p) => p.paper },
                { key: "role", header: "Role", accessor: (p) => p.role },
                {
                  key: "link",
                  header: "Paper",
                  render: (p) => {
                    const slug = paperSlugForCode(p.paper);
                    return slug ? <Link href={`/papers/${slug}`}>view</Link> : <span>&mdash;</span>;
                  },
                },
              ]}
              rows={program.papers}
              rowKey={(p, idx) => `${p.paper}-${idx}`}
            />

            <h3 style={{ fontSize: 16, marginTop: 28, marginBottom: 10 }}>
              External data sources
            </h3>
            <DataTable
              columns={[
                { key: "name", header: "Source", accessor: (d) => d.name },
                { key: "kind", header: "Kind", accessor: (d) => d.kind },
                { key: "license", header: "License", mono: true, accessor: (d) => d.license ?? "—" },
                {
                  key: "link",
                  header: "Link",
                  render: (d) =>
                    d.link !== "not-publicly-released" ? (
                      <a href={d.link} target="_blank" rel="noreferrer" className="mono" style={{ fontSize: 12 }}>
                        source &#8599;
                      </a>
                    ) : (
                      <span style={{ color: "var(--ink-3)" }}>not publicly released</span>
                    ),
                },
              ]}
              rows={program.external_data}
              rowKey={(d, idx) => `${d.name}-${idx}`}
            />
          </Band>
        );
      })}

      <Band width="content" id="releases">
        <h2 className="page-header-title" style={{ fontSize: 24 }}>
          Releases &amp; DOIs
        </h2>
        <p style={{ maxWidth: "72ch", color: "var(--ink-2)", marginTop: 8 }}>
          Archival records and data mirrors for every work that has one — Zenodo (permanent DOI),
          HuggingFace (dataset mirror), Backblaze B2 (raw-file mirror), and the GitHub source
          repository. A release without a minted DOI yet is cited via its pinned repository commit
          in the meantime, never left uncited.
        </p>
        <div style={{ marginTop: 16 }}>
          <DataTable columns={releaseColumns} rows={RELEASES} rowKey={(r) => r.work} />
        </div>
      </Band>

      <Band width="content">
        <h2 className="page-header-title" style={{ fontSize: 24 }}>
          How to run one
        </h2>
        <p style={{ maxWidth: "72ch", color: "var(--ink-2)", marginTop: 8 }}>
          Every experiment row above names its own entrypoint. In general:
        </p>
        <pre
          className="mono"
          style={{
            marginTop: 12,
            padding: "16px 20px",
            border: "1px solid var(--rule)",
            borderRadius: 4,
            background: "var(--tool)",
            fontSize: 13,
            overflowX: "auto",
          }}
        >
{`git clone https://github.com/Hubify-Projects/bigbounce
cd bigbounce
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# then run the exact entrypoint from the experiment's "Scripts" cell above, e.g.:
python3 research/track_a3_multichannel/pbh_abundance_fnl.py`}
        </pre>
      </Band>
    </>
  );
}
