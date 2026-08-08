import Link from "next/link";
import type { Metadata } from "next";
import { papers, researchPrograms } from "@/data/papers";
import { publicationArchitecture, publicationExecution, publicationMap } from "@/data/publish";
import "./publish.css";

export const metadata: Metadata = {
  title: "Portfolio Decisions",
  description:
    "Approved research-program publication architecture, portfolio roles, and candidate-package evidence for BigBounce.",
};

export default function PublishPage() {
  return (
    <>
      <p className="pub-kicker">Publication architecture</p>
      <h1 className="pub-title">Choose the science before the submission sequence</h1>
      <p className="pub-lede">{publicationArchitecture.headline}</p>
      <p className="pub-meta">Updated {publicationArchitecture.lastUpdatedDisplay}</p>

      <section className="pub-section pub-summary" aria-label="Publication strategy summary">
        <p>
          <strong>The rule:</strong> paper count follows distinct scientific questions and publishable contributions—not the number of files already in the repository. There are three programs, six eventual standalone works, and one integrated supporting data release (P3).
        </p>
        <p>
          <strong>Execution order:</strong> {publicationExecution.selectedOrder.join(" → ")}. The anomaly rerun proceeds in parallel; its flagship is drafted only if its regenerated evidence is scientifically and reproducibly strong enough.
        </p>
        <p>
          <strong>Active decision:</strong> <Link href="/final-review">Review the exact P2 candidate →</Link>
        </p>
      </section>

      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">01</span>
          <h2 className="pub-section-title">Research programs</h2>
        </div>
        <p className="pub-section-sub">
          Each program starts with its question, lead result, and boundary. Specialist outputs and technical candidates remain linked as evidence rather than being treated as equal flagships.
        </p>
        <div className="pub-programs">
          {researchPrograms.map((program) => {
            const lead = program.leadSlug ? papers.find((paper) => paper.slug === program.leadSlug) : undefined;
            const support = program.supportSlugs.flatMap((slug) => {
              const paper = papers.find((item) => item.slug === slug);
              return paper ? [paper] : [];
            });
            return (
              <article className="pub-program" key={program.id}>
                <p className="pub-program-status">{program.status}</p>
                <h3>{program.title}</h3>
                <p><strong>Question:</strong> {program.question}</p>
                <p><strong>Current result:</strong> {program.result}</p>
                <p className="pub-program-boundary"><strong>Boundary:</strong> {program.limitation}</p>
                <div className="pub-program-links">
                  {lead && <Link href={`/papers/${lead.slug}`}>Lead: {lead.number} &middot; {lead.title}</Link>}
                  {support.map((paper) => <Link key={paper.slug} href={`/papers/${paper.slug}`}>Support: {paper.number} &middot; {paper.title}</Link>)}
                </div>
              </article>
            );
          })}
        </div>
      </section>

      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">02</span>
          <h2 className="pub-section-title">What we publish, and what supports it</h2>
        </div>
        <p className="pub-section-sub">
          Manuscripts make scientific arguments. Data, checkpoints, and code make those arguments inspectable and reusable; they are tracked separately so no artifact is mistaken for a paper or a discovery claim.
        </p>
        {publicationMap.map((group) => (
          <div className="pub-map-group" key={group.title}>
            <h3>{group.title}</h3>
            <p>{group.detail}</p>
            <div className="pub-map-rows">
              {group.rows.map((row) => (
                <article className="pub-map-row" key={row.name}>
                  <h4>{row.external ? <a href={row.href} target="_blank" rel="noopener noreferrer">{row.name}</a> : <Link href={row.href}>{row.name}</Link>}</h4>
                  <dl>
                    <div><dt>Role</dt><dd>{row.role}</dd></div>
                    <div><dt>Status</dt><dd>{row.status}</dd></div>
                    <div><dt>Destination</dt><dd>{row.destination}</dd></div>
                    <div><dt>Depends on</dt><dd>{row.dependency}</dd></div>
                    <div><dt>Next gate</dt><dd>{row.nextGate}</dd></div>
                  </dl>
                </article>
              ))}
            </div>
          </div>
        ))}
      </section>

      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">03</span>
          <h2 className="pub-section-title">Approved portfolio decisions</h2>
        </div>
        <p className="pub-section-sub">
          These decisions settle what each output is for. The remaining work is manuscript review, flagship reconstruction, and then the separate endorsement and submission phase.
        </p>
        <div className="pub-holds">
          {publicationArchitecture.decisions.map((hold) => (
            <article className="pub-hold" key={hold.title}>
              <h3>{hold.title}</h3>
              <p>{hold.detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">04</span>
          <h2 className="pub-section-title">Candidate package evidence</h2>
        </div>
        <p className="pub-section-sub">
          Every candidate remains available with its exact PDF and artifact record. The evidence percentage below is a packaging/review record, not a claim that the paper is science-complete, independently publishable, or awaiting endorsement only.
        </p>
        <div className="pub-table-wrap">
          <table className="pub-table">
            <thead>
              <tr>
                <th className="pub-th">Candidate</th>
                <th className="pub-th">Portfolio role</th>
                <th className="pub-th">Evidence record</th>
                <th className="pub-th">Artifact</th>
              </tr>
            </thead>
            <tbody>
              {papers.map((paper) => {
                const program = researchPrograms.find((item) => item.leadSlug === paper.slug || item.supportSlugs.includes(paper.slug));
                const pdf = paper.artifacts.find((artifact) => artifact.kind === "primary" && artifact.href.endsWith(".pdf"));
                return (
                  <tr key={paper.slug}>
                    <td className="pub-td"><span className="pub-paper-code">{paper.number}</span><span className="pub-paper-title">{paper.title}</span></td>
                    <td className="pub-td">{paper.publicationRole}<br /><span className="pub-paper-title">{paper.standaloneSubmission ? "Selected standalone submission" : "Integrated support release"} · {program?.title}</span></td>
                    <td className="pub-td"><span className="pub-readiness">{paper.readiness}%</span><br /><span className="pub-paper-title">Versioned review and package evidence</span></td>
                    <td className="pub-td">{pdf ? <a className="pub-artifact-link" href={pdf.href} target="_blank" rel="noopener noreferrer">Read PDF</a> : "—"}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        <p className="pub-note">
          Detailed package paths and review state are retained in <Link href="/paper">research programs</Link> and <Link href="/reviews">the review record</Link>.
        </p>
      </section>
    </>
  );
}
