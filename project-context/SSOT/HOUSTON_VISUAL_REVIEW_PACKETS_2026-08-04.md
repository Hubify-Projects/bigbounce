# Houston visual-review and decision packets

**Canonical selected-manuscript review packet · 2026-08-04**

This is the shortest honest route from the current 95-point agent gates to
Houston's final editorial decision. Review the five standalone manuscripts in
the order below. Current P3 is reviewed separately as supporting data; it is
not the anomaly-discovery paper and is not a sixth approval target.

## How the decision works

- `APPROVE` means this exact manuscript may move from **95 to 100** and enter
  its post-approval publishing steps.
- `REVISE` means state the reader-visible change needed; the changed PDF must
  be rebuilt, visually audited, re-hashed, and shown again.
- `DEFER` means preserve the candidate without submitting it now.
- There is **no 96 state**. Package acceptance is evidence within the existing
  95-point gate, not another score.
- Approval is manuscript-specific. It does not claim journal acceptance,
  arXiv endorsement, outreach, or publication.

## Evidence boundary

The current six source/PDF pairs pass the deterministic portfolio preflight:
[`portfolio-preflight-2026-08-03.json`](final-acceptance/portfolio-preflight-2026-08-03.json),
generated `2026-08-04T08:04:33Z` at manuscript-bearing head `8055a5b1`,
verdict `PASS`, receipt SHA-256
`3b7cbb31663202c7483cbd51639ccbf200b5e0465335e7f14b27b47463d5fcd5`.
The receipt covers exact source/PDF hashes, generic rules, artifact contracts,
claim dependencies, mirrors, packages, and PDF checks. A 2026-08-04 Git diff
from that head to this packet found **zero changes across the 12 canonical
manuscript source/PDF paths**. Later commits were documentation/site state, not
manuscript changes.

The final-hash reviews are bounded residual checks, not independent human peer
review and not three-provider consensus. Provider failures and page limits are
stated per manuscript below.

## Review order at a glance

| Order | Work | Why it exists | Decision |
|---:|---|---|---|
| 1 | P2 | Primary exact matter-contraction non-Gaussianity result | Houston approval |
| 2 | P1A | Narrow ECH boundary/convention Note | Houston approval |
| 3 | P4 | Primary chirality catalog and observed-label dipole null | Houston approval |
| 4 | P1B | Reusable NaMaster/provenance verification software | Houston approval |
| 5 | P5 | Distinct chirality-versus-environment companion test | Houston approval |
| — | P3 support | Public-ID/provenance repair used by the anomaly rebuild | Integration feedback only |

## 1. P2 — Exact matter-contraction amplitude

