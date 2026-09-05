// Shared contribution-type vocabulary — labels the KIND of contribution a
// work makes, shown as a small chip next to its novelty tier (N1/N2/N3)
// wherever the tier appears. Distinct from novelty tier: type says what
// the work IS, tier says how novel it is. Never used to imply a tier value.
export type ContributionType =
  | "measurement"
  | "derivation"
  | "null-result"
  | "method-tool"
  | "data-release"
  | "reproduction"
  | "catalogue";

export const CONTRIBUTION_TYPE_LABEL: Record<ContributionType, string> = {
  measurement: "Measurement",
  derivation: "Derivation",
  "null-result": "Null result",
  "method-tool": "Method / tool",
  "data-release": "Data release",
  reproduction: "Reproduction",
  catalogue: "Catalogue",
};

export const CONTRIBUTION_TYPE_HINT: Record<ContributionType, string> = {
  measurement: "A physical quantity measured from data.",
  derivation: "A result obtained analytically or by direct computation.",
  "null-result": "A tested prediction that did not clear its bar — reported as a null.",
  "method-tool": "Reusable verification software, pipeline, or method.",
  "data-release": "A public dataset released with provenance for independent use.",
  reproduction: "An existing result or pipeline reproduced end to end.",
  catalogue: "A curated, cross-matched list of candidates or objects.",
};
