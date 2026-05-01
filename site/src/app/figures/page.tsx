import type { Metadata } from"next";
import { figureSections } from"@/data/figures";
import { FigureGallery } from"./figure-gallery";

export const metadata: Metadata = {
  title:"Figures",
  description:
"Gallery of 64 research figures from the BigBounce spin-torsion cosmology program.",
};

export default function FiguresPage() {
  const totalFigures = figureSections.reduce((s, sec) => s + sec.items.length, 0);
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Research Figures · Spin-Torsion Cosmology Program
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Figures
        </h1>
        <p className="subtitle">
          Gallery of {totalFigures} research figures spanning all 4 papers,
          MCMC verification, survey mining, and chirality catalog work.
        </p>
      </div>

      <FigureGallery sections={figureSections} />
    </>
  );
}
