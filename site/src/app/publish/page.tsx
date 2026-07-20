import Link from "next/link";
import type { Metadata } from "next";
import {
  publishData,
  type PublishDecision,
  type PublishWave,
  type PublishBlocker,
  type PaperReadiness,
} from "@/data/publish";
import "./publish.css";

export const metadata: Metadata = {
  title: "Publication Command Center",
  description:
    "The publication decision dashboard: the five author-only decisions (D1–D5), the compressed submission plan, the single remaining blocker, and per-paper submission readiness across all six manuscripts.",
};

function StatusChip({ decision }: { decision: PublishDecision }) {
  if (decision.status === "done") {
    return <span className="pub-chip is-done">Done</span>;
  }
  if (decision.scheduleRisk) {
    return <span className="pub-chip is-risk">Pending · risk</span>;
  }
  return <span className="pub-chip is-pending">Pending</span>;
}

function DItems({ items }: { items: string[] }) {
  return (
    <span className="pub-ditems">
      {items.map((d) => (
        <span key={d} className="pub-ditem">
          {d}
        </span>
      ))}
    </span>
  );
}

function WaveCard({ wave }: { wave: PublishWave }) {
  const stateLabel =
    wave.state === "ready" ? "ready" : wave.state === "building" ? "building" : "queued";
  return (
    <div className="pub-wave">
      <div className="pub-wave-head">
        <span className="pub-wave-label">{wave.label}</span>
        <span className={`pub-wave-state state-${wave.state}`}>{stateLabel}</span>
      </div>
      <div className="pub-wave-order">
        {wave.order.map((p, i) => (
          <span key={p} style={{ display: "inline-flex", alignItems: "center", gap: 6 }}>
            {i > 0 && <span className="pub-wave-arrow">→</span>}
            <span className="pub-wave-step">{p}</span>
          </span>
        ))}
      </div>
      <p className="pub-wave-note">{wave.note}</p>
      {wave.kit && <span className="pub-wave-kit">{wave.kit}</span>}
    </div>
  );
}

function BlockerCard({ blocker }: { blocker: PublishBlocker }) {
  return (
    <div className={`pub-blocker sev-${blocker.severity}`}>
      <span className="pub-blocker-dot" aria-hidden="true" />
      <div className="pub-blocker-body">
        <p className="pub-blocker-title">
          {blocker.title}
          {blocker.decision && (
            <span className="pub-blocker-decision">{blocker.decision}</span>
          )}
        </p>
        <p className="pub-blocker-detail">{blocker.detail}</p>
      </div>
    </div>
  );
}

function PaperRow({ paper }: { paper: PaperReadiness }) {
  const waveTagClass = paper.wave === "wave-1" ? "tag-wave-1" : "";
  return (
    <tr>
      <td className="pub-td">
        <span className="pub-paper-code">{paper.code}</span>
        <span className="pub-paper-title">{paper.title}</span>
      </td>
      <td className="pub-td">
        <span className="pub-version">{paper.version}</span>
      </td>
      <td className="pub-td">
        <span className="pub-readiness">{paper.readiness}</span>
      </td>
      <td className="pub-td">
        <span className={`pub-wave-tag ${waveTagClass}`}>
          {paper.wave.replace("-", " ")}
        </span>
      </td>
      <td className="pub-td">{paper.board}</td>
      <td className="pub-td">
        <DItems items={paper.remaining} />
      </td>
    </tr>
  );
}

export default function PublishPage() {
  const { decisions, waves, blockers, papers, deadlineNote, lastUpdatedDisplay } = publishData;
  const openDecisions = decisions.filter((d) => d.status !== "done").length;

  return (
    <>
      <p className="pub-kicker">Publication Command Center</p>
      <h1 className="pub-title">The decision dashboard for the publication sprint</h1>
      <p className="pub-lede">{deadlineNote}</p>
      <p className="pub-meta">
        {openDecisions} decisions pending · six papers review-converged · updated {lastUpdatedDisplay}
      </p>

      {/* ── 1. The 5 decisions ─────────────────────────────────────────── */}
      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">01</span>
          <h2 className="pub-section-title">The five decisions</h2>
        </div>
        <p className="pub-section-sub">
          Each is a decision only Houston can make. Status chips are placeholders driven from the
          data file, so a sync can flip any to <strong>Done</strong> as it lands. D4 carries the
          schedule risk — make it first.
        </p>
        <div className="pub-table-wrap">
          <table className="pub-table">
            <thead>
              <tr>
                <th className="pub-th">Decision</th>
                <th className="pub-th">Status</th>
                <th className="pub-th">Options</th>
                <th className="pub-th">Recommendation</th>
                <th className="pub-th">Unblocks</th>
              </tr>
            </thead>
            <tbody>
              {decisions.map((d) => (
                <tr key={d.id} className={d.scheduleRisk ? "is-risk-row" : undefined}>
                  <td className="pub-td">
                    <span className="pub-id">{d.id}</span>
                    <span className="pub-decision-title">{d.title}</span>
                  </td>
                  <td className="pub-td">
                    <StatusChip decision={d} />
                  </td>
                  <td className="pub-td">{d.options}</td>
                  <td className="pub-td pub-rec">{d.recommendation}</td>
                  <td className="pub-td pub-unblocks">{d.unblocks}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* ── 2. The compressed plan ─────────────────────────────────────── */}
      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">02</span>
          <h2 className="pub-section-title">The compressed plan</h2>
        </div>
        <p className="pub-section-sub">
          Everything executes today / ASAP. Wave 1's click-walkthrough is written and verified; wave
          2's kit is being assembled now; P5 follows the moment P4 has an arXiv ID.
        </p>
        <div className="pub-waves">
          {waves.map((w) => (
            <WaveCard key={w.id} wave={w} />
          ))}
        </div>
      </section>

      {/* ── 3. Blockers ────────────────────────────────────────────────── */}
      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">03</span>
          <h2 className="pub-section-title">Blockers</h2>
        </div>
        <p className="pub-section-sub">
          One honest blocker remains on the critical path. Everything else is green.
        </p>
        <div className="pub-blockers">
          {blockers.map((b) => (
            <BlockerCard key={b.title} blocker={b} />
          ))}
        </div>
      </section>

      {/* ── 4. Per-paper submission readiness ──────────────────────────── */}
      <section className="pub-section">
        <div className="pub-section-head">
          <span className="pub-section-index">04</span>
          <h2 className="pub-section-title">Submission readiness — all six</h2>
        </div>
        <p className="pub-section-sub">
          Version, the last exact-PDF board and its disposition, the submission wave, and which
          decisions still gate each paper. Readiness caps hold pending human review and archive/DOI
          gates; no verdict word converts into journal acceptance.
        </p>
        <div className="pub-table-wrap">
          <table className="pub-table">
            <thead>
              <tr>
                <th className="pub-th">Paper</th>
                <th className="pub-th">Version</th>
                <th className="pub-th">Readiness</th>
                <th className="pub-th">Wave</th>
                <th className="pub-th">Board state</th>
                <th className="pub-th">Remaining</th>
              </tr>
            </thead>
            <tbody>
              {papers.map((p) => (
                <PaperRow key={p.code} paper={p} />
              ))}
            </tbody>
          </table>
        </div>
        <p className="pub-note">
          Full round-by-round history lives at{" "}
          <Link href="/reviews">/reviews</Link>; per-paper detail at{" "}
          <Link href="/paper">/papers</Link>. Machine events stream at{" "}
          <Link href="/activity">/activity</Link>.
        </p>
      </section>
    </>
  );
}
