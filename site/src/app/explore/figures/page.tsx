import type { Metadata } from "next";
import { figureSections as staticSections, type FigureSection } from "@/data/figures";
import { getAllFiguresGroupedByPaper, type PaperFigure } from "@/lib/livePapers";
import { researchPrograms } from "@/data/papers";
import { Band, PageHeader } from "@/components/primitives";
import { FigureExplorer } from "./FigureExplorer";

export const metadata: Metadata = {
  title: "Figures",
  description:
    "Every research figure across the BigBounce portfolio, synced from each work's current LaTeX source, filterable by track.",
};

const SECTION_ORDER: Array<{ slug: string; title: string }> = [
  { slug: "paper-1a", title: "Paper 1A — ECH channel-level closure" },
  { slug: "paper-1b", title: "Paper 1B — namaster-proof software verification" },
  { slug: "paper-2", title: "Paper 2 — matter-bounce f_NL SPHEREx forecast" },
  { slug: "paper-3", title: "Paper 3 — supporting DESI data release" },
  { slug: "paper-4", title: "Paper 4 — galaxy chirality catalog" },
  { slug: "paper-5", title: "Paper 5 — DESI chirality x cosmic-web environment" },
];

function sectionsFromConvex(grouped: Record<string, PaperFigure[]>): FigureSection[] {
  const sections: FigureSection[] = [];
  for (const { slug, title } of SECTION_ORDER) {
    const rows = (grouped[slug] || [])
      .filter((r) => (r.status ?? "in-paper") !== "retracted")
      .slice()
      .sort((a, b) => a.ordinal - b.ordinal);
    if (rows.length === 0) continue;
    sections.push({
      title,
      count: `${rows.length} figure${rows.length === 1 ? "" : "s"}`,
      items: rows.map((r) => ({
        src: r.src,
        alt: r.alt,
        number: r.status === "candidate" ? `Candidate #${r.ordinal - 100}` : `Figure ${r.ordinal}`,
        title: r.title,
        desc: r.desc,
        source: `${title.split("—")[0].trim()} · ${r.status === "candidate" ? "candidate pool" : r.paperVersion}`,
      })),
    });
  }
  return sections;
}

export default async function ExploreFiguresPage() {
  let sections: FigureSection[] = staticSections;
  try {
    const grouped = await getAllFiguresGroupedByPaper();
    const live = sectionsFromConvex(grouped);
    if (live.length > 0) sections = live;
  } catch {
    // static fallback already set
  }

  const totalFigures = sections.reduce((s, sec) => s + sec.items.length, 0);
  const trackCount = researchPrograms.length;

  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow="Explore · Figures"
          title="Figures"
          lead={`${totalFigures} research figures across the portfolio's ${trackCount} research tracks. In-paper figures sync from each work's current LaTeX source on every build; candidate figures are validated analysis outputs not yet included in a draft.`}
        />
      </Band>
      <Band width="content">
        <FigureExplorer sections={sections} />
      </Band>
    </>
  );
}
