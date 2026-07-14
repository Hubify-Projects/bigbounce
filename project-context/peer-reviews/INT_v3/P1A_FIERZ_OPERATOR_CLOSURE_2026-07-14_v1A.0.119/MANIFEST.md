# P1A Fierz operator closure manifest

## Purpose

This bundle closes the exact Fierz convention and row/column defect found by
the v1A.0.118 confirmation panel and independently audited afterward.

## Canonical files

| Artifact | SHA-256 |
|---|---|
| `arxiv/paper1a_ech_nogo.tex` | `a7a74e2d2e9b9cb3a5e159ce071c3258782473e2b7f64ce1e931babb7a6b6d87` |
| `arxiv/paper1a_ech_nogo.pdf` | `dfe2a47a3221888477dfa47adb9cddf7ebbe25acc96185c3af9e58a1e7c065d0` |
| `arxiv/scripts/fierz_lemma_check.py` | `a989ccef618dad3843c96b67fb81b718525f2c6f31efac31c8b2bc8df799cdca` |
| `arxiv/scripts/njl_gap_equation_route1.py` | `7a78c01de3c1cc1591ca2d047f2f4645fb619141af23764efb1d9654fd3834ac` |
| `arxiv/scripts/njl_gap_equation_route1_results.json` | `74e189a4d9fd4debbc0fc6de14556dd3e63e78fa4286eeff0392ce521ed5f5aa` |

The proof copies are byte-identical to these canonical files.  `SHA256SUMS.txt`
covers every proof, audit, log, and render artifact in this directory.

## Validation commands

```text
python3 arxiv/scripts/fierz_lemma_check.py
python3 arxiv/scripts/njl_gap_equation_route1.py
tectonic -b /tmp/tectonic-p1a-bundle -o <out> -k --keep-logs -r 2 paper1a_ech_nogo.tex
shasum -a 256 -c SHA256SUMS.txt
```

The scripts are deterministic: repeated executions produce byte-identical
stdout and JSON.

## Superseded evidence

- `P1A_EXACT_CONVENTION_CLOSURE_2026-07-14_v1A.0.117` is retained as frozen
  historical evidence but its `-3*kappa/64` Fierz coefficient is superseded.
- `P1A_CLAIM_BOUNDARY_CLOSURE_2026-07-14_v1A.0.118` is retained for its claim
  surgery, but its inherited Fierz coefficient is superseded.
- `ROUND_2026-07-14-P1A-v1A.0.118-EXACTPDF-9a5d9216-NONANTHROPIC-CONFIRM`
  remains the raw review-of-record.  Its new independent-audit addendum records
  the c-number/Grassmann axial-sign nuance verbatim.

## Honest status

This is a computation-and-edit closure, not a fresh multi-model acceptance
round.  The next publication gate is a blinded exact-PDF confirmation against
the frozen v1A.0.119 PDF hash.  No readiness score or publication status is
advanced here.
