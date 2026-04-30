import { predictions } from "@/data/predictions";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Predictions",
  description: "Testable predictions from the bounce cosmology portfolio.",
};

const statusVariantMap: Record<
  string,
  "default" | "secondary" | "destructive" | "outline"
> = {
  green: "default",
  blue: "secondary",
  amber: "outline",
  red: "destructive",
  purple: "secondary",
};

export default function PredictionsIndexPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Bounce Cosmology Portfolio &middot; {predictions.length} Channels
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          Predictions
        </h1>
        <p className="subtitle">
          Each prediction is a distinct observational channel for testing bounce
          cosmology against inflation. Click any to see connected surveys, papers,
          and next steps.
        </p>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>Observational Channels</h2>
        <div className="grid gap-4 md:grid-cols-2">
          {predictions.map((pred) => (
            <Card key={pred.slug} className="flex flex-col">
              <CardHeader className="pb-3">
                <div className="flex items-start justify-between gap-3">
                  <CardTitle
                    className="text-base"
                    style={{ fontFamily: "var(--font-serif)" }}
                  >
                    {pred.name}
                  </CardTitle>
                  <Badge variant={statusVariantMap[pred.statusVariant]}>
                    {pred.status}
                  </Badge>
                </div>
                <CardDescription className="font-mono text-lg font-bold text-foreground">
                  {pred.value}
                </CardDescription>
              </CardHeader>
              <CardContent className="flex-1">
                <p className="text-sm text-muted-foreground">
                  {pred.description.slice(0, 220)}
                  {pred.description.length > 220 ? "…" : ""}
                </p>
                <div className="mt-3 flex flex-wrap gap-2 text-xs">
                  <Badge variant="outline">{pred.bestModel}</Badge>
                  <Badge variant="outline">{pred.experiment}</Badge>
                  <Badge variant="outline">
                    {pred.nextSteps.length} next steps
                  </Badge>
                </div>
              </CardContent>
              <CardFooter className="pt-0">
                <Button asChild size="sm" variant="outline">
                  <Link href={`/predictions/${pred.slug}`}>
                    Open prediction &rarr;
                  </Link>
                </Button>
              </CardFooter>
            </Card>
          ))}
        </div>
      </section>
    </>
  );
}
