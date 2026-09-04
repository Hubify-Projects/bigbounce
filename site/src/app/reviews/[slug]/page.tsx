import { readFile } from "node:fs/promises";
import path from "node:path";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { reviewRounds, getReviewRoundByReportSlug } from "@/data/reviewTimeline";
import { renderMarkdown } from "@/lib/markdown";
import { Band, PageHeader } from "@/components/primitives";
import "../reviews.css";

type PageParams = Promise<{ slug: string }>;

export function generateStaticParams() {
  return reviewRounds.filter((r) => r.reportSlug).map((r) => ({ slug: r.reportSlug as string }));
}

export async function generateMetadata({ params }: { params: PageParams }): Promise<Metadata> {
  const { slug } = await params;
  const round = getReviewRoundByReportSlug(slug);
  if (!round) return { title: "Review report" };
  return { title: `${round.id} — review report`, description: round.summary };
}

async function loadReport(slug: string): Promise<string | null> {
  try {
    const file = path.join(process.cwd(), "public", "reviews", `${slug}.md`);
    return await readFile(file, "utf-8");
  } catch {
    return null;
  }
}

export default async function ReviewReportPage({ params }: { params: PageParams }) {
  const { slug } = await params;
  const round = getReviewRoundByReportSlug(slug);
  if (!round) notFound();

  const md = await loadReport(slug);
  if (!md) notFound();

  return (
    <Band>
      <PageHeader
        eyebrow={`${round.dateISO} · ${round.kind.replace(/-/g, " ")}`}
        title={round.id}
        lead={round.summary}
        actions={[{ label: "← Review activity", href: "/reviews" }]}
      />
      <article
        className="review-report-body"
        dangerouslySetInnerHTML={{ __html: renderMarkdown(md) }}
      />
    </Band>
  );
}
