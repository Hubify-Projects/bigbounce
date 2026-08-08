# Decisions

## 2026-08-03 — Publication architecture reset

- The six-paper count is an operational history, not a scientific requirement.
- The active public map is three programs: bounce theory, survey discovery,
  and galaxy chirality.
- P2, a rebuilt anomaly-science paper, and P4 are the three core scientific
  stories; P1A and P1B are specialist theory/software publications.
- Current P3 is a technical public-ID recovery output, not a replacement for
  the original anomaly survey. It is an integrated supporting data/provenance
  release, not a standalone ApJS paper.
- P5 remains a standalone AJ companion because its environment question,
  DESI/LSS joins, and systematics-controlled null are distinct from P4.
- Houston approved executing the three-program architecture on 2026-08-04.
- Approved endpoint: six standalone works (including the rebuilt anomaly
  flagship and P5, excluding P3) plus the integrated P3 supporting release.
- Governing document:
  `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`.

## 2026-08-04 — Bounded final-hash acceptance and decision packets

- Bounded final-hash evidence is accepted as adequate for Houston's visual
  review; provider limitations remain explicit and do not justify a `96`
  readiness state.
- Each standalone work remains at 95 until Houston's explicit decision:
  `APPROVE` moves that work from 95 to 100; no agent may infer approval.
- P3 is reviewed only as the integrated supporting release, not as a
  standalone anomaly-science paper or an independent 95→100 decision target.
- Decision packet reference:
  `project-context/SSOT/HOUSTON_VISUAL_REVIEW_PACKETS_2026-08-04.md`.

## 2026-08-04 — Master publication and release map

- The durable strategy is three scientific programs, six eventual standalone
  works, and one integrated P3 supporting release—not a fixed six-paper quota.
- A lead paper ships with the data, code, model, schema, validation, archive,
  and provenance needed to reproduce it; those components are not spun into
  derivative papers unless they independently answer a new scientific question.
- The rebuilt anomaly flagship depends on the selected clean DESI rerun. P3 is
  its supporting public-ID/provenance release; P4's catalog/classifier is the
  upstream dependency of P5.
- Governing plain-English map:
  `project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md`.

## 2026-08-03 — Canonical program map

- `ops/PLAN.md` is the single executable plan.
- `project-context/paper_registry.json` owns paper identities and paths.
- `project-context/SSOT/index.md` owns current portfolio status; per-paper
  details live in `project-context/SSOT/paper-*/status.md`.
- Directive P governs readiness: four agent gates total 95; only Houston's
  explicit per-paper sign-off reaches 100.
- Automated convergence is zero genuinely-new-real findings outstanding across
  active legs. Literal verdict words are diagnostic.
- Publishing workflow and independent human review are tracked separately and
  do not reduce readiness.
- Final PDFs receive one bounded final-hash confirmation because they contain
  post-board closures; this is not a new open-ended review campaign.
- You.md context points to canonical sources and does not duplicate detailed
  SSOT or review evidence.
