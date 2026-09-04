import type { Metadata } from "next";
import { Band, PageHeader, RowList } from "@/components/primitives";
import { getAllFiguresGroupedByPaper } from "@/lib/livePapers";
import { figureSections } from "@/data/figures";

export const metadata: Metadata = {
  title: "Explore",
  description: "Interactive tools for the BigBounce datasets — galaxy chirality, anomaly candidates, Bayes-factor discrimination, the bounce visualized, and every research figure.",
};

export default async function ExplorePage() {
  let figureCount = figureSections.reduce((s, sec) => s + sec.items.length, 0);
  try {
    const grouped = await getAllFiguresGroupedByPaper();
    const liveCount = Object.values(grouped).reduce((s, rows) => s + rows.length, 0);
    if (liveCount > 0) figureCount = liveCount;
  } catch {
    // static fallback count already set
  }

  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow="Explore"
          title="Explore the data"
          lead="Five interactive tools, direct access to the datasets behind the papers — no paper required."
        />
      </Band>
      <Band width="content">
        <RowList
          items={[
            {
              title: "Galaxy chirality explorer",
              purpose: "8.47M DESI galaxies tested for a handedness dipole (result: null).",
              href: "/galaxy-explorer",
              right: "8.47M galaxies",
            },
            {
              title: "Anomaly candidate explorer",
              purpose: "DESI spectral anomaly candidates from the autoencoder pipeline.",
              href: "/anomaly-explorer",
              right: "77,905 candidates",
            },
            {
              title: "Bayes-factor data explorer",
              purpose: "Bounce-vs-inflation discrimination power across current survey constraints.",
              href: "/data-explorer",
            },
            {
              title: "Visualize the bounce",
              purpose: "A 3D scene of parent-universe collapse through the bounce.",
              href: "/visualize",
            },
            {
              title: "Figures",
              purpose: "Every research figure across every work, filterable by track.",
              href: "/explore/figures",
              right: `${figureCount} figures`,
            },
          ]}
        />
      </Band>
    </>
  );
}
