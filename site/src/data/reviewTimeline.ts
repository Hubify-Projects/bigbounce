export type ReviewRoundKind =
  | "external-browser"
  | "internal-api"
  | "internal-cc"
  | "skill-improvement"
  | "closure-wave";

export type PaperId = "P1A" | "P1B" | "P2" | "P3" | "P4" | "P5";

export interface ReviewRoundLink {
  label: string;
  href: string;
}

export interface GapMetric {
  /** Findings only the external tier caught — the internal/external gap. */
  externalOnlyFindings: number;
  note: string;
}

/**
 * One event on the review-activity timeline. ALL strings are ONE-LINE only —
 * long-form round reports live as markdown files under site/public/reviews/
 * and render at /reviews/<reportSlug>.
 */
export interface ReviewRound {
  id: string;
  kind: ReviewRoundKind;
  dateISO: string;
  title: string;
  papers: PaperId[];
  summary: string;
  keyTakeaways: string[];
  gapMetric?: GapMetric;
  links: ReviewRoundLink[];
  /** Slug of a markdown report at /reviews/<slug> (file: public/reviews/<slug>.md). */
  reportSlug?: string;
}

const GH = "https://github.com/Hubify-Projects/bigbounce/blob/main";
const PR = `${GH}/project-context/peer-reviews`;

