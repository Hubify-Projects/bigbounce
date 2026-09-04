import type { Metadata } from "next";
import { PageHeader, RowList } from "@/components/primitives";
import { articles } from "@/data/articles";

export const metadata: Metadata = {
  title: "Learn",
  description:
    "Start here: the plain-English explainer, the glossary, the cosmic timeline, deep-dive articles, and clearly-labeled speculation.",
};

export default function LearnPage() {
  return (
    <>
      <PageHeader
        eyebrow="Learn"
        title="Learn the bounce"
        lead="No jargon required to start. Read the explainer first, then go as deep as you want — the glossary, the timeline, longer articles, and finally the speculative ideas we haven't formalized yet."
      />

      <section className="mt-2">
        <RowList
          items={[
            {
              title: "Explained",
              purpose: "What is a big bounce, in plain English — start here.",
              href: "/explained",
            },
            {
              title: "Glossary",
              purpose: `${24} plain-English glosses for every term used across the site.`,
              href: "/glossary",
            },
            {
              title: "Timeline",
              purpose: "From the parent universe through the bounce to SPHEREx 2028.",
              href: "/timeline",
            },
            {
              title: "Articles",
              purpose: `${articles.length} deep-dive essays and strategic assessments.`,
              href: "/articles",
            },
            {
              title: "Speculations",
              purpose: "Future research directions — clearly labeled as not yet formal work.",
              href: "/speculations",
            },
          ]}
        />
      </section>
    </>
  );
}
