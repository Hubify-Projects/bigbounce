import Link from "next/link";
import { surveys, type Survey } from "@/data/surveys";
import { DataTable } from "@/components/primitives";

/**
 * Canonical survey QC table — single source of truth is data/surveys.ts.
 * Rendered on the homepage and /status so the two pages can never disagree
 * about a survey's QC verdict (previously /status hardcoded NEOWISE/Planck
 * as FAIL while surveys.ts said PASS).
 *
 * Uses the shared DataTable primitive (the one sanctioned bordered surface)
 * with a tonal dot+label QC mark instead of a nested Card > Table > Badge
 * stack — the prior shadcn Card/Badge combo double- and triple-bordered
 * every row (BRAND_QA_2026-09-08.md: "Retire on sight: ui/card.tsx ...
 * any nested bordered panel").
 */
const QC_TONE: Record<Survey["qcStatus"], { color: string; label: string }> = {
  pass: { color: "var(--success)", label: "PASS" },
  caution: { color: "var(--warn)", label: "CAUTION" },
  fail: { color: "var(--crit)", label: "FAIL" },
  "needs-expansion": { color: "var(--text-tertiary)", label: "EXPAND" },
};

export function SurveyQcTable() {
  return (
    <DataTable
      rows={surveys}
      rowKey={(s) => s.slug}
      columns={[
        {
          key: "survey",
          header: "Survey",
          render: (s) => (
            <Link href={`/surveys/${s.slug}`} style={{ fontWeight: 600 }}>
              {s.name}
            </Link>
          ),
        },
        { key: "sources", header: "Sources", render: (s) => s.sources },
        {
          key: "anomalies",
          header: "Anomalies",
          mono: true,
          render: (s) => `${s.anomalies.toLocaleString()} (${s.anomalyRate})`,
        },
        {
          key: "qc",
          header: "QC",
          render: (s) => {
            const tone = QC_TONE[s.qcStatus];
            return (
              <span
                className="mono"
                title={s.qcNote}
                style={{ display: "inline-flex", alignItems: "center", gap: 6, fontSize: 12.5 }}
              >
                <span
                  aria-hidden="true"
                  style={{
                    width: 6,
                    height: 6,
                    borderRadius: 2,
                    background: tone.color,
                    display: "inline-block",
                  }}
                />
                <span style={{ color: tone.color }}>{tone.label}</span>
              </span>
            );
          },
        },
      ]}
    />
  );
}
