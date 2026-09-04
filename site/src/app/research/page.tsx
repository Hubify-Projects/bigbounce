import type { Metadata } from "next";
import { Band, PageHeader, EvidenceChip, RowList } from "@/components/primitives";
import { MathText } from "@/components/MathText";
import { tracks, contributions } from "@/data/tracks";
import { getPaperBySlug } from "@/data/papers";
import { getLivePapers, displayVersion } from "@/lib/livePapers";

export const metadata: Metadata = {
  title: "Research",
  description:
    "Three research tracks — bounce vs. inflation, the ECH Note, and DESI data products — each with its lead result, evidence, and open questions.",
};

const TIER_LABEL: Record<string, string> = {
  N3: "First-of-kind demonstration",
  N2: "Novel combination / extension",
  N1: "Incremental refinement / replication",
};

export default async function ResearchPage() {
  const live = await getLivePapers();
  const liveBySlug = new Map(live.map((p) => [p.slug, p]));

  return (
    <>
      <Band tone="base" width="content">
        <PageHeader
          eyebrow="Research"
          title="Three questions, three lead results"
          lead="The portfolio is organized by scientific question, not a fixed paper count. Track A is the flagship line testing bounce vs. inflation; Track B is one closed theory Note; Track C is DESI data products tested against a specific physical prediction, on-vision per the lab's guiding question — was the Big Bang the beginning?"
        />
      </Band>

      {tracks.map((track) => {
        const works = track.paperSlugs
          .map((slug) => {
            const stat = getPaperBySlug(slug);
            const lp = liveBySlug.get(slug);
            if (!stat) return null;
            return {
              slug,
              title: stat.title,
              plainTitle: stat.plainTitle,
              version: lp?.currentVersion ?? stat.version,
              readiness: lp?.readinessComputed ?? stat.readiness,
            };
          })
          .filter((w): w is NonNullable<typeof w> => w !== null);
        const lead = works[0];

        return (
          <Band tone="alt" width="content" key={track.slug}>
            <p className="eyebrow">{track.navTitle}</p>
            <h3 style={{ margin: "4px 0 8px", fontSize: 20 }}>
              <MathText>{track.question}</MathText>
            </h3>
            <p style={{ fontSize: 14.5, lineHeight: 1.6, maxWidth: "70ch", marginBottom: 6 }}>
              {track.leadResult}
            </p>
            <EvidenceChip grade={track.leadGrade} />
            {lead && (
              <p style={{ marginTop: 8, fontSize: 13, fontFamily: "var(--font-mono-stack)" }}>
                Readiness: {lead.readiness}% · {displayVersion(lead.version)}
              </p>
            )}
            <div style={{ marginTop: 10 }}>
              <RowList
                items={works.map((w) => ({
                  title: w.title,
                  purpose: w.plainTitle,
                  href: `/papers/${w.slug}`,
                  right: `${displayVersion(w.version)} · ${w.readiness}%`,
                }))}
              />
            </div>
            <p style={{ marginTop: 10, fontSize: 13 }}>
              <a href={`/research/${track.slug}`} style={{ color: "var(--accent)" }}>
                Full track — channels, open items, boundary &rarr;
              </a>
            </p>
          </Band>
        );
      })}

      <Band tone="base" width="content" id="contributions">
        <p className="eyebrow">Contributions</p>
        <PageHeader
          title="What's novel here"
          lead="Every result the lab claims as its own, ranked on a four-tier novelty scale. Self-claim ceiling is N3 (first-of-kind); N4 (paradigm-shifting) is reserved for outside arbiters and never self-claimed."
        />
        <RowList
          items={contributions.map((c) => ({
            title: c.title,
            purpose: `${TIER_LABEL[c.tier]} · ${c.track} — ${c.oneLine}`,
            href: c.href,
            right: c.tier,
            external: c.href.startsWith("http"),
          }))}
        />
      </Band>
    </>
  );
}