/** Authored newest-first; the page re-sorts by dateISO desc (stable on ties). */
export const reviewRounds: ReviewRound[] = [
  {
    id: "EXT3",
    kind: "external-browser",
    dateISO: "2026-06-11",
    title: "EXT3 — third in-thread external round: Grok clean 6/6 ACCEPT, gap 60 → 32 → 27",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Round-3 delta reviews on v1A.0.60-class versions: Grok delivered a clean external round (6/6 ACCEPT), Gemini escalations were artifact-falsified, ChatGPT residuals shrank to wording/policy items — zero substantive physics blockers remain.",
    keyTakeaways: [
      "Grok Heavy: first clean external round of the campaign — ACCEPT on all six papers",
      "Gap metric: 60 (EXT1) → 32 (EXT2) → 27 (EXT3), with EXT3 residues dominated by wording and stale figure assets",
      "ChatGPT 3-round citation dispute VINDICATED on source fetch — promoted to pattern-052 (re-raise vindication test)",
      "Silent Gemini submission failures caught and fixed: growth-based completion waits + version-presence gates now mandatory in the skill",
    ],
    gapMetric: {
      externalOnlyFindings: 27,
      note: "EXT3: ~27 genuinely-new findings, none physics-blocking — exit criterion within one closure wave",
    },
    links: [
      { label: "manifest · GitHub", href: `${PR}/EXT3_BROWSER_MANIFEST.md` },
      { label: "P1A audit", href: `${PR}/EXT3_P1A_TRUTH_AUDIT.md` },
      { label: "P5 audit", href: `${PR}/EXT3_P5_TRUTH_AUDIT.md` },
    ],
  },
  {
    id: "EXT2-CLOSURES",
    kind: "closure-wave",
    dateISO: "2026-06-10",
    title: "EXT2 closure wave — all six papers restamped same-day; pattern-051 closure-wave protocol active",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Same-day EXT2 truth-audit closures restamped all six papers (v1A.0.59 / v1B.0.57 / v1.7.51 / v3.1.90 / v1.0.174 / v0.1.63): confabulated reference replaced, a closure-introduced sign-error chain deleted, sample counts chain-confirmed, and the P2 headline honestly rebooked.",
    keyTakeaways: [
      "P1A Ref [22]: confabulated Mercuri-Capozziello entry (arXiv:0808.0571 is a math.CO paper) replaced with externally-verified Shapiro & Teixeira 2014 (CQG 31, 185002) after surviving ~30 internal rounds + EXT1",
      "P1A: the R29 pair-exchange 'proof' chain — a closure-introduced sign error — deleted at both sites; the Bianchi contraction stands alone",
      "P1A App. C: WKB smallness estimate recomputed — 10^-63 eV corrected to 10^-35 eV, the margin is ~30 orders, not ~60",
      "P1B: 176,240 full-tension sample count chain-confirmed; planck_bao_sn CORRECTED diagnostics added and ΔN_eff/H0 quotes rebooked to the regenerated artifact (+0.058±0.179 / 67.78±1.09)",
      "P2 headline: realistic post-budget range honestly rebooked 3-5σ → 2.6-5σ at every site, with cross-paper sweeps through P1A and P3",
      "pattern-051 closure-wave protocol active: every stamp now ends with a git-diff re-read + swept-term residual grep before commit",
    ],
    links: [
      { label: "P1A audit", href: `${PR}/EXT2_P1A_TRUTH_AUDIT.md` },
      { label: "P1B audit", href: `${PR}/EXT2_P1B_TRUTH_AUDIT.md` },
      { label: "P2 audit", href: `${PR}/EXT2_P2_TRUTH_AUDIT.md` },
      { label: "P3 audit", href: `${PR}/EXT2_P3_TRUTH_AUDIT.md` },
      { label: "P4 audit", href: `${PR}/EXT2_P4_TRUTH_AUDIT.md` },
      { label: "P5 audit", href: `${PR}/EXT2_P5_TRUTH_AUDIT.md` },
    ],
  },
  {
    id: "EXT2",
    kind: "external-browser",
    dateISO: "2026-06-10",
    title: "EXT2 — in-thread delta round: revised PDFs + delta-prompts into the same 18 referee threads; 10 of 18 verdicts improved, first ACCEPTs of the program",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "All six R29 restamps (v1A.0.58 / v1B.0.56 / v1.7.50 / v3.1.89 / v1.0.173 / v0.1.62) posted into the SAME EXT1 chat threads with per-paper delta-prompts; verdict movement 10 improved / 7 held / 1 regressed, with five reviewer legs reaching ACCEPT.",
    keyTakeaways: [
      "First ACCEPT verdicts of the program: Grok P1A/P1B/P4/P5 + Gemini P4 — and ChatGPT moved P1A REJECT → MAJOR ('moved substantially toward publishability')",
      "Gap metric vs the 60-finding EXT1 baseline: 32 genuinely-new substantive findings (P1A 6 · P1B 4 · P2 6 · P3 11 · P4 2 · P5 3) — a 47% one-cycle reduction",
      "Truth-audit headline falsification: Gemini's P5 MAJOR rests entirely on a Table VII row-inversion that is a PDF-extraction artifact — FALSIFIED by the LaTeX source, calibrated verdict ACCEPT",
      "Closure-introduced regressions are the dominant new-finding class (2 of 6 on P1A, 3 of 4 on P1B, 2 of 6 on P2) — promoted into the catalog as pattern-051",
      "The lone regression (Gemini P1B MINOR → MAJOR) was truth-audited rather than auto-accepted, per the standing per-finding audit protocol",
    ],
    gapMetric: {
      externalOnlyFindings: 32,
      note: "EXT1 60 → EXT2 32 genuinely-new substantive findings; counting P4/P5 net-new PARTIAL/OPINION items too the looser total is 47",
    },
    links: [
      { label: "manifest · GitHub", href: `${PR}/EXT2_BROWSER_MANIFEST.md` },
      { label: "P1A audit", href: `${PR}/EXT2_P1A_TRUTH_AUDIT.md` },
      { label: "P1B audit", href: `${PR}/EXT2_P1B_TRUTH_AUDIT.md` },
      { label: "P2 audit", href: `${PR}/EXT2_P2_TRUTH_AUDIT.md` },
      { label: "P3 audit", href: `${PR}/EXT2_P3_TRUTH_AUDIT.md` },
      { label: "P4 audit", href: `${PR}/EXT2_P4_TRUTH_AUDIT.md` },
      { label: "P5 audit", href: `${PR}/EXT2_P5_TRUTH_AUDIT.md` },
    ],
    reportSlug: "ext2-browser-manifest",
  },
  {
    id: "R29",
    kind: "internal-api",
    dateISO: "2026-06-10",
    title: "R29 — post-EXT1 internal round validates the upgraded reviewers: 30 API legs + same-day patch wave across all six papers",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "First internal round after the EXT1 gap-mine upgrades: the rebuilt sweeps caught closure-introduced regressions and a chain-level artifact bug, and every VERIFIED finding was truth-audited and patched same-day with all six papers restamped (v1A.0.58 / v1B.0.56 / v1.7.50 / v3.1.89 / v1.0.173 / v0.1.62).",
    keyTakeaways: [
      "Upgraded sweeps caught closure-introduced regressions: P2 dimensionally inconsistent OOM bounds, P3 half-applied eROSITA de-scope, P1A repro-bundle version desync — all introduced by prior closure waves",
      "P1B export-script off-by-one root-caused from the chains themselves: the frozen parameter_summary.json bug is a uniform column-permutation in the export, not a unit-conversion issue",
      "P4 NSIDE block-scale sensitivity computed (headline exclusion z stable 16.9–19.4 across NSIDE 4/8/16) and the missing non-spiral Fig.1 panel restored",
      "P2 title recast + structured 5-paragraph abstract; headline BF rebooked to ~9–14 under the noise-weighted r≈0.84 bounce-amplitude bookkeeping",
    ],
    gapMetric: {
      externalOnlyFindings: 0,
      note: "internal tier caught everything this round found pre-EXT2 — EXT2 measures the true residual gap",
    },
    links: [
      { label: "P1A audit", href: `${PR}/R29_P1A_TRUTH_AUDIT.md` },
      { label: "P1B audit", href: `${PR}/R29_P1B_TRUTH_AUDIT.md` },
      { label: "P2 audit", href: `${PR}/R29_P2_TRUTH_AUDIT.md` },
      { label: "P3 audit", href: `${PR}/R29_P3_TRUTH_AUDIT.md` },
      { label: "P4 audit", href: `${PR}/R29_P4_TRUTH_AUDIT.md` },
      { label: "P5 audit", href: `${PR}/R29_P5_TRUTH_AUDIT.md` },
    ],
  },
  {
    id: "EXT1-CLOSURES",
    kind: "closure-wave",
    dateISO: "2026-06-10",
    title: "EXT1 closure wave — six parallel agents implement every VERIFIED/PARTIAL finding, hardest first",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Same-day closures across all six papers: convention unification and figure regeneration (P1A), three artifact blockers (P1B), abstract caveats + birefringence rescope (P2), eROSITA de-scope + citation fix (P3), stale-hash blocker (P4), terminology + statistics additions (P5).",
    keyTakeaways: [
      "P1A: ALP sector unified to a single phi-canonical convention across body + App C; washout claim recast as an explicit conditional; 4 stale burned-in figures regenerated",
      "P1B: frozen-artifact unit README + burn-in reconciliation + DES-SN5YR/Pantheon+ overlap disclosure — fixes a referee-downloadable contradiction without rewriting frozen artifacts",
      "P3: eROSITA Table III scores formally de-scoped as non-science data product; Liang2023 corrected to ApJL 956 L6 (ADS-verified); SHA-256 release manifest created",
      "P4: Data Availability commit hash was 5 versions stale — the exact class the new version-bump provenance gate now blocks",
      "HOUSTON-DECISION items preserved untouched and listed per paper in the truth-audit files",
    ],
    links: [
      { label: "P1A audit", href: `${PR}/EXT1_P1A_TRUTH_AUDIT.md` },
      { label: "P1B audit", href: `${PR}/EXT1_P1B_TRUTH_AUDIT.md` },
      { label: "P2 audit", href: `${PR}/EXT1_P2_TRUTH_AUDIT.md` },
      { label: "P3 audit", href: `${PR}/EXT1_P3_TRUTH_AUDIT.md` },
      { label: "P4 audit", href: `${PR}/EXT1_P4_TRUTH_AUDIT.md` },
      { label: "P5 audit", href: `${PR}/EXT1_P5_TRUTH_AUDIT.md` },
    ],
  },
  {
    id: "EXT1-GAPMINE",
    kind: "skill-improvement",
    dateISO: "2026-06-10",
    title: "EXT1 gap-mine — 4 new review patterns, mechanical artifact cross-checker, and 5 reviewer-prompt rules from external-only misses",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Every finding the external tier caught and the internal rounds missed was promoted into the internal review machinery, then each new rule was validated by re-running it on the pre-closure papers to confirm it reproduces the external catch.",
    keyTakeaways: [
      "Patterns 045-048: abstract/body claim drift, artifact/paper cross-check, version-pin staleness on bump, uncomputed quantitative claims",
      "tools/artifact_crosscheck.py: mechanical sweep of every cited artifact path, version label, and commit hash — found 4 unresolved paths beyond what reviewers caught",
      "v3 reviewer prompts gained 5 instruction blocks: abstract-last drift sweep, provenance audit, uncomputed-claim demands, standalone-reader test, effect sizes",
      "Validation protocol: a new rule only counts as an upgrade if it fires on the pre-closure snapshot — one regex failed this test and was fixed because of it",
    ],
    gapMetric: {
      externalOnlyFindings: 60,
      note: "EXT1 baseline: 60 externally-VERIFIED findings survived six clean internal rounds — this number must shrink every cycle",
    },
    links: [
      { label: "pattern catalog", href: `${GH}/project-context/review-patterns` },
      { label: "artifact_crosscheck.py", href: `${GH}/tools/artifact_crosscheck.py` },
    ],
  },
  {
    id: "EXT1-AUDIT",
    kind: "internal-cc",
    dateISO: "2026-06-10",
    title: "EXT1 truth-audit — 18 referee reports, ~175 findings verdicted by six parallel auditors",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Every external finding verified against the repo before any closure: 60 VERIFIED, 53 PARTIAL, 19 FALSIFIED; ChatGPT's P1A REJECT audits down to MAJOR while one of its P5 BLOCKERs was falsified outright.",
    keyTakeaways: [
      "Verdicts: P1A 18 VERIFIED (MAJOR, REJECT over-called) · P1B 11 (3 artifact blockers) · P2 4 (MINOR path) · P3 10 (3 hard fixes) · P4 5 (incl. stale-hash blocker) · P5 12 (4 reviewer claims falsified)",
      "External reviewers over-call severity without repo context — but 60 real findings survived six clean internal rounds, which is the gap this loop exists to close",
      "Headline falsifications: P5 k-unbounded rerun IS in the paper; P1B PR3/PR4 attribution was correct; P3 Planck denominator claims were documented all along",
    ],
    links: [
      { label: "P1A audit", href: `${PR}/EXT1_P1A_TRUTH_AUDIT.md` },
      { label: "P1B audit", href: `${PR}/EXT1_P1B_TRUTH_AUDIT.md` },
      { label: "P2 audit", href: `${PR}/EXT1_P2_TRUTH_AUDIT.md` },
      { label: "P3 audit", href: `${PR}/EXT1_P3_TRUTH_AUDIT.md` },
      { label: "P4 audit", href: `${PR}/EXT1_P4_TRUTH_AUDIT.md` },
      { label: "P5 audit", href: `${PR}/EXT1_P5_TRUTH_AUDIT.md` },
    ],
  },
  {
    id: "EXT1",
    kind: "external-browser",
    dateISO: "2026-06-10",
    title: "EXT1 — first automated browser-tier external round: 6 papers × 3 frontier web apps, 18 submissions",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "All six current PDFs (md5-verified against site mirrors) submitted to ChatGPT Pro Extended, Grok Heavy, and Gemini Thinking via the logged-in browser loop; all 18 reports harvested same-day.",
    keyTakeaways: [
      "18/18 submissions confirmed, with model + effort tier verified in each provider UI before every send",
      "Each chat carries the calibration-armed referee prompt scraped live from this site's per-paper pages",
      "Chat threads are reusable: EXT2 posts revised PDFs + delta-prompts into the SAME threads to keep referee context",
      "Harvest order: Grok + Gemini first, ChatGPT Pro Extended last (30–60+ min per chat), then /peer-review-truth-audit",
    ],
    gapMetric: {
      externalOnlyFindings: 60,
      note: "harvested: verdicts P1A REJECT/MAJOR/MAJOR, P3 MAJOR x3, others MAJOR/MINOR mix — 60 VERIFIED after truth-audit",
    },
    links: [
      { label: "P1A · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96" },
      { label: "P1A · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=5abdb89c-8b7d-4ec0-8839-c39f5a634f03" },
      { label: "P1A · Gemini", href: "https://gemini.google.com/app/4f6bdc99c91dc1d2" },
      { label: "P1B · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded" },
      { label: "P1B · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e" },
      { label: "P1B · Gemini", href: "https://gemini.google.com/app/2ba6d99c84794eb7" },
      { label: "P2 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d" },
      { label: "P2 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=0c4cb7d1-7bc6-4033-a4ac-f4605ec99269" },
      { label: "P2 · Gemini", href: "https://gemini.google.com/app/c01bc000d0305271" },
      { label: "P3 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a" },
      { label: "P3 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54" },
      { label: "P3 · Gemini", href: "https://gemini.google.com/app/b10514f2f6e2ff2f" },
      { label: "P4 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37" },
      { label: "P4 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=411d5219-2864-4196-8d60-da2c97771cc0" },
      { label: "P4 · Gemini", href: "https://gemini.google.com/app/8340abb820aada09" },
      { label: "P5 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064" },
      { label: "P5 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a" },
      { label: "P5 · Gemini", href: "https://gemini.google.com/app/3cbe98b65fe83d40" },
      { label: "manifest · GitHub", href: `${PR}/EXT1_BROWSER_MANIFEST.md` },
    ],
    reportSlug: "ext1-browser-manifest",
  },
  {
    id: "SKILL-EXT-LOOP",
    kind: "skill-improvement",
    dateISO: "2026-06-10",
    title: "Internal-skill upgrade — calibration-armed referee prompts + reusable-thread protocol for external rounds",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Lessons mined from earlier external reviews hardened into the loop: prompts now pre-empt known false-positive classes and external threads persist across rounds.",
    keyTakeaways: [
      "Referee prompts pre-empt 5 known false-positive classes: future-dated arXiv IDs, deliberate correction notes, placeholder companion cites, labeled conservatism, PDF-extraction artifacts",
      "Prompts are generated per-paper on the live site, so external reviewers always receive the current version + focus areas",
      "/external-review-browser-loop automates submission to logged-in provider web apps with model/effort verification before each send",
    ],
    links: [
      { label: "review-patterns catalog", href: `${GH}/project-context/review-patterns` },
      { label: "findings archive", href: `${PR}/findings-archive` },
    ],
  },
  {
    id: "R23-R26-ROLLUP",
    kind: "closure-wave",
    dateISO: "2026-06-10",
    title: "Internal campaign rollup — R23conf → R26conf: ~700 findings truth-audited, 5 pipeline bugs found + fixed",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Four back-to-back full five-vendor confirmation rounds over 2026-06-08..10; every VERIFIED finding closed same-day in bundled hard-fix waves, all version bumps mirrored to this site in the same commit.",
    keyTakeaways: [
      "5 pipeline bugs found + fixed, including the P4 all-CW null-generator selection bug and the P5 ZONEVOID zone-offset join bug",
      "Three of six papers reached the sign-off gate (P4 v1.0.171, P2 v1.7.48, P1B v1B.0.54); the rest carry derivation/recompute residue only",
      "Zero arithmetic errors survived the final wave — every committed number chain-reproduced or corrected in-text",
    ],
    links: [
      { label: "SSOT dashboard", href: `${GH}/project-context/SSOT/index.md` },
      { label: "peer-reviews directory", href: "https://github.com/Hubify-Projects/bigbounce/tree/main/project-context/peer-reviews" },
    ],
  },
  {
    id: "R26conf",
    kind: "internal-api",
    dateISO: "2026-06-10",
    title: "R26conf — five-vendor confirmation round: P1B clean, three of six papers at the sign-off gate",
    papers: ["P1A", "P1B", "P3", "P5"],
    summary: "Zero arithmetic errors across the wave; P1B round clean → sign-off-ready; P1A/P3/P5 carry derivation/recompute residue only and queue for R27conf.",
    keyTakeaways: [
      "P1B v1B.0.54: lone substantive accusation (CPL crossing) falsified by shown arithmetic (z* = +0.39 inside range); every committed number chain-reproduced",
      "P1A v1A.0.56: Cartan factor-2 normalization inconsistency disclosed (single-convention re-derivation queued) + dimensionally inconsistent thermal clause removed",
      "P3 v3.1.87: 12 textual closures — cluster accounting made exact from the dedup artifact; NANOGrav Eq. E1 claim falsified by rederivation",
      "P5 v0.1.60: 9 closures including code-verified tidal-tensor sign documentation",
    ],
    links: [
      { label: "P1B synthesis", href: `${PR}/R26conf_P1B_SYNTHESIS.md` },
      { label: "P1B truth-audit", href: `${PR}/R26conf_P1B_TRUTH_AUDIT.md` },
      { label: "P1A synthesis", href: `${PR}/R26conf_P1A_SYNTHESIS.md` },
      { label: "P3 synthesis", href: `${PR}/R26conf_P3_SYNTHESIS.md` },
    ],
  },
  {
    id: "R25conf",
    kind: "internal-api",
    dateISO: "2026-06-10",
    title: "R25conf — priority round on P2 + P4: both clean, first papers to reach the sign-off gate",
    papers: ["P2", "P4"],
    summary: "P4 completes its 2-of-2 post-retraction clean requirement and P2 comes back clean — both marked READY-FOR-SUBMISSION pending Houston sign-off.",
    keyTakeaways: [
      "P4 v1.0.170: round 2-of-2 clean post-retraction — 93 findings audited; one substantive catch (App A field-convention description) closed same-day, no number changed",
      "P2 v1.7.48: round clean — GR-degradation calibration corrected ~15% → ~23% (c9k-verified); σ_theory continuous-marginalization ranking stable (c9l)",
      "Readiness P4 85 → 95 and P2 92 → 95 under the 99%-cap rule; the final 1% is Houston-only",
    ],
    links: [
      { label: "P4 synthesis", href: `${PR}/R25conf_P4_SYNTHESIS.md` },
      { label: "P4 truth-audit", href: `${PR}/R25conf_P4_TRUTH_AUDIT.md` },
      { label: "P2 synthesis", href: `${PR}/R25conf_P2_SYNTHESIS.md` },
      { label: "P2 truth-audit", href: `${PR}/R25conf_P2_TRUTH_AUDIT.md` },
    ],
  },
  {
    id: "R24conf",
    kind: "internal-api",
    dateISO: "2026-06-10",
    title: "R24conf — full five-vendor confirmation round on all six papers: ~110 verified findings closed",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Confirmation round on the R23conf versions; all six papers bumped with 0-error compiles, every closure mirrored to the site same-commit.",
    keyTakeaways: [
      "P5 v0.1.54: ZONEVOID zone-offset join bug found + fixed — GALZONE void counts corrected, conclusion unchanged, earlier-draft disclosure added in §VIII.D",
      "P2 v1.7.47: two substantive physics fixes — QSFI scaling endpoints corrected per Chen–Wang; −35/16 result re-attributed to Li–Quintin–Wang–Cai at 17 sites",
      "P1B v1B.0.53: S8 marginal corrected 0.831 ± 0.018 → 0.827 ± 0.010, chain-recomputed with an in-text correction note",
      "P4 v1.0.169: 7 local recomputes closed — confidence-cut profile z=+4.27 → +0.41 confirms the low-confidence-tail attribution; formal A_dip 95% UL committed",
    ],
    links: [
      { label: "P4 synthesis", href: `${PR}/R24conf_P4_SYNTHESIS.md` },
      { label: "P2 synthesis", href: `${PR}/R24conf_P2_SYNTHESIS.md` },
      { label: "P5 synthesis", href: `${PR}/R24conf_P5_SYNTHESIS.md` },
    ],
  },
  {
    id: "R23conf",
    kind: "internal-api",
    dateISO: "2026-06-09",
    title: "R23conf — first full-coverage five-vendor confirmation round: ~200 findings truth-audited, all six papers bumped",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "First full-coverage confirmation round on the post-provenance-audit versions — Claude in-session + OpenAI/Gemini/Grok/Perplexity via API + GPT-5-Pro meta; every VERIFIED finding closed same-day.",
    keyTakeaways: [
      "P4 v1.0.168: headline real-space null regenerated from a fixed generator — the committed generator had an all-CW selection bug; verdict unchanged at +0.41σ (p=0.31)",
      "P1B v1B.0.52: §VI ALP provenance rewrite — invented benchmark-config story replaced by the committed chain truth (run1/run2/run3, 9,720 samples)",
      "P2 v1.7.46: irreproducible Table III rebuilt from the committed c9g recompute; Φ/ζ convention mapping proven exactly",
      "P3 v3.1.81: abstract novelty rate arithmetic-anchored 7.9% → 9.4%; gold/silver novelty tiers defined",
    ],
    links: [
      { label: "P4 synthesis", href: `${PR}/R23conf_P4_SYNTHESIS.md` },
      { label: "P1B synthesis", href: `${PR}/R23conf_P1B_SYNTHESIS.md` },
      { label: "P1A truth-audit", href: `${PR}/R23conf_P1A_TRUTH_AUDIT.md` },
    ],
  },
];

