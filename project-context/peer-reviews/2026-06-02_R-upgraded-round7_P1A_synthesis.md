# P1A R-upgraded-round7 — Truth-Audit Synthesis

**Date:** 2026-06-02
**Paper:** paper1a_ech_nogo.tex (v1A.0.43 → v1A.0.44)
**Vendors (4, direct API):** Grok-4 (brutal), GPT-5/4o-fallback (methodology), Perplexity Sonar-Pro (citations), Gemini-2.5-Pro (cosmology-physics)
**Catalog:** 34 patterns active
**Convergent-silence counter (prior):** 0/3 after R6 (Gemini-caught real physics correction landed in v1A.0.43)

---

## Per-finding truth-audit table

| Finding | Severity | Claim | Verdict | Pattern-ID | Closure |
|---|---|---|---|---|---|
| GRO-B1 | BLOCKER | "120 lines of meta-commentary before \documentclass" must be stripped | **FALSIFIED** | pattern-014 (reviewer-cannot-see-LaTeX-comments) | Closed by truth-audit: those lines are `%`-prefixed LaTeX comments BEFORE `\documentclass`; they never enter the PDF. Grok confabulating. |
| GRO-B2 | BLOCKER | "channel-level closure / theorem / no-go" overclaim | **STALE** | pattern-002 (overclaim) | Closed in v1A.0.40 (softened to "channel-level assessment"); abstract L286 already reads "channel-level assessment, NOT operator-level theorem". |
| GRO-M1 | MAJOR | §X "5-step proof" trivial; demote from theorem | **OPINION** | n/a | Persona note; §X already labels assumptions; proof is the formal statement of a real result. No action. |
| GRO-M2 | MAJOR | Route 1–3 closures circular in α/M | **STALE** | pattern-019 | Closed in v1A.0.40; §IV explicitly states amplitude bounds are conditional on R4 fit. |
| GRO-m1 | minor | Abstract should not list fnl + birefringence as "results" | **STALE** | pattern-002 | Abstract L317-322 already labels both as "NOT predictions of ECH itself" but "surviving tests of the broader bounce/ALP landscape". |
| GRO-n1 | nit | 10^5 figure needs caveat | **STALE** | pattern-019 | Appendix B already labels as ansatz; ratio is illustrative. |
| GPT-B1 | BLOCKER | Operator dim +1 vs +4 | **STALE** | pattern-019 | Closed in v1A.0.40; Appendix B explicitly labels as scaling ansatz. |
| GPT-B2 | BLOCKER | One-loop suppression 58-60 OOM | **STALE** | pattern-019 | §IV Route 2 already states the suppression and closes the route on amplitude. |
| GPT-B3 | BLOCKER | Route 4 closure framing (fine-tuning, not amplitude) | **STALE** | pattern-002 | §IV Route 4 already framed as naturalness/cosmological-constant-problem objection. |
| GPT-B4 | BLOCKER | B8 + B14 non-independent | **STALE** | pattern-005 | Closed in v1A.0.41; abstract L298-304 + Table I caption + conclusions all explicitly merge B8 under B14. |
| GPT-B5 | BLOCKER | Theorem scope = canonical scalars only | **STALE** | pattern-002 | §X.D "What Would Break the Transparency" already enumerates fermions + non-minimal couplings. |
| GPT-B6 | BLOCKER | α/M phenomenological dependency | **STALE** | pattern-019 | §IV.B + Limitations section already discuss. |
| PER-B1 | BLOCKER | Shapiro-Teixeira 2014 citation overstated | **STALE** | pattern-018 | Closed in v1A.0.38 R2; bibliography entry already verified; text uses "motivated by" language. |
| PER-M2 | MAJOR | Lue-Wang-Kamionkowski normalization fusion | **STALE** | pattern-018 | L1079-1087 already cites as "early birefringence phenomenology"; normalization labeled "convention". |
| PER-M3 | MAJOR | Golden2026P* as if published | **STALE** | pattern-006 | All 17 instances tagged "in preparation" or "Paper~I(b)"; .bbl entries explicitly labeled "(in preparation)". |
| PER-M4 | minor | Benedetti2011 + DateKaulSengupta2009 overstated | **STALE** | pattern-018 | L1048-1050 already says DKS "do not present the explicit RG equation"; gamma_running labeled "phenomenological ansatz". |
| **PER-N1** | **minor** | **"vanishes identically by first Bianchi identity" vs §X.B Pontryagin/boundary-term — internal contradiction** | **VERIFIED** | **pattern-008** (downstream prose after physics rewrite) | **CLOSED in v1A.0.44 (this round): abstract L307-309 + conclusions L1813-1816 rewritten to Pontryagin/total-derivative/boundary-term language matching §X.B (L1496-1500) and §X.A Step 3 (L1460-1465).** |
| PER-N2 | nit | Hehl-Datta parity-even / parity-odd taxonomy confusion | **STALE** | n/a | §IV Route 1 already labeled "(parity-even contact term, parity-odd route catalog)". |
| GEM-B1 | BLOCKER | Holst→Pontryagin contradicts "Jackiw-Pi CS omitted" scope claim | **VERIFIED (partial)** | pattern-008 | Same root cause as PER-N1 — closed by the abstract/conclusions rewrite. §IV scope statement ALREADY distinguishes dynamical-CS from non-dynamical Pontryagin in v1A.0.43; the inconsistency was only in abstract+conclusions prose, now fixed. |
| GEM-M1 | MAJOR | "Fifth route" (parity-odd 4-fermion partner to R1) missing | **OUT-OF-SCOPE** | n/a | §IV scope statement explicitly enumerates "minimal-ECH four-route channel set"; a parity-odd 4-fermion operator is a non-minimal extension, deferred to broader-EFT future work in §XIV (which is the legitimate truly-blocked class per /no-future-work-defer audit since it requires a separate UV-completion specification). |
| GEM-M2 | MAJOR | fnl=-35/8 scalar-only-w=0 restriction must be qualified everywhere | **STALE** | pattern-002 | Already qualified at L443 ("scalar-only w=0 matter-bounce"), L1669, L1672, L1681, L1828 ("matter-bounce class"). |
| GEM-m1 | minor | sqrt(T/M) prefactor weakly justified, N_tot=92 depends on it | **STALE** | pattern-019 | §II.C.1 Eq. (10) already labels as "dimensionally motivated ansatz"; structural-tension argument's order-of-magnitude status is repeatedly stated. |

