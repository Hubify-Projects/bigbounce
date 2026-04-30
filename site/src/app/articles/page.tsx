import type { Metadata } from "next";
import Link from "next/link";
import { articles } from "@/data/articles";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export const metadata: Metadata = {
  title: "Articles",
  description:
    "Deep dives, explainers, and strategic assessments from the BigBounce research program.",
};

export default function ArticlesPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Articles · Spin-Torsion Cosmology Program
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          Articles
        </h1>
        <p className="subtitle">
          Deep dives, explainers, strategic assessments, and visual guides from
          the BigBounce research program. Written for researchers, students, and
          anyone curious about the frontiers of quantum gravity and cosmology.
        </p>
      </div>

      <section className="section">
        <div className="grid gap-3">
          {articles.map((article) => (
            <Link
              key={article.slug}
              href={`/articles/${article.slug}`}
              className="no-underline text-foreground"
            >
              <Card className="transition-colors hover:bg-accent/40">
                <CardHeader className="pb-2">
                  <div className="flex flex-wrap items-center gap-2">
                    <Badge variant="outline" className="font-mono text-[10px]">
                      {article.type}
                    </Badge>
                    {article.category && (
                      <Badge variant="secondary" className="font-mono text-[10px]">
                        {article.category}
                      </Badge>
                    )}
                    {article.isNew && (
                      <Badge variant="default" className="font-mono text-[10px]">
                        NEW
                      </Badge>
                    )}
                  </div>
                  <CardTitle
                    className="mt-2 text-base leading-snug"
                    style={{ fontFamily: "var(--font-serif)" }}
                  >
                    {article.title}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground">
                    {article.summary}
                  </p>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </section>
    </>
  );
}
