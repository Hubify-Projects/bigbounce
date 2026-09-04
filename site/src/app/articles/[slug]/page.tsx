import { readFile } from"node:fs/promises";
import path from"node:path";
import { notFound } from"next/navigation";
import type { Metadata } from"next";
import Script from"next/script";
import Link from"next/link";
import { articles } from"@/data/articles";

type PageParams = Promise<{ slug: string }>;

const REPO_ROOT = path.resolve(/* turbopackIgnore: true */ process.cwd(),"..");

async function loadArticleBody(slug: string): Promise<string | null> {
  try {
    const file = path.join(REPO_ROOT,"articles", `${slug}.html`);
    const html = await readFile(file,"utf-8");
    const match = html.match(/<main class="container">([\s\S]*?)<\/main>/);
    if (!match) return null;
    let body = match[1];
    // Rewrite relative image paths to absolute /articles/images/... or /public/...
    body = body.replace(
      /(src|href)="(?!https?:|\/|#|mailto:)([^"]+)"/g,
      (_full, attr, p) => {
        if (p.startsWith("articles/")) return `${attr}="/${p}"`;
        if (p.startsWith("../")) return `${attr}="/${p.replace(/^\.\.\//,"")}"`;
        if (p.startsWith("public/")) return `${attr}="/${p}"`;
        return `${attr}="/articles/${p}"`;
      },
    );
    return body;
  } catch {
    return null;
  }
}

export async function generateStaticParams() {
  return articles.map((a) => ({ slug: a.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: PageParams;
}): Promise<Metadata> {
  const { slug } = await params;
  const article = articles.find((a) => a.slug === slug);
  if (!article) return { title:"Article" };
  return {
    title: article.title,
    description: article.summary,
  };
}

export default async function ArticlePage({ params }: { params: PageParams }) {
  const { slug } = await params;
  const article = articles.find((a) => a.slug === slug);
  if (!article) notFound();

  const body = await loadArticleBody(slug);

  return (
    <>
      <div className="mb-6 text-xs">
        <Link
          href="/articles"
          className="font-mono uppercase tracking-wider text-muted-foreground hover:text-foreground"
        >
          ← All articles
        </Link>
      </div>

      <p className="mono mb-6 text-xs uppercase tracking-wider text-muted-foreground">
        {[article.type, article.category, article.isNew ? "new" : null]
          .filter(Boolean)
          .join(" · ")}
      </p>

      {body ? (
        <article
          className="article-body"
          dangerouslySetInnerHTML={{ __html: body }}
        />
      ) : (
        <div>
          <h1 style={{ fontFamily:"var(--font-mono-stack)" }}>{article.title}</h1>
          <p className="subtitle">{article.summary}</p>
          <p className="text-sm text-muted-foreground">
            Article source could not be loaded.
          </p>
        </div>
      )}

      <Script
        id="mathjax-config"
        strategy="beforeInteractive"
      >{`window.MathJax = { tex: { inlineMath: [['$','$'], ['\\\\(','\\\\)']] } };`}</Script>
      <Script
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        strategy="afterInteractive"
      />
    </>
  );
}