/* ── Structured progress dataset (powers the /reviews Progress visualizations) ──
 * Sources (do NOT invent numbers — pattern-036):
 * EXT1/EXT2 verdicts: project-context/peer-reviews/EXT{1,2}_BROWSER_MANIFEST.md harvest tables.
 * Gap series: GAP METRIC sections of EXT2_P*_TRUTH_AUDIT.md + the 60-finding EXT1 baseline.
 * Readiness: SSOT/index.md R25conf/EXT1/R29 truth-audit checkpoints (95-cap rule in force).
 * Skills: project-context/review-patterns/ catalog + EXT1/EXT2 gap-mine commits.
 */

export type Verdict = "REJECT" | "MAJOR" | "MINOR" | "ACCEPT";

export type ReviewerId = "ChatGPT" | "Grok" | "Gemini";

export const REVIEWERS: ReviewerId[] = ["ChatGPT", "Grok", "Gemini"];

export const PAPER_IDS: PaperId[] = ["P1A", "P1B", "P2", "P3", "P4", "P5"];

export interface ExternalRoundVerdicts {
  roundId: string;
  dateISO: string;
  /** Verdicts in REVIEWERS order: [ChatGPT, Grok, Gemini]. */
  verdicts: Record<PaperId, [Verdict, Verdict, Verdict]>;
  note: string;
}

