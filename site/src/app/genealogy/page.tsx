import type { Metadata } from "next";
import { Band, EvidenceChip, PageHeader, RowList } from "@/components/primitives";
import {
  disclaimer,
  generations,
  openQuestions,
  provenance,
  retired,
} from "@/data/genealogy";

export const metadata: Metadata = {
  title: "Research genealogy",
  description:
    "The pre-2026 exploratory lineage of the BigBounce program — four generations of ideas, the hypotheses that were retired, and the questions that survived.",
};

const NOT_A_CLAIM = "Not a current claim";
const OPEN_QUESTION = "Open question · not a result";

export default function GenealogyPage() {
  return (
    <>
      <PageHeader
        eyebrow="Learn · Genealogy"
        title="Where the bounce program came from"
        lead="The ideas below are the pre-2026 exploratory lineage of this project — mined for questions, not restored as theory."
      />

      <Band tone="deep" width="content" className="my-6">
        <p className="py-3 text-sm font-medium">{disclaimer}</p>
      </Band>

      <section className="section">
        <h2>Four generations</h2>
        <ol className="flex flex-col">
          {generations.map((gen) => (
            <li
              key={gen.period}
              className="grid grid-cols-[minmax(84px,auto)_1fr] gap-x-5 gap-y-1 border-t py-4 md:grid-cols-[160px_1fr]"
              style={{ borderColor: "var(--rule, var(--border))" }}
            >
              <span className="mono self-baseline text-xs uppercase tracking-wider text-muted-foreground">
                {gen.period}
              </span>
              <div>
                <p
                  className="text-base font-semibold"
                  style={{ fontFamily: "var(--font-mono-stack)" }}
                >
                  {gen.title}
                </p>
                <p className="mt-1 text-sm leading-relaxed text-muted-foreground">
                  <span className="font-medium text-foreground">Explored: </span>
                  {gen.explored}
                </p>
                <p className="mt-1 text-sm leading-relaxed text-muted-foreground">
                  <span className="font-medium text-foreground">Survived: </span>
                  {gen.survived}
                </p>
              </div>
            </li>
          ))}
        </ol>
      </section>

      <section className="section">
        <h2>Retired hypotheses</h2>
        <div className="flat-item-list">
          {retired.map((item) => (
            <div key={item.name} className="py-4">
              <p
                className="mb-1 text-sm font-semibold"
                style={{ fontFamily: "var(--font-mono-stack)" }}
              >
                {item.name}
              </p>
              <p className="mb-1 text-sm leading-relaxed text-muted-foreground">
                <span className="font-medium text-foreground">Claim: </span>
                {item.claim}
              </p>
              <p className="mb-2 text-sm leading-relaxed text-muted-foreground">
                <span className="font-medium text-foreground">Why retired: </span>
                {item.whyRetired}
              </p>
              <div className="flex flex-wrap items-center gap-3">
                <EvidenceChip grade="null" label={item.status} />
                <span className="mono text-[10px] text-muted-foreground opacity-70">
                  {item.evidence}
                </span>
                <span className="mono text-[10px] uppercase tracking-wider text-muted-foreground opacity-70">
                  {NOT_A_CLAIM}
                </span>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Open questions carried forward</h2>
        <RowList
          items={openQuestions.map((q) => ({
            title: q.title,
            purpose: (
              <>
                {q.question}
                <span className="mt-1 block text-xs leading-relaxed text-muted-foreground">
                  Finding: {q.finding}
                </span>
              </>
            ),
            href: "/speculations",
            right: `Ledger ${q.ledgerItem}`,
            chips: (
              <span className="mono text-[10px] uppercase tracking-wider text-muted-foreground opacity-70">
                {OPEN_QUESTION}
              </span>
            ),
          }))}
        />
      </section>

      <section className="section">
        <h2>Provenance</h2>
        <div className="row-list">
          {provenance.map((p) => (
            <div key={p.title} className="row" style={{ cursor: "default" }}>
              <span className="row-main">
                <span className="row-title">{p.title}</span>
                <span className="row-purpose">{p.role}</span>
              </span>
            </div>
          ))}
        </div>
        <p className="mt-4 text-sm text-muted-foreground">
          Internal archive:{" "}
          <span className="mono text-xs opacity-80">
            research/archaeology_2025/
          </span>
        </p>
      </section>
    </>
  );
}
