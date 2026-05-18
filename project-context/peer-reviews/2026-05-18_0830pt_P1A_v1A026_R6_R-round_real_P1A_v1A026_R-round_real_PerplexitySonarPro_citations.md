# P1A_v1A026 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_0830pt_P1A_v1A026_R6_R-round_real
**Wall time**: 10.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=27799, completion=726, total=28525

---

## PAPER-PER-B1

**BLOCKER** — The bibliography is not auditable from the provided text, and several cited works are internally suspect or fused with unsupported claims. For example, the paper cites `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, and `Golden2026P4` as if already real companion papers, but no verifiable metadata is provided here; that makes the citation chain incomplete at the source level. **Fix:** add a complete reference list with real titles, venues, arXiv IDs/DOIs, and ensure every in-text companion citation resolves to an actual accessible record.

## PAPER-PER-B2

**BLOCKER** — The paper’s claimed one-loop and birefringence citations are likely metadata-fused or at least not source-clean. The text attributes route-2 parity-odd one-loop results to `Mercuri2009` and `MercuriCapozziello2008`, but the paper’s own derivation later admits the relevant amplitude comparison had dimensional inconsistencies and multiple incompatible orderings, which is a strong sign the cited papers do not actually support the stated quantitative closure. **Fix:** isolate each cited result, quote the exact equation or statement it supports, and remove any claim that is not directly traceable to the cited source.

## PAPER-PER-M1

**MAJOR** — The paper repeatedly treats the ECH Holst sector as perturbation-transparent for canonical scalar matter, then extends that to amplitude-level no-go claims about dark energy. That is a scope jump: “no scalar/tensor perturbation effect” does not by itself imply “no dark-energy route,” especially when the paper itself admits phenomenological ansätze and on-shell scaling are doing the heavy lifting. **Fix:** separate the strict perturbation result from the dark-energy no-go and state the latter as conditional on the added scaling ansatz, not as a theorem.

## PAPER-PER-M2

**MAJOR** — Route 4 is not consistently closed. The paper explicitly says the spectator-ALP route is **not** closed by amplitude mismatch and can match both birefringence and dark energy if \(\alpha/M\) is floated; that means the “closure” is only under a rigidity assumption, not intrinsic to the model. **Fix:** state the assumption up front and downgrade the conclusion to “conditional no-go under fixed one-loop matching,” otherwise the route remains open.

## PAPER-PER-m1

**minor** — The paper’s own internal counting is unstable: it alternates between 14 barriers, 13 logically independent barriers, and B8 subsumed by B14. That is not wrong if clearly labeled, but the naming is noisy and risks misleading readers about the actual number of independent constraints. **Fix:** use one consistent count everywhere and define “historical catalog entries” versus “logically independent barriers” once, in one place.

## PAPER-PER-n1

**nit** — The manuscript is over-assertive in places where it should be explicit about provenance, especially for numerical claims like \(N_{\rm tot}\approx 92\), \(\beta\approx 0.27^\circ\), and \(\fnl=-35/8\). These are not all derived within this paper, and several are imported from companion or class-level analyses. **Fix:** tag every externally inherited number as “from companion paper” or “class-level input” at first use.