**Reader-first decision surface:**
[open the live P2 final-review page](https://bigbounce.hubify.app/final-review).
It binds the exact PDF, five page-level reading checks, package evidence, and
the one-line decision response in one place.

**Why it exists.** It answers the clearest original bounce-cosmology question:
what local non-Gaussian amplitude follows from the stated matter-dominated
contracting background and cubic action?

**Notable contribution.** It rederives the complete four-vertex result
`f_NL^local = -35/16`, gives the ordered polynomial coefficients and independent
cross-checks, and explains why the printed `-35/8` value is not reproduced.
The survey mapping is useful orientation but subordinate to the derivation.

**It does not claim.** A measured detection, a complete nonsingular-bounce
model, unconditional cubic transmission through every bounce, or a new joint
SPHEREx forecast.

**Exact candidate.** v1.7.130 · 12 pages · PDF SHA-256
`d3afe79fe70ce13cee5ec8149e84c4b42c78224ca6a90569058ec501222f5c2f`.

- [Open local PDF](../../research/focused_paper_source_integration/02_full_draft.pdf)
- [Open production PDF](https://bigbounce.hubify.app/papers/02_full_draft_v1.7.130.pdf)
- [Open PRD submission kit](PRD_SUBMISSION_KIT_P2_2026-07-24.md)
- [Open final-hash truth audit](../peer-reviews/FINALHASH_2026-08-03_P2_v1.7.130_P2_TRUTH_AUDIT.md)

**Bounded review result.** Zero genuinely-new-real defects; no reopening. Grok
completed. Gemini was unavailable after receipt/model failure and Perplexity
had insufficient quota, so this is one usable provider leg, not consensus.

**After approval.** Confirm APS account/ORCID/data-availability selections,
final portal metadata, and upload the exact PRD package. The existing Zenodo
record is behind the current patch and must be represented honestly.

`P2 APPROVE | REVISE | DEFER — feedback:`

## 2. P1A — Minimal ECH boundary Note

**Why it exists.** A broader torsion/dark-energy program narrowed under review
to the defensible result: eliminate the non-propagating Cartan connection under
minimal assumptions and state exactly what remains on the spin-sourced and
zero-spin scalar branches.

**Notable contribution.** It consolidates the convention-sensitive axial
contact coefficient, a sharply bounded scale benchmark, the declared
mean-field sign result, and the classical scalar/tensor transparency statement
in one auditable Note.

**It does not claim.** A new dark-energy model, a universal torsion-cosmology
no-go theorem, a birefringence prediction, or an empirical discovery.

**Exact candidate.** v1A.0.127 · 8 pages · PDF SHA-256
`210be8f0b285034d88b9854c532eaac4a32147cea2621dedbaaac94540bbc7f0`.

- [Open local PDF](../../arxiv/paper1a_ech_nogo.pdf)
- [Open production PDF](https://bigbounce.hubify.app/papers/paper1a_ech_nogo_v1A.0.127.pdf)
- [Open CQG submission kit](CQG_SUBMISSION_KIT_P1A_2026-07-24.md)
- [Open final-hash truth audit](../peer-reviews/ROUND_2026-08-03-P1A-v1A.0.127-FINALHASH/TRUTH_AUDIT.md)

**Bounded review result.** Zero genuinely-new-real defects; no reopening.
Grok completed. Gemini routing/model fallback and Perplexity quota failed, so
this is one usable provider leg, not consensus.

**After approval.** Confirm ScholarOne account fields and final referee
choices, then upload the exact CQG Note package. The published Zenodo record is
already cited by the manuscript.

`P1A APPROVE | REVISE | DEFER — feedback:`

## 3. P4 — Chirality catalog and observed-label dipole null

**Why it exists.** It tests a disputed large-scale galaxy-chirality claim on a
much larger DESI imaging catalog while exposing classifier, selection, and
transfer limitations rather than hiding them.

**Notable contribution.** It releases 8,474,531 observed labels, defines a
quality-controlled 890,069-object high-confidence sample, and reports a primary
dipole statistic consistent with zero. It also isolates an upstream label
asymmetry and unreproduced training-composition behavior.

**It does not claim.** A physical primordial-parity bound. That inference
remains gated on morphology transfer and unresolved systematics.

**Exact candidate.** v1.0.274 · 32 pages · PDF SHA-256
`2641a228af1e3decf17d18341570c4e779483a823267421fe041aade1375e0d7`.

- [Open local PDF](../../pipelines/p2_chirality/chirality_catalog_paper.pdf)
- [Open production PDF](https://bigbounce.hubify.app/papers/chirality_catalog_paper_v1.0.274.pdf)
- [Open ApJS portal kit](../../pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md)
- [Open final-hash truth audit](../peer-reviews/FINALHASH_2026-08-03_P4_v1.0.273/TRUTH_AUDIT.md)

**Bounded review result.** v1.0.273 PDF SHA-256
`88bb513284db6adf4c6cf22ee7e08be2787cf8c3ebf43ffdcc289f2d369cee05`
received a complete 32-page native Gemini review and a Grok review limited to
pages 1–25. The only genuinely new
item was editorial: expand `ECE` at first use. Commit `1b75dea1` closed exactly
that item in v1.0.274; the diff changed the version marker and expansion only,
with no scientific claim, number, or caveat change. No substantive reopening.
This is still not a complete multi-provider/two-pass consensus.

**After approval.** Refresh the existing Zenodo record to v1.0.274, verify the
restaged bytes, then complete the ApJS portal choices and upload. Do not publish
the archive update before approval.

`P4 APPROVE | REVISE | DEFER — feedback:`

## 4. P1B — `namaster-proof` software

**Why it exists.** The reusable part of a broader companion analysis became a
small tool that prevents two concrete failures: approximating the full
pseudo-`C_ell` window operator and losing the binding between results and their
execution evidence.

**Notable contribution.** A focused Python verification library for exact
NaMaster bandpower-window inference, rotation recovery, deterministic support
contracts, and tamper-evident content-bound receipts.

**It does not claim.** A sky analysis, foreground model, cosmological
measurement, or second bounce-physics result.

**Exact candidate.** v2B.0.16 · 6 pages · PDF SHA-256
`2fb957101604066382ddb604da41b9fe3bc2a48ae4a799ca25c2b34eaac6267a`.

- [Open local PDF](../../arxiv/paper1b_namaster_proof.pdf)
- [Open production PDF](https://bigbounce.hubify.app/papers/paper1b_namaster_proof_v2B.0.16.pdf)
- [Open JORS submission kit](JORS_SUBMISSION_KIT_P1B_2026-07-24.md)
- [Open final-hash truth audit](../peer-reviews/ROUND_2026-08-03-P1B-v2B.0.16-FINALHASH/TRUTH_AUDIT.md)

**Bounded review result.** Zero genuinely-new-real defects; no reopening.
Gemini returned the native-PDF review plus a no-new second pass. Grok and
Perplexity were blocked by the then-stale packet receipt, so this is one usable
provider leg, not consensus.

**After approval.** Supply three real reviewer names/emails, make the APC or
waiver choice, confirm JORS portal metadata, and upload the exact package. The
paper and software Zenodo DOIs are live.

`P1B APPROVE | REVISE | DEFER — feedback:`

## 5. P5 — Chirality–environment companion

**Why it exists.** After P4 created the observed-label catalog, this paper asks
a distinct question: do those labels differ between released DESIVAST void and
non-void environments?

**Notable contribution.** It performs a covariate-standardized,
cluster-robust catalog-native comparison with a declared focal contrast and
multiple sensitivity paths; the focal result is consistent with zero.

**It does not claim.** Independence from P4, preregistration, physical
handedness, a real-space result, or a cosmological constraint. It is explicitly
exploratory and post-hoc.

**Exact candidate.** v0.1.147-2026-08-03 · 46 pages · PDF SHA-256
`3c1c484118d21ecab9a26655135df9d982c27d375095c2693b4376a86317b18e`.

- [Open local PDF](../../pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf)
- [Open production PDF](https://bigbounce.hubify.app/papers/p5_desi_chirality_v0.1.147-2026-08-03.pdf)
- [Open AJ portal kit](../../pipelines/p5_desi_chirality/paper/AJ_PORTAL_KIT_v0.1.147-2026-08-03.md)
- [Open final-hash truth audit](../peer-reviews/FINALHASH_2026-08-03_P5_v0.1.147/TRUTH_AUDIT.md)

**Bounded review result.** Zero genuinely-new-real defects in the completed
Grok report; no reopening. The only completed provider leg saw rasterized pages
1–25 of 46. Full-document Gemini retries timed out and produced no report;
Perplexity failed. This is the weakest final-hash coverage in the selected set
and must not be described as full-document or multi-provider consensus.

**After approval.** Create and verify the immutable v0.1.147 Git tag and Zenodo
snapshot, replace the explicit availability placeholders, rebuild, visually
audit, re-hash, and show the exact back-patched PDF before AJ upload.

`P5 APPROVE | REVISE | DEFER — feedback:`

## P3 support release — integration feedback only

**Why it exists.** The historical anomaly list used mixed internal identifiers.
P3 repairs that provenance problem so a subset can be joined back to public
DESI spectra.

**Contribution.** Memory-bounded join/checkpoint machinery and 181 warning-free
TARGETID associations: 170 high-coordinate-consistency core and 11
lower-confidence positional associations.

**Boundary.** It does not run or validate the anomaly detector, establish
novelty or purity, estimate anomaly rates, or replace the original discovery
survey. It is integrated evidence for the clean anomaly rebuild, not a
standalone ApJS submission.

- [Open local PDF](../../pipelines/p3_anomaly_engine/paper3_apjs.pdf)
- [Open production PDF](https://bigbounce.hubify.app/papers/paper3_apjs_v3.2.0-r17.pdf)
- [Open technical package receipt](../../pipelines/p3_anomaly_engine/FINAL_PACKAGE_RECEIPT_v3.2.0-r17_2026-08-03.md)

`P3 SUPPORT RELEASE ACCEPT | REVISE | DEFER — feedback:`

## One-copy response block

```text
P2  APPROVE | REVISE | DEFER — feedback:
P1A APPROVE | REVISE | DEFER — feedback:
P4  APPROVE | REVISE | DEFER — feedback:
P1B APPROVE | REVISE | DEFER — feedback:
P5  APPROVE | REVISE | DEFER — feedback:
P3 SUPPORT RELEASE ACCEPT | REVISE | DEFER — feedback:
```

After an approval is recorded, the canonical board owns the 100-point state
and the journal/archive/endorsement tracker owns execution. No external action
is marked complete without a portal, message, DOI, or submission receipt.
