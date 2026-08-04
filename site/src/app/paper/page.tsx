import { papers, researchPrograms } from "@/data/papers";
import { getLivePapers } from "@/lib/livePapers";
import { PublicationPathCompact } from "@/components/PublicationPath";
import { Button } from "@/components/ui/button";
import { MathText } from "@/components/MathText";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { Download, FileText } from "lucide-react";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Research Programs",
  description:
    "BigBounce research programs, their lead scientific results, and their supporting papers and artifacts.",
};

function readinessColor(pct: number) {
  if (pct === 100) return "progress-fill-success";
  if (pct >= 90) return "progress-fill-near";
  return "progress-fill-caution";
}

export default async function PaperPage() {
  const live = await getLivePapers();
  const liveReadiness = new Map(live.map((paper) => [paper.slug, paper.readinessComputed]));
  const livePapers = papers.map((paper) => ({
    ...paper,
    readiness: liveReadiness.get(paper.slug) ?? paper.readiness,
  }));

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research programs &middot; evidence library
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          Research programs
        </h1>
        <p className="subtitle">
          Three research questions lead this portfolio. The PDFs, software, data
          products, and candidate manuscripts below retain their versioned evidence
          without being presented as six equal scientific claims.
        </p>
      </div>

      {researchPrograms.map((program) => {
        const lead = program.leadSlug
          ? livePapers.find((paper) => paper.slug === program.leadSlug)
          : undefined;
        const supports = program.supportSlugs
          .flatMap((slug) => {
            const paper = livePapers.find((paper) => paper.slug === slug);
            return paper ? [paper] : [];
          });
        const programPapers = lead ? [lead, ...supports] : supports;

        return (
          <section className="section" key={program.id}>
            <p className="text-xs sans" style={{ marginBottom: 8 }}>
              {program.status}
            </p>
            <h2>{program.title}</h2>
            <p className="text-sm text-muted-foreground leading-relaxed" style={{ maxWidth: "70ch", marginTop: 6 }}>
              <strong className="text-foreground">Question:</strong> {program.question}
            </p>
            <p className="text-sm text-muted-foreground leading-relaxed" style={{ maxWidth: "70ch", marginTop: 4 }}>
              <strong className="text-foreground">Boundary:</strong> {program.limitation}
            </p>

            <div className="flex flex-col gap-4 mt-5">
              {programPapers.map((paper) => (
                <Card key={paper.slug} className="index-card overflow-hidden">
                  <CardHeader className="pb-3">
                    <CardDescription className="text-xs uppercase tracking-wider">
                      {paper.slug === program.leadSlug ? "Lead result" : "Supporting output"} &middot; {paper.number} &middot; {paper.version}
                    </CardDescription>
                    <CardTitle className="mt-1 text-base break-words" style={{ fontFamily: "var(--font-mono-stack)" }}>
                      <MathText>{paper.title}</MathText>
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="mb-3 text-sm text-muted-foreground leading-relaxed">
                      <MathText>{paper.tldr}</MathText>
                    </p>
                    <div className="mb-3 flex items-center gap-3">
                      <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-border">
                        <div className={`h-full rounded-full ${readinessColor(paper.readiness)}`} style={{ width: `${paper.readiness}%` }} />
                      </div>
                      <span className="text-xs font-mono text-muted-foreground shrink-0">
                        {paper.pages} pp &middot; evidence {paper.readiness}%
                      </span>
                    </div>
                    <PublicationPathCompact paper={paper} />
                  </CardContent>
                  <CardFooter className="flex flex-wrap gap-2">
                    {(() => {
                      const pdf = paper.artifacts.find((artifact) => artifact.kind === "primary" && artifact.href.toLowerCase().endsWith(".pdf"));
                      const download = paper.artifacts.find((artifact) => artifact.download && artifact.href.toLowerCase().endsWith(".pdf"));
                      return (
                        <>
                          {pdf && <Button asChild size="sm"><a href={pdf.href} target="_blank" rel="noopener noreferrer"><FileText size={14} />Read PDF</a></Button>}
                          {download && <Button asChild size="sm" variant="outline"><a href={download.href} download><Download size={14} />Download</a></Button>}
                          <Button asChild size="sm" variant="outline"><Link href={`/papers/${paper.slug}`}>Details &rarr;</Link></Button>
                        </>
                      );
                    })()}
                  </CardFooter>
                </Card>
              ))}
            </div>
          </section>
        );
      })}
    </>
  );
}