/** Per-paper external referee verdicts per browser-tier round (oldest → newest). */
export const externalVerdictRounds: ExternalRoundVerdicts[] = [
  {
    roundId: "EXT1",
    dateISO: "2026-06-10",
    verdicts: {
      P1A: ["REJECT", "MAJOR", "MAJOR"],
      P1B: ["MAJOR", "MINOR", "MINOR"],
      P2: ["MAJOR", "MINOR", "MINOR"],
      P3: ["MAJOR", "MAJOR", "MAJOR"],
      P4: ["MAJOR", "MINOR", "MINOR"],
      P5: ["MAJOR", "MINOR", "MAJOR"],
    },
    note: "First automated browser-tier round: ChatGPT Pro Extended · Grok Heavy · Gemini Thinking, 18 submissions",
  },
  {
    roundId: "EXT2",
    dateISO: "2026-06-10",
    verdicts: {
      P1A: ["MAJOR", "ACCEPT", "MINOR"],
      P1B: ["MAJOR", "ACCEPT", "MAJOR"],
      P2: ["MAJOR", "MINOR", "MINOR"],
      P3: ["MAJOR", "MINOR", "MINOR"],
      P4: ["MAJOR", "ACCEPT", "ACCEPT"],
      P5: ["MAJOR", "ACCEPT", "MAJOR"],
    },
    note: "Same 18 threads, delta-prompts: 10 improved / 7 held / 1 regressed; Gemini P5 MAJOR audits to ACCEPT (PDF-extraction artifact), Gemini P1B regression truth-audited",
  },
];

