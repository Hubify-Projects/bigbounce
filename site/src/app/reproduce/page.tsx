import Link from "next/link";
import type { Metadata } from "next";
import { reproPrograms, type ReproStatus } from "@/data/repro";
import {
  labRollup,
  programRollup,
  programExperimentsInDagOrder,
  paperSlugForCode,
  formatCost,
  STATUS_LABEL,
} from "@/lib/reproLab";
import { Badge } from "@/components/ui/badge";

export const metadata: Metadata = {
  title: "Reproduce This Lab",
  description:
    "Every BigBounce research program and every individual experiment carries a manifest — sealed inputs, exact entrypoints, and a verification method — so a stranger, or Hubify, can reproduce it.",
};

const STATUS_VARIANT: Record<ReproStatus, "green" | "amber" | "neutral"> = {
  "runnable-now": "green",
  "needs-data-restore": "amber",
  superseded: "neutral",
};

export default function ReproducePage() {
  const lab = labRollup();

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Reproducibility &middot; manifests
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          Reproduce this lab
        </h1>
        <p className="subtitle">
          The lab contract: every experiment, simulation, derivation, training run, scan, or
          analysis ships a manifest with sealed inputs (external data with links, or repo-pinned
          internal artifacts), exact entrypoints (the literal command that runs it), and a
          verification method — so a stranger, or Hubify, can reproduce it without asking us
          anything. The full-reproduction pass across every program is the final pre-publication
          test of this lab, not an afterthought.
        </p>
      </div>

      <section className="section">
        <div className="insight-strip">
          <div className="insight">
            <div className="insight-label">Research programs</div>
            <div className="insight-value">{lab.totalPrograms}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Experiment manifests</div>
            <div className="insight-value">{lab.totalExperiments}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Runnable now</div>
            <div className="insight-value">{lab.runnableNow}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Est. total reproduction cost</div>
            <div className="insight-value">{formatCost(lab.totalEstCostUsd)}</div>
          </div>
        </div>
        <p
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: "0.72rem",
            color: "var(--text-muted)",
            marginTop: 10,
          }}
        >
          {lab.needsDataRestore} experiment{lab.needsDataRestore === 1 ? "" : "s"} need a data
          restore before they can run; {lab.superseded} {lab.superseded === 1 ? "is" : "are"}{" "}
          superseded and kept for lineage only, never offered as a live reproduction target.
          Per-program cost/time estimates are rollups, not literal sums of the individual
          experiment estimates below — see each program&apos;s <code>full_reproduction.order</code>{" "}
          note for sequencing.
        </p>
      </section>

      {reproPrograms.map((program) => {
        const rollup = programRollup(program);
        const rows = programExperimentsInDagOrder(program);

        return (
          <section className="section" key={program.id}>
            <p className="text-xs sans" style={{ marginBottom: 8 }}>
              Research program &middot; {program.id}
            </p>
            <h2>{program.title}</h2>
            <p
              className="text-sm text-muted-foreground leading-relaxed"
              style={{ maxWidth: "78ch", marginTop: 6 }}
            >
              <strong className="text-foreground">Question:</strong> {program.question}
            </p>

            <div style={{ display: "flex", flexWrap: "wrap", gap: 16, margin: "12px 0 4px" }}>
              <span style={{ fontFamily: "var(--font-mono-stack)", fontSize: 12.5, color: "var(--text-tertiary)" }}>
                {rollup.totalExperiments} experiments &middot; {rollup.runnableNow} runnable now
              </span>
              <span style={{ fontFamily: "var(--font-mono-stack)", fontSize: 12.5, color: "var(--text-tertiary)" }}>
                full reproduction: {formatCost(rollup.estCostUsd)} &middot; {rollup.estWallClock}
              </span>
            </div>

            <h3 style={{ fontFamily: "var(--font-mono-stack)", fontSize: 14, marginTop: 20 }}>
              Papers
            </h3>
            <div style={{ display: "grid", gap: 0, marginTop: 4 }}>
              {program.papers.map((p, i) => {
                const slug = paperSlugForCode(p.paper);
                return (
                  <div
                    key={`${p.paper}-${i}`}
                    style={{
                      display: "flex",
                      flexWrap: "wrap",
                      alignItems: "baseline",
                      gap: 10,
                      padding: "8px 0",
                      borderTop: i === 0 ? "none" : "1px solid var(--border)",
                      fontSize: 13,
                    }}
                  >
                    <Badge variant="outline">{p.paper}</Badge>
                    <Badge variant="secondary">{p.role}</Badge>
                    <span style={{ color: "var(--text-secondary)" }}>{p.title}</span>
                    {slug && (
                      <Link href={`/papers/${slug}`} style={{ color: "var(--accent-link)", fontFamily: "var(--font-mono-stack)", fontSize: 12 }}>
                        view paper
                      </Link>
                    )}
                  </div>
                );
              })}
            </div>

            <h3 style={{ fontFamily: "var(--font-mono-stack)", fontSize: 14, marginTop: 24 }}>
              External data sources
            </h3>
            <div style={{ display: "grid", gap: 0, marginTop: 4 }}>
              {program.external_data.map((d, i) => (
                <div
                  key={`${d.name}-${i}`}
                  style={{
                    display: "flex",
                    flexWrap: "wrap",
                    alignItems: "baseline",
                    gap: 10,
                    padding: "8px 0",
                    borderTop: i === 0 ? "none" : "1px solid var(--border)",
                    fontSize: 13,
                  }}
                >
                  <span style={{ color: "var(--text-secondary)", maxWidth: "50ch" }}>{d.name}</span>
                  <Badge variant="neutral">{d.kind}</Badge>
                  {d.license && (
                    <span style={{ fontFamily: "var(--font-mono-stack)", fontSize: 11.5, color: "var(--text-tertiary)" }}>
                      {d.license}
                    </span>
                  )}
                  {d.link !== "not-publicly-released" ? (
                    <a
                      href={d.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{ color: "var(--accent-link)", fontFamily: "var(--font-mono-stack)", fontSize: 12 }}
                    >
                      source ↗
                    </a>
                  ) : (
                    <span style={{ fontFamily: "var(--font-mono-stack)", fontSize: 11.5, color: "var(--text-tertiary)" }}>
                      not publicly released
                    </span>
                  )}
                </div>
              ))}
            </div>

            <h3 style={{ fontFamily: "var(--font-mono-stack)", fontSize: 14, marginTop: 24 }}>
              Experiments &mdash; reproduction DAG order
            </h3>
            <div className="table-scroll">
              <table>
                <thead>
                  <tr>
                    <th>Experiment</th>
                    <th>Kind</th>
                    <th>Status</th>
                    <th>Venue</th>
                    <th>Est. wall-clock</th>
                    <th>Est. cost</th>
                    <th>Verification</th>
                  </tr>
                </thead>
                <tbody>
                  {rows.map(({ entry, experiment }) => (
                    <tr key={experiment.id}>
                      <td>
                        <div style={{ fontFamily: "var(--font-mono-stack)", fontSize: 12.5 }}>
                          {experiment.title}
                        </div>
                        <div style={{ fontSize: 11, color: "var(--text-tertiary)", marginTop: 2 }}>
                          {experiment.id}
                          {entry.depends_on.length > 0 && (
                            <> &middot; depends on {entry.depends_on.join(", ")}</>
                          )}
                        </div>
                      </td>
                      <td style={{ fontFamily: "var(--font-mono-stack)", fontSize: 12 }}>
                        {experiment.kind}
                      </td>
                      <td>
                        <Badge variant={STATUS_VARIANT[experiment.status]}>
                          {STATUS_LABEL[experiment.status]}
                        </Badge>
                      </td>
                      <td style={{ fontSize: 12.5 }}>{experiment.reproduction.recommended_venue}</td>
                      <td style={{ fontSize: 12.5 }}>{experiment.reproduction.est_wall_clock}</td>
                      <td style={{ fontFamily: "var(--font-mono-stack)", fontSize: 12.5 }}>
                        {formatCost(experiment.reproduction.est_cost_usd)}
                      </td>
                      <td style={{ fontSize: 12.5, maxWidth: "36ch" }}>{experiment.verification}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        );
      })}
    </>
  );
}
