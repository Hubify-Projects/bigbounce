# Deposit readiness — BigBounce six-paper portfolio

## 2026-07-21 update (current state — supersedes the 2026-07-15 table below)

**Published DOIs (2026-07-20, irreversible, receipts in this directory):**
P2 → 10.5281/zenodo.21461881 · P3 → 10.5281/zenodo.21461888 · P4 → 10.5281/zenodo.21461899.
All three DOIs are embedded in the current manuscripts.

**Still fail-closed (correctly) on Houston's D2 license decision:** P1A (license
is the ONLY gate), P1B (license + namaster-proof software DOI), P5 (license +
Paper-IV arXiv-ID back-patch). Verified 2026-07-21: `prepare_paper_deposit.py`
refuses all three with the exact blocker text — the gates are current.

**namaster-proof 0.1.7 software archive (P1B prerequisite): PUBLISHED
2026-07-21** on Houston's explicit go ("publish the namaster-proof draft do it
yes") — **DOI 10.5281/zenodo.21481753**, record live (HTTP 200), all 5 file
MD5s verified ([receipt](namaster-proof_v0.1.7_zenodo_receipt_2026-07-21.json)).

**D2 RESOLVED 2026-07-21:** Houston chose **CC-BY-4.0** ("D2 i go with your
recommendation"). Applied via `d2_authorize_deposits.py --write` with the
software DOI; P1A and P1B fully unblocked, staged at HEAD (isolated recompiles
pass, 0 undef-refs), and uploaded as Zenodo **drafts** with prereserved DOIs:
P1A → 10.5281/zenodo.21481838
([receipt](P1A_zenodo_draft_receipt_2026-07-21.json)), P1B →
10.5281/zenodo.21481842
([receipt](P1B_zenodo_draft_receipt_2026-07-21.json)). Publishing these two is
one explicit Houston go. P5 keeps only the Paper-IV back-patch gate.

**D2 runbook (the moment Houston names the license, e.g. cc-by-4.0):**

```bash
# 1. authorize (records Houston's decision + provenance stamp)
python3 tools/d2_authorize_deposits.py cc-by-4.0 \
  --authorized-by "Houston, YYYY-MM-DD, chat" --write
# 2. stage each unblocked paper at HEAD
python3 tools/prepare_paper_deposit.py --paper P1A --git-commit $(git rev-parse HEAD) --verify-tarball --write
# 3. draft + upload + verify (reversible; add --publish --confirm PUBLISH only on Houston's go)
python3 tools/zenodo_deposit.py --staging-dir .deposit-staging/P1A/<version> \
  --paper P1A --receipt-out project-context/SSOT/zenodo/P1A_zenodo_receipt_<date>.json
# P1B: publish the namaster-proof draft first, then re-run step 1 with --p1b-software-doi <doi>
```

---

**Audited:** 2026-07-15. All six papers remain **IN REVISION**. This directory previously claimed that obsolete June versions were “one-click ready”; that claim was false for the current manuscripts and is withdrawn.

| Paper | Current version | Readiness | Current PDF | Deposit state |
|---|---:|---:|---|---|
| P1A | v1A.0.123 | 62 | 7 pp; SHA-256 `4c450a67…3f71` | Exact source bundle and standalone proof pass; metadata intentionally fails closed until Houston authorizes a license; no draft or DOI |
| P1B | v1B.0.112 | 56 | 20 pp; SHA-256 `d420a7f5…31c` | v1B.0.111 exact-board provenance/estimator/prior defects are closed with regression gates; confirmation, human review, and archive/DOI package remain open |
| P2 | v1.7.122 | 80 | 10 pp; SHA-256 `4097bac5…25c9` | **Verified exact-commit candidate in reversible GitHub draft; all 8 remote digests match; no DOI or archive publication** |
| P3 | v3.2.0-r8 | 56 | 16 pp; MD5 `8faac098b5f4cde3133937460b8df4c5` | **Verified exact-commit candidate in reversible GitHub draft; all 8 remote digests match; no DOI or archive publication** |
| P4 | v1.0.255 | 80 | 29 pp; SHA-256 `f9b011a8…7dce` | Exact commit-bound source bundle and isolated 29-page proof pass; the reversible GitHub draft is still the superseded v1.0.252 candidate; no DOI reserved or archive published |
| P5 | v0.1.134-2026-07-15 | 74 | 39 pp; SHA-256 `c2ecb845…afc6` | Exact commit-bound source bundle and isolated 39-page proof pass; deposit metadata intentionally fails closed pending license authorization and Paper-IV gates; no public tag/DOI |

## P2 evidence

- Exact package target: `4599a4056fdd6e588c07c6c45ff0dc546bbb2cc7`.
- Draft-release receipt: [`../github-releases/P2_v1.7.122_draft_release_receipt.json`](../github-releases/P2_v1.7.122_draft_release_receipt.json).
- Deposit specification: [`P2_zenodo_deposition.md`](P2_zenodo_deposition.md).
- Standalone proof: [`../arxiv_tarballs/paper2_arxiv_v1.7.122.proof.json`](../arxiv_tarballs/paper2_arxiv_v1.7.122.proof.json).

## P4 evidence

- Current bundle source/config target: `678e93febd505d37768e554f337bdbd4f838a514`.
- Current standalone source proof: [`../arxiv_tarballs/paper4_arxiv_v1.0.260.proof.json`](../arxiv_tarballs/paper4_arxiv_v1.0.260.proof.json).
- Historical reversible draft receipt (v1.0.252 only): [`../github-releases/P4_v1.0.252_draft_release_receipt.json`](../github-releases/P4_v1.0.252_draft_release_receipt.json).
- Deposit specification and supersession note: [`P4_zenodo_deposition.md`](P4_zenodo_deposition.md).

## P5 evidence

- Current bundle source/config target: `678e93febd505d37768e554f337bdbd4f838a514`.
- Current standalone source proof: [`../arxiv_tarballs/paper5_arxiv_v0.1.134-2026-07-15.proof.json`](../arxiv_tarballs/paper5_arxiv_v0.1.134-2026-07-15.proof.json).
- The old P5 deposition note is explicitly superseded and is not authorized metadata: [`P5_zenodo_deposition.md`](P5_zenodo_deposition.md).

## P1A and P3 evidence

- P1A exact bundle/proof: [`../arxiv_tarballs/paper1a_arxiv_v1A.0.123.proof.json`](../arxiv_tarballs/paper1a_arxiv_v1A.0.123.proof.json). Its previous unsupported CC BY assertion is withdrawn; the package fails closed on license authorization.
- P3 draft receipt: [`../github-releases/P3_v3.2.0-r8_draft_release_receipt.json`](../github-releases/P3_v3.2.0-r8_draft_release_receipt.json).
- P3 deposit specification: [`P3_zenodo_deposition.md`](P3_zenodo_deposition.md).
- P3 standalone proof: [`../arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r8.proof.json`](../arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r8.proof.json).

## Accelerated, fail-closed workflow

`tools/prepare_paper_deposit.py` now binds a package to a full Git commit and manuscript version; requires byte-identical tracked TeX, PDF, source bundle, proof, and provenance inputs; validates the PDF and standalone compile; generates a deterministic provenance archive, manifest, checksums, and placeholder-free Zenodo metadata; writes only to ignored staging unless `--write` is explicit; and never mutates GitHub, Zenodo, arXiv, or journal state.

P2 and P3 exercise this workflow end to end through reversible drafts. P4 and
P5 now have current deterministic bundles and isolated proofs, but P4's existing
draft is superseded and P5 metadata intentionally fails closed. P1A also stops
before metadata/draft creation because its license is unresolved. Final Zenodo
publication remains confirmation-gated because it is immutable.
