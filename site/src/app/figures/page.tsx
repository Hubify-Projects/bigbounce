import type { Metadata } from "next";
import { figureSections } from "@/data/figures";
import { FigureGallery } from "./figure-gallery";

export const metadata: Metadata = {
  title: "Figures",
  description:
    "Gallery of 64 research figures from the BigBounce spin-torsion cosmology program.",
};

export default function FiguresPage() {
  const totalFigures = figureSections.reduce((s, sec) => s + sec.items.length, 0);
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Figures · Spin-Torsion Cosmology Program
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          Figures
        </h1>
        <p className="subtitle">
          Gallery of {totalFigures} research figures spanning all 4 papers and the
          MCMC verification work. Click any figure to view full-size.
        </p>
      </div>

      <FigureGallery sections={figureSections} />
    </>
  );
}
