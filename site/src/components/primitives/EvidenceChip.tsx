import { cn } from "@/lib/utils";

export type EvidenceGrade = "measured" | "derived" | "null" | "open";

const GRADE_LABEL: Record<EvidenceGrade, string> = {
  measured: "measured",
  derived: "derived",
  null: "null",
  open: "open",
};

export interface EvidenceChipProps {
  grade: EvidenceGrade;
  label?: string;
  className?: string;
}

/**
 * Evidence-grade primitive (REDESIGN_SPEC.md §1 commitment 1, §4.2, §5.1 #4).
 * A 6px square dot + label text, never a filled/bordered pill. `null` is a
 * contribution, rendered in calm slate — never red.
 */
export function EvidenceChip({ grade, label, className }: EvidenceChipProps) {
  return (
    <span className={cn("evidence-chip", `evidence-chip-${grade}`, className)}>
      <span className="evidence-chip-dot" aria-hidden="true" />
      {label ?? GRADE_LABEL[grade]}
    </span>
  );
}
