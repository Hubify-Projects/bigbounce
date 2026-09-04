import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { Band, PageHeader, EvidenceChip, DataTable, RowList } from "@/components/primitives";
import { MathText } from "@/components/MathText";
import { tracks, getTrack } from "@/data/tracks";
import { getPaperBySlug } from "@/data/papers";
import { getLivePapers, displayVersion } from "@/lib/livePapers";

export function generateStaticParams() {
  return tracks.map((t) => ({ track: t.slug }));
}

export function generateMetadata({
  params,
}: {
  params: { track: string };
}): Metadata {
  const track = getTrack(params.track);
  if (!track) return { title: "Track not found" };
  return {
    title: track.navTitle,
    description: track.question,
  };
}

export default async function TrackPage({
  params,
}: {
  params: { track: string };
}) {
  const track = getTrack(params.track);
  if (!track) notFound();

  const live = await getLivePapers();
  const liveBySlug = new Map(live.map((p) => [p.slug, p]));

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

  return (
    <>
      <Band tone="base" width="content">
        <PageHeader
          eyebrow={`Research · ${track.navTitle}`}
          title={<MathText>{track.question}</MathText>}
        />
      </Band>

      <Band tone="alt" width="prose">
        <p className="eyebrow">Lead result</p>
        {track.leadEquation && (
          <p
            className="mono"
            style={{ fontSize: 19, textAlign: "center", margin: "16px 0" }}
          >
            <MathText>{track.leadEquation}</MathText>
          </p>
        )}
        <p style={{ fontSize: 16, lineHeight: 1.65, marginBottom: 12 }}>
          {track.leadResult}
        </p>
        <EvidenceChip grade={track.leadGrade} />
      </Band>

      <Band tone="base" width="content">
        <p className="eyebrow">Channels &amp; tests</p>
        <DataTable
          columns={[
            { key: "channel", header: "Channel", accessor: (r) => r.channel },
            { key: "prediction", header: "Prediction", accessor: (r) => r.prediction },
            { key: "currentData", header: "Current data", accessor: (r) => r.currentData },
            {
              key: "grade",
              header: "Evidence",
              accessor: (r) => <EvidenceChip grade={r.grade} />,
            },
            {
              key: "receipt",
              header: "Receipt",
              accessor: (r) => (
                <a href={r.receiptHref} target="_blank" rel="noreferrer" className="mono">
                  {r.receiptLabel}
                </a>
              ),
            },
          ]}
          rows={track.channels}
          rowKey={(r) => r.channel}
        />
      </Band>

      <Band tone="alt" width="content">
        <p className="eyebrow">Works in this track</p>
        <RowList
          items={works.map((w) => ({
            title: w.title,
            purpose: w.plainTitle,
            href: `/papers/${w.slug}`,
            right: `${displayVersion(w.version)} · ${w.readiness}%`,
          }))}
        />
      </Band>

      <Band tone="base" width="prose">
        <p className="eyebrow">What is still open</p>
        <div className="row-list">
          {track.openItems.map((o) => (
            <div className="row" key={o.item}>
              <span className="row-main">
                <span className="row-title">{o.item}</span>
                <span className="row-purpose">{o.blocker}</span>
              </span>
            </div>
          ))}
        </div>
      </Band>

      <Band tone="deep" width="prose">
        <p className="eyebrow">Boundary</p>
        <p style={{ fontSize: 15, lineHeight: 1.65 }}>{track.boundary}</p>
      </Band>
    </>
  );
}