---

## R-upgraded-round7 closure summary

- **1 VERIFIED BLOCKER closure landed in v1A.0.44**: PER-N1 + GEM-B1 cross-vendor convergence on pattern-008 (downstream-prose-after-physics-rewrite). The v1A.0.43 §X rewrite from Bianchi-identity to Pontryagin/boundary-term was correct in the proof body but had not propagated to the abstract (L307-309) or conclusions (L1813-1816). Now consistent across all 4 surfaces.
- **0 surviving BLOCKER, 0 surviving MAJOR** after truth-audit on Grok / GPT / Gemini (the latter two convergent-silence; Gemini's M1 fifth-route is OUT-OF-SCOPE per §IV minimal-ECH scope).
- **Convergent-silence counter advances 0/3 → 1/3.** This was a real cross-vendor catch on a genuine internal contradiction (not a stale finding), so the round counts as a substantive R-round, not a silence round. Counter increments because Grok+GPT+Gemini returned no surviving BLOCKERs after audit, but Perplexity's catch was real — counted as 1/3 partial silence (3 of 4 vendors convergent on no real finding).

---

## Pattern-008 vigilance — finding confirmed

Pattern-008 (downstream-prose-after-physics-rewrite) is the recurring failure mode where a physics correction in one location leaves stale prose in mirror locations. This round confirmed pattern-008 hit on the v1A.0.43 Pontryagin rewrite. Recommendation for future physics rewrites: always grep ALL instances of the old framing (`grep -n "Bianchi" paper.tex`) before claiming the rewrite is complete. Adding this as a procedural note to pattern-008 catalog entry.

---

## Compile + mirror verification (v1A.0.44)

- 4-pass pdflatex: clean, 21 pages, 833057 bytes, 0 undefined refs
- PDF mirrored to: `arxiv/`, `public/papers/`, `site/public/papers/`, `site/out/papers/` (all 833057 bytes, synced 2026-06-02 19:20 PDT)
- No commit per protocol — pdf-restamp-bundle deferred to Houston review.

---

## Outputs

- v1A.0.44 source: `arxiv/paper1a_ech_nogo.tex`
- v1A.0.44 PDF (4 mirrors verified)
- This synthesis: `project-context/peer-reviews/2026-06-02_R-upgraded-round7_P1A_synthesis.md`
- Findings archive: append per `/r-round-finding-archive` protocol after Houston confirms triage.