export interface GapPoint {
  roundId: string;
  dateISO: string;
  /** Externally-caught substantive findings that survived all internal rounds. */
  total: number;
  perPaper: Record<PaperId, number>;
  note: string;
}

/** Internal/external gap series — must shrink every cycle; target is zero. */
export const gapSeries: GapPoint[] = [
  {
    roundId: "EXT3",
    dateISO: "2026-06-11",
    total: 27,
    perPaper: { P1A: 3, P1B: 3, P2: 5, P3: 5, P4: 6, P5: 6 },
    note: "EXT3 truth-audits: ~27 genuinely-new, all wording/asset/policy class — zero substantive physics blockers",
  },
  {
    roundId: "EXT1",
    dateISO: "2026-06-10",
    total: 60,
    perPaper: { P1A: 18, P1B: 11, P2: 4, P3: 10, P4: 5, P5: 12 },
    note: "60 externally-VERIFIED findings survived six clean internal rounds (EXT1 truth-audit baseline)",
  },
  {
    roundId: "EXT2",
    dateISO: "2026-06-10",
    total: 32,
    perPaper: { P1A: 6, P1B: 4, P2: 6, P3: 11, P4: 2, P5: 3 },
    note: "Genuinely-new substantive findings per EXT2 truth-audit GAP METRIC sections; P4/P5 net-new incl. PARTIAL/OPINION is 10 each (looser total 47)",
  },
];

