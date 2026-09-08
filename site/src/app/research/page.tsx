import type { Metadata } from "next";
import { Band, PageHeader, EvidenceChip, RowList } from "@/components/primitives";
import { MathText } from "@/components/MathText";
import { tracks, contributions } from "@/data/tracks";
import { getPaperBySlug } from "@/data/papers";
import { getLivePapers, displayVersion } from "@/lib/livePapers";
import { CONTRIBUTION_TYPE_LABEL, CONTRIBUTION_TYPE_HINT } from "@/lib/contributionTypes";

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
      <Band tone="base" width="content" open>
        <PageHeader
          eyebrow="Research"
          title="Three questions, three lead results"
          lead="Started from one question — was the Big Bang the beginning? The portfolio is organized by scientific question, not a fixed paper count. Track A is the flagship line testing bounce vs. inflation; Track B is one closed theory Note; Track C is DESI data products tested against a specific physical prediction, on-vision per the lab's guiding question."
        />
      </Band>

      {tracks.map((track, i) => {
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
          <Band
            tone={i % 2 === 0 ? "alt" : "base"}
            width="content"
            key={track.slug}
            tight={i > 0}
          >
            <div className="band-head">
              <p className="eyebrow">{track.navTitle}</p>
              <h2 className="band-title">
                <MathText>{track.question}</MathText>
              </h2>
            </div>
            <p className="band-body" style={{ marginTop: 0 }}>{track.leadResult}</p>
            <div className="chip-line">
              <EvidenceChip grade={track.leadGrade} />
              {lead && (
                <span className="evidence-chip evidence-chip-type">
                  <span className="evidence-chip-dot" aria-hidden="true" />
                  readiness {lead.readiness}% &middot; {displayVersion(lead.version)}
                </span>
              )}
            </div>
            <div style={{ marginTop: "var(--space-7)" }}>
              <RowList
                items={works.map((w) => ({
                  title: w.title,
                  purpose: w.plainTitle,
                  href: `/papers/${w.slug}`,
                  right: `${displayVersion(w.version)} · ${w.readiness}%`,
                }))}
              />
            </div>
            <p className="band-note">
              <a href={`/research/${track.slug}`} className="band-link">
                Full track — channels, open items, boundary &rarr;
              </a>
            </p>
          </Band>
        );
      })}

      <Band tone="deep" width="content" id="contributions" close>
        <div className="band-head">
          <p className="eyebrow">Contributions</p>
          <h2 className="band-title">What&rsquo;s novel here</h2>
        </div>
        <p className="band-body" style={{ marginTop: 0, marginBottom: "var(--space-7)" }}>
          Every result the lab claims as its own — what kind of contribution it is, and how novel,
          ranked on a four-tier scale. Self-claim ceiling is N3 (first-of-kind); N4
          (paradigm-shifting) is reserved for outside arbiters and never self-claimed.
        </p>
        <RowList
          items={contributions.map((c) => ({
            title: c.title,
            purpose: `${TIER_LABEL[c.tier]} · ${c.track} — ${c.oneLine}`,
            href: c.href,
            right: c.tier,
            chips: (
              <span
                className="evidence-chip evidence-chip-type"
                title={CONTRIBUTION_TYPE_HINT[c.contributionType]}
              >
                <span className="evidence-chip-dot" aria-hidden="true" />
                {CONTRIBUTION_TYPE_LABEL[c.contributionType]}
              </span>
            ),
            external: c.href.startsWith("http"),
          }))}
        />
      </Band>
    </>
  );
}
