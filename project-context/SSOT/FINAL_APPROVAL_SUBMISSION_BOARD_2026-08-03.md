# Selected-portfolio approval, endorsement, and submission board

**Canonical execution board · reconciled 2026-08-04 · private project operations**

> **REGENERATED 2026-08-04 AFTER ARCHITECTURE APPROVAL.** Current P3 is an
> integrated supporting data/provenance release, not a standalone ApJS paper.
> P5 remains a standalone AJ companion. The rebuilt DESI anomaly flagship is a
> new primary-science workstream and does not yet have an approvable PDF.

This is the one-screen bridge from preserved candidate packages to the selected
portfolio. It does not replace `ops/PLAN.md` for program policy or the per-paper
SSOT files for scientific limitations.

## Stage and score

- The five preserved standalone submissions remain **95/100** under Directive
  P: P1A, P1B, P2, P4, and P5. Houston's explicit per-paper sign-off is the
  final 5. Current P3 retains a 95-point technical-package record but is no
  longer scored as an independent submission.
- Do **not** invent 96. Exact-package acceptance is evidence inside the existing
  95-point packaging gate, not a new scoring category.
- Current stage: bounded current-hash acceptance complete; Houston visual
  review is the active gate. Use the concise
  [`HOUSTON_VISUAL_REVIEW_PACKETS_2026-08-04.md`](HOUSTON_VISUAL_REVIEW_PACKETS_2026-08-04.md)
  in the recommended order P2 → P1A → P4 → P1B → P5.
- P3 r17 is **Supporting Data Release · DESI Public-ID Recovery** and will be
  integrated into the rebuilt anomaly flagship release.
- P5 is **Standalone Companion · Chirality–Environment Null Test**.
- Submission, endorsement, journal review, and publication are tracked below but
  remain separate from readiness.

## Houston visual-review map

