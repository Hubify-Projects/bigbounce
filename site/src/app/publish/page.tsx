import Link from "next/link";
import type { Metadata } from "next";
import { papers, researchPrograms } from "@/data/papers";
import { publicationArchitecture, publicationExecution, publicationMap } from "@/data/publish";
import { Band, PageHeader, RowList, DataTable, EvidenceChip } from "@/components/primitives";

export const metadata: Metadata = {
  title: "Portfolio Decisions",
  description:
    "Approved research-program publication architecture, portfolio roles, and candidate-package evidence for BigBounce.",
};

export default function PublishPage() {
  return (
    <>
      <Band>
        <PageHeader
          eyebrow={`Publication architecture · updated ${publicationArchitecture.lastUpdatedDisplay}`}
          title="Choose the science before the submission sequence"
          lead={publicationArchitecture.headline}
        />
        <p className="row-purpose">
          <strong>Execution order:</strong> {publicationExecution.selectedOrder.join(" → ")}. The
          anomaly rerun proceeds in parallel; its flagship is drafted only if its regenerated
          evidence is scientifically and reproducibly strong enough.{" "}
          <Link href="/status#signoff">Review the sign-off gates for every work →</Link>
        </p>
      </Band>

      <Band tone="alt">
        <PageHeader eyebrow="01" title="Research tracks" lead="Each program starts with its question, lead result, and boundary." />
        <RowList
          items={researchPrograms.map((program) => {
            const lead = program.leadSlug ? papers.find((paper) => paper.slug === program.leadSlug) : undefined;
            return {
              title: program.title,
              purpose: `Q: ${program.question} — ${program.result}`,
              href: lead ? `/papers/${lead.slug}` : "/research",
              right: <EvidenceChip grade="open" label={program.status} />,
            };
          })}
        />
      </Band>

      <Band>
        <PageHeader
          eyebrow="02"
          title="What we publish, and what supports it"
          lead="Manuscripts make scientific arguments. Data, checkpoints, and code make those arguments inspectable; they are tracked separately so no artifact is mistaken for a discovery claim."
        />
        {publicationMap.map((group) => (
          <div key={group.title} className="widget-row">
            <p className="row-title">{group.title}</p>
            <p className="row-purpose" style={{ marginBottom: 10 }}>{group.detail}</p>
            <RowList
              items={group.rows.map((row) => ({
                title: row.name,
                purpose: `${row.role} — ${row.status}`,
                href: row.href,
                external: row.external,
                right: <span className="mono">{row.destination}</span>,
              }))}
            />
          </div>
        ))}
      </Band>

      <Band tone="alt">
        <PageHeader
          eyebrow="03"
          title="Approved portfolio decisions"
          lead="These decisions settle what each output is for. The remaining work is manuscript review, then the separate endorsement and submission phase."
        />
        <RowList
          items={publicationArchitecture.decisions.map((hold) => ({
            title: hold.title,
            purpose: hold.detail,
            href: "/research",
          }))}
        />
      </Band>

      <Band width="full">
        <div style={{ maxWidth: "var(--content-width)", margin: "0 auto", padding: "0 24px" }}>
          <PageHeader
            eyebrow="04"
            title="Candidate package evidence"
            lead="Every candidate remains available with its exact PDF and artifact record. The evidence percentage is a packaging/review record, not a claim of journal acceptance."
          />
          <DataTable
            rows={papers}
            rowKey={(p) => p.slug}
            columns={[
              {
                key: "candidate",
                header: "Candidate",
                render: (p) => (
                  <>
                    <span className="mono">{p.number}</span> <span className="row-purpose">{p.title}</span>
                  </>
                ),
              },
              {
                key: "role",
                header: "Portfolio role",
                render: (p) => (
                  <>
                    {p.publicationRole}
                    <br />
                    <span className="row-purpose">
                      {p.standaloneSubmission ? "Selected standalone submission" : "Integrated support release"}
                    </span>
                  </>
                ),
              },
              { key: "evidence", header: "Evidence", mono: true, render: (p) => `${p.readiness}%` },
              {
                key: "artifact",
                header: "Artifact",
                render: (p) => {
                  const pdf = p.artifacts.find((a) => a.kind === "primary" && a.href.endsWith(".pdf"));
                  return pdf ? (
                    <a href={pdf.href} target="_blank" rel="noopener noreferrer">
                      Read PDF
                    </a>
                  ) : (
                    "—"
                  );
                },
              },
            ]}
          />
          <p className="row-purpose" style={{ marginTop: 12 }}>
            Detailed package paths and review state are retained in{" "}
            <Link href="/research">research tracks</Link> and <Link href="/reviews">the review record</Link>.
          </p>
        </div>
      </Band>
    </>
  );
}
