import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { predictions, getPredictionBySlug, type Prediction } from "@/data/predictions";
import { MathText } from "@/components/MathText";
import { Band, PageHeader, EvidenceChip, type EvidenceGrade } from "@/components/primitives";

export function generateStaticParams() {
  return predictions.map((p) => ({ slug: p.slug }));
}

type PageParams = Promise<{ slug: string }>;

export async function generateMetadata({ params }: { params: PageParams }): Promise<Metadata> {
  const { slug } = await params;
  const pred = getPredictionBySlug(slug);
  if (!pred) return { title: "Not found" };
  return { title: pred.name, description: `${pred.name}: ${pred.value}. ${pred.status}.` };
}

function predictionGrade(pred: Prediction): EvidenceGrade {
  if (pred.statusVariant === "purple") return "derived";
  if (pred.statusVariant === "green") return "measured";
  if (pred.statusVariant === "red") return "null";
  return "open";
}

export default async function PredictionPage({ params }: { params: PageParams }) {
  const { slug } = await params;
  const pred = getPredictionBySlug(slug);
  if (!pred) notFound();

  return (
    <>
      <Band width="prose">
        <p className="row-purpose" style={{ marginBottom: 4 }}>
          <Link href="/predictions">Predictions</Link> &rarr; <MathText>{pred.name}</MathText>
        </p>
        <PageHeader
          eyebrow="Prediction"
          title={<MathText>{pred.name}</MathText>}
          lead={<MathText>{pred.description}</MathText>}
          meta={[
            { label: "value", value: <MathText>{pred.value}</MathText>, mono: true },
            { label: "model", value: pred.bestModel },
            { label: "experiment", value: pred.experiment },
          ]}
        />
        <EvidenceChip grade={predictionGrade(pred)} label={pred.status} />
      </Band>

      <Band width="prose">
        <h2 className="section-h2">Current constraint</h2>
        <p className="prose-body"><MathText>{pred.currentConstraint}</MathText></p>
      </Band>

      <Band width="prose">
        <h2 className="section-h2">Key results</h2>
        <ul className="result-summary-list">
          {pred.keyResults.map((r, i) => (
            <li key={i}><span><MathText>{r}</MathText></span></li>
          ))}
        </ul>
      </Band>

      {(pred.surveys.length > 0 || pred.papers.length > 0) && (
        <Band width="prose">
          <h2 className="section-h2">Connected work</h2>
          {pred.surveys.length > 0 && (
            <p className="prose-body" style={{ marginBottom: 8 }}>
              <strong>Surveys:</strong> {pred.surveys.join(" · ")}
            </p>
          )}
          {pred.papers.length > 0 && (
            <p className="prose-body"><strong>Papers:</strong> {pred.papers.join(" · ")}</p>
          )}
        </Band>
      )}

      <Band width="prose">
        <h2 className="section-h2">Timeline</h2>
        <p className="prose-body"><MathText>{pred.timeline}</MathText></p>
      </Band>

      <Band width="prose">
        <h2 className="section-h2">Next steps</h2>
        <ul className="result-summary-list">
          {pred.nextSteps.map((step, i) => (
            <li key={i}><EvidenceChip grade="open" /><span><MathText>{step}</MathText></span></li>
          ))}
        </ul>
      </Band>
    </>
  );
}
