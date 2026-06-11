import { surveys } from "@/data/surveys";
import { Badge } from "@/components/ui/badge";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Card, CardContent } from "@/components/ui/card";
import Link from "next/link";

/**
 * Canonical survey QC table — single source of truth is data/surveys.ts.
 * Rendered on the homepage and /status so the two pages can never disagree
 * about a survey's QC verdict (previously /status hardcoded NEOWISE/Planck
 * as FAIL while surveys.ts said PASS).
 */
const surveyQcVariant: Record<
  "pass" | "caution" | "fail" | "needs-expansion",
  { variant: "default" | "secondary" | "destructive" | "outline"; label: string }
> = {
  pass: { variant: "default", label: "PASS" },
  caution: { variant: "outline", label: "CAUTION" },
  fail: { variant: "destructive", label: "FAIL" },
  "needs-expansion": { variant: "outline", label: "EXPAND" },
};

export function SurveyQcTable() {
  return (
    <Card>
      <CardContent className="p-0">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Survey</TableHead>
              <TableHead>Sources</TableHead>
              <TableHead>Anomalies</TableHead>
              <TableHead>QC</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {surveys.map((survey) => {
              const qc = surveyQcVariant[survey.qcStatus];
              return (
                <TableRow key={survey.slug}>
                  <TableCell>
                    <Link
                      href={`/surveys/${survey.slug}`}
                      className="font-semibold underline-offset-4 hover:underline"
                    >
                      {survey.name}
                    </Link>
                  </TableCell>
                  <TableCell className="text-muted-foreground">
                    {survey.sources}
                  </TableCell>
                  <TableCell className="font-mono text-muted-foreground">
                    {survey.anomalies.toLocaleString()} ({survey.anomalyRate})
                  </TableCell>
                  <TableCell>
                    <Badge variant={qc.variant} title={survey.qcNote}>
                      {qc.label}
                    </Badge>
                  </TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  );
}
