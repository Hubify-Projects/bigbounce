import type { Metadata } from "next";
import { figureSections as staticSections, type FigureSection } from "@/data/figures";
import { getAllFiguresGroupedByPaper, type PaperFigure } from "@/lib/livePapers";
import { FigureGallery } from "./figure-gallery";

export const metadata: Metadata = {
  title: "Figures",
  description:
    "Gallery of research figures from the BigBounce spin-torsion cosmology program — auto-synced from each paper's current .tex sources via Convex.",
};

// Canonical display order. Sections matching a paperSlug appear in this order;
// any extras fall through to the "X" cross-cutting group below.
const SECTION_ORDER: Array<{ slug: string; title: string }> = [
  { slug: "paper-1a", title: "Paper 1A — ECH Structural Closure (No-Go Theorem)" },
  { slug: "paper-1b", title: "Paper 1B — Technical Verification Companion (MCMC + NaMaster)" },
  { slug: "paper-2",  title: "Paper 2 — Matter-Bounce f_NL SPHEREx Forecast" },
  { slug: "paper-3",  title: "Paper 3 — DESI Spectral Anomalies (Multi-Survey Catalog)" },
  { slug: "paper-4",  title: "Paper 4 — Galaxy Chirality Catalog (3.2M Spirals)" },
  { slug: "paper-5",  title: "Paper 5 — DESI Chirality × Cosmic-Web Environment" },
];

function sectionsFromConvex(
  grouped: Record<string, PaperFigure[]>
): FigureSection[] {
  const sections: FigureSection[] = [];
  for (const { slug, title } of SECTION_ORDER) {
    const allRows = (grouped[slug] || []).slice().sort((a, b) => a.ordinal - b.ordinal);
    // Exclude retracted figures from the main gallery; in-paper + candidates
    // are surfaced together so Houston can browse the full valid pool.
    const rows = allRows.filter((r) => (r.status ?? "in-paper") !== "retracted");
    if (rows.length === 0) continue;
    const inPaperCount = rows.filter((r) => (r.status ?? "in-paper") === "in-paper").length;
    const candCount = rows.filter((r) => r.status === "candidate").length;
    const countLabel = candCount > 0
      ? `${inPaperCount} in paper · ${candCount} candidate${candCount === 1 ? "" : "s"}`
      : `${inPaperCount} figure${inPaperCount === 1 ? "" : "s"}`;
    sections.push({
      title,
      count: countLabel,
      items: rows.map((r) => {
        const isCandidate = r.status === "candidate";
        return {
          src: r.src,
          alt: r.alt,
          number: isCandidate
            ? `Candidate #${r.ordinal - 100}`
            : r.citationLabel
              ? `Figure ${r.ordinal} (${r.citationLabel})`
              : `Figure ${r.ordinal}`,
          title: isCandidate ? `[candidate] ${r.title}` : r.title,
          desc: r.desc,
          source: `${title.split("—")[0].trim()} · ${isCandidate ? "candidate pool" : r.paperVersion}`,
        };
      }),
    });
  }
  return sections;
}

export default async function FiguresPage() {
  // Convex-first: re-read on every build (static export still renders at
  // build time, so this acts as the same-build snapshot). Falls back to
  // the static figures.ts when Convex is unreachable.
  let sections: FigureSection[] = staticSections;
  try {
    const grouped = await getAllFiguresGroupedByPaper();
    const live = sectionsFromConvex(grouped);
    if (live.length > 0) sections = live;
  } catch {
    // already logged in getAllFiguresGroupedByPaper; fall back silently
  }

  const totalFigures = sections.reduce((s, sec) => s + sec.items.length, 0);
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Research Figures · Spin-Torsion Cosmology Program
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          Figures
        </h1>
        <p className="subtitle">
          {`${totalFigures} research figures across all 6 papers (P1A · P1B · P2 · P3 · P4 · P5). In-paper figures are synced from each paper's current LaTeX source on every build; candidate figures are validated analysis outputs not yet included in a draft.`}
        </p>
      </div>

      <FigureGallery sections={sections} />
    </>
  );
}
