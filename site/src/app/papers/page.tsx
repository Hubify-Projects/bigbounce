import { papers, researchPrograms, type Paper } from "@/data/papers";
import { getLivePapers, displayVersion } from "@/lib/livePapers";
import { MathText } from "@/components/MathText";
import { Badge } from "@/components/ui/badge";
import { ArrowRight } from "lucide-react";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "All Papers",
  description:
    "Every BigBounce paper, dataset, and research-software release in one flat, plain-English list — no grouping, no jargon-only titles.",
};

type PaperRole = "lead" | "specialist" | "companion" | "supporting release";

/**
 * Editorial role within the three-program portfolio (see researchPrograms in
 * data/papers.ts). "lead" comes straight from a program's leadSlug; the rest
 * are read off the paper's own publicationRole label so this never drifts
 * from the program page.
 */
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

function programForSlug(slug: string) {
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

export default async function PapersIndexPage() {
  const live = await getLivePapers();
  const liveBySlug = new Map(live.map((p) => [p.slug, p]));

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          All papers &middot; flat index
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          All papers
        </h1>
        <p className="subtitle">
          Every paper, dataset, and research-software release in the portfolio,
          in one flat list — no grouping by research track. Prefer the
          question-first view?{" "}
          <Link href="/paper" style={{ color: "var(--accent-link)" }}>
            See research tracks
          </Link>
          .
        </p>
      </div>

      <section className="section">
        <div style={{ display: "grid", gap: 0, marginTop: 4 }}>
          {papers.map((paper, i) => {
            const program = programForSlug(paper.slug);
            const role = paperRole(paper);
            const livePaper = liveBySlug.get(paper.slug);
            const version = displayVersion(livePaper?.currentVersion ?? paper.version);
            return (
              <div
                key={paper.slug}
                style={{
                  padding: "20px 0",
                  borderTop: i === 0 ? "none" : "1px solid var(--border)",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    flexWrap: "wrap",
                    alignItems: "center",
                    gap: 8,
                    marginBottom: 6,
                  }}
                >
                  <span
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 11,
                      fontWeight: 700,
                      color: "var(--accent)",
                    }}
                  >
                    P{paper.number}
                  </span>
                  {program && <Badge variant="outline">{program.title}</Badge>}
                  <Badge variant="secondary">{ROLE_LABEL[role]}</Badge>
                  <span
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 11.5,
                      color: "var(--text-tertiary)",
                    }}
                  >
                    {version}
                  </span>
                </div>

                <h3
                  style={{
                    margin: 0,
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 16,
                    lineHeight: 1.4,
                  }}
                >
                  <MathText>{paper.title}</MathText>
                </h3>
                <p
                  style={{
                    margin: "5px 0 0",
                    fontSize: 13.5,
                    lineHeight: 1.6,
                    color: "var(--text-secondary)",
                    maxWidth: "78ch",
                  }}
                >
                  {paper.plainTitle}
                </p>

                {paper.archivedInto && (
                  <p
                    style={{
                      margin: "6px 0 0",
                      fontSize: 12,
                      lineHeight: 1.5,
                      color: "var(--text-tertiary)",
                      maxWidth: "78ch",
                    }}
                  >
                    Archived —{" "}
                    <Link
                      href={`/papers/${paper.archivedInto.successorSlug}`}
                      style={{ color: "var(--accent-link)" }}
                    >
                      see current version
                    </Link>
                    . {paper.archivedInto.note}
                    {paper.archivedInto.zenodoDoi && (
                      <>
                        {" "}
                        <a
                          href={paper.archivedInto.zenodoDoi}
                          target="_blank"
                          rel="noreferrer"
                          style={{ color: "var(--accent-link)" }}
                        >
                          Zenodo DOI (archived version)
                        </a>
                        .
                      </>
                    )}
                  </p>
                )}

                <div
                  style={{
                    display: "flex",
                    flexWrap: "wrap",
                    gap: 16,
                    marginTop: 10,
                    fontSize: 12.5,
                  }}
                >
                  <span style={{ color: "var(--text-tertiary)" }}>
                    target: {paper.target}
                  </span>
                  <Link
                    href={`/papers/${paper.slug}`}
                    style={{
                      display: "inline-flex",
                      alignItems: "center",
                      gap: 4,
                      color: "var(--accent)",
                      fontFamily: "var(--font-mono-stack)",
                    }}
                  >
                    Details <ArrowRight size={13} />
                  </Link>
                </div>
              </div>
            );
          })}

          {researchPrograms
            .flatMap((program) =>
              (program.supportingLinks ?? []).map((link) => ({ program, link })),
            )
            .map(({ program, link }) => (
              <div
                key={link.href}
                style={{
                  padding: "20px 0",
                  borderTop: "1px solid var(--border)",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    flexWrap: "wrap",
                    alignItems: "center",
                    gap: 8,
                    marginBottom: 6,
                  }}
                >
                  <Badge variant="outline">{program.title}</Badge>
                  <Badge variant="secondary">Supporting link</Badge>
                </div>

                <h3
                  style={{
                    margin: 0,
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 16,
                    lineHeight: 1.4,
                  }}
                >
                  <MathText>{link.title}</MathText>
                </h3>
                <p
                  style={{
                    margin: "5px 0 0",
                    fontSize: 13.5,
                    lineHeight: 1.6,
                    color: "var(--text-secondary)",
                    maxWidth: "78ch",
                  }}
                >
                  {link.plainTitle}
                </p>

                <div
                  style={{
                    display: "flex",
                    flexWrap: "wrap",
                    gap: 16,
                    marginTop: 10,
                    fontSize: 12.5,
                  }}
                >
                  <span style={{ color: "var(--text-tertiary)" }}>
                    {link.role}
                  </span>
                  <a
                    href={link.href}
                    target={link.external ? "_blank" : undefined}
                    rel={link.external ? "noopener noreferrer" : undefined}
                    style={{
                      display: "inline-flex",
                      alignItems: "center",
                      gap: 4,
                      color: "var(--accent)",
                      fontFamily: "var(--font-mono-stack)",
                    }}
                  >
                    Read PDF <ArrowRight size={13} />
                  </a>
                </div>
              </div>
            ))}
        </div>
      </section>
    </>
  );
}
