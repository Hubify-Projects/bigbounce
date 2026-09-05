import Link from "next/link";
import { Band, PageHeader, StatRow, EvidenceChip, RowList } from "@/components/primitives";
import { MathText } from "@/components/MathText";
import { tracks } from "@/data/tracks";
import { getPaperBySlug } from "@/data/papers";
import { getLivePapers, displayVersion } from "@/lib/livePapers";
import { getRecentActivity } from "@/lib/liveActivity";
import { reproPrograms, reproExperiments } from "@/data/repro";

// ──────────────────────────────────────────────────────────────────────
// Homepage — REDESIGN_SPEC.md §3.1. Full-width bands, no cards. Readiness
// and version numbers come ONLY from lib/livePapers.ts (Convex-first);
// this file never re-types a readiness percentage.
// ──────────────────────────────────────────────────────────────────────

const NULLS = [
  {
    label: "Pulsar timing (nHz background)",
    detail: "14.3 dex below the NANOGrav 15-yr signal",
    href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/track_a3_multichannel",
  },
  {
    label: "Primordial black holes",
    detail: "f_PBH = 0, 7.0 dex short of a detectable population",
    href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/track_a3_multichannel",
  },
  {
    label: "High-z PNG / early-SMBH seeds",
    detail: "FIRAS excludes the amplitude by roughly 1.8e3×",
    href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/track_a3_multichannel",
  },
  {
    label: "Chiral gravitational waves (LISA band)",
    detail: "no parity-odd operator exists in minimal ECH; Δ_h ≤ 6e−13",
    href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/chiral_gw_gate",
  },
];

