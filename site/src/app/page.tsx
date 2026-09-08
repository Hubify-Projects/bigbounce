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
  const readiness95Count = live.filter((p) => p.readinessComputed === 95).length;

  return (
    <>
      {/* ACT I — the question. One display line, one accent moment. */}
      <Band tone="base" width="content" open>
        <p className="eyebrow">Spin-torsion cosmology · reproducible lab</p>
        <h1 className="display-line">Was the Big Bang the beginning?</h1>
        <p className="band-lede">
          This lab tests a nonsingular bounce against data that exists now — and publishes the
          nulls.
        </p>
        <div className="link-row">
          <Link href="/explained" className="band-link band-link-accent">
            Start with the explainer &rarr;
          </Link>
          <Link href="/papers" className="band-link">
            All works
          </Link>
        </div>
      </Band>

      {/* ACT II — where the work stands. Tone shifts once; the two bands
          below share it and are separated by whitespace, not a border. */}
      <Band tone="alt" width="content">
        <div className="band-head">
          <p className="eyebrow">Where the work stands</p>
          <h2 className="band-title">Current results, read from the live record.</h2>
        </div>
        <StatRow
          items={[
            { value: publishReadyCount, label: "works publish-ready", href: "/status" },
            { value: 3, label: "channels closed as nulls", href: "#nulls" },
            { value: runnableCount, label: "experiment manifests runnable now", href: "/reproduce" },
            { value: `$${totalCostUsd.toFixed(2)}`, label: "estimated reproduction cost", href: "/reproduce" },
          ]}
        />
      </Band>

      <Band tone="alt" width="content" tight>
        <div className="band-head">
          <p className="eyebrow">Research tracks</p>
          <h2 className="band-title">Three tracks, each with a lead result.</h2>
        </div>
        <div className="row-list">
          {tracks.map((track) => {
            const leadSlug = track.paperSlugs[0];
            const lp = leadSlug ? liveBySlug.get(leadSlug) : undefined;
            const stat = leadSlug ? getPaperBySlug(leadSlug) : undefined;
            const readiness = lp?.readinessComputed ?? stat?.readiness;
            return (
              <Link key={track.slug} href={`/research/${track.slug}`} className="row">
                <span className="row-main">
                  <span className="row-title">{track.navTitle}</span>
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
        <p className="band-note">
          <Link href="/research" className="band-link">
            The three tracks in full &rarr;
          </Link>
        </p>
      </Band>

      {/* ACT III — the nulls, stated as results, then the strongest sentence. */}
      <Band tone="base" width="content" id="nulls">
        <div className="band-head">
          <p className="eyebrow">What we ruled out</p>
          <h2 className="band-title">Nulls are results. These channels are closed.</h2>
        </div>
        <div className="row-list">
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
        <p className="band-note">
          <a href="/research#contributions" className="band-link">
            Every contribution the lab claims &rarr;
          </a>
        </p>
      </Band>

      <Band tone="base" width="prose" tight>
        <p className="eyebrow">The lab&rsquo;s strongest sentence</p>
        <p className="claim-line mono">
          <MathText>{"f_NL^local = −35/16  →  f_NL^after ∈ [−0.65, −0.50]"}</MathText>
        </p>
        <p className="band-body">
          The exact matter-contraction amplitude, transmitted through an explicit nonsingular
          bounce — the number a survey would actually see.
        </p>
        <p className="claim-grade">
          <EvidenceChip grade="derived" />
        </p>
      </Band>

      {/* ACT IV — how the lab works. */}
      <Band tone="alt" width="prose">
        <div className="band-head">
          <p className="eyebrow">Started from one question</p>
          <h2 className="band-title">A reproducible research agent, guided by a human.</h2>
        </div>
        <p className="band-body">
          One question, months of work, many lanes of research. A human asks the next question,
          approves the compute, and pushes back. What if your next question could lead to a
          discovery?
        </p>
        <StatRow
          className="stat-row-quiet"
          items={[
            { value: 17, label: "ledger rows worked (as of 2026-09-04)", href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/NEXT_SCIENCE_LEDGER.md" },
            { value: reproPrograms.length, label: "reproducibility programs", href: "/reproduce" },
            { value: reproExperiments.length, label: "reproducibility manifests", href: "/reproduce" },
            { value: readiness95Count, label: "works at readiness 95", href: "/status" },
            { value: NULLS.length, label: "channels published as nulls", href: "#nulls" },
          ]}
        />
      </Band>

      <Band tone="alt" width="content" tight>
        <div className="band-head">
          <p className="eyebrow">Reproducibility</p>
          <h2 className="band-title">Every experiment carries a manifest.</h2>
        </div>
        <p className="band-body">
          Inputs, scripts, compute venue, and an estimated cost and wall-clock time to reproduce
          it. BigBounce is the flagship reproducible lab for the Hubify platform.
        </p>
        <div className="link-row">
          <Link href="/reproduce" className="band-link">Reproduce it &rarr;</Link>
          <a href="https://huggingface.co/bamfai" target="_blank" rel="noreferrer" className="band-link">
            HuggingFace
          </a>
          <a href="https://github.com/Hubify-Projects/bigbounce" target="_blank" rel="noreferrer" className="band-link">
            GitHub source
          </a>
          <Link href="/reproduce" className="band-link">Zenodo releases &amp; DOIs</Link>
        </div>
      </Band>

      {/* ACT V — the running record. */}
      <Band tone="deep" width="content" close>
        <div className="band-head">
          <p className="eyebrow">Latest</p>
          <h2 className="band-title">What changed most recently.</h2>
        </div>
        <RowList
          items={activity.events.slice(0, 5).map((e) => ({
            title: e.headline,
            purpose: e.detail,
            href: "/activity",
            right: new Date(e.timestamp).toISOString().slice(0, 10),
          }))}
        />
        <p className="band-note">
          <Link href="/activity" className="band-link">Full activity feed &rarr;</Link>
          {" · "}
          <Link href="/reviews" className="band-link">Review timeline &rarr;</Link>
        </p>
      </Band>
    </>
  );
}