export interface ReadinessCheckpoint {
  id: string;
  dateISO: string;
  /** Sparse — only papers whose readiness was explicitly stated at that checkpoint. */
  values: Partial<Record<PaperId, number>>;
  note: string;
}

/** Readiness percent checkpoints from SSOT (95-cap until clean external round + Houston sign-off). */
export const readinessCheckpoints: ReadinessCheckpoint[] = [
  {
    id: "pre-R25conf",
    dateISO: "2026-06-10",
    values: { P2: 92, P4: 85 },
    note: "Documented pre-R25conf positions (P4 post-retraction rebuild, P2 pre-clean-round)",
  },
  {
    id: "R25conf",
    dateISO: "2026-06-10",
    values: { P2: 95, P4: 95 },
    note: "Both clean — first papers to reach the sign-off gate under the 99%-cap rule",
  },
  {
    id: "EXT1-AUDIT",
    dateISO: "2026-06-10",
    values: { P1A: 93, P1B: 94, P2: 95, P3: 94, P4: 95, P5: 95 },
    note: "P1A rolled BACK to 93 after 18 externally-VERIFIED findings — readiness oscillates backward by design",
  },
  {
    id: "R29",
    dateISO: "2026-06-10",
    values: { P1A: 94, P1B: 94, P2: 94, P3: 94, P4: 95, P5: 95 },
    note: "P1A 93→94, P2 95→94 (dimensional regressions found+fixed) — per R29 truth-audit",
  },
  {
    id: "EXT2-CLOSURES",
    dateISO: "2026-06-10",
    values: { P1A: 95, P1B: 94, P2: 94, P3: 95, P4: 95, P5: 95 },
    note: "Current: EXT2 cycle complete — P1A 94→95 (hardest blockers closed), P3 94→95; P1B/P2 held at 94 pending compute-queue closures; EXT3 pending",
  },
];