export default async function HomePage() {
  const live = await getLivePapers();
  const liveBySlug = new Map(live.map((p) => [p.slug, p]));

  const runnableCount = reproExperiments.filter((e) => e.status === "runnable-now").length;
  const totalCostUsd = reproExperiments.reduce(
    (acc, e) => acc + (e.reproduction?.est_cost_usd ?? 0),
    0,
  );
  const publishReadyCount = live.filter((p) => p.readinessComputed >= 90).length;

  const activity = await getRecentActivity(5);

  return (
    <>
      {/* 1 — Hero */}
      <Band tone="base" width="content">
        <p className="eyebrow">Spin-torsion cosmology · reproducible lab</p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontSize: 44, fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.02em", margin: "8px 0 12px", maxWidth: "16ch" }}>
          Was the Big Bang the beginning?
        </h1>
        <p style={{ fontSize: 19, lineHeight: 1.55, maxWidth: "62ch", color: "var(--text-secondary)" }}>
          This lab tests a nonsingular bounce against data that exists now — and publishes the nulls.
        </p>
        <div style={{ display: "flex", gap: 20, marginTop: 18, fontSize: 15 }}>
          <Link href="/explained" style={{ color: "var(--accent)", fontWeight: 600 }}>
            Start with the explainer &rarr;
          </Link>
          <Link href="/papers" style={{ color: "var(--text-secondary)" }}>
            All works
          </Link>
        </div>
      </Band>

      {/* 2 — Live result strip */}
      <Band tone="base" width="content">
        <StatRow
          items={[
            { value: publishReadyCount, label: "works publish-ready", href: "/status" },
            { value: 3, label: "channels closed as nulls", href: "#nulls" },
            { value: runnableCount, label: "experiment manifests runnable now", href: "/reproduce" },
            { value: `$${totalCostUsd.toFixed(2)}`, label: "estimated reproduction cost", href: "/reproduce" },
          ]}
        />
      </Band>

      {/* 3 — The claim band */}
      <Band tone="alt" width="prose">
        <p className="eyebrow">The lab's strongest sentence</p>
        <p className="mono" style={{ fontSize: 22, textAlign: "center", margin: "18px 0" }}>
          <MathText>{"f_NL^local = −35/16  →  f_NL^after ∈ [−0.65, −0.50]"}</MathText>
        </p>
        <p style={{ fontSize: 14.5, lineHeight: 1.6, color: "var(--text-secondary)", textAlign: "center" }}>
          The exact matter-contraction amplitude, transmitted through an explicit nonsingular bounce — the number a survey would actually see.
        </p>
        <div style={{ textAlign: "center", marginTop: 8 }}>
          <EvidenceChip grade="derived" />
        </div>
      </Band>

      {/* 4 — Three tracks band */}
      <Band tone="base" width="content">
        <p className="eyebrow">Research tracks</p>
        <div className="row-list" style={{ marginTop: 8 }}>
          {tracks.map((track) => {
            const leadSlug = track.paperSlugs[0];
            const lp = leadSlug ? liveBySlug.get(leadSlug) : undefined;
            const stat = leadSlug ? getPaperBySlug(leadSlug) : undefined;
            const readiness = lp?.readinessComputed ?? stat?.readiness;
            return (
              <Link key={track.slug} href={`/research/${track.slug}`} className="row">
                <span className="row-main">
                  <span className="row-title" style={{ fontSize: 18 }}>{track.navTitle}</span>
                  <span className="row-purpose">{track.leadResult}</span>
                  <span className="row-chips">
                    <EvidenceChip grade={track.leadGrade} />
                  </span>
                </span>
                {readiness !== undefined && (
                  <span className="row-right mono">{readiness}% ready</span>
                )}
              </Link>
            );
          })}
        </div>
      </Band>

      {/* 5 — Nulls band */}
      <Band tone="deep" width="content" id="nulls">
        <p className="eyebrow">What we ruled out</p>
        <div className="row-list" style={{ marginTop: 8 }}>
          {NULLS.map((n) => (
            <a key={n.label} href={n.href} target="_blank" rel="noreferrer" className="row">
              <span className="row-main">
                <span className="row-title">{n.label}</span>
                <span className="row-purpose">{n.detail} — closed as a null.</span>
              </span>
              <span className="row-right">
                <EvidenceChip grade="null" />
              </span>
            </a>
          ))}
        </div>
        <p style={{ marginTop: 12, fontSize: 13.5 }}>
          <a href="/research#contributions" style={{ color: "var(--accent)" }}>
            See every contribution the lab claims &rarr;
          </a>
        </p>
      </Band>

      {/* 6 — Reproducibility band */}
      <Band tone="base" width="content">
        <p className="eyebrow">Reproducibility</p>
        <p style={{ fontSize: 15, lineHeight: 1.6, maxWidth: "70ch", marginBottom: 12 }}>
          Every experiment carries a manifest — inputs, scripts, compute venue, and an estimated
          cost and wall-clock time to reproduce it. BigBounce is the flagship reproducible lab for
          the Hubify platform.
        </p>
        <StatRow
          items={[
            { value: reproPrograms.length, label: "programs", href: "/reproduce" },
            { value: reproExperiments.length, label: "experiment manifests", href: "/reproduce" },
            { value: runnableCount, label: "runnable now", href: "/reproduce" },
          ]}
        />
        <p style={{ marginTop: 12, fontSize: 13.5 }}>
          <a href="https://huggingface.co/bamfai" target="_blank" rel="noreferrer" style={{ color: "var(--accent)" }}>
            HuggingFace
          </a>{" · "}
          <a href="https://github.com/Hubify-Projects/bigbounce" target="_blank" rel="noreferrer" style={{ color: "var(--accent)" }}>
            Backblaze B2 (via GitHub source)
          </a>{" · "}
          <Link href="/reproduce" style={{ color: "var(--accent)" }}>Zenodo releases &amp; DOIs &rarr;</Link>
        </p>
      </Band>

      {/* 7 — Latest band */}
      <Band tone="alt" width="content">
        <p className="eyebrow">Latest</p>
        <RowList
          items={activity.events.slice(0, 5).map((e) => ({
            title: e.headline,
            purpose: e.detail,
            href: "/activity",
            right: new Date(e.timestamp).toISOString().slice(0, 10),
          }))}
        />
        <p style={{ marginTop: 10, fontSize: 13 }}>
          <Link href="/activity" style={{ color: "var(--accent)" }}>Full activity feed &rarr;</Link>
        </p>
      </Band>
    </>
  );
}
