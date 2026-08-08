import { predictions } from"@/data/predictions";
import { Badge } from"@/components/ui/badge";
import { Button } from"@/components/ui/button";
import { MathText } from"@/components/MathText";
import { Separator } from"@/components/ui/separator";

// Shorten verbose badge labels: clip at first parenthesis
function displayStatus(status: string): string {
  return status.split("(")[0].trim();
}
import Link from"next/link";
import type { Metadata } from"next";

export const metadata: Metadata = {
  title:"Predictions",
  description:"Testable predictions from the bounce cosmology portfolio.",
};

const statusVariantMap: Record<
  string,
"default" |"secondary" |"destructive" |"outline"
> = {
  green:"default",
  blue:"secondary",
  amber:"outline",
  red:"destructive",
  purple:"secondary",
};

const flagship = predictions.find((prediction) => prediction.statusVariant === "purple");
const liveChannels = predictions.filter((prediction) =>
  prediction.experiment.includes("NOW") || prediction.currentConstraint.length > 0,
).length;

export default function PredictionsIndexPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Bounce Cosmology Portfolio &middot; {predictions.length} Channels
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Predictions
        </h1>
        <p className="subtitle">
          Each prediction is a distinct observational channel for testing bounce
          cosmology against inflation. Click any to see connected surveys, papers,
          and next steps.
        </p>
        <div className="insight-strip">
          <div className="insight">
            <div className="insight-label">Flagship signal</div>
            <div className="insight-value">
              <MathText>{flagship?.value ?? "f_NL"}</MathText>
            </div>
          </div>
          <div className="insight">
            <div className="insight-label">Channels</div>
            <div className="insight-value">{predictions.length}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Live constraints</div>
            <div className="insight-value">{liveChannels}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Next decisive test</div>
            <div className="insight-value">SPHEREx</div>
          </div>
        </div>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>Observational Channels</h2>
        <div className="flat-item-list">
          {predictions.map((pred) => (
            <div key={pred.slug} className="py-5">
              <div className="flex items-start justify-between gap-3 mb-3">
                <div className="flex-1">
                  <div className="card-kicker">{pred.experiment}</div>
                  <div
                    className="mt-1 text-base font-semibold"
                    style={{ fontFamily: "var(--font-mono-stack)" }}
                  >
                    <MathText>{pred.name}</MathText>
                  </div>
                </div>
                <Badge variant={statusVariantMap[pred.statusVariant]}>
                  {displayStatus(pred.status)}
                </Badge>
              </div>
              <div
                className="big-value mb-3"
                style={{ borderTop: "1px solid var(--border-subtle)", paddingTop: 12 }}
              >
                <MathText>{pred.value}</MathText>
              </div>
              <p className="text-sm text-muted-foreground mb-3">
                <MathText>{pred.description.slice(0, 220)}</MathText>
                {pred.description.length > 220 ? "…" : ""}
              </p>
              <div className="flex items-center justify-between flex-wrap gap-2">
                <div className="chip-row text-xs">
                  <Badge variant="outline">{pred.bestModel}</Badge>
                  <Badge variant="outline">
                    {pred.nextSteps.length} next steps
                  </Badge>
                </div>
                <Button asChild size="sm" variant="outline">
                  <Link href={`/predictions/${pred.slug}`}>
                    Open prediction &rarr;
                  </Link>
                </Button>
              </div>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