export interface SkillsPoint {
  id: string;
  dateISO: string;
  /** Review-pattern catalog size (project-context/review-patterns/). */
  patterns: number;
  /** v3 native-PDF reviewer-prompt instruction rules. */
  promptRules: number;
  note: string;
}

/** Skills-stack growth — the internal review machinery self-improving each round. */
export const skillsSeries: SkillsPoint[] = [
  { id: "retro", dateISO: "2026-06-02", patterns: 34, promptRules: 14, note: "2026-06-02 retro baseline: 34 codified patterns" },
  { id: "R23conf-mine", dateISO: "2026-06-09", patterns: 44, promptRules: 14, note: "R23conf pattern-mine: catalog at 44 (incl. draft patterns 040-044)" },
  { id: "EXT1-gapmine", dateISO: "2026-06-10", patterns: 48, promptRules: 19, note: "EXT1 gap-mine: patterns 045-048 + artifact_crosscheck.py + reviewer-prompt rules 15-19" },
  { id: "EXT2-gapmine", dateISO: "2026-06-10", patterns: 49, promptRules: 19, note: "EXT2 gap-mine: pattern-051 closure-introduced regression (5-point closure-wave protocol)" },
];

export function getReviewRoundByReportSlug(slug: string): ReviewRound | undefined {
  return reviewRounds.find((r) => r.reportSlug === slug);
}

/** Newest-first ordering for the feed (stable on date ties, preserving authored order). */
export function sortedReviewRounds(): ReviewRound[] {
  return [...reviewRounds].sort((a, b) => b.dateISO.localeCompare(a.dateISO));
}
