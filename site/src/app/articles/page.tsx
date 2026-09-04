import type { Metadata } from "next";
import { PageHeader, RowList } from "@/components/primitives";
import { articles } from "@/data/articles";

function toDisplayLabel(s: string): string {
  return s.replace(/\b([a-z])/g, (c) => c.toUpperCase());
}

export const metadata: Metadata = {
  title: "Articles",
  description:
    "Deep dives, explainers, and strategic assessments from the BigBounce research program.",
};

export default function ArticlesPage() {
  return (
    <>
      <PageHeader
        eyebrow="Research articles"
        title="Articles"
        lead="Deep dives, explainers, strategic assessments, and visual guides from the BigBounce research program — written for researchers, students, and anyone curious about the frontiers of quantum gravity and cosmology."
      />

      <section className="mt-2">
        <RowList
          items={articles.map((article) => ({
            title: article.title,
            purpose: article.summary,
            href: `/articles/${article.slug}`,
            chips: [
              toDisplayLabel(article.type),
              article.category ? toDisplayLabel(article.category) : null,
              article.isNew ? "New" : null,
            ]
              .filter(Boolean)
              .join(" · "),
          }))}
        />
      </section>
    </>
  );
}
