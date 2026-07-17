# INT v3 Referee Report — Paper P3 (Independent Claude-stack leg)

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-16 PT
- **Paper:** P3 v3.2.0-r8 — "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations"
- **pdf_sha256:** b5f254f92b10bda43b687f07c5f58b828a6f7dc70d98c08f9e9b609edbba08b0
- **Venue:** The Astrophysical Journal Supplement Series (ApJS)
- **Referee profile:** APJS-CATALOG
- **PARSED VERDICT:** MINOR REVISIONS

---

## Referee prompt (as issued)

> You are an expert referee for The Astrophysical Journal Supplement Series. Review this Catalog article manuscript under profile APJS-CATALOG to the standard of a real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim supported?

---

## Verbatim referee report

**(1) VERDICT: MINOR REVISIONS**

This is an unusually scrupulous, well-documented catalog-integrity / public-ID-recovery
paper. The declared deliverable — recover public DESI DR1 `TARGETID`s for a frozen
historical anomaly list, with an exactly reproducible build, checksum-bound provenance,
and an independent field-by-field validator — is delivered and internally consistent.
The paper is exemplary in *not* overclaiming: it repeatedly and correctly states the
release is a reproducible follow-up list, not validated detections and not an unbiased
sample for anomaly-rate inference. The audit matrix (Table 8) reports PASS on every
declared contract check, the selection waterfall (Table 4 / Fig. 2) reconciles
(20,299,155 -> 2,468 -> 2,448 -> 181), the two quality tiers (170 core + 11 tail = 181)
are consistent across the abstract, Tables 2, 4, 5, and the appendix, and the data-
availability section pins immutable Hugging Face commit hashes plus explicit build/validate
commands.

I verified the one apparent internal tension I found — Table 2 lists P3-DESI-000017 at
0.130508" (the 0.1–1" tail) while Table 5 lists P3-DESI-000007 at 0.002" — and confirmed
these are two distinct candidate IDs, not a contradiction; Table 5's tail rows (000003 ->
0.274", 000005 -> 0.991", 000039 -> 0.221") reproduce Table 2 exactly. No catalog-integrity
error was found on this axis.

The verdict is MINOR REVISIONS rather than ACCEPT because the paper's enduring-value/venue
case needs to be argued more forcefully (Issue 1), and a set of presentation, justification,
and editorial items should be addressed. None of these require new observations, new
computation, or reanalysis — the audit artifacts already exist — which is why the overall
verdict is MINOR rather than MAJOR revisions.

**(2) ISSUES:**

