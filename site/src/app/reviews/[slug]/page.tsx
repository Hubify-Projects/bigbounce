import { readFile } from "node:fs/promises";
import path from "node:path";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  reviewRounds,
  getReviewRoundByReportSlug,
} from "@/data/reviewTimeline";
import { renderMarkdown } from "@/lib/markdown";
import "../reviews.css";

type PageParams = Promise<{ slug: string }>;

export function generateStaticParams() {
  return reviewRounds
    .filter((r) => r.reportSlug)
    .map((r) => ({ slug: r.reportSlug as string }));
}

export async function generateMetadata({
  params,
}: {
  params: PageParams;
}): Promise<Metadata> {
  const { slug } = await params;
  const round = getReviewRoundByReportSlug(slug);
  if (!round) return { title: "Review report" };
  return {
    title: `${round.id} — review report`,
    description: round.summary,
  };
}

async function loadReport(slug: string): Promise<string | null> {
  try {
    const file = path.join(process.cwd(), "public", "reviews", `${slug}.md`);
    return await readFile(file, "utf-8");
  } catch {
    return null;
  }
}

export default async function ReviewReportPage({
  params,
}: {
  params: PageParams;
}) {
  const { slug } = await params;
  const round = getReviewRoundByReportSlug(slug);
  if (!round) notFound();

  const md = await loadReport(slug);
  if (!md) notFound();

  return (
    <>
      <p className="text-xs sans" style={{ marginBottom: 14 }}>
        <Link
          href="/reviews"
          style={{ color: "var(--text-muted)", textDecoration: "none" }}
        >
          ← Review activity
        </Link>
      </p>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          alignItems: "baseline",
          gap: 10,
          marginBottom: 4,
        }}
      >
        <span
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.74rem",
            color: "var(--text-muted)",
            letterSpacing: "0.04em",
          }}
        >
          {round.dateISO}
        </span>
        <span
          className={
            round.kind === "external-browser"
              ? "review-kind-badge is-external"
              : "review-kind-badge"
          }
        >
          {round.id}
        </span>
      </div>
      <p
        style={{
          maxWidth: "72ch",
          fontSize: "0.85rem",
          color: "var(--text-muted)",
          lineHeight: 1.55,
          margin: "0 0 24px 0",
        }}
      >
        {round.summary}
      </p>

      <article
        className="review-report-body"
        dangerouslySetInnerHTML={{ __html: renderMarkdown(md) }}
      />
    </>
  );
}
