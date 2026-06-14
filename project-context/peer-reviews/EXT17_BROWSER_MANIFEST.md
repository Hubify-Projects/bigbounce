# EXT17 Browser Manifest — 2026-06-13

**EXT17 launched: 18 chats submitted** — ChatGPT (6 in-thread delta) + Grok (6 in-thread delta) + Gemini (6 fresh chats, pattern-058 MNRAS referee-format first-line). P1B+P4 courtesy re-confirmation prompts. Status: IN FLIGHT. Harvest ETA ≥30 min from submission.

## Context

- EXT16 = 14/18 ACCEPT (Grok 9th consecutive 6/6 · Gemini 6/6 ACCEPT with pattern-058 · P1B+P4 3/3 ACCEPT frozen)
- EXT16-closure: 4 papers bumped (P1A v1A.0.77 · P2 v1.7.68 · P3 v3.1.111 · P5 v0.1.80)
- Pattern-060 first catch: V\mbox{-}Web at P5 l.2864 — \mbox{} escape form missed by pattern-059 grep
- P1B v1B.0.72 + P4 v1.0.188: FROZEN at universal 3/3 ACCEPT (3 and 4 consecutive rounds respectively)
- Target: 18/18 ACCEPT → arXiv coordinated drop

## PDF Versions Submitted (EXT17)

| Paper | Version | PDF MD5 (prefix 8) | Pages | Status |
|-------|---------|---------------------|-------|--------|
| P1A | v1A.0.77 | `f1eab008` | 29 | active |
| P1B | v1B.0.72 | `5a3c98e9` | 21 | FROZEN |
| P2  | v1.7.68  | `5a8a1af4` | 29 | active |
| P3  | v3.1.111 | `4a8c1172` | 30 | active |
| P4  | v1.0.188 | `c47abc18` | 23 | FROZEN |
| P5  | v0.1.80-2026-06-13 | `7bb73989` | 32 | active |

All md5s verified against source PDFs before submission (gate passes).

## Per-Paper EXT17 Closure Summaries (submitted to each chat)

### P1A (active, v1A.0.77)
EXT16 closure: Sec XII.A 'C/P-violating thermal scattering' propagation chain now explicit — chirality-flipping and depolarizing thermal interactions named (missed step from EXT15 Sec II.C.1 fix). No new analysis introduced. v1A.0.77 (md5 f1eab008).

### P1B (FROZEN, v1B.0.72 — courtesy re-confirmation)
**No changes since EXT14 — please confirm ACCEPT verdict still holds.** FROZEN at v1B.0.72 — universal 3/3 ACCEPT confirmed EXT14+EXT16 (ChatGPT+Grok+Gemini, 3 consecutive rounds).

### P2 (active, v1.7.68)
EXT16 closure: CDF-tail direction corrected in Sec VI.C summary paragraph — 'reduces' → 'raises' (for narrow delta-prior B, the CDF-tail from 5.69 to 7.0 is upward, raising evidence for the bounce). Sign typo fixed. v1.7.68 (md5 5a8a1af4).

### P3 (active, v3.1.111)
EXT16 closure: Table IX tablenote(a) clarified with row-specific prior density 1/Δγ denominator and explicit reweighting note for non-fiducial γ rows — computation chain per-row is now explicit. v3.1.111 (md5 4a8c1172).

### P4 (FROZEN, v1.0.188 — courtesy re-confirmation)
**No changes since EXT14 — please confirm ACCEPT verdict still holds.** FROZEN at v1.0.188 — universal 3/3 ACCEPT (first-ever ChatGPT ACCEPT in campaign confirmed EXT12+EXT14+EXT16; 4 consecutive rounds).

### P5 (active, v0.1.80-2026-06-13)
EXT16 closure: 3 text fixes — (1) math `V\mbox{-}Web` at l.2864 corrected to `T\mbox{-}Web` (pattern-060: the \mbox{} hyphen-escape form was missed by the pattern-059 grep sweep — new union regex now covers all four escape forms); (2) nomenclature note direction corrected; (3) duplicate T-Web phrase at l.1117 removed. v0.1.80 (md5 7bb73989).

## Submission Protocol

### ChatGPT (6 in-thread delta — same EXT16 thread URLs)
- P1A, P1B, P2, P3, P4, P5: in-thread delta prompts on EXT16 threads
- P1B, P4: courtesy re-confirmation prompt: "No changes since EXT14 — please confirm ACCEPT verdict still holds."
- Gemini pattern-058 first-line NOT required for ChatGPT

### Grok (6 in-thread delta — same EXT16 thread URLs)
- P1A, P1B, P2, P3, P4, P5: in-thread delta prompts on EXT16 threads
- P1B, P4: courtesy re-confirmation prompt: "No changes since EXT14 — please confirm ACCEPT verdict still holds."
- Gemini pattern-058 first-line NOT required for Grok

### Gemini (6 FRESH chats — pattern-058 first-line REQUIRED)
Pattern-058 MNRAS referee-format first-line (verbatim, every chat):

> "You are a professional scientific referee for Monthly Notices of the Royal Astronomical Society (MNRAS). Please review the attached PDF and provide a formal referee report with a clear verdict: ACCEPT, MINOR REVISIONS, MAJOR REVISIONS, or REJECT. Be direct about which category this paper falls into."

- 6 fresh Gemini chats (one per paper) with the above first-line
- Upload current PDF for each paper
- P1B, P4: include courtesy re-confirmation context ("No changes since EXT14")

## Versioned PDF locations (site/public/papers/)

All canonical versioned PDFs verified at site/public/papers/:
- paper1a_ech_nogo_v1A.0.77.pdf (already in site/public/papers/ from EXT16-closure tex bumps)
- paper1b_mcmc_companion_v1B.0.72.pdf
- paper2_fnl_forecast_v1.7.68.pdf
- paper3_anomaly_catalog_v3.1.111.pdf
- chirality_catalog_paper_v1.0.188.pdf
- p5_desi_chirality_v0.1.80-2026-06-13.pdf

## Tarball manifest (EXT17-closure versions ready)

| Paper | Tarball | MD5 |
|-------|---------|-----|
| P1A | paper1a_arxiv_v1A.0.77.tar.gz | d051803c |
| P1B | paper1b_arxiv_v1B.0.72.tar.gz | (existing) |
| P2  | paper2_arxiv_v1.7.68.tar.gz | 8d8b4da2 |
| P3  | paper3_arxiv_v3.1.111.tar.gz | 2aa35ec5 |
| P4  | paper4_arxiv_v1.0.188.tar.gz | (existing) |
| P5  | paper5_arxiv_v0.1.80-2026-06-13.tar.gz | 4d27ac49 |