**[MAJOR] 1 — Enduring value / venue-fit (Abstract; §1; §5.2 "Recommended uses"; §8).**
The catalog's *selection quantity* — the historical anomaly score `S` from the 496->128
five-seed-mean-MSE BigAE stream — is explicitly non-reproducible from public spectra
(§2.1: "the released per-object `S` values cannot be numerically reproduced ... no physical
feature or detection efficiency is assigned to them"), and the primary anomaly product it
recovers (ref. [5]) is an unrefereed, self-authored Hugging Face dataset, not a peer-reviewed
catalog. The manuscript should therefore make the *standalone* ApJS value proposition
explicit and unmissable: what a reader gains from these 181 objects that they could not get
by drawing their own outlier sample from public DESI DR1. As written, §5.2 lists *uses* but
does not establish *priority value* for the specific 181-row list, whose defining axis is
irreproducible. The honest and defensible answer already latent in the paper — that the
enduring contribution is (a) the reusable memory-bounded, checkpointed 28.4M-row join +
provenance/validation *machinery* and (b) a fully public-key, checksum-audited follow-up set
that rejoins to public spectra by `TARGETID` — should be stated up front as the deliverable,
with the object list framed as an instance of that machinery. Recommend a short explicit
paragraph (Abstract + §1 + §5.2) foregrounding the reproducibility/provenance framework as
the primary contribution. This is the single item most likely to determine an editor's
accept decision; it is an argument-strengthening revision, not a science redo.

**[MINOR] 2 — "Association evidence" wording risks over-reading a near-tautological
self-match (§3.5; §4.1; Fig. 1).** Because the historical cluster coordinates were copied
directly from DESI FIBERMAP `TARGET_RA`/`TARGET_DEC` (§2.1), the sub-0.1" positional match
is, for DESI-only single-member clusters, essentially a coordinate self-join by construction,
not independent astrophysical association. The local-shift control (2,456 observed vs 0.75
shifted at 0.1") therefore largely measures that identical coordinates match themselves. The
paper does disclose this ("uses coordinates as a source"; "aggregate association, not
individual identity"), but the phrase "strong association evidence" for the sub-0.1" core
still invites over-reading. Recommend one explicit sentence stating that the sub-0.1" core is
a coordinate self-recovery by construction (cluster means offset from single members only via
multi-member averaging), so the shift-control excess there is expected and is not evidence of
an astrophysical clustering signal.

**[MINOR] 3 — Post-hoc 0.1" tier boundary lacks a principled basis (§3.4; §4; Abstract).**
The 170/11 split at 0.1" is honestly disclosed as introduced *after* inspecting the quality
reproduction and "not a pre-declared selection cut." Good — but no rationale is given for
0.1" specifically (vs. 0.05" or 0.2"). Because the "170 high-coordinate-consistency core"
headline number rides on this boundary, provide the physical/operational motivation (e.g.,
DESI fiber-positioning / coordinate-precision scale, or the observed separation-distribution
knee visible in Fig. 2b) so the tier is not perceived as tuned.

**[MINOR] 4 — Irreproducible score / unrefereed input — surface the caveat earlier (§2.1;
§7 "First"; ref. [5]).** The non-reproducibility of `S` and the reliance on an unrefereed HF
dataset are the most consequential scope limits and are currently reached only midway through
§2.1 and in §7. Given ApJS catalog readers, elevate a one-line statement of this to the
abstract/intro so the scope is set before the reader invests in the machinery.

**[MINOR] 5 — Internal release-candidate version tags clutter the manuscript (throughout;
Abstract; §6.4; §6.6).** The narrative threads r2 (primary), r5 (warned auxiliary), r7
(submission bundle), and r8 (this manuscript) — e.g., "the v3.2.0-r2 data release audited in
this v3.2.0-r8 manuscript." This internal build/QA versioning leaking into the published text
is genuinely confusing to an external reader. Recommend collapsing to a single published
version identifier plus one provenance note, and moving the r-tag lineage to a provenance
appendix or the release manifest.

**[MINOR] 6 — Machine-readable table and AAS DOI (§4.4; §6.5; Table 5 note; §Software/AAS).**
Only a 12-row illustrative excerpt (Table 5) appears in the manuscript; the full 181-row,
43-column product (`tab3.tsv`) is deferred to an AAS machine-readable digital asset with a
DOI listed as "pending." For refereeing, the complete MRT must accompany the submission so the
referee can inspect the full catalog contract, and the DOI must resolve before publication.
Confirm the MRT is available to the referee at review time.

**[MINOR] 7 — Interpretation of observed < random in the 0.1–1" annulus (§4.1; Abstract).**
The result "shifted 0.1–1" annulus contains 75.6 ± 13.0 vs. 11 observed" means the observed
tail count is *below* the random expectation — a coherent and honest outcome (real associations
concentrate at <0.1", depleting the annulus), but a mildly counterintuitive statement as
phrased. Add one sentence making explicit that observed *below* shifted-random in the annulus
reinforces that the 11-row tail carries no secure positional identity.

**[MINOR] 8 — Minor presentation items.** (a) Table 5 renders two negative small redshifts as
"−0.000" (P3-DESI-000018, 000163); show enough precision to distinguish them from zero or add a
footnote. (b) The BigAE "496-to-128" architecture and "five-seed mean reconstruction MSE" are
referenced without enough description for a reader to understand the score's provenance; add a
one-line architecture/provenance note or a pointer. (c) "BigAE autoencoder" is redundant (AE =
autoencoder).

**(3) One sentence — is the central claim supported?** Yes: the central claim — an exactly
reproducible public-`TARGETID` recovery of a frozen historical anomaly list, released as an
auditable follow-up catalog and explicitly *not* as validated detections or an unbiased
anomaly-rate sample — is well supported by the checksum-bound provenance, the reconciled
selection waterfall, the independent field-by-field validator, and the all-PASS integrity
matrix (Table 8).

---

## Summary counts

- MAJOR: 1
- MINOR: 7
- Parsed verdict: MINOR REVISIONS