| Paper | Exact candidate | Local PDF | Live PDF | Portal kit | Houston decision |
|---|---|---|---|---|---|
| P1A | v1A.0.127 · 8 pp · SHA-256 `210be8f0…bc7f0` | [`paper1a_ech_nogo.pdf`](../../arxiv/paper1a_ech_nogo.pdf) | [Production](https://bigbounce.hubify.app/papers/paper1a_ech_nogo_v1A.0.127.pdf) | [`CQG`](CQG_SUBMISSION_KIT_P1A_2026-07-24.md) | PENDING |
| P1B | v2B.0.16 · 6 pp · SHA-256 `2fb95710…6267a` | [`paper1b_namaster_proof.pdf`](../../arxiv/paper1b_namaster_proof.pdf) | [Production](https://bigbounce.hubify.app/papers/paper1b_namaster_proof_v2B.0.16.pdf) | [`JORS`](JORS_SUBMISSION_KIT_P1B_2026-07-24.md) | PENDING |
| P2 | v1.7.130 · 12 pp · SHA-256 `d3afe79f…5c2f` | [`02_full_draft.pdf`](../../research/focused_paper_source_integration/02_full_draft.pdf) | [Production](https://bigbounce.hubify.app/papers/02_full_draft_v1.7.130.pdf) | [`PRD`](PRD_SUBMISSION_KIT_P2_2026-07-24.md) | PENDING |
| P3 support | v3.2.0-r17 · 17 pp · SHA-256 `9a376926…b779a0b` | [`paper3_apjs.pdf`](../../pipelines/p3_anomaly_engine/paper3_apjs.pdf) | [Production](https://bigbounce.hubify.app/papers/paper3_apjs_v3.2.0-r17.pdf) | [`Receipt`](../../pipelines/p3_anomaly_engine/FINAL_PACKAGE_RECEIPT_v3.2.0-r17_2026-08-03.md) | INTEGRATE; NO STANDALONE SUBMISSION |
| P4 | v1.0.274 · 32 pp · SHA-256 `2641a228…75e0d7` | [`chirality_catalog_paper.pdf`](../../pipelines/p2_chirality/chirality_catalog_paper.pdf) | [Production](https://bigbounce.hubify.app/papers/chirality_catalog_paper_v1.0.274.pdf) | [`ApJS`](../../pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md) | PENDING |
| P5 | v0.1.147-2026-08-03 · 46 pp · SHA-256 `3c1c4841…7b18e` | [`p5_desi_chirality.pdf`](../../pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf) | [Production](https://bigbounce.hubify.app/papers/p5_desi_chirality_v0.1.147-2026-08-03.pdf) | [`AJ`](../../pipelines/p5_desi_chirality/paper/AJ_PORTAL_KIT_v0.1.147-2026-08-03.md) | PENDING |

Houston can reply with one line per paper:

```text
P1A APPROVE | FEEDBACK: ...
P1B APPROVE | FEEDBACK: ...
P2  APPROVE | FEEDBACK: ...
P3 SUPPORT RELEASE FEEDBACK: ...
P4  APPROVE | FEEDBACK: ...
P5  APPROVE | FEEDBACK: ...
```

Only an `APPROVE` decision moves that paper from 95 to 100.

## Exact source packages

| Paper | Package | SHA-256 | Independent package state |
|---|---|---|---|
| P1A | `arxiv/paper1a_arxiv_v1A.0.127.tar.gz` | `35bd4234…958` | PASS · 8 pp · all-page visual audit |
| P1B | `project-context/SSOT/arxiv_tarballs/paper1b_namaster_proof_arxiv_v2B.0.16.tar.gz` | `4fa8cc9a…dddf` | PASS · 6 pp; JORS bundle also rebuilt |
| P2 | `research/focused_paper_source_integration/paper2_arxiv_v1.7.130.tar.gz` | `74124142…a69` | PASS · missing bibliography defect closed |
| P3 | `pipelines/p3_anomaly_engine/paper3_apjs_arxiv_v3.2.0-r17.tar.gz` | `47fac374…1843` | PASS · technical data-note package · 17-page visual audit |
| P4 | `pipelines/p2_chirality/paper4_arxiv_v1.0.274.tar.gz` | `9503ddd1…be736` | PASS · flat AASTeX 7.0.2 package · 32-page visual audit |
| P5 | `pipelines/p5_desi_chirality/paper/paper5_aj_v0.1.147-2026-08-03.tar.gz` | `a6a444f0…0b69` | PASS · flat AASTeX 7.0.2 AJ/arXiv package · 46-page visual audit |

The current content-addressed receipt under `final-acceptance/` is a `PASS`
generated `2026-08-04T08:04:33Z` at manuscript-bearing head `8055a5b1`; receipt
SHA-256 is `3b7cbb31…5fcd5`. A fresh diff from that head found zero changes to
the six canonical source/PDF pairs, so it binds the exact candidates above even
though later documentation commits advance repository HEAD. Final-hash coverage
is not uniform: P1A/P1B/P2 each have one usable provider leg, P4 has a complete
32-page Gemini leg plus partial Grok coverage and its sole ECE copy-edit closed
in v1.0.274, and P5 has only a Grok leg over pages 1–25 of 46. These limits are
carried paper by paper in the visual-review packet; no multi-provider consensus
is claimed.

## Journal execution tracker

| Paper | Venue | Technical packet | Remaining author/portal action | Submit state |
|---|---|---|---|---|
| P2 | PRD | READY | Sign-off; APS account/ORCID/DAS and final portal choices | NOT STARTED |
| P1A | CQG Note | READY | Sign-off; ScholarOne account and final referee choices | NOT STARTED |
| P3 support | Integrated with anomaly flagship | PACKAGE PRESERVED | Bind release/DOI and provenance into rebuilt flagship | NO STANDALONE SUBMISSION |
| P4 | ApJS | READY | Sign-off; live portal choices; refresh current Zenodo version | NOT STARTED |
| P1B | JORS | READY | Sign-off; three real reviewer names/emails and APC/waiver choice | NOT STARTED |
| P5 | AJ | READY FOR APPROVAL | Sign-off, then immutable tag/Zenodo mint, identifier back-patch, final rebuild, and portal choices | NOT STARTED |

Recommended journal order after approvals: **P2 → P1A → P4 → P1B → P5**,
then the rebuilt anomaly flagship when its evidence and manuscript are ready.
Current P3 ships as supporting release infrastructure, not as a journal slot.

## arXiv endorsement tracker

The official code pages require Houston's logged-in session today, so the named
candidate eligibility table from 2026-07-22 is a dated research snapshot, not
current proof. No repository or prompt evidence shows that any request was sent.

| Code | Category / papers | Plan | Draft | Sent | Reply | Endorsed |
|---|---|---|---|---|---|---|
| `HYEJ7S` | gr-qc · P1A | Reverify a personally known qualified endorser in Houston's signed-in arXiv session | READY | NO | NONE | NO |
| `L8TIPN` | astro-ph.IM · P1B (and future anomaly flagship if venue-compatible) | Same | READY | NO | NONE | NO |
| `LRZHC4` | astro-ph.CO · P2 | Same | READY | NO | NONE | NO |
| `CLVMAQ` | astro-ph.GA · P4/P5 | Same | READY | NO | NONE | NO |

Drafts: [`ENDORSEMENT_REQUEST_DRAFTS_2026-07-24.md`](ENDORSEMENT_REQUEST_DRAFTS_2026-07-24.md).
Policy: [arXiv endorsement help](https://info.arxiv.org/help/endorsement.html).
Record `Sent`, `Reply`, or `Endorsed` only from an actual message/portal receipt.
Journal submission does not wait on arXiv endorsement.

## Archive and identifier state

| Paper | Durable public record | Final-candidate alignment |
|---|---|---|
| P1A | Zenodo `10.5281/zenodo.21481838` | Published; current manuscript cites it |
| P1B | Zenodo `10.5281/zenodo.21481842`; software `10.5281/zenodo.21481753` | Published; current manuscript cites both |
| P2 | Zenodo `10.5281/zenodo.21461881` | Published record is behind current patch; manuscript states the relationship |
| P3 support | Zenodo `10.5281/zenodo.21461888` | Bind the current release lineage into the rebuilt anomaly flagship; do not mint a standalone-paper route |
| P4 | Zenodo `10.5281/zenodo.21461899` | Refresh to v1.0.274 only after architecture approval and sign-off |
| P5 | No published Paper V DOI | Mint immutable tag/Zenodo snapshot only after sign-off and explicit publish authorization |

## Stop rules

- No 96 or 100 without a real scoring gate or Houston's explicit sign-off.
- No outreach/endorsement/submission status without a receipt.
- No standalone P3 submission; it is an integrated supporting release.
- No P4/P5 irreversible archive publication before Houston approves the paper.
- Any post-sign-off identifier back-patch must be rebuilt, visually audited,
  re-hashed, mirrored, and shown to Houston as the exact submission artifact.
