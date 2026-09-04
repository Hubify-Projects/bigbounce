import type { Metadata } from "next";
import { predictions, type Prediction } from "@/data/predictions";
import { MathText } from "@/components/MathText";
import { Band, PageHeader, StatRow, RowList, EvidenceChip, type EvidenceGrade } from "@/components/primitives";

export const metadata: Metadata = {
  title: "Predictions",
  description: "Testable observational channels for bounce cosmology — each with its current constraint and evidence grade.",
};

function predictionGrade(pred: Prediction): EvidenceGrade {
  if (pred.statusVariant === "purple") return "derived";
  if (pred.statusVariant === "green") return "measured";
  if (pred.statusVariant === "red") return "null";
  return "open";
}

const flagship = predictions.find((p) => p.statusVariant === "purple");

export default function PredictionsIndexPage() {
  return (
    <>
      <Band width="content">
        <PageHeader
          eyebrow="Predictions"
          title="Predictions"
          lead="Every distinct observational channel for testing bounce cosmology against inflation — its current constraint, its evidence grade, and what would decide it."
        />
      </Band>
      <Band width="content">
        <StatRow
          items={[
            { value: <MathText>{flagship?.value ?? "f_NL"}</MathText>, label: "flagship signal" },
            { value: predictions.length, label: "channels" },
            { value: "SPHEREx", label: "next decisive test", mono: false },
          ]}
        />
      </Band>
      <Band width="content">
        <RowList
          items={predictions.map((pred) => ({
            title: <MathText>{pred.name}</MathText>,
            purpose: pred.description.slice(0, 160) + (pred.description.length > 160 ? "…" : ""),
            href: `/predictions/${pred.slug}`,
            right: <MathText>{pred.value}</MathText>,
            chips: <EvidenceChip grade={predictionGrade(pred)} />,
          }))}
        />
      </Band>
    </>
  );
}
