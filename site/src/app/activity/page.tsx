import { FeedItem } from "@/components/Feed/FeedItem";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Activity",
  description: "Live research status and chronological timeline of the BigBounce program.",
};

export default function ActivityPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>Live Research Activity</p>
        <h1>Activity Feed</h1>
        <p className="subtitle">
          What we&apos;re working on now, what happened recently, and what&apos;s coming next.
        </p>
      </div>

      {/* Current Focus Banner */}
      <div className="card" style={{ borderLeft: "4px solid #1e40af", marginBottom: 32 }}>
        <div style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: "0.06em", fontWeight: 700, color: "#1e40af", marginBottom: 4 }}>
          Current Research Focus
        </div>
        <div style={{ fontSize: "1.15rem", fontWeight: 700, marginBottom: 6 }}>
          Full Project Reset &mdash; Houston Method v2, Wiki, Next.js, H200 Queue v2
        </div>
        <p style={{ fontSize: 14, color: "var(--text-secondary)", margin: 0, lineHeight: 1.6 }}>
          Quality audit revealed 6 of 10 H200 experiments have QC failures.
          Implementing Houston Method v2: mandatory 9-step completion loop.
          New H200 pod active with 50-experiment queue across 10 phases.
          First re-run (Planck CMB with galactic mask) already PASSES QC.
          Est. total: ~492 GPU-hours, ~$1,768.
        </p>
      </div>

      <hr />

      <section className="section">
        <h2>Research Timeline</h2>
        <div className="feed">
          <FeedItem
            date="2026-04-04"
            title="Planck CMB Re-Run PASSES QC — Galactic Mask Fix Works"
            type="positive"
            tags={["Planck CMB", "QC PASS", "Phase 1", "H200 Queue v2"]}
          >
            Re-ran Planck CMB anomaly detection with GAL080 galactic mask applied
            before patch extraction. val_loss=0.138 (was 0.831). Top anomaly at
            RA=208.5°, Dec=-21.2° (no longer at Dec&lt;-84° galactic pole).
            193 anomalies from 19,296 masked patches. First Phase 1 experiment complete.
          </FeedItem>

          <FeedItem
            date="2026-04-04"
            title="Full Project Reset: Houston Method v2, Wiki, Next.js, H200 Queue v2"
            type="milestone"
            tags={["Quality Audit", "Houston Method v2", "Wiki", "Next.js", "Project Reset"]}
          >
            Quality audit of H200 results revealed 6/10 experiments have QC failures:
            Planck CMB (galactic contamination), ACT DR6 (undertrained), NEOWISE
            (ecliptic systematic), super-resolution (null coordinates), taxonomy
            (degenerate clustering), Gaia (sample too small). Implemented Houston Method
            v2 with mandatory 9-step completion loop. Created Karpathy-style wiki
            (25 pages). Scaffolded Next.js app. H200 pod terminated by credit expiry
            — all data safe. New 50-experiment queue designed.
          </FeedItem>

          <FeedItem
            date="2026-04-04"
            title="H200 Pod Terminated — Credits Expired Overnight, All Data Safe"
            type="negative"
            tags={["Infrastructure", "Pod Terminated", "No Data Loss"]}
          >
            RunPod credits ran out during the night of Apr 3-4. H200 pod terminated.
            No data lost — all 10 experiment results were already backed up to local
            disk. New pod provisioned with fresh credits for queue v2.
          </FeedItem>

          <FeedItem
            date="2026-04-03"
            title="ACT Birefringence: β = 17.4° ± 12.1° — Systematic-Dominated"
            tags={["Birefringence", "Systematic", "ACT DR6"]}
          >
            Ran birefringence estimator on real ACT DR6 5.3GB IQU map. Result:
            β = 17.4° ± 12.1° — NOT consistent with 0.27° prediction. Root cause:
            flat-sky FFT picks up galactic foreground Q/U leakage. Needs proper
            analysis with NaMaster/PolSpice + galactic mask.
          </FeedItem>

          <FeedItem
            date="2026-04-03"
            title="f_NL Multi-Tracer Pipeline: 6.1% Improvement — PUBLISHABLE"
            type="positive"
            tags={["f_NL", "Multi-Tracer", "Publishable"]}
          >
            Ran full f_NL pipeline on DESI + SDSS anomalies. σ(f_NL) improved 6.1%
            (DESI alone) and 16.4% (DESI+SDSS combined). Clears 5% threshold for
            publication. SPHEREx forecast: 4.38σ detection of f_NL = -35/8.
          </FeedItem>

          <FeedItem
            date="2026-04-02"
            title="All 10 H200 Experiments Complete — 33.5M Sources, 328K Anomalies"
            type="milestone"
            tags={["H200 Queue", "Multi-Survey", "Complete"]}
          >
            Multi-survey anomaly sweep finished: DESI, SDSS, LAMOST, eROSITA,
            Planck, ACT, NEOWISE, Gaia + NANOGrav consistency + super-resolution.
            Grand total: 33.5M sources scored, 328,448 anomalies across 8 surveys.
            (Later audit revealed 6/10 need re-running due to QC issues.)
          </FeedItem>
        </div>
      </section>
    </>
  );
}
