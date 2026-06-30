import type { Metadata } from "next";
import { SearchClient } from "./SearchClient";

export const metadata: Metadata = {
  title: "Search",
  description:
    "Search across papers, contributions, figures, equations, glossary, surveys, and articles in the BigBounce research program.",
};

export default function SearchPage() {
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          BigBounce · research index
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          Search
        </h1>
        <p className="subtitle">
          Find anything across the research program — contributions, theorems,
          equations, figures, papers, surveys, glossary entries, and articles.
        </p>
      </div>

      <SearchClient />
    </>
  );
}
